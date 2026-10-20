# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/78549138-104c-475b-b6d5-c16ae158c3be.jsonl`
- **Structured JSON:** [`e405fb3ebc15e82052cc.json`](../../sessions/e4/e405fb3ebc15e82052cc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T18:15:56.070Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T18:15:56.070Z",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.\n\nDirection: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.\n\nContribution type: METHOD ONLY. Propose new algorithms — not profiling studies.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Generous for efficiency work.\n2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.\n3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.\n\nLook for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.\n\nTag: direction=efficiency, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 3/10)\n{\n  \"title\": \"Cross-Axis Redundancy Coordination: Unified Signal for Joint MLP Sparsity and KV Eviction in Reasoning Inference\",\n  \"core_problem\": \"Reasoning models generate highly redundant thinking traces, yet current efficiency methods each address a single bottleneck axis: Token Filtering (arXiv:2512.07090) uses EMA-based key-value similarity to skip attention layers but leaves MLP computation untouched; R-KV evicts redundant KV entries using costly O(B²) pairwise similarity unsuitable for per-token triggering; TEAL applies uniform MLP activation sparsity regardless of token redundancy; and FASA uses offline-calibrated frequency chunks for KV compression without modulating MLP compute. No existing method uses a per-token redundancy signal to simultaneously coordinate savings across both compute-bound (MLP) and memory-bound (KV cache) bottlenecks — each method optimizes its own axis independently, leaving complementary gains unrealized.\",\n  \"opportunity\": \"Token Filtering demonstrated that EMA centroid similarity of key-value vectors reliably identifies redundant tokens at O(1) per-token cost for attention layer skipping. However, this signal's potential to drive efficiency across MULTIPLE orthogonal axes simultaneously remains unexplored. We observe that extending this signal to coordinate both (1) elevated MLP activation sparsity via TEAL's existing kernel and (2) KV cache eviction achieves complementary wall-clock savings on independent bottlenecks — compute-bound MLP forward passes and memory-bound attention over cached keys — without any training, calibration, or kernel modification. The key insight is architectural: during reasoning generation (primarily batch=1), MLP processing and KV attention are independently rate-limiting at different stages, so reducing both with a single trigger yields additive speedups that no single-axis method can match.\",\n  \"landscape\": \"Token Filtering (arXiv:2512.07090, Dec 2025) introduces an EMA anchor for key-value vectors (Anchor ← γ·Anchor + (1−γ)·k_current) with variance-aware fusion (Eq. 2-3) to skip attention layers during inference — the signal that we build upon, extending it to MLP sparsity and KV eviction. R-KV (NeurIPS 2025) achieves 90% KV memory savings using O(B²) pairwise key similarity for periodic eviction — proving redundancy-aware KV eviction works but with a signal too expensive for per-token use. TEAL (ICLR 2025 Spotlight) achieves 40–50% training-free MLP activation sparsity with 1.5–1.8× decoding speedup via magnitude pruning, but applies uniform per-layer thresholds regardless of token content. KeyDiff (arXiv:2504.15364) uses mean-of-keys (not EMA) as an anchor for KV eviction, prioritizing geometrically distinctive keys — a related anchor approach but without recency bias and limited to the KV axis. FASA (ICLR 2026) discovers RoPE-induced frequency-chunk functional sparsity for 8× KV compression, requiring one-time offline calibration and not modulating MLP compute. ThinKV (ICLR 2026 Oral) decomposes reasoning chains into thought types for hybrid quantization-eviction using offline KDE calibration on attention sparsity distributions (not a learned classifier). Polar Sparsity (NeurIPS 2025) shows that MLP neuron-level sparsity vanishes at larger batch sizes (union of active neurons approaches dense), but attention head sparsity remains batch-invariant — confirming MLP sparsity gains are primarily valuable at batch=1/small-batch. EvoSparse (ACL 2026) leverages cross-step token importance accumulation for dynamic sparse attention, but addresses only the attention axis. CSAttention (arXiv:2604.08584) constructs query-centric lookup tables during offline prefill for 95% attention sparsity, demonstrating that key-only metrics can miss query-dependent importance — a limitation we acknowledge. 'EMA Is Not All You Need' (arXiv:2604.08556, Apr 2026) shows EMA traces suffer irreversible information dilution when used as context representations, motivating our windowed-reset mechanism for maintaining signal discriminability over long reasoning chains. QuickSilver (2025) combines token halting, KV skipping, and token fusion using hidden-state L2 drift — a multi-mechanism approach where each mechanism uses a different signal. SeerAttention-R (ICLR 2026) learns sparse attention gates requiring 0.4B tokens of post-training. No existing work demonstrates a training-free, calibration-free coordination of MLP sparsity and KV cache eviction from a single per-token redundancy signal.\",\n  \"approach\": \"We propose Cross-Axis Redundancy Coordination (CARC), a training-free inference method that extends Token Filtering's EMA-based redundancy signal to simultaneously orchestrate MLP activation sparsity and KV cache eviction — a cross-axis coordination that no prior work achieves.\\n\\n**1. Enhanced redundancy signal (extending Token Filtering).** We adopt Token Filtering's EMA centroid with variance-aware key+value fusion as the base signal: Anchor_k ← γ·Anchor_k + (1−γ)·k_new; Anchor_v ← γ·Anchor_v + (1−γ)·v_new; with adaptive weighting α = σ_v^(-2)/(σ_k^(-2) + σ_v^(-2)) and final score S = α·cos(k_new, Anchor_k) + (1−α)·cos(v_new, Anchor_v). Our enhancement: a **windowed reset mechanism** to address EMA information dilution over long reasoning chains (per 'EMA Is Not All You Need'). When S drops below a reset threshold τ_reset (indicating a topic/reasoning-phase shift), the EMA is reinitialized from a short sliding window (last W=16 tokens), preventing the centroid from becoming an indiscriminate 'smeared summary.' This gives the signal locality awareness that pure EMA lacks. Storage: <1MB for a 14B model. Compute overhead: <0.001% FLOPs.\\n\\n**2. Two-tier MLP sparsity.** When S > τ (token classified as redundant), we apply TEAL's magnitude-pruning kernel with an elevated threshold (50–55% sparsity) versus TEAL's default 40% for novel tokens. This stays safely below the documented 65% performance cliff on SwiGLU architectures while providing meaningful differentiation. Implementation: tokens are batched into redundant/novel groups and routed to the appropriate threshold — a control-flow change requiring no kernel modification.\\n\\n**3. Redundancy-aware KV eviction.** Tokens classified as redundant are evicted from the KV cache following R-KV's management strategy, triggered by our O(1) signal rather than R-KV's periodic O(B²) scoring. Unlike KeyDiff's global mean anchor, our EMA provides recency bias that better captures local redundancy patterns in reasoning chains.\\n\\n**Complementary (additive) savings.** MLP sparsity reduces compute-bound processing during each redundant token's forward pass; KV eviction reduces memory footprint and attention FLOPs for all subsequent tokens. These target independent bottlenecks and compose additively in wall-clock time.\\n\\n**Batch-size scope.** We explicitly frame CARC as targeting batch=1 or small-batch reasoning generation, the dominant use case for reasoning models. Per Polar Sparsity, MLP neuron-level sparsity gains diminish at larger batch sizes (union of active neurons approaches dense). At batch=1, both axes provide full savings.\\n\\n**Limitations acknowledged.** (1) Key+value similarity is an incomplete redundancy proxy — query-dependent importance (per CSAttention) is not captured. We include an oracle ablation measuring the gap. (2) MLP sparsity gains diminish at batch>4. (3) The EMA windowed-reset adds a hyperparameter (W, τ_reset) requiring tuning.\\n\\nWe sweep γ ∈ {0.85, 0.9, 0.95}, τ ∈ {0.88, 0.91, 0.94}, reset window W ∈ {8, 16, 32}, and τ_reset ∈ {0.6, 0.7, 0.8}. We evaluate on DeepSeek-R1-Distill-Qwen-14B/32B and Qwen3-8B across primary benchmarks (perplexity on WikiText-2 and C4, MMLU, LongBench, RULER, MT-Bench) and supplementary reasoning benchmarks (AIME 2024, MATH-500, GPQA Diamond, HumanEval), measuring end-to-end latency, peak GPU memory, and accuracy against single-axis baselines (TEAL-only, R-KV-only, Token Filtering-only, FASA) and ablations (with/without windowed reset, two-tier vs uniform sparsity, with/without KV eviction, EMA vs sliding-window-mean, with/without value fusion).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~100h H100 80GB\",\n      \"gpu_utilization\": \"Low (~25%): GPUs idle while researcher integrates Token Filtering signal with TEAL threshold routing and R-KV eviction code\",\n      \"timeline\": \"14–16 days (targets EMNLP 2026 ARR deadline May 25, 2026)\",\n      \"team\": \"1–2 researchers (systems ML background; implementation leverages existing codebases for Token Filtering, TEAL, and R-KV)\",\n      \"estimated_gpu_cost\": \"$200–300 (100h × $2.00–3.00/hr on-demand H100 80GB)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~150h H100 80GB\",\n      \"gpu_utilization\": \"Moderate (~55%): agent runs τ/γ/W sweeps and benchmark evaluations autonomously, waits for human on reset mechanism design and sparsity level selection\",\n      \"timeline\": \"10–12 days\",\n      \"team\": \"1 researcher, ~45 min/day reviewing agent proposals and experiment results\",\n      \"claude_api_cost\": \"$120–250 (1200–2500 turns for implementation, experiment design, analysis, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$300–450 (150h × $2.00–3.00/hr)\",\n      \"risk_note\": \"Tight EMNLP deadline (May 25) means limited time for extensive ablations; may need to scope down to 2 models (14B, 8B) instead of 3. Token routing between two TEAL threshold levels requires careful integration with R-KV's eviction logic — ordering dependencies possible.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~250h H100 80GB (γ×τ×W grid across 3×3×3=27 configurations + reset threshold sweep + cross-model evaluation)\",\n      \"gpu_utilization\": \"High (~90%): agent pipelines experiments back-to-back with zero human wait time\",\n      \"timeline\": \"7–10 days with 4× H100 80GB; 4–5 days with 8× H100\",\n      \"team\": \"0 (initial setup ~2 hours for codebase access and GPU provisioning)\",\n      \"claude_api_cost\": \"$250–400 (2500–4000 turns for autonomous implementation, debugging, experiment orchestration, and paper writing)\",\n      \"estimated_gpu_cost\": \"$500–750 (250h × $2.00–3.00/hr)\",\n      \"speed_bottleneck\": \"Sequential dependency: windowed-reset hyperparameters must be validated before full benchmark evaluation. EMNLP deadline pressure means agent must prioritize core results over exhaustive ablations.\",\n      \"risk_note\": \"Integration complexity between three existing codebases (Token Filtering, TEAL, R-KV) may surface unexpected incompatibilities. Agent may over-explore reset mechanism variants given tight deadline.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026 — primary target, 15 days)\",\n    \"AAAI 2027 (expected abstract late Jul 2026 — fallback with extended ablations)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Token Filtering: Leveraging KV Similarity for Online Structured Pruning in LLMs (arXiv:2512.07090, Dec 2025)\",\n    \"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models (NeurIPS 2025)\",\n    \"TEAL: Training-Free Activation Sparsity in Large Language Models (ICLR 2025 Spotlight)\",\n    \"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference (arXiv:2504.15364)\",\n    \"FASA: Frequency-Aware Sparse Attention (ICLR 2026)\",\n    \"EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context (arXiv:2604.08556, Apr 2026)\",\n    \"CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference (arXiv:2604.08584, Apr 2026)\",\n    \"EvoSparse: Evolving Sparsity — Leveraging Token Importance Dynamics for Efficient LLM Decoding (ACL 2026)\",\n    \"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral)\",\n    \"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity (NeurIPS 2025)\",\n    \"SeerAttention-R: Sparse Attention Adaptation for Long Reasoning (ICLR 2026)\",\n    \"QuickSilver: Speeding up LLM Inference through Dynamic Token Halting and KV Skipping (arXiv 2025)\"\n  ],\n  \"description\": \"We propose Cross-Axis Redundancy Coordination (CARC), a training-free inference method that extends Token Filtering's EMA-based key-value similarity signal (arXiv:2512.07090) to simultaneously drive MLP activation sparsity and KV cache eviction — a cross-axis coordination that no prior work achieves. Token Filtering uses this signal only for attention layer skipping (FFN untouched, no KV eviction); CARC demonstrates that the same signal can orchestrate complementary savings on two additional independent bottlenecks. Our contributions: (1) We enhance the EMA signal with a windowed-reset mechanism to address information dilution over long reasoning chains (motivated by 'EMA Is Not All You Need,' arXiv:2604.08556), reinitializing the centroid from a sliding window upon detecting reasoning-phase shifts. (2) We route tokens classified as redundant (S > τ) to TEAL's existing magnitude-pruning kernel with an elevated 50–55% sparsity threshold (vs. 40% default), staying below the documented 65% SwiGLU cliff — no kernel modification required. (3) We trigger KV cache eviction for redundant tokens using R-KV's management strategy, replacing its O(B²) periodic scoring with our O(1) per-token signal. Unlike KeyDiff's global mean anchor, our EMA provides recency bias for local redundancy patterns. These two axes target independent bottlenecks (compute-bound MLP, memory-bound KV attention) and compose additively in wall-clock time. We explicitly scope to batch=1/small-batch reasoning generation (per Polar Sparsity's finding that MLP sparsity vanishes under batching) and acknowledge key+value similarity as an incomplete proxy for query-dependent importance (per CSAttention). We evaluate on DeepSeek-R1-Distill-Qwen-14B/32B and Qwen3-8B across primary benchmarks (WikiText-2/C4 perplexity, MMLU, LongBench, RULER, MT-Bench) and reasoning benchmarks (AIME 2024, MATH-500, GPQA Diamond, HumanEval), comparing against Token Filtering, TEAL-only, R-KV-only, and FASA. The contribution is a systems coordination insight: a known redundancy signal, enhanced with stability mechanisms, can orchestrate savings across orthogonal efficiency axes that prior work optimizes independently. We target EMNLP 2026 ARR (May 25) as primary venue.\",\n  \"project_name\": \"redundancy_compound_sparsity\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"R-KV's redundancy detection is O(B_budget²) pairwise similarity, NOT 'a single dot product per token at near-zero cost' — this mischaracterization undermines the entire efficiency argument of the triggering signal\", \"Polar Sparsity uses batch-invariant head selection — per-token head pruning contradicts its core design and breaks its batched computation model. You cannot skip different heads for different tokens in the same batch\", \"TEAL's CUDA kernel uses fixed per-layer thresholds; adaptive per-token sparsity (40-50% vs 60-70%) requires non-trivial kernel modification not acknowledged in the timeline\", \"Evaluation benchmarks (AIME, MATH-500, GPQA Diamond) do not match user-required benchmarks (perplexity Wiki/C4, MMLU, LongBench, RULER, MT-Bench). Only HumanEval overlaps\", \"Resource estimates specified in A100 hours, not H100 hours as user requires\", \"The 'compound' savings claim assumes multiplicative gains, but tokens that are KV-evicted don't participate in future attention regardless — so MLP sparsity on evicted tokens only saves the current forward pass, limiting compound benefits\", \"15-day timeline to integrate three separate CUDA codebases (R-KV, TEAL, Polar Sparsity), resolve incompatible memory layouts, run full benchmarks, AND write a paper is highly unrealistic\", \"FASA (ICLR 2026) already demonstrates using a single cheap signal (RoPE functional sparsity) for token importance-driven compression with 2.56× speedup — similar single-signal philosophy applied to KV cache\"]\nFeedback: The core concept of using redundancy detection to modulate compute across multiple axes has merit, but the proposal has critical technical errors that must be fixed:\n\n1. **Fix the triggering mechanism**: Don't claim R-KV's signal is 'a single dot product.' Instead, propose a simplified incremental version: compare each new token's key against the mean or centroid of the last W tokens (truly O(1) per token). This would be your novel contribution — a lightweight proxy for redundancy.\n\n2. **Replace Polar Sparsity with per-token head pruning**: Since Polar Sparsity is batch-invariant, either (a) propose your own per-token head importance criterion (e.g., correlation between key similarity and head attention entropy), or (b) drop to two axes (MLP + KV eviction) which are both genuinely per-token compatible.\n\n3. **Acknowledge CUDA kernel work**: The per-token TEAL threshold requires a modified kernel. Budget 2-3 days for this or propose a simpler two-tier approach (batch tokens into 'redundant' and 'novel' groups, apply different fixed thresholds to each group).\n\n4. **Match user-required evaluation**: Add perplexity (WikiText-2, C4), MMLU, LongBench, RULER, and MT-Bench. Keep AIME/MATH-500 as supplementary reasoning-specific metrics.\n\n5. **Convert resource estimates to H100-hours**: 200 H100-hours ≈ 300 A100-hours, so the manual estimate fits. Report in H100.\n\n6. **Consider targeting AAAI 2027 (Aug deadline) instead of EMNLP May 25**: The integration complexity of three systems with kernel modifications is not achievable in 15 days. AAAI gives 11 more weeks.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL NOVELTY FLAW: Token Filtering (Lee et al., Dec 2025, arXiv:2512.07090) uses the EXACT same EMA centroid signal — Anchor ← γ·Anchor + (1−γ)·k_current with per-head cosine similarity aggregated across heads. The paper's claimed 'novel contribution' (#1) is therefore NOT novel. Token Filtering applies this signal to attention layer skipping; extending it to MLP sparsity and KV eviction is incremental, not a new signal.\", \"VENUE MISMATCH: User explicitly required 'Target: EMNLP 2026, ARR submission deadline 2026-05-25.' The idea targets AAAI 2027 and ICLR 2027 instead. While round 1 suggested this retargeting, the user's requirement has not changed. The simplified two-axis approach (no kernel mods) may actually be feasible in 16 days for EMNLP 2026.\", \"EMA STABILITY CONCERN: 'EMA Is Not All You Need' (arXiv:2604.08556, Apr 2026) shows EMA traces destroy token identity and suffer irreversible information dilution — after ~50 steps with decay 0.98, the centroid becomes a 'smeared summary' losing discriminative power. For reasoning traces spanning 1000+ tokens, the EMA centroid may become indistinguishable from a static average, making the redundancy signal unreliable for long chains.\", \"TEAL 65% SPARSITY CLIFF: Anti-evidence shows that at 65% MLP sparsity, most models (especially newer SwiGLU architectures like Qwen3 and DeepSeek-R1-Distill) degrade significantly. The proposed 60-65% threshold for 'redundant' tokens is right at this documented performance cliff. The safety margin between 'works' (40-50%) and 'breaks' (65%+) is dangerously thin.\", \"ThinKV MISCHARACTERIZATION: The landscape states ThinKV 'requires a learned phase classifier' — this is INCORRECT. ThinKV uses kernel density estimation (KDE) on attention sparsity distributions to compute thresholds, a heuristic approach, not a learned classifier. This weakens the positioning against ThinKV.\", \"KEY-ONLY SIMILARITY IS AN INCOMPLETE REDUNDANCY PROXY: Two tokens may have very similar key vectors but be attended to very differently by queries at different positions. Research on query-key distribution shift (CSAttention, FASA) shows that key-only metrics miss query-dependent importance. The generator should acknowledge this limitation or incorporate value similarity (as Token Filtering does).\", \"MLP SPARSITY VANISHES UNDER BATCHING: Polar Sparsity (NeurIPS 2025) shows that MLP neuron-level sparsity disappears at larger batch sizes (union of active neurons approaches dense). The proposed two-tier MLP sparsity would show diminishing returns under batched serving — a critical limitation for the 'efficient serving' framing.\", \"MISSING CRITICAL REFERENCES: Token Filtering (arXiv:2512.07090), KeyDiff (arXiv:2504.15364), EvoSparse (ACL 2026), CSAttention (arXiv:2604.08584), and 'EMA Is Not All You Need' (arXiv:2604.08556) are all directly relevant but uncited.\"]\nFeedback: The proposal has improved significantly from round 1 — dropping Polar Sparsity from core, using two-tier TEAL thresholds without kernel mods, and matching user-required benchmarks are all correct fixes. However, a critical novelty problem has emerged:\n\n1. **Cite Token Filtering and reframe the contribution**: Token Filtering (arXiv:2512.07090) already proposes the EMA centroid signal for per-token redundancy detection. You MUST cite this paper and reframe your contribution from 'novel signal' to 'novel DUAL APPLICATION of a known signal.' Specifically: Token Filtering uses EMA similarity only for attention layer skipping, while RTDS extends it to simultaneously drive MLP sparsity (via TEAL) AND KV cache eviction — a cross-axis coordination that no prior work achieves. Also consider incorporating Token Filtering's variance-aware key+value fusion (Eq. 2-3) to improve signal quality, which would be a genuine enhancement.\n\n2. **Address EMA stability for long sequences**: The 'EMA Is Not All You Need' paper directly challenges your core mechanism. Mitigate by: (a) using a shorter decay window (α=0.1-0.2 instead of 0.01-0.05) to prevent information dilution, (b) adding a 'reset' mechanism when the similarity drops sharply (indicating a topic shift in reasoning), or (c) using a sliding window mean instead of EMA for better locality. Include an ablation comparing EMA vs. sliding window vs. Token Filtering's variant.\n\n3. **Lower the redundant-token sparsity from 60-65% to 50-55%**: This provides a safer margin above TEAL's validated 40-50% range while still providing meaningful differentiation between tiers. The 65% cliff is well-documented and will likely cause accuracy degradation on Qwen3/DeepSeek models with SwiGLU.\n\n4. **Reconsider EMNLP 2026**: With the simplified approach (no kernel mods, ~130h H100, two clean axes), the 16-day timeline IS tight but possibly feasible, especially since you have available code for both R-KV and TEAL. If you keep AAAI 2027, you should also consider EMNLP 2026 as a stretch target — the approach is simple enough that a focused implementation sprint could work. The user explicitly requested EMNLP 2026.\n\n5. **Fix ThinKV characterization**: Replace 'requires a learned phase classifier' with 'requires offline KDE calibration on attention sparsity distributions.'\n\n6. **Add KeyDiff citation and differentiation**: KeyDiff uses mean-of-keys (not EMA) for KV eviction. Cite it and explain why EMA is preferable (recency bias captures local redundancy patterns better than global mean).\n\n7. **Acknowledge the batching limitation**: State explicitly that MLP sparsity gains diminish at larger batch sizes (per Polar Sparsity) and that RTDS is primarily targeted at batch=1 or small-batch reasoning generation, which is the dominant use case for reasoning models.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T18:15:56.074Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T18:15:56.074Z",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-10T18:15:56.098Z_

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

## Idea under review (round 3/10)
{
  "title": "Cross-Axis Redundancy Coordination: Unified Signal for Joint MLP Sparsity and KV Eviction in Reasoning Inference",
  "core_problem": "Reasoning models generate highly redundant thinking traces, yet current efficiency methods each address a single bottleneck axis: Token Filtering (arXiv:2512.07090) uses EMA-based key-value similarity to skip attention layers but leaves MLP computation untouched; R-KV evicts redundant KV entries using costly O(B²) pairwise similarity unsuitable for per-token triggering; TEAL applies uniform MLP activation sparsity regardless of token redundancy; and FASA uses offline-calibrated frequency chunks for KV compression without modulating MLP compute. No existing method uses a per-token redundancy signal to simultaneously coordinate savings across both compute-bound (MLP) and memory-bound (KV cache) bottlenecks — each method optimizes its own axis independently, leaving complementary gains unrealized.",
  "opportunity": "Token Filtering demonstrated that EMA centroid similarity of key-value vectors reliably identifies redundant tokens at O(1) per-token cost for attention layer skipping. However, this signal's potential to drive efficiency across MULTIPLE orthogonal axes simultaneously remains unexplored. We observe that extending this signal to coordinate both (1) elevated MLP activation sparsity via TEAL's existing kernel and (2) KV cache eviction achieves complementary wall-clock savings on independent bottlenecks — compute-bound MLP forward passes and memory-bound attention over cached keys — without any training, calibration, or kernel modification. The key insight is architectural: during reasoning generation (primarily batch=1), MLP processing and KV attention are independently rate-limiting at different stages, so reducing both with a single trigger yields additive speedups that no single-axis method can match.",
  "landscape": "Token Filtering (arXiv:2512.07090, Dec 2025) introduces an EMA anchor for key-value vectors (Anchor ← γ·Anchor + (1−γ)·k_current) with variance-aware fusion (Eq. 2-3) to skip attention layers during inference — the signal that we build upon, extending it to MLP sparsity and KV eviction. R-KV (NeurIPS 2025) achieves 90% KV memory savings using O(B²) pairwise key similarity for periodic eviction — proving redundancy-aware KV eviction works but with a signal too expensive for per-token use. TEAL (ICLR 2025 Spotlight) achieves 40–50% training-free MLP activation sparsity with 1.5–1.8× decoding speedup via magnitude pruning, but applies uniform per-layer thresholds regardless of token content. KeyDiff (arXiv:2504.15364) uses mean-of-keys (not EMA) as an anchor for KV eviction, prioritizing geometrically distinctive keys — a related anchor approach but without recency bias and limited to the KV axis. FASA (ICLR 2026) discovers RoPE-induced frequency-chunk functional sparsity for 8× KV compression, requiring one-time offline calibration and not modulating MLP compute. ThinKV (ICLR 2026 Oral) decomposes reasoning chains into thought types for hybrid quantization-eviction using offline KDE calibration on attention sparsity distributions (not a learned classifier). Polar Sparsity (NeurIPS 2025) shows that MLP neuron-level sparsity vanishes at larger batch sizes (union of active neurons approaches dense), but attention head sparsity remains batch-invariant — confirming MLP sparsity gains are primarily valuable at batch=1/small-batch. EvoSparse (ACL 2026) leverages cross-step token importance accumulation for dynamic sparse attention, but addresses only the attention axis. CSAttention (arXiv:2604.08584) constructs query-centric lookup tables during offline prefill for 95% attention sparsity, demonstrating that key-only metrics can miss query-dependent importance — a limitation we acknowledge. 'EMA Is Not All You Need' (arXiv:2604.08556, Apr 2026) shows EMA traces suffer irreversible information dilution when used as context representations, motivating our windowed-reset mechanism for maintaining signal discriminability over long reasoning chains. QuickSilver (2025) combines token halting, KV skipping, and token fusion using hidden-state L2 drift — a multi-mechanism approach where each mechanism uses a different signal. SeerAttention-R (ICLR 2026) learns sparse attention gates requiring 0.4B tokens of post-training. No existing work demonstrates a training-free, calibration-free coordination of MLP sparsity and KV cache eviction from a single per-token redundancy signal.",
  "approach": "We propose Cross-Axis Redundancy Coordination (CARC), a training-free inference method that extends Token Filtering's EMA-based redundancy signal to simultaneously orchestrate MLP activation sparsity and KV cache eviction — a cross-axis coordination that no prior work achieves.\n\n**1. Enhanced redundancy signal (extending Token Filtering).** We adopt Token Filtering's EMA centroid with variance-aware key+value fusion as the base signal: Anchor_k ← γ·Anchor_k + (1−γ)·k_new; Anchor_v ← γ·Anchor_v + (1−γ)·v_new; with adaptive weighting α = σ_v^(-2)/(σ_k^(-2) + σ_v^(-2)) and final score S = α·cos(k_new, Anchor_k) + (1−α)·cos(v_new, Anchor_v). Our enhancement: a **windowed reset mechanism** to address EMA information dilution over long reasoning chains (per 'EMA Is Not All You Need'). When S drops below a reset threshold τ_reset (indicating a topic/reasoning-phase shift), the EMA is reinitialized from a short sliding window (last W=16 tokens), preventing the centroid from becoming an indiscriminate 'smeared summary.' This gives the signal locality awareness that pure EMA lacks. Storage: <1MB for a 14B model. Compute overhead: <0.001% FLOPs.\n\n**2. Two-tier MLP sparsity.** When S > τ (token classified as redundant), we apply TEAL's magnitude-pruning kernel with an elevated threshold (50–55% sparsity) versus TEAL's default 40% for novel tokens. This stays safely below the documented 65% performance cliff on SwiGLU architectures while providing meaningful differentiation. Implementation: tokens are batched into redundant/novel groups and routed to the appropriate threshold — a control-flow change requiring no kernel modification.\n\n**3. Redundancy-aware KV eviction.** Tokens classified as redundant are evicted from the KV cache following R-KV's management strategy, triggered by our O(1) signal rather than R-KV's periodic O(B²) scoring. Unlike KeyDiff's global mean anchor, our EMA provides recency bias that better captures local redundancy patterns in reasoning chains.\n\n**Complementary (additive) savings.** MLP sparsity reduces compute-bound processing during each redundant token's forward pass; KV eviction reduces memory footprint and attention FLOPs for all subsequent tokens. These target independent bottlenecks and compose additively in wall-clock time.\n\n**Batch-size scope.** We explicitly frame CARC as targeting batch=1 or small-batch reasoning generation, the dominant use case for reasoning models. Per Polar Sparsity, MLP neuron-level sparsity gains diminish at larger batch sizes (union of active neurons approaches dense). At batch=1, both axes provide full savings.\n\n**Limitations acknowledged.** (1) Key+value similarity is an incomplete redundancy proxy — query-dependent importance (per CSAttention) is not captured. We include an oracle ablation measuring the gap. (2) MLP sparsity gains diminish at batch>4. (3) The EMA windowed-reset adds a hyperparameter (W, τ_reset) requiring tuning.\n\nWe sweep γ ∈ {0.85, 0.9, 0.95}, τ ∈ {0.88, 0.91, 0.94}, reset window W ∈ {8, 16, 32}, and τ_reset ∈ {0.6, 0.7, 0.8}. We evaluate on DeepSeek-R1-Distill-Qwen-14B/32B and Qwen3-8B across primary benchmarks (perplexity on WikiText-2 and C4, MMLU, LongBench, RULER, MT-Bench) and supplementary reasoning benchmarks (AIME 2024, MATH-500, GPQA Diamond, HumanEval), measuring end-to-end latency, peak GPU memory, and accuracy against single-axis baselines (TEAL-only, R-KV-only, Token Filtering-only, FASA) and ablations (with/without windowed reset, two-tier vs uniform sparsity, with/without KV eviction, EMA vs sliding-window-mean, with/without value fusion).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~100h H100 80GB",
      "gpu_utilization": "Low (~25%): GPUs idle while researcher integrates Token Filtering signal with TEAL threshold routing and R-KV eviction code",
      "timeline": "14–16 days (targets EMNLP 2026 ARR deadline May 25, 2026)",
      "team": "1–2 researchers (systems ML background; implementation leverages existing codebases for Token Filtering, TEAL, and R-KV)",
      "estimated_gpu_cost": "$200–300 (100h × $2.00–3.00/hr on-demand H100 80GB)"
    },
    "human_in_loop": {
      "gpu_hours": "~150h H100 80GB",
      "gpu_utilization": "Moderate (~55%): agent runs τ/γ/W sweeps and benchmark evaluations autonomously, waits for human on reset mechanism design and sparsity level selection",
      "timeline": "10–12 days",
      "team": "1 researcher, ~45 min/day reviewing agent proposals and experiment results",
      "claude_api_cost": "$120–250 (1200–2500 turns for implementation, experiment design, analysis, and paper drafting)",
      "estimated_gpu_cost": "$300–450 (150h × $2.00–3.00/hr)",
      "risk_note": "Tight EMNLP deadline (May 25) means limited time for extensive ablations; may need to scope down to 2 models (14B, 8B) instead of 3. Token routing between two TEAL threshold levels requires careful integration with R-KV's eviction logic — ordering dependencies possible."
    },
    "auto_research": {
      "gpu_hours": "~250h H100 80GB (γ×τ×W grid across 3×3×3=27 configurations + reset threshold sweep + cross-model evaluation)",
      "gpu_utilization": "High (~90%): agent pipelines experiments back-to-back with zero human wait time",
      "timeline": "7–10 days with 4× H100 80GB; 4–5 days with 8× H100",
      "team": "0 (initial setup ~2 hours for codebase access and GPU provisioning)",
      "claude_api_cost": "$250–400 (2500–4000 turns for autonomous implementation, debugging, experiment orchestration, and paper writing)",
      "estimated_gpu_cost": "$500–750 (250h × $2.00–3.00/hr)",
      "speed_bottleneck": "Sequential dependency: windowed-reset hyperparameters must be validated before full benchmark evaluation. EMNLP deadline pressure means agent must prioritize core results over exhaustive ablations.",
      "risk_note": "Integration complexity between three existing codebases (Token Filtering, TEAL, R-KV) may surface unexpected incompatibilities. Agent may over-explore reset mechanism variants given tight deadline."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026 — primary target, 15 days)",
    "AAAI 2027 (expected abstract late Jul 2026 — fallback with extended ablations)"
  ],
  "level": "solid",
  "key_references": [
    "Token Filtering: Leveraging KV Similarity for Online Structured Pruning in LLMs (arXiv:2512.07090, Dec 2025)",
    "R-KV: Redundancy-aware KV Cache Compression for Reasoning Models (NeurIPS 2025)",
    "TEAL: Training-Free Activation Sparsity in Large Language Models (ICLR 2025 Spotlight)",
    "KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference (arXiv:2504.15364)",
    "FASA: Frequency-Aware Sparse Attention (ICLR 2026)",
    "EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context (arXiv:2604.08556, Apr 2026)",
    "CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference (arXiv:2604.08584, Apr 2026)",
    "EvoSparse: Evolving Sparsity — Leveraging Token Importance Dynamics for Efficient LLM Decoding (ACL 2026)",
    "ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral)",
    "Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity (NeurIPS 2025)",
    "SeerAttention-R: Sparse Attention Adaptation for Long Reasoning (ICLR 2026)",
    "QuickSilver: Speeding up LLM Inference through Dynamic Token Halting and KV Skipping (arXiv 2025)"
  ],
  "description": "We propose Cross-Axis Redundancy Coordination (CARC), a training-free inference method that extends Token Filtering's EMA-based key-value similarity signal (arXiv:2512.07090) to simultaneously drive MLP activation sparsity and KV cache eviction — a cross-axis coordination that no prior work achieves. Token Filtering uses this signal only for attention layer skipping (FFN untouched, no KV eviction); CARC demonstrates that the same signal can orchestrate complementary savings on two additional independent bottlenecks. Our contributions: (1) We enhance the EMA signal with a windowed-reset mechanism to address information dilution over long reasoning chains (motivated by 'EMA Is Not All You Need,' arXiv:2604.08556), reinitializing the centroid from a sliding window upon detecting reasoning-phase shifts. (2) We route tokens classified as redundant (S > τ) to TEAL's existing magnitude-pruning kernel with an elevated 50–55% sparsity threshold (vs. 40% default), staying below the documented 65% SwiGLU cliff — no kernel modification required. (3) We trigger KV cache eviction for redundant tokens using R-KV's management strategy, replacing its O(B²) periodic scoring with our O(1) per-token signal. Unlike KeyDiff's global mean anchor, our EMA provides recency bias for local redundancy patterns. These two axes target independent bottlenecks (compute-bound MLP, memory-bound KV attention) and compose additively in wall-clock time. We explicitly scope to batch=1/small-batch reasoning generation (per Polar Sparsity's finding that MLP sparsity vanishes under batching) and acknowledge key+value similarity as an incomplete proxy for query-dependent importance (per CSAttention). We evaluate on DeepSeek-R1-Distill-Qwen-14B/32B and Qwen3-8B across primary benchmarks (WikiText-2/C4 perplexity, MMLU, LongBench, RULER, MT-Bench) and reasoning benchmarks (AIME 2024, MATH-500, GPQA Diamond, HumanEval), comparing against Token Filtering, TEAL-only, R-KV-only, and FASA. The contribution is a systems coordination insight: a known redundancy signal, enhanced with stability mechanisms, can orchestrate savings across orthogonal efficiency axes that prior work optimizes independently. We target EMNLP 2026 ARR (May 25) as primary venue.",
  "project_name": "redundancy_compound_sparsity",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["R-KV's redundancy detection is O(B_budget²) pairwise similarity, NOT 'a single dot product per token at near-zero cost' — this mischaracterization undermines the entire efficiency argument of the triggering signal", "Polar Sparsity uses batch-invariant head selection — per-token head pruning contradicts its core design and breaks its batched computation model. You cannot skip different heads for different tokens in the same batch", "TEAL's CUDA kernel uses fixed per-layer thresholds; adaptive per-token sparsity (40-50% vs 60-70%) requires non-trivial kernel modification not acknowledged in the timeline", "Evaluation benchmarks (AIME, MATH-500, GPQA Diamond) do not match user-required benchmarks (perplexity Wiki/C4, MMLU, LongBench, RULER, MT-Bench). Only HumanEval overlaps", "Resource estimates specified in A100 hours, not H100 hours as user requires", "The 'compound' savings claim assumes multiplicative gains, but tokens that are KV-evicted don't participate in future attention regardless — so MLP sparsity on evicted tokens only saves the current forward pass, limiting compound benefits", "15-day timeline to integrate three separate CUDA codebases (R-KV, TEAL, Polar Sparsity), resolve incompatible memory layouts, run full benchmarks, AND write a paper is highly unrealistic", "FASA (ICLR 2026) already demonstrates using a single cheap signal (RoPE functional sparsity) for token importance-driven compression with 2.56× speedup — similar single-signal philosophy applied to KV cache"]
