# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/d91b6641-7766-46ec-8211-66f280f961a2.jsonl`
- **Structured JSON:** [`69d66d80b731091386ae.json`](../../sessions/69/69d66d80b731091386ae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T20:57:35.114Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T20:57:35.114Z",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.\n\nDirection: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.\n\nContribution type: METHOD ONLY. Propose new algorithms — not profiling studies.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Generous for efficiency work.\n2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.\n3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.\n\nLook for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.\n\nTag: direction=efficiency, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 6/10)\n{\n  \"title\": \"Segment-Role-Aware Sparse Attention for Agent Serving\",\n  \"core_problem\": \"Agent workloads interleave semantically heterogeneous context segments — system instructions, tool definitions, conversation history, and tool outputs — with fundamentally different importance dynamics, but all current sparse attention methods treat tokens uniformly by position, recency, or head-level statistics, ignoring the semantic role each segment plays in driving model behavior at different generation phases. While content-type-differentiated KV compression has been explored for multimodal models (VL-Cache for visual vs. text tokens; HybridKV for modality-aware head classification), these approaches exploit architecturally distinct modality boundaries. Agent contexts present a harder problem: all segments are text tokens within a single modality, yet exhibit distinct and phase-dependent attention patterns that require semantic-role-level (not modality-level) differentiation. Meanwhile, prompt-level optimizations like Tool Attention (April 2026) reduce the number of tool tokens entering context via middleware-layer filtering, but tokens that remain in context — system prompts, conversation history, retained tool schemas, and tool outputs — still occupy the full KV cache without role-differentiated compression. Furthermore, chunk-level KV compression (ChunkKV, NeurIPS 2025) and adaptive token-level pruning (Twilight, NeurIPS 2025 Spotlight) have advanced general-purpose compression, but neither exploits the structurally available semantic-role boundaries unique to agent contexts. This challenge is compounded by the rise of hybrid architectures (e.g., Qwen3.6-27B with 48 Gated DeltaNet + 16 standard attention layers), where KV caches exist only in the attention layers but constitute the dominant memory bottleneck — making attention-layer-targeted compression both necessary and sufficient.\",\n  \"opportunity\": \"CacheTTL (Nov 2025) showed agent workloads have distinct KV reuse patterns across turns. CodeComp (April 2026) demonstrated structural priors dramatically improve KV compression for code-specific tasks. 'Don't Break the Cache' (Jan 2026) empirically proved that segment-aware caching strategies (e.g., caching system prompts while excluding dynamic tool results) outperform uniform approaches for agent workloads. 'The Pitfalls of KV Cache Compression' (Oct 2025) identified that system prompts degrade catastrophically under uniform KV eviction, causing instruction-following failures. VL-Cache (ICLR 2025) demonstrated that content-type-differentiated compression (visual vs. text tokens) with layer-adaptive budget allocation achieves 90% KV cache reduction in VLMs — proving the general principle that content-type-aware sparsity vastly outperforms uniform approaches. However, VL-Cache's modality boundary is architecturally defined (vision encoder outputs vs. text embeddings), whereas agent segment roles are semantically defined within a single text modality. CrossKV (OpenReview preprint, Sep 2025) decomposes agent contexts into fine-grained semantic segments for KV cache sharing across agents in multi-agent workflows, demonstrating the value of segment-level decomposition — but targets cross-request cache reuse (breaking prefix barriers), not within-request attention sparsity. CacheSlide (FAST 2026) identifies relative-position-dependent caching patterns in agent workflows for cross-position KV reuse, but again targets caching/reuse rather than compression. SABlock (Oct 2025) introduces semantic-aware KV cache eviction using punctuation-based linguistic segmentation with segment-guided token scoring — but operates on natural language sentence boundaries without agent-role awareness or phase-dependent dynamics. Tool Attention (April 2026) achieves projected 95% tool-token reduction at the prompt/middleware level via two-phase lazy schema loading — but this addresses which tokens enter the context, not how retained tokens' KV caches are compressed. After prompt-level filtering, the remaining context still contains system instructions, conversation history, retained tool schemas (for latency-critical or stateless deployments), and tool outputs that occupy KV cache without role differentiation. ChunkKV (NeurIPS 2025) treats fixed-size token groups (default 10 tokens) as compression units with attention-score-based chunk importance scoring and layer-wise index reuse — achieving strong results on long-context benchmarks. However, ChunkKV's fixed-size chunks are content-agnostic: they split across segment boundaries, compressing system instructions and tool outputs identically, and lack phase-dependent dynamics. Twilight (NeurIPS 2025 Spotlight) introduces adaptive attention sparsity via hierarchical top-p pruning, dynamically adjusting per-head budgets based on attention weight distributions — directly validating that fixed-budget sparsity fails in dynamic scenarios. However, Twilight adapts at the token level without structural priors about segment roles, requiring the model to rediscover role importance purely from attention statistics. 'The Sparse Frontier' (arXiv, Jan 2026) provides the largest-scale empirical analysis of training-free sparse attention, finding that no single strategy generalizes across tasks and phases — reinforcing that task-aware and phase-aware sparsity is needed. Segment-Based Attention Masking (ACL 2025, Katz et al.) relaxes causal masking within structured input segments during prefill to improve model quality via lightweight fine-tuning — sharing the concept of segment-aware attention modification but addressing a fundamentally different problem (prefill quality improvement, not inference-time KV compression) and requiring model fine-tuning rather than being training-free. The gap: no method combines structurally available segment-role boundaries with generation-phase-aware dynamic sparsity for attention-level compression of tokens already in context — specifically, (1) the phase-dependent importance dynamics of tool definitions (critical during tool-call generation, negligible during reasoning), which has no analog in VLM compression, chunk-level compression, or prompt-level filtering, and (2) the availability of zero-cost segment classification from chat-template metadata (vs. VL-Cache's attention-score-based scoring, HybridKV's head-classification overhead, ChunkKV's attention-score aggregation, SABlock's punctuation-based boundary detection, and Twilight's attention-weight-distribution analysis). KEEP (Feb 2026) demonstrates static-dynamic memory partitioning for embodied planning agents but operates at the API-level memory management layer, not within the attention mechanism itself. SentenceKV (COLM 2025) manages KV cache at the sentence-semantic level but lacks agent-role awareness. The emerging prevalence of hybrid architectures (Qwen3.5/3.6 series with Gated DeltaNet) creates an additional opportunity: these architectures concentrate all KV cache memory in a minority of attention layers (~25%), making targeted segment-role compression of those specific layers both more impactful per-layer and more tractable to study. The opportunity is a framework that combines zero-cost chat-template-based segment classification with generation-phase-aware dynamic sparsity profiles for tokens already present in context — complementary to both prompt-level optimizations (Tool Attention, prompt caching) that reduce context size upstream, and token-level adaptive methods (Twilight, ClusterAttn) that can operate within each segment's budget.\",\n  \"landscape\": \"**Content-type-differentiated KV compression (VLM domain)**: VL-Cache (ICLR 2025) differentiates visual and text tokens in VLMs via modality-aware token scoring with layer-adaptive budget allocation, achieving 90% KV reduction. HybridKV (April 2026) classifies attention heads as static/dynamic using text-centric sparsity for multimodal LLMs, achieving 7.9x KV reduction. Both exploit architecturally distinct modality boundaries (vision encoder vs. text embeddings) — inapplicable to single-modality agent contexts where segment roles are semantically, not architecturally, defined.\\n\\n**Chunk-level and semantic-unit KV management**: ChunkKV (NeurIPS 2025) groups tokens into fixed-size chunks (default 10 tokens) as compression units with attention-score-based chunk importance scoring and layer-wise index reuse, achieving up to 8.7% precision improvement over token-level methods at equivalent compression ratios. ChunkKV's fixed-size chunks are content-agnostic — they uniformly partition the context without regard to segment boundaries, compressing system instructions and tool schemas identically. SegAttn's role boundaries are structurally defined by chat-template metadata at zero cost, not by attention-score aggregation, and enable phase-dependent differential treatment. SentenceKV (COLM 2025) groups tokens at sentence level using semantic similarity for KV cache management — operates on linguistic structure without agent-role awareness. SABlock (Oct 2025) introduces semantic-aware KV cache eviction with segment-guided token scoring using punctuation-based linguistic boundaries — achieves strong results on long-context benchmarks but segments by natural language structure (sentences/clauses), not by agent message roles, and lacks phase-dependent dynamics. KEEP (Feb 2026) introduces static-dynamic memory construction with mixed-granularity groups for embodied planning agents, differentiating segments by update frequency — operates at the memory/API level, not within attention computation.\\n\\n**Adaptive sparse attention**: Twilight (NeurIPS 2025 Spotlight) introduces adaptive attention sparsity via hierarchical top-p pruning, dynamically adjusting per-head budgets based on attention weight distributions rather than using fixed token budgets. Twilight demonstrates that adaptive budgeting is critical — fixed-budget methods fail to capture varying attention concentration across heads and inputs. However, Twilight operates purely bottom-up from attention statistics without structural priors about input composition; it must rediscover segment importance from attention weights alone. SegAttn provides complementary top-down structural priors: role-level budgets set the coarse allocation, while token-level adaptive methods (including Twilight-style top-p) can operate within each role's budget for fine-grained selection. 'The Sparse Frontier' (arXiv, Jan 2026) provides the largest-scale empirical analysis of training-free sparse attention across six methods, multiple model families, and sequences up to 128K tokens, finding that 'no clear strategy performs best across tasks and phases' and that static patterns fail to generalize. This reinforces our design: SegAttn's role-level budgets are coarse-grained structural priors (analogous to VL-Cache's modality split), not fine-grained static per-token patterns — and the phase-gating mechanism provides the dynamic component that adapts behavior across generation phases. ClusterAttn (ACL 2025) identifies intrinsic attention clustering patterns and adaptively fits density-based clusters for KV cache compression — achieving strong results but operating on emergent attention patterns without explicit segment-role awareness.\\n\\n**Segment-aware attention modification (different problem)**: Segment-Based Attention Masking (MAS, ACL 2025, Katz et al.) relaxes causal masking within structured input segments during the prefill phase, enabling bidirectional attention within segments to improve model quality. MAS shares the concept of segment-aware attention modification with SegAttn but addresses a fundamentally different problem: prefill-phase quality improvement via fine-tuning, not inference-time KV cache compression. MAS requires lightweight fine-tuning and does not reduce memory; SegAttn is training-free and targets KV cache reduction.\\n\\n**Prompt-level tool optimization**: Tool Attention (April 2026) achieves projected 95% tool-token reduction via two-phase lazy schema loading — compact tool summaries remain resident while full schemas are promoted only for top-k selected tools during tool-call generation. Note: the 95% reduction figure is based on projected/simulated results from measured token counts combined with deployment telemetry, not measured on live LLM agents. Tool Attention operates at the middleware/prompt layer (embedding-based routing + state gating), requires no LLM modification, and is explicitly orthogonal to KV cache compression. It validates the phase-dependent importance insight (tool schemas matter more during tool-call generation) at the prompt level, but does not compress KV caches for tokens already in context. Deployments that retain full schemas (for latency-critical serving, stateless architectures, or multi-turn cache reuse) still face the uncompressed KV cache problem.\\n\\n**Agent-specific KV/cache management**: CacheTTL (Nov 2025) introduces time-to-live KV cache management for agent scheduling — handles when to retain cache, not how to compress attention. CodeComp (April 2026) uses Code Property Graphs for structural KV compression, but is domain-specific to code. 'Don't Break the Cache' (Jan 2026) demonstrates segment-aware caching benefits for agent tasks but focuses on API-level prompt caching, not attention-level sparsity. SideQuest (Feb 2026) lets the model decide KV eviction via self-compression but lacks explicit segment-role priors — the model must rediscover role importance without structural guidance.\\n\\n**Agent-context segment decomposition for cache reuse**: CrossKV (OpenReview preprint, Sep 2025) decomposes agent contexts into fine-grained semantic segments and enables dynamic cross-agent KV cache reuse at arbitrary positions via vLLM's PagedAttention, breaking the rigid prefix-matching barrier. CacheSlide (FAST 2026) identifies Relative-Position-Dependent Caching (RPDC) patterns in agent workflows, enabling cross-position KV reuse with 3.1-4.3x latency reduction. Both focus on inter-request cache sharing/reuse for throughput, not intra-request attention compression for memory — they are complementary to, not competing with, segment-role-aware sparsity.\\n\\n**General sparse attention**: LServe (MLSys 2025) converts half of attention heads to streaming heads regardless of workload type — workload-agnostic. EvoSparse (ACL 2026) tracks token importance dynamics across steps and layers but does not distinguish semantic segment roles. KVzip (NeurIPS 2025 Oral) enables query-agnostic 3-4x KV compression but treats all context tokens identically. Task-KV (Jan 2025) allocates differentiated KV budgets based on attention-head-level semantic heterogeneity — operates at the head level, not at the input-segment level. 'The Pitfalls of KV Cache Compression' (Oct 2025) identifies system prompt degradation under uniform compression and proposes eviction-order fixes, but does not provide a systematic role-differentiated framework. HeteroCache (Jan 2026) exploits head-level heterogeneity via stability-based clustering. MSA (March 2026) introduces document-level routing for 100M-token contexts but uses position-based chunking without agent-specific awareness. SeerAttention (ICLR 2026) learns block-level sparsity via gating but does not differentiate blocks by content type.\\n\\nNo method provides generation-phase-aware, segment-role-differentiated sparse attention for heterogeneous agent contexts within a single text modality — including for emerging hybrid architectures where KV caches are concentrated in a subset of attention layers. Existing adaptive methods (Twilight, ClusterAttn) provide complementary token-level dynamics but lack structural priors; existing structural methods (ChunkKV, SABlock) use content-agnostic or linguistic boundaries without agent-role awareness. SegAttn occupies the unique intersection: zero-cost structural priors from chat-template metadata combined with phase-aware dynamic sparsity, composable with both upstream prompt-level filtering (Tool Attention) and downstream token-level adaptive pruning (Twilight).\",\n  \"approach\": \"We propose SegAttn, a training-free sparse attention framework with two core contributions: (1) an empirical attention profiling study demonstrating that segment-role attention patterns are consistent and exploitable across models and agent workloads, and (2) a practical system that operationalizes these patterns via role-differentiated, phase-aware sparsity budgets — designed to be complementary to both prompt-level optimizations (Tool Attention, prompt caching) that reduce context size upstream and token-level adaptive methods (Twilight, ClusterAttn) that can refine selection within each segment's budget.\\n\\n**Positioning on the static-vs-dynamic spectrum**: 'The Sparse Frontier' (Jan 2026) and Twilight (NeurIPS 2025) demonstrate that purely static, fine-grained sparsity patterns fail to generalize across heads, inputs, and tasks. We distinguish between two levels of sparsity decision: (i) role-level budget allocation — coarse-grained structural priors determining how much compression each segment type receives, analogous to VL-Cache's modality split — and (ii) token-level importance scoring — fine-grained, per-input decisions about which specific tokens to retain within each budget. SegAttn operates at level (i) and is explicitly composable with dynamic token-level methods at level (ii). Role-level budgets are semi-static (calibrated per architecture, with dynamic phase-switching for tool definitions), while token-level selection within each role's budget can use any existing adaptive method (attention-score-based eviction, top-p pruning, etc.). This two-level design avoids the failure mode of static token-level patterns while exploiting structural regularities that purely bottom-up methods must rediscover from attention statistics alone.\\n\\n**Model selection rationale**: We use Llama-3.1-8B (8B, 32 attention layers, 8 KV heads, 128 head_dim) as the primary model — a standard transformer where SegAttn applies uniformly to all layers, yielding clean, generalizable results. Qwen3.6-27B (27B, 16 Gated Attention + 48 Gated DeltaNet layers) serves as a best-effort pilot demonstration of hybrid-architecture applicability. In Qwen3.6-27B, only the 16 Gated Attention layers have traditional KV caches (4 KV heads, 256 head_dim); the 48 DeltaNet layers use fixed-size O(d²) recurrent states (~0.5 MB per layer, ~24 MB total) that are sequence-length-independent and require no compression. SegAttn targets exactly the 16 attention layers, which hold 100% of the model's KV cache memory (~6.55 GB at 100K context in BF16 — 273× the total DeltaNet state). Note: SGLang's hybrid model support (GitHub issue #12867) remains under development with multiple pending features (prefix caching adaptation, speculative decoding, kernel optimization among nine areas) and is currently marked inactive as of May 2026. If SGLang integration proves intractable within the timeline, the Llama-3.1-8B results alone constitute the complete primary contribution; the hybrid-architecture pilot is scoped as best-effort and may be deferred to camera-ready or follow-up work.\\n\\n**Key differentiators from VL-Cache, content-type compression, chunk-level compression, adaptive pruning, segment-level cache sharing, and prompt-level filtering**: SegAttn addresses properties unique to agent contexts: (a) **Dynamic phase-gating** — tool definition tokens shift between critical (during tool-call generation) and negligible (during reasoning) within a single inference pass; VL-Cache's visual/text split is static throughout generation; ChunkKV's fixed chunks are phase-unaware; Twilight adapts per-head budgets but without structural role priors; Tool Attention exploits this same insight but at the prompt layer (excluding schemas entirely), while SegAttn compresses schemas that are retained in context. (b) **Zero-cost segment classification** — chat-template metadata (ChatML role tags, Llama-style [INST] markers) provides exact segment boundaries without any scoring computation; VL-Cache requires attention-score-based modality-aware scoring, HybridKV requires text-centric sparsity head classification, ChunkKV requires attention-score aggregation per chunk, SABlock requires punctuation-based boundary detection, Twilight requires attention-weight-distribution analysis for top-p thresholding. (c) **Intra-request compression of retained context** — CrossKV and CacheSlide decompose segments for inter-request cache reuse; Tool Attention filters tokens before they enter context; SegAttn compresses segments within the attention computation of a single request for tokens already present. (d) **Composability with adaptive token-level methods** — SegAttn's role-level budgets define how much to compress each segment type; within each segment's budget, any token-level selection method (attention-score eviction, Twilight-style top-p, etc.) can be applied. This makes SegAttn a structural prior layer that enhances, rather than replaces, existing adaptive compression.\\n\\n**Segment Classification**: Tokens are tagged by semantic role (system instruction, tool schema, conversation turn, tool output) using chat-template metadata and structured message boundaries. This requires no model modification and no scoring overhead — just parsing the tokenized input against known template patterns.\\n\\n**Role-Differentiated Sparsity**: System instructions receive block-level KV sparsity (retain only high-attention blocks identified during a short calibration pass), exploiting their persistent but diffuse pattern identified by 'Pitfalls of KV Cache Compression'. Tool definitions are phase-gated: preserved at full fidelity when tool-call generation is detected (reactive detection via chat-template special tokens like `&lt;tool_call>` or `<|plugin|>` — once the first tool-call token appears, the sparsity profile switches for subsequent tokens in the sequence; the 1-2 token detection delay is negligible given tool-call sequences span 50-200 tokens), and aggressively compressed during reasoning phases. Recent tool outputs are protected from eviction within a recency window. For hybrid architectures like Qwen3.6-27B, phase-gating modifies only the 16 attention layers' masks — but since these layers contain 100% of the compressible KV cache, phase-gating controls the entirety of the memory reduction opportunity.\\n\\n**Implementation via FlashInfer with FlexAttention Fallback**: We leverage FlashInfer's existing block-sparse attention API and paged KV-cache management, already integrated into SGLang. Segment-role masks are generated as block-sparse attention masks fed to FlashInfer's sparse attention kernels for the attention layers only. Phase-gating is implemented as dynamic mask switching triggered by special token detection in the decode loop. **Addressing plan() reconfiguration overhead** (GitHub issue #2938): FlashInfer's `plan()` function triggers device-to-host memcpy for scheduling, which can create synchronization overhead during mask reconfiguration. For SegAttn, this is mitigated by three factors: (i) phase transitions are infrequent (1-2 per generation spanning 50-200+ tokens), so plan() is called at most 1-2 additional times per generation, amortized over dozens to hundreds of decode steps; (ii) we pass host tensors (indptr, indices) directly to plan() to avoid GPU-to-CPU transfers, following FlashInfer v0.2 best practices; (iii) non-blocking host-to-device transfers during plan() further reduce pipeline stalls. We will benchmark plan() reconfiguration latency during ablation studies to quantify amortized overhead. **FlexAttention fallback**: If FlashInfer's plan() overhead proves prohibitive for specific deployment scenarios, PyTorch's FlexAttention provides an alternative via `create_block_mask()` + `score_mod()` that supports dynamic mask changes without kernel recompilation — the compiled kernel remains valid when only the BlockMask metadata changes. FlexAttention's block_mask approach is well-suited for phase-gating since the sparsity pattern change is a one-time switch per phase transition.\\n\\n**Profiling Protocol (Contribution 1)**: We profile attention patterns on: (a) 100 BFCL v3 multi-turn function-calling traces, and (b) 50 multi-turn ReAct-style traces (from HotpotQA with tool-augmented retrieval). For Llama-3.1-8B, we profile all 32 attention layers. For Qwen3.6-27B (if SGLang integration permits), we profile the 16 Gated Attention layers specifically. We explicitly investigate whether having fewer, more widely-spaced attention layers (every 4th layer) concentrates segment-role patterns compared to dense attention architectures. For each trace, we extract per-layer, per-head attention mass ratios allocated to each segment role during different generation phases (tool-call generation vs. free-form reasoning vs. summarization). Key metrics: (i) segment-role attention mass concentration, (ii) cross-segment attention entropy, (iii) phase-conditional attention shift. **Cross-architecture analysis**: Rather than requiring a single universal profile, we evaluate whether per-architecture profiles are necessary — consistency within each architecture is the primary criterion, with cross-architecture transferability as a bonus. **Falsification criterion**: if the coefficient of variation of segment-role attention mass ratios across workloads exceeds 0.5 for any segment type within either architecture (not across architectures), the 'consistent patterns' hypothesis is rejected for that architecture and the system would fall back to per-workload calibration.\\n\\n**Evaluation with Layered Optimization Conditions**: Llama-3.1-8B (primary, 16GB BF16, all 32 layers are attention) and Qwen3.6-27B (best-effort pilot, 55.6GB BF16, 16 attention layers) on: (a) **agent benchmark** — BFCL v3 for tool-calling accuracy; (b) **general capability** — WikiText-2 perplexity and MMLU to demonstrate no regression; (c) **instruction-following quality** — MT-Bench to verify system-prompt compression does not degrade instruction adherence, directly addressing the system-prompt sensitivity identified by 'Pitfalls of KV Cache Compression'; (d) **long-context capability** — LongBench (multi-task long-context evaluation) to demonstrate no regression on retrieval and comprehension tasks critical for agent workloads with extended conversation histories. **Critically, we evaluate SegAttn under three conditions**: (C1) SegAttn alone — full tool schemas in context, measuring standalone compression value; (C2) Prompt caching ('Don't Break the Cache') + SegAttn — segment-aware API-level caching active, measuring marginal benefit of attention-level compression on top of caching optimization; (C3) Tool-schema filtering (simulating Tool Attention's projected 95% reduction) + SegAttn — only top-k relevant tool schemas retained in context, measuring marginal benefit of attention-level compression when prompt-level filtering is already applied. **Transparency note on C3**: The C3 condition simulates the effect of prompt-level tool filtering by manually retaining only top-k tool schemas rather than composing with Tool Attention's actual implementation (whose 95% reduction is itself based on projected results, not live agent measurements). C3 thus tests a hypothetical but conservative composition — if SegAttn provides meaningful compression even after ideal prompt-level optimization, the value under real-world (likely less ideal) filtering is strictly greater. This layered evaluation directly addresses whether attention-level segment-role compression provides value beyond prompt-level optimizations. **Expected value argument**: Even under C3, retained context still contains system instructions (~500-2000 tokens), full conversation history (growing with turns), the retained top-k tool schemas, and tool outputs — all of which benefit from role-differentiated compression. SegAttn's value increases with conversation length (as history and outputs accumulate), precisely the regime where prompt-level filtering alone is insufficient. Target: meaningful KV cache reduction with <2% task degradation on BFCL v3, <0.1 perplexity increase on WikiText-2, and <5% score degradation on MT-Bench and LongBench. For Qwen3.6-27B pilot (if feasible), we additionally report the effective whole-model memory reduction.\\n\\n**Differentiation summary**: VL-Cache differentiates modalities via scoring (architecture-level); SegAttn differentiates semantic roles via chat templates (zero-cost, within single modality). HybridKV classifies heads by sparsity type; SegAttn classifies input segments by semantic role. ChunkKV groups fixed-size token chunks with attention-score aggregation; SegAttn groups variable-size agent segments with zero-cost chat-template boundaries and phase-awareness. Twilight adapts token-level budgets via top-p pruning (bottom-up); SegAttn sets role-level budgets via structural priors (top-down) — composable as two complementary layers. Segment-Based Attention Masking (ACL 2025) relaxes causal masks within segments during prefill for quality improvement (requires fine-tuning); SegAttn compresses KV caches by segment role during inference (training-free). CrossKV decomposes segments for cross-agent cache sharing (inter-request reuse); SegAttn decomposes segments for intra-request attention compression. CacheSlide exploits cross-position reuse patterns for serving throughput; SegAttn compresses within the attention mechanism. KEEP manages static/dynamic memory at the API level; SegAttn operates within attention computation. Tool Attention filters which tool schemas enter the context (prompt-level); SegAttn compresses KV caches for tokens already in context (attention-level) — they are complementary and composable. SABlock segments by linguistic punctuation boundaries; SegAttn segments by agent message roles from chat-template metadata with phase-awareness. Task-KV differentiates which attention heads matter (head-level); SegAttn differentiates which input segments to compress (token-segment-level). 'Pitfalls' proposes eviction-order fixes; SegAttn provides a systematic role-differentiated framework. CodeComp uses code-specific structural priors; SegAttn is domain-general. SideQuest requires the model to rediscover role importance; SegAttn provides explicit priors from chat-template metadata. SentenceKV operates at linguistic sentence granularity; SegAttn operates at agent message-role granularity with phase-awareness. ClusterAttn identifies emergent attention clusters; SegAttn exploits known structural role boundaries.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~165h H100 (attention profiling on both architectures: 35h, FlashInfer integration + mask generation: 20h, phase-gating implementation with plan() benchmarking: 18h, hybrid-architecture pilot: 10h, ablation studies including layered evaluation conditions: 32h, benchmark evaluation incl. MT-Bench and LongBench: 38h, buffer: 12h)\",\n      \"gpu_utilization\": \"~20-30% effective; GPUs idle during FlashInfer integration debugging and attention heatmap analysis\",\n      \"timeline\": \"3-4 weeks (does NOT fit May 25 deadline)\",\n      \"team\": \"1-2 researchers (1 ML/attention, 1 systems/serving)\",\n      \"estimated_gpu_cost\": \"$660 (165h × $4.00/hr H100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~185h H100 (attention profiling across both architectures: 40h, integration: 25h, phase-gating + plan() overhead benchmarking: 18h, hybrid-arch pilot: 10h, ablation including 3 evaluation conditions (C1-C3): 42h, benchmarks incl. MT-Bench + LongBench: 38h, buffer: 12h)\",\n      \"gpu_utilization\": \"~55-70%; agent queues experiments while human reviews segment-budget ratios and validates attention profiling results\",\n      \"timeline\": \"12-16 days (tight but possible for May 25 deadline)\",\n      \"team\": \"1 researcher, ~25-35 min/day reviewing agent proposals for mask generation logic and profiling analysis\",\n      \"claude_api_cost\": \"$200-400 (~2000-4000 turns for code generation, experiment design, profiling analysis)\",\n      \"estimated_gpu_cost\": \"$740 (185h × $4.00/hr H100)\",\n      \"risk_note\": \"FlashInfer plan() overhead (issue #2938) may require switching to FlexAttention fallback; SGLang hybrid support (issue #12867, currently inactive) may limit Qwen3.6-27B pilot to basic inference or require deferral to camera-ready\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~205h H100 (profiling across both architectures × multiple workloads: 50h, 2x more budget configurations explored: 40h, hybrid-arch pilot ablations: 15h, layered evaluation grid (C1-C3 × 2 models) + MT-Bench + LongBench: 52h, cross-architecture comparison: 20h, plan() overhead benchmarking: 5h, buffer: 23h)\",\n      \"gpu_utilization\": \"~80-90%; continuous experiment pipeline with agent iterating across segment-budget ratios, phase-detection thresholds, and recency windows\",\n      \"timeline\": \"8-12 days with 2 H100 GPUs available concurrently (the ONLY path that reliably fits the May 25 EMNLP deadline)\",\n      \"team\": \"0 (initial setup only, ~2 hours to configure SGLang + FlashInfer environment and benchmark datasets)\",\n      \"claude_api_cost\": \"$400-700 (~4000-7000 turns for iterative development, experiment execution, profiling analysis)\",\n      \"estimated_gpu_cost\": \"$820 (205h × $4.00/hr H100)\",\n      \"speed_bottleneck\": \"GPU count: 2 H100 80GB needed (one for Qwen3.6-27B serving, one for Llama-3.1-8B + experiment orchestration); FlashInfer API exploration may require multiple iteration cycles; if plan() overhead is prohibitive, FlexAttention integration adds ~1 day\",\n      \"risk_note\": \"Agent may over-explore the segment-budget configuration space without human pruning; SGLang's hybrid support (issue #12867, inactive) may limit Qwen3.6-27B pilot scope or require deferral; profiling study must complete in days 1-3 to leave time for system building\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline: May 25, 2026 — requires auto_research path)\",\n    \"AAAI 2027 (submission deadline: August 1, 2026 — comfortable with any path)\",\n    \"ICLR 2027 (estimated deadline: September-October 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration (ICLR 2025)\",\n    \"HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference (arXiv 2604.05887, April 2026)\",\n    \"SentenceKV: Efficient LLM Inference via Sentence-Level Semantic KV Caching (COLM 2025)\",\n    \"KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning (arXiv 2602.23592, Feb 2026)\",\n    \"Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live (arXiv 2025)\",\n    \"CodeComp: Structural KV Cache Compression for Agentic Coding (arXiv 2026)\",\n    \"LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention (MLSys 2025)\",\n    \"Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention (ACL 2026)\",\n    \"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction (NeurIPS 2025 Oral)\",\n    \"Task-KV: Task-aware KV Cache Optimization via Semantic Differentiation of Attention Heads (arXiv 2501.15113, Jan 2025)\",\n    \"The Pitfalls of KV Cache Compression (arXiv 2510.00231, Oct 2025)\",\n    \"HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference (arXiv 2026)\",\n    \"SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning (arXiv 2026)\",\n    \"MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens (arXiv 2026)\",\n    \"SeerAttention: Learning Intrinsic Sparse Attention in Your LLMs (ICLR 2026)\",\n    \"Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks (arXiv 2026)\",\n    \"Block Sparse Flash Attention (arXiv 2512.07011, Dec 2025)\",\n    \"FlashInfer: Efficient and Customizable Attention Engine for LLM Inference (arXiv 2501.01005, Jan 2025)\",\n    \"Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing (OpenReview preprint, Sep 2025)\",\n    \"CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving (FAST 2026)\",\n    \"Gated DeltaNet: Adaptive Fast-Weight Model (NeurIPS 2024)\",\n    \"Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows (arXiv 2604.21816, April 2026)\",\n    \"SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size (arXiv 2510.22556, Oct 2025)\",\n    \"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference (NeurIPS 2025)\",\n    \"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning (NeurIPS 2025 Spotlight)\",\n    \"Segment-Based Attention Masking for GPTs (ACL 2025, arXiv 2412.18487)\",\n    \"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs (arXiv 2504.17768, Jan 2026)\",\n    \"ClusterAttn: KV Cache Compression under Intrinsic Attention Clustering (ACL 2025)\"\n  ],\n  \"description\": \"Agent workloads interleave semantically heterogeneous context segments — system instructions, tool schemas, conversation history, and tool outputs — with fundamentally different attention dynamics, yet all current sparse attention methods treat tokens uniformly. While content-type-differentiated KV compression has been explored for VLMs (VL-Cache, HybridKV), chunk-level compression with fixed-size token groups (ChunkKV), adaptive token-level pruning (Twilight), segment-level decomposition for agent cache sharing (CrossKV, CacheSlide), semantic-unit eviction for linguistic boundaries (SABlock), segment-aware attention masking for prefill quality (MAS, ACL 2025), and prompt-level tool filtering at the middleware layer (Tool Attention), no method combines structurally available segment-role boundaries with generation-phase-aware dynamic sparsity for within-request attention compression of tokens already in context. We propose SegAttn, a training-free framework with two contributions: (1) a hypothesis-driven empirical profiling study measuring segment-role attention patterns across architectures — standard transformers (Llama-3.1-8B, all 32 layers profiled) and hybrid linear-attention architectures (Qwen3.6-27B, 16 Gated Attention layers profiled as a best-effort pilot) — across agent workloads (100 BFCL v3 traces, 50 ReAct traces) and generation phases, with per-architecture falsification criteria (CV > 0.5 rejects consistency); and (2) a practical system exploiting three properties unique to agent contexts: zero-cost segment classification from chat-template metadata (vs. ChunkKV's attention-score aggregation and Twilight's attention-weight analysis), dynamic phase-gating of tool definitions (critical during tool-call generation, compressed during reasoning — validating at the attention level the same insight Tool Attention exploits at the prompt level), and recency-windowed protection of tool outputs. We explicitly position SegAttn on the static-vs-dynamic spectrum: role-level budgets are coarse-grained structural priors (analogous to VL-Cache's modality split), not fine-grained static per-token patterns that 'The Sparse Frontier' identifies as a failure mode. The phase-gating mechanism provides the dynamic component, and SegAttn is composable with token-level adaptive methods (Twilight-style top-p pruning) within each segment's budget. We evaluate under layered optimization conditions: SegAttn alone (C1), with prompt caching (C2), and with simulated prompt-level tool filtering (C3, acknowledging Tool Attention's projected rather than measured results), demonstrating marginal value beyond upstream optimizations. Evaluation spans BFCL v3 (tool-calling), WikiText-2 perplexity, MMLU (general capability), MT-Bench (instruction-following quality under compression), and LongBench (long-context retrieval and comprehension). Implemented using FlashInfer's block-sparse attention API within SGLang (with FlexAttention as fallback for dynamic mask reconfiguration, addressing FlashInfer plan() overhead per GitHub issue #2938). Unlike VL-Cache (static modality split), ChunkKV (fixed-size content-agnostic chunks), Twilight (bottom-up adaptive pruning without structural priors), MAS (prefill quality via fine-tuning), CrossKV (inter-request segment sharing), CacheSlide (cross-position reuse), KEEP (API-level memory), SABlock (linguistic-unit segmentation), SentenceKV (linguistic-unit granularity), Tool Attention (prompt-level filtering with projected results), or SideQuest (model self-compression), SegAttn is the first method combining zero-cost chat-template classification with generation-phase-aware sparsity for attention-level compression of retained agent context — providing top-down structural priors composable with bottom-up adaptive token-level methods — applicable to both standard and hybrid architectures. Estimated ≤205 H100-hours. Primary target: EMNLP 2026 (auto_research path required for May 25 deadline).\",\n  \"project_name\": \"seg_role_sparse_attn\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: Resource estimate (400-800h A100) exceeds user's hard constraint of ≤200 H100-hours by 2-4x. The idea must be scoped down or the approach simplified to fit within budget.\", \"CRITICAL: Llama-4-Scout-17B-16E requires ~220GB VRAM in BF16 (109B total parameters across 16 experts), not ~70GB as claimed. This means multi-GPU tensor-parallel serving is mandatory, significantly increasing complexity and effective GPU-hour consumption.\", \"Phase-gating mechanism via 'output-vocabulary monitoring' is underspecified and technically problematic. Detection of tool-call generation is retroactive — you only know the model is generating a tool call after it outputs the first tool-call tokens (e.g., '&lt;tool_call>' special token). How do you proactively switch attention profiles before the attention computation for those tokens?\", \"Missing highly relevant citations: (1) Task-KV (arXiv 2501.15113, Jan 2025) — task-aware KV cache optimization via semantic differentiation of attention heads; (2) 'The Pitfalls of KV Cache Compression' (arXiv 2510.00231, Oct 2025) — identifies system prompt degradation under compression and proposes eviction policy fixes. Both directly address subproblems that SegAttn claims to solve.\", \"Evaluation benchmark mismatch: User requires perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench, but the idea only proposes BFCL v4, SWE-Bench, AgentBench. While agent-specific benchmarks are appropriate for this idea, the user's required benchmarks should also be included to demonstrate no regression on general capabilities.\", \"The 3-5x KV cache reduction target lacks supporting evidence. The claim that heuristic segment-role tagging can match or exceed KVzip's 3-4x compression (which uses sophisticated reconstruction-based importance scoring) requires justification.\", \"16-day timeline is extremely tight for: custom Triton kernel development for phase-gated block-sparse attention, SGLang attention backend integration, attention profiling across 2 models, ablation studies on role-specific budgets, and evaluation on 3 agent benchmarks. This risks producing an incomplete or poorly-evaluated paper.\", \"Generalizability concern: The approach relies on chat-template metadata and structured message boundaries for segment classification. Different models use different chat templates (ChatML, Llama-style, etc.), and the role-budget allocations may need per-model tuning, undermining the 'general-purpose' claim.\"]\nFeedback: To reach pass quality, address these priority items:\n\n1. **Fix compute budget**: Drop Llama-4-Scout entirely (too large for the budget) and focus on Qwen3.6-27B plus one smaller model (e.g., Llama-3.1-8B or Qwen3-14B). Reduce to 2 agent benchmarks (BFCL v4 + SWE-Bench). Target ≤180 H100-hours with a concrete hour breakdown: profiling (X h), kernel development (Y h), ablation (Z h), final eval (W h).\n\n2. **Fix phase-gating mechanism**: Replace 'output-vocabulary monitoring' with a concrete, implementable detection strategy. The simplest: use the chat template's special tokens (e.g., `&lt;tool_call>`, `<|plugin|>`) as reactive triggers — once detected, switch sparsity profiles for subsequent tokens in the tool-call sequence. Acknowledge this is reactive (1-2 token delay) and quantify the impact. Alternatively, use a lightweight classifier on the last-layer hidden state to predict phase 1-2 tokens ahead.\n\n3. **Add missing citations and differentiate**: Cite Task-KV and 'Pitfalls of KV Cache Compression.' Explicitly explain how SegAttn differs: Task-KV differentiates at the attention-head level (which heads matter for the task), while SegAttn differentiates at the token-segment level (which input segments to compress). 'Pitfalls' identifies the problem but only proposes simple eviction-order fixes, while SegAttn provides a systematic role-differentiated framework.\n\n4. **Include user-required benchmarks**: Add perplexity (WikiText/C4) and at least MMLU or MT-Bench alongside agent benchmarks to demonstrate no general-capability regression.\n\n5. **Scope down for 16-day timeline**: Consider using existing sparse attention kernels (e.g., from LServe or FlashAttention block-sparse mode) rather than writing custom Triton kernels from scratch. This trades peak performance for development speed.\n\n6. **Strengthen novelty**: The current contribution is 'combine three known techniques under a taxonomy.' To strengthen: (a) provide empirical attention profiling data showing that segment-role patterns are consistent and exploitable across models (this is the key assumption that needs validation), or (b) propose a learned segment-budget allocator rather than hand-tuned heuristics.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"IMPORTANT: Missing citation VL-Cache (ICLR 2025) — applies content-type-differentiated KV compression for VLMs (visual vs. text tokens with different budgets and phase-aware strategies). This is conceptually the closest prior work to SegAttn's segment-role differentiation, just in the multimodal domain instead of agent contexts. The generator MUST cite this and explicitly differentiate — otherwise reviewers familiar with VLM efficiency will view SegAttn as a straightforward domain transfer.\", \"Missing citations: SentenceKV (COLM 2025) — semantic-unit-level KV cache management; HybridKV (arXiv 2604.05887, April 2026) — content-type-aware hybrid KV compression for multimodal LLMs with head classification by text-centric sparsity. Both demonstrate that 'differential compression by content type' is an established pattern, not a novel contribution.\", \"Timeline contradiction: The manual estimate says 4-6 weeks but the deadline is 15 days. Even the auto_research estimate of 8-12 days with 2 H100s is cutting it very close to May 25. The attention profiling study across 2 models × multiple agent workloads is itself a multi-day effort before any system building begins.\", \"The 2-3x KV compression target still lacks supporting evidence from any preliminary experiment or prior empirical observation. The Pitfalls paper shows system prompts degrade under uniform compression, but that tells us which segments to PROTECT, not how much we can compress others. Without pilot data showing how much agent-context tool definitions and conversation history can actually be compressed without task degradation, the target is speculative.\", \"Evaluation scope vs. timeline mismatch: BFCL v4 + SWE-Bench (agent benchmarks) + WikiText-2 perplexity + MMLU + MT-Bench across 2 models is 10+ separate evaluation runs. SWE-Bench alone (with its agentic scaffolding) takes significant compute and setup time. This is likely the first thing to be cut under time pressure, weakening the paper.\", \"KEEP (arXiv 2602.23592, Feb 2026) is missing from the landscape — it introduces static-dynamic memory construction with mixed-granularity groups for agent KV cache, which shares the insight that different memory segments have different reuse patterns and deserve different treatment.\", \"The profiling study (contribution 1) and the system (contribution 2) compete for limited time. If profiling reveals unexpected patterns (e.g., segment-role patterns are NOT consistent across models or workloads), the entire system design needs to change. This is a research risk that the tight timeline cannot absorb.\"]\nFeedback: The revision successfully addressed Round 1's critical issues (compute budget, model selection, phase-gating mechanism, missing Task-KV/Pitfalls citations). The proposal is now within budget and technically concrete. To reach pass quality:\n\n1. **Cite VL-Cache (ICLR 2025) and differentiate explicitly**: VL-Cache differentiates visual vs. text tokens in VLMs with modality-aware budgets and phase-aware strategies. SegAttn differentiates semantic roles in text-only agent contexts. The key differentiator is that VL-Cache's modalities are architecturally distinct (vision encoder tokens vs. text tokens), while SegAttn's segment roles are semantically defined within a single modality via chat-template metadata. Also cite SentenceKV, HybridKV, and KEEP.\n\n2. **Strengthen novelty beyond 'domain transfer'**: Currently SegAttn risks being viewed as 'VL-Cache for agents.' To differentiate: (a) emphasize the phase-gating mechanism (tool definitions shift between critical and negligible depending on generation phase — this dynamic role-switching has no analog in VL-Cache's static visual/text split); (b) the fact that agent segment boundaries are known a priori from chat templates (zero-cost classification vs. VL-Cache's learned scoring); (c) present the profiling study as revealing agent-specific attention patterns that fundamentally differ from VLM patterns.\n\n3. **Reduce evaluation scope to fit timeline**: Drop SWE-Bench (too heavy for 15 days) and keep BFCL v4 as the agent benchmark. For general capability, WikiText-2 perplexity + MMLU should suffice. This makes the evaluation completable in 2-3 days rather than 5+.\n\n4. **Add pilot profiling data or at minimum a concrete protocol**: Describe exactly which agent workloads you'll profile (e.g., 100 BFCL traces, 50 multi-turn ReAct traces), what metrics you'll extract (per-segment attention mass ratios, cross-segment attention entropy), and what threshold would falsify your hypothesis. This transforms the profiling study from speculative to hypothesis-driven.\n\n5. **Reconcile timeline estimates**: Set manual at 3-4 weeks, HIL at 12-16 days, auto at 8-12 days. The auto path is the only one that fits the May 25 deadline — be explicit about this.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL: Qwen3.6-27B uses a hybrid architecture with 16×(3×(Gated DeltaNet→FFN)→1×(Gated Attention→FFN)) = 48 DeltaNet layers + 16 standard attention layers. Only the 16 attention layers have traditional KV caches and attention patterns. The proposal assumes a standard transformer throughout — profiling study, FlashInfer block-sparse masks, and phase-gating all only apply to 25% of the model's layers. While 100% of the KV cache memory resides in these 16 layers (DeltaNet uses O(d²) fixed-size states), this architectural reality must be explicitly acknowledged and its implications discussed.\", \"Missing citation: 'Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing' (ICLR 2026, OpenReview). This paper decomposes agent context into 'fine-grained semantic segments' for KV cache management on vLLM. While it focuses on multi-agent segment SHARING (not single-agent compression), the shared concept of agent-context segment decomposition must be cited and differentiated.\", \"The profiling study's generalizability is weakened for hybrid architectures: measuring 'segment-role attention patterns' across only 16 attention layers in Qwen3.6-27B provides a very different signal than profiling all 32 layers in Llama-3.1-8B. The falsification criteria (CV > 0.5) should account for this architectural asymmetry — consistency across models with fundamentally different attention coverage is a higher bar.\", \"The compression ratio target remains speculative. For Qwen3.6-27B, the 16 attention layers use only 4 KV heads with 256 dim, yielding ~6.4 GB KV cache at 100K tokens. With DeltaNet handling 75% of computation efficiently, the marginal benefit of KV compression in the attention layers may be less impactful than implied. A concrete analysis of where the actual serving bottleneck lies for this specific architecture would strengthen the proposal.\", \"Phase-gating implementation on Qwen3.6 needs clarification: in a hybrid architecture where DeltaNet layers process all tokens via recurrence (no masking possible), does phase-gating only modify the 16 attention layers' masks? If so, the efficiency gain from phase-gating is limited to those layers' compute, which is ~25% of total attention compute.\"]\nFeedback: The proposal has improved significantly across rounds 1-2, with excellent differentiation from prior work and concrete implementation details. To reach pass quality:\n\n1. **Address Qwen3.6-27B hybrid architecture explicitly**: Acknowledge that SegAttn targets the 16 standard attention layers (which hold 100% of the KV cache). Frame this positively: since DeltaNet layers already handle long contexts efficiently via O(d²) states, the attention layers are precisely where compression matters most. The profiling study should focus on these 16 layers and discuss whether having fewer attention layers actually CONCENTRATES segment-role patterns (making them easier to exploit).\n\n2. **Cite 'Collaborative Memory' (ICLR 2026)**: Differentiate clearly — that work decomposes segments for multi-agent SHARING across requests (breaking prefix barriers); SegAttn decomposes segments for single-agent COMPRESSION within attention computation. They're complementary, not competing.\n\n3. **Adjust profiling study scope**: State that for hybrid architectures, the profiling study targets attention layers specifically (the only layers with exploitable attention patterns). For Llama-3.1-8B (all 32 layers are attention), the full model is profiled. Discuss whether cross-architecture generalization is a goal or whether per-architecture profiles are acceptable.\n\n4. **Quantify the actual bottleneck**: For Qwen3.6-27B at 100K tokens, the 16 attention layers' KV cache is ~6.4 GB. Is this the actual serving bottleneck, or does the DeltaNet state computation dominate? A concrete calculation showing that attention-layer KV cache is the memory bottleneck (not DeltaNet computation) would justify the approach.\n\n5. **Consider making Llama-3.1-8B the primary model**: Since it's a standard transformer where SegAttn applies uniformly to all layers, results will be cleaner and more generalizable. Use Qwen3.6-27B as the secondary model to demonstrate applicability to hybrid architectures.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"IMPORTANT: Missing citation 'Tool Attention Is All You Need' (arXiv:2604.21816, April 2026). This middleware-layer mechanism uses two-phase lazy schema loading — keeping compact tool summaries during reasoning and promoting full schemas only for top-k selected tools during tool-call generation. While it operates at the prompt/API level (not attention level), it validates the same phase-dependent tool schema importance insight that SegAttn's phase-gating exploits. The 95% tool-token reduction it achieves at the prompt level raises a crucial question: if tool schemas can simply be excluded from the context during reasoning, how much additional benefit does attention-level phase-gating provide on top of prompt-level filtering? SegAttn must demonstrate complementary value — compressing tool tokens that remain in context after prompt-level optimization, or handling cases where full schemas must be retained for other reasons.\", \"IMPORTANT: FlashInfer plan() overhead threatens phase-gating implementation. GitHub issue #2938 (April 2026) documents that dynamic_block_sparse_fwd_flashinfer triggers per-block device-to-host memcpy during the planning phase, making mask reconfiguration expensive. Phase-gating requires calling plan() with a new mask when a phase transition is detected. While transitions are infrequent (1-2 per generation), the overhead may be non-trivial for latency-sensitive serving. The proposal should: (a) acknowledge this limitation explicitly, (b) benchmark plan() reconfiguration latency, and (c) discuss FlexAttention (PyTorch) as a fallback if FlashInfer's overhead is prohibitive.\", \"SGLang hybrid model support for Gated DeltaNet architectures remains under active development (GitHub issue #12867). Key features including prefix caching adaptation, speculative decoding, and GDN kernel optimization are listed as pending on the roadmap. The Qwen3.6-27B experiments may encounter missing features or bugs. The proposal should explicitly acknowledge this risk and have a fallback: either use vLLM's hybrid support (which has its own limitations per issue #41560) or scope Qwen3.6-27B as a 'preliminary/pilot' evaluation rather than a full secondary model.\", \"Missing citation: SABlock (arXiv:2510.22556, Oct 2025) — semantic-aware KV cache eviction with segment-guided token scoring. While it operates on linguistic semantic boundaries (not agent-role boundaries) and lacks phase-gating, it is the closest prior work on semantic segmentation for KV cache management within a single text modality. Should be cited and differentiated: SABlock segments by linguistic coherence; SegAttn segments by agent message roles from chat-template metadata.\", \"The relationship between prompt-level tool-schema optimization and attention-level compression is unexamined. In realistic agent deployments, prompt caching ('Don't Break the Cache') and tool-schema filtering ('Tool Attention') are already applied at the prompt level. SegAttn's evaluation should include a condition where these prompt-level optimizations are already active, measuring the marginal benefit of attention-level segment-role compression on top of an already-optimized context. Without this, the claimed compression opportunity may be overstated.\", \"CrossKV venue claim needs verification: the proposal states 'ICLR 2026' but the paper was posted on OpenReview in October 2025 without confirmed ICLR 2026 acceptance in my searches. If the venue cannot be verified, cite as 'OpenReview 2025' or 'arXiv preprint' to avoid inaccuracy.\"]\nFeedback: The proposal has improved substantially over 4 rounds and is approaching pass quality. The remaining issues are important but addressable:\n\n1. **Cite and position against 'Tool Attention Is All You Need' (arXiv:2604.21816)**: This is the most important addition. Differentiate clearly: Tool Attention operates at the middleware/prompt layer (filtering which schemas enter context); SegAttn operates at the attention computation layer (compressing KV cache for schemas already in context). Frame them as complementary — Tool Attention reduces the number of tool tokens entering context, while SegAttn compresses the remaining tokens' KV cache based on their segment role. Critically, add an evaluation condition where prompt-level tool filtering is already applied, measuring SegAttn's marginal benefit on top of it.\n\n2. **Address FlashInfer plan() overhead**: Add a paragraph acknowledging GitHub issue #2938 and discussing mitigation. Key argument: phase transitions are infrequent (1-2 per generation of 50-200+ tokens), so the amortized overhead per decode step is small. Include a plan to benchmark plan() reconfiguration latency during ablation studies. Mention FlexAttention as a fallback option.\n\n3. **Temper Qwen3.6-27B claims**: Acknowledge SGLang's hybrid support is under development. Frame Qwen3.6-27B experiments as 'preliminary demonstration of hybrid-architecture applicability' rather than a full-fledged secondary evaluation. If SGLang integration proves intractable within the timeline, the Llama-3.1-8B results alone are sufficient for a solid contribution.\n\n4. **Add SABlock citation and verify CrossKV venue claim**.\n\n5. **Strengthen the impact argument**: The 'Tool Attention' paper shows 95% tool-token reduction at the prompt level. SegAttn must argue why attention-level compression is still valuable: (a) not all deployments use middleware-level filtering; (b) even after filtering, retained context segments (system prompts, conversation history, recent tool outputs) still benefit from role-differentiated compression; (c) SegAttn's phase-gating applies to tokens that are already in context and cannot be filtered out.\n\nWith these changes, the novelty and impact arguments become significantly stronger, and the feasibility risks are properly acknowledged. The proposal would likely pass.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"IMPORTANT: Missing citations: (1) ChunkKV (NeurIPS 2025) — semantic-chunk-based KV compression using fixed-size token groups as compression units. While SegAttn uses agent-role boundaries (not fixed chunks), ChunkKV demonstrates that chunk-level compression is an active and competitive approach. (2) Twilight (NeurIPS 2025) — adaptive attention sparsity with hierarchical top-p pruning that dynamically adjusts sparsity per-context. This directly validates the need for adaptive (not static) sparsity — and challenges SegAttn's semi-static profile approach. (3) 'Segment-Based Attention Masking for GPTs' (ACL 2025, arXiv:2412.18487) — relaxes causal masking within structured input segments during prefill. While it addresses bidirectional attention rather than KV compression, the shared concept of segment-aware attention modification must be cited.\", \"IMPORTANT: Anti-evidence on static sparsity not addressed. Recent literature ('The Sparse Frontier', ClusterAttn ACL 2025, training-free native sparse attention studies) explicitly identifies static sparsity patterns as a failure mode — 'failing to capture the adaptive sparsity ratio and dynamic sparse pattern across attention heads, input contents and model architectures.' SegAttn's approach is semi-static (role-level budgets calibrated once, with dynamic phase-switching), which is more flexible than purely static approaches but still relies on the assumption that per-role budgets are consistent across workloads. The proposal should explicitly acknowledge this concern and argue why role-level granularity (coarser than token-level, finer than model-level) hits the right abstraction level — or add per-workload calibration as a fallback.\", \"SGLang hybrid support (issue #12867) is marked INACTIVE, not merely 'under active development' as the proposal states. The issue shows nine major pending development areas with stalled progress. This significantly increases the risk that the Qwen3.6-27B pilot will encounter blocking issues. The proposal should update this characterization and strengthen the fallback plan — explicitly stating that Llama-3.1-8B alone is the primary contribution and the hybrid pilot may be deferred to a camera-ready or follow-up.\", \"Evaluation benchmark gap: User requirements explicitly include HumanEval, LongBench, RULER, and MT-Bench, but the proposal only covers WikiText-2 perplexity, MMLU, and BFCL v3. While the agent-focused evaluation (BFCL v3) is the right primary benchmark, at minimum MT-Bench (for instruction-following quality under compression) and one long-context benchmark (LongBench or RULER) should be added to demonstrate no regression on conversation quality and long-context retrieval — both critical for agent workloads.\", \"Tool Attention's '95% tool-token reduction' is based on projected/simulated results (the authors explicitly state this), not measured on live LLM agents. The complementarity argument ('even after Tool Attention reduces tool tokens, retained context still needs compression') is sound in principle, but the C3 evaluation condition simulates Tool Attention's effect rather than composing with an actual implementation. This should be acknowledged — the C3 condition tests a hypothetical composition, not a measured one.\"]\nFeedback: The proposal is approaching pass quality after 5 rounds of thorough revision. The remaining issues are addressable:\n\n1. **Add 3 missing citations and differentiate**: (a) ChunkKV — uses fixed-size chunks, not semantic roles; SegAttn's role boundaries are zero-cost from chat templates while ChunkKV requires attention-score aggregation. (b) Twilight — adapts sparsity per-context via attention weight distribution (bottom-up); SegAttn uses structural priors from chat templates (top-down). Argue that top-down priors are complementary to bottom-up adaptation. (c) 'Segment-Based Attention Masking for GPTs' (ACL 2025) — addresses prefill-phase causal mask relaxation, not inference-time KV compression; different problem and objective.\n\n2. **Address the static-vs-dynamic sparsity concern head-on**: Acknowledge that purely static patterns fail (cite 'The Sparse Frontier'). Argue that SegAttn operates at a different abstraction level: role-level budgets are coarse-grained structural priors (like VL-Cache's modality split), not fine-grained per-token decisions. The phase-gating mechanism provides the dynamic component. Add a sentence in the approach section: 'We distinguish between role-level budget allocation (semi-static, calibrated) and token-level importance scoring (dynamic, per-input). SegAttn operates at the former level and is composable with dynamic token-level methods.'\n\n3. **Update SGLang hybrid status**: Change 'under active development' to 'remains under development with pending features (marked inactive as of May 2026)' and strengthen the fallback: Llama-3.1-8B results constitute the full contribution; the hybrid pilot is best-effort.\n\n4. **Add MT-Bench to evaluation**: MT-Bench tests instruction-following quality, which is directly relevant to the system-prompt-compression concern identified by 'Pitfalls of KV Cache Compression.' This costs minimal additional compute (~2-3 H100-hours) and directly addresses a key risk.\n\n5. **Acknowledge Tool Attention's simulated results**: Note that C3 simulates the effect of prompt-level tool filtering rather than composing with Tool Attention's actual implementation, and frame this as a conservative test (simulating ideal prompt-level optimization).\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T20:57:35.119Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T20:57:35.119Z",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-10T20:57:35.150Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-10 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.

Direction: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.

Contribution type: METHOD ONLY. Propose new algorithms — not profiling studies.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Generous for efficiency work.
2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.
3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.

Look for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.

Tag: direction=efficiency, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].**
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

