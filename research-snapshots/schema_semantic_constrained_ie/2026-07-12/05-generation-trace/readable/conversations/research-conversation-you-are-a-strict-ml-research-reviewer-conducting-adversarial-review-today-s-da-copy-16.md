# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/39816bd0-bf80-4353-985c-a102c062aef3.jsonl`
- **Structured JSON:** [`35d664333c78bd5fc2c6.json`](../../sessions/35/35d664333c78bd5fc2c6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-11T23:56:32.308Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-11T23:56:32.308Z",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.\n\nDirection: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.\n\nContribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.\n2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.\n3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.\n\nLook for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.\n\nTag: direction=information_extraction, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 4/10)\n{\n  \"title\": \"Ontology-Faithful Information Extraction via Compiled Semantic Constraints: Automatic Ontology-to-Decoder Compilation with Forward-Only Type Masking\",\n  \"core_problem\": \"Can we automatically compile IE ontology schemas — entity type hierarchies, relation domain/range restrictions, event argument role-filler types — into efficient decoding-time constraint specifications that enforce semantic validity without degrading extraction accuracy, and what is the actual rate of ontology constraint violations in unconstrained LLM-based IE — is it significant enough to warrant decoding-time enforcement?\",\n  \"opportunity\": \"LLM-based IE systems produce structurally valid but semantically invalid outputs at unknown rates: while structural validity (valid JSON, correct field names) is now reliably enforced by grammar-constrained decoding (XGrammar-2, default in vLLM/SGLang/TensorRT-LLM since 2026), no existing system enforces semantic validity — cross-field type constraints such as relation domain/range restrictions or event argument role-filler types. For instance, an ACE05 PHYS.Located relation requires a PER/GPE Arg-1 and a FAC/LOC/GPE Arg-2; a system that assigns two ORG entities produces structurally valid but semantically invalid output. Although the exact prevalence of such violations in LLM-based IE is unknown (no prior work has systematically measured it), the existence of the gap between grammar-enforceable structural constraints and the context-sensitive semantic constraints that ontologies specify creates a clear engineering and scientific opportunity. If violation rates are non-trivial (>5%), decoding-time enforcement directly improves output quality. If rates are low (<5%), this is an important negative result establishing that LLMs implicitly learn ontology constraints from training data, saving the community effort pursuing constrained decoding for semantic validity. Either way, the quantification itself is a first-order contribution. The grammar+semantic-callback paradigm for constrained decoding has been explored in code generation — Synchromesh (ICLR 2022) introduced two-layer Completion Engines combining syntactic and semantic constraints, and IterGen (ICLR 2025) added backtracking with user-defined semantic callbacks — but no existing work automatically compiles IE ontology schemas into such constraint systems. IE ontologies present unique challenges absent from code generation: (1) constraints are input-dependent (valid relation arguments depend on which entity types have been extracted so far, requiring a dynamic entity type registry), (2) ontology type hierarchies create inheritance-aware constraints (a GPE-typed entity can fill a LOC argument slot), and (3) the constraint graph is schema-specific and varies across IE tasks, requiring automatic compilation rather than manual Completion Engine implementation. Furthermore, recent work demonstrates that constrained decoding degrades generation quality: The Format Tax (arXiv Apr 2026) shows that format-requesting prompts account for ~70% of the quality loss while grammar masking contributes only ~30%, and the Structure Snowballing phenomenon (arXiv Apr 2026) documents how strict structural constraints can trigger cascading errors in Qwen3-8B. These findings motivate our two-pass strategy (S2), which avoids applying semantic constraints during entity extraction and instead compiles them into vocabulary constraints for a second pass.\",\n  \"landscape\": \"**Grammar+semantic constraint paradigm (code generation).** Synchromesh (Poesia et al., ICLR 2022) is the foundational work combining syntactic and semantic constraints during decoding. Its Constrained Semantic Decoding (CSD) framework defines Completion Engines with two layers — a context-free layer for syntactic validity and a context-sensitive layer for semantic constraints (scope, typing, contextual logic) — applied to SQL, Vega-Lite, and SMCalFlow code generation. IterGen (Ugare et al., ICLR 2025) extends this paradigm with backtracking: users define semantic callbacks that check generated content at grammar symbol boundaries, and the system backtracks via KV cache state restoration when violations are detected, achieving 18.5% improvement over forward-only grammar-guided generation on SQL/Vega-Lite. Both require manual implementation of domain-specific constraint logic (Completion Engines or callbacks). Neither addresses IE ontology constraints or automatic constraint compilation from schema definitions.\\n\\n**Constrained decoding for IE.** GenIE (Josifoski et al., NAACL 2022) pioneered bi-level constrained generation for IE with structural constraints and prefix trie vocabulary constraints, but enforces only entity/relation name validity, not cross-field type consistency. Geng et al. (EMNLP 2023) demonstrated input-dependent grammars for closed IE on Wikidata, again limited to vocabulary membership. Schmidt & Cimiano (Frontiers AI 2024) applied grammar-constrained decoding to clinical IE. Lazy-k (Hemmer et al., EMNLP 2023) explored constrained decoding for token classification IE. SciDC (arXiv Apr 2026) introduced multi-layer decoding constraints for scientific domains but uses hand-crafted rules. Dialogue Ontology RE (SIGDIAL 2024) constrained LLM generation to ontology terms and relation types. None of these enforce cross-field type constraints (relation domain/range, event argument role-filler types) — the context-sensitive constraints that are well-known to be beyond CFG expressiveness.\\n\\n**Constrained inference for joint IE (non-generative).** EnriCo (Zaratiana et al., arXiv Apr 2024) introduces globally constrained inference for joint entity-relation extraction using Answer Set Programming (ASP) to enforce entity type constraints: unique type assignment, non-overlapping spans, and dataset-specific valid entity-relation type combinations. On ACE05 (7 entity types, 6 relation types), constrained decoding improved relation F1 by ~1 point (69.1 vs. ~68). This is the closest prior work to our constraint enforcement goal, but operates on discriminative span-classification models rather than autoregressive LLM generation, uses ASP solvers incompatible with GPU-accelerated batch serving, and requires manual constraint specification per dataset. SH-ETRs (Expert Systems 2025) learns soft-hard entity type rules for document-level RE, achieving 74.39 F1 on DocRED by combining path-based hard rules with neural soft rules. TyRaL (CEUR 2024) proposes type-constrained rule learning for document-level RE. Both are training-time approaches that learn type constraints from data rather than compiling them from ontology definitions.\\n\\n**Training-time schema compliance.** GoLLIE (Sainz et al., ICLR 2024) achieves strong zero-shot IE by fine-tuning Code-Llama to follow annotation guidelines encoded as Python class schemas, outperforming zero-shot baselines by ~13 F1 points. This represents an orthogonal approach: training-time schema internalization vs. decoding-time constraint enforcement. Whether these are complementary (decoding constraints on GoLLIE-trained models) or redundant is an open empirical question.\\n\\n**Post-processing ontology alignment.** RELATE (arXiv Sep 2025) introduces a three-stage pipeline mapping LLM-extracted biomedical relations to standardized ontology predicates via embedding-based retrieval and LLM reranking, achieving 52% exact match on ChemProt. This is a post-hoc approach — it maps free-text outputs to ontology terms after generation rather than constraining during generation. It addresses vocabulary standardization (mapping synonymous relation descriptions to canonical predicates) rather than type consistency (ensuring argument types match relation constraints).\\n\\n**Constrained decoding quality degradation.** CRANE (Banerjee et al., ICML 2025) proved that constrained decoding to restrictive grammars limits LLMs to TC⁰ complexity, and proposed reasoning-augmented grammars. DCCD (arXiv Mar 2026) demonstrated that standard constrained decoding incurs a cumulative 'projection tax' from repeated reverse-KL projections, and proposed draft-conditioned constrained decoding, achieving +24pp gains on GSM8K with a 1B model — but was evaluated only on reasoning benchmarks, not IE tasks. The Format Tax (arXiv Apr 2026) systematically decomposed constrained decoding quality loss into prompt-level (~70%) and decoder-level (~30%) components, showing that format-requesting instructions cause most accuracy loss before any grammar mask is applied; critically, newer closed-weight models show near-zero format tax, suggesting the problem is solvable through training. The Structure Snowballing phenomenon (arXiv Apr 2026) documented how strict structural constraints trigger cascading formatting errors in Qwen3-8B under constrained decoding. The Hidden Cost of Structure (RANLP 2025) confirmed constrained decoding forces models away from preferred distributions. These findings collectively motivate strategies that minimize the scope and duration of constraint application during IE generation.\\n\\n**Ontology constraint enforcement via alternative mechanisms.** Ontology-to-tools compilation (arXiv Feb 2026) compiles ontologies into tool interfaces for LLM agents — effective but incompatible with batch serving. Ru-LLM (NLPCC 2025) used MCTS with logical rules for document-level RE. Schema RL (ACL 2025) used RL with fine-grained schema validators. Schema Key Wording (arXiv Apr 2026) showed schema naming affects LLM behavior under constrained decoding. PARSE (EMNLP 2025 Industry) optimized schemas for reliable entity extraction.\\n\\n**The key gap:** No existing work (1) automatically compiles IE ontology schemas into decoding-time constraint specifications — a 'zero-code schema compliance' capability where a researcher provides a standard ontology definition and gets a working constrained decoding setup without writing any constraint logic, (2) handles input-dependent cross-field type constraints via stateful entity registries in autoregressive LLM generation, or (3) systematically quantifies ontology type violation rates in unconstrained LLM-based IE to establish whether decoding-time enforcement is warranted.\",\n  \"approach\": \"We develop OntoCoDec (Ontology-Compiled Decoding Constraints), an automatic ontology-to-constraint compiler that translates IE schemas into decoding-time constraint specifications, with explicit mechanisms to mitigate constrained decoding's quality degradation.\\n\\n**Ontology-to-constraint compiler ('zero-code schema compliance').** The compiler takes a standard IE schema definition — expressed as a JSON schema or Python dataclass (entity type hierarchy, relation domain/range signatures, event argument role-filler type constraints) — and emits a two-component constraint specification: (1) an EBNF grammar (XGrammar-2 compatible) enforcing JSON structural validity and type vocabulary constraints — what CFGs can express; (2) a stateful type-masking specification for cross-field constraints — what CFGs cannot. The key user-facing contribution is that a researcher provides a standard ontology definition (e.g., ACE05's 7 entity types + 6 relation type signatures + 33 event type argument specifications) and receives a fully functional constrained decoding setup without implementing any Completion Engines (unlike Synchromesh) or semantic callbacks (unlike IterGen). The grammar component uses XGrammar-2's TagDispatch to switch between free-text span generation and type-constrained fields. The type-masking component maintains a running entity type registry: as entities are generated, their types are recorded; when relation/event argument slots are decoded, the type registry dynamically restricts valid entity references to those satisfying domain/range constraints, with inheritance-aware matching (e.g., GPE satisfies LOC constraints in ACE05's type hierarchy).\\n\\n**Unified LogitsProcessor architecture.** We implement a single unified LogitsProcessor in vLLM V1 that internally manages both constraint layers. vLLM V1's LogitsProcessor API supports loading multiple processors via FQCN registration, and guided decoding is itself implemented as a LogitsProcessor — so our unified processor (1) calls XGrammar's compiled grammar to compute the structural validity mask, (2) computes the type constraint mask from the entity registry, and (3) applies the intersection of both masks to the logits. This approach is architecturally clean: it leverages vLLM's existing batch-granularity LogitsProcessor interface (validate_params, __init__, apply, update_state) and avoids composability issues. The processor operates at (num_requests × vocab_size) tensor granularity, enabling efficient batched inference.\\n\\n**Two primary decoding strategies to navigate the validity-accuracy tradeoff.** Motivated by The Format Tax's finding that prompt-level effects dominate quality degradation and Structure Snowballing's documentation of cascading constraint errors:\\n- **(S1) Direct constrained decoding:** Both grammar and type masks applied throughout generation. Maximizes validity, potential accuracy cost. Serves as the simplest comparison point.\\n- **(S2) Two-pass extraction:** Pass 1 extracts entities with grammar constraints only (entity types are independent, fully CFG-expressible, no semantic masking needed). Pass 2 generates relations/events with an input-dependent grammar compiled from Pass 1's entity outputs — the type constraints become vocabulary constraints in the second pass (only entities matching the domain/range types for each relation are included in the grammar's entity vocabulary), eliminating the need for stateful masking entirely. This is the most novel and IE-specific strategy: it exploits the structure of IE ontologies to convert context-sensitive constraints into context-free ones by conditioning the grammar on prior extraction results. Follows the spirit of Geng et al.'s input-dependent grammars but with inheritance-aware type filtering and automatic compilation.\\n- **(S3, optional/stretch) Draft-conditioned extraction (DCCD-style):** Generate an unconstrained extraction draft first, then re-decode conditioned on the draft with full ontology constraints applied. Included as a comparison point if resources allow, but acknowledged as less IE-specific: DCCD was validated only on reasoning benchmarks (GSM8K), and The Format Tax's finding that decoder-level masking contributes only ~30% of quality loss suggests the projection tax may be smaller for IE's shorter, more structured outputs.\\n\\nThe comparison of S1/S2 (and optionally S3) directly addresses whether semantic constraints help or hurt extraction F1 — a key scientific question beyond the engineering contribution.\\n\\n**Differentiation from Synchromesh, IterGen, and EnriCo.** Unlike Synchromesh, which requires manual Completion Engine implementation for each target language, OntoCoDec automatically compiles standard IE ontology definitions into constraint specifications — no domain-specific programming required. Unlike IterGen, which uses post-hoc semantic checking with backtracking (incompatible with KV-cache-efficient batch serving in vLLM's continuous batching), OntoCoDec uses forward-only logit masking that integrates with standard autoregressive serving pipelines. Unlike EnriCo, which uses ASP solvers for constrained inference on discriminative span-classification models and requires manual constraint specification, OntoCoDec operates on autoregressive LLM generation, automatically compiles constraints from ontology definitions, and uses GPU-native logit masking compatible with batch serving. The IE domain also introduces challenges absent from code generation: input-dependent constraints (the valid set of relation arguments changes as entities are generated), inheritance-aware type matching (ontology hierarchies), and schema variability across IE tasks (ACE05 vs. SciERC have different ontologies, both handled by the same compiler).\\n\\n**Evaluation.** We evaluate on two IE datasets with complementary ontology structures, both featuring relation types with domain/range constraints that test the core novel contribution:\\n- **ACE05** (news, 7 entity types, 6 relation types with domain/range constraints, 33 event types with typed argument roles) — the richest ontology constraint structure, testing both relation and event argument type constraints.\\n- **SciERC** (scientific abstracts, 6 entity types, 7 relation types) — different domain, simpler ontology, tests compiler generalization across schemas.\\n\\nBoth datasets have explicit entity type constraints on relation arguments, directly testing the cross-field type constraint contribution. This focused selection (vs. including GENIA, which has no relation types and would only test entity vocabulary constraints trivially handled by grammar-only decoding) ensures every experiment exercises the novel constraint mechanism.\\n\\nPrimary model: Qwen3-8B served via vLLM (using enable_thinking=True with /no_think prompt suffix per resolved issue #18819, or vLLM ≥0.9.0). Secondary model: Llama-3.1-8B-Instruct (cross-model generalization, lower priority if budget constrained).\\n\\nBaselines: (1) Unconstrained generation (establishes type violation rate — the first-order empirical contribution), (2) JSON-only constrained decoding (XGrammar-2, grammar constraints only — no semantic enforcement), (3) Unconstrained + post-hoc type filtering (extract with no semantic constraints, then filter/reject outputs violating ontology type constraints — the natural non-decoding-time alternative that directly tests whether decoding-time enforcement outperforms post-hoc validation), (4) GoLLIE (training-time schema compliance — tests whether decoding-time and training-time approaches are complementary or redundant).\\n\\nMetrics: extraction F1 (entities, relations, events separately), semantic validity rate (% outputs satisfying all ontology constraints), constraint violation rate by category (entity type, relation domain/range, event argument role-filler), validity-vs-F1 tradeoff across S1/S2, and per-step latency overhead.\\n\\n**Acknowledging the violation rate risk.** If unconstrained LLM-based IE produces ontology type violations at rates <5%, the decoding-time enforcement contribution becomes primarily negative — establishing that LLMs implicitly learn type constraints, and the engineering complexity of decoding-time enforcement is unjustified. We explicitly frame this as a valuable finding: the quantification of violation rates across two datasets and two models is a first-order contribution regardless of direction. The automatic compiler and LogitsProcessor architecture remain useful engineering contributions for applications requiring guaranteed type validity (e.g., knowledge graph population with strict schema compliance).\\n\\n**Key scientific contributions beyond engineering:** (a) First systematic quantification of ontology type violation rates in unconstrained LLM-based IE across multiple datasets and models — establishing the empirical foundation for whether this problem warrants solution. (b) Comparison of constraint enforcement strategies (forward masking S1 vs. two-pass S2 vs. post-hoc filtering) — answering whether and how semantic constraints affect extraction F1. (c) Empirical test of whether decoding-time constraints complement or substitute training-time schema compliance (GoLLIE comparison). (d) Analysis of which constraint types (entity vocabulary, relation domain/range, event argument role-filler) contribute most to validity and F1 improvements — granular ablation of the constraint hierarchy. (e) First automatic 'zero-code' compiler from IE ontology definitions to decoding-time constraint specifications.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~170h H100-80GB (2 datasets × 2 models × 2 primary strategies × 4 baselines + ablations)\",\n      \"gpu_utilization\": \"~15-25% — GPU idles during compiler implementation, LogitsProcessor debugging, and constraint specification iteration\",\n      \"timeline\": \"3-5 months\",\n      \"team\": \"1-2 researchers (1 NLP + 1 systems)\",\n      \"estimated_gpu_cost\": \"$340-595 at ~$2.00-3.50/hr H100\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200h H100-80GB\",\n      \"gpu_utilization\": \"~40-55% — agent handles constraint specification generation, experiment execution, and result parsing; human reviews LogitsProcessor correctness and validates constraint coverage\",\n      \"timeline\": \"5-7 weeks\",\n      \"team\": \"1 researcher, ~60min/day reviewing compiler output, LogitsProcessor state transitions, and validity-vs-F1 tradeoff analysis\",\n      \"claude_api_cost\": \"$150-350 (~1500-3500 Opus turns for compiler iteration, experiment orchestration, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$400-700\",\n      \"risk_note\": \"Unified LogitsProcessor correctness requires careful validation — subtle bugs in mask intersection or entity registry updates may silently permit invalid extractions or over-constrain valid ones. Risk mitigated by focusing on S1/S2 (forward-only, no re-decoding complexity).\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~350h H100-80GB (2 datasets × 2 models × 2 strategies × 4 baselines × ablations over constraint granularity and type hierarchy depth)\",\n      \"gpu_utilization\": \"~80-90% — agent pipelines experiments continuously across datasets and configurations\",\n      \"timeline\": \"12-18 days with 2 H100 GPUs available concurrently\",\n      \"team\": \"0 (initial setup: schema definitions, dataset paths, evaluation scripts)\",\n      \"claude_api_cost\": \"$250-550 (~3000-5500 Opus turns for iterative constraint refinement, multi-dataset experiment orchestration, failure diagnosis, and paper writing)\",\n      \"estimated_gpu_cost\": \"$700-1225\",\n      \"speed_bottleneck\": \"GPU count (parallel ablations across 2 datasets × 2 strategies require multiple concurrent vLLM instances) and LogitsProcessor debugging cycle\",\n      \"risk_note\": \"Automated LogitsProcessor generation for ACE05's event ontology (33 event types with typed argument roles) may require manual intervention for edge cases in type hierarchy resolution\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline: May 25, 2026 — tight but feasible with focused ACE05 + SciERC evaluation)\",\n    \"AACL-IJCNLP 2026 (ARR submission deadline: May 25, 2026 — same cycle, must select target at submission)\",\n    \"AAAI 2027 (expected deadline: ~August 1, 2026 — allows complete evaluation with all ablations)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Synchromesh: Reliable Code Generation from Pre-trained Language Models (ICLR 2022, Poesia et al.) — foundational two-layer syntactic+semantic constrained decoding via Completion Engines\",\n    \"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking (ICLR 2025, Ugare et al.) — grammar+semantic callback paradigm with backtracking; key comparison for forward-only vs. backtracking design choice\",\n    \"CRANE: Reasoning with Constrained LLM Generation (ICML 2025, Banerjee et al.) — theoretical proof that strict grammar constraints limit LLMs to TC⁰; motivates reasoning-augmented and draft-conditioned alternatives\",\n    \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024, Sainz et al.) — training-time schema compliance baseline; tests complementarity with decoding-time constraints\",\n    \"GenIE: Generative Information Extraction (NAACL 2022, Josifoski et al.) — bi-level constrained generation for IE with prefix trie vocabulary constraints; precursor lacking cross-field type enforcement\",\n    \"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction (arXiv Apr 2024, Zaratiana et al.) — ASP-based constrained inference enforcing entity type constraints for joint IE; reports ~1 F1 improvement from constraints on ACE05; closest prior work but non-generative and requires manual constraint specification\",\n    \"RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints (arXiv Sep 2025) — post-processing pipeline mapping LLM-extracted relations to standardized ontology predicates; addresses vocabulary standardization rather than decoding-time type consistency\",\n    \"SH-ETRs: Learning Soft-Hard Rules with Entity Type Constraints for Document-Level Relation Extraction (Expert Systems 2025) — training-time entity type rule learning for DocRE; alternative constraint enforcement via learned rules rather than ontology compilation\",\n    \"TyRaL: End-to-End Document-level Relation Extraction via Type-Constrained Rule Learning (CEUR 2024) — type-constrained rule learning for DocRE; training-time approach complementary to decoding-time enforcement\",\n    \"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs (arXiv Jan 2026, Li et al.) — TagDispatch mechanism for free-text/structured switching; grammar backend\",\n    \"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models (MLSys 2025)\",\n    \"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs (arXiv Mar 2026) — projection tax analysis and draft-conditioned alternative; evaluated on reasoning benchmarks only (GSM8K), not IE; informs our optional S3 strategy\",\n    \"The Format Tax (arXiv Apr 2026) — systematic decomposition of constrained decoding quality loss: prompt-level effects (~70%) dominate over decoder-level grammar masking (~30%); newer closed-weight models show near-zero tax; informs our two-pass strategy design\",\n    \"From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection (arXiv Apr 2026) — documents cascading formatting errors under strict structural constraints in Qwen3-8B; motivates minimizing constraint scope during generation\",\n    \"Thinking Before Constraining: A Unified Decoding Framework for Large Language Models (arXiv Jan 2026)\",\n    \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance (RANLP 2025) — empirical confirmation of quality degradation under constrained decoding\",\n    \"Type-Constrained Code Generation with Language Models (PLDI 2025) — demonstrates cross-field type constraints are context-sensitive, beyond CFG expressiveness\",\n    \"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning (EMNLP 2023, Geng et al.) — input-dependent grammars for closed IE\",\n    \"Lazy-k Decoding: Constrained Decoding for Information Extraction (EMNLP 2023, Hemmer et al.)\",\n    \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction (EMNLP 2025 Industry)\",\n    \"Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents (arXiv Feb 2026)\",\n    \"Scientific Knowledge-driven Decoding Constraints (arXiv Apr 2026, SciDC)\",\n    \"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction (NLPCC 2025, Ru-LLM)\",\n    \"Grammar-constrained decoding for structured information extraction with fine-tuned generative models (Frontiers AI 2024)\",\n    \"Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding (arXiv Apr 2026)\",\n    \"Learning to Generate Structured Output with Schema Reinforcement Learning (ACL 2025)\",\n    \"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding (SIGDIAL 2024)\"\n  ],\n  \"description\": \"We propose OntoCoDec, an automatic ontology-to-constraint compiler that translates IE schemas into decoding-time constraint specifications enforced during LLM generation — enabling 'zero-code schema compliance' where a researcher provides a standard ontology definition (JSON/Python dataclass) and receives a working constrained decoding setup without writing any constraint logic. Unlike prior grammar+semantic-callback paradigms (Synchromesh, ICLR 2022; IterGen, ICLR 2025) which require manual constraint implementation for code generation domains, and unlike EnriCo (arXiv 2024) which uses ASP solvers for discriminative models, OntoCoDec automatically compiles standard IE ontology definitions — entity type hierarchies, relation domain/range signatures, event argument role-filler constraints — into a unified LogitsProcessor that combines grammar-based structural masking (via XGrammar-2) with stateful type-constraint masking via a dynamic entity type registry, operating within vLLM V1's batch-serving pipeline. We implement and compare two primary strategies: (S1) direct constrained decoding with full grammar+type masking, and (S2) two-pass extraction where entity types extracted in Pass 1 are compiled into input-dependent grammars for Pass 2, converting context-sensitive type constraints into context-free vocabulary constraints — the most novel and IE-specific strategy. Draft-conditioned extraction (S3, DCCD-style) is included as an optional comparison. We evaluate on ACE05 (7 entity types, 6 relation types, 33 event types — rich ontology) and SciERC (6 entity types, 7 relation types — different domain), using Qwen3-8B and Llama-3.1-8B. Baselines include unconstrained generation (establishing violation rates), JSON-only grammar constraints, post-hoc type filtering (testing whether decoding-time enforcement outperforms post-hoc validation), and GoLLIE (testing complementarity with training-time schema compliance). The key scientific contributions are: (1) first systematic quantification of ontology type violation rates in unconstrained LLM-based IE — valuable regardless of whether rates are high (justifying enforcement) or low (establishing LLMs implicitly learn constraints); (2) comparison of constraint enforcement strategies revealing the validity-vs-accuracy tradeoff; (3) empirical test of decoding-time vs. training-time schema compliance complementarity; (4) granular ablation of which ontology constraint types contribute most to validity and F1.\",\n  \"project_name\": \"schema_semantic_constrained_ie\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: Context-free grammars cannot enforce cross-field back-reference constraints. The claim that 'a PER-ORG relation non-terminal can only derive entity spans previously tagged as PER in the subject slot' requires context-sensitive language properties. This is not a CFG limitation that can be worked around — it's a fundamental result in formal language theory (Chomsky hierarchy). The Type-Constrained Code Generation paper (arXiv:2504.09246, Apr 2025) explicitly demonstrates that type constraints exceed CFG expressiveness.\", \"CRITICAL: Misunderstanding of XGrammar's 'context-dependent token masking'. XGrammar categorizes tokens as context-independent (decidable from local automata state) vs context-dependent (requiring full PDA stack state). This is about grammar rule nesting/recursion — NOT about conditioning on previously generated content values. The proposal incorrectly equates these two very different concepts.\", \"Missing XGrammar-2 (arXiv:2601.04426, Jan 2026): This major update introduces mask_callback() for custom constraint functions and TagDispatch for dynamic structure switching. The mask_callback interface is actually the mechanism needed for content-dependent semantic constraints — but it's NOT grammar-based. The proposal should build on XGrammar-2, not XGrammar-1.\", \"Missing Draft-Conditioned Constrained Decoding (arXiv:2603.03305, Mar 2026): Directly addresses the distortion problem of constrained decoding on semantics — relevant baseline that should be compared.\", \"Missing 'Thinking Before Constraining' (arXiv:2601.07525, Jan 2026): Proposes free reasoning before constraint enforcement, achieving up to 27% accuracy gains. Relevant concurrent work.\", \"Missing Schema Reinforcement Learning (ACL 2025): Uses RL with schema validators for structured generation — an alternative approach to ensuring schema compliance.\", \"Missing Ru-LLM (NLPCC 2025): Logical rule-constrained LLMs for document-level RE using MCTS — directly addresses type constraints for relation extraction.\", \"Novelty over Geng et al. (EMNLP 2023) is unclear: That paper already demonstrated grammar-constrained decoding for IE (closed IE on Wikidata with entity/relation vocabulary constraints). The proposed extension to type-hierarchy constraints is either infeasible (strong version) or incremental (weak version).\", \"Resource estimates use A100-hours but user constraint specifies H100-hours. While roughly compatible given ~2x speedup, this should be addressed.\", \"The 16-day timeline is very aggressive for: (1) developing a novel ontology-to-grammar compiler, (2) debugging EBNF rules for 3 different IE schemas, (3) running experiments on ACE05 + SciERC + TACRED with 2 model sizes, (4) implementing baselines (BoostCD), and (5) writing the paper.\"]\nFeedback: The core intuition — that IE-specific constraints should be enforced during decoding, not just JSON syntax — is valuable and worth pursuing. However, the proposal fundamentally misidentifies the mechanism. Here is how to fix it:\n\n1. **Abandon the pure-CFG approach for cross-field constraints.** CFGs cannot enforce that entity spans match type labels assigned elsewhere in the output. Instead, explore:\n   - **XGrammar-2's mask_callback()**: Use a custom logit processor that tracks generated entity types and dynamically restricts valid relation arguments. This is NOT grammar-based but achieves the desired semantic enforcement. Frame the contribution as a hybrid grammar+callback system.\n   - **Two-pass approach**: First generate entities with type-constrained grammar, then generate relations with an input-dependent grammar conditioned on extracted entities (similar to Geng et al.'s input-dependent grammars). This IS expressible as a CFG because the grammar for pass 2 is compiled from pass 1's output.\n   - **Draft-conditioned constrained decoding**: Generate unconstrained draft, then use ontology-derived grammar for the structured realization pass.\n\n2. **Clearly differentiate from Geng et al. (2023)**: That paper already did grammar-constrained IE. Articulate what is NEW: the ontology compiler, the multi-level constraint hierarchy, the near-zero overhead via XGrammar-2.\n\n3. **Address concurrent work**: Compare against DCCD (Mar 2026), discuss XGrammar-2 as the implementation substrate, position against Schema RL (ACL 2025) and Ru-LLM.\n\n4. **Narrow the scope for 16 days**: Focus on ONE dataset (ACE05 joint IE) and ONE model (Qwen3-8B for feasibility). Drop TACRED (relation-only, less interesting for joint constraints). Add other datasets only if time permits.\n\n5. **Reframe the contribution**: Instead of 'compile ontology into CFG', frame as 'ontology-aware structured decoding via hybrid grammar-callback constraints' that leverages XGrammar-2's extensibility. The compiler still exists but outputs grammar + callback specifications, not pure EBNF.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL: Missing discussion of IterGen (ICLR 2025, Ugare et al.) — the most closely related prior work. IterGen implements grammar-guided generation with semantic-aware backtracking via user-defined callbacks, essentially the same grammar+callback paradigm applied to code generation. The proposal lists IterGen in references but does not discuss it in the landscape, failing to articulate what is novel beyond domain transfer from code to IE.\", \"CRITICAL: Missing discussion of Synchromesh/Constrained Semantic Decoding (ICLR 2022, Poesia et al.) — the foundational work on combining syntactic and semantic constraints during decoding. Not cited at all. This is the intellectual ancestor of the proposed approach.\", \"Missing discussion of CRANE (ICML 2025, Banerjee et al.) which demonstrates that strict grammar enforcement during decoding degrades LLM reasoning quality. The proposal's dual-layer constraints (grammar + logit masking) could similarly degrade extraction accuracy. This tension needs to be acknowledged and addressed — possibly by incorporating free-reasoning windows or comparing against DCCD-style draft-then-constrain alternatives.\", \"Missing GoLLIE (ICLR 2024) as a baseline — the leading open LLM-based IE system that uses code-based schemas for structured extraction without constrained decoding. A natural comparison: does adding decoding-time constraints improve over GoLLIE's training-time approach?\", \"XGrammar + custom LogitsProcessor composability is an engineering risk. In vLLM V1, guided decoding (XGrammar) is configured via SamplingParams.guided_decoding while custom LogitsProcessors go through a separate init-time registration path. No documented API supports combining both in the same request. The proposal should acknowledge this and describe a concrete solution (e.g., a unified wrapper processor).\", \"Evaluation scope (ACE05 only, Qwen3-8B only) is too narrow for EMNLP main track. Reviewers will expect at least 2-3 IE datasets (e.g., ACE05 + SciERC or DocRED) and ideally results showing the approach generalizes across model families or sizes.\", \"The 'provably beyond CFG expressiveness' framing is overstated. The PLDI 2025 paper observes this well-known fact from formal language theory as motivation for its prefix automata — it does not prove a novel theorem about IE constraints. Rephrase as 'well-known that cross-field type constraints are context-sensitive, requiring mechanisms beyond CFGs.'\", \"Known Qwen3 + vLLM structured output bug (GitHub issue #18819): structured output with enable_thinking=False produces malformed JSON. Workaround exists (enable_thinking=True + /no_think prompt suffix) but should be noted as an implementation consideration.\", \"The contribution risks being perceived as primarily engineering (ontology compiler + logit processor implementation) rather than scientific insight. To elevate beyond a systems paper, the authors should include: (a) analysis of what fraction of extraction errors are type violations (quantifying the problem), (b) comparison of constraint enforcement strategies (single-pass vs two-pass vs draft-conditioned), and (c) analysis of whether semantic constraints help or hurt extraction F1 (not just validity rate).\"]\nFeedback: The revised proposal correctly addresses the round 1 criticism about CFG limitations by adopting a hybrid grammar+callback architecture. This is technically sound. However, the novelty positioning has a critical gap: IterGen (ICLR 2025) and Synchromesh (ICLR 2022) already implement the grammar+semantic-callback paradigm for code generation. The paper MUST discuss both and clearly articulate what's novel beyond domain transfer. Here's how to strengthen:\n\n1. **Position against IterGen and Synchromesh explicitly.** IterGen uses backtracking on constraint violation; your approach uses forward-only masking (no backtracking). Synchromesh targets code semantics; you target IE ontology semantics. Articulate why the IE domain requires different design choices (e.g., entity type registries, input-dependent grammars from extracted entities).\n\n2. **Address CRANE's quality degradation concern.** Acknowledge that constrained decoding can hurt generation quality. Consider: (a) measuring extraction F1 degradation vs. validity improvement tradeoff, (b) a DCCD-style draft-conditioned variant where constraints don't affect the initial generation.\n\n3. **Add GoLLIE as a baseline.** This comparison is highly informative: training-time schema compliance (GoLLIE) vs. decoding-time constraint enforcement (your approach). If they're complementary, that's a strong result.\n\n4. **Expand evaluation if at all possible.** Add SciERC (different domain, different ontology complexity) to show the compiler generalizes. Even preliminary results on a second dataset would strengthen the paper significantly.\n\n5. **Quantify the problem first.** Before showing the solution works, show the problem matters: run unconstrained Qwen3-8B on ACE05 and report what fraction of outputs contain type violations. If it's 30%, the contribution is clearly valuable. If it's 3%, the impact is limited.\n\n6. **Solve the composability problem explicitly.** Describe the concrete implementation plan: will you build a unified LogitsProcessor that internally calls XGrammar's grammar masking and your type constraint masking? Or will you implement both layers in a single custom processor? This is a practical blocker that reviewers will ask about.\n\n7. **Soften the 'provably beyond CFG' language.** Say 'cross-field type constraints are context-sensitive and cannot be expressed as CFGs' without claiming this is a novel proof.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"HARD CONSTRAINT VIOLATION: Manual GPU estimate of ~250h H100-80GB exceeds the user's hard constraint of ≤200 H100-hours. With 3 datasets × 2 models × 3 strategies × 5 baselines = 30 configurations, this needs scoping down. Dropping GENIA and focusing on ACE05 + SciERC with one primary model (Qwen3-8B) and Llama-3.1-8B as secondary would bring it to ~150-180h.\", \"The claimed '15-40% type violation rate' for unconstrained LLM-based IE is unsubstantiated — no citation or preliminary evidence supports this. The only data point I found suggests ~12% invalid response rate for GPT-4 on complex extraction (including all error types, not just ontology violations). If the actual ontology type violation rate is <5%, the entire motivation for decoding-time enforcement weakens significantly. The proposal correctly frames quantifying this as a contribution, but the risk of a negative result (low violation rate → minimal impact) should be acknowledged.\", \"GENIA evaluation is misaligned with the novel contribution. GENIA has 5 entity types but NO relation types — it only tests entity vocabulary constraints, which are trivially handled by grammar-only constrained decoding. The novel contribution (cross-field type constraints: relation domain/range, event argument role-filler) cannot be tested on GENIA. Recommend replacing GENIA with a dataset that has rich relation/event ontology constraints, or clearly framing GENIA as entity-only ablation.\", \"Missing related work: (1) RELATE (arXiv Sep 2025) — ontology-constrained relation extraction in biomedical domain via post-processing pipeline mapping LLM outputs to ontology predicates; (2) EnriCo (arXiv Apr 2024) — globally constrained inference for joint entity-relation extraction using decoding algorithms with task/dataset-specific constraints; (3) SH-ETRs and TyRaL — entity type constraint learning for document-level RE. These are training-time or post-processing approaches, distinct from decoding-time enforcement, but should be discussed to complete the landscape of ontology constraint enforcement mechanisms.\", \"The DCCD-style draft-conditioned strategy (S3) doubles inference cost per sample (two full forward passes) and has not been validated on IE tasks — DCCD was evaluated only on reasoning benchmarks (GSM8K). There's a risk that the draft-conditioned approach doesn't transfer well to IE because IE outputs are shorter and more structured than reasoning chains, potentially reducing the projection tax that DCCD is designed to mitigate. This risk should be acknowledged.\", \"Timeline risk for 16 days: The unified LogitsProcessor requires careful engineering — mask intersection between XGrammar's structural mask and the type constraint mask must be correct for every token position, and the entity registry must handle incremental updates correctly as entities are generated. Debugging this for 2-3 different ontology schemas (ACE05's 7 entity types + 6 relation types + 33 event types vs. SciERC's 6+7) is non-trivial. Recommend implementing S1 (direct constrained) and S2 (two-pass) first, with S3 (draft-conditioned) as a stretch goal.\", \"BoostCD/BoostIE (EMNLP 2025) was evaluated on Wiki-cIE using Wikidata, not on ACE05/SciERC. Reproducing BoostIE on ACE05/SciERC within 16 days as a baseline may require non-trivial adaptation. Consider replacing with a simpler baseline: unconstrained + post-hoc type filtering (extract with no constraints, then filter outputs violating ontology constraints). This provides a natural comparison point (decoding-time vs. post-hoc enforcement) with minimal implementation overhead.\"]\nFeedback: The proposal has improved substantially from rounds 1-2. The hybrid grammar+type-masking architecture is technically sound, the positioning against Synchromesh/IterGen/CRANE/DCCD is well-done, and the scientific questions are well-formulated. To reach pass quality, address these specific points:\n\n1. **Fix the resource budget**: Scope down to ACE05 + SciERC (drop GENIA), Qwen3-8B as primary model, Llama-3.1-8B as secondary. Target ~150-180 H100-hours. This also improves the paper's focus: both ACE05 and SciERC have relation types, so the cross-field type constraint contribution is consistently tested.\n\n2. **Acknowledge the violation rate risk**: State explicitly that if ontology type violations are <5%, the decoding-time enforcement may not justify its complexity. Frame the quantification as a first-order contribution regardless of the finding direction (positive: constraints help; negative: constraints are unnecessary, saving the community effort pursuing this direction).\n\n3. **Prioritize strategies S1 and S2**: Two-pass extraction (S2) is the most novel and IE-specific strategy — it turns cross-field type constraints into vocabulary constraints by conditioning the second pass on first-pass entities. Direct constrained (S1) is the simplest comparison point. Draft-conditioned (S3) is the most engineering-intensive and least IE-specific — make it optional.\n\n4. **Replace BoostIE baseline with post-hoc filtering**: Unconstrained extraction → post-hoc ontology constraint checking/filtering is a natural, easy-to-implement baseline that directly tests whether decoding-time enforcement outperforms post-hoc validation.\n\n5. **Add the missing related work** (RELATE, EnriCo, SH-ETRs) with one sentence each positioning them as alternative constraint enforcement mechanisms (training-time, post-processing) vs. your decoding-time approach.\n\n6. **Strengthen the novelty pitch**: The strongest novelty argument is that OntoCoDec is the first *automatic* compiler from IE ontology definitions to constraint specifications — unlike Synchromesh's manual Completion Engines or IterGen's manual callbacks. Emphasize that a researcher can provide a standard ontology definition (JSON/Python dataclass) and get a working constrained decoding setup without writing any constraint logic. This 'zero-code schema compliance' angle is practically very appealing.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-11T23:56:32.313Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-11T23:56:32.313Z",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-11T23:56:32.351Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-11 (UTC).**

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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?
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
  "title": "Ontology-Faithful Information Extraction via Compiled Semantic Constraints: Automatic Ontology-to-Decoder Compilation with Forward-Only Type Masking",
  "core_problem": "Can we automatically compile IE ontology schemas — entity type hierarchies, relation domain/range restrictions, event argument role-filler types — into efficient decoding-time constraint specifications that enforce semantic validity without degrading extraction accuracy, and what is the actual rate of ontology constraint violations in unconstrained LLM-based IE — is it significant enough to warrant decoding-time enforcement?",
  "opportunity": "LLM-based IE systems produce structurally valid but semantically invalid outputs at unknown rates: while structural validity (valid JSON, correct field names) is now reliably enforced by grammar-constrained decoding (XGrammar-2, default in vLLM/SGLang/TensorRT-LLM since 2026), no existing system enforces semantic validity — cross-field type constraints such as relation domain/range restrictions or event argument role-filler types. For instance, an ACE05 PHYS.Located relation requires a PER/GPE Arg-1 and a FAC/LOC/GPE Arg-2; a system that assigns two ORG entities produces structurally valid but semantically invalid output. Although the exact prevalence of such violations in LLM-based IE is unknown (no prior work has systematically measured it), the existence of the gap between grammar-enforceable structural constraints and the context-sensitive semantic constraints that ontologies specify creates a clear engineering and scientific opportunity. If violation rates are non-trivial (>5%), decoding-time enforcement directly improves output quality. If rates are low (<5%), this is an important negative result establishing that LLMs implicitly learn ontology constraints from training data, saving the community effort pursuing constrained decoding for semantic validity. Either way, the quantification itself is a first-order contribution. The grammar+semantic-callback paradigm for constrained decoding has been explored in code generation — Synchromesh (ICLR 2022) introduced two-layer Completion Engines combining syntactic and semantic constraints, and IterGen (ICLR 2025) added backtracking with user-defined semantic callbacks — but no existing work automatically compiles IE ontology schemas into such constraint systems. IE ontologies present unique challenges absent from code generation: (1) constraints are input-dependent (valid relation arguments depend on which entity types have been extracted so far, requiring a dynamic entity type registry), (2) ontology type hierarchies create inheritance-aware constraints (a GPE-typed entity can fill a LOC argument slot), and (3) the constraint graph is schema-specific and varies across IE tasks, requiring automatic compilation rather than manual Completion Engine implementation. Furthermore, recent work demonstrates that constrained decoding degrades generation quality: The Format Tax (arXiv Apr 2026) shows that format-requesting prompts account for ~70% of the quality loss while grammar masking contributes only ~30%, and the Structure Snowballing phenomenon (arXiv Apr 2026) documents how strict structural constraints can trigger cascading errors in Qwen3-8B. These findings motivate our two-pass strategy (S2), which avoids applying semantic constraints during entity extraction and instead compiles them into vocabulary constraints for a second pass.",
  "landscape": "**Grammar+semantic constraint paradigm (code generation).** Synchromesh (Poesia et al., ICLR 2022) is the foundational work combining syntactic and semantic constraints during decoding. Its Constrained Semantic Decoding (CSD) framework defines Completion Engines with two layers — a context-free layer for syntactic validity and a context-sensitive layer for semantic constraints (scope, typing, contextual logic) — applied to SQL, Vega-Lite, and SMCalFlow code generation. IterGen (Ugare et al., ICLR 2025) extends this paradigm with backtracking: users define semantic callbacks that check generated content at grammar symbol boundaries, and the system backtracks via KV cache state restoration when violations are detected, achieving 18.5% improvement over forward-only grammar-guided generation on SQL/Vega-Lite. Both require manual implementation of domain-specific constraint logic (Completion Engines or callbacks). Neither addresses IE ontology constraints or automatic constraint compilation from schema definitions.\n\n**Constrained decoding for IE.** GenIE (Josifoski et al., NAACL 2022) pioneered bi-level constrained generation for IE with structural constraints and prefix trie vocabulary constraints, but enforces only entity/relation name validity, not cross-field type consistency. Geng et al. (EMNLP 2023) demonstrated input-dependent grammars for closed IE on Wikidata, again limited to vocabulary membership. Schmidt & Cimiano (Frontiers AI 2024) applied grammar-constrained decoding to clinical IE. Lazy-k (Hemmer et al., EMNLP 2023) explored constrained decoding for token classification IE. SciDC (arXiv Apr 2026) introduced multi-layer decoding constraints for scientific domains but uses hand-crafted rules. Dialogue Ontology RE (SIGDIAL 2024) constrained LLM generation to ontology terms and relation types. None of these enforce cross-field type constraints (relation domain/range, event argument role-filler types) — the context-sensitive constraints that are well-known to be beyond CFG expressiveness.\n\n**Constrained inference for joint IE (non-generative).** EnriCo (Zaratiana et al., arXiv Apr 2024) introduces globally constrained inference for joint entity-relation extraction using Answer Set Programming (ASP) to enforce entity type constraints: unique type assignment, non-overlapping spans, and dataset-specific valid entity-relation type combinations. On ACE05 (7 entity types, 6 relation types), constrained decoding improved relation F1 by ~1 point (69.1 vs. ~68). This is the closest prior work to our constraint enforcement goal, but operates on discriminative span-classification models rather than autoregressive LLM generation, uses ASP solvers incompatible with GPU-accelerated batch serving, and requires manual constraint specification per dataset. SH-ETRs (Expert Systems 2025) learns soft-hard entity type rules for document-level RE, achieving 74.39 F1 on DocRED by combining path-based hard rules with neural soft rules. TyRaL (CEUR 2024) proposes type-constrained rule learning for document-level RE. Both are training-time approaches that learn type constraints from data rather than compiling them from ontology definitions.\n\n**Training-time schema compliance.** GoLLIE (Sainz et al., ICLR 2024) achieves strong zero-shot IE by fine-tuning Code-Llama to follow annotation guidelines encoded as Python class schemas, outperforming zero-shot baselines by ~13 F1 points. This represents an orthogonal approach: training-time schema internalization vs. decoding-time constraint enforcement. Whether these are complementary (decoding constraints on GoLLIE-trained models) or redundant is an open empirical question.\n\n**Post-processing ontology alignment.** RELATE (arXiv Sep 2025) introduces a three-stage pipeline mapping LLM-extracted biomedical relations to standardized ontology predicates via embedding-based retrieval and LLM reranking, achieving 52% exact match on ChemProt. This is a post-hoc approach — it maps free-text outputs to ontology terms after generation rather than constraining during generation. It addresses vocabulary standardization (mapping synonymous relation descriptions to canonical predicates) rather than type consistency (ensuring argument types match relation constraints).\n\n**Constrained decoding quality degradation.** CRANE (Banerjee et al., ICML 2025) proved that constrained decoding to restrictive grammars limits LLMs to TC⁰ complexity, and proposed reasoning-augmented grammars. DCCD (arXiv Mar 2026) demonstrated that standard constrained decoding incurs a cumulative 'projection tax' from repeated reverse-KL projections, and proposed draft-conditioned constrained decoding, achieving +24pp gains on GSM8K with a 1B model — but was evaluated only on reasoning benchmarks, not IE tasks. The Format Tax (arXiv Apr 2026) systematically decomposed constrained decoding quality loss into prompt-level (~70%) and decoder-level (~30%) components, showing that format-requesting instructions cause most accuracy loss before any grammar mask is applied; critically, newer closed-weight models show near-zero format tax, suggesting the problem is solvable through training. The Structure Snowballing phenomenon (arXiv Apr 2026) documented how strict structural constraints trigger cascading formatting errors in Qwen3-8B under constrained decoding. The Hidden Cost of Structure (RANLP 2025) confirmed constrained decoding forces models away from preferred distributions. These findings collectively motivate strategies that minimize the scope and duration of constraint application during IE generation.\n\n**Ontology constraint enforcement via alternative mechanisms.** Ontology-to-tools compilation (arXiv Feb 2026) compiles ontologies into tool interfaces for LLM agents — effective but incompatible with batch serving. Ru-LLM (NLPCC 2025) used MCTS with logical rules for document-level RE. Schema RL (ACL 2025) used RL with fine-grained schema validators. Schema Key Wording (arXiv Apr 2026) showed schema naming affects LLM behavior under constrained decoding. PARSE (EMNLP 2025 Industry) optimized schemas for reliable entity extraction.\n\n**The key gap:** No existing work (1) automatically compiles IE ontology schemas into decoding-time constraint specifications — a 'zero-code schema compliance' capability where a researcher provides a standard ontology definition and gets a working constrained decoding setup without writing any constraint logic, (2) handles input-dependent cross-field type constraints via stateful entity registries in autoregressive LLM generation, or (3) systematically quantifies ontology type violation rates in unconstrained LLM-based IE to establish whether decoding-time enforcement is warranted.",
  "approach": "We develop OntoCoDec (Ontology-Compiled Decoding Constraints), an automatic ontology-to-constraint compiler that translates IE schemas into decoding-time constraint specifications, with explicit mechanisms to mitigate constrained decoding's quality degradation.\n\n**Ontology-to-constraint compiler ('zero-code schema compliance').** The compiler takes a standard IE schema definition — expressed as a JSON schema or Python dataclass (entity type hierarchy, relation domain/range signatures, event argument role-filler type constraints) — and emits a two-component constraint specification: (1) an EBNF grammar (XGrammar-2 compatible) enforcing JSON structural validity and type vocabulary constraints — what CFGs can express; (2) a stateful type-masking specification for cross-field constraints — what CFGs cannot. The key user-facing contribution is that a researcher provides a standard ontology definition (e.g., ACE05's 7 entity types + 6 relation type signatures + 33 event type argument specifications) and receives a fully functional constrained decoding setup without implementing any Completion Engines (unlike Synchromesh) or semantic callbacks (unlike IterGen). The grammar component uses XGrammar-2's TagDispatch to switch between free-text span generation and type-constrained fields. The type-masking component maintains a running entity type registry: as entities are generated, their types are recorded; when relation/event argument slots are decoded, the type registry dynamically restricts valid entity references to those satisfying domain/range constraints, with inheritance-aware matching (e.g., GPE satisfies LOC constraints in ACE05's type hierarchy).\n\n**Unified LogitsProcessor architecture.** We implement a single unified LogitsProcessor in vLLM V1 that internally manages both constraint layers. vLLM V1's LogitsProcessor API supports loading multiple processors via FQCN registration, and guided decoding is itself implemented as a LogitsProcessor — so our unified processor (1) calls XGrammar's compiled grammar to compute the structural validity mask, (2) computes the type constraint mask from the entity registry, and (3) applies the intersection of both masks to the logits. This approach is architecturally clean: it leverages vLLM's existing batch-granularity LogitsProcessor interface (validate_params, __init__, apply, update_state) and avoids composability issues. The processor operates at (num_requests × vocab_size) tensor granularity, enabling efficient batched inference.\n\n**Two primary decoding strategies to navigate the validity-accuracy tradeoff.** Motivated by The Format Tax's finding that prompt-level effects dominate quality degradation and Structure Snowballing's documentation of cascading constraint errors:\n- **(S1) Direct constrained decoding:** Both grammar and type masks applied throughout generation. Maximizes validity, potential accuracy cost. Serves as the simplest comparison point.\n- **(S2) Two-pass extraction:** Pass 1 extracts entities with grammar constraints only (entity types are independent, fully CFG-expressible, no semantic masking needed). Pass 2 generates relations/events with an input-dependent grammar compiled from Pass 1's entity outputs — the type constraints become vocabulary constraints in the second pass (only entities matching the domain/range types for each relation are included in the grammar's entity vocabulary), eliminating the need for stateful masking entirely. This is the most novel and IE-specific strategy: it exploits the structure of IE ontologies to convert context-sensitive constraints into context-free ones by conditioning the grammar on prior extraction results. Follows the spirit of Geng et al.'s input-dependent grammars but with inheritance-aware type filtering and automatic compilation.\n- **(S3, optional/stretch) Draft-conditioned extraction (DCCD-style):** Generate an unconstrained extraction draft first, then re-decode conditioned on the draft with full ontology constraints applied. Included as a comparison point if resources allow, but acknowledged as less IE-specific: DCCD was validated only on reasoning benchmarks (GSM8K), and The Format Tax's finding that decoder-level masking contributes only ~30% of quality loss suggests the projection tax may be smaller for IE's shorter, more structured outputs.\n\nThe comparison of S1/S2 (and optionally S3) directly addresses whether semantic constraints help or hurt extraction F1 — a key scientific question beyond the engineering contribution.\n\n**Differentiation from Synchromesh, IterGen, and EnriCo.** Unlike Synchromesh, which requires manual Completion Engine implementation for each target language, OntoCoDec automatically compiles standard IE ontology definitions into constraint specifications — no domain-specific programming required. Unlike IterGen, which uses post-hoc semantic checking with backtracking (incompatible with KV-cache-efficient batch serving in vLLM's continuous batching), OntoCoDec uses forward-only logit masking that integrates with standard autoregressive serving pipelines. Unlike EnriCo, which uses ASP solvers for constrained inference on discriminative span-classification models and requires manual constraint specification, OntoCoDec operates on autoregressive LLM generation, automatically compiles constraints from ontology definitions, and uses GPU-native logit masking compatible with batch serving. The IE domain also introduces challenges absent from code generation: input-dependent constraints (the valid set of relation arguments changes as entities are generated), inheritance-aware type matching (ontology hierarchies), and schema variability across IE tasks (ACE05 vs. SciERC have different ontologies, both handled by the same compiler).\n\n**Evaluation.** We evaluate on two IE datasets with complementary ontology structures, both featuring relation types with domain/range constraints that test the core novel contribution:\n- **ACE05** (news, 7 entity types, 6 relation types with domain/range constraints, 33 event types with typed argument roles) — the richest ontology constraint structure, testing both relation and event argument type constraints.\n- **SciERC** (scientific abstracts, 6 entity types, 7 relation types) — different domain, simpler ontology, tests compiler generalization across schemas.\n\nBoth datasets have explicit entity type constraints on relation arguments, directly testing the cross-field type constraint contribution. This focused selection (vs. including GENIA, which has no relation types and would only test entity vocabulary constraints trivially handled by grammar-only decoding) ensures every experiment exercises the novel constraint mechanism.\n\nPrimary model: Qwen3-8B served via vLLM (using enable_thinking=True with /no_think prompt suffix per resolved issue #18819, or vLLM ≥0.9.0). Secondary model: Llama-3.1-8B-Instruct (cross-model generalization, lower priority if budget constrained).\n\nBaselines: (1) Unconstrained generation (establishes type violation rate — the first-order empirical contribution), (2) JSON-only constrained decoding (XGrammar-2, grammar constraints only — no semantic enforcement), (3) Unconstrained + post-hoc type filtering (extract with no semantic constraints, then filter/reject outputs violating ontology type constraints — the natural non-decoding-time alternative that directly tests whether decoding-time enforcement outperforms post-hoc validation), (4) GoLLIE (training-time schema compliance — tests whether decoding-time and training-time approaches are complementary or redundant).\n\nMetrics: extraction F1 (entities, relations, events separately), semantic validity rate (% outputs satisfying all ontology constraints), constraint violation rate by category (entity type, relation domain/range, event argument role-filler), validity-vs-F1 tradeoff across S1/S2, and per-step latency overhead.\n\n**Acknowledging the violation rate risk.** If unconstrained LLM-based IE produces ontology type violations at rates <5%, the decoding-time enforcement contribution becomes primarily negative — establishing that LLMs implicitly learn type constraints, and the engineering complexity of decoding-time enforcement is unjustified. We explicitly frame this as a valuable finding: the quantification of violation rates across two datasets and two models is a first-order contribution regardless of direction. The automatic compiler and LogitsProcessor architecture remain useful engineering contributions for applications requiring guaranteed type validity (e.g., knowledge graph population with strict schema compliance).\n\n**Key scientific contributions beyond engineering:** (a) First systematic quantification of ontology type violation rates in unconstrained LLM-based IE across multiple datasets and models — establishing the empirical foundation for whether this problem warrants solution. (b) Comparison of constraint enforcement strategies (forward masking S1 vs. two-pass S2 vs. post-hoc filtering) — answering whether and how semantic constraints affect extraction F1. (c) Empirical test of whether decoding-time constraints complement or substitute training-time schema compliance (GoLLIE comparison). (d) Analysis of which constraint types (entity vocabulary, relation domain/range, event argument role-filler) contribute most to validity and F1 improvements — granular ablation of the constraint hierarchy. (e) First automatic 'zero-code' compiler from IE ontology definitions to decoding-time constraint specifications.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~170h H100-80GB (2 datasets × 2 models × 2 primary strategies × 4 baselines + ablations)",
      "gpu_utilization": "~15-25% — GPU idles during compiler implementation, LogitsProcessor debugging, and constraint specification iteration",
      "timeline": "3-5 months",
      "team": "1-2 researchers (1 NLP + 1 systems)",
      "estimated_gpu_cost": "$340-595 at ~$2.00-3.50/hr H100"
    },
    "human_in_loop": {
      "gpu_hours": "~200h H100-80GB",
      "gpu_utilization": "~40-55% — agent handles constraint specification generation, experiment execution, and result parsing; human reviews LogitsProcessor correctness and validates constraint coverage",
      "timeline": "5-7 weeks",
      "team": "1 researcher, ~60min/day reviewing compiler output, LogitsProcessor state transitions, and validity-vs-F1 tradeoff analysis",
      "claude_api_cost": "$150-350 (~1500-3500 Opus turns for compiler iteration, experiment orchestration, and paper drafting)",
      "estimated_gpu_cost": "$400-700",
      "risk_note": "Unified LogitsProcessor correctness requires careful validation — subtle bugs in mask intersection or entity registry updates may silently permit invalid extractions or over-constrain valid ones. Risk mitigated by focusing on S1/S2 (forward-only, no re-decoding complexity)."
    },
    "auto_research": {
      "gpu_hours": "~350h H100-80GB (2 datasets × 2 models × 2 strategies × 4 baselines × ablations over constraint granularity and type hierarchy depth)",
      "gpu_utilization": "~80-90% — agent pipelines experiments continuously across datasets and configurations",
      "timeline": "12-18 days with 2 H100 GPUs available concurrently",
      "team": "0 (initial setup: schema definitions, dataset paths, evaluation scripts)",
      "claude_api_cost": "$250-550 (~3000-5500 Opus turns for iterative constraint refinement, multi-dataset experiment orchestration, failure diagnosis, and paper writing)",
      "estimated_gpu_cost": "$700-1225",
      "speed_bottleneck": "GPU count (parallel ablations across 2 datasets × 2 strategies require multiple concurrent vLLM instances) and LogitsProcessor debugging cycle",
      "risk_note": "Automated LogitsProcessor generation for ACE05's event ontology (33 event types with typed argument roles) may require manual intervention for edge cases in type hierarchy resolution"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline: May 25, 2026 — tight but feasible with focused ACE05 + SciERC evaluation)",
    "AACL-IJCNLP 2026 (ARR submission deadline: May 25, 2026 — same cycle, must select target at submission)",
    "AAAI 2027 (expected deadline: ~August 1, 2026 — allows complete evaluation with all ablations)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Synchromesh: Reliable Code Generation from Pre-trained Language Models (ICLR 2022, Poesia et al.) — foundational two-layer syntactic+semantic constrained decoding via Completion Engines",
    "IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking (ICLR 2025, Ugare et al.) — grammar+semantic callback paradigm with backtracking; key comparison for forward-only vs. backtracking design choice",
    "CRANE: Reasoning with Constrained LLM Generation (ICML 2025, Banerjee et al.) — theoretical proof that strict grammar constraints limit LLMs to TC⁰; motivates reasoning-augmented and draft-conditioned alternatives",
    "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024, Sainz et al.) — training-time schema compliance baseline; tests complementarity with decoding-time constraints",
    "GenIE: Generative Information Extraction (NAACL 2022, Josifoski et al.) — bi-level constrained generation for IE with prefix trie vocabulary constraints; precursor lacking cross-field type enforcement",
    "EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction (arXiv Apr 2024, Zaratiana et al.) — ASP-based constrained inference enforcing entity type constraints for joint IE; reports ~1 F1 improvement from constraints on ACE05; closest prior work but non-generative and requires manual constraint specification",
    "RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints (arXiv Sep 2025) — post-processing pipeline mapping LLM-extracted relations to standardized ontology predicates; addresses vocabulary standardization rather than decoding-time type consistency",
    "SH-ETRs: Learning Soft-Hard Rules with Entity Type Constraints for Document-Level Relation Extraction (Expert Systems 2025) — training-time entity type rule learning for DocRE; alternative constraint enforcement via learned rules rather than ontology compilation",
    "TyRaL: End-to-End Document-level Relation Extraction via Type-Constrained Rule Learning (CEUR 2024) — type-constrained rule learning for DocRE; training-time approach complementary to decoding-time enforcement",
    "XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs (arXiv Jan 2026, Li et al.) — TagDispatch mechanism for free-text/structured switching; grammar backend",
    "XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models (MLSys 2025)",
    "Draft-Conditioned Constrained Decoding for Structured Generation in LLMs (arXiv Mar 2026) — projection tax analysis and draft-conditioned alternative; evaluated on reasoning benchmarks only (GSM8K), not IE; informs our optional S3 strategy",
    "The Format Tax (arXiv Apr 2026) — systematic decomposition of constrained decoding quality loss: prompt-level effects (~70%) dominate over decoder-level grammar masking (~30%); newer closed-weight models show near-zero tax; informs our two-pass strategy design",
    "From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection (arXiv Apr 2026) — documents cascading formatting errors under strict structural constraints in Qwen3-8B; motivates minimizing constraint scope during generation",
    "Thinking Before Constraining: A Unified Decoding Framework for Large Language Models (arXiv Jan 2026)",
    "The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance (RANLP 2025) — empirical confirmation of quality degradation under constrained decoding",
    "Type-Constrained Code Generation with Language Models (PLDI 2025) — demonstrates cross-field type constraints are context-sensitive, beyond CFG expressiveness",
    "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning (EMNLP 2023, Geng et al.) — input-dependent grammars for closed IE",
    "Lazy-k Decoding: Constrained Decoding for Information Extraction (EMNLP 2023, Hemmer et al.)",
    "PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction (EMNLP 2025 Industry)",
    "Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents (arXiv Feb 2026)",
    "Scientific Knowledge-driven Decoding Constraints (arXiv Apr 2026, SciDC)",
    "Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction (NLPCC 2025, Ru-LLM)",
    "Grammar-constrained decoding for structured information extraction with fine-tuned generative models (Frontiers AI 2024)",
    "Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding (arXiv Apr 2026)",
    "Learning to Generate Structured Output with Schema Reinforcement Learning (ACL 2025)",
    "Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding (SIGDIAL 2024)"
  ],
  "description": "We propose OntoCoDec, an automatic ontology-to-constraint compiler that translates IE schemas into decoding-time constraint specifications enforced during LLM generation — enabling 'zero-code schema compliance' where a researcher provides a standard ontology definition (JSON/Python dataclass) and receives a working constrained decoding setup without writing any constraint logic. Unlike prior grammar+semantic-callback paradigms (Synchromesh, ICLR 2022; IterGen, ICLR 2025) which require manual constraint implementation for code generation domains, and unlike EnriCo (arXiv 2024) which uses ASP solvers for discriminative models, OntoCoDec automatically compiles standard IE ontology definitions — entity type hierarchies, relation domain/range signatures, event argument role-filler constraints — into a unified LogitsProcessor that combines grammar-based structural masking (via XGrammar-2) with stateful type-constraint masking via a dynamic entity type registry, operating within vLLM V1's batch-serving pipeline. We implement and compare two primary strategies: (S1) direct constrained decoding with full grammar+type masking, and (S2) two-pass extraction where entity types extracted in Pass 1 are compiled into input-dependent grammars for Pass 2, converting context-sensitive type constraints into context-free vocabulary constraints — the most novel and IE-specific strategy. Draft-conditioned extraction (S3, DCCD-style) is included as an optional comparison. We evaluate on ACE05 (7 entity types, 6 relation types, 33 event types — rich ontology) and SciERC (6 entity types, 7 relation types — different domain), using Qwen3-8B and Llama-3.1-8B. Baselines include unconstrained generation (establishing violation rates), JSON-only grammar constraints, post-hoc type filtering (testing whether decoding-time enforcement outperforms post-hoc validation), and GoLLIE (testing complementarity with training-time schema compliance). The key scientific contributions are: (1) first systematic quantification of ontology type violation rates in unconstrained LLM-based IE — valuable regardless of whether rates are high (justifying enforcement) or low (establishing LLMs implicitly learn constraints); (2) comparison of constraint enforcement strategies revealing the validity-vs-accuracy tradeoff; (3) empirical test of decoding-time vs. training-time schema compliance complementarity; (4) granular ablation of which ontology constraint types contribute most to validity and F1.",
  "project_name": "schema_semantic_constrained_ie",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL: Context-free grammars cannot enforce cross-field back-reference constraints. The claim that 'a PER-ORG relation non-terminal can only derive entity spans previously tagged as PER in the subject slot' requires context-sensitive language properties. This is not a CFG limitation that can be worked around — it's a fundamental result in formal language theory (Chomsky hierarchy). The Type-Constrained Code Generation paper (arXiv:2504.09246, Apr 2025) explicitly demonstrates that type constraints exceed CFG expressiveness.", "CRITICAL: Misunderstanding of XGrammar's 'context-dependent token masking'. XGrammar categorizes tokens as context-independent (decidable from local automata state) vs context-dependent (requiring full PDA stack state). This is about grammar rule nesting/recursion — NOT about conditioning on previously generated content values. The proposal incorrectly equates these two very different concepts.", "Missing XGrammar-2 (arXiv:2601.04426, Jan 2026): This major update introduces mask_callback() for custom constraint functions and TagDispatch for dynamic structure switching. The mask_callback interface is actually the mechanism needed for content-dependent semantic constraints — but it's NOT grammar-based. The proposal should build on XGrammar-2, not XGrammar-1.", "Missing Draft-Conditioned Constrained Decoding (arXiv:2603.03305, Mar 2026): Directly addresses the distortion problem of constrained decoding on semantics — relevant baseline that should be compared.", "Missing 'Thinking Before Constraining' (arXiv:2601.07525, Jan 2026): Proposes free reasoning before constraint enforcement, achieving up to 27% accuracy gains. Relevant concurrent work.", "Missing Schema Reinforcement Learning (ACL 2025): Uses RL with schema validators for structured generation — an alternative approach to ensuring schema compliance.", "Missing Ru-LLM (NLPCC 2025): Logical rule-constrained LLMs for document-level RE using MCTS — directly addresses type constraints for relation extraction.", "Novelty over Geng et al. (EMNLP 2023) is unclear: That paper already demonstrated grammar-constrained decoding for IE (closed IE on Wikidata with entity/relation vocabulary constraints). The proposed extension to type-hierarchy constraints is either infeasible (strong version) or incremental (weak version).", "Resource estimates use A100-hours but user constraint specifies H100-hours. While roughly compatible given ~2x speedup, this should be addressed.", "The 16-day timeline is very aggressive for: (1) developing a novel ontology-to-grammar compiler, (2) debugging EBNF rules for 3 different IE schemas, (3) running experiments on ACE05 + SciERC + TACRED with 2 model sizes, (4) implementing baselines (BoostCD), and (5) writing the paper."]