Feedback: The core concept of using redundancy detection to modulate compute across multiple axes has merit, but the proposal has critical technical errors that must be fixed:

1. **Fix the triggering mechanism**: Don't claim R-KV's signal is 'a single dot product.' Instead, propose a simplified incremental version: compare each new token's key against the mean or centroid of the last W tokens (truly O(1) per token). This would be your novel contribution — a lightweight proxy for redundancy.

2. **Replace Polar Sparsity with per-token head pruning**: Since Polar Sparsity is batch-invariant, either (a) propose your own per-token head importance criterion (e.g., correlation between key similarity and head attention entropy), or (b) drop to two axes (MLP + KV eviction) which are both genuinely per-token compatible.

3. **Acknowledge CUDA kernel work**: The per-token TEAL threshold requires a modified kernel. Budget 2-3 days for this or propose a simpler two-tier approach (batch tokens into 'redundant' and 'novel' groups, apply different fixed thresholds to each group).

4. **Match user-required evaluation**: Add perplexity (WikiText-2, C4), MMLU, LongBench, RULER, and MT-Bench. Keep AIME/MATH-500 as supplementary reasoning-specific metrics.

5. **Convert resource estimates to H100-hours**: 200 H100-hours ≈ 300 A100-hours, so the manual estimate fits. Report in H100.

6. **Consider targeting AAAI 2027 (Aug deadline) instead of EMNLP May 25**: The integration complexity of three systems with kernel modifications is not achievable in 15 days. AAAI gives 11 more weeks.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL NOVELTY FLAW: Token Filtering (Lee et al., Dec 2025, arXiv:2512.07090) uses the EXACT same EMA centroid signal — Anchor ← γ·Anchor + (1−γ)·k_current with per-head cosine similarity aggregated across heads. The paper's claimed 'novel contribution' (#1) is therefore NOT novel. Token Filtering applies this signal to attention layer skipping; extending it to MLP sparsity and KV eviction is incremental, not a new signal.", "VENUE MISMATCH: User explicitly required 'Target: EMNLP 2026, ARR submission deadline 2026-05-25.' The idea targets AAAI 2027 and ICLR 2027 instead. While round 1 suggested this retargeting, the user's requirement has not changed. The simplified two-axis approach (no kernel mods) may actually be feasible in 16 days for EMNLP 2026.", "EMA STABILITY CONCERN: 'EMA Is Not All You Need' (arXiv:2604.08556, Apr 2026) shows EMA traces destroy token identity and suffer irreversible information dilution — after ~50 steps with decay 0.98, the centroid becomes a 'smeared summary' losing discriminative power. For reasoning traces spanning 1000+ tokens, the EMA centroid may become indistinguishable from a static average, making the redundancy signal unreliable for long chains.", "TEAL 65% SPARSITY CLIFF: Anti-evidence shows that at 65% MLP sparsity, most models (especially newer SwiGLU architectures like Qwen3 and DeepSeek-R1-Distill) degrade significantly. The proposed 60-65% threshold for 'redundant' tokens is right at this documented performance cliff. The safety margin between 'works' (40-50%) and 'breaks' (65%+) is dangerously thin.", "ThinKV MISCHARACTERIZATION: The landscape states ThinKV 'requires a learned phase classifier' — this is INCORRECT. ThinKV uses kernel density estimation (KDE) on attention sparsity distributions to compute thresholds, a heuristic approach, not a learned classifier. This weakens the positioning against ThinKV.", "KEY-ONLY SIMILARITY IS AN INCOMPLETE REDUNDANCY PROXY: Two tokens may have very similar key vectors but be attended to very differently by queries at different positions. Research on query-key distribution shift (CSAttention, FASA) shows that key-only metrics miss query-dependent importance. The generator should acknowledge this limitation or incorporate value similarity (as Token Filtering does).", "MLP SPARSITY VANISHES UNDER BATCHING: Polar Sparsity (NeurIPS 2025) shows that MLP neuron-level sparsity disappears at larger batch sizes (union of active neurons approaches dense). The proposed two-tier MLP sparsity would show diminishing returns under batched serving — a critical limitation for the 'efficient serving' framing.", "MISSING CRITICAL REFERENCES: Token Filtering (arXiv:2512.07090), KeyDiff (arXiv:2504.15364), EvoSparse (ACL 2026), CSAttention (arXiv:2604.08584), and 'EMA Is Not All You Need' (arXiv:2604.08556) are all directly relevant but uncited."]
Feedback: The proposal has improved significantly from round 1 — dropping Polar Sparsity from core, using two-tier TEAL thresholds without kernel mods, and matching user-required benchmarks are all correct fixes. However, a critical novelty problem has emerged:

1. **Cite Token Filtering and reframe the contribution**: Token Filtering (arXiv:2512.07090) already proposes the EMA centroid signal for per-token redundancy detection. You MUST cite this paper and reframe your contribution from 'novel signal' to 'novel DUAL APPLICATION of a known signal.' Specifically: Token Filtering uses EMA similarity only for attention layer skipping, while RTDS extends it to simultaneously drive MLP sparsity (via TEAL) AND KV cache eviction — a cross-axis coordination that no prior work achieves. Also consider incorporating Token Filtering's variance-aware key+value fusion (Eq. 2-3) to improve signal quality, which would be a genuine enhancement.

2. **Address EMA stability for long sequences**: The 'EMA Is Not All You Need' paper directly challenges your core mechanism. Mitigate by: (a) using a shorter decay window (α=0.1-0.2 instead of 0.01-0.05) to prevent information dilution, (b) adding a 'reset' mechanism when the similarity drops sharply (indicating a topic shift in reasoning), or (c) using a sliding window mean instead of EMA for better locality. Include an ablation comparing EMA vs. sliding window vs. Token Filtering's variant.

3. **Lower the redundant-token sparsity from 60-65% to 50-55%**: This provides a safer margin above TEAL's validated 40-50% range while still providing meaningful differentiation between tiers. The 65% cliff is well-documented and will likely cause accuracy degradation on Qwen3/DeepSeek models with SwiGLU.

4. **Reconsider EMNLP 2026**: With the simplified approach (no kernel mods, ~130h H100, two clean axes), the 16-day timeline IS tight but possibly feasible, especially since you have available code for both R-KV and TEAL. If you keep AAAI 2027, you should also consider EMNLP 2026 as a stretch target — the approach is simple enough that a focused implementation sprint could work. The user explicitly requested EMNLP 2026.

5. **Fix ThinKV characterization**: Replace 'requires a learned phase classifier' with 'requires offline KDE calibration on attention sparsity distributions.'

6. **Add KeyDiff citation and differentiation**: KeyDiff uses mean-of-keys (not EMA) for KV eviction. Cite it and explain why EMA is preferable (recency bias captures local redundancy patterns better than global mean).

7. **Acknowledge the batching limitation**: State explicitly that MLP sparsity gains diminish at larger batch sizes (per Polar Sparsity) and that RTDS is primarily targeted at batch=1 or small-batch reasoning generation, which is the dominant use case for reasoning models.


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
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "type": "user",
  "uuid": "6fd1ca46-94f3-4c94-8c1f-717e56804ec9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T18:15:56.096Z_

