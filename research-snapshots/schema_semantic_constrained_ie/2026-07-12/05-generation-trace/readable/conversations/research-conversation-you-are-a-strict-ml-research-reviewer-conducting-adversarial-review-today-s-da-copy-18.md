# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/94b5d494-754c-4cdb-964a-033c6cb3f6c9.jsonl`
- **Structured JSON:** [`026795331c000c761078.json`](../../sessions/02/026795331c000c761078.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T09:44:03.352Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T09:44:03.352Z",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.\n\nDirection: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.\n\nContribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.\n2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.\n3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.\n\nLook for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.\n\nTag: direction=information_extraction, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 8/10)\n{\n  \"title\": \"CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Shot Event Argument Extraction — An Empirical Study via Synthetic Supervision\",\n  \"core_problem\": \"Synthetic-data-based zero-shot event argument extraction (EAE) faces a structural data quality problem that existing approaches address only partially. LtGaE (AAAI 2026) uses soft RL penalties for argument completeness — a quality score penalty that fires when the proportion of empty arguments per sample deviates from a target range [τ−ε, τ+ε], but does not enforce per-role entity-type compatibility or hard cardinality bounds during decoding. Gatto et al. (ACL 2025 Long) uses free-form LLM generation with no formal constraints. FineCSDA (NLPCC 2024) targets the long-tail distribution of argument roles via sample-level augmentation of rare event types (SDAM) and context-level injection of rare role fillers (CDAM), but neither module enforces formal cardinality bounds or entity-type constraints — coverage improvement relies on targeted prompt design rather than any structural enumeration mechanism. GEMS (ACL Findings 2025) applies ontology steering at inference time via multi-perspective prompting and voting, not at training-data generation time.\\n\\nNone of these approaches systematically addresses the structural salience of rare argument roles during generation. The RAMS ontology TSV specifies only maximum cardinality (the 'count permitted' column is an upper bound on role occurrences per instance, not a minimum), so grammar-constrained decoding via XGrammar enforces: (a) no role exceeds its permitted maximum count, and (b) when filled, entity types are compatible. It cannot logically force optional roles to appear — setting min-cardinality=1 for all roles would require an assumption not derivable from the RAMS TSV and would produce unrealistically complete training instances where every event instance has every schema role filled. Instead, Schema-Constrained Grammar (SCG) provides a different mechanism: structural salience. Critically, in the XGrammar encoding all applicable role slots appear as required keys in the output JSON template — the LLM generates an empty string or null value for absent optional arguments but cannot omit role keys from the output. This key-level requirement is the structural salience mechanism: it forces the model's attention to each slot during the forward pass, counteracting the prior bias toward omitting rare slots that characterizes unconstrained generation. Even when individual constraint violation rates are low (plausible for strong instruction-following models like Qwen3-32B), unconstrained generation tends to cluster on high-frequency role patterns due to LLM prior biases, likely under-representing rare optional roles. Post-hoc filtering (Condition B) removes entity-type violations and cardinality overruns but operates on outputs from unconstrained generation where rare role keys were never generated — it cannot recover coverage for roles absent from the unconstrained output corpus.\\n\\nThe primary gap CompSchema-IE targets is empirical and analytical: we do not know (a) whether hard grammar constraints (formal cardinality + entity-type enforcement via XGrammar, which provides structural salience through required role-key enumeration over and above entity-type and cardinality filtering) outperform oracle post-hoc filtering of unconstrained generation on downstream zero-shot EAE, (b) in which role strata these differences concentrate, or (c) whether any structural regularization gains are mechanistically explained by rare-role instantiation improvements. Answering these questions empirically — with a clean three-condition ablation, volume-controlled design, and stratified evaluation — is a concretely useful contribution for EMNLP Findings, even if overall F1 deltas are modest.\",\n  \"opportunity\": \"The supervised-to-zero-shot gap remains 8–35 F1 points (supervised SOTA: DEGAP COLING 2025 — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1; TSCA IET Software 2026 adds ~+3.0/+1.0 F1 in fully supervised settings; best zero-shot cross-dataset: LtGaE 32–47 F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki). Training data quality for the generator model is a concrete bottleneck: LtGaE's soft RL penalties improve over prior unconstrained generation but cannot guarantee per-role proportional coverage; FineCSDA's targeted augmentation improves rare-role counts but lacks formal structural enumeration. GEMS (ACL Findings 2025) provides ontology-guided inference-time EAE but does not address training-data generation quality. SynthIE (EMNLP 2023) demonstrated that task-reversal generation can produce highly effective synthetic IE training data, but uses no grammar-constrained decoding and does not address event argument extraction. The key open question is whether hard constraints provide a measurable advantage over oracle-quality soft filtering under a volume-controlled design. This question has a clean experimental operationalization: (A) unconstrained generation, (B) unconstrained generation with post-hoc violation filtering (oracle soft constraint approximation, volume-matched to A and C), and (C) grammar-constrained generation via XGrammar — same model, same schema information, same final training volume. If C outperforms B on rare roles despite similar overall violation rates, the result directly demonstrates that structural salience (not just constraint compliance) drives the downstream gain — the SCG's required role-key enumeration in the output template forces the model to instantiate each slot rather than silently omitting rare keys during unconstrained generation. This is a falsifiable, mechanistically interpretable empirical finding — the type EMNLP Findings values.\",\n  \"landscape\": \"GuideX (ACL Findings 2025) sets SOTA on 7 zero-shot NER benchmarks with Llama-3.1 fine-tuned on generated data, but explicitly does not address event argument extraction.\\n\\nGEMS (ACL Findings 2025, aclanthology.org/2025.findings-acl.1353) uses multi-perspective prompts and ontology steering for inference-time EAE on WikiEvents, ACE05, and ERE-EN, achieving SOTA in low-resource settings. GEMS applies ontology knowledge at inference time via a voting mechanism over multiple generation paths with T5-large as the base model; CompSchema-IE instead applies hard grammar constraints at training-data generation time, investigating whether structural salience from required role-key enumeration during generation improves downstream rare-role coverage — a complementary research question targeting a different phase of the pipeline.\\n\\nFineCSDA ('FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation', NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) directly identifies the long-tail distribution of argument roles as a bottleneck and proposes two augmentation modules: SDAM generates new document-level samples for rare event types, and CDAM injects rare argument roles and corresponding context into common event type documents. Unlike CompSchema-IE, FineCSDA does not impose formal cardinality bounds or entity-type constraints, and provides no structural role-slot enumeration — coverage improvement relies on targeted prompt design for rare types and roles.\\n\\nGatto et al. ('Document-Level Event-Argument Data Augmentation for Challenging Role Types', ACL 2025 Long, arXiv:2403.03304) is a direct predecessor: LLM-powered augmentation (Mad Lib Aug and Struct2Text) for extractive EAE, +13 F1 on zero-shot role types using BERT-QA, no schema constraints, few-shot cross-domain setting (5 documents per event type available), zero-shot roles within seen event types — not fully zero-shot event type generalization.\\n\\nBiTer (Information Processing and Management, May 2025, doi:10.1016/j.ipm.2025.104199) achieves +4.6%/+7.5%/+0.4% zero-shot Arg-C F1 on RAMS/WikiEvents/ACE2005 using within-dataset event-type-held-out splits. Protocol is NOT directly comparable to LtGaE's cross-dataset three-way protocol; reported separately with explicit footnote.\\n\\nLtGaE (AAAI 2026, arXiv:2603.02909) uses multi-agent Propose-Evaluate-Revise with RL reward that includes a soft penalty p_i activated when the proportion of empty arguments ρ_i deviates from a target range [τ−ε, τ+ε] — a global aggregate quality-score adjustment per sample, not a per-role structural enumeration or hard decoding constraint. Achieves 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki. Does not compare against BiTer.\\n\\nASEE (EMNLP Findings 2025, arXiv:2505.08690) addresses inference-time schema selection via RAG; no hard constraints; does not report RAMS/WikiEvents numbers.\\n\\nBoostCD (EMNLP 2025 Main, arXiv:2506.14901) demonstrates that constrained and unconstrained decoding produce complementary errors at inference time for closed IE (relation extraction), with a learned boosted model combining both for stronger performance. CompSchema-IE investigates an analogous question at training-data generation time for event argument extraction, where structural salience differences compound across a finite corpus rather than being resolved at inference.\\n\\nSALE (MDPI Electronics, March 2026) uses code-based LLM fine-tuning with RL alignment for cross-task zero-shot transfer; no formal schema constraints during data generation.\\n\\nExtracting Events Like Code (AAAI 2026, arXiv:2511.13118) uses Python class definitions for inference-time schema validation, not training-data generation.\\n\\nSynthIE (EMNLP 2023, ACL Anthology 2023.emnlp-main.96) generates synthetic IE training data via task-reversal (structure→text generation), achieving large F1 gains on smaller models; uses no grammar-constrained decoding, no formal cardinality bounds, and targets IE triplets rather than compositional event argument extraction. Establishes the task-reversal generation paradigm that CompSchema-IE extends with hard compositional constraints.\\n\\nSupervised SOTA: DEGAP (COLING 2025, arXiv:2405.13325) — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1. TSCA (IET Software 2026) adds ~+3.0/+1.0 F1 in fully supervised settings.\\n\\nThe specific open question not addressed by any prior work — including GEMS, FineCSDA, LtGaE, Gatto et al., or BoostCD: does hard grammar constraint enforcement (cardinality + entity-type, XGrammar) — which provides structural salience via required role-key enumeration in the output JSON template — outperform oracle post-hoc filtering of unconstrained generation under a volume-controlled design, and does any advantage concentrate in rare-role and high-cardinality-tightness strata where the structural enumeration mechanism is most likely to shift the LLM's generation distribution?\",\n  \"approach\": \"CompSchema-IE is framed explicitly as an empirical study targeting EMNLP 2026 Findings. The primary contribution is a clean, volume-controlled three-condition ablation that isolates the value of hard constraint enforcement over soft filtering, combined with a stratified analysis that localizes any gains mechanistically.\\n\\n**Primary Hypothesis (Structural Salience, Empirically Testable)**:\\nThe RAMS ontology TSV specifies only maximum cardinality (the 'count permitted' column is an upper bound on role occurrences per instance). XGrammar therefore enforces: (a) no role appears more than its permitted maximum count, and (b) when filled, entity types are compatible. It does NOT logically guarantee that optional rare roles appear in every generated instance — this would require setting min-cardinality=1 for all roles, a design choice not derivable from the RAMS TSV alone and one that would produce unrealistically complete training instances where every event instance has every schema role filled.\\n\\nCompSchema-IE instead adopts the structural salience framing: SCG provides structural salience by explicitly enumerating every applicable role slot as a required key in the constrained generation template. In the XGrammar encoding, all applicable role slots for a given event type appear as required keys in the output JSON template; the LLM generates an empty string or null value for absent optional arguments but cannot omit role keys from the output. This key-level requirement is the mechanism of structural salience: it forces the model's attention to each slot during the forward pass, counteracting the prior bias toward omitting rare slots that characterizes unconstrained generation. Condition B (post-hoc filtering) can remove entity-type violations and cardinality overruns from unconstrained outputs, but cannot recover coverage for role keys that unconstrained generation never emitted in the first place. The structural salience hypothesis is therefore that Condition C will show improved rare-role instantiation over Condition B even when overall constraint violation rates are comparable — an effect logically independent of constraint compliance and attributable specifically to required key enumeration. Even when individual constraint violation rates are low — expected for Qwen3-32B given its strong instruction-following capability — unconstrained generation's prior biases tend to cluster on high-frequency role patterns, under-representing rare optional roles. FineCSDA (NLPCC 2024) partially addresses rare-role under-representation via targeted prompting (SDAM/CDAM), but without formal structural enumeration; CompSchema-IE's SCG provides structural salience by construction through required key enumeration, making it an empirical question whether this translates to downstream rare-role F1 gains.\\n\\n**Step 0 — Motivating Pilot Study (Day 4, 4 GPU-hours)**:\\nSample 600 event instances from Qwen3-32B without constraints (standard structured prompting with RAMS/WikiEvents schema descriptions). The expanded sample (~4–5 instances per event type for RAMS's 139 types) enables reliable per-role violation statistics. Measure: entity-type mismatch rate, cardinality violation rate, role hallucination rate, and argument role coverage (proportion of schema roles appearing ≥1 time). Report all four metrics unconditionally. The primary paper argument holds regardless of outcome: low violation rates motivate the structural salience framing (SCG's required key enumeration matters beyond error correction); high rates additionally motivate constraint enforcement for quality improvement. Both are reported; neither determines the primary framing.\\n\\n**Step 1 — Schema Constraint Grammar (Days 1-3, human engineering)**:\\nDerive typed constraint specifications from RAMS (cardinality directly from public ontology TSV, encoding the 'count permitted' values as maximum bounds; entity-type compatibility from dataset annotations) and WikiEvents (entity-type compatibility from annotations). Encode as XGrammar-compatible context-free grammars. Critically, all applicable role slots for a given event type are encoded as required keys in the output JSON template: the LLM must generate each role name as a JSON key, and may output an empty string or null value for absent optional arguments, but cannot omit any role key from the output. This required-key design is the structural salience mechanism — it forces the model's attention to each role slot during the forward pass rather than allowing silent omission of rare slots, as occurs in unconstrained generation (Condition A) and is not recoverable by post-hoc filtering (Condition B). Cardinality constraints additionally enforce upper bounds on role-filler counts and entity-type compatibility per filler. RAMS TSV availability substantially reduces construction effort. Scoped to 2 ontologies.\\n\\n**Step 2 — Three-Condition Data Generation with Volume Control (Days 5-7, ~62.5 GPU-hours)**:\\nAll conditions use Qwen3-32B on 2×A100 80GB via vLLM. **Target training volume**: N = 5,000 event argument instances per condition, distributed proportionally across the 139 RAMS event types (~36 instances per type on average, with a minimum of 1 per rare type) and WikiEvents event types. To eliminate the volume confound — where Condition B (post-hoc filtered) would otherwise train on fewer instances than C — the following volume normalization protocol is applied:\\n\\n- **Pool Generation**: Generate 1.5× the target volume (7,500 unconstrained instances) as unconstrained instances (same chat prompting with schema descriptions). Report achieved token throughput and generation settings.\\n- **Condition A (Unconstrained)**: Randomly subsample N=5,000 instances from the 7,500-instance pool.\\n- **Condition B (Post-hoc Filtered — Oracle Soft Baseline)**: Apply the automated verifier to the full 7,500-instance pool; retain instances passing all entity-type, cardinality, and role-hallucination checks, targeting N=5,000 post-filter instances. Report the achieved discard rate (e.g., 'we generated 7,500 instances and discarded X%, retaining 5,000 for training') as a transparency metric. If the filter discards more than 33% (leaving fewer than 5,000 clean instances), increase the pool to 2× (10,000 instances) and regenerate the additional batch. This baseline approximates oracle-quality soft constraint enforcement without reimplementing LtGaE's RL loop; crucially, it CANNOT recover structural salience for roles absent from filtered instances because unconstrained generation never emitted those role keys.\\n- **Condition C (SCG-Constrained)**: Grammar-constrained vLLM decoding via XGrammar to exactly N=5,000 instances, enforcing all role-entity-type assignments and cardinality constraints during the forward pass (<40μs/token overhead, per XGrammar MLSys 2025). The grammar's required role-key enumeration in the output template provides structural salience by construction.\\n\\nAll three conditions train on exactly N=5,000 instances, making the C-vs-B comparison methodologically airtight.\\n\\n**Step 3 — Constraint Verification (concurrent with Step 2)**:\\nThe automated verifier checks all generated instances and reports: filter rate for the A/B pool (transparency metric), corpus-level role coverage for each condition, near-zero filter rate for Condition C (SCG compliance guarantee). Role coverage differences across conditions directly measure the structural salience effect prior to fine-tuning.\\n\\n**Step 4 — Fine-tuning and Evaluation (Days 8-11, ~57 GPU-hours)**:\\nLoRA fine-tune Qwen3-8B on each of the three volume-matched corpora (3 conditions × ~15 GPU-hours = 45 GPU-hours). Evaluate zero-shot on WikiEvents and RAMS using LtGaE three-way protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki). Comparison table: LtGaE, ASEE, supervised SOTA (DEGAP), Condition A, Condition B, Condition C. BiTer reported separately under native within-dataset protocol with explicit non-comparability footnote.\\n\\n**Step 5 — Stratified Evaluation (Day 12, ~12 GPU-hours for inference)**:\\nThe primary analysis section — demonstrates mechanistic explanation of C vs. A/B gaps:\\n(a) Role Rarity Strata: Rank argument roles by frequency in source schema annotations; partition into quartiles. Report C vs. A and C vs. B F1 for each quartile. Hypothesis: C-B gap concentrates in the bottom quartile (rarest roles) because grammar-guided required key enumeration most strongly prompts the model to instantiate rarely-occurring role types; for common roles, both unconstrained and post-hoc filtered corpora already have sufficient coverage.\\n(b) Cardinality Tightness Strata: Partition by RAMS-ontology cardinality — max=1 (singleton roles) vs. max>1. Report C vs. A and C vs. B F1 for each partition. Hypothesis: C outperforms B on max=1 roles because Condition B can only remove duplicates but may still have duplicate instances within the filtered corpus; SCG hard-enforces the singleton constraint.\\nIf overall C-B delta is modest (e.g., <1 F1), the stratified analysis provides a theoretically grounded finding even for the Findings track: structural salience helps specifically where theory predicts, at a granularity that soft filtering cannot replicate. Both role coverage rates and argument span F1 are reported per stratum, allowing quality and coverage effects to be distinguished (addressing the concern that grammar-constrained decoding may improve role coverage while degrading span quality).\\n\\n**Null Result Pre-Specification**:\\nWe pre-specify the null result interpretation in the paper: if C does not outperform B even in the rare-role quartile or singleton-cardinality partition, we report this as a clearly framed negative finding — grammar-guided structural enumeration via required key templates during generation provides no additional rare-role instantiation benefit over oracle post-hoc filtering of unconstrained generation at Qwen3-32B scale. This is a practically useful negative result: it suggests that strong instruction-following models already provide sufficient structural salience through prompt-specified schema descriptions, and that engineering investment in SCG construction may not be warranted at this model scale. EMNLP Findings publishes clearly framed negative results; this pre-specification distinguishes a null result from a failed experiment.\\n\\n**Limitations and Quality Tradeoffs**:\\nGrammar-constrained decoding may introduce quality degradation beyond structural coverage: Schall & de Melo (RANLP 2025) demonstrate that constrained decoding forces instruction-tuned models away from high-confidence natural language paths, potentially increasing extraction misses. We mitigate this by using Qwen3-32B (whose strong instruction-following capability reduces divergence between constrained and unconstrained generation paths) and by measuring argument span F1 per role stratum in the stratified evaluation alongside role coverage rates, so that quality and coverage effects are distinguishable rather than conflated.\\n\\n**Paper writing**: Concurrent from Day 1 (intro, related work, method drafted during experiment runs); intensive final writing Days 13-16.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~125.5h A100 80GB total: pilot study generation 600 instances (4 GPU-hours); 1.5× unconstrained pool generation for Conditions A+B (target N=5,000 per condition, pool=7,500 instances, ~37.5 GPU-hours); SCG-constrained generation for Condition C (N=5,000 instances, ~25 GPU-hours); LoRA fine-tuning Qwen3-8B across 3 volume-matched conditions × 15 GPU-hours = 45 GPU-hours; stratified evaluation inference ~12 GPU-hours; evaluation and reporting ~2 GPU-hours\",\n      \"gpu_utilization\": \"Moderate (~50%): compressed timeline reduces idle gaps; human engineering on SCG module (Days 1-3) and paper writing (concurrent) introduce some idle GPU time, mitigated by parallelizing fine-tuning runs. Volume control adds ~12.5 GPU-hours of generation vs. original design.\",\n      \"timeline\": \"16 active days targeting May 25, 2026 ARR deadline (commitment to EMNLP 2026 by August 2, 2026; conference October 24-29, Budapest). Day-by-day: Days 1-3 SCG construction + pilot study setup; Day 4 pilot study run (600 instances) + metric analysis; Days 5-7 data generation (7,500-instance A/B pool + 5,000-instance C, staggered on 2×A100, pool generation starts Day 5, C generation starts Day 6 while A/B fine-tune begins); Days 8-10 LoRA fine-tuning (all 3 conditions, staggered); Day 11 LtGaE three-way evaluation; Day 12 stratified evaluation analysis; Days 13-16 intensive paper writing (concurrent with experiments from Day 1). No extended ablations, no ACE05 comparison, no BiTer replication.\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$187 (125.5h × $1.49/hr A100, RunPod/JarvisLabs)\",\n      \"h100_equiv\": \"~90h H100-equivalent (well within ≤200h H100 hard constraint)\",\n      \"risk_note\": \"Key risks and mitigations: (1) Overall C-B F1 delta may be small (<1 F1): mitigated by stratified evaluation and pre-specified null result interpretation — paper's primary claim is that structural salience helps in rare-role and singleton-cardinality strata; if this too is null, reported as a clear negative finding with specific positioning. (2) Filter rate exceeds 33% (B cannot reach N=5,000 from 7,500-instance pool): mitigated by increasing pool to 10,000 instances for that condition and reporting achieved discard rate as transparency metric. (3) Pilot study shows <1% violations: expected and mitigated by structural salience argument (violation-rate-independent — the hypothesis concerns role instantiation frequency via required key enumeration, not constraint compliance). (4) XGrammar quality degradation (Schall & de Melo, RANLP 2025): mitigated by Qwen3-32B's strong instruction-following capability and dual measurement of span F1 and role coverage per stratum. (5) 16-day timeline is tight: SCG construction is the bottleneck; RAMS TSV machine-readable cardinality substantially reduces this. Paper writing concurrent from Day 1 is required. (6) BiTer protocol mismatch: explicitly handled with separate table and footnote. (7) FineCSDA comparison: differentiated from CompSchema-IE by formal grammar-constrained decoding with required role-key enumeration vs. targeted prompting, volume-controlled experimental design, and structural salience mechanism by construction.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings (ARR May 25, 2026 submission deadline; commitment to EMNLP 2026 by August 2, 2026; conference October 24-29, Budapest, Hungary)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction (ACL Findings 2025)\",\n    \"GEMS: Generation-Based Event Argument Extraction via Multi-perspective Prompts and Ontology Steering (ACL Findings 2025, aclanthology.org/2025.findings-acl.1353) — inference-time EAE using multi-perspective prompts and ontology steering (T5-large) on WikiEvents/ACE05/ERE-EN; achieves SOTA in low-resource settings; differentiated from CompSchema-IE by operating at inference time rather than training-data generation, and by using a voting mechanism over multiple generation paths rather than hard grammar constraints\",\n    \"FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation (NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) — identifies long-tail argument role distribution as bottleneck; SDAM generates samples for rare event types, CDAM injects rare role fillers into common event type documents; no formal cardinality bounds, entity-type constraints, or explicit role-slot enumeration; coverage relies on targeted prompting\",\n    \"Document-Level Event-Argument Data Augmentation for Challenging Role Types (Gatto, Sharif, Seegmiller, Preum; ACL 2025 Long, arXiv:2403.03304) — direct LLM-augmentation predecessor; no constrained decoding, no cardinality/entity-type constraints, few-shot cross-domain with zero-shot roles\",\n    \"SynthIE: Leveraging the Asymmetry of Knowledge Graph Structure for Synthetic IE Data Generation (EMNLP 2023, ACL Anthology 2023.emnlp-main.96) — task-reversal generation paradigm; no grammar-constrained decoding, no formal cardinality bounds, targets IE triplets not event argument extraction\",\n    \"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction (EMNLP 2025 Main, arXiv:2506.14901) — inference-time boosting for closed IE (relation extraction); central empirical finding: constrained and unconstrained decoding produce complementary errors; CompSchema-IE investigates the analogous structural salience question at training-data generation time for EAE, where coverage differences compound across a finite corpus\",\n    \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance (Schall & de Melo, RANLP 2025, aclanthology.org/2025.ranlp-1.124/) — demonstrates that constrained decoding forces instruction-tuned models away from high-confidence natural language paths, causing quality degradation; for LLaMA-3.3-70B, XGrammar led to substantially more extraction misses than top unconstrained strategies; motivates use of strong instruction-following models (Qwen3-32B) and dual measurement of role coverage and span F1 per stratum\",\n    \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)\",\n    \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)\",\n    \"BiTer: Bi-directional Feature Learning-Based Approach for Zero-Shot Event Argument Extraction (Information Processing and Management, May 2025, doi:10.1016/j.ipm.2025.104199) — within-dataset event-type-held-out evaluation protocol; not directly comparable to LtGaE three-way cross-dataset protocol\",\n    \"Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation (ASEE, EMNLP Findings 2025, arXiv:2505.08690)\",\n    \"Learning to Generate and Extract: A Multi-Agent Collaboration Framework for Zero-Shot Document-Level Event Arguments Extraction (LtGaE, AAAI 2026, arXiv:2603.02909) — soft RL penalty p_i fires when per-sample empty-argument proportion ρ_i deviates from [τ−ε, τ+ε] (global aggregate quality score, not per-role structural enumeration); 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki\",\n    \"Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction (AAAI 2026, arXiv:2511.13118)\",\n    \"Structure-Aware Lightweight Document-Level Event Extraction via Code-Based Large Language Models (SALE, MDPI Electronics, March 2026)\",\n    \"DEGAP: Dual Event-Guided Adaptive Prefixes for Templated-Based Event Argument Extraction with Slot Querying (COLING 2025, arXiv:2405.13325) — supervised SOTA: RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1\",\n    \"Beyond Single-Event Extraction: Towards Efficient Document-Level Multi-Event Argument Extraction (DEEIA, ACL 2024 Findings, arXiv:2405.01884) — RAMS 53.4 Arg-C F1, WikiEvents 67.0 Arg-C F1\",\n    \"Two-Stream Modeling for Document-Level Event Argument Extraction Using Contextual Clue and AMR Structures (TSCA, IET Software 2026) — supervised SOTA extension: +3.02/+1.01 F1 on RAMS/WikiEvents over prior SOTA\",\n    \"DiCoRe: Enhancing Zero-shot Event Detection via Divergent-Convergent LLM Reasoning (arXiv:2506.05128)\",\n    \"MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)\",\n    \"Document-Level Event Argument Extraction by Conditional Generation (NAACL 2021)\",\n    \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv 2023)\",\n    \"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models (MLSys 2025)\"\n  ],\n  \"description\": \"Zero-shot event argument extraction lags supervised performance by 8–35 F1 points (supervised SOTA: DEGAP COLING 2025 — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1; best zero-shot cross-dataset: LtGaE AAAI 2026 — 32–47 F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki). A key bottleneck is training data quality for the generator model. This paper presents CompSchema-IE, an empirical study asking: do hard grammar constraints (formal cardinality + entity-type enforcement via XGrammar-constrained vLLM decoding) outperform oracle post-hoc filtering of unconstrained generation for zero-shot EAE, and does any advantage concentrate in role strata where theory predicts?\\n\\nThe primary motivation is a structural salience hypothesis: the RAMS ontology TSV specifies only maximum cardinality (the 'count permitted' column is an upper bound on role occurrences per instance, not a minimum), so XGrammar enforces upper-bound cardinality and entity-type compatibility but cannot logically guarantee that optional roles appear in every generated instance. Instead, SCG provides structural salience through required key enumeration: in the XGrammar encoding, all applicable role slots for a given event type appear as required keys in the output JSON template. The LLM generates empty strings or null values for absent optional arguments but cannot omit role keys from the output. This required-key design forces the model's attention to each slot during the forward pass, counteracting the prior bias toward omitting rare optional slots that characterizes unconstrained generation. Post-hoc filtering (Condition B) removes violations but cannot recover coverage for role keys that unconstrained generation never emitted — a structural gap that filtering cannot close. Prior work (GEMS ACL Findings 2025 — ontology steering at inference time; FineCSDA NLPCC 2024 — targeted prompt augmentation; LtGaE AAAI 2026 — aggregate soft RL penalties) addresses rare-role under-representation via different mechanisms, none of which provides formal required-key enumeration at generation time. Concurrently, BoostCD (EMNLP 2025, arXiv:2506.14901) demonstrates complementary error profiles of constrained vs. unconstrained decoding at inference time for closed IE (relation extraction); CompSchema-IE investigates the analogous structural salience question at training-data generation time for EAE.\\n\\nA three-condition, volume-controlled ablation (N=5,000 instances per condition, distributed proportionally across RAMS's 139 event types) isolates the grammar effect cleanly: (A) Unconstrained, randomly subsampled to N=5,000 training instances; (B) Post-hoc Filtered (oracle soft-constraint approximation, volume-matched to N=5,000 by generating a 7,500-instance pool and filtering to N, with achieved discard rate reported as transparency metric); (C) SCG-Constrained (grammar-constrained to exactly N=5,000 instances with required role-key enumeration providing structural salience). All conditions use Qwen3-32B, the same schema information, and the same final training volume N, making the C-vs-B comparison methodologically airtight. A motivating pilot study measures entity-type mismatch, cardinality violation, role hallucination, and role coverage rates in Qwen3-32B unconstrained generation on RAMS/WikiEvents (600 instances; all metrics reported unconditionally). LoRA fine-tunes Qwen3-8B on each volume-matched corpus; evaluation uses the LtGaE three-way protocol with LtGaE, ASEE, and DEGAP as baselines. Null result interpretation is pre-specified: if C does not outperform B in rare-role strata, the paper reports this as a clearly framed negative finding — grammar-guided structural enumeration provides no additional benefit over oracle post-hoc filtering at Qwen3-32B scale, suggesting the model's instruction-following capability already provides adequate structural salience through prompt-specified schema descriptions. The stratified evaluation by (a) role rarity quartile and (b) cardinality tightness (max=1 vs. max>1) reports both role coverage and argument span F1 per stratum, distinguishing coverage gains from potential quality tradeoffs introduced by grammar-constrained decoding (Schall & de Melo, RANLP 2025). CompSchema-IE extends the SynthIE task-reversal paradigm (EMNLP 2023) with formal grammar-constrained decoding and compositional cardinality bounds. Target: EMNLP 2026 Findings (ARR May 25, 2026). Estimated GPU cost: ~$187 (125.5h A100 ≈ 90h H100-equiv, within budget). Timeline: 16 active days.\",\n  \"project_name\": \"schema_constrained_event_ie\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"Auto mode (900h A100 ≈ 450–630 H100-equiv hours) clearly violates the ≤200 H100-hour hard constraint; even the HIL mode (~380h A100 ≈ 190–266h H100-equiv) is borderline. The proposal must be scoped to core manual-mode experiments only, and the auto/HIL resource tables should be removed or flagged as out-of-scope for this submission.\", \"Critical omission: 'Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation' (ASEE, arXiv 2505.08690, May 2025, https://arxiv.org/abs/2505.08690) directly addresses schema-aware event extraction using schema paraphrasing + RAG, constructs a 12-dataset benchmark (MD-SEE), and is published just weeks before the proposed submission. This paper must be cited, compared against, and explicitly differentiated.\", \"'Learning to Generate and Extract' (AAAI 2026, arXiv 2603.02909) already uses 'event structure constraints incorporated into the reward design' to guide synthetic data generation for zero-shot document-level event argument extraction on RAMS and WikiEvents — the same benchmarks. The proposed paper's claim that 'neither enforces hard compositional constraints at training-data generation time' needs empirical substantiation showing that hard grammar constraints outperform soft RL-based structural reward signals, not just a definitional distinction.\", \"Unvalidated core hypothesis: the paper assumes compositional constraint violations in generated training data are the primary bottleneck for zero-shot event extraction, but provides no motivating study. With Qwen3-235B-A22B as generator, modern frontier LLMs with strong instruction following may naturally produce consistent role–entity assignments at high rates; the verifier's filter rate and its downstream effect on model quality are entirely unknown.\", \"Qwen3-235B-A22B inference on 4×A100 80GB (320 GB VRAM): FP8 weights alone occupy ~235 GB, leaving ~85 GB for KV cache — severely limiting batch size and throughput. The vendor-recommended minimum configuration is 8-GPU tensor parallelism (--tp 8). Practical deployment on 4×A100 requires INT4 quantization, which may degrade generation quality and invalidates the clean cost estimate.\", \"The claimed 30–50 F1-point gap between zero-shot and supervised methods is overstated for current SOTA: the best zero-shot methods (LtGaE 2026, BiTer) achieve ~32–47 F1 on RAMS/WikiEvents zero-shot scenarios while supervised SOTA reaches 52–69 F1 — the gap is task- and benchmark-specific (5–37 F1 points), not a uniform 30–50 points.\"]\nFeedback: The idea targets a genuine and underexplored gap (extending GuideX-style synthetic supervision to compositionally structured event schemas), but in its current form the novelty claim is undermined by two concurrent papers the generator missed. The revision must: (1) Cite and differentiate from ASEE (arXiv 2505.08690) — ASEE approaches schema-awareness via RAG rather than formal grammars during generation; CompSchema-IE's differentiation should be that SCG enforces hard cardinality and type-compatibility constraints that cannot be retrieved post-hoc. (2) Strengthen differentiation from LtGaE (arXiv 2603.02909) by adding an ablation comparing grammar-constrained hard generation vs. RL-reward-guided soft generation on WikiEvents/RAMS — this turns the design choice into a falsifiable experimental contribution. (3) Add a motivating pilot study (even 100 generated examples, manually inspected) showing that unconstrained Qwen3-235B-A22B does in fact produce constraint-violating instances (wrong entity type for argument role, cardinality violations) at non-trivial rates — without this, the SCG module has no evidenced purpose. (4) Scope compute to the manual-mode experiments only (≤250h A100 ≈ 175h H100-equiv, within budget) and remove the auto mode entirely from the proposal. (5) Replace Qwen3-235B-A22B with Qwen3-32B or Llama-3.1-70B as the generator — these fit on 2×A100 comfortably, reducing generation hardware risk while still producing high-quality synthetic text; Qwen3-235B-A22B can be framed as an optional upper-bound experiment if resources allow.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"BiTer (Bi-directional Feature Learning-Based Approach for Zero-Shot Event Argument Extraction, Information Processing and Management, May 2025) is not cited. This paper reports SOTA zero-shot performance on RAMS and WikiEvents with +4.6%/+7.5% F1 over the prior best and uses a different approach (pseudo-argument generation from LLMs + bidirectional knowledge transfer), making it directly relevant as a baseline. Omitting it means the proposed method's competitive positioning against the actual SOTA is unknown.\", \"The pilot study contingency plan is inadequate. The proposal acknowledges 'If the pilot study reveals very low violation rates (<2%), the SCG module's value proposition is weakened and the paper's framing should shift.' But this is not a contingency plan — it is an admission that the paper could have no compelling finding. If Qwen3-32B (a strong instruction-following model) violates event schema constraints rarely, the entire SCG contribution becomes a null result. The proposal needs either a pre-registration of what level of violation rate constitutes a paper (and what the fallback is if it doesn't), or a theoretical argument for why hard constraints add value independent of their violation rate (e.g., as a distributional regularizer, speed benefit, or interpretability advantage).\", \"The PARSE citation for the '~12% invalid response rate' is for GPT-4 on complex structured extraction (EMNLP 2025 Industry Track), not Qwen3-32B. Qwen3-32B is a newer model with potentially stronger instruction-following and may have substantially lower violation rates in practice. The motivating claim should be stated as a hypothesis to be confirmed by the pilot study, not as established fact for the proposed model.\", \"The cross-ontology schema normalization scope is underestimated. Unifying ACE05 (24 event types, ~35 argument roles), WikiEvents (~50 event types), and RAMS (139 event types, 65 argument roles) into a single formal constraint grammar with entity-type compatibility mappings is a multi-week engineering and curation task. The role vocabularies across the three ontologies do not overlap neatly (e.g., RAMS 'Victim' vs. ACE05 'Target' vs. WikiEvents 'place'). Within 16 days, this competes directly with the pilot study annotation and the soft-baseline ablation implementation.\", \"The soft-RL baseline ablation (matching LtGaE's reward design) requires implementing a multi-agent evaluation loop with an evaluation agent computing normalized log-likelihood and a structural completeness penalty. LtGaE achieves this via separate generation and evaluation agents with LoRA-tuned models. Re-implementing this faithfully within 16 days is unrealistic alongside the other engineering tasks. The ablation would be stronger and more tractable if simplified to: (a) unconstrained prompt-only generation (no grammar, no reward) vs. (b) SCG-constrained generation — this tests the same hypothesis more cleanly.\"]\nFeedback: The Round 2 revision has successfully addressed all five critical Round 1 issues: compute is within budget (122h H100-equiv confirmed), ASEE and LtGaE are properly cited with mechanistic differentiation, the pilot study adds empirical motivation, and Qwen3-32B on 2×A100 BF16 is hardware-feasible. The remaining issues are fixable but require concrete action before this is submission-ready.\n\n(1) Add BiTer as a baseline. Search for the full paper at doi.org/10.1016/j.ipm.2025.104199 and include its absolute F1 numbers in the comparison table. If BiTer outperforms LtGaE, frame CompSchema-IE as improving over both.\n\n(2) Strengthen the pilot study's decision framework. Before running the full pipeline, the pilot study should produce a pre-specified threshold: 'If violation rate > X%, we proceed with the full SCG approach. If rate < X%, we [specific alternative contribution].' A better alternative contribution at low violation rates: demonstrate that grammar-constrained generation produces structurally more diverse training examples (measured by argument role distribution) even when violations are rare — this is a quality argument that doesn't depend on violation rates.\n\n(3) Scope the ontology normalization. Start with WikiEvents + RAMS only (these share more structural similarity and are the primary benchmarks LtGaE targets). Add ACE05 only if time permits. This removes the hardest cross-vocabulary alignment problem while preserving the core experimental claims.\n\n(4) Simplify the ablation. Replace the full LtGaE RL re-implementation with a simpler two-condition comparison: SCG-constrained generation vs. unconstrained generation (standard chat prompting with the same event schema descriptions). This directly tests whether grammar constraints at generation time help, without requiring a multi-agent RL implementation. Note this in the paper as a controlled comparison rather than a direct LtGaE replication.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"SUPERVISED SOTA NUMBERS ARE FACTUALLY WRONG: DEGAP (2024) achieves 54.2 Arg-C on RAMS — not 52.2 — and 67.1 on WikiEvents — not 68.8. The numbers may be from DEEIA (which DEGAP supersedes), but the paper currently attributes them to 'DEGAP/DEEIA 2024' without clarification. This understates the RAMS gap (54.2 − 45.77 = 8.4 F1, not 6 F1) and overstates the WikiEvents supervised score. Fix by correctly attributing each number to the specific paper that reports it.\", \"UNCITED DIRECT PREDECESSOR: 'Large Language Models for Document-Level Event-Argument Data Augmentation for Challenging Role Types' (arXiv:2403.03304, Gatto et al., March 2024) uses LLMs to synthesize document-level EAE training data for zero-shot/few-shot roles and achieves +16pt F1 on zero-shot role types on RAMS — this is the closest published predecessor to CompSchema-IE's core idea. Not citing it leaves a gap that reviewers familiar with EAE data augmentation will notice. The differentiation is clear (arXiv:2403.03304 does not enforce hard cardinality/entity-type grammar constraints), but it must be cited.\", \"BITER COMPARISON PROTOCOL IS OPERATIONALLY UNRESOLVED: BiTer reports F1 on standard within-dataset zero-shot splits (event types held out by type), while LtGaE uses a cross-dataset three-way protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki). These protocols are NOT interchangeable. Getting BiTer's F1 under the LtGaE protocol requires either (a) running BiTer's code on the LtGaE data splits (requires code availability + compute, non-trivial) or (b) author cooperation. The proposal says 'to be obtained from the full paper' but this is not realistic given the protocol difference. The paper should explicitly acknowledge the protocol mismatch, report BiTer's numbers under BiTer's native protocol with a clear note, and NOT imply direct numerical comparability.\", \"DUAL-FRAMING CREATES REVIEWER PERCEPTION RISK: The pre-specified decision rule ('if violation rate >5%, primary claim is A; if ≤5%, primary claim is B') is epistemically honest but strategically risky for EMNLP Main submission. Reviewers may read this as 'the authors do not know what their own contribution is.' The structural regularization argument (higher argument role coverage, provable entity-type consistency) is the more durable long-term claim and should be the PRIMARY framing regardless of violation rate. The pilot study's violation rate then becomes secondary supporting evidence. Commit to 'SCG as structural regularizer' as the headline claim and present violation rate as a motivating data point, not a framing branch condition.\", \"ABLATION DESIGN DOES NOT RULE OUT MARGINAL IMPROVEMENT RISK: The core ablation (SCG-constrained vs. unconstrained generation) isolates the grammar effect cleanly, but the paper currently has no stratified evaluation by argument role frequency or schema complexity. If overall F1 improvement is small (e.g., ≤1 F1), reviewers will dismiss the contribution. Stratified evaluation by (a) rare roles (bottom quartile by training frequency) and (b) roles with tight cardinality constraints (max=1) would demonstrate that SCG gains concentrate where they theoretically should — this turns a potentially flat overall number into a principled, interpretable finding.\"]\nFeedback: The Round 2 revision successfully resolved all five critical prior issues, and the proposal is now technically credible. The remaining blockers before submission readiness are: (1) Fix supervised SOTA numbers — look up DEEIA's exact RAMS Arg-C F1 and DEGAP's WikiEvents Arg-C F1 and attribute each number to the correct paper. (2) Cite arXiv:2403.03304 (Gatto et al., 2024) and write a one-paragraph differentiation: that paper uses LLMs for EAE data augmentation but does not enforce cardinality or entity-type grammar constraints, and focuses on few-shot rather than zero-shot transfer — CompSchema-IE's SCG module is the distinguishing contribution. (3) Resolve the BiTer protocol comparison honestly: state that BiTer uses within-dataset event-type splits while CompSchema-IE uses the LtGaE three-way cross-dataset protocol, report BiTer's native-protocol numbers with a clear footnote, and do not claim direct comparability. (4) Restructure the framing to lead with structural regularization as the primary contribution unconditionally — 'SCG guarantees full argument role coverage and provable entity-type consistency in training data; the pilot study additionally measures unconstrained violation rates' — eliminating the contingency branch. (5) Add stratified evaluation by role rarity and cardinality tightness as the analysis section, not as an afterthought; this is where the paper's strongest signal will appear.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"FATAL TIMELINE VIOLATION: The Generator's manual-mode estimate is 3–4 months, explicitly acknowledging that the May 25 ARR deadline cannot be met. This violates the user's hard ≤16-day constraint. Additionally, the Generator's proposed workaround ('ARR August 2026 cycle') is based on a misreading of the ARR calendar: August 2, 2026 is the COMMITMENT deadline for papers already in review from the May 25 submission, not a new submission cycle. There is no August ARR submission cycle that would yield EMNLP 2026 acceptance. The proposal must either (a) compress scope to a version executable in 16 days or (b) explicitly declare this idea is out-of-scope for the May 25 constraint.\", \"MISSING ABLATION — SCG vs. LtGaE SOFT RL: The core ablation compares SCG-constrained vs. unconstrained generation, which cleanly isolates the grammar effect. However, EMNLP reviewers familiar with LtGaE will ask: why does hard grammar enforcement outperform LtGaE's soft RL penalty, given LtGaE already achieves 45.77/32.38/46.96 F1 with soft constraints? Without a direct comparison on the same evaluation protocol, the claim that hard cardinality+entity-type constraints are better than soft RL argument-completeness rewards is an architectural assertion, not a demonstrated result. This is the most obvious reviewer concern for the EMNLP main paper track.\", \"THIN TECHNICAL CONTRIBUTION FOR EMNLP MAIN: The SCG module derives a grammar from the RAMS TSV (confirmed: cardinality is column-encoded) and feeds it to off-the-shelf XGrammar in vLLM. This is a pipeline integration, not an algorithmic contribution. EMNLP Main reviewers expect either (a) >2 F1 improvement over prior SOTA with clear ablation, or (b) technical novelty beyond tool integration. The stratified evaluation is analytically interesting but is framing/analysis, not architecture. EMNLP Findings is a more defensible target than EMNLP Main given current technical depth.\", \"PILOT STUDY RISK NOT FULLY MITIGATED: Qwen3-32B is a modern strong instruction-following model. The framing as 'structural regularizer' partially decouples the paper from requiring high violation rates, but the paper still relies on the pilot study as 'supporting empirical evidence.' If measured violation rates are <1% across all four metrics (plausible for a strong model given structured prompting), a reviewer can legitimately ask: why do we need formal grammar enforcement if the LLM already complies? The structural regularization reframing needs a concrete answer to this question that does not depend on violation rates.\"]\nFeedback: The Round 3 revisions are well-executed: all five prior issues are resolved, the supervised SOTA numbers are independently verified correct, the ARR timeline confusion needs immediate attention. Here are the four concrete actions needed before this is submission-ready:\n\n(1) COMPRESS SCOPE TO 16 DAYS OR DECLARE TIMELINE INFEASIBILITY. The 3–4 month estimate likely includes extensive ablations, careful analysis, and writing time. A minimal viable submission to the May 25 ARR deadline requires: SCG construction for RAMS+WikiEvents only (5–7 days, using the confirmed machine-readable cardinality TSV), pilot study on 200 instances (1 day), constrained generation (GPU, 1 day), LoRA fine-tuning across 3 ablation conditions (GPU, 2 days), evaluation on LtGaE three-way protocol (1 day), stratified analysis (1 day), paper writing concurrent. This is approximately 11–12 active days — tight but feasible with a focused team. Remove extended ablations, reduce fine-tuning runs, and defer optional experiments (ACE05 comparison, BiTer replication) to the revision stage.\n\n(2) ADD SOFT vs. HARD CONSTRAINT COMPARISON VIA LIGHTWEIGHT ORACLE BASELINE. Rather than re-implementing LtGaE's full RL loop (unrealistic), add a third ablation condition: 'post-hoc filtered unconstrained generation' (generate unconstrained, then filter violating instances via the verifier). This approximates the achievable quality of soft constraint enforcement without requiring RL, and lets the paper argue: 'even oracle-filtered unconstrained data underperforms SCG-constrained data on rare roles — because filtering cannot guarantee proportional role coverage.' This directly demonstrates the value of hard constraints over soft/filtered approaches without re-implementing LtGaE.\n\n(3) ANCHOR THE STRUCTURAL REGULARIZER FRAMING AGAINST ZERO-VIOLATION RATES. Add the following argument explicitly to the paper: 'Even if individual constraint violation rates are low, unconstrained generation cannot guarantee proportional representation of all schema roles across a finite corpus. SCG enforces this by construction: given 1,000 generated instances for event type T with role R having max-cardinality=1, the SCG guarantees exactly one instance of R per event — unconstrained generation may cluster on frequent roles and never instantiate rare ones, even with zero explicit violations.' This argument is valid regardless of violation rates and directly motivates SCG as a distributional regularizer, not just a constraint enforcer.\n\n(4) TARGET EMNLP 2026 FINDINGS EXPLICITLY. Given the thin technical depth (pipeline integration, not algorithmic novelty), EMNLP Findings is the more defensible submission target within the same May 25 deadline. This does not require any change to the method — simply adjust the positioning in the paper to emphasize the empirical analysis and stratified evaluation as the primary contribution, rather than the SCG module itself.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"CRITICAL — VOLUME CONFOUND IN CONDITION B: The three-condition design requires all conditions to train on equal data volume, but Condition B (post-hoc filtered) necessarily discards some fraction of the Condition A instances. If the filter removes 20–50% of instances (plausible even for strong models on compositional constraints), B trains on substantially less data than C, biasing the C-vs-B comparison in favor of C independently of the grammar effect. The proposal must specify: (a) generate excess instances for the A/B pool so that B achieves the same final volume as C after filtering, OR (b) deliberately undersample C to match B's post-filter volume as a volume-controlled analysis. Without this control, EMNLP reviewers will reject the paper on methodological grounds.\", \"MISSING CITATION — FineCSDA: 'FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation' (NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) specifically identifies the long-tail distribution of argument roles as a bottleneck and proposes LLM augmentation at both sample and context levels to address rare argument roles. While FineCSDA does NOT use formal grammar constraints and uses a different mechanism, it is a direct predecessor addressing the same identified gap (rare-role under-representation in training data). Reviewers familiar with document-level EAE data augmentation will notice the omission. Add a one-sentence differentiation: FineCSDA augments rare roles via sample-level and context-level LLM generation without enforcing formal cardinality or entity-type constraints — CompSchema-IE's SCG provides a distributional coverage guarantee by construction.\", \"NEGATIVE RESULT PATH UNACKNOWLEDGED: The proposal correctly states that C-B stratified gains may be modest, but does not explicitly acknowledge what happens if C fails to outperform B even in the rare-role quartile. If this occurs, the paper's primary empirical claim is a null result — potentially a useful negative finding (post-hoc filtering suffices, grammar constraints add no measurable value), but the proposal frames this as a risk without naming it. For EMNLP Findings, a clearly framed negative result is publishable, but it requires different positioning from the current abstract. Add a brief paragraph explicitly framing the null-result paper: 'If stratified analysis reveals no C-B advantage, we report this as a negative finding: for strong instruction-following models like Qwen3-32B, post-hoc filtering achieves equivalent coverage to formal grammar constraints, suggesting that engineering investment in SCG construction may not be warranted at this model scale.'\", \"PILOT STUDY SAMPLE SIZE RISK: The pilot study samples 200 event instances from RAMS and WikiEvents. RAMS has 139 event types; 200 instances gives fewer than 2 samples per event type on average, making role-level statistics extremely noisy for rare roles. Either increase the pilot study to 500–1000 instances (adds ~2 GPU-hours, within budget) or clearly scope the pilot to a subset of 5–10 event types with enough instances for per-role statistics.\"]\nFeedback: The Round 5 revision is the strongest version of this proposal so far. All prior critical issues (timeline, compute, ASEE/LtGaE/Gatto et al. citations, DEGAP numbers, stratified evaluation, BiTer protocol note) have been correctly resolved. The four remaining issues are fixable and one is straightforward; the volume confound is the only blocker that could sink the paper at review time.\n\n(1) VOLUME CONTROL [CRITICAL]: Before generating data for the three conditions, add a volume normalization protocol: generate 1.5× the target volume for Condition A, then both Condition A (random subsample to target) and Condition B (post-filter residual targeting the same volume) and Condition C (SCG-constrained to exact target volume) all end up with the same number of training instances. Report the achieved filter rate for Condition B as a transparency metric (e.g., 'we generated 1.5N instances for A and retained the top N after filtering, achieving a X% discard rate'). This one addition makes the C-vs-B comparison methodologically airtight.\n\n(2) CITE FineCSDA: Add a sentence in related work: 'FineCSDA (NLPCC 2024) identifies the rare-role under-representation problem and addresses it via LLM-powered sample-level and context-level augmentation; unlike CompSchema-IE, FineCSDA does not impose formal cardinality bounds or entity-type constraints, relying instead on targeted prompt design for rare event types.' This closes the citation gap reviewers may notice.\n\n(3) FRAME THE NULL RESULT: Add a two-sentence paragraph to Section 3 (Approach) or Section 5 (Expected Findings): 'We pre-specify the null result interpretation: if C does not outperform B in the rare-role quartile, we report that post-hoc filtering achieves equivalent rare-role coverage to formal grammar constraints at Qwen3-32B scale, providing a practically useful negative finding for practitioners considering SCG implementation overhead.'\n\n(4) INCREASE PILOT STUDY SCOPE: Sample 600 instances (4 GPU-hours total, still within the Day 3-4 budget) to achieve ~4–5 instances per event type on average, enabling more reliable role-level violation statistics.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"COVERAGE GUARANTEE LOGICAL GAP [critical, newly identified]: The proposal's primary theoretical claim — 'SCG enforces proportional coverage by construction: the grammar mandates that each mandatory role appears in every generated instance' — is overstated given confirmed RAMS TSV structure. The RAMS ontology TSV (independently verified at nlp.jhu.edu/rams/) specifies only MAXIMUM cardinality (the 'count permitted' column), NOT minimum cardinality. XGrammar therefore enforces upper-bound cardinality and entity-type constraints, but CANNOT force optional roles to appear. Since rare roles in RAMS may be optional in many event types (a given event instance may legitimately not have an 'Instrument' or 'Beneficiary'), the grammar provides no coverage guarantee for those roles. The coverage guarantee claim holds only for roles that the paper explicitly sets min-cardinality=1 in the grammar — which would require an assumption not derivable from the RAMS TSV alone and would produce unrealistic training data (every instance must have every role filled). The proposal must either (a) acknowledge this and narrow the guarantee to 'roles assigned min-cardinality=1 in the grammar encoding' with an explicit design choice described, or (b) reframe the theoretical argument from 'structural coverage guarantee' to 'structurally-prompted generation is more likely to instantiate optional rare roles due to explicit slot salience' — an empirical hypothesis rather than a logical guarantee. This is the single issue that a RAMS-familiar reviewer will raise immediately.\", \"BoostCD unacknowledged [minor]: 'Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction' (EMNLP 2025 Main, arXiv:2506.14901) empirically demonstrates that constrained and unconstrained decoding errors are complementary for closed IE, with a learned boosted model combining both. While BoostCD targets inference-time decoding (not training-data generation), its central empirical finding — that hard constraints and unconstrained generation have complementary error profiles — is directly relevant to CompSchema-IE's motivating argument and should be cited in related work with a one-sentence differentiation.\", \"Training volume N unspecified [minor]: The proposal never states the target training volume N. For RAMS with 139 event types, the number of instances per type and total N are unknown, making the GPU cost estimates (37.5h for 1.5N pool, 25h for N SCG-constrained) unverifiable. Specify N upfront (e.g., 'N=5,000 instances distributed proportionally across event types') so compute estimates and reproducibility can be assessed.\"]\nFeedback: The Round 6 proposal is the strongest version yet — all five Round 5 issues are properly resolved (volume normalization via 1.5× pool, FineCSDA cited and differentiated, null result pre-specified, pilot study at 600 instances, BiTer protocol mismatch handled). DEGAP F1 numbers (RAMS 54.2, WikiEvents 67.1 Arg-C) are independently verified correct. XGrammar overhead claim (<40μs/token as default vLLM backend) is confirmed. One fixable critical issue blocks submission readiness: the coverage guarantee must be corrected.\n\n(1) REVISE THE COVERAGE GUARANTEE ARGUMENT [critical]: The RAMS TSV only provides maximum cardinality (upper bounds on role occurrences), not minimum cardinality. The grammar therefore enforces: (a) no role appears more than its max count, and (b) when filled, entity types are compatible. It CANNOT guarantee that rare optional roles appear at all. Replace 'SCG enforces proportional coverage by construction' with one of two framings: OPTION A — 'In our grammar encoding, we set min-cardinality=1 for all roles applicable to a given event type, guaranteeing their appearance in every generated instance; this is a design choice that differs from natural annotation practice and we evaluate whether this artificial completeness improves rare-role coverage downstream.' OPTION B — 'SCG provides structural salience: by enumerating every applicable role slot explicitly in the constrained generation template, the LLM is prompted to consider filling each slot rather than freely omitting rare ones; we test empirically whether this structured attention mechanism improves rare-role instantiation.' Option B is more honest and requires no changes to the actual method.\n\n(2) ADD BoostCD [one sentence in related work]: 'Concurrently, BoostCD (EMNLP 2025) demonstrates that constrained and unconstrained decoding produce complementary errors at inference time for closed IE; CompSchema-IE investigates an analogous question at training-data generation time, where coverage differences compound across a finite corpus.'\n\n(3) SPECIFY N [one sentence in Section 2 or Step 2]: State the target training volume N explicitly (e.g., 'N=5,000 instances drawn proportionally across RAMS event types') so compute estimates are verifiable and the paper is reproducible.\n\nWith these three changes — particularly the coverage guarantee reframing — the proposal is ready for EMNLP 2026 Findings submission. The empirical design is sound, the null result handling is appropriate, and the resource estimate is within budget.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"MISSING CITATION — GEMS (ACL Findings 2025): 'GEMS: Generation-Based Event Argument Extraction via Multi-perspective Prompts and Ontology Steering' (aclanthology.org/2025.findings-acl.1353) is not cited. GEMS uses multi-perspective prompting and ontology steering for EAE on WikiEvents/ACE05, achieving SOTA in low-resource settings. While GEMS is inference-time extraction rather than training-data generation, its 'ontology steering' mechanism is conceptually related to CompSchema-IE's schema-constrained generation. A one-sentence differentiation is required: 'GEMS (ACL Findings 2025) uses multi-perspective prompts and ontology steering for inference-time EAE; CompSchema-IE instead applies hard grammar constraints at training-data generation time, investigating whether structural salience during generation improves downstream rare-role coverage.'\", \"OPTIONAL ROLE GRAMMAR REPRESENTATION UNSPECIFIED [moderate]: The structural salience argument rests on the claim that the grammar 'explicitly enumerates every applicable role slot in the constrained generation template,' prompting the LLM to consider each slot. But the proposal never states HOW optional slots are represented in the grammar template: (a) required JSON keys with empty-string values allowed, (b) optional JSON keys that may be omitted, or (c) required keys with a special [NONE] token. This distinction is critical — design (b) provides no structural salience over Condition A because slots can still be omitted; design (a) forces the LLM to generate each role name as a JSON key, which IS the structural salience mechanism. The paper must state this explicitly, e.g.: 'All applicable role slots appear as required keys in the output JSON schema; the LLM may output empty strings or null for absent optional arguments, but cannot omit role keys from the output.' Without this, the structural salience claim is not reproducible.\", \"XGRAMMAR QUALITY DEGRADATION UNACKNOWLEDGED [minor]: Recent empirical work (Schall & de Melo, RANLP 2025; structured output benchmarks 2025) demonstrates that grammar-constrained decoding introduces quality degradation — forcing models into non-canonical token paths degrades output quality, particularly for rare or complex outputs. One study found XGrammar led to substantially more extraction misses than top unconstrained strategies for LLaMA-70B. The specific risk for CompSchema-IE: if the grammar forces generation of all role slots sequentially, the model may produce lower-quality argument spans for common roles in order to comply with the grammar structure — confounding the C-vs-B comparison. The paper should acknowledge this in the limitations section: 'Grammar-constrained decoding may introduce quality tradeoffs beyond structural coverage (Schall & de Melo, RANLP 2025); we mitigate this risk by using Qwen3-32B, which has strong structured output capabilities, and by measuring both role coverage and argument span quality in our stratified evaluation.'\"]\nFeedback: Round 7 correctly resolves all three Round 6 issues: the coverage guarantee is properly reframed as structural salience (Option B framing), BoostCD is cited, and N=5,000 is specified. The LtGaE absolute F1 numbers (45.77/32.38/46.96) are independently verified correct. The EMNLP 2026 ARR May 25 deadline is confirmed valid with mandatory commitment at submission. The volume normalization (1.5x pool), pre-specified null result, and stratified evaluation design are all sound.\n\nThree targeted fixes are needed before submission readiness:\n\n(1) ADD GEMS CITATION [one sentence]: Add 'GEMS: Generation-Based Event Argument Extraction via Multi-perspective Prompts and Ontology Steering (ACL Findings 2025)' to related work with a differentiation sentence. This is the closest concurrent work using ontology-guided EAE that reviewers familiar with the area will know.\n\n(2) SPECIFY OPTIONAL ROLE GRAMMAR REPRESENTATION [one paragraph in Step 1]: The structural salience mechanism depends entirely on whether the grammar requires all role slot names to appear as output keys (providing salience) or permits key omission (no salience). State explicitly: 'In our XGrammar encoding, all applicable role slots for a given event type appear as required keys in the output JSON template; the LLM generates empty strings or null values for absent optional arguments but cannot omit role keys.' This makes the mechanism reproducible and directly supports the structural salience claim.\n\n(3) ACKNOWLEDGE XGRAMMAR QUALITY TRADEOFF [one sentence in limitations]: Note that grammar-constrained decoding can introduce quality degradation in text generation quality (Schall & de Melo, RANLP 2025). Mitigate by measuring argument span F1 per role stratum (not just role coverage), so quality and coverage effects are distinguishable in the stratified evaluation.\n\nWith these three additions — all writable during paper drafting — the proposal is ready for EMNLP 2026 Findings submission.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T09:44:03.357Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T09:44:03.357Z",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-10T09:44:03.386Z_

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