## Idea under review (round 6/10)
{
  "title": "Segment-Role-Aware Sparse Attention for Agent Serving",
  "core_problem": "Agent workloads interleave semantically heterogeneous context segments — system instructions, tool definitions, conversation history, and tool outputs — with fundamentally different importance dynamics, but all current sparse attention methods treat tokens uniformly by position, recency, or head-level statistics, ignoring the semantic role each segment plays in driving model behavior at different generation phases. While content-type-differentiated KV compression has been explored for multimodal models (VL-Cache for visual vs. text tokens; HybridKV for modality-aware head classification), these approaches exploit architecturally distinct modality boundaries. Agent contexts present a harder problem: all segments are text tokens within a single modality, yet exhibit distinct and phase-dependent attention patterns that require semantic-role-level (not modality-level) differentiation. Meanwhile, prompt-level optimizations like Tool Attention (April 2026) reduce the number of tool tokens entering context via middleware-layer filtering, but tokens that remain in context — system prompts, conversation history, retained tool schemas, and tool outputs — still occupy the full KV cache without role-differentiated compression. Furthermore, chunk-level KV compression (ChunkKV, NeurIPS 2025) and adaptive token-level pruning (Twilight, NeurIPS 2025 Spotlight) have advanced general-purpose compression, but neither exploits the structurally available semantic-role boundaries unique to agent contexts. This challenge is compounded by the rise of hybrid architectures (e.g., Qwen3.6-27B with 48 Gated DeltaNet + 16 standard attention layers), where KV caches exist only in the attention layers but constitute the dominant memory bottleneck — making attention-layer-targeted compression both necessary and sufficient.",
  "opportunity": "CacheTTL (Nov 2025) showed agent workloads have distinct KV reuse patterns across turns. CodeComp (April 2026) demonstrated structural priors dramatically improve KV compression for code-specific tasks. 'Don't Break the Cache' (Jan 2026) empirically proved that segment-aware caching strategies (e.g., caching system prompts while excluding dynamic tool results) outperform uniform approaches for agent workloads. 'The Pitfalls of KV Cache Compression' (Oct 2025) identified that system prompts degrade catastrophically under uniform KV eviction, causing instruction-following failures. VL-Cache (ICLR 2025) demonstrated that content-type-differentiated compression (visual vs. text tokens) with layer-adaptive budget allocation achieves 90% KV cache reduction in VLMs — proving the general principle that content-type-aware sparsity vastly outperforms uniform approaches. However, VL-Cache's modality boundary is architecturally defined (vision encoder outputs vs. text embeddings), whereas agent segment roles are semantically defined within a single text modality. CrossKV (OpenReview preprint, Sep 2025) decomposes agent contexts into fine-grained semantic segments for KV cache sharing across agents in multi-agent workflows, demonstrating the value of segment-level decomposition — but targets cross-request cache reuse (breaking prefix barriers), not within-request attention sparsity. CacheSlide (FAST 2026) identifies relative-position-dependent caching patterns in agent workflows for cross-position KV reuse, but again targets caching/reuse rather than compression. SABlock (Oct 2025) introduces semantic-aware KV cache eviction using punctuation-based linguistic segmentation with segment-guided token scoring — but operates on natural language sentence boundaries without agent-role awareness or phase-dependent dynamics. Tool Attention (April 2026) achieves projected 95% tool-token reduction at the prompt/middleware level via two-phase lazy schema loading — but this addresses which tokens enter the context, not how retained tokens' KV caches are compressed. After prompt-level filtering, the remaining context still contains system instructions, conversation history, retained tool schemas (for latency-critical or stateless deployments), and tool outputs that occupy KV cache without role differentiation. ChunkKV (NeurIPS 2025) treats fixed-size token groups (default 10 tokens) as compression units with attention-score-based chunk importance scoring and layer-wise index reuse — achieving strong results on long-context benchmarks. However, ChunkKV's fixed-size chunks are content-agnostic: they split across segment boundaries, compressing system instructions and tool outputs identically, and lack phase-dependent dynamics. Twilight (NeurIPS 2025 Spotlight) introduces adaptive attention sparsity via hierarchical top-p pruning, dynamically adjusting per-head budgets based on attention weight distributions — directly validating that fixed-budget sparsity fails in dynamic scenarios. However, Twilight adapts at the token level without structural priors about segment roles, requiring the model to rediscover role importance purely from attention statistics. 'The Sparse Frontier' (arXiv, Jan 2026) provides the largest-scale empirical analysis of training-free sparse attention, finding that no single strategy generalizes across tasks and phases — reinforcing that task-aware and phase-aware sparsity is needed. Segment-Based Attention Masking (ACL 2025, Katz et al.) relaxes causal masking within structured input segments during prefill to improve model quality via lightweight fine-tuning — sharing the concept of segment-aware attention modification but addressing a fundamentally different problem (prefill quality improvement, not inference-time KV compression) and requiring model fine-tuning rather than being training-free. The gap: no method combines structurally available segment-role boundaries with generation-phase-aware dynamic sparsity for attention-level compression of tokens already in context — specifically, (1) the phase-dependent importance dynamics of tool definitions (critical during tool-call generation, negligible during reasoning), which has no analog in VLM compression, chunk-level compression, or prompt-level filtering, and (2) the availability of zero-cost segment classification from chat-template metadata (vs. VL-Cache's attention-score-based scoring, HybridKV's head-classification overhead, ChunkKV's attention-score aggregation, SABlock's punctuation-based boundary detection, and Twilight's attention-weight-distribution analysis). KEEP (Feb 2026) demonstrates static-dynamic memory partitioning for embodied planning agents but operates at the API-level memory management layer, not within the attention mechanism itself. SentenceKV (COLM 2025) manages KV cache at the sentence-semantic level but lacks agent-role awareness. The emerging prevalence of hybrid architectures (Qwen3.5/3.6 series with Gated DeltaNet) creates an additional opportunity: these architectures concentrate all KV cache memory in a minority of attention layers (~25%), making targeted segment-role compression of those specific layers both more impactful per-layer and more tractable to study. The opportunity is a framework that combines zero-cost chat-template-based segment classification with generation-phase-aware dynamic sparsity profiles for tokens already present in context — complementary to both prompt-level optimizations (Tool Attention, prompt caching) that reduce context size upstream, and token-level adaptive methods (Twilight, ClusterAttn) that can operate within each segment's budget.",
  "landscape": "**Content-type-differentiated KV compression (VLM domain)**: VL-Cache (ICLR 2025) differentiates visual and text tokens in VLMs via modality-aware token scoring with layer-adaptive budget allocation, achieving 90% KV reduction. HybridKV (April 2026) classifies attention heads as static/dynamic using text-centric sparsity for multimodal LLMs, achieving 7.9x KV reduction. Both exploit architecturally distinct modality boundaries (vision encoder vs. text embeddings) — inapplicable to single-modality agent contexts where segment roles are semantically, not architecturally, defined.\n\n**Chunk-level and semantic-unit KV management**: ChunkKV (NeurIPS 2025) groups tokens into fixed-size chunks (default 10 tokens) as compression units with attention-score-based chunk importance scoring and layer-wise index reuse, achieving up to 8.7% precision improvement over token-level methods at equivalent compression ratios. ChunkKV's fixed-size chunks are content-agnostic — they uniformly partition the context without regard to segment boundaries, compressing system instructions and tool schemas identically. SegAttn's role boundaries are structurally defined by chat-template metadata at zero cost, not by attention-score aggregation, and enable phase-dependent differential treatment. SentenceKV (COLM 2025) groups tokens at sentence level using semantic similarity for KV cache management — operates on linguistic structure without agent-role awareness. SABlock (Oct 2025) introduces semantic-aware KV cache eviction with segment-guided token scoring using punctuation-based linguistic boundaries — achieves strong results on long-context benchmarks but segments by natural language structure (sentences/clauses), not by agent message roles, and lacks phase-dependent dynamics. KEEP (Feb 2026) introduces static-dynamic memory construction with mixed-granularity groups for embodied planning agents, differentiating segments by update frequency — operates at the memory/API level, not within attention computation.\n\n**Adaptive sparse attention**: Twilight (NeurIPS 2025 Spotlight) introduces adaptive attention sparsity via hierarchical top-p pruning, dynamically adjusting per-head budgets based on attention weight distributions rather than using fixed token budgets. Twilight demonstrates that adaptive budgeting is critical — fixed-budget methods fail to capture varying attention concentration across heads and inputs. However, Twilight operates purely bottom-up from attention statistics without structural priors about input composition; it must rediscover segment importance from attention weights alone. SegAttn provides complementary top-down structural priors: role-level budgets set the coarse allocation, while token-level adaptive methods (including Twilight-style top-p) can operate within each role's budget for fine-grained selection. 'The Sparse Frontier' (arXiv, Jan 2026) provides the largest-scale empirical analysis of training-free sparse attention across six methods, multiple model families, and sequences up to 128K tokens, finding that 'no clear strategy performs best across tasks and phases' and that static patterns fail to generalize. This reinforces our design: SegAttn's role-level budgets are coarse-grained structural priors (analogous to VL-Cache's modality split), not fine-grained static per-token patterns — and the phase-gating mechanism provides the dynamic component that adapts behavior across generation phases. ClusterAttn (ACL 2025) identifies intrinsic attention clustering patterns and adaptively fits density-based clusters for KV cache compression — achieving strong results but operating on emergent attention patterns without explicit segment-role awareness.\n\n**Segment-aware attention modification (different problem)**: Segment-Based Attention Masking (MAS, ACL 2025, Katz et al.) relaxes causal masking within structured input segments during the prefill phase, enabling bidirectional attention within segments to improve model quality. MAS shares the concept of segment-aware attention modification with SegAttn but addresses a fundamentally different problem: prefill-phase quality improvement via fine-tuning, not inference-time KV cache compression. MAS requires lightweight fine-tuning and does not reduce memory; SegAttn is training-free and targets KV cache reduction.\n\n**Prompt-level tool optimization**: Tool Attention (April 2026) achieves projected 95% tool-token reduction via two-phase lazy schema loading — compact tool summaries remain resident while full schemas are promoted only for top-k selected tools during tool-call generation. Note: the 95% reduction figure is based on projected/simulated results from measured token counts combined with deployment telemetry, not measured on live LLM agents. Tool Attention operates at the middleware/prompt layer (embedding-based routing + state gating), requires no LLM modification, and is explicitly orthogonal to KV cache compression. It validates the phase-dependent importance insight (tool schemas matter more during tool-call generation) at the prompt level, but does not compress KV caches for tokens already in context. Deployments that retain full schemas (for latency-critical serving, stateless architectures, or multi-turn cache reuse) still face the uncompressed KV cache problem.\n\n**Agent-specific KV/cache management**: CacheTTL (Nov 2025) introduces time-to-live KV cache management for agent scheduling — handles when to retain cache, not how to compress attention. CodeComp (April 2026) uses Code Property Graphs for structural KV compression, but is domain-specific to code. 'Don't Break the Cache' (Jan 2026) demonstrates segment-aware caching benefits for agent tasks but focuses on API-level prompt caching, not attention-level sparsity. SideQuest (Feb 2026) lets the model decide KV eviction via self-compression but lacks explicit segment-role priors — the model must rediscover role importance without structural guidance.\n\n**Agent-context segment decomposition for cache reuse**: CrossKV (OpenReview preprint, Sep 2025) decomposes agent contexts into fine-grained semantic segments and enables dynamic cross-agent KV cache reuse at arbitrary positions via vLLM's PagedAttention, breaking the rigid prefix-matching barrier. CacheSlide (FAST 2026) identifies Relative-Position-Dependent Caching (RPDC) patterns in agent workflows, enabling cross-position KV reuse with 3.1-4.3x latency reduction. Both focus on inter-request cache sharing/reuse for throughput, not intra-request attention compression for memory — they are complementary to, not competing with, segment-role-aware sparsity.\n\n**General sparse attention**: LServe (MLSys 2025) converts half of attention heads to streaming heads regardless of workload type — workload-agnostic. EvoSparse (ACL 2026) tracks token importance dynamics across steps and layers but does not distinguish semantic segment roles. KVzip (NeurIPS 2025 Oral) enables query-agnostic 3-4x KV compression but treats all context tokens identically. Task-KV (Jan 2025) allocates differentiated KV budgets based on attention-head-level semantic heterogeneity — operates at the head level, not at the input-segment level. 'The Pitfalls of KV Cache Compression' (Oct 2025) identifies system prompt degradation under uniform compression and proposes eviction-order fixes, but does not provide a systematic role-differentiated framework. HeteroCache (Jan 2026) exploits head-level heterogeneity via stability-based clustering. MSA (March 2026) introduces document-level routing for 100M-token contexts but uses position-based chunking without agent-specific awareness. SeerAttention (ICLR 2026) learns block-level sparsity via gating but does not differentiate blocks by content type.\n\nNo method provides generation-phase-aware, segment-role-differentiated sparse attention for heterogeneous agent contexts within a single text modality — including for emerging hybrid architectures where KV caches are concentrated in a subset of attention layers. Existing adaptive methods (Twilight, ClusterAttn) provide complementary token-level dynamics but lack structural priors; existing structural methods (ChunkKV, SABlock) use content-agnostic or linguistic boundaries without agent-role awareness. SegAttn occupies the unique intersection: zero-cost structural priors from chat-template metadata combined with phase-aware dynamic sparsity, composable with both upstream prompt-level filtering (Tool Attention) and downstream token-level adaptive pruning (Twilight).",
  "approach": "We propose SegAttn, a training-free sparse attention framework with two core contributions: (1) an empirical attention profiling study demonstrating that segment-role attention patterns are consistent and exploitable across models and agent workloads, and (2) a practical system that operationalizes these patterns via role-differentiated, phase-aware sparsity budgets — designed to be complementary to both prompt-level optimizations (Tool Attention, prompt caching) that reduce context size upstream and token-level adaptive methods (Twilight, ClusterAttn) that can refine selection within each segment's budget.\n\n**Positioning on the static-vs-dynamic spectrum**: 'The Sparse Frontier' (Jan 2026) and Twilight (NeurIPS 2025) demonstrate that purely static, fine-grained sparsity patterns fail to generalize across heads, inputs, and tasks. We distinguish between two levels of sparsity decision: (i) role-level budget allocation — coarse-grained structural priors determining how much compression each segment type receives, analogous to VL-Cache's modality split — and (ii) token-level importance scoring — fine-grained, per-input decisions about which specific tokens to retain within each budget. SegAttn operates at level (i) and is explicitly composable with dynamic token-level methods at level (ii). Role-level budgets are semi-static (calibrated per architecture, with dynamic phase-switching for tool definitions), while token-level selection within each role's budget can use any existing adaptive method (attention-score-based eviction, top-p pruning, etc.). This two-level design avoids the failure mode of static token-level patterns while exploiting structural regularities that purely bottom-up methods must rediscover from attention statistics alone.\n\n**Model selection rationale**: We use Llama-3.1-8B (8B, 32 attention layers, 8 KV heads, 128 head_dim) as the primary model — a standard transformer where SegAttn applies uniformly to all layers, yielding clean, generalizable results. Qwen3.6-27B (27B, 16 Gated Attention + 48 Gated DeltaNet layers) serves as a best-effort pilot demonstration of hybrid-architecture applicability. In Qwen3.6-27B, only the 16 Gated Attention layers have traditional KV caches (4 KV heads, 256 head_dim); the 48 DeltaNet layers use fixed-size O(d²) recurrent states (~0.5 MB per layer, ~24 MB total) that are sequence-length-independent and require no compression. SegAttn targets exactly the 16 attention layers, which hold 100% of the model's KV cache memory (~6.55 GB at 100K context in BF16 — 273× the total DeltaNet state). Note: SGLang's hybrid model support (GitHub issue #12867) remains under development with multiple pending features (prefix caching adaptation, speculative decoding, kernel optimization among nine areas) and is currently marked inactive as of May 2026. If SGLang integration proves intractable within the timeline, the Llama-3.1-8B results alone constitute the complete primary contribution; the hybrid-architecture pilot is scoped as best-effort and may be deferred to camera-ready or follow-up work.\n\n**Key differentiators from VL-Cache, content-type compression, chunk-level compression, adaptive pruning, segment-level cache sharing, and prompt-level filtering**: SegAttn addresses properties unique to agent contexts: (a) **Dynamic phase-gating** — tool definition tokens shift between critical (during tool-call generation) and negligible (during reasoning) within a single inference pass; VL-Cache's visual/text split is static throughout generation; ChunkKV's fixed chunks are phase-unaware; Twilight adapts per-head budgets but without structural role priors; Tool Attention exploits this same insight but at the prompt layer (excluding schemas entirely), while SegAttn compresses schemas that are retained in context. (b) **Zero-cost segment classification** — chat-template metadata (ChatML role tags, Llama-style [INST] markers) provides exact segment boundaries without any scoring computation; VL-Cache requires attention-score-based modality-aware scoring, HybridKV requires text-centric sparsity head classification, ChunkKV requires attention-score aggregation per chunk, SABlock requires punctuation-based boundary detection, Twilight requires attention-weight-distribution analysis for top-p thresholding. (c) **Intra-request compression of retained context** — CrossKV and CacheSlide decompose segments for inter-request cache reuse; Tool Attention filters tokens before they enter context; SegAttn compresses segments within the attention computation of a single request for tokens already present. (d) **Composability with adaptive token-level methods** — SegAttn's role-level budgets define how much to compress each segment type; within each segment's budget, any token-level selection method (attention-score eviction, Twilight-style top-p, etc.) can be applied. This makes SegAttn a structural prior layer that enhances, rather than replaces, existing adaptive compression.\n\n**Segment Classification**: Tokens are tagged by semantic role (system instruction, tool schema, conversation turn, tool output) using chat-template metadata and structured message boundaries. This requires no model modification and no scoring overhead — just parsing the tokenized input against known template patterns.\n\n**Role-Differentiated Sparsity**: System instructions receive block-level KV sparsity (retain only high-attention blocks identified during a short calibration pass), exploiting their persistent but diffuse pattern identified by 'Pitfalls of KV Cache Compression'. Tool definitions are phase-gated: preserved at full fidelity when tool-call generation is detected (reactive detection via chat-template special tokens like `&lt;tool_call>` or `<|plugin|>` — once the first tool-call token appears, the sparsity profile switches for subsequent tokens in the sequence; the 1-2 token detection delay is negligible given tool-call sequences span 50-200 tokens), and aggressively compressed during reasoning phases. Recent tool outputs are protected from eviction within a recency window. For hybrid architectures like Qwen3.6-27B, phase-gating modifies only the 16 attention layers' masks — but since these layers contain 100% of the compressible KV cache, phase-gating controls the entirety of the memory reduction opportunity.\n\n**Implementation via FlashInfer with FlexAttention Fallback**: We leverage FlashInfer's existing block-sparse attention API and paged KV-cache management, already integrated into SGLang. Segment-role masks are generated as block-sparse attention masks fed to FlashInfer's sparse attention kernels for the attention layers only. Phase-gating is implemented as dynamic mask switching triggered by special token detection in the decode loop. **Addressing plan() reconfiguration overhead** (GitHub issue #2938): FlashInfer's `plan()` function triggers device-to-host memcpy for scheduling, which can create synchronization overhead during mask reconfiguration. For SegAttn, this is mitigated by three factors: (i) phase transitions are infrequent (1-2 per generation spanning 50-200+ tokens), so plan() is called at most 1-2 additional times per generation, amortized over dozens to hundreds of decode steps; (ii) we pass host tensors (indptr, indices) directly to plan() to avoid GPU-to-CPU transfers, following FlashInfer v0.2 best practices; (iii) non-blocking host-to-device transfers during plan() further reduce pipeline stalls. We will benchmark plan() reconfiguration latency during ablation studies to quantify amortized overhead. **FlexAttention fallback**: If FlashInfer's plan() overhead proves prohibitive for specific deployment scenarios, PyTorch's FlexAttention provides an alternative via `create_block_mask()` + `score_mod()` that supports dynamic mask changes without kernel recompilation — the compiled kernel remains valid when only the BlockMask metadata changes. FlexAttention's block_mask approach is well-suited for phase-gating since the sparsity pattern change is a one-time switch per phase transition.\n\n**Profiling Protocol (Contribution 1)**: We profile attention patterns on: (a) 100 BFCL v3 multi-turn function-calling traces, and (b) 50 multi-turn ReAct-style traces (from HotpotQA with tool-augmented retrieval). For Llama-3.1-8B, we profile all 32 attention layers. For Qwen3.6-27B (if SGLang integration permits), we profile the 16 Gated Attention layers specifically. We explicitly investigate whether having fewer, more widely-spaced attention layers (every 4th layer) concentrates segment-role patterns compared to dense attention architectures. For each trace, we extract per-layer, per-head attention mass ratios allocated to each segment role during different generation phases (tool-call generation vs. free-form reasoning vs. summarization). Key metrics: (i) segment-role attention mass concentration, (ii) cross-segment attention entropy, (iii) phase-conditional attention shift. **Cross-architecture analysis**: Rather than requiring a single universal profile, we evaluate whether per-architecture profiles are necessary — consistency within each architecture is the primary criterion, with cross-architecture transferability as a bonus. **Falsification criterion**: if the coefficient of variation of segment-role attention mass ratios across workloads exceeds 0.5 for any segment type within either architecture (not across architectures), the 'consistent patterns' hypothesis is rejected for that architecture and the system would fall back to per-workload calibration.\n\n**Evaluation with Layered Optimization Conditions**: Llama-3.1-8B (primary, 16GB BF16, all 32 layers are attention) and Qwen3.6-27B (best-effort pilot, 55.6GB BF16, 16 attention layers) on: (a) **agent benchmark** — BFCL v3 for tool-calling accuracy; (b) **general capability** — WikiText-2 perplexity and MMLU to demonstrate no regression; (c) **instruction-following quality** — MT-Bench to verify system-prompt compression does not degrade instruction adherence, directly addressing the system-prompt sensitivity identified by 'Pitfalls of KV Cache Compression'; (d) **long-context capability** — LongBench (multi-task long-context evaluation) to demonstrate no regression on retrieval and comprehension tasks critical for agent workloads with extended conversation histories. **Critically, we evaluate SegAttn under three conditions**: (C1) SegAttn alone — full tool schemas in context, measuring standalone compression value; (C2) Prompt caching ('Don't Break the Cache') + SegAttn — segment-aware API-level caching active, measuring marginal benefit of attention-level compression on top of caching optimization; (C3) Tool-schema filtering (simulating Tool Attention's projected 95% reduction) + SegAttn — only top-k relevant tool schemas retained in context, measuring marginal benefit of attention-level compression when prompt-level filtering is already applied. **Transparency note on C3**: The C3 condition simulates the effect of prompt-level tool filtering by manually retaining only top-k tool schemas rather than composing with Tool Attention's actual implementation (whose 95% reduction is itself based on projected results, not live agent measurements). C3 thus tests a hypothetical but conservative composition — if SegAttn provides meaningful compression even after ideal prompt-level optimization, the value under real-world (likely less ideal) filtering is strictly greater. This layered evaluation directly addresses whether attention-level segment-role compression provides value beyond prompt-level optimizations. **Expected value argument**: Even under C3, retained context still contains system instructions (~500-2000 tokens), full conversation history (growing with turns), the retained top-k tool schemas, and tool outputs — all of which benefit from role-differentiated compression. SegAttn's value increases with conversation length (as history and outputs accumulate), precisely the regime where prompt-level filtering alone is insufficient. Target: meaningful KV cache reduction with <2% task degradation on BFCL v3, <0.1 perplexity increase on WikiText-2, and <5% score degradation on MT-Bench and LongBench. For Qwen3.6-27B pilot (if feasible), we additionally report the effective whole-model memory reduction.\n\n**Differentiation summary**: VL-Cache differentiates modalities via scoring (architecture-level); SegAttn differentiates semantic roles via chat templates (zero-cost, within single modality). HybridKV classifies heads by sparsity type; SegAttn classifies input segments by semantic role. ChunkKV groups fixed-size token chunks with attention-score aggregation; SegAttn groups variable-size agent segments with zero-cost chat-template boundaries and phase-awareness. Twilight adapts token-level budgets via top-p pruning (bottom-up); SegAttn sets role-level budgets via structural priors (top-down) — composable as two complementary layers. Segment-Based Attention Masking (ACL 2025) relaxes causal masks within segments during prefill for quality improvement (requires fine-tuning); SegAttn compresses KV caches by segment role during inference (training-free). CrossKV decomposes segments for cross-agent cache sharing (inter-request reuse); SegAttn decomposes segments for intra-request attention compression. CacheSlide exploits cross-position reuse patterns for serving throughput; SegAttn compresses within the attention mechanism. KEEP manages static/dynamic memory at the API level; SegAttn operates within attention computation. Tool Attention filters which tool schemas enter the context (prompt-level); SegAttn compresses KV caches for tokens already in context (attention-level) — they are complementary and composable. SABlock segments by linguistic punctuation boundaries; SegAttn segments by agent message roles from chat-template metadata with phase-awareness. Task-KV differentiates which attention heads matter (head-level); SegAttn differentiates which input segments to compress (token-segment-level). 'Pitfalls' proposes eviction-order fixes; SegAttn provides a systematic role-differentiated framework. CodeComp uses code-specific structural priors; SegAttn is domain-general. SideQuest requires the model to rediscover role importance; SegAttn provides explicit priors from chat-template metadata. SentenceKV operates at linguistic sentence granularity; SegAttn operates at agent message-role granularity with phase-awareness. ClusterAttn identifies emergent attention clusters; SegAttn exploits known structural role boundaries.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~165h H100 (attention profiling on both architectures: 35h, FlashInfer integration + mask generation: 20h, phase-gating implementation with plan() benchmarking: 18h, hybrid-architecture pilot: 10h, ablation studies including layered evaluation conditions: 32h, benchmark evaluation incl. MT-Bench and LongBench: 38h, buffer: 12h)",
      "gpu_utilization": "~20-30% effective; GPUs idle during FlashInfer integration debugging and attention heatmap analysis",
      "timeline": "3-4 weeks (does NOT fit May 25 deadline)",
      "team": "1-2 researchers (1 ML/attention, 1 systems/serving)",
      "estimated_gpu_cost": "$660 (165h × $4.00/hr H100)"
    },
    "human_in_loop": {
      "gpu_hours": "~185h H100 (attention profiling across both architectures: 40h, integration: 25h, phase-gating + plan() overhead benchmarking: 18h, hybrid-arch pilot: 10h, ablation including 3 evaluation conditions (C1-C3): 42h, benchmarks incl. MT-Bench + LongBench: 38h, buffer: 12h)",
      "gpu_utilization": "~55-70%; agent queues experiments while human reviews segment-budget ratios and validates attention profiling results",
      "timeline": "12-16 days (tight but possible for May 25 deadline)",
      "team": "1 researcher, ~25-35 min/day reviewing agent proposals for mask generation logic and profiling analysis",
      "claude_api_cost": "$200-400 (~2000-4000 turns for code generation, experiment design, profiling analysis)",
      "estimated_gpu_cost": "$740 (185h × $4.00/hr H100)",
      "risk_note": "FlashInfer plan() overhead (issue #2938) may require switching to FlexAttention fallback; SGLang hybrid support (issue #12867, currently inactive) may limit Qwen3.6-27B pilot to basic inference or require deferral to camera-ready"
    },
    "auto_research": {
      "gpu_hours": "~205h H100 (profiling across both architectures × multiple workloads: 50h, 2x more budget configurations explored: 40h, hybrid-arch pilot ablations: 15h, layered evaluation grid (C1-C3 × 2 models) + MT-Bench + LongBench: 52h, cross-architecture comparison: 20h, plan() overhead benchmarking: 5h, buffer: 23h)",
      "gpu_utilization": "~80-90%; continuous experiment pipeline with agent iterating across segment-budget ratios, phase-detection thresholds, and recency windows",
      "timeline": "8-12 days with 2 H100 GPUs available concurrently (the ONLY path that reliably fits the May 25 EMNLP deadline)",
      "team": "0 (initial setup only, ~2 hours to configure SGLang + FlashInfer environment and benchmark datasets)",
      "claude_api_cost": "$400-700 (~4000-7000 turns for iterative development, experiment execution, profiling analysis)",
      "estimated_gpu_cost": "$820 (205h × $4.00/hr H100)",
      "speed_bottleneck": "GPU count: 2 H100 80GB needed (one for Qwen3.6-27B serving, one for Llama-3.1-8B + experiment orchestration); FlashInfer API exploration may require multiple iteration cycles; if plan() overhead is prohibitive, FlexAttention integration adds ~1 day",
      "risk_note": "Agent may over-explore the segment-budget configuration space without human pruning; SGLang's hybrid support (issue #12867, inactive) may limit Qwen3.6-27B pilot scope or require deferral; profiling study must complete in days 1-3 to leave time for system building"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline: May 25, 2026 — requires auto_research path)",
    "AAAI 2027 (submission deadline: August 1, 2026 — comfortable with any path)",
    "ICLR 2027 (estimated deadline: September-October 2026)"
  ],
  "level": "solid",
  "key_references": [
    "VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration (ICLR 2025)",
    "HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference (arXiv 2604.05887, April 2026)",
    "SentenceKV: Efficient LLM Inference via Sentence-Level Semantic KV Caching (COLM 2025)",
    "KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning (arXiv 2602.23592, Feb 2026)",
    "Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live (arXiv 2025)",
    "CodeComp: Structural KV Cache Compression for Agentic Coding (arXiv 2026)",
    "LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention (MLSys 2025)",
    "Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention (ACL 2026)",
    "KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction (NeurIPS 2025 Oral)",
    "Task-KV: Task-aware KV Cache Optimization via Semantic Differentiation of Attention Heads (arXiv 2501.15113, Jan 2025)",
    "The Pitfalls of KV Cache Compression (arXiv 2510.00231, Oct 2025)",
    "HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference (arXiv 2026)",
    "SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning (arXiv 2026)",
    "MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens (arXiv 2026)",
    "SeerAttention: Learning Intrinsic Sparse Attention in Your LLMs (ICLR 2026)",
    "Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks (arXiv 2026)",
    "Block Sparse Flash Attention (arXiv 2512.07011, Dec 2025)",
    "FlashInfer: Efficient and Customizable Attention Engine for LLM Inference (arXiv 2501.01005, Jan 2025)",
    "Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing (OpenReview preprint, Sep 2025)",
    "CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving (FAST 2026)",
    "Gated DeltaNet: Adaptive Fast-Weight Model (NeurIPS 2024)",
    "Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows (arXiv 2604.21816, April 2026)",
    "SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size (arXiv 2510.22556, Oct 2025)",
    "ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference (NeurIPS 2025)",
    "Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning (NeurIPS 2025 Spotlight)",
    "Segment-Based Attention Masking for GPTs (ACL 2025, arXiv 2412.18487)",
    "The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs (arXiv 2504.17768, Jan 2026)",
    "ClusterAttn: KV Cache Compression under Intrinsic Attention Clustering (ACL 2025)"
  ],
  "description": "Agent workloads interleave semantically heterogeneous context segments — system instructions, tool schemas, conversation history, and tool outputs — with fundamentally different attention dynamics, yet all current sparse attention methods treat tokens uniformly. While content-type-differentiated KV compression has been explored for VLMs (VL-Cache, HybridKV), chunk-level compression with fixed-size token groups (ChunkKV), adaptive token-level pruning (Twilight), segment-level decomposition for agent cache sharing (CrossKV, CacheSlide), semantic-unit eviction for linguistic boundaries (SABlock), segment-aware attention masking for prefill quality (MAS, ACL 2025), and prompt-level tool filtering at the middleware layer (Tool Attention), no method combines structurally available segment-role boundaries with generation-phase-aware dynamic sparsity for within-request attention compression of tokens already in context. We propose SegAttn, a training-free framework with two contributions: (1) a hypothesis-driven empirical profiling study measuring segment-role attention patterns across architectures — standard transformers (Llama-3.1-8B, all 32 layers profiled) and hybrid linear-attention architectures (Qwen3.6-27B, 16 Gated Attention layers profiled as a best-effort pilot) — across agent workloads (100 BFCL v3 traces, 50 ReAct traces) and generation phases, with per-architecture falsification criteria (CV > 0.5 rejects consistency); and (2) a practical system exploiting three properties unique to agent contexts: zero-cost segment classification from chat-template metadata (vs. ChunkKV's attention-score aggregation and Twilight's attention-weight analysis), dynamic phase-gating of tool definitions (critical during tool-call generation, compressed during reasoning — validating at the attention level the same insight Tool Attention exploits at the prompt level), and recency-windowed protection of tool outputs. We explicitly position SegAttn on the static-vs-dynamic spectrum: role-level budgets are coarse-grained structural priors (analogous to VL-Cache's modality split), not fine-grained static per-token patterns that 'The Sparse Frontier' identifies as a failure mode. The phase-gating mechanism provides the dynamic component, and SegAttn is composable with token-level adaptive methods (Twilight-style top-p pruning) within each segment's budget. We evaluate under layered optimization conditions: SegAttn alone (C1), with prompt caching (C2), and with simulated prompt-level tool filtering (C3, acknowledging Tool Attention's projected rather than measured results), demonstrating marginal value beyond upstream optimizations. Evaluation spans BFCL v3 (tool-calling), WikiText-2 perplexity, MMLU (general capability), MT-Bench (instruction-following quality under compression), and LongBench (long-context retrieval and comprehension). Implemented using FlashInfer's block-sparse attention API within SGLang (with FlexAttention as fallback for dynamic mask reconfiguration, addressing FlashInfer plan() overhead per GitHub issue #2938). Unlike VL-Cache (static modality split), ChunkKV (fixed-size content-agnostic chunks), Twilight (bottom-up adaptive pruning without structural priors), MAS (prefill quality via fine-tuning), CrossKV (inter-request segment sharing), CacheSlide (cross-position reuse), KEEP (API-level memory), SABlock (linguistic-unit segmentation), SentenceKV (linguistic-unit granularity), Tool Attention (prompt-level filtering with projected results), or SideQuest (model self-compression), SegAttn is the first method combining zero-cost chat-template classification with generation-phase-aware sparsity for attention-level compression of retained agent context — providing top-down structural priors composable with bottom-up adaptive token-level methods — applicable to both standard and hybrid architectures. Estimated ≤205 H100-hours. Primary target: EMNLP 2026 (auto_research path required for May 25 deadline).",
  "project_name": "seg_role_sparse_attn",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL: Resource estimate (400-800h A100) exceeds user's hard constraint of ≤200 H100-hours by 2-4x. The idea must be scoped down or the approach simplified to fit within budget.", "CRITICAL: Llama-4-Scout-17B-16E requires ~220GB VRAM in BF16 (109B total parameters across 16 experts), not ~70GB as claimed. This means multi-GPU tensor-parallel serving is mandatory, significantly increasing complexity and effective GPU-hour consumption.", "Phase-gating mechanism via 'output-vocabulary monitoring' is underspecified and technically problematic. Detection of tool-call generation is retroactive — you only know the model is generating a tool call after it outputs the first tool-call tokens (e.g., '&lt;tool_call>' special token). How do you proactively switch attention profiles before the attention computation for those tokens?", "Missing highly relevant citations: (1) Task-KV (arXiv 2501.15113, Jan 2025) — task-aware KV cache optimization via semantic differentiation of attention heads; (2) 'The Pitfalls of KV Cache Compression' (arXiv 2510.00231, Oct 2025) — identifies system prompt degradation under compression and proposes eviction policy fixes. Both directly address subproblems that SegAttn claims to solve.", "Evaluation benchmark mismatch: User requires perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench, but the idea only proposes BFCL v4, SWE-Bench, AgentBench. While agent-specific benchmarks are appropriate for this idea, the user's required benchmarks should also be included to demonstrate no regression on general capabilities.", "The 3-5x KV cache reduction target lacks supporting evidence. The claim that heuristic segment-role tagging can match or exceed KVzip's 3-4x compression (which uses sophisticated reconstruction-based importance scoring) requires justification.", "16-day timeline is extremely tight for: custom Triton kernel development for phase-gated block-sparse attention, SGLang attention backend integration, attention profiling across 2 models, ablation studies on role-specific budgets, and evaluation on 3 agent benchmarks. This risks producing an incomplete or poorly-evaluated paper.", "Generalizability concern: The approach relies on chat-template metadata and structured message boundaries for segment classification. Different models use different chat templates (ChatML, Llama-style, etc.), and the role-budget allocations may need per-model tuning, undermining the 'general-purpose' claim."]
