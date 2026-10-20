# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/c9c317b6-258b-43eb-b84c-bc4c97ee2780.jsonl`
- **Structured JSON:** [`ae37e02ae177ecb48652.json`](../../sessions/ae/ae37e02ae177ecb48652.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T00:19:14.674Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T00:19:14.674Z",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.\n\nDirection: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.\n\nContribution type: METHOD ONLY. Propose new algorithms — not profiling studies.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Generous for efficiency work.\n2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.\n3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.\n\nLook for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.\n\nTag: direction=efficiency, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 5/10)\n{\n  \"title\": \"Sparsity Interaction Surfaces: Characterizing How Attention and MLP Activation Sparsity Interact Across Reasoning Phases\",\n  \"core_problem\": \"Reasoning models exhibit distinct computational patterns during thinking vs. answer phases, yet all existing compute sparsity methods — whether targeting attention heads (Polar Sparsity, Twilight), MLP activations (TEAL, WAS, ActTail), or both jointly (R-Sparse, AMP) — treat attention and MLP sparsity as independent, separable axes. Within each transformer block, however, a causal dependency exists: attention output flows through the residual stream and layer normalization before becoming MLP input, creating a direct information pathway. Recent mechanistic work establishes that these components serve fundamentally different functions: 'Attention Retrieves, MLP Memorizes' (arXiv 2506.01115) shows attention performs contextual retrieval while MLP stores learned patterns, and 'Interpreting Context Look-ups in Transformers' (EMNLP 2024) empirically demonstrates that specific attention heads causally trigger downstream MLP neurons. This functional asymmetry and causal coupling means that sparsifying the retrieval mechanism directly changes what the memorization mechanism has to work with — yet no existing work characterizes the cross-partial derivative d²Q/(ds_attn · ds_mlp), i.e., whether jointly sparsifying attention and MLP degrades quality more than expected from individual axes (compounding), less than expected (complementing), or as expected (independent). This interaction question is distinct from KV cache sparsity and from individual-axis sparsity. R-Sparse (ICLR 2025) applies joint sparsity but assumes additivity without measuring interaction effects. 'When Reasoning Meets Compression' (ICLR 2026) shows MLP up projections in the final layer are critically important for reasoning — protecting just 2% of excessively compressed weights raises accuracy by 6.57% — but does not study how attention sparsity modulates this MLP sensitivity. The field lacks the empirical characterization needed to determine whether the additive assumption underlying joint methods is justified or whether it silently compounds errors at certain reasoning phases.\",\n  \"opportunity\": \"Three converging lines of evidence provide both theoretical motivation and practical urgency for characterizing the attention-MLP sparsity interaction surface: (1) Causal coupling with functional asymmetry: The transformer block's sequential structure (attention → residual → layer norm → MLP) creates a direct dependency where attention output quality determines MLP input distribution. 'Attention Retrieves, MLP Memorizes' shows these components serve distinct roles — attention retrieves contextual information, MLP memorizes learned patterns — so sparsifying retrieval changes what memorization can operate on. Three interaction regimes are theoretically possible: if attention drops tokens critical for MLP's memorization role, joint sparsity compounds (positive cross-partial in degradation); if MLP can compensate via the residual stream bypass, joint sparsity complements (negative cross-partial); if the dropped information was redundant to MLP processing, the axes are independent (near-zero cross-partial). Which regime dominates — and whether it varies across reasoning phases — is an empirical question with direct implications for system design. (2) Reasoning-specific sensitivity asymmetry: 'When Reasoning Meets Compression' (ICLR 2026) shows MLP up projections are disproportionately important for reasoning accuracy, while 'From LLMs to LRMs' (arXiv 2601.18091) shows width pruning (MLP-like) is more robust than depth pruning (attention-like) for reasoning tasks across 17 benchmarks. These asymmetric sensitivity profiles suggest the interaction surface is unlikely to be flat. Polar Sparsity (NeurIPS 2025) showed attention head sparsity is batch-invariant while MLP sparsity degrades with batching — further evidence of fundamentally different scaling properties that likely produce phase-dependent interactions. (3) Practical urgency without empirical grounding: Reasoning models (DeepSeek-R1, Qwen3) are mainstream with thinking tokens comprising 80-95% of generation and decode costs 5-10x higher than standard models. ThinKV (ICLR 2026 Oral) proved KV cache sparsity varies dramatically across reasoning phases, but compute sparsity interactions across phases remain uncharacterized. The Sparsing Law (ICML 2025) establishes that SwiGLU models have substantially lower natural activation sparsity than ReLU models, and existing forced-sparsity evidence (ActTail, WAS) comes from non-reasoning models — whether SwiGLU-based reasoning models retain sufficient headroom for practical joint sparsity is an open question our profiling directly answers. 'Thinking Tokens are Information Peaks' (NeurIPS 2025) showed mutual information peaks are sparse (<5% of tokens) at transition/reflection points, suggesting qualitatively different compute requirements at different reasoning stages.\",\n  \"landscape\": \"Attention-head sparsity: Polar Sparsity (NeurIPS 2025) achieves 2.2x decode speedup via batch-invariant head-level sparsity; critically demonstrates that MLP union sparsity vanishes under batching while attention head sparsity remains stable — evidence the two axes have fundamentally different scaling properties. Twilight (NeurIPS 2025 Spotlight) enables adaptive attention budget via hierarchical top-p pruning with 3.9x decode acceleration but is attention-only. EvoSparse (ACL 2026) models token importance as an evolving process for dynamic sparse attention but is attention-only. RaaS (ACL 2025 Findings) identifies milestone-token attention patterns in reasoning but is attention-only and phase-agnostic. SeerAttention-R learns decode-time sparse attention with 9x speedup at 90% sparsity but requires training and is attention-only. SpecAttn (arXiv 2602.07223, Feb 2026) co-designs sparse attention with self-speculative decoding, achieving 2.81x throughput — attention-only, no MLP interaction. MLP activation sparsity: TEAL (ICLR 2025) achieves 1.5-1.8x MLP-only speedup via magnitude pruning at 40-50% sparsity. WAS (EMNLP 2025) improves over TEAL with weight-aware scoring and Bayesian-optimized inter-block allocation, achieving 1.68x at 60% sparsity. WiSparse (arXiv 2026) advances MLP sparsity with mixed-granularity allocation, preserving 97% of dense performance at 50% sparsity. ActTail (arXiv 2026) applies HT-SR theory for global sparsity allocation across projections, reducing perplexity by 21.8% at 80% sparsity vs. TEAL's uniform allocation — the most recent MLP sparsity method confirming meaningful headroom in SwiGLU models. Joint attention-MLP sparsity: R-Sparse (ICLR 2025) is the most relevant baseline: applies rank-aware activation sparsity to both attention and MLP jointly at 50% model-wide level with 1.43x speedup, but treats the two axes as additive without measuring interaction effects and applies the same sparsity uniformly across all decode steps. AMP (IJCNN 2025) jointly prunes attention heads and MLP but applies static uniform pruning without runtime adaptation or interaction analysis. Reasoning model compression: 'When Reasoning Meets Compression' (ICLR 2026, arXiv 2504.02010) benchmarks compressed DeepSeek-R1 across reasoning tasks and identifies MLP up projection in the final layer as critically important — protecting 2% of excessively compressed weights raises accuracy by 6.57%. Directly motivates understanding how attention sparsity modulates MLP sensitivity in reasoning models. 'From LLMs to LRMs' (arXiv 2601.18091, Jan 2026) evaluates static/dynamic depth/width pruning across 17 tasks, finding width pruning more robust than depth pruning for reasoning, and static pruning better than dynamic for reasoning preservation — provides context for MLP vs. attention sparsity sensitivity asymmetry. RAC (NeurIPS 2025 Workshop) demonstrates reasoning-aware calibration for weight pruning via CoT reconstruction at 50% weight sparsity. 'Doing More With Less' (arXiv 2604.25098, April 2026) shows unstructured weight pruning can maintain or improve test-time scaling in reasoning models. Mechanistic understanding: 'Attention Retrieves, MLP Memorizes' (arXiv 2506.01115, June 2025) disentangles transformer components: random attention (frozen Q,K) still works competitively while frozen MLPs cause the biggest performance drop, establishing a functional basis for asymmetric sparsity tolerance and providing theoretical grounding for why sparsifying attention changes MLP's operating conditions. 'Interpreting Context Look-ups in Transformers' (EMNLP 2024, arXiv 2402.15055) shows specific attention heads causally trigger downstream MLP neurons — direct empirical evidence that sparsifying attention affects MLP processing, the mechanistic basis for non-trivial interaction. 'Thinking Tokens are Information Peaks' (NeurIPS 2025) shows MI peaks are sparse (<5% of tokens) at transition/reflection points. Reasoning phase awareness: ThinKV (ICLR 2026 Oral) applies thought-adaptive KV compression using KDE-based phase classification with <5% KV cache usage — targets memory, not compute, but establishes that reasoning phases have distinct sparsity profiles. LazyEviction (arXiv 2025) reveals Token Importance Recurrence — tokens regain high attention after multiple decode steps — relevant to understanding phase-dependent attention patterns. Elastic Reasoning (ICLR 2026) separates thinking and solution budgets but via different model sizes, not sparsity. Sparsity foundations: Sparsing Law (ICML 2025) establishes that SiLU/SwiGLU models have fundamentally lower natural activation sparsity than ReLU models, with convergent power-law relationships — directly relevant to headroom assessment. ELAS (arXiv 2605.03667, May 2026) combines low-rank + 2:4 activation sparsity with Squared-ReLU reaching 84-98% sparsity, but uses a different activation function. arXiv 2507.22928 shows CoT induces higher SAE feature sparsity in Pythia — relevant but on small non-SwiGLU models. Other complementary work: FASA (ICLR 2026) performs frequency-aware sparse attention achieving 2.56x on AIME24. LServe (MLSys 2025) unifies sparse attention for prefill+decode. SparseSpec (arXiv 2025) accelerates reasoning inference via sparse self-speculative decoding. Nemotron Elastic (ICML 2026) enables elastic inference. Gap: No existing work (1) characterizes the interaction surface between attention-head and MLP activation sparsity across reasoning phases, (2) provides theoretical motivation grounded in the attention→MLP causal dependency and functional asymmetry for why this interaction should be non-trivial, (3) tests transferability of interaction patterns across task families (math, code, general reasoning), or (4) characterizes forced-sparsity headroom in SwiGLU-based reasoning models specifically.\",\n  \"approach\": \"We present Sparsity Interaction Surfaces (SIS), an empirical characterization study with three contributions: theoretical motivation for non-trivial interaction, systematic measurement of the interaction surface across reasoning phases and task families, and a demonstration that phase-aware joint allocation informed by the characterization outperforms additive baselines.\\n\\n(1) Theoretical Motivation for Non-Trivial Interaction (Contribution 1): We formalize the architectural argument for attention-MLP sparsity interaction. Within each transformer block, the causal chain attention_output → residual_add → layer_norm → MLP_input creates a direct information dependency. Drawing on 'Attention Retrieves, MLP Memorizes', we argue that sparsifying the retrieval mechanism (attention) changes the input distribution to the memorization mechanism (MLP). Drawing on 'When Reasoning Meets Compression', we argue this sensitivity is amplified during reasoning, where MLP up projections are disproportionately important. We enumerate three interaction regimes and the conditions under which each should emerge: (a) Compounding (positive cross-partial in degradation): attention drops tokens critical for MLP's retrieval-dependent memorization pathway — expected when attention and MLP process overlapping information at a given phase, so removing capacity from both creates synergistic loss. Exploration phases, where attention broadly retrieves diverse context and MLP integrates it, are hypothesized to be compounding-prone. (b) Complementing (negative cross-partial): MLP compensates for attention's information loss via the residual stream bypass, or attention's redundancy allows MLP to operate on a cleaner signal — expected when the residual stream provides sufficient bypass information. Verification phases, where patterns are repetitive and MLP memorization dominates, may show complementing. (c) Independent (near-zero cross-partial): the two axes process orthogonal information subspaces — validates R-Sparse's additive assumption. This theoretical framework provides testable hypotheses that structure the empirical investigation.\\n\\n(2) Interaction Surface Measurement (Core Contribution): We instrument DeepSeek-R1-Distill-Llama-8B (primary) during inference on reasoning and general benchmarks. For each token, we record per-head attention importance (mean attention entropy, head output norm) and MLP activation magnitudes in SwiGLU intermediate states. We apply forced sparsity using top-k head masking (attention) and magnitude-based activation pruning following ActTail's tail-aware strategy (MLP) for SwiGLU compatibility.\\n\\nSparsity Grid: We sweep a 5×5 grid of (s_attn, s_mlp) in {0%, 20%, 40%, 60%, 80%}² = 25 configurations per phase.\\n\\nPhase Segmentation: We segment outputs using &lt;think>/&lt;/think> boundaries and detect sub-phases — problem-intake (first 10% of thinking tokens), exploration (10-50%), verification (50-90%), and answer-generation — via attention entropy shifts and hidden-state norm dynamics, following ThinKV's phase decomposition methodology.\\n\\nInteraction Analysis: At each phase p, we measure quality Q(s_attn, s_mlp, p) via token-level perplexity and downstream accuracy. The cross-partial derivative d²Q/(ds_attn · ds_mlp) at each phase reveals the interaction regime. We estimate this via finite differences over the grid and test statistical significance across multiple prompts (≥50 per benchmark).\\n\\nTransferability Analysis: We evaluate the interaction surface across three task families to determine whether interaction patterns generalize: mathematical reasoning (AIME 2024, MATH-500), code generation (HumanEval, LiveCodeBench), and general reasoning (MMLU-Pro, MT-Bench). If the interaction pattern (which phases compound vs. complement) is consistent across task families, the characterization becomes a reusable design principle for joint sparsity. If it varies, that establishes task-specificity of phase-aware allocation — either finding is informative and publishable. This transferability test transforms a single-model profiling study into a potentially generalizable finding.\\n\\nSwiGLU Headroom Characterization: As secondary analysis, we measure the forced-sparsity quality curve for DeepSeek-R1-Distill-Llama-8B across sparsity levels, providing the first data point for SwiGLU-based reasoning models. Existing evidence (ActTail at 80%, WAS at 60%) comes from non-reasoning models; whether the Sparsing Law's prediction of lower SwiGLU headroom is amplified or modulated by reasoning-specific activation patterns is an empirical question we resolve.\\n\\n(3) Phase-Aware Joint Allocation Demonstration: Informed by the interaction surface, we demonstrate that phase-specific (s_attn, s_mlp) selection via constrained grid search — exploiting complementing phases for aggressive sparsity, protecting compounding phases — outperforms phase-agnostic baselines. This is explicitly positioned as an application of the characterization demonstrating its practical utility, not a claimed algorithmic contribution. We solve: minimize weighted average latency sum_p f_p · L(s_attn_p, s_mlp_p) subject to Q(s_attn_p, s_mlp_p) >= tau_p for each phase p, where f_p is the token fraction per phase and tau_p are phase-specific quality thresholds (strict for answer tokens, relaxed for exploration tokens). At runtime, a lightweight phase router detects phase via &lt;think>/&lt;/think> boundaries and online attention entropy monitoring from 2-3 layers (<0.1% overhead).\\n\\nBaselines: (1) Dense (no sparsity), (2) R-Sparse uniform joint (phase-agnostic joint, ICLR 2025), (3) TEAL uniform (MLP-only, phase-agnostic), (4) Polar Sparsity uniform (attention-only, phase-agnostic), (5) ActTail global allocation (MLP-only with HT-SR allocation, phase-agnostic), (6) SIS phase-aware joint (ours — demonstration, not method claim).\\n\\nAblations: (a) Per-layer interaction surfaces for layers 1, N/4, N/2, 3N/4, N — testing depth variation, motivated by 'When Reasoning Meets Compression' finding that final-layer MLP is disproportionately important; (b) phase-aware attention-only vs. phase-aware MLP-only vs. phase-aware joint — isolating interaction contribution and directly validating interaction surface predictions; (c) uniform joint at same average sparsity vs. phase-differentiated — isolating phase-awareness value; (d) interaction surface comparison across math/code/general — quantifying transferability.\\n\\nSpeedup Target: 1.3-1.7x average decode speedup over dense baselines, acknowledging that attention and MLP savings add (not multiply), MLP sparsity degrades under batching (per Polar Sparsity), and SwiGLU headroom limits aggressive MLP sparsity. The lower bound (1.3x) reflects conservative joint sparsity; the upper bound (1.7x) requires that thinking tokens (80-95% of generation) tolerate moderate joint sparsity with complementing interaction at some phases. We evaluate on AIME and MATH-500 as primary reasoning benchmarks, plus HumanEval, LiveCodeBench, MMLU-Pro, and MT-Bench for transferability, with wall-clock latency and throughput on H100.\\n\\nFallback Contribution Structure: If profiling reveals near-zero cross-partial derivatives at all phases (confirming the additive assumption), the paper retains three contributions: (a) the first systematic empirical validation that R-Sparse's independence assumption holds — itself a valuable negative result that provides principled justification for current practice, (b) the SwiGLU forced-sparsity headroom characterization for reasoning models extending ActTail/WAS evidence, (c) transferability analysis of phase-specific sparsity profiles across task families. This fallback is positioned for EMNLP Findings.\\n\\nImplementation Strategy: DeepSeek-R1-Distill-Llama-8B's Llama-3.1 architecture is natively supported by Polar Sparsity (attention head selection via Selective Head Attention kernels) and TEAL (MLP magnitude pruning with custom Triton kernels), eliminating codebase integration risk. R-Sparse serves as our primary joint baseline; its core method (rank-aware magnitude thresholding) is algorithmically simple to re-implement.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~170h H100 (interaction surface profiling ~70h with 5x5 grid sweeps across 4 phases x 6 benchmarks for transferability, baseline experiments ~35h for 5 baselines, per-layer ablation ~15h, SwiGLU headroom profiling ~10h, phase-aware demonstration ~15h, ablations ~15h, buffer ~10h)\",\n      \"gpu_utilization\": \"Low-moderate (~25-35%). Researcher time spent analyzing interaction surfaces, computing cross-partial derivatives, testing statistical significance, designing transferability comparisons, and creating visualizations between GPU runs.\",\n      \"timeline\": \"14 days\",\n      \"team\": \"1-2 researchers with systems ML experience\",\n      \"estimated_gpu_cost\": \"$425-510 (170h x $2.50-3.00/hr H100 spot)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~190h H100 (agent runs broader interaction surface sweeps with finer granularity, more extensive transferability coverage across all 6 benchmarks, additional per-layer analysis)\",\n      \"gpu_utilization\": \"Moderate (~45-55%). Agent automates grid sweeps and cross-partial computation; human reviews interaction analysis, validates phase detection accuracy, judges interaction regime thresholds, and guides transferability interpretation.\",\n      \"timeline\": \"12-14 days\",\n      \"team\": \"1 researcher, ~1.5hr/day reviewing interaction surface analysis and validating phase-specific patterns\",\n      \"claude_api_cost\": \"$50-120 (~500-1200 turns for experiment design, analysis, visualization, paper drafting)\",\n      \"estimated_gpu_cost\": \"$475-570 (190h x $2.50-3.00/hr)\",\n      \"risk_note\": \"Primary risk is that interaction effects are negligibly small (near-zero cross-partial derivatives at all phases), making the two axes effectively independent. This would validate R-Sparse's additive assumption but reduce impact to Findings level. Mitigated by: (a) theoretical motivation from causal coupling and functional asymmetry provides a priori reason to expect non-trivial interaction, (b) the characterization and SwiGLU headroom analysis retain publication value regardless, (c) transferability analysis adds a second dimension of contribution.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~190h H100 (comprehensive 5x5 sweeps at all phases across all 6 benchmarks, extensive per-layer ablations, full transferability characterization, SwiGLU headroom profiling)\",\n      \"gpu_utilization\": \"High (~75-85%). Agent runs continuous grid sweeps with automated quality measurement, cross-partial computation, and statistical significance testing.\",\n      \"timeline\": \"10-12 days with 2-4 H100 GPUs available concurrently\",\n      \"team\": \"0 (initial setup ~2hrs, then fully autonomous with periodic human review of interaction regime classifications)\",\n      \"claude_api_cost\": \"$150-300 (~1500-3000 turns for exploration, interaction analysis, transferability evaluation, visualization, paper drafting)\",\n      \"estimated_gpu_cost\": \"$475-570 (190h x $2.50-3.00/hr)\",\n      \"speed_bottleneck\": \"GPU count (2-4 concurrent H100s to parallelize interaction surface sweeps across benchmarks and phases). Single model eliminates architecture integration risk.\",\n      \"risk_note\": \"Integration of Polar Sparsity and TEAL codebases with DeepSeek-R1-Distill-Llama-8B should be straightforward (Llama-3.1 architecture natively supported). Automated numerical validation against dense baselines ensures correctness. Transferability analysis may reveal task-family-specific patterns requiring human interpretation of practical implications.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission: May 25, 2026; commitment: Aug 2, 2026) — Main if interaction effects are significant and transferability analysis strengthens the characterization; Findings if cross-partial is near-zero (valuable negative result validating additive assumption)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference (ICLR 2025)\",\n    \"When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models (ICLR 2026)\",\n    \"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models (arXiv 2601.18091, Jan 2026)\",\n    \"Attention Retrieves, MLP Memorizes: Disentangling Trainable Components in the Transformer (arXiv 2506.01115, June 2025)\",\n    \"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions (EMNLP 2024)\",\n    \"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity (NeurIPS 2025)\",\n    \"Training-Free Activation Sparsity in Large Language Models [TEAL] (ICLR 2025)\",\n    \"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral)\",\n    \"Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for LLMs [WAS] (EMNLP 2025)\",\n    \"ActTail: Global Activation Sparsity in Large Language Models (arXiv 2026)\",\n    \"WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity (arXiv 2026)\",\n    \"Efficient LLMs with AMP: Attention Heads and MLP Pruning (IJCNN 2025)\",\n    \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity (ICML 2025)\",\n    \"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning (NeurIPS 2025 Spotlight)\",\n    \"Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention [EvoSparse] (ACL 2026)\",\n    \"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding (arXiv 2602.07223, Feb 2026)\",\n    \"FASA: Frequency-aware Sparse Attention (ICLR 2026)\",\n    \"RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning (ACL 2025 Findings)\",\n    \"SeerAttention-R: Sparse Attention Adaptation for Long Reasoning (arXiv 2025)\",\n    \"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning (arXiv 2025)\",\n    \"LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention (MLSys 2025)\",\n    \"Scalable Chain of Thoughts via Elastic Reasoning (ICLR 2026)\",\n    \"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning (NeurIPS 2025)\",\n    \"How does Chain of Thought Think? Mechanistic Interpretability of Chain-of-Thought Reasoning with Sparse Autoencoding (arXiv 2507.22928)\",\n    \"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding [SparseSpec] (arXiv 2025)\",\n    \"Nemotron Elastic: Towards Efficient Many-in-One Reasoning LLMs (ICML 2026)\",\n    \"Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction [RAC] (NeurIPS 2025 Workshop on Efficient Reasoning)\",\n    \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling (arXiv 2604.25098, April 2026)\",\n    \"ELAS: Efficient Pre-Training of Low-Rank Large Language Models via 2:4 Activation Sparsity (arXiv 2605.03667, May 2026)\"\n  ],\n  \"description\": \"Current compute sparsity methods for LLM inference treat attention-head and MLP activation sparsity as independent, separable axes — yet the transformer's architecture creates a causal dependency (attention output → residual → layer norm → MLP input) that makes this independence assumption empirically untested. We present Sparsity Interaction Surfaces (SIS), the first systematic empirical characterization of how attention and MLP sparsity interact across reasoning phases. We ground our investigation in a theoretical motivation: 'Attention Retrieves, MLP Memorizes' (arXiv 2506.01115) shows these components serve fundamentally different functions, so sparsifying retrieval changes what memorization can operate on; 'When Reasoning Meets Compression' (ICLR 2026) shows MLP up projections are critically important for reasoning; 'Interpreting Context Look-ups in Transformers' (EMNLP 2024) demonstrates causal coupling where specific attention heads trigger downstream MLP neurons. We enumerate three possible interaction regimes — compounding (joint degradation exceeds individual sum), complementing (joint is better than expected), and independent (R-Sparse's additive assumption holds) — and measure which regime dominates at each reasoning phase by sweeping a 5x5 grid of (attention_sparsity, mlp_sparsity) levels during problem-intake, exploration, verification, and answer-generation in DeepSeek-R1-Distill-Llama-8B. We test transferability across three task families (math, code, general reasoning) to determine whether interaction patterns generalize. As a demonstration of the characterization's utility, we show that phase-aware joint allocation guided by the interaction surface achieves 1.3-1.7x decode speedup with <3% accuracy loss, outperforming phase-agnostic baselines. The work additionally contributes the first characterization of forced-sparsity headroom in SwiGLU-based reasoning models. The paper retains value under all outcomes: significant interaction effects motivate phase-aware joint design (Main); near-zero cross-partial validates R-Sparse's additive assumption — itself a useful negative result — plus the SwiGLU headroom and transferability analyses (Findings). Primary target: EMNLP 2026 (ARR May 25, 2026).\",\n  \"project_name\": \"sparsity_interaction_surfaces\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"FATAL: Wrong venue — user requires EMNLP 2026 (ARR deadline May 25, 2026), but idea targets AAAI 2027 (Aug 2), ICLR 2027 (Sep 24), and MLSys 2027 (~Oct 31). Must retarget to EMNLP 2026.\", \"FATAL: GPU budget violation — user constraint is ≤200 H100-hours total, but the manual estimate alone is ~300h (50% over). The approach must be simplified to fit within 200h, e.g., by dropping custom CUDA kernel development and using existing sparse kernels from Polar Sparsity/TEAL/FlashInfer.\", \"FATAL: Timeline violation — user constraint is ≤16 days, but even the auto_research estimate is 2-4 weeks. Custom CUDA kernel development is the primary bottleneck and should be eliminated in favor of existing kernel infrastructure.\", \"FATAL: Benchmark mismatch — user specifies perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench and wall-clock/throughput on H100. The idea evaluates only on AIME, MATH500, LiveCodeBench. Must add all required benchmarks.\", \"Novelty concern: ThinKV (ICLR 2026 Oral) already identifies 3 reasoning phases (Reasoning, Execution, Transition) with distinct sparsity profiles via KDE-based classification. PAJS's phase detection is closely related. Generator must explicitly differentiate from ThinKV's thought-type classification.\", \"Novelty concern: AMP (IJCNN 2025) already performs joint attention-head and MLP pruning. The only differentiation is phase-awareness, which is borrowed from ThinKV/Elastic Reasoning.\", \"Feasibility risk: ThinKV found that backtracking/transition tokens have HIGH sparsity but are critically important — 'removing them causes the model to loop endlessly.' This directly challenges the assumption that exploration/backtracking phases can tolerate aggressive sparsity.\", \"Model name errors: 'DeepSeek-R1-Distill-Qwen3-8B' does not exist — the correct model is 'DeepSeek-R1-0528-Qwen3-8B'. 'Qwen3-8B-Thinking' is not a separate model — Qwen3-8B supports thinking mode natively via &lt;think> tags.\", \"Missing competing work: Weight-Aware Activation Sparsity (WAS, EMNLP 2025) applies inter-block sparsity with constrained Bayesian optimization — relevant baseline not discussed. LoopServe (arXiv 2025) does dual-phase adaptive inference — adjacent work not mentioned.\", \"The resource_estimate section provides manual/HIL/auto modes, but none satisfy user constraints. The user's 200 H100-hour budget and 16-day timeline are hard constraints that must be met, not approximated.\"]\nFeedback: This idea has a promising direction but fundamentally fails to meet the user's constraints. To revise:\n\n1. **Retarget to EMNLP 2026** (ARR May 25, 2026). This is non-negotiable per user requirements.\n\n2. **Fit within 200 H100-hours and 16 days**: Drop custom CUDA kernel development entirely. Instead, build on existing sparse inference kernels from Polar Sparsity (open-source), TEAL (GitHub: FasterDecoding/TEAL), Twilight (GitHub: tsinghua-ideal/Twilight), and FlashInfer. The phase router can use Python-level switching between pre-configured sparsity settings — no fused kernel needed for a paper contribution. This alone cuts 100+ hours and weeks of development.\n\n3. **Add required benchmarks**: The user specifies perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench, plus wall-clock and throughput on H100. You can keep AIME/MATH500 as supplementary reasoning benchmarks but MUST include the required set.\n\n4. **Sharpen novelty against ThinKV**: ThinKV already detects thought types (R/E/T) with sparsity-based classification. Your phase router must be clearly differentiated — perhaps by operating on compute sparsity (attention heads + MLP activations) rather than KV cache, and by showing that compute sparsity profiles differ from KV cache sparsity profiles across phases.\n\n5. **Address backtracking safety**: ThinKV showed backtracking tokens are sparsity-high but importance-critical. Your approach must demonstrate that MLP/attention-head sparsity can be applied safely to these tokens even when KV cache sparsity cannot.\n\n6. **Fix model names**: Use 'DeepSeek-R1-0528-Qwen3-8B' and 'Qwen3-8B' (with thinking mode enabled), not the nonexistent model names.\n\n7. **Simplify scope**: Given 200 H100-hours, focus on profiling (phase characterization) + phase-aware application of existing sparsity methods (Polar Sparsity + TEAL) with a lightweight Python-level phase classifier. Save kernel engineering for a follow-up systems paper. This makes the contribution more of a method/analysis paper suitable for EMNLP's Efficient Methods track.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"Feasibility risk: Polar Sparsity GitHub (susavlsh10/Polar-Sparsity) has only 6 commits and supports only OPT and Llama models — no Qwen3 support. TEAL (FasterDecoding/TEAL) self-describes as 'just a proof of concept' with FP16-only support and only supports Llama/Mistral. Adapting BOTH codebases to Qwen3-8B / DeepSeek-R1-0528-Qwen3-8B within the 10-14 day timeline is a major unacknowledged risk.\", \"Manual timeline violation: manual mode estimates '4-6 weeks', which exceeds the user's hard 16-day constraint.\", \"Methodological thinness: The core method reduces to 'compose Polar Sparsity + TEAL + logistic classifier on pooled hidden states.' A logistic classifier on hidden state norms with <0.1% overhead is simple engineering, not a method contribution. The phase detection using &lt;think>/&lt;/think> boundaries is trivial, and attention entropy is closely related to ThinKV's KDE-based classification — differentiation is insufficient.\", \"Missing competitor: 'Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction' (RAC, NeurIPS 2025) demonstrates that reasoning models require reasoning-aware calibration for sparsity/pruning. This is a relevant baseline showing that phase/reasoning awareness matters for sparsity, and should be discussed.\", \"Missing competitor: FASA (ICLR 2026) performs frequency-aware sparse attention evaluated on LongCoT reasoning tasks with 2.56x speedup on AIME24. While KV-focused, it's a relevant phase-aware attention optimization baseline.\", \"Speedup target may be over-optimistic: Claiming 2-3x average decode speedup by composing two methods that individually achieve 1.5-2.2x requires multiplicative stacking of attention + MLP sparsity. At the high sparsity levels needed (50-60% head + 50% MLP), quality degradation may prevent achieving both simultaneously — especially since Polar Sparsity's 2.2x is for attention-only at large batch sizes, not decode.\", \"The backtracking-token compute tolerance hypothesis is high-risk: ThinKV explicitly warns that backtracking tokens 'cannot be removed without causing infinite loops.' While compute sparsity preserves tokens in context, applying aggressive compute sparsity (fewer heads, sparser MLP) to these critical tokens could still degrade the quality of the backtracking signal, leading to extended or failed reasoning chains. If this hypothesis fails, one of the three claimed contributions is lost.\", \"Missing analysis of recent work showing CoT tokens already exhibit higher activation sparsity (arxiv 2507.22928): If thinking tokens are already naturally more sparse in their activations, the headroom for additional compute sparsity during thinking phases may be smaller than assumed.\"]\nFeedback: The revision successfully addressed Round 1's fatal issues (venue, benchmarks, model names, GPU budget). The gap is real and the direction timely. However, four issues need attention before this can pass:\n\n1. **Mitigate the codebase compatibility risk** (most critical): Neither Polar Sparsity nor TEAL supports Qwen3 natively. Options: (a) Switch to Llama-3.1-8B-Instruct with reasoning fine-tuning, which both codebases support natively, reducing integration risk dramatically. You can keep DeepSeek-R1-0528-Qwen3-8B as a secondary model with custom integration. (b) Alternatively, acknowledge this risk explicitly with a fallback plan (e.g., re-implement magnitude-based MLP pruning for Qwen3 directly rather than depending on TEAL's codebase, since TEAL's core method is simple magnitude thresholding).\n\n2. **Strengthen the method contribution**: A logistic classifier on pooled hidden states is too thin for a method paper. Consider: (a) Formulating the phase-specific sparsity budget selection as an optimization problem (e.g., minimize quality loss subject to per-phase sparsity budgets, solved via the profiling data); (b) Analyzing the interaction effects between attention-head and MLP sparsity — do they compound, interfere, or complement? This cross-component analysis would be a genuine methodological insight; (c) Providing theoretical motivation for why compute sparsity should behave differently from KV cache sparsity across phases.\n\n3. **Add RAC (NeurIPS 2025) and FASA (ICLR 2026) to the landscape**: RAC demonstrates reasoning-aware pruning calibration and is a natural baseline. FASA's phase-aware attention on reasoning benchmarks is relevant context. Also discuss the finding from arxiv 2507.22928 that CoT tokens already show higher activation sparsity — this could support or limit your approach.\n\n4. **Fix manual timeline**: Must be ≤16 days per user constraint. Consider scoping to 2 weeks with reduced ablation budget.\n\n5. **Temper speedup claims**: State '1.5-2.5x average decode speedup' rather than '2-3x' to be more realistic about multiplicative sparsity composition.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"Method contribution is still primarily compositional: the core approach is applying existing sparsity methods (Polar Sparsity for attention, TEAL for MLP) with a phase classifier (borrowing from ThinKV's reasoning-phase decomposition) and Bayesian optimization (borrowing from WAS). The interaction analysis (cross-partial derivatives d²Q/ds_attn·ds_mlp) is the most genuinely novel element but is buried as one sub-point rather than being the centerpiece.\", \"Natural sparsity headroom risk insufficiently addressed: arxiv 2507.22928 shows CoT induces higher activation sparsity. While the idea notes this was on Pythia-2.8B (non-SwiGLU), it only frames this as a 'research question' without a concrete plan for what the paper contributes if profiling reveals limited headroom for forced sparsity on top of natural sparsity. If thinking tokens already tolerate 60% natural sparsity, the marginal gain from phase-aware allocation may be negligible vs. phase-agnostic methods.\", \"Speedup upper bound of 2.5x may still be unrealistic: TEAL achieves 1.5-1.8x for MLP-only, and Polar Sparsity achieves 2.2x for attention-only at large batch sizes. Joint composition doesn't multiply — attention and MLP are in series, so savings add rather than multiply. With evidence showing practical speedups consistently below theoretical (CHESS reports structured sparsity degrades under batching; SwiGLU limits sparsity ceilings), a more honest range would be 1.3-2.0x.\", \"Missing relevant work: 'Doing More With Less: Revisiting Effectiveness of LLM Pruning for Test-Time Scaling' (arXiv 2604.25098, April 2026) shows unstructured pruning can maintain or even improve test-time scaling performance in reasoning models (Qwen3-8B, s1.1-7B). While this is weight pruning (not activation sparsity), it demonstrates that reasoning-aware pruning analysis is an active concurrent direction and should be discussed.\", \"Scope may be too broad for 14 days with immature codebases: profiling 2 models × 8+ benchmarks × 4 baselines + implementing the optimization framework + phase detection + ablations is extremely ambitious. Consider dropping Qwen3-8B entirely and doing a deeper, more thorough analysis on DeepSeek-R1-Distill-Llama-8B alone — one model studied deeply is more convincing than two models studied superficially with integration bugs.\", \"RAC is cited as 'NeurIPS 2025' but evidence suggests it may be a NeurIPS 2025 Workshop paper (1st Workshop on Efficient Reasoning) rather than main conference — the neurips.cc URL pattern (virtual/2025/126571 vs. virtual/2025/poster/...) suggests workshop. Minor but should be verified and corrected if needed.\", \"Bayesian optimization over 8 parameters (4 phases × 2 sparsity dimensions) may be over-engineered — grid search or random search would likely suffice for such a low-dimensional space, and claiming Bayesian optimization as a methodological contribution for 8 parameters weakens the paper.\"]\nFeedback: The idea has improved substantially across rounds — the gap is genuine, the landscape is comprehensive, and the constraints are met. To push this to passing quality, three changes would make the biggest difference:\n\n1. **Elevate the interaction analysis as THE core contribution**: The cross-partial derivative analysis of attention × MLP sparsity across reasoning phases is genuinely novel — no one has characterized whether these two sparsity axes compound or complement at different reasoning stages. Make this the centerpiece of the paper, not component (2b). Reframe the paper as: 'We provide the first characterization of how attention-head and MLP activation sparsity interact across reasoning phases, and show that this interaction structure enables phase-specific joint optimization that outperforms phase-agnostic methods.' This shifts the contribution from 'we combined existing methods' to 'we discovered a previously unknown phenomenon and exploited it.'\n\n2. **Concretely address the natural sparsity headroom risk**: Add a fallback contribution structure. If profiling shows limited headroom: (a) the interaction analysis itself is still a contribution (showing when joint sparsity helps vs. hurts), (b) the characterization of compute vs. KV cache sparsity profiles is valuable even if speedups are modest, (c) a negative result on backtracking token compute tolerance is publishable. State this explicitly so reviewers see the paper has value regardless of the speedup numbers.\n\n3. **Narrow scope to one model, deeper analysis**: Drop Qwen3-8B and focus entirely on DeepSeek-R1-Distill-Llama-8B. This eliminates codebase integration risk for a second architecture, frees ~40-50 H100-hours for more thorough profiling and ablations on the primary model, and allows deeper analysis of the interaction surface. You can note Qwen3-8B generalization as future work. One model studied thoroughly > two models studied shallowly.\n\nAdditional improvements: (a) Reduce speedup claims to 1.3-2.0x. (b) Replace Bayesian optimization with simpler grid search over the 8-parameter space — it's more honest and equally effective at this dimensionality. (c) Add 'Doing More With Less' (arXiv 2604.25098) to the landscape. (d) Verify RAC's venue (workshop vs. main conference).\n\n### Round 4 review\nVerdict: revise\nIssues: [\"Impact is conditional on empirical findings: if the cross-partial derivative is near-zero at all phases (axes are independent), the phase-aware allocation becomes unjustified and the paper reduces to a characterization study confirming R-Sparse's additive assumption holds. While the generator acknowledges this with a fallback structure, the fallback contributions (characterization + backtracking analysis) are better suited to EMNLP Findings than Main.\", \"The 'method' contribution (grid search over 8 parameters to select phase-specific sparsity levels) is engineering application of the characterization, not a novel algorithm. For EMNLP Efficient Methods track, reviewers expect algorithmic contributions — a systematic profiling study with grid search may not meet that bar for Main conference.\", \"SwiGLU headroom risk is more severe than acknowledged: Sparsing Law (ICML 2025) shows SwiGLU models have substantially lower natural activation sparsity than ReLU. The CoT SAE sparsity result (arxiv 2507.22928) was on Pythia (non-SwiGLU). If forced sparsity in DeepSeek-R1-Distill-Llama-8B (SwiGLU) causes steep quality drops at even moderate levels, the 2D interaction surface will be trivially shaped (compounding everywhere at practical sparsity levels), making the characterization less informative.\", \"Missing relevant concurrent work: (1) 'When Reasoning Meets Compression' (ICLR 2026) explicitly studies how compression affects reasoning in DeepSeek-R1, finding MLP up projection in the final layer is critically important — directly relevant to understanding MLP sparsity sensitivity in reasoning models. (2) 'From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models' (arXiv 2601.18091, Jan 2026) shows width pruning is more robust than depth pruning for reasoning tasks — provides context for MLP vs. attention sparsity sensitivity.\", \"Speedup upper bound of 2.0x may still be optimistic: attention and MLP are in series (savings add, not multiply), MLP sparsity degrades under batching (Polar Sparsity), and practical speedups consistently fall below theoretical. With Polar Sparsity's attention-only result at 2.2x achieved at large batch sizes (not batch=1 decode typical for reasoning), the joint 2.0x at decode requires very optimistic assumptions about complementing interactions. Consider stating 1.3-1.7x for credibility.\", \"No theoretical motivation for why the interaction should be non-trivial: the attention output feeds into MLP input within each transformer block (causal dependency), so sparsifying attention should change the representation quality seen by MLP, potentially affecting MLP sparsity tolerance. This architectural argument is absent from the proposal but would significantly strengthen the case that the interaction surface will be informative.\"]\nFeedback: The idea has improved substantially through 4 rounds — the gap is genuine, the landscape is comprehensive, and the constraints are met. The interaction surface characterization is a real contribution that no one has done. To push this over the threshold, three specific changes would help most:\n\n1. **Reposition as a characterization + analysis paper, not a method paper**: The strongest element is the interaction surface discovery, not the phase-aware allocation (which is grid search). For EMNLP, frame the contribution as: 'We provide the first empirical characterization of how attention-head and MLP activation sparsity interact across reasoning phases, revealing [compounding/complementing/independent] patterns that provide principled guidance for joint sparsity design.' This framing is more honest and more likely to satisfy reviewers than claiming a novel method. Target Findings explicitly if the interaction effects are moderate.\n\n2. **Add theoretical motivation for non-trivial interaction**: The causal dependency within each transformer block (attention output → layer norm → MLP input) means that reducing attention quality via head sparsification changes the representation quality fed to MLP. If attention sparsity causes the residual stream to lose information about certain tokens, MLP sparsity on top of that could be either catastrophic (compounding: MLP can't recover what attention lost) or benign (complementing: if MLP was only refining the same information attention already dropped). This architectural argument should be made explicit — it strengthens the a priori case that the interaction will be non-trivial and differentiates from studies that treat components as independent.\n\n3. **Strengthen impact with a transferability test**: Can the interaction surface shape (which phases compound vs. complement) transfer across different prompt types (math vs. code vs. general reasoning)? If the interaction pattern is consistent across tasks, the characterization becomes a reusable design principle. If it varies, that's also informative — it means phase-aware allocation must be task-specific. Either way, testing transferability transforms a single-model profiling study into a generalizable finding. This could be done within the existing 150h budget by allocating ~20h to testing on additional benchmark categories.\n\n4. **Cite missing concurrent work**: Add 'When Reasoning Meets Compression' (ICLR 2026) — its finding that MLP up projection in the final layer is critically important for reasoning directly motivates understanding MLP sparsity sensitivity at different reasoning phases. Add 'From LLMs to LRMs' (arXiv 2601.18091) for context on structural pruning in reasoning models.\n\n5. **Tighten speedup claims to 1.3-1.7x**: This is more credible given that (a) attention and MLP savings add rather than multiply, (b) MLP sparsity degrades under batching, and (c) the SwiGLU headroom concern limits aggressive MLP sparsity. A conservative claim that is met is far more convincing than an optimistic claim that falls short.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-12T00:19:14.687Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T00:19:14.687Z",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-12T00:19:14.732Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-11 (UTC).**

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

## Idea under review (round 5/10)
{
  "title": "Sparsity Interaction Surfaces: Characterizing How Attention and MLP Activation Sparsity Interact Across Reasoning Phases",
  "core_problem": "Reasoning models exhibit distinct computational patterns during thinking vs. answer phases, yet all existing compute sparsity methods — whether targeting attention heads (Polar Sparsity, Twilight), MLP activations (TEAL, WAS, ActTail), or both jointly (R-Sparse, AMP) — treat attention and MLP sparsity as independent, separable axes. Within each transformer block, however, a causal dependency exists: attention output flows through the residual stream and layer normalization before becoming MLP input, creating a direct information pathway. Recent mechanistic work establishes that these components serve fundamentally different functions: 'Attention Retrieves, MLP Memorizes' (arXiv 2506.01115) shows attention performs contextual retrieval while MLP stores learned patterns, and 'Interpreting Context Look-ups in Transformers' (EMNLP 2024) empirically demonstrates that specific attention heads causally trigger downstream MLP neurons. This functional asymmetry and causal coupling means that sparsifying the retrieval mechanism directly changes what the memorization mechanism has to work with — yet no existing work characterizes the cross-partial derivative d²Q/(ds_attn · ds_mlp), i.e., whether jointly sparsifying attention and MLP degrades quality more than expected from individual axes (compounding), less than expected (complementing), or as expected (independent). This interaction question is distinct from KV cache sparsity and from individual-axis sparsity. R-Sparse (ICLR 2025) applies joint sparsity but assumes additivity without measuring interaction effects. 'When Reasoning Meets Compression' (ICLR 2026) shows MLP up projections in the final layer are critically important for reasoning — protecting just 2% of excessively compressed weights raises accuracy by 6.57% — but does not study how attention sparsity modulates this MLP sensitivity. The field lacks the empirical characterization needed to determine whether the additive assumption underlying joint methods is justified or whether it silently compounds errors at certain reasoning phases.",
  "opportunity": "Three converging lines of evidence provide both theoretical motivation and practical urgency for characterizing the attention-MLP sparsity interaction surface: (1) Causal coupling with functional asymmetry: The transformer block's sequential structure (attention → residual → layer norm → MLP) creates a direct dependency where attention output quality determines MLP input distribution. 'Attention Retrieves, MLP Memorizes' shows these components serve distinct roles — attention retrieves contextual information, MLP memorizes learned patterns — so sparsifying retrieval changes what memorization can operate on. Three interaction regimes are theoretically possible: if attention drops tokens critical for MLP's memorization role, joint sparsity compounds (positive cross-partial in degradation); if MLP can compensate via the residual stream bypass, joint sparsity complements (negative cross-partial); if the dropped information was redundant to MLP processing, the axes are independent (near-zero cross-partial). Which regime dominates — and whether it varies across reasoning phases — is an empirical question with direct implications for system design. (2) Reasoning-specific sensitivity asymmetry: 'When Reasoning Meets Compression' (ICLR 2026) shows MLP up projections are disproportionately important for reasoning accuracy, while 'From LLMs to LRMs' (arXiv 2601.18091) shows width pruning (MLP-like) is more robust than depth pruning (attention-like) for reasoning tasks across 17 benchmarks. These asymmetric sensitivity profiles suggest the interaction surface is unlikely to be flat. Polar Sparsity (NeurIPS 2025) showed attention head sparsity is batch-invariant while MLP sparsity degrades with batching — further evidence of fundamentally different scaling properties that likely produce phase-dependent interactions. (3) Practical urgency without empirical grounding: Reasoning models (DeepSeek-R1, Qwen3) are mainstream with thinking tokens comprising 80-95% of generation and decode costs 5-10x higher than standard models. ThinKV (ICLR 2026 Oral) proved KV cache sparsity varies dramatically across reasoning phases, but compute sparsity interactions across phases remain uncharacterized. The Sparsing Law (ICML 2025) establishes that SwiGLU models have substantially lower natural activation sparsity than ReLU models, and existing forced-sparsity evidence (ActTail, WAS) comes from non-reasoning models — whether SwiGLU-based reasoning models retain sufficient headroom for practical joint sparsity is an open question our profiling directly answers. 'Thinking Tokens are Information Peaks' (NeurIPS 2025) showed mutual information peaks are sparse (<5% of tokens) at transition/reflection points, suggesting qualitatively different compute requirements at different reasoning stages.",
  "landscape": "Attention-head sparsity: Polar Sparsity (NeurIPS 2025) achieves 2.2x decode speedup via batch-invariant head-level sparsity; critically demonstrates that MLP union sparsity vanishes under batching while attention head sparsity remains stable — evidence the two axes have fundamentally different scaling properties. Twilight (NeurIPS 2025 Spotlight) enables adaptive attention budget via hierarchical top-p pruning with 3.9x decode acceleration but is attention-only. EvoSparse (ACL 2026) models token importance as an evolving process for dynamic sparse attention but is attention-only. RaaS (ACL 2025 Findings) identifies milestone-token attention patterns in reasoning but is attention-only and phase-agnostic. SeerAttention-R learns decode-time sparse attention with 9x speedup at 90% sparsity but requires training and is attention-only. SpecAttn (arXiv 2602.07223, Feb 2026) co-designs sparse attention with self-speculative decoding, achieving 2.81x throughput — attention-only, no MLP interaction. MLP activation sparsity: TEAL (ICLR 2025) achieves 1.5-1.8x MLP-only speedup via magnitude pruning at 40-50% sparsity. WAS (EMNLP 2025) improves over TEAL with weight-aware scoring and Bayesian-optimized inter-block allocation, achieving 1.68x at 60% sparsity. WiSparse (arXiv 2026) advances MLP sparsity with mixed-granularity allocation, preserving 97% of dense performance at 50% sparsity. ActTail (arXiv 2026) applies HT-SR theory for global sparsity allocation across projections, reducing perplexity by 21.8% at 80% sparsity vs. TEAL's uniform allocation — the most recent MLP sparsity method confirming meaningful headroom in SwiGLU models. Joint attention-MLP sparsity: R-Sparse (ICLR 2025) is the most relevant baseline: applies rank-aware activation sparsity to both attention and MLP jointly at 50% model-wide level with 1.43x speedup, but treats the two axes as additive without measuring interaction effects and applies the same sparsity uniformly across all decode steps. AMP (IJCNN 2025) jointly prunes attention heads and MLP but applies static uniform pruning without runtime adaptation or interaction analysis. Reasoning model compression: 'When Reasoning Meets Compression' (ICLR 2026, arXiv 2504.02010) benchmarks compressed DeepSeek-R1 across reasoning tasks and identifies MLP up projection in the final layer as critically important — protecting 2% of excessively compressed weights raises accuracy by 6.57%. Directly motivates understanding how attention sparsity modulates MLP sensitivity in reasoning models. 'From LLMs to LRMs' (arXiv 2601.18091, Jan 2026) evaluates static/dynamic depth/width pruning across 17 tasks, finding width pruning more robust than depth pruning for reasoning, and static pruning better than dynamic for reasoning preservation — provides context for MLP vs. attention sparsity sensitivity asymmetry. RAC (NeurIPS 2025 Workshop) demonstrates reasoning-aware calibration for weight pruning via CoT reconstruction at 50% weight sparsity. 'Doing More With Less' (arXiv 2604.25098, April 2026) shows unstructured weight pruning can maintain or improve test-time scaling in reasoning models. Mechanistic understanding: 'Attention Retrieves, MLP Memorizes' (arXiv 2506.01115, June 2025) disentangles transformer components: random attention (frozen Q,K) still works competitively while frozen MLPs cause the biggest performance drop, establishing a functional basis for asymmetric sparsity tolerance and providing theoretical grounding for why sparsifying attention changes MLP's operating conditions. 'Interpreting Context Look-ups in Transformers' (EMNLP 2024, arXiv 2402.15055) shows specific attention heads causally trigger downstream MLP neurons — direct empirical evidence that sparsifying attention affects MLP processing, the mechanistic basis for non-trivial interaction. 'Thinking Tokens are Information Peaks' (NeurIPS 2025) shows MI peaks are sparse (<5% of tokens) at transition/reflection points. Reasoning phase awareness: ThinKV (ICLR 2026 Oral) applies thought-adaptive KV compression using KDE-based phase classification with <5% KV cache usage — targets memory, not compute, but establishes that reasoning phases have distinct sparsity profiles. LazyEviction (arXiv 2025) reveals Token Importance Recurrence — tokens regain high attention after multiple decode steps — relevant to understanding phase-dependent attention patterns. Elastic Reasoning (ICLR 2026) separates thinking and solution budgets but via different model sizes, not sparsity. Sparsity foundations: Sparsing Law (ICML 2025) establishes that SiLU/SwiGLU models have fundamentally lower natural activation sparsity than ReLU models, with convergent power-law relationships — directly relevant to headroom assessment. ELAS (arXiv 2605.03667, May 2026) combines low-rank + 2:4 activation sparsity with Squared-ReLU reaching 84-98% sparsity, but uses a different activation function. arXiv 2507.22928 shows CoT induces higher SAE feature sparsity in Pythia — relevant but on small non-SwiGLU models. Other complementary work: FASA (ICLR 2026) performs frequency-aware sparse attention achieving 2.56x on AIME24. LServe (MLSys 2025) unifies sparse attention for prefill+decode. SparseSpec (arXiv 2025) accelerates reasoning inference via sparse self-speculative decoding. Nemotron Elastic (ICML 2026) enables elastic inference. Gap: No existing work (1) characterizes the interaction surface between attention-head and MLP activation sparsity across reasoning phases, (2) provides theoretical motivation grounded in the attention→MLP causal dependency and functional asymmetry for why this interaction should be non-trivial, (3) tests transferability of interaction patterns across task families (math, code, general reasoning), or (4) characterizes forced-sparsity headroom in SwiGLU-based reasoning models specifically.",
  "approach": "We present Sparsity Interaction Surfaces (SIS), an empirical characterization study with three contributions: theoretical motivation for non-trivial interaction, systematic measurement of the interaction surface across reasoning phases and task families, and a demonstration that phase-aware joint allocation informed by the characterization outperforms additive baselines.\n\n(1) Theoretical Motivation for Non-Trivial Interaction (Contribution 1): We formalize the architectural argument for attention-MLP sparsity interaction. Within each transformer block, the causal chain attention_output → residual_add → layer_norm → MLP_input creates a direct information dependency. Drawing on 'Attention Retrieves, MLP Memorizes', we argue that sparsifying the retrieval mechanism (attention) changes the input distribution to the memorization mechanism (MLP). Drawing on 'When Reasoning Meets Compression', we argue this sensitivity is amplified during reasoning, where MLP up projections are disproportionately important. We enumerate three interaction regimes and the conditions under which each should emerge: (a) Compounding (positive cross-partial in degradation): attention drops tokens critical for MLP's retrieval-dependent memorization pathway — expected when attention and MLP process overlapping information at a given phase, so removing capacity from both creates synergistic loss. Exploration phases, where attention broadly retrieves diverse context and MLP integrates it, are hypothesized to be compounding-prone. (b) Complementing (negative cross-partial): MLP compensates for attention's information loss via the residual stream bypass, or attention's redundancy allows MLP to operate on a cleaner signal — expected when the residual stream provides sufficient bypass information. Verification phases, where patterns are repetitive and MLP memorization dominates, may show complementing. (c) Independent (near-zero cross-partial): the two axes process orthogonal information subspaces — validates R-Sparse's additive assumption. This theoretical framework provides testable hypotheses that structure the empirical investigation.\n\n(2) Interaction Surface Measurement (Core Contribution): We instrument DeepSeek-R1-Distill-Llama-8B (primary) during inference on reasoning and general benchmarks. For each token, we record per-head attention importance (mean attention entropy, head output norm) and MLP activation magnitudes in SwiGLU intermediate states. We apply forced sparsity using top-k head masking (attention) and magnitude-based activation pruning following ActTail's tail-aware strategy (MLP) for SwiGLU compatibility.\n\nSparsity Grid: We sweep a 5×5 grid of (s_attn, s_mlp) in {0%, 20%, 40%, 60%, 80%}² = 25 configurations per phase.\n\nPhase Segmentation: We segment outputs using &lt;think>/&lt;/think> boundaries and detect sub-phases — problem-intake (first 10% of thinking tokens), exploration (10-50%), verification (50-90%), and answer-generation — via attention entropy shifts and hidden-state norm dynamics, following ThinKV's phase decomposition methodology.\n\nInteraction Analysis: At each phase p, we measure quality Q(s_attn, s_mlp, p) via token-level perplexity and downstream accuracy. The cross-partial derivative d²Q/(ds_attn · ds_mlp) at each phase reveals the interaction regime. We estimate this via finite differences over the grid and test statistical significance across multiple prompts (≥50 per benchmark).\n\nTransferability Analysis: We evaluate the interaction surface across three task families to determine whether interaction patterns generalize: mathematical reasoning (AIME 2024, MATH-500), code generation (HumanEval, LiveCodeBench), and general reasoning (MMLU-Pro, MT-Bench). If the interaction pattern (which phases compound vs. complement) is consistent across task families, the characterization becomes a reusable design principle for joint sparsity. If it varies, that establishes task-specificity of phase-aware allocation — either finding is informative and publishable. This transferability test transforms a single-model profiling study into a potentially generalizable finding.\n\nSwiGLU Headroom Characterization: As secondary analysis, we measure the forced-sparsity quality curve for DeepSeek-R1-Distill-Llama-8B across sparsity levels, providing the first data point for SwiGLU-based reasoning models. Existing evidence (ActTail at 80%, WAS at 60%) comes from non-reasoning models; whether the Sparsing Law's prediction of lower SwiGLU headroom is amplified or modulated by reasoning-specific activation patterns is an empirical question we resolve.\n\n(3) Phase-Aware Joint Allocation Demonstration: Informed by the interaction surface, we demonstrate that phase-specific (s_attn, s_mlp) selection via constrained grid search — exploiting complementing phases for aggressive sparsity, protecting compounding phases — outperforms phase-agnostic baselines. This is explicitly positioned as an application of the characterization demonstrating its practical utility, not a claimed algorithmic contribution. We solve: minimize weighted average latency sum_p f_p · L(s_attn_p, s_mlp_p) subject to Q(s_attn_p, s_mlp_p) >= tau_p for each phase p, where f_p is the token fraction per phase and tau_p are phase-specific quality thresholds (strict for answer tokens, relaxed for exploration tokens). At runtime, a lightweight phase router detects phase via &lt;think>/&lt;/think> boundaries and online attention entropy monitoring from 2-3 layers (<0.1% overhead).\n\nBaselines: (1) Dense (no sparsity), (2) R-Sparse uniform joint (phase-agnostic joint, ICLR 2025), (3) TEAL uniform (MLP-only, phase-agnostic), (4) Polar Sparsity uniform (attention-only, phase-agnostic), (5) ActTail global allocation (MLP-only with HT-SR allocation, phase-agnostic), (6) SIS phase-aware joint (ours — demonstration, not method claim).\n\nAblations: (a) Per-layer interaction surfaces for layers 1, N/4, N/2, 3N/4, N — testing depth variation, motivated by 'When Reasoning Meets Compression' finding that final-layer MLP is disproportionately important; (b) phase-aware attention-only vs. phase-aware MLP-only vs. phase-aware joint — isolating interaction contribution and directly validating interaction surface predictions; (c) uniform joint at same average sparsity vs. phase-differentiated — isolating phase-awareness value; (d) interaction surface comparison across math/code/general — quantifying transferability.\n\nSpeedup Target: 1.3-1.7x average decode speedup over dense baselines, acknowledging that attention and MLP savings add (not multiply), MLP sparsity degrades under batching (per Polar Sparsity), and SwiGLU headroom limits aggressive MLP sparsity. The lower bound (1.3x) reflects conservative joint sparsity; the upper bound (1.7x) requires that thinking tokens (80-95% of generation) tolerate moderate joint sparsity with complementing interaction at some phases. We evaluate on AIME and MATH-500 as primary reasoning benchmarks, plus HumanEval, LiveCodeBench, MMLU-Pro, and MT-Bench for transferability, with wall-clock latency and throughput on H100.\n\nFallback Contribution Structure: If profiling reveals near-zero cross-partial derivatives at all phases (confirming the additive assumption), the paper retains three contributions: (a) the first systematic empirical validation that R-Sparse's independence assumption holds — itself a valuable negative result that provides principled justification for current practice, (b) the SwiGLU forced-sparsity headroom characterization for reasoning models extending ActTail/WAS evidence, (c) transferability analysis of phase-specific sparsity profiles across task families. This fallback is positioned for EMNLP Findings.\n\nImplementation Strategy: DeepSeek-R1-Distill-Llama-8B's Llama-3.1 architecture is natively supported by Polar Sparsity (attention head selection via Selective Head Attention kernels) and TEAL (MLP magnitude pruning with custom Triton kernels), eliminating codebase integration risk. R-Sparse serves as our primary joint baseline; its core method (rank-aware magnitude thresholding) is algorithmically simple to re-implement.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~170h H100 (interaction surface profiling ~70h with 5x5 grid sweeps across 4 phases x 6 benchmarks for transferability, baseline experiments ~35h for 5 baselines, per-layer ablation ~15h, SwiGLU headroom profiling ~10h, phase-aware demonstration ~15h, ablations ~15h, buffer ~10h)",
      "gpu_utilization": "Low-moderate (~25-35%). Researcher time spent analyzing interaction surfaces, computing cross-partial derivatives, testing statistical significance, designing transferability comparisons, and creating visualizations between GPU runs.",
      "timeline": "14 days",
      "team": "1-2 researchers with systems ML experience",
      "estimated_gpu_cost": "$425-510 (170h x $2.50-3.00/hr H100 spot)"
    },
    "human_in_loop": {
      "gpu_hours": "~190h H100 (agent runs broader interaction surface sweeps with finer granularity, more extensive transferability coverage across all 6 benchmarks, additional per-layer analysis)",
      "gpu_utilization": "Moderate (~45-55%). Agent automates grid sweeps and cross-partial computation; human reviews interaction analysis, validates phase detection accuracy, judges interaction regime thresholds, and guides transferability interpretation.",
      "timeline": "12-14 days",
      "team": "1 researcher, ~1.5hr/day reviewing interaction surface analysis and validating phase-specific patterns",
      "claude_api_cost": "$50-120 (~500-1200 turns for experiment design, analysis, visualization, paper drafting)",
      "estimated_gpu_cost": "$475-570 (190h x $2.50-3.00/hr)",
      "risk_note": "Primary risk is that interaction effects are negligibly small (near-zero cross-partial derivatives at all phases), making the two axes effectively independent. This would validate R-Sparse's additive assumption but reduce impact to Findings level. Mitigated by: (a) theoretical motivation from causal coupling and functional asymmetry provides a priori reason to expect non-trivial interaction, (b) the characterization and SwiGLU headroom analysis retain publication value regardless, (c) transferability analysis adds a second dimension of contribution."
    },
    "auto_research": {
      "gpu_hours": "~190h H100 (comprehensive 5x5 sweeps at all phases across all 6 benchmarks, extensive per-layer ablations, full transferability characterization, SwiGLU headroom profiling)",
      "gpu_utilization": "High (~75-85%). Agent runs continuous grid sweeps with automated quality measurement, cross-partial computation, and statistical significance testing.",
      "timeline": "10-12 days with 2-4 H100 GPUs available concurrently",
      "team": "0 (initial setup ~2hrs, then fully autonomous with periodic human review of interaction regime classifications)",
      "claude_api_cost": "$150-300 (~1500-3000 turns for exploration, interaction analysis, transferability evaluation, visualization, paper drafting)",
      "estimated_gpu_cost": "$475-570 (190h x $2.50-3.00/hr)",
      "speed_bottleneck": "GPU count (2-4 concurrent H100s to parallelize interaction surface sweeps across benchmarks and phases). Single model eliminates architecture integration risk.",
      "risk_note": "Integration of Polar Sparsity and TEAL codebases with DeepSeek-R1-Distill-Llama-8B should be straightforward (Llama-3.1 architecture natively supported). Automated numerical validation against dense baselines ensures correctness. Transferability analysis may reveal task-family-specific patterns requiring human interpretation of practical implications."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission: May 25, 2026; commitment: Aug 2, 2026) — Main if interaction effects are significant and transferability analysis strengthens the characterization; Findings if cross-partial is near-zero (valuable negative result validating additive assumption)"
  ],
  "level": "top-tier",
  "key_references": [
    "R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference (ICLR 2025)",
    "When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models (ICLR 2026)",
    "From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models (arXiv 2601.18091, Jan 2026)",
    "Attention Retrieves, MLP Memorizes: Disentangling Trainable Components in the Transformer (arXiv 2506.01115, June 2025)",
    "Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions (EMNLP 2024)",
    "Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity (NeurIPS 2025)",
    "Training-Free Activation Sparsity in Large Language Models [TEAL] (ICLR 2025)",
    "ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral)",
    "Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for LLMs [WAS] (EMNLP 2025)",
    "ActTail: Global Activation Sparsity in Large Language Models (arXiv 2026)",
    "WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity (arXiv 2026)",
    "Efficient LLMs with AMP: Attention Heads and MLP Pruning (IJCNN 2025)",
    "Sparsing Law: Towards Large Language Models with Greater Activation Sparsity (ICML 2025)",
    "Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning (NeurIPS 2025 Spotlight)",
    "Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention [EvoSparse] (ACL 2026)",
    "SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding (arXiv 2602.07223, Feb 2026)",
    "FASA: Frequency-aware Sparse Attention (ICLR 2026)",
    "RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning (ACL 2025 Findings)",
    "SeerAttention-R: Sparse Attention Adaptation for Long Reasoning (arXiv 2025)",
    "LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning (arXiv 2025)",
    "LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention (MLSys 2025)",
    "Scalable Chain of Thoughts via Elastic Reasoning (ICLR 2026)",
    "Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning (NeurIPS 2025)",
    "How does Chain of Thought Think? Mechanistic Interpretability of Chain-of-Thought Reasoning with Sparse Autoencoding (arXiv 2507.22928)",
    "Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding [SparseSpec] (arXiv 2025)",
    "Nemotron Elastic: Towards Efficient Many-in-One Reasoning LLMs (ICML 2026)",
    "Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction [RAC] (NeurIPS 2025 Workshop on Efficient Reasoning)",
    "Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling (arXiv 2604.25098, April 2026)",
    "ELAS: Efficient Pre-Training of Low-Rank Large Language Models via 2:4 Activation Sparsity (arXiv 2605.03667, May 2026)"
  ],
  "description": "Current compute sparsity methods for LLM inference treat attention-head and MLP activation sparsity as independent, separable axes — yet the transformer's architecture creates a causal dependency (attention output → residual → layer norm → MLP input) that makes this independence assumption empirically untested. We present Sparsity Interaction Surfaces (SIS), the first systematic empirical characterization of how attention and MLP sparsity interact across reasoning phases. We ground our investigation in a theoretical motivation: 'Attention Retrieves, MLP Memorizes' (arXiv 2506.01115) shows these components serve fundamentally different functions, so sparsifying retrieval changes what memorization can operate on; 'When Reasoning Meets Compression' (ICLR 2026) shows MLP up projections are critically important for reasoning; 'Interpreting Context Look-ups in Transformers' (EMNLP 2024) demonstrates causal coupling where specific attention heads trigger downstream MLP neurons. We enumerate three possible interaction regimes — compounding (joint degradation exceeds individual sum), complementing (joint is better than expected), and independent (R-Sparse's additive assumption holds) — and measure which regime dominates at each reasoning phase by sweeping a 5x5 grid of (attention_sparsity, mlp_sparsity) levels during problem-intake, exploration, verification, and answer-generation in DeepSeek-R1-Distill-Llama-8B. We test transferability across three task families (math, code, general reasoning) to determine whether interaction patterns generalize. As a demonstration of the characterization's utility, we show that phase-aware joint allocation guided by the interaction surface achieves 1.3-1.7x decode speedup with <3% accuracy loss, outperforming phase-agnostic baselines. The work additionally contributes the first characterization of forced-sparsity headroom in SwiGLU-based reasoning models. The paper retains value under all outcomes: significant interaction effects motivate phase-aware joint design (Main); near-zero cross-partial validates R-Sparse's additive assumption — itself a useful negative result — plus the SwiGLU headroom and transferability analyses (Findings). Primary target: EMNLP 2026 (ARR May 25, 2026).",
  "project_name": "sparsity_interaction_surfaces",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["FATAL: Wrong venue — user requires EMNLP 2026 (ARR deadline May 25, 2026), but idea targets AAAI 2027 (Aug 2), ICLR 2027 (Sep 24), and MLSys 2027 (~Oct 31). Must retarget to EMNLP 2026.", "FATAL: GPU budget violation — user constraint is ≤200 H100-hours total, but the manual estimate alone is ~300h (50% over). The approach must be simplified to fit within 200h, e.g., by dropping custom CUDA kernel development and using existing sparse kernels from Polar Sparsity/TEAL/FlashInfer.", "FATAL: Timeline violation — user constraint is ≤16 days, but even the auto_research estimate is 2-4 weeks. Custom CUDA kernel development is the primary bottleneck and should be eliminated in favor of existing kernel infrastructure.", "FATAL: Benchmark mismatch — user specifies perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench and wall-clock/throughput on H100. The idea evaluates only on AIME, MATH500, LiveCodeBench. Must add all required benchmarks.", "Novelty concern: ThinKV (ICLR 2026 Oral) already identifies 3 reasoning phases (Reasoning, Execution, Transition) with distinct sparsity profiles via KDE-based classification. PAJS's phase detection is closely related. Generator must explicitly differentiate from ThinKV's thought-type classification.", "Novelty concern: AMP (IJCNN 2025) already performs joint attention-head and MLP pruning. The only differentiation is phase-awareness, which is borrowed from ThinKV/Elastic Reasoning.", "Feasibility risk: ThinKV found that backtracking/transition tokens have HIGH sparsity but are critically important — 'removing them causes the model to loop endlessly.' This directly challenges the assumption that exploration/backtracking phases can tolerate aggressive sparsity.", "Model name errors: 'DeepSeek-R1-Distill-Qwen3-8B' does not exist — the correct model is 'DeepSeek-R1-0528-Qwen3-8B'. 'Qwen3-8B-Thinking' is not a separate model — Qwen3-8B supports thinking mode natively via &lt;think> tags.", "Missing competing work: Weight-Aware Activation Sparsity (WAS, EMNLP 2025) applies inter-block sparsity with constrained Bayesian optimization — relevant baseline not discussed. LoopServe (arXiv 2025) does dual-phase adaptive inference — adjacent work not mentioned.", "The resource_estimate section provides manual/HIL/auto modes, but none satisfy user constraints. The user's 200 H100-hour budget and 16-day timeline are hard constraints that must be met, not approximated."]
Feedback: This idea has a promising direction but fundamentally fails to meet the user's constraints. To revise:

1. **Retarget to EMNLP 2026** (ARR May 25, 2026). This is non-negotiable per user requirements.

2. **Fit within 200 H100-hours and 16 days**: Drop custom CUDA kernel development entirely. Instead, build on existing sparse inference kernels from Polar Sparsity (open-source), TEAL (GitHub: FasterDecoding/TEAL), Twilight (GitHub: tsinghua-ideal/Twilight), and FlashInfer. The phase router can use Python-level switching between pre-configured sparsity settings — no fused kernel needed for a paper contribution. This alone cuts 100+ hours and weeks of development.

3. **Add required benchmarks**: The user specifies perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench, plus wall-clock and throughput on H100. You can keep AIME/MATH500 as supplementary reasoning benchmarks but MUST include the required set.

4. **Sharpen novelty against ThinKV**: ThinKV already detects thought types (R/E/T) with sparsity-based classification. Your phase router must be clearly differentiated — perhaps by operating on compute sparsity (attention heads + MLP activations) rather than KV cache, and by showing that compute sparsity profiles differ from KV cache sparsity profiles across phases.

5. **Address backtracking safety**: ThinKV showed backtracking tokens are sparsity-high but importance-critical. Your approach must demonstrate that MLP/attention-head sparsity can be applied safely to these tokens even when KV cache sparsity cannot.

6. **Fix model names**: Use 'DeepSeek-R1-0528-Qwen3-8B' and 'Qwen3-8B' (with thinking mode enabled), not the nonexistent model names.

7. **Simplify scope**: Given 200 H100-hours, focus on profiling (phase characterization) + phase-aware application of existing sparsity methods (Polar Sparsity + TEAL) with a lightweight Python-level phase classifier. Save kernel engineering for a follow-up systems paper. This makes the contribution more of a method/analysis paper suitable for EMNLP's Efficient Methods track.

### Round 2 review
Verdict: revise
Issues: ["Feasibility risk: Polar Sparsity GitHub (susavlsh10/Polar-Sparsity) has only 6 commits and supports only OPT and Llama models — no Qwen3 support. TEAL (FasterDecoding/TEAL) self-describes as 'just a proof of concept' with FP16-only support and only supports Llama/Mistral. Adapting BOTH codebases to Qwen3-8B / DeepSeek-R1-0528-Qwen3-8B within the 10-14 day timeline is a major unacknowledged risk.", "Manual timeline violation: manual mode estimates '4-6 weeks', which exceeds the user's hard 16-day constraint.", "Methodological thinness: The core method reduces to 'compose Polar Sparsity + TEAL + logistic classifier on pooled hidden states.' A logistic classifier on hidden state norms with <0.1% overhead is simple engineering, not a method contribution. The phase detection using &lt;think>/&lt;/think> boundaries is trivial, and attention entropy is closely related to ThinKV's KDE-based classification — differentiation is insufficient.", "Missing competitor: 'Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction' (RAC, NeurIPS 2025) demonstrates that reasoning models require reasoning-aware calibration for sparsity/pruning. This is a relevant baseline showing that phase/reasoning awareness matters for sparsity, and should be discussed.", "Missing competitor: FASA (ICLR 2026) performs frequency-aware sparse attention evaluated on LongCoT reasoning tasks with 2.56x speedup on AIME24. While KV-focused, it's a relevant phase-aware attention optimization baseline.", "Speedup target may be over-optimistic: Claiming 2-3x average decode speedup by composing two methods that individually achieve 1.5-2.2x requires multiplicative stacking of attention + MLP sparsity. At the high sparsity levels needed (50-60% head + 50% MLP), quality degradation may prevent achieving both simultaneously — especially since Polar Sparsity's 2.2x is for attention-only at large batch sizes, not decode.", "The backtracking-token compute tolerance hypothesis is high-risk: ThinKV explicitly warns that backtracking tokens 'cannot be removed without causing infinite loops.' While compute sparsity preserves tokens in context, applying aggressive compute sparsity (fewer heads, sparser MLP) to these critical tokens could still degrade the quality of the backtracking signal, leading to extended or failed reasoning chains. If this hypothesis fails, one of the three claimed contributions is lost.", "Missing analysis of recent work showing CoT tokens already exhibit higher activation sparsity (arxiv 2507.22928): If thinking tokens are already naturally more sparse in their activations, the headroom for additional compute sparsity during thinking phases may be smaller than assumed."]
Feedback: The revision successfully addressed Round 1's fatal issues (venue, benchmarks, model names, GPU budget). The gap is real and the direction timely. However, four issues need attention before this can pass:

1. **Mitigate the codebase compatibility risk** (most critical): Neither Polar Sparsity nor TEAL supports Qwen3 natively. Options: (a) Switch to Llama-3.1-8B-Instruct with reasoning fine-tuning, which both codebases support natively, reducing integration risk dramatically. You can keep DeepSeek-R1-0528-Qwen3-8B as a secondary model with custom integration. (b) Alternatively, acknowledge this risk explicitly with a fallback plan (e.g., re-implement magnitude-based MLP pruning for Qwen3 directly rather than depending on TEAL's codebase, since TEAL's core method is simple magnitude thresholding).

2. **Strengthen the method contribution**: A logistic classifier on pooled hidden states is too thin for a method paper. Consider: (a) Formulating the phase-specific sparsity budget selection as an optimization problem (e.g., minimize quality loss subject to per-phase sparsity budgets, solved via the profiling data); (b) Analyzing the interaction effects between attention-head and MLP sparsity — do they compound, interfere, or complement? This cross-component analysis would be a genuine methodological insight; (c) Providing theoretical motivation for why compute sparsity should behave differently from KV cache sparsity across phases.

3. **Add RAC (NeurIPS 2025) and FASA (ICLR 2026) to the landscape**: RAC demonstrates reasoning-aware pruning calibration and is a natural baseline. FASA's phase-aware attention on reasoning benchmarks is relevant context. Also discuss the finding from arxiv 2507.22928 that CoT tokens already show higher activation sparsity — this could support or limit your approach.

4. **Fix manual timeline**: Must be ≤16 days per user constraint. Consider scoping to 2 weeks with reduced ablation budget.

5. **Temper speedup claims**: State '1.5-2.5x average decode speedup' rather than '2-3x' to be more realistic about multiplicative sparsity composition.

### Round 3 review
Verdict: revise
Issues: ["Method contribution is still primarily compositional: the core approach is applying existing sparsity methods (Polar Sparsity for attention, TEAL for MLP) with a phase classifier (borrowing from ThinKV's reasoning-phase decomposition) and Bayesian optimization (borrowing from WAS). The interaction analysis (cross-partial derivatives d²Q/ds_attn·ds_mlp) is the most genuinely novel element but is buried as one sub-point rather than being the centerpiece.", "Natural sparsity headroom risk insufficiently addressed: arxiv 2507.22928 shows CoT induces higher activation sparsity. While the idea notes this was on Pythia-2.8B (non-SwiGLU), it only frames this as a 'research question' without a concrete plan for what the paper contributes if profiling reveals limited headroom for forced sparsity on top of natural sparsity. If thinking tokens already tolerate 60% natural sparsity, the marginal gain from phase-aware allocation may be negligible vs. phase-agnostic methods.", "Speedup upper bound of 2.5x may still be unrealistic: TEAL achieves 1.5-1.8x for MLP-only, and Polar Sparsity achieves 2.2x for attention-only at large batch sizes. Joint composition doesn't multiply — attention and MLP are in series, so savings add rather than multiply. With evidence showing practical speedups consistently below theoretical (CHESS reports structured sparsity degrades under batching; SwiGLU limits sparsity ceilings), a more honest range would be 1.3-2.0x.", "Missing relevant work: 'Doing More With Less: Revisiting Effectiveness of LLM Pruning for Test-Time Scaling' (arXiv 2604.25098, April 2026) shows unstructured pruning can maintain or even improve test-time scaling performance in reasoning models (Qwen3-8B, s1.1-7B). While this is weight pruning (not activation sparsity), it demonstrates that reasoning-aware pruning analysis is an active concurrent direction and should be discussed.", "Scope may be too broad for 14 days with immature codebases: profiling 2 models × 8+ benchmarks × 4 baselines + implementing the optimization framework + phase detection + ablations is extremely ambitious. Consider dropping Qwen3-8B entirely and doing a deeper, more thorough analysis on DeepSeek-R1-Distill-Llama-8B alone — one model studied deeply is more convincing than two models studied superficially with integration bugs.", "RAC is cited as 'NeurIPS 2025' but evidence suggests it may be a NeurIPS 2025 Workshop paper (1st Workshop on Efficient Reasoning) rather than main conference — the neurips.cc URL pattern (virtual/2025/126571 vs. virtual/2025/poster/...) suggests workshop. Minor but should be verified and corrected if needed.", "Bayesian optimization over 8 parameters (4 phases × 2 sparsity dimensions) may be over-engineered — grid search or random search would likely suffice for such a low-dimensional space, and claiming Bayesian optimization as a methodological contribution for 8 parameters weakens the paper."]
Feedback: The idea has improved substantially across rounds — the gap is genuine, the landscape is comprehensive, and the constraints are met. To push this to passing quality, three changes would make the biggest difference:

1. **Elevate the interaction analysis as THE core contribution**: The cross-partial derivative analysis of attention × MLP sparsity across reasoning phases is genuinely novel — no one has characterized whether these two sparsity axes compound or complement at different reasoning stages. Make this the centerpiece of the paper, not component (2b). Reframe the paper as: 'We provide the first characterization of how attention-head and MLP activation sparsity interact across reasoning phases, and show that this interaction structure enables phase-specific joint optimization that outperforms phase-agnostic methods.' This shifts the contribution from 'we combined existing methods' to 'we discovered a previously unknown phenomenon and exploited it.'

2. **Concretely address the natural sparsity headroom risk**: Add a fallback contribution structure. If profiling shows limited headroom: (a) the interaction analysis itself is still a contribution (showing when joint sparsity helps vs. hurts), (b) the characterization of compute vs. KV cache sparsity profiles is valuable even if speedups are modest, (c) a negative result on backtracking token compute tolerance is publishable. State this explicitly so reviewers see the paper has value regardless of the speedup numbers.

3. **Narrow scope to one model, deeper analysis**: Drop Qwen3-8B and focus entirely on DeepSeek-R1-Distill-Llama-8B. This eliminates codebase integration risk for a second architecture, frees ~40-50 H100-hours for more thorough profiling and ablations on the primary model, and allows deeper analysis of the interaction surface. You can note Qwen3-8B generalization as future work. One model studied thoroughly > two models studied shallowly.

Additional improvements: (a) Reduce speedup claims to 1.3-2.0x. (b) Replace Bayesian optimization with simpler grid search over the 8-parameter space — it's more honest and equally effective at this dimensionality. (c) Add 'Doing More With Less' (arXiv 2604.25098) to the landscape. (d) Verify RAC's venue (workshop vs. main conference).

### Round 4 review
Verdict: revise
Issues: ["Impact is conditional on empirical findings: if the cross-partial derivative is near-zero at all phases (axes are independent), the phase-aware allocation becomes unjustified and the paper reduces to a characterization study confirming R-Sparse's additive assumption holds. While the generator acknowledges this with a fallback structure, the fallback contributions (characterization + backtracking analysis) are better suited to EMNLP Findings than Main.", "The 'method' contribution (grid search over 8 parameters to select phase-specific sparsity levels) is engineering application of the characterization, not a novel algorithm. For EMNLP Efficient Methods track, reviewers expect algorithmic contributions — a systematic profiling study with grid search may not meet that bar for Main conference.", "SwiGLU headroom risk is more severe than acknowledged: Sparsing Law (ICML 2025) shows SwiGLU models have substantially lower natural activation sparsity than ReLU. The CoT SAE sparsity result (arxiv 2507.22928) was on Pythia (non-SwiGLU). If forced sparsity in DeepSeek-R1-Distill-Llama-8B (SwiGLU) causes steep quality drops at even moderate levels, the 2D interaction surface will be trivially shaped (compounding everywhere at practical sparsity levels), making the characterization less informative.", "Missing relevant concurrent work: (1) 'When Reasoning Meets Compression' (ICLR 2026) explicitly studies how compression affects reasoning in DeepSeek-R1, finding MLP up projection in the final layer is critically important — directly relevant to understanding MLP sparsity sensitivity in reasoning models. (2) 'From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models' (arXiv 2601.18091, Jan 2026) shows width pruning is more robust than depth pruning for reasoning tasks — provides context for MLP vs. attention sparsity sensitivity.", "Speedup upper bound of 2.0x may still be optimistic: attention and MLP are in series (savings add, not multiply), MLP sparsity degrades under batching (Polar Sparsity), and practical speedups consistently fall below theoretical. With Polar Sparsity's attention-only result at 2.2x achieved at large batch sizes (not batch=1 decode typical for reasoning), the joint 2.0x at decode requires very optimistic assumptions about complementing interactions. Consider stating 1.3-1.7x for credibility.", "No theoretical motivation for why the interaction should be non-trivial: the attention output feeds into MLP input within each transformer block (causal dependency), so sparsifying attention should change the representation quality seen by MLP, potentially affecting MLP sparsity tolerance. This architectural argument is absent from the proposal but would significantly strengthen the case that the interaction surface will be informative."]
Feedback: The idea has improved substantially through 4 rounds — the gap is genuine, the landscape is comprehensive, and the constraints are met. The interaction surface characterization is a real contribution that no one has done. To push this over the threshold, three specific changes would help most:

1. **Reposition as a characterization + analysis paper, not a method paper**: The strongest element is the interaction surface discovery, not the phase-aware allocation (which is grid search). For EMNLP, frame the contribution as: 'We provide the first empirical characterization of how attention-head and MLP activation sparsity interact across reasoning phases, revealing [compounding/complementing/independent] patterns that provide principled guidance for joint sparsity design.' This framing is more honest and more likely to satisfy reviewers than claiming a novel method. Target Findings explicitly if the interaction effects are moderate.

2. **Add theoretical motivation for non-trivial interaction**: The causal dependency within each transformer block (attention output → layer norm → MLP input) means that reducing attention quality via head sparsification changes the representation quality fed to MLP. If attention sparsity causes the residual stream to lose information about certain tokens, MLP sparsity on top of that could be either catastrophic (compounding: MLP can't recover what attention lost) or benign (complementing: if MLP was only refining the same information attention already dropped). This architectural argument should be made explicit — it strengthens the a priori case that the interaction will be non-trivial and differentiates from studies that treat components as independent.

3. **Strengthen impact with a transferability test**: Can the interaction surface shape (which phases compound vs. complement) transfer across different prompt types (math vs. code vs. general reasoning)? If the interaction pattern is consistent across tasks, the characterization becomes a reusable design principle. If it varies, that's also informative — it means phase-aware allocation must be task-specific. Either way, testing transferability transforms a single-model profiling study into a generalizable finding. This could be done within the existing 150h budget by allocating ~20h to testing on additional benchmark categories.

4. **Cite missing concurrent work**: Add 'When Reasoning Meets Compression' (ICLR 2026) — its finding that MLP up projection in the final layer is critically important for reasoning directly motivates understanding MLP sparsity sensitivity at different reasoning phases. Add 'From LLMs to LRMs' (arXiv 2601.18091) for context on structural pruning in reasoning models.

5. **Tighten speedup claims to 1.3-1.7x**: This is more credible given that (a) attention and MLP savings add rather than multiply, (b) MLP sparsity degrades under batching, and (c) the SwiGLU headroom concern limits aggressive MLP sparsity. A conservative claim that is met is far more convincing than an optimistic claim that falls short.


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
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "type": "user",
  "uuid": "c4c5ac0a-80e2-4134-80d3-84d7abf4bbdd",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T00:19:14.728Z_

```json
{
  "parentUuid": "c4c5ac0a-80e2-4134-80d3-84d7abf4bbdd",
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
  "uuid": "c10f7fee-c6be-4ee8-bf30-157dbd39b289",
  "timestamp": "2026-05-12T00:19:14.728Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T00:19:14.728Z_

```json
{
  "parentUuid": "c10f7fee-c6be-4ee8-bf30-157dbd39b289",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ac0b5338-e495-4303-84b4-c90e9a1db674",
  "timestamp": "2026-05-12T00:19:14.728Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
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
  "leafUuid": "ac0b5338-e495-4303-84b4-c90e9a1db674",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing attention-MLP sparsity interaction in reasoning models",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

### Assistant

_source line 8 · 2026-05-12T00:19:22.214Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea - "Sparsity Interaction Surfaces" - which is now in round 5 of review. I need to independently verify claims, check for competing work, and assess whether the revisions from rounds 1-4 have been adequately addressed.

Let me start by doing thorough research on the key claims and checking for competing/concurrent work.

Key things to verify:
1. Whether the attention-MLP sparsity interaction has been studied
2. Whether the cited papers exist and say what's claimed
3. Current SOTA in joint sparsity methods
4. Whether the gap is still valid
5. Feasibility of the approach within constraints


6. What theoretical foundation supports the non-trivial interaction between these components
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac0b5338-e495-4303-84b4-c90e9a1db674",
  "isSidechain": false,
  "requestId": "req_011CawiVF5cSgXzt885nW29a",
  "type": "assistant",
  "uuid": "3be24082-21f9-43f0-97a3-6095b34d068a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aBY3D7xncJhd2aX1admhd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21789,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21789
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

_source line 9 · 2026-05-12T00:19:22.626Z_

I'll conduct a thorough independent review of this idea. Let me start by verifying key claims, checking for competing work, and assessing the interaction surface concept.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3be24082-21f9-43f0-97a3-6095b34d068a",
  "isSidechain": false,
  "requestId": "req_011CawiVF5cSgXzt885nW29a",
  "type": "assistant",
  "uuid": "29191eb2-2a32-45ac-98f6-8fa57812c6ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aBY3D7xncJhd2aX1admhd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21789,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21789
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

_source line 10 · 2026-05-12T00:19:31.373Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LKQUrmbLNT8184zDTaYKfa`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify R-Sparse and joint sparsity",
  "prompt": "Search the web for these specific topics and report what you find. I need factual verification for an ML paper review.\n\n1. Search for \"R-Sparse rank-aware activation sparsity ICLR 2025\" - verify this paper exists, what it actually does (does it treat attention and MLP sparsity as additive/independent?), and its reported speedups.\n\n2. Search for \"attention MLP sparsity interaction transformer\" or \"joint attention MLP sparsity\" - are there ANY papers that study the interaction between attention-head sparsity and MLP activation sparsity (not just applying both, but characterizing how they interact)?\n\n3. Search for \"AMP attention heads MLP pruning IJCNN 2025\" - verify this paper exists and what it does.\n\n4. Search for \"cross-partial derivative sparsity\" or \"sparsity interaction surface\" - has anyone formalized sparsity interaction this way?\n\n5. Search for \"ActTail global activation sparsity 2026\" and \"WiSparse mixed-granularity activation sparsity 2026\" - verify these recent MLP sparsity papers exist.\n\nUse WebSearch for each query. Report exactly what you find - titles, venues, dates, key claims. Do not speculate beyond what the search results show."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29191eb2-2a32-45ac-98f6-8fa57812c6ed",
  "isSidechain": false,
  "requestId": "req_011CawiVF5cSgXzt885nW29a",
  "type": "assistant",
  "uuid": "52a9f4a8-d350-44a7-bbf3-c8f074c6f457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aBY3D7xncJhd2aX1admhd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21789,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21789
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

_source line 11 · 2026-05-12T00:19:39.024Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GXKACmEWDcMHu9hGPZqC5f`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check reasoning model compression",
  "prompt": "Search the web for these specific papers and topics. I need factual verification for an ML paper review.\n\n1. Search for \"When Reasoning Meets Compression ICLR 2026\" or \"arXiv 2504.02010\" - verify this paper exists, is it actually ICLR 2026, and does it really find that MLP up projection in the final layer is critically important for reasoning (protecting 2% of weights raises accuracy by 6.57%)?\n\n2. Search for \"From LLMs to LRMs pruning reasoning arXiv 2601.18091\" - verify this paper exists and its claim that width pruning is more robust than depth pruning for reasoning.\n\n3. Search for \"Attention Retrieves MLP Memorizes arXiv 2506.01115\" - verify this paper exists and its claims about functional asymmetry.\n\n4. Search for \"Interpreting Context Look-ups in Transformers EMNLP 2024\" or \"arXiv 2402.15055\" - verify this paper and its claim about attention heads causally triggering MLP neurons.\n\n5. Search for \"Sparsing Law activation sparsity ICML 2025\" - verify the claim that SwiGLU/SiLU models have lower natural activation sparsity than ReLU.\n\n6. Search for \"ELAS low-rank activation sparsity arXiv 2605.03667\" - verify this very recent paper.\n\nUse WebSearch for each query. Report exactly what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52a9f4a8-d350-44a7-bbf3-c8f074c6f457",
  "isSidechain": false,
  "requestId": "req_011CawiVF5cSgXzt885nW29a",
  "type": "assistant",
  "uuid": "94ab50ba-6c77-42ca-ac4d-877688a3b9eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aBY3D7xncJhd2aX1admhd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21789,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21789
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

_source line 12 · 2026-05-12T00:19:45.768Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013cojHeDH3xnVWAqLa395Td`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check attention sparsity methods",
  "prompt": "Search the web for these specific papers and topics. I need factual verification for an ML paper review.\n\n1. Search for \"Polar Sparsity NeurIPS 2025 batch-invariant attention sparsity\" - verify this paper, its venue, and its claim about MLP union sparsity vanishing under batching.\n\n2. Search for \"Twilight adaptive attention sparsity NeurIPS 2025 Spotlight\" - verify venue and key claims.\n\n3. Search for \"EvoSparse evolving sparsity sparse attention ACL 2026\" - verify this paper exists and its venue.\n\n4. Search for \"SpecAttn sparse attention self-speculative decoding arXiv 2602.07223\" - verify existence.\n\n5. Search for \"ThinKV thought-adaptive KV compression ICLR 2026 Oral\" - verify this is actually ICLR 2026 Oral, and its phase classification methodology.\n\n6. Search for \"RaaS reasoning-aware attention sparsity ACL 2025\" - verify venue.\n\n7. Search for \"SeerAttention-R sparse attention long reasoning\" - verify existence and key claims (9x speedup at 90% sparsity).\n\nUse WebSearch for each query. Report what you find - titles, venues, dates, key claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94ab50ba-6c77-42ca-ac4d-877688a3b9eb",
  "isSidechain": false,
  "requestId": "req_011CawiVF5cSgXzt885nW29a",
  "type": "assistant",
  "uuid": "a815df03-3488-4fc9-89c5-27ce3b1fbb14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aBY3D7xncJhd2aX1admhd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21789,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21789
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

_source line 13 · 2026-05-12T00:19:55.201Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01H4p34NN9hmEvch32zbvjKY`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competing/concurrent work",
  "prompt": "Search the web for concurrent and competing work that might overlap with a paper about \"characterizing how attention and MLP activation sparsity interact across reasoning phases in LLMs.\" This is the most critical search - I need to find work the paper's author may have missed.\n\nTry these searches:\n\n1. \"joint sparsity attention MLP reasoning LLM 2025 2026\" - any recent work on joint component sparsity in reasoning models\n\n2. \"compute sparsity reasoning model thinking tokens 2026\" - compute-side sparsity for reasoning\n\n3. \"phase-aware inference optimization reasoning LLM\" - phase-specific optimization for reasoning models\n\n4. \"activation sparsity DeepSeek-R1\" - anyone studying sparsity in DeepSeek-R1 specifically\n\n5. \"transformer block interaction sparsity attention feedforward\" - interaction between attention and FFN sparsity\n\n6. \"reasoning model efficient inference 2026\" - recent efficiency methods for reasoning models\n\n7. \"EMNLP 2026 ARR deadline May 2026\" - verify the ARR submission deadline\n\n8. \"Doing More With Less pruning test-time scaling arXiv 2604.25098\" - verify this paper\n\n9. \"Nemotron Elastic inference ICML 2026\" - verify this paper\n\n10. \"LazyEviction token importance recurrence\" - verify this paper\n\nUse WebSearch for each. Report exactly what you find. Be thorough - this determines whether the paper's novelty claim holds."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a815df03-3488-4fc9-89c5-27ce3b1fbb14",
  "isSidechain": false,
  "requestId": "req_011CawiVF5cSgXzt885nW29a",
  "type": "assistant",
  "uuid": "9729e54b-5c63-4914-b9d5-3549df31cecd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012aBY3D7xncJhd2aX1admhd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21789,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21789
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

_source line 14 · 2026-05-12T00:21:02.927Z_

<details><summary>↩ Tool result · `toolu_013cojHeDH3xnVWAqLa395Td`</summary>

```text
Here are my findings for all seven papers:

---

## 1. Polar Sparsity (NeurIPS 2025)

**VERIFIED.** The paper "Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity" is a real NeurIPS 2025 paper (poster). The claim about MLP union sparsity vanishing under batching is confirmed -- the paper's core insight is that MLP sparsity breaks down under batching (union of activation patterns across sequences fills in), while attention head sparsity remains batch-invariant because each sequence computes attention independently. This is the paper's central motivation for shifting the focus from MLP sparsity to attention head sparsity.

- Venue: **NeurIPS 2025 (Poster)**
- arXiv: 2505.14884
- [OpenReview page](https://openreview.net/forum?id=cg2S1qqNSq)

---

## 2. Twilight (NeurIPS 2025 Spotlight)

**VERIFIED.** "Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning" is confirmed as a **NeurIPS 2025 Spotlight** paper. The GitHub repository from Tsinghua IDEAL explicitly tags it as "[NeurIPS'25 Spotlight]". Key claims: uses top-p (nucleus sampling) idea for adaptive budget decisions in sparse attention; can prune up to 98% of redundant tokens; achieves 15.4x acceleration in self-attention and 3.9x end-to-end per-token latency speedup in long-context decoding.

- Venue: **NeurIPS 2025 (Spotlight)**
- arXiv: 2502.02770
- [GitHub](https://github.com/tsinghua-ideal/Twilight)

---

## 3. EvoSparse (ACL 2026)

**VERIFIED.** "Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention" exists and is accepted at **ACL 2026 main conference**. A GitHub repository from iLearn-Lab explicitly labels it "[ACL 2026 main]". Authors are from Harbin Institute of Technology (Shenzhen) and Great Bay University.

- Venue: **ACL 2026 (Main)**
- [GitHub](https://github.com/iLearn-Lab/ACL26-EvoSparse)

---

## 4. SpecAttn (arXiv 2602.07223)

**VERIFIED.** "SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding" exists at arXiv ID 2602.07223. It co-designs drafting and verification phases of self-speculative decoding, using full attention results from verification to identify critical KV entries for sparse attention in subsequent drafting. Claims 2.81x higher throughput over vanilla autoregressive decoding, 1.29x over SOTA sparsity-based self-speculative methods. Implemented in vLLM as a plug-and-play solution.

- Note: There is also a separate, earlier paper called "SpecAttn: Speculating Sparse Attention" (arXiv 2510.27641) -- these appear to be different papers with similar names.
- [arXiv 2602.07223](https://arxiv.org/abs/2602.07223)

---

## 5. ThinKV (ICLR 2026 Oral)

**VERIFIED.** "ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models" is confirmed as an **ICLR 2026 Oral** presentation. The ICLR virtual site shows it as an Oral (presented April 24, 2026).

**Phase classification methodology:** ThinKV categorizes thinking tokens into **three thought types**:
- **R (Reasoning):** Systematic thinking
- **E (Execution):** Calculations or code generation
- **T (Transition):** Uncertainty and backtracking behavior

It then applies a hybrid quantization-eviction strategy based on thought importance: "Think Before you Quantize" (TBQ) assigns precision based on thought type importance, and "Think Before You Evict" (TBE) progressively evicts tokens from less critical thoughts. Achieves competitive accuracy with ~1.3% of the KV cache (1024 tokens), and up to 5.8x throughput improvement.

- Venue: **ICLR 2026 (Oral)**
- arXiv: 2510.01290
- [OpenReview](https://openreview.net/forum?id=M3CeHnZKNC)

---

## 6. RaaS (ACL 2025)

**PARTIALLY VERIFIED -- venue distinction matters.** "RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Inference with Long Decoding Chains" is real, but its venue is **ACL 2025 Findings**, NOT the ACL 2025 main conference. The ACL Anthology URL is `aclanthology.org/2025.findings-acl.131.pdf`, and the ACL 2025 website lists it under "Accepted Findings Papers." If your review cites it as "ACL 2025" without the "Findings" qualifier, that is technically imprecise.

Key claims: identifies "milestone tokens" (analogous to lemmas) and "phoenix tokens" (tokens that lose attention then regain it); achieves O(L) time and memory complexity for reasoning tasks.

- Venue: **ACL 2025 Findings** (not main conference)
- arXiv: 2502.11147
- [ACL Anthology](https://aclanthology.org/2025.findings-acl.131.pdf)

---

## 7. SeerAttention-R

**VERIFIED.** "SeerAttention-R: Sparse Attention Adaptation for Long Reasoning" is a real paper from Microsoft Research. The 9x speedup claim is approximately correct -- the paper reports **up to 8.6x speedup** over FlashAttention-3 on H100 at 90% sparsity (at batch size 16, sequence length >= 32k), using TileLang kernels. The "up to 9x" phrasing appears in the abstract as a rounded figure; the precise experimental number is 8.6x. It uses a self-distilled gating mechanism for learning block-level sparsity patterns, trained on only 0.4B tokens.

- arXiv: 2506.08889
- [GitHub (Microsoft)](https://github.com/microsoft/SeerAttention)
- [arXiv page](https://arxiv.org/abs/2506.08889)

---

## Summary of potential issues for your review:

1. **RaaS venue**: If cited as "ACL 2025," it should be specified as "ACL 2025 Findings" -- this is a meaningful distinction in the NLP community.
2. **SeerAttention-R speedup**: The precise number is 8.6x, not 9x. The abstract rounds up, but citing "9x" without qualification could be flagged as imprecise.
3. All other papers, venues, and key claims check out as stated.

Sources:
- [Polar Sparsity - OpenReview](https://openreview.net/forum?id=cg2S1qqNSq)
- [Polar Sparsity - arXiv](https://arxiv.org/abs/2505.14884)
- [Twilight - GitHub](https://github.com/tsinghua-ideal/Twilight)
- [Twilight - arXiv](https://arxiv.org/abs/2502.02770)
- [EvoSparse - GitHub](https://github.com/iLearn-Lab/ACL26-EvoSparse)
- [SpecAttn - arXiv 2602.07223](https://arxiv.org/abs/2602.07223)
- [ThinKV - ICLR 2026 Virtual](https://iclr.cc/virtual/2026/oral/10009981)
- [ThinKV - OpenReview](https://openreview.net/forum?id=M3CeHnZKNC)
- [ThinKV - arXiv](https://arxiv.org/abs/2510.01290)
- [RaaS - ACL Anthology (Findings)](https://aclanthology.org/2025.findings-acl.131.pdf)
- [RaaS - arXiv](https://arxiv.org/abs/2502.11147)
- [SeerAttention-R - arXiv](https://arxiv.org/abs/2506.08889)
- [SeerAttention-R - Microsoft Research](https://www.microsoft.com/en-us/research/publication/seerattention-r-sparse-attention-adaptation-for-long-reasoning/)

agentId: a3397cb661bf77deb (use SendMessage with to: 'a3397cb661bf77deb' to continue this agent)
&lt;usage>total_tokens: 22424
tool_uses: 11
duration_ms: 77157&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a815df03-3488-4fc9-89c5-27ce3b1fbb14",
  "isSidechain": false,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "type": "user",
  "uuid": "63f3c45e-1b6f-478d-ae44-6d703e8867ee",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for these specific papers and topics. I need factual verification for an ML paper review.\n\n1. Search for \"Polar Sparsity NeurIPS 2025 batch-invariant attention sparsity\" - verify this paper, its venue, and its claim about MLP union sparsity vanishing under batching.\n\n2. Search for \"Twilight adaptive attention sparsity NeurIPS 2025 Spotlight\" - verify venue and key claims.\n\n3. Search for \"EvoSparse evolving sparsity sparse attention ACL 2026\" - verify this paper exists and its venue.\n\n4. Search for \"SpecAttn sparse attention self-speculative decoding arXiv 2602.07223\" - verify existence.\n\n5. Search for \"ThinKV thought-adaptive KV compression ICLR 2026 Oral\" - verify this is actually ICLR 2026 Oral, and its phase classification methodology.\n\n6. Search for \"RaaS reasoning-aware attention sparsity ACL 2025\" - verify venue.\n\n7. Search for \"SeerAttention-R sparse attention long reasoning\" - verify existence and key claims (9x speedup at 90% sparsity).\n\nUse WebSearch for each query. Report what you find - titles, venues, dates, key claims.",
    "agentId": "a3397cb661bf77deb",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings for all seven papers:\n\n---\n\n## 1. Polar Sparsity (NeurIPS 2025)\n\n**VERIFIED.** The paper \"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity\" is a real NeurIPS 2025 paper (poster). The claim about MLP union sparsity vanishing under batching is confirmed -- the paper's core insight is that MLP sparsity breaks down under batching (union of activation patterns across sequences fills in), while attention head sparsity remains batch-invariant because each sequence computes attention independently. This is the paper's central motivation for shifting the focus from MLP sparsity to attention head sparsity.\n\n- Venue: **NeurIPS 2025 (Poster)**\n- arXiv: 2505.14884\n- [OpenReview page](https://openreview.net/forum?id=cg2S1qqNSq)\n\n---\n\n## 2. Twilight (NeurIPS 2025 Spotlight)\n\n**VERIFIED.** \"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\" is confirmed as a **NeurIPS 2025 Spotlight** paper. The GitHub repository from Tsinghua IDEAL explicitly tags it as \"[NeurIPS'25 Spotlight]\". Key claims: uses top-p (nucleus sampling) idea for adaptive budget decisions in sparse attention; can prune up to 98% of redundant tokens; achieves 15.4x acceleration in self-attention and 3.9x end-to-end per-token latency speedup in long-context decoding.\n\n- Venue: **NeurIPS 2025 (Spotlight)**\n- arXiv: 2502.02770\n- [GitHub](https://github.com/tsinghua-ideal/Twilight)\n\n---\n\n## 3. EvoSparse (ACL 2026)\n\n**VERIFIED.** \"Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention\" exists and is accepted at **ACL 2026 main conference**. A GitHub repository from iLearn-Lab explicitly labels it \"[ACL 2026 main]\". Authors are from Harbin Institute of Technology (Shenzhen) and Great Bay University.\n\n- Venue: **ACL 2026 (Main)**\n- [GitHub](https://github.com/iLearn-Lab/ACL26-EvoSparse)\n\n---\n\n## 4. SpecAttn (arXiv 2602.07223)\n\n**VERIFIED.** \"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding\" exists at arXiv ID 2602.07223. It co-designs drafting and verification phases of self-speculative decoding, using full attention results from verification to identify critical KV entries for sparse attention in subsequent drafting. Claims 2.81x higher throughput over vanilla autoregressive decoding, 1.29x over SOTA sparsity-based self-speculative methods. Implemented in vLLM as a plug-and-play solution.\n\n- Note: There is also a separate, earlier paper called \"SpecAttn: Speculating Sparse Attention\" (arXiv 2510.27641) -- these appear to be different papers with similar names.\n- [arXiv 2602.07223](https://arxiv.org/abs/2602.07223)\n\n---\n\n## 5. ThinKV (ICLR 2026 Oral)\n\n**VERIFIED.** \"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models\" is confirmed as an **ICLR 2026 Oral** presentation. The ICLR virtual site shows it as an Oral (presented April 24, 2026).\n\n**Phase classification methodology:** ThinKV categorizes thinking tokens into **three thought types**:\n- **R (Reasoning):** Systematic thinking\n- **E (Execution):** Calculations or code generation\n- **T (Transition):** Uncertainty and backtracking behavior\n\nIt then applies a hybrid quantization-eviction strategy based on thought importance: \"Think Before you Quantize\" (TBQ) assigns precision based on thought type importance, and \"Think Before You Evict\" (TBE) progressively evicts tokens from less critical thoughts. Achieves competitive accuracy with ~1.3% of the KV cache (1024 tokens), and up to 5.8x throughput improvement.\n\n- Venue: **ICLR 2026 (Oral)**\n- arXiv: 2510.01290\n- [OpenReview](https://openreview.net/forum?id=M3CeHnZKNC)\n\n---\n\n## 6. RaaS (ACL 2025)\n\n**PARTIALLY VERIFIED -- venue distinction matters.** \"RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Inference with Long Decoding Chains\" is real, but its venue is **ACL 2025 Findings**, NOT the ACL 2025 main conference. The ACL Anthology URL is `aclanthology.org/2025.findings-acl.131.pdf`, and the ACL 2025 website lists it under \"Accepted Findings Papers.\" If your review cites it as \"ACL 2025\" without the \"Findings\" qualifier, that is technically imprecise.\n\nKey claims: identifies \"milestone tokens\" (analogous to lemmas) and \"phoenix tokens\" (tokens that lose attention then regain it); achieves O(L) time and memory complexity for reasoning tasks.\n\n- Venue: **ACL 2025 Findings** (not main conference)\n- arXiv: 2502.11147\n- [ACL Anthology](https://aclanthology.org/2025.findings-acl.131.pdf)\n\n---\n\n## 7. SeerAttention-R\n\n**VERIFIED.** \"SeerAttention-R: Sparse Attention Adaptation for Long Reasoning\" is a real paper from Microsoft Research. The 9x speedup claim is approximately correct -- the paper reports **up to 8.6x speedup** over FlashAttention-3 on H100 at 90% sparsity (at batch size 16, sequence length >= 32k), using TileLang kernels. The \"up to 9x\" phrasing appears in the abstract as a rounded figure; the precise experimental number is 8.6x. It uses a self-distilled gating mechanism for learning block-level sparsity patterns, trained on only 0.4B tokens.\n\n- arXiv: 2506.08889\n- [GitHub (Microsoft)](https://github.com/microsoft/SeerAttention)\n- [arXiv page](https://arxiv.org/abs/2506.08889)\n\n---\n\n## Summary of potential issues for your review:\n\n1. **RaaS venue**: If cited as \"ACL 2025,\" it should be specified as \"ACL 2025 Findings\" -- this is a meaningful distinction in the NLP community.\n2. **SeerAttention-R speedup**: The precise number is 8.6x, not 9x. The abstract rounds up, but citing \"9x\" without qualification could be flagged as imprecise.\n3. All other papers, venues, and key claims check out as stated.\n\nSources:\n- [Polar Sparsity - OpenReview](https://openreview.net/forum?id=cg2S1qqNSq)\n- [Polar Sparsity - arXiv](https://arxiv.org/abs/2505.14884)\n- [Twilight - GitHub](https://github.com/tsinghua-ideal/Twilight)\n- [Twilight - arXiv](https://arxiv.org/abs/2502.02770)\n- [EvoSparse - GitHub](https://github.com/iLearn-Lab/ACL26-EvoSparse)\n- [SpecAttn - arXiv 2602.07223](https://arxiv.org/abs/2602.07223)\n- [ThinKV - ICLR 2026 Virtual](https://iclr.cc/virtual/2026/oral/10009981)\n- [ThinKV - OpenReview](https://openreview.net/forum?id=M3CeHnZKNC)\n- [ThinKV - arXiv](https://arxiv.org/abs/2510.01290)\n- [RaaS - ACL Anthology (Findings)](https://aclanthology.org/2025.findings-acl.131.pdf)\n- [RaaS - arXiv](https://arxiv.org/abs/2502.11147)\n- [SeerAttention-R - arXiv](https://arxiv.org/abs/2506.08889)\n- [SeerAttention-R - Microsoft Research](https://www.microsoft.com/en-us/research/publication/seerattention-r-sparse-attention-adaptation-for-long-reasoning/)"
      }
    ],
    "totalDurationMs": 77157,
    "totalTokens": 22424,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4668,
      "cache_read_input_tokens": 15559,
      "output_tokens": 2196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4668
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2196,
          "cache_read_input_tokens": 15559,
          "cache_creation_input_tokens": 4668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4668,
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
  "sourceToolAssistantUUID": "a815df03-3488-4fc9-89c5-27ce3b1fbb14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T00:21:08.255Z_

<details><summary>↩ Tool result · `toolu_01LKQUrmbLNT8184zDTaYKfa`</summary>

```text
Here are the factual findings from all five searches:

---

## 1. R-Sparse (ICLR 2025) -- VERIFIED

**Paper exists.** "R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference" is a confirmed ICLR 2025 conference paper by Zhenyu Zhang et al. (UT Austin / Meta AI). It appears on the official ICLR proceedings site, arXiv (2504.19449), OpenReview, and has a GitHub repo (VITA-Group/R-Sparse).

**What it does:** R-Sparse is a training-free activation sparsity method. It decomposes each linear layer into sparse and low-rank components. Sparse channels (large-magnitude activations) are selected and only the corresponding weight rows are loaded; non-sparse channels are routed through offline low-rank decompositions of the original weights. It uses an evolutionary search algorithm to determine the optimal per-layer sparsity recipe.

**Attention vs. MLP treatment:** R-Sparse is described as "feasible for both attention and MLP blocks." The search results indicate that the patterns of sparse and low-rank combinations "vary across different layers," meaning R-Sparse applies its mechanism to both attention and MLP projections but determines sparsity ratios independently per-layer via evolutionary search. The search results do not show any explicit modeling of the *interaction* between attention sparsity and MLP sparsity -- each projection's sparsity budget is determined by the search procedure, not by a joint interaction model. This is consistent with treating them as effectively independent (additive) contributions to the overall sparsity budget.

**Reported speedups:** 50% model-level sparsity with comparable performance, yielding **43% end-to-end efficiency improvement** with customized CUDA kernels. Tested on Llama-2/3 and Mistral across ten tasks.

---

## 2. Attention-MLP Sparsity Interaction -- VERY LIMITED PRIOR WORK

The search found papers that apply sparsity to both attention and MLP, but **no paper that formally characterizes how attention-head sparsity and MLP activation sparsity interact** (i.e., whether they are additive, synergistic, or antagonistic).

What does exist:

- **JoMA** (arXiv 2310.00535) studies joint *training dynamics* of attention and MLP (not sparsity interaction per se). It integrates out attention to derive modified MLP dynamics, predicting that attention first becomes sparse then dense during training.
- **AMP** (IJCNN 2025, see item 3) prunes both attention heads and MLP neurons jointly and observes an important interaction: pruning only attention heads drops accuracy by 23.39 percentage points compared to pruning both components. This is empirical evidence of interaction, but AMP does not formalize or characterize the interaction mathematically.
- **"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions"** (arXiv 2402.15055) studies how attention heads and next-token MLP neurons interact mechanistically, but does not address sparsity.
- **"What Matters in Transformers? Not All Attention is Needed"** (arXiv 2406.15786) examines dropping attention and MLP layers jointly but again does not formalize the interaction.

**Bottom line:** No paper was found that formally models or measures the *interaction term* between attention sparsity and MLP sparsity as a joint phenomenon.

---

## 3. AMP (IJCNN 2025) -- VERIFIED

**Paper exists.** "Efficient LLMs with AMP: Attention Heads and MLP Pruning" is confirmed on arXiv (2504.21174) and IEEE Xplore. It was published at IJCNN 2025 (Rome, Italy). Authors: Leandro Giusti Mugnaini, Bruno Lopes Yamamoto, Lucas Lauton de Alcantara, Victor Zacarias, Edson Bollis, Lucas Pellicer, Anna Helena Reali Costa, and Artur Jordao.

**What it does:** AMP is a structured pruning method that removes less critical attention heads and MLP neurons. It assesses structural importance by projecting input data onto weights. At 30% pruning ratio, it surpasses state-of-the-art on commonsense reasoning tasks by up to 1.49 percentage points with minimal zero-shot performance impact. Tested on LLaMA and Phi families.

**Key empirical finding on interaction:** Pruning only attention heads (without also pruning MLP) reduces accuracy by 23.39 points, suggesting pruning these components independently is suboptimal. However, AMP does not formalize this interaction mathematically.

---

## 4. "Cross-partial derivative sparsity" / "Sparsity interaction surface" -- NOT FOUND

**No results whatsoever.** The exact phrase "sparsity interaction surface" returned zero hits. "Cross-partial derivative sparsity" combined with neural networks also returned no relevant results. Broader searches for these concepts in the machine learning literature found nothing matching this terminology.

The closest related concept found was "Sparse Interaction Additive Networks (SIAN)" from OpenReview, which is about feature interaction detection in additive models -- a completely different topic.

**These terms do not appear to exist in the published literature.**

---

## 5. ActTail and WiSparse (2026) -- BOTH VERIFIED

### ActTail -- VERIFIED
**Paper exists.** "ActTail: Global Activation Sparsity in Large Language Models," arXiv 2603.12272, submitted February 18, 2026.

**What it does:** A TopK magnitude-based activation sparsity method with *global* (non-uniform) sparsity allocation grounded in Heavy-Tailed Self-Regularization (HT-SR) theory. Uses the heavy-tail exponent computed from each projection's empirical spectral density to assign projection-specific sparsity budgets. At 80% sparsity: perplexity reduced by 21.8% on LLaMA-2-7B, 40.1% on LLaMA-2-13B, 9.4% on Mistral-7B vs. uniform allocation.

### WiSparse -- VERIFIED
**Paper exists.** "WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity," arXiv 2602.14452, February 2026.

**What it does:** A weight-aware, mixed-granularity, training-free activation sparsity method. Integrates activation magnitudes with precomputed weight norms for channel saliency. Uses a coarse-to-fine allocation: global budget distributed across blocks via evolutionary search, then refined within blocks to minimize reconstruction error. At 50% sparsity, preserves 97% of Llama3.1 dense performance, surpassing the strongest baseline by 2.23 points, with 21.4% end-to-end speedup.

Note: "Mixed-granularity" refers to sparsity allocation granularity (block-level vs. projection-level budgets), not to mixing attention and MLP sparsity types.

---

## Summary Table

| Claim | Verdict |
|---|---|
| R-Sparse exists at ICLR 2025 | Confirmed |
| R-Sparse treats attn/MLP sparsity independently | Consistent with evidence (per-layer search, no joint interaction model) |
| R-Sparse 43% speedup at 50% sparsity | Confirmed |
| Papers studying attn-MLP sparsity *interaction* | None found that formalize the interaction |
| AMP at IJCNN 2025 | Confirmed |
| "Cross-partial derivative sparsity" or "sparsity interaction surface" | Not found in any literature |
| ActTail (2026) | Confirmed (arXiv 2603.12272) |
| WiSparse (2026) | Confirmed (arXiv 2602.14452) |

Sources:
- [R-Sparse ICLR 2025 proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
- [R-Sparse arXiv](https://arxiv.org/abs/2504.19449)
- [R-Sparse OpenReview](https://openreview.net/forum?id=9VMW4iXfKt)
- [R-Sparse GitHub](https://github.com/VITA-Group/R-Sparse)
- [R-Sparse HTML](https://arxiv.org/html/2504.19449v1)
- [AMP arXiv](https://arxiv.org/abs/2504.21174)
- [AMP IEEE Xplore](https://ieeexplore.ieee.org/document/11227985/)
- [AMP HTML](https://arxiv.org/html/2504.21174)
- [JoMA arXiv](https://arxiv.org/abs/2310.00535)
- [Interpreting Attention-MLP Interactions](https://arxiv.org/abs/2402.15055)
- [What Matters in Transformers](https://arxiv.org/html/2406.15786v6)
- [ActTail arXiv](https://arxiv.org/abs/2603.12272)
- [WiSparse arXiv](https://arxiv.org/abs/2602.14452)
- [WiSparse HTML](https://arxiv.org/html/2602.14452)

agentId: a5e7811df73ba992a (use SendMessage with to: 'a5e7811df73ba992a' to continue this agent)
&lt;usage>total_tokens: 22721
tool_uses: 12
duration_ms: 96876&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52a9f4a8-d350-44a7-bbf3-c8f074c6f457",
  "isSidechain": false,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "type": "user",
  "uuid": "89a9ce17-8a89-4298-b628-3a854c1e2846",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for these specific topics and report what you find. I need factual verification for an ML paper review.\n\n1. Search for \"R-Sparse rank-aware activation sparsity ICLR 2025\" - verify this paper exists, what it actually does (does it treat attention and MLP sparsity as additive/independent?), and its reported speedups.\n\n2. Search for \"attention MLP sparsity interaction transformer\" or \"joint attention MLP sparsity\" - are there ANY papers that study the interaction between attention-head sparsity and MLP activation sparsity (not just applying both, but characterizing how they interact)?\n\n3. Search for \"AMP attention heads MLP pruning IJCNN 2025\" - verify this paper exists and what it does.\n\n4. Search for \"cross-partial derivative sparsity\" or \"sparsity interaction surface\" - has anyone formalized sparsity interaction this way?\n\n5. Search for \"ActTail global activation sparsity 2026\" and \"WiSparse mixed-granularity activation sparsity 2026\" - verify these recent MLP sparsity papers exist.\n\nUse WebSearch for each query. Report exactly what you find - titles, venues, dates, key claims. Do not speculate beyond what the search results show.",
    "agentId": "a5e7811df73ba992a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the factual findings from all five searches:\n\n---\n\n## 1. R-Sparse (ICLR 2025) -- VERIFIED\n\n**Paper exists.** \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\" is a confirmed ICLR 2025 conference paper by Zhenyu Zhang et al. (UT Austin / Meta AI). It appears on the official ICLR proceedings site, arXiv (2504.19449), OpenReview, and has a GitHub repo (VITA-Group/R-Sparse).\n\n**What it does:** R-Sparse is a training-free activation sparsity method. It decomposes each linear layer into sparse and low-rank components. Sparse channels (large-magnitude activations) are selected and only the corresponding weight rows are loaded; non-sparse channels are routed through offline low-rank decompositions of the original weights. It uses an evolutionary search algorithm to determine the optimal per-layer sparsity recipe.\n\n**Attention vs. MLP treatment:** R-Sparse is described as \"feasible for both attention and MLP blocks.\" The search results indicate that the patterns of sparse and low-rank combinations \"vary across different layers,\" meaning R-Sparse applies its mechanism to both attention and MLP projections but determines sparsity ratios independently per-layer via evolutionary search. The search results do not show any explicit modeling of the *interaction* between attention sparsity and MLP sparsity -- each projection's sparsity budget is determined by the search procedure, not by a joint interaction model. This is consistent with treating them as effectively independent (additive) contributions to the overall sparsity budget.\n\n**Reported speedups:** 50% model-level sparsity with comparable performance, yielding **43% end-to-end efficiency improvement** with customized CUDA kernels. Tested on Llama-2/3 and Mistral across ten tasks.\n\n---\n\n## 2. Attention-MLP Sparsity Interaction -- VERY LIMITED PRIOR WORK\n\nThe search found papers that apply sparsity to both attention and MLP, but **no paper that formally characterizes how attention-head sparsity and MLP activation sparsity interact** (i.e., whether they are additive, synergistic, or antagonistic).\n\nWhat does exist:\n\n- **JoMA** (arXiv 2310.00535) studies joint *training dynamics* of attention and MLP (not sparsity interaction per se). It integrates out attention to derive modified MLP dynamics, predicting that attention first becomes sparse then dense during training.\n- **AMP** (IJCNN 2025, see item 3) prunes both attention heads and MLP neurons jointly and observes an important interaction: pruning only attention heads drops accuracy by 23.39 percentage points compared to pruning both components. This is empirical evidence of interaction, but AMP does not formalize or characterize the interaction mathematically.\n- **\"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions\"** (arXiv 2402.15055) studies how attention heads and next-token MLP neurons interact mechanistically, but does not address sparsity.\n- **\"What Matters in Transformers? Not All Attention is Needed\"** (arXiv 2406.15786) examines dropping attention and MLP layers jointly but again does not formalize the interaction.\n\n**Bottom line:** No paper was found that formally models or measures the *interaction term* between attention sparsity and MLP sparsity as a joint phenomenon.\n\n---\n\n## 3. AMP (IJCNN 2025) -- VERIFIED\n\n**Paper exists.** \"Efficient LLMs with AMP: Attention Heads and MLP Pruning\" is confirmed on arXiv (2504.21174) and IEEE Xplore. It was published at IJCNN 2025 (Rome, Italy). Authors: Leandro Giusti Mugnaini, Bruno Lopes Yamamoto, Lucas Lauton de Alcantara, Victor Zacarias, Edson Bollis, Lucas Pellicer, Anna Helena Reali Costa, and Artur Jordao.\n\n**What it does:** AMP is a structured pruning method that removes less critical attention heads and MLP neurons. It assesses structural importance by projecting input data onto weights. At 30% pruning ratio, it surpasses state-of-the-art on commonsense reasoning tasks by up to 1.49 percentage points with minimal zero-shot performance impact. Tested on LLaMA and Phi families.\n\n**Key empirical finding on interaction:** Pruning only attention heads (without also pruning MLP) reduces accuracy by 23.39 points, suggesting pruning these components independently is suboptimal. However, AMP does not formalize this interaction mathematically.\n\n---\n\n## 4. \"Cross-partial derivative sparsity\" / \"Sparsity interaction surface\" -- NOT FOUND\n\n**No results whatsoever.** The exact phrase \"sparsity interaction surface\" returned zero hits. \"Cross-partial derivative sparsity\" combined with neural networks also returned no relevant results. Broader searches for these concepts in the machine learning literature found nothing matching this terminology.\n\nThe closest related concept found was \"Sparse Interaction Additive Networks (SIAN)\" from OpenReview, which is about feature interaction detection in additive models -- a completely different topic.\n\n**These terms do not appear to exist in the published literature.**\n\n---\n\n## 5. ActTail and WiSparse (2026) -- BOTH VERIFIED\n\n### ActTail -- VERIFIED\n**Paper exists.** \"ActTail: Global Activation Sparsity in Large Language Models,\" arXiv 2603.12272, submitted February 18, 2026.\n\n**What it does:** A TopK magnitude-based activation sparsity method with *global* (non-uniform) sparsity allocation grounded in Heavy-Tailed Self-Regularization (HT-SR) theory. Uses the heavy-tail exponent computed from each projection's empirical spectral density to assign projection-specific sparsity budgets. At 80% sparsity: perplexity reduced by 21.8% on LLaMA-2-7B, 40.1% on LLaMA-2-13B, 9.4% on Mistral-7B vs. uniform allocation.\n\n### WiSparse -- VERIFIED\n**Paper exists.** \"WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity,\" arXiv 2602.14452, February 2026.\n\n**What it does:** A weight-aware, mixed-granularity, training-free activation sparsity method. Integrates activation magnitudes with precomputed weight norms for channel saliency. Uses a coarse-to-fine allocation: global budget distributed across blocks via evolutionary search, then refined within blocks to minimize reconstruction error. At 50% sparsity, preserves 97% of Llama3.1 dense performance, surpassing the strongest baseline by 2.23 points, with 21.4% end-to-end speedup.\n\nNote: \"Mixed-granularity\" refers to sparsity allocation granularity (block-level vs. projection-level budgets), not to mixing attention and MLP sparsity types.\n\n---\n\n## Summary Table\n\n| Claim | Verdict |\n|---|---|\n| R-Sparse exists at ICLR 2025 | Confirmed |\n| R-Sparse treats attn/MLP sparsity independently | Consistent with evidence (per-layer search, no joint interaction model) |\n| R-Sparse 43% speedup at 50% sparsity | Confirmed |\n| Papers studying attn-MLP sparsity *interaction* | None found that formalize the interaction |\n| AMP at IJCNN 2025 | Confirmed |\n| \"Cross-partial derivative sparsity\" or \"sparsity interaction surface\" | Not found in any literature |\n| ActTail (2026) | Confirmed (arXiv 2603.12272) |\n| WiSparse (2026) | Confirmed (arXiv 2602.14452) |\n\nSources:\n- [R-Sparse ICLR 2025 proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)\n- [R-Sparse arXiv](https://arxiv.org/abs/2504.19449)\n- [R-Sparse OpenReview](https://openreview.net/forum?id=9VMW4iXfKt)\n- [R-Sparse GitHub](https://github.com/VITA-Group/R-Sparse)\n- [R-Sparse HTML](https://arxiv.org/html/2504.19449v1)\n- [AMP arXiv](https://arxiv.org/abs/2504.21174)\n- [AMP IEEE Xplore](https://ieeexplore.ieee.org/document/11227985/)\n- [AMP HTML](https://arxiv.org/html/2504.21174)\n- [JoMA arXiv](https://arxiv.org/abs/2310.00535)\n- [Interpreting Attention-MLP Interactions](https://arxiv.org/abs/2402.15055)\n- [What Matters in Transformers](https://arxiv.org/html/2406.15786v6)\n- [ActTail arXiv](https://arxiv.org/abs/2603.12272)\n- [WiSparse arXiv](https://arxiv.org/abs/2602.14452)\n- [WiSparse HTML](https://arxiv.org/html/2602.14452)"
      }
    ],
    "totalDurationMs": 96876,
    "totalTokens": 22721,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2809,
      "cache_read_input_tokens": 17574,
      "output_tokens": 2337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2809
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2337,
          "cache_read_input_tokens": 17574,
          "cache_creation_input_tokens": 2809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2809,
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
  "sourceToolAssistantUUID": "52a9f4a8-d350-44a7-bbf3-c8f074c6f457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
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
  "leafUuid": "89a9ce17-8a89-4298-b628-3a854c1e2846",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing attention-MLP sparsity interaction in reasoning models",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

### Tool result

_source line 18 · 2026-05-12T00:22:02.674Z_

<details><summary>↩ Tool result · `toolu_01GXKACmEWDcMHu9hGPZqC5f`</summary>

```text
Now I have all the information needed. Here is my complete report:

---

## Verification Results for All Six Papers

### 1. "When Reasoning Meets Compression" (arXiv 2504.02010)

**VERIFIED.** The paper exists and is confirmed as accepted at ICLR 2026. Full title: "When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models" by Nan Zhang, Eugene Kwek, Yusen Zhang, Ngoc-Hieu Nguyen, Prasenjit Mitra, and Rui Zhang (Penn State / CMU). Originally submitted April 2, 2025; revised through v3 on March 2, 2026.

**Specific claim about MLP up projection:** Confirmed. The paper uses difference-of-means and attribution patching to locate compression effects on every linear component. It finds that the MLP up projection in the final layer is critically important for reasoning in distilled LRMs, and that protecting just 2% of excessively compressed weights raises average accuracy by 6.57%. This finding specifically applies to quantized models where current methods overly compress final-layer modules and MLP gate projections.

Sources:
- [arXiv:2504.02010](https://arxiv.org/abs/2504.02010)
- [HTML version](https://arxiv.org/html/2504.02010)

---

### 2. "From LLMs to LRMs" (arXiv 2601.18091)

**VERIFIED.** The paper exists: "From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models," submitted January 26, 2026. It also has an OpenReview page.

**Specific claim about width vs. depth pruning:** Confirmed. The paper conducts a controlled study of pruning across 17 tasks for both instruction-following (LLM-instruct) and reasoning-augmented (LLM-think) models. It finds that **depth pruning outperforms width pruning on classification tasks**, while **width pruning is more robust for generation and reasoning tasks**. Additionally, static pruning better preserves reasoning performance, while dynamic pruning excels on classification/generation but is challenging for long-chain reasoning.

Sources:
- [arXiv:2601.18091](https://arxiv.org/abs/2601.18091)
- [OpenReview](https://openreview.net/forum?id=eHHQEsphbN)

---

### 3. "Attention Retrieves, MLP Memorizes" (arXiv 2506.01115)

**VERIFIED.** The paper exists. Full title: "Attention Retrieves, MLP Memorizes: Disentangling Trainable Components in the Transformer" by Yihe Dong, Lorenzo Noci, Mikhail Khodak, and Mufan Li (Princeton / ETH Zurich).

**Claims about functional asymmetry:** Confirmed. The paper demonstrates a clear functional division: attention is responsible for in-context reasoning and retrieval (models with random attention underperform on retrieval tasks), while MLPs are largely responsible for memorization/knowledge storage (freezing MLPs causes the biggest performance drop on memorization tasks). They also introduce "MixiT," an architecture with entirely random attention scores, to disentangle these roles. However, the paper also notes that standard Transformers outperform all ablations, suggesting attention and MLPs **collaborate** -- not that they are fully independent.

Sources:
- [arXiv:2506.01115](https://arxiv.org/abs/2506.01115)
- [HTML version](https://arxiv.org/html/2506.01115v1)

---

### 4. "Interpreting Context Look-ups in Transformers" (arXiv 2402.15055)

**VERIFIED.** The paper exists and is confirmed published at **EMNLP 2024 (Main Conference)**. Full title: "Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions" by Clement Neo, Shay B. Cohen, and Fazl Barez. It appears in the ACL Anthology as EMNLP 2024 Main paper #930.

**Claim about attention heads causally triggering MLP neurons:** Confirmed. The paper proposes a methodology to identify "next-token neurons" in the MLP, find prompts that highly activate them, and then determine the upstream attention heads responsible. They find that some attention heads recognize specific contexts and causally activate downstream token-predicting MLP neurons, establishing a direct attention-to-MLP causal pathway for next-token prediction.

Sources:
- [ACL Anthology: EMNLP 2024](https://aclanthology.org/2024.emnlp-main.930/)
- [arXiv:2402.15055](https://arxiv.org/abs/2402.15055)

---

### 5. "Sparsing Law" (arXiv 2411.02335)

**VERIFIED.** The paper exists: "Sparsing Law: Towards Large Language Models with Greater Activation Sparsity." It is confirmed as accepted at **ICML 2025** (presented as a poster).

**Claim about SwiGLU/SiLU vs. ReLU activation sparsity:** Confirmed. The paper explicitly finds that ReLU-activated LLMs exhibit higher natural activation sparsity than SiLU-activated LLMs (SwiGLU uses SiLU internally). Specifically: "the sparsity ratio of ReLU-activated LLMs always surpasses that of SiLU-activated LLMs" given the same parameter scale, with comparable downstream performance. They also find ReLU-activated LLMs become more sparse with more training data (a convergent power-law relationship). They propose a new metric called CETT-PPL-1% to measure activation sparsity more accurately.

Sources:
- [ICML 2025 Poster](https://icml.cc/virtual/2025/poster/45239)
- [arXiv:2411.02335](https://arxiv.org/abs/2411.02335)
- [OpenReview](https://openreview.net/forum?id=B9XP2R9LtG)

---

### 6. "ELAS" (arXiv 2605.03667)

**VERIFIED.** The paper exists and is very recent (submitted May 5, 2026). Full title: "ELAS: Efficient Pre-Training of Low-Rank Large Language Models via 2:4 Activation Sparsity." It also has an OpenReview page.

**Description:** ELAS addresses the problem that existing low-rank LLM training methods leave activation matrices in full-rank, which dominates memory consumption and limits throughput during large-batch training. The approach applies squared ReLU activation functions to the FFN in low-rank models and implements 2:4 structured sparsity on the resulting activations, leveraging NVIDIA GPU hardware support for the 2:4 sparse format.

Sources:
- [arXiv:2605.03667](https://arxiv.org/abs/2605.03667)
- [OpenReview](https://openreview.net/forum?id=gvDyT1KucD)

---

**Summary:** All six papers are verified to exist. All specific claims you asked about are substantiated by the search results. The venue attributions (ICLR 2026, EMNLP 2024, ICML 2025) are all confirmed correct.

agentId: aed0595c3fcea2c3e (use SendMessage with to: 'aed0595c3fcea2c3e' to continue this agent)
&lt;usage>total_tokens: 20724
tool_uses: 10
duration_ms: 143648&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94ab50ba-6c77-42ca-ac4d-877688a3b9eb",
  "isSidechain": false,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "type": "user",
  "uuid": "986fbaed-4d75-497c-a729-c09d6063ba4f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for these specific papers and topics. I need factual verification for an ML paper review.\n\n1. Search for \"When Reasoning Meets Compression ICLR 2026\" or \"arXiv 2504.02010\" - verify this paper exists, is it actually ICLR 2026, and does it really find that MLP up projection in the final layer is critically important for reasoning (protecting 2% of weights raises accuracy by 6.57%)?\n\n2. Search for \"From LLMs to LRMs pruning reasoning arXiv 2601.18091\" - verify this paper exists and its claim that width pruning is more robust than depth pruning for reasoning.\n\n3. Search for \"Attention Retrieves MLP Memorizes arXiv 2506.01115\" - verify this paper exists and its claims about functional asymmetry.\n\n4. Search for \"Interpreting Context Look-ups in Transformers EMNLP 2024\" or \"arXiv 2402.15055\" - verify this paper and its claim about attention heads causally triggering MLP neurons.\n\n5. Search for \"Sparsing Law activation sparsity ICML 2025\" - verify the claim that SwiGLU/SiLU models have lower natural activation sparsity than ReLU.\n\n6. Search for \"ELAS low-rank activation sparsity arXiv 2605.03667\" - verify this very recent paper.\n\nUse WebSearch for each query. Report exactly what you find.",
    "agentId": "aed0595c3fcea2c3e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Here is my complete report:\n\n---\n\n## Verification Results for All Six Papers\n\n### 1. \"When Reasoning Meets Compression\" (arXiv 2504.02010)\n\n**VERIFIED.** The paper exists and is confirmed as accepted at ICLR 2026. Full title: \"When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models\" by Nan Zhang, Eugene Kwek, Yusen Zhang, Ngoc-Hieu Nguyen, Prasenjit Mitra, and Rui Zhang (Penn State / CMU). Originally submitted April 2, 2025; revised through v3 on March 2, 2026.\n\n**Specific claim about MLP up projection:** Confirmed. The paper uses difference-of-means and attribution patching to locate compression effects on every linear component. It finds that the MLP up projection in the final layer is critically important for reasoning in distilled LRMs, and that protecting just 2% of excessively compressed weights raises average accuracy by 6.57%. This finding specifically applies to quantized models where current methods overly compress final-layer modules and MLP gate projections.\n\nSources:\n- [arXiv:2504.02010](https://arxiv.org/abs/2504.02010)\n- [HTML version](https://arxiv.org/html/2504.02010)\n\n---\n\n### 2. \"From LLMs to LRMs\" (arXiv 2601.18091)\n\n**VERIFIED.** The paper exists: \"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models,\" submitted January 26, 2026. It also has an OpenReview page.\n\n**Specific claim about width vs. depth pruning:** Confirmed. The paper conducts a controlled study of pruning across 17 tasks for both instruction-following (LLM-instruct) and reasoning-augmented (LLM-think) models. It finds that **depth pruning outperforms width pruning on classification tasks**, while **width pruning is more robust for generation and reasoning tasks**. Additionally, static pruning better preserves reasoning performance, while dynamic pruning excels on classification/generation but is challenging for long-chain reasoning.\n\nSources:\n- [arXiv:2601.18091](https://arxiv.org/abs/2601.18091)\n- [OpenReview](https://openreview.net/forum?id=eHHQEsphbN)\n\n---\n\n### 3. \"Attention Retrieves, MLP Memorizes\" (arXiv 2506.01115)\n\n**VERIFIED.** The paper exists. Full title: \"Attention Retrieves, MLP Memorizes: Disentangling Trainable Components in the Transformer\" by Yihe Dong, Lorenzo Noci, Mikhail Khodak, and Mufan Li (Princeton / ETH Zurich).\n\n**Claims about functional asymmetry:** Confirmed. The paper demonstrates a clear functional division: attention is responsible for in-context reasoning and retrieval (models with random attention underperform on retrieval tasks), while MLPs are largely responsible for memorization/knowledge storage (freezing MLPs causes the biggest performance drop on memorization tasks). They also introduce \"MixiT,\" an architecture with entirely random attention scores, to disentangle these roles. However, the paper also notes that standard Transformers outperform all ablations, suggesting attention and MLPs **collaborate** -- not that they are fully independent.\n\nSources:\n- [arXiv:2506.01115](https://arxiv.org/abs/2506.01115)\n- [HTML version](https://arxiv.org/html/2506.01115v1)\n\n---\n\n### 4. \"Interpreting Context Look-ups in Transformers\" (arXiv 2402.15055)\n\n**VERIFIED.** The paper exists and is confirmed published at **EMNLP 2024 (Main Conference)**. Full title: \"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions\" by Clement Neo, Shay B. Cohen, and Fazl Barez. It appears in the ACL Anthology as EMNLP 2024 Main paper #930.\n\n**Claim about attention heads causally triggering MLP neurons:** Confirmed. The paper proposes a methodology to identify \"next-token neurons\" in the MLP, find prompts that highly activate them, and then determine the upstream attention heads responsible. They find that some attention heads recognize specific contexts and causally activate downstream token-predicting MLP neurons, establishing a direct attention-to-MLP causal pathway for next-token prediction.\n\nSources:\n- [ACL Anthology: EMNLP 2024](https://aclanthology.org/2024.emnlp-main.930/)\n- [arXiv:2402.15055](https://arxiv.org/abs/2402.15055)\n\n---\n\n### 5. \"Sparsing Law\" (arXiv 2411.02335)\n\n**VERIFIED.** The paper exists: \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity.\" It is confirmed as accepted at **ICML 2025** (presented as a poster).\n\n**Claim about SwiGLU/SiLU vs. ReLU activation sparsity:** Confirmed. The paper explicitly finds that ReLU-activated LLMs exhibit higher natural activation sparsity than SiLU-activated LLMs (SwiGLU uses SiLU internally). Specifically: \"the sparsity ratio of ReLU-activated LLMs always surpasses that of SiLU-activated LLMs\" given the same parameter scale, with comparable downstream performance. They also find ReLU-activated LLMs become more sparse with more training data (a convergent power-law relationship). They propose a new metric called CETT-PPL-1% to measure activation sparsity more accurately.\n\nSources:\n- [ICML 2025 Poster](https://icml.cc/virtual/2025/poster/45239)\n- [arXiv:2411.02335](https://arxiv.org/abs/2411.02335)\n- [OpenReview](https://openreview.net/forum?id=B9XP2R9LtG)\n\n---\n\n### 6. \"ELAS\" (arXiv 2605.03667)\n\n**VERIFIED.** The paper exists and is very recent (submitted May 5, 2026). Full title: \"ELAS: Efficient Pre-Training of Low-Rank Large Language Models via 2:4 Activation Sparsity.\" It also has an OpenReview page.\n\n**Description:** ELAS addresses the problem that existing low-rank LLM training methods leave activation matrices in full-rank, which dominates memory consumption and limits throughput during large-batch training. The approach applies squared ReLU activation functions to the FFN in low-rank models and implements 2:4 structured sparsity on the resulting activations, leveraging NVIDIA GPU hardware support for the 2:4 sparse format.\n\nSources:\n- [arXiv:2605.03667](https://arxiv.org/abs/2605.03667)\n- [OpenReview](https://openreview.net/forum?id=gvDyT1KucD)\n\n---\n\n**Summary:** All six papers are verified to exist. All specific claims you asked about are substantiated by the search results. The venue attributions (ICLR 2026, EMNLP 2024, ICML 2025) are all confirmed correct."
      }
    ],
    "totalDurationMs": 143648,
    "totalTokens": 20724,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 18003,
      "output_tokens": 1815,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 905
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1815,
          "cache_read_input_tokens": 18003,
          "cache_creation_input_tokens": 905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 905,
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
  "sourceToolAssistantUUID": "94ab50ba-6c77-42ca-ac4d-877688a3b9eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:23:04.019Z_

<details><summary>↩ Tool result · `toolu_01H4p34NN9hmEvch32zbvjKY`</summary>

```text
Now I have comprehensive results across all 10 searches plus additional targeted searches. Here is my thorough report:

---

## Comprehensive Competitive Landscape Report

### Search 1: Joint Sparsity Attention + MLP in Reasoning LLMs

Several papers directly overlap with the proposed work's territory:

**Most Threatening Competitors:**

- **Spark Transformer** (NeurIPS 2025) -- Achieves sparsity in *both* FFN and attention simultaneously. Only 8% of FFN neurons activated, each token attends to max 256 tokens. 2.5x FLOP reduction. This is the closest work to "joint attention+MLP sparsity" but focuses on *architectural* sparsity (training a new model) rather than *characterizing* existing sparsity patterns in reasoning models.
  - [arXiv:2506.06644](https://arxiv.org/abs/2506.06644)

- **Polar Sparsity** (NeurIPS 2025) -- Key finding directly relevant: as batch size and sequence length grow, sparsity importance *shifts from MLP to Attention*. MLP union activation increases (sparsity vanishes) while attention head sparsity remains stable and batch-invariant. This paper studies the *interaction* between attention and MLP sparsity, which is very close to the proposed paper's topic.
  - [arXiv:2505.14884](https://arxiv.org/abs/2505.14884)

- **CLADA: Cognitive-Load-Aware Dynamic Activation** (Feb 2025) -- Directly studies how activation sparsity should *adapt* based on reasoning difficulty (cognitive load). Uses surprisal/entropy to modulate sparsity levels dynamically. Achieves 40%+ sparsity with ~20% speedup. This is quite close to "phase-aware sparsity" -- it argues sparsity should vary by task difficulty, analogous to varying across reasoning phases.
  - [arXiv:2502.19078](https://arxiv.org/abs/2502.19078)

- **EvoSparse** (ACL 2026 main) -- Studies how token importance *dynamics* evolve across decoding steps and layers for sparse attention. Reuses cross-layer and cross-step signals. Directly relevant to understanding how sparsity changes temporally during generation.
  - [GitHub: iLearn-Lab/ACL26-EvoSparse](https://github.com/iLearn-Lab/ACL26-EvoSparse)

---

### Search 2: Compute Sparsity for Reasoning / Thinking Tokens

- **ThinKV** (ICLR 2026 Oral) -- This is perhaps the most directly competing paper. It explicitly distinguishes *thought types within CoT* and finds that "attention sparsity reveals distinct thought types with varying importance." It applies phase-specific compression strategies (hybrid quantization-eviction assigned by thought importance). Tested on DeepSeek-R1-Distill, GPT-OSS, and AceReason. Achieves near-lossless accuracy with <5% of original KV cache.
  - [arXiv:2510.01290](https://arxiv.org/abs/2510.01290)

- **"Thinking with Reasoning Skills: Fewer Tokens, More Accuracy"** (arXiv 2604.21764, April 2026) -- Focuses on reducing thinking tokens while maintaining accuracy.
  - [arXiv:2604.21764](https://arxiv.org/html/2604.21764)

---

### Search 3: Phase-Aware Inference Optimization for Reasoning

- **PASCAL** (HPCA 2026) -- Phase-aware scheduling that explicitly distinguishes reasoning vs. answering phases in serving reasoning LLMs. Reduces tail TTFT by up to 72% on DeepSeek-R1-Distill-Qwen-32B. While this is systems/scheduling (not sparsity characterization), it validates that phase-awareness matters for reasoning models.
  - [arXiv:2602.11530](https://arxiv.org/abs/2602.11530)

---

### Search 4: Activation Sparsity in DeepSeek-R1

No papers were found specifically studying *activation sparsity patterns* within DeepSeek-R1's inference. The search results only describe R1's MoE architecture (37B of 671B params activated). This appears to be a genuine gap -- nobody has published a characterization of how activation sparsity behaves during R1's thinking vs. answering phases. This supports the paper's novelty.

---

### Search 5: Transformer Block Interaction (Attention + FFN Sparsity)

- **"Analyzing Feed-Forward Blocks in Transformers through the Lens of Attention Maps"** -- Shows FFN and its surrounding components tend to cancel each other's effects, suggesting redundancy.
  - [arXiv:2302.00456](https://arxiv.org/html/2302.00456v3)

- **"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions"** -- Directly studies attention-MLP interactions, showing attention heads activate specific MLP neurons through the residual connection.
  - [arXiv:2402.15055](https://arxiv.org/html/2402.15055v1)

---

### Search 6: Reasoning Model Efficient Inference 2026

- **Adaptive Parallel Reasoning** (Berkeley AI, May 2026) -- Introduces parallel reasoning to overcome linear scaling limits of sequential inference.
  - [BAIR Blog](https://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)

- **ZAYA1-8B** (May 2026) -- MoE reasoning model, 8B total but <1B active per token, 91.9% on AIME'25. Demonstrates the MoE approach to reasoning efficiency.
  - [BuildFastWithAI](https://www.buildfastwithai.com/blogs/zaya1-8b-reasoning-model-2026)

- **DUET** -- Collaborative inference with capable + lightweight model working together.
  - [arXiv:2605.01111](https://arxiv.org/html/2605.01111v1)

---

### Search 7: EMNLP 2026 ARR Deadline

**Confirmed:** The ARR submission deadline for EMNLP 2026 is **May 25, 2026**. Important note: since EMNLP and AACL share the ARR May cycle, authors must explicitly select a target conference at submission time, and this choice is binding.
- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR Dates](http://aclrollingreview.org/dates)

---

### Search 8: "Doing More With Less" (arXiv 2604.25098)

**Verified.** The paper exists: "Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling" by Ocean Monjur, Shahriar Kabir Nahin, and Anshuman Chhabra. Submitted April 28, 2026. Key finding: unstructured pruning can augment test-time scaling performance compared to structured pruning, and sometimes outperforms unpruned models. Tested on s1.1-7B and Qwen3-8B across four reasoning benchmarks.
- [arXiv:2604.25098](https://arxiv.org/abs/2604.25098)

---

### Search 9: Nemotron Elastic / ICML 2026

**Partially verified.** Nemotron Elastic exists (arXiv:2511.16664). The associated paper "Star Elastic: Many-in-One Reasoning LLMs with Efficient Budget Control" is accepted at **ICML 2026** (July 6-11, 2026, Seoul). The framework embeds multiple nested submodels within a single parent model. Applied to Nemotron Nano V2 12B, producing 9B and 6B submodels with 360x cost reduction vs. training from scratch.
- [arXiv:2511.16664](https://arxiv.org/abs/2511.16664)
- [ICML 2026](https://icml.cc/)

---

### Search 10: LazyEviction Token Importance Recurrence

**Verified.** LazyEviction (arXiv:2506.15969) introduces the **Token Importance Recurrence** phenomenon -- tokens regain high attention after multiple decoding steps. Uses Maximum Recurrence Interval (MRI) tracking. Reduces KV cache by 50% while maintaining accuracy on math reasoning. This is relevant because it shows attention patterns are dynamic during reasoning, with tokens becoming periodically important.
- [arXiv:2506.15969](https://arxiv.org/abs/2506.15969)

---

### Additional Key Papers Found

- **RaaS: Reasoning-Aware Attention Sparsity** (ACL 2025 Findings) -- Identifies "milestone tokens" in reasoning that emerge, are used, then become unimportant. Achieves O(L) time and memory. This is directly about *reasoning-specific* attention sparsity patterns.
  - [arXiv:2502.11147](https://arxiv.org/abs/2502.11147)

- **R-Sparse** (ICLR 2025) -- Rank-aware activation sparsity for LLM inference, 50% model-wide sparsity with 43% efficiency improvement.
  - [arXiv:2504.19449](https://arxiv.org/abs/2504.19449)

- **TEAL** (ICLR 2025 Spotlight) -- Training-free activation sparsity, 40-50% model-wide sparsity.
  - [arXiv:2408.14690](https://arxiv.org/abs/2408.14690)

- **The Sparse Frontier** (2025) -- Largest-scale empirical analysis of sparse attention trade-offs. Key finding: sparsity attainable during *decoding* is higher than during *prefilling*, and correlates with model size. No single strategy works across tasks.
  - [arXiv:2504.17768](https://arxiv.org/abs/2504.17768)

---

## Assessment of Novelty

**The proposed paper's novelty claim -- characterizing how attention and MLP activation sparsity *interact across reasoning phases* -- occupies a specific niche but faces real overlap threats:**

**Strongest threats to novelty:**
1. **ThinKV** (ICLR 2026 Oral) already shows that attention sparsity reveals distinct thought types with varying importance within CoT, and exploits this for phase-specific compression. If the proposed paper doesn't cite and differentiate from ThinKV, reviewers will flag this.
2. **CLADA** (Feb 2025) studies how activation sparsity should adapt based on cognitive load/reasoning difficulty -- conceptually very similar to "sparsity varies across reasoning phases."
3. **Polar Sparsity** (NeurIPS 2025) directly studies the MLP-vs-attention sparsity interaction and shows they behave differently under scaling.
4. **RaaS** (ACL 2025) identifies reasoning-specific attention patterns (milestone tokens) that change during reasoning.
5. **EvoSparse** (ACL 2026) studies how token importance dynamics evolve across steps and layers.

**Where the paper may still be novel:**
- No paper found specifically characterizes the *joint* behavior of attention AND MLP sparsity across explicit thinking vs. answering phases in reasoning LLMs (like DeepSeek-R1). ThinKV is closest but focuses on KV cache compression as the application, not on the characterization itself. Polar Sparsity studies the interaction but not in the context of reasoning phases. CLADA adapts sparsity by difficulty but doesn't separate attention from MLP sparsity. The intersection of (a) joint attention+MLP analysis, (b) explicit reasoning phase distinction, and (c) applied to modern reasoning models like R1 appears to be a genuine gap.

The paper's authors should be sure to cite and differentiate from ThinKV, CLADA, Polar Sparsity, RaaS, EvoSparse, Spark Transformer, and The Sparse Frontier at minimum.

agentId: a27928a3eda0c5ef3 (use SendMessage with to: 'a27928a3eda0c5ef3' to continue this agent)
&lt;usage>total_tokens: 37646
tool_uses: 24
duration_ms: 188814&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9729e54b-5c63-4914-b9d5-3549df31cecd",
  "isSidechain": false,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "type": "user",
  "uuid": "3b93c3f5-a9bd-4573-b0de-1f7f19a92679",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for concurrent and competing work that might overlap with a paper about \"characterizing how attention and MLP activation sparsity interact across reasoning phases in LLMs.\" This is the most critical search - I need to find work the paper's author may have missed.\n\nTry these searches:\n\n1. \"joint sparsity attention MLP reasoning LLM 2025 2026\" - any recent work on joint component sparsity in reasoning models\n\n2. \"compute sparsity reasoning model thinking tokens 2026\" - compute-side sparsity for reasoning\n\n3. \"phase-aware inference optimization reasoning LLM\" - phase-specific optimization for reasoning models\n\n4. \"activation sparsity DeepSeek-R1\" - anyone studying sparsity in DeepSeek-R1 specifically\n\n5. \"transformer block interaction sparsity attention feedforward\" - interaction between attention and FFN sparsity\n\n6. \"reasoning model efficient inference 2026\" - recent efficiency methods for reasoning models\n\n7. \"EMNLP 2026 ARR deadline May 2026\" - verify the ARR submission deadline\n\n8. \"Doing More With Less pruning test-time scaling arXiv 2604.25098\" - verify this paper\n\n9. \"Nemotron Elastic inference ICML 2026\" - verify this paper\n\n10. \"LazyEviction token importance recurrence\" - verify this paper\n\nUse WebSearch for each. Report exactly what you find. Be thorough - this determines whether the paper's novelty claim holds.",
    "agentId": "a27928a3eda0c5ef3",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive results across all 10 searches plus additional targeted searches. Here is my thorough report:\n\n---\n\n## Comprehensive Competitive Landscape Report\n\n### Search 1: Joint Sparsity Attention + MLP in Reasoning LLMs\n\nSeveral papers directly overlap with the proposed work's territory:\n\n**Most Threatening Competitors:**\n\n- **Spark Transformer** (NeurIPS 2025) -- Achieves sparsity in *both* FFN and attention simultaneously. Only 8% of FFN neurons activated, each token attends to max 256 tokens. 2.5x FLOP reduction. This is the closest work to \"joint attention+MLP sparsity\" but focuses on *architectural* sparsity (training a new model) rather than *characterizing* existing sparsity patterns in reasoning models.\n  - [arXiv:2506.06644](https://arxiv.org/abs/2506.06644)\n\n- **Polar Sparsity** (NeurIPS 2025) -- Key finding directly relevant: as batch size and sequence length grow, sparsity importance *shifts from MLP to Attention*. MLP union activation increases (sparsity vanishes) while attention head sparsity remains stable and batch-invariant. This paper studies the *interaction* between attention and MLP sparsity, which is very close to the proposed paper's topic.\n  - [arXiv:2505.14884](https://arxiv.org/abs/2505.14884)\n\n- **CLADA: Cognitive-Load-Aware Dynamic Activation** (Feb 2025) -- Directly studies how activation sparsity should *adapt* based on reasoning difficulty (cognitive load). Uses surprisal/entropy to modulate sparsity levels dynamically. Achieves 40%+ sparsity with ~20% speedup. This is quite close to \"phase-aware sparsity\" -- it argues sparsity should vary by task difficulty, analogous to varying across reasoning phases.\n  - [arXiv:2502.19078](https://arxiv.org/abs/2502.19078)\n\n- **EvoSparse** (ACL 2026 main) -- Studies how token importance *dynamics* evolve across decoding steps and layers for sparse attention. Reuses cross-layer and cross-step signals. Directly relevant to understanding how sparsity changes temporally during generation.\n  - [GitHub: iLearn-Lab/ACL26-EvoSparse](https://github.com/iLearn-Lab/ACL26-EvoSparse)\n\n---\n\n### Search 2: Compute Sparsity for Reasoning / Thinking Tokens\n\n- **ThinKV** (ICLR 2026 Oral) -- This is perhaps the most directly competing paper. It explicitly distinguishes *thought types within CoT* and finds that \"attention sparsity reveals distinct thought types with varying importance.\" It applies phase-specific compression strategies (hybrid quantization-eviction assigned by thought importance). Tested on DeepSeek-R1-Distill, GPT-OSS, and AceReason. Achieves near-lossless accuracy with <5% of original KV cache.\n  - [arXiv:2510.01290](https://arxiv.org/abs/2510.01290)\n\n- **\"Thinking with Reasoning Skills: Fewer Tokens, More Accuracy\"** (arXiv 2604.21764, April 2026) -- Focuses on reducing thinking tokens while maintaining accuracy.\n  - [arXiv:2604.21764](https://arxiv.org/html/2604.21764)\n\n---\n\n### Search 3: Phase-Aware Inference Optimization for Reasoning\n\n- **PASCAL** (HPCA 2026) -- Phase-aware scheduling that explicitly distinguishes reasoning vs. answering phases in serving reasoning LLMs. Reduces tail TTFT by up to 72% on DeepSeek-R1-Distill-Qwen-32B. While this is systems/scheduling (not sparsity characterization), it validates that phase-awareness matters for reasoning models.\n  - [arXiv:2602.11530](https://arxiv.org/abs/2602.11530)\n\n---\n\n### Search 4: Activation Sparsity in DeepSeek-R1\n\nNo papers were found specifically studying *activation sparsity patterns* within DeepSeek-R1's inference. The search results only describe R1's MoE architecture (37B of 671B params activated). This appears to be a genuine gap -- nobody has published a characterization of how activation sparsity behaves during R1's thinking vs. answering phases. This supports the paper's novelty.\n\n---\n\n### Search 5: Transformer Block Interaction (Attention + FFN Sparsity)\n\n- **\"Analyzing Feed-Forward Blocks in Transformers through the Lens of Attention Maps\"** -- Shows FFN and its surrounding components tend to cancel each other's effects, suggesting redundancy.\n  - [arXiv:2302.00456](https://arxiv.org/html/2302.00456v3)\n\n- **\"Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions\"** -- Directly studies attention-MLP interactions, showing attention heads activate specific MLP neurons through the residual connection.\n  - [arXiv:2402.15055](https://arxiv.org/html/2402.15055v1)\n\n---\n\n### Search 6: Reasoning Model Efficient Inference 2026\n\n- **Adaptive Parallel Reasoning** (Berkeley AI, May 2026) -- Introduces parallel reasoning to overcome linear scaling limits of sequential inference.\n  - [BAIR Blog](https://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)\n\n- **ZAYA1-8B** (May 2026) -- MoE reasoning model, 8B total but <1B active per token, 91.9% on AIME'25. Demonstrates the MoE approach to reasoning efficiency.\n  - [BuildFastWithAI](https://www.buildfastwithai.com/blogs/zaya1-8b-reasoning-model-2026)\n\n- **DUET** -- Collaborative inference with capable + lightweight model working together.\n  - [arXiv:2605.01111](https://arxiv.org/html/2605.01111v1)\n\n---\n\n### Search 7: EMNLP 2026 ARR Deadline\n\n**Confirmed:** The ARR submission deadline for EMNLP 2026 is **May 25, 2026**. Important note: since EMNLP and AACL share the ARR May cycle, authors must explicitly select a target conference at submission time, and this choice is binding.\n- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)\n- [ARR Dates](http://aclrollingreview.org/dates)\n\n---\n\n### Search 8: \"Doing More With Less\" (arXiv 2604.25098)\n\n**Verified.** The paper exists: \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\" by Ocean Monjur, Shahriar Kabir Nahin, and Anshuman Chhabra. Submitted April 28, 2026. Key finding: unstructured pruning can augment test-time scaling performance compared to structured pruning, and sometimes outperforms unpruned models. Tested on s1.1-7B and Qwen3-8B across four reasoning benchmarks.\n- [arXiv:2604.25098](https://arxiv.org/abs/2604.25098)\n\n---\n\n### Search 9: Nemotron Elastic / ICML 2026\n\n**Partially verified.** Nemotron Elastic exists (arXiv:2511.16664). The associated paper \"Star Elastic: Many-in-One Reasoning LLMs with Efficient Budget Control\" is accepted at **ICML 2026** (July 6-11, 2026, Seoul). The framework embeds multiple nested submodels within a single parent model. Applied to Nemotron Nano V2 12B, producing 9B and 6B submodels with 360x cost reduction vs. training from scratch.\n- [arXiv:2511.16664](https://arxiv.org/abs/2511.16664)\n- [ICML 2026](https://icml.cc/)\n\n---\n\n### Search 10: LazyEviction Token Importance Recurrence\n\n**Verified.** LazyEviction (arXiv:2506.15969) introduces the **Token Importance Recurrence** phenomenon -- tokens regain high attention after multiple decoding steps. Uses Maximum Recurrence Interval (MRI) tracking. Reduces KV cache by 50% while maintaining accuracy on math reasoning. This is relevant because it shows attention patterns are dynamic during reasoning, with tokens becoming periodically important.\n- [arXiv:2506.15969](https://arxiv.org/abs/2506.15969)\n\n---\n\n### Additional Key Papers Found\n\n- **RaaS: Reasoning-Aware Attention Sparsity** (ACL 2025 Findings) -- Identifies \"milestone tokens\" in reasoning that emerge, are used, then become unimportant. Achieves O(L) time and memory. This is directly about *reasoning-specific* attention sparsity patterns.\n  - [arXiv:2502.11147](https://arxiv.org/abs/2502.11147)\n\n- **R-Sparse** (ICLR 2025) -- Rank-aware activation sparsity for LLM inference, 50% model-wide sparsity with 43% efficiency improvement.\n  - [arXiv:2504.19449](https://arxiv.org/abs/2504.19449)\n\n- **TEAL** (ICLR 2025 Spotlight) -- Training-free activation sparsity, 40-50% model-wide sparsity.\n  - [arXiv:2408.14690](https://arxiv.org/abs/2408.14690)\n\n- **The Sparse Frontier** (2025) -- Largest-scale empirical analysis of sparse attention trade-offs. Key finding: sparsity attainable during *decoding* is higher than during *prefilling*, and correlates with model size. No single strategy works across tasks.\n  - [arXiv:2504.17768](https://arxiv.org/abs/2504.17768)\n\n---\n\n## Assessment of Novelty\n\n**The proposed paper's novelty claim -- characterizing how attention and MLP activation sparsity *interact across reasoning phases* -- occupies a specific niche but faces real overlap threats:**\n\n**Strongest threats to novelty:**\n1. **ThinKV** (ICLR 2026 Oral) already shows that attention sparsity reveals distinct thought types with varying importance within CoT, and exploits this for phase-specific compression. If the proposed paper doesn't cite and differentiate from ThinKV, reviewers will flag this.\n2. **CLADA** (Feb 2025) studies how activation sparsity should adapt based on cognitive load/reasoning difficulty -- conceptually very similar to \"sparsity varies across reasoning phases.\"\n3. **Polar Sparsity** (NeurIPS 2025) directly studies the MLP-vs-attention sparsity interaction and shows they behave differently under scaling.\n4. **RaaS** (ACL 2025) identifies reasoning-specific attention patterns (milestone tokens) that change during reasoning.\n5. **EvoSparse** (ACL 2026) studies how token importance dynamics evolve across steps and layers.\n\n**Where the paper may still be novel:**\n- No paper found specifically characterizes the *joint* behavior of attention AND MLP sparsity across explicit thinking vs. answering phases in reasoning LLMs (like DeepSeek-R1). ThinKV is closest but focuses on KV cache compression as the application, not on the characterization itself. Polar Sparsity studies the interaction but not in the context of reasoning phases. CLADA adapts sparsity by difficulty but doesn't separate attention from MLP sparsity. The intersection of (a) joint attention+MLP analysis, (b) explicit reasoning phase distinction, and (c) applied to modern reasoning models like R1 appears to be a genuine gap.\n\nThe paper's authors should be sure to cite and differentiate from ThinKV, CLADA, Polar Sparsity, RaaS, EvoSparse, Spark Transformer, and The Sparse Frontier at minimum."
      }
    ],
    "totalDurationMs": 188814,
    "totalTokens": 37646,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2107,
      "cache_read_input_tokens": 32529,
      "output_tokens": 3009,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2107
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3009,
          "cache_read_input_tokens": 32529,
          "cache_creation_input_tokens": 2107,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2107,
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
  "sourceToolAssistantUUID": "9729e54b-5c63-4914-b9d5-3549df31cecd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
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
  "leafUuid": "3b93c3f5-a9bd-4573-b0de-1f7f19a92679",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing attention-MLP sparsity interaction in reasoning models",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

### Assistant

_source line 22 · 2026-05-12T00:23:14.901Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have extensive research results. Let me also check a few more things that are critical:

1. CLADA is a potentially missed competitor - let me look at this more carefully
2. The idea has been repositioned as a characterization study with the interaction surface as the core contribution
3. Let me check RAC's venue (workshop vs main)

Let me also verify a couple more things and then do a deep assessment.

Key findings so far:
1. All major cited papers verified (R-Sparse, Polar Sparsity, ThinKV, TEAL, etc.)
2. The "cross-partial derivative" / "sparsity interaction surface" terminology is genuinely novel - not found in literature


3. No existing work directly characterizes how attention and MLP sparsity interact across different reasoning phases
4. CLADA adapts activation sparsity based on cognitive load and could be a relevant competitor I need to examine more closely
5. The literature already shows that attention and MLP sparsity respond differently to batching, and joint pruning produces different results than pruning either component alone

I should dig deeper into CLADA and confirm whether RAC was published as a workshop paper or in the main conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b93c3f5-a9bd-4573-b0de-1f7f19a92679",
  "isSidechain": false,
  "requestId": "req_011Cawin8YBcvPVgdkkpkjzS",
  "type": "assistant",
  "uuid": "5f1f1aef-14f3-431b-bb90-6e30390fb98d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLw5dCq7gwCEoU5strJbVv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11586,
      "cache_read_input_tokens": 33630,
      "output_tokens": 1073,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11586,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1073,
          "cache_read_input_tokens": 33630,
          "cache_creation_input_tokens": 11586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11586
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

_source line 23 · 2026-05-12T00:23:14.902Z_

Good research so far. Let me check a couple more critical items — particularly CLADA (a potentially missed competitor) and RAC's venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f1f1aef-14f3-431b-bb90-6e30390fb98d",
  "isSidechain": false,
  "requestId": "req_011Cawin8YBcvPVgdkkpkjzS",
  "type": "assistant",
  "uuid": "5f38c13e-4d88-4299-ba19-3037dfdb2ec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLw5dCq7gwCEoU5strJbVv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11586,
      "cache_read_input_tokens": 33630,
      "output_tokens": 1073,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11586,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1073,
          "cache_read_input_tokens": 33630,
          "cache_creation_input_tokens": 11586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11586
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

_source line 24 · 2026-05-12T00:23:25.837Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UoigfPN1StD9FnJJUvXkKJ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify CLADA and RAC papers",
  "prompt": "Search the web for these specific papers. I need detailed verification.\n\n1. Search for \"CLADA Cognitive-Load-Aware Dynamic Activation arXiv 2502.19078\" - I need to know: does this paper study BOTH attention AND MLP sparsity jointly? Or is it MLP-only? Does it consider reasoning phases? What models does it test on? This is critical for assessing novelty overlap with a paper about joint attention-MLP sparsity interaction across reasoning phases.\n\n2. Search for \"RAC reasoning models pruned chain-of-thought reconstruction NeurIPS 2025\" - is this NeurIPS 2025 main conference or NeurIPS 2025 Workshop? The URL pattern neurips.cc/virtual/2025/126571 was mentioned - check if this is a workshop paper.\n\n3. Search for \"WAS weight-aware activation sparsity EMNLP 2025\" or \"weight-aware activation sparsity Bayesian optimization\" - verify venue and key claims. The proposal cites this as \"EMNLP 2025.\"\n\n4. Search for \"DeepSeek-R1-Distill-Llama-8B\" - verify this model exists (not \"DeepSeek-R1-Distill-Llama-3.1-8B\" or something else). What architecture is it based on? Is it Llama-3.1 architecture? This matters for codebase compatibility claims.\n\nUse WebSearch and WebFetch if needed. Report exactly what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f38c13e-4d88-4299-ba19-3037dfdb2ec1",
  "isSidechain": false,
  "requestId": "req_011Cawin8YBcvPVgdkkpkjzS",
  "type": "assistant",
  "uuid": "fc21d7ab-641c-4969-9d43-3d2915d33fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLw5dCq7gwCEoU5strJbVv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11586,
      "cache_read_input_tokens": 33630,
      "output_tokens": 1073,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11586,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1073,
          "cache_read_input_tokens": 33630,
          "cache_creation_input_tokens": 11586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11586
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

_source line 25 · 2026-05-12T00:23:30.573Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01F72z4C4rK1GRr651ZRVbqD`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check Polar Sparsity TEAL codebases",
  "prompt": "Search the web for information about the practical usability of these codebases. I need to assess whether building on them within 14 days is realistic.\n\n1. Search for \"Polar Sparsity GitHub susavlsh10\" - how mature is this codebase? How many stars, commits, supported models? Does it support Llama 3.1 / DeepSeek-R1-Distill models?\n\n2. Search for \"TEAL GitHub FasterDecoding\" - same questions. Is it a proof of concept or production-ready? What models does it support?\n\n3. Search for \"R-Sparse GitHub VITA-Group\" - same questions. What models does it support? Does it have custom kernels?\n\n4. Search for \"ActTail GitHub implementation\" or \"ActTail activation sparsity code\" - is there an open-source implementation?\n\nUse WebSearch. Report what you find about each codebase's maturity and model support."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc21d7ab-641c-4969-9d43-3d2915d33fad",
  "isSidechain": false,
  "requestId": "req_011Cawin8YBcvPVgdkkpkjzS",
  "type": "assistant",
  "uuid": "242a53f7-913c-42f6-ab19-cd3f0b5c8ee2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLw5dCq7gwCEoU5strJbVv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11586,
      "cache_read_input_tokens": 33630,
      "output_tokens": 1073,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11586,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1073,
          "cache_read_input_tokens": 33630,
          "cache_creation_input_tokens": 11586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11586
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

_source line 26 · 2026-05-12T00:25:24.754Z_

<details><summary>↩ Tool result · `toolu_01F72z4C4rK1GRr651ZRVbqD`</summary>

```text
Now I have comprehensive information on all four codebases. Here is the assessment:

---

## Codebase Maturity Assessment for 14-Day Build Feasibility

### 1. Polar Sparsity (susavlsh10/Polar-Sparsity)

**Repository stats:** 6 stars, 6 commits, 0 forks, 1 open issue. This is a very young, low-activity repository.

**Supported models (in code):** OPT-6.7B, OPT-66B, Llama-2-7B, Llama-3.1-70B. The paper also mentions Qwen and Mistral. **Llama 3.1 is explicitly listed** in the model index (`activations.py`). **DeepSeek-R1-Distill is NOT supported.**

**Custom kernels:** Yes -- custom Triton kernels for selective MLP and attention operations with autotuning.

**Maturity verdict:** Early-stage research code. Only 6 commits suggests the code was dumped in one or two pushes rather than iteratively developed. The README notes that benchmark evaluation uses HuggingFace masking rather than optimized kernels. Building on this within 14 days is risky -- you would be debugging and extending a minimally-maintained research prototype. Adding DeepSeek-R1-Distill support would require understanding and modifying the router/predictor architecture for a different model family.

**Key risk:** Extremely low community adoption means you will be on your own for bugs and issues.

---

### 2. TEAL (FasterDecoding/TEAL)

**Repository stats:** 164 stars, 21 commits, 15 forks. The most popular of the four, with meaningful community interest.

**Supported models:** Llama-2/3 (7B to 70B) and Mistral, with pre-calibrated thresholds provided. **Llama 3.1 is NOT explicitly mentioned** (the repo references "Llama-3" broadly). **DeepSeek-R1-Distill is NOT supported.**

**Custom kernels:** Yes -- custom sparse CUDA/Triton kernels in a `kernels/` directory.

**Critical caveat:** The README **explicitly states**: *"Please treat the current inference implementation as just a proof of concept!"* Known limitations include:
- FP16 only (BF16 not supported due to Triton limitations)
- Block-wise greedy sparsities not implemented
- Quantized sparse kernels unavailable
- Speculative decoding untested

**Maturity verdict:** The method itself is well-validated (ICLR 2025 Spotlight), but the code is self-described as a proof of concept. The evaluation/calibration pipeline is more mature than the inference pipeline. Adding new models would require calibrating magnitude thresholds. TEAL's approach (simple magnitude-based thresholding) is conceptually the simplest of the four, which is an advantage for a 14-day timeline -- but the PoC status of the inference code is a real concern.

**Key risk:** The authors themselves warn the inference code is not production-quality. BF16 limitation may be a blocker depending on your target models.

---

### 3. R-Sparse (VITA-Group/R-Sparse)

**Repository stats:** 19 stars, **only 2 commits**, 5 forks. Language breakdown: 85% Python, 13.8% CUDA.

**Supported models:** Llama-2, Llama-3, Mistral. **Llama 3.1 and DeepSeek-R1-Distill are NOT mentioned.**

**Custom kernels:** Yes -- there is a `triton_kernel/` directory and CUDA code (13.8% of the repo). However, the README has a TODO list that includes "Triton implementation (pending)" -- suggesting the Triton kernels may be incomplete or not yet integrated.

**Maturity verdict:** This is the least mature of the three available codebases. Only 2 commits on main signals a single code dump. The pending TODO items (accuracy benchmark examples, Triton implementation) indicate the repository is incomplete. Despite being published at ICLR 2025, the code release appears to be an afterthought.

**Key risk:** Incomplete implementation with pending critical features. Building on a 2-commit repo with unfinished Triton kernels in 14 days is very high risk.

---

### 4. ActTail

**Paper:** arXiv 2603.12272, published February 2026. Evaluated on LLaMA-2-7B, LLaMA-2-13B, Mistral-7B.

**Code availability: NO open-source implementation exists.** There is no GitHub repository, no code link in the paper, and no "code will be released" statement. Multiple searches turned up nothing.

**Maturity verdict:** Paper-only. You would need to implement this from scratch. The method (TopK magnitude-based sparsity with per-projection budgets derived from heavy-tail exponents of weight spectral density) is conceptually straightforward but implementing it correctly with efficient kernels in 14 days would be a significant undertaking.

**Key risk:** Complete implementation from scratch required.

---

## Summary Comparison

| Criteria | Polar Sparsity | TEAL | R-Sparse | ActTail |
|---|---|---|---|---|
| Stars | 6 | 164 | 19 | N/A |
| Commits | 6 | 21 | 2 | No repo |
| Custom kernels | Triton | CUDA/Triton | CUDA + Triton (partial) | N/A |
| Llama 3.1 | Yes (70B) | Not explicit | No | No |
| DeepSeek-R1-Distill | No | No | No | No |
| Self-assessed maturity | Research code | "Proof of concept" | Incomplete TODOs | Paper only |
| 14-day feasibility | High risk | Moderate risk | Very high risk | Unrealistic |

**Bottom line:** None of these are production-ready. TEAL has the most community traction and the simplest method (magnitude thresholding), making it the most realistic foundation for a 14-day effort -- but even it is self-described as a PoC. Polar Sparsity is the only one with explicit Llama 3.1 support in code, but is very low-activity. None support DeepSeek-R1-Distill, so adding that model family would require custom integration work regardless of which codebase you choose.

Sources:
- [Polar Sparsity GitHub](https://github.com/susavlsh10/Polar-Sparsity)
- [Polar Sparsity Paper (arXiv)](https://arxiv.org/abs/2505.14884)
- [TEAL GitHub](https://github.com/FasterDecoding/TEAL)
- [TEAL Paper (arXiv)](https://arxiv.org/abs/2408.14690)
- [TEAL Blog Post (Together AI)](https://www.together.ai/blog/teal-training-free-activation-sparsity-in-large-language-models)
- [R-Sparse GitHub](https://github.com/VITA-Group/R-Sparse)
- [R-Sparse Paper (arXiv)](https://arxiv.org/abs/2504.19449)
- [ActTail Paper (arXiv)](https://arxiv.org/abs/2603.12272)

agentId: a8ee124bb0e70493a (use SendMessage with to: 'a8ee124bb0e70493a' to continue this agent)
&lt;usage>total_tokens: 24334
tool_uses: 15
duration_ms: 114178&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "242a53f7-913c-42f6-ab19-cd3f0b5c8ee2",
  "isSidechain": false,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "type": "user",
  "uuid": "da3dafe0-2b81-4906-bb10-34a7f2ede5f2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for information about the practical usability of these codebases. I need to assess whether building on them within 14 days is realistic.\n\n1. Search for \"Polar Sparsity GitHub susavlsh10\" - how mature is this codebase? How many stars, commits, supported models? Does it support Llama 3.1 / DeepSeek-R1-Distill models?\n\n2. Search for \"TEAL GitHub FasterDecoding\" - same questions. Is it a proof of concept or production-ready? What models does it support?\n\n3. Search for \"R-Sparse GitHub VITA-Group\" - same questions. What models does it support? Does it have custom kernels?\n\n4. Search for \"ActTail GitHub implementation\" or \"ActTail activation sparsity code\" - is there an open-source implementation?\n\nUse WebSearch. Report what you find about each codebase's maturity and model support.",
    "agentId": "a8ee124bb0e70493a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on all four codebases. Here is the assessment:\n\n---\n\n## Codebase Maturity Assessment for 14-Day Build Feasibility\n\n### 1. Polar Sparsity (susavlsh10/Polar-Sparsity)\n\n**Repository stats:** 6 stars, 6 commits, 0 forks, 1 open issue. This is a very young, low-activity repository.\n\n**Supported models (in code):** OPT-6.7B, OPT-66B, Llama-2-7B, Llama-3.1-70B. The paper also mentions Qwen and Mistral. **Llama 3.1 is explicitly listed** in the model index (`activations.py`). **DeepSeek-R1-Distill is NOT supported.**\n\n**Custom kernels:** Yes -- custom Triton kernels for selective MLP and attention operations with autotuning.\n\n**Maturity verdict:** Early-stage research code. Only 6 commits suggests the code was dumped in one or two pushes rather than iteratively developed. The README notes that benchmark evaluation uses HuggingFace masking rather than optimized kernels. Building on this within 14 days is risky -- you would be debugging and extending a minimally-maintained research prototype. Adding DeepSeek-R1-Distill support would require understanding and modifying the router/predictor architecture for a different model family.\n\n**Key risk:** Extremely low community adoption means you will be on your own for bugs and issues.\n\n---\n\n### 2. TEAL (FasterDecoding/TEAL)\n\n**Repository stats:** 164 stars, 21 commits, 15 forks. The most popular of the four, with meaningful community interest.\n\n**Supported models:** Llama-2/3 (7B to 70B) and Mistral, with pre-calibrated thresholds provided. **Llama 3.1 is NOT explicitly mentioned** (the repo references \"Llama-3\" broadly). **DeepSeek-R1-Distill is NOT supported.**\n\n**Custom kernels:** Yes -- custom sparse CUDA/Triton kernels in a `kernels/` directory.\n\n**Critical caveat:** The README **explicitly states**: *\"Please treat the current inference implementation as just a proof of concept!\"* Known limitations include:\n- FP16 only (BF16 not supported due to Triton limitations)\n- Block-wise greedy sparsities not implemented\n- Quantized sparse kernels unavailable\n- Speculative decoding untested\n\n**Maturity verdict:** The method itself is well-validated (ICLR 2025 Spotlight), but the code is self-described as a proof of concept. The evaluation/calibration pipeline is more mature than the inference pipeline. Adding new models would require calibrating magnitude thresholds. TEAL's approach (simple magnitude-based thresholding) is conceptually the simplest of the four, which is an advantage for a 14-day timeline -- but the PoC status of the inference code is a real concern.\n\n**Key risk:** The authors themselves warn the inference code is not production-quality. BF16 limitation may be a blocker depending on your target models.\n\n---\n\n### 3. R-Sparse (VITA-Group/R-Sparse)\n\n**Repository stats:** 19 stars, **only 2 commits**, 5 forks. Language breakdown: 85% Python, 13.8% CUDA.\n\n**Supported models:** Llama-2, Llama-3, Mistral. **Llama 3.1 and DeepSeek-R1-Distill are NOT mentioned.**\n\n**Custom kernels:** Yes -- there is a `triton_kernel/` directory and CUDA code (13.8% of the repo). However, the README has a TODO list that includes \"Triton implementation (pending)\" -- suggesting the Triton kernels may be incomplete or not yet integrated.\n\n**Maturity verdict:** This is the least mature of the three available codebases. Only 2 commits on main signals a single code dump. The pending TODO items (accuracy benchmark examples, Triton implementation) indicate the repository is incomplete. Despite being published at ICLR 2025, the code release appears to be an afterthought.\n\n**Key risk:** Incomplete implementation with pending critical features. Building on a 2-commit repo with unfinished Triton kernels in 14 days is very high risk.\n\n---\n\n### 4. ActTail\n\n**Paper:** arXiv 2603.12272, published February 2026. Evaluated on LLaMA-2-7B, LLaMA-2-13B, Mistral-7B.\n\n**Code availability: NO open-source implementation exists.** There is no GitHub repository, no code link in the paper, and no \"code will be released\" statement. Multiple searches turned up nothing.\n\n**Maturity verdict:** Paper-only. You would need to implement this from scratch. The method (TopK magnitude-based sparsity with per-projection budgets derived from heavy-tail exponents of weight spectral density) is conceptually straightforward but implementing it correctly with efficient kernels in 14 days would be a significant undertaking.\n\n**Key risk:** Complete implementation from scratch required.\n\n---\n\n## Summary Comparison\n\n| Criteria | Polar Sparsity | TEAL | R-Sparse | ActTail |\n|---|---|---|---|---|\n| Stars | 6 | 164 | 19 | N/A |\n| Commits | 6 | 21 | 2 | No repo |\n| Custom kernels | Triton | CUDA/Triton | CUDA + Triton (partial) | N/A |\n| Llama 3.1 | Yes (70B) | Not explicit | No | No |\n| DeepSeek-R1-Distill | No | No | No | No |\n| Self-assessed maturity | Research code | \"Proof of concept\" | Incomplete TODOs | Paper only |\n| 14-day feasibility | High risk | Moderate risk | Very high risk | Unrealistic |\n\n**Bottom line:** None of these are production-ready. TEAL has the most community traction and the simplest method (magnitude thresholding), making it the most realistic foundation for a 14-day effort -- but even it is self-described as a PoC. Polar Sparsity is the only one with explicit Llama 3.1 support in code, but is very low-activity. None support DeepSeek-R1-Distill, so adding that model family would require custom integration work regardless of which codebase you choose.\n\nSources:\n- [Polar Sparsity GitHub](https://github.com/susavlsh10/Polar-Sparsity)\n- [Polar Sparsity Paper (arXiv)](https://arxiv.org/abs/2505.14884)\n- [TEAL GitHub](https://github.com/FasterDecoding/TEAL)\n- [TEAL Paper (arXiv)](https://arxiv.org/abs/2408.14690)\n- [TEAL Blog Post (Together AI)](https://www.together.ai/blog/teal-training-free-activation-sparsity-in-large-language-models)\n- [R-Sparse GitHub](https://github.com/VITA-Group/R-Sparse)\n- [R-Sparse Paper (arXiv)](https://arxiv.org/abs/2504.19449)\n- [ActTail Paper (arXiv)](https://arxiv.org/abs/2603.12272)"
      }
    ],
    "totalDurationMs": 114178,
    "totalTokens": 24334,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 669,
      "cache_read_input_tokens": 21856,
      "output_tokens": 1808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 669
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1808,
          "cache_read_input_tokens": 21856,
          "cache_creation_input_tokens": 669,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 669,
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
  "sourceToolAssistantUUID": "242a53f7-913c-42f6-ab19-cd3f0b5c8ee2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T00:28:07.500Z_

<details><summary>↩ Tool result · `toolu_01UoigfPN1StD9FnJJUvXkKJ`</summary>

```text
Excellent. Now I have the full picture. The RAC paper was presented at both venues. Let me compile the comprehensive findings.

Here are the detailed findings for all four items:

---

## 1. CLADA (arXiv 2502.19078)

**Full title:** "Sparse Brains are Also Adaptive Brains: Cognitive-Load-Aware Dynamic Activation for LLMs"
**Authors:** Yiheng Yang, Yujie Wang, Chi Ma, Lei Yu, Emmanuele Chersoni, Chu-Ren Huang

**MLP-only, NOT joint attention+MLP.** The paper explicitly states: "we especially focus on the MLP blocks of LLM models, which constitute approximately 67% of the parameters." There is no mention of sparsifying attention heads or attention weight matrices anywhere in the methodology. It does **not** study the interaction between attention and MLP sparsity.

**No reasoning phases.** The "cognitive load" concept refers to **token-level linguistic complexity** measured via surprisal (negative log-probability of individual tokens) and entropy (vocabulary distribution uncertainty). This is computed per-token during generation. The paper draws analogies to neuroscience ERP components (N400/P600) but these refer to semantic processing difficulty at the word level -- not to reasoning phases like "thinking vs. output" or "chain-of-thought vs. answer generation."

**Models tested:** OPT-350M, OPT-2.7B, Gemma-2B, LLaMA-2-7B, LLaMA-3-8B, Mistral-7B (six models total).

**Bottom line for novelty assessment:** A proposal about joint attention-MLP sparsity interaction across reasoning phases would have minimal novelty overlap with CLADA, which is MLP-only and does not consider reasoning phases.

---

## 2. RAC -- "Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction"

**Authors:** Ryan Lucas, Kayhan Behdin, Zhipeng Wang, Qingquan Song, Shao Tang, Rahul Mazumder

**Venue status -- it appeared at BOTH venues:**
- **NeurIPS 2025 Workshop** -- specifically "The First Workshop on Efficient Reasoning" (workshop code "ER"). Presented as a **poster** at the workshop. The NeurIPS virtual page at `neurips.cc/virtual/2025/loc/san-diego/126571` confirms this. The OpenReview submission (forum ID `o9z7pK1C76`) is under "NeurIPS 2025 Workshop ER."
- **ICLR 2026 Main Conference** -- accepted as a **poster** at the main ICLR 2026 conference. The OpenReview page (forum ID `tyGfwG6xTh`) shows "ICLR 2026 Poster" with publication date January 26, 2026.

So: the URL pattern `neurips.cc/virtual/2025/126571` is indeed a **NeurIPS 2025 workshop paper**, not main conference. However, the same paper was subsequently accepted at **ICLR 2026 main conference** as a poster. If someone cites this as "NeurIPS 2025," that is technically a workshop citation, not a main conference citation.

---

## 3. WAS -- "Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models"

**Authors:** Ming Wang, Miao Zhang, Xuebo Liu, Liqiang Nie

**Venue confirmed: EMNLP 2025 Main Conference.** Published in "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing" (not Findings). The ACL Anthology entry is `2025.emnlp-main.57`, confirming it is a main conference paper.

**Sparsity scope:** WAS addresses activation sparsity broadly. It proposes a weight-aware scoring method for measuring activation importance, combined with constrained Bayesian optimization for block-level sparsity scheduling. The search results indicate it addresses sparsity across blocks (which include both attention and MLP components), using inter-block scheduling via Bayesian optimization and intra-block sparsity via greedy search. However, the abstract describes "activation sparsity" generically without explicitly distinguishing attention vs. MLP -- I could not get a fully definitive answer on whether it jointly optimizes both or focuses on MLP activations only from the publicly available information.

**Models tested:** The paper tests on LLaMA-2, LLaMA-3/3.1, and Mistral model families at 40%, 60%, and 75% sparsity levels. The specific mention of "LLaMA-3.1-8B" appears in analysis of activation distributions.

**Main result:** Up to 1.68x inference speedup at 60% model-level sparsity with no retraining or weight updates.

---

## 4. DeepSeek-R1-Distill-Llama-8B

**The model exists and the name is exactly "DeepSeek-R1-Distill-Llama-8B"** -- there is no "3.1" in the model name itself. However:

**It IS based on Llama-3.1-8B architecture.** The official HuggingFace model card at `huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B` explicitly lists the base model as **Llama-3.1-8B** in its model table. The model page states: "DeepSeek-R1-Distill models are fine-tuned based on open-source models, using samples generated by DeepSeek-R1. We slightly change their configs and tokenizers."

**Key specs:**
- 8B parameters, BF16 tensor type
- Based on Meta's Llama-3.1-8B-Base architecture
- Fine-tuned with 800K samples curated from DeepSeek-R1's reasoning data
- Modified configs and tokenizers from the base Llama-3.1
- Maximum context length: 32,768 tokens
- License: MIT (derived from llama3.1 license)

**For codebase compatibility:** Since the underlying architecture is Llama-3.1-8B, any codebase compatible with Llama-3.1 architecture should work, but note DeepSeek's warning that they "slightly change their configs and tokenizers" -- so one must use DeepSeek's specific settings, not the vanilla Llama-3.1 config.

---

Sources:
- [CLADA paper (arXiv)](https://arxiv.org/abs/2502.19078)
- [CLADA full HTML](https://arxiv.org/html/2502.19078)
- [CLADA GitHub](https://github.com/Oldify/CLADA)
- [RAC paper (arXiv)](https://arxiv.org/abs/2509.12464)
- [RAC at NeurIPS 2025 Workshop](https://neurips.cc/virtual/2025/loc/san-diego/126571)
- [RAC OpenReview - NeurIPS Workshop ER](https://openreview.net/forum?id=o9z7pK1C76)
- [RAC OpenReview - ICLR 2026](https://openreview.net/forum?id=tyGfwG6xTh)
- [WAS paper (ACL Anthology)](https://aclanthology.org/2025.emnlp-main.57/)
- [WAS GitHub](https://github.com/HITSZ-Miao-Group/WAS)
- [DeepSeek-R1-Distill-Llama-8B (HuggingFace)](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B)

agentId: afec513d3e1ff8dd8 (use SendMessage with to: 'afec513d3e1ff8dd8' to continue this agent)
&lt;usage>total_tokens: 26789
tool_uses: 22
duration_ms: 281658&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc21d7ab-641c-4969-9d43-3d2915d33fad",
  "isSidechain": false,
  "promptId": "4862c963-98f1-4305-955d-b5fa9b271a7d",
  "type": "user",
  "uuid": "df115b25-d5c4-4b83-8cef-9e1795e9f5df",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for these specific papers. I need detailed verification.\n\n1. Search for \"CLADA Cognitive-Load-Aware Dynamic Activation arXiv 2502.19078\" - I need to know: does this paper study BOTH attention AND MLP sparsity jointly? Or is it MLP-only? Does it consider reasoning phases? What models does it test on? This is critical for assessing novelty overlap with a paper about joint attention-MLP sparsity interaction across reasoning phases.\n\n2. Search for \"RAC reasoning models pruned chain-of-thought reconstruction NeurIPS 2025\" - is this NeurIPS 2025 main conference or NeurIPS 2025 Workshop? The URL pattern neurips.cc/virtual/2025/126571 was mentioned - check if this is a workshop paper.\n\n3. Search for \"WAS weight-aware activation sparsity EMNLP 2025\" or \"weight-aware activation sparsity Bayesian optimization\" - verify venue and key claims. The proposal cites this as \"EMNLP 2025.\"\n\n4. Search for \"DeepSeek-R1-Distill-Llama-8B\" - verify this model exists (not \"DeepSeek-R1-Distill-Llama-3.1-8B\" or something else). What architecture is it based on? Is it Llama-3.1 architecture? This matters for codebase compatibility claims.\n\nUse WebSearch and WebFetch if needed. Report exactly what you find.",
    "agentId": "afec513d3e1ff8dd8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Excellent. Now I have the full picture. The RAC paper was presented at both venues. Let me compile the comprehensive findings.\n\nHere are the detailed findings for all four items:\n\n---\n\n## 1. CLADA (arXiv 2502.19078)\n\n**Full title:** \"Sparse Brains are Also Adaptive Brains: Cognitive-Load-Aware Dynamic Activation for LLMs\"\n**Authors:** Yiheng Yang, Yujie Wang, Chi Ma, Lei Yu, Emmanuele Chersoni, Chu-Ren Huang\n\n**MLP-only, NOT joint attention+MLP.** The paper explicitly states: \"we especially focus on the MLP blocks of LLM models, which constitute approximately 67% of the parameters.\" There is no mention of sparsifying attention heads or attention weight matrices anywhere in the methodology. It does **not** study the interaction between attention and MLP sparsity.\n\n**No reasoning phases.** The \"cognitive load\" concept refers to **token-level linguistic complexity** measured via surprisal (negative log-probability of individual tokens) and entropy (vocabulary distribution uncertainty). This is computed per-token during generation. The paper draws analogies to neuroscience ERP components (N400/P600) but these refer to semantic processing difficulty at the word level -- not to reasoning phases like \"thinking vs. output\" or \"chain-of-thought vs. answer generation.\"\n\n**Models tested:** OPT-350M, OPT-2.7B, Gemma-2B, LLaMA-2-7B, LLaMA-3-8B, Mistral-7B (six models total).\n\n**Bottom line for novelty assessment:** A proposal about joint attention-MLP sparsity interaction across reasoning phases would have minimal novelty overlap with CLADA, which is MLP-only and does not consider reasoning phases.\n\n---\n\n## 2. RAC -- \"Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction\"\n\n**Authors:** Ryan Lucas, Kayhan Behdin, Zhipeng Wang, Qingquan Song, Shao Tang, Rahul Mazumder\n\n**Venue status -- it appeared at BOTH venues:**\n- **NeurIPS 2025 Workshop** -- specifically \"The First Workshop on Efficient Reasoning\" (workshop code \"ER\"). Presented as a **poster** at the workshop. The NeurIPS virtual page at `neurips.cc/virtual/2025/loc/san-diego/126571` confirms this. The OpenReview submission (forum ID `o9z7pK1C76`) is under \"NeurIPS 2025 Workshop ER.\"\n- **ICLR 2026 Main Conference** -- accepted as a **poster** at the main ICLR 2026 conference. The OpenReview page (forum ID `tyGfwG6xTh`) shows \"ICLR 2026 Poster\" with publication date January 26, 2026.\n\nSo: the URL pattern `neurips.cc/virtual/2025/126571` is indeed a **NeurIPS 2025 workshop paper**, not main conference. However, the same paper was subsequently accepted at **ICLR 2026 main conference** as a poster. If someone cites this as \"NeurIPS 2025,\" that is technically a workshop citation, not a main conference citation.\n\n---\n\n## 3. WAS -- \"Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models\"\n\n**Authors:** Ming Wang, Miao Zhang, Xuebo Liu, Liqiang Nie\n\n**Venue confirmed: EMNLP 2025 Main Conference.** Published in \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing\" (not Findings). The ACL Anthology entry is `2025.emnlp-main.57`, confirming it is a main conference paper.\n\n**Sparsity scope:** WAS addresses activation sparsity broadly. It proposes a weight-aware scoring method for measuring activation importance, combined with constrained Bayesian optimization for block-level sparsity scheduling. The search results indicate it addresses sparsity across blocks (which include both attention and MLP components), using inter-block scheduling via Bayesian optimization and intra-block sparsity via greedy search. However, the abstract describes \"activation sparsity\" generically without explicitly distinguishing attention vs. MLP -- I could not get a fully definitive answer on whether it jointly optimizes both or focuses on MLP activations only from the publicly available information.\n\n**Models tested:** The paper tests on LLaMA-2, LLaMA-3/3.1, and Mistral model families at 40%, 60%, and 75% sparsity levels. The specific mention of \"LLaMA-3.1-8B\" appears in analysis of activation distributions.\n\n**Main result:** Up to 1.68x inference speedup at 60% model-level sparsity with no retraining or weight updates.\n\n---\n\n## 4. DeepSeek-R1-Distill-Llama-8B\n\n**The model exists and the name is exactly \"DeepSeek-R1-Distill-Llama-8B\"** -- there is no \"3.1\" in the model name itself. However:\n\n**It IS based on Llama-3.1-8B architecture.** The official HuggingFace model card at `huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B` explicitly lists the base model as **Llama-3.1-8B** in its model table. The model page states: \"DeepSeek-R1-Distill models are fine-tuned based on open-source models, using samples generated by DeepSeek-R1. We slightly change their configs and tokenizers.\"\n\n**Key specs:**\n- 8B parameters, BF16 tensor type\n- Based on Meta's Llama-3.1-8B-Base architecture\n- Fine-tuned with 800K samples curated from DeepSeek-R1's reasoning data\n- Modified configs and tokenizers from the base Llama-3.1\n- Maximum context length: 32,768 tokens\n- License: MIT (derived from llama3.1 license)\n\n**For codebase compatibility:** Since the underlying architecture is Llama-3.1-8B, any codebase compatible with Llama-3.1 architecture should work, but note DeepSeek's warning that they \"slightly change their configs and tokenizers\" -- so one must use DeepSeek's specific settings, not the vanilla Llama-3.1 config.\n\n---\n\nSources:\n- [CLADA paper (arXiv)](https://arxiv.org/abs/2502.19078)\n- [CLADA full HTML](https://arxiv.org/html/2502.19078)\n- [CLADA GitHub](https://github.com/Oldify/CLADA)\n- [RAC paper (arXiv)](https://arxiv.org/abs/2509.12464)\n- [RAC at NeurIPS 2025 Workshop](https://neurips.cc/virtual/2025/loc/san-diego/126571)\n- [RAC OpenReview - NeurIPS Workshop ER](https://openreview.net/forum?id=o9z7pK1C76)\n- [RAC OpenReview - ICLR 2026](https://openreview.net/forum?id=tyGfwG6xTh)\n- [WAS paper (ACL Anthology)](https://aclanthology.org/2025.emnlp-main.57/)\n- [WAS GitHub](https://github.com/HITSZ-Miao-Group/WAS)\n- [DeepSeek-R1-Distill-Llama-8B (HuggingFace)](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B)"
      }
    ],
    "totalDurationMs": 281658,
    "totalTokens": 26789,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 280,
      "cache_read_input_tokens": 24587,
      "output_tokens": 1921,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 280
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1921,
          "cache_read_input_tokens": 24587,
          "cache_creation_input_tokens": 280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 280,
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
  "sourceToolAssistantUUID": "fc21d7ab-641c-4969-9d43-3d2915d33fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "df115b25-d5c4-4b83-8cef-9e1795e9f5df",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing attention-MLP sparsity interaction in reasoning models",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

### Assistant

_source line 30 · 2026-05-12T00:29:40.051Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have extensive research results. Let me synthesize my findings and form my assessment.

## Key Findings

### Reference Verification
- All major papers verified to exist with correct venues
- RAC is NeurIPS 2025 Workshop (+ ICLR 2026 Main) — the proposal correctly updated this to "NeurIPS 2025 Workshop on Efficient Reasoning"
- RaaS is ACL 2025 Findings, not ACL 2025 Main — the proposal correctly says "ACL 2025 Findings"


- DeepSeek-R1-Distill-Llama-8B is indeed based on Llama-3.1-8B, which works well for the compatibility requirements
- CLADA operates as MLP-only, so it's not a direct competitor to what the proposal is doing with interaction surface characterization

### Novelty Assessment
The sparsity interaction surface framework using cross-partial derivatives is genuinely novel—no existing work formalizes how attention and MLP sparsity interact with each other. The proposal uniquely characterizes joint attention+MLP sparsity behavior across different reasoning phases, which hasn't been done before.

There are some related works that touch on adjacent territory: Polar Sparsity observed that attention and MLP sparsity behave differently (MLP sparsity collapses under batching while attention head sparsity remains stable), and AMP empirically showed that joint pruning differs from attention-only pruning by 23 percentage points in accuracy. ThinKV does phase-specific sparsity for reasoning models, though it targets KV cache rather than compute sparsity. The main contribution here is empirical characterization rather than a new algorithm.

### Feasibility Assessment
DeepSeek-R1-Distill-Llama-8B uses the Llama-3.1 architecture, which means both Polar Sparsity and TEAL should be compatible with it.

The single-model focus reduces architecture integration risk, and the 170-hour GPU budget fits within the 200-hour constraint with a 14-day timeline that works within the 16-day window. However, the existing codebases are quite immature—TEAL describes itself as a proof of concept, Polar Sparsity has minimal commits, and R-Sparse is barely started. ActTail lacks any open-source implementation. The experimental grid of 5×5 sparsity levels across 4 phases, 6 benchmarks, and 50 prompts per benchmark is substantial, so I need to validate whether 170 hours is realistic. For a characterization study, I might not need production-grade kernels, which could simplify the implementation. There's a fundamental tension here—the user explicitly wants a METHOD with new algorithms, but this paper is structured as a characterization study with grid search as the application. The generator even notes this isn't positioned as an algorithmic contribution. I need to figure out if the interaction surface characterization plus phase-aware allocation can actually be reframed as a genuine method, or if this approach doesn't align with what the user is asking for. The reviewer feedback has consistently pushed toward positioning this as a characterization study rather than a pure methods paper, and the generator has adapted accordingly—though this creates some tension with the user's "METHOD ONLY" constraint. The impact hinges on what the interaction analysis reveals: strong interaction effects would make this actionable guidance for joint sparsity design in reasoning models with moderate-to-high impact, while near-zero interactions would be a useful negative result confirming additive assumptions but landing at a lower tier. The practical speedup is solid but not transformative, especially since it's framed as a demonstration of the characterization rather than the main contribution.

Now scoring the work itself: the interaction surface formalization is genuinely novel—measuring cross-partial derivatives of joint attention and MLP sparsity hasn't been done before—but the empirical approach is standard grid sweeping with finite differences, and the theoretical motivation, while conceptually clean, lacks mathematical depth. The positioning relative to ThinKV and R-Sparse is clear and well-differentiated. Feasibility looks reasonable within the constraints, though there's a note about codebase compatibility that seems to cut off. maturity (TEAL is PoC, Polar Sparsity has 6 commits) creates real integration risk
- For the characterization core, you can use masking/zeroing without production kernels — feasible
- For the speedup demonstration, you need working kernels — risky with these codebases
- The scope is still ambitious for 14 days: 5×5 grid × 4 phases × 6 benchmarks × 50+ prompts + baselines + ablations
- Held back by codebase risk and scope ambition

**Clarity: 4/5**
- The proposal is well-structured with clear delineation of contributions
- The theoretical framework (three interaction regimes) is well-motivated
- Baseline selection is comprehensive and well-justified
- The fallback contribution structure is honest and well-thought-out
- The proposal is lengthy and somewhat repetitive in places

**Impact: 3/5**
- The interaction characterization is useful but incremental — it guides design rather than introducing a breakthrough
- The practical speedup (1.3-1.7x) lags behind dedicated methods (Polar Sparsity 2.2x, Twilight 3.9x)
- The contribution hinges on whether the interaction is non-trivial; if it's not, this becomes a Findings-level paper
- It addresses a real gap in joint sparsity design for reasoning models, but the value is primarily informational
- The user wanted a novel algorithm, and this doesn't deliver that

Averaging the scores gives 3.5, which falls short of the 4.0 bar. I need to decide whether revising makes sense or if I should acknowledge this doesn't meet the threshold.

This is round 5 of 10, and the idea has genuinely improved — it's addressed most of the critical issues from round 1 like venue fit, budget, timeline, and benchmarks. The core research question is sound, but two fundamental problems persist. First, the user explicitly asked for a method contribution, yet this is fundamentally a characterization study with grid search applied — earlier review rounds pushed it toward profiling, which made it more honest but also more misaligned with what was requested. Second, the whole contribution depends on finding meaningful interaction effects; if those turn out to be negligible, this becomes at best a useful negative result suitable for Findings. The methodological novelty is thin — it's essentially grid search over eight parameters — and the empirical contribution, while interesting, doesn't quite reach top-venue Main conference caliber.

The path forward is either to genuinely strengthen the algorithmic side by developing something adaptive that uses online interaction estimates to dynamically adjust joint sparsity rather than relying on pre-computed grids, or to accept this is a characterization study and target Findings instead, which means accepting lower impact. But re-reading the user's requirements makes the tension unavoidable: they explicitly want METHOD ONLY, not profiling studies, and the current proposal is fundamentally a profiling study dressed up as an application. I'm reconsidering how severe the mismatch really is — the user did mention efficient serving of reasoning models, and the paper does propose a method: phase-aware joint allocation grounded in interaction surface analysis. The real problem is that the authors themselves downplay the algorithmic contribution, when they could reframe it as a genuine method with proper phase detection and online adaptation for joint sparsity selection. Let me also think through whether the previous review guidance actually conflicts with the user's requirements or if there's a way to reconcile them.

The core issue is clear now: the user explicitly wants a METHOD, not a profiling study, so the framing needs to flip entirely. The interaction surface discovery should be the analytical foundation that enables the method, not the main contribution itself. The phase-aware allocation is too simplistic as currently presented, and there are real risks around conditional impact and codebase integration that haven't been adequately addressed.

Looking at the scores, I'm hovering around 3.5 across the board — novelty is limited because the methodology is fairly standard, feasibility is constrained by codebase complexity, and the impact remains conditional on whether the speedups actually materialize. But stepping back, the user's requirements specifically call for cache-aware methods for reasoning models and efficient serving with variable-length thinking, which is exactly what this work targets. The interaction surface characterization itself is genuinely novel, even if the allocation method isn't — so maybe the real opportunity is to lean harder into that novelty and build a more sophisticated method on top of it rather than treating characterization as the main story.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df115b25-d5c4-4b83-8cef-9e1795e9f5df",
  "isSidechain": false,
  "requestId": "req_011CawjAW3rsVnotjS8cMC6W",
  "type": "assistant",
  "uuid": "627d6233-ac8f-43d8-928d-97fd8916c51f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3qp1AcJJ4zZx78VBCguhR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1908,
      "cache_creation_input_tokens": 3095,
      "cache_read_input_tokens": 45216,
      "output_tokens": 5858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3095,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1908,
          "output_tokens": 5858,
          "cache_read_input_tokens": 45216,
          "cache_creation_input_tokens": 3095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3095
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

_source line 31 · 2026-05-12T00:30:30.729Z_

Now let me synthesize all findings into my review assessment.

Key research findings:
1. **All major references verified** — R-Sparse (ICLR 2025), Polar Sparsity (NeurIPS 2025), ThinKV (ICLR 2026 Oral), TEAL (ICLR 2025), WAS (EMNLP 2025 Main), ActTail, WiSparse all confirmed
2. **"Sparsity interaction surface" / cross-partial derivative framework is genuinely novel** — zero results in literature for this formalization
3. **No paper characterizes joint attention+MLP sparsity interaction across reasoning phases** — the gap is real
4. **CLADA (arXiv 2502.19078) is MLP-only**, not a direct competitor
5. **RAC is NeurIPS 2025 Workshop + ICLR 2026 Main** — the proposal correctly cites it as workshop
6. **DeepSeek-R1-Distill-Llama-8B IS Llama-3.1 architecture** — good for compatibility
7. **All codebases are immature**: TEAL self-describes as "proof of concept," Polar Sparsity has 6 commits, R-Sparse has 2 commits, ActTail has no code release

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 4, "rationale": "The sparsity interaction surface formalization (cross-partial derivative d²Q/(ds_attn · ds_mlp) across reasoning phases) is genuinely novel — zero prior work measures or formalizes the joint interaction between attention-head and MLP activation sparsity. The three-regime framework (compounding/complementing/independent) provides a clean theoretical lens. However, the empirical methodology is standard (grid sweep + finite differences)."},
    "feasibility": {"score": 3, "rationale": "Within GPU (170h) and timeline (14d) constraints, and DeepSeek-R1-Distill-Llama-8B's Llama-3.1 architecture enables codebase compatibility in principle. However, ALL dependency codebases are immature — TEAL is self-described 'proof of concept,' Polar Sparsity has 6 commits, R-Sparse has 2, ActTail has no code. The scope (5×5 grid × 4 phases × 6 benchmarks × 50+ prompts + 5 baselines + ablations) is very ambitious for 14 days with these codebases."},
    "clarity": {"score": 4, "rationale": "Well-structured with clear three-contribution delineation, comprehensive baseline selection, well-motivated theoretical framework, and honest fallback structure. The proposal is thorough — perhaps overly so — but the core argument is clearly communicated."},
    "impact": {"score": 3, "rationale": "The interaction characterization addresses a real gap and provides design guidance for joint sparsity, but the practical contribution is modest: 1.3-1.7x speedup via grid search is below what dedicated methods achieve (Polar Sparsity 2.2x, Twilight 3.9x). Impact is conditional on finding non-trivial interaction effects. Most critically, the user explicitly required 'METHOD ONLY — not profiling studies,' and this idea is primarily a profiling/characterization study with a grid-search application."}
  },
  "issues": [
    "CRITICAL: User requirement mismatch — the user explicitly states 'Contribution type: METHOD ONLY. Propose new algorithms — not profiling studies.' The current proposal explicitly positions the main contribution as characterization/profiling ('empirical characterization study with three contributions') and the phase-aware allocation as 'explicitly positioned as an application of the characterization demonstrating its practical utility, not a claimed algorithmic contribution.' This directly contradicts the user's core requirement. The generator must either (a) develop a genuine algorithmic contribution that uses the interaction surface to drive a novel method, or (b) acknowledge this is a Findings-level characterization paper — but option (b) conflicts with user requirements.",
    "The phase-aware allocation 'method' is grid search over 8 parameters (4 phases × 2 sparsity dimensions) — this is engineering, not algorithmic innovation. Previous review rounds (Rounds 3-4) correctly identified this but pushed the paper toward 'characterization' framing, which inadvertently made the user-requirement mismatch worse. The method component needs genuine algorithmic depth: e.g., an online algorithm that estimates interaction gradients during inference and dynamically adjusts joint sparsity without pre-computed profiles, or a learnable interaction-aware sparsity predictor.",
    "Codebase integration risk is underacknowledged: TEAL self-describes as 'just a proof of concept' with FP16-only support. Polar Sparsity has 6 stars and 6 commits. R-Sparse has 2 commits with incomplete Triton kernels. ActTail has no open-source implementation at all. None natively support DeepSeek-R1-Distill-Llama-8B. While the model IS Llama-3.1 architecture (verified), DeepSeek modifies configs and tokenizers. The proposal should specify which codebase it will actually use and have a concrete fallback (e.g., implement magnitude-based pruning from scratch using HuggingFace hooks, which is simpler but eliminates codebase dependency risk).",
    "Conditional impact: if cross-partial derivatives are near-zero at all phases, the paper reduces to (a) confirming R-Sparse's additive assumption (negative result), (b) SwiGLU headroom characterization, and (c) transferability analysis. While the fallback structure is well-designed and honest, EMNLP Main reviewers may not consider a negative result + headroom profiling sufficient for Main conference — especially in the Efficient Methods track where algorithmic contributions are expected. The proposal should strengthen the fallback by having a method contribution that works regardless of the interaction surface shape.",
    "Missing competitor: CLADA (arXiv 2502.19078, Feb 2025) — 'Sparse Brains are Also Adaptive Brains: Cognitive-Load-Aware Dynamic Activation for LLMs' — adapts MLP activation sparsity based on token-level cognitive load (surprisal/entropy). While MLP-only and not reasoning-phase-aware, it establishes the principle of adaptive sparsity based on computational demand and should be discussed as related work.",
    "The 170h GPU estimate may be tight: 5×5 grid = 25 configurations per phase, × 4 phases = 100 configurations. Each requires running 50+ prompts across 6 benchmarks = 300+ runs per configuration. Even if each run is short (~10 seconds for a single 8B model generation), the total inference time for the grid sweep alone is substantial. Add 5 baselines × 6 benchmarks × 50 prompts each + ablations + SwiGLU headroom profiling + buffer, and 170h may require very careful scheduling. The proposal should provide a more detailed computation showing how 170h covers all experiments."
  ],
  "feedback": "The core insight — that attention and MLP sparsity interact non-trivially across reasoning phases and this interaction has not been characterized — is genuinely novel and verified. The gap is real. But to meet the user's explicit 'METHOD ONLY' requirement, the paper needs restructuring:\n\n1. **Develop a genuine algorithmic contribution**: Use the interaction surface as the foundation for a novel algorithm, not just a grid-search application. Concrete options:\n   (a) **Online Interaction-Aware Sparsity (OIAS)**: An algorithm that maintains running estimates of local interaction gradients (compounding vs. complementing) during inference by monitoring attention entropy and MLP activation statistics, and dynamically adjusts both attention-head and MLP sparsity levels within each block. Unlike grid search, this adapts in real-time without pre-computed profiles.\n   (b) **Interaction-Guided Sparsity Allocation**: Formulate joint sparsity allocation as a constrained optimization where the objective function explicitly includes an interaction penalty term derived from the cross-partial derivative. Solve this per-layer and per-phase to produce sparsity configurations that respect interaction structure. This is more principled than independent per-axis allocation (R-Sparse) or uniform joint allocation (AMP).\n   Either approach transforms the paper from 'we profiled something interesting' to 'we discovered a phenomenon and built an algorithm that exploits it.'\n\n2. **Restructure contributions**: Lead with the method (algorithm for interaction-aware joint sparsity), supported by the interaction surface characterization (which motivates and validates the method). The characterization becomes the analytical foundation, not the main claim.\n\n3. **Address codebase risk concretely**: For the characterization component, you don't need production sparse kernels — standard PyTorch masking/zeroing of attention heads and MLP activations suffices to measure quality degradation. For the speedup demonstration, specify that you'll use Polar Sparsity's existing Llama-3.1 support for attention head selection and implement simple magnitude-based MLP pruning via PyTorch hooks (TEAL's core method is just top-k magnitude thresholding, which is ~50 lines of code). Have a concrete fallback: if Polar Sparsity integration fails, use attention head masking via HuggingFace model hooks.\n\n4. **Make the method work regardless of interaction shape**: If interaction is strong (compounding/complementing), the algorithm exploits the interaction structure. If interaction is near-zero (independent), the algorithm degrades gracefully to per-axis allocation equivalent to R-Sparse — but the algorithm itself is still a contribution because it handles the general case. This eliminates the conditional impact problem.",
  "reason": "Genuine novel gap but fundamentally misaligned with user's 'METHOD ONLY' requirement — the paper is a profiling study with grid-search application, not a new algorithm."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "627d6233-ac8f-43d8-928d-97fd8916c51f",
  "isSidechain": false,
  "requestId": "req_011CawjAW3rsVnotjS8cMC6W",
  "type": "assistant",
  "uuid": "6b03e576-a9d4-4041-8217-ee67f9f9f46b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3qp1AcJJ4zZx78VBCguhR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1908,
      "cache_creation_input_tokens": 3095,
      "cache_read_input_tokens": 45216,
      "output_tokens": 5858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3095,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1908,
          "output_tokens": 5858,
          "cache_read_input_tokens": 45216,
          "cache_creation_input_tokens": 3095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3095
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "6b03e576-a9d4-4041-8217-ee67f9f9f46b",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing attention-MLP sparsity interaction in reasoning models",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "6b03e576-a9d4-4041-8217-ee67f9f9f46b",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing attention-MLP sparsity interaction in reasoning models",
  "sessionId": "c9c317b6-258b-43eb-b84c-bc4c97ee2780"
}
```

---