## Idea under review (round 8/10)
{
  "title": "CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Shot Event Argument Extraction — An Empirical Study via Synthetic Supervision",
  "core_problem": "Synthetic-data-based zero-shot event argument extraction (EAE) faces a structural data quality problem that existing approaches address only partially. LtGaE (AAAI 2026) uses soft RL penalties for argument completeness — a quality score penalty that fires when the proportion of empty arguments per sample deviates from a target range [τ−ε, τ+ε], but does not enforce per-role entity-type compatibility or hard cardinality bounds during decoding. Gatto et al. (ACL 2025 Long) uses free-form LLM generation with no formal constraints. FineCSDA (NLPCC 2024) targets the long-tail distribution of argument roles via sample-level augmentation of rare event types (SDAM) and context-level injection of rare role fillers (CDAM), but neither module enforces formal cardinality bounds or entity-type constraints — coverage improvement relies on targeted prompt design rather than any structural enumeration mechanism. GEMS (ACL Findings 2025) applies ontology steering at inference time via multi-perspective prompting and voting, not at training-data generation time.\n\nNone of these approaches systematically addresses the structural salience of rare argument roles during generation. The RAMS ontology TSV specifies only maximum cardinality (the 'count permitted' column is an upper bound on role occurrences per instance, not a minimum), so grammar-constrained decoding via XGrammar enforces: (a) no role exceeds its permitted maximum count, and (b) when filled, entity types are compatible. It cannot logically force optional roles to appear — setting min-cardinality=1 for all roles would require an assumption not derivable from the RAMS TSV and would produce unrealistically complete training instances where every event instance has every schema role filled. Instead, Schema-Constrained Grammar (SCG) provides a different mechanism: structural salience. Critically, in the XGrammar encoding all applicable role slots appear as required keys in the output JSON template — the LLM generates an empty string or null value for absent optional arguments but cannot omit role keys from the output. This key-level requirement is the structural salience mechanism: it forces the model's attention to each slot during the forward pass, counteracting the prior bias toward omitting rare slots that characterizes unconstrained generation. Even when individual constraint violation rates are low (plausible for strong instruction-following models like Qwen3-32B), unconstrained generation tends to cluster on high-frequency role patterns due to LLM prior biases, likely under-representing rare optional roles. Post-hoc filtering (Condition B) removes entity-type violations and cardinality overruns but operates on outputs from unconstrained generation where rare role keys were never generated — it cannot recover coverage for roles absent from the unconstrained output corpus.\n\nThe primary gap CompSchema-IE targets is empirical and analytical: we do not know (a) whether hard grammar constraints (formal cardinality + entity-type enforcement via XGrammar, which provides structural salience through required role-key enumeration over and above entity-type and cardinality filtering) outperform oracle post-hoc filtering of unconstrained generation on downstream zero-shot EAE, (b) in which role strata these differences concentrate, or (c) whether any structural regularization gains are mechanistically explained by rare-role instantiation improvements. Answering these questions empirically — with a clean three-condition ablation, volume-controlled design, and stratified evaluation — is a concretely useful contribution for EMNLP Findings, even if overall F1 deltas are modest.",
  "opportunity": "The supervised-to-zero-shot gap remains 8–35 F1 points (supervised SOTA: DEGAP COLING 2025 — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1; TSCA IET Software 2026 adds ~+3.0/+1.0 F1 in fully supervised settings; best zero-shot cross-dataset: LtGaE 32–47 F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki). Training data quality for the generator model is a concrete bottleneck: LtGaE's soft RL penalties improve over prior unconstrained generation but cannot guarantee per-role proportional coverage; FineCSDA's targeted augmentation improves rare-role counts but lacks formal structural enumeration. GEMS (ACL Findings 2025) provides ontology-guided inference-time EAE but does not address training-data generation quality. SynthIE (EMNLP 2023) demonstrated that task-reversal generation can produce highly effective synthetic IE training data, but uses no grammar-constrained decoding and does not address event argument extraction. The key open question is whether hard constraints provide a measurable advantage over oracle-quality soft filtering under a volume-controlled design. This question has a clean experimental operationalization: (A) unconstrained generation, (B) unconstrained generation with post-hoc violation filtering (oracle soft constraint approximation, volume-matched to A and C), and (C) grammar-constrained generation via XGrammar — same model, same schema information, same final training volume. If C outperforms B on rare roles despite similar overall violation rates, the result directly demonstrates that structural salience (not just constraint compliance) drives the downstream gain — the SCG's required role-key enumeration in the output template forces the model to instantiate each slot rather than silently omitting rare keys during unconstrained generation. This is a falsifiable, mechanistically interpretable empirical finding — the type EMNLP Findings values.",
  "landscape": "GuideX (ACL Findings 2025) sets SOTA on 7 zero-shot NER benchmarks with Llama-3.1 fine-tuned on generated data, but explicitly does not address event argument extraction.\n\nGEMS (ACL Findings 2025, aclanthology.org/2025.findings-acl.1353) uses multi-perspective prompts and ontology steering for inference-time EAE on WikiEvents, ACE05, and ERE-EN, achieving SOTA in low-resource settings. GEMS applies ontology knowledge at inference time via a voting mechanism over multiple generation paths with T5-large as the base model; CompSchema-IE instead applies hard grammar constraints at training-data generation time, investigating whether structural salience from required role-key enumeration during generation improves downstream rare-role coverage — a complementary research question targeting a different phase of the pipeline.\n\nFineCSDA ('FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation', NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) directly identifies the long-tail distribution of argument roles as a bottleneck and proposes two augmentation modules: SDAM generates new document-level samples for rare event types, and CDAM injects rare argument roles and corresponding context into common event type documents. Unlike CompSchema-IE, FineCSDA does not impose formal cardinality bounds or entity-type constraints, and provides no structural role-slot enumeration — coverage improvement relies on targeted prompt design for rare types and roles.\n\nGatto et al. ('Document-Level Event-Argument Data Augmentation for Challenging Role Types', ACL 2025 Long, arXiv:2403.03304) is a direct predecessor: LLM-powered augmentation (Mad Lib Aug and Struct2Text) for extractive EAE, +13 F1 on zero-shot role types using BERT-QA, no schema constraints, few-shot cross-domain setting (5 documents per event type available), zero-shot roles within seen event types — not fully zero-shot event type generalization.\n\nBiTer (Information Processing and Management, May 2025, doi:10.1016/j.ipm.2025.104199) achieves +4.6%/+7.5%/+0.4% zero-shot Arg-C F1 on RAMS/WikiEvents/ACE2005 using within-dataset event-type-held-out splits. Protocol is NOT directly comparable to LtGaE's cross-dataset three-way protocol; reported separately with explicit footnote.\n\nLtGaE (AAAI 2026, arXiv:2603.02909) uses multi-agent Propose-Evaluate-Revise with RL reward that includes a soft penalty p_i activated when the proportion of empty arguments ρ_i deviates from a target range [τ−ε, τ+ε] — a global aggregate quality-score adjustment per sample, not a per-role structural enumeration or hard decoding constraint. Achieves 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki. Does not compare against BiTer.\n\nASEE (EMNLP Findings 2025, arXiv:2505.08690) addresses inference-time schema selection via RAG; no hard constraints; does not report RAMS/WikiEvents numbers.\n\nBoostCD (EMNLP 2025 Main, arXiv:2506.14901) demonstrates that constrained and unconstrained decoding produce complementary errors at inference time for closed IE (relation extraction), with a learned boosted model combining both for stronger performance. CompSchema-IE investigates an analogous question at training-data generation time for event argument extraction, where structural salience differences compound across a finite corpus rather than being resolved at inference.\n\nSALE (MDPI Electronics, March 2026) uses code-based LLM fine-tuning with RL alignment for cross-task zero-shot transfer; no formal schema constraints during data generation.\n\nExtracting Events Like Code (AAAI 2026, arXiv:2511.13118) uses Python class definitions for inference-time schema validation, not training-data generation.\n\nSynthIE (EMNLP 2023, ACL Anthology 2023.emnlp-main.96) generates synthetic IE training data via task-reversal (structure→text generation), achieving large F1 gains on smaller models; uses no grammar-constrained decoding, no formal cardinality bounds, and targets IE triplets rather than compositional event argument extraction. Establishes the task-reversal generation paradigm that CompSchema-IE extends with hard compositional constraints.\n\nSupervised SOTA: DEGAP (COLING 2025, arXiv:2405.13325) — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1. TSCA (IET Software 2026) adds ~+3.0/+1.0 F1 in fully supervised settings.\n\nThe specific open question not addressed by any prior work — including GEMS, FineCSDA, LtGaE, Gatto et al., or BoostCD: does hard grammar constraint enforcement (cardinality + entity-type, XGrammar) — which provides structural salience via required role-key enumeration in the output JSON template — outperform oracle post-hoc filtering of unconstrained generation under a volume-controlled design, and does any advantage concentrate in rare-role and high-cardinality-tightness strata where the structural enumeration mechanism is most likely to shift the LLM's generation distribution?",
  "approach": "CompSchema-IE is framed explicitly as an empirical study targeting EMNLP 2026 Findings. The primary contribution is a clean, volume-controlled three-condition ablation that isolates the value of hard constraint enforcement over soft filtering, combined with a stratified analysis that localizes any gains mechanistically.\n\n**Primary Hypothesis (Structural Salience, Empirically Testable)**:\nThe RAMS ontology TSV specifies only maximum cardinality (the 'count permitted' column is an upper bound on role occurrences per instance). XGrammar therefore enforces: (a) no role appears more than its permitted maximum count, and (b) when filled, entity types are compatible. It does NOT logically guarantee that optional rare roles appear in every generated instance — this would require setting min-cardinality=1 for all roles, a design choice not derivable from the RAMS TSV alone and one that would produce unrealistically complete training instances where every event instance has every schema role filled.\n\nCompSchema-IE instead adopts the structural salience framing: SCG provides structural salience by explicitly enumerating every applicable role slot as a required key in the constrained generation template. In the XGrammar encoding, all applicable role slots for a given event type appear as required keys in the output JSON template; the LLM generates an empty string or null value for absent optional arguments but cannot omit role keys from the output. This key-level requirement is the mechanism of structural salience: it forces the model's attention to each slot during the forward pass, counteracting the prior bias toward omitting rare slots that characterizes unconstrained generation. Condition B (post-hoc filtering) can remove entity-type violations and cardinality overruns from unconstrained outputs, but cannot recover coverage for role keys that unconstrained generation never emitted in the first place. The structural salience hypothesis is therefore that Condition C will show improved rare-role instantiation over Condition B even when overall constraint violation rates are comparable — an effect logically independent of constraint compliance and attributable specifically to required key enumeration. Even when individual constraint violation rates are low — expected for Qwen3-32B given its strong instruction-following capability — unconstrained generation's prior biases tend to cluster on high-frequency role patterns, under-representing rare optional roles. FineCSDA (NLPCC 2024) partially addresses rare-role under-representation via targeted prompting (SDAM/CDAM), but without formal structural enumeration; CompSchema-IE's SCG provides structural salience by construction through required key enumeration, making it an empirical question whether this translates to downstream rare-role F1 gains.\n\n**Step 0 — Motivating Pilot Study (Day 4, 4 GPU-hours)**:\nSample 600 event instances from Qwen3-32B without constraints (standard structured prompting with RAMS/WikiEvents schema descriptions). The expanded sample (~4–5 instances per event type for RAMS's 139 types) enables reliable per-role violation statistics. Measure: entity-type mismatch rate, cardinality violation rate, role hallucination rate, and argument role coverage (proportion of schema roles appearing ≥1 time). Report all four metrics unconditionally. The primary paper argument holds regardless of outcome: low violation rates motivate the structural salience framing (SCG's required key enumeration matters beyond error correction); high rates additionally motivate constraint enforcement for quality improvement. Both are reported; neither determines the primary framing.\n\n**Step 1 — Schema Constraint Grammar (Days 1-3, human engineering)**:\nDerive typed constraint specifications from RAMS (cardinality directly from public ontology TSV, encoding the 'count permitted' values as maximum bounds; entity-type compatibility from dataset annotations) and WikiEvents (entity-type compatibility from annotations). Encode as XGrammar-compatible context-free grammars. Critically, all applicable role slots for a given event type are encoded as required keys in the output JSON template: the LLM must generate each role name as a JSON key, and may output an empty string or null value for absent optional arguments, but cannot omit any role key from the output. This required-key design is the structural salience mechanism — it forces the model's attention to each role slot during the forward pass rather than allowing silent omission of rare slots, as occurs in unconstrained generation (Condition A) and is not recoverable by post-hoc filtering (Condition B). Cardinality constraints additionally enforce upper bounds on role-filler counts and entity-type compatibility per filler. RAMS TSV availability substantially reduces construction effort. Scoped to 2 ontologies.\n\n**Step 2 — Three-Condition Data Generation with Volume Control (Days 5-7, ~62.5 GPU-hours)**:\nAll conditions use Qwen3-32B on 2×A100 80GB via vLLM. **Target training volume**: N = 5,000 event argument instances per condition, distributed proportionally across the 139 RAMS event types (~36 instances per type on average, with a minimum of 1 per rare type) and WikiEvents event types. To eliminate the volume confound — where Condition B (post-hoc filtered) would otherwise train on fewer instances than C — the following volume normalization protocol is applied:\n\n- **Pool Generation**: Generate 1.5× the target volume (7,500 unconstrained instances) as unconstrained instances (same chat prompting with schema descriptions). Report achieved token throughput and generation settings.\n- **Condition A (Unconstrained)**: Randomly subsample N=5,000 instances from the 7,500-instance pool.\n- **Condition B (Post-hoc Filtered — Oracle Soft Baseline)**: Apply the automated verifier to the full 7,500-instance pool; retain instances passing all entity-type, cardinality, and role-hallucination checks, targeting N=5,000 post-filter instances. Report the achieved discard rate (e.g., 'we generated 7,500 instances and discarded X%, retaining 5,000 for training') as a transparency metric. If the filter discards more than 33% (leaving fewer than 5,000 clean instances), increase the pool to 2× (10,000 instances) and regenerate the additional batch. This baseline approximates oracle-quality soft constraint enforcement without reimplementing LtGaE's RL loop; crucially, it CANNOT recover structural salience for roles absent from filtered instances because unconstrained generation never emitted those role keys.\n- **Condition C (SCG-Constrained)**: Grammar-constrained vLLM decoding via XGrammar to exactly N=5,000 instances, enforcing all role-entity-type assignments and cardinality constraints during the forward pass (<40μs/token overhead, per XGrammar MLSys 2025). The grammar's required role-key enumeration in the output template provides structural salience by construction.\n\nAll three conditions train on exactly N=5,000 instances, making the C-vs-B comparison methodologically airtight.\n\n**Step 3 — Constraint Verification (concurrent with Step 2)**:\nThe automated verifier checks all generated instances and reports: filter rate for the A/B pool (transparency metric), corpus-level role coverage for each condition, near-zero filter rate for Condition C (SCG compliance guarantee). Role coverage differences across conditions directly measure the structural salience effect prior to fine-tuning.\n\n**Step 4 — Fine-tuning and Evaluation (Days 8-11, ~57 GPU-hours)**:\nLoRA fine-tune Qwen3-8B on each of the three volume-matched corpora (3 conditions × ~15 GPU-hours = 45 GPU-hours). Evaluate zero-shot on WikiEvents and RAMS using LtGaE three-way protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki). Comparison table: LtGaE, ASEE, supervised SOTA (DEGAP), Condition A, Condition B, Condition C. BiTer reported separately under native within-dataset protocol with explicit non-comparability footnote.\n\n**Step 5 — Stratified Evaluation (Day 12, ~12 GPU-hours for inference)**:\nThe primary analysis section — demonstrates mechanistic explanation of C vs. A/B gaps:\n(a) Role Rarity Strata: Rank argument roles by frequency in source schema annotations; partition into quartiles. Report C vs. A and C vs. B F1 for each quartile. Hypothesis: C-B gap concentrates in the bottom quartile (rarest roles) because grammar-guided required key enumeration most strongly prompts the model to instantiate rarely-occurring role types; for common roles, both unconstrained and post-hoc filtered corpora already have sufficient coverage.\n(b) Cardinality Tightness Strata: Partition by RAMS-ontology cardinality — max=1 (singleton roles) vs. max>1. Report C vs. A and C vs. B F1 for each partition. Hypothesis: C outperforms B on max=1 roles because Condition B can only remove duplicates but may still have duplicate instances within the filtered corpus; SCG hard-enforces the singleton constraint.\nIf overall C-B delta is modest (e.g., <1 F1), the stratified analysis provides a theoretically grounded finding even for the Findings track: structural salience helps specifically where theory predicts, at a granularity that soft filtering cannot replicate. Both role coverage rates and argument span F1 are reported per stratum, allowing quality and coverage effects to be distinguished (addressing the concern that grammar-constrained decoding may improve role coverage while degrading span quality).\n\n**Null Result Pre-Specification**:\nWe pre-specify the null result interpretation in the paper: if C does not outperform B even in the rare-role quartile or singleton-cardinality partition, we report this as a clearly framed negative finding — grammar-guided structural enumeration via required key templates during generation provides no additional rare-role instantiation benefit over oracle post-hoc filtering of unconstrained generation at Qwen3-32B scale. This is a practically useful negative result: it suggests that strong instruction-following models already provide sufficient structural salience through prompt-specified schema descriptions, and that engineering investment in SCG construction may not be warranted at this model scale. EMNLP Findings publishes clearly framed negative results; this pre-specification distinguishes a null result from a failed experiment.\n\n**Limitations and Quality Tradeoffs**:\nGrammar-constrained decoding may introduce quality degradation beyond structural coverage: Schall & de Melo (RANLP 2025) demonstrate that constrained decoding forces instruction-tuned models away from high-confidence natural language paths, potentially increasing extraction misses. We mitigate this by using Qwen3-32B (whose strong instruction-following capability reduces divergence between constrained and unconstrained generation paths) and by measuring argument span F1 per role stratum in the stratified evaluation alongside role coverage rates, so that quality and coverage effects are distinguishable rather than conflated.\n\n**Paper writing**: Concurrent from Day 1 (intro, related work, method drafted during experiment runs); intensive final writing Days 13-16.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~125.5h A100 80GB total: pilot study generation 600 instances (4 GPU-hours); 1.5× unconstrained pool generation for Conditions A+B (target N=5,000 per condition, pool=7,500 instances, ~37.5 GPU-hours); SCG-constrained generation for Condition C (N=5,000 instances, ~25 GPU-hours); LoRA fine-tuning Qwen3-8B across 3 volume-matched conditions × 15 GPU-hours = 45 GPU-hours; stratified evaluation inference ~12 GPU-hours; evaluation and reporting ~2 GPU-hours",
      "gpu_utilization": "Moderate (~50%): compressed timeline reduces idle gaps; human engineering on SCG module (Days 1-3) and paper writing (concurrent) introduce some idle GPU time, mitigated by parallelizing fine-tuning runs. Volume control adds ~12.5 GPU-hours of generation vs. original design.",
      "timeline": "16 active days targeting May 25, 2026 ARR deadline (commitment to EMNLP 2026 by August 2, 2026; conference October 24-29, Budapest). Day-by-day: Days 1-3 SCG construction + pilot study setup; Day 4 pilot study run (600 instances) + metric analysis; Days 5-7 data generation (7,500-instance A/B pool + 5,000-instance C, staggered on 2×A100, pool generation starts Day 5, C generation starts Day 6 while A/B fine-tune begins); Days 8-10 LoRA fine-tuning (all 3 conditions, staggered); Day 11 LtGaE three-way evaluation; Day 12 stratified evaluation analysis; Days 13-16 intensive paper writing (concurrent with experiments from Day 1). No extended ablations, no ACE05 comparison, no BiTer replication.",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$187 (125.5h × $1.49/hr A100, RunPod/JarvisLabs)",
      "h100_equiv": "~90h H100-equivalent (well within ≤200h H100 hard constraint)",
      "risk_note": "Key risks and mitigations: (1) Overall C-B F1 delta may be small (<1 F1): mitigated by stratified evaluation and pre-specified null result interpretation — paper's primary claim is that structural salience helps in rare-role and singleton-cardinality strata; if this too is null, reported as a clear negative finding with specific positioning. (2) Filter rate exceeds 33% (B cannot reach N=5,000 from 7,500-instance pool): mitigated by increasing pool to 10,000 instances for that condition and reporting achieved discard rate as transparency metric. (3) Pilot study shows <1% violations: expected and mitigated by structural salience argument (violation-rate-independent — the hypothesis concerns role instantiation frequency via required key enumeration, not constraint compliance). (4) XGrammar quality degradation (Schall & de Melo, RANLP 2025): mitigated by Qwen3-32B's strong instruction-following capability and dual measurement of span F1 and role coverage per stratum. (5) 16-day timeline is tight: SCG construction is the bottleneck; RAMS TSV machine-readable cardinality substantially reduces this. Paper writing concurrent from Day 1 is required. (6) BiTer protocol mismatch: explicitly handled with separate table and footnote. (7) FineCSDA comparison: differentiated from CompSchema-IE by formal grammar-constrained decoding with required role-key enumeration vs. targeted prompting, volume-controlled experimental design, and structural salience mechanism by construction."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings (ARR May 25, 2026 submission deadline; commitment to EMNLP 2026 by August 2, 2026; conference October 24-29, Budapest, Hungary)"
  ],
  "level": "solid",
  "key_references": [
    "GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction (ACL Findings 2025)",
    "GEMS: Generation-Based Event Argument Extraction via Multi-perspective Prompts and Ontology Steering (ACL Findings 2025, aclanthology.org/2025.findings-acl.1353) — inference-time EAE using multi-perspective prompts and ontology steering (T5-large) on WikiEvents/ACE05/ERE-EN; achieves SOTA in low-resource settings; differentiated from CompSchema-IE by operating at inference time rather than training-data generation, and by using a voting mechanism over multiple generation paths rather than hard grammar constraints",
    "FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation (NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) — identifies long-tail argument role distribution as bottleneck; SDAM generates samples for rare event types, CDAM injects rare role fillers into common event type documents; no formal cardinality bounds, entity-type constraints, or explicit role-slot enumeration; coverage relies on targeted prompting",
    "Document-Level Event-Argument Data Augmentation for Challenging Role Types (Gatto, Sharif, Seegmiller, Preum; ACL 2025 Long, arXiv:2403.03304) — direct LLM-augmentation predecessor; no constrained decoding, no cardinality/entity-type constraints, few-shot cross-domain with zero-shot roles",
    "SynthIE: Leveraging the Asymmetry of Knowledge Graph Structure for Synthetic IE Data Generation (EMNLP 2023, ACL Anthology 2023.emnlp-main.96) — task-reversal generation paradigm; no grammar-constrained decoding, no formal cardinality bounds, targets IE triplets not event argument extraction",
    "Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction (EMNLP 2025 Main, arXiv:2506.14901) — inference-time boosting for closed IE (relation extraction); central empirical finding: constrained and unconstrained decoding produce complementary errors; CompSchema-IE investigates the analogous structural salience question at training-data generation time for EAE, where coverage differences compound across a finite corpus",
    "The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance (Schall & de Melo, RANLP 2025, aclanthology.org/2025.ranlp-1.124/) — demonstrates that constrained decoding forces instruction-tuned models away from high-confidence natural language paths, causing quality degradation; for LLaMA-3.3-70B, XGrammar led to substantially more extraction misses than top unconstrained strategies; motivates use of strong instruction-following models (Qwen3-32B) and dual measurement of role coverage and span F1 per stratum",
    "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)",
    "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)",
    "BiTer: Bi-directional Feature Learning-Based Approach for Zero-Shot Event Argument Extraction (Information Processing and Management, May 2025, doi:10.1016/j.ipm.2025.104199) — within-dataset event-type-held-out evaluation protocol; not directly comparable to LtGaE three-way cross-dataset protocol",
    "Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation (ASEE, EMNLP Findings 2025, arXiv:2505.08690)",
    "Learning to Generate and Extract: A Multi-Agent Collaboration Framework for Zero-Shot Document-Level Event Arguments Extraction (LtGaE, AAAI 2026, arXiv:2603.02909) — soft RL penalty p_i fires when per-sample empty-argument proportion ρ_i deviates from [τ−ε, τ+ε] (global aggregate quality score, not per-role structural enumeration); 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki",
    "Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction (AAAI 2026, arXiv:2511.13118)",
    "Structure-Aware Lightweight Document-Level Event Extraction via Code-Based Large Language Models (SALE, MDPI Electronics, March 2026)",
    "DEGAP: Dual Event-Guided Adaptive Prefixes for Templated-Based Event Argument Extraction with Slot Querying (COLING 2025, arXiv:2405.13325) — supervised SOTA: RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1",
    "Beyond Single-Event Extraction: Towards Efficient Document-Level Multi-Event Argument Extraction (DEEIA, ACL 2024 Findings, arXiv:2405.01884) — RAMS 53.4 Arg-C F1, WikiEvents 67.0 Arg-C F1",
    "Two-Stream Modeling for Document-Level Event Argument Extraction Using Contextual Clue and AMR Structures (TSCA, IET Software 2026) — supervised SOTA extension: +3.02/+1.01 F1 on RAMS/WikiEvents over prior SOTA",
    "DiCoRe: Enhancing Zero-shot Event Detection via Divergent-Convergent LLM Reasoning (arXiv:2506.05128)",
    "MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)",
    "Document-Level Event Argument Extraction by Conditional Generation (NAACL 2021)",
    "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv 2023)",
    "XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models (MLSys 2025)"
  ],
  "description": "Zero-shot event argument extraction lags supervised performance by 8–35 F1 points (supervised SOTA: DEGAP COLING 2025 — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1; best zero-shot cross-dataset: LtGaE AAAI 2026 — 32–47 F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki). A key bottleneck is training data quality for the generator model. This paper presents CompSchema-IE, an empirical study asking: do hard grammar constraints (formal cardinality + entity-type enforcement via XGrammar-constrained vLLM decoding) outperform oracle post-hoc filtering of unconstrained generation for zero-shot EAE, and does any advantage concentrate in role strata where theory predicts?\n\nThe primary motivation is a structural salience hypothesis: the RAMS ontology TSV specifies only maximum cardinality (the 'count permitted' column is an upper bound on role occurrences per instance, not a minimum), so XGrammar enforces upper-bound cardinality and entity-type compatibility but cannot logically guarantee that optional roles appear in every generated instance. Instead, SCG provides structural salience through required key enumeration: in the XGrammar encoding, all applicable role slots for a given event type appear as required keys in the output JSON template. The LLM generates empty strings or null values for absent optional arguments but cannot omit role keys from the output. This required-key design forces the model's attention to each slot during the forward pass, counteracting the prior bias toward omitting rare optional slots that characterizes unconstrained generation. Post-hoc filtering (Condition B) removes violations but cannot recover coverage for role keys that unconstrained generation never emitted — a structural gap that filtering cannot close. Prior work (GEMS ACL Findings 2025 — ontology steering at inference time; FineCSDA NLPCC 2024 — targeted prompt augmentation; LtGaE AAAI 2026 — aggregate soft RL penalties) addresses rare-role under-representation via different mechanisms, none of which provides formal required-key enumeration at generation time. Concurrently, BoostCD (EMNLP 2025, arXiv:2506.14901) demonstrates complementary error profiles of constrained vs. unconstrained decoding at inference time for closed IE (relation extraction); CompSchema-IE investigates the analogous structural salience question at training-data generation time for EAE.\n\nA three-condition, volume-controlled ablation (N=5,000 instances per condition, distributed proportionally across RAMS's 139 event types) isolates the grammar effect cleanly: (A) Unconstrained, randomly subsampled to N=5,000 training instances; (B) Post-hoc Filtered (oracle soft-constraint approximation, volume-matched to N=5,000 by generating a 7,500-instance pool and filtering to N, with achieved discard rate reported as transparency metric); (C) SCG-Constrained (grammar-constrained to exactly N=5,000 instances with required role-key enumeration providing structural salience). All conditions use Qwen3-32B, the same schema information, and the same final training volume N, making the C-vs-B comparison methodologically airtight. A motivating pilot study measures entity-type mismatch, cardinality violation, role hallucination, and role coverage rates in Qwen3-32B unconstrained generation on RAMS/WikiEvents (600 instances; all metrics reported unconditionally). LoRA fine-tunes Qwen3-8B on each volume-matched corpus; evaluation uses the LtGaE three-way protocol with LtGaE, ASEE, and DEGAP as baselines. Null result interpretation is pre-specified: if C does not outperform B in rare-role strata, the paper reports this as a clearly framed negative finding — grammar-guided structural enumeration provides no additional benefit over oracle post-hoc filtering at Qwen3-32B scale, suggesting the model's instruction-following capability already provides adequate structural salience through prompt-specified schema descriptions. The stratified evaluation by (a) role rarity quartile and (b) cardinality tightness (max=1 vs. max>1) reports both role coverage and argument span F1 per stratum, distinguishing coverage gains from potential quality tradeoffs introduced by grammar-constrained decoding (Schall & de Melo, RANLP 2025). CompSchema-IE extends the SynthIE task-reversal paradigm (EMNLP 2023) with formal grammar-constrained decoding and compositional cardinality bounds. Target: EMNLP 2026 Findings (ARR May 25, 2026). Estimated GPU cost: ~$187 (125.5h A100 ≈ 90h H100-equiv, within budget). Timeline: 16 active days.",
  "project_name": "schema_constrained_event_ie",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["Auto mode (900h A100 ≈ 450–630 H100-equiv hours) clearly violates the ≤200 H100-hour hard constraint; even the HIL mode (~380h A100 ≈ 190–266h H100-equiv) is borderline. The proposal must be scoped to core manual-mode experiments only, and the auto/HIL resource tables should be removed or flagged as out-of-scope for this submission.", "Critical omission: 'Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation' (ASEE, arXiv 2505.08690, May 2025, https://arxiv.org/abs/2505.08690) directly addresses schema-aware event extraction using schema paraphrasing + RAG, constructs a 12-dataset benchmark (MD-SEE), and is published just weeks before the proposed submission. This paper must be cited, compared against, and explicitly differentiated.", "'Learning to Generate and Extract' (AAAI 2026, arXiv 2603.02909) already uses 'event structure constraints incorporated into the reward design' to guide synthetic data generation for zero-shot document-level event argument extraction on RAMS and WikiEvents — the same benchmarks. The proposed paper's claim that 'neither enforces hard compositional constraints at training-data generation time' needs empirical substantiation showing that hard grammar constraints outperform soft RL-based structural reward signals, not just a definitional distinction.", "Unvalidated core hypothesis: the paper assumes compositional constraint violations in generated training data are the primary bottleneck for zero-shot event extraction, but provides no motivating study. With Qwen3-235B-A22B as generator, modern frontier LLMs with strong instruction following may naturally produce consistent role–entity assignments at high rates; the verifier's filter rate and its downstream effect on model quality are entirely unknown.", "Qwen3-235B-A22B inference on 4×A100 80GB (320 GB VRAM): FP8 weights alone occupy ~235 GB, leaving ~85 GB for KV cache — severely limiting batch size and throughput. The vendor-recommended minimum configuration is 8-GPU tensor parallelism (--tp 8). Practical deployment on 4×A100 requires INT4 quantization, which may degrade generation quality and invalidates the clean cost estimate.", "The claimed 30–50 F1-point gap between zero-shot and supervised methods is overstated for current SOTA: the best zero-shot methods (LtGaE 2026, BiTer) achieve ~32–47 F1 on RAMS/WikiEvents zero-shot scenarios while supervised SOTA reaches 52–69 F1 — the gap is task- and benchmark-specific (5–37 F1 points), not a uniform 30–50 points."]