Feedback: To reach pass quality, address these priority items:

1. **Fix compute budget**: Drop Llama-4-Scout entirely (too large for the budget) and focus on Qwen3.6-27B plus one smaller model (e.g., Llama-3.1-8B or Qwen3-14B). Reduce to 2 agent benchmarks (BFCL v4 + SWE-Bench). Target ≤180 H100-hours with a concrete hour breakdown: profiling (X h), kernel development (Y h), ablation (Z h), final eval (W h).

2. **Fix phase-gating mechanism**: Replace 'output-vocabulary monitoring' with a concrete, implementable detection strategy. The simplest: use the chat template's special tokens (e.g., `&lt;tool_call>`, `<|plugin|>`) as reactive triggers — once detected, switch sparsity profiles for subsequent tokens in the tool-call sequence. Acknowledge this is reactive (1-2 token delay) and quantify the impact. Alternatively, use a lightweight classifier on the last-layer hidden state to predict phase 1-2 tokens ahead.

3. **Add missing citations and differentiate**: Cite Task-KV and 'Pitfalls of KV Cache Compression.' Explicitly explain how SegAttn differs: Task-KV differentiates at the attention-head level (which heads matter for the task), while SegAttn differentiates at the token-segment level (which input segments to compress). 'Pitfalls' identifies the problem but only proposes simple eviction-order fixes, while SegAttn provides a systematic role-differentiated framework.