Feedback: The core intuition — that IE-specific constraints should be enforced during decoding, not just JSON syntax — is valuable and worth pursuing. However, the proposal fundamentally misidentifies the mechanism. Here is how to fix it:

1. **Abandon the pure-CFG approach for cross-field constraints.** CFGs cannot enforce that entity spans match type labels assigned elsewhere in the output. Instead, explore:
   - **XGrammar-2's mask_callback()**: Use a custom logit processor that tracks generated entity types and dynamically restricts valid relation arguments. This is NOT grammar-based but achieves the desired semantic enforcement. Frame the contribution as a hybrid grammar+callback system.
   - **Two-pass approach**: First generate entities with type-constrained grammar, then generate relations with an input-dependent grammar conditioned on extracted entities (similar to Geng et al.'s input-dependent grammars). This IS expressible as a CFG because the grammar for pass 2 is compiled from pass 1's output.
   - **Draft-conditioned constrained decoding**: Generate unconstrained draft, then use ontology-derived grammar for the structured realization pass.

2. **Clearly differentiate from Geng et al. (2023)**: That paper already did grammar-constrained IE. Articulate what is NEW: the ontology compiler, the multi-level constraint hierarchy, the near-zero overhead via XGrammar-2.

3. **Address concurrent work**: Compare against DCCD (Mar 2026), discuss XGrammar-2 as the implementation substrate, position against Schema RL (ACL 2025) and Ru-LLM.

4. **Narrow the scope for 16 days**: Focus on ONE dataset (ACE05 joint IE) and ONE model (Qwen3-8B for feasibility). Drop TACRED (relation-only, less interesting for joint constraints). Add other datasets only if time permits.

5. **Reframe the contribution**: Instead of 'compile ontology into CFG', frame as 'ontology-aware structured decoding via hybrid grammar-callback constraints' that leverages XGrammar-2's extensibility. The compiler still exists but outputs grammar + callback specifications, not pure EBNF.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL: Missing discussion of IterGen (ICLR 2025, Ugare et al.) — the most closely related prior work. IterGen implements grammar-guided generation with semantic-aware backtracking via user-defined callbacks, essentially the same grammar+callback paradigm applied to code generation. The proposal lists IterGen in references but does not discuss it in the landscape, failing to articulate what is novel beyond domain transfer from code to IE.", "CRITICAL: Missing discussion of Synchromesh/Constrained Semantic Decoding (ICLR 2022, Poesia et al.) — the foundational work on combining syntactic and semantic constraints during decoding. Not cited at all. This is the intellectual ancestor of the proposed approach.", "Missing discussion of CRANE (ICML 2025, Banerjee et al.) which demonstrates that strict grammar enforcement during decoding degrades LLM reasoning quality. The proposal's dual-layer constraints (grammar + logit masking) could similarly degrade extraction accuracy. This tension needs to be acknowledged and addressed — possibly by incorporating free-reasoning windows or comparing against DCCD-style draft-then-constrain alternatives.", "Missing GoLLIE (ICLR 2024) as a baseline — the leading open LLM-based IE system that uses code-based schemas for structured extraction without constrained decoding. A natural comparison: does adding decoding-time constraints improve over GoLLIE's training-time approach?", "XGrammar + custom LogitsProcessor composability is an engineering risk. In vLLM V1, guided decoding (XGrammar) is configured via SamplingParams.guided_decoding while custom LogitsProcessors go through a separate init-time registration path. No documented API supports combining both in the same request. The proposal should acknowledge this and describe a concrete solution (e.g., a unified wrapper processor).", "Evaluation scope (ACE05 only, Qwen3-8B only) is too narrow for EMNLP main track. Reviewers will expect at least 2-3 IE datasets (e.g., ACE05 + SciERC or DocRED) and ideally results showing the approach generalizes across model families or sizes.", "The 'provably beyond CFG expressiveness' framing is overstated. The PLDI 2025 paper observes this well-known fact from formal language theory as motivation for its prefix automata — it does not prove a novel theorem about IE constraints. Rephrase as 'well-known that cross-field type constraints are context-sensitive, requiring mechanisms beyond CFGs.'", "Known Qwen3 + vLLM structured output bug (GitHub issue #18819): structured output with enable_thinking=False produces malformed JSON. Workaround exists (enable_thinking=True + /no_think prompt suffix) but should be noted as an implementation consideration.", "The contribution risks being perceived as primarily engineering (ontology compiler + logit processor implementation) rather than scientific insight. To elevate beyond a systems paper, the authors should include: (a) analysis of what fraction of extraction errors are type violations (quantifying the problem), (b) comparison of constraint enforcement strategies (single-pass vs two-pass vs draft-conditioned), and (c) analysis of whether semantic constraints help or hurt extraction F1 (not just validity rate)."]
Feedback: The revised proposal correctly addresses the round 1 criticism about CFG limitations by adopting a hybrid grammar+callback architecture. This is technically sound. However, the novelty positioning has a critical gap: IterGen (ICLR 2025) and Synchromesh (ICLR 2022) already implement the grammar+semantic-callback paradigm for code generation. The paper MUST discuss both and clearly articulate what's novel beyond domain transfer. Here's how to strengthen:

1. **Position against IterGen and Synchromesh explicitly.** IterGen uses backtracking on constraint violation; your approach uses forward-only masking (no backtracking). Synchromesh targets code semantics; you target IE ontology semantics. Articulate why the IE domain requires different design choices (e.g., entity type registries, input-dependent grammars from extracted entities).

2. **Address CRANE's quality degradation concern.** Acknowledge that constrained decoding can hurt generation quality. Consider: (a) measuring extraction F1 degradation vs. validity improvement tradeoff, (b) a DCCD-style draft-conditioned variant where constraints don't affect the initial generation.

3. **Add GoLLIE as a baseline.** This comparison is highly informative: training-time schema compliance (GoLLIE) vs. decoding-time constraint enforcement (your approach). If they're complementary, that's a strong result.

4. **Expand evaluation if at all possible.** Add SciERC (different domain, different ontology complexity) to show the compiler generalizes. Even preliminary results on a second dataset would strengthen the paper significantly.

5. **Quantify the problem first.** Before showing the solution works, show the problem matters: run unconstrained Qwen3-8B on ACE05 and report what fraction of outputs contain type violations. If it's 30%, the contribution is clearly valuable. If it's 3%, the impact is limited.

6. **Solve the composability problem explicitly.** Describe the concrete implementation plan: will you build a unified LogitsProcessor that internally calls XGrammar's grammar masking and your type constraint masking? Or will you implement both layers in a single custom processor? This is a practical blocker that reviewers will ask about.

7. **Soften the 'provably beyond CFG' language.** Say 'cross-field type constraints are context-sensitive and cannot be expressed as CFGs' without claiming this is a novel proof.

### Round 3 review
Verdict: revise
Issues: ["HARD CONSTRAINT VIOLATION: Manual GPU estimate of ~250h H100-80GB exceeds the user's hard constraint of ≤200 H100-hours. With 3 datasets × 2 models × 3 strategies × 5 baselines = 30 configurations, this needs scoping down. Dropping GENIA and focusing on ACE05 + SciERC with one primary model (Qwen3-8B) and Llama-3.1-8B as secondary would bring it to ~150-180h.", "The claimed '15-40% type violation rate' for unconstrained LLM-based IE is unsubstantiated — no citation or preliminary evidence supports this. The only data point I found suggests ~12% invalid response rate for GPT-4 on complex extraction (including all error types, not just ontology violations). If the actual ontology type violation rate is <5%, the entire motivation for decoding-time enforcement weakens significantly. The proposal correctly frames quantifying this as a contribution, but the risk of a negative result (low violation rate → minimal impact) should be acknowledged.", "GENIA evaluation is misaligned with the novel contribution. GENIA has 5 entity types but NO relation types — it only tests entity vocabulary constraints, which are trivially handled by grammar-only constrained decoding. The novel contribution (cross-field type constraints: relation domain/range, event argument role-filler) cannot be tested on GENIA. Recommend replacing GENIA with a dataset that has rich relation/event ontology constraints, or clearly framing GENIA as entity-only ablation.", "Missing related work: (1) RELATE (arXiv Sep 2025) — ontology-constrained relation extraction in biomedical domain via post-processing pipeline mapping LLM outputs to ontology predicates; (2) EnriCo (arXiv Apr 2024) — globally constrained inference for joint entity-relation extraction using decoding algorithms with task/dataset-specific constraints; (3) SH-ETRs and TyRaL — entity type constraint learning for document-level RE. These are training-time or post-processing approaches, distinct from decoding-time enforcement, but should be discussed to complete the landscape of ontology constraint enforcement mechanisms.", "The DCCD-style draft-conditioned strategy (S3) doubles inference cost per sample (two full forward passes) and has not been validated on IE tasks — DCCD was evaluated only on reasoning benchmarks (GSM8K). There's a risk that the draft-conditioned approach doesn't transfer well to IE because IE outputs are shorter and more structured than reasoning chains, potentially reducing the projection tax that DCCD is designed to mitigate. This risk should be acknowledged.", "Timeline risk for 16 days: The unified LogitsProcessor requires careful engineering — mask intersection between XGrammar's structural mask and the type constraint mask must be correct for every token position, and the entity registry must handle incremental updates correctly as entities are generated. Debugging this for 2-3 different ontology schemas (ACE05's 7 entity types + 6 relation types + 33 event types vs. SciERC's 6+7) is non-trivial. Recommend implementing S1 (direct constrained) and S2 (two-pass) first, with S3 (draft-conditioned) as a stretch goal.", "BoostCD/BoostIE (EMNLP 2025) was evaluated on Wiki-cIE using Wikidata, not on ACE05/SciERC. Reproducing BoostIE on ACE05/SciERC within 16 days as a baseline may require non-trivial adaptation. Consider replacing with a simpler baseline: unconstrained + post-hoc type filtering (extract with no constraints, then filter outputs violating ontology constraints). This provides a natural comparison point (decoding-time vs. post-hoc enforcement) with minimal implementation overhead."]
Feedback: The proposal has improved substantially from rounds 1-2. The hybrid grammar+type-masking architecture is technically sound, the positioning against Synchromesh/IterGen/CRANE/DCCD is well-done, and the scientific questions are well-formulated. To reach pass quality, address these specific points:

1. **Fix the resource budget**: Scope down to ACE05 + SciERC (drop GENIA), Qwen3-8B as primary model, Llama-3.1-8B as secondary. Target ~150-180 H100-hours. This also improves the paper's focus: both ACE05 and SciERC have relation types, so the cross-field type constraint contribution is consistently tested.

2. **Acknowledge the violation rate risk**: State explicitly that if ontology type violations are <5%, the decoding-time enforcement may not justify its complexity. Frame the quantification as a first-order contribution regardless of the finding direction (positive: constraints help; negative: constraints are unnecessary, saving the community effort pursuing this direction).

3. **Prioritize strategies S1 and S2**: Two-pass extraction (S2) is the most novel and IE-specific strategy — it turns cross-field type constraints into vocabulary constraints by conditioning the second pass on first-pass entities. Direct constrained (S1) is the simplest comparison point. Draft-conditioned (S3) is the most engineering-intensive and least IE-specific — make it optional.

4. **Replace BoostIE baseline with post-hoc filtering**: Unconstrained extraction → post-hoc ontology constraint checking/filtering is a natural, easy-to-implement baseline that directly tests whether decoding-time enforcement outperforms post-hoc validation.

5. **Add the missing related work** (RELATE, EnriCo, SH-ETRs) with one sentence each positioning them as alternative constraint enforcement mechanisms (training-time, post-processing) vs. your decoding-time approach.

6. **Strengthen the novelty pitch**: The strongest novelty argument is that OntoCoDec is the first *automatic* compiler from IE ontology definitions to constraint specifications — unlike Synchromesh's manual Completion Engines or IterGen's manual callbacks. Emphasize that a researcher can provide a standard ontology definition (JSON/Python dataclass) and get a working constrained decoding setup without writing any constraint logic. This 'zero-code schema compliance' angle is practically very appealing.


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
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "type": "user",
  "uuid": "1e3608c5-b95a-416c-9210-deb014c2f543",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-11T23:56:32.347Z_

```json
{
  "parentUuid": "1e3608c5-b95a-416c-9210-deb014c2f543",
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
  "uuid": "841c0e58-9e03-45d9-9c87-b0755b47e125",
  "timestamp": "2026-05-11T23:56:32.347Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-11T23:56:32.347Z_

```json
{
  "parentUuid": "841c0e58-9e03-45d9-9c87-b0755b47e125",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f53e3c8c-ead0-4637-870c-2af310d7ed89",
  "timestamp": "2026-05-11T23:56:32.347Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "f53e3c8c-ead0-4637-870c-2af310d7ed89",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Semantic constraint compilation for IE decoding",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

### Assistant

_source line 8 · 2026-05-11T23:56:42.787Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea for Round 4. The proposal has gone through 3 rounds of revision already. I need to independently verify claims, check for missing work, and assess whether the revisions adequately address prior concerns.

Let me start by searching for the key claims and related work.

Key things to verify:
1. Whether the cited papers exist and are correctly characterized
2. Current SOTA in constrained decoding for IE
3. Whether the claimed gap (no automatic ontology-to-constraint compiler for IE) actually exists
4. Violation rates in unconstrained LLM-based IE


5. Whether the approach is feasible given the resource constraints
6. Any concurrent work that might overlap with this direction

Let me search systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f53e3c8c-ead0-4637-870c-2af310d7ed89",
  "isSidechain": false,
  "requestId": "req_011CawgkpK4MknFF7GyPcFDx",
  "type": "assistant",
  "uuid": "787854d0-da3a-4a59-9665-db8f9e7c5a2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWgUnvfo6LcJ2MaVB5GqYp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1926,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20408
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

_source line 9 · 2026-05-11T23:56:42.791Z_

I'll conduct an independent adversarial review of this proposal. Let me start by verifying the key claims and searching for competing/missing work across multiple dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "787854d0-da3a-4a59-9665-db8f9e7c5a2c",
  "isSidechain": false,
  "requestId": "req_011CawgkpK4MknFF7GyPcFDx",
  "type": "assistant",
  "uuid": "3f13178d-7028-4c7c-b956-7bb99a7fba7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWgUnvfo6LcJ2MaVB5GqYp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1926,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20408
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

_source line 10 · 2026-05-11T23:56:52.459Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Ph8gkJ6FpDZHwKAMK9NSFU`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify core cited papers",
  "prompt": "You are helping me verify citations for an ML paper review. I need you to use WebSearch and WebFetch to verify that the following papers exist and are correctly characterized. For each paper, search for it and confirm: (1) it exists, (2) venue/year is correct, (3) the characterization is accurate.\n\nPapers to verify:\n1. \"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking\" — claimed ICLR 2025, Ugare et al. — claimed to use grammar+semantic callback with backtracking for code generation (SQL, Vega-Lite)\n2. \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\" — claimed ICLR 2022, Poesia et al. — claimed to introduce Constrained Semantic Decoding with two-layer Completion Engines\n3. \"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction\" — claimed arXiv Apr 2024, Zaratiana et al. — claimed to use ASP for constrained inference on ACE05, ~1 F1 improvement from constraints\n4. \"The Format Tax\" — claimed arXiv Apr 2026 — claimed to show prompt-level effects (~70%) dominate decoder-level grammar masking (~30%) in constrained decoding quality loss\n5. \"XGrammar-2\" — claimed arXiv Jan 2026 — claimed to introduce TagDispatch and mask_callback\n\nFor each, do a WebSearch and try to find the actual paper. Report what you find — whether each exists, if the venue/year match, and if the characterization seems accurate. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f13178d-7028-4c7c-b956-7bb99a7fba7e",
  "isSidechain": false,
  "requestId": "req_011CawgkpK4MknFF7GyPcFDx",
  "type": "assistant",
  "uuid": "177f3140-507f-4ecb-a7e0-8c3b4531a2b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWgUnvfo6LcJ2MaVB5GqYp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1926,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20408
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

_source line 11 · 2026-05-11T23:57:00.030Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01WYnf9DvyMa2QAFhBsXWu6H`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competing work",
  "prompt": "You are helping me review an ML paper proposal about \"ontology-compiled constrained decoding for information extraction.\" The core idea is automatically compiling IE ontology schemas (entity types, relation domain/range constraints, event argument types) into decoding-time constraint specifications for LLM-based IE.\n\nI need you to search for competing/concurrent work that the proposal might have missed. Use WebSearch with multiple queries:\n\n1. Search: \"ontology constrained decoding information extraction 2025 2026 site:arxiv.org\"\n2. Search: \"schema-guided structured extraction LLM 2025 2026\"\n3. Search: \"type constraint relation extraction decoding 2025 2026\"\n4. Search: \"constrained generation information extraction ontology 2026\"\n5. Search: \"semantic constraint logits masking LLM generation 2025 2026\"\n6. Search: \"structured output LLM type safety extraction 2026\"\n\nFor each search, report the top results and whether any represent work that is highly similar to or directly competes with the proposed approach of compiling IE ontology constraints into decoding-time enforcement. I'm especially looking for papers from the last 6 months (Nov 2025 - May 2026) that might be concurrent work."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "177f3140-507f-4ecb-a7e0-8c3b4531a2b3",
  "isSidechain": false,
  "requestId": "req_011CawgkpK4MknFF7GyPcFDx",
  "type": "assistant",
  "uuid": "cce44aad-4305-4115-aefe-0d90d2658158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWgUnvfo6LcJ2MaVB5GqYp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1926,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20408
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

_source line 12 · 2026-05-11T23:57:09.155Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01R6n3LHDGRz91GjWPNr4QBw`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check violation rates and SOTA",
  "prompt": "You are helping me review an ML paper proposal. I need you to investigate two specific claims:\n\n**Claim 1: Ontology type violation rates in LLM-based IE are unknown/unmeasured.**\nThe proposal claims no prior work has systematically measured the rate at which LLMs produce ontology-invalid outputs during information extraction (e.g., assigning wrong entity types to relation arguments). Search for:\n- \"LLM information extraction error analysis type violation\"\n- \"structured output validity LLM named entity relation extraction\"\n- \"ontology violation rate LLM knowledge extraction\"\n- \"type error LLM relation extraction\"\nLook for any papers that have measured or reported rates of type-constraint violations in LLM-based IE systems.\n\n**Claim 2: Current SOTA on ACE05 and SciERC.**\nSearch for:\n- \"ACE05 joint information extraction state of the art 2025 2026\"\n- \"SciERC relation extraction SOTA 2025 2026\"\n- \"site:paperswithcode.com ACE05\"\n- \"site:paperswithcode.com SciERC\"\nReport what the current SOTA results are on these benchmarks and which methods achieve them.\n\n**Claim 3: GoLLIE performance.**\nSearch for \"GoLLIE zero-shot information extraction ICLR 2024\" and verify it was accepted at ICLR 2024 and that the characterization as \"outperforming zero-shot baselines by ~13 F1 points\" is accurate.\n\nReport all findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cce44aad-4305-4115-aefe-0d90d2658158",
  "isSidechain": false,
  "requestId": "req_011CawgkpK4MknFF7GyPcFDx",
  "type": "assistant",
  "uuid": "8b4f5fe9-3a45-4982-afa5-74c48e11a322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWgUnvfo6LcJ2MaVB5GqYp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1926,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20408
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

_source line 13 · 2026-05-11T23:57:15.698Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0164y8sgx7BYB6H9KVz4aKrz`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check EMNLP deadline and vLLM feasibility",
  "prompt": "You are helping me review an ML paper proposal. I need you to verify several practical claims:\n\n**1. EMNLP 2026 ARR submission deadline.**\nSearch for \"EMNLP 2026 submission deadline\" and \"ARR 2026 May submission deadline\" to verify that the ARR submission deadline is indeed May 25, 2026.\n\n**2. vLLM V1 LogitsProcessor API.**\nSearch for \"vLLM V1 LogitsProcessor API\" and \"vLLM custom LogitsProcessor guided decoding\" to verify:\n- Can custom LogitsProcessors be registered in vLLM V1?\n- Can they be composed with XGrammar-based guided decoding?\n- Is there a documented way to combine grammar-based constraints with custom logit masking?\n\n**3. Qwen3-8B + vLLM structured output bug.**\nSearch for \"vLLM Qwen3 structured output issue 18819\" or \"Qwen3 vLLM enable_thinking structured output\" to verify whether this bug exists and what the workaround is.\n\n**4. XGrammar-2 TagDispatch.**\nSearch for \"XGrammar-2 TagDispatch mask_callback\" to verify whether TagDispatch actually supports dynamic switching between free-text and structured fields as claimed.\n\nReport all findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b4f5fe9-3a45-4982-afa5-74c48e11a322",
  "isSidechain": false,
  "requestId": "req_011CawgkpK4MknFF7GyPcFDx",
  "type": "assistant",
  "uuid": "b35a8935-c07a-437e-a2a6-1f598e9e2541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWgUnvfo6LcJ2MaVB5GqYp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1926,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20408
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

_source line 14 · 2026-05-11T23:58:54.325Z_

<details><summary>↩ Tool result · `toolu_0164y8sgx7BYB6H9KVz4aKrz`</summary>

```text
Here are my findings on all four claims:

---

## 1. EMNLP 2026 ARR Submission Deadline

**Verdict: CONFIRMED.** The ARR submission deadline for EMNLP 2026 is indeed **May 25, 2026**. This is confirmed by both the [official EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/) and the [EMNLP 2026 Twitter/X announcement](https://x.com/emnlpmeeting/status/2029508292637061462).

One important caveat your proposal should note: because EMNLP and AACL share the ARR May cycle, authors must **explicitly select a target conference at submission time**, and this choice is **binding**. See the [EMNLP clarification post](https://x.com/emnlpmeeting/status/2047754845919031450). Other key dates include author response/discussion July 7-13, meta-reviews July 30, and commitment deadline August 2, 2026.

---

## 2. vLLM V1 LogitsProcessor API

**Verdict: PARTIALLY CONFIRMED, with important nuances.**

- **Can custom LogitsProcessors be registered in vLLM V1?** Yes. vLLM V1 has a documented [LogitsProcessor API](https://docs.vllm.ai/en/latest/api/vllm/v1/sample/logits_processor/) where custom processors subclass `vllm.v1.sample.logits_processor.LogitsProcessor`. There are also `AdapterLogitsProcessor` and `RequestLogitsProcessor` variants. Official [examples](https://docs.vllm.ai/en/latest/examples/offline_inference/logits_processor/) demonstrate batch-level and request-level custom processors.

- **Can they be composed with XGrammar-based guided decoding?** This is where the claim needs care. vLLM's guided decoding (including XGrammar) is itself implemented as a logits processor internally. The engine maintains a **list** of loaded logits processors and applies them sequentially in each engine step. So in principle, multiple processors (including a grammar-based one and a custom one) can coexist. However, there is **no explicit documented API** for "compose my custom LogitsProcessor with XGrammar guided decoding in a single request." The [design docs](https://docs.vllm.ai/en/latest/design/logits_processors/) describe the batch-level pipeline, and [Issue #21672](https://github.com/vllm-project/vllm/issues/21672) discusses logits processor support in V1, but explicit composition with guided decoding is not a first-class documented feature.

- **Is there a documented way to combine grammar-based constraints with custom logit masking?** Not as a single clean API. The mechanism exists at the infrastructure level (multiple processors applied sequentially to the logits tensor), but the user-facing documentation does not provide a "here's how to stack your custom mask on top of XGrammar" tutorial. If the paper claims this is straightforward, it should acknowledge this is an implementation-level capability rather than a documented, supported workflow.

Sources: [vLLM LogitsProcessor design](https://docs.vllm.ai/en/latest/design/logits_processors/), [Custom LogitsProcessors examples](https://docs.vllm.ai/en/latest/examples/offline_inference/logits_processor/), [Issue #21672](https://github.com/vllm-project/vllm/issues/21672), [PR #10905](https://github.com/vllm-project/vllm/pull/10905)

---

## 3. Qwen3-8B + vLLM Structured Output Bug (Issue #18819)

**Verdict: CONFIRMED, including the workaround.**

[Issue #18819](https://github.com/vllm-project/vllm/issues/18819) documents exactly the bug described: when serving Qwen3 models with `enable_thinking=False` and a `guided_json` schema, the output JSON is malformed -- extra `{`, `[`, or triple-backtick prefixes, sometimes complete gibberish.

**Workarounds:**
1. Set `enable_thinking=True` -- the model then produces valid structured output.
2. Keep `enable_thinking=True` but append `/no_think` to the user prompt -- the model skips the thinking step but still produces valid JSON.

**Resolution:** The bug was fixed in **vLLM 0.9.0** with the introduction of the `qwen3` reasoning parser. As of vLLM 0.8.5, `enable_thinking=False` was explicitly not compatible with structured output/guided decoding. The [Qwen deployment docs](https://qwen.readthedocs.io/en/latest/deployment/vllm.html) confirm this timeline.

If the paper references this bug, it should note whether the work targets pre-0.9.0 or post-0.9.0 vLLM, since the bug is now resolved in current releases.

---

## 4. XGrammar-2 TagDispatch

**Verdict: CONFIRMED, but the claim should be stated precisely.**

TagDispatch is a real, documented feature of XGrammar-2. Based on the [XGrammar-2 paper (arXiv 2601.04426)](https://arxiv.org/abs/2601.04426) and the [MLC blog post](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation):

- **TagDispatch** is a first-class grammar construct that enables **tag-triggered dynamic switching** between free-form text generation and structured sub-grammars.
- It operates in two modes: **dispatching mode** (free-form text, with an Aho-Corasick automaton scanning for trigger tags) and **dispatched mode** (grammar-constrained generation using the sub-grammar associated with the matched tag). After the sub-grammar completes, it returns to dispatching mode.
- It is parameterized by (i) a list of tag-grammar pairs and (ii) a set of stop strings.
- The `mask_callback()` interface provides engine-agnostic integration -- it intercepts logits, applies the relevant mask depending on the current dispatching state, and returns masked logits to the sampler.

**However**, the claim that TagDispatch supports "dynamic switching between free-text and structured fields" is accurate **only in the sense of tag-triggered switching within a single generation sequence** (e.g., tool-call scenarios where a model outputs free text, then a tool-call tag, then structured JSON). It is **not** a mechanism for per-field switching within a JSON schema (e.g., "this field is free-text, this field is constrained"). For per-field behavior within a schema, XGrammar-2's structural tag feature (documented in the [advanced structural tag tutorial](https://xgrammar.mlc.ai/docs/tutorials/advanced_structural_tag.html)) would be more relevant. The paper should be precise about which mechanism it means.

Performance is reported as <10ms per mask generation step on RTX 5090 / Xeon Platinum, with <6% total overhead.

Sources: [XGrammar-2 paper](https://arxiv.org/html/2601.04426), [MLC blog](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation), [Advanced Structural Tag docs](https://xgrammar.mlc.ai/docs/tutorials/advanced_structural_tag.html), [XGrammar GitHub](https://github.com/mlc-ai/xgrammar)

agentId: afbd3305008a4f6b8 (use SendMessage with to: 'afbd3305008a4f6b8' to continue this agent)
&lt;usage>total_tokens: 22740
tool_uses: 11
duration_ms: 98618&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b35a8935-c07a-437e-a2a6-1f598e9e2541",
  "isSidechain": false,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "type": "user",
  "uuid": "7e4280d9-6c88-4aa0-8cdf-37a10332f514",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me review an ML paper proposal. I need you to verify several practical claims:\n\n**1. EMNLP 2026 ARR submission deadline.**\nSearch for \"EMNLP 2026 submission deadline\" and \"ARR 2026 May submission deadline\" to verify that the ARR submission deadline is indeed May 25, 2026.\n\n**2. vLLM V1 LogitsProcessor API.**\nSearch for \"vLLM V1 LogitsProcessor API\" and \"vLLM custom LogitsProcessor guided decoding\" to verify:\n- Can custom LogitsProcessors be registered in vLLM V1?\n- Can they be composed with XGrammar-based guided decoding?\n- Is there a documented way to combine grammar-based constraints with custom logit masking?\n\n**3. Qwen3-8B + vLLM structured output bug.**\nSearch for \"vLLM Qwen3 structured output issue 18819\" or \"Qwen3 vLLM enable_thinking structured output\" to verify whether this bug exists and what the workaround is.\n\n**4. XGrammar-2 TagDispatch.**\nSearch for \"XGrammar-2 TagDispatch mask_callback\" to verify whether TagDispatch actually supports dynamic switching between free-text and structured fields as claimed.\n\nReport all findings.",
    "agentId": "afbd3305008a4f6b8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings on all four claims:\n\n---\n\n## 1. EMNLP 2026 ARR Submission Deadline\n\n**Verdict: CONFIRMED.** The ARR submission deadline for EMNLP 2026 is indeed **May 25, 2026**. This is confirmed by both the [official EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/) and the [EMNLP 2026 Twitter/X announcement](https://x.com/emnlpmeeting/status/2029508292637061462).\n\nOne important caveat your proposal should note: because EMNLP and AACL share the ARR May cycle, authors must **explicitly select a target conference at submission time**, and this choice is **binding**. See the [EMNLP clarification post](https://x.com/emnlpmeeting/status/2047754845919031450). Other key dates include author response/discussion July 7-13, meta-reviews July 30, and commitment deadline August 2, 2026.\n\n---\n\n## 2. vLLM V1 LogitsProcessor API\n\n**Verdict: PARTIALLY CONFIRMED, with important nuances.**\n\n- **Can custom LogitsProcessors be registered in vLLM V1?** Yes. vLLM V1 has a documented [LogitsProcessor API](https://docs.vllm.ai/en/latest/api/vllm/v1/sample/logits_processor/) where custom processors subclass `vllm.v1.sample.logits_processor.LogitsProcessor`. There are also `AdapterLogitsProcessor` and `RequestLogitsProcessor` variants. Official [examples](https://docs.vllm.ai/en/latest/examples/offline_inference/logits_processor/) demonstrate batch-level and request-level custom processors.\n\n- **Can they be composed with XGrammar-based guided decoding?** This is where the claim needs care. vLLM's guided decoding (including XGrammar) is itself implemented as a logits processor internally. The engine maintains a **list** of loaded logits processors and applies them sequentially in each engine step. So in principle, multiple processors (including a grammar-based one and a custom one) can coexist. However, there is **no explicit documented API** for \"compose my custom LogitsProcessor with XGrammar guided decoding in a single request.\" The [design docs](https://docs.vllm.ai/en/latest/design/logits_processors/) describe the batch-level pipeline, and [Issue #21672](https://github.com/vllm-project/vllm/issues/21672) discusses logits processor support in V1, but explicit composition with guided decoding is not a first-class documented feature.\n\n- **Is there a documented way to combine grammar-based constraints with custom logit masking?** Not as a single clean API. The mechanism exists at the infrastructure level (multiple processors applied sequentially to the logits tensor), but the user-facing documentation does not provide a \"here's how to stack your custom mask on top of XGrammar\" tutorial. If the paper claims this is straightforward, it should acknowledge this is an implementation-level capability rather than a documented, supported workflow.\n\nSources: [vLLM LogitsProcessor design](https://docs.vllm.ai/en/latest/design/logits_processors/), [Custom LogitsProcessors examples](https://docs.vllm.ai/en/latest/examples/offline_inference/logits_processor/), [Issue #21672](https://github.com/vllm-project/vllm/issues/21672), [PR #10905](https://github.com/vllm-project/vllm/pull/10905)\n\n---\n\n## 3. Qwen3-8B + vLLM Structured Output Bug (Issue #18819)\n\n**Verdict: CONFIRMED, including the workaround.**\n\n[Issue #18819](https://github.com/vllm-project/vllm/issues/18819) documents exactly the bug described: when serving Qwen3 models with `enable_thinking=False` and a `guided_json` schema, the output JSON is malformed -- extra `{`, `[`, or triple-backtick prefixes, sometimes complete gibberish.\n\n**Workarounds:**\n1. Set `enable_thinking=True` -- the model then produces valid structured output.\n2. Keep `enable_thinking=True` but append `/no_think` to the user prompt -- the model skips the thinking step but still produces valid JSON.\n\n**Resolution:** The bug was fixed in **vLLM 0.9.0** with the introduction of the `qwen3` reasoning parser. As of vLLM 0.8.5, `enable_thinking=False` was explicitly not compatible with structured output/guided decoding. The [Qwen deployment docs](https://qwen.readthedocs.io/en/latest/deployment/vllm.html) confirm this timeline.\n\nIf the paper references this bug, it should note whether the work targets pre-0.9.0 or post-0.9.0 vLLM, since the bug is now resolved in current releases.\n\n---\n\n## 4. XGrammar-2 TagDispatch\n\n**Verdict: CONFIRMED, but the claim should be stated precisely.**\n\nTagDispatch is a real, documented feature of XGrammar-2. Based on the [XGrammar-2 paper (arXiv 2601.04426)](https://arxiv.org/abs/2601.04426) and the [MLC blog post](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation):\n\n- **TagDispatch** is a first-class grammar construct that enables **tag-triggered dynamic switching** between free-form text generation and structured sub-grammars.\n- It operates in two modes: **dispatching mode** (free-form text, with an Aho-Corasick automaton scanning for trigger tags) and **dispatched mode** (grammar-constrained generation using the sub-grammar associated with the matched tag). After the sub-grammar completes, it returns to dispatching mode.\n- It is parameterized by (i) a list of tag-grammar pairs and (ii) a set of stop strings.\n- The `mask_callback()` interface provides engine-agnostic integration -- it intercepts logits, applies the relevant mask depending on the current dispatching state, and returns masked logits to the sampler.\n\n**However**, the claim that TagDispatch supports \"dynamic switching between free-text and structured fields\" is accurate **only in the sense of tag-triggered switching within a single generation sequence** (e.g., tool-call scenarios where a model outputs free text, then a tool-call tag, then structured JSON). It is **not** a mechanism for per-field switching within a JSON schema (e.g., \"this field is free-text, this field is constrained\"). For per-field behavior within a schema, XGrammar-2's structural tag feature (documented in the [advanced structural tag tutorial](https://xgrammar.mlc.ai/docs/tutorials/advanced_structural_tag.html)) would be more relevant. The paper should be precise about which mechanism it means.\n\nPerformance is reported as <10ms per mask generation step on RTX 5090 / Xeon Platinum, with <6% total overhead.\n\nSources: [XGrammar-2 paper](https://arxiv.org/html/2601.04426), [MLC blog](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation), [Advanced Structural Tag docs](https://xgrammar.mlc.ai/docs/tutorials/advanced_structural_tag.html), [XGrammar GitHub](https://github.com/mlc-ai/xgrammar)"
      }
    ],
    "totalDurationMs": 98618,
    "totalTokens": 22740,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3138,
      "cache_read_input_tokens": 17735,
      "output_tokens": 1866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3138
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1866,
          "cache_read_input_tokens": 17735,
          "cache_creation_input_tokens": 3138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3138,
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
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "b35a8935-c07a-437e-a2a6-1f598e9e2541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T23:59:19.048Z_

<details><summary>↩ Tool result · `toolu_01WYnf9DvyMa2QAFhBsXWu6H`</summary>

```text
Here is my comprehensive analysis of competing and concurrent work relevant to your proposal on "ontology-compiled constrained decoding for information extraction."

---

## Competitive Landscape Analysis

### TIER 1: HIGHLY SIMILAR / DIRECTLY COMPETING WORK

These papers share the core idea of compiling ontological or schema knowledge into decoding-time constraints for LLM-based extraction. Your proposal must cite and differentiate from all of these.

**1. "Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents" (arXiv:2602.03439, February 2026)**
This is the most directly competing paper. It compiles ontological specifications into executable tool interfaces and validators that define the action space available to LLMs, enforcing semantic constraints during generation rather than through post-hoc validation. The key difference from your proposal is that it works through a *tool-calling* mechanism (the ontology is compiled into tools the agent must call) rather than through *logits masking / token-level constrained decoding*. Applied to knowledge graph construction from chemistry literature. This is very recent (Feb 2026) and represents concurrent work. You need to clearly articulate how decoding-level constraint enforcement differs from and potentially improves upon tool-level enforcement.

**2. "Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding" (arXiv:2408.02361, updated March 2025)**
Directly constrains LLM decoding to ontology terms and relation types during generative relation extraction, aiming to reduce hallucination. The approach constrains the CoT decoding process so that generated reasoning steps and outputs conform to ontology-defined vocabulary. This is a clear precursor; your proposal should discuss how it generalizes this idea beyond dialogue RE to full IE ontologies (entities, relations, events).

**3. "Ontology-Constrained Generation of Domain-Specific Clinical Summaries" (arXiv:2411.15666, EKAW 2024)**
Uses ontology-guided constrained beam search where the SNOMED-CT medical ontology constrains the decoding process. Applied to clinical summarization rather than IE proper, but the mechanism -- ontology-driven constrained beam search -- is very close to your core contribution. Code available on GitHub. Your work should differentiate by focusing on IE-specific ontology structures (entity/relation/event schemas with domain/range constraints) rather than terminology ontologies.

**4. PARSE: "LLM Driven Schema Optimization for Reliable Entity Extraction" (arXiv:2510.08623, EMNLP 2025 Industry Track, October 2025)**
Uses constrained decoding (via Outlines) to guarantee schema compliance during entity extraction. The twist is that PARSE also *optimizes* the JSON schema itself for LLM consumption, achieving up to 64.7% improvement. This tackles a complementary but overlapping problem: if you compile an ontology into constraints, PARSE argues the schema representation itself matters for extraction quality. Your proposal should address whether the compiled constraint specification also needs to be "LLM-friendly."

---

### TIER 2: CLOSELY RELATED WORK (different angle on similar problem)

**5. ODKE+: "Ontology-Guided Open-Domain Knowledge Extraction with LLMs" (arXiv:2509.04696, September 2025, Apple)**
A production system that dynamically generates ontology snippets tailored to each entity type to align extractions with schema constraints -- but uses *prompt-based* guidance rather than decoding-time constraints. Deployed at scale (19M facts, 98.8% precision). This is the "soft constraint" alternative to your "hard constraint" approach. Your proposal should benchmark against or discuss this prompt-based paradigm.

**6. "Thinking Before Constraining: A Unified Decoding Framework for Large Language Models" (arXiv:2601.07525, January 2026)**
Proposes a hybrid approach ("In-Writing") that lets LLMs reason freely until trigger tokens appear, then switches to structured constrained generation. Achieves up to 27% accuracy gain over pure natural generation with only 10-20 extra tokens of overhead. This is architecturally relevant -- your ontology-compiled constraints may benefit from a similar "think then constrain" approach rather than constraining from the first token.

**7. OntoKG: "Ontology-Oriented Knowledge Graph Construction with Intrinsic-Relational Routing" (arXiv:2604.02618, April 2026)**
Classifies every property as intrinsic (attribute) vs. relational (edge) and routes to corresponding schema modules, enabling LLM-guided extraction that respects ontological structure. Very recent (April 2026). While it does not use constrained decoding per se, the intrinsic-relational routing is a form of ontology compilation that guides extraction.

**8. "Structure-Aware Decoding Mechanisms for Complex Entity Extraction with Large-Scale Language Models" (arXiv:2512.13980, December 2025)**
Introduces hierarchical structural constraints during decoding for nested and overlapping entity extraction, jointly optimizing classification loss and structural consistency loss. This targets the entity extraction subtask with structure-aware decoding, which overlaps with the entity-type constraint portion of your proposal.

**9. SCG-MEM: "To Know is to Construct: Schema-Constrained Generation for Agent Memory" (arXiv:2604.20117, April 2026)**
Compiles a schema into a dynamic Prefix Trie that acts as a hard constraint on LLM decoding -- only valid paths through the trie can be generated. While targeted at agent memory rather than IE, the core mechanism (schema compiled to trie, used for constrained decoding) is technically very close to your approach. Very recent (late April 2026).

---

### TIER 3: FOUNDATIONAL/INFRASTRUCTURE WORK TO CITE

**10. Grammar-Constrained Decoding for Structured NLP Tasks (arXiv:2305.13971, updated 2025) and Grammar-Constrained Decoding for Clinical Trial IE (Frontiers in AI, January 2025)**
These establish the CFG-based constrained decoding framework your work likely builds on.

**11. XGrammar (MLSys 2025) and llguidance**
The dominant constrained decoding engines as of 2026. XGrammar became the default backend for vLLM, SGLang, and TensorRT-LLM by March 2026. Your ontology compiler presumably targets one of these backends.

**12. "Schema-Constrained Dynamic Decoding" (SDD, from AdaKGC)**
An earlier mechanism for schema adaptation without retraining, discussed in the KG construction survey (arXiv:2510.20345).

**13. "Document-level Relation Extraction with Entity Type Constraints" (ScienceDirect, May 2026)**
Constructs type-constrained graphs and type-constrained loss for relation extraction -- enforces domain/range constraints at training time rather than decoding time.

---

### ASSESSMENT: GAPS AND RISKS

**Most critical concurrent work:** The February 2026 "Ontology-to-tools compilation" paper (arXiv:2602.03439) is the closest competitor. It shares the "compile ontology into executable constraints" framing but uses tool-calling rather than logits masking. Your proposal needs a clear argument for why token-level constrained decoding is superior to (or complementary with) tool-level enforcement.

**Papers from the Nov 2025 - May 2026 window** (your concurrent-work concern): Items #1, #6, #7, #8, #9 above all fall in this window. The SCG-MEM trie-based approach (#9, April 2026) and the "Thinking Before Constraining" framework (#6, January 2026) are particularly worth noting as they may not yet be widely known.

**No exact match found:** I did not find a paper that does exactly what you describe -- automatically compiling a full IE ontology (entity types + relation domain/range + event argument role constraints) into a unified decoding-time constraint specification. The existing work tends to address pieces of this (ontology-to-tools, ontology-constrained beam search for specific domains, grammar-constrained decoding for JSON schemas, type constraints for RE). Your contribution of a *unified compiler* from IE ontology to decoding constraints appears to still be a distinct contribution, but the space is crowded and the differentiation needs to be sharp.

---

Sources:
- [Ontology-to-tools compilation (arXiv:2602.03439)](https://arxiv.org/abs/2602.03439)
- [Dialogue Ontology Relation Extraction via Constrained CoT Decoding (arXiv:2408.02361)](https://arxiv.org/abs/2408.02361)
- [Ontology-Constrained Generation of Clinical Summaries (arXiv:2411.15666)](https://arxiv.org/abs/2411.15666)
- [PARSE: LLM Driven Schema Optimization (arXiv:2510.08623)](https://arxiv.org/abs/2510.08623)
- [ODKE+: Ontology-Guided Knowledge Extraction (arXiv:2509.04696)](https://arxiv.org/abs/2509.04696)
- [Thinking Before Constraining (arXiv:2601.07525)](https://arxiv.org/abs/2601.07525)
- [OntoKG (arXiv:2604.02618)](https://arxiv.org/abs/2604.02618)
- [Structure-Aware Decoding for Entity Extraction (arXiv:2512.13980)](https://arxiv.org/abs/2512.13980)
- [SCG-MEM: Schema-Constrained Generation for Agent Memory (arXiv:2604.20117)](https://arxiv.org/abs/2604.20117)
- [Grammar-Constrained Decoding for Structured NLP Tasks (arXiv:2305.13971)](https://arxiv.org/abs/2305.13971)
- [Grammar-Constrained Decoding for Clinical Trial IE (Frontiers in AI)](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full)
- [LLM-empowered KG Construction Survey (arXiv:2510.20345)](https://arxiv.org/abs/2510.20345)
- [Document-level RE with Entity Type Constraints (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0893608025013504)
- [Awesome LLM Constrained Decoding (GitHub)](https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding)
- [XGrammar / vLLM Structured Outputs](https://docs.vllm.ai/en/latest/features/structured_outputs/)
- [Constrained Decoding Guide (Let's Data Science)](https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json)

agentId: af9a7c70661e00e4c (use SendMessage with to: 'af9a7c70661e00e4c' to continue this agent)
&lt;usage>total_tokens: 30282
tool_uses: 19
duration_ms: 139010&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cce44aad-4305-4115-aefe-0d90d2658158",
  "isSidechain": false,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "type": "user",
  "uuid": "424a8d2d-9d9b-480e-9258-db10a27fddba",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me review an ML paper proposal about \"ontology-compiled constrained decoding for information extraction.\" The core idea is automatically compiling IE ontology schemas (entity types, relation domain/range constraints, event argument types) into decoding-time constraint specifications for LLM-based IE.\n\nI need you to search for competing/concurrent work that the proposal might have missed. Use WebSearch with multiple queries:\n\n1. Search: \"ontology constrained decoding information extraction 2025 2026 site:arxiv.org\"\n2. Search: \"schema-guided structured extraction LLM 2025 2026\"\n3. Search: \"type constraint relation extraction decoding 2025 2026\"\n4. Search: \"constrained generation information extraction ontology 2026\"\n5. Search: \"semantic constraint logits masking LLM generation 2025 2026\"\n6. Search: \"structured output LLM type safety extraction 2026\"\n\nFor each search, report the top results and whether any represent work that is highly similar to or directly competes with the proposed approach of compiling IE ontology constraints into decoding-time enforcement. I'm especially looking for papers from the last 6 months (Nov 2025 - May 2026) that might be concurrent work.",
    "agentId": "af9a7c70661e00e4c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my comprehensive analysis of competing and concurrent work relevant to your proposal on \"ontology-compiled constrained decoding for information extraction.\"\n\n---\n\n## Competitive Landscape Analysis\n\n### TIER 1: HIGHLY SIMILAR / DIRECTLY COMPETING WORK\n\nThese papers share the core idea of compiling ontological or schema knowledge into decoding-time constraints for LLM-based extraction. Your proposal must cite and differentiate from all of these.\n\n**1. \"Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents\" (arXiv:2602.03439, February 2026)**\nThis is the most directly competing paper. It compiles ontological specifications into executable tool interfaces and validators that define the action space available to LLMs, enforcing semantic constraints during generation rather than through post-hoc validation. The key difference from your proposal is that it works through a *tool-calling* mechanism (the ontology is compiled into tools the agent must call) rather than through *logits masking / token-level constrained decoding*. Applied to knowledge graph construction from chemistry literature. This is very recent (Feb 2026) and represents concurrent work. You need to clearly articulate how decoding-level constraint enforcement differs from and potentially improves upon tool-level enforcement.\n\n**2. \"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding\" (arXiv:2408.02361, updated March 2025)**\nDirectly constrains LLM decoding to ontology terms and relation types during generative relation extraction, aiming to reduce hallucination. The approach constrains the CoT decoding process so that generated reasoning steps and outputs conform to ontology-defined vocabulary. This is a clear precursor; your proposal should discuss how it generalizes this idea beyond dialogue RE to full IE ontologies (entities, relations, events).\n\n**3. \"Ontology-Constrained Generation of Domain-Specific Clinical Summaries\" (arXiv:2411.15666, EKAW 2024)**\nUses ontology-guided constrained beam search where the SNOMED-CT medical ontology constrains the decoding process. Applied to clinical summarization rather than IE proper, but the mechanism -- ontology-driven constrained beam search -- is very close to your core contribution. Code available on GitHub. Your work should differentiate by focusing on IE-specific ontology structures (entity/relation/event schemas with domain/range constraints) rather than terminology ontologies.\n\n**4. PARSE: \"LLM Driven Schema Optimization for Reliable Entity Extraction\" (arXiv:2510.08623, EMNLP 2025 Industry Track, October 2025)**\nUses constrained decoding (via Outlines) to guarantee schema compliance during entity extraction. The twist is that PARSE also *optimizes* the JSON schema itself for LLM consumption, achieving up to 64.7% improvement. This tackles a complementary but overlapping problem: if you compile an ontology into constraints, PARSE argues the schema representation itself matters for extraction quality. Your proposal should address whether the compiled constraint specification also needs to be \"LLM-friendly.\"\n\n---\n\n### TIER 2: CLOSELY RELATED WORK (different angle on similar problem)\n\n**5. ODKE+: \"Ontology-Guided Open-Domain Knowledge Extraction with LLMs\" (arXiv:2509.04696, September 2025, Apple)**\nA production system that dynamically generates ontology snippets tailored to each entity type to align extractions with schema constraints -- but uses *prompt-based* guidance rather than decoding-time constraints. Deployed at scale (19M facts, 98.8% precision). This is the \"soft constraint\" alternative to your \"hard constraint\" approach. Your proposal should benchmark against or discuss this prompt-based paradigm.\n\n**6. \"Thinking Before Constraining: A Unified Decoding Framework for Large Language Models\" (arXiv:2601.07525, January 2026)**\nProposes a hybrid approach (\"In-Writing\") that lets LLMs reason freely until trigger tokens appear, then switches to structured constrained generation. Achieves up to 27% accuracy gain over pure natural generation with only 10-20 extra tokens of overhead. This is architecturally relevant -- your ontology-compiled constraints may benefit from a similar \"think then constrain\" approach rather than constraining from the first token.\n\n**7. OntoKG: \"Ontology-Oriented Knowledge Graph Construction with Intrinsic-Relational Routing\" (arXiv:2604.02618, April 2026)**\nClassifies every property as intrinsic (attribute) vs. relational (edge) and routes to corresponding schema modules, enabling LLM-guided extraction that respects ontological structure. Very recent (April 2026). While it does not use constrained decoding per se, the intrinsic-relational routing is a form of ontology compilation that guides extraction.\n\n**8. \"Structure-Aware Decoding Mechanisms for Complex Entity Extraction with Large-Scale Language Models\" (arXiv:2512.13980, December 2025)**\nIntroduces hierarchical structural constraints during decoding for nested and overlapping entity extraction, jointly optimizing classification loss and structural consistency loss. This targets the entity extraction subtask with structure-aware decoding, which overlaps with the entity-type constraint portion of your proposal.\n\n**9. SCG-MEM: \"To Know is to Construct: Schema-Constrained Generation for Agent Memory\" (arXiv:2604.20117, April 2026)**\nCompiles a schema into a dynamic Prefix Trie that acts as a hard constraint on LLM decoding -- only valid paths through the trie can be generated. While targeted at agent memory rather than IE, the core mechanism (schema compiled to trie, used for constrained decoding) is technically very close to your approach. Very recent (late April 2026).\n\n---\n\n### TIER 3: FOUNDATIONAL/INFRASTRUCTURE WORK TO CITE\n\n**10. Grammar-Constrained Decoding for Structured NLP Tasks (arXiv:2305.13971, updated 2025) and Grammar-Constrained Decoding for Clinical Trial IE (Frontiers in AI, January 2025)**\nThese establish the CFG-based constrained decoding framework your work likely builds on.\n\n**11. XGrammar (MLSys 2025) and llguidance**\nThe dominant constrained decoding engines as of 2026. XGrammar became the default backend for vLLM, SGLang, and TensorRT-LLM by March 2026. Your ontology compiler presumably targets one of these backends.\n\n**12. \"Schema-Constrained Dynamic Decoding\" (SDD, from AdaKGC)**\nAn earlier mechanism for schema adaptation without retraining, discussed in the KG construction survey (arXiv:2510.20345).\n\n**13. \"Document-level Relation Extraction with Entity Type Constraints\" (ScienceDirect, May 2026)**\nConstructs type-constrained graphs and type-constrained loss for relation extraction -- enforces domain/range constraints at training time rather than decoding time.\n\n---\n\n### ASSESSMENT: GAPS AND RISKS\n\n**Most critical concurrent work:** The February 2026 \"Ontology-to-tools compilation\" paper (arXiv:2602.03439) is the closest competitor. It shares the \"compile ontology into executable constraints\" framing but uses tool-calling rather than logits masking. Your proposal needs a clear argument for why token-level constrained decoding is superior to (or complementary with) tool-level enforcement.\n\n**Papers from the Nov 2025 - May 2026 window** (your concurrent-work concern): Items #1, #6, #7, #8, #9 above all fall in this window. The SCG-MEM trie-based approach (#9, April 2026) and the \"Thinking Before Constraining\" framework (#6, January 2026) are particularly worth noting as they may not yet be widely known.\n\n**No exact match found:** I did not find a paper that does exactly what you describe -- automatically compiling a full IE ontology (entity types + relation domain/range + event argument role constraints) into a unified decoding-time constraint specification. The existing work tends to address pieces of this (ontology-to-tools, ontology-constrained beam search for specific domains, grammar-constrained decoding for JSON schemas, type constraints for RE). Your contribution of a *unified compiler* from IE ontology to decoding constraints appears to still be a distinct contribution, but the space is crowded and the differentiation needs to be sharp.\n\n---\n\nSources:\n- [Ontology-to-tools compilation (arXiv:2602.03439)](https://arxiv.org/abs/2602.03439)\n- [Dialogue Ontology Relation Extraction via Constrained CoT Decoding (arXiv:2408.02361)](https://arxiv.org/abs/2408.02361)\n- [Ontology-Constrained Generation of Clinical Summaries (arXiv:2411.15666)](https://arxiv.org/abs/2411.15666)\n- [PARSE: LLM Driven Schema Optimization (arXiv:2510.08623)](https://arxiv.org/abs/2510.08623)\n- [ODKE+: Ontology-Guided Knowledge Extraction (arXiv:2509.04696)](https://arxiv.org/abs/2509.04696)\n- [Thinking Before Constraining (arXiv:2601.07525)](https://arxiv.org/abs/2601.07525)\n- [OntoKG (arXiv:2604.02618)](https://arxiv.org/abs/2604.02618)\n- [Structure-Aware Decoding for Entity Extraction (arXiv:2512.13980)](https://arxiv.org/abs/2512.13980)\n- [SCG-MEM: Schema-Constrained Generation for Agent Memory (arXiv:2604.20117)](https://arxiv.org/abs/2604.20117)\n- [Grammar-Constrained Decoding for Structured NLP Tasks (arXiv:2305.13971)](https://arxiv.org/abs/2305.13971)\n- [Grammar-Constrained Decoding for Clinical Trial IE (Frontiers in AI)](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full)\n- [LLM-empowered KG Construction Survey (arXiv:2510.20345)](https://arxiv.org/abs/2510.20345)\n- [Document-level RE with Entity Type Constraints (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0893608025013504)\n- [Awesome LLM Constrained Decoding (GitHub)](https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding)\n- [XGrammar / vLLM Structured Outputs](https://docs.vllm.ai/en/latest/features/structured_outputs/)\n- [Constrained Decoding Guide (Let's Data Science)](https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json)"
      }
    ],
    "totalDurationMs": 139010,
    "totalTokens": 30282,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 961,
      "cache_creation_input_tokens": 1895,
      "cache_read_input_tokens": 24769,
      "output_tokens": 2657,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1895
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 961,
          "output_tokens": 2657,
          "cache_read_input_tokens": 24769,
          "cache_creation_input_tokens": 1895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1895,
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
  "sourceToolAssistantUUID": "cce44aad-4305-4115-aefe-0d90d2658158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "424a8d2d-9d9b-480e-9258-db10a27fddba",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Semantic constraint compilation for IE decoding",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

### Tool result

_source line 18 · 2026-05-12T00:00:08.572Z_

<details><summary>↩ Tool result · `toolu_01Ph8gkJ6FpDZHwKAMK9NSFU`</summary>

```text
Now I have all the information I need. Here is my comprehensive verification report:

---

## Citation Verification Report

### 1. "IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking" -- Ugare et al., ICLR 2025

**Exists:** YES (arXiv:2410.07295)

**Venue/Year:** CORRECT. Published at ICLR 2025 as a poster. Confirmed via both OpenReview and the official ICLR 2025 virtual site.

**Authors:** Shubham Ugare, Rohan Gumaste, Tarun Suresh, Gagandeep Singh, Sasa Misailovic. The claim of "Ugare et al." is correct.

**Characterization accuracy:** MOSTLY ACCURATE. The paper does use grammar-guided generation with backtracking (bidirectional navigation over grammar symbols) and demonstrates effectiveness on SQL and Vega-Lite code generation. The characterization of "grammar+semantic callback" is a reasonable shorthand -- the system uses grammar-based constraints with semantic checks that can trigger backtracking. The KV cache state is maintained to support efficient backtracking. One nuance: the paper also covers privacy leakage reduction as a use case, not just code generation.

**Verdict: CONFIRMED**

---

### 2. "Synchromesh: Reliable Code Generation from Pre-trained Language Models" -- Poesia et al., ICLR 2022

**Exists:** YES (arXiv:2201.11227)

**Venue/Year:** CORRECT. Published at ICLR 2022. Confirmed via OpenReview (forum ID: KmtVD97J43e).

**Authors:** Gabriel Poesia, Oleksandr Polozov, Vu Le, Ashish Tiwari, Gustavo Soares, Christopher Meek, and Sumit Gulwani. "Poesia et al." is correct.

**Characterization accuracy:** ACCURATE. The paper introduces Constrained Semantic Decoding (CSD) and the Completion Engine abstraction. The claim of "two-layer Completion Engines" is confirmed: the completion engines are implemented in two layers -- a context-free layer (enforcing syntactic validity, built automatically from the grammar) and a context-sensitive layer (encoding semantic constraints specific to the target language and user context, e.g., database schema). This is a precise and accurate characterization.

**Verdict: CONFIRMED**

---

### 3. "EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction" -- Zaratiana et al., arXiv Apr 2024

**Exists:** YES (arXiv:2404.12493)

**Venue/Year:** CORRECT. Submitted to arXiv on April 18, 2024.

**Authors:** Urchade Zaratiana, Nadi Tomeh, Yann Dauxais, Pierre Holat, Thierry Charnois. "Zaratiana et al." is correct.

**Characterization accuracy:** PARTIALLY ACCURATE, with caveats.
- **ASP for constrained inference:** CONFIRMED. The paper explicitly states it formulates entity and relation prediction using an Answer Set Programming (ASP) solver for exact solutions.
- **ACE05 evaluation:** CONFIRMED. ACE05 is one of three datasets used (along with CoNLL04 and SciERC).
- **"~1 F1 improvement from constraints":** MISLEADING. The actual improvements from constraints are far more dramatic than "~1 F1." On ACE05, entity F1 jumps from ~60.2 (unconstrained) to ~90.1 (constrained) -- a ~30 point improvement. For relation F1 on ACE05, the improvement is ~0.5 F1 points. If the claim of "~1 F1 improvement" refers specifically to relation F1, it is approximately correct but understates the massive impact on entity F1. The constraint contribution varies enormously depending on the subtask.

**Verdict: EXISTS and venue is correct, but the "~1 F1 improvement" characterization is incomplete/misleading -- constraints provide ~30 F1 improvement for entities and ~0.5 for relations on ACE05.**

---

### 4. "The Format Tax" -- arXiv Apr 2026

**Exists:** YES (arXiv:2604.03616)

**Venue/Year:** CORRECT. Published on arXiv April 4, 2026.

**Authors:** Ivan Yee Lee, Loris D'Antoni, Taylor Berg-Kirkpatrick (UC San Diego).

**Characterization accuracy:** PARTIALLY ACCURATE, with an important inaccuracy.
- The paper does show that prompt-level effects dominate decoder-level grammar masking. This is correct.
- However, the specific claim of "~70% prompt-level, ~30% decoder-level" is NOT what the paper states. The actual numbers from the paper are: of 39 cells with statistically significant effects, 36 (92%) are present under the format-requesting prompt alone, and only 15 (38%) involve grammar-constrained decoding. The average degradation is -3.9 percentage points from the prompt alone, with an additional -1.6 from GCD. This makes the prompt responsible for roughly 71% of total degradation and GCD for 29% -- so the ~70/30 characterization is actually a reasonable approximation of the magnitude split, even if the paper itself does not frame it this way. The paper's own language is that the prompt is "dominant" and sampling bias accounts for "only a fraction."

**Verdict: CONFIRMED. The ~70/30 framing is a reasonable approximation of the paper's findings (-3.9 vs -1.6 pp), though the paper itself describes this qualitatively rather than with those exact percentages.**

---

### 5. "XGrammar-2" -- arXiv Jan 2026

**Exists:** YES (arXiv:2601.04426, "XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs")

**Venue/Year:** CORRECT. Initially submitted January 7, 2026; revised March 26, 2026.

**Authors:** Linzhang Li, Yixin Dong, Guanjie Wang, Ziyi Xu, Alexander Jiang, Tianqi Chen.

**Characterization accuracy:** PARTIALLY ACCURATE.
- **TagDispatch:** CONFIRMED. TagDispatch is a core contribution -- a first-class grammar construct for dynamic tag-triggered structural dispatching within a request.
- **mask_callback:** NOT CONFIRMED. After thorough search of the paper's abstract, HTML version, and descriptions, there is no mention of "mask_callback" anywhere in the paper. The paper discusses an "Earley-based adaptive token mask cache" and token masking mechanisms, but does not introduce a concept or API called "mask_callback." This term may be confused with the implementation-level API in the XGrammar library or may be fabricated.

**Verdict: Paper exists, venue/date correct, TagDispatch confirmed, but "mask_callback" could not be verified as a concept introduced in this paper.**

---

## Summary Table

| Paper | Exists | Venue/Year | Characterization |
|-------|--------|------------|-----------------|
| IterGen (Ugare et al.) | Yes | ICLR 2025 -- Correct | Accurate |
| Synchromesh (Poesia et al.) | Yes | ICLR 2022 -- Correct | Accurate (two-layer CEs confirmed) |
| EnriCo (Zaratiana et al.) | Yes | arXiv Apr 2024 -- Correct | Partially accurate (~1 F1 claim misleading) |
| The Format Tax | Yes | arXiv Apr 2026 -- Correct | Mostly accurate (~70/30 is reasonable approx) |
| XGrammar-2 | Yes | arXiv Jan 2026 -- Correct | Partially accurate (mask_callback not found) |

Sources:
- [IterGen on arXiv](https://arxiv.org/abs/2410.07295)
- [IterGen on OpenReview (ICLR 2025)](https://openreview.net/forum?id=ac93gRzxxV)
- [IterGen ICLR 2025 Poster](https://iclr.cc/virtual/2025/poster/29157)
- [Synchromesh on arXiv](https://arxiv.org/abs/2201.11227)
- [Synchromesh on OpenReview (ICLR 2022)](https://openreview.net/forum?id=KmtVD97J43e)
- [Synchromesh GitHub](https://github.com/kanishkg/synchromesh)
- [Synchromesh PDF (Microsoft Research)](https://www.microsoft.com/en-us/research/wp-content/uploads/2022/01/csd_arxiv.pdf)
- [EnriCo on arXiv](https://arxiv.org/abs/2404.12493)
- [EnriCo HTML](https://arxiv.org/html/2404.12493v1)
- [EnriCo GitHub](https://github.com/urchade/EnriCo)
- [The Format Tax on arXiv](https://arxiv.org/abs/2604.03616)
- [The Format Tax HTML](https://arxiv.org/html/2604.03616v1)
- [XGrammar-2 on arXiv](https://arxiv.org/abs/2601.04426)
- [XGrammar-2 HTML](https://arxiv.org/html/2601.04426)
- [XGrammar-2 MLC Blog Post](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation)

agentId: a3836842801235d25 (use SendMessage with to: 'a3836842801235d25' to continue this agent)
&lt;usage>total_tokens: 25989
tool_uses: 22
duration_ms: 196107&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "177f3140-507f-4ecb-a7e0-8c3b4531a2b3",
  "isSidechain": false,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "type": "user",
  "uuid": "58432d9e-97ec-48cd-8f3d-236c80cf8f5b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me verify citations for an ML paper review. I need you to use WebSearch and WebFetch to verify that the following papers exist and are correctly characterized. For each paper, search for it and confirm: (1) it exists, (2) venue/year is correct, (3) the characterization is accurate.\n\nPapers to verify:\n1. \"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking\" — claimed ICLR 2025, Ugare et al. — claimed to use grammar+semantic callback with backtracking for code generation (SQL, Vega-Lite)\n2. \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\" — claimed ICLR 2022, Poesia et al. — claimed to introduce Constrained Semantic Decoding with two-layer Completion Engines\n3. \"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction\" — claimed arXiv Apr 2024, Zaratiana et al. — claimed to use ASP for constrained inference on ACE05, ~1 F1 improvement from constraints\n4. \"The Format Tax\" — claimed arXiv Apr 2026 — claimed to show prompt-level effects (~70%) dominate decoder-level grammar masking (~30%) in constrained decoding quality loss\n5. \"XGrammar-2\" — claimed arXiv Jan 2026 — claimed to introduce TagDispatch and mask_callback\n\nFor each, do a WebSearch and try to find the actual paper. Report what you find — whether each exists, if the venue/year match, and if the characterization seems accurate. Be thorough.",
    "agentId": "a3836842801235d25",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information I need. Here is my comprehensive verification report:\n\n---\n\n## Citation Verification Report\n\n### 1. \"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking\" -- Ugare et al., ICLR 2025\n\n**Exists:** YES (arXiv:2410.07295)\n\n**Venue/Year:** CORRECT. Published at ICLR 2025 as a poster. Confirmed via both OpenReview and the official ICLR 2025 virtual site.\n\n**Authors:** Shubham Ugare, Rohan Gumaste, Tarun Suresh, Gagandeep Singh, Sasa Misailovic. The claim of \"Ugare et al.\" is correct.\n\n**Characterization accuracy:** MOSTLY ACCURATE. The paper does use grammar-guided generation with backtracking (bidirectional navigation over grammar symbols) and demonstrates effectiveness on SQL and Vega-Lite code generation. The characterization of \"grammar+semantic callback\" is a reasonable shorthand -- the system uses grammar-based constraints with semantic checks that can trigger backtracking. The KV cache state is maintained to support efficient backtracking. One nuance: the paper also covers privacy leakage reduction as a use case, not just code generation.\n\n**Verdict: CONFIRMED**\n\n---\n\n### 2. \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\" -- Poesia et al., ICLR 2022\n\n**Exists:** YES (arXiv:2201.11227)\n\n**Venue/Year:** CORRECT. Published at ICLR 2022. Confirmed via OpenReview (forum ID: KmtVD97J43e).\n\n**Authors:** Gabriel Poesia, Oleksandr Polozov, Vu Le, Ashish Tiwari, Gustavo Soares, Christopher Meek, and Sumit Gulwani. \"Poesia et al.\" is correct.\n\n**Characterization accuracy:** ACCURATE. The paper introduces Constrained Semantic Decoding (CSD) and the Completion Engine abstraction. The claim of \"two-layer Completion Engines\" is confirmed: the completion engines are implemented in two layers -- a context-free layer (enforcing syntactic validity, built automatically from the grammar) and a context-sensitive layer (encoding semantic constraints specific to the target language and user context, e.g., database schema). This is a precise and accurate characterization.\n\n**Verdict: CONFIRMED**\n\n---\n\n### 3. \"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction\" -- Zaratiana et al., arXiv Apr 2024\n\n**Exists:** YES (arXiv:2404.12493)\n\n**Venue/Year:** CORRECT. Submitted to arXiv on April 18, 2024.\n\n**Authors:** Urchade Zaratiana, Nadi Tomeh, Yann Dauxais, Pierre Holat, Thierry Charnois. \"Zaratiana et al.\" is correct.\n\n**Characterization accuracy:** PARTIALLY ACCURATE, with caveats.\n- **ASP for constrained inference:** CONFIRMED. The paper explicitly states it formulates entity and relation prediction using an Answer Set Programming (ASP) solver for exact solutions.\n- **ACE05 evaluation:** CONFIRMED. ACE05 is one of three datasets used (along with CoNLL04 and SciERC).\n- **\"~1 F1 improvement from constraints\":** MISLEADING. The actual improvements from constraints are far more dramatic than \"~1 F1.\" On ACE05, entity F1 jumps from ~60.2 (unconstrained) to ~90.1 (constrained) -- a ~30 point improvement. For relation F1 on ACE05, the improvement is ~0.5 F1 points. If the claim of \"~1 F1 improvement\" refers specifically to relation F1, it is approximately correct but understates the massive impact on entity F1. The constraint contribution varies enormously depending on the subtask.\n\n**Verdict: EXISTS and venue is correct, but the \"~1 F1 improvement\" characterization is incomplete/misleading -- constraints provide ~30 F1 improvement for entities and ~0.5 for relations on ACE05.**\n\n---\n\n### 4. \"The Format Tax\" -- arXiv Apr 2026\n\n**Exists:** YES (arXiv:2604.03616)\n\n**Venue/Year:** CORRECT. Published on arXiv April 4, 2026.\n\n**Authors:** Ivan Yee Lee, Loris D'Antoni, Taylor Berg-Kirkpatrick (UC San Diego).\n\n**Characterization accuracy:** PARTIALLY ACCURATE, with an important inaccuracy.\n- The paper does show that prompt-level effects dominate decoder-level grammar masking. This is correct.\n- However, the specific claim of \"~70% prompt-level, ~30% decoder-level\" is NOT what the paper states. The actual numbers from the paper are: of 39 cells with statistically significant effects, 36 (92%) are present under the format-requesting prompt alone, and only 15 (38%) involve grammar-constrained decoding. The average degradation is -3.9 percentage points from the prompt alone, with an additional -1.6 from GCD. This makes the prompt responsible for roughly 71% of total degradation and GCD for 29% -- so the ~70/30 characterization is actually a reasonable approximation of the magnitude split, even if the paper itself does not frame it this way. The paper's own language is that the prompt is \"dominant\" and sampling bias accounts for \"only a fraction.\"\n\n**Verdict: CONFIRMED. The ~70/30 framing is a reasonable approximation of the paper's findings (-3.9 vs -1.6 pp), though the paper itself describes this qualitatively rather than with those exact percentages.**\n\n---\n\n### 5. \"XGrammar-2\" -- arXiv Jan 2026\n\n**Exists:** YES (arXiv:2601.04426, \"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs\")\n\n**Venue/Year:** CORRECT. Initially submitted January 7, 2026; revised March 26, 2026.\n\n**Authors:** Linzhang Li, Yixin Dong, Guanjie Wang, Ziyi Xu, Alexander Jiang, Tianqi Chen.\n\n**Characterization accuracy:** PARTIALLY ACCURATE.\n- **TagDispatch:** CONFIRMED. TagDispatch is a core contribution -- a first-class grammar construct for dynamic tag-triggered structural dispatching within a request.\n- **mask_callback:** NOT CONFIRMED. After thorough search of the paper's abstract, HTML version, and descriptions, there is no mention of \"mask_callback\" anywhere in the paper. The paper discusses an \"Earley-based adaptive token mask cache\" and token masking mechanisms, but does not introduce a concept or API called \"mask_callback.\" This term may be confused with the implementation-level API in the XGrammar library or may be fabricated.\n\n**Verdict: Paper exists, venue/date correct, TagDispatch confirmed, but \"mask_callback\" could not be verified as a concept introduced in this paper.**\n\n---\n\n## Summary Table\n\n| Paper | Exists | Venue/Year | Characterization |\n|-------|--------|------------|-----------------|\n| IterGen (Ugare et al.) | Yes | ICLR 2025 -- Correct | Accurate |\n| Synchromesh (Poesia et al.) | Yes | ICLR 2022 -- Correct | Accurate (two-layer CEs confirmed) |\n| EnriCo (Zaratiana et al.) | Yes | arXiv Apr 2024 -- Correct | Partially accurate (~1 F1 claim misleading) |\n| The Format Tax | Yes | arXiv Apr 2026 -- Correct | Mostly accurate (~70/30 is reasonable approx) |\n| XGrammar-2 | Yes | arXiv Jan 2026 -- Correct | Partially accurate (mask_callback not found) |\n\nSources:\n- [IterGen on arXiv](https://arxiv.org/abs/2410.07295)\n- [IterGen on OpenReview (ICLR 2025)](https://openreview.net/forum?id=ac93gRzxxV)\n- [IterGen ICLR 2025 Poster](https://iclr.cc/virtual/2025/poster/29157)\n- [Synchromesh on arXiv](https://arxiv.org/abs/2201.11227)\n- [Synchromesh on OpenReview (ICLR 2022)](https://openreview.net/forum?id=KmtVD97J43e)\n- [Synchromesh GitHub](https://github.com/kanishkg/synchromesh)\n- [Synchromesh PDF (Microsoft Research)](https://www.microsoft.com/en-us/research/wp-content/uploads/2022/01/csd_arxiv.pdf)\n- [EnriCo on arXiv](https://arxiv.org/abs/2404.12493)\n- [EnriCo HTML](https://arxiv.org/html/2404.12493v1)\n- [EnriCo GitHub](https://github.com/urchade/EnriCo)\n- [The Format Tax on arXiv](https://arxiv.org/abs/2604.03616)\n- [The Format Tax HTML](https://arxiv.org/html/2604.03616v1)\n- [XGrammar-2 on arXiv](https://arxiv.org/abs/2601.04426)\n- [XGrammar-2 HTML](https://arxiv.org/html/2601.04426)\n- [XGrammar-2 MLC Blog Post](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation)"
      }
    ],
    "totalDurationMs": 196107,
    "totalTokens": 25989,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 23283,
      "output_tokens": 2405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 300
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2405,
          "cache_read_input_tokens": 23283,
          "cache_creation_input_tokens": 300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 300,
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
  "sourceToolAssistantUUID": "177f3140-507f-4ecb-a7e0-8c3b4531a2b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:04:16.947Z_

<details><summary>↩ Tool result · `toolu_01R6n3LHDGRz91GjWPNr4QBw`</summary>

```text
Now I have all the information needed. Let me compile the comprehensive findings.

---

Here is my detailed report on all three claims:

---

## Claim 1: Ontology Type Violation Rates in LLM-based IE Are Unknown/Unmeasured

**Verdict: Partially supported -- but the claim needs nuancing.**

After extensive searching, I found that **no paper has performed a dedicated, systematic study measuring the rate at which LLMs produce ontology-type-invalid outputs** (e.g., assigning a PERSON entity as the argument to a relation that requires an ORGANIZATION) **specifically in the context of standard IE benchmarks like ACE05, TACRED, or SciERC.**

However, there are several pieces of adjacent/partial work:

1. **"Revisiting Relation Extraction in the era of Large Language Models" (ACL 2023)** -- This paper found that Flan-T5 generated "over 120 unique relations" violating the predefined relation schema on CoNLL, and 13.9% of generations on ADE produced non-conforming outputs. But these are **relation label** violations (inventing relation names), not entity **type** constraint violations (wrong argument types).

2. **"Relation Classification with Entity Type Restriction" (2021)** -- Reports that ~11% of false positives on TACRED "break entity type restrictions." This is the closest quantitative finding to what the proposal describes, but it was for traditional models, not LLMs specifically.

3. **PARSE (EMNLP 2025 Industry)** -- Reports GPT-4 has an **11.97% invalid response rate** for complex extraction tasks, but this is about schema non-adherence broadly (missing fields, wrong formats), not specifically ontology type-constraint violations on relation arguments.

4. **OntoLogX and related KG extraction work** -- Uses SHACL violation ratios to measure ontology compliance in LLM-generated knowledge graphs, but this is in the knowledge graph construction domain, not standard IE benchmarks.

5. **ErrorAtlas** -- A taxonomy of LLM failure modes covering 7,049 failures, but does not specifically isolate ontology type violations in IE.

**Bottom line:** The proposal's claim is largely correct. While there are scattered, tangential measurements, no one has systematically quantified the rate at which LLMs produce entity-type-invalid relation arguments on standard IE benchmarks. The gap is real. However, the proposal should acknowledge the partial evidence that exists (e.g., the TACRED 11% false-positive rate from type restriction violations, the 13.9% non-conforming output rate on ADE).

---

## Claim 2: Current SOTA on ACE05 and SciERC

### ACE05 (Relation Extraction)

The established strong baseline is **PL-Marker** (ACL 2022):
- **Entity F1: 89.8** (BERT-base)
- **Relation F1: 69.0** (BERT-base) / **71.1** (ALBERT-xxlarge)
- **Strict Relation F1: 66.5** (BERT-base)
- Gained +4.1% strict relation F1 over PURE (which had 64.8).

More recent models have continued to push results. One method reports improvements of **+4.7% absolute F1** over previous SOTA on ACE05 RE. The **ITER** model with DeBERTa-large reports an F1 of **71.37**. Some configurations report F1 as high as **77.70%**, though the exact setup and evaluation protocol are not fully clear from the search results.

Papers with Code tracks this leaderboard at [ACE 2005 Benchmark (Relation Extraction)](https://paperswithcode.com/sota/relation-extraction-on-ace-2005), but the site was redirecting during my fetch attempts, preventing me from getting the complete current ranking.

### SciERC (Joint Entity and Relation Extraction)

- **PL-Marker** with SciBERT: Entity F1 69.9, Relation F1 53.2, Strict Relation F1 41.6.
- **HGERE** (a graph-structured model with dynamic graph attention) is reported as the newer SOTA, significantly outperforming both PURE and PL-Marker on SciERC. HGERE achieved **86.85% NER F1** and **61.10% strict end-to-end RE F1** on in-domain test data.

The leaderboard is tracked at [Joint Entity and Relation Extraction on SciERC](https://paperswithcode.com/sota/joint-entity-and-relation-extraction-on).

---

## Claim 3: GoLLIE Performance

**Venue: Confirmed.** GoLLIE was published as a conference paper at **ICLR 2024** ([poster page](https://iclr.cc/virtual/2024/poster/18435), [OpenReview](https://openreview.net/forum?id=Y3wpuxd7u9), [proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf)).

**~13 F1 improvement: Confirmed, but requires precise characterization.** The 13 F1 point improvement is the gap between **GoLLIE and its own baseline** (same model architecture without guideline-following fine-tuning), NOT the gap over external zero-shot baselines like Instruct-UIE. Specifically from Table 3:

- **Baseline (no guidelines):** 42.3 F1 average
- **GoLLIE 7B (with guidelines):** 55.3 F1 average
- **Difference: ~13.0 F1 points**

When compared against **external zero-shot SOTA** (Instruct-UIE, Entailment-based IE), the numbers are:
- External zero-shot SOTA average: **42.6 F1**
- GoLLIE 7B: **58.4 F1** (a ~15.8 point improvement over external SOTA)
- GoLLIE 34B: **60.0 F1**

So the characterization "outperforming zero-shot baselines by ~13 F1 points" is **slightly imprecise**. If "baselines" refers to GoLLIE's own ablation baseline (same model without guidelines), the ~13 figure is correct. If it refers to prior external zero-shot SOTA methods, the improvement is actually **larger** (~15-17 points). The proposal should clarify which comparison is meant.

---

Sources:
- [GoLLIE paper (arXiv HTML)](https://arxiv.org/html/2310.03668v5)
- [GoLLIE at ICLR 2024](https://iclr.cc/virtual/2024/poster/18435)
- [GoLLIE OpenReview](https://openreview.net/forum?id=Y3wpuxd7u9)
- [PL-Marker paper](https://ar5iv.labs.arxiv.org/html/2109.06067)
- [ACE 2005 Benchmark (Papers with Code)](https://paperswithcode.com/sota/relation-extraction-on-ace-2005)
- [SciERC Joint Extraction Benchmark (Papers with Code)](https://paperswithcode.com/sota/joint-entity-and-relation-extraction-on)
- [Revisiting Relation Extraction in the era of LLMs](https://pmc.ncbi.nlm.nih.gov/articles/PMC10482322/)
- [Relation Classification with Entity Type Restriction](https://ar5iv.labs.arxiv.org/html/2105.08393)
- [PARSE: Schema Optimization for Entity Extraction](https://arxiv.org/html/2510.08623v1)
- [OntoLogX: Ontology-Guided KG Extraction](https://arxiv.org/html/2510.01409v2)
- [SciNLP benchmark with HGERE results](https://arxiv.org/html/2509.07801)
- [ErrorAtlas taxonomy](https://www.emergentmind.com/topics/erroratlas)
- [Survey on relation extraction techniques](https://link.springer.com/article/10.1007/s10462-025-11280-0)
- [Document-level RE with entity type constraints](https://www.sciencedirect.com/science/article/abs/pii/S0893608025013504)

agentId: a970d91c60de5fb09 (use SendMessage with to: 'a970d91c60de5fb09' to continue this agent)
&lt;usage>total_tokens: 43346
tool_uses: 36
duration_ms: 427787&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b4f5fe9-3a45-4982-afa5-74c48e11a322",
  "isSidechain": false,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "type": "user",
  "uuid": "e701e53a-980c-438b-b688-935d02708fee",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me review an ML paper proposal. I need you to investigate two specific claims:\n\n**Claim 1: Ontology type violation rates in LLM-based IE are unknown/unmeasured.**\nThe proposal claims no prior work has systematically measured the rate at which LLMs produce ontology-invalid outputs during information extraction (e.g., assigning wrong entity types to relation arguments). Search for:\n- \"LLM information extraction error analysis type violation\"\n- \"structured output validity LLM named entity relation extraction\"\n- \"ontology violation rate LLM knowledge extraction\"\n- \"type error LLM relation extraction\"\nLook for any papers that have measured or reported rates of type-constraint violations in LLM-based IE systems.\n\n**Claim 2: Current SOTA on ACE05 and SciERC.**\nSearch for:\n- \"ACE05 joint information extraction state of the art 2025 2026\"\n- \"SciERC relation extraction SOTA 2025 2026\"\n- \"site:paperswithcode.com ACE05\"\n- \"site:paperswithcode.com SciERC\"\nReport what the current SOTA results are on these benchmarks and which methods achieve them.\n\n**Claim 3: GoLLIE performance.**\nSearch for \"GoLLIE zero-shot information extraction ICLR 2024\" and verify it was accepted at ICLR 2024 and that the characterization as \"outperforming zero-shot baselines by ~13 F1 points\" is accurate.\n\nReport all findings in detail.",
    "agentId": "a970d91c60de5fb09",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Let me compile the comprehensive findings.\n\n---\n\nHere is my detailed report on all three claims:\n\n---\n\n## Claim 1: Ontology Type Violation Rates in LLM-based IE Are Unknown/Unmeasured\n\n**Verdict: Partially supported -- but the claim needs nuancing.**\n\nAfter extensive searching, I found that **no paper has performed a dedicated, systematic study measuring the rate at which LLMs produce ontology-type-invalid outputs** (e.g., assigning a PERSON entity as the argument to a relation that requires an ORGANIZATION) **specifically in the context of standard IE benchmarks like ACE05, TACRED, or SciERC.**\n\nHowever, there are several pieces of adjacent/partial work:\n\n1. **\"Revisiting Relation Extraction in the era of Large Language Models\" (ACL 2023)** -- This paper found that Flan-T5 generated \"over 120 unique relations\" violating the predefined relation schema on CoNLL, and 13.9% of generations on ADE produced non-conforming outputs. But these are **relation label** violations (inventing relation names), not entity **type** constraint violations (wrong argument types).\n\n2. **\"Relation Classification with Entity Type Restriction\" (2021)** -- Reports that ~11% of false positives on TACRED \"break entity type restrictions.\" This is the closest quantitative finding to what the proposal describes, but it was for traditional models, not LLMs specifically.\n\n3. **PARSE (EMNLP 2025 Industry)** -- Reports GPT-4 has an **11.97% invalid response rate** for complex extraction tasks, but this is about schema non-adherence broadly (missing fields, wrong formats), not specifically ontology type-constraint violations on relation arguments.\n\n4. **OntoLogX and related KG extraction work** -- Uses SHACL violation ratios to measure ontology compliance in LLM-generated knowledge graphs, but this is in the knowledge graph construction domain, not standard IE benchmarks.\n\n5. **ErrorAtlas** -- A taxonomy of LLM failure modes covering 7,049 failures, but does not specifically isolate ontology type violations in IE.\n\n**Bottom line:** The proposal's claim is largely correct. While there are scattered, tangential measurements, no one has systematically quantified the rate at which LLMs produce entity-type-invalid relation arguments on standard IE benchmarks. The gap is real. However, the proposal should acknowledge the partial evidence that exists (e.g., the TACRED 11% false-positive rate from type restriction violations, the 13.9% non-conforming output rate on ADE).\n\n---\n\n## Claim 2: Current SOTA on ACE05 and SciERC\n\n### ACE05 (Relation Extraction)\n\nThe established strong baseline is **PL-Marker** (ACL 2022):\n- **Entity F1: 89.8** (BERT-base)\n- **Relation F1: 69.0** (BERT-base) / **71.1** (ALBERT-xxlarge)\n- **Strict Relation F1: 66.5** (BERT-base)\n- Gained +4.1% strict relation F1 over PURE (which had 64.8).\n\nMore recent models have continued to push results. One method reports improvements of **+4.7% absolute F1** over previous SOTA on ACE05 RE. The **ITER** model with DeBERTa-large reports an F1 of **71.37**. Some configurations report F1 as high as **77.70%**, though the exact setup and evaluation protocol are not fully clear from the search results.\n\nPapers with Code tracks this leaderboard at [ACE 2005 Benchmark (Relation Extraction)](https://paperswithcode.com/sota/relation-extraction-on-ace-2005), but the site was redirecting during my fetch attempts, preventing me from getting the complete current ranking.\n\n### SciERC (Joint Entity and Relation Extraction)\n\n- **PL-Marker** with SciBERT: Entity F1 69.9, Relation F1 53.2, Strict Relation F1 41.6.\n- **HGERE** (a graph-structured model with dynamic graph attention) is reported as the newer SOTA, significantly outperforming both PURE and PL-Marker on SciERC. HGERE achieved **86.85% NER F1** and **61.10% strict end-to-end RE F1** on in-domain test data.\n\nThe leaderboard is tracked at [Joint Entity and Relation Extraction on SciERC](https://paperswithcode.com/sota/joint-entity-and-relation-extraction-on).\n\n---\n\n## Claim 3: GoLLIE Performance\n\n**Venue: Confirmed.** GoLLIE was published as a conference paper at **ICLR 2024** ([poster page](https://iclr.cc/virtual/2024/poster/18435), [OpenReview](https://openreview.net/forum?id=Y3wpuxd7u9), [proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf)).\n\n**~13 F1 improvement: Confirmed, but requires precise characterization.** The 13 F1 point improvement is the gap between **GoLLIE and its own baseline** (same model architecture without guideline-following fine-tuning), NOT the gap over external zero-shot baselines like Instruct-UIE. Specifically from Table 3:\n\n- **Baseline (no guidelines):** 42.3 F1 average\n- **GoLLIE 7B (with guidelines):** 55.3 F1 average\n- **Difference: ~13.0 F1 points**\n\nWhen compared against **external zero-shot SOTA** (Instruct-UIE, Entailment-based IE), the numbers are:\n- External zero-shot SOTA average: **42.6 F1**\n- GoLLIE 7B: **58.4 F1** (a ~15.8 point improvement over external SOTA)\n- GoLLIE 34B: **60.0 F1**\n\nSo the characterization \"outperforming zero-shot baselines by ~13 F1 points\" is **slightly imprecise**. If \"baselines\" refers to GoLLIE's own ablation baseline (same model without guidelines), the ~13 figure is correct. If it refers to prior external zero-shot SOTA methods, the improvement is actually **larger** (~15-17 points). The proposal should clarify which comparison is meant.\n\n---\n\nSources:\n- [GoLLIE paper (arXiv HTML)](https://arxiv.org/html/2310.03668v5)\n- [GoLLIE at ICLR 2024](https://iclr.cc/virtual/2024/poster/18435)\n- [GoLLIE OpenReview](https://openreview.net/forum?id=Y3wpuxd7u9)\n- [PL-Marker paper](https://ar5iv.labs.arxiv.org/html/2109.06067)\n- [ACE 2005 Benchmark (Papers with Code)](https://paperswithcode.com/sota/relation-extraction-on-ace-2005)\n- [SciERC Joint Extraction Benchmark (Papers with Code)](https://paperswithcode.com/sota/joint-entity-and-relation-extraction-on)\n- [Revisiting Relation Extraction in the era of LLMs](https://pmc.ncbi.nlm.nih.gov/articles/PMC10482322/)\n- [Relation Classification with Entity Type Restriction](https://ar5iv.labs.arxiv.org/html/2105.08393)\n- [PARSE: Schema Optimization for Entity Extraction](https://arxiv.org/html/2510.08623v1)\n- [OntoLogX: Ontology-Guided KG Extraction](https://arxiv.org/html/2510.01409v2)\n- [SciNLP benchmark with HGERE results](https://arxiv.org/html/2509.07801)\n- [ErrorAtlas taxonomy](https://www.emergentmind.com/topics/erroratlas)\n- [Survey on relation extraction techniques](https://link.springer.com/article/10.1007/s10462-025-11280-0)\n- [Document-level RE with entity type constraints](https://www.sciencedirect.com/science/article/abs/pii/S0893608025013504)"
      }
    ],
    "totalDurationMs": 427787,
    "totalTokens": 43346,
    "totalToolUseCount": 36,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 40640,
      "output_tokens": 2085,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 620
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2085,
          "cache_read_input_tokens": 40640,
          "cache_creation_input_tokens": 620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 620,
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
      "otherToolCount": 36
    }
  },
  "sourceToolAssistantUUID": "8b4f5fe9-3a45-4982-afa5-74c48e11a322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e701e53a-980c-438b-b688-935d02708fee",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Semantic constraint compilation for IE decoding",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

### Assistant

_source line 22 · 2026-05-12T00:04:20.241Z_

Good, I have extensive findings from all four research agents. Let me now do a few targeted follow-up searches on the most critical concerns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e701e53a-980c-438b-b688-935d02708fee",
  "isSidechain": false,
  "requestId": "req_011CawhM3pbo1rDhHkQY7xD7",
  "type": "assistant",
  "uuid": "a2fd6361-bcfe-4bfa-8ee6-5027100f6192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Di92mMAyHAXiHB664te2Wu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1969,
      "cache_creation_input_tokens": 9334,
      "cache_read_input_tokens": 32249,
      "output_tokens": 778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9334,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1969,
          "output_tokens": 778,
          "cache_read_input_tokens": 32249,
          "cache_creation_input_tokens": 9334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9334
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

_source line 23 · 2026-05-12T00:04:29.048Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BqKJ4V6quSxQMDAEeoNxHf`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Structure Snowballing and DCCD",
  "prompt": "I need to verify two more papers cited in an ML proposal:\n\n1. **\"From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection\"** — claimed arXiv Apr 2026. The proposal says it \"documents cascading formatting errors under strict structural constraints in Qwen3-8B.\" Search for this paper on arXiv. Does it exist? Is the characterization accurate?\n\n2. **\"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs\"** — claimed arXiv Mar 2026. The proposal says it demonstrates a \"projection tax\" from constrained decoding and achieves +24pp gains on GSM8K. Search for this paper. Does it exist? Is it accurately characterized?\n\n3. Also search for: \"CRANE constrained decoding reasoning ICML 2025 Banerjee\" — the proposal claims CRANE proved that constrained decoding limits LLMs to TC⁰ complexity. Verify this.\n\nUse WebSearch for each. Report findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2fd6361-bcfe-4bfa-8ee6-5027100f6192",
  "isSidechain": false,
  "requestId": "req_011CawhM3pbo1rDhHkQY7xD7",
  "type": "assistant",
  "uuid": "dc5c4986-8951-4749-9dc6-dccf2c92bfc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Di92mMAyHAXiHB664te2Wu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1969,
      "cache_creation_input_tokens": 9334,
      "cache_read_input_tokens": 32249,
      "output_tokens": 778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9334,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1969,
          "output_tokens": 778,
          "cache_read_input_tokens": 32249,
          "cache_creation_input_tokens": 9334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9334
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

_source line 24 · 2026-05-12T00:04:37.060Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FQBmvGV2XTHvQEXYURbnUt`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check resource estimate realism",
  "prompt": "I need to verify whether the following compute resource estimate is realistic for an IE (Information Extraction) research project:\n\nThe proposal claims ~170h H100-80GB for:\n- 2 datasets (ACE05, SciERC)\n- 2 models (Qwen3-8B, Llama-3.1-8B)\n- 2 primary strategies (direct constrained decoding, two-pass extraction)\n- 4 baselines (unconstrained, JSON-only grammar, post-hoc filtering, GoLLIE)\n- Plus ablations\n\nSearch for:\n1. \"ACE05 dataset size\" — how many examples are in ACE05?\n2. \"SciERC dataset size\" — how many examples in SciERC?\n3. \"vLLM inference throughput 8B model H100\" — what's the typical inference throughput?\n4. \"GoLLIE training cost GPU hours\" — how expensive is it to run GoLLIE?\n\nBased on the dataset sizes and typical inference throughput for 8B models on H100, estimate whether ~170h is reasonable for the described experiments. Key considerations:\n- ACE05 and SciERC are small-medium datasets\n- 8B models on H100 should have fast inference\n- But GoLLIE requires fine-tuning, which is more expensive\n- Constrained decoding adds overhead\n\nReport your analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc5c4986-8951-4749-9dc6-dccf2c92bfc6",
  "isSidechain": false,
  "requestId": "req_011CawhM3pbo1rDhHkQY7xD7",
  "type": "assistant",
  "uuid": "18676244-4675-47bf-8651-fc825a5a0d19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Di92mMAyHAXiHB664te2Wu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1969,
      "cache_creation_input_tokens": 9334,
      "cache_read_input_tokens": 32249,
      "output_tokens": 778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9334,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1969,
          "output_tokens": 778,
          "cache_read_input_tokens": 32249,
          "cache_creation_input_tokens": 9334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9334
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

_source line 25 · 2026-05-12T00:05:24.516Z_

<details><summary>↩ Tool result · `toolu_01BqKJ4V6quSxQMDAEeoNxHf`</summary>

```text
Here are my findings for all three papers:

---

## Paper 1: "From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection"

**Exists?** Yes. It is on arXiv as [2604.06066](https://arxiv.org/abs/2604.06066), published April 7, 2026.

**Characterization accuracy:** The proposal's claim that it "documents cascading formatting errors under strict structural constraints in Qwen3-8B" is **accurate**. The paper evaluates Qwen3-8B (an 8-billion-parameter model) and finds that imposing structured reflection via Outlines-based constrained decoding triggers a failure mode they call "structure snowballing" -- where the cognitive load of satisfying strict formatting rules pushes the model into formatting traps. Baseline accuracy dropped from 50.0% to 38.0% under constrained conditions, demonstrating a clear "alignment tax."

---

## Paper 2: "Draft-Conditioned Constrained Decoding for Structured Generation in LLMs"

**Exists?** Yes. It is on arXiv as [2603.03305](https://arxiv.org/abs/2603.03305), submitted February 8, 2026 (published in March 2026 on arXiv, consistent with the "Mar 2026" claim).

**Characterization accuracy:** The proposal's claims are **accurate but require slight nuance**:

- **"Projection tax"**: Correct. The paper analyzes constrained decoding through a KL-projection view and explicitly uses the term "projection tax" to describe the cumulative distortion induced by hard constraints.
- **"+24pp gains on GSM8K"**: Correct. DCCD improves strict structured accuracy by up to +24 percentage points over standard constrained decoding on GSM8K (e.g., 15.2% to 39.0% with a 1B model). However, it is worth noting this is the gain for a very small 1B model. Larger models (7B--14B) already have strong baselines and the absolute gains are smaller (though DCCD still helps). The proposal should ideally mention the model size when citing this number, as "+24pp" without context could be misleading about the general magnitude of improvement.

---

## Paper 3: CRANE (Banerjee et al., ICML 2025)

**Exists?** Yes. Published as [CRANE: Reasoning with constrained LLM generation](https://proceedings.mlr.press/v267/banerjee25a.html) at ICML 2025 (PMLR 267:2836-2857). Also on arXiv as [2502.09061](https://arxiv.org/abs/2502.09061).

**Characterization accuracy:** The proposal's claim that "CRANE proved that constrained decoding limits LLMs to TC^0 complexity" is **substantively correct but slightly overstated**. What the paper actually shows (Proposition 3.1) is:

- A single LLM autoregressive step can be simulated by a logspace-uniform constant-depth threshold circuit (TC^0).
- Therefore, LLMs under restrictive constrained decoding (grammars that only allow syntactically valid final answers with no room for intermediate reasoning tokens) can only solve problems within TC^0.
- Unless TC^0 = NL, such constrained LLMs cannot solve problems like st-connectivity that unconstrained LLMs can handle.

The nuance is that this limitation applies specifically to constrained decoding with **restrictive grammars that forbid intermediate reasoning steps**. CRANE's own solution demonstrates that augmenting the grammar to allow reasoning tokens removes this limitation. So the claim "constrained decoding limits LLMs to TC^0" is correct only for the restrictive case -- CRANE itself shows the limitation is avoidable by designing better grammars.

---

## Summary

| Paper | Exists? | Characterization |
|-------|---------|-----------------|
| Structure Snowballing (Apr 2026) | Yes | Accurate |
| DCCD (Mar 2026) | Yes | Accurate, but +24pp figure is specific to a 1B model |
| CRANE (ICML 2025) | Yes | Substantively correct, but the TC^0 limit applies only to restrictive grammars, not all constrained decoding |

Sources:
- [From Hallucination to Structure Snowballing (arXiv)](https://arxiv.org/abs/2604.06066)
- [From Hallucination to Structure Snowballing (HTML)](https://arxiv.org/html/2604.06066)
- [Draft-Conditioned Constrained Decoding (arXiv)](https://arxiv.org/abs/2603.03305)
- [Draft-Conditioned Constrained Decoding (PDF)](https://arxiv.org/pdf/2603.03305)
- [CRANE: Reasoning with constrained LLM generation (ICML proceedings)](https://proceedings.mlr.press/v267/banerjee25a.html)
- [CRANE (arXiv)](https://arxiv.org/abs/2502.09061)
- [CRANE (OpenReview)](https://openreview.net/forum?id=wKs9fHYxCV)
- [CRANE (ICML poster)](https://icml.cc/virtual/2025/poster/43624)

agentId: a02c99b6bc249deff (use SendMessage with to: 'a02c99b6bc249deff' to continue this agent)
&lt;usage>total_tokens: 16416
tool_uses: 6
duration_ms: 55463&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc5c4986-8951-4749-9dc6-dccf2c92bfc6",
  "isSidechain": false,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "type": "user",
  "uuid": "50b1a66b-84e4-497b-a6a5-31ae222bc3e9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two more papers cited in an ML proposal:\n\n1. **\"From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection\"** — claimed arXiv Apr 2026. The proposal says it \"documents cascading formatting errors under strict structural constraints in Qwen3-8B.\" Search for this paper on arXiv. Does it exist? Is the characterization accurate?\n\n2. **\"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs\"** — claimed arXiv Mar 2026. The proposal says it demonstrates a \"projection tax\" from constrained decoding and achieves +24pp gains on GSM8K. Search for this paper. Does it exist? Is it accurately characterized?\n\n3. Also search for: \"CRANE constrained decoding reasoning ICML 2025 Banerjee\" — the proposal claims CRANE proved that constrained decoding limits LLMs to TC⁰ complexity. Verify this.\n\nUse WebSearch for each. Report findings.",
    "agentId": "a02c99b6bc249deff",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings for all three papers:\n\n---\n\n## Paper 1: \"From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection\"\n\n**Exists?** Yes. It is on arXiv as [2604.06066](https://arxiv.org/abs/2604.06066), published April 7, 2026.\n\n**Characterization accuracy:** The proposal's claim that it \"documents cascading formatting errors under strict structural constraints in Qwen3-8B\" is **accurate**. The paper evaluates Qwen3-8B (an 8-billion-parameter model) and finds that imposing structured reflection via Outlines-based constrained decoding triggers a failure mode they call \"structure snowballing\" -- where the cognitive load of satisfying strict formatting rules pushes the model into formatting traps. Baseline accuracy dropped from 50.0% to 38.0% under constrained conditions, demonstrating a clear \"alignment tax.\"\n\n---\n\n## Paper 2: \"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs\"\n\n**Exists?** Yes. It is on arXiv as [2603.03305](https://arxiv.org/abs/2603.03305), submitted February 8, 2026 (published in March 2026 on arXiv, consistent with the \"Mar 2026\" claim).\n\n**Characterization accuracy:** The proposal's claims are **accurate but require slight nuance**:\n\n- **\"Projection tax\"**: Correct. The paper analyzes constrained decoding through a KL-projection view and explicitly uses the term \"projection tax\" to describe the cumulative distortion induced by hard constraints.\n- **\"+24pp gains on GSM8K\"**: Correct. DCCD improves strict structured accuracy by up to +24 percentage points over standard constrained decoding on GSM8K (e.g., 15.2% to 39.0% with a 1B model). However, it is worth noting this is the gain for a very small 1B model. Larger models (7B--14B) already have strong baselines and the absolute gains are smaller (though DCCD still helps). The proposal should ideally mention the model size when citing this number, as \"+24pp\" without context could be misleading about the general magnitude of improvement.\n\n---\n\n## Paper 3: CRANE (Banerjee et al., ICML 2025)\n\n**Exists?** Yes. Published as [CRANE: Reasoning with constrained LLM generation](https://proceedings.mlr.press/v267/banerjee25a.html) at ICML 2025 (PMLR 267:2836-2857). Also on arXiv as [2502.09061](https://arxiv.org/abs/2502.09061).\n\n**Characterization accuracy:** The proposal's claim that \"CRANE proved that constrained decoding limits LLMs to TC^0 complexity\" is **substantively correct but slightly overstated**. What the paper actually shows (Proposition 3.1) is:\n\n- A single LLM autoregressive step can be simulated by a logspace-uniform constant-depth threshold circuit (TC^0).\n- Therefore, LLMs under restrictive constrained decoding (grammars that only allow syntactically valid final answers with no room for intermediate reasoning tokens) can only solve problems within TC^0.\n- Unless TC^0 = NL, such constrained LLMs cannot solve problems like st-connectivity that unconstrained LLMs can handle.\n\nThe nuance is that this limitation applies specifically to constrained decoding with **restrictive grammars that forbid intermediate reasoning steps**. CRANE's own solution demonstrates that augmenting the grammar to allow reasoning tokens removes this limitation. So the claim \"constrained decoding limits LLMs to TC^0\" is correct only for the restrictive case -- CRANE itself shows the limitation is avoidable by designing better grammars.\n\n---\n\n## Summary\n\n| Paper | Exists? | Characterization |\n|-------|---------|-----------------|\n| Structure Snowballing (Apr 2026) | Yes | Accurate |\n| DCCD (Mar 2026) | Yes | Accurate, but +24pp figure is specific to a 1B model |\n| CRANE (ICML 2025) | Yes | Substantively correct, but the TC^0 limit applies only to restrictive grammars, not all constrained decoding |\n\nSources:\n- [From Hallucination to Structure Snowballing (arXiv)](https://arxiv.org/abs/2604.06066)\n- [From Hallucination to Structure Snowballing (HTML)](https://arxiv.org/html/2604.06066)\n- [Draft-Conditioned Constrained Decoding (arXiv)](https://arxiv.org/abs/2603.03305)\n- [Draft-Conditioned Constrained Decoding (PDF)](https://arxiv.org/pdf/2603.03305)\n- [CRANE: Reasoning with constrained LLM generation (ICML proceedings)](https://proceedings.mlr.press/v267/banerjee25a.html)\n- [CRANE (arXiv)](https://arxiv.org/abs/2502.09061)\n- [CRANE (OpenReview)](https://openreview.net/forum?id=wKs9fHYxCV)\n- [CRANE (ICML poster)](https://icml.cc/virtual/2025/poster/43624)"
      }
    ],
    "totalDurationMs": 55463,
    "totalTokens": 16416,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 862,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 13208,
      "output_tokens": 1307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 862,
          "output_tokens": 1307,
          "cache_read_input_tokens": 13208,
          "cache_creation_input_tokens": 1039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1039,
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
  "sourceToolAssistantUUID": "dc5c4986-8951-4749-9dc6-dccf2c92bfc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T00:06:34.777Z_

<details><summary>↩ Tool result · `toolu_01FQBmvGV2XTHvQEXYURbnUt`</summary>

```text
I now have enough data to provide a thorough analysis. Here is my assessment:

---

## Compute Estimate Analysis: ~170 H100-80GB Hours for IE Research

### 1. Dataset Sizes

**ACE05 (English):**
- ~599 documents total (479 train / 60 dev / 60 test)
- ~19,718 sentences total (16,105 train / 2,015 dev / 1,598 test)
- ~61,321 entity mentions
- This is a **small-medium** dataset by modern standards.

**SciERC:**
- 500 scientific abstracts
- ~2,687 sentences total (1,861 train / 275 dev / 551 test)
- 6 entity types, 7 relation types
- This is a **small** dataset.

**Combined inference corpus:** For evaluation purposes, the relevant splits are test (and possibly dev for tuning). That is roughly 1,598 + 551 = ~2,149 test sentences, and ~2,015 + 275 = ~2,290 dev sentences. For training baselines like GoLLIE, the training sets total ~17,966 sentences.

### 2. Inference Throughput: 8B Models on H100

vLLM achieves approximately **12,500 tokens/second** for Llama-3.1-8B (BF16) on a single H100-80GB. At typical IE prompt+completion lengths (say ~500-1,000 tokens per example including the prompt and structured output), this means roughly **12-25 examples per second** in batch mode.

For the test sets alone (~2,149 sentences), raw unconstrained inference would take roughly **1.5-3 minutes per model per strategy**. Even running over the full datasets (train+dev+test, ~22,000 sentences) at these speeds, a single pass would take **15-30 minutes**.

### 3. Constrained Decoding Overhead

Modern constrained decoding with xgrammar/outlines in vLLM adds overhead but is heavily optimized. Naive implementations can add 2-5x overhead, but with xgrammar's compiled finite state machines, the practical overhead is more like **1.3-2x** for well-structured grammars. For complex IE grammars, expect the higher end. This still keeps individual runs well under an hour for these datasets.

### 4. GoLLIE Fine-Tuning Cost (The Major Cost Driver)

GoLLIE was originally trained on 2x A100-80GB for 3 epochs with batch size 32. For an 8B model fine-tuned on IE datasets:

- Full fine-tuning of an 8B model on a single H100: **8-20 hours** depending on dataset size and epochs
- LoRA/QLoRA fine-tuning: **2-6 hours** on a single H100
- The proposal likely needs to fine-tune GoLLIE-style models for **2 base models x 2 datasets = 4 fine-tuning runs**
- If full fine-tuning: ~4 x 10-20h = **40-80 H100-hours** just for GoLLIE
- If LoRA: ~4 x 3-6h = **12-24 H100-hours**

### 5. Full Experiment Breakdown Estimate

Let me enumerate all experimental configurations:

**Inference-only experiments (2 models x 2 datasets x test+dev):**

| Configuration | Runs | Est. Time per Run | Subtotal |
|---|---|---|---|
| Unconstrained baseline | 4 | 0.5-1h | 2-4h |
| JSON-only grammar | 4 | 0.5-1.5h | 2-6h |
| Post-hoc filtering | 4 | 0.5-1h | 2-4h |
| Direct constrained decoding | 4 | 1-2h | 4-8h |
| Two-pass extraction | 4 (x2 passes) | 1-3h | 4-12h |

Inference subtotal: **~14-34 H100-hours**

**GoLLIE fine-tuning + inference:**

| Configuration | Runs | Est. Time per Run | Subtotal |
|---|---|---|---|
| GoLLIE fine-tuning | 4 | 10-20h (full FT) | 40-80h |
| GoLLIE inference | 4 | 0.5-1h | 2-4h |

GoLLIE subtotal: **~42-84 H100-hours**

**Ablations** (assume ~50% of primary experiments repeated with variations):
- ~15-30 H100-hours

**Hyperparameter sweeps, debugging, failed runs** (standard 1.5-2x overhead):
- ~20-40 H100-hours

### 6. Total Estimate

| Component | Low Estimate | High Estimate |
|---|---|---|
| Inference-only experiments | 14h | 34h |
| GoLLIE fine-tuning + inference | 42h | 84h |
| Ablations | 15h | 30h |
| Debugging/sweeps overhead | 20h | 40h |
| **Total** | **~91h** | **~188h** |

### Verdict

**The ~170 H100-hour estimate is realistic and reasonable.** It falls squarely in the middle of the plausible range (91-188h). Here is the reasoning:

- **ACE05 and SciERC are small datasets**, so raw inference is cheap. This part alone would take well under 40 hours even with constrained decoding overhead.
- **GoLLIE is the dominant cost driver.** Fine-tuning 4 model-dataset combinations (2 models x 2 datasets) as a baseline accounts for roughly half the total budget. If they use full fine-tuning rather than LoRA (which is likely, since GoLLIE's original approach uses full fine-tuning), this alone could be 40-80 hours.
- **The 170h estimate implicitly budgets ~30-40% for overhead** (debugging, hyperparameter tuning, failed runs, re-runs), which is a standard and prudent assumption for research projects.
- **The estimate would be unreasonable** only if they were using LoRA exclusively for GoLLIE and had no ablations -- in that case, ~80-100h would suffice. Conversely, if ablations are extensive or they run many hyperparameter sweeps, 170h could even be slightly tight.

**One flag:** If the proposal intends to train GoLLIE from scratch (rather than adapting existing GoLLIE weights to the new base models Qwen3-8B and Llama-3.1-8B), the fine-tuning cost could be higher since GoLLIE was originally based on Code-Llama, and porting the approach to different architectures may require more tuning iterations.

Sources:
- [ACE 2005 Multilingual Training Corpus - LDC](https://catalog.ldc.upenn.edu/LDC2006T06)
- [ACE05-Processor - GitHub](https://github.com/wasiahmad/ACE05-Processor)
- [SciERC Dataset - Papers With Code](https://paperswithcode.com/dataset/scierc)
- [SciERC - Multi-Task Identification of Entities, Relations, and Coreference - ACL Anthology](https://aclanthology.org/D18-1360/)
- [vLLM v0.6.0 Performance Update](https://blog.vllm.ai/2024/09/05/perf-update.html)
- [Llama 3.1 8B Performance on H100 - Microsoft](https://techcommunity.microsoft.com/blog/azurehighperformancecomputingblog/performance-of-llama-3-1-8b-ai-inference-using-vllm-on-nd-h100-v5/4448355)
- [Benchmarking Llama 3.1 8B on H100 and A100 - Ori](https://www.ori.co/blog/benchmarking-llama-3.1-8b-instruct-on-nvidia-h100-and-a100-chips-with-the-vllm-inferencing-engine)
- [GoLLIE Paper - arXiv](https://arxiv.org/abs/2310.03668)
- [GoLLIE - GitHub](https://github.com/hitz-zentroa/GoLLIE)
- [Guided Decoding Performance - SqueezeBits](https://blog.squeezebits.com/guided-decoding-performance-vllm-sglang)
- [Structured Decoding in vLLM - vLLM Blog](https://blog.vllm.ai/2025/01/14/struct-decode-intro.html)
- [Fine-Tuning Qwen3-8B - E2E Networks](https://www.e2enetworks.com/blog/fine-tuning-qwen3-8b-medical-reasoning-qlora-e2e-networks-a100)
- [How to Fine-Tune LLMs in 2026 - Spheron](https://www.spheron.network/blog/how-to-fine-tune-llm-2026/)

agentId: a3a1f63a014b62f49 (use SendMessage with to: 'a3a1f63a014b62f49' to continue this agent)
&lt;usage>total_tokens: 25886
tool_uses: 12
duration_ms: 117714&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18676244-4675-47bf-8651-fc825a5a0d19",
  "isSidechain": false,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "type": "user",
  "uuid": "20c7cf18-e275-41e5-8e1f-ac4b04cee814",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify whether the following compute resource estimate is realistic for an IE (Information Extraction) research project:\n\nThe proposal claims ~170h H100-80GB for:\n- 2 datasets (ACE05, SciERC)\n- 2 models (Qwen3-8B, Llama-3.1-8B)\n- 2 primary strategies (direct constrained decoding, two-pass extraction)\n- 4 baselines (unconstrained, JSON-only grammar, post-hoc filtering, GoLLIE)\n- Plus ablations\n\nSearch for:\n1. \"ACE05 dataset size\" — how many examples are in ACE05?\n2. \"SciERC dataset size\" — how many examples in SciERC?\n3. \"vLLM inference throughput 8B model H100\" — what's the typical inference throughput?\n4. \"GoLLIE training cost GPU hours\" — how expensive is it to run GoLLIE?\n\nBased on the dataset sizes and typical inference throughput for 8B models on H100, estimate whether ~170h is reasonable for the described experiments. Key considerations:\n- ACE05 and SciERC are small-medium datasets\n- 8B models on H100 should have fast inference\n- But GoLLIE requires fine-tuning, which is more expensive\n- Constrained decoding adds overhead\n\nReport your analysis.",
    "agentId": "a3a1f63a014b62f49",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have enough data to provide a thorough analysis. Here is my assessment:\n\n---\n\n## Compute Estimate Analysis: ~170 H100-80GB Hours for IE Research\n\n### 1. Dataset Sizes\n\n**ACE05 (English):**\n- ~599 documents total (479 train / 60 dev / 60 test)\n- ~19,718 sentences total (16,105 train / 2,015 dev / 1,598 test)\n- ~61,321 entity mentions\n- This is a **small-medium** dataset by modern standards.\n\n**SciERC:**\n- 500 scientific abstracts\n- ~2,687 sentences total (1,861 train / 275 dev / 551 test)\n- 6 entity types, 7 relation types\n- This is a **small** dataset.\n\n**Combined inference corpus:** For evaluation purposes, the relevant splits are test (and possibly dev for tuning). That is roughly 1,598 + 551 = ~2,149 test sentences, and ~2,015 + 275 = ~2,290 dev sentences. For training baselines like GoLLIE, the training sets total ~17,966 sentences.\n\n### 2. Inference Throughput: 8B Models on H100\n\nvLLM achieves approximately **12,500 tokens/second** for Llama-3.1-8B (BF16) on a single H100-80GB. At typical IE prompt+completion lengths (say ~500-1,000 tokens per example including the prompt and structured output), this means roughly **12-25 examples per second** in batch mode.\n\nFor the test sets alone (~2,149 sentences), raw unconstrained inference would take roughly **1.5-3 minutes per model per strategy**. Even running over the full datasets (train+dev+test, ~22,000 sentences) at these speeds, a single pass would take **15-30 minutes**.\n\n### 3. Constrained Decoding Overhead\n\nModern constrained decoding with xgrammar/outlines in vLLM adds overhead but is heavily optimized. Naive implementations can add 2-5x overhead, but with xgrammar's compiled finite state machines, the practical overhead is more like **1.3-2x** for well-structured grammars. For complex IE grammars, expect the higher end. This still keeps individual runs well under an hour for these datasets.\n\n### 4. GoLLIE Fine-Tuning Cost (The Major Cost Driver)\n\nGoLLIE was originally trained on 2x A100-80GB for 3 epochs with batch size 32. For an 8B model fine-tuned on IE datasets:\n\n- Full fine-tuning of an 8B model on a single H100: **8-20 hours** depending on dataset size and epochs\n- LoRA/QLoRA fine-tuning: **2-6 hours** on a single H100\n- The proposal likely needs to fine-tune GoLLIE-style models for **2 base models x 2 datasets = 4 fine-tuning runs**\n- If full fine-tuning: ~4 x 10-20h = **40-80 H100-hours** just for GoLLIE\n- If LoRA: ~4 x 3-6h = **12-24 H100-hours**\n\n### 5. Full Experiment Breakdown Estimate\n\nLet me enumerate all experimental configurations:\n\n**Inference-only experiments (2 models x 2 datasets x test+dev):**\n\n| Configuration | Runs | Est. Time per Run | Subtotal |\n|---|---|---|---|\n| Unconstrained baseline | 4 | 0.5-1h | 2-4h |\n| JSON-only grammar | 4 | 0.5-1.5h | 2-6h |\n| Post-hoc filtering | 4 | 0.5-1h | 2-4h |\n| Direct constrained decoding | 4 | 1-2h | 4-8h |\n| Two-pass extraction | 4 (x2 passes) | 1-3h | 4-12h |\n\nInference subtotal: **~14-34 H100-hours**\n\n**GoLLIE fine-tuning + inference:**\n\n| Configuration | Runs | Est. Time per Run | Subtotal |\n|---|---|---|---|\n| GoLLIE fine-tuning | 4 | 10-20h (full FT) | 40-80h |\n| GoLLIE inference | 4 | 0.5-1h | 2-4h |\n\nGoLLIE subtotal: **~42-84 H100-hours**\n\n**Ablations** (assume ~50% of primary experiments repeated with variations):\n- ~15-30 H100-hours\n\n**Hyperparameter sweeps, debugging, failed runs** (standard 1.5-2x overhead):\n- ~20-40 H100-hours\n\n### 6. Total Estimate\n\n| Component | Low Estimate | High Estimate |\n|---|---|---|\n| Inference-only experiments | 14h | 34h |\n| GoLLIE fine-tuning + inference | 42h | 84h |\n| Ablations | 15h | 30h |\n| Debugging/sweeps overhead | 20h | 40h |\n| **Total** | **~91h** | **~188h** |\n\n### Verdict\n\n**The ~170 H100-hour estimate is realistic and reasonable.** It falls squarely in the middle of the plausible range (91-188h). Here is the reasoning:\n\n- **ACE05 and SciERC are small datasets**, so raw inference is cheap. This part alone would take well under 40 hours even with constrained decoding overhead.\n- **GoLLIE is the dominant cost driver.** Fine-tuning 4 model-dataset combinations (2 models x 2 datasets) as a baseline accounts for roughly half the total budget. If they use full fine-tuning rather than LoRA (which is likely, since GoLLIE's original approach uses full fine-tuning), this alone could be 40-80 hours.\n- **The 170h estimate implicitly budgets ~30-40% for overhead** (debugging, hyperparameter tuning, failed runs, re-runs), which is a standard and prudent assumption for research projects.\n- **The estimate would be unreasonable** only if they were using LoRA exclusively for GoLLIE and had no ablations -- in that case, ~80-100h would suffice. Conversely, if ablations are extensive or they run many hyperparameter sweeps, 170h could even be slightly tight.\n\n**One flag:** If the proposal intends to train GoLLIE from scratch (rather than adapting existing GoLLIE weights to the new base models Qwen3-8B and Llama-3.1-8B), the fine-tuning cost could be higher since GoLLIE was originally based on Code-Llama, and porting the approach to different architectures may require more tuning iterations.\n\nSources:\n- [ACE 2005 Multilingual Training Corpus - LDC](https://catalog.ldc.upenn.edu/LDC2006T06)\n- [ACE05-Processor - GitHub](https://github.com/wasiahmad/ACE05-Processor)\n- [SciERC Dataset - Papers With Code](https://paperswithcode.com/dataset/scierc)\n- [SciERC - Multi-Task Identification of Entities, Relations, and Coreference - ACL Anthology](https://aclanthology.org/D18-1360/)\n- [vLLM v0.6.0 Performance Update](https://blog.vllm.ai/2024/09/05/perf-update.html)\n- [Llama 3.1 8B Performance on H100 - Microsoft](https://techcommunity.microsoft.com/blog/azurehighperformancecomputingblog/performance-of-llama-3-1-8b-ai-inference-using-vllm-on-nd-h100-v5/4448355)\n- [Benchmarking Llama 3.1 8B on H100 and A100 - Ori](https://www.ori.co/blog/benchmarking-llama-3.1-8b-instruct-on-nvidia-h100-and-a100-chips-with-the-vllm-inferencing-engine)\n- [GoLLIE Paper - arXiv](https://arxiv.org/abs/2310.03668)\n- [GoLLIE - GitHub](https://github.com/hitz-zentroa/GoLLIE)\n- [Guided Decoding Performance - SqueezeBits](https://blog.squeezebits.com/guided-decoding-performance-vllm-sglang)\n- [Structured Decoding in vLLM - vLLM Blog](https://blog.vllm.ai/2025/01/14/struct-decode-intro.html)\n- [Fine-Tuning Qwen3-8B - E2E Networks](https://www.e2enetworks.com/blog/fine-tuning-qwen3-8b-medical-reasoning-qlora-e2e-networks-a100)\n- [How to Fine-Tune LLMs in 2026 - Spheron](https://www.spheron.network/blog/how-to-fine-tune-llm-2026/)"
      }
    ],
    "totalDurationMs": 117714,
    "totalTokens": 25886,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1178,
      "cache_creation_input_tokens": 2347,
      "cache_read_input_tokens": 20053,
      "output_tokens": 2308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2347
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1178,
          "output_tokens": 2308,
          "cache_read_input_tokens": 20053,
          "cache_creation_input_tokens": 2347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2347,
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
  "sourceToolAssistantUUID": "18676244-4675-47bf-8651-fc825a5a0d19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "20c7cf18-e275-41e5-8e1f-ac4b04cee814",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Semantic constraint compilation for IE decoding",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

### Assistant

_source line 29 · 2026-05-12T00:09:06.788Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive findings from all my research agents. Let me synthesize my review.

## Key findings from my research:

### Citation Verification
1. **IterGen (ICLR 2025)** — Confirmed, characterization accurate
2. **Synchromesh (ICLR 2022)** — Confirmed, characterization accurate
3. **EnriCo (arXiv 2024)** — Exists, but the "~1 F1 improvement" characterization is misleading — entity F1 improved by ~30 points, relation F1 by ~0.5 points


4. **The Format Tax (arXiv Apr 2026)** — Confirmed, ~70/30 characterization is reasonable approximation
5. **XGrammar-2 (arXiv Jan 2026)** — Confirmed, TagDispatch confirmed, though "mask_callback" may not be the paper's exact terminology
6. **Structure Snowballing (arXiv Apr 2026)** — Confirmed, characterization accurate
7. **DCCD (arXiv Mar 2026)** — Confirmed, though the +24pp improvement is specific to the 1B model
8. **CRANE** — Still verifying details...
9. **GoLLIE (ICLR 2024)** — Confirmed, shows roughly 13-17 F1 point improvements depending on the baseline

Now I'm checking the competing work landscape. The search turned up several related papers, but nothing that directly matches what I'm proposing. A few new papers surfaced that aren't currently cited—one on ontology-constrained clinical summaries and another prompt-based approach from Apple—though most of the relevant work is already accounted for.

On the violation rate claim, I'm finding that the assertion about no prior systematic measurement of ontology type violations in LLM-based IE holds up reasonably well. There's scattered evidence of constraint violations in existing work, but nothing that directly addresses this gap the way the proposal does.

For SOTA benchmarks, PL-Marker sets the baseline on ACE05 RE around 69-71 F1, while HGERE achieves strong results on SciERC with 86.85% NER and 61.10% strict RE F1—though these are discriminative models, so they're not directly comparable to the LLM-based approach being proposed.

The resource estimate of ~170 H100 hours looks solid and fits comfortably within the 200-hour constraint, with GoLLIE fine-tuning being the main bottleneck. For the engineering side, vLLM's custom LogitsProcessors can handle the constraint decoding, and while composing with XGrammar isn't explicitly documented, it's technically feasible at the infrastructure level.

There's a confirmed bug with Qwen3 and vLLM's structured output that has a workaround and is fixed in 0.9.0, and XGrammar-2 TagDispatch is confirmed working. The EMNLP 2026 deadline is May 25—14 days away.

Looking at novelty, the core contributions hold up: automatic compilation from IE ontologies to constraints is genuinely novel, the two-pass strategy for converting context-sensitive to context-free constraints is IE-specific and original, and systematically quantifying ontology violations appears mostly novel. The forward-only approach clearly differentiates from IterGen's backtracking strategy.

That said, the space is already crowded with Synchromesh, IterGen, EnriCo, and other constrained decoding work for IE. The grammar-plus-semantic-constraint paradigm itself isn't new—the novelty really comes from the automatic compilation and IE-specific strategies. The "zero-code schema compliance" framing is practically compelling but scientifically feels somewhat incremental over existing work. I'd rate novelty around 3.5—the automatic compilation and two-pass approach are genuinely interesting, but the underlying paradigm is established and extending it to IE feels somewhat natural.

On feasibility, the ~170 hours on H100 fits within the 200-hour constraint, and with 14 days left (not 16 as stated—today is May 11), the timeline is extremely tight. The scope is reasonable though: two datasets, two models, two strategies keeps it manageable.

The main engineering risks are the unified LogitsProcessor, XGrammar composition, and the complexity of the ACE05 event ontology. The GoLLIE baseline also requires fine-tuning, which eats into the timeline. It's aggressive but doable if the researcher has relevant experience—I'd give feasibility a 3.

The proposal itself is exceptionally well-written with comprehensive landscape coverage and clear technical exposition. The intellectual honesty about the violation rate risk is refreshing. Clarity gets a 4.5.

Impact hinges entirely on whether violation rates are high enough to matter. If they're above 15%, this is clearly valuable; below 5% and it becomes "LLMs already handle this." That uncertainty is acknowledged but remains the paper's biggest vulnerability.

Averaging the scores gives 3.625, which falls short of the 4.0 threshold. The core problems are the 14-day timeline being genuinely tight, the unvalidated assumption about violation rates, and solid but not exceptional novelty.

But wait—this proposal has already cycled through three review rounds with meaningful improvements. The R3 reviewer's concerns have been systematically addressed: the resource budget is now reasonable at 170 hours, the dataset focus is tighter, the violation rate risk is acknowledged, and the related work section has been substantially expanded. The remaining feedback items appear to have been resolved.

Looking at this more carefully, the two-pass strategy is actually quite specific to IE—it's not just applying an existing technique but rather exploiting the structure of IE ontologies by converting context-sensitive constraints into context-free ones through entity conditioning. That's genuinely novel, though I'd rate it around 3.5 rather than exceptional. The real constraint is the 14-day timeline, which needs to cover the ontology compiler, the vLLM integration, experiments across multiple datasets and models, and paper writing. It's ambitious, but the proposal seems to have thought through the scope.

Now I'm noticing a discrepancy with the EnriCo baseline—the proposal characterizes it as showing only ~1 F1 improvement from constraints on ACE05, but my research found it actually improved entity F1 by roughly 30 points while relation F1 barely moved.  The ~1 F1 figure likely refers to relation F1, which is technically accurate but obscures how effective constraints were for entity extraction. That said, EnriCo's constraints operate at the span level (preventing overlaps, enforcing type consistency), whereas OntoCoDec targets cross-field type constraints like relation domain and range restrictions—so the entity gains may not directly transfer to a generative setting. The relation F1 improvement is the more apples-to-apples comparison here.

Now I'm weighing whether this proposal clears the 4.0 bar. The work is well-motivated with solid technical execution, appropriate scope, and honest acknowledgment of risks around violation rates. The dual contribution—both the constraint compiler and the empirical analysis of different constraint strategies—is meaningful, and the two-pass approach is genuinely novel for information extraction. The main concerns are the compressed timeline for engineering and experiments, plus the heavy dependence on how often constraints actually get violated in practice. The novelty is there, but execution risk is real. but incremental over the established grammar+semantic paradigm. I'm missing some related work, though that's minor.

Scoring this: novelty at 3.5 for solid contributions like S2 and automatic compilation but within an established paradigm, feasibility at 3.0 since the compute is manageable but 14 days is extremely aggressive for the full scope, clarity at 4.5 for excellent writing and honest risk framing, and impact at 3.0 since it hinges on violation rates being significant with no preliminary evidence. That averages to 3.5, below the 4.0 threshold.

The timeline is the killer here—fitting a compiler, LogitsProcessor, evaluations across multiple datasets and models with baselines and ablations, plus paper writing into two weeks is unrealistic even for experienced researchers. The impact is also speculative without knowing if violation rates are actually meaningful, and while the novelty is solid, it doesn't quite reach the exceptional bar needed for acceptance.

My recommendation is to scope down significantly: focus on a single primary model like Qwen3-8B and run an unconstrained baseline first to measure actual violation rates. If they're below 5%, reframe this as a negative result with engineering value. If they're higher, then pursue the full evaluation. I should also reconsider the GoLLIE baseline since fine-tuning could take 40-80 hours—either use pre-trained weights if available or treat it as a discussion point rather than a full experimental baseline. than a full empirical baseline.
3. Consider running a quick pilot experiment to establish violation rates before committing to the full evaluation. This de-risks the entire project.

Actually, let me reconsider. This is round 4 of 10. The proposal has improved significantly and addresses all R3 issues. The remaining concerns are:

1. Timeline — hard to fix, it's a hard constraint
2. Impact risk — acknowledged, framed well
3. Novelty — solid, improved from earlier rounds

For a "revise" verdict, I should give actionable feedback. Let me think about what specific changes would make this pass.

For a pass, I'd need:
- Feasibility score ≥ 3.5: Narrow scope for EMNLP timeline, have AAAI as primary target
- Impact score ≥ 3.5: Frame the violation rate quantification more centrally as the primary contribution, with constraint enforcement as secondary
- Novelty stays at 3.5, Clarity stays at 4.5
- Average would be (3.5 + 3.5 + 4.5 + 3.5) / 4 = 3.75 — still below 4.0

To reach 4.0 average, I'd need novelty or impact to hit 4.0. The two-pass strategy is genuinely novel — it converts context-sensitive constraints to context-free ones by conditioning the grammar on prior extraction results, which exploits IE-specific structure in ways existing approaches can't. The automatic compilation is a real zero-code contribution. Though I think 3.5 is fair since it's a solid extension of existing paradigms rather than a fundamental shift.

For impact, if the paper includes violation rate quantification, strategy comparison, and GoLLIE complementarity testing, those are independently interesting contributions. But the violation rate risk could undermine the headline contribution.

This feels like a genuinely 3.5 average idea — solid work and well-framed, but not quite at the "clearly top venue" level yet. The main blockers are timeline and conditional impact. Let me think about whether I'm being too harsh here. The user is targeting EMNLP 2026, which includes Findings track, and Findings has a lower acceptance bar than Main. For Findings quality, this could actually work. Since they listed both Main and Findings as targets, Findings would be acceptable.

For Findings, the novelty bar is lower — a solid technical contribution with clear experiments is usually sufficient. So a 3.5 novelty score might be acceptable there. But I should score the idea quality itself, not venue fit.

The proposal is genuinely well-developed and solid. The real constraints are the 14-day timeline — building a LogitsProcessor with mask intersection, entity registry, and ontology compiler while debugging across two schemas (ACE05's event ontology is particularly complex) is non-trivial, especially after the previous round already tightened scope. And adapting GoLLIE to Qwen3-8B and Llama-3.1-8B requires retraining with different tokenizers and architectures, which could easily consume a week on its own.

The violation rate is also uncertain without preliminary experiments to de-risk it. This feels like a revise recommendation — the idea is sound and publishable, but needs better timeline scoping and risk mitigation strategies.

I should also verify whether the proposal has addressed the competing work I found. Looking back at my search results, the ontology-to-tools compilation paper and the dialogue ontology work are already cited, as is PARSE. The clinical summaries paper from EKAW 2024 isn't cited, though it's a constrained beam search approach rather than directly overlapping.

Scanning through the remaining uncited papers — ODKE+ is the most relevant since it tackles a similar goal with a prompt-based mechanism, but the others like OntoKG and the structure-aware decoding work approach the problem differently enough that their absence isn't a critical gap.

Now checking the EnriCo characterization more carefully. The proposal claims constrained decoding improved relation F1 by about 1 point on ACE05, and that tracks with what I'm finding — entity F1 jumped ~30 points but relation F1 only gained ~0.5 points. The relation comparison is what matters here since OntoCoDec focuses on cross-field type constraints rather than entity-level ones, so the characterization holds up even though it downplays how much the entity constraints helped.

I've also verified the Qwen3 + vLLM workaround details are correct, and now I'm assessing whether the 14-day timeline is realistic. The scope includes implementing the compiler and LogitsProcessor, running 32 experimental configurations across datasets and models, doing ablations, and writing the paper. For an experienced researcher with existing vLLM infrastructure, the first week would cover the core implementation work.

The second week would handle experiments and paper writing, which is extremely tight—especially given the risk of subtle bugs in the LogitsProcessor mask intersection logic. With 2 H100s and ~170 compute hours needed, running experiments 12 hours daily is feasible but leaves little margin for error.

My final assessment is to recommend revision with three key points: the GoLLIE baseline should either use an existing checkpoint or move to discussion, the timeline risk should be mitigated by prioritizing the unconstrained baseline and violation rate measurement first, and the ACE05 event extraction scope should be narrowed to focus on entity and relation constraints rather than all 33 event types, which are too complex for the ontology compiler in this timeframe.

Looking at the scores—novelty 3.5, feasibility 3.0, clarity 4.5, impact 3.0—the average of 3.5 falls below the 4.0 threshold, confirming a revision is needed.

Actually, reconsidering the novelty score, the two-pass strategy is more clever than I initially credited. The core insight is that entity extraction produces type information that constrains which entities can fill relation and event argument slots. By extracting entities first, you can compile those extracted types directly into the grammar for the second pass, converting a context-sensitive constraint—where relation argument types depend on previously extracted entities—into something more tractable.

The automatic compilation from standard schema definitions is also a genuine usability win compared to prior work like Synchromesh, IterGen, and EnriCo, which all require manual specification. So I'll keep novelty at 3.5.

On impact, I'm less convinced. If violation rates stay below 5%, the decoding-time enforcement doesn't add much value, and even with higher violation rates, simple post-hoc filtering might be just as effective. The quantification of violation rates has some merit, but I'm not sure it's substantial enough on its own for a venue like EMNLP. I'll stick with impact at 3.0.

Now thinking about what would actually make this work: the proposal needs to be much more realistic about the 14-day constraint—right now S3 is marked optional but everything else reads mandatory. The GoLLIE baseline alone could eat 40-80 hours and a full week, so either adapt existing weights with LoRA or just compare against published results. For ACE05, start with entity and relation constraints, treat event argument constraints as a stretch goal since those 33 event types are quite involved. And run the violation rate measurement as the first experiment to get that data early.

This approach de-risks the whole project and shapes everything that follows. Even with these cuts, feasibility only reaches 3.5, bringing the average to 3.625—still shy of 4.0. To actually pass, I'd need either novelty or impact to hit 4.0 on its own.

The impact angle works if the violation rate measurement uncovers meaningful patterns—say, some relation types show 30% violations while others are nearly perfect. That kind of granular finding, combined with comparing when decoding-time enforcement actually helps versus the other strategies, could genuinely reach 4.0 impact.

For novelty, the two-pass strategy is the strongest element. If I can provide theoretical analysis showing when S2 strictly dominates S1—like when entity extraction is already accurate—that could push novelty to 4.0.

So my final call is to revise with concrete, actionable feedback.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20c7cf18-e275-41e5-8e1f-ac4b04cee814",
  "isSidechain": false,
  "requestId": "req_011CawhXD8yDfoLNsDxAkANa",
  "type": "assistant",
  "uuid": "cd768552-ecef-476a-adfd-fe99d974fda3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sc9LFxcr9zSCUhaysNqe9Z",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6566,
      "cache_read_input_tokens": 41583,
      "output_tokens": 8079,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8079,
          "cache_read_input_tokens": 41583,
          "cache_creation_input_tokens": 6566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6566
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

_source line 30 · 2026-05-12T00:09:52.646Z_

Now I have comprehensive findings from all my research agents. Let me synthesize the final review.

## Summary of Verification Findings

**Citations**: All major cited papers verified as existing with correct venues. Minor characterization issues: EnriCo's "~1 F1 improvement" understates entity-level gains (~30 F1), though the relation F1 comparison (~0.5) is the relevant one. DCCD's +24pp gain is specific to a 1B model. CRANE's TC⁰ result applies only to restrictive grammars.

**Competing work**: No exact match found for automatic IE ontology-to-constraint compilation. Closest uncited work is ODKE+ (Apple, arXiv Sep 2025, prompt-based ontology guidance), SCG-MEM (arXiv Apr 2026, schema-to-trie for agent memory), and Ontology-Constrained Clinical Summaries (EKAW 2024). None are critical omissions.

**Violation rate claim**: Largely confirmed as a real gap. Partial evidence: ~11% type-restriction false positives on TACRED (traditional models), ~13.9% non-conforming outputs on ADE (Flan-T5), but no systematic study on LLM-based IE.

**Resource estimate**: ~170h H100 verified as realistic (91-188h plausible range). GoLLIE fine-tuning (~40-80h) is the dominant cost driver.

**Venue deadline**: ARR May 25, 2026 confirmed — 14 days from today.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "S2 two-pass strategy converting context-sensitive type constraints to context-free vocabulary constraints is genuinely novel and IE-specific. Automatic 'zero-code' compilation differentiates from Synchromesh (manual Completion Engines) and IterGen (manual callbacks). However, the grammar+semantic constraint paradigm is established (Synchromesh 2022, IterGen 2025), making this a well-executed extension rather than a paradigm shift."},
    "feasibility": {"score": 3, "rationale": "Compute budget (~170h) fits within ≤200 H100-hour constraint and is realistic per my verification. However, 14 days is extremely aggressive for: (1) implementing ontology-to-constraint compiler for ACE05's complex event ontology (33 event types with typed argument roles), (2) engineering a unified LogitsProcessor with correct mask intersection, (3) GoLLIE fine-tuning for 2 base models (~40-80h and significant engineering), (4) running all experiments, and (5) writing the paper. The LogitsProcessor debugging cycle alone is a timeline risk — subtle bugs in entity registry updates or mask intersection can silently produce incorrect results."},
    "clarity": {"score": 4.5, "rationale": "Exceptionally well-written proposal with comprehensive landscape coverage, clear technical architecture, honest risk acknowledgment (violation rates may be low), and precise differentiation from 6+ prior systems. The strategy comparison framing (S1 vs S2 vs post-hoc filtering) clearly articulates the scientific questions beyond engineering."},
    "impact": {"score": 3, "rationale": "Impact is conditional on an unknown quantity: ontology type violation rates. If rates are >10%, the decoding-time enforcement is clearly valuable. If <5%, the paper reduces to a negative result ('LLMs already learn type constraints') plus an engineering contribution. The quantification itself has value, but partial evidence (TACRED ~11% type-restriction false positives in traditional models, PARSE ~12% invalid response rates for GPT-4) suggests LLM violation rates may be modest, making the headline contribution uncertain."}
  },
  "issues": [
    "TIMELINE RISK: 14 days remaining (not 16 — today is May 11, deadline May 25) for implementing compiler + LogitsProcessor + running 2×2×2×4=32 configurations + ablations + paper writing. GoLLIE baseline alone requires fine-tuning Code-Llama-style training on Qwen3-8B and Llama-3.1-8B (different architectures from GoLLIE's original Code-Llama base), estimated at 40-80 H100-hours and significant engineering effort for architecture adaptation.",
    "GoLLIE BASELINE COST: GoLLIE was trained on Code-Llama. Porting to Qwen3-8B and Llama-3.1-8B is not trivial — different tokenizers, different chat templates, different code-generation pretraining. Fine-tuning 4 model-dataset combinations (2 models × 2 datasets) could consume half the compute budget (~40-80h) and a week of engineering time, leaving insufficient budget for the primary contribution experiments.",
    "ACE05 EVENT ONTOLOGY COMPLEXITY: ACE05 has 33 event types with typed argument roles — compiling these into constraint specifications is significantly more complex than entity+relation constraints. The entity type registry must handle event trigger identification, argument role assignment, and role-filler type matching simultaneously. This is the most complex test case and may require disproportionate debugging time for the compiler and LogitsProcessor.",
    "VIOLATION RATE DE-RISKING: The entire project motivation depends on violation rates being non-trivial, but no preliminary experiment is planned to establish this before committing to full implementation. If unconstrained Qwen3-8B on ACE05 produces <3% ontology type violations, the decoding-time enforcement contribution becomes marginal, and the extensive engineering effort (compiler, LogitsProcessor, two-pass strategy) yields minimal F1 improvement.",
    "MISSING MINOR RELATED WORK: ODKE+ (Apple, arXiv Sep 2025) — a production system using prompt-based ontology guidance for knowledge extraction achieving 98.8% precision at scale. Should be discussed as the 'soft constraint' alternative to the proposed 'hard constraint' approach. Also: Document-level RE with Entity Type Constraints (ScienceDirect, May 2026) — training-time type-constrained graph approach for DocRE."
  ],
  "feedback": "The proposal has improved substantially through 3 revision rounds and is close to pass quality. The architecture is sound, the landscape coverage is comprehensive, and the scientific questions are well-formulated. Three specific changes would bring this to pass quality:\n\n1. **De-risk the violation rate on Day 1.** Before any compiler/LogitsProcessor engineering, run unconstrained Qwen3-8B and Llama-3.1-8B on ACE05 and SciERC test sets with a simple JSON schema prompt. Write a lightweight Python script to check extracted outputs against ontology type constraints (relation domain/range, event argument role-filler types). This takes <1 day and <5 H100-hours. If violation rates are >5%, proceed with full implementation. If <5%, pivot immediately: the quantification itself plus the automatic compiler (as a 'guaranteed compliance' engineering tool) become the contribution, and you skip the expensive strategy comparison.\n\n2. **Reduce GoLLIE baseline scope.** Instead of fine-tuning GoLLIE on Qwen3-8B and Llama-3.1-8B from scratch (40-80h, major engineering), either: (a) use GoLLIE's published Code-Llama-34B checkpoint and compare against published numbers on ACE05/SciERC, or (b) adapt via LoRA with the GoLLIE training recipe on one model only (Qwen3-8B), or (c) demote GoLLIE to a discussion comparison rather than a full empirical baseline. This saves 30-60 H100-hours and ~3-5 days of engineering.\n\n3. **Scope ACE05 events as a stretch goal.** Start with entity+relation constraints for both ACE05 and SciERC (the core novel contribution of cross-field type constraints). ACE05 event extraction with 33 typed argument roles is the most complex compilation target — make it a stretch goal that strengthens the paper if achieved but isn't required for the core contribution. This reduces compiler debugging time by ~2-3 days.\n\nWith these changes, the timeline becomes: Day 1-2: violation rate pilot + analysis. Day 2-6: compiler + LogitsProcessor for entity+relation constraints. Day 6-10: experiments (S1, S2, baselines). Day 10-14: ablations + paper writing + optional event constraints. This is still tight but feasible for an experienced systems+NLP researcher.",
  "reason": "Sound architecture and well-positioned novelty, but 14-day timeline is too aggressive for full scope (GoLLIE fine-tuning + ACE05 events + 32 configurations), and impact hinges on unknown violation rates that should be measured before committing to implementation."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd768552-ecef-476a-adfd-fe99d974fda3",
  "isSidechain": false,
  "requestId": "req_011CawhXD8yDfoLNsDxAkANa",
  "type": "assistant",
  "uuid": "80bc3c7c-5fd1-49a4-8103-52fe5716b6c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sc9LFxcr9zSCUhaysNqe9Z",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6566,
      "cache_read_input_tokens": 41583,
      "output_tokens": 8079,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8079,
          "cache_read_input_tokens": 41583,
          "cache_creation_input_tokens": 6566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6566
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "80bc3c7c-5fd1-49a4-8103-52fe5716b6c3",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Semantic constraint compilation for IE decoding",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "80bc3c7c-5fd1-49a4-8103-52fe5716b6c3",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Semantic constraint compilation for IE decoding",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3"
}
```

---