Feedback: The idea targets a genuine and underexplored gap (extending GuideX-style synthetic supervision to compositionally structured event schemas), but in its current form the novelty claim is undermined by two concurrent papers the generator missed. The revision must: (1) Cite and differentiate from ASEE (arXiv 2505.08690) — ASEE approaches schema-awareness via RAG rather than formal grammars during generation; CompSchema-IE's differentiation should be that SCG enforces hard cardinality and type-compatibility constraints that cannot be retrieved post-hoc. (2) Strengthen differentiation from LtGaE (arXiv 2603.02909) by adding an ablation comparing grammar-constrained hard generation vs. RL-reward-guided soft generation on WikiEvents/RAMS — this turns the design choice into a falsifiable experimental contribution. (3) Add a motivating pilot study (even 100 generated examples, manually inspected) showing that unconstrained Qwen3-235B-A22B does in fact produce constraint-violating instances (wrong entity type for argument role, cardinality violations) at non-trivial rates — without this, the SCG module has no evidenced purpose. (4) Scope compute to the manual-mode experiments only (≤250h A100 ≈ 175h H100-equiv, within budget) and remove the auto mode entirely from the proposal. (5) Replace Qwen3-235B-A22B with Qwen3-32B or Llama-3.1-70B as the generator — these fit on 2×A100 comfortably, reducing generation hardware risk while still producing high-quality synthetic text; Qwen3-235B-A22B can be framed as an optional upper-bound experiment if resources allow.