4. **Include user-required benchmarks**: Add perplexity (WikiText/C4) and at least MMLU or MT-Bench alongside agent benchmarks to demonstrate no general-capability regression.

5. **Scope down for 16-day timeline**: Consider using existing sparse attention kernels (e.g., from LServe or FlashAttention block-sparse mode) rather than writing custom Triton kernels from scratch. This trades peak performance for development speed.

6. **Strengthen novelty**: The current contribution is 'combine three known techniques under a taxonomy.' To strengthen: (a) provide empirical attention profiling data showing that segment-role patterns are consistent and exploitable across models (this is the key assumption that needs validation), or (b) propose a learned segment-budget allocator rather than hand-tuned heuristics.

### Round 2 review
Verdict: revise
Issues: ["IMPORTANT: Missing citation VL-Cache (ICLR 2025) — applies content-type-differentiated KV compression for VLMs (visual vs. text tokens with different budgets and phase-aware strategies). This is conceptually the closest prior work to SegAttn's segment-role differentiation, just in the multimodal domain instead of agent contexts. The generator MUST cite this and explicitly differentiate — otherwise reviewers familiar with VLM efficiency will view SegAttn as a straightforward domain transfer.", "Missing citations: SentenceKV (COLM 2025) — semantic-unit-level KV cache management; HybridKV (arXiv 2604.05887, April 2026) — content-type-aware hybrid KV compression for multimodal LLMs with head classification by text-centric sparsity. Both demonstrate that 'differential compression by content type' is an established pattern, not a novel contribution.", "Timeline contradiction: The manual estimate says 4-6 weeks but the deadline is 15 days. Even the auto_research estimate of 8-12 days with 2 H100s is cutting it very close to May 25. The attention profiling study across 2 models × multiple agent workloads is itself a multi-day effort before any system building begins.", "The 2-3x KV compression target still lacks supporting evidence from any preliminary experiment or prior empirical observation. The Pitfalls paper shows system prompts degrade under uniform compression, but that tells us which segments to PROTECT, not how much we can compress others. Without pilot data showing how much agent-context tool definitions and conversation history can actually be compressed without task degradation, the target is speculative.", "Evaluation scope vs. timeline mismatch: BFCL v4 + SWE-Bench (agent benchmarks) + WikiText-2 perplexity + MMLU + MT-Bench across 2 models is 10+ separate evaluation runs. SWE-Bench alone (with its agentic scaffolding) takes significant compute and setup time. This is likely the first thing to be cut under time pressure, weakening the paper.", "KEEP (arXiv 2602.23592, Feb 2026) is missing from the landscape — it introduces static-dynamic memory construction with mixed-granularity groups for agent KV cache, which shares the insight that different memory segments have different reuse patterns and deserve different treatment.", "The profiling study (contribution 1) and the system (contribution 2) compete for limited time. If profiling reveals unexpected patterns (e.g., segment-role patterns are NOT consistent across models or workloads), the entire system design needs to change. This is a research risk that the tight timeline cannot absorb."]
Feedback: The revision successfully addressed Round 1's critical issues (compute budget, model selection, phase-gating mechanism, missing Task-KV/Pitfalls citations). The proposal is now within budget and technically concrete. To reach pass quality:

1. **Cite VL-Cache (ICLR 2025) and differentiate explicitly**: VL-Cache differentiates visual vs. text tokens in VLMs with modality-aware budgets and phase-aware strategies. SegAttn differentiates semantic roles in text-only agent contexts. The key differentiator is that VL-Cache's modalities are architecturally distinct (vision encoder tokens vs. text tokens), while SegAttn's segment roles are semantically defined within a single modality via chat-template metadata. Also cite SentenceKV, HybridKV, and KEEP.

2. **Strengthen novelty beyond 'domain transfer'**: Currently SegAttn risks being viewed as 'VL-Cache for agents.' To differentiate: (a) emphasize the phase-gating mechanism (tool definitions shift between critical and negligible depending on generation phase — this dynamic role-switching has no analog in VL-Cache's static visual/text split); (b) the fact that agent segment boundaries are known a priori from chat templates (zero-cost classification vs. VL-Cache's learned scoring); (c) present the profiling study as revealing agent-specific attention patterns that fundamentally differ from VLM patterns.

3. **Reduce evaluation scope to fit timeline**: Drop SWE-Bench (too heavy for 15 days) and keep BFCL v4 as the agent benchmark. For general capability, WikiText-2 perplexity + MMLU should suffice. This makes the evaluation completable in 2-3 days rather than 5+.

4. **Add pilot profiling data or at minimum a concrete protocol**: Describe exactly which agent workloads you'll profile (e.g., 100 BFCL traces, 50 multi-turn ReAct traces), what metrics you'll extract (per-segment attention mass ratios, cross-segment attention entropy), and what threshold would falsify your hypothesis. This transforms the profiling study from speculative to hypothesis-driven.

5. **Reconcile timeline estimates**: Set manual at 3-4 weeks, HIL at 12-16 days, auto at 8-12 days. The auto path is the only one that fits the May 25 deadline — be explicit about this.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL: Qwen3.6-27B uses a hybrid architecture with 16×(3×(Gated DeltaNet→FFN)→1×(Gated Attention→FFN)) = 48 DeltaNet layers + 16 standard attention layers. Only the 16 attention layers have traditional KV caches and attention patterns. The proposal assumes a standard transformer throughout — profiling study, FlashInfer block-sparse masks, and phase-gating all only apply to 25% of the model's layers. While 100% of the KV cache memory resides in these 16 layers (DeltaNet uses O(d²) fixed-size states), this architectural reality must be explicitly acknowledged and its implications discussed.", "Missing citation: 'Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing' (ICLR 2026, OpenReview). This paper decomposes agent context into 'fine-grained semantic segments' for KV cache management on vLLM. While it focuses on multi-agent segment SHARING (not single-agent compression), the shared concept of agent-context segment decomposition must be cited and differentiated.", "The profiling study's generalizability is weakened for hybrid architectures: measuring 'segment-role attention patterns' across only 16 attention layers in Qwen3.6-27B provides a very different signal than profiling all 32 layers in Llama-3.1-8B. The falsification criteria (CV > 0.5) should account for this architectural asymmetry — consistency across models with fundamentally different attention coverage is a higher bar.", "The compression ratio target remains speculative. For Qwen3.6-27B, the 16 attention layers use only 4 KV heads with 256 dim, yielding ~6.4 GB KV cache at 100K tokens. With DeltaNet handling 75% of computation efficiently, the marginal benefit of KV compression in the attention layers may be less impactful than implied. A concrete analysis of where the actual serving bottleneck lies for this specific architecture would strengthen the proposal.", "Phase-gating implementation on Qwen3.6 needs clarification: in a hybrid architecture where DeltaNet layers process all tokens via recurrence (no masking possible), does phase-gating only modify the 16 attention layers' masks? If so, the efficiency gain from phase-gating is limited to those layers' compute, which is ~25% of total attention compute."]
Feedback: The proposal has improved significantly across rounds 1-2, with excellent differentiation from prior work and concrete implementation details. To reach pass quality:

1. **Address Qwen3.6-27B hybrid architecture explicitly**: Acknowledge that SegAttn targets the 16 standard attention layers (which hold 100% of the KV cache). Frame this positively: since DeltaNet layers already handle long contexts efficiently via O(d²) states, the attention layers are precisely where compression matters most. The profiling study should focus on these 16 layers and discuss whether having fewer attention layers actually CONCENTRATES segment-role patterns (making them easier to exploit).

2. **Cite 'Collaborative Memory' (ICLR 2026)**: Differentiate clearly — that work decomposes segments for multi-agent SHARING across requests (breaking prefix barriers); SegAttn decomposes segments for single-agent COMPRESSION within attention computation. They're complementary, not competing.

3. **Adjust profiling study scope**: State that for hybrid architectures, the profiling study targets attention layers specifically (the only layers with exploitable attention patterns). For Llama-3.1-8B (all 32 layers are attention), the full model is profiled. Discuss whether cross-architecture generalization is a goal or whether per-architecture profiles are acceptable.

4. **Quantify the actual bottleneck**: For Qwen3.6-27B at 100K tokens, the 16 attention layers' KV cache is ~6.4 GB. Is this the actual serving bottleneck, or does the DeltaNet state computation dominate? A concrete calculation showing that attention-layer KV cache is the memory bottleneck (not DeltaNet computation) would justify the approach.

5. **Consider making Llama-3.1-8B the primary model**: Since it's a standard transformer where SegAttn applies uniformly to all layers, results will be cleaner and more generalizable. Use Qwen3.6-27B as the secondary model to demonstrate applicability to hybrid architectures.

### Round 4 review
Verdict: revise
Issues: ["IMPORTANT: Missing citation 'Tool Attention Is All You Need' (arXiv:2604.21816, April 2026). This middleware-layer mechanism uses two-phase lazy schema loading — keeping compact tool summaries during reasoning and promoting full schemas only for top-k selected tools during tool-call generation. While it operates at the prompt/API level (not attention level), it validates the same phase-dependent tool schema importance insight that SegAttn's phase-gating exploits. The 95% tool-token reduction it achieves at the prompt level raises a crucial question: if tool schemas can simply be excluded from the context during reasoning, how much additional benefit does attention-level phase-gating provide on top of prompt-level filtering? SegAttn must demonstrate complementary value — compressing tool tokens that remain in context after prompt-level optimization, or handling cases where full schemas must be retained for other reasons.", "IMPORTANT: FlashInfer plan() overhead threatens phase-gating implementation. GitHub issue #2938 (April 2026) documents that dynamic_block_sparse_fwd_flashinfer triggers per-block device-to-host memcpy during the planning phase, making mask reconfiguration expensive. Phase-gating requires calling plan() with a new mask when a phase transition is detected. While transitions are infrequent (1-2 per generation), the overhead may be non-trivial for latency-sensitive serving. The proposal should: (a) acknowledge this limitation explicitly, (b) benchmark plan() reconfiguration latency, and (c) discuss FlexAttention (PyTorch) as a fallback if FlashInfer's overhead is prohibitive.", "SGLang hybrid model support for Gated DeltaNet architectures remains under active development (GitHub issue #12867). Key features including prefix caching adaptation, speculative decoding, and GDN kernel optimization are listed as pending on the roadmap. The Qwen3.6-27B experiments may encounter missing features or bugs. The proposal should explicitly acknowledge this risk and have a fallback: either use vLLM's hybrid support (which has its own limitations per issue #41560) or scope Qwen3.6-27B as a 'preliminary/pilot' evaluation rather than a full secondary model.", "Missing citation: SABlock (arXiv:2510.22556, Oct 2025) — semantic-aware KV cache eviction with segment-guided token scoring. While it operates on linguistic semantic boundaries (not agent-role boundaries) and lacks phase-gating, it is the closest prior work on semantic segmentation for KV cache management within a single text modality. Should be cited and differentiated: SABlock segments by linguistic coherence; SegAttn segments by agent message roles from chat-template metadata.", "The relationship between prompt-level tool-schema optimization and attention-level compression is unexamined. In realistic agent deployments, prompt caching ('Don't Break the Cache') and tool-schema filtering ('Tool Attention') are already applied at the prompt level. SegAttn's evaluation should include a condition where these prompt-level optimizations are already active, measuring the marginal benefit of attention-level segment-role compression on top of an already-optimized context. Without this, the claimed compression opportunity may be overstated.", "CrossKV venue claim needs verification: the proposal states 'ICLR 2026' but the paper was posted on OpenReview in October 2025 without confirmed ICLR 2026 acceptance in my searches. If the venue cannot be verified, cite as 'OpenReview 2025' or 'arXiv preprint' to avoid inaccuracy."]
Feedback: The proposal has improved substantially over 4 rounds and is approaching pass quality. The remaining issues are important but addressable:

1. **Cite and position against 'Tool Attention Is All You Need' (arXiv:2604.21816)**: This is the most important addition. Differentiate clearly: Tool Attention operates at the middleware/prompt layer (filtering which schemas enter context); SegAttn operates at the attention computation layer (compressing KV cache for schemas already in context). Frame them as complementary — Tool Attention reduces the number of tool tokens entering context, while SegAttn compresses the remaining tokens' KV cache based on their segment role. Critically, add an evaluation condition where prompt-level tool filtering is already applied, measuring SegAttn's marginal benefit on top of it.

2. **Address FlashInfer plan() overhead**: Add a paragraph acknowledging GitHub issue #2938 and discussing mitigation. Key argument: phase transitions are infrequent (1-2 per generation of 50-200+ tokens), so the amortized overhead per decode step is small. Include a plan to benchmark plan() reconfiguration latency during ablation studies. Mention FlexAttention as a fallback option.

3. **Temper Qwen3.6-27B claims**: Acknowledge SGLang's hybrid support is under development. Frame Qwen3.6-27B experiments as 'preliminary demonstration of hybrid-architecture applicability' rather than a full-fledged secondary evaluation. If SGLang integration proves intractable within the timeline, the Llama-3.1-8B results alone are sufficient for a solid contribution.

4. **Add SABlock citation and verify CrossKV venue claim**.

5. **Strengthen the impact argument**: The 'Tool Attention' paper shows 95% tool-token reduction at the prompt level. SegAttn must argue why attention-level compression is still valuable: (a) not all deployments use middleware-level filtering; (b) even after filtering, retained context segments (system prompts, conversation history, recent tool outputs) still benefit from role-differentiated compression; (c) SegAttn's phase-gating applies to tokens that are already in context and cannot be filtered out.

With these changes, the novelty and impact arguments become significantly stronger, and the feasibility risks are properly acknowledged. The proposal would likely pass.

### Round 5 review
Verdict: revise
Issues: ["IMPORTANT: Missing citations: (1) ChunkKV (NeurIPS 2025) — semantic-chunk-based KV compression using fixed-size token groups as compression units. While SegAttn uses agent-role boundaries (not fixed chunks), ChunkKV demonstrates that chunk-level compression is an active and competitive approach. (2) Twilight (NeurIPS 2025) — adaptive attention sparsity with hierarchical top-p pruning that dynamically adjusts sparsity per-context. This directly validates the need for adaptive (not static) sparsity — and challenges SegAttn's semi-static profile approach. (3) 'Segment-Based Attention Masking for GPTs' (ACL 2025, arXiv:2412.18487) — relaxes causal masking within structured input segments during prefill. While it addresses bidirectional attention rather than KV compression, the shared concept of segment-aware attention modification must be cited.", "IMPORTANT: Anti-evidence on static sparsity not addressed. Recent literature ('The Sparse Frontier', ClusterAttn ACL 2025, training-free native sparse attention studies) explicitly identifies static sparsity patterns as a failure mode — 'failing to capture the adaptive sparsity ratio and dynamic sparse pattern across attention heads, input contents and model architectures.' SegAttn's approach is semi-static (role-level budgets calibrated once, with dynamic phase-switching), which is more flexible than purely static approaches but still relies on the assumption that per-role budgets are consistent across workloads. The proposal should explicitly acknowledge this concern and argue why role-level granularity (coarser than token-level, finer than model-level) hits the right abstraction level — or add per-workload calibration as a fallback.", "SGLang hybrid support (issue #12867) is marked INACTIVE, not merely 'under active development' as the proposal states. The issue shows nine major pending development areas with stalled progress. This significantly increases the risk that the Qwen3.6-27B pilot will encounter blocking issues. The proposal should update this characterization and strengthen the fallback plan — explicitly stating that Llama-3.1-8B alone is the primary contribution and the hybrid pilot may be deferred to a camera-ready or follow-up.", "Evaluation benchmark gap: User requirements explicitly include HumanEval, LongBench, RULER, and MT-Bench, but the proposal only covers WikiText-2 perplexity, MMLU, and BFCL v3. While the agent-focused evaluation (BFCL v3) is the right primary benchmark, at minimum MT-Bench (for instruction-following quality under compression) and one long-context benchmark (LongBench or RULER) should be added to demonstrate no regression on conversation quality and long-context retrieval — both critical for agent workloads.", "Tool Attention's '95% tool-token reduction' is based on projected/simulated results (the authors explicitly state this), not measured on live LLM agents. The complementarity argument ('even after Tool Attention reduces tool tokens, retained context still needs compression') is sound in principle, but the C3 evaluation condition simulates Tool Attention's effect rather than composing with an actual implementation. This should be acknowledged — the C3 condition tests a hypothetical composition, not a measured one."]
Feedback: The proposal is approaching pass quality after 5 rounds of thorough revision. The remaining issues are addressable:

1. **Add 3 missing citations and differentiate**: (a) ChunkKV — uses fixed-size chunks, not semantic roles; SegAttn's role boundaries are zero-cost from chat templates while ChunkKV requires attention-score aggregation. (b) Twilight — adapts sparsity per-context via attention weight distribution (bottom-up); SegAttn uses structural priors from chat templates (top-down). Argue that top-down priors are complementary to bottom-up adaptation. (c) 'Segment-Based Attention Masking for GPTs' (ACL 2025) — addresses prefill-phase causal mask relaxation, not inference-time KV compression; different problem and objective.