```json
{
  "parentUuid": "6fd1ca46-94f3-4c94-8c1f-717e56804ec9",
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
  "uuid": "936d18c9-6b38-4194-b8a4-29aa7e445785",
  "timestamp": "2026-05-10T18:15:56.096Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T18:15:56.096Z_

```json
{
  "parentUuid": "936d18c9-6b38-4194-b8a4-29aa7e445785",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cd27eee5-65ae-420e-816f-9dc30b61485e",
  "timestamp": "2026-05-10T18:15:56.096Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
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
  "leafUuid": "cd27eee5-65ae-420e-816f-9dc30b61485e",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify redundancy-coordination efficiency method for EMNLP",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

### Assistant

_source line 8 · 2026-05-10T18:16:09.722Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea - "Cross-Axis Redundancy Coordination (CARC)" - which is now in round 3 of review. The idea proposes using Token Filtering's EMA-based redundancy signal to simultaneously drive MLP sparsity and KV cache eviction during reasoning model inference.

Let me first understand what changed from round 2:
1. Token Filtering is now properly cited and the contribution is reframed as extending a known signal to coordinate across multiple axes
2. A windowed-reset mechanism is proposed to address EMA stability concerns


3. The MLP sparsity targets have been adjusted down to 50-55% for redundant tokens, ThinKV's characterization is now based on kernel density estimation rather than a learned classifier, and KeyDiff is properly cited with clear differentiation from the EMA approach. The batching limitation is acknowledged with focus on single-batch inference, EMNLP 2026 is the target venue, and the benchmarks align with the stated requirements.

Now I need to verify the foundational claims - whether Token Filtering actually implements the EMA signal as described, and what R-KV's exact contributions are.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd27eee5-65ae-420e-816f-9dc30b61485e",
  "isSidechain": false,
  "requestId": "req_011CauLyTLWw3wKRS9Qvp2gZ",
  "type": "assistant",
  "uuid": "008ac7b7-ad98-4669-93e2-1d8b67bdd1f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FntQts6Tz5tGU314WFL4dD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15680,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1992,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1992,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 15680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15680
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

_source line 9 · 2026-05-10T18:16:09.730Z_

I'll conduct an independent verification of this round 3 proposal. Let me search for the key papers and competing work in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "008ac7b7-ad98-4669-93e2-1d8b67bdd1f4",
  "isSidechain": false,
  "requestId": "req_011CauLyTLWw3wKRS9Qvp2gZ",
  "type": "assistant",
  "uuid": "135ebcd9-ab88-4500-98b1-838b7f84504d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FntQts6Tz5tGU314WFL4dD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15680,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1992,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1992,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 15680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15680
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

_source line 10 · 2026-05-10T18:16:16.233Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011XF9E87Z33FUFjf5Pp9Dpm`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Token Filtering paper",
  "prompt": "Search the web to verify the paper \"Token Filtering: Leveraging KV Similarity for Online Structured Pruning in LLMs\" (arXiv:2512.07090, Dec 2025). I need to know:\n1. Does this paper actually exist on arXiv?\n2. What is the exact method? Does it use EMA centroid similarity of key-value vectors?\n3. Does it have variance-aware key+value fusion (equations 2-3)?\n4. What does it use the signal for — attention layer skipping? Does it also do MLP sparsity or KV eviction?\n5. What speedups does it report?\n\nUse WebSearch and WebFetch to find and read the paper. Search for \"Token Filtering KV Similarity arXiv 2512.07090\" and \"Token Filtering Leveraging KV Similarity Online Structured Pruning\". Try to fetch the actual arXiv page. Report all details you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "135ebcd9-ab88-4500-98b1-838b7f84504d",
  "isSidechain": false,
  "requestId": "req_011CauLyTLWw3wKRS9Qvp2gZ",
  "type": "assistant",
  "uuid": "79b06418-e62a-4b89-b95e-5eff5a0ed43f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FntQts6Tz5tGU314WFL4dD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15680,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1992,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1992,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 15680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15680
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

_source line 11 · 2026-05-10T18:16:22.068Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01YYkQ6D7WauBiTHWu5kTJm5`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify R-KV and TEAL papers",
  "prompt": "Search the web to verify these two papers:\n\n1. \"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models\" — claimed to be at NeurIPS 2025. Does it exist? What is its approach? Does it use O(B²) pairwise key similarity for periodic eviction? What KV memory savings does it achieve?\n\n2. \"TEAL: Training-Free Activation Sparsity in Large Language Models\" — claimed to be ICLR 2025 Spotlight. Does it exist? Does it achieve 40-50% MLP activation sparsity with 1.5-1.8× decoding speedup? Does it use magnitude pruning with fixed per-layer thresholds? Is there a documented performance cliff at 65% sparsity for SwiGLU architectures?\n\nUse WebSearch and WebFetch. Search for exact titles and arXiv IDs. Report all details found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79b06418-e62a-4b89-b95e-5eff5a0ed43f",
  "isSidechain": false,
  "requestId": "req_011CauLyTLWw3wKRS9Qvp2gZ",
  "type": "assistant",
  "uuid": "45268ce4-a575-423c-9f95-d3e5e271ae6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FntQts6Tz5tGU314WFL4dD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15680,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1992,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1992,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 15680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15680
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

_source line 12 · 2026-05-10T18:16:26.771Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AH27kSVUGyerCPBv72LGzj`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify EMA paper and KeyDiff",
  "prompt": "Search the web to verify these papers:\n\n1. \"EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context\" (arXiv:2604.08556, Apr 2026). Does this paper exist? Does it show that EMA traces suffer irreversible information dilution? What are its key findings about EMA as context representations?\n\n2. \"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference\" (arXiv:2504.15364). Does this paper exist? Does it use mean-of-keys (not EMA) as an anchor for KV eviction?\n\n3. \"CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference\" (arXiv:2604.08584, Apr 2026). Does this paper exist? Does it construct query-centric lookup tables?\n\nUse WebSearch and WebFetch. Search for exact titles and arXiv IDs. Report all details found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45268ce4-a575-423c-9f95-d3e5e271ae6d",
  "isSidechain": false,
  "requestId": "req_011CauLyTLWw3wKRS9Qvp2gZ",
  "type": "assistant",
  "uuid": "df24462c-56c1-465a-bed6-3d3bfd026572",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FntQts6Tz5tGU314WFL4dD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15680,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1992,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1992,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 15680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15680
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

_source line 13 · 2026-05-10T18:16:34.783Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01J6W4Rd2J59tjxwBMRQ4Yre`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competing work",
  "prompt": "Search the web for recent papers (2025-2026) that combine multiple efficiency axes for LLM inference — specifically papers that jointly optimize MLP sparsity AND KV cache compression/eviction during inference. I want to find competing work that the idea \"Cross-Axis Redundancy Coordination\" might have missed.\n\nSearch queries to use:\n1. \"joint MLP sparsity KV cache compression LLM inference 2025 2026\"\n2. \"multi-axis efficiency LLM reasoning inference\"\n3. \"unified signal MLP KV cache optimization\"\n4. \"cross-layer sparsity KV eviction reasoning models\"\n5. \"QuickSilver LLM inference token halting\" — verify this paper exists\n6. \"EvoSparse evolving sparsity token importance ACL 2026\"\n7. \"FASA frequency-aware sparse attention ICLR 2026\"\n8. \"ThinKV thought-adaptive KV cache compression ICLR 2026\"\n9. \"SeerAttention-R sparse attention reasoning ICLR 2026\"\n10. \"Polar Sparsity batched LLM inference NeurIPS 2025\"\n\nUse WebSearch for each. Report what you find — especially any paper that coordinates savings across both MLP and KV cache axes simultaneously."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df24462c-56c1-465a-bed6-3d3bfd026572",
  "isSidechain": false,
  "requestId": "req_011CauLyTLWw3wKRS9Qvp2gZ",
  "type": "assistant",
  "uuid": "11afa0ba-bc03-4021-bc6c-f46e4a4b8a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FntQts6Tz5tGU314WFL4dD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15680,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1992,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1992,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 15680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15680
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

_source line 14 · 2026-05-10T18:16:37.570Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BtThyJ2ujpFx8cTMP2nK2K`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify EMNLP 2026 deadline",
  "prompt": "Search the web to verify the EMNLP 2026 submission deadline. The claim is that the ARR submission deadline is May 25, 2026. Search for:\n1. \"EMNLP 2026 submission deadline\"\n2. \"ACL Rolling Review ARR 2026 May deadline\"\n3. \"EMNLP 2026 call for papers\"\n\nAlso check: is May 25, 2026 an ARR cycle deadline? How does ARR submission work for EMNLP 2026?\n\nReport all details found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11afa0ba-bc03-4021-bc6c-f46e4a4b8a4c",
  "isSidechain": false,
  "requestId": "req_011CauLyTLWw3wKRS9Qvp2gZ",
  "type": "assistant",
  "uuid": "c83e8b5d-696a-44c2-bf29-98ecfa1bc599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FntQts6Tz5tGU314WFL4dD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15680,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1992,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1992,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 15680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15680
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

_source line 15 · 2026-05-10T18:17:29.842Z_

<details><summary>↩ Tool result · `toolu_01BtThyJ2ujpFx8cTMP2nK2K`</summary>

```text
I now have comprehensive information. Here is the full report.

---

## EMNLP 2026 Submission Deadline Verification

### Claim Verified: The ARR submission deadline of May 25, 2026 is CONFIRMED.

The official EMNLP 2026 Call for Papers and the ACL Rolling Review dates page both confirm that **May 25, 2026** is the ARR submission deadline for EMNLP 2026. The EMNLP 2026 Twitter/X account also announced this date explicitly.

---

### All Key Dates for EMNLP 2026

| Milestone | Date |
|---|---|
| ARR Submission Deadline (long & short papers) | **May 25, 2026** |
| Reviewer Registration Deadline (for ALL authors) | May 27, 2026 |
| Reviews Due | June 29, 2026 |
| Author Response & Author-Reviewer Discussion | July 7 -- July 13, 2026 |
| Meta-reviews Released | July 30, 2026 |
| EMNLP Commitment Deadline | August 2, 2026 |
| Notification of Acceptance | August 20, 2026 |
| Camera-Ready Papers Due | September 20, 2026 |
| Main Conference (Budapest, Hungary) | October 24 -- 29, 2026 |

All deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth").

---

### Is May 25, 2026 an ARR Cycle Deadline?

Yes. May 25, 2026 is the official submission deadline for the **May 2026 ARR cycle**. The ARR switched from 8-week to 10-week review cycles starting in May 2025, so there are roughly 5 cycles per year. The 2026 ARR cycles are:

| ARR Cycle | Submission Deadline | Cycle End |
|---|---|---|
| March 2026 | March 16 | May 24 |
| **May 2026** | **May 25** | **August 2** |
| August 2026 | August 3 | October 11 |
| October 2026 | October 12 | December 20 |

---

### How ARR Submission Works for EMNLP 2026

EMNLP 2026 uses a **two-stage process** through ACL Rolling Review:

1. **Stage 1 -- ARR Submission:** Authors submit their paper to the May 2026 ARR cycle by May 25, 2026. The paper goes through the standard ARR review process (reviews, author response, meta-reviews).

2. **Stage 2 -- Commitment to EMNLP:** Once reviews are complete, authors "commit" their reviewed paper to EMNLP 2026 by the commitment deadline of August 2, 2026.

**Critical policy for EMNLP 2026 -- Binding Venue Declaration:** Because the May 2026 ARR cycle is shared with two conferences (EMNLP 2026 and AACL 2026), authors must **explicitly declare at submission time** which conference they intend to commit to. This declaration is **binding for EMNLP**: ARR May 2026 submissions that do not select EMNLP 2026 during submission will NOT be able to commit to EMNLP 2026 later. (However, AACL 2026 retains flexibility -- its commitment deadline is August 26, 2026.)

Other important policies:
- Modification of the author list between submission and commitment is not allowed (though reordering is permitted).
- EMNLP 2026 warns against unethical submissions (thinly sliced contributions, hallucinated citations, entirely AI-generated papers), which may result in desk rejection and a ban from committing to EMNLP 2026 and EMNLP 2027.

---

### Summary

The claim that the ARR submission deadline is **May 25, 2026** is **correct and verified** across multiple official sources. This is the deadline for the May 2026 ARR cycle, which feeds into EMNLP 2026 (commitment deadline August 2, 2026). Authors must remember to declare EMNLP as their target venue at submission time, as this choice is binding.

Sources:
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL Rolling Review -- Dates and Venues](http://aclrollingreview.org/dates)
- [EMNLP 2026 Official Twitter/X Announcement](https://x.com/emnlpmeeting/status/2029508292637061462)
- [2026 *ACL Conference Dates (Computational Linguistics)](https://submissions.cljournal.org/index.php/cljournal/announcement/view/14)
- [EMNLP 2026 Official Website](https://2026.emnlp.org/)

agentId: a20ed2cc207789ad3 (use SendMessage with to: 'a20ed2cc207789ad3' to continue this agent)
&lt;usage>total_tokens: 16201
tool_uses: 7
duration_ms: 52267&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c83e8b5d-696a-44c2-bf29-98ecfa1bc599",
  "isSidechain": false,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "type": "user",
  "uuid": "a3aa02c8-1a19-4aa2-b773-56e52db178e9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify the EMNLP 2026 submission deadline. The claim is that the ARR submission deadline is May 25, 2026. Search for:\n1. \"EMNLP 2026 submission deadline\"\n2. \"ACL Rolling Review ARR 2026 May deadline\"\n3. \"EMNLP 2026 call for papers\"\n\nAlso check: is May 25, 2026 an ARR cycle deadline? How does ARR submission work for EMNLP 2026?\n\nReport all details found.",
    "agentId": "a20ed2cc207789ad3",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is the full report.\n\n---\n\n## EMNLP 2026 Submission Deadline Verification\n\n### Claim Verified: The ARR submission deadline of May 25, 2026 is CONFIRMED.\n\nThe official EMNLP 2026 Call for Papers and the ACL Rolling Review dates page both confirm that **May 25, 2026** is the ARR submission deadline for EMNLP 2026. The EMNLP 2026 Twitter/X account also announced this date explicitly.\n\n---\n\n### All Key Dates for EMNLP 2026\n\n| Milestone | Date |\n|---|---|\n| ARR Submission Deadline (long & short papers) | **May 25, 2026** |\n| Reviewer Registration Deadline (for ALL authors) | May 27, 2026 |\n| Reviews Due | June 29, 2026 |\n| Author Response & Author-Reviewer Discussion | July 7 -- July 13, 2026 |\n| Meta-reviews Released | July 30, 2026 |\n| EMNLP Commitment Deadline | August 2, 2026 |\n| Notification of Acceptance | August 20, 2026 |\n| Camera-Ready Papers Due | September 20, 2026 |\n| Main Conference (Budapest, Hungary) | October 24 -- 29, 2026 |\n\nAll deadlines are 11:59 PM UTC-12:00 (\"anywhere on Earth\").\n\n---\n\n### Is May 25, 2026 an ARR Cycle Deadline?\n\nYes. May 25, 2026 is the official submission deadline for the **May 2026 ARR cycle**. The ARR switched from 8-week to 10-week review cycles starting in May 2025, so there are roughly 5 cycles per year. The 2026 ARR cycles are:\n\n| ARR Cycle | Submission Deadline | Cycle End |\n|---|---|---|\n| March 2026 | March 16 | May 24 |\n| **May 2026** | **May 25** | **August 2** |\n| August 2026 | August 3 | October 11 |\n| October 2026 | October 12 | December 20 |\n\n---\n\n### How ARR Submission Works for EMNLP 2026\n\nEMNLP 2026 uses a **two-stage process** through ACL Rolling Review:\n\n1. **Stage 1 -- ARR Submission:** Authors submit their paper to the May 2026 ARR cycle by May 25, 2026. The paper goes through the standard ARR review process (reviews, author response, meta-reviews).\n\n2. **Stage 2 -- Commitment to EMNLP:** Once reviews are complete, authors \"commit\" their reviewed paper to EMNLP 2026 by the commitment deadline of August 2, 2026.\n\n**Critical policy for EMNLP 2026 -- Binding Venue Declaration:** Because the May 2026 ARR cycle is shared with two conferences (EMNLP 2026 and AACL 2026), authors must **explicitly declare at submission time** which conference they intend to commit to. This declaration is **binding for EMNLP**: ARR May 2026 submissions that do not select EMNLP 2026 during submission will NOT be able to commit to EMNLP 2026 later. (However, AACL 2026 retains flexibility -- its commitment deadline is August 26, 2026.)\n\nOther important policies:\n- Modification of the author list between submission and commitment is not allowed (though reordering is permitted).\n- EMNLP 2026 warns against unethical submissions (thinly sliced contributions, hallucinated citations, entirely AI-generated papers), which may result in desk rejection and a ban from committing to EMNLP 2026 and EMNLP 2027.\n\n---\n\n### Summary\n\nThe claim that the ARR submission deadline is **May 25, 2026** is **correct and verified** across multiple official sources. This is the deadline for the May 2026 ARR cycle, which feeds into EMNLP 2026 (commitment deadline August 2, 2026). Authors must remember to declare EMNLP as their target venue at submission time, as this choice is binding.\n\nSources:\n- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [ACL Rolling Review -- Dates and Venues](http://aclrollingreview.org/dates)\n- [EMNLP 2026 Official Twitter/X Announcement](https://x.com/emnlpmeeting/status/2029508292637061462)\n- [2026 *ACL Conference Dates (Computational Linguistics)](https://submissions.cljournal.org/index.php/cljournal/announcement/view/14)\n- [EMNLP 2026 Official Website](https://2026.emnlp.org/)"
      }
    ],
    "totalDurationMs": 52267,
    "totalTokens": 16201,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 479,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 13620,
      "output_tokens": 1228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 479,
          "output_tokens": 1228,
          "cache_read_input_tokens": 13620,
          "cache_creation_input_tokens": 874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 874,
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
  "sourceToolAssistantUUID": "c83e8b5d-696a-44c2-bf29-98ecfa1bc599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:17:31.180Z_

<details><summary>↩ Tool result · `toolu_011XF9E87Z33FUFjf5Pp9Dpm`</summary>

```text
ResearchGate blocked the request, but I have enough information from the arXiv HTML version which was very detailed. Here is my full report.

---

## Findings: arXiv:2512.07090

### 1. Does this paper actually exist on arXiv?

**Yes.** The paper is real and available at [arxiv.org/abs/2512.07090](https://arxiv.org/abs/2512.07090). Its exact title is **"Leveraging KV Similarity for Online Structured Pruning in LLMs"** (not "Token Filtering: Leveraging..."). "Token Filtering" is the name of the proposed method, not part of the paper title. It was submitted December 8, 2025. The authors are **Jungmin Lee, Gwangeun Byeon, Yulhwa Kim, and Seokin Hong**.

### 2. Exact method -- does it use EMA centroid similarity?

**Yes, it uses EMA (exponential moving average) anchors, not simple mean centroids.** The method maintains per-layer EMA "anchors" for both keys and values:

- **Equation 1**: `Anchor <- gamma * Anchor + (1 - gamma) * k_current`, with gamma close to 1.0 (e.g., 0.9), which emphasizes recent tokens and captures a "recent window of key information."
- Per-head **cosine similarity** is then computed between the current token's key/value vectors and the respective EMA anchors.

### 3. Variance-aware key+value fusion (Equations 2-3)?

**Yes, this is confirmed.** The paper has exactly this:

- **Equation 2** (variance-aware weighting): `alpha = sigma_v^(-2) / (sigma_k^(-2) + sigma_v^(-2))` -- this weights the more stable feature (lower variance across heads) more heavily.
- **Equation 3** (fused similarity score): `S_KV = alpha * s_k + (1 - alpha) * s_v` -- the final score is a variance-weighted combination of key similarity and value similarity.

So the claim about "variance-aware key+value fusion in Equations 2-3" is accurate.

### 4. What does it use the signal for?

**Attention layer skipping** -- this is the primary use. When the fused similarity score exceeds a layer-specific threshold, the entire attention computation for that token at that layer is skipped. The FFN/MLP still executes normally, and the attention output effectively becomes zero via the residual connection.

Additional details:
- **Equation 4** (tail pruning): `P_tail = P_global / Y` -- distributes pruning budget across layers.
- **Equation 5** (threshold adaptation): `T_l <- T_l + eta * (P_current - P_tail)` -- dynamically adjusts per-layer thresholds via proportional feedback to hit the target pruning ratio.

Regarding your specific sub-questions:
- **Attention layer skipping**: Yes, this is the core mechanism.
- **MLP sparsity**: No -- the FFN/MLP always executes; only attention is skipped.
- **KV eviction**: No -- this is not a KV cache eviction method. It is structured token-level pruning of attention computation. (Note: the PDF fetch gave a conflicting answer suggesting KV eviction, but the detailed HTML version clearly describes attention layer skipping, which is more reliable.)

### 5. What speedups does it report?

Concrete numbers from the paper:
- **46.6% latency reduction** at batch size 128
- **33.6% memory reduction** at batch size 128
- **~87% throughput improvement**: from 4.7 to 8.8 tokens/sec at batch size 128 for LLaMA-2-13B
- Speedup increases with batch size; minimal gains at small batches (attention is only ~68% of latency at batch size 8)
- Pruning ratios tested: **20%, 25%, 33%, and 50%** across LLaMA-2 7B/13B, LLaMA-3 8B, Mistral-7B, and Phi-4-14B
- Accuracy is preserved on commonsense reasoning benchmarks and MMLU even at 50% pruning

---

**Summary**: The paper is real, uses EMA anchor similarity (not simple mean), does have variance-aware key+value fusion in Equations 2-3 exactly as described, performs attention layer skipping (not MLP sparsity or KV eviction), and reports up to ~87% throughput gain / 46.6% latency reduction at high batch sizes with 50% pruning.

Sources:
- [arXiv:2512.07090 Abstract](https://arxiv.org/abs/2512.07090)
- [arXiv:2512.07090 HTML Full Paper](https://arxiv.org/html/2512.07090)
- [arXiv:2512.07090 PDF](https://www.arxiv.org/pdf/2512.07090)

agentId: a0b8547c4ed79c1cc (use SendMessage with to: 'a0b8547c4ed79c1cc' to continue this agent)
&lt;usage>total_tokens: 16500
tool_uses: 7
duration_ms: 74941&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79b06418-e62a-4b89-b95e-5eff5a0ed43f",
  "isSidechain": false,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "type": "user",
  "uuid": "7935ca87-f376-4f64-ab00-7dfa1cf090b4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify the paper \"Token Filtering: Leveraging KV Similarity for Online Structured Pruning in LLMs\" (arXiv:2512.07090, Dec 2025). I need to know:\n1. Does this paper actually exist on arXiv?\n2. What is the exact method? Does it use EMA centroid similarity of key-value vectors?\n3. Does it have variance-aware key+value fusion (equations 2-3)?\n4. What does it use the signal for — attention layer skipping? Does it also do MLP sparsity or KV eviction?\n5. What speedups does it report?\n\nUse WebSearch and WebFetch to find and read the paper. Search for \"Token Filtering KV Similarity arXiv 2512.07090\" and \"Token Filtering Leveraging KV Similarity Online Structured Pruning\". Try to fetch the actual arXiv page. Report all details you find.",
    "agentId": "a0b8547c4ed79c1cc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "ResearchGate blocked the request, but I have enough information from the arXiv HTML version which was very detailed. Here is my full report.\n\n---\n\n## Findings: arXiv:2512.07090\n\n### 1. Does this paper actually exist on arXiv?\n\n**Yes.** The paper is real and available at [arxiv.org/abs/2512.07090](https://arxiv.org/abs/2512.07090). Its exact title is **\"Leveraging KV Similarity for Online Structured Pruning in LLMs\"** (not \"Token Filtering: Leveraging...\"). \"Token Filtering\" is the name of the proposed method, not part of the paper title. It was submitted December 8, 2025. The authors are **Jungmin Lee, Gwangeun Byeon, Yulhwa Kim, and Seokin Hong**.\n\n### 2. Exact method -- does it use EMA centroid similarity?\n\n**Yes, it uses EMA (exponential moving average) anchors, not simple mean centroids.** The method maintains per-layer EMA \"anchors\" for both keys and values:\n\n- **Equation 1**: `Anchor <- gamma * Anchor + (1 - gamma) * k_current`, with gamma close to 1.0 (e.g., 0.9), which emphasizes recent tokens and captures a \"recent window of key information.\"\n- Per-head **cosine similarity** is then computed between the current token's key/value vectors and the respective EMA anchors.\n\n### 3. Variance-aware key+value fusion (Equations 2-3)?\n\n**Yes, this is confirmed.** The paper has exactly this:\n\n- **Equation 2** (variance-aware weighting): `alpha = sigma_v^(-2) / (sigma_k^(-2) + sigma_v^(-2))` -- this weights the more stable feature (lower variance across heads) more heavily.\n- **Equation 3** (fused similarity score): `S_KV = alpha * s_k + (1 - alpha) * s_v` -- the final score is a variance-weighted combination of key similarity and value similarity.\n\nSo the claim about \"variance-aware key+value fusion in Equations 2-3\" is accurate.\n\n### 4. What does it use the signal for?\n\n**Attention layer skipping** -- this is the primary use. When the fused similarity score exceeds a layer-specific threshold, the entire attention computation for that token at that layer is skipped. The FFN/MLP still executes normally, and the attention output effectively becomes zero via the residual connection.\n\nAdditional details:\n- **Equation 4** (tail pruning): `P_tail = P_global / Y` -- distributes pruning budget across layers.\n- **Equation 5** (threshold adaptation): `T_l <- T_l + eta * (P_current - P_tail)` -- dynamically adjusts per-layer thresholds via proportional feedback to hit the target pruning ratio.\n\nRegarding your specific sub-questions:\n- **Attention layer skipping**: Yes, this is the core mechanism.\n- **MLP sparsity**: No -- the FFN/MLP always executes; only attention is skipped.\n- **KV eviction**: No -- this is not a KV cache eviction method. It is structured token-level pruning of attention computation. (Note: the PDF fetch gave a conflicting answer suggesting KV eviction, but the detailed HTML version clearly describes attention layer skipping, which is more reliable.)\n\n### 5. What speedups does it report?\n\nConcrete numbers from the paper:\n- **46.6% latency reduction** at batch size 128\n- **33.6% memory reduction** at batch size 128\n- **~87% throughput improvement**: from 4.7 to 8.8 tokens/sec at batch size 128 for LLaMA-2-13B\n- Speedup increases with batch size; minimal gains at small batches (attention is only ~68% of latency at batch size 8)\n- Pruning ratios tested: **20%, 25%, 33%, and 50%** across LLaMA-2 7B/13B, LLaMA-3 8B, Mistral-7B, and Phi-4-14B\n- Accuracy is preserved on commonsense reasoning benchmarks and MMLU even at 50% pruning\n\n---\n\n**Summary**: The paper is real, uses EMA anchor similarity (not simple mean), does have variance-aware key+value fusion in Equations 2-3 exactly as described, performs attention layer skipping (not MLP sparsity or KV eviction), and reports up to ~87% throughput gain / 46.6% latency reduction at high batch sizes with 50% pruning.\n\nSources:\n- [arXiv:2512.07090 Abstract](https://arxiv.org/abs/2512.07090)\n- [arXiv:2512.07090 HTML Full Paper](https://arxiv.org/html/2512.07090)\n- [arXiv:2512.07090 PDF](https://www.arxiv.org/pdf/2512.07090)"
      }
    ],
    "totalDurationMs": 74941,
    "totalTokens": 16500,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 14958,
      "output_tokens": 1223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 318
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1223,
          "cache_read_input_tokens": 14958,
          "cache_creation_input_tokens": 318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 318,
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
  "sourceToolAssistantUUID": "79b06418-e62a-4b89-b95e-5eff5a0ed43f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "7935ca87-f376-4f64-ab00-7dfa1cf090b4",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify redundancy-coordination efficiency method for EMNLP",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

### Tool result

_source line 19 · 2026-05-10T18:17:53.879Z_

<details><summary>↩ Tool result · `toolu_01AH27kSVUGyerCPBv72LGzj`</summary>

```text
Now I have comprehensive details on all three papers. Here is the full report.

---

## Paper 1: "EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context"

**arXiv ID:** 2604.08556 -- **EXISTS: YES**

- **URL:** [https://arxiv.org/abs/2604.08556](https://arxiv.org/abs/2604.08556)
- **Author:** Arth Singh (AIM Intelligence, National Institute of Technology Agartala)
- **Submission date:** March 17, 2026

**Does it show that EMA traces suffer irreversible information dilution?** Yes. The abstract explicitly states that "fixed-coefficient accumulation suffers irreversible information dilution that only learned, input-dependent selection can resolve." The paper invokes the data processing inequality to formally explain this phenomenon.

**Key findings about EMA as context representations:**

1. **EMA encodes temporal structure well.** A Hebbian architecture using multi-timescale EMA traces achieves 96% of a supervised BiGRU on grammatical role assignment with zero labels, and surpasses the supervised model on structure-dependent roles.
2. **EMA destroys token identity.** A 130M-parameter language model using only EMA context reaches a C4 perplexity of 260, which is 8x worse than GPT-2 -- demonstrating that EMA's lossy, data-independent compression cannot preserve individual token information.
3. **The core thesis:** EMA handles structural patterns effectively but fundamentally cannot preserve semantic content. Learned, input-dependent gating (as in real recurrent models) is necessary to cross that boundary.

---

## Paper 2: "KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference"

**arXiv ID:** 2504.15364 -- **EXISTS: YES**

- **URL:** [https://arxiv.org/abs/2504.15364](https://arxiv.org/abs/2504.15364)
- **Authors:** Junyoung Park, Dalton Jones, Matthew J Morse, Raghavv Goel, Mingu Lee, and Chris Lott
- **Submission date:** April 21, 2025

**Does it use mean-of-keys (not EMA) as an anchor for KV eviction?** Yes, it does use mean-of-keys. The paper computes an anchor vector as the mean of all cached keys: `mu(K) = (1/n) * sum(k_i)`. It then computes cosine similarity between each key and this mean anchor. Keys that are **most dissimilar** from the mean (i.e., most geometrically distinctive) are retained, while keys similar to the mean are evicted. The formula is `topk(-CosSim(mu(K), k_i), N)`. This is explicitly a mean-of-keys approach, **not** EMA.

**Additional details:**
- The efficient variant runs in O(n) time (vs O(n^2) for full pairwise similarity) by using the single mean anchor vector.
- This allows compatibility with FlashAttention since it does not require attention scores.
- With an 8K cache budget (~23% KV cache reduction), KeyDiff achieves less than 0.04% performance gap from the non-evicting baseline on LongBench.
- Achieves up to 30% end-to-end inference latency reduction compared to existing KV cache eviction methods.

---

## Paper 3: "CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference"

**arXiv ID:** 2604.08584 -- **EXISTS: YES**

- **URL:** [https://arxiv.org/abs/2604.08584](https://arxiv.org/abs/2604.08584)
- **Authors:** Chuxu Song, Zhencan Peng, Jiuqi Wei, and Chuanhui Yang
- **Submission date:** March 30, 2026
- Also appears on [OpenReview](https://openreview.net/forum?id=CEpNboUJyw)

**Does it construct query-centric lookup tables?** Yes, explicitly. The abstract states CSAttention "constructs query-centric lookup tables during offline prefill, whose size remains fixed during decoding."

**How centroid-scoring works step by step:**

1. **Offline prefill phase:** Prefill queries Q are partitioned into m subspaces. For each subspace, queries are clustered into C centroids using cosine k-means (centroids are built from **queries**, not keys -- this is the "query-centric" aspect).
2. **Centroid-score computation:** For each centroid, the method precomputes inner products (partial dot-products) between the centroid and all prefill keys, storing the Top-L key indices and scores as bounded lookup tables.
3. **Online decode phase:** For a new decode query: (a) find the nearest centroid per subspace via cosine similarity, (b) fetch m short lists from the lookup tables, (c) aggregate scores across subspaces, (d) select Top-K keys from accumulated scores.
4. This replaces full-context scans with efficient table lookups.

**Performance:** At 95% sparsity (keeping only ~5% of tokens), CSAttention maintains accuracy within statistical noise of full attention. Achieves up to 4.24-4.6x speedup over full attention at 128K context length.

---

**Summary:** All three papers exist at their stated arXiv IDs. Paper 1 does show irreversible information dilution of EMA traces. Paper 2 does use mean-of-keys (not EMA) as an anchor. Paper 3 does construct query-centric lookup tables by clustering prefill queries into centroids.

Sources:
- [EMA Is Not All You Need (arXiv:2604.08556)](https://arxiv.org/abs/2604.08556)
- [KeyDiff (arXiv:2504.15364)](https://arxiv.org/abs/2504.15364)
- [KeyDiff on alphaXiv](https://www.alphaxiv.org/abs/2504.15364)
- [KeyDiff on HuggingFace Papers](https://huggingface.co/papers/2504.15364)
- [CSAttention (arXiv:2604.08584)](https://arxiv.org/abs/2604.08584)
- [CSAttention on OpenReview](https://openreview.net/forum?id=CEpNboUJyw)

agentId: a24a26c99a74dea2d (use SendMessage with to: 'a24a26c99a74dea2d' to continue this agent)
&lt;usage>total_tokens: 17837
tool_uses: 9
duration_ms: 87106&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df24462c-56c1-465a-bed6-3d3bfd026572",
  "isSidechain": false,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "type": "user",
  "uuid": "c0c4765e-d877-4095-80e2-7302cdfe4f67",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify these papers:\n\n1. \"EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context\" (arXiv:2604.08556, Apr 2026). Does this paper exist? Does it show that EMA traces suffer irreversible information dilution? What are its key findings about EMA as context representations?\n\n2. \"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference\" (arXiv:2504.15364). Does this paper exist? Does it use mean-of-keys (not EMA) as an anchor for KV eviction?\n\n3. \"CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference\" (arXiv:2604.08584, Apr 2026). Does this paper exist? Does it construct query-centric lookup tables?\n\nUse WebSearch and WebFetch. Search for exact titles and arXiv IDs. Report all details found.",
    "agentId": "a24a26c99a74dea2d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive details on all three papers. Here is the full report.\n\n---\n\n## Paper 1: \"EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context\"\n\n**arXiv ID:** 2604.08556 -- **EXISTS: YES**\n\n- **URL:** [https://arxiv.org/abs/2604.08556](https://arxiv.org/abs/2604.08556)\n- **Author:** Arth Singh (AIM Intelligence, National Institute of Technology Agartala)\n- **Submission date:** March 17, 2026\n\n**Does it show that EMA traces suffer irreversible information dilution?** Yes. The abstract explicitly states that \"fixed-coefficient accumulation suffers irreversible information dilution that only learned, input-dependent selection can resolve.\" The paper invokes the data processing inequality to formally explain this phenomenon.\n\n**Key findings about EMA as context representations:**\n\n1. **EMA encodes temporal structure well.** A Hebbian architecture using multi-timescale EMA traces achieves 96% of a supervised BiGRU on grammatical role assignment with zero labels, and surpasses the supervised model on structure-dependent roles.\n2. **EMA destroys token identity.** A 130M-parameter language model using only EMA context reaches a C4 perplexity of 260, which is 8x worse than GPT-2 -- demonstrating that EMA's lossy, data-independent compression cannot preserve individual token information.\n3. **The core thesis:** EMA handles structural patterns effectively but fundamentally cannot preserve semantic content. Learned, input-dependent gating (as in real recurrent models) is necessary to cross that boundary.\n\n---\n\n## Paper 2: \"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference\"\n\n**arXiv ID:** 2504.15364 -- **EXISTS: YES**\n\n- **URL:** [https://arxiv.org/abs/2504.15364](https://arxiv.org/abs/2504.15364)\n- **Authors:** Junyoung Park, Dalton Jones, Matthew J Morse, Raghavv Goel, Mingu Lee, and Chris Lott\n- **Submission date:** April 21, 2025\n\n**Does it use mean-of-keys (not EMA) as an anchor for KV eviction?** Yes, it does use mean-of-keys. The paper computes an anchor vector as the mean of all cached keys: `mu(K) = (1/n) * sum(k_i)`. It then computes cosine similarity between each key and this mean anchor. Keys that are **most dissimilar** from the mean (i.e., most geometrically distinctive) are retained, while keys similar to the mean are evicted. The formula is `topk(-CosSim(mu(K), k_i), N)`. This is explicitly a mean-of-keys approach, **not** EMA.\n\n**Additional details:**\n- The efficient variant runs in O(n) time (vs O(n^2) for full pairwise similarity) by using the single mean anchor vector.\n- This allows compatibility with FlashAttention since it does not require attention scores.\n- With an 8K cache budget (~23% KV cache reduction), KeyDiff achieves less than 0.04% performance gap from the non-evicting baseline on LongBench.\n- Achieves up to 30% end-to-end inference latency reduction compared to existing KV cache eviction methods.\n\n---\n\n## Paper 3: \"CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference\"\n\n**arXiv ID:** 2604.08584 -- **EXISTS: YES**\n\n- **URL:** [https://arxiv.org/abs/2604.08584](https://arxiv.org/abs/2604.08584)\n- **Authors:** Chuxu Song, Zhencan Peng, Jiuqi Wei, and Chuanhui Yang\n- **Submission date:** March 30, 2026\n- Also appears on [OpenReview](https://openreview.net/forum?id=CEpNboUJyw)\n\n**Does it construct query-centric lookup tables?** Yes, explicitly. The abstract states CSAttention \"constructs query-centric lookup tables during offline prefill, whose size remains fixed during decoding.\"\n\n**How centroid-scoring works step by step:**\n\n1. **Offline prefill phase:** Prefill queries Q are partitioned into m subspaces. For each subspace, queries are clustered into C centroids using cosine k-means (centroids are built from **queries**, not keys -- this is the \"query-centric\" aspect).\n2. **Centroid-score computation:** For each centroid, the method precomputes inner products (partial dot-products) between the centroid and all prefill keys, storing the Top-L key indices and scores as bounded lookup tables.\n3. **Online decode phase:** For a new decode query: (a) find the nearest centroid per subspace via cosine similarity, (b) fetch m short lists from the lookup tables, (c) aggregate scores across subspaces, (d) select Top-K keys from accumulated scores.\n4. This replaces full-context scans with efficient table lookups.\n\n**Performance:** At 95% sparsity (keeping only ~5% of tokens), CSAttention maintains accuracy within statistical noise of full attention. Achieves up to 4.24-4.6x speedup over full attention at 128K context length.\n\n---\n\n**Summary:** All three papers exist at their stated arXiv IDs. Paper 1 does show irreversible information dilution of EMA traces. Paper 2 does use mean-of-keys (not EMA) as an anchor. Paper 3 does construct query-centric lookup tables by clustering prefill queries into centroids.\n\nSources:\n- [EMA Is Not All You Need (arXiv:2604.08556)](https://arxiv.org/abs/2604.08556)\n- [KeyDiff (arXiv:2504.15364)](https://arxiv.org/abs/2504.15364)\n- [KeyDiff on alphaXiv](https://www.alphaxiv.org/abs/2504.15364)\n- [KeyDiff on HuggingFace Papers](https://huggingface.co/papers/2504.15364)\n- [CSAttention (arXiv:2604.08584)](https://arxiv.org/abs/2604.08584)\n- [CSAttention on OpenReview](https://openreview.net/forum?id=CEpNboUJyw)"
      }
    ],
    "totalDurationMs": 87106,
    "totalTokens": 17837,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 468,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 15095,
      "output_tokens": 1582,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 692
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 468,
          "output_tokens": 1582,
          "cache_read_input_tokens": 15095,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 692,
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
      "otherToolCount": 9
    }
  },
  "sourceToolAssistantUUID": "df24462c-56c1-465a-bed6-3d3bfd026572",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T18:18:23.572Z_

<details><summary>↩ Tool result · `toolu_01J6W4Rd2J59tjxwBMRQ4Yre`</summary>

```text
Here is my comprehensive report on the search findings.

---

## Results Summary

### Papers Verified as Real

All 6 specific papers you asked about exist and are confirmed:

**1. QuickSilver (arXiv 2506.22396, June 2025)**
This is the most directly relevant paper to the "Cross-Axis Redundancy Coordination" concept. QuickSilver integrates four synergistic mechanisms in a single framework operating on frozen dense models: (i) Dynamic Token Halting (halts computation for tokens with converged representations via L2 drift), (ii) KV Cache Skipping (selectively suppresses memory writes for inactive tokens), (iii) Contextual Token Fusion (merges redundant tokens to shrink sequence length), and (iv) Adaptive Matryoshka Quantization. It achieves up to 39.6% FLOP reduction with <=0.2 perplexity degradation on GPT-2 and Llama-2. The authors explicitly describe these as targeting "orthogonal inefficiencies" that can be stacked. This is a genuine multi-axis coordination paper, though it focuses on token-level signals rather than explicitly coordinating MLP sparsity with KV cache compression.

**2. EvoSparse (ACL 2026 main)**
Confirmed. "Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention." Uses cross-step accumulation of token importance signals and retrieval head indices to guide non-retrieval heads across layers. Focus is on sparse attention (KV cache side) rather than MLP sparsity. Authors from Harbin Institute of Technology and Great Bay University. Code available at `github.com/iLearn-Lab/ACL26-EvoSparse`.

**3. FASA: Frequency-Aware Sparse Attention (ICLR 2026)**
Confirmed. Training-free, query-aware predictor for token significance during decoding. Key insight: differential frequencies within RoPE induce functional sparsity among frequency chunks; only "dominant FCs" contribute to contextual awareness. Achieves near-lossless performance with up to 2.56x speedup at 64K context. This is an attention/KV-cache-side optimization only.

**4. ThinKV: Thought-Adaptive KV Cache Compression (ICLR 2026 Oral)**
Confirmed. Decomposes chain-of-thought into distinct thought types by their attention sparsity, then applies hybrid quantization-eviction with per-thought-type precision. Achieves near-lossless accuracy with <5% of original KV cache and up to 5.8x throughput improvement. Tested on DeepSeek-R1-Distill, GPT-OSS, and NVIDIA AceReason. This is KV-cache-only but demonstrates that reasoning structure creates exploitable signals.

**5. SeerAttention-R (ICLR 2026)**
Confirmed. Microsoft Research. Sparse attention adaptation for long reasoning via self-distilled gating mechanism. Achieves near-lossless reasoning accuracy with 4K token budget and up to 9x speedup over FlashAttention-3 at 90% sparsity on H100. Attention-side optimization only.

**6. Polar Sparsity (NeurIPS 2025)**
Confirmed. This paper contains a critical insight: as batch size and sequence length grow, the importance of sparsity shifts from MLP layers to Attention layers. MLP sparsity vanishes under batching (union of active neurons approaches dense), while head-level sparsity remains stable and batch-invariant. Introduces Selective Head Attention with hardware-efficient GPU kernels, achieving 2.2x end-to-end speedups. This paper explicitly analyzes the interplay between MLP and attention sparsity, making it highly relevant as a competing/complementary observation, even though it ultimately focuses on attention sparsity for the scalable regime.

---

### Additional Papers Found That Coordinate Multiple Axes

**7. Q-Infer (ACM TACO, 2025)**
A GPU-CPU collaborative LLM inference system that coordinates both MLP neuron sparsity and KV cache compression. It uses a cross-layer MLP predictor that predicts activated neurons of the next layer during current-layer MLP computation, prefetching only Top-K neurons to GPU. Simultaneously, it dynamically selects key tokens via a multi-window mechanism, quantizing (not discarding) unimportant KV entries. This is arguably the closest competitor to "Cross-Axis Redundancy Coordination" -- it jointly manages both MLP activation sparsity and KV cache at the system level, though with separate mechanisms rather than a unified signal.

**8. ForesightKV (arXiv 2602.03203, Feb 2026)**
Training-based KV cache eviction framework that learns to predict which KV pairs to evict using future attention scores via a "Golden Eviction" algorithm. Focused on KV-cache side.

**9. LazyEviction (arXiv 2506.15969, June 2025)**
Discovers a "Token Importance Recurrence" phenomenon in reasoning tasks -- tokens periodically regain high attention after multiple decoding steps. Uses observation-window-based lagged eviction with recurrence interval tracking. Achieves 50-70% KV cache reduction on DeepSeek-R1. KV-cache only, but the recurrence signal could inform MLP sparsity decisions too.

**10. Self-Indexing KVCache (arXiv 2603.14224, March 2026)**
Jointly optimizes dynamic sparsity and quantization by recognizing that sparsity prediction in attention is essentially a top-k retrieval problem based on cosine similarity. Operates in the compressed domain directly.

**11. SparKV (arXiv 2604.21231, April 2026)**
Uses a lightweight MLP predictor that estimates per-chunk computation latency from attention sparsity features for overhead-aware KV cache loading on-device.

---

### Key Findings for "Cross-Axis Redundancy Coordination"

**Papers that genuinely coordinate across MLP and KV cache axes simultaneously:**

1. **QuickSilver** is the strongest competitor. It uses a shared token-level signal (representation convergence / L2 drift) to drive decisions across multiple axes: halting MLP computation, skipping KV writes, and fusing tokens. However, the coordination is token-centric rather than based on a unified redundancy signal across architectural components.

2. **Q-Infer** jointly manages MLP neuron activation sparsity (via cross-layer predictors) and KV cache (via multi-window token selection + quantization), but uses separate mechanisms for each axis rather than a coordinated signal.

3. **Polar Sparsity** provides the crucial empirical observation that MLP and attention sparsity behave differently under scaling (MLP sparsity vanishes in batched settings while attention head sparsity remains stable). Any "Cross-Axis" coordination framework must account for this asymmetry.

**Gap that "Cross-Axis Redundancy Coordination" could fill:**

None of the papers found use a truly unified redundancy signal that simultaneously informs both MLP sparsity and KV cache eviction/compression decisions. QuickSilver comes closest with its token-level convergence metric, but it treats the mechanisms as independently stackable ("orthogonal inefficiencies") rather than finding synergistic coordination where MLP sparsity patterns directly inform KV cache decisions and vice versa. The Polar Sparsity observation about the MLP-vs-attention sparsity shift under batching is a challenge that a coordinated approach would need to address.

---

Sources:
- [QuickSilver (arXiv 2506.22396)](https://arxiv.org/abs/2506.22396)
- [EvoSparse - ACL 2026](https://github.com/iLearn-Lab/ACL26-EvoSparse)
- [FASA: Frequency-Aware Sparse Attention (arXiv 2602.03152)](https://arxiv.org/abs/2602.03152)
- [ThinKV: Thought-Adaptive KV Cache Compression - ICLR 2026 Oral](https://arxiv.org/abs/2510.01290)
- [SeerAttention-R - ICLR 2026](https://arxiv.org/abs/2506.08889)
- [Polar Sparsity - NeurIPS 2025](https://arxiv.org/abs/2505.14884)
- [Q-Infer - ACM TACO](https://dl.acm.org/doi/full/10.1145/3764589)
- [ForesightKV (arXiv 2602.03203)](https://arxiv.org/abs/2602.03203)
- [LazyEviction (arXiv 2506.15969)](https://arxiv.org/abs/2506.15969)
- [Self-Indexing KVCache (arXiv 2603.14224)](https://arxiv.org/html/2603.14224v1)
- [SparKV (arXiv 2604.21231)](https://arxiv.org/html/2604.21231v1)
- [KV Cache Compression Survey (arXiv 2412.19442)](https://arxiv.org/html/2412.19442v3)
- [SqueezeAttention - OpenReview](https://openreview.net/forum?id=9HK2rHNAhd)
- [Top 10 KV Cache Compression Techniques - MarkTechPost](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)

agentId: a64b1f256f627b938 (use SendMessage with to: 'a64b1f256f627b938' to continue this agent)
&lt;usage>total_tokens: 29335
tool_uses: 17
duration_ms: 108786&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11afa0ba-bc03-4021-bc6c-f46e4a4b8a4c",
  "isSidechain": false,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "type": "user",
  "uuid": "93a86db1-9689-4e7c-80d0-855ca28817d2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for recent papers (2025-2026) that combine multiple efficiency axes for LLM inference — specifically papers that jointly optimize MLP sparsity AND KV cache compression/eviction during inference. I want to find competing work that the idea \"Cross-Axis Redundancy Coordination\" might have missed.\n\nSearch queries to use:\n1. \"joint MLP sparsity KV cache compression LLM inference 2025 2026\"\n2. \"multi-axis efficiency LLM reasoning inference\"\n3. \"unified signal MLP KV cache optimization\"\n4. \"cross-layer sparsity KV eviction reasoning models\"\n5. \"QuickSilver LLM inference token halting\" — verify this paper exists\n6. \"EvoSparse evolving sparsity token importance ACL 2026\"\n7. \"FASA frequency-aware sparse attention ICLR 2026\"\n8. \"ThinKV thought-adaptive KV cache compression ICLR 2026\"\n9. \"SeerAttention-R sparse attention reasoning ICLR 2026\"\n10. \"Polar Sparsity batched LLM inference NeurIPS 2025\"\n\nUse WebSearch for each. Report what you find — especially any paper that coordinates savings across both MLP and KV cache axes simultaneously.",
    "agentId": "a64b1f256f627b938",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my comprehensive report on the search findings.\n\n---\n\n## Results Summary\n\n### Papers Verified as Real\n\nAll 6 specific papers you asked about exist and are confirmed:\n\n**1. QuickSilver (arXiv 2506.22396, June 2025)**\nThis is the most directly relevant paper to the \"Cross-Axis Redundancy Coordination\" concept. QuickSilver integrates four synergistic mechanisms in a single framework operating on frozen dense models: (i) Dynamic Token Halting (halts computation for tokens with converged representations via L2 drift), (ii) KV Cache Skipping (selectively suppresses memory writes for inactive tokens), (iii) Contextual Token Fusion (merges redundant tokens to shrink sequence length), and (iv) Adaptive Matryoshka Quantization. It achieves up to 39.6% FLOP reduction with <=0.2 perplexity degradation on GPT-2 and Llama-2. The authors explicitly describe these as targeting \"orthogonal inefficiencies\" that can be stacked. This is a genuine multi-axis coordination paper, though it focuses on token-level signals rather than explicitly coordinating MLP sparsity with KV cache compression.\n\n**2. EvoSparse (ACL 2026 main)**\nConfirmed. \"Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention.\" Uses cross-step accumulation of token importance signals and retrieval head indices to guide non-retrieval heads across layers. Focus is on sparse attention (KV cache side) rather than MLP sparsity. Authors from Harbin Institute of Technology and Great Bay University. Code available at `github.com/iLearn-Lab/ACL26-EvoSparse`.\n\n**3. FASA: Frequency-Aware Sparse Attention (ICLR 2026)**\nConfirmed. Training-free, query-aware predictor for token significance during decoding. Key insight: differential frequencies within RoPE induce functional sparsity among frequency chunks; only \"dominant FCs\" contribute to contextual awareness. Achieves near-lossless performance with up to 2.56x speedup at 64K context. This is an attention/KV-cache-side optimization only.\n\n**4. ThinKV: Thought-Adaptive KV Cache Compression (ICLR 2026 Oral)**\nConfirmed. Decomposes chain-of-thought into distinct thought types by their attention sparsity, then applies hybrid quantization-eviction with per-thought-type precision. Achieves near-lossless accuracy with <5% of original KV cache and up to 5.8x throughput improvement. Tested on DeepSeek-R1-Distill, GPT-OSS, and NVIDIA AceReason. This is KV-cache-only but demonstrates that reasoning structure creates exploitable signals.\n\n**5. SeerAttention-R (ICLR 2026)**\nConfirmed. Microsoft Research. Sparse attention adaptation for long reasoning via self-distilled gating mechanism. Achieves near-lossless reasoning accuracy with 4K token budget and up to 9x speedup over FlashAttention-3 at 90% sparsity on H100. Attention-side optimization only.\n\n**6. Polar Sparsity (NeurIPS 2025)**\nConfirmed. This paper contains a critical insight: as batch size and sequence length grow, the importance of sparsity shifts from MLP layers to Attention layers. MLP sparsity vanishes under batching (union of active neurons approaches dense), while head-level sparsity remains stable and batch-invariant. Introduces Selective Head Attention with hardware-efficient GPU kernels, achieving 2.2x end-to-end speedups. This paper explicitly analyzes the interplay between MLP and attention sparsity, making it highly relevant as a competing/complementary observation, even though it ultimately focuses on attention sparsity for the scalable regime.\n\n---\n\n### Additional Papers Found That Coordinate Multiple Axes\n\n**7. Q-Infer (ACM TACO, 2025)**\nA GPU-CPU collaborative LLM inference system that coordinates both MLP neuron sparsity and KV cache compression. It uses a cross-layer MLP predictor that predicts activated neurons of the next layer during current-layer MLP computation, prefetching only Top-K neurons to GPU. Simultaneously, it dynamically selects key tokens via a multi-window mechanism, quantizing (not discarding) unimportant KV entries. This is arguably the closest competitor to \"Cross-Axis Redundancy Coordination\" -- it jointly manages both MLP activation sparsity and KV cache at the system level, though with separate mechanisms rather than a unified signal.\n\n**8. ForesightKV (arXiv 2602.03203, Feb 2026)**\nTraining-based KV cache eviction framework that learns to predict which KV pairs to evict using future attention scores via a \"Golden Eviction\" algorithm. Focused on KV-cache side.\n\n**9. LazyEviction (arXiv 2506.15969, June 2025)**\nDiscovers a \"Token Importance Recurrence\" phenomenon in reasoning tasks -- tokens periodically regain high attention after multiple decoding steps. Uses observation-window-based lagged eviction with recurrence interval tracking. Achieves 50-70% KV cache reduction on DeepSeek-R1. KV-cache only, but the recurrence signal could inform MLP sparsity decisions too.\n\n**10. Self-Indexing KVCache (arXiv 2603.14224, March 2026)**\nJointly optimizes dynamic sparsity and quantization by recognizing that sparsity prediction in attention is essentially a top-k retrieval problem based on cosine similarity. Operates in the compressed domain directly.\n\n**11. SparKV (arXiv 2604.21231, April 2026)**\nUses a lightweight MLP predictor that estimates per-chunk computation latency from attention sparsity features for overhead-aware KV cache loading on-device.\n\n---\n\n### Key Findings for \"Cross-Axis Redundancy Coordination\"\n\n**Papers that genuinely coordinate across MLP and KV cache axes simultaneously:**\n\n1. **QuickSilver** is the strongest competitor. It uses a shared token-level signal (representation convergence / L2 drift) to drive decisions across multiple axes: halting MLP computation, skipping KV writes, and fusing tokens. However, the coordination is token-centric rather than based on a unified redundancy signal across architectural components.\n\n2. **Q-Infer** jointly manages MLP neuron activation sparsity (via cross-layer predictors) and KV cache (via multi-window token selection + quantization), but uses separate mechanisms for each axis rather than a coordinated signal.\n\n3. **Polar Sparsity** provides the crucial empirical observation that MLP and attention sparsity behave differently under scaling (MLP sparsity vanishes in batched settings while attention head sparsity remains stable). Any \"Cross-Axis\" coordination framework must account for this asymmetry.\n\n**Gap that \"Cross-Axis Redundancy Coordination\" could fill:**\n\nNone of the papers found use a truly unified redundancy signal that simultaneously informs both MLP sparsity and KV cache eviction/compression decisions. QuickSilver comes closest with its token-level convergence metric, but it treats the mechanisms as independently stackable (\"orthogonal inefficiencies\") rather than finding synergistic coordination where MLP sparsity patterns directly inform KV cache decisions and vice versa. The Polar Sparsity observation about the MLP-vs-attention sparsity shift under batching is a challenge that a coordinated approach would need to address.\n\n---\n\nSources:\n- [QuickSilver (arXiv 2506.22396)](https://arxiv.org/abs/2506.22396)\n- [EvoSparse - ACL 2026](https://github.com/iLearn-Lab/ACL26-EvoSparse)\n- [FASA: Frequency-Aware Sparse Attention (arXiv 2602.03152)](https://arxiv.org/abs/2602.03152)\n- [ThinKV: Thought-Adaptive KV Cache Compression - ICLR 2026 Oral](https://arxiv.org/abs/2510.01290)\n- [SeerAttention-R - ICLR 2026](https://arxiv.org/abs/2506.08889)\n- [Polar Sparsity - NeurIPS 2025](https://arxiv.org/abs/2505.14884)\n- [Q-Infer - ACM TACO](https://dl.acm.org/doi/full/10.1145/3764589)\n- [ForesightKV (arXiv 2602.03203)](https://arxiv.org/abs/2602.03203)\n- [LazyEviction (arXiv 2506.15969)](https://arxiv.org/abs/2506.15969)\n- [Self-Indexing KVCache (arXiv 2603.14224)](https://arxiv.org/html/2603.14224v1)\n- [SparKV (arXiv 2604.21231)](https://arxiv.org/html/2604.21231v1)\n- [KV Cache Compression Survey (arXiv 2412.19442)](https://arxiv.org/html/2412.19442v3)\n- [SqueezeAttention - OpenReview](https://openreview.net/forum?id=9HK2rHNAhd)\n- [Top 10 KV Cache Compression Techniques - MarkTechPost](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)"
      }
    ],
    "totalDurationMs": 108786,
    "totalTokens": 29335,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3068,
      "cache_read_input_tokens": 23894,
      "output_tokens": 2372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3068
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2372,
          "cache_read_input_tokens": 23894,
          "cache_creation_input_tokens": 3068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3068,
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
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "11afa0ba-bc03-4021-bc6c-f46e4a4b8a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "93a86db1-9689-4e7c-80d0-855ca28817d2",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify redundancy-coordination efficiency method for EMNLP",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

### Tool result

_source line 23 · 2026-05-10T18:18:31.196Z_

<details><summary>↩ Tool result · `toolu_01YYkQ6D7WauBiTHWu5kTJm5`</summary>

```text
I now have comprehensive information on both papers. Here is my full report.

---

## Paper 1: R-KV: Redundancy-aware KV Cache Compression for Reasoning Models

**Existence:** Confirmed. arXiv ID: [2505.24133](https://arxiv.org/abs/2505.24133). Authors led by Zefan Cai.

**Venue:** Confirmed NeurIPS 2025 (poster). This is verified via [OpenReview](https://openreview.net/forum?id=2jwAjomEDB) (published 18 Sept 2025) and the [GitHub repository](https://github.com/Zefan-Cai/R-KV) which is titled "[NeurIPS 2025] R-KV."

**Approach:** R-KV has three components:
1. An attention-based importance scoring mechanism that selects critical tokens for retention.
2. A dynamic redundancy scoring mechanism that identifies repetitive tokens through real-time analysis of key vectors.
3. A joint eviction mechanism that balances redundancy and importance for cache optimization.

**Does it use O(B^2) pairwise key similarity for periodic eviction?** Yes to both parts:
- **O(B^2) pairwise similarity:** The paper explicitly states the redundancy estimation has complexity O(B_budget^2). It computes a cosine similarity matrix S^h over all key tokens in the budget, which is a pairwise operation.
- **Periodic eviction:** Confirmed. R-KV performs KV cache compression after the model generates each fixed-length text segment in the buffer. The default interval is every 128 decoding steps (B_buffer = 128).

**KV memory savings:**
- 90% memory saving reported (retaining only ~10% of the KV cache).
- At 10% KV cache budget, preserves nearly 100% of full-cache performance.
- At 16% KV cache budget, achieves 105% of full-cache accuracy (on AIME-24 with DeepSeek-R1-Distill-Llama-8B).
- 6.6x throughput improvement over standard chain-of-thought inference.
- Up to 13.4x larger batch sizes with 16K sequences.

---

## Paper 2: TEAL: Training-Free Activation Sparsity in Large Language Models

**Existence:** Confirmed. arXiv ID: [2408.14690](https://arxiv.org/abs/2408.14690).

**Venue:** Confirmed ICLR 2025 Spotlight. The arXiv page states "Rev. 2: ICLR 2025 Acceptance (Spotlight)" and the paper appears in the [ICLR 2025 proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf).

**Does it achieve 40-50% MLP activation sparsity with 1.5-1.8x decoding speedup?** Partially accurate but imprecise in scope. TEAL achieves 40-50% **model-wide** sparsity (not just MLP), applied to all hidden states throughout the entire model including attention projections (W_q, W_k, W_v, W_o) and all MLP components. The speedup numbers are accurate: **1.53x at 40% sparsity** and **1.8x at 50% sparsity**.

**Does it use magnitude pruning with fixed per-layer thresholds?** Partially correct:
- **Magnitude pruning:** Yes. Activations where |x_i| <= t_p are set to zero.
- **Per-layer thresholds:** Yes, thresholds are determined per-layer (and actually per-matrix -- there are seven matrices per block). However, calling them "fixed" is somewhat misleading. They are **calibrated offline** using an empirical distribution from generic text (C4 data), then remain constant during inference. So they are fixed at inference time, but not arbitrary -- they are calibrated per-layer/per-matrix to match a target sparsity level. Additionally, a greedy optimization algorithm (Section 4.3) finds individual sparsity levels for each matrix.

**Is there a documented performance cliff at 65% sparsity for SwiGLU architectures?** Yes, this is documented in the paper. Table 1 shows significant degradation at 65% sparsity:
- Llama-3-8B perplexity jumps from 5.87 (baseline) to 9.06 at 65% sparsity.
- Llama-2-7B perplexity rises from 5.07 to 6.62.
- The paper explicitly states: "Most models degrade significantly at 65% sparsity, with the exception of Llama-2-70B which is still reasonably performant."
- The paper confirms it targets modern LLMs that use SwiGLU rather than ReLU-based feedforward layers. However, the degradation is documented as a general finding across models rather than being framed specifically as a "SwiGLU-specific" cliff -- it is simply the behavior observed on modern SwiGLU-based models (Llama-2, Llama-3, Mistral).

---

## Summary of Claim Verification

| Claim | Verdict |
|---|---|
| R-KV exists and is at NeurIPS 2025 | **Confirmed** (poster) |
| R-KV uses O(B^2) pairwise key similarity | **Confirmed** |
| R-KV uses periodic eviction | **Confirmed** (every 128 steps) |
| R-KV achieves 90% KV memory savings | **Confirmed** |
| TEAL exists and is ICLR 2025 Spotlight | **Confirmed** |
| TEAL achieves 40-50% sparsity with 1.5-1.8x speedup | **Confirmed**, but sparsity is model-wide, not MLP-only |
| TEAL uses magnitude pruning with fixed per-layer thresholds | **Mostly confirmed** -- calibrated per-matrix, fixed at inference |
| Performance cliff at 65% sparsity for SwiGLU | **Confirmed** in Table 1, though documented as general finding on SwiGLU-based models |

Sources:
- [R-KV arXiv page](https://arxiv.org/abs/2505.24133)
- [R-KV full HTML paper](https://arxiv.org/html/2505.24133)
- [R-KV GitHub repository](https://github.com/Zefan-Cai/R-KV)
- [R-KV OpenReview](https://openreview.net/forum?id=2jwAjomEDB)
- [TEAL arXiv page](https://arxiv.org/abs/2408.14690)
- [TEAL full HTML paper](https://arxiv.org/html/2408.14690v1)
- [TEAL ICLR 2025 proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf)
- [TEAL OpenReview](https://openreview.net/forum?id=dGVZwyq5tV)
- [TEAL Together AI blog](https://www.together.ai/blog/teal-training-free-activation-sparsity-in-large-language-models)

agentId: a6855bcaa013c18e0 (use SendMessage with to: 'a6855bcaa013c18e0' to continue this agent)
&lt;usage>total_tokens: 21517
tool_uses: 13
duration_ms: 129124&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45268ce4-a575-423c-9f95-d3e5e271ae6d",
  "isSidechain": false,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "type": "user",
  "uuid": "07653e65-b8a1-4513-85ca-0da0f538fa36",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify these two papers:\n\n1. \"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models\" — claimed to be at NeurIPS 2025. Does it exist? What is its approach? Does it use O(B²) pairwise key similarity for periodic eviction? What KV memory savings does it achieve?\n\n2. \"TEAL: Training-Free Activation Sparsity in Large Language Models\" — claimed to be ICLR 2025 Spotlight. Does it exist? Does it achieve 40-50% MLP activation sparsity with 1.5-1.8× decoding speedup? Does it use magnitude pruning with fixed per-layer thresholds? Is there a documented performance cliff at 65% sparsity for SwiGLU architectures?\n\nUse WebSearch and WebFetch. Search for exact titles and arXiv IDs. Report all details found.",
    "agentId": "a6855bcaa013c18e0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on both papers. Here is my full report.\n\n---\n\n## Paper 1: R-KV: Redundancy-aware KV Cache Compression for Reasoning Models\n\n**Existence:** Confirmed. arXiv ID: [2505.24133](https://arxiv.org/abs/2505.24133). Authors led by Zefan Cai.\n\n**Venue:** Confirmed NeurIPS 2025 (poster). This is verified via [OpenReview](https://openreview.net/forum?id=2jwAjomEDB) (published 18 Sept 2025) and the [GitHub repository](https://github.com/Zefan-Cai/R-KV) which is titled \"[NeurIPS 2025] R-KV.\"\n\n**Approach:** R-KV has three components:\n1. An attention-based importance scoring mechanism that selects critical tokens for retention.\n2. A dynamic redundancy scoring mechanism that identifies repetitive tokens through real-time analysis of key vectors.\n3. A joint eviction mechanism that balances redundancy and importance for cache optimization.\n\n**Does it use O(B^2) pairwise key similarity for periodic eviction?** Yes to both parts:\n- **O(B^2) pairwise similarity:** The paper explicitly states the redundancy estimation has complexity O(B_budget^2). It computes a cosine similarity matrix S^h over all key tokens in the budget, which is a pairwise operation.\n- **Periodic eviction:** Confirmed. R-KV performs KV cache compression after the model generates each fixed-length text segment in the buffer. The default interval is every 128 decoding steps (B_buffer = 128).\n\n**KV memory savings:**\n- 90% memory saving reported (retaining only ~10% of the KV cache).\n- At 10% KV cache budget, preserves nearly 100% of full-cache performance.\n- At 16% KV cache budget, achieves 105% of full-cache accuracy (on AIME-24 with DeepSeek-R1-Distill-Llama-8B).\n- 6.6x throughput improvement over standard chain-of-thought inference.\n- Up to 13.4x larger batch sizes with 16K sequences.\n\n---\n\n## Paper 2: TEAL: Training-Free Activation Sparsity in Large Language Models\n\n**Existence:** Confirmed. arXiv ID: [2408.14690](https://arxiv.org/abs/2408.14690).\n\n**Venue:** Confirmed ICLR 2025 Spotlight. The arXiv page states \"Rev. 2: ICLR 2025 Acceptance (Spotlight)\" and the paper appears in the [ICLR 2025 proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf).\n\n**Does it achieve 40-50% MLP activation sparsity with 1.5-1.8x decoding speedup?** Partially accurate but imprecise in scope. TEAL achieves 40-50% **model-wide** sparsity (not just MLP), applied to all hidden states throughout the entire model including attention projections (W_q, W_k, W_v, W_o) and all MLP components. The speedup numbers are accurate: **1.53x at 40% sparsity** and **1.8x at 50% sparsity**.\n\n**Does it use magnitude pruning with fixed per-layer thresholds?** Partially correct:\n- **Magnitude pruning:** Yes. Activations where |x_i| <= t_p are set to zero.\n- **Per-layer thresholds:** Yes, thresholds are determined per-layer (and actually per-matrix -- there are seven matrices per block). However, calling them \"fixed\" is somewhat misleading. They are **calibrated offline** using an empirical distribution from generic text (C4 data), then remain constant during inference. So they are fixed at inference time, but not arbitrary -- they are calibrated per-layer/per-matrix to match a target sparsity level. Additionally, a greedy optimization algorithm (Section 4.3) finds individual sparsity levels for each matrix.\n\n**Is there a documented performance cliff at 65% sparsity for SwiGLU architectures?** Yes, this is documented in the paper. Table 1 shows significant degradation at 65% sparsity:\n- Llama-3-8B perplexity jumps from 5.87 (baseline) to 9.06 at 65% sparsity.\n- Llama-2-7B perplexity rises from 5.07 to 6.62.\n- The paper explicitly states: \"Most models degrade significantly at 65% sparsity, with the exception of Llama-2-70B which is still reasonably performant.\"\n- The paper confirms it targets modern LLMs that use SwiGLU rather than ReLU-based feedforward layers. However, the degradation is documented as a general finding across models rather than being framed specifically as a \"SwiGLU-specific\" cliff -- it is simply the behavior observed on modern SwiGLU-based models (Llama-2, Llama-3, Mistral).\n\n---\n\n## Summary of Claim Verification\n\n| Claim | Verdict |\n|---|---|\n| R-KV exists and is at NeurIPS 2025 | **Confirmed** (poster) |\n| R-KV uses O(B^2) pairwise key similarity | **Confirmed** |\n| R-KV uses periodic eviction | **Confirmed** (every 128 steps) |\n| R-KV achieves 90% KV memory savings | **Confirmed** |\n| TEAL exists and is ICLR 2025 Spotlight | **Confirmed** |\n| TEAL achieves 40-50% sparsity with 1.5-1.8x speedup | **Confirmed**, but sparsity is model-wide, not MLP-only |\n| TEAL uses magnitude pruning with fixed per-layer thresholds | **Mostly confirmed** -- calibrated per-matrix, fixed at inference |\n| Performance cliff at 65% sparsity for SwiGLU | **Confirmed** in Table 1, though documented as general finding on SwiGLU-based models |\n\nSources:\n- [R-KV arXiv page](https://arxiv.org/abs/2505.24133)\n- [R-KV full HTML paper](https://arxiv.org/html/2505.24133)\n- [R-KV GitHub repository](https://github.com/Zefan-Cai/R-KV)\n- [R-KV OpenReview](https://openreview.net/forum?id=2jwAjomEDB)\n- [TEAL arXiv page](https://arxiv.org/abs/2408.14690)\n- [TEAL full HTML paper](https://arxiv.org/html/2408.14690v1)\n- [TEAL ICLR 2025 proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf)\n- [TEAL OpenReview](https://openreview.net/forum?id=dGVZwyq5tV)\n- [TEAL Together AI blog](https://www.together.ai/blog/teal-training-free-activation-sparsity-in-large-language-models)"
      }
    ],
    "totalDurationMs": 129124,
    "totalTokens": 21517,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 19043,
      "output_tokens": 1851,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 622
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1851,
          "cache_read_input_tokens": 19043,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 622,
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
  "sourceToolAssistantUUID": "45268ce4-a575-423c-9f95-d3e5e271ae6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T18:21:21.006Z_

<details><summary>Logged reasoning block</summary>

```text
Good, now I have extensive information. Let me summarize what I've learned:

## Token Filtering (arXiv:2512.07090)
- **EXISTS**: Yes, confirmed
- **EMA centroid signal**: Confirmed — uses EMA anchors for keys and values
- **Variance-aware fusion (Eq 2-3)**: Confirmed
- **Uses for**: Attention layer skipping ONLY — no MLP sparsity, no KV eviction
- **Speedups**: Up to 46.6% latency reduction, ~87% throughput improvement at batch=128


## R-KV (NeurIPS 2025)
- **EXISTS**: Confirmed at NeurIPS 2025 (poster)
- **O(B²) pairwise similarity**: Confirmed (O(B_budget²))
- **Periodic eviction**: Confirmed (every 128 steps)
- **90% memory savings**: Confirmed

## TEAL (ICLR 2025 Spotlight)
- **EXISTS**: Confirmed
- **40-50% sparsity with 1.5-1.8× speedup**: Confirmed, but sparsity is model-wide, not MLP-only
- **Magnitude pruning with**

Now I'm verifying the per-layer threshold approach — it's calibrated offline using per-matrix thresholds, and the 65% performance cliff is documented in their results table.

## EMA Is Not All You Need (arXiv:2604.08556)
- **EXISTS**: Confirmed
- **EMA information dilution**: Confirmed — shows irreversible information dilution

## KeyDiff (arXiv:2504.15364)
- **EXISTS**: Confirmed
- **Mean-of-keys (not EMA)**: Confirmed

## CSAttention (arXiv:2604.08584)
- **EXISTS**: Confirmed
- **Query-centric lookup tables**: Confirmed

## Competing work
Looking at QuickSilver as the main competitor — it combines four different mechanisms (token halting, KV skipping, token fusion, and quantization) coordinated through an L2 drift signal, though each mechanism operates independently rather than on a unified axis.

Q-Infer handles MLP neuron sparsity and KV cache compression jointly but with separate mechanisms, while Polar Sparsity's MLP sparsity approach breaks down under batching conditions.

The EMNLP 2026 deadline is May 25, 2026 for ARR submissions. Now I need to search for any recent concurrent work that combines EMA similarity with MLP sparsity, whether the windowed reset mechanism in CARC has prior art, and if there are papers extending Token Filtering's signal since its publication.

The key novelty question comes down to whether extending Token Filtering's EMA signal to simultaneously drive both MLP sparsity and KV cache eviction as a unified mechanism is genuinely novel.

Token Filtering only handles attention layer skipping, while CARC applies the same signal to two-tier MLP sparsity and KV cache eviction. QuickSilver already coordinates multiple optimization axes using L2 drift as its signal, whereas CARC uses EMA centroid similarity instead. The windowed reset mechanism offers a modest but genuine enhancement to the EMA signal itself. This feels like a system integration paper where the novelty lies in connecting Token Filtering's redundancy detection to activation sparsity and applying the same signal across multiple optimization dimensions.

The timeline is feasible since the approach avoids kernel modifications and reuses existing thresholds and eviction strategies with different triggers. The main challenge is integrating three separate codebases, though the target models are all open-weight and accessible. TEAL applies model-wide sparsity, which raises questions about how the approach handles...

Actually, I need to reconsider the independence claim here. TEAL's sparsity covers all hidden states including attention projections, not just MLPs, so the two-tier routing might not target as cleanly separated bottlenecks as proposed. And while MLP is compute-bound and attention is memory-bound during batch=1 decode, KV eviction also reduces attention FLOPs, creating some overlap in the performance gains. The windowed reset adds complexity with additional hyperparameters to sweep—W and τ_reset—which expands the search space.

The EMA dilution issue is a real concern from prior work, and the windowed reset is a reasonable mitigation, though it feels somewhat ad-hoc. The proposal does include an ablation comparing EMA against a sliding-window mean, which is good practice. Now I'm trying to figure out whether I should dig deeper into the experimental validation.

Actually, I need to verify whether the two-tier TEAL threshold approach is actually feasible. The core question is whether you can really split tokens into redundant and novel groups and apply different thresholds without modifying the kernel. The proposal suggests batching tokens separately and running TEAL twice per layer, which would work but introduces overhead from multiple kernel launches. That's a practical trade-off worth noting.

But wait — at batch size 1, which is typical for inference, this becomes trivial. Each token is processed individually, so the signal S just determines whether to use a 40% or 50-55% sparsity threshold for that single token. You're just changing the threshold value passed to the kernel, no batching or routing needed at all. That's actually clean and simple.

Now I'm thinking through what issues I should raise in my assessment, starting with the positive changes from the latest round: the Token Filtering citation is now correct, the windowed reset mechanism properly addresses EMA stability concerns, and the MLP sparsity has been adjusted downward.

Looking at the remaining concerns though, the core novelty feels moderate — it's essentially applying Token Filtering's EMA signal to modulate TEAL thresholds and trigger KV eviction, with a windowed reset as a minor refinement. That's solid work for EMNLP Findings, but probably not strong enough for the main conference track. And QuickSilver from 2025 already shows multi-axis coordination across token halting, KV skipping, and token fusion, which makes the positioning trickier.

The differentiation against QuickSilver needs sharpening too — they use L2 drift to capture representation convergence while CARC uses KV similarity for content redundancy, which are complementary but the paper should make that distinction clearer. There's also a characterization issue where TEAL is framed as MLP-specific sparsity when it actually applies across all hidden states. The two-tier sparsity split (50-55% for redundant tokens versus 40% for novel ones) only gives a 10-15 percentage point margin, so the actual quality improvement over a uniform 45% baseline might be marginal — the planned ablation will help validate that. And I need to ensure the resource cost accounting stays consistent throughout. mode has 100h H100 at ~25% utilization, which seems like only 25 actual GPU hours of computation but 100h of wall-clock allocation. Auto mode has 250h at ~90% utilization, which is 225h of actual compute. The ratio seems inconsistent — why does auto need 9× more actual compute than manual? Because of the hyperparameter grid (27 configs × 3 models × multiple benchmarks).

Actually, let me reconsider. The proposal is:
- Manual: 100h H100 total (25% utilization = researcher is only using 25h effectively)
- Auto: 250h H100 total (90% utilization = 225h effective)

The auto mode runs a much larger sweep. Manual mode probably does targeted experiments. This seems reasonable.

6. **The "additive speedup" claim**: The proposal claims MLP sparsity and KV eviction provide additive speedups because they target independent bottlenecks. At batch=1 decode, MLP forward is compute-bound with high arithmetic intensity while attention forward is memory-bound with low arithmetic intensity dominated by KV cache reads. These are indeed independent bottlenecks in the roofline model, so reducing MLP compute and reducing KV attention memory access should compose roughly additively in wall-clock time. That's a solid argument.

7. **Timeline**: 14-16 days is tight, but the proposal leverages existing codebases (Token Filtering, TEAL, R-KV) and the main work involves integrating EMA signal computation, adding threshold routing for batch=1 scenarios, interfacing with R-KV's eviction logic for the KV eviction trigger, implementing a windowed reset mechanism, and running benchmarks across 2-3 models and 6+ benchmarks. Most of these are straightforward integrations rather than novel implementations.

Now I need to write the paper itself. This is ambitious but feasible for an experienced researcher — the main risk is how long the benchmark evaluation actually takes.

Looking at the overall assessment, the proposal has genuinely improved from earlier rounds. The core technical issues have been resolved: Token Filtering is properly cited, sparsity levels are justified, benchmark coverage is comprehensive, EMNLP 2026 is the right target, and limitations are honestly stated. What remains are questions about novelty depth and some minor characterization issues.

For scoring, novelty is probably 3/5 — the contribution is real but incremental, extending an existing signal to two additional axes with a modest windowed reset enhancement. QuickSilver already demonstrates multi-axis coordination with a different signal. This is solid for EMNLP Findings but might be borderline for the main conference.

The compute allocation makes sense once I account for the hyperparameter sweep scale — auto mode needs 9× more actual compute because it's exploring 27 configurations across multiple models and benchmarks, while manual mode does targeted experiments. The additive speedup claim holds up because MLP and attention target independent roofline bottlenecks at batch=1 decode. The timeline is tight but realistic given the existing codebases and straightforward integration work required.

Before I finalize my assessment, I should double-check a couple of things about the experimental design and whether there's additional novelty I might have missed.

Looking back at TEAL's actual mechanism more carefully—it applies sparsity across all weight matrices in both attention and MLP layers, not just the MLP forward pass as the paper frames it. The proposal's characterization of TEAL as primarily magnitude-pruning with a fixed threshold seems to oversimplify how TEAL actually works, which affects how much the combined approach truly differentiates itself. I'm settling on the key criticisms for my review: the novelty feels incremental over Token Filtering, the QuickSilver baseline needs stronger evaluation, and there's ambiguity about whether TEAL applies model-wide or just to MLPs. The practical speedup gains from two-tier sparsity versus uniform sparsity might also be marginal. I'm also noticing Q-Infer from ACM TACO 2025 is a significant missing reference—it jointly optimizes MLP sparsity and KV cache compression, which directly overlaps with what this proposal is doing, so that's a notable gap in the related work.

The proposal claims no prior work uses a unified per-token signal to coordinate both compute-bound and memory-bound bottlenecks, and technically Q-Infer uses separate mechanisms rather than a single coordinating signal, so the claim might hold. But Q-Infer should definitely be cited as the closest system-level coordination work. The real question I need to dig into is whether the cross-axis coordination actually delivers meaningful additional speedup—if TEAL alone gives 1.5× and KV eviction alone gives 1.3×, does combining them actually reach something like 1.8× or does it plateau closer to 1.5×?

Overall this feels like a solid paper with clear writing and honest limitations. For EMNLP Findings it's a good fit, though for the main conference the novelty might fall short. The novelty is incremental—extending an existing signal to new axes—and while the windowed reset mechanism is reasonable, it's not particularly deep. Feasibility looks strong since it's training-free and uses existing kernels. The clarity is good throughout with proper citations and transparent about limitations.

Scoring it out: novelty at 3/5, feasibility at 4/5, clarity at 4/5, and impact at 3/5 since the practical gains over individual methods need better demonstration. That averages to 3.5, which falls below the 4.0 pass threshold, so I'd recommend revision.

The main issues to address are differentiating from Q-Infer, strengthening the novelty claim by exploring whether there's a deeper insight about why KV similarity predicts MLP redundancy—maybe showing correlation between EMA similarity and activation magnitude distribution would help—quantifying the expected speedup breakdown between MLP and KV contributions, and clarifying whether TEAL applies model-wide or just to MLPs.

Let me reread the approach section more carefully to see if I'm missing something.

Ah, I see now—the routing mechanism is actually quite straightforward. At batch=1, you compute the similarity score S for the current token and decide whether to pass it to TEAL's magnitude-pruning kernel with a higher 50–55% sparsity threshold instead of the default 40%, staying safely below the documented 65% SwiGLU cliff. No kernel modifications needed, just a single control-flow branch.

And there's a key distinction with the KV cache eviction: R-KV does periodic scoring every 128 steps with O(B²) complexity, but CARC triggers per-token eviction using the similarity signal instead, which is O(1).

But wait—I'm realizing the actual eviction strategies are fundamentally different. R-KV identifies which cached tokens to remove based on their pairwise similarity to each other, whereas CARC decides whether to add the current token to the cache in the first place if it's classified as redundant. The proposal mentions "following R-KV's management strategy," but the mechanism is completely different—one is cache insertion filtering, the other is periodic eviction of existing entries. I need to clarify whether CARC is preventing redundant tokens from entering the cache at all, or if it's using the EMA signal to periodically evict tokens like R-KV does. it's different from R-KV's approach of curating the existing cache.
If (b), then how does the per-token EMA signal decide which existing cached tokens to evict? The EMA signal compares the CURRENT token to the centroid — it doesn't evaluate which cached tokens are mutually redundant.

I think the proposal means (a) — don't cache redundant tokens. But it says "following R-KV's management strategy" which implies (b). This is a clarity issue.

Hmm, actually re-reading again: "Tokens classified as redundant are evicted from the KV cache." This could mean either:
- Redundant tokens are not stored in the KV cache (insertion filtering)
- Redundant tokens that are already cached are removed

The first interpretation makes more sense with the per-token trigger. The second would require a different mechanism.

This is an ambiguity I should flag.

Now I'm questioning whether KV similarity is actually a reliable indicator of MLP activation sparsity. Token Filtering works well for attention because redundant tokens contribute little there, but that doesn't necessarily mean their hidden states will have sparse MLP activations — position encoding and residual stream contributions could make them quite different. The paper assumes redundant tokens can tolerate more aggressive MLP pruning without justifying why KV redundancy should correlate with activation patterns. This feels like a significant gap that needs empirical validation.

Let me finalize my assessment. Novelty is incremental — it's extending Token Filtering to additional dimensions, though QuickSilver and Q-Infer already explore multi-axis coordination differently. Feasibility looks reasonable on paper: training-free, uses existing kernels, accessible models, tight but doable timeline. The main risk is that unvalidated assumption about KV similarity predicting MLP sparsity could cause accuracy issues requiring redesign.

The proposal is well-structured with good citations and honest about limitations, though there's ambiguity around how KV eviction actually integrates and a missing Q-Infer reference. Impact is limited to batch=1 reasoning with unclear practical speedup — the efficiency gains stack to maybe 10% additional MLP savings plus KV savings, which feels modest.

This lands below the 4.0 threshold, so I'm leaning toward revise. Before I finalize feedback, I want to search for any existing work on the correlation between KV similarity and activation sparsity patterns, since that's the core assumption here.

I'm also realizing the insertion filtering angle is worth examining more carefully. KeyDiff and H2O both do KV eviction, but they evict periodically rather than filtering at insertion time. Token Filtering skips attention computation but still caches the KV for future use. If CARC doesn't cache redundant tokens at all, that's a real problem — future tokens lose the ability to attend to those positions, which could hurt accuracy on long sequences where early tokens become relevant again. That's a legitimate concern worth flagging.

Now I'm checking one more detail about TEAL's sparsity claims. TEAL prunes activations before each linear layer across attention projections and MLP layers. The proposal mentions elevating MLP sparsity for redundant tokens, which is technically feasible since TEAL uses per-matrix thresholds — you could apply default thresholds to attention matrices while using elevated thresholds for MLP matrices on redundant tokens. But the proposal doesn't spell out this level of implementation detail, just says "MLP sparsity."

Stepping back to assess the overall contribution for EMNLP: the core narrative is solid — redundant tokens exist, Token Filtering detects them, and applying that signal to both MLP sparsity and KV eviction targets independent bottlenecks with composable savings. For Findings, this is probably sufficient with the windowed reset mechanism as a technical contribution. For Main conference, I'd want stronger justification — why KV similarity predicts MLP redundancy, how it compares to QuickSilver's approach, formal analysis of when composition holds, and larger-scale validation. This feels borderline for a 2026 Main submission, though it could work with careful execution.

Now I'm settling on a "revise" verdict with specific, actionable feedback. The novelty and impact scores are moderate at 3/5 each, feasibility and clarity are stronger at 4/5, averaging 3.5 overall. The main gaps are missing references like Q-Infer that already handle joint MLP and KV optimization, no clear explanation for why KV similarity correlates with MLP sparsity opportunities, ambiguity around the KV eviction mechanism itself, and insufficient comparison with QuickSilver's drift-based signal. I should push the authors toward three concrete improvements: solidifying the cross-axis assumption with either theory or empirical evidence, clarifying the KV mechanism and its interaction with insertion filtering, and quantifying expected speedup composition rather than just claiming it's additive.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07653e65-b8a1-4513-85ca-0da0f538fa36",
  "isSidechain": false,
  "requestId": "req_011CauMAsi2eKB5y6tuBULXb",
  "type": "assistant",
  "uuid": "197e70c8-c1cd-49ab-b104-0afac76c98e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017iFRfWrHEVcvRdz3g6fM4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5474,
      "cache_creation_input_tokens": 5264,
      "cache_read_input_tokens": 27484,
      "output_tokens": 7501,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5474,
          "output_tokens": 7501,
          "cache_read_input_tokens": 27484,
          "cache_creation_input_tokens": 5264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5264
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

_source line 25 · 2026-05-10T18:21:21.008Z_

Now let me do a few more targeted searches to check for critical gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "197e70c8-c1cd-49ab-b104-0afac76c98e0",
  "isSidechain": false,
  "requestId": "req_011CauMAsi2eKB5y6tuBULXb",
  "type": "assistant",
  "uuid": "e8d15823-f180-414a-9072-db7aa8c4609a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017iFRfWrHEVcvRdz3g6fM4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5474,
      "cache_creation_input_tokens": 5264,
      "cache_read_input_tokens": 27484,
      "output_tokens": 7501,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5474,
          "output_tokens": 7501,
          "cache_read_input_tokens": 27484,
          "cache_creation_input_tokens": 5264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5264
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

_source line 26 · 2026-05-10T18:21:27.471Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0171KsMGXURabgxeiUvBP3UQ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search KV similarity MLP correlation",
  "prompt": "Search the web for papers or analysis studying whether KV cache similarity (key-value vector similarity between tokens) correlates with MLP activation sparsity or activation magnitude patterns in LLMs. I want to know if there's any evidence that tokens with similar keys also have more compressible/sparse MLP activations.\n\nSearch queries:\n1. \"KV similarity activation sparsity correlation LLM\"\n2. \"token redundancy MLP computation skip LLM inference\"\n3. \"key vector similarity predict activation magnitude transformer\"\n4. \"redundant token MLP sparsity reasoning LLM\"\n5. \"token importance MLP attention correlation transformer inference\"\n\nAlso search for papers on KV cache \"insertion filtering\" — methods that decide whether to add a token to the KV cache at the time of generation (as opposed to periodic eviction of cached entries):\n6. \"KV cache insertion filtering LLM inference\"\n7. \"selective KV cache storage token generation\"\n8. \"token importance recurrence KV eviction reasoning\"\n\nReport what you find. This is important for assessing whether a KV-similarity-based signal can validly drive MLP sparsity decisions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d15823-f180-414a-9072-db7aa8c4609a",
  "isSidechain": false,
  "requestId": "req_011CauMAsi2eKB5y6tuBULXb",
  "type": "assistant",
  "uuid": "64f9ea6e-c999-46fc-99b8-ae406097a7e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017iFRfWrHEVcvRdz3g6fM4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5474,
      "cache_creation_input_tokens": 5264,
      "cache_read_input_tokens": 27484,
      "output_tokens": 7501,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5474,
          "output_tokens": 7501,
          "cache_read_input_tokens": 27484,
          "cache_creation_input_tokens": 5264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5264
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

_source line 27 · 2026-05-10T18:21:32.527Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01X97aAgDZG1nBp3kSpvbWby`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search Q-Infer and multi-axis",
  "prompt": "Search for the paper \"Q-Infer\" which is described as a GPU-CPU collaborative LLM inference system that coordinates both MLP neuron sparsity and KV cache compression, published in ACM TACO 2025. Verify it exists and understand its approach.\n\nAlso search for any papers from 2025-2026 that specifically propose using a SINGLE signal to drive BOTH MLP sparsity and KV cache decisions:\n1. \"Q-Infer GPU CPU MLP sparsity KV cache ACM TACO\"\n2. \"unified signal MLP KV cache coordination LLM inference 2025 2026\"  \n3. \"single metric MLP sparsity KV eviction transformer\"\n4. \"cross-axis optimization MLP attention LLM inference\"\n5. \"joint compute memory optimization LLM decoding\"\n\nReport what you find — especially whether Q-Infer or any other paper uses a unified redundancy signal across both axes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64f9ea6e-c999-46fc-99b8-ae406097a7e3",
  "isSidechain": false,
  "requestId": "req_011CauMAsi2eKB5y6tuBULXb",
  "type": "assistant",
  "uuid": "a30e59b5-e03f-45b6-bb4a-68a59d6b7e56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017iFRfWrHEVcvRdz3g6fM4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5474,
      "cache_creation_input_tokens": 5264,
      "cache_read_input_tokens": 27484,
      "output_tokens": 7501,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5474,
          "output_tokens": 7501,
          "cache_read_input_tokens": 27484,
          "cache_creation_input_tokens": 5264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5264
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
  "leafUuid": "a30e59b5-e03f-45b6-bb4a-68a59d6b7e56",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify redundancy-coordination efficiency method for EMNLP",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

### Tool result

_source line 30 · 2026-05-10T18:23:24.914Z_

<details><summary>↩ Tool result · `toolu_01X97aAgDZG1nBp3kSpvbWby`</summary>

```text
Now I have a comprehensive picture. Here is my report:

---

## Findings

### Q-Infer: Verified and Characterized

**Q-Infer** is a real, published paper. Its full title is "Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling," published in **ACM Transactions on Architecture and Code Optimization (TACO)**, 2025. It is available at:

- [ACM Digital Library](https://dl.acm.org/doi/full/10.1145/3764589)
- [ResearchGate](https://www.researchgate.net/publication/395071810_Q-Infer_Towards_Efficient_GPU-CPU_Collaborative_LLM_Inference_via_Sparsity-Aware_Dynamic_Scheduling)
- [GitHub (PDS-Lab/Q-Infer)](https://github.com/PDS-Lab/Q-Infer)

**Q-Infer's approach** addresses both MLP neuron sparsity and KV cache compression, but it treats them as **two separate optimization mechanisms coordinated at the system/scheduling level**, not as a single unified signal:

1. **MLP Sparsity**: Q-Infer uses an online MLP predictor to predict which neurons will be activated in each Transformer layer. Only the Top-K activated neurons are prefetched to the GPU; the rest remain on the CPU. This exploits contextual sparsity in the MLP blocks.

2. **KV Cache Compression**: Independently, Q-Infer uses a **multi-window mechanism** that divides the KV cache into three windows:
   - A **recent window** (full-precision recent tokens)
   - A **key tokens window** (dynamically selected important tokens)
   - A **quantization window** (less important tokens stored in quantized form on the CPU, computed via AVX-512 instructions)

3. **Coordination**: These two mechanisms are coordinated through a **sparsity-aware dynamic scheduling** layer that balances GPU-CPU workloads and I/O latency. The MLP predictor and the token importance selection for KV cache are **separate predictors/signals** -- they are orchestrated together in a system-level scheduler, but they do not share a single redundancy metric.

**Performance**: Q-Infer achieves approximately 1.4x, 2x, and 10x higher throughput compared to PowerInfer, llama.cpp, and FlexGen respectively.

---

### Does Any Paper Use a Single Unified Signal for Both MLP Sparsity and KV Cache Decisions?

After extensive searching across five different query formulations, **I did not find any published paper (2025-2026) that proposes using a single, shared redundancy signal to simultaneously drive both MLP neuron sparsity decisions and KV cache eviction/compression decisions.** Here is what the landscape looks like:

**Papers that address both axes but with separate mechanisms:**

- **Q-Infer** (ACM TACO 2025): As described above -- separate MLP predictor and KV cache window mechanism, coordinated at the scheduling level.
- **[Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression](https://arxiv.org/abs/2507.20613)** (Zhang et al., 2025): Combines weight pruning with KV cache quantization using a Tree-structured Parzen Estimator to search for optimal per-layer configurations. But pruning and quantization use separate metrics (weight/activation importance for pruning, uniform asymmetric quantization for KV cache). These are jointly *optimized* but driven by *different signals*.
- **SkipGPT** (ICML 2025): Decouples MLP and self-attention pruning decisions, using a learned router to make per-token, per-module skip decisions. This is arguably the closest to a unified framework, as a single router makes decisions about both MLP and attention modules. However, it operates at the **layer-skipping** level (deciding whether to skip an MLP or attention sub-layer entirely), not at the neuron-sparsity / KV-eviction level. And the router produces separate skip signals for MLP vs. attention rather than one shared redundancy score.

**Papers that address KV cache only (with relevant techniques):**
- **SparK** (AMD, 2025): Query-aware channel-level KV cache pruning.
- **R-KV**: Redundancy scoring based on key-vector similarity for KV eviction.
- **DeltaKV**: Residual-based KV cache compression via long-range similarity.

**Papers that address MLP sparsity only:**
- **Polar Sparsity** (2025): Batched LLM inference with scalable contextual sparsity.
- **DejaVu / PowerInfer**: Foundational MLP contextual sparsity work (2023-2024).

---

### Summary

- **Q-Infer is real and verified** -- published in ACM TACO 2025, with code on GitHub. It addresses both MLP sparsity and KV cache compression, but uses **separate mechanisms** (MLP activation predictor + multi-window KV cache management) coordinated through a system-level dynamic scheduler.

- **No paper found that uses a single unified redundancy signal across both axes.** The closest works either (a) jointly optimize both but with separate metrics (Q-Infer, the multimodal sparsity+quantization paper), or (b) use a single router that makes separate decisions per module type (SkipGPT). The idea of a single scalar or vector "redundancy signal" that simultaneously determines which MLP neurons to skip and which KV cache entries to evict appears to be an **open research gap** as of the searches conducted.

Sources:
- [Q-Infer (ACM TACO)](https://dl.acm.org/doi/full/10.1145/3764589)
- [Q-Infer PDF](https://dl.acm.org/doi/pdf/10.1145/3764589)
- [Q-Infer on ResearchGate](https://www.researchgate.net/publication/395071810_Q-Infer_Towards_Efficient_GPU-CPU_Collaborative_LLM_Inference_via_Sparsity-Aware_Dynamic_Scheduling)
- [Q-Infer on Semantic Scholar](https://www.semanticscholar.org/paper/Q-Infer:-Towards-Efficient-GPU-CPU-Collaborative-Lu-Wei/6d2fee68aef566c75bf4678c2f7ae176d5314a44)
- [Q-Infer GitHub](https://github.com/PDS-Lab/Q-Infer)
- [Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression](https://arxiv.org/abs/2507.20613)
- [SkipGPT (ICML 2025)](https://arxiv.org/abs/2506.04179)
- [SkipGPT GitHub](https://github.com/EIT-NLP/SkipGPT)
- [SparK (AMD ROCm Blog)](https://rocm.blogs.amd.com/artificial-intelligence/spark-blog/README.html)
- [Polar Sparsity](https://arxiv.org/html/2505.14884)
- [KV Cache Optimization Strategies Survey](https://arxiv.org/html/2603.20397v1)
- [ICLR 2025 Workshop: LLMs Know What to Drop](https://openreview.net/pdf?id=qg9dlCcNzr)

agentId: ac2d475fdb055a07a (use SendMessage with to: 'ac2d475fdb055a07a' to continue this agent)
&lt;usage>total_tokens: 26446
tool_uses: 14
duration_ms: 112384&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a30e59b5-e03f-45b6-bb4a-68a59d6b7e56",
  "isSidechain": false,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "type": "user",
  "uuid": "9c2d07cb-3b5c-409c-ae2b-2478aced0dae",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the paper \"Q-Infer\" which is described as a GPU-CPU collaborative LLM inference system that coordinates both MLP neuron sparsity and KV cache compression, published in ACM TACO 2025. Verify it exists and understand its approach.\n\nAlso search for any papers from 2025-2026 that specifically propose using a SINGLE signal to drive BOTH MLP sparsity and KV cache decisions:\n1. \"Q-Infer GPU CPU MLP sparsity KV cache ACM TACO\"\n2. \"unified signal MLP KV cache coordination LLM inference 2025 2026\"  \n3. \"single metric MLP sparsity KV eviction transformer\"\n4. \"cross-axis optimization MLP attention LLM inference\"\n5. \"joint compute memory optimization LLM decoding\"\n\nReport what you find — especially whether Q-Infer or any other paper uses a unified redundancy signal across both axes.",
    "agentId": "ac2d475fdb055a07a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Here is my report:\n\n---\n\n## Findings\n\n### Q-Infer: Verified and Characterized\n\n**Q-Infer** is a real, published paper. Its full title is \"Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling,\" published in **ACM Transactions on Architecture and Code Optimization (TACO)**, 2025. It is available at:\n\n- [ACM Digital Library](https://dl.acm.org/doi/full/10.1145/3764589)\n- [ResearchGate](https://www.researchgate.net/publication/395071810_Q-Infer_Towards_Efficient_GPU-CPU_Collaborative_LLM_Inference_via_Sparsity-Aware_Dynamic_Scheduling)\n- [GitHub (PDS-Lab/Q-Infer)](https://github.com/PDS-Lab/Q-Infer)\n\n**Q-Infer's approach** addresses both MLP neuron sparsity and KV cache compression, but it treats them as **two separate optimization mechanisms coordinated at the system/scheduling level**, not as a single unified signal:\n\n1. **MLP Sparsity**: Q-Infer uses an online MLP predictor to predict which neurons will be activated in each Transformer layer. Only the Top-K activated neurons are prefetched to the GPU; the rest remain on the CPU. This exploits contextual sparsity in the MLP blocks.\n\n2. **KV Cache Compression**: Independently, Q-Infer uses a **multi-window mechanism** that divides the KV cache into three windows:\n   - A **recent window** (full-precision recent tokens)\n   - A **key tokens window** (dynamically selected important tokens)\n   - A **quantization window** (less important tokens stored in quantized form on the CPU, computed via AVX-512 instructions)\n\n3. **Coordination**: These two mechanisms are coordinated through a **sparsity-aware dynamic scheduling** layer that balances GPU-CPU workloads and I/O latency. The MLP predictor and the token importance selection for KV cache are **separate predictors/signals** -- they are orchestrated together in a system-level scheduler, but they do not share a single redundancy metric.\n\n**Performance**: Q-Infer achieves approximately 1.4x, 2x, and 10x higher throughput compared to PowerInfer, llama.cpp, and FlexGen respectively.\n\n---\n\n### Does Any Paper Use a Single Unified Signal for Both MLP Sparsity and KV Cache Decisions?\n\nAfter extensive searching across five different query formulations, **I did not find any published paper (2025-2026) that proposes using a single, shared redundancy signal to simultaneously drive both MLP neuron sparsity decisions and KV cache eviction/compression decisions.** Here is what the landscape looks like:\n\n**Papers that address both axes but with separate mechanisms:**\n\n- **Q-Infer** (ACM TACO 2025): As described above -- separate MLP predictor and KV cache window mechanism, coordinated at the scheduling level.\n- **[Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression](https://arxiv.org/abs/2507.20613)** (Zhang et al., 2025): Combines weight pruning with KV cache quantization using a Tree-structured Parzen Estimator to search for optimal per-layer configurations. But pruning and quantization use separate metrics (weight/activation importance for pruning, uniform asymmetric quantization for KV cache). These are jointly *optimized* but driven by *different signals*.\n- **SkipGPT** (ICML 2025): Decouples MLP and self-attention pruning decisions, using a learned router to make per-token, per-module skip decisions. This is arguably the closest to a unified framework, as a single router makes decisions about both MLP and attention modules. However, it operates at the **layer-skipping** level (deciding whether to skip an MLP or attention sub-layer entirely), not at the neuron-sparsity / KV-eviction level. And the router produces separate skip signals for MLP vs. attention rather than one shared redundancy score.\n\n**Papers that address KV cache only (with relevant techniques):**\n- **SparK** (AMD, 2025): Query-aware channel-level KV cache pruning.\n- **R-KV**: Redundancy scoring based on key-vector similarity for KV eviction.\n- **DeltaKV**: Residual-based KV cache compression via long-range similarity.\n\n**Papers that address MLP sparsity only:**\n- **Polar Sparsity** (2025): Batched LLM inference with scalable contextual sparsity.\n- **DejaVu / PowerInfer**: Foundational MLP contextual sparsity work (2023-2024).\n\n---\n\n### Summary\n\n- **Q-Infer is real and verified** -- published in ACM TACO 2025, with code on GitHub. It addresses both MLP sparsity and KV cache compression, but uses **separate mechanisms** (MLP activation predictor + multi-window KV cache management) coordinated through a system-level dynamic scheduler.\n\n- **No paper found that uses a single unified redundancy signal across both axes.** The closest works either (a) jointly optimize both but with separate metrics (Q-Infer, the multimodal sparsity+quantization paper), or (b) use a single router that makes separate decisions per module type (SkipGPT). The idea of a single scalar or vector \"redundancy signal\" that simultaneously determines which MLP neurons to skip and which KV cache entries to evict appears to be an **open research gap** as of the searches conducted.\n\nSources:\n- [Q-Infer (ACM TACO)](https://dl.acm.org/doi/full/10.1145/3764589)\n- [Q-Infer PDF](https://dl.acm.org/doi/pdf/10.1145/3764589)\n- [Q-Infer on ResearchGate](https://www.researchgate.net/publication/395071810_Q-Infer_Towards_Efficient_GPU-CPU_Collaborative_LLM_Inference_via_Sparsity-Aware_Dynamic_Scheduling)\n- [Q-Infer on Semantic Scholar](https://www.semanticscholar.org/paper/Q-Infer:-Towards-Efficient-GPU-CPU-Collaborative-Lu-Wei/6d2fee68aef566c75bf4678c2f7ae176d5314a44)\n- [Q-Infer GitHub](https://github.com/PDS-Lab/Q-Infer)\n- [Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression](https://arxiv.org/abs/2507.20613)\n- [SkipGPT (ICML 2025)](https://arxiv.org/abs/2506.04179)\n- [SkipGPT GitHub](https://github.com/EIT-NLP/SkipGPT)\n- [SparK (AMD ROCm Blog)](https://rocm.blogs.amd.com/artificial-intelligence/spark-blog/README.html)\n- [Polar Sparsity](https://arxiv.org/html/2505.14884)\n- [KV Cache Optimization Strategies Survey](https://arxiv.org/html/2603.20397v1)\n- [ICLR 2025 Workshop: LLMs Know What to Drop](https://openreview.net/pdf?id=qg9dlCcNzr)"
      }
    ],
    "totalDurationMs": 112384,
    "totalTokens": 26446,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3229,
      "cache_read_input_tokens": 21362,
      "output_tokens": 1854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3229
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1854,
          "cache_read_input_tokens": 21362,
          "cache_creation_input_tokens": 3229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3229,
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
  "sourceToolAssistantUUID": "a30e59b5-e03f-45b6-bb4a-68a59d6b7e56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T18:23:55.183Z_

<details><summary>↩ Tool result · `toolu_0171KsMGXURabgxeiUvBP3UQ`</summary>

```text
Here is a comprehensive report of what the literature says across your two main lines of inquiry.

---

## Part 1: Does KV Cache Similarity Correlate with MLP Activation Sparsity?

### Direct evidence linking key similarity to MLP sparsity

No paper was found that directly studies the correlation "tokens with similar keys also have more compressible/sparse MLP activations." The two phenomena -- KV redundancy and MLP activation sparsity -- are well-studied individually, and a few papers come close to bridging them, but the explicit causal or correlational link you are asking about remains largely unestablished in the literature. Here is what exists:

### 1. KeyDiff (arXiv 2504.15364, NeurIPS 2025)

This is the strongest result connecting key similarity to token importance. KeyDiff demonstrates that **keys with lower average pairwise cosine similarity tend to receive higher attention scores**, with a correlation of rho ~0.94 across layers. This means geometrically distinctive keys (low cosine similarity to neighbors) are strongly aligned with tokens that matter more for attention computation. KeyDiff uses this as an eviction signal: tokens whose keys are very similar to other cached keys are treated as redundant and evicted. Critically, this works **without computing attention scores at all**, enabling compatibility with FlashAttention. However, KeyDiff says nothing about what happens in the MLP layers for those redundant tokens.

### 2. Deja Vu: Contextual Sparsity (arXiv 2310.17157, ICML 2024)

Deja Vu is the foundational paper on contextual sparsity. It shows that for any given input token, **over 80% of attention heads and over 95% of MLP neurons can be zeroed out** with minimal accuracy loss. It trains small two-layer MLP "routers" to predict which neurons/heads to activate, and these routers achieve ~93-99% accuracy. The key insight is that the **residual stream representation changes slowly across layers**, enabling predictions one layer ahead. However, Deja Vu does not use KV similarity as a predictor -- it uses separate trained routers per layer. The prediction is from the hidden state, not from key vectors specifically.

### 3. Polar Sparsity (arXiv 2505.14884, NeurIPS 2025)

Polar Sparsity extends Deja Vu to batched inference and makes an important observation: **MLP sparsity does not scale well to large batches** (the union of active neurons across a batch quickly approaches dense computation), while **attention head sparsity remains batch-invariant**. It also uses trained MLP routers to predict neuron activations. Again, the router predicts from hidden states, not from key similarity. But the observation that attention-level sparsity is more stable than MLP-level sparsity is relevant to your question -- it suggests that signals derived from the attention mechanism (like KV similarity) might be a more reliable basis for optimization than MLP-internal signals.

### 4. Token Filtering via KV Similarity (arXiv 2512.07090)

This paper uses **joint key-value similarity** with a variance-aware fusion strategy to perform online structured pruning -- deciding to skip entire attention computations for redundant tokens during inference. It achieves 50% pruning with minimal accuracy loss on LLaMA-2/3 and Mistral. Importantly, this is **structured pruning of the token dimension** (skipping a token's participation in attention), not MLP sparsity. But it validates that KV similarity is a strong signal for identifying tokens that contribute little to computation.

### 5. Attention-MLP Interaction (arXiv 2402.15055, EMNLP 2024)

This mechanistic interpretability paper shows that **specific attention heads recognize contexts and activate downstream "next-token neurons" in the MLP** through the residual stream. This demonstrates a functional coupling between attention patterns and MLP neuron firing, but the relationship is mediated by the residual stream, not by key similarity per se.

### 6. Probe and Skip / SPTS (arXiv 2601.13155)

This training-free framework uses **Partial Attention Probing (PAP)** for attention and **Low-rank Transformation Probing (LTP)** for FFN layers. For FFN token skipping, it constructs a low-rank proxy of the FFN and uses a combination of proxy output magnitude and attention scores to decide which tokens to skip. This is the closest to using an attention-derived signal to drive MLP-level decisions, but it still relies on a proxy computation rather than raw KV similarity.

### 7. SkipGPT (arXiv 2506.04179)

SkipGPT performs **decoupled pruning of MLP and attention modules**, finding that attention modules exhibit greater redundancy than MLP modules. It uses global token-aware routing to prioritize critical tokens, but the MLP and attention pruning decisions are made by separate policies, not coupled through KV similarity.

### Assessment for your question

The gap in the literature is clear: **no one has explicitly tested whether tokens with high pairwise key similarity also exhibit sparser/more compressible MLP activations**. The building blocks exist -- KeyDiff shows key similarity predicts token importance for attention, Deja Vu/Polar Sparsity show MLP activations are highly sparse and predictable from hidden states, and the attention-MLP interaction work shows functional coupling. But the specific hypothesis that KV similarity could serve as a valid signal for MLP sparsity decisions has not been validated.

There is an indirect reason to think it might work: if two tokens have very similar keys, they will receive similar attention patterns and thus produce similar post-attention residual stream updates. Since the MLP takes the residual stream as input, similar post-attention representations would likely produce similar MLP activation patterns (and thus similar sparsity patterns). But "similar sparsity patterns" is not the same as "higher sparsity." For the signal to validly drive MLP sparsity, you would need to show that **redundant tokens (high key similarity to neighbors) tend to have higher MLP activation sparsity**, not just similar sparsity to their neighbors.

---

## Part 2: KV Cache Insertion Filtering (Deciding at Generation Time Whether to Cache)

### Papers that address filtering at insertion time (as opposed to periodic eviction)

### 1. SkipKV (arXiv 2512.07993)

This is the most directly relevant paper. SkipKV is a **sentence-aware selective KV eviction and generation framework** for reasoning models. It has two components:
- A **sentence-primary scoring method** that identifies and removes highly similar sentences (not just tokens) while maintaining semantic coherence
- An **adaptive steering method** that dynamically adjusts hidden activation states to suppress redundant generation entirely

SkipKV skips both the **storage** and **generation** of KV pairs for redundant tokens. It maintains up to 26.7% improved accuracy vs. alternatives at similar compression budgets and achieves 1.6x fewer generated tokens with 1.7x throughput improvement. Evaluated on DeepSeek-R1 variants.

### 2. LazyEviction (arXiv 2506.15969)

LazyEviction identifies a **"Token Importance Recurrence" phenomenon** in reasoning tasks: tokens that appear unimportant (low attention) in a local window can suddenly become critical many steps later. It introduces:
- **Recurrence Interval Tracking** to capture temporal variation in token importance
- A **Maximum Recurrence Interval-Centric Eviction Policy** that avoids evicting tokens with long recurrence patterns

This achieves 50% KV cache reduction while maintaining accuracy on math reasoning. The key insight for your work: **any insertion-filtering approach must account for the fact that token importance is non-monotonic in reasoning tasks** -- a token that looks redundant now may be critical 100 steps later.

### 3. TRIM-KV / Cache What Lasts (arXiv 2512.03324)

Each gate predicts a scalar **retention score** that decays over time, reflecting the long-term utility of a token for a specific layer and head. Tokens with low scores are evicted when the memory budget is exceeded. This is closer to a continuous scoring mechanism than a binary insertion filter.

### 4. Expected Attention (arXiv 2510.00636)

This paper tackles the fundamental challenge of insertion-time filtering: you need to estimate importance for **future queries that haven't been generated yet**. Expected Attention estimates future attention distributions and uses them to prune up to 60% of the KV cache while preserving quality.

### 5. PaFu-KV (Past and Future-Informed KV Cache Policy)

Uses a lightweight **Salience Estimation Head** distilled from a bidirectional teacher to estimate token salience, combining past and future importance signals. This enables more informed retention decisions.

### 6. Attention-Gate (arXiv 2410.12876)

In-context KV cache eviction using learned attention gates that modulate which tokens to retain.

### 7. StreamingLLM

Retains only "sink tokens" (initial tokens that accumulate disproportionate attention) and a local sliding window. This is a simple insertion-time heuristic: keep the first few tokens always, keep recent tokens, discard everything else.

### Assessment for insertion filtering

The literature shows a clear progression:
- Early methods (StreamingLLM) use static rules
- Middle-generation methods (H2O, SnapKV) use attention-score accumulators to evict periodically
- Recent methods (SkipKV, LazyEviction, Expected Attention) try to make proactive decisions at or near insertion time, incorporating future-importance estimation

The major caveat from LazyEviction is that **insertion-time filtering is dangerous for reasoning tasks** because of token importance recurrence. Any viable approach would need a mechanism to either (a) defer final eviction decisions, or (b) recompute evicted entries when they become important again.

---

## Summary Assessment

**Can KV-similarity-based signal validly drive MLP sparsity decisions?** The literature provides indirect support but no direct validation:

1. Key similarity is a validated proxy for **attention-level token importance** (KeyDiff, rho ~0.94).
2. MLP activations are highly sparse and predictable from **hidden states** (Deja Vu, Polar Sparsity).
3. Attention patterns functionally couple to MLP neuron activation through the **residual stream** (attention-MLP interaction work).
4. The missing link is empirical evidence that tokens flagged as redundant by KV similarity also have higher/more predictable MLP sparsity.
5. The theoretical argument (similar keys -> similar attention -> similar residual -> similar MLP behavior) is plausible but does not directly imply *higher* sparsity for redundant tokens.

**For insertion filtering:** SkipKV is the closest existing work, operating at sentence level with both storage and generation skipping. LazyEviction's finding on token importance recurrence is a critical caveat: naive insertion filtering will fail on reasoning tasks.

Sources:
- [KeyDiff: Key Similarity-Based KV Cache Eviction](https://arxiv.org/abs/2504.15364)
- [Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time](https://arxiv.org/abs/2310.17157)
- [Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity](https://arxiv.org/abs/2505.14884)
- [Token Filtering: Leveraging KV Similarity for Online Structured Pruning in LLMs](https://arxiv.org/abs/2512.07090)
- [Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions](https://arxiv.org/abs/2402.15055)
- [Probe and Skip: Self-Predictive Token Skipping for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2601.13155)
- [SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling](https://arxiv.org/abs/2506.04179)
- [SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models](https://arxiv.org/abs/2512.07993)
- [LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning](https://arxiv.org/abs/2506.15969)
- [Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs](https://arxiv.org/abs/2512.03324)
- [Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution](https://arxiv.org/abs/2510.00636)
- [KV Cache Optimization Strategies for Scalable and Efficient LLM Inference](https://arxiv.org/abs/2603.20397)
- [Think Clearly: Improving Reasoning via Redundant Token Pruning](https://arxiv.org/html/2507.08806v1)
- [The Lazy Neuron Phenomenon: On Emergence of Activation Sparsity in Transformers](https://openreview.net/forum?id=TJ2nxciYCk-)
- [Uncovering Layer-Dependent Activation Sparsity Patterns in ReLU Transformers](https://arxiv.org/abs/2407.07848)

agentId: aa1543551dfcb7eca (use SendMessage with to: 'aa1543551dfcb7eca' to continue this agent)
&lt;usage>total_tokens: 31498
tool_uses: 19
duration_ms: 147707&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64f9ea6e-c999-46fc-99b8-ae406097a7e3",
  "isSidechain": false,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "type": "user",
  "uuid": "009c95ba-7d3a-47c7-96f5-293131b9af51",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for papers or analysis studying whether KV cache similarity (key-value vector similarity between tokens) correlates with MLP activation sparsity or activation magnitude patterns in LLMs. I want to know if there's any evidence that tokens with similar keys also have more compressible/sparse MLP activations.\n\nSearch queries:\n1. \"KV similarity activation sparsity correlation LLM\"\n2. \"token redundancy MLP computation skip LLM inference\"\n3. \"key vector similarity predict activation magnitude transformer\"\n4. \"redundant token MLP sparsity reasoning LLM\"\n5. \"token importance MLP attention correlation transformer inference\"\n\nAlso search for papers on KV cache \"insertion filtering\" — methods that decide whether to add a token to the KV cache at the time of generation (as opposed to periodic eviction of cached entries):\n6. \"KV cache insertion filtering LLM inference\"\n7. \"selective KV cache storage token generation\"\n8. \"token importance recurrence KV eviction reasoning\"\n\nReport what you find. This is important for assessing whether a KV-similarity-based signal can validly drive MLP sparsity decisions.",
    "agentId": "aa1543551dfcb7eca",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive report of what the literature says across your two main lines of inquiry.\n\n---\n\n## Part 1: Does KV Cache Similarity Correlate with MLP Activation Sparsity?\n\n### Direct evidence linking key similarity to MLP sparsity\n\nNo paper was found that directly studies the correlation \"tokens with similar keys also have more compressible/sparse MLP activations.\" The two phenomena -- KV redundancy and MLP activation sparsity -- are well-studied individually, and a few papers come close to bridging them, but the explicit causal or correlational link you are asking about remains largely unestablished in the literature. Here is what exists:\n\n### 1. KeyDiff (arXiv 2504.15364, NeurIPS 2025)\n\nThis is the strongest result connecting key similarity to token importance. KeyDiff demonstrates that **keys with lower average pairwise cosine similarity tend to receive higher attention scores**, with a correlation of rho ~0.94 across layers. This means geometrically distinctive keys (low cosine similarity to neighbors) are strongly aligned with tokens that matter more for attention computation. KeyDiff uses this as an eviction signal: tokens whose keys are very similar to other cached keys are treated as redundant and evicted. Critically, this works **without computing attention scores at all**, enabling compatibility with FlashAttention. However, KeyDiff says nothing about what happens in the MLP layers for those redundant tokens.\n\n### 2. Deja Vu: Contextual Sparsity (arXiv 2310.17157, ICML 2024)\n\nDeja Vu is the foundational paper on contextual sparsity. It shows that for any given input token, **over 80% of attention heads and over 95% of MLP neurons can be zeroed out** with minimal accuracy loss. It trains small two-layer MLP \"routers\" to predict which neurons/heads to activate, and these routers achieve ~93-99% accuracy. The key insight is that the **residual stream representation changes slowly across layers**, enabling predictions one layer ahead. However, Deja Vu does not use KV similarity as a predictor -- it uses separate trained routers per layer. The prediction is from the hidden state, not from key vectors specifically.\n\n### 3. Polar Sparsity (arXiv 2505.14884, NeurIPS 2025)\n\nPolar Sparsity extends Deja Vu to batched inference and makes an important observation: **MLP sparsity does not scale well to large batches** (the union of active neurons across a batch quickly approaches dense computation), while **attention head sparsity remains batch-invariant**. It also uses trained MLP routers to predict neuron activations. Again, the router predicts from hidden states, not from key similarity. But the observation that attention-level sparsity is more stable than MLP-level sparsity is relevant to your question -- it suggests that signals derived from the attention mechanism (like KV similarity) might be a more reliable basis for optimization than MLP-internal signals.\n\n### 4. Token Filtering via KV Similarity (arXiv 2512.07090)\n\nThis paper uses **joint key-value similarity** with a variance-aware fusion strategy to perform online structured pruning -- deciding to skip entire attention computations for redundant tokens during inference. It achieves 50% pruning with minimal accuracy loss on LLaMA-2/3 and Mistral. Importantly, this is **structured pruning of the token dimension** (skipping a token's participation in attention), not MLP sparsity. But it validates that KV similarity is a strong signal for identifying tokens that contribute little to computation.\n\n### 5. Attention-MLP Interaction (arXiv 2402.15055, EMNLP 2024)\n\nThis mechanistic interpretability paper shows that **specific attention heads recognize contexts and activate downstream \"next-token neurons\" in the MLP** through the residual stream. This demonstrates a functional coupling between attention patterns and MLP neuron firing, but the relationship is mediated by the residual stream, not by key similarity per se.\n\n### 6. Probe and Skip / SPTS (arXiv 2601.13155)\n\nThis training-free framework uses **Partial Attention Probing (PAP)** for attention and **Low-rank Transformation Probing (LTP)** for FFN layers. For FFN token skipping, it constructs a low-rank proxy of the FFN and uses a combination of proxy output magnitude and attention scores to decide which tokens to skip. This is the closest to using an attention-derived signal to drive MLP-level decisions, but it still relies on a proxy computation rather than raw KV similarity.\n\n### 7. SkipGPT (arXiv 2506.04179)\n\nSkipGPT performs **decoupled pruning of MLP and attention modules**, finding that attention modules exhibit greater redundancy than MLP modules. It uses global token-aware routing to prioritize critical tokens, but the MLP and attention pruning decisions are made by separate policies, not coupled through KV similarity.\n\n### Assessment for your question\n\nThe gap in the literature is clear: **no one has explicitly tested whether tokens with high pairwise key similarity also exhibit sparser/more compressible MLP activations**. The building blocks exist -- KeyDiff shows key similarity predicts token importance for attention, Deja Vu/Polar Sparsity show MLP activations are highly sparse and predictable from hidden states, and the attention-MLP interaction work shows functional coupling. But the specific hypothesis that KV similarity could serve as a valid signal for MLP sparsity decisions has not been validated.\n\nThere is an indirect reason to think it might work: if two tokens have very similar keys, they will receive similar attention patterns and thus produce similar post-attention residual stream updates. Since the MLP takes the residual stream as input, similar post-attention representations would likely produce similar MLP activation patterns (and thus similar sparsity patterns). But \"similar sparsity patterns\" is not the same as \"higher sparsity.\" For the signal to validly drive MLP sparsity, you would need to show that **redundant tokens (high key similarity to neighbors) tend to have higher MLP activation sparsity**, not just similar sparsity to their neighbors.\n\n---\n\n## Part 2: KV Cache Insertion Filtering (Deciding at Generation Time Whether to Cache)\n\n### Papers that address filtering at insertion time (as opposed to periodic eviction)\n\n### 1. SkipKV (arXiv 2512.07993)\n\nThis is the most directly relevant paper. SkipKV is a **sentence-aware selective KV eviction and generation framework** for reasoning models. It has two components:\n- A **sentence-primary scoring method** that identifies and removes highly similar sentences (not just tokens) while maintaining semantic coherence\n- An **adaptive steering method** that dynamically adjusts hidden activation states to suppress redundant generation entirely\n\nSkipKV skips both the **storage** and **generation** of KV pairs for redundant tokens. It maintains up to 26.7% improved accuracy vs. alternatives at similar compression budgets and achieves 1.6x fewer generated tokens with 1.7x throughput improvement. Evaluated on DeepSeek-R1 variants.\n\n### 2. LazyEviction (arXiv 2506.15969)\n\nLazyEviction identifies a **\"Token Importance Recurrence\" phenomenon** in reasoning tasks: tokens that appear unimportant (low attention) in a local window can suddenly become critical many steps later. It introduces:\n- **Recurrence Interval Tracking** to capture temporal variation in token importance\n- A **Maximum Recurrence Interval-Centric Eviction Policy** that avoids evicting tokens with long recurrence patterns\n\nThis achieves 50% KV cache reduction while maintaining accuracy on math reasoning. The key insight for your work: **any insertion-filtering approach must account for the fact that token importance is non-monotonic in reasoning tasks** -- a token that looks redundant now may be critical 100 steps later.\n\n### 3. TRIM-KV / Cache What Lasts (arXiv 2512.03324)\n\nEach gate predicts a scalar **retention score** that decays over time, reflecting the long-term utility of a token for a specific layer and head. Tokens with low scores are evicted when the memory budget is exceeded. This is closer to a continuous scoring mechanism than a binary insertion filter.\n\n### 4. Expected Attention (arXiv 2510.00636)\n\nThis paper tackles the fundamental challenge of insertion-time filtering: you need to estimate importance for **future queries that haven't been generated yet**. Expected Attention estimates future attention distributions and uses them to prune up to 60% of the KV cache while preserving quality.\n\n### 5. PaFu-KV (Past and Future-Informed KV Cache Policy)\n\nUses a lightweight **Salience Estimation Head** distilled from a bidirectional teacher to estimate token salience, combining past and future importance signals. This enables more informed retention decisions.\n\n### 6. Attention-Gate (arXiv 2410.12876)\n\nIn-context KV cache eviction using learned attention gates that modulate which tokens to retain.\n\n### 7. StreamingLLM\n\nRetains only \"sink tokens\" (initial tokens that accumulate disproportionate attention) and a local sliding window. This is a simple insertion-time heuristic: keep the first few tokens always, keep recent tokens, discard everything else.\n\n### Assessment for insertion filtering\n\nThe literature shows a clear progression:\n- Early methods (StreamingLLM) use static rules\n- Middle-generation methods (H2O, SnapKV) use attention-score accumulators to evict periodically\n- Recent methods (SkipKV, LazyEviction, Expected Attention) try to make proactive decisions at or near insertion time, incorporating future-importance estimation\n\nThe major caveat from LazyEviction is that **insertion-time filtering is dangerous for reasoning tasks** because of token importance recurrence. Any viable approach would need a mechanism to either (a) defer final eviction decisions, or (b) recompute evicted entries when they become important again.\n\n---\n\n## Summary Assessment\n\n**Can KV-similarity-based signal validly drive MLP sparsity decisions?** The literature provides indirect support but no direct validation:\n\n1. Key similarity is a validated proxy for **attention-level token importance** (KeyDiff, rho ~0.94).\n2. MLP activations are highly sparse and predictable from **hidden states** (Deja Vu, Polar Sparsity).\n3. Attention patterns functionally couple to MLP neuron activation through the **residual stream** (attention-MLP interaction work).\n4. The missing link is empirical evidence that tokens flagged as redundant by KV similarity also have higher/more predictable MLP sparsity.\n5. The theoretical argument (similar keys -> similar attention -> similar residual -> similar MLP behavior) is plausible but does not directly imply *higher* sparsity for redundant tokens.\n\n**For insertion filtering:** SkipKV is the closest existing work, operating at sentence level with both storage and generation skipping. LazyEviction's finding on token importance recurrence is a critical caveat: naive insertion filtering will fail on reasoning tasks.\n\nSources:\n- [KeyDiff: Key Similarity-Based KV Cache Eviction](https://arxiv.org/abs/2504.15364)\n- [Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time](https://arxiv.org/abs/2310.17157)\n- [Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity](https://arxiv.org/abs/2505.14884)\n- [Token Filtering: Leveraging KV Similarity for Online Structured Pruning in LLMs](https://arxiv.org/abs/2512.07090)\n- [Interpreting Context Look-ups in Transformers: Investigating Attention-MLP Interactions](https://arxiv.org/abs/2402.15055)\n- [Probe and Skip: Self-Predictive Token Skipping for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2601.13155)\n- [SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling](https://arxiv.org/abs/2506.04179)\n- [SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models](https://arxiv.org/abs/2512.07993)\n- [LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning](https://arxiv.org/abs/2506.15969)\n- [Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs](https://arxiv.org/abs/2512.03324)\n- [Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution](https://arxiv.org/abs/2510.00636)\n- [KV Cache Optimization Strategies for Scalable and Efficient LLM Inference](https://arxiv.org/abs/2603.20397)\n- [Think Clearly: Improving Reasoning via Redundant Token Pruning](https://arxiv.org/html/2507.08806v1)\n- [The Lazy Neuron Phenomenon: On Emergence of Activation Sparsity in Transformers](https://openreview.net/forum?id=TJ2nxciYCk-)\n- [Uncovering Layer-Dependent Activation Sparsity Patterns in ReLU Transformers](https://arxiv.org/abs/2407.07848)"
      }
    ],
    "totalDurationMs": 147707,
    "totalTokens": 31498,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2140,
      "cache_read_input_tokens": 26119,
      "output_tokens": 3238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2140
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3238,
          "cache_read_input_tokens": 26119,
          "cache_creation_input_tokens": 2140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2140,
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
  "sourceToolAssistantUUID": "64f9ea6e-c999-46fc-99b8-ae406097a7e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "009c95ba-7d3a-47c7-96f5-293131b9af51",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify redundancy-coordination efficiency method for EMNLP",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

### Assistant

_source line 34 · 2026-05-10T18:24:59.438Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me synthesize my findings and write the final review.

## Key Findings from My Research

### Paper Verification
All cited papers verified as real:
- Token Filtering (arXiv:2512.07090) ✓ — uses EMA centroid with variance-aware key+value fusion, for attention layer skipping only (NOT MLP or KV eviction)
- R-KV (NeurIPS 2025) ✓ — O(B²) pairwise similarity, periodic eviction
- TEAL (ICLR 2025 Spotlight) ✓ — model-wide sparsity (not MLP-only), 40-50% sparsity, 65% cliff confirmed


- EMA Is Not All You Need (arXiv:2604.08556) ✓ — EMA information dilution confirmed
- KeyDiff (arXiv:2504.15364) ✓ — mean-of-keys, not EMA
- CSAttention (arXiv:2604.08584) ✓ — query-centric lookup tables
- All other cited papers (FASA, ThinKV, SeerAttention-R, Polar Sparsity, EvoSparse, QuickSilver) confirmed

### EMNLP 2026 Deadline
May 25, 2026 confirmed as the submission deadline.

### Critical Novelty Assessment
The unified signal gap holds up—no existing work uses a single shared redundancy signal to drive both MLP sparsity and KV cache decisions simultaneously. QuickSilver, Q-Infer, and SkipGPT all handle these mechanisms separately with different signals, which strengthens the novelty position.

### Critical Technical Concerns
The core assumption that KV similarity enables more aggressive MLP pruning lacks empirical validation. The theoretical reasoning—similar keys lead to similar attention patterns and thus similar residual streams, allowing MLP sparsity—is intuitive but unproven.

There's also ambiguity around whether CARC filters tokens at insertion or evicts them post-caching, which matters because insertion filtering could trigger LazyEviction's token importance recurrence issues. Additionally, TEAL applies model-wide sparsity including attention projections rather than MLP-only, so the proposal's framing needs clarification. I should also note that SkipKV (arXiv:2512.07993) handles sentence-level KV generation and storage skipping for reasoning models, which is a relevant reference I'm missing.

Looking at what's actually improved from the previous round: the token filtering is properly cited, the contribution is reframed as a cross-axis extension, the windowed reset addresses EMA stability concerns, the 50-55% sparsity target sits safely below the 65% cliff, EMNLP 2026 is the right venue, benchmarks align with requirements, and I've acknowledged honest limitations. On novelty, the unified signal across both axes is genuinely novel since no prior work combines them this way, though the individual signals themselves draw from existing work.

The real question is whether coordinating both axes with a single signal constitutes a meaningful contribution or if it's just straightforward application of existing techniques. I think the coordination itself is valuable enough for EMNLP Findings, but Main conference acceptance would require deeper analytical insight—specifically understanding why KV similarity correlates with MLP sparsity tolerance. I'm settling on a 3 for novelty given this is more of a coordination insight than a fundamental breakthrough.

Feasibility looks strong at 4 out of 5: the approach is training-free, relies on existing kernels, and resource estimates fit within the H100 budget. The main constraint is the tight 14-16 day timeline.

The unvalidated assumption about KV-MLP correlation is a real risk—if that doesn't hold, the two-tier MLP sparsity becomes marginal, reducing the contribution to just KV eviction with a different triggering mechanism. On clarity, the paper is well-structured with good citations and honest limitations, though the KV eviction mechanism could use more detail and I'm missing references to SkipKV and LazyEviction. Impact is limited since this only applies to batch-1 reasoning, and the practical speedup gains need concrete demonstration. If the MLP tier differentiation only yields around 4% wall-clock improvement, that's underwhelming compared to the stronger KV eviction contribution.

The score sits at 3.375, below the 4.0 threshold, but I'm noticing the proposal has genuinely improved across iterations—the novelty concern from earlier was addressed well. The remaining gaps are all fixable: the cross-axis assumption needs a preliminary experiment, the missing references should be added, the KV mechanism needs clarification as insertion filtering with a recurrence safeguard, and TEAL's scope could be tightened. More importantly, I can't find any existing work using a unified signal for both MLP and KV optimization, which suggests this is a real gap worth exploring. I should give a "revise" verdict with specific, actionable feedback.

The coordination insight is valid but the execution is straightforward—it's a novel combination of existing techniques rather than a fundamentally new mechanism, so 3/5 for novelty feels right. The oracle ablation measuring the gap between KV similarity and query-dependent importance is a positive addition, though it doesn't fully address the KV-MLP correlation question. My final assessment: Novelty 3/5, Feasibility 4/5, Clarity 4/5, Impact 3/5, averaging to 3.5 with a revise recommendation.

To push this toward acceptance, the most impactful changes would be adding a preliminary analysis showing the correlation between EMA similarity scores and MLP activation sparsity—that would shift this from "we tried it and it works" to demonstrating *why* it works. They should also position this against SkipKV, LazyEviction, and Q-Infer, and provide concrete speedup decomposition numbers. If they add the KV-MLP correlation analysis, that could bump novelty and impact each to 3.5, bringing the average to 3.75—still below 4.0 but meaningfully closer. This reads as solid Findings-level work.

Given that the user is targeting both Main and Findings tracks for EMNLP 2026, I should acknowledge that Findings acceptance would be reasonable here, though the current state falls short of the Main conference threshold. The fixable issues point toward a "revise" recommendation rather than outright rejection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "009c95ba-7d3a-47c7-96f5-293131b9af51",
  "isSidechain": false,
  "requestId": "req_011CauMakuvK4YVZxBGuGQEU",
  "type": "assistant",
  "uuid": "401003a1-4702-4889-b304-cda96aa6b002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcJ47sVKpVhoUDpkQCetDb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1954,
      "cache_creation_input_tokens": 16295,
      "cache_read_input_tokens": 32748,
      "output_tokens": 4540,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16295,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1954,
          "output_tokens": 4540,
          "cache_read_input_tokens": 32748,
          "cache_creation_input_tokens": 16295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16295
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

_source line 35 · 2026-05-10T18:25:50.959Z_

I now have comprehensive research findings. Let me synthesize my independent verification and write the review.

Key findings from my research:
- All cited papers verified as real
- EMNLP 2026 ARR deadline May 25, 2026 confirmed
- The "unified signal across MLP + KV" gap is **genuinely novel** — no prior paper does this
- But critical unvalidated assumption: KV similarity → MLP sparsity tolerance
- Missing important references: SkipKV, LazyEviction, Q-Infer
- TEAL applies model-wide sparsity, not MLP-only as framed

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The unified signal gap is real — no prior work uses a single redundancy signal to coordinate both MLP sparsity and KV eviction. However, the signal itself is borrowed verbatim from Token Filtering (EMA centroid + variance-aware fusion), and each axis applies it to existing techniques (TEAL threshold routing, R-KV eviction strategy). The windowed reset is a reasonable but modest enhancement. The contribution is a valid coordination insight — novel as a combination, but incremental in both signal design and per-axis mechanism. EMNLP Findings caliber; Main requires a deeper analytical contribution."
    },
    "feasibility": {
      "score": 4,
      "rationale": "Training-free, no kernel modifications, existing codebases for all components. ~100h H100 manual estimate is realistic. The 14-16 day timeline is tight but possible given the simplicity of the approach (at batch=1, two-tier TEAL is just a conditional threshold switch). Main feasibility risk: the unvalidated assumption that KV-redundant tokens tolerate higher MLP sparsity — if this doesn't hold empirically, the MLP axis contribution collapses, requiring redesign."
    },
    "clarity": {
      "score": 4,
      "rationale": "Substantially improved from rounds 1-2. Token Filtering is properly cited and the contribution clearly reframed. Landscape coverage is comprehensive with honest limitations. Two remaining clarity issues: (1) the KV eviction mechanism is ambiguous — is it insertion filtering (not caching redundant tokens) or cache curation (evicting existing entries)?; (2) TEAL applies model-wide sparsity including attention projections, but the proposal frames it as 'MLP activation sparsity' throughout."
    },
    "impact": {
      "score": 3,
      "rationale": "Explicitly scoped to batch=1 reasoning (correct per Polar Sparsity), but this limits applicability. The practical speedup margin from two-tier MLP sparsity may be thin: going from 40% to 50-55% sparsity on redundant tokens saves ~10-15% additional MLP FLOPs on a fraction of tokens, translating to perhaps 3-5% wall-clock on the MLP axis alone. The KV eviction with O(1) triggering (vs R-KV's O(B²)) is the stronger practical contribution. Without quantified speedup decomposition, the additive gains claim remains unsubstantiated."
    }
  },
  "issues": [
    "UNVALIDATED CORE ASSUMPTION: No empirical or theoretical evidence exists that tokens with high KV similarity (redundant by the EMA signal) can tolerate higher MLP activation sparsity. The literature confirms KV similarity predicts attention-level token importance (KeyDiff, ρ~0.94) and that MLP activations are predictable from hidden states (Deja Vu), but the specific link 'KV-redundant → MLP-sparsity-tolerant' has never been tested. The theoretical argument (similar keys → similar attention → similar residual → similar MLP behavior) implies SIMILAR sparsity patterns, not HIGHER sparsity tolerance. This is the central assumption enabling cross-axis coordination; if it fails, the MLP axis collapses to uniform TEAL and the contribution reduces to 'KV eviction with a cheaper trigger signal.'",
    "MISSING CRITICAL REFERENCES: (1) SkipKV (arXiv:2512.07993) performs sentence-level KV generation and storage skipping for reasoning models — directly relevant to the KV eviction component. (2) LazyEviction (arXiv:2506.15969) discovers 'Token Importance Recurrence' in reasoning: tokens that appear redundant can become critical 100+ steps later. This directly challenges any insertion-filtering approach. (3) Q-Infer (ACM TACO 2025) jointly manages MLP neuron sparsity and KV cache compression at the system level — the closest multi-axis prior work. All three must be cited and differentiated against.",
    "KV EVICTION MECHANISM AMBIGUITY: The proposal states 'Tokens classified as redundant are evicted from the KV cache following R-KV's management strategy' but R-KV curates existing cache entries via periodic pairwise scoring, while CARC's per-token signal naturally suggests insertion filtering (not caching redundant tokens at generation time). These are fundamentally different mechanisms. If CARC does insertion filtering, LazyEviction's token importance recurrence is a serious accuracy risk for long reasoning chains. If CARC does periodic cache curation triggered by the EMA signal, the 'following R-KV's management strategy' claim needs specification of what is borrowed vs. novel.",
    "TEAL SCOPE MISCHARACTERIZATION: TEAL applies sparsity model-wide — to all hidden states before every linear layer including attention projections (W_q, W_k, W_v, W_o), not just MLP layers. The proposal frames TEAL usage as 'MLP activation sparsity' throughout. If two-tier thresholds are applied only to MLP matrices (W_up, W_gate, W_down) while attention projections use default thresholds, this should be stated explicitly. If applied model-wide, the framing as 'MLP sparsity' is misleading.",
    "THIN SPEEDUP MARGIN FOR MLP AXIS: Two-tier MLP sparsity (50-55% for redundant vs 40% for novel tokens) provides only 10-15 percentage points of additional sparsity on redundant tokens. Given that MLP computation accounts for roughly 60-70% of per-token FLOPs at batch=1 and only a fraction of tokens will be classified as redundant, the wall-clock contribution from the MLP axis may be ~3-5% — modest relative to the KV eviction contribution. An estimated speedup decomposition (MLP axis vs KV axis vs overhead) would substantiate or refute the 'additive gains' narrative.",
    "QUICKSILVER DIFFERENTIATION IS WEAK: QuickSilver (2025) integrates four mechanisms targeting orthogonal inefficiencies (token halting, KV skipping, token fusion, quantization). The proposal notes QuickSilver uses 'hidden-state L2 drift' and 'a different signal' for each mechanism, but doesn't explain why CARC's unified-signal approach is preferable. Is a single signal better (simpler, lower overhead) or worse (one signal can't capture different types of redundancy)? A principled comparison is needed."
  ],
  "feedback": "The proposal has improved significantly across rounds — Token Filtering citation, windowed reset, safe sparsity levels, and EMNLP 2026 targeting are all correct fixes. The unified-signal gap is genuinely novel (my independent search confirmed no prior work does this). However, three changes are needed to reach pass quality:\n\n1. **VALIDATE THE CROSS-AXIS ASSUMPTION (most critical):** Add a preliminary empirical analysis showing correlation between EMA similarity score and TEAL activation sparsity distribution. Concretely: run Token Filtering's EMA signal on a few hundred reasoning tokens from DeepSeek-R1-Distill-14B, then measure the actual activation magnitude distribution (TEAL's sparsity metric) for tokens classified as redundant vs. novel. If redundant tokens DO have higher natural sparsity, this validates the two-tier design and becomes a genuine analytical contribution. If they DON'T, pivot: drop two-tier MLP to uniform TEAL + the KV eviction with O(1) triggering as the main contribution (which is still novel and useful).\n\n2. **CLARIFY KV EVICTION AND ADDRESS RECURRENCE:** Specify whether CARC does insertion filtering or cache curation. If insertion filtering (more natural for per-token signal): cite LazyEviction and add a safeguard — e.g., a 'grace period' buffer where redundant tokens are marked but retained for W_grace steps before actual eviction, mitigating token importance recurrence. This would be a genuine design contribution beyond 'just don't cache redundant tokens.'\n\n3. **ADD MISSING REFERENCES AND SPEEDUP DECOMPOSITION:** Cite SkipKV, LazyEviction, and Q-Infer with clear differentiation. Add a back-of-envelope speedup decomposition: given typical MLP/attention time split at batch=1 for a 14B model on H100, estimate the wall-clock contribution from each axis independently. This makes the 'additive gains' claim concrete rather than hand-wavy.\n\nMinor fixes: correct TEAL scope framing (model-wide, not MLP-only, or specify that you apply two-tier only to MLP matrices); strengthen QuickSilver comparison (unified signal = lower overhead + simpler implementation vs. QuickSilver's per-mechanism signals).",
  "reason": "Core coordination insight is genuinely novel but the central assumption (KV redundancy → MLP sparsity tolerance) is unvalidated, KV eviction mechanism is ambiguous, and three important competing references are missing."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "401003a1-4702-4889-b304-cda96aa6b002",
  "isSidechain": false,
  "requestId": "req_011CauMakuvK4YVZxBGuGQEU",
  "type": "assistant",
  "uuid": "ec9a73c0-59ab-42d8-b764-6c42fc972436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcJ47sVKpVhoUDpkQCetDb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1954,
      "cache_creation_input_tokens": 16295,
      "cache_read_input_tokens": 32748,
      "output_tokens": 4540,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16295,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1954,
          "output_tokens": 4540,
          "cache_read_input_tokens": 32748,
          "cache_creation_input_tokens": 16295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16295
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
  "leafUuid": "ec9a73c0-59ab-42d8-b764-6c42fc972436",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify redundancy-coordination efficiency method for EMNLP",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be"
}
```

---