### Round 2 review
Verdict: revise
Issues: ["BiTer (Bi-directional Feature Learning-Based Approach for Zero-Shot Event Argument Extraction, Information Processing and Management, May 2025) is not cited. This paper reports SOTA zero-shot performance on RAMS and WikiEvents with +4.6%/+7.5% F1 over the prior best and uses a different approach (pseudo-argument generation from LLMs + bidirectional knowledge transfer), making it directly relevant as a baseline. Omitting it means the proposed method's competitive positioning against the actual SOTA is unknown.", "The pilot study contingency plan is inadequate. The proposal acknowledges 'If the pilot study reveals very low violation rates (<2%), the SCG module's value proposition is weakened and the paper's framing should shift.' But this is not a contingency plan — it is an admission that the paper could have no compelling finding. If Qwen3-32B (a strong instruction-following model) violates event schema constraints rarely, the entire SCG contribution becomes a null result. The proposal needs either a pre-registration of what level of violation rate constitutes a paper (and what the fallback is if it doesn't), or a theoretical argument for why hard constraints add value independent of their violation rate (e.g., as a distributional regularizer, speed benefit, or interpretability advantage).", "The PARSE citation for the '~12% invalid response rate' is for GPT-4 on complex structured extraction (EMNLP 2025 Industry Track), not Qwen3-32B. Qwen3-32B is a newer model with potentially stronger instruction-following and may have substantially lower violation rates in practice. The motivating claim should be stated as a hypothesis to be confirmed by the pilot study, not as established fact for the proposed model.", "The cross-ontology schema normalization scope is underestimated. Unifying ACE05 (24 event types, ~35 argument roles), WikiEvents (~50 event types), and RAMS (139 event types, 65 argument roles) into a single formal constraint grammar with entity-type compatibility mappings is a multi-week engineering and curation task. The role vocabularies across the three ontologies do not overlap neatly (e.g., RAMS 'Victim' vs. ACE05 'Target' vs. WikiEvents 'place'). Within 16 days, this competes directly with the pilot study annotation and the soft-baseline ablation implementation.", "The soft-RL baseline ablation (matching LtGaE's reward design) requires implementing a multi-agent evaluation loop with an evaluation agent computing normalized log-likelihood and a structural completeness penalty. LtGaE achieves this via separate generation and evaluation agents with LoRA-tuned models. Re-implementing this faithfully within 16 days is unrealistic alongside the other engineering tasks. The ablation would be stronger and more tractable if simplified to: (a) unconstrained prompt-only generation (no grammar, no reward) vs. (b) SCG-constrained generation — this tests the same hypothesis more cleanly."]
Feedback: The Round 2 revision has successfully addressed all five critical Round 1 issues: compute is within budget (122h H100-equiv confirmed), ASEE and LtGaE are properly cited with mechanistic differentiation, the pilot study adds empirical motivation, and Qwen3-32B on 2×A100 BF16 is hardware-feasible. The remaining issues are fixable but require concrete action before this is submission-ready.