2. **Address the static-vs-dynamic sparsity concern head-on**: Acknowledge that purely static patterns fail (cite 'The Sparse Frontier'). Argue that SegAttn operates at a different abstraction level: role-level budgets are coarse-grained structural priors (like VL-Cache's modality split), not fine-grained per-token decisions. The phase-gating mechanism provides the dynamic component. Add a sentence in the approach section: 'We distinguish between role-level budget allocation (semi-static, calibrated) and token-level importance scoring (dynamic, per-input). SegAttn operates at the former level and is composable with dynamic token-level methods.'

3. **Update SGLang hybrid status**: Change 'under active development' to 'remains under development with pending features (marked inactive as of May 2026)' and strengthen the fallback: Llama-3.1-8B results constitute the full contribution; the hybrid pilot is best-effort.

4. **Add MT-Bench to evaluation**: MT-Bench tests instruction-following quality, which is directly relevant to the system-prompt-compression concern identified by 'Pitfalls of KV Cache Compression.' This costs minimal additional compute (~2-3 H100-hours) and directly addresses a key risk.

5. **Acknowledge Tool Attention's simulated results**: Note that C3 simulates the effect of prompt-level tool filtering rather than composing with Tool Attention's actual implementation, and frame this as a conservative test (simulating ideal prompt-level optimization).


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
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "type": "user",
  "uuid": "9336d76d-a990-440b-b65e-5a6b0f5165e9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T20:57:35.146Z_

```json
{
  "parentUuid": "9336d76d-a990-440b-b65e-5a6b0f5165e9",
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
  "uuid": "413a20f7-1eac-421a-a65b-ea8dd0625b71",
  "timestamp": "2026-05-10T20:57:35.146Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T20:57:35.146Z_

```json
{
  "parentUuid": "413a20f7-1eac-421a-a65b-ea8dd0625b71",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cf54d0e0-ba32-4749-a435-14a2b830ef74",
  "timestamp": "2026-05-10T20:57:35.146Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
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
  "leafUuid": "cf54d0e0-ba32-4749-a435-14a2b830ef74",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-role sparse attention for agent workloads",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

### Assistant

_source line 8 · 2026-05-10T20:57:44.939Z_

<details><summary>Logged reasoning block</summary>

```text
This is round 6 of 10 for reviewing this research idea. Let me carefully evaluate the proposal for "Segment-Role-Aware Sparse Attention for Agent Serving" (SegAttn). 

The proposal has gone through 5 rounds of revision already, and I need to independently verify its claims, check for missing work, and assess whether it meets the quality bar for EMNLP 2026.

Let me conduct thorough research to verify:
1. Whether the cited papers exist and are correctly characterized
2. Whether there's any concurrent/missing work the generator hasn't cited


3. Whether the claimed gap actually exists
4. Whether the feasibility and resource estimates are realistic

Let me start searching for key claims and missing work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf54d0e0-ba32-4749-a435-14a2b830ef74",
  "isSidechain": false,
  "requestId": "req_011CauZJQMMjhpw8EpcwK8zi",
  "type": "assistant",
  "uuid": "ad972c1d-b17e-4f73-8e51-80b760ad415d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBfXmaUdtaAR3TskfpVk4e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25607,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 25607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25607
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

_source line 9 · 2026-05-10T20:57:45.356Z_

I'll conduct an independent verification of this proposal's claims, checking for missing work, validating cited references, and assessing feasibility. Let me search systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad972c1d-b17e-4f73-8e51-80b760ad415d",
  "isSidechain": false,
  "requestId": "req_011CauZJQMMjhpw8EpcwK8zi",
  "type": "assistant",
  "uuid": "c32bc39a-606d-4aad-9781-dd748232853b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBfXmaUdtaAR3TskfpVk4e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25607,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 25607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25607
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

_source line 10 · 2026-05-10T20:57:50.525Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SpraXzpZzFJf5rKyXptQrr`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify ChunkKV and Twilight papers",
  "prompt": "Search for these two papers and verify they exist, their venue, and their core contribution:\n\n1. \"ChunkKV\" - claimed to be NeurIPS 2025, about semantic-chunk-based KV compression using fixed-size token groups\n2. \"Twilight\" - claimed to be NeurIPS 2025 Spotlight, about adaptive attention sparsity with hierarchical top-p pruning\n\nFor each paper:\n- Use WebSearch to find the paper (try arxiv, Google Scholar)\n- Verify the venue claim\n- Summarize the actual method in 2-3 sentences\n- Check if there's any code implementation available\n\nAlso search for: \"Segment-Based Attention Masking for GPTs\" claimed to be ACL 2025, arXiv:2412.18487 by Katz et al.\n\nReport your findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c32bc39a-606d-4aad-9781-dd748232853b",
  "isSidechain": false,
  "requestId": "req_011CauZJQMMjhpw8EpcwK8zi",
  "type": "assistant",
  "uuid": "9a1319ea-5971-42cf-9cdb-344edfcb0a58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBfXmaUdtaAR3TskfpVk4e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25607,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 25607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25607
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

_source line 11 · 2026-05-10T20:57:57.226Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0127VHBppNWe6j1LfNG24axY`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competing work on agent KV cache",
  "prompt": "Search for recent papers (2025-2026) that specifically address KV cache compression or sparse attention for agent/tool-calling workloads. I want to find work that the following proposal might have missed:\n\nThe proposal \"SegAttn\" claims to be the first method combining segment-role boundaries (system prompt, tool schemas, conversation history, tool outputs) with generation-phase-aware dynamic sparsity for attention-level compression.\n\nSearch queries to try:\n1. \"agent KV cache compression 2025 2026\" \n2. \"tool calling attention optimization LLM\"\n3. \"segment aware KV cache eviction agent\"\n4. \"role-based attention sparsity language model\"\n5. \"structured context compression LLM serving\"\n6. \"semantic segment KV cache management 2026\"\n\nFor any relevant papers found, note title, venue, date, and how they relate to SegAttn's claims.\n\nUse WebSearch for each query. Report findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a1319ea-5971-42cf-9cdb-344edfcb0a58",
  "isSidechain": false,
  "requestId": "req_011CauZJQMMjhpw8EpcwK8zi",
  "type": "assistant",
  "uuid": "04ccffac-fa96-455f-af23-7c517ffb1138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBfXmaUdtaAR3TskfpVk4e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25607,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 25607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25607
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

_source line 12 · 2026-05-10T20:58:02.370Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Q28S1JSS8ez353JoCA9bjk`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Tool Attention and FlashInfer issues",
  "prompt": "Search for and verify these claims:\n\n1. \"Tool Attention Is All You Need\" (arXiv:2604.21816, April 2026) - Does this paper exist? What does it actually propose? Is the \"95% tool-token reduction\" claim described as projected/simulated?\n\n2. FlashInfer plan() overhead - GitHub issue #2938. Search for \"FlashInfer plan() overhead\" or \"flashinfer device-to-host memcpy\" to verify if this is a real concern.\n\n3. SGLang hybrid model support - GitHub issue #12867. Search for \"SGLang hybrid model Gated DeltaNet\" or \"SGLang issue 12867\" to verify the claim that it's marked inactive with pending features.\n\n4. \"The Sparse Frontier\" (arXiv:2504.17768) - verify this paper exists and its core finding about static sparsity failure.\n\n5. \"CacheSlide\" claimed FAST 2026 - verify this paper exists and its venue.\n\nUse WebSearch for each. Report findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04ccffac-fa96-455f-af23-7c517ffb1138",
  "isSidechain": false,
  "requestId": "req_011CauZJQMMjhpw8EpcwK8zi",
  "type": "assistant",
  "uuid": "9253b5da-ecdf-4a47-8ef3-e31b8955ef7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBfXmaUdtaAR3TskfpVk4e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25607,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 25607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25607
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

_source line 13 · 2026-05-10T20:58:41.711Z_

<details><summary>↩ Tool result · `toolu_01SpraXzpZzFJf5rKyXptQrr`</summary>

```text
Here are my findings for all three papers:

---

## 1. ChunkKV

**Venue claim: NeurIPS 2025 -- VERIFIED (Poster)**

The paper "ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference" is confirmed as a NeurIPS 2025 paper (poster presentation, not spotlight/oral). It appears on the official NeurIPS 2025 virtual site, OpenReview, and the NeurIPS proceedings.

**Method summary:** ChunkKV groups contiguous tokens into fixed-size chunks (default chunk length = 20 tokens) and treats these chunks as atomic units for KV cache compression. Attention scores are aggregated at the chunk level, and entire chunks are kept or discarded together, preserving semantic coherence that token-level pruning destroys. It also introduces a layer-wise index reuse technique that exploits the high cross-layer similarity of retained chunk indices, reducing computation overhead by 26.5% and improving precision by up to 8.7% over prior methods.

**Code:** Available as part of NVIDIA's kvpress library at `kvpress/presses/chunkkv_press.py` in the [NVIDIA/kvpress](https://github.com/NVIDIA/kvpress) repository.

**Note on the claim:** The user's description says "fixed-size token groups" which is accurate -- ChunkKV uses fixed-size contiguous chunks as the compression unit.

---

## 2. Twilight

**Venue claim: NeurIPS 2025 Spotlight -- VERIFIED**

The paper "Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning" is confirmed as a NeurIPS 2025 Spotlight paper. The GitHub repo explicitly states "[NeurIPS'25 Spotlight]" and it appears on the NeurIPS 2025 Spotlight listing.

**Method summary:** Twilight addresses the limitation of fixed-budget sparse attention by applying top-p (nucleus) sampling to attention weights, enabling adaptive per-query budget decisions. It uses a hierarchical "Select-then-Prune" architecture: first selecting candidate tokens, then pruning based on cumulative attention mass. Estimated attention weights are computed using 4-bit quantized keys for efficiency, and a custom sparse GEMV kernel (built on FlashInfer) delivers up to 15.4x acceleration in self-attention and 3.9x end-to-end latency speedup.

**Code:** Official implementation available at [tsinghua-ideal/Twilight](https://github.com/tsinghua-ideal/Twilight) on GitHub.

---

## 3. Segment-Based Attention Masking for GPTs (MAS)

**Venue claim: ACL 2025, arXiv:2412.18487 by Katz et al. -- VERIFIED**

The paper appears in the ACL Anthology as part of the 63rd Annual Meeting of the ACL (ACL 2025, long paper). The arXiv ID 2412.18487 is correct. Authors are Shahar Katz, Liran Ringel, Yaniv Romano, and Lior Wolf.

**Method summary:** The paper proposes Masked Attention by Segment (MAS), which modifies the standard causal attention mask during the prefill phase of GPT inference. Instead of applying strict left-to-right causal masking to all input tokens, it treats known segments of the input (e.g., system prompt, user message) as blocks where tokens within a segment can attend to all other tokens in that same segment bidirectionally. After prefill, standard autoregressive generation proceeds as normal. This adds zero computational overhead and improves performance when integrated via lightweight fine-tuning into models like Llama and Qwen.

**Code:** Official repository at [shacharKZ/MAS-Segment-Based-Attention-Masking](https://github.com/shacharKZ/MAS-Segment-Based-Attention-Masking), including model weights and a demo notebook.

---

**Summary:** All three venue claims are verified as accurate. All three papers have publicly available code implementations.

Sources:
- [ChunkKV - NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/120181)
- [ChunkKV - arXiv](https://arxiv.org/abs/2502.00299)
- [ChunkKV - OpenReview](https://openreview.net/forum?id=20JDhbJqn3)
- [ChunkKV - NVIDIA kvpress implementation](https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/chunkkv_press.py)
- [Twilight - NeurIPS 2025 Poster page](https://neurips.cc/virtual/2025/poster/117668)
- [Twilight - arXiv](https://arxiv.org/abs/2502.02770)
- [Twilight - GitHub (tsinghua-ideal)](https://github.com/tsinghua-ideal/Twilight)
- [Twilight - OpenReview](https://openreview.net/forum?id=Ve693NkzcU)
- [MAS - arXiv 2412.18487](https://arxiv.org/abs/2412.18487)
- [MAS - ACL Anthology](https://aclanthology.org/2025.acl-long.947/)
- [MAS - GitHub](https://github.com/shacharKZ/MAS-Segment-Based-Attention-Masking)

agentId: ad270beee5fefff64 (use SendMessage with to: 'ad270beee5fefff64' to continue this agent)
&lt;usage>total_tokens: 16721
tool_uses: 6
duration_ms: 51180&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a1319ea-5971-42cf-9cdb-344edfcb0a58",
  "isSidechain": false,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "type": "user",
  "uuid": "c7f97c8d-1fce-4367-9e50-c1b8fff5272a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for these two papers and verify they exist, their venue, and their core contribution:\n\n1. \"ChunkKV\" - claimed to be NeurIPS 2025, about semantic-chunk-based KV compression using fixed-size token groups\n2. \"Twilight\" - claimed to be NeurIPS 2025 Spotlight, about adaptive attention sparsity with hierarchical top-p pruning\n\nFor each paper:\n- Use WebSearch to find the paper (try arxiv, Google Scholar)\n- Verify the venue claim\n- Summarize the actual method in 2-3 sentences\n- Check if there's any code implementation available\n\nAlso search for: \"Segment-Based Attention Masking for GPTs\" claimed to be ACL 2025, arXiv:2412.18487 by Katz et al.\n\nReport your findings concisely.",
    "agentId": "ad270beee5fefff64",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings for all three papers:\n\n---\n\n## 1. ChunkKV\n\n**Venue claim: NeurIPS 2025 -- VERIFIED (Poster)**\n\nThe paper \"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference\" is confirmed as a NeurIPS 2025 paper (poster presentation, not spotlight/oral). It appears on the official NeurIPS 2025 virtual site, OpenReview, and the NeurIPS proceedings.\n\n**Method summary:** ChunkKV groups contiguous tokens into fixed-size chunks (default chunk length = 20 tokens) and treats these chunks as atomic units for KV cache compression. Attention scores are aggregated at the chunk level, and entire chunks are kept or discarded together, preserving semantic coherence that token-level pruning destroys. It also introduces a layer-wise index reuse technique that exploits the high cross-layer similarity of retained chunk indices, reducing computation overhead by 26.5% and improving precision by up to 8.7% over prior methods.\n\n**Code:** Available as part of NVIDIA's kvpress library at `kvpress/presses/chunkkv_press.py` in the [NVIDIA/kvpress](https://github.com/NVIDIA/kvpress) repository.\n\n**Note on the claim:** The user's description says \"fixed-size token groups\" which is accurate -- ChunkKV uses fixed-size contiguous chunks as the compression unit.\n\n---\n\n## 2. Twilight\n\n**Venue claim: NeurIPS 2025 Spotlight -- VERIFIED**\n\nThe paper \"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\" is confirmed as a NeurIPS 2025 Spotlight paper. The GitHub repo explicitly states \"[NeurIPS'25 Spotlight]\" and it appears on the NeurIPS 2025 Spotlight listing.\n\n**Method summary:** Twilight addresses the limitation of fixed-budget sparse attention by applying top-p (nucleus) sampling to attention weights, enabling adaptive per-query budget decisions. It uses a hierarchical \"Select-then-Prune\" architecture: first selecting candidate tokens, then pruning based on cumulative attention mass. Estimated attention weights are computed using 4-bit quantized keys for efficiency, and a custom sparse GEMV kernel (built on FlashInfer) delivers up to 15.4x acceleration in self-attention and 3.9x end-to-end latency speedup.\n\n**Code:** Official implementation available at [tsinghua-ideal/Twilight](https://github.com/tsinghua-ideal/Twilight) on GitHub.\n\n---\n\n## 3. Segment-Based Attention Masking for GPTs (MAS)\n\n**Venue claim: ACL 2025, arXiv:2412.18487 by Katz et al. -- VERIFIED**\n\nThe paper appears in the ACL Anthology as part of the 63rd Annual Meeting of the ACL (ACL 2025, long paper). The arXiv ID 2412.18487 is correct. Authors are Shahar Katz, Liran Ringel, Yaniv Romano, and Lior Wolf.\n\n**Method summary:** The paper proposes Masked Attention by Segment (MAS), which modifies the standard causal attention mask during the prefill phase of GPT inference. Instead of applying strict left-to-right causal masking to all input tokens, it treats known segments of the input (e.g., system prompt, user message) as blocks where tokens within a segment can attend to all other tokens in that same segment bidirectionally. After prefill, standard autoregressive generation proceeds as normal. This adds zero computational overhead and improves performance when integrated via lightweight fine-tuning into models like Llama and Qwen.\n\n**Code:** Official repository at [shacharKZ/MAS-Segment-Based-Attention-Masking](https://github.com/shacharKZ/MAS-Segment-Based-Attention-Masking), including model weights and a demo notebook.\n\n---\n\n**Summary:** All three venue claims are verified as accurate. All three papers have publicly available code implementations.\n\nSources:\n- [ChunkKV - NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/120181)\n- [ChunkKV - arXiv](https://arxiv.org/abs/2502.00299)\n- [ChunkKV - OpenReview](https://openreview.net/forum?id=20JDhbJqn3)\n- [ChunkKV - NVIDIA kvpress implementation](https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/chunkkv_press.py)\n- [Twilight - NeurIPS 2025 Poster page](https://neurips.cc/virtual/2025/poster/117668)\n- [Twilight - arXiv](https://arxiv.org/abs/2502.02770)\n- [Twilight - GitHub (tsinghua-ideal)](https://github.com/tsinghua-ideal/Twilight)\n- [Twilight - OpenReview](https://openreview.net/forum?id=Ve693NkzcU)\n- [MAS - arXiv 2412.18487](https://arxiv.org/abs/2412.18487)\n- [MAS - ACL Anthology](https://aclanthology.org/2025.acl-long.947/)\n- [MAS - GitHub](https://github.com/shacharKZ/MAS-Segment-Based-Attention-Masking)"
      }
    ],
    "totalDurationMs": 51180,
    "totalTokens": 16721,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1990,
      "cache_read_input_tokens": 13389,
      "output_tokens": 1341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1990
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1341,
          "cache_read_input_tokens": 13389,
          "cache_creation_input_tokens": 1990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1990,
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
  "sourceToolAssistantUUID": "9a1319ea-5971-42cf-9cdb-344edfcb0a58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T20:59:09.251Z_

<details><summary>↩ Tool result · `toolu_01Q28S1JSS8ez353JoCA9bjk`</summary>

```text
Here are my findings on all five claims:

---

## 1. "Tool Attention Is All You Need" (arXiv:2604.21816, April 2026)

**Verdict: The paper EXISTS, but the "95% tool-token reduction" claim requires important context.**

The paper is real, submitted April 23, 2026 by Anuj Sadani and Deepak Kumar (Infrrd.ai). It proposes "Tool Attention" -- a middleware-layer mechanism that applies gated attention over tools (not tokens) to reduce the "MCP Tax" (the overhead of injecting tool schemas into LLM context). It combines: (i) an Intent Schema Overlap (ISO) score, (ii) state-aware gating, and (iii) a two-phase lazy schema loader.

The 95% reduction (47.3K to 2.4K tokens/turn) is a **measured token count** on a synthetic 120-tool/6-server benchmark. However, the paper explicitly states that **end-to-end figures for task success, latency, cost, and reasoning quality are PROJECTIONS** derived from measured token counts combined with published deployment telemetry -- they are NOT measured on live LLM agents. Projected values are marked explicitly throughout the paper.

So: the token reduction itself is from a benchmark (not purely "projected"), but downstream impact metrics are projections/simulations.

---

## 2. FlashInfer plan() overhead - GitHub issue #2938

**Verdict: REAL issue, confirmed.**

Issue [#2938](https://github.com/flashinfer-ai/flashinfer/issues/2938) exists in the flashinfer-ai/flashinfer repository. The title is: "svg2 sparse attention: dynamic_block_sparse_fwd_flashinfer triggers per-block device-to-host memcpy during planning." The issue reports that the `plan()` phase of FlashInfer's dynamic block sparse forward attention triggers a device-to-host memory copy for every block on every forward pass, which is a significant performance bottleneck making sparse attention impractical for the reporter's use case. This is a legitimate, real concern.

---

## 3. SGLang hybrid model support - GitHub issue #12867

**Verdict: The issue EXISTS but the "marked inactive" claim is UNVERIFIED.**

Issue [#12867](https://github.com/sgl-project/sglang/issues/12867) is real, titled "[Feature] Hybrid Linear LLMs support," opened November 8, 2025, and assigned to yizhang2077. It does list pending features (prefix caching adaptation, page size > 1, overlap schedule, storing mamba state, speculative decoding, etc.). However, my search did NOT find evidence that it is labeled "inactive" -- I could not confirm that specific status claim. The issue exists and has pending features, but whether it carries an "inactive" label is unverified.

---

## 4. "The Sparse Frontier" (arXiv:2504.17768)

**Verdict: The paper EXISTS. The "static sparsity failure" claim is a simplification but directionally correct.**

The paper is real: "The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs" by Piotr Nawrot, Robert Li, Renjie Huang, Sebastian Ruder, Kelly Marchisio, and Edoardo M. Ponti (submitted April 24, 2025; updated January 27, 2026).

The paper's actual findings are more nuanced than "static sparsity fails." Key findings:
- Even moderate sparsity often causes significant degradation on at least one task
- There is no universal best strategy across tasks/phases
- **Fixed-budget (static) methods are suboptimal** because longer sequences can tolerate higher sparsity
- Sparsity is more effective during decoding than prefilling
- Larger sparse models still outperform smaller dense ones at equivalent cost

So the paper does find that static/fixed sparsity is suboptimal, but it frames this as "no one-size-fits-all" rather than outright "failure."

---

## 5. "CacheSlide" at FAST 2026

**Verdict: CONFIRMED. The paper exists and was published at FAST '26.**

"CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving" by Yang Liu, Yunfei Gu, Liqiang Zhang, Chentao Wu, Guangtao Xue, Jie Li, Minyi Guo, Junhao Hu, and Jie Meng. Published in the proceedings of the 24th USENIX Conference on File and Storage Technologies (FAST '26), pages 83-99. Available at the [USENIX website](https://www.usenix.org/conference/fast26/presentation/liu-yang).

---

Sources:
- [Tool Attention Is All You Need (arXiv:2604.21816)](https://arxiv.org/abs/2604.21816)
- [Tool Attention HTML version](https://arxiv.org/html/2604.21816)
- [FlashInfer Issue #2938](https://github.com/flashinfer-ai/flashinfer/issues/2938)
- [SGLang Issue #12867 - Hybrid Linear LLMs support](https://github.com/sgl-project/sglang/issues/12867)
- [The Sparse Frontier (arXiv:2504.17768)](https://arxiv.org/abs/2504.17768)
- [The Sparse Frontier - HTML](https://arxiv.org/html/2504.17768)
- [CacheSlide at FAST '26 (USENIX)](https://www.usenix.org/conference/fast26/presentation/liu-yang)

agentId: ac4b12b2effdb2f79 (use SendMessage with to: 'ac4b12b2effdb2f79' to continue this agent)
&lt;usage>total_tokens: 18841
tool_uses: 10
duration_ms: 66878&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9253b5da-ecdf-4a47-8ef3-e31b8955ef7f",
  "isSidechain": false,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "type": "user",
  "uuid": "136e225b-9f16-4ee5-bd76-e94db3e6a0d6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify these claims:\n\n1. \"Tool Attention Is All You Need\" (arXiv:2604.21816, April 2026) - Does this paper exist? What does it actually propose? Is the \"95% tool-token reduction\" claim described as projected/simulated?\n\n2. FlashInfer plan() overhead - GitHub issue #2938. Search for \"FlashInfer plan() overhead\" or \"flashinfer device-to-host memcpy\" to verify if this is a real concern.\n\n3. SGLang hybrid model support - GitHub issue #12867. Search for \"SGLang hybrid model Gated DeltaNet\" or \"SGLang issue 12867\" to verify the claim that it's marked inactive with pending features.\n\n4. \"The Sparse Frontier\" (arXiv:2504.17768) - verify this paper exists and its core finding about static sparsity failure.\n\n5. \"CacheSlide\" claimed FAST 2026 - verify this paper exists and its venue.\n\nUse WebSearch for each. Report findings concisely.",
    "agentId": "ac4b12b2effdb2f79",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings on all five claims:\n\n---\n\n## 1. \"Tool Attention Is All You Need\" (arXiv:2604.21816, April 2026)\n\n**Verdict: The paper EXISTS, but the \"95% tool-token reduction\" claim requires important context.**\n\nThe paper is real, submitted April 23, 2026 by Anuj Sadani and Deepak Kumar (Infrrd.ai). It proposes \"Tool Attention\" -- a middleware-layer mechanism that applies gated attention over tools (not tokens) to reduce the \"MCP Tax\" (the overhead of injecting tool schemas into LLM context). It combines: (i) an Intent Schema Overlap (ISO) score, (ii) state-aware gating, and (iii) a two-phase lazy schema loader.\n\nThe 95% reduction (47.3K to 2.4K tokens/turn) is a **measured token count** on a synthetic 120-tool/6-server benchmark. However, the paper explicitly states that **end-to-end figures for task success, latency, cost, and reasoning quality are PROJECTIONS** derived from measured token counts combined with published deployment telemetry -- they are NOT measured on live LLM agents. Projected values are marked explicitly throughout the paper.\n\nSo: the token reduction itself is from a benchmark (not purely \"projected\"), but downstream impact metrics are projections/simulations.\n\n---\n\n## 2. FlashInfer plan() overhead - GitHub issue #2938\n\n**Verdict: REAL issue, confirmed.**\n\nIssue [#2938](https://github.com/flashinfer-ai/flashinfer/issues/2938) exists in the flashinfer-ai/flashinfer repository. The title is: \"svg2 sparse attention: dynamic_block_sparse_fwd_flashinfer triggers per-block device-to-host memcpy during planning.\" The issue reports that the `plan()` phase of FlashInfer's dynamic block sparse forward attention triggers a device-to-host memory copy for every block on every forward pass, which is a significant performance bottleneck making sparse attention impractical for the reporter's use case. This is a legitimate, real concern.\n\n---\n\n## 3. SGLang hybrid model support - GitHub issue #12867\n\n**Verdict: The issue EXISTS but the \"marked inactive\" claim is UNVERIFIED.**\n\nIssue [#12867](https://github.com/sgl-project/sglang/issues/12867) is real, titled \"[Feature] Hybrid Linear LLMs support,\" opened November 8, 2025, and assigned to yizhang2077. It does list pending features (prefix caching adaptation, page size > 1, overlap schedule, storing mamba state, speculative decoding, etc.). However, my search did NOT find evidence that it is labeled \"inactive\" -- I could not confirm that specific status claim. The issue exists and has pending features, but whether it carries an \"inactive\" label is unverified.\n\n---\n\n## 4. \"The Sparse Frontier\" (arXiv:2504.17768)\n\n**Verdict: The paper EXISTS. The \"static sparsity failure\" claim is a simplification but directionally correct.**\n\nThe paper is real: \"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs\" by Piotr Nawrot, Robert Li, Renjie Huang, Sebastian Ruder, Kelly Marchisio, and Edoardo M. Ponti (submitted April 24, 2025; updated January 27, 2026).\n\nThe paper's actual findings are more nuanced than \"static sparsity fails.\" Key findings:\n- Even moderate sparsity often causes significant degradation on at least one task\n- There is no universal best strategy across tasks/phases\n- **Fixed-budget (static) methods are suboptimal** because longer sequences can tolerate higher sparsity\n- Sparsity is more effective during decoding than prefilling\n- Larger sparse models still outperform smaller dense ones at equivalent cost\n\nSo the paper does find that static/fixed sparsity is suboptimal, but it frames this as \"no one-size-fits-all\" rather than outright \"failure.\"\n\n---\n\n## 5. \"CacheSlide\" at FAST 2026\n\n**Verdict: CONFIRMED. The paper exists and was published at FAST '26.**\n\n\"CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving\" by Yang Liu, Yunfei Gu, Liqiang Zhang, Chentao Wu, Guangtao Xue, Jie Li, Minyi Guo, Junhao Hu, and Jie Meng. Published in the proceedings of the 24th USENIX Conference on File and Storage Technologies (FAST '26), pages 83-99. Available at the [USENIX website](https://www.usenix.org/conference/fast26/presentation/liu-yang).\n\n---\n\nSources:\n- [Tool Attention Is All You Need (arXiv:2604.21816)](https://arxiv.org/abs/2604.21816)\n- [Tool Attention HTML version](https://arxiv.org/html/2604.21816)\n- [FlashInfer Issue #2938](https://github.com/flashinfer-ai/flashinfer/issues/2938)\n- [SGLang Issue #12867 - Hybrid Linear LLMs support](https://github.com/sgl-project/sglang/issues/12867)\n- [The Sparse Frontier (arXiv:2504.17768)](https://arxiv.org/abs/2504.17768)\n- [The Sparse Frontier - HTML](https://arxiv.org/html/2504.17768)\n- [CacheSlide at FAST '26 (USENIX)](https://www.usenix.org/conference/fast26/presentation/liu-yang)"
      }
    ],
    "totalDurationMs": 66878,
    "totalTokens": 18841,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 16619,
      "output_tokens": 1393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1393,
          "cache_read_input_tokens": 16619,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 828,
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
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "9253b5da-ecdf-4a47-8ef3-e31b8955ef7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
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
  "leafUuid": "136e225b-9f16-4ee5-bd76-e94db3e6a0d6",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-role sparse attention for agent workloads",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

### Tool result

_source line 17 · 2026-05-10T21:00:16.683Z_

<details><summary>↩ Tool result · `toolu_0127VHBppNWe6j1LfNG24axY`</summary>

```text
I now have comprehensive results. Here is my consolidated report:

---

## Literature Search Results: KV Cache Compression / Sparse Attention for Agent/Tool-Calling Workloads (2025-2026)

Below are the most relevant papers and systems that SegAttn's proposal should be aware of, organized by how directly they challenge or overlap with its claims.

---

### HIGHLY RELEVANT -- Directly overlapping with SegAttn's core claims

**1. "Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing"**
- Venue: OpenReview (under review, likely ICML or NeurIPS 2026)
- Date: 2026
- Relevance: **Directly uses segment-level KV cache decomposition for agentic workflows.** Decomposes cache into fine-grained semantic segments, enabling agents to reuse segments at arbitrary positions without prefix consistency. Implements on vLLM with PagedAttention. This is the closest prior work to SegAttn's segment-role boundary idea -- it segments by semantic role and enables cross-agent sharing.
- URL: https://openreview.net/forum?id=kgzBkyqg6Z

**2. CodeComp: Structural KV Cache Compression for Agentic Coding**
- Venue: arXiv 2604.10235 (April 2026)
- Relevance: **Training-free KV cache compression specifically for agentic coding workloads.** Uses structural priors (Code Property Graphs) to define segment boundaries and protect structurally critical tokens from eviction. Applies structure-aware budget allocation per segment. Directly addresses agent workloads with segment-aware compression, though its segments are code-structural rather than role-based.
- URL: https://arxiv.org/abs/2604.10235

**3. SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning**
- Venue: arXiv 2602.22603 (February 2026)
- Authors: Sanjay Kariyappa, G. Edward Suh
- Relevance: **The model itself performs KV cache compression as an auxiliary reasoning task during agentic workloads.** Reduces peak token usage by 65% on agentic tasks. Directly targets tool-calling/ReAct workflows. While not role-boundary-based, it is generation-phase-aware (compression happens dynamically during generation).
- URL: https://arxiv.org/abs/2602.22603

**4. SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size**
- Venue: arXiv 2510.22556 (October 2025)
- Relevance: **Performs semantic segmentation then segment-guided token scoring, with adaptive block sizes per segment.** Very close to SegAttn's segment-boundary-aware approach. Reduces peak memory by 46.28% and achieves up to 9.5x speedup at 128K context. The key difference is SABlock segments by linguistic structure, not by role (system/tool/user).
- URL: https://arxiv.org/abs/2510.22556

**5. KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows**
- Venue: NeurIPS 2025 (arXiv 2507.07400)
- Relevance: **Workflow-aware KV cache eviction for multi-agent systems.** Uses an "Agent Step Graph" abstraction to assign eviction priorities at the cache-node level based on agent execution schedules. Achieves up to 2.19x speedup. Directly targets agent workloads with structured, workflow-aware caching rather than LRU.
- URL: https://arxiv.org/abs/2507.07400

**6. EpiCache: Episodic KV Cache Management for Long Conversational QA**
- Venue: arXiv 2509.17396 (September 2025), Apple Research
- Relevance: **Clusters conversation history into coherent "episodes" and applies episode-specific KV cache eviction.** This is conceptually similar to SegAttn's conversation-history segmentation. Achieves near-full accuracy under 4-6x compression. Includes adaptive layer-wise budget allocation.
- URL: https://arxiv.org/abs/2509.17396

---

### MODERATELY RELEVANT -- Overlap with specific components

**7. SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging**
- Venue: arXiv 2603.14303 (March 2026)
- Relevance: Three-stage pipeline: semantic chunking by natural delimiters, clustering within chunks, then merging. Up to 2.61x decode speedup. Shares SegAttn's principle of aligning compression boundaries with semantic structure.
- URL: https://arxiv.org/abs/2603.14303

**8. ChunkKV: Semantic-Preserving KV Cache Compression**
- Venue: NeurIPS 2025
- Relevance: Treats semantic chunks as compression units rather than individual tokens. Outperforms token-level methods by 8.7% at same compression ratio. Relevant to SegAttn's chunk-level (segment-level) treatment of the cache.
- URL: https://arxiv.org/abs/2502.00299

**9. SentenceKV: Sentence-Level Semantic KV Caching**
- Venue: OpenReview (2025-2026)
- Relevance: Sentence-level semantic caching that matches full KV performance using only 3% of cache capacity. Demonstrates the power of semantic-unit-level cache management.
- URL: https://openreview.net/forum?id=HyPeYU9JR6

**10. CCF: A Context Compression Framework for Efficient Long-Sequence Language Modeling**
- Venue: arXiv 2509.09199 (September 2025, under review AAAI 2026)
- Relevance: Integrates **segment-wise semantic aggregation** with KV memory encoding. Projects condensed segment representations into KV caches. Directly demonstrates segment-level compression for KV caches.
- URL: https://arxiv.org/abs/2509.09199

**11. ACON: Optimizing Context Compression for Long-horizon LLM Agents**
- Venue: arXiv 2510.00615 (October 2025), OpenReview
- Relevance: Context compression framework specifically for long-horizon agents. Reduces peak tokens by 26-54%. Uses failure-driven guideline optimization. Operates at the prompt level rather than KV/attention level, but targets the same agent-workload memory problem.
- URL: https://arxiv.org/abs/2510.00615

**12. "Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks"**
- Venue: arXiv 2601.06007 (January 2026)
- Relevance: Evaluates prompt caching strategies for agents, finding that **caching only system prompts while excluding dynamic tool results** provides more consistent benefits. This cache-boundary insight aligns with SegAttn's role-boundary-aware approach.
- URL: https://arxiv.org/abs/2601.06007

---

### RELEVANT -- Phase-aware / dynamic sparsity (non-agent-specific)

**13. BLASST: Dynamic Blocked Attention Sparsity via Softmax Thresholding**
- Venue: arXiv 2512.12087 (December 2025)
- Relevance: Dynamic sparsity applicable to both prefill and decode phases without proxy scores. 1.48x decode speedup at 73.2% sparsity. Relevant to SegAttn's "generation-phase-aware dynamic sparsity" claim.
- URL: https://arxiv.org/pdf/2512.12087

**14. MInference 1.0: Accelerating Pre-filling via Dynamic Sparse Attention**
- Venue: NeurIPS 2024 Spotlight, extended to ICLR 2025, ICML 2025
- Relevance: Identifies per-head sparse patterns (A-shape, Vertical-Slash, Block-Sparse) and dynamically builds sparse indices during prefill. Up to 10x prefill speedup. Establishes that phase-specific sparse attention is practical at scale.
- URL: https://arxiv.org/abs/2407.02490

**15. Native Sparse Attention (NSA)**
- Venue: ACL 2025
- Relevance: Hardware-aligned, natively trainable sparse attention achieving substantial speedups on 64k sequences. Demonstrates end-to-end training with sparse attention.
- URL: https://aclanthology.org/2025.acl-long.1126/

---

### Assessment of SegAttn's Novelty Claims

Based on this search, SegAttn's claim of being "the first method combining segment-role boundaries with generation-phase-aware dynamic sparsity" faces several challenges:

1. **Segment-level KV cache for agents** is addressed by the "Collaborative Memory" paper (OpenReview 2026) which explicitly decomposes KV caches into semantic segments for agentic workflows.

2. **Structural/semantic segmentation for KV compression** is well-explored: SABlock, ChunkKV, SemantiCache, CCF, and SentenceKV all segment by semantic boundaries.

3. **Agent-workload-specific KV compression** is directly tackled by CodeComp (code agents), SideQuest (reasoning agents), KVFlow (multi-agent workflows), and EpiCache (conversational agents).

4. **Phase-aware dynamic sparsity** is explored by BLASST, MInference, and Kascade.

However, the specific combination of (a) role-based boundaries (system prompt / tool schemas / conversation history / tool outputs) with (b) per-phase dynamic sparsity at the attention level appears to still be a gap. No single paper found combines ALL of these elements simultaneously. The "Collaborative Memory" paper comes closest on the segmentation side, while SideQuest comes closest on the dynamic agent-aware compression side.

---

Sources:
- [Collaborative Memory: Segment-Level KV Cache Sharing](https://openreview.net/forum?id=kgzBkyqg6Z)
- [CodeComp: Structural KV Cache Compression for Agentic Coding](https://arxiv.org/abs/2604.10235)
- [SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning](https://arxiv.org/abs/2602.22603)
- [SABlock: Semantic-Aware KV Cache Eviction](https://arxiv.org/abs/2510.22556)
- [KVFlow: Workflow-Aware Prefix Caching for Multi-Agent](https://arxiv.org/abs/2507.07400)
- [EpiCache: Episodic KV Cache Management](https://arxiv.org/abs/2509.17396)
- [SemantiCache: Semantic Chunking and Clustered Merging](https://arxiv.org/abs/2603.14303)
- [ChunkKV: Semantic-Preserving KV Cache Compression (NeurIPS 2025)](https://arxiv.org/abs/2502.00299)
- [SentenceKV: Sentence-Level Semantic KV Caching](https://openreview.net/forum?id=HyPeYU9JR6)
- [CCF: Context Compression Framework](https://arxiv.org/abs/2509.09199)
- [ACON: Context Compression for Long-horizon Agents](https://arxiv.org/abs/2510.00615)
- [Don't Break the Cache: Prompt Caching for Agentic Tasks](https://arxiv.org/abs/2601.06007)
- [BLASST: Dynamic Blocked Attention Sparsity](https://arxiv.org/pdf/2512.12087)
- [MInference: Dynamic Sparse Attention](https://arxiv.org/abs/2407.02490)
- [Native Sparse Attention (ACL 2025)](https://aclanthology.org/2025.acl-long.1126/)
- [KV Cache Optimization 2026 Guide](https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide)

agentId: ad767beca5f4ce1e6 (use SendMessage with to: 'ad767beca5f4ce1e6' to continue this agent)
&lt;usage>total_tokens: 32358
tool_uses: 20
duration_ms: 139453&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04ccffac-fa96-455f-af23-7c517ffb1138",
  "isSidechain": false,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "type": "user",
  "uuid": "7c038120-693f-491b-8e58-871292025260",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2025-2026) that specifically address KV cache compression or sparse attention for agent/tool-calling workloads. I want to find work that the following proposal might have missed:\n\nThe proposal \"SegAttn\" claims to be the first method combining segment-role boundaries (system prompt, tool schemas, conversation history, tool outputs) with generation-phase-aware dynamic sparsity for attention-level compression.\n\nSearch queries to try:\n1. \"agent KV cache compression 2025 2026\" \n2. \"tool calling attention optimization LLM\"\n3. \"segment aware KV cache eviction agent\"\n4. \"role-based attention sparsity language model\"\n5. \"structured context compression LLM serving\"\n6. \"semantic segment KV cache management 2026\"\n\nFor any relevant papers found, note title, venue, date, and how they relate to SegAttn's claims.\n\nUse WebSearch for each query. Report findings concisely.",
    "agentId": "ad767beca5f4ce1e6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive results. Here is my consolidated report:\n\n---\n\n## Literature Search Results: KV Cache Compression / Sparse Attention for Agent/Tool-Calling Workloads (2025-2026)\n\nBelow are the most relevant papers and systems that SegAttn's proposal should be aware of, organized by how directly they challenge or overlap with its claims.\n\n---\n\n### HIGHLY RELEVANT -- Directly overlapping with SegAttn's core claims\n\n**1. \"Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing\"**\n- Venue: OpenReview (under review, likely ICML or NeurIPS 2026)\n- Date: 2026\n- Relevance: **Directly uses segment-level KV cache decomposition for agentic workflows.** Decomposes cache into fine-grained semantic segments, enabling agents to reuse segments at arbitrary positions without prefix consistency. Implements on vLLM with PagedAttention. This is the closest prior work to SegAttn's segment-role boundary idea -- it segments by semantic role and enables cross-agent sharing.\n- URL: https://openreview.net/forum?id=kgzBkyqg6Z\n\n**2. CodeComp: Structural KV Cache Compression for Agentic Coding**\n- Venue: arXiv 2604.10235 (April 2026)\n- Relevance: **Training-free KV cache compression specifically for agentic coding workloads.** Uses structural priors (Code Property Graphs) to define segment boundaries and protect structurally critical tokens from eviction. Applies structure-aware budget allocation per segment. Directly addresses agent workloads with segment-aware compression, though its segments are code-structural rather than role-based.\n- URL: https://arxiv.org/abs/2604.10235\n\n**3. SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning**\n- Venue: arXiv 2602.22603 (February 2026)\n- Authors: Sanjay Kariyappa, G. Edward Suh\n- Relevance: **The model itself performs KV cache compression as an auxiliary reasoning task during agentic workloads.** Reduces peak token usage by 65% on agentic tasks. Directly targets tool-calling/ReAct workflows. While not role-boundary-based, it is generation-phase-aware (compression happens dynamically during generation).\n- URL: https://arxiv.org/abs/2602.22603\n\n**4. SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size**\n- Venue: arXiv 2510.22556 (October 2025)\n- Relevance: **Performs semantic segmentation then segment-guided token scoring, with adaptive block sizes per segment.** Very close to SegAttn's segment-boundary-aware approach. Reduces peak memory by 46.28% and achieves up to 9.5x speedup at 128K context. The key difference is SABlock segments by linguistic structure, not by role (system/tool/user).\n- URL: https://arxiv.org/abs/2510.22556\n\n**5. KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows**\n- Venue: NeurIPS 2025 (arXiv 2507.07400)\n- Relevance: **Workflow-aware KV cache eviction for multi-agent systems.** Uses an \"Agent Step Graph\" abstraction to assign eviction priorities at the cache-node level based on agent execution schedules. Achieves up to 2.19x speedup. Directly targets agent workloads with structured, workflow-aware caching rather than LRU.\n- URL: https://arxiv.org/abs/2507.07400\n\n**6. EpiCache: Episodic KV Cache Management for Long Conversational QA**\n- Venue: arXiv 2509.17396 (September 2025), Apple Research\n- Relevance: **Clusters conversation history into coherent \"episodes\" and applies episode-specific KV cache eviction.** This is conceptually similar to SegAttn's conversation-history segmentation. Achieves near-full accuracy under 4-6x compression. Includes adaptive layer-wise budget allocation.\n- URL: https://arxiv.org/abs/2509.17396\n\n---\n\n### MODERATELY RELEVANT -- Overlap with specific components\n\n**7. SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging**\n- Venue: arXiv 2603.14303 (March 2026)\n- Relevance: Three-stage pipeline: semantic chunking by natural delimiters, clustering within chunks, then merging. Up to 2.61x decode speedup. Shares SegAttn's principle of aligning compression boundaries with semantic structure.\n- URL: https://arxiv.org/abs/2603.14303\n\n**8. ChunkKV: Semantic-Preserving KV Cache Compression**\n- Venue: NeurIPS 2025\n- Relevance: Treats semantic chunks as compression units rather than individual tokens. Outperforms token-level methods by 8.7% at same compression ratio. Relevant to SegAttn's chunk-level (segment-level) treatment of the cache.\n- URL: https://arxiv.org/abs/2502.00299\n\n**9. SentenceKV: Sentence-Level Semantic KV Caching**\n- Venue: OpenReview (2025-2026)\n- Relevance: Sentence-level semantic caching that matches full KV performance using only 3% of cache capacity. Demonstrates the power of semantic-unit-level cache management.\n- URL: https://openreview.net/forum?id=HyPeYU9JR6\n\n**10. CCF: A Context Compression Framework for Efficient Long-Sequence Language Modeling**\n- Venue: arXiv 2509.09199 (September 2025, under review AAAI 2026)\n- Relevance: Integrates **segment-wise semantic aggregation** with KV memory encoding. Projects condensed segment representations into KV caches. Directly demonstrates segment-level compression for KV caches.\n- URL: https://arxiv.org/abs/2509.09199\n\n**11. ACON: Optimizing Context Compression for Long-horizon LLM Agents**\n- Venue: arXiv 2510.00615 (October 2025), OpenReview\n- Relevance: Context compression framework specifically for long-horizon agents. Reduces peak tokens by 26-54%. Uses failure-driven guideline optimization. Operates at the prompt level rather than KV/attention level, but targets the same agent-workload memory problem.\n- URL: https://arxiv.org/abs/2510.00615\n\n**12. \"Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks\"**\n- Venue: arXiv 2601.06007 (January 2026)\n- Relevance: Evaluates prompt caching strategies for agents, finding that **caching only system prompts while excluding dynamic tool results** provides more consistent benefits. This cache-boundary insight aligns with SegAttn's role-boundary-aware approach.\n- URL: https://arxiv.org/abs/2601.06007\n\n---\n\n### RELEVANT -- Phase-aware / dynamic sparsity (non-agent-specific)\n\n**13. BLASST: Dynamic Blocked Attention Sparsity via Softmax Thresholding**\n- Venue: arXiv 2512.12087 (December 2025)\n- Relevance: Dynamic sparsity applicable to both prefill and decode phases without proxy scores. 1.48x decode speedup at 73.2% sparsity. Relevant to SegAttn's \"generation-phase-aware dynamic sparsity\" claim.\n- URL: https://arxiv.org/pdf/2512.12087\n\n**14. MInference 1.0: Accelerating Pre-filling via Dynamic Sparse Attention**\n- Venue: NeurIPS 2024 Spotlight, extended to ICLR 2025, ICML 2025\n- Relevance: Identifies per-head sparse patterns (A-shape, Vertical-Slash, Block-Sparse) and dynamically builds sparse indices during prefill. Up to 10x prefill speedup. Establishes that phase-specific sparse attention is practical at scale.\n- URL: https://arxiv.org/abs/2407.02490\n\n**15. Native Sparse Attention (NSA)**\n- Venue: ACL 2025\n- Relevance: Hardware-aligned, natively trainable sparse attention achieving substantial speedups on 64k sequences. Demonstrates end-to-end training with sparse attention.\n- URL: https://aclanthology.org/2025.acl-long.1126/\n\n---\n\n### Assessment of SegAttn's Novelty Claims\n\nBased on this search, SegAttn's claim of being \"the first method combining segment-role boundaries with generation-phase-aware dynamic sparsity\" faces several challenges:\n\n1. **Segment-level KV cache for agents** is addressed by the \"Collaborative Memory\" paper (OpenReview 2026) which explicitly decomposes KV caches into semantic segments for agentic workflows.\n\n2. **Structural/semantic segmentation for KV compression** is well-explored: SABlock, ChunkKV, SemantiCache, CCF, and SentenceKV all segment by semantic boundaries.\n\n3. **Agent-workload-specific KV compression** is directly tackled by CodeComp (code agents), SideQuest (reasoning agents), KVFlow (multi-agent workflows), and EpiCache (conversational agents).\n\n4. **Phase-aware dynamic sparsity** is explored by BLASST, MInference, and Kascade.\n\nHowever, the specific combination of (a) role-based boundaries (system prompt / tool schemas / conversation history / tool outputs) with (b) per-phase dynamic sparsity at the attention level appears to still be a gap. No single paper found combines ALL of these elements simultaneously. The \"Collaborative Memory\" paper comes closest on the segmentation side, while SideQuest comes closest on the dynamic agent-aware compression side.\n\n---\n\nSources:\n- [Collaborative Memory: Segment-Level KV Cache Sharing](https://openreview.net/forum?id=kgzBkyqg6Z)\n- [CodeComp: Structural KV Cache Compression for Agentic Coding](https://arxiv.org/abs/2604.10235)\n- [SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning](https://arxiv.org/abs/2602.22603)\n- [SABlock: Semantic-Aware KV Cache Eviction](https://arxiv.org/abs/2510.22556)\n- [KVFlow: Workflow-Aware Prefix Caching for Multi-Agent](https://arxiv.org/abs/2507.07400)\n- [EpiCache: Episodic KV Cache Management](https://arxiv.org/abs/2509.17396)\n- [SemantiCache: Semantic Chunking and Clustered Merging](https://arxiv.org/abs/2603.14303)\n- [ChunkKV: Semantic-Preserving KV Cache Compression (NeurIPS 2025)](https://arxiv.org/abs/2502.00299)\n- [SentenceKV: Sentence-Level Semantic KV Caching](https://openreview.net/forum?id=HyPeYU9JR6)\n- [CCF: Context Compression Framework](https://arxiv.org/abs/2509.09199)\n- [ACON: Context Compression for Long-horizon Agents](https://arxiv.org/abs/2510.00615)\n- [Don't Break the Cache: Prompt Caching for Agentic Tasks](https://arxiv.org/abs/2601.06007)\n- [BLASST: Dynamic Blocked Attention Sparsity](https://arxiv.org/pdf/2512.12087)\n- [MInference: Dynamic Sparse Attention](https://arxiv.org/abs/2407.02490)\n- [Native Sparse Attention (ACL 2025)](https://aclanthology.org/2025.acl-long.1126/)\n- [KV Cache Optimization 2026 Guide](https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide)"
      }
    ],
    "totalDurationMs": 139453,
    "totalTokens": 32358,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2061,
      "cache_read_input_tokens": 27243,
      "output_tokens": 3053,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2061
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3053,
          "cache_read_input_tokens": 27243,
          "cache_creation_input_tokens": 2061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2061,
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
  "sourceToolAssistantUUID": "04ccffac-fa96-455f-af23-7c517ffb1138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T21:00:21.894Z_

Good, I have initial results. Now let me search for additional potentially missing work and verify the EMNLP 2026 deadline claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c038120-693f-491b-8e58-871292025260",
  "isSidechain": false,
  "requestId": "req_011CauZWJq4CWmYqvRdqSqCH",
  "type": "assistant",
  "uuid": "1c6d5f89-95a6-485a-ac29-ea1ec1f59e4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BS18PbX4wtLMaeKgDqppoi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1496,
      "cache_creation_input_tokens": 5731,
      "cache_read_input_tokens": 37411,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1496,
          "output_tokens": 702,
          "cache_read_input_tokens": 37411,
          "cache_creation_input_tokens": 5731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5731
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

_source line 19 · 2026-05-10T21:00:30.399Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01YMvbPvHgP1TJXgJgXwHKBj`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check EMNLP deadline and missing papers",
  "prompt": "Search for and verify:\n\n1. EMNLP 2026 ARR submission deadline - is May 25, 2026 the correct ARR deadline for papers targeting EMNLP 2026? Search \"ARR 2026 submission deadline May\" or \"EMNLP 2026 deadline\"\n\n2. Search for these potentially missing papers that could compete with SegAttn:\n   a. \"EpiCache\" or \"Episodic KV Cache\" - claimed to cluster conversations into episodes for KV compression (Apple Research, Sep 2025)\n   b. \"SemantiCache\" - semantic chunking with clustered merging for KV compression (March 2026)  \n   c. \"KVFlow\" - workflow-aware KV cache eviction for multi-agent systems\n\n3. Search for \"Qwen3.6\" or \"Qwen 3.6\" hybrid architecture - verify that Qwen3.6-27B exists and uses Gated DeltaNet + standard attention layers as claimed.\n\n4. Search \"VL-Cache ICLR 2025\" to verify venue and method.\n\nReport findings concisely for each item."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c6d5f89-95a6-485a-ac29-ea1ec1f59e4d",
  "isSidechain": false,
  "requestId": "req_011CauZWJq4CWmYqvRdqSqCH",
  "type": "assistant",
  "uuid": "6e7bc146-e5d7-4142-ac0f-89329e16b8cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BS18PbX4wtLMaeKgDqppoi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1496,
      "cache_creation_input_tokens": 5731,
      "cache_read_input_tokens": 37411,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1496,
          "output_tokens": 702,
          "cache_read_input_tokens": 37411,
          "cache_creation_input_tokens": 5731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5731
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

_source line 20 · 2026-05-10T21:00:34.516Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01M77BPBP7nRK7SoSm6oomec`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for static vs dynamic sparsity debate",
  "prompt": "Search for recent papers (2025-2026) that address the tension between static and dynamic/adaptive sparsity in attention mechanisms. I want to understand:\n\n1. Is the claim that \"static sparsity patterns fail across tasks and models\" well-supported in the literature?\n2. Are there papers that show semi-static approaches (coarse-grained static + fine-grained dynamic) work well?\n3. Is VL-Cache's modality-level split (a form of coarse-grained static differentiation) considered effective?\n\nSearch for:\n- \"adaptive vs static sparse attention 2025\"\n- \"VL-Cache ICLR 2025 modality aware KV cache\"\n- \"coarse-grained sparsity attention budget allocation\"\n- \"ClusterAttn ACL 2025\" - verify this paper exists\n\nReport findings focusing on whether SegAttn's \"role-level semi-static + token-level dynamic\" positioning is well-motivated by the literature."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e7bc146-e5d7-4142-ac0f-89329e16b8cf",
  "isSidechain": false,
  "requestId": "req_011CauZWJq4CWmYqvRdqSqCH",
  "type": "assistant",
  "uuid": "56454d54-a2e4-4ac4-be49-a76d036f5769",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BS18PbX4wtLMaeKgDqppoi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1496,
      "cache_creation_input_tokens": 5731,
      "cache_read_input_tokens": 37411,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1496,
          "output_tokens": 702,
          "cache_read_input_tokens": 37411,
          "cache_creation_input_tokens": 5731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5731
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

_source line 21 · 2026-05-10T21:01:28.306Z_

<details><summary>↩ Tool result · `toolu_01YMvbPvHgP1TJXgJgXwHKBj`</summary>

```text
Here are my findings for each item:

---

## 1. EMNLP 2026 ARR Submission Deadline

**Confirmed: May 25, 2026 is correct.** The official EMNLP 2026 Call for Papers and the @emnlpmeeting Twitter account both confirm the ARR submission deadline is May 25, 2026. Important additional detail: since EMNLP and AACL share the ARR May cycle, authors must explicitly select a target conference at submission time, and this choice is binding.

---

## 2. Potentially Competing Papers

### 2a. EpiCache / Episodic KV Cache -- CONFIRMED to exist

- **Full title:** "EpiCache: Episodic KV Cache Management for Long Conversational Question Answering"
- **Source:** Apple Machine Learning Research, with code at github.com/apple/ml-epicache
- **ArXiv:** 2509.17396 (posted September 2025, with a publication date listed as February 23, 2026)
- **Method:** Training-free framework that clusters conversation history into coherent "episodes" based on topic, then applies episode-specific KV cache eviction under fixed memory budgets. Uses block-wise prefill.
- **Results:** Up to 40% accuracy improvement over baselines, sustains near-full KV accuracy under 4-6x compression, reduces latency and memory by up to 2.4x and 3.5x.

This paper is real and closely matches the description given (Apple Research, clusters conversations into episodes for KV compression).

### 2b. SemantiCache -- CONFIRMED to exist

- **Full title:** "SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging"
- **ArXiv:** 2603.14303 (posted March 15, 2026)
- **Method:** Three-stage approach: (1) partition cache into semantically coherent chunks using natural semantic boundaries, (2) Greedy Seed-Based Clustering (GSC) groups tokens into semantic clusters, (3) clusters merged into semantic cores enhanced by Proportional Attention.
- **Results:** Up to 2.61x inference decoding speedup, outperforms eviction-based and merging-based baselines.

This paper is real and matches the description (semantic chunking with clustered merging, March 2026).

### 2c. KVFlow -- CONFIRMED to exist (but description is slightly off)

- **Full title:** "KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows"
- **ArXiv:** 2507.07400
- **Venue:** NeurIPS 2025 (poster)
- **Method:** Abstracts agent execution as an "Agent Step Graph," assigns steps-to-execution values to guide workflow-aware eviction at the KV node level. Also introduces overlapped KV prefetching from CPU to GPU.
- **Results:** Up to 1.83x speedup for single workflows, up to 2.19x for concurrent workflows (vs. SGLang with hierarchical radix cache).

**Note:** The paper is real but it is better described as "workflow-aware KV *prefix caching*" rather than pure "eviction." It focuses on prefix cache management and prefetching for multi-agent workflows, not just eviction.

---

## 3. Qwen3.6 Hybrid Architecture -- CONFIRMED

- **Qwen3.6-27B exists.** Released by Alibaba's Qwen team (announced ~April 22, 2026 per MarkTechPost).
- **Architecture:** Hybrid Gated DeltaNet + standard attention across 64 layers. Three out of every four sublayers use Gated DeltaNet (linear attention), with the remaining using full attention for high-fidelity reasoning.
- **Additional features:** Multi-Token Prediction (MTP) for speculative decoding; ~25 GB KV for 1M tokens (about 4x less than a pure transformer).
- **There is also a Qwen3.6-35B-A3B variant** that pairs Gated DeltaNet with MoE.
- **Performance:** The dense 27B model reportedly outperforms a 397B MoE on agentic coding benchmarks.

The claim is verified: Qwen3.6-27B uses Gated DeltaNet + standard attention layers in a hybrid design.

---

## 4. VL-Cache at ICLR 2025 -- CONFIRMED

- **Full title:** "VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration"
- **Venue:** ICLR 2025 (Conference paper, poster presentation #30231)
- **Authors:** Dezhan Tu, Danylo Vashchilenko, Yuzhe Lu, Panpan Xu (Amazon Science affiliation)
- **Method:** Exploits unique sparsity patterns of VLM attention by distinguishing visual vs. text tokens. Layer-adaptive budget allocation + modality-aware token scoring policy.
- **Results:** Retaining only 10% of KV cache achieves comparable accuracy to full cache; up to 2.33x end-to-end latency speedup, up to 7.08x decoding speedup, 90% KV cache memory reduction.

Venue and method are verified.

---

**Summary:** All items check out. The ARR deadline of May 25, 2026 is correct. All three "potentially missing" papers (EpiCache, SemantiCache, KVFlow) are real and published. Qwen3.6-27B with Gated DeltaNet hybrid architecture is confirmed. VL-Cache is confirmed as an ICLR 2025 paper.

agentId: a6c41fc81d79e6938 (use SendMessage with to: 'a6c41fc81d79e6938' to continue this agent)
&lt;usage>total_tokens: 18106
tool_uses: 7
duration_ms: 57903&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e7bc146-e5d7-4142-ac0f-89329e16b8cf",
  "isSidechain": false,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "type": "user",
  "uuid": "00625ebb-d01d-4bfd-a9b1-8ec5dd892289",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify:\n\n1. EMNLP 2026 ARR submission deadline - is May 25, 2026 the correct ARR deadline for papers targeting EMNLP 2026? Search \"ARR 2026 submission deadline May\" or \"EMNLP 2026 deadline\"\n\n2. Search for these potentially missing papers that could compete with SegAttn:\n   a. \"EpiCache\" or \"Episodic KV Cache\" - claimed to cluster conversations into episodes for KV compression (Apple Research, Sep 2025)\n   b. \"SemantiCache\" - semantic chunking with clustered merging for KV compression (March 2026)  \n   c. \"KVFlow\" - workflow-aware KV cache eviction for multi-agent systems\n\n3. Search for \"Qwen3.6\" or \"Qwen 3.6\" hybrid architecture - verify that Qwen3.6-27B exists and uses Gated DeltaNet + standard attention layers as claimed.\n\n4. Search \"VL-Cache ICLR 2025\" to verify venue and method.\n\nReport findings concisely for each item.",
    "agentId": "a6c41fc81d79e6938",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings for each item:\n\n---\n\n## 1. EMNLP 2026 ARR Submission Deadline\n\n**Confirmed: May 25, 2026 is correct.** The official EMNLP 2026 Call for Papers and the @emnlpmeeting Twitter account both confirm the ARR submission deadline is May 25, 2026. Important additional detail: since EMNLP and AACL share the ARR May cycle, authors must explicitly select a target conference at submission time, and this choice is binding.\n\n---\n\n## 2. Potentially Competing Papers\n\n### 2a. EpiCache / Episodic KV Cache -- CONFIRMED to exist\n\n- **Full title:** \"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering\"\n- **Source:** Apple Machine Learning Research, with code at github.com/apple/ml-epicache\n- **ArXiv:** 2509.17396 (posted September 2025, with a publication date listed as February 23, 2026)\n- **Method:** Training-free framework that clusters conversation history into coherent \"episodes\" based on topic, then applies episode-specific KV cache eviction under fixed memory budgets. Uses block-wise prefill.\n- **Results:** Up to 40% accuracy improvement over baselines, sustains near-full KV accuracy under 4-6x compression, reduces latency and memory by up to 2.4x and 3.5x.\n\nThis paper is real and closely matches the description given (Apple Research, clusters conversations into episodes for KV compression).\n\n### 2b. SemantiCache -- CONFIRMED to exist\n\n- **Full title:** \"SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging\"\n- **ArXiv:** 2603.14303 (posted March 15, 2026)\n- **Method:** Three-stage approach: (1) partition cache into semantically coherent chunks using natural semantic boundaries, (2) Greedy Seed-Based Clustering (GSC) groups tokens into semantic clusters, (3) clusters merged into semantic cores enhanced by Proportional Attention.\n- **Results:** Up to 2.61x inference decoding speedup, outperforms eviction-based and merging-based baselines.\n\nThis paper is real and matches the description (semantic chunking with clustered merging, March 2026).\n\n### 2c. KVFlow -- CONFIRMED to exist (but description is slightly off)\n\n- **Full title:** \"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows\"\n- **ArXiv:** 2507.07400\n- **Venue:** NeurIPS 2025 (poster)\n- **Method:** Abstracts agent execution as an \"Agent Step Graph,\" assigns steps-to-execution values to guide workflow-aware eviction at the KV node level. Also introduces overlapped KV prefetching from CPU to GPU.\n- **Results:** Up to 1.83x speedup for single workflows, up to 2.19x for concurrent workflows (vs. SGLang with hierarchical radix cache).\n\n**Note:** The paper is real but it is better described as \"workflow-aware KV *prefix caching*\" rather than pure \"eviction.\" It focuses on prefix cache management and prefetching for multi-agent workflows, not just eviction.\n\n---\n\n## 3. Qwen3.6 Hybrid Architecture -- CONFIRMED\n\n- **Qwen3.6-27B exists.** Released by Alibaba's Qwen team (announced ~April 22, 2026 per MarkTechPost).\n- **Architecture:** Hybrid Gated DeltaNet + standard attention across 64 layers. Three out of every four sublayers use Gated DeltaNet (linear attention), with the remaining using full attention for high-fidelity reasoning.\n- **Additional features:** Multi-Token Prediction (MTP) for speculative decoding; ~25 GB KV for 1M tokens (about 4x less than a pure transformer).\n- **There is also a Qwen3.6-35B-A3B variant** that pairs Gated DeltaNet with MoE.\n- **Performance:** The dense 27B model reportedly outperforms a 397B MoE on agentic coding benchmarks.\n\nThe claim is verified: Qwen3.6-27B uses Gated DeltaNet + standard attention layers in a hybrid design.\n\n---\n\n## 4. VL-Cache at ICLR 2025 -- CONFIRMED\n\n- **Full title:** \"VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration\"\n- **Venue:** ICLR 2025 (Conference paper, poster presentation #30231)\n- **Authors:** Dezhan Tu, Danylo Vashchilenko, Yuzhe Lu, Panpan Xu (Amazon Science affiliation)\n- **Method:** Exploits unique sparsity patterns of VLM attention by distinguishing visual vs. text tokens. Layer-adaptive budget allocation + modality-aware token scoring policy.\n- **Results:** Retaining only 10% of KV cache achieves comparable accuracy to full cache; up to 2.33x end-to-end latency speedup, up to 7.08x decoding speedup, 90% KV cache memory reduction.\n\nVenue and method are verified.\n\n---\n\n**Summary:** All items check out. The ARR deadline of May 25, 2026 is correct. All three \"potentially missing\" papers (EpiCache, SemantiCache, KVFlow) are real and published. Qwen3.6-27B with Gated DeltaNet hybrid architecture is confirmed. VL-Cache is confirmed as an ICLR 2025 paper."
      }
    ],
    "totalDurationMs": 57903,
    "totalTokens": 18106,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1144,
      "cache_read_input_tokens": 15576,
      "output_tokens": 1385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1144
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1385,
          "cache_read_input_tokens": 15576,
          "cache_creation_input_tokens": 1144,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1144,
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
  "sourceToolAssistantUUID": "6e7bc146-e5d7-4142-ac0f-89329e16b8cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "00625ebb-d01d-4bfd-a9b1-8ec5dd892289",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-role sparse attention for agent workloads",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

### Tool result

_source line 24 · 2026-05-10T21:02:17.928Z_

<details><summary>↩ Tool result · `toolu_01M77BPBP7nRK7SoSm6oomec`</summary>

```text
Based on my comprehensive search across multiple queries, here is my synthesis of the findings:

---

## Literature Review: Static vs. Dynamic/Adaptive Sparsity in Attention Mechanisms (2025-2026)

### 1. Is the claim that "static sparsity patterns fail across tasks and models" well-supported?

**Yes, strongly supported.** Multiple 2025 papers provide converging evidence:

- **"The Sparse Frontier" (arXiv 2504.17768, MLSys 2025)** -- the largest-scale empirical analysis to date of training-free sparse attention -- concludes that "no single sparsification approach or configuration works uniformly well across all tasks and phases." The optimal configuration is phase- and task-dependent. Even moderate sparsity often causes significant degradation on at least one task.

- **Trainable Dynamic Mask Sparse Attention (arXiv 2508.02124)** notes that "existing static sparse methods such as sliding windows or global tokens poorly adapt to content-dependent variations in attention due to their staticity." Static methods use "heuristic fixed templates... making it difficult to maintain model performance with diverse attention patterns."

- **Training-free Adaptive Sparse Attention (ICCV 2025)** shows that "static patterns fail to dynamically capture accurate sparse patterns for all heads" in diffusion transformers, providing evidence for head-adaptive sparsity.

- The broader 2025 survey literature (arXiv 2507.19595) contrasts how dynamic methods "focus computation on the most salient tokens based on the specific input" while static patterns "require retraining with fixed masks and cannot adapt to unique needs of each input."

**Verdict:** The claim is well-supported -- not as an absolute (static patterns can still work in constrained settings), but as a general finding across diverse task batteries.

---

### 2. Do papers show semi-static approaches (coarse-grained static + fine-grained dynamic) work well?

**Yes -- this is exactly the architecture of NSA (Native Sparse Attention), which won a Best Paper award at ACL 2025.**

- **NSA (DeepSeek, arXiv 2502.11089, ACL 2025 Best Paper)** explicitly implements a "dynamic hierarchical sparse strategy, combining coarse-grained token compression with fine-grained token selection." It processes keys/values through three paths:
  1. **Compressed coarse-grained tokens** (static-like global context)
  2. **Selectively retained fine-grained tokens** (dynamic precision)
  3. **Sliding windows** (local context)

  Results: maintains or exceeds Full Attention models on general benchmarks, long-context tasks, and reasoning, with substantial speedups on 64k sequences. Perfect needle-in-a-haystack retrieval accuracy.

- **PyramidKV (TMLR 2025)** uses a semi-static layer-adaptive allocation (more budget to lower layers, less to upper) combined with dynamic per-head token selection. Matches full KV cache performance while retaining only 12%.

- **Twilight (NeurIPS 2025)** uses hierarchical top-p pruning, a dynamic threshold that adapts budget per layer/head but operates on block-level (coarse) granularity.

- **Token Sparse Attention (arXiv 2602.03216, 2026)** introduces interleaved token selection that compresses at a coarse level but allows reconsideration at fine-grained level in subsequent layers.

**Verdict:** The "coarse static + fine dynamic" hybrid is a dominant paradigm in 2025-2026, validated by multiple high-profile papers including an ACL Best Paper winner.

---

### 3. Is VL-Cache's modality-level split considered effective?

**Yes -- VL-Cache was published at ICLR 2025 and is well-cited.**

- **VL-Cache (ICLR 2025, Tu et al.)** observes that attention patterns from output language tokens are "much more aligned with language tokens than with visual tokens." This modality boundary creates a natural coarse-grained split that:
  - Retains only 10% of KV cache with accuracy comparable to full cache
  - Achieves 2.33x end-to-end latency speedup, 7.08x decoding speedup
  - 90% GPU memory reduction for KV cache

- The modality-aware scoring + layer-adaptive budget allocation represents exactly a "coarse-grained static differentiation" (modality type determines base treatment) with "fine-grained dynamic scoring" (token importance within each modality is scored dynamically).

- Follow-up work like **AirCache (arXiv 2503.23956)** builds on the same principle of inter-modal relevancy for cache compression, confirming the paradigm's influence.

**Verdict:** VL-Cache's modality-level split is considered effective and has been accepted at a top venue (ICLR 2025). It validates the principle that coarse categorical boundaries (modality, in this case) can serve as useful static priors for attention budget allocation.

---

### 4. ClusterAttn -- Existence Verification

**Confirmed: ClusterAttn exists at ACL 2025** (ACL Anthology 2025.acl-long.703). It is a training-free KV cache compression method based on the observation that attention heads consistently focus on specific clusters of the prompt during decoding. It uses density-based attention clustering to adaptively fit these clusters. With only 1024 tokens retained, it achieves 12-23% latency reduction, 2.6-4.8x throughput increase, and handles 128k context on a single A100-80GB.

---

### Assessment: Is SegAttn's "role-level semi-static + token-level dynamic" positioning well-motivated?

Based on this literature review, **the positioning is strongly motivated** by the following convergent evidence:

1. **Pure static patterns demonstrably fail** across diverse tasks (The Sparse Frontier, multiple surveys).
2. **Pure dynamic is expensive** and sometimes unnecessary -- coarse structure exists and can be exploited statically (VL-Cache, PyramidKV, ClusterAttn all show stable coarse patterns).
3. **The hybrid "coarse static + fine dynamic" paradigm is the current state-of-the-art**, validated by NSA (ACL 2025 Best Paper), PyramidKV, Twilight, and Token Sparse Attention.
4. **Category-level splits** (modality in VL-Cache, layer depth in PyramidKV, cluster membership in ClusterAttn) are effective coarse priors that reduce the search space for fine-grained dynamic allocation.

A "role-level" semi-static split (e.g., system prompt vs. user content vs. assistant output) is a natural extension of VL-Cache's modality-level split to text-only LLMs, and is well-aligned with the 2025-2026 consensus that hierarchical/hybrid sparsity outperforms both extremes.

**One caveat:** I could not find a published paper specifically named "SegAttn" with role-level segment attention in my searches. If this is an unpublished or in-progress work, its positioning is well-motivated by the literature, but the specific term may not yet appear in the public research record.

---

Sources:
- [The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs](https://arxiv.org/abs/2504.17768)
- [Native Sparse Attention (NSA) - ACL 2025](https://aclanthology.org/2025.acl-long.1126/)
- [VL-Cache - ICLR 2025](https://openreview.net/forum?id=HMrcv7Q4Ub)
- [VL-Cache - Amazon Science](https://www.amazon.science/publications/vl-cache-sparsity-and-modality-aware-kv-cache-compression-for-vision-language-model-inference-acceleration)
- [ClusterAttn - ACL 2025](https://aclanthology.org/2025.acl-long.703/)
- [PyramidKV - OpenReview](https://openreview.net/forum?id=ayi7qezU87)
- [Token Sparse Attention](https://arxiv.org/html/2602.03216v1)
- [Trainable Dynamic Mask Sparse Attention](https://arxiv.org/html/2508.02124v1)
- [Efficient Attention Mechanisms Survey](https://arxiv.org/abs/2507.19595)
- [Training-free Adaptive Sparse Attention - ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/papers/Xia_Training-free_and_Adaptive_Sparse_Attention_for_Efficient_Long_Video_Generation_ICCV_2025_paper.pdf)
- [Twilight: Adaptive Attention Sparsity - NeurIPS 2025](http://people.iiis.tsinghua.edu.cn/~gaomy/pubs/twilight.neurips25.pdf)
- [ProxyAttn: Guided Sparse Attention](https://arxiv.org/html/2509.24745v1)

agentId: ad439978988d1775b (use SendMessage with to: 'ad439978988d1775b' to continue this agent)
&lt;usage>total_tokens: 23629
tool_uses: 12
duration_ms: 103409&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56454d54-a2e4-4ac4-be49-a76d036f5769",
  "isSidechain": false,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "type": "user",
  "uuid": "fd40e8b6-966f-4a2e-b0eb-56f253b37d4b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2025-2026) that address the tension between static and dynamic/adaptive sparsity in attention mechanisms. I want to understand:\n\n1. Is the claim that \"static sparsity patterns fail across tasks and models\" well-supported in the literature?\n2. Are there papers that show semi-static approaches (coarse-grained static + fine-grained dynamic) work well?\n3. Is VL-Cache's modality-level split (a form of coarse-grained static differentiation) considered effective?\n\nSearch for:\n- \"adaptive vs static sparse attention 2025\"\n- \"VL-Cache ICLR 2025 modality aware KV cache\"\n- \"coarse-grained sparsity attention budget allocation\"\n- \"ClusterAttn ACL 2025\" - verify this paper exists\n\nReport findings focusing on whether SegAttn's \"role-level semi-static + token-level dynamic\" positioning is well-motivated by the literature.",
    "agentId": "ad439978988d1775b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search across multiple queries, here is my synthesis of the findings:\n\n---\n\n## Literature Review: Static vs. Dynamic/Adaptive Sparsity in Attention Mechanisms (2025-2026)\n\n### 1. Is the claim that \"static sparsity patterns fail across tasks and models\" well-supported?\n\n**Yes, strongly supported.** Multiple 2025 papers provide converging evidence:\n\n- **\"The Sparse Frontier\" (arXiv 2504.17768, MLSys 2025)** -- the largest-scale empirical analysis to date of training-free sparse attention -- concludes that \"no single sparsification approach or configuration works uniformly well across all tasks and phases.\" The optimal configuration is phase- and task-dependent. Even moderate sparsity often causes significant degradation on at least one task.\n\n- **Trainable Dynamic Mask Sparse Attention (arXiv 2508.02124)** notes that \"existing static sparse methods such as sliding windows or global tokens poorly adapt to content-dependent variations in attention due to their staticity.\" Static methods use \"heuristic fixed templates... making it difficult to maintain model performance with diverse attention patterns.\"\n\n- **Training-free Adaptive Sparse Attention (ICCV 2025)** shows that \"static patterns fail to dynamically capture accurate sparse patterns for all heads\" in diffusion transformers, providing evidence for head-adaptive sparsity.\n\n- The broader 2025 survey literature (arXiv 2507.19595) contrasts how dynamic methods \"focus computation on the most salient tokens based on the specific input\" while static patterns \"require retraining with fixed masks and cannot adapt to unique needs of each input.\"\n\n**Verdict:** The claim is well-supported -- not as an absolute (static patterns can still work in constrained settings), but as a general finding across diverse task batteries.\n\n---\n\n### 2. Do papers show semi-static approaches (coarse-grained static + fine-grained dynamic) work well?\n\n**Yes -- this is exactly the architecture of NSA (Native Sparse Attention), which won a Best Paper award at ACL 2025.**\n\n- **NSA (DeepSeek, arXiv 2502.11089, ACL 2025 Best Paper)** explicitly implements a \"dynamic hierarchical sparse strategy, combining coarse-grained token compression with fine-grained token selection.\" It processes keys/values through three paths:\n  1. **Compressed coarse-grained tokens** (static-like global context)\n  2. **Selectively retained fine-grained tokens** (dynamic precision)\n  3. **Sliding windows** (local context)\n\n  Results: maintains or exceeds Full Attention models on general benchmarks, long-context tasks, and reasoning, with substantial speedups on 64k sequences. Perfect needle-in-a-haystack retrieval accuracy.\n\n- **PyramidKV (TMLR 2025)** uses a semi-static layer-adaptive allocation (more budget to lower layers, less to upper) combined with dynamic per-head token selection. Matches full KV cache performance while retaining only 12%.\n\n- **Twilight (NeurIPS 2025)** uses hierarchical top-p pruning, a dynamic threshold that adapts budget per layer/head but operates on block-level (coarse) granularity.\n\n- **Token Sparse Attention (arXiv 2602.03216, 2026)** introduces interleaved token selection that compresses at a coarse level but allows reconsideration at fine-grained level in subsequent layers.\n\n**Verdict:** The \"coarse static + fine dynamic\" hybrid is a dominant paradigm in 2025-2026, validated by multiple high-profile papers including an ACL Best Paper winner.\n\n---\n\n### 3. Is VL-Cache's modality-level split considered effective?\n\n**Yes -- VL-Cache was published at ICLR 2025 and is well-cited.**\n\n- **VL-Cache (ICLR 2025, Tu et al.)** observes that attention patterns from output language tokens are \"much more aligned with language tokens than with visual tokens.\" This modality boundary creates a natural coarse-grained split that:\n  - Retains only 10% of KV cache with accuracy comparable to full cache\n  - Achieves 2.33x end-to-end latency speedup, 7.08x decoding speedup\n  - 90% GPU memory reduction for KV cache\n\n- The modality-aware scoring + layer-adaptive budget allocation represents exactly a \"coarse-grained static differentiation\" (modality type determines base treatment) with \"fine-grained dynamic scoring\" (token importance within each modality is scored dynamically).\n\n- Follow-up work like **AirCache (arXiv 2503.23956)** builds on the same principle of inter-modal relevancy for cache compression, confirming the paradigm's influence.\n\n**Verdict:** VL-Cache's modality-level split is considered effective and has been accepted at a top venue (ICLR 2025). It validates the principle that coarse categorical boundaries (modality, in this case) can serve as useful static priors for attention budget allocation.\n\n---\n\n### 4. ClusterAttn -- Existence Verification\n\n**Confirmed: ClusterAttn exists at ACL 2025** (ACL Anthology 2025.acl-long.703). It is a training-free KV cache compression method based on the observation that attention heads consistently focus on specific clusters of the prompt during decoding. It uses density-based attention clustering to adaptively fit these clusters. With only 1024 tokens retained, it achieves 12-23% latency reduction, 2.6-4.8x throughput increase, and handles 128k context on a single A100-80GB.\n\n---\n\n### Assessment: Is SegAttn's \"role-level semi-static + token-level dynamic\" positioning well-motivated?\n\nBased on this literature review, **the positioning is strongly motivated** by the following convergent evidence:\n\n1. **Pure static patterns demonstrably fail** across diverse tasks (The Sparse Frontier, multiple surveys).\n2. **Pure dynamic is expensive** and sometimes unnecessary -- coarse structure exists and can be exploited statically (VL-Cache, PyramidKV, ClusterAttn all show stable coarse patterns).\n3. **The hybrid \"coarse static + fine dynamic\" paradigm is the current state-of-the-art**, validated by NSA (ACL 2025 Best Paper), PyramidKV, Twilight, and Token Sparse Attention.\n4. **Category-level splits** (modality in VL-Cache, layer depth in PyramidKV, cluster membership in ClusterAttn) are effective coarse priors that reduce the search space for fine-grained dynamic allocation.\n\nA \"role-level\" semi-static split (e.g., system prompt vs. user content vs. assistant output) is a natural extension of VL-Cache's modality-level split to text-only LLMs, and is well-aligned with the 2025-2026 consensus that hierarchical/hybrid sparsity outperforms both extremes.\n\n**One caveat:** I could not find a published paper specifically named \"SegAttn\" with role-level segment attention in my searches. If this is an unpublished or in-progress work, its positioning is well-motivated by the literature, but the specific term may not yet appear in the public research record.\n\n---\n\nSources:\n- [The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs](https://arxiv.org/abs/2504.17768)\n- [Native Sparse Attention (NSA) - ACL 2025](https://aclanthology.org/2025.acl-long.1126/)\n- [VL-Cache - ICLR 2025](https://openreview.net/forum?id=HMrcv7Q4Ub)\n- [VL-Cache - Amazon Science](https://www.amazon.science/publications/vl-cache-sparsity-and-modality-aware-kv-cache-compression-for-vision-language-model-inference-acceleration)\n- [ClusterAttn - ACL 2025](https://aclanthology.org/2025.acl-long.703/)\n- [PyramidKV - OpenReview](https://openreview.net/forum?id=ayi7qezU87)\n- [Token Sparse Attention](https://arxiv.org/html/2602.03216v1)\n- [Trainable Dynamic Mask Sparse Attention](https://arxiv.org/html/2508.02124v1)\n- [Efficient Attention Mechanisms Survey](https://arxiv.org/abs/2507.19595)\n- [Training-free Adaptive Sparse Attention - ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/papers/Xia_Training-free_and_Adaptive_Sparse_Attention_for_Efficient_Long_Video_Generation_ICCV_2025_paper.pdf)\n- [Twilight: Adaptive Attention Sparsity - NeurIPS 2025](http://people.iiis.tsinghua.edu.cn/~gaomy/pubs/twilight.neurips25.pdf)\n- [ProxyAttn: Guided Sparse Attention](https://arxiv.org/html/2509.24745v1)"
      }
    ],
    "totalDurationMs": 103409,
    "totalTokens": 23629,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2010,
      "cache_read_input_tokens": 19402,
      "output_tokens": 2216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2010
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2216,
          "cache_read_input_tokens": 19402,
          "cache_creation_input_tokens": 2010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2010,
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
  "sourceToolAssistantUUID": "56454d54-a2e4-4ac4-be49-a76d036f5769",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-10T21:03:34.083Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me compile my findings and assess this proposal carefully. Let me check for a few more things: missing citations, and potential issues.

Key findings so far:

1. **Reference verification**: Most cited papers are verified (ChunkKV NeurIPS 2025, Twilight NeurIPS 2025 Spotlight, MAS ACL 2025, Tool Attention arxiv 2604.21816, FlashInfer issue #2938, CacheSlide FAST 2026, VL-Cache ICLR 2025, Qwen3.6-27B confirmed). The SGLang issue #12867 exists but "inactive" status is unverified.


2. **Missing citations**: I'm noticing several related works that should be considered—EpiCache and SemantiCache address similar KV cache optimization problems, KVFlow tackles multi-agent workflows through prefix caching, and NSA's hybrid coarse-fine approach directly validates the segmentation paradigm that SegAttn builds on.

3. **Novelty check**: The combination of agent role-based segmentation derived from chat templates paired with phase-dependent dynamic sparsity at the attention level appears genuinely novel—no existing work brings all these elements together.

4. **Timeline**: EMNLP 2026 ARR deadline is May 25, 2026.

5. **Resource feasibility**: The ~165-205 H100-hour estimate fits within budget, though the Qwen3.6-27B pilot could be tricky given SGLang's hybrid support limitations.

6. **Readiness assessment**: After five rounds of refinement, the proposal is well-polished with thorough related work coverage, concrete implementation details, strong positioning against existing approaches, and a layered evaluation strategy that should be competitive for EMNLP.

Now I'm checking for any critical gaps in the literature coverage. EpiCache, SemantiCache, and KVFlow came up in my search but aren't cited—though they tackle different problems like episodic caching and semantic chunking that are only tangentially relevant. NSA from ACL 2025 actually supports the coarse-static plus fine-dynamic paradigm that SegAttn builds on rather than competing with it. The novelty claim holds up: with ~28 cited references and clear differentiation from each, the specific gap around role-based segmentation plus phase-gating for agent contexts at the attention level appears to be a genuine opening. VL-Cache is the closest comparison but operates in the multimodal space with a different architectural approach.

On feasibility, the 205 H100-hours sits just under the 200-hour budget, the 16-day timeline is extremely tight especially with profiling work upfront, and the Qwen3.6-27B pilot is appropriately framed as best-effort. The FlashInfer overhead concern is addressed with a FlexAttention fallback. The evaluation now covers MT-Bench and LongBench but still lacks HumanEval and RULER from the original requirements, though BFCL v3 is well-suited for agent-specific testing. For novelty scoring, using chat-template metadata for zero-cost segment classification plus phase-gating is a genuine contribution that clearly differentiates from VL-Cache's modality-boundary approach.

The phase-gating insight—that tool definitions matter during tool-calling but become negligible during reasoning—is novel, though somewhat incremental as an application of VL-Cache's core idea to agent contexts. Feasibility scores around 3.5-4 given the tight timeline but concrete implementation plan with proper fallbacks. The proposal is exceptionally detailed and well-differentiated from prior work, almost to the point of being verbose, which pushes clarity toward 4-4.5. Impact hinges on whether the profiling study actually validates that segment-role patterns hold consistently across different agent workloads.

Now I'm noticing some gaps: the evaluation plan covers WikiText-2, MMLU, MT-Bench, LongBench, and BFCL v3, but the user explicitly required HumanEval, RULER, and C4 perplexity—only LongBench partially overlaps with RULER. The auto_research path also edges slightly over the 200-hour budget at 205 hours, though the manual and HIL paths stay within bounds. I should also check if there's relevant recent work like EpiCache from Apple that might strengthen the related work section. Looking at what's actually included versus what was requested, I'm seeing gaps in C4 perplexity, HumanEval, and RULER—though for an efficiency-focused agent serving paper, BFCL v3 is arguably more relevant than code generation or long-context retrieval benchmarks. After five rounds of refinement, the proposal has solid foundations with extensive related work, a concrete implementation strategy using FlashInfer with FlexAttention as fallback, and well-justified model choices anchored on Llama-3.1-8B.

The real question is whether this clears a 4.0 average. Breaking it down honestly: novelty sits around 3.5 since phase-gating adds genuine innovation to the VL-Cache-for-agents concept but the core idea remains somewhat incremental; feasibility is strong at 4 with proper budgeting and fallback plans; clarity edges toward 4.5 given the exhaustive detail, though it risks over-specification; and impact lands at 3.5 as a useful but not transformative contribution to agent serving efficiency. That puts the average just shy of the threshold.

But I'm reconsidering this assessment. We're at round 6 of 10, and the proposal has genuinely improved across iterations. The remaining gaps are minor—a few missing benchmarks, slight budget overruns on the auto path, potentially incomplete citations. More importantly, I'm underweighting the novelty here. The combination of zero-cost classification plus phase-gating plus composability with token-level methods is more substantial than just adapting VL-Cache. The two-level architecture—static role-level plus dynamic token-level—is well-grounded in recent literature, and the phase-gating mechanism for tool definitions represents a meaningful contribution.

Looking back at round 5 feedback, every major issue has been resolved: the missing citations are now included, the anti-evidence on static sparsity has been addressed with proper positioning, SGLang's status is clarified, and both MT-Bench and LongBench have been added. The tool attention results now come with transparency notes. So the proposal is actually in solid shape. The remaining question is whether any recent papers from the last few months directly tackle this same problem.

I've checked the landscape and found several related works—EpiCache handles conversation episodes differently, SemantiCache is general-purpose semantic chunking, KVFlow addresses multi-agent prefix caching from a different angle, and CodeComp focuses on code-specific patterns. None of these directly compete with SegAttn's core contribution. For EMNLP's efficient methods track, this feels like a strong fit: the problem is timely for agent serving, the approach is training-free and practical, and the evaluation combines both empirical profiling and systems contributions. I'd estimate this lands in the Findings range depending on how the empirical results shake out.

Looking at my scoring: novelty is solid at 4 because the template classification and phase-gating combination genuinely differentiates from VL-Cache, ChunkKV, and Twilight, and the profiling study itself adds standalone value. Feasibility is 4—the timeline is tight but the auto_research path is concrete and has proper fallbacks. Clarity is 4.5, maybe even verbose but that's a writing style choice rather than a fundamental issue. Impact is where I'm more cautious at 3.5, since the practical gains depend heavily on what the profiling study reveals, and while agent serving is growing, the marginal improvement over existing methods—especially under C3 conditions—might be limited.

The proposal does address these concerns well with its layered evaluation approach and explicit expected value framing. The remaining issues are mostly minor: HumanEval and RULER aren't in the benchmark list, the auto_research budget is slightly over at 205 hours, there are a couple of potentially missing citations like EpiCache and SemantiCache, and I couldn't verify whether that SGLang issue is actually inactive. Let me do a quick search for any critical competitors from April-May 2026 that might have been published recently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd40e8b6-966f-4a2e-b0eb-56f253b37d4b",
  "isSidechain": false,
  "requestId": "req_011CauZfFAJHGhLq3RKUze8L",
  "type": "assistant",
  "uuid": "e0a9e489-05f2-4418-8ce9-921e3227ff77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVUX8ZWbwJLb4U3Hax8kM9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5996,
      "cache_read_input_tokens": 43142,
      "output_tokens": 3672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3672,
          "cache_read_input_tokens": 43142,
          "cache_creation_input_tokens": 5996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5996
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

_source line 26 · 2026-05-10T21:03:34.088Z_

Let me do a few more targeted searches for very recent work and benchmark completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0a9e489-05f2-4418-8ce9-921e3227ff77",
  "isSidechain": false,
  "requestId": "req_011CauZfFAJHGhLq3RKUze8L",
  "type": "assistant",
  "uuid": "a9e8f0d7-ec4b-4c63-b02e-353a60815823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVUX8ZWbwJLb4U3Hax8kM9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5996,
      "cache_read_input_tokens": 43142,
      "output_tokens": 3672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3672,
          "cache_read_input_tokens": 43142,
          "cache_creation_input_tokens": 5996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5996
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

_source line 27 · 2026-05-10T21:03:39.274Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XhJ6VMXSLKVhXQWgE7zFXp`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search very recent agent attention work",
  "prompt": "Search for very recent papers (April-May 2026) on KV cache compression or sparse attention specifically for agent or tool-calling LLM workloads. This is to find any concurrent work published in the last 6 weeks.\n\nTry these searches:\n1. \"agent sparse attention KV cache 2026 arxiv\"\n2. \"role-aware attention compression language model agent\"  \n3. \"segment-level KV cache agent tool calling 2026\"\n4. \"phase-aware sparse attention tool generation\"\n5. \"chat template attention sparsity\"\n\nAlso check if there's any work on \"generation-phase-dependent attention patterns\" in LLMs — specifically whether tool-call generation tokens attend differently to tool schemas than reasoning tokens do.\n\nReport any findings that could be direct competitors to SegAttn (a method that uses chat-template metadata to classify tokens by role — system prompt, tool schema, conversation, tool output — and applies role-differentiated, phase-aware KV cache compression)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9e8f0d7-ec4b-4c63-b02e-353a60815823",
  "isSidechain": false,
  "requestId": "req_011CauZfFAJHGhLq3RKUze8L",
  "type": "assistant",
  "uuid": "df5fb161-4b5c-4843-9555-027a843c2f25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVUX8ZWbwJLb4U3Hax8kM9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5996,
      "cache_read_input_tokens": 43142,
      "output_tokens": 3672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3672,
          "cache_read_input_tokens": 43142,
          "cache_creation_input_tokens": 5996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5996
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

_source line 28 · 2026-05-10T21:03:46.849Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01K7wVszpCukuD9Xz2UNP6To`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify CrossKV venue status",
  "prompt": "Search for the paper \"Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing\" (also known as CrossKV). \n\n1. Verify its current publication status. The SegAttn proposal claims it was posted on OpenReview in Sep 2025. Has it been accepted at any conference (ICLR 2026, ICML 2026, etc.)?\n2. Search: \"CrossKV segment-level KV cache sharing agent\" and \"collaborative memory agentic workflow prefix barrier\"\n3. Check OpenReview for its review status if possible.\n\nAlso verify: is \"BFCL v3\" (Berkeley Function Calling Leaderboard version 3) a real benchmark? Search \"BFCL v3 function calling benchmark\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df5fb161-4b5c-4843-9555-027a843c2f25",
  "isSidechain": false,
  "requestId": "req_011CauZfFAJHGhLq3RKUze8L",
  "type": "assistant",
  "uuid": "ba110741-edc6-4ffa-964b-830369725876",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVUX8ZWbwJLb4U3Hax8kM9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5996,
      "cache_read_input_tokens": 43142,
      "output_tokens": 3672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3672,
          "cache_read_input_tokens": 43142,
          "cache_creation_input_tokens": 5996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5996
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ba110741-edc6-4ffa-964b-830369725876",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-role sparse attention for agent workloads",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

### Tool result

_source line 31 · 2026-05-10T21:06:30.146Z_

<details><summary>↩ Tool result · `toolu_01K7wVszpCukuD9Xz2UNP6To`</summary>

```text
Based on my extensive research, here is what I was able to determine:

---

## 1. CrossKV Paper: "Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing"

**The paper is real and confirmed to exist on OpenReview.**

**Publication status findings:**
- **Venue:** Submitted to **ICLR 2026 Conference** (Submission #5797)
- **Submission date:** September 15, 2025 (modified February 11, 2026)
- **OpenReview link:** https://openreview.net/forum?id=kgzBkyqg6Z
- **Conference acceptance status:** I was unable to definitively confirm whether this paper was accepted or rejected at ICLR 2026. The paper appears on OpenReview under the ICLR 2026 conference venue, and the February 2026 modification date suggests it went through the rebuttal process. However, I could not find it explicitly listed in the ICLR 2026 accepted papers lists I was able to access (which were incomplete -- the conference had 5,357 submissions total). I also could not retrieve specific review scores from the OpenReview page.

**The claim that it was "posted on OpenReview in Sep 2025" is confirmed accurate** (September 15, 2025).

**Key details about the paper:**
- Proposes segment-level KV cache sharing that breaks the prefix matching constraint
- Enables cross-agent KV cache reuse at arbitrary positions (not just matching prefixes)
- Built on vLLM framework using PagedAttention
- Three stages: Pre-Alias during Pre-Filling, Decoding, and Memory Table management

---

## 2. BFCL v3 (Berkeley Function Calling Leaderboard Version 3)

**Yes, BFCL v3 is a real, well-established benchmark.**

- **Release date:** September 19, 2024 (last updated December 10, 2024)
- **Institution:** UC Berkeley (part of the Gorilla project)
- **Authors:** Shishir G. Patil, Huanzhi Mao, Fanjia Yan, Charlie Cheng-Jie Ji, Vishnu Suresh, Ion Stoica, Joseph E. Gonzalez
- **Publication:** The BFCL paper was published as a poster at **ICML 2025** (proceedings at MLR Press: `proceedings.mlr.press/v267/patil25a.html`)
- **What v3 adds:** Multi-turn and multi-step function calling evaluation (Base Multi-Turn: 200 examples; Augmented Multi-Turn: 800 examples)
- **Evaluation method:** State-based verification (checks actual API system state after execution, rather than AST matching)
- **Current status:** Now at V4, accessible at `gorilla.cs.berkeley.edu/leaderboard.html`
- **Official page for v3:** https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html

BFCL is described as having become "the de facto standard for evaluating function-calls" in LLMs.

---

## Summary

| Item | Status |
|------|--------|
| CrossKV paper exists | Confirmed |
| Posted on OpenReview Sep 2025 | Confirmed (Sep 15, 2025) |
| Submitted to ICLR 2026 | Confirmed |
| Accepted at ICLR 2026 | Could not definitively confirm or deny |
| BFCL v3 is real | Confirmed |
| BFCL v3 is from Berkeley | Confirmed (UC Berkeley, Gorilla project) |
| BFCL paper published | Yes, at ICML 2025 |

Sources:
- [CrossKV on OpenReview](https://openreview.net/forum?id=kgzBkyqg6Z)
- [BFCL V3 Blog Post](https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html)
- [BFCL Paper at ICML 2025](https://icml.cc/virtual/2025/poster/46593)
- [BFCL Paper in MLR Proceedings](https://proceedings.mlr.press/v267/patil25a.html)
- [BFCL V4 Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [ICLR 2026 Conference on OpenReview](https://openreview.net/group?id=ICLR.cc%2F2026%2FConference)
- [ICLR 2026 Papers (papers.cool)](https://papers.cool/venue/ICLR.2026)

agentId: a337e4be66e068a7b (use SendMessage with to: 'a337e4be66e068a7b' to continue this agent)
&lt;usage>total_tokens: 28034
tool_uses: 22
duration_ms: 163295&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba110741-edc6-4ffa-964b-830369725876",
  "isSidechain": false,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "type": "user",
  "uuid": "7667c9dc-7ccb-457a-abb3-d2bc37cb0f83",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the paper \"Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing\" (also known as CrossKV). \n\n1. Verify its current publication status. The SegAttn proposal claims it was posted on OpenReview in Sep 2025. Has it been accepted at any conference (ICLR 2026, ICML 2026, etc.)?\n2. Search: \"CrossKV segment-level KV cache sharing agent\" and \"collaborative memory agentic workflow prefix barrier\"\n3. Check OpenReview for its review status if possible.\n\nAlso verify: is \"BFCL v3\" (Berkeley Function Calling Leaderboard version 3) a real benchmark? Search \"BFCL v3 function calling benchmark\".",
    "agentId": "a337e4be66e068a7b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Based on my extensive research, here is what I was able to determine:\n\n---\n\n## 1. CrossKV Paper: \"Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing\"\n\n**The paper is real and confirmed to exist on OpenReview.**\n\n**Publication status findings:**\n- **Venue:** Submitted to **ICLR 2026 Conference** (Submission #5797)\n- **Submission date:** September 15, 2025 (modified February 11, 2026)\n- **OpenReview link:** https://openreview.net/forum?id=kgzBkyqg6Z\n- **Conference acceptance status:** I was unable to definitively confirm whether this paper was accepted or rejected at ICLR 2026. The paper appears on OpenReview under the ICLR 2026 conference venue, and the February 2026 modification date suggests it went through the rebuttal process. However, I could not find it explicitly listed in the ICLR 2026 accepted papers lists I was able to access (which were incomplete -- the conference had 5,357 submissions total). I also could not retrieve specific review scores from the OpenReview page.\n\n**The claim that it was \"posted on OpenReview in Sep 2025\" is confirmed accurate** (September 15, 2025).\n\n**Key details about the paper:**\n- Proposes segment-level KV cache sharing that breaks the prefix matching constraint\n- Enables cross-agent KV cache reuse at arbitrary positions (not just matching prefixes)\n- Built on vLLM framework using PagedAttention\n- Three stages: Pre-Alias during Pre-Filling, Decoding, and Memory Table management\n\n---\n\n## 2. BFCL v3 (Berkeley Function Calling Leaderboard Version 3)\n\n**Yes, BFCL v3 is a real, well-established benchmark.**\n\n- **Release date:** September 19, 2024 (last updated December 10, 2024)\n- **Institution:** UC Berkeley (part of the Gorilla project)\n- **Authors:** Shishir G. Patil, Huanzhi Mao, Fanjia Yan, Charlie Cheng-Jie Ji, Vishnu Suresh, Ion Stoica, Joseph E. Gonzalez\n- **Publication:** The BFCL paper was published as a poster at **ICML 2025** (proceedings at MLR Press: `proceedings.mlr.press/v267/patil25a.html`)\n- **What v3 adds:** Multi-turn and multi-step function calling evaluation (Base Multi-Turn: 200 examples; Augmented Multi-Turn: 800 examples)\n- **Evaluation method:** State-based verification (checks actual API system state after execution, rather than AST matching)\n- **Current status:** Now at V4, accessible at `gorilla.cs.berkeley.edu/leaderboard.html`\n- **Official page for v3:** https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html\n\nBFCL is described as having become \"the de facto standard for evaluating function-calls\" in LLMs.\n\n---\n\n## Summary\n\n| Item | Status |\n|------|--------|\n| CrossKV paper exists | Confirmed |\n| Posted on OpenReview Sep 2025 | Confirmed (Sep 15, 2025) |\n| Submitted to ICLR 2026 | Confirmed |\n| Accepted at ICLR 2026 | Could not definitively confirm or deny |\n| BFCL v3 is real | Confirmed |\n| BFCL v3 is from Berkeley | Confirmed (UC Berkeley, Gorilla project) |\n| BFCL paper published | Yes, at ICML 2025 |\n\nSources:\n- [CrossKV on OpenReview](https://openreview.net/forum?id=kgzBkyqg6Z)\n- [BFCL V3 Blog Post](https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html)\n- [BFCL Paper at ICML 2025](https://icml.cc/virtual/2025/poster/46593)\n- [BFCL Paper in MLR Proceedings](https://proceedings.mlr.press/v267/patil25a.html)\n- [BFCL V4 Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)\n- [ICLR 2026 Conference on OpenReview](https://openreview.net/group?id=ICLR.cc%2F2026%2FConference)\n- [ICLR 2026 Papers (papers.cool)](https://papers.cool/venue/ICLR.2026)"
      }
    ],
    "totalDurationMs": 163295,
    "totalTokens": 28034,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 25393,
      "output_tokens": 1184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1456
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1184,
          "cache_read_input_tokens": 25393,
          "cache_creation_input_tokens": 1456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1456,
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
  "sourceToolAssistantUUID": "ba110741-edc6-4ffa-964b-830369725876",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T21:07:00.869Z_

<details><summary>↩ Tool result · `toolu_01XhJ6VMXSLKVhXQWgE7zFXp`</summary>

```text
Based on my comprehensive search across multiple queries, here is my report on recent work (primarily April-May 2026, with relevant earlier 2026 papers) that could be considered concurrent or competitive to SegAttn:

---

## Findings: Concurrent Work Related to SegAttn

### Most Directly Relevant Competitors

**1. Transactional Attention (TA) -- April 2026** (arXiv:2604.11288)
- The closest competitor to the "role-aware retention" aspect of SegAttn
- Uses structural anchor patterns (e.g., "key:", "password:", "Authorization:"[REDACTED] to protect adjacent value-bearing tokens from KV cache eviction
- Specifically targets function-calling workloads: achieves 100% credential retrieval accuracy across 200 function-calling trials at extreme compression (K=16 tokens)
- Key difference from SegAttn: TA operates on local structural patterns (key-value pairs in text) rather than chat-template-level role boundaries. It is not phase-aware and does not differentiate between prefill reasoning vs. generation phases
- TA-Fast variant is attention-free, reducing overhead by 52%

**2. SideQuest -- February 2026** (arXiv:2602.22603)
- Directly targets agentic ReAct-style workloads with tool calls
- Model-driven KV cache management: the LLM itself reasons about which segments of its KV cache are stale and selectively clears them (self-garbage-collection)
- Identifies "stale tool calls and associated responses that have lost their utility" -- this is segment-level reasoning about tool outputs
- Achieves 60-65% peak token reduction with negligible accuracy loss
- Key difference from SegAttn: SideQuest relies on the model itself to decide eviction dynamically at inference time, rather than using metadata-driven policies derived from chat template structure. It does not use pre-defined role categories or phase-aware compression ratios

**3. CrossKV / Segment-Level KV Cache Sharing -- ICLR 2026 workshop** (OpenReview)
- Decomposes KV cache into "fine-grained semantic segments" for sharing across agents
- Overcomes prefix-matching limitations by enabling arbitrary-position segment reuse
- Built on vLLM with PageAttention
- Key difference from SegAttn: focuses on multi-agent cache sharing rather than within-session compression. However, its segment decomposition concept (breaking cache into semantically meaningful segments by role/template boundaries) is philosophically similar

**4. SemantiCache -- March 2026** (arXiv:2603.14303)
- Three-stage pipeline: semantic chunking by delimiters, clustering within chunks, merged compression
- Partitions KV cache into "semantically coherent chunks by delimiters" -- delimiters include natural boundaries that could correspond to chat template markers
- Up to 2.61x inference speedup
- Key difference from SegAttn: delimiter-based chunking is generic (not chat-role-aware), and compression is uniform across chunks rather than role-differentiated

**5. EvoSparse -- ACL 2026 main**
- Dynamic sparse attention that evolves across decoding steps and layers
- Models token importance as an accumulating process over generation steps -- this is "phase-aware" in the sense that importance changes during generation
- Key difference from SegAttn: phase-awareness is per-token temporal dynamics, not role-classified (system/tool-schema/conversation/tool-output)

---

### Relevant But Less Directly Competing

**6. CacheTTL / Continuum -- Nov 2025, ICLR 2026 workshop**
- Addresses multi-turn agent workloads by predicting tool-call duration and setting time-to-live for KV cache retention
- Parses tool calls from LLM outputs, tracks per-tool latency
- 8x improvement in job completion time
- Orthogonal to SegAttn: operates at serving-system scheduling level, not attention-pattern level

**7. ACON -- ICLR 2026 Lifelong Agent workshop**
- Gradient-free compression of environment observations and interaction histories for long-horizon agents
- Learns compression guidelines from failure trajectories
- 26-54% peak token reduction while preserving task performance
- Operates at prompt/text level rather than KV cache level

**8. Task-KV -- January 2025** (arXiv:2501.15113)
- Semantically differentiates attention heads into "heterogeneous" vs "non-heterogeneous" categories and applies differentiated KV budgets
- Conceptual overlap: differentiated budgets based on semantic function
- Key difference: differentiates by head type, not by token role/segment

**9. Active Context Compression (Focus Agent) -- January 2026**
- Agent-centric: the agent itself decides when to compress/prune its context
- Targets software engineering agents
- Operates at interaction-history level, not attention-mechanism level

**10. EpiCache -- 2025**
- Episodic clustering of conversation history into coherent episodes with per-episode KV cache eviction
- Adaptive layer-wise budget allocation based on sensitivity
- Relevant overlap: treats conversation as composed of episodes (analogous to role segments) with differentiated treatment

---

### On "Generation-Phase-Dependent Attention Patterns"

I found NO published work specifically studying whether tool-call generation tokens attend differently to tool schemas than reasoning tokens do. The closest findings:

- **Dual-decoder architectures** (YOCO, Phi-4-mini-flash) separate prefill and generation phases but do not study role-specific attention differences within the generation phase
- **MInference** identifies three spatial aggregation patterns in attention (A-shape, Vertical-Slash, Block-Sparse) but these are input-agnostic, not role-specific
- **Attention head interpretability** research (Cell/Patterns 2025) catalogs head types (retrieval heads, induction heads, etc.) but does not examine role-conditioned generation-phase behavior
- **EvoSparse** models temporal evolution of token importance during decoding but does not condition on what role the attended-to tokens belong to

This appears to be a genuine gap in the literature -- the intersection of (a) generation-phase attention analysis with (b) role/segment classification of context tokens has not been explicitly studied.

---

### Summary Assessment for SegAttn Novelty

SegAttn's key differentiator -- using chat-template metadata to classify tokens by role (system prompt, tool schema, conversation, tool output) and then applying BOTH role-differentiated AND phase-aware (prefill vs. generation) compression policies -- does not appear to have a direct published competitor as of May 2026. The closest threats are:

1. **Transactional Attention** overlaps on the "protect structurally important tokens" angle for function-calling, but lacks role classification and phase awareness
2. **SideQuest** overlaps on segment-level reasoning about tool outputs in agent workloads, but uses dynamic model-driven eviction rather than metadata-driven policies
3. **SemantiCache** overlaps on delimiter-based semantic chunking, but applies uniform compression rather than role-differentiated budgets
4. **CrossKV** overlaps on segment-level decomposition, but targets multi-agent sharing not compression

None of these combine all three of SegAttn's claimed contributions: (1) chat-template-derived role classification, (2) role-differentiated compression budgets, and (3) phase-aware (generation-dependent) sparsity patterns.

---

Sources:
- [Transactional Attention: Semantic Sponsorship for KV-Cache Retention](https://arxiv.org/abs/2604.11288)
- [SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning](https://arxiv.org/abs/2602.22603)
- [Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing](https://openreview.net/forum?id=kgzBkyqg6Z)
- [SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging](https://arxiv.org/abs/2603.14303)
- [EvoSparse: Evolving Sparsity (ACL 2026)](https://github.com/iLearn-Lab/ACL26-EvoSparse)
- [Continuum/CacheTTL: Efficient Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live](https://arxiv.org/abs/2511.02230)
- [ACON: Optimizing Context Compression for Long-horizon LLM Agents](https://arxiv.org/abs/2510.00615)
- [Task-KV: Task-aware KV Cache Optimization via Semantic Differentiation of Attention Heads](https://arxiv.org/abs/2501.15113)
- [Active Context Compression: Autonomous Memory Management in LLM Agents](https://arxiv.org/abs/2601.07190)
- [AgentCompress: Task-Aware Compression for Affordable LLM Agents](https://arxiv.org/abs/2601.05191)
- [Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys](https://arxiv.org/abs/2603.14224)
- [HySparse: Hybrid Sparse Attention with Oracle Token Selection](https://arxiv.org/abs/2602.03560)
- [SentenceKV: Efficient LLM Inference via Sentence-Level Semantic KV Caching](https://arxiv.org/html/2504.00970v1)
- [EpiCache: Episodic KV Cache Management for Long Conversational QA](https://arxiv.org/html/2509.17396v1)

agentId: a80169cb8fdaccf57 (use SendMessage with to: 'a80169cb8fdaccf57' to continue this agent)
&lt;usage>total_tokens: 35398
tool_uses: 24
duration_ms: 201590&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df5fb161-4b5c-4843-9555-027a843c2f25",
  "isSidechain": false,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "type": "user",
  "uuid": "fc5a6399-2128-40ae-bb0c-da9013011155",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for very recent papers (April-May 2026) on KV cache compression or sparse attention specifically for agent or tool-calling LLM workloads. This is to find any concurrent work published in the last 6 weeks.\n\nTry these searches:\n1. \"agent sparse attention KV cache 2026 arxiv\"\n2. \"role-aware attention compression language model agent\"  \n3. \"segment-level KV cache agent tool calling 2026\"\n4. \"phase-aware sparse attention tool generation\"\n5. \"chat template attention sparsity\"\n\nAlso check if there's any work on \"generation-phase-dependent attention patterns\" in LLMs — specifically whether tool-call generation tokens attend differently to tool schemas than reasoning tokens do.\n\nReport any findings that could be direct competitors to SegAttn (a method that uses chat-template metadata to classify tokens by role — system prompt, tool schema, conversation, tool output — and applies role-differentiated, phase-aware KV cache compression).",
    "agentId": "a80169cb8fdaccf57",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search across multiple queries, here is my report on recent work (primarily April-May 2026, with relevant earlier 2026 papers) that could be considered concurrent or competitive to SegAttn:\n\n---\n\n## Findings: Concurrent Work Related to SegAttn\n\n### Most Directly Relevant Competitors\n\n**1. Transactional Attention (TA) -- April 2026** (arXiv:2604.11288)\n- The closest competitor to the \"role-aware retention\" aspect of SegAttn\n- Uses structural anchor patterns (e.g., \"key:\", \"password:\", \"Authorization:\"[REDACTED] to protect adjacent value-bearing tokens from KV cache eviction\n- Specifically targets function-calling workloads: achieves 100% credential retrieval accuracy across 200 function-calling trials at extreme compression (K=16 tokens)\n- Key difference from SegAttn: TA operates on local structural patterns (key-value pairs in text) rather than chat-template-level role boundaries. It is not phase-aware and does not differentiate between prefill reasoning vs. generation phases\n- TA-Fast variant is attention-free, reducing overhead by 52%\n\n**2. SideQuest -- February 2026** (arXiv:2602.22603)\n- Directly targets agentic ReAct-style workloads with tool calls\n- Model-driven KV cache management: the LLM itself reasons about which segments of its KV cache are stale and selectively clears them (self-garbage-collection)\n- Identifies \"stale tool calls and associated responses that have lost their utility\" -- this is segment-level reasoning about tool outputs\n- Achieves 60-65% peak token reduction with negligible accuracy loss\n- Key difference from SegAttn: SideQuest relies on the model itself to decide eviction dynamically at inference time, rather than using metadata-driven policies derived from chat template structure. It does not use pre-defined role categories or phase-aware compression ratios\n\n**3. CrossKV / Segment-Level KV Cache Sharing -- ICLR 2026 workshop** (OpenReview)\n- Decomposes KV cache into \"fine-grained semantic segments\" for sharing across agents\n- Overcomes prefix-matching limitations by enabling arbitrary-position segment reuse\n- Built on vLLM with PageAttention\n- Key difference from SegAttn: focuses on multi-agent cache sharing rather than within-session compression. However, its segment decomposition concept (breaking cache into semantically meaningful segments by role/template boundaries) is philosophically similar\n\n**4. SemantiCache -- March 2026** (arXiv:2603.14303)\n- Three-stage pipeline: semantic chunking by delimiters, clustering within chunks, merged compression\n- Partitions KV cache into \"semantically coherent chunks by delimiters\" -- delimiters include natural boundaries that could correspond to chat template markers\n- Up to 2.61x inference speedup\n- Key difference from SegAttn: delimiter-based chunking is generic (not chat-role-aware), and compression is uniform across chunks rather than role-differentiated\n\n**5. EvoSparse -- ACL 2026 main**\n- Dynamic sparse attention that evolves across decoding steps and layers\n- Models token importance as an accumulating process over generation steps -- this is \"phase-aware\" in the sense that importance changes during generation\n- Key difference from SegAttn: phase-awareness is per-token temporal dynamics, not role-classified (system/tool-schema/conversation/tool-output)\n\n---\n\n### Relevant But Less Directly Competing\n\n**6. CacheTTL / Continuum -- Nov 2025, ICLR 2026 workshop**\n- Addresses multi-turn agent workloads by predicting tool-call duration and setting time-to-live for KV cache retention\n- Parses tool calls from LLM outputs, tracks per-tool latency\n- 8x improvement in job completion time\n- Orthogonal to SegAttn: operates at serving-system scheduling level, not attention-pattern level\n\n**7. ACON -- ICLR 2026 Lifelong Agent workshop**\n- Gradient-free compression of environment observations and interaction histories for long-horizon agents\n- Learns compression guidelines from failure trajectories\n- 26-54% peak token reduction while preserving task performance\n- Operates at prompt/text level rather than KV cache level\n\n**8. Task-KV -- January 2025** (arXiv:2501.15113)\n- Semantically differentiates attention heads into \"heterogeneous\" vs \"non-heterogeneous\" categories and applies differentiated KV budgets\n- Conceptual overlap: differentiated budgets based on semantic function\n- Key difference: differentiates by head type, not by token role/segment\n\n**9. Active Context Compression (Focus Agent) -- January 2026**\n- Agent-centric: the agent itself decides when to compress/prune its context\n- Targets software engineering agents\n- Operates at interaction-history level, not attention-mechanism level\n\n**10. EpiCache -- 2025**\n- Episodic clustering of conversation history into coherent episodes with per-episode KV cache eviction\n- Adaptive layer-wise budget allocation based on sensitivity\n- Relevant overlap: treats conversation as composed of episodes (analogous to role segments) with differentiated treatment\n\n---\n\n### On \"Generation-Phase-Dependent Attention Patterns\"\n\nI found NO published work specifically studying whether tool-call generation tokens attend differently to tool schemas than reasoning tokens do. The closest findings:\n\n- **Dual-decoder architectures** (YOCO, Phi-4-mini-flash) separate prefill and generation phases but do not study role-specific attention differences within the generation phase\n- **MInference** identifies three spatial aggregation patterns in attention (A-shape, Vertical-Slash, Block-Sparse) but these are input-agnostic, not role-specific\n- **Attention head interpretability** research (Cell/Patterns 2025) catalogs head types (retrieval heads, induction heads, etc.) but does not examine role-conditioned generation-phase behavior\n- **EvoSparse** models temporal evolution of token importance during decoding but does not condition on what role the attended-to tokens belong to\n\nThis appears to be a genuine gap in the literature -- the intersection of (a) generation-phase attention analysis with (b) role/segment classification of context tokens has not been explicitly studied.\n\n---\n\n### Summary Assessment for SegAttn Novelty\n\nSegAttn's key differentiator -- using chat-template metadata to classify tokens by role (system prompt, tool schema, conversation, tool output) and then applying BOTH role-differentiated AND phase-aware (prefill vs. generation) compression policies -- does not appear to have a direct published competitor as of May 2026. The closest threats are:\n\n1. **Transactional Attention** overlaps on the \"protect structurally important tokens\" angle for function-calling, but lacks role classification and phase awareness\n2. **SideQuest** overlaps on segment-level reasoning about tool outputs in agent workloads, but uses dynamic model-driven eviction rather than metadata-driven policies\n3. **SemantiCache** overlaps on delimiter-based semantic chunking, but applies uniform compression rather than role-differentiated budgets\n4. **CrossKV** overlaps on segment-level decomposition, but targets multi-agent sharing not compression\n\nNone of these combine all three of SegAttn's claimed contributions: (1) chat-template-derived role classification, (2) role-differentiated compression budgets, and (3) phase-aware (generation-dependent) sparsity patterns.\n\n---\n\nSources:\n- [Transactional Attention: Semantic Sponsorship for KV-Cache Retention](https://arxiv.org/abs/2604.11288)\n- [SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning](https://arxiv.org/abs/2602.22603)\n- [Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing](https://openreview.net/forum?id=kgzBkyqg6Z)\n- [SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging](https://arxiv.org/abs/2603.14303)\n- [EvoSparse: Evolving Sparsity (ACL 2026)](https://github.com/iLearn-Lab/ACL26-EvoSparse)\n- [Continuum/CacheTTL: Efficient Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live](https://arxiv.org/abs/2511.02230)\n- [ACON: Optimizing Context Compression for Long-horizon LLM Agents](https://arxiv.org/abs/2510.00615)\n- [Task-KV: Task-aware KV Cache Optimization via Semantic Differentiation of Attention Heads](https://arxiv.org/abs/2501.15113)\n- [Active Context Compression: Autonomous Memory Management in LLM Agents](https://arxiv.org/abs/2601.07190)\n- [AgentCompress: Task-Aware Compression for Affordable LLM Agents](https://arxiv.org/abs/2601.05191)\n- [Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys](https://arxiv.org/abs/2603.14224)\n- [HySparse: Hybrid Sparse Attention with Oracle Token Selection](https://arxiv.org/abs/2602.03560)\n- [SentenceKV: Efficient LLM Inference via Sentence-Level Semantic KV Caching](https://arxiv.org/html/2504.00970v1)\n- [EpiCache: Episodic KV Cache Management for Long Conversational QA](https://arxiv.org/html/2509.17396v1)"
      }
    ],
    "totalDurationMs": 201590,
    "totalTokens": 35398,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 1038,
      "cache_read_input_tokens": 31103,
      "output_tokens": 2357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1038
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 900,
          "output_tokens": 2357,
          "cache_read_input_tokens": 31103,
          "cache_creation_input_tokens": 1038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1038,
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
      "otherToolCount": 24
    }
  },
  "sourceToolAssistantUUID": "df5fb161-4b5c-4843-9555-027a843c2f25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-10T21:07:00.877Z_

```json
{
  "parentUuid": "fc5a6399-2128-40ae-bb0c-da9013011155",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ca8e64cb-ebc3-499a-a6d4-7e56c0390b4e",
  "timestamp": "2026-05-10T21:07:00.877Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-10T21:08:12.534Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research results. Let me synthesize my findings and make a final assessment.

## Summary of Research Findings

### Reference Verification
- **ChunkKV (NeurIPS 2025)**: ✅ Verified (poster)
- **Twilight (NeurIPS 2025 Spotlight)**: ✅ Verified
- **MAS/Segment-Based Attention Masking (ACL 2025)**: ✅ Verified
- **Tool Attention (arXiv:2604.21816)**: ✅ Verified; 95% reduction is measured token count but downstream metrics are projections


- **FlashInfer plan() issue #2938**: ✅ Verified as real
- **SGLang issue #12867**: ✅ Exists, though the "inactive" status couldn't be independently confirmed
- **The Sparse Frontier (arXiv:2504.17768)**: ✅ Verified
- **CacheSlide (FAST 2026)**: ✅ Verified
- **VL-Cache (ICLR 2025)**: ✅ Verified
- **Qwen3.6-27B with hybrid architecture**: ✅ Verified
- **CrossKV**: ✅ Exists on OpenReview as an ICLR 2026 submission

, though acceptance status remains unclear
- **BFCL v3**: ✅ Real benchmark from UC Berkeley
- **EMNLP 2026 ARR deadline May 25**: ✅ Confirmed

Now I'm identifying some additional papers that should be cited. Transactional Attention from April 2026 specifically addresses function-calling workloads by protecting structurally important tokens from KV cache eviction, achieving perfect credential retrieval under extreme compression—this is distinct from SegAttn's approach and directly relevant. EpiCache from Apple handles episodic KV caching for conversational QA, which is tangentially related. I'm also noting SemantiCache from March, though the entry appears incomplete.

Looking at the broader landscape, KVFlow tackles prefix caching for multi-agent workflows rather than attention compression, and NSA validates the coarse-static plus fine-dynamic paradigm that SegAttn builds on. The core innovation here—combining chat-template-derived role classification with role-differentiated compression budgets and phase-aware sparsity patterns—doesn't have a direct competitor. Transactional Attention protects function-calling tokens but lacks role classification and phase awareness, while other approaches like SideQuest use model-driven segment eviction without the same role-based differentiation.

The novelty is real but somewhat incremental: VL-Cache proved content-type differentiation works, ChunkKV demonstrated chunk-level compression, and Twilight showed adaptive sparsity is viable. SegAttn synthesizes these insights specifically for the agent domain with generation-phase-dependent attention patterns across role segments—something not explicitly studied before. The feasibility checks out at 165-205 H100-hours with an 8-12 day timeline, keeping within the budget constraints.

For the auto_research path, FlashInfer's block-sparse API is available with FlexAttention as a fallback, though SGLang hybrid support remains uncertain and the plan() overhead could be problematic. If needed, Llama-3.1-8B alone provides a well-scoped primary contribution. There are a few gaps to address: Transactional Attention from April 2026 is relevant for function-calling KV cache retention but not critical, and the benchmarks need to include HumanEval, RULER, and C4 perplexity alongside the currently planned WikiText-2, MMLU, MT-Bench, LongBench, and BFCL v3 evaluations. The 205-hour compute budget is tight but workable for the May 25 deadline.

The proposal's strengths are substantial—the landscape review is comprehensive with over 28 references, the implementation plan includes proper fallbacks, and the phase-gating mechanism with reactive detection is well-specified. The layered evaluation approach (C1-C3) directly addresses whether the benefits are marginal, and the falsification criteria for the profiling study provide clear success metrics. The risk acknowledgment around the hybrid architecture pilot shows realistic planning.

On the flip side, the core contribution is somewhat incremental—applying established static-versus-dynamic principles to a new context. The entire system hinges on the profiling study validating the hypothesis, which hasn't been tested yet. A few user-required benchmarks are missing, the timeline is tight, and the impact could be significantly constrained if prompt-level filtering already handles most cases (the C3 condition).

Looking at the scoring: novelty lands at 4/5 because the specific combination and phase-gating insight are genuinely new, even if not paradigm-shifting. Feasibility is also 4/5—the budget works, the plan is concrete with proper fallbacks, though the profiling study remains the critical risk. Clarity is 4.5/5, with the proposal being exceptionally detailed and well-differentiated, though the thought cuts off mid-sentence.

The impact score is 3.5/5 since agent serving is timely but the marginal gain over existing approaches is unclear, especially under C3 constraints. This puts it at EMNLP Findings level rather than main conference. The average lands right at 4.0, which is the threshold.

But stepping back after five rounds of feedback, the real concern is the benchmark gap. The user explicitly required HumanEval, RULER, and C4, and while the proposal substitutes LongBench as a partial replacement for RULER, that's still a mismatch against stated requirements. There's also a missing Transactional Attention citation from April 2026 and a slight budget overage on the auto_research path, though these are less critical than the benchmark issue.

Given the proposal's overall quality after extensive revision, I'm leaning toward a minor revise rather than reject. The Transactional Attention omission matters for a function-calling paper, but the work is clearly differentiated from that approach. The real question is whether an EMNLP reviewer would actually reject over these remaining gaps or view them as manageable issues in an otherwise solid proposal. The average lands right at 4.0, which is borderline for a pass. Given the steady improvements across rounds, I'm leaning toward a conditional revision rather than outright rejection—the novelty and feasibility are solid, though the 3.5 impact score is the main drag. I should focus feedback on three concrete fixes: citing the recent Transactional Attention work and clarifying differentiation, adding the missing benchmarks the user specified, and tightening the impact argument around conversation length benefits.

Wait, I need to reconsider this more carefully. The user laid out a hard constraint requiring six specific benchmarks—perplexity on Wiki and C4, MMLU, HumanEval, LongBench, RULER, and MT-Bench—and the proposal is missing three of them: C4, HumanEval, and RULER. That's a significant gap, not a minor one. Even though adding these evaluations wouldn't be technically difficult, the proposal objectively fails to meet the stated requirements. The computational budget also needs a small adjustment to stay under 200 hours. These aren't trivial oversights—they're concrete unmet constraints that warrant a revise decision.

On the impact score, I'm torn. Agent serving is genuinely important infrastructure that major AI labs are investing in, and a training-free optimization targeting the KV cache bottleneck has real practical value. But the approach relies on unvalidated assumptions about how well metadata-based pruning generalizes, and the marginal benefit under Claude remains uncertain. I'll settle on 3.5 as a fair middle ground—acknowledging the genuine importance while reflecting the uncertainty.

So my final call is **revise** with minor, actionable feedback. The paper should pass in the next round with those adjustments, and I'm landing on an average score around 4.0.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca8e64cb-ebc3-499a-a6d4-7e56c0390b4e",
  "isSidechain": false,
  "requestId": "req_011Caua27dwnj3M44wL7F4yc",
  "type": "assistant",
  "uuid": "322f4d78-e4e4-4e88-935c-94890635e244",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012G2zmPLuofxxmURrWoF88C",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7513,
      "cache_read_input_tokens": 49138,
      "output_tokens": 4703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4703,
          "cache_read_input_tokens": 49138,
          "cache_creation_input_tokens": 7513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7513
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

_source line 35 · 2026-05-10T21:08:48.257Z_

Now I have comprehensive results from my independent research. Let me synthesize my findings into a final assessment.

## Key Research Findings

**References verified**: ChunkKV (NeurIPS 2025 ✓), Twilight (NeurIPS 2025 Spotlight ✓), MAS (ACL 2025 ✓), Tool Attention (arXiv:2604.21816 ✓), FlashInfer issue #2938 (✓), CacheSlide (FAST 2026 ✓), VL-Cache (ICLR 2025 ✓), Qwen3.6-27B hybrid architecture (✓), EMNLP 2026 ARR deadline May 25 (✓), BFCL v3 (✓), CrossKV on OpenReview Sep 2025 (✓ — ICLR 2026 acceptance unconfirmed).

**Gap validity**: Confirmed. No published work combines chat-template role classification + role-differentiated budgets + phase-aware dynamic sparsity at the attention level. The combination is genuinely novel.

**Key missing work found**: Transactional Attention (arXiv:2604.11288, April 2026) — protects structurally important tokens for function-calling via structural anchor patterns, achieving 100% credential retrieval at extreme compression. Different mechanism but same workload target.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 4, "rationale": "The combination of zero-cost chat-template classification + phase-gating + composability with token-level methods is genuinely novel. Well-differentiated from VL-Cache (modality vs. semantic role), ChunkKV (fixed chunks vs. role boundaries), and Twilight (bottom-up vs. top-down). The profiling study's phase-dependent attention patterns for agent roles appear unstudied."},
    "feasibility": {"score": 4, "rationale": "165-205 H100-hours is within/marginally over budget. Implementation via FlashInfer block-sparse API is concrete with FlexAttention fallback. Qwen3.6-27B properly scoped as best-effort pilot. Auto_research path at 8-12 days is tight but feasible for May 25."},
    "clarity": {"score": 4, "rationale": "Exceptionally detailed proposal with 28+ references, explicit differentiation from each, concrete implementation details, falsification criteria, and layered evaluation design. Among the best-structured proposals I've reviewed."},
    "impact": {"score": 3, "rationale": "Agent serving is timely, but marginal benefit under C3 (after prompt-level filtering) is uncertain. The contribution may be EMNLP Findings quality rather than main conference — essentially applies proven principles (content-type differentiation, phase-awareness) to a new domain. The profiling study is valuable regardless but alone may be insufficient for a top venue."}
  },
  "issues": [
    "IMPORTANT: Missing citation 'Transactional Attention' (arXiv:2604.11288, April 2026) — uses structural anchor patterns to protect value-bearing tokens adjacent to keys (e.g., 'Authorization:', 'password:'[REDACTED] from KV cache eviction in function-calling workloads. Achieves 100% credential retrieval accuracy at extreme compression (K=16). While it operates on local text patterns rather than chat-template role boundaries and lacks phase-awareness, it directly targets function-calling KV cache retention — the same workload SegAttn addresses. Must be cited and differentiated.",
    "User benchmark requirements partially unmet: The user explicitly requires 'perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench' as evaluation benchmarks. The proposal covers WikiText-2, MMLU, MT-Bench, LongBench, BFCL v3 — but is still missing C4 perplexity, HumanEval, and RULER. While LongBench partially overlaps with RULER and BFCL v3 is more relevant than HumanEval for agent work, at minimum C4 perplexity (trivial to add) should be included for compliance with user requirements.",
    "Auto_research path at 205 H100-hours marginally exceeds the user's hard constraint of ≤200 H100-hours. The buffer allocation (23h) should be reduced by 5h to bring the total to exactly 200h, or the cross-architecture comparison (20h) should be folded into the profiling phase.",
    "Impact argument under C3 condition needs strengthening: if Tool Attention achieves 95% tool-token reduction at the prompt level, and the remaining context is primarily system instructions (~500-2000 tokens) + conversation history + tool outputs, the absolute KV cache savings from role-differentiated compression of this reduced context may be modest in short conversations. The proposal should quantify: at what conversation length (number of turns) does SegAttn's marginal benefit under C3 become substantial? A concrete example (e.g., 'at 20 turns with 5 tool calls, retained context is X tokens, of which Y% benefits from role-differentiated compression') would strengthen the impact argument.",
    "SGLang issue #12867 'inactive' characterization could not be independently verified. The issue exists and has pending features, but my search did not confirm an explicit 'inactive' label. Consider softening to 'remains under development with multiple pending features and stalled progress as of May 2026' rather than asserting 'marked inactive.'"
  ],
  "feedback": "The proposal is approaching pass quality after 5 rounds of substantial improvement. The remaining issues are minor and addressable in one round:\n\n1. **Cite Transactional Attention (arXiv:2604.11288, April 2026)**: Differentiate clearly — TA protects local structural patterns (key-value pairs in text) via anchor-based sponsorship; SegAttn classifies entire message-level segments via chat-template metadata with phase-aware budgets. TA lacks role classification, phase-awareness, and operates at token-adjacency level rather than message-role level. They are complementary — TA could refine token selection within SegAttn's tool-output segments.\n\n2. **Add C4 perplexity to evaluation**: This is trivial (evaluate on C4 validation set alongside WikiText-2). For HumanEval and RULER, either add them (adding ~5-8 H100-hours) or explicitly justify their exclusion: RULER's long-context probing is largely covered by LongBench's retrieval tasks, and HumanEval evaluates code generation quality which is tangential to agent tool-calling. If adding them, reduce the buffer or cross-architecture comparison budget accordingly to stay within 200h.\n\n3. **Trim auto_research to ≤200h**: Reduce buffer from 23h to 18h, or merge cross-architecture comparison into the profiling phase.\n\n4. **Quantify C3 marginal benefit**: Add a concrete worked example showing retained context size at different conversation lengths under C3. This strengthens the impact argument by showing SegAttn's value grows with conversation depth.\n\n5. **Soften SGLang characterization**: Replace 'marked inactive' with 'remains under development with stalled progress.'\n\nWith these changes, the average score should reach pass threshold. The novelty and feasibility are solid; the impact score is the main drag — strengthening the C3 quantification will help.",
  "reason": "Minor remaining issues (1 missing citation, benchmark gap, marginal budget overage, impact quantification) prevent pass at round 6, but all are addressable in one revision round."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "322f4d78-e4e4-4e88-935c-94890635e244",
  "isSidechain": false,
  "requestId": "req_011Caua27dwnj3M44wL7F4yc",
  "type": "assistant",
  "uuid": "ecf27a89-a26b-4faf-9b27-ed9778e2ce84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012G2zmPLuofxxmURrWoF88C",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7513,
      "cache_read_input_tokens": 49138,
      "output_tokens": 4703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4703,
          "cache_read_input_tokens": 49138,
          "cache_creation_input_tokens": 7513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7513
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ecf27a89-a26b-4faf-9b27-ed9778e2ce84",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-role sparse attention for agent workloads",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ecf27a89-a26b-4faf-9b27-ed9778e2ce84",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-role sparse attention for agent workloads",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2"
}
```

---