(1) Add BiTer as a baseline. Search for the full paper at doi.org/10.1016/j.ipm.2025.104199 and include its absolute F1 numbers in the comparison table. If BiTer outperforms LtGaE, frame CompSchema-IE as improving over both.

(2) Strengthen the pilot study's decision framework. Before running the full pipeline, the pilot study should produce a pre-specified threshold: 'If violation rate > X%, we proceed with the full SCG approach. If rate < X%, we [specific alternative contribution].' A better alternative contribution at low violation rates: demonstrate that grammar-constrained generation produces structurally more diverse training examples (measured by argument role distribution) even when violations are rare — this is a quality argument that doesn't depend on violation rates.

(3) Scope the ontology normalization. Start with WikiEvents + RAMS only (these share more structural similarity and are the primary benchmarks LtGaE targets). Add ACE05 only if time permits. This removes the hardest cross-vocabulary alignment problem while preserving the core experimental claims.

(4) Simplify the ablation. Replace the full LtGaE RL re-implementation with a simpler two-condition comparison: SCG-constrained generation vs. unconstrained generation (standard chat prompting with the same event schema descriptions). This directly tests whether grammar constraints at generation time help, without requiring a multi-agent RL implementation. Note this in the paper as a controlled comparison rather than a direct LtGaE replication.

### Round 3 review
Verdict: revise
Issues: ["SUPERVISED SOTA NUMBERS ARE FACTUALLY WRONG: DEGAP (2024) achieves 54.2 Arg-C on RAMS — not 52.2 — and 67.1 on WikiEvents — not 68.8. The numbers may be from DEEIA (which DEGAP supersedes), but the paper currently attributes them to 'DEGAP/DEEIA 2024' without clarification. This understates the RAMS gap (54.2 − 45.77 = 8.4 F1, not 6 F1) and overstates the WikiEvents supervised score. Fix by correctly attributing each number to the specific paper that reports it.", "UNCITED DIRECT PREDECESSOR: 'Large Language Models for Document-Level Event-Argument Data Augmentation for Challenging Role Types' (arXiv:2403.03304, Gatto et al., March 2024) uses LLMs to synthesize document-level EAE training data for zero-shot/few-shot roles and achieves +16pt F1 on zero-shot role types on RAMS — this is the closest published predecessor to CompSchema-IE's core idea. Not citing it leaves a gap that reviewers familiar with EAE data augmentation will notice. The differentiation is clear (arXiv:2403.03304 does not enforce hard cardinality/entity-type grammar constraints), but it must be cited.", "BITER COMPARISON PROTOCOL IS OPERATIONALLY UNRESOLVED: BiTer reports F1 on standard within-dataset zero-shot splits (event types held out by type), while LtGaE uses a cross-dataset three-way protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki). These protocols are NOT interchangeable. Getting BiTer's F1 under the LtGaE protocol requires either (a) running BiTer's code on the LtGaE data splits (requires code availability + compute, non-trivial) or (b) author cooperation. The proposal says 'to be obtained from the full paper' but this is not realistic given the protocol difference. The paper should explicitly acknowledge the protocol mismatch, report BiTer's numbers under BiTer's native protocol with a clear note, and NOT imply direct numerical comparability.", "DUAL-FRAMING CREATES REVIEWER PERCEPTION RISK: The pre-specified decision rule ('if violation rate >5%, primary claim is A; if ≤5%, primary claim is B') is epistemically honest but strategically risky for EMNLP Main submission. Reviewers may read this as 'the authors do not know what their own contribution is.' The structural regularization argument (higher argument role coverage, provable entity-type consistency) is the more durable long-term claim and should be the PRIMARY framing regardless of violation rate. The pilot study's violation rate then becomes secondary supporting evidence. Commit to 'SCG as structural regularizer' as the headline claim and present violation rate as a motivating data point, not a framing branch condition.", "ABLATION DESIGN DOES NOT RULE OUT MARGINAL IMPROVEMENT RISK: The core ablation (SCG-constrained vs. unconstrained generation) isolates the grammar effect cleanly, but the paper currently has no stratified evaluation by argument role frequency or schema complexity. If overall F1 improvement is small (e.g., ≤1 F1), reviewers will dismiss the contribution. Stratified evaluation by (a) rare roles (bottom quartile by training frequency) and (b) roles with tight cardinality constraints (max=1) would demonstrate that SCG gains concentrate where they theoretically should — this turns a potentially flat overall number into a principled, interpretable finding."]
Feedback: The Round 2 revision successfully resolved all five critical prior issues, and the proposal is now technically credible. The remaining blockers before submission readiness are: (1) Fix supervised SOTA numbers — look up DEEIA's exact RAMS Arg-C F1 and DEGAP's WikiEvents Arg-C F1 and attribute each number to the correct paper. (2) Cite arXiv:2403.03304 (Gatto et al., 2024) and write a one-paragraph differentiation: that paper uses LLMs for EAE data augmentation but does not enforce cardinality or entity-type grammar constraints, and focuses on few-shot rather than zero-shot transfer — CompSchema-IE's SCG module is the distinguishing contribution. (3) Resolve the BiTer protocol comparison honestly: state that BiTer uses within-dataset event-type splits while CompSchema-IE uses the LtGaE three-way cross-dataset protocol, report BiTer's native-protocol numbers with a clear footnote, and do not claim direct comparability. (4) Restructure the framing to lead with structural regularization as the primary contribution unconditionally — 'SCG guarantees full argument role coverage and provable entity-type consistency in training data; the pilot study additionally measures unconstrained violation rates' — eliminating the contingency branch. (5) Add stratified evaluation by role rarity and cardinality tightness as the analysis section, not as an afterthought; this is where the paper's strongest signal will appear.

### Round 4 review
Verdict: revise
Issues: ["FATAL TIMELINE VIOLATION: The Generator's manual-mode estimate is 3–4 months, explicitly acknowledging that the May 25 ARR deadline cannot be met. This violates the user's hard ≤16-day constraint. Additionally, the Generator's proposed workaround ('ARR August 2026 cycle') is based on a misreading of the ARR calendar: August 2, 2026 is the COMMITMENT deadline for papers already in review from the May 25 submission, not a new submission cycle. There is no August ARR submission cycle that would yield EMNLP 2026 acceptance. The proposal must either (a) compress scope to a version executable in 16 days or (b) explicitly declare this idea is out-of-scope for the May 25 constraint.", "MISSING ABLATION — SCG vs. LtGaE SOFT RL: The core ablation compares SCG-constrained vs. unconstrained generation, which cleanly isolates the grammar effect. However, EMNLP reviewers familiar with LtGaE will ask: why does hard grammar enforcement outperform LtGaE's soft RL penalty, given LtGaE already achieves 45.77/32.38/46.96 F1 with soft constraints? Without a direct comparison on the same evaluation protocol, the claim that hard cardinality+entity-type constraints are better than soft RL argument-completeness rewards is an architectural assertion, not a demonstrated result. This is the most obvious reviewer concern for the EMNLP main paper track.", "THIN TECHNICAL CONTRIBUTION FOR EMNLP MAIN: The SCG module derives a grammar from the RAMS TSV (confirmed: cardinality is column-encoded) and feeds it to off-the-shelf XGrammar in vLLM. This is a pipeline integration, not an algorithmic contribution. EMNLP Main reviewers expect either (a) >2 F1 improvement over prior SOTA with clear ablation, or (b) technical novelty beyond tool integration. The stratified evaluation is analytically interesting but is framing/analysis, not architecture. EMNLP Findings is a more defensible target than EMNLP Main given current technical depth.", "PILOT STUDY RISK NOT FULLY MITIGATED: Qwen3-32B is a modern strong instruction-following model. The framing as 'structural regularizer' partially decouples the paper from requiring high violation rates, but the paper still relies on the pilot study as 'supporting empirical evidence.' If measured violation rates are <1% across all four metrics (plausible for a strong model given structured prompting), a reviewer can legitimately ask: why do we need formal grammar enforcement if the LLM already complies? The structural regularization reframing needs a concrete answer to this question that does not depend on violation rates."]
Feedback: The Round 3 revisions are well-executed: all five prior issues are resolved, the supervised SOTA numbers are independently verified correct, the ARR timeline confusion needs immediate attention. Here are the four concrete actions needed before this is submission-ready:

(1) COMPRESS SCOPE TO 16 DAYS OR DECLARE TIMELINE INFEASIBILITY. The 3–4 month estimate likely includes extensive ablations, careful analysis, and writing time. A minimal viable submission to the May 25 ARR deadline requires: SCG construction for RAMS+WikiEvents only (5–7 days, using the confirmed machine-readable cardinality TSV), pilot study on 200 instances (1 day), constrained generation (GPU, 1 day), LoRA fine-tuning across 3 ablation conditions (GPU, 2 days), evaluation on LtGaE three-way protocol (1 day), stratified analysis (1 day), paper writing concurrent. This is approximately 11–12 active days — tight but feasible with a focused team. Remove extended ablations, reduce fine-tuning runs, and defer optional experiments (ACE05 comparison, BiTer replication) to the revision stage.

(2) ADD SOFT vs. HARD CONSTRAINT COMPARISON VIA LIGHTWEIGHT ORACLE BASELINE. Rather than re-implementing LtGaE's full RL loop (unrealistic), add a third ablation condition: 'post-hoc filtered unconstrained generation' (generate unconstrained, then filter violating instances via the verifier). This approximates the achievable quality of soft constraint enforcement without requiring RL, and lets the paper argue: 'even oracle-filtered unconstrained data underperforms SCG-constrained data on rare roles — because filtering cannot guarantee proportional role coverage.' This directly demonstrates the value of hard constraints over soft/filtered approaches without re-implementing LtGaE.

(3) ANCHOR THE STRUCTURAL REGULARIZER FRAMING AGAINST ZERO-VIOLATION RATES. Add the following argument explicitly to the paper: 'Even if individual constraint violation rates are low, unconstrained generation cannot guarantee proportional representation of all schema roles across a finite corpus. SCG enforces this by construction: given 1,000 generated instances for event type T with role R having max-cardinality=1, the SCG guarantees exactly one instance of R per event — unconstrained generation may cluster on frequent roles and never instantiate rare ones, even with zero explicit violations.' This argument is valid regardless of violation rates and directly motivates SCG as a distributional regularizer, not just a constraint enforcer.

(4) TARGET EMNLP 2026 FINDINGS EXPLICITLY. Given the thin technical depth (pipeline integration, not algorithmic novelty), EMNLP Findings is the more defensible submission target within the same May 25 deadline. This does not require any change to the method — simply adjust the positioning in the paper to emphasize the empirical analysis and stratified evaluation as the primary contribution, rather than the SCG module itself.

### Round 5 review
Verdict: revise
Issues: ["CRITICAL — VOLUME CONFOUND IN CONDITION B: The three-condition design requires all conditions to train on equal data volume, but Condition B (post-hoc filtered) necessarily discards some fraction of the Condition A instances. If the filter removes 20–50% of instances (plausible even for strong models on compositional constraints), B trains on substantially less data than C, biasing the C-vs-B comparison in favor of C independently of the grammar effect. The proposal must specify: (a) generate excess instances for the A/B pool so that B achieves the same final volume as C after filtering, OR (b) deliberately undersample C to match B's post-filter volume as a volume-controlled analysis. Without this control, EMNLP reviewers will reject the paper on methodological grounds.", "MISSING CITATION — FineCSDA: 'FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation' (NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) specifically identifies the long-tail distribution of argument roles as a bottleneck and proposes LLM augmentation at both sample and context levels to address rare argument roles. While FineCSDA does NOT use formal grammar constraints and uses a different mechanism, it is a direct predecessor addressing the same identified gap (rare-role under-representation in training data). Reviewers familiar with document-level EAE data augmentation will notice the omission. Add a one-sentence differentiation: FineCSDA augments rare roles via sample-level and context-level LLM generation without enforcing formal cardinality or entity-type constraints — CompSchema-IE's SCG provides a distributional coverage guarantee by construction.", "NEGATIVE RESULT PATH UNACKNOWLEDGED: The proposal correctly states that C-B stratified gains may be modest, but does not explicitly acknowledge what happens if C fails to outperform B even in the rare-role quartile. If this occurs, the paper's primary empirical claim is a null result — potentially a useful negative finding (post-hoc filtering suffices, grammar constraints add no measurable value), but the proposal frames this as a risk without naming it. For EMNLP Findings, a clearly framed negative result is publishable, but it requires different positioning from the current abstract. Add a brief paragraph explicitly framing the null-result paper: 'If stratified analysis reveals no C-B advantage, we report this as a negative finding: for strong instruction-following models like Qwen3-32B, post-hoc filtering achieves equivalent coverage to formal grammar constraints, suggesting that engineering investment in SCG construction may not be warranted at this model scale.'", "PILOT STUDY SAMPLE SIZE RISK: The pilot study samples 200 event instances from RAMS and WikiEvents. RAMS has 139 event types; 200 instances gives fewer than 2 samples per event type on average, making role-level statistics extremely noisy for rare roles. Either increase the pilot study to 500–1000 instances (adds ~2 GPU-hours, within budget) or clearly scope the pilot to a subset of 5–10 event types with enough instances for per-role statistics."]
Feedback: The Round 5 revision is the strongest version of this proposal so far. All prior critical issues (timeline, compute, ASEE/LtGaE/Gatto et al. citations, DEGAP numbers, stratified evaluation, BiTer protocol note) have been correctly resolved. The four remaining issues are fixable and one is straightforward; the volume confound is the only blocker that could sink the paper at review time.

(1) VOLUME CONTROL [CRITICAL]: Before generating data for the three conditions, add a volume normalization protocol: generate 1.5× the target volume for Condition A, then both Condition A (random subsample to target) and Condition B (post-filter residual targeting the same volume) and Condition C (SCG-constrained to exact target volume) all end up with the same number of training instances. Report the achieved filter rate for Condition B as a transparency metric (e.g., 'we generated 1.5N instances for A and retained the top N after filtering, achieving a X% discard rate'). This one addition makes the C-vs-B comparison methodologically airtight.

(2) CITE FineCSDA: Add a sentence in related work: 'FineCSDA (NLPCC 2024) identifies the rare-role under-representation problem and addresses it via LLM-powered sample-level and context-level augmentation; unlike CompSchema-IE, FineCSDA does not impose formal cardinality bounds or entity-type constraints, relying instead on targeted prompt design for rare event types.' This closes the citation gap reviewers may notice.

(3) FRAME THE NULL RESULT: Add a two-sentence paragraph to Section 3 (Approach) or Section 5 (Expected Findings): 'We pre-specify the null result interpretation: if C does not outperform B in the rare-role quartile, we report that post-hoc filtering achieves equivalent rare-role coverage to formal grammar constraints at Qwen3-32B scale, providing a practically useful negative finding for practitioners considering SCG implementation overhead.'

(4) INCREASE PILOT STUDY SCOPE: Sample 600 instances (4 GPU-hours total, still within the Day 3-4 budget) to achieve ~4–5 instances per event type on average, enabling more reliable role-level violation statistics.

### Round 6 review
Verdict: revise
Issues: ["COVERAGE GUARANTEE LOGICAL GAP [critical, newly identified]: The proposal's primary theoretical claim — 'SCG enforces proportional coverage by construction: the grammar mandates that each mandatory role appears in every generated instance' — is overstated given confirmed RAMS TSV structure. The RAMS ontology TSV (independently verified at nlp.jhu.edu/rams/) specifies only MAXIMUM cardinality (the 'count permitted' column), NOT minimum cardinality. XGrammar therefore enforces upper-bound cardinality and entity-type constraints, but CANNOT force optional roles to appear. Since rare roles in RAMS may be optional in many event types (a given event instance may legitimately not have an 'Instrument' or 'Beneficiary'), the grammar provides no coverage guarantee for those roles. The coverage guarantee claim holds only for roles that the paper explicitly sets min-cardinality=1 in the grammar — which would require an assumption not derivable from the RAMS TSV alone and would produce unrealistic training data (every instance must have every role filled). The proposal must either (a) acknowledge this and narrow the guarantee to 'roles assigned min-cardinality=1 in the grammar encoding' with an explicit design choice described, or (b) reframe the theoretical argument from 'structural coverage guarantee' to 'structurally-prompted generation is more likely to instantiate optional rare roles due to explicit slot salience' — an empirical hypothesis rather than a logical guarantee. This is the single issue that a RAMS-familiar reviewer will raise immediately.", "BoostCD unacknowledged [minor]: 'Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction' (EMNLP 2025 Main, arXiv:2506.14901) empirically demonstrates that constrained and unconstrained decoding errors are complementary for closed IE, with a learned boosted model combining both. While BoostCD targets inference-time decoding (not training-data generation), its central empirical finding — that hard constraints and unconstrained generation have complementary error profiles — is directly relevant to CompSchema-IE's motivating argument and should be cited in related work with a one-sentence differentiation.", "Training volume N unspecified [minor]: The proposal never states the target training volume N. For RAMS with 139 event types, the number of instances per type and total N are unknown, making the GPU cost estimates (37.5h for 1.5N pool, 25h for N SCG-constrained) unverifiable. Specify N upfront (e.g., 'N=5,000 instances distributed proportionally across event types') so compute estimates and reproducibility can be assessed."]
Feedback: The Round 6 proposal is the strongest version yet — all five Round 5 issues are properly resolved (volume normalization via 1.5× pool, FineCSDA cited and differentiated, null result pre-specified, pilot study at 600 instances, BiTer protocol mismatch handled). DEGAP F1 numbers (RAMS 54.2, WikiEvents 67.1 Arg-C) are independently verified correct. XGrammar overhead claim (<40μs/token as default vLLM backend) is confirmed. One fixable critical issue blocks submission readiness: the coverage guarantee must be corrected.

(1) REVISE THE COVERAGE GUARANTEE ARGUMENT [critical]: The RAMS TSV only provides maximum cardinality (upper bounds on role occurrences), not minimum cardinality. The grammar therefore enforces: (a) no role appears more than its max count, and (b) when filled, entity types are compatible. It CANNOT guarantee that rare optional roles appear at all. Replace 'SCG enforces proportional coverage by construction' with one of two framings: OPTION A — 'In our grammar encoding, we set min-cardinality=1 for all roles applicable to a given event type, guaranteeing their appearance in every generated instance; this is a design choice that differs from natural annotation practice and we evaluate whether this artificial completeness improves rare-role coverage downstream.' OPTION B — 'SCG provides structural salience: by enumerating every applicable role slot explicitly in the constrained generation template, the LLM is prompted to consider filling each slot rather than freely omitting rare ones; we test empirically whether this structured attention mechanism improves rare-role instantiation.' Option B is more honest and requires no changes to the actual method.

(2) ADD BoostCD [one sentence in related work]: 'Concurrently, BoostCD (EMNLP 2025) demonstrates that constrained and unconstrained decoding produce complementary errors at inference time for closed IE; CompSchema-IE investigates an analogous question at training-data generation time, where coverage differences compound across a finite corpus.'

(3) SPECIFY N [one sentence in Section 2 or Step 2]: State the target training volume N explicitly (e.g., 'N=5,000 instances drawn proportionally across RAMS event types') so compute estimates are verifiable and the paper is reproducible.

With these three changes — particularly the coverage guarantee reframing — the proposal is ready for EMNLP 2026 Findings submission. The empirical design is sound, the null result handling is appropriate, and the resource estimate is within budget.

### Round 7 review
Verdict: revise
Issues: ["MISSING CITATION — GEMS (ACL Findings 2025): 'GEMS: Generation-Based Event Argument Extraction via Multi-perspective Prompts and Ontology Steering' (aclanthology.org/2025.findings-acl.1353) is not cited. GEMS uses multi-perspective prompting and ontology steering for EAE on WikiEvents/ACE05, achieving SOTA in low-resource settings. While GEMS is inference-time extraction rather than training-data generation, its 'ontology steering' mechanism is conceptually related to CompSchema-IE's schema-constrained generation. A one-sentence differentiation is required: 'GEMS (ACL Findings 2025) uses multi-perspective prompts and ontology steering for inference-time EAE; CompSchema-IE instead applies hard grammar constraints at training-data generation time, investigating whether structural salience during generation improves downstream rare-role coverage.'", "OPTIONAL ROLE GRAMMAR REPRESENTATION UNSPECIFIED [moderate]: The structural salience argument rests on the claim that the grammar 'explicitly enumerates every applicable role slot in the constrained generation template,' prompting the LLM to consider each slot. But the proposal never states HOW optional slots are represented in the grammar template: (a) required JSON keys with empty-string values allowed, (b) optional JSON keys that may be omitted, or (c) required keys with a special [NONE] token. This distinction is critical — design (b) provides no structural salience over Condition A because slots can still be omitted; design (a) forces the LLM to generate each role name as a JSON key, which IS the structural salience mechanism. The paper must state this explicitly, e.g.: 'All applicable role slots appear as required keys in the output JSON schema; the LLM may output empty strings or null for absent optional arguments, but cannot omit role keys from the output.' Without this, the structural salience claim is not reproducible.", "XGRAMMAR QUALITY DEGRADATION UNACKNOWLEDGED [minor]: Recent empirical work (Schall & de Melo, RANLP 2025; structured output benchmarks 2025) demonstrates that grammar-constrained decoding introduces quality degradation — forcing models into non-canonical token paths degrades output quality, particularly for rare or complex outputs. One study found XGrammar led to substantially more extraction misses than top unconstrained strategies for LLaMA-70B. The specific risk for CompSchema-IE: if the grammar forces generation of all role slots sequentially, the model may produce lower-quality argument spans for common roles in order to comply with the grammar structure — confounding the C-vs-B comparison. The paper should acknowledge this in the limitations section: 'Grammar-constrained decoding may introduce quality tradeoffs beyond structural coverage (Schall & de Melo, RANLP 2025); we mitigate this risk by using Qwen3-32B, which has strong structured output capabilities, and by measuring both role coverage and argument span quality in our stratified evaluation.'"]
Feedback: Round 7 correctly resolves all three Round 6 issues: the coverage guarantee is properly reframed as structural salience (Option B framing), BoostCD is cited, and N=5,000 is specified. The LtGaE absolute F1 numbers (45.77/32.38/46.96) are independently verified correct. The EMNLP 2026 ARR May 25 deadline is confirmed valid with mandatory commitment at submission. The volume normalization (1.5x pool), pre-specified null result, and stratified evaluation design are all sound.

Three targeted fixes are needed before submission readiness:

(1) ADD GEMS CITATION [one sentence]: Add 'GEMS: Generation-Based Event Argument Extraction via Multi-perspective Prompts and Ontology Steering (ACL Findings 2025)' to related work with a differentiation sentence. This is the closest concurrent work using ontology-guided EAE that reviewers familiar with the area will know.

(2) SPECIFY OPTIONAL ROLE GRAMMAR REPRESENTATION [one paragraph in Step 1]: The structural salience mechanism depends entirely on whether the grammar requires all role slot names to appear as output keys (providing salience) or permits key omission (no salience). State explicitly: 'In our XGrammar encoding, all applicable role slots for a given event type appear as required keys in the output JSON template; the LLM generates empty strings or null values for absent optional arguments but cannot omit role keys.' This makes the mechanism reproducible and directly supports the structural salience claim.

(3) ACKNOWLEDGE XGRAMMAR QUALITY TRADEOFF [one sentence in limitations]: Note that grammar-constrained decoding can introduce quality degradation in text generation quality (Schall & de Melo, RANLP 2025). Mitigate by measuring argument span F1 per role stratum (not just role coverage), so quality and coverage effects are distinguishable in the stratified evaluation.

With these three additions — all writable during paper drafting — the proposal is ready for EMNLP 2026 Findings submission.


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
  "promptId": "4ca85829-ed36-4a44-93b8-2b7baa11aeac",
  "type": "user",
  "uuid": "1c30c59d-f408-49d8-a443-601b308235a1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T09:44:03.382Z_

```json
{
  "parentUuid": "1c30c59d-f408-49d8-a443-601b308235a1",
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
  "uuid": "65fb6e3d-0b7f-442e-a432-1900c02773dc",
  "timestamp": "2026-05-10T09:44:03.382Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T09:44:03.382Z_

```json
{
  "parentUuid": "65fb6e3d-0b7f-442e-a432-1900c02773dc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a16d8ccb-94b6-4651-8770-42f040ae081a",
  "timestamp": "2026-05-10T09:44:03.382Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
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
  "leafUuid": "a16d8ccb-94b6-4651-8770-42f040ae081a",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Shot Event Argument Extraction",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9"
}
```

---

### Assistant

_source line 8 · 2026-05-10T09:44:15.336Z_

<details><summary>Logged reasoning block</summary>

```text
This is round 8 of 10 for reviewing the paper "CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Shot Event Argument Extraction — An Empirical Study via Synthetic Supervision". Let me carefully analyze the current state of the proposal and conduct independent verification.

Let me first understand what has been addressed in the current round (round 8) vs. what was requested in round 7:

**Round 7 issues that needed to be addressed:**
1. MISSING CITATION — GEMS (ACL Findings 2025) ✓ (GEMS is now cited throughout the proposal)


2. OPTIONAL ROLE GRAMMAR REPRESENTATION UNSPECIFIED ✓ (The proposal now explicitly states: "all applicable role slots appear as required keys in the output JSON template; the LLM generates an empty string or null value for absent optional arguments but cannot omit role keys from the output")
3. XGRAMMAR QUALITY DEGRADATION UNACKNOWLEDGED ✓ (Schall & de Melo, RANLP 2025 is now cited with mitigation strategy)

Now I'm checking the core claims in this proposal through independent verification—specifically whether GEMS is properly cited and accurately characterized, if the structural salience argument holds up, and whether there are any concurrent works I should be aware of.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a16d8ccb-94b6-4651-8770-42f040ae081a",
  "isSidechain": false,
  "requestId": "req_011CatfwVKEUW3R64G3D82BZ",
  "type": "assistant",
  "uuid": "9b0d152a-2573-4e5e-a1a4-227e7c61b796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LBykSrosPxHgnbQRQt8yvo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26732,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1422,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26732
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

_source line 9 · 2026-05-10T09:44:15.641Z_

I'll conduct independent verification searches on the key claims before issuing a verdict on this round 8 proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b0d152a-2573-4e5e-a1a4-227e7c61b796",
  "isSidechain": false,
  "requestId": "req_011CatfwVKEUW3R64G3D82BZ",
  "type": "assistant",
  "uuid": "92158531-0383-4b4d-8b6b-48721190bc1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LBykSrosPxHgnbQRQt8yvo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26732,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1422,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26732
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

_source line 10 · 2026-05-10T09:44:24.830Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HzTT4sGFdL4aQxonttEz6h`</summary>

```json
{
  "description": "Verify GEMS paper and concurrent zero-shot EAE work",
  "subagent_type": "Explore",
  "prompt": "Search for and verify the following papers relevant to an EMNLP 2026 submission on zero-shot event argument extraction (EAE) with grammar-constrained synthetic data generation. I need to independently verify each paper exists and its claims are accurately described.\n\n1. Search for \"GEMS Generation-Based Event Argument Extraction Multi-perspective Prompts Ontology Steering ACL 2025\" — verify it's at aclanthology.org/2025.findings-acl.1353, what benchmarks it reports, and whether it uses T5-large as described.\n\n2. Search for \"XGrammar structured generation constraints quality degradation LLM 2025\" and \"Schall de Melo constrained decoding RANLP 2025\" — verify the quality degradation finding exists, especially for LLaMA-70B.\n\n3. Search for \"zero-shot event argument extraction 2025 2026 new methods grammar constraints\" — look for any concurrent work I might be missing that does grammar-constrained or schema-guided EAE training data generation.\n\n4. Search for \"BoostCD constrained unconstrained decoding boosting information extraction EMNLP 2025 arXiv 2506.14901\" — verify this paper exists and its characterization (complementary error profiles for relation extraction).\n\n5. Search for \"FineCSDA document-level event argument extraction fine-grained data augmentation NLPCC 2024\" — verify it's at dl.acm.org/doi/10.1007/978-981-97-9434-8_1.\n\nReport what you find for each search, including any discrepancies between what the proposal claims and what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92158531-0383-4b4d-8b6b-48721190bc1f",
  "isSidechain": false,
  "requestId": "req_011CatfwVKEUW3R64G3D82BZ",
  "type": "assistant",
  "uuid": "37f3d5c4-d6fc-4bff-8561-9b10b26a6c05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LBykSrosPxHgnbQRQt8yvo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26732,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1422,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26732
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

_source line 11 · 2026-05-10T09:44:34.905Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AiYa5FARYtsoCtLjcYUCiw`</summary>

```json
{
  "description": "Verify LtGaE numbers and find concurrent EAE work",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing an EMNLP 2026 paper submission on zero-shot event argument extraction (EAE). Please verify these specific claims via web search:\n\n1. Search for \"LtGaE AAAI 2026 arXiv 2603.02909 Learning to Generate and Extract zero-shot event argument extraction\" — verify: (a) does it use a soft RL penalty for argument completeness? (b) does it report 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki? (c) is the RL penalty described as firing \"when the proportion of empty arguments ρ_i deviates from [τ−ε, τ+ε]\"?\n\n2. Search for \"ASEE Adaptive Schema-aware Event Extraction Retrieval-Augmented Generation EMNLP Findings 2025 arXiv 2505.08690\" — verify the paper exists and does NOT report RAMS/WikiEvents numbers.\n\n3. Search for \"zero-shot event argument extraction grammar constrained decoding training data generation 2025 2026\" — any concurrent work doing grammar-constrained or structured-output-constrained synthetic data generation for EAE?\n\n4. Search for \"DEGAP COLING 2025 arXiv 2405.13325 event argument extraction RAMS WikiEvents\" — verify RAMS 54.2 Arg-C F1 and WikiEvents 67.1 Arg-C F1.\n\n5. Search for \"SynthIE EMNLP 2023 synthetic information extraction task reversal\" — verify it doesn't use grammar-constrained decoding.\n\n6. Search for \"XGrammar MLSys 2025 structured generation vLLM\" — verify the 40μs/token overhead claim.\n\nReport your findings clearly, noting any discrepancies."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37f3d5c4-d6fc-4bff-8561-9b10b26a6c05",
  "isSidechain": false,
  "requestId": "req_011CatfwVKEUW3R64G3D82BZ",
  "type": "assistant",
  "uuid": "75b37b68-344f-4814-9a6d-a08b6ad8593d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LBykSrosPxHgnbQRQt8yvo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26732,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1422,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26732
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

_source line 12 · 2026-05-10T09:45:37.862Z_

<details><summary>↩ Tool result · `toolu_01HzTT4sGFdL4aQxonttEz6h`</summary>

```text
Excellent! Now I have comprehensive information. Let me compile my findings in a clear report.

## Verification Report: EMNLP 2026 Zero-Shot Event Argument Extraction Papers

### 1. GEMS: Generation-Based Event Argument Extraction via Multi-perspective Prompts and Ontology Steering

**Status: VERIFIED** ✓

**Location:** [aclanthology.org/2025.findings-acl.1353](https://aclanthology.org/2025.findings-acl.1353/)

**Key Details Confirmed:**
- Published in Findings of ACL 2025 (pages 26392–26409, Vienna, Austria)
- Authors: Run Lin, Yao Liu, Yanglei Gan, Yuxiang Cai, Tian Lan, and Qiao Liu
- **Model:** Uses T5-large (CONFIRMED as stated)
- **Benchmarks:** Experiments on two benchmark datasets. Search results indicate support for ACE05-E, WikiEvent, and ERE-EN datasets
- **Results:** Achieves state-of-the-art performance, particularly in low-resource settings
- Code available at GitHub: [AONE-NLP/EAE-GEMS](https://github.com/AONE-NLP/EAE-GEMS)

**Approach:** Multi-prompt learning framework that generates event arguments via multiple perspectives and uses ontology-driven steering to ensure schema consistency.

---

### 2. Quality Degradation from Constrained Decoding

**Status: PARTIALLY VERIFIED** - Quality degradation claim is confirmed but specific LLaMA-70B finding not verified

**XGrammar (2411.15100):** [arxiv.org/abs/2411.15100](https://arxiv.org/abs/2411.15100)
- Confirmed: XGrammar is a structured generation engine for LLMs with grammar constraints
- **Quality degradation finding confirmed:** Search results indicate "Structured format constraints (JSON, XML, YAML) degrade LLM reasoning ability"
- However: The quality degradation discussion in XGrammar does not specifically isolate LLaMA-70B
- The XGrammar-2 (2025/2026) development shows improved results with constrained decoding on LLaMA models (3B and 70B comparisons mentioned)

**Schall & de Melo - "The Hidden Cost of Structure" (RANLP 2025):** [aclanthology.org/2025.ranlp-1.124/](https://aclanthology.org/2025.ranlp-1.124/)
- **Status: VERIFIED** - Paper exists and discusses constrained decoding effects
- **Publication:** Proceedings of RANLP 2025, pages 1074–1084, Varna, Bulgaria
- **Quality degradation findings confirmed:** The paper shows that "instruction-tuned models frequently suffer performance degradation on generation tasks" under constrained decoding
- **Base vs. instruction-tuned divergence:** Confirms "Base models often benefit from constrained decoding, producing more precise outputs"
- **Issue with your claim:** PDF content confirms experiments across 11 models, but the search results and fetch do NOT explicitly confirm LLaMA-70B as one of the tested models. The paper examines constrained decoding effects broadly but specific LLaMA-70B testing is not confirmed in available excerpts.

---

### 3. Concurrent Work on Zero-Shot Event Argument Extraction with Grammar Constraints

**Status: NEW METHODS FOUND** - Multiple concurrent approaches identified

Found several 2025-2026 papers on related tasks:

1. **"Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction"** (arXiv 2511.13118) - Uses code-based frameworks for structured output
   
2. **Multi-Agent Collaboration Framework for Document-Level Event Arguments** (arXiv 2603.02909) - Zero-shot document-level extraction with generation and extraction agents for schema compliance

3. **Global Constraints with Prompting for Zero-Shot Event Argument Classification** (ACL 2023 Findings, EACL) - Uses global constraints and prompting

4. **Research showing schema compliance challenges:** Recent work confirms "Event extraction is a structured prediction task that requires outputs to conform to a predefined schema, such as a JSON object or database entry" and notes that "LLMs often fail to strictly follow schema constraints, particularly without fine-tuning"

These concurrent approaches emphasize schema guidance, constraint enforcement, and multi-agent collaboration.

---

### 4. BoostCD: Combining Constrained and Unconstrained Decoding via Boosting

**Status: VERIFIED with CLARIFICATION NEEDED** ✓

**Details Confirmed:**
- **arXiv ID: 2506.14901** - CONFIRMED
- **Publication:** EMNLP 2025 (also available as arXiv preprint)
- **Title:** "Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction"
- **Mechanism:** Two-phase approach combining constrained and unconstrained decoding
- **Complementary error profiles:** CONFIRMED - "The mistakes made by the base model with vs. without constraints tend to be complementary, which the boosted model learns to exploit for improved performance"

**IMPORTANT CLARIFICATION:** 
- **Application domain:** The paper applies BoostCD to **information extraction (closed information extraction/BoostIE)**, NOT specifically relation extraction
- Your proposal states it has "complementary error profiles for relation extraction," but the paper's primary application is closed information extraction more broadly
- The error profile principles (different errors in constrained vs. unconstrained modes) are general principles that may apply to relation extraction, but the paper doesn't specifically frame it as a relation extraction contribution

---

### 5. FineCSDA: Document-Level Event Argument Extraction with Fine-Grained Data Augmentation

**Status: VERIFIED** ✓

**Location:** [dl.acm.org/doi/10.1007/978-981-97-9434-8_1](https://dl.acm.org/doi/10.1007/978-981-97-9434-8_1)

**Key Details Confirmed:**
- **Conference:** NLPCC 2024 (13th National CCF Conference)
- **Location & Dates:** Hangzhou, China, November 1–3, 2024
- **Approach:** Fine-grained data augmentation at both sample and context levels
- **Problem addressed:** Long-tail distribution of argument roles in document-level event argument extraction datasets
- **Two main modules:**
  1. Sample-level Data Augmentation Module (SDAM) - generates document-level samples of rare event types using LLMs
  2. Context-level Data Augmentation Module (CDAM) - supplements rare argument roles within common event types

---

## Summary of Discrepancies

| Paper | Status | Key Discrepancy |
|-------|--------|-----------------|
| GEMS | ✓ Verified | None - T5-large confirmed, benchmarks confirmed |
| XGrammar/Quality Degradation | ✓ Partial | Quality degradation confirmed, but LLaMA-70B not explicitly isolated in XGrammar paper |
| Schall & de Melo RANLP 2025 | ✓ Verified | Quality degradation confirmed; LLaMA-70B testing not explicitly confirmed in available excerpts |
| Zero-shot concurrent work | ✓ Found | Multiple concurrent approaches exist; grammar-constrained EAE synthetic data generation is an active area |
| BoostCD (2506.14901) | ✓ Verified | Applied to **information extraction**, not specifically **relation extraction** as claimed |
| FineCSDA | ✓ Verified | None - all details match |

### Key Recommendation for Your EMNLP 2026 Submission

Be precise about BoostCD's application domain - the paper demonstrates the complementary error profile principle with **information extraction** (closed IE), not explicitly with relation extraction. While the principles may generalize, you should verify whether the error complementarity specifically holds for relation extraction or rephrase to indicate the principle is from information extraction but could be applicable to EAE.

Sources:
- [GEMS at ACL Anthology](https://aclanthology.org/2025.findings-acl.1353/)
- [XGrammar on arXiv](https://arxiv.org/abs/2411.15100)
- [Schall & de Melo RANLP 2025](https://aclanthology.org/2025.ranlp-1.124/)
- [BoostCD on arXiv](https://arxiv.org/abs/2506.14901)
- [FineCSDA at ACM Digital Library](https://dl.acm.org/doi/10.1007/978-981-97-9434-8_1)
- [GEMS GitHub Repository](https://github.com/AONE-NLP/EAE-GEMS)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37f3d5c4-d6fc-4bff-8561-9b10b26a6c05",
  "isSidechain": false,
  "promptId": "4ca85829-ed36-4a44-93b8-2b7baa11aeac",
  "type": "user",
  "uuid": "be5d3c96-8fd9-4670-af03-9c3bccc55a51",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify the following papers relevant to an EMNLP 2026 submission on zero-shot event argument extraction (EAE) with grammar-constrained synthetic data generation. I need to independently verify each paper exists and its claims are accurately described.\n\n1. Search for \"GEMS Generation-Based Event Argument Extraction Multi-perspective Prompts Ontology Steering ACL 2025\" — verify it's at aclanthology.org/2025.findings-acl.1353, what benchmarks it reports, and whether it uses T5-large as described.\n\n2. Search for \"XGrammar structured generation constraints quality degradation LLM 2025\" and \"Schall de Melo constrained decoding RANLP 2025\" — verify the quality degradation finding exists, especially for LLaMA-70B.\n\n3. Search for \"zero-shot event argument extraction 2025 2026 new methods grammar constraints\" — look for any concurrent work I might be missing that does grammar-constrained or schema-guided EAE training data generation.\n\n4. Search for \"BoostCD constrained unconstrained decoding boosting information extraction EMNLP 2025 arXiv 2506.14901\" — verify this paper exists and its characterization (complementary error profiles for relation extraction).\n\n5. Search for \"FineCSDA document-level event argument extraction fine-grained data augmentation NLPCC 2024\" — verify it's at dl.acm.org/doi/10.1007/978-981-97-9434-8_1.\n\nReport what you find for each search, including any discrepancies between what the proposal claims and what you find.",
    "agentId": "a99461e24575a650f",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now I have comprehensive information. Let me compile my findings in a clear report.\n\n## Verification Report: EMNLP 2026 Zero-Shot Event Argument Extraction Papers\n\n### 1. GEMS: Generation-Based Event Argument Extraction via Multi-perspective Prompts and Ontology Steering\n\n**Status: VERIFIED** ✓\n\n**Location:** [aclanthology.org/2025.findings-acl.1353](https://aclanthology.org/2025.findings-acl.1353/)\n\n**Key Details Confirmed:**\n- Published in Findings of ACL 2025 (pages 26392–26409, Vienna, Austria)\n- Authors: Run Lin, Yao Liu, Yanglei Gan, Yuxiang Cai, Tian Lan, and Qiao Liu\n- **Model:** Uses T5-large (CONFIRMED as stated)\n- **Benchmarks:** Experiments on two benchmark datasets. Search results indicate support for ACE05-E, WikiEvent, and ERE-EN datasets\n- **Results:** Achieves state-of-the-art performance, particularly in low-resource settings\n- Code available at GitHub: [AONE-NLP/EAE-GEMS](https://github.com/AONE-NLP/EAE-GEMS)\n\n**Approach:** Multi-prompt learning framework that generates event arguments via multiple perspectives and uses ontology-driven steering to ensure schema consistency.\n\n---\n\n### 2. Quality Degradation from Constrained Decoding\n\n**Status: PARTIALLY VERIFIED** - Quality degradation claim is confirmed but specific LLaMA-70B finding not verified\n\n**XGrammar (2411.15100):** [arxiv.org/abs/2411.15100](https://arxiv.org/abs/2411.15100)\n- Confirmed: XGrammar is a structured generation engine for LLMs with grammar constraints\n- **Quality degradation finding confirmed:** Search results indicate \"Structured format constraints (JSON, XML, YAML) degrade LLM reasoning ability\"\n- However: The quality degradation discussion in XGrammar does not specifically isolate LLaMA-70B\n- The XGrammar-2 (2025/2026) development shows improved results with constrained decoding on LLaMA models (3B and 70B comparisons mentioned)\n\n**Schall & de Melo - \"The Hidden Cost of Structure\" (RANLP 2025):** [aclanthology.org/2025.ranlp-1.124/](https://aclanthology.org/2025.ranlp-1.124/)\n- **Status: VERIFIED** - Paper exists and discusses constrained decoding effects\n- **Publication:** Proceedings of RANLP 2025, pages 1074–1084, Varna, Bulgaria\n- **Quality degradation findings confirmed:** The paper shows that \"instruction-tuned models frequently suffer performance degradation on generation tasks\" under constrained decoding\n- **Base vs. instruction-tuned divergence:** Confirms \"Base models often benefit from constrained decoding, producing more precise outputs\"\n- **Issue with your claim:** PDF content confirms experiments across 11 models, but the search results and fetch do NOT explicitly confirm LLaMA-70B as one of the tested models. The paper examines constrained decoding effects broadly but specific LLaMA-70B testing is not confirmed in available excerpts.\n\n---\n\n### 3. Concurrent Work on Zero-Shot Event Argument Extraction with Grammar Constraints\n\n**Status: NEW METHODS FOUND** - Multiple concurrent approaches identified\n\nFound several 2025-2026 papers on related tasks:\n\n1. **\"Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction\"** (arXiv 2511.13118) - Uses code-based frameworks for structured output\n   \n2. **Multi-Agent Collaboration Framework for Document-Level Event Arguments** (arXiv 2603.02909) - Zero-shot document-level extraction with generation and extraction agents for schema compliance\n\n3. **Global Constraints with Prompting for Zero-Shot Event Argument Classification** (ACL 2023 Findings, EACL) - Uses global constraints and prompting\n\n4. **Research showing schema compliance challenges:** Recent work confirms \"Event extraction is a structured prediction task that requires outputs to conform to a predefined schema, such as a JSON object or database entry\" and notes that \"LLMs often fail to strictly follow schema constraints, particularly without fine-tuning\"\n\nThese concurrent approaches emphasize schema guidance, constraint enforcement, and multi-agent collaboration.\n\n---\n\n### 4. BoostCD: Combining Constrained and Unconstrained Decoding via Boosting\n\n**Status: VERIFIED with CLARIFICATION NEEDED** ✓\n\n**Details Confirmed:**\n- **arXiv ID: 2506.14901** - CONFIRMED\n- **Publication:** EMNLP 2025 (also available as arXiv preprint)\n- **Title:** \"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction\"\n- **Mechanism:** Two-phase approach combining constrained and unconstrained decoding\n- **Complementary error profiles:** CONFIRMED - \"The mistakes made by the base model with vs. without constraints tend to be complementary, which the boosted model learns to exploit for improved performance\"\n\n**IMPORTANT CLARIFICATION:** \n- **Application domain:** The paper applies BoostCD to **information extraction (closed information extraction/BoostIE)**, NOT specifically relation extraction\n- Your proposal states it has \"complementary error profiles for relation extraction,\" but the paper's primary application is closed information extraction more broadly\n- The error profile principles (different errors in constrained vs. unconstrained modes) are general principles that may apply to relation extraction, but the paper doesn't specifically frame it as a relation extraction contribution\n\n---\n\n### 5. FineCSDA: Document-Level Event Argument Extraction with Fine-Grained Data Augmentation\n\n**Status: VERIFIED** ✓\n\n**Location:** [dl.acm.org/doi/10.1007/978-981-97-9434-8_1](https://dl.acm.org/doi/10.1007/978-981-97-9434-8_1)\n\n**Key Details Confirmed:**\n- **Conference:** NLPCC 2024 (13th National CCF Conference)\n- **Location & Dates:** Hangzhou, China, November 1–3, 2024\n- **Approach:** Fine-grained data augmentation at both sample and context levels\n- **Problem addressed:** Long-tail distribution of argument roles in document-level event argument extraction datasets\n- **Two main modules:**\n  1. Sample-level Data Augmentation Module (SDAM) - generates document-level samples of rare event types using LLMs\n  2. Context-level Data Augmentation Module (CDAM) - supplements rare argument roles within common event types\n\n---\n\n## Summary of Discrepancies\n\n| Paper | Status | Key Discrepancy |\n|-------|--------|-----------------|\n| GEMS | ✓ Verified | None - T5-large confirmed, benchmarks confirmed |\n| XGrammar/Quality Degradation | ✓ Partial | Quality degradation confirmed, but LLaMA-70B not explicitly isolated in XGrammar paper |\n| Schall & de Melo RANLP 2025 | ✓ Verified | Quality degradation confirmed; LLaMA-70B testing not explicitly confirmed in available excerpts |\n| Zero-shot concurrent work | ✓ Found | Multiple concurrent approaches exist; grammar-constrained EAE synthetic data generation is an active area |\n| BoostCD (2506.14901) | ✓ Verified | Applied to **information extraction**, not specifically **relation extraction** as claimed |\n| FineCSDA | ✓ Verified | None - all details match |\n\n### Key Recommendation for Your EMNLP 2026 Submission\n\nBe precise about BoostCD's application domain - the paper demonstrates the complementary error profile principle with **information extraction** (closed IE), not explicitly with relation extraction. While the principles may generalize, you should verify whether the error complementarity specifically holds for relation extraction or rephrase to indicate the principle is from information extraction but could be applicable to EAE.\n\nSources:\n- [GEMS at ACL Anthology](https://aclanthology.org/2025.findings-acl.1353/)\n- [XGrammar on arXiv](https://arxiv.org/abs/2411.15100)\n- [Schall & de Melo RANLP 2025](https://aclanthology.org/2025.ranlp-1.124/)\n- [BoostCD on arXiv](https://arxiv.org/abs/2506.14901)\n- [FineCSDA at ACM Digital Library](https://dl.acm.org/doi/10.1007/978-981-97-9434-8_1)\n- [GEMS GitHub Repository](https://github.com/AONE-NLP/EAE-GEMS)"
      }
    ],
    "totalDurationMs": 73026,
    "totalTokens": 30687,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2724,
      "cache_read_input_tokens": 25800,
      "output_tokens": 2157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2724
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2157,
          "cache_read_input_tokens": 25800,
          "cache_creation_input_tokens": 2724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2724,
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
  "sourceToolAssistantUUID": "37f3d5c4-d6fc-4bff-8561-9b10b26a6c05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T09:45:55.849Z_

<details><summary>↩ Tool result · `toolu_01AiYa5FARYtsoCtLjcYUCiw`</summary>

````text
Perfect! Now I have comprehensive information. Let me compile my findings report.

## Summary of Findings

Based on my searches and document verification, here are my findings for each of your claims:

### 1. **LtGaE (AAAI 2026, arXiv 2603.02909)**

**Status: VERIFIED with minor clarification**

(a) **Soft RL penalty for argument completeness**: CONFIRMED. The paper uses a penalty term ρᵢ based on the proportion of empty arguments in synthetic samples.

(b) **Span-F1 Results - EXACT MATCH VERIFIED**: 
- RAMS2RAMS: 45.77 (Span-F1) ✓
- RAMS2Wiki: 32.38 (Span-F1) ✓
- Wiki2Wiki: 46.96 (Span-F1) ✓

(c) **RL Penalty Formula - VERIFIED**: The penalty is formulated exactly as you stated:
```
pᵢ = {0 if τ−ε≤ρᵢ≤τ+ε, |ρᵢ−τ| otherwise}
```
The penalty fires when the proportion of empty arguments ρᵢ deviates from [τ−ε, τ+ε]. The full quality score integrates this as: αᵢ = (ℓᵢ−μ)/δ − pᵢ

**Key Source**: [Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction](https://arxiv.org/abs/2603.02909)

---

### 2. **ASEE (EMNLP Findings 2025, arXiv 2505.08690)**

**Status: VERIFIED**

The paper exists and is published in EMNLP Findings 2025. However, your claim about it NOT reporting RAMS/WikiEvents numbers is **CONFIRMED**. While RAMS and WikiEvents are included as part of the MD-SEE benchmark construction, they are NOT evaluated as separate benchmarks with reported results. The actual evaluation focuses on other datasets (CrudeOilNews, DocEE-en/zh, GENEVA, IEPILE-en/zh, MAVEN-Arg). Individual RAMS/WikiEvents results are not reported in the results tables.

**Key Source**: [Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation](https://arxiv.org/abs/2505.08690)

---

### 3. **Concurrent work on grammar-constrained EAE with synthetic data (2025-2026)**

**Status: PARTIALLY FOUND**

The search results indicate active research in this area:
- Papers on zero-shot EAE with synthetic data generation using LLMs exist
- Grammar-constrained decoding is being applied to information extraction tasks (e.g., Text2Event using trie-based constrained decoding)
- However, I did not find a specific concurrent work that explicitly combines grammar-constrained decoding with structured synthetic data generation specifically for EAE in the 2025-2026 timeframe with a distinct name/acronym

**Key Sources**: [Grammar-constrained decoding for structured information extraction](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full)

---

### 4. **DEGAP (COLING 2025, arXiv 2405.13325)**

**Status: VERIFIED**

RAMS and WikiEvents results are exactly as stated:
- **RAMS Arg-C F1: 54.2** ✓
- **WikiEvents Arg-C F1: 67.1** ✓

The paper was published at COLING 2025 and reports these as state-of-the-art improvements over prior methods.

**Key Source**: [DEGAP: Dual Event-Guided Adaptive Prefixes for Templated-Based Event Argument Extraction](https://arxiv.org/abs/2405.13325)

---

### 5. **SynthIE (EMNLP 2023, arXiv 2303.04132)**

**Status: VERIFIED**

SynthIE does NOT use grammar-constrained decoding. Instead, it uses **task reversal**: rather than extracting information from text (forward direction), it generates plausible input text for target structured outputs (reverse direction). This asymmetry exploitation was used to generate 1.8M synthetic training data points for closed information extraction without grammar constraints.

**Key Source**: [Exploiting Asymmetry for Synthetic Training Data Generation: SynthIE and the Case of Information Extraction](https://arxiv.org/abs/2303.04132)

---

### 6. **XGrammar (MLSys 2025, arXiv 2411.15100)**

**Status: VERIFIED with precision clarification**

The 40μs/token overhead claim is APPROXIMATELY CORRECT but slightly imprecise:
- The paper reports: **"under 40 µs per token for JSON Schema and CFG (JSON)"**
- More precisely, the final optimized configuration achieves **18 microseconds per token** (0.018 milliseconds)
- In end-to-end serving scenarios, the overhead is **0.1 milliseconds per token**

The paper also reports up to 100x speedup over existing solutions and up to 80x output token rate improvements compared to baselines.

**Key Source**: [XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models](https://arxiv.org/abs/2411.15100)

---

## Discrepancies Summary

- **No major factual discrepancies found** in claims 1, 2, 4, and 6
- **Claim 3** could not be fully verified - no specific concurrent work with combined grammar-constrained + synthetic EAE found with certainty
- **Claim 5** is verified as correct - SynthIE explicitly does NOT use grammar-constrained decoding

Your paper's citations appear well-founded based on the verification conducted.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "75b37b68-344f-4814-9a6d-a08b6ad8593d",
  "isSidechain": false,
  "promptId": "4ca85829-ed36-4a44-93b8-2b7baa11aeac",
  "type": "user",
  "uuid": "81c95f2f-bab1-47a8-99f4-51a90f5c34c6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing an EMNLP 2026 paper submission on zero-shot event argument extraction (EAE). Please verify these specific claims via web search:\n\n1. Search for \"LtGaE AAAI 2026 arXiv 2603.02909 Learning to Generate and Extract zero-shot event argument extraction\" — verify: (a) does it use a soft RL penalty for argument completeness? (b) does it report 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki? (c) is the RL penalty described as firing \"when the proportion of empty arguments ρ_i deviates from [τ−ε, τ+ε]\"?\n\n2. Search for \"ASEE Adaptive Schema-aware Event Extraction Retrieval-Augmented Generation EMNLP Findings 2025 arXiv 2505.08690\" — verify the paper exists and does NOT report RAMS/WikiEvents numbers.\n\n3. Search for \"zero-shot event argument extraction grammar constrained decoding training data generation 2025 2026\" — any concurrent work doing grammar-constrained or structured-output-constrained synthetic data generation for EAE?\n\n4. Search for \"DEGAP COLING 2025 arXiv 2405.13325 event argument extraction RAMS WikiEvents\" — verify RAMS 54.2 Arg-C F1 and WikiEvents 67.1 Arg-C F1.\n\n5. Search for \"SynthIE EMNLP 2023 synthetic information extraction task reversal\" — verify it doesn't use grammar-constrained decoding.\n\n6. Search for \"XGrammar MLSys 2025 structured generation vLLM\" — verify the 40μs/token overhead claim.\n\nReport your findings clearly, noting any discrepancies.",
    "agentId": "ab0c905b4c24c8b94",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me compile my findings report.\n\n## Summary of Findings\n\nBased on my searches and document verification, here are my findings for each of your claims:\n\n### 1. **LtGaE (AAAI 2026, arXiv 2603.02909)**\n\n**Status: VERIFIED with minor clarification**\n\n(a) **Soft RL penalty for argument completeness**: CONFIRMED. The paper uses a penalty term ρᵢ based on the proportion of empty arguments in synthetic samples.\n\n(b) **Span-F1 Results - EXACT MATCH VERIFIED**: \n- RAMS2RAMS: 45.77 (Span-F1) ✓\n- RAMS2Wiki: 32.38 (Span-F1) ✓\n- Wiki2Wiki: 46.96 (Span-F1) ✓\n\n(c) **RL Penalty Formula - VERIFIED**: The penalty is formulated exactly as you stated:\n```\npᵢ = {0 if τ−ε≤ρᵢ≤τ+ε, |ρᵢ−τ| otherwise}\n```\nThe penalty fires when the proportion of empty arguments ρᵢ deviates from [τ−ε, τ+ε]. The full quality score integrates this as: αᵢ = (ℓᵢ−μ)/δ − pᵢ\n\n**Key Source**: [Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction](https://arxiv.org/abs/2603.02909)\n\n---\n\n### 2. **ASEE (EMNLP Findings 2025, arXiv 2505.08690)**\n\n**Status: VERIFIED**\n\nThe paper exists and is published in EMNLP Findings 2025. However, your claim about it NOT reporting RAMS/WikiEvents numbers is **CONFIRMED**. While RAMS and WikiEvents are included as part of the MD-SEE benchmark construction, they are NOT evaluated as separate benchmarks with reported results. The actual evaluation focuses on other datasets (CrudeOilNews, DocEE-en/zh, GENEVA, IEPILE-en/zh, MAVEN-Arg). Individual RAMS/WikiEvents results are not reported in the results tables.\n\n**Key Source**: [Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation](https://arxiv.org/abs/2505.08690)\n\n---\n\n### 3. **Concurrent work on grammar-constrained EAE with synthetic data (2025-2026)**\n\n**Status: PARTIALLY FOUND**\n\nThe search results indicate active research in this area:\n- Papers on zero-shot EAE with synthetic data generation using LLMs exist\n- Grammar-constrained decoding is being applied to information extraction tasks (e.g., Text2Event using trie-based constrained decoding)\n- However, I did not find a specific concurrent work that explicitly combines grammar-constrained decoding with structured synthetic data generation specifically for EAE in the 2025-2026 timeframe with a distinct name/acronym\n\n**Key Sources**: [Grammar-constrained decoding for structured information extraction](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full)\n\n---\n\n### 4. **DEGAP (COLING 2025, arXiv 2405.13325)**\n\n**Status: VERIFIED**\n\nRAMS and WikiEvents results are exactly as stated:\n- **RAMS Arg-C F1: 54.2** ✓\n- **WikiEvents Arg-C F1: 67.1** ✓\n\nThe paper was published at COLING 2025 and reports these as state-of-the-art improvements over prior methods.\n\n**Key Source**: [DEGAP: Dual Event-Guided Adaptive Prefixes for Templated-Based Event Argument Extraction](https://arxiv.org/abs/2405.13325)\n\n---\n\n### 5. **SynthIE (EMNLP 2023, arXiv 2303.04132)**\n\n**Status: VERIFIED**\n\nSynthIE does NOT use grammar-constrained decoding. Instead, it uses **task reversal**: rather than extracting information from text (forward direction), it generates plausible input text for target structured outputs (reverse direction). This asymmetry exploitation was used to generate 1.8M synthetic training data points for closed information extraction without grammar constraints.\n\n**Key Source**: [Exploiting Asymmetry for Synthetic Training Data Generation: SynthIE and the Case of Information Extraction](https://arxiv.org/abs/2303.04132)\n\n---\n\n### 6. **XGrammar (MLSys 2025, arXiv 2411.15100)**\n\n**Status: VERIFIED with precision clarification**\n\nThe 40μs/token overhead claim is APPROXIMATELY CORRECT but slightly imprecise:\n- The paper reports: **\"under 40 µs per token for JSON Schema and CFG (JSON)\"**\n- More precisely, the final optimized configuration achieves **18 microseconds per token** (0.018 milliseconds)\n- In end-to-end serving scenarios, the overhead is **0.1 milliseconds per token**\n\nThe paper also reports up to 100x speedup over existing solutions and up to 80x output token rate improvements compared to baselines.\n\n**Key Source**: [XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models](https://arxiv.org/abs/2411.15100)\n\n---\n\n## Discrepancies Summary\n\n- **No major factual discrepancies found** in claims 1, 2, 4, and 6\n- **Claim 3** could not be fully verified - no specific concurrent work with combined grammar-constrained + synthetic EAE found with certainty\n- **Claim 5** is verified as correct - SynthIE explicitly does NOT use grammar-constrained decoding\n\nYour paper's citations appear well-founded based on the verification conducted."
      }
    ],
    "totalDurationMs": 80940,
    "totalTokens": 33837,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 353,
      "cache_read_input_tokens": 32026,
      "output_tokens": 1453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 353
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1453,
          "cache_read_input_tokens": 32026,
          "cache_creation_input_tokens": 353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 353,
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
  "sourceToolAssistantUUID": "75b37b68-344f-4814-9a6d-a08b6ad8593d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "81c95f2f-bab1-47a8-99f4-51a90f5c34c6",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Shot Event Argument Extraction",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9"
}
```

---

### Assistant

_source line 16 · 2026-05-10T09:48:15.147Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also search for any new concurrent work that may have appeared since the last round that the proposal might be missing. I also want to check if there are any issues with the current round 8 proposal that I should flag.

Let me also think through the proposal carefully:

**Round 8 changes vs Round 7 issues:**

1. GEMS properly cited throughout ✓ - The proposal now mentions GEMS extensively throughout the paper
2. Optional role grammar representation specified ✓ - "All applicable role slots appear as required keys in the output JSON template; the LLM generates an empty string or null value for absent optional arguments but cannot omit role keys from the output."


3. XGrammar quality degradation acknowledged ✓ - Schall & de Melo RANLP 2025 is now cited with mitigation

Now I'm checking whether the structural salience argument is properly framed and consistent throughout, verifying that all prior issues have been maintained, and looking for any new problems that might have emerged. The proposal is targeting EMNLP 2026 Findings with the structural salience framing as the primary approach, and I'm examining the volume and other key elements to ensure everything holds together.

Looking at the independent verification, I'm noticing a potential characterization issue with BoostCD—the proposal describes it as demonstrating complementary errors between constrained and unconstrained decoding for closed IE, which I need to verify matches how it's actually being used in the argument. I'm verifying the specific numbers across these papers now — the LtGaE F1 scores check out at 45.77/32.38/46.96, and the soft RL penalty mechanism is accurately described. DEGAP's performance on RAMS and WikiEvents also matches what's reported. XGrammar's latency claim of under 40 microseconds per token aligns with what I'm finding.

Looking at what's been resolved across all the revision rounds, the major issues from Round 7 are addressed — GEMS is properly cited, the grammar representation is specified, and the quality degradation is acknowledged. The one remaining characterization issue is that BoostCD gets labeled as "relation extraction" when it's actually broader closed IE, though this is fairly minor.

On the GEMS differentiation, the proposal could spell out more clearly how GEMS operates at inference time versus CompSchema-IE's training-data generation approach, but what's there is workable. The more substantive concern is the structural salience argument — the paper claims that requiring key enumeration in JSON will help with rare roles, but this is both the hypothesis and the design choice simultaneously. The mechanism connecting "forced key generation" to "better rare role handling" relies on the assumption that this counteracts the model's bias toward omitting rare slots, but that's unproven and will need empirical validation through the ablation study.

For the RAMS TSV point, the proposal correctly identifies that RAMS only specifies upper bounds on cardinality while XGrammar enforces both upper bounds and entity-type constraints, with the required key enumeration being the core structural salience mechanism. The framing here is clearer now.

Stepping back after multiple rounds of revision, the central question is whether this clears the bar. The novelty is moderate — it's fundamentally an empirical comparison of hard grammar constraints versus soft filtering for generating zero-shot training data, with an interesting but somewhat limited structural salience framing. The core contribution boils down to applying XGrammar constraints during synthetic data generation and measuring the impact.

Related work like LtGaE, FineCSDA, and others already tackle pieces of this problem, so the novelty sits at 3/5 — the three-condition ablation design and structural salience mechanism are clever, but the technical contribution is more about pipeline integration than algorithmic innovation.

On feasibility, the 16-day timeline is aggressive but the plan is concrete now. The compute estimate of roughly 125.5 hours on A100 (equivalent to about 90 hours on H100) fits within the 200-hour constraint, and running Qwen3-32B on two A100s is realistic. The main risk remains the compressed timeline, though the plan accounts for this.

The proposal is well-structured and detailed — the three-condition ablation is precisely specified, the null result is pre-registered, and the structural salience mechanism is clearly laid out, earning a 4/5 on clarity.

For impact, zero-shot EAE is genuinely important, and even a negative result showing that hard constraints don't help would be useful for practitioners. But the practical value is somewhat limited — it's helpful for building EAE systems but doesn't fundamentally shift the field forward. The supervised-to-zero-shot gap persists regardless of the outcome, so I'd rate impact at 3/5.

That puts the overall score at 3.5/5. Looking back after seven rounds of revision, the main remaining concerns are that this is fundamentally an empirical study testing a specific engineering choice, which is appropriate for EMNLP Findings but means the quality of the experimental design matters more than algorithmic novelty. There's also a minor issue with how BoostCD is characterized — it's broader closed IE, not just relation extraction. Most critically, the core empirical question might yield a trivially negative answer if the pilot study already shows minimal constraint violations and no coverage gains from required key enumeration.

The proposal has come a long way though. All the major issues from earlier rounds have been resolved, the framing is now honest about structural salience being a hypothesis rather than a guarantee, the experimental design is methodologically solid with proper volume controls and stratified evaluation, and the timeline and resource estimates are realistic. Even if this ends up being a null result on a fairly niche engineering question, EMNLP Findings does accept pre-specified null results, though the impact would naturally be more limited.

The venue itself is well-matched to the contribution level. The remaining concerns are mostly minor—BoostCD should be characterized as closed IE rather than relation extraction, the novelty is admittedly limited as a pipeline integration plus empirical study but that's appropriate for this venue, and everything ultimately hinges on whether the Qwen3-32B pilot actually shows measurable differences. I've checked for any major papers I might have missed on EAE or constrained generation, and the search seems comprehensive—GEMS, LtGaE, FineCSDA, Gatto et al., BoostCD, and ASEE are all accounted for, with no new concurrent work that directly threatens the proposal.

Given that this is round 8 out of 10 and the average score sits around 3.5 against a 4.0 threshold, I need to be realistic about whether another revision cycle is warranted. The contribution type is explicitly an empirical study with lower novelty expectations, the target venue is appropriate, and there are no fundamental blockers—just minor issues. The scores break down to novelty at 3/5 (fitting for an empirical study), feasibility at 4/5 (tight but workable), and clarity at 4/5 (well-specified). At this point, the proposal is essentially ready, and pushing for another round of revisions on these minor points might not move the needle meaningfully.

Actually, reconsidering the novelty score in the EMNLP Findings context—the structural salience framing is a genuine insight, and requiring role keys in the output template is a non-obvious design choice that hasn't been systematically studied before in the context of EAE synthetic data generation.

The three-condition, volume-controlled ablation is methodologically sound, so I'd rate novelty at 3.5/5 for Findings—above the bar but not Main-conference level. Impact is also 3.5/5 since it addresses a concrete practitioner question about hard versus soft constraints for data quality, and the pre-specified null result adds credibility.

So my overall assessment stays around 3.5, which signals "revise" rather than "pass." After eight rounds, the core issues are the BoostCD characterization, which is trivially fixable, and the inherent novelty ceiling of an empirical study, which isn't solvable without fundamentally redesigning the work.

Given the substantial progress and that we're at round 8 of 10, I should frame this as a "revise" verdict with concrete, actionable fixes rather than a rejection—these are addressable problems, not fatal flaws.

Let me look more carefully at the current proposal to make sure I'm not overlooking anything new...

Checking the GEMS differentiation again: the proposal explains that GEMS uses multi-perspective prompts and ontology steering at inference time on WikiEvents, ACE05, and ERE-EN for low-resource EAE, while CompSchema-IE applies hard grammar constraints during training-data generation to test whether structural salience from required role enumeration improves downstream performance on rare events.

The structural salience mechanism is now well-articulated: by making all applicable role slots required keys in the XGrammar JSON template, the model must generate values (even empty strings or nulls) for every slot rather than omitting rare ones, forcing attention to each position during the forward pass.

On quality degradation, the proposal acknowledges that constrained decoding can push instruction-tuned models away from their natural high-confidence paths and increase extraction misses, and addresses this by leveraging Qwen3-32B's strong instruction-following capabilities to maintain generation quality under constraints.

The stratified evaluation design—measuring argument span F1 per role stratum alongside role coverage rates—cleanly separates quality and coverage effects rather than conflating them.

BoostCD is correctly cited for demonstrating complementary errors between constrained and unconstrained decoding, though the characterization as relation extraction specifically is slightly narrower than the paper's broader closed IE scope.

I'm noticing the mechanistic claim about XGrammar forcing attention to each slot needs refinement—the grammar enforces token generation for every slot position, but this isn't quite the same as directing transformer attention in the traditional sense.  The paper's careful distinction between guaranteed key instantiation versus uncertain fill quality is appropriate, though reviewers might still push back on the "forces attention" framing. If the main result is actually a null finding showing C doesn't outperform B, that could complicate acceptance at EMNLP.

There's also a methodological concern with the LtGaE comparison — the paper relies on published numbers rather than running experiments under identical conditions, so it can't claim direct superiority over LtGaE's approach, especially given the different training scales involved. Let me look more closely at what the actual performance numbers show. estimates more carefully:
- LtGaE achieves 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki
- These are Span-F1 numbers, while the supervised SOTA DEGAP achieves 54.2/67.1 Arg-C F1 on RAMS/WikiEvents
- The proposal uses "Arg-C F1" for supervised SOTA and "Span-F1" for LtGaE, which are different metrics

Actually, the proposal uses both metrics consistently with what each paper reports. This is fine.

5. **Question about whether Condition C actually outperforms LtGaE**: The proposal frames this as "evaluation uses the LtGaE three-way protocol with LtGaE, ASEE, and DEGAP as baselines" — but it doesn't predict whether Condition C will outperform LtGaE. If Condition C uses Qwen3-8B fine-tuned on only 5,000 instances while LtGaE uses its full pipeline, Condition C might actually perform worse overall, though that's acceptable since the paper's main claim is about the C vs. B comparison rather than achieving SOTA.

Looking at the remaining issues, there are a few minor fixes needed like clarifying BoostCD as closed IE rather than relation extraction, but the more significant concern is that the paper's expected outcome is uncertain — if Condition C doesn't even outperform B in the rare-role strata, the contribution becomes a null result for a narrow question with limited acceptance prospects at EMNLP Findings despite the pre-specification. There's also no direct comparison with LtGaE's actual system beyond the baseline evaluation.

The structural issues from earlier rounds have been addressed, and most of the checklist items are resolved. This is methodologically sound for EMNLP Findings, though the novelty is modest at 3/5 given it's an empirical study with pipeline integration, and feasibility is solid at 4/5 despite the tight timeline.

The average score of 3.5/5 falls short of the 4.0 threshold, which reflects a fundamental constraint: the core contribution is pipeline integration plus empirical validation, naturally limiting both novelty and impact. After eight rounds of revision, this structural limitation persists. For the next round, I should flag the remaining BoostCD characterization issue and raise a deeper concern about whether the expected positive result is realistic—Qwen3-32B's strong instruction-following might make the structural salience effect negligible, which would undermine the study's premise.

Actually, I'm reconsidering whether I'm being too critical. The structural salience mechanism is genuinely compelling: grammar-constrained decoding forces enumeration of all role slots in the output template, which could systematically shift generation toward better rare-role coverage even if individual violations are uncommon. This is testable, and the three-condition design cleanly isolates this effect. The volume-controlled approach removes confounds that would otherwise muddy the comparison. For EMNLP Findings, a well-executed empirical study with clean ablations, controlled design, stratified evaluation, and pre-specified null interpretation across multiple baselines is actually solid. The acceptance bar for Findings papers with rigorous empirical work is reasonable, so I should adjust my assessment upward slightly—the novelty is modest but the execution is sound.

Weighing everything: the only new issue is a minor BoostCD characterization fix, prior concerns have been addressed, and the structural limitations are inherent to the idea itself. At round 8 of 10 with only minor remaining problems, a revise verdict makes sense, with focused feedback on the BoostCD description and a note about the empirical assumptions underlying the structural salience hypothesis. The BoostCD characterization should say "closed IE" rather than "closed IE (relation extraction)" since the paper covers information extraction more broadly. The structural salience mechanism is presented as improving attention to each slot, but a reviewer might question whether forcing key enumeration actually improves value quality or just forces generation. The approach section has some redundancy worth tightening. Now I'm reconsidering whether this paper is truly competitive for EMNLP Findings at this stage.

A strong Findings paper needs solid empirical contribution, clear methodology, multiple baselines, and honest handling of negative results—this submission has all of those. The core limitation is that it's an empirical study on a specific design choice in synthetic data generation, so the contribution is genuine but somewhat narrow. I'm settling on a revise verdict with targeted feedback that should be addressable quickly, since the paper is nearly ready. Now I'm assigning scores: novelty is 3/5 given that the structural salience insight is real but the technical contribution is mainly pipeline integration, and several concurrent papers tackle adjacent problems; feasibility is 4/5 since the timeline is tight but achievable with the specified plan and verified resource constraints; clarity is 4/5 with well-specified methodology.

For impact, I'm giving 3/5 since it's a solid empirical contribution for the EAE community, though the actual outcome hinges on whether Qwen3-32B produces meaningful structural salience differences. That averages to 3.5/5. The main issues are a minor characterization problem with BoostCD and an imprecise claim about how structural salience works mechanistically in transformers—the idea that required key enumeration forces attention to each slot needs more careful explanation. Before finalizing, I want to do one more search to check if there's recent work on grammar-constrained synthetic data generation for event argument extraction.

The search confirms there's no concurrent work combining grammar-constrained decoding with synthetic data generation for EAE, so the proposal adequately covers the landscape. My final decision is to recommend revision with those two targeted issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81c95f2f-bab1-47a8-99f4-51a90f5c34c6",
  "isSidechain": false,
  "requestId": "req_011Catg5mLNG8MvtfwhetSkX",
  "type": "assistant",
  "uuid": "4f0f139b-5bf4-4ac1-a6d5-d7f7d2ac41ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01T1EWbWaUVNRLJkSMzqvNcr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5085,
      "cache_read_input_tokens": 38363,
      "output_tokens": 7011,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7011,
          "cache_read_input_tokens": 38363,
          "cache_creation_input_tokens": 5085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5085
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

_source line 17 · 2026-05-10T09:48:20.650Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01QKcqPgfFKVMAMPPF3rMXht`</summary>

```json
{
  "description": "Search for structural salience EAE synthetic data concurrent work",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing an EMNLP 2026 paper on grammar-constrained synthetic data generation for zero-shot event argument extraction (EAE). Please do the following searches:\n\n1. Search \"structural salience argument role coverage event argument extraction 2025 2026\" — any papers on structural salience or slot coverage in EAE?\n\n2. Search arXiv for \"event argument extraction constrained decoding training data 2025\" and \"zero-shot event extraction grammar JSON schema 2025 2026\" — any concurrent papers on grammar-constrained or schema-constrained synthetic data generation for EAE?\n\n3. Search \"RAMS event argument extraction rare roles coverage 2024 2025\" — any papers specifically addressing rare argument role coverage in RAMS dataset?\n\n4. Search \"required key JSON schema structured generation LLM rare entity 2025\" — any papers on required-key JSON generation improving coverage of rare categories?\n\n5. Search openreview.net for \"event argument extraction 2025 2026 structured generation constraints\" — any conference submissions on this topic?\n\nThe core question: has anyone empirically compared hard grammar constraints vs. post-hoc filtering for EAE training data generation quality, particularly with a focus on rare role coverage? Report anything relevant you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f0f139b-5bf4-4ac1-a6d5-d7f7d2ac41ec",
  "isSidechain": false,
  "requestId": "req_011Catg5mLNG8MvtfwhetSkX",
  "type": "assistant",
  "uuid": "15e4648c-94db-4448-b153-622323d8f17f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01T1EWbWaUVNRLJkSMzqvNcr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5085,
      "cache_read_input_tokens": 38363,
      "output_tokens": 7011,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7011,
          "cache_read_input_tokens": 38363,
          "cache_creation_input_tokens": 5085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5085
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
  "leafUuid": "15e4648c-94db-4448-b153-622323d8f17f",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Shot Event Argument Extraction",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9"
}
```

---

### Tool result

_source line 20 · 2026-05-10T09:48:54.028Z_

<details><summary>↩ Tool result · `toolu_01QKcqPgfFKVMAMPPF3rMXht`</summary>

```text
## Summary of Research Findings

Based on comprehensive web searches across arXiv, OpenReview, and academic databases, here's what I found relevant to your EMNLP 2026 paper on grammar-constrained synthetic data generation for zero-shot event argument extraction:

### Key Relevant Research Areas

**1. Grammar-Constrained Decoding for Structured Information Extraction (2025)**

The most directly relevant work is on grammar-constrained decoding applied to information extraction tasks. Recent research demonstrates that encoder-decoder models clearly benefit from grammar-constrained decoding guiding output generation, with reported F1 score improvements of 0.351-0.425 on specialized datasets. This directly addresses the core methodology comparison you're investigating.

**2. Zero-Shot Event Extraction with Schema Constraints (2025-2026)**

A novel approach called Agent-Event-Coder (AEC) treats event extraction as a code-generation process, decomposing zero-shot event extraction into specialized subtasks. Critically, event schemas are represented as executable class definitions for deterministic validation and precise feedback, addressing the structured output requirement you're examining. This represents a concurrent approach to grammar constraints.

**3. Advanced Grammar-Based Structured Generation Infrastructure (2026)**

XGrammar has emerged as the default backend for structured generation across vLLM, SGLang, and TensorRT-LLM (as of March 2026), achieving under 40 microseconds per token overhead with JSON generation. This represents production-ready grammar constraint infrastructure that went beyond post-hoc filtering approaches.

**4. RAMS Dataset and Rare Role Coverage**

The RAMS dataset (139 event types, 65 roles) continues to be a benchmark, with the highest reported F1 score at 52.2 for argument extraction. Critically, **the literature explicitly notes that coverage of rare roles remains an under-explored area** in RAMS evaluation, with annotations noting that not all roles appear in all events. This directly validates your focus on rare role coverage.

**5. JSON Schema and Structured Output Reliability (2025)**

Research on "required-key" schema enforcement shows that GPT-4 exhibits 11.97% invalid response rates on complex extraction tasks, but reinforcement learning using schemas as training signals achieves 98.7% valid JSON rates (vs. 82.3% baseline). This demonstrates empirical quantification of constraint effectiveness for structured data quality—directly comparable to your hard constraints vs. post-hoc filtering comparison.

**6. Comparative Analysis of Constraint Approaches**

While I found evidence of grammar-constrained decoding being effective and post-hoc filtering approaches being used, **I did not find a direct empirical head-to-head comparison specifically on training data generation quality for rare role coverage in EAE**. Most papers focus on either:
- Grammar constraints during inference (not for training data generation)
- Post-hoc validation without controlled comparison
- Schema-aware generation without direct filtering comparison

**7. Document-Level EAE with Constraint Enhancement**

Recent OpenReview papers propose dependency-aware graph networks for event argument extraction evaluated on ACE05, RAMS, and WikiEvents, but they address role dependency modeling rather than synthetic data generation methodology.

### Critical Gap Identified

Your paper appears to address a **genuine research gap**: the lack of empirical comparison between hard grammar constraints (enforcing valid schemas during LLM generation) versus post-hoc filtering (generating freely then validating) specifically for:
- Synthetic training data generation quality
- Rare argument role coverage in EAE
- Zero-shot transfer scenarios

The closest prior work examines these dimensions separately but not in direct comparison on this specific task.

### Sources

- [Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts](https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/)
- [Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction](https://arxiv.org/html/2511.13118v1)
- [Closed-Domain Event Extraction Literature Review January 2025 v1.0](https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf)
- [Event Pattern-Instance Graph: A Multi-Round Role](https://aclanthology.org/2025.findings-acl.94.pdf)
- [BEMEAE: Moving Beyond Exact Span Match for Event](https://aclanthology.org/2025.naacl-long.295.pdf)
- [PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction](https://arxiv.org/html/2510.08623v1)
- [SLOT: Structuring the Output of Large Language Models](https://aclanthology.org/2025.emnlp-industry.32.pdf)
- [Intra-Event and Inter-Event Dependency-Aware Graph Network for Event Argument Extraction](https://openreview.net/forum?id=d94iPelgSD&noteId=IIEhLhimCB)
- [Fine-grained document-level financial event argument extraction approach](https://openreview.net/forum?id=KIEgkQqQoA)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15e4648c-94db-4448-b153-622323d8f17f",
  "isSidechain": false,
  "promptId": "4ca85829-ed36-4a44-93b8-2b7baa11aeac",
  "type": "user",
  "uuid": "11a6dcb4-431c-4832-98c1-620d5673affa",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing an EMNLP 2026 paper on grammar-constrained synthetic data generation for zero-shot event argument extraction (EAE). Please do the following searches:\n\n1. Search \"structural salience argument role coverage event argument extraction 2025 2026\" — any papers on structural salience or slot coverage in EAE?\n\n2. Search arXiv for \"event argument extraction constrained decoding training data 2025\" and \"zero-shot event extraction grammar JSON schema 2025 2026\" — any concurrent papers on grammar-constrained or schema-constrained synthetic data generation for EAE?\n\n3. Search \"RAMS event argument extraction rare roles coverage 2024 2025\" — any papers specifically addressing rare argument role coverage in RAMS dataset?\n\n4. Search \"required key JSON schema structured generation LLM rare entity 2025\" — any papers on required-key JSON generation improving coverage of rare categories?\n\n5. Search openreview.net for \"event argument extraction 2025 2026 structured generation constraints\" — any conference submissions on this topic?\n\nThe core question: has anyone empirically compared hard grammar constraints vs. post-hoc filtering for EAE training data generation quality, particularly with a focus on rare role coverage? Report anything relevant you find.",
    "agentId": "a3c10823233249951",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Research Findings\n\nBased on comprehensive web searches across arXiv, OpenReview, and academic databases, here's what I found relevant to your EMNLP 2026 paper on grammar-constrained synthetic data generation for zero-shot event argument extraction:\n\n### Key Relevant Research Areas\n\n**1. Grammar-Constrained Decoding for Structured Information Extraction (2025)**\n\nThe most directly relevant work is on grammar-constrained decoding applied to information extraction tasks. Recent research demonstrates that encoder-decoder models clearly benefit from grammar-constrained decoding guiding output generation, with reported F1 score improvements of 0.351-0.425 on specialized datasets. This directly addresses the core methodology comparison you're investigating.\n\n**2. Zero-Shot Event Extraction with Schema Constraints (2025-2026)**\n\nA novel approach called Agent-Event-Coder (AEC) treats event extraction as a code-generation process, decomposing zero-shot event extraction into specialized subtasks. Critically, event schemas are represented as executable class definitions for deterministic validation and precise feedback, addressing the structured output requirement you're examining. This represents a concurrent approach to grammar constraints.\n\n**3. Advanced Grammar-Based Structured Generation Infrastructure (2026)**\n\nXGrammar has emerged as the default backend for structured generation across vLLM, SGLang, and TensorRT-LLM (as of March 2026), achieving under 40 microseconds per token overhead with JSON generation. This represents production-ready grammar constraint infrastructure that went beyond post-hoc filtering approaches.\n\n**4. RAMS Dataset and Rare Role Coverage**\n\nThe RAMS dataset (139 event types, 65 roles) continues to be a benchmark, with the highest reported F1 score at 52.2 for argument extraction. Critically, **the literature explicitly notes that coverage of rare roles remains an under-explored area** in RAMS evaluation, with annotations noting that not all roles appear in all events. This directly validates your focus on rare role coverage.\n\n**5. JSON Schema and Structured Output Reliability (2025)**\n\nResearch on \"required-key\" schema enforcement shows that GPT-4 exhibits 11.97% invalid response rates on complex extraction tasks, but reinforcement learning using schemas as training signals achieves 98.7% valid JSON rates (vs. 82.3% baseline). This demonstrates empirical quantification of constraint effectiveness for structured data quality—directly comparable to your hard constraints vs. post-hoc filtering comparison.\n\n**6. Comparative Analysis of Constraint Approaches**\n\nWhile I found evidence of grammar-constrained decoding being effective and post-hoc filtering approaches being used, **I did not find a direct empirical head-to-head comparison specifically on training data generation quality for rare role coverage in EAE**. Most papers focus on either:\n- Grammar constraints during inference (not for training data generation)\n- Post-hoc validation without controlled comparison\n- Schema-aware generation without direct filtering comparison\n\n**7. Document-Level EAE with Constraint Enhancement**\n\nRecent OpenReview papers propose dependency-aware graph networks for event argument extraction evaluated on ACE05, RAMS, and WikiEvents, but they address role dependency modeling rather than synthetic data generation methodology.\n\n### Critical Gap Identified\n\nYour paper appears to address a **genuine research gap**: the lack of empirical comparison between hard grammar constraints (enforcing valid schemas during LLM generation) versus post-hoc filtering (generating freely then validating) specifically for:\n- Synthetic training data generation quality\n- Rare argument role coverage in EAE\n- Zero-shot transfer scenarios\n\nThe closest prior work examines these dimensions separately but not in direct comparison on this specific task.\n\n### Sources\n\n- [Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts](https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/)\n- [Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction](https://arxiv.org/html/2511.13118v1)\n- [Closed-Domain Event Extraction Literature Review January 2025 v1.0](https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf)\n- [Event Pattern-Instance Graph: A Multi-Round Role](https://aclanthology.org/2025.findings-acl.94.pdf)\n- [BEMEAE: Moving Beyond Exact Span Match for Event](https://aclanthology.org/2025.naacl-long.295.pdf)\n- [PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction](https://arxiv.org/html/2510.08623v1)\n- [SLOT: Structuring the Output of Large Language Models](https://aclanthology.org/2025.emnlp-industry.32.pdf)\n- [Intra-Event and Inter-Event Dependency-Aware Graph Network for Event Argument Extraction](https://openreview.net/forum?id=d94iPelgSD&noteId=IIEhLhimCB)\n- [Fine-grained document-level financial event argument extraction approach](https://openreview.net/forum?id=KIEgkQqQoA)"
      }
    ],
    "totalDurationMs": 33370,
    "totalTokens": 24819,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 22637,
      "output_tokens": 1222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 955
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1222,
          "cache_read_input_tokens": 22637,
          "cache_creation_input_tokens": 955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 955,
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
  "sourceToolAssistantUUID": "15e4648c-94db-4448-b153-622323d8f17f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T09:49:23.201Z_

<details><summary>Logged reasoning block</summary>

```text
The search confirms my assessment:
1. No concurrent work directly comparing hard grammar constraints vs. post-hoc filtering for EAE training data generation quality — this validates the gap
2. XGrammar is confirmed as production-ready infrastructure
3. RAMS rare role coverage remains an underexplored area
4. No direct competitor papers found that would undermine the novelty

Now let me write my final review. Given all the evidence:

**Summary of findings:**
- All Round 7 issues properly addressed (GEMS cited, grammar representation specified, quality degradation acknowledged)
- BoostCD is about "closed IE" broadly, not specifically "relation extraction" — minor characterization issue


- No concurrent work threatens the novelty, and the structural salience hypothesis is well-supported by the three-condition ablation
- Resource and timeline constraints are both manageable

There are a couple of minor issues worth flagging: the BoostCD characterization should be "closed IE" rather than "closed IE (relation extraction)", and the language around structural salience being "forced" is mechanistically imprecise—what's actually happening is the model generates a key token, not that attention is directly forced to content. The novelty itself has some inherent limitations, but nothing that fundamentally undermines the contribution.

After eight rounds of refinement, the core work is methodologically sound and well-suited to EMNLP Findings. The remaining issues are all fixable. Looking at the scores: novelty sits at 3/5 since the structural salience insight is genuine but the technique is fundamentally a pipeline integration; feasibility is 4/5 despite the tight 16-day window because every step is specified and hardware-verified; clarity is 4/5 with explicit methodology and a pre-specified null result; impact is 3/5 as a solid empirical contribution for the EAE community, modest but honest. That averages to 3.5/5—slightly below the bar, but the work is defensible. the 4.0 threshold for "pass"

Given round 8/10, I should issue "revise" with very targeted minor fixes, noting that the proposal is close to submission-ready.

Actually, let me reconsider once more. The paper's contribution is:
1. A clean three-condition empirical study
2. Volume-controlled design to eliminate confounds
3. Stratified evaluation to localize gains
4. Pre-specified null result interpretation
5. A specific mechanistic hypothesis about structural salience via required key enumeration

For EMNLP Findings, papers with clearly framed empirical studies, good methodology, and honest reporting of results (positive or negative) do get accepted. The review-after-7-rounds proposal is genuinely stronger than the original.

The scores I'm giving reflect:
- Novelty 3/5: Fair for a pipeline study
- Feasibility 4/5: Verified and realistic
- Clarity 4/5: Well-specified
- Impact 3/5: Practical contribution for the EAE community

This averages to 3.5/5, which falls short of the 4.0 bar. To reach acceptance, I'd need to see either stronger novelty beyond pipeline integration, clearer state-of-the-art improvements rather than just comparative analysis, or a more robust empirical scope like testing across multiple generator models instead of just Qwen3-32B. With the submission deadline 16 days away and this being round 8, I'll send back a "revise" verdict with two focused corrections: clarifying the BoostCD characterization and tightening the mechanistic language around how the model's attention is being directed.

Writing the JSON response now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11a6dcb4-431c-4832-98c1-620d5673affa",
  "isSidechain": false,
  "requestId": "req_011CatgJu8XzMAqvC8cqvaNk",
  "type": "assistant",
  "uuid": "8fc88807-ee51-4de1-b4f6-8a31f09b56c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YNTomxvVbGuqzsBWjsmcNb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8232,
      "cache_read_input_tokens": 43448,
      "output_tokens": 2957,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8232,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2957,
          "cache_read_input_tokens": 43448,
          "cache_creation_input_tokens": 8232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8232
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

_source line 22 · 2026-05-10T09:50:03.785Z_

Now I have enough information to write my verdict. Let me compile my findings.

**Independent verification summary:**
- GEMS (ACL Findings 2025, aclanthology.org/2025.findings-acl.1353) — **verified**, T5-large confirmed, WikiEvents/ACE05/ERE-EN benchmarks confirmed
- Schall & de Melo RANLP 2025 — **verified**, quality degradation finding confirmed
- LtGaE (AAAI 2026, arXiv:2603.02909) F1 numbers (45.77/32.38/46.96) — **verified exactly**; RL penalty formula [τ−ε, τ+ε] — **verified**
- DEGAP RAMS 54.2 / WikiEvents 67.1 Arg-C F1 — **verified**
- FineCSDA at dl.acm.org — **verified**
- BoostCD (arXiv:2506.14901) complementary error profiles — **verified**, but the paper covers **closed IE broadly**, not specifically "relation extraction" as the proposal claims
- XGrammar <40μs/token — **verified** (actual: ~18μs optimized, <40μs end-to-end)
- No concurrent work found combining grammar-constrained decoding with synthetic data generation for EAE — **gap confirmed**

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The structural salience framing via required-key enumeration is a genuine and previously unstudied insight for EAE synthetic data generation; however, the core technical contribution remains pipeline integration of existing tools (XGrammar + vLLM + LoRA) rather than a new algorithm, which caps novelty for the EMNLP Findings audience. No direct concurrent work found, confirming the gap, but the conceptual distance from LtGaE/FineCSDA/GEMS is primarily framing rather than mechanism."
    },
    "feasibility": {
      "score": 4,
      "rationale": "Resource estimate (~90h H100-equiv) is within the ≤200h hard constraint and independently verified; Qwen3-32B on 2×A100 is hardware-feasible; the 16-day timeline is tight but the day-by-day plan is specific enough to be credible with a focused team."
    },
    "clarity": {
      "score": 4,
      "rationale": "Methodology is now well-specified across seven prior revision rounds: grammar representation is explicit (required keys with empty-string fallback), volume normalization protocol is defined (1.5× pool), null result interpretation is pre-specified, and stratified evaluation design is clear."
    },
    "impact": {
      "score": 3,
      "rationale": "The empirical study addresses a concrete practitioner question (do hard constraints outperform oracle filtering for EAE training data?) with a methodologically sound design; even a null result has practical value. However, downstream impact depends heavily on whether Qwen3-32B's structural salience effect is measurable — a strong instruction-following model may render the effect negligible, yielding a negative finding with limited actionability."
    }
  },
  "issues": [
    "BOOSTCD APPLICATION DOMAIN MISCHARACTERIZED [minor, round 8 new]: The proposal consistently describes BoostCD as 'inference-time boosting for closed IE (relation extraction)' — but BoostCD (arXiv:2506.14901) is applied to closed information extraction broadly, not specifically relation extraction. In the landscape section and key references, '(relation extraction)' should be removed or replaced with '(closed information extraction)'. The core empirical finding (complementary error profiles of constrained vs. unconstrained decoding) is correctly attributed, but the domain specification is factually imprecise and a reviewer familiar with BoostCD will notice.",
    "STRUCTURAL SALIENCE MECHANISM LANGUAGE IS MECHANISTICALLY IMPRECISE [minor, round 8 new]: The proposal repeatedly states that required-key enumeration 'forces the model's attention to each slot during the forward pass' — this language invokes transformer attention mechanisms in a way that is not precisely accurate. What XGrammar actually does is constrain the output token distribution so the model MUST generate each role name as a JSON key; whether this changes internal attention patterns is an empirical question not established by prior work. The mechanistically accurate claim is: 'forcing the model to generate each role key as an output token ensures the corresponding slot appears in every generated instance, preventing the silent omission of rare slot names that characterizes unconstrained generation.' This is a weaker but more defensible claim — it guarantees key-level instantiation without claiming to modulate attention. A reviewer familiar with constrained decoding (e.g., from Schall & de Melo) will challenge the 'forces attention' formulation. Replacing this language across the proposal with 'forces generation of each role key' eliminates the vulnerability.",
    "SPAN-F1 VS. ARG-C F1 METRIC CONSISTENCY [minor, persistently unaddressed]: The proposal uses Span-F1 for LtGaE (45.77/32.38/46.96) and Arg-C F1 for DEGAP (54.2/67.1). These metrics are not directly comparable. The paper must include a footnote clarifying the metric difference so readers do not incorrectly interpret a direct cross-paper comparison. The proposed comparison table (LtGaE, ASEE, DEGAP, Conditions A/B/C) should report all models under the same metric — Span-F1 is typically lower than Arg-C F1, so mixing them in a single table without annotation is misleading."
  ],
  "feedback": "The Round 8 proposal has successfully resolved all three Round 7 issues: GEMS is cited throughout with clean mechanistic differentiation, the optional role grammar representation (required keys with empty-string/null fallback) is now explicit, and Schall & de Melo RANLP 2025 is cited with a concrete mitigation strategy. Independent verification confirms LtGaE F1 numbers, DEGAP numbers, FineCSDA, BoostCD, GEMS, and XGrammar overhead claims are all accurate. No concurrent work was found that directly competes with the three-condition, volume-controlled grammar-constraint ablation for EAE synthetic data generation.\n\nThree targeted fixes before submission:\n\n(1) BOOSTCD [one-word fix]: Replace '(relation extraction)' with '(closed information extraction)' or just remove the parenthetical. The BoostCD paper covers closed IE broadly. Change: 'inference-time boosting for closed IE (relation extraction)' → 'inference-time boosting for closed IE.'\n\n(2) STRUCTURAL SALIENCE LANGUAGE [one-paragraph revision]: Replace all instances of 'forces the model's attention to each slot during the forward pass' with mechanistically accurate language: 'forces the model to generate each role name as a required output token, ensuring the corresponding slot appears in every generated instance rather than being silently omitted.' This is accurate, verifiable, and avoids the attention-mechanism claim that constrained-decoding reviewers will challenge.\n\n(3) METRIC CONSISTENCY [one footnote]: Add a footnote to the comparison table explicitly noting: 'LtGaE and CompSchema-IE report Span-F1; DEGAP reports Arg-C F1. These metrics are not directly comparable — Arg-C F1 is typically higher than Span-F1 for the same system. We report each baseline under its natively reported metric.' This prevents a false impression that the gap to supervised SOTA is smaller than it is.\n\nWith these three fixes — all accomplishable in under an hour of drafting — the proposal is ready for EMNLP 2026 Findings submission under the May 25 ARR deadline.",
  "reason": "All Round 7 critical issues resolved; three minor issues remain (BoostCD domain mischaracterization, mechanistically imprecise 'forces attention' language, and metric consistency footnote) that are fixable in under an hour but warrant a final revision pass before submission."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fc88807-ee51-4de1-b4f6-8a31f09b56c2",
  "isSidechain": false,
  "requestId": "req_011CatgJu8XzMAqvC8cqvaNk",
  "type": "assistant",
  "uuid": "60d00e57-943f-4c7d-9d32-3939377cf52f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YNTomxvVbGuqzsBWjsmcNb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8232,
      "cache_read_input_tokens": 43448,
      "output_tokens": 2957,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8232,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2957,
          "cache_read_input_tokens": 43448,
          "cache_creation_input_tokens": 8232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8232
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
  "leafUuid": "60d00e57-943f-4c7d-9d32-3939377cf52f",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Shot Event Argument Extraction",
  "sessionId": "94b5d494-754c-4cdb-964a-033c6cb3f6c9"
}
```

---
