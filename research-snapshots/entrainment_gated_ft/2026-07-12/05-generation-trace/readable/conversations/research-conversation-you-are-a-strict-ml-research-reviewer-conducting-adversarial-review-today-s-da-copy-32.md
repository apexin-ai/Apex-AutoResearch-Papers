# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/947b4d90-011e-4fa3-b17f-236d81333ba3.jsonl`
- **Structured JSON:** [`d90dd748cf3130f0a71f.json`](../../sessions/d9/d90dd748cf3130f0a71f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T01:42:53.204Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T01:42:53.204Z",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.\n\nDirection: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.\n\nContribution type: METHOD ONLY. Propose new algorithms — not profiling studies.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Generous for efficiency work.\n2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.\n3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.\n\nLook for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.\n\nTag: direction=efficiency, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 9/10)\n{\n  \"title\": \"Trajectory-Aware Joint Compression for Long-Horizon Agentic KV Caches\",\n  \"core_problem\": \"Agentic LLM systems (coding agents, research agents, tool-use agents) maintain KV caches that grow across dozens of reasoning-and-action steps, often exceeding 100K tokens. Current KV cache compression methods — including strong joint quantization-eviction approaches like ThinKV, HqeKV, and ARKV, as well as future-aware eviction methods like NGC and LookaheadKV — were designed for single-turn or single-model inference and optimize per-step reconstruction error or per-step eviction quality independently. In multi-step agentic workloads, compression errors compound across planning steps: PM-KVQ (ICLR 2026) demonstrates that directly quantizing KV cache at each decoding step causes cumulative quantization error that degrades long-CoT reasoning by up to 8% versus progressive strategies; 'Hold Onto That Thought' (under review, ICLR 2026) empirically shows that existing KV compression strategies designed for prefill-phase long-context tasks degrade significantly on reasoning tasks requiring extended decoding. Theoretical analysis from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves lower bounds showing exponential error growth Ω((n/s)^(T-1)) for oblivious cache strategies across T reasoning stages in k-hop pointer chasing; we note that this bound applies specifically to single-model multi-step reasoning with locality-respecting cache controllers, not directly to agentic tool-use workflows with external observation injection — the analogy is suggestive but not a formal proof. The empirical evidence from PM-KVQ and 'Hold Onto That Thought' provides the primary, more directly applicable motivation. No existing work formulates joint quantization-eviction that explicitly minimizes cumulative trajectory-level error for agentic workloads.\",\n  \"opportunity\": \"Two converging trends expose a clear research gap. First, agentic inference is now the dominant LLM deployment pattern (SWE-bench, GAIA, τ-bench), but KV cache compression research overwhelmingly targets single-turn inference. Existing agentic KV cache works address only parts of the problem: SideQuest (Feb 2026) uses model-driven eviction but not quantization; CodeComp (April 2026) leverages structural code priors for eviction only; CacheTTL (Nov 2025) manages cache scheduling without compression; PBKV (May 2026) predicts future agent invocations for cache management but performs no within-request compression; KVFlow (NeurIPS 2025) optimizes prefix caching for multi-agent workflows without compression; EpiCache (Apple, Sep 2025) manages episodic multi-turn cache but targets conversational QA, not agentic tool-use. NGC (April 2026) learns trajectory-aware KV eviction via RL within single-model reasoning chains, jointly optimizing reasoning and memory management from task reward alone — the closest conceptual competitor, but it requires RL training, is eviction-only (no quantization), and operates on single-model reasoning traces without explicit agent step boundaries or external observation injection. CapKV (April 2026) derives information-theoretic KV eviction via the Information Bottleneck principle with capacity-aware scoring — theoretically grounded but eviction-only and per-step.\\n\\nSecond, single-turn KV cache compression has matured across multiple fronts: (a) joint quantization-eviction via ThinKV (ICLR 2026 Oral, 20x compression), HqeKV (per-element compression actions), ARKV (tri-state assignment); (b) future-aware eviction via NGC (RL-based trajectory-aware eviction for single-model reasoning), LookaheadKV (ICLR 2026, predictive eviction via lookahead tokens + LoRA); (c) optimal bit allocation via RateQuant (rate-distortion reverse waterfilling, May 2026) and MixedDimKV (Lagrangian dual decomposition for per-token dimensions); (d) temporal and structural KV management via TTKV (temporal tiering with heterogeneous precision), TRIM-KV/Cache What Lasts (ICLR 2026, learned retention gates with temporal decay), and Transactional Attention (structural anchor protection for value-bearing tokens); (e) information-theoretic eviction via CapKV (Information Bottleneck with statistical leverage scores). However, none model how compression decisions at step t propagate errors to steps t+1 through T in multi-step agentic workflows with external tool observations. The key insight: in agentic workloads, token importance is cross-step structured in ways that single-turn methods cannot exploit. Instruction and plan tokens maintain importance across all steps; current-step observations are critical but rapidly decay; historical tool outputs become redundant as new observations arrive. This temporal structure, combined with the empirically-grounded error compounding problem (PM-KVQ, 'Hold Onto That Thought'), demands a fundamentally different optimization objective: minimizing trajectory-level degradation rather than per-step reconstruction error.\",\n  \"landscape\": \"**Joint quantization-eviction (single-turn):** ThinKV (ICLR 2026 Oral) applies thought-adaptive hybrid quantization-eviction achieving 20x compression with <5% KV cache — the strongest single-turn baseline, but no public code as of May 2026 (partial proxy available via NVIDIA's kvpress library as 'ThinKPress'). HqeKV (ACL ARR Jan 2026) provides an integrated optimizer selecting optimal compression actions (quantization level or eviction) per cached element under memory constraints; **public code confirmed** (github.com/skywclouds/HqeKV). ARKV (arXiv Feb 2026) dynamically assigns tokens to Original/Quantization/Eviction states based on per-layer attention statistics. KVTC (ICLR 2026) achieves 20x via PCA + adaptive quantization + entropy coding.\\n\\n**Constrained optimization for KV compression:** MixedDimKV (March 2026) formulates KV cache compression as a constrained optimization problem using Lagrangian dual decomposition with bisection search over λ, allocating per-token dimensions under a memory budget. This uses the same Lagrangian optimization technique as TrajComp. The critical difference: MixedDimKV minimizes per-step reconstruction error (single-step objective), while TrajComp minimizes trajectory-level error accumulation across T agent steps (multi-step objective). The trajectory extension is non-trivial because: (i) the search space expands from per-step to cross-step — compressing token i at step t affects attention distributions at steps t+1...T; (ii) the objective changes from reconstruction fidelity to trajectory success rate; (iii) the importance model must account for temporal structure (persistent vs. decaying tokens) absent in single-turn settings. RateQuant (May 2026) applies rate-distortion theory with reverse waterfilling for optimal per-head bit allocation — a complementary per-step optimization that TrajComp could incorporate as a sub-routine for within-step bit allocation.\\n\\n**Trajectory-aware and future-aware eviction:** NGC (April 2026, arXiv:2604.18002) learns trajectory-aware KV eviction via RL, treating both reasoning tokens and cache-eviction decisions as discrete actions sampled from the language model, trained end-to-end from outcome-based task reward alone. On Countdown, AMC, and AIME, NGC achieves 2-3x peak KV cache compression while maintaining strong accuracy. TrajComp differs from NGC in three key ways: (1) training-free (Lagrangian optimization vs. RL training required), (2) joint quantization-eviction (vs. eviction-only), and (3) designed for multi-step agentic workflows with explicit step boundaries and external observation injection (vs. single-model reasoning traces where the model interleaves thinking and eviction). LookaheadKV (ICLR 2026, Samsung) predicts future attention patterns via trainable lookahead tokens + LoRA, achieving <0.7% drop at 81% compression — also eviction-only and single-turn.\\n\\n**Information-theoretic eviction:** CapKV (April 2026, arXiv:2604.25975) derives capacity-aware KV eviction via the Information Bottleneck principle, using a log-determinant approximation with statistical leverage scores under a linear-Gaussian surrogate of attention. It provides a theoretically grounded mechanism that replaces heuristic selection with capacity-maximization. TrajComp differs: joint quantization-eviction with a trajectory-level multi-step objective vs. CapKV's per-step information-theoretic eviction-only framework.\\n\\n**Temporal and structural KV management:** TTKV (March 2026) partitions KV cache into temporal tiers with heterogeneous precision across HBM/DRAM, achieving 76% latency reduction on 128K contexts. Its temporal tiering directly overlaps with TrajComp's 'decaying context' category — but TTKV is a system-level memory hierarchy approach without trajectory-aware error optimization. TRIM-KV/Cache What Lasts (ICLR 2026) learns per-token retention gates with temporal decay via distillation — conceptually similar to cross-step importance decay, but training-required, eviction-only, and single-turn. Transactional Attention (April 2026) protects structural anchor tokens (credentials, API keys) from eviction via semantic sponsorship — overlaps with TrajComp's 'persistent anchors' category, but is domain-specific to credential/configuration retention and does not perform compression.\\n\\n**Agentic KV cache management:** SideQuest (Feb 2026) uses the reasoning model itself to identify dispensable tokens, achieving 65% peak token reduction on agentic tasks — eviction only, no quantization, no public code. CodeComp (April 2026) uses Code Property Graph priors for structure-aware eviction in agentic coding — domain-specific and eviction only. CacheTTL/Continuum (Nov 2025) manages multi-turn cache scheduling with TTL-based retention. PBKV (May 2026) predicts future agent invocations and manages cache across workflow steps — system-level scheduling without within-request compression. KVFlow (NeurIPS 2025) optimizes prefix caching for multi-agent workflows. EpiCache (Apple, Sep 2025) manages episodic multi-turn cache for conversational QA. Agent Memory Below the Prompt (Feb 2026) persists Q4 KV caches across agents on edge devices. KVComm (Oct 2025) enables cross-context KV sharing.\\n\\n**Other relevant methods:** TriAttention (MIT/NVIDIA, April 2026) achieves 10.7x via trigonometric key importance scoring. R-KV (NeurIPS 2025) achieves 100% accuracy at 10% KV via redundancy-aware eviction with **public code** (github.com/Zefan-Cai/R-KV, 1.2k stars, vLLM/SGLang/FlashInfer integrations). DMS (NeurIPS 2025) achieves 8x with lightweight training. EVICPRESS (Microsoft, Dec 2025) jointly optimizes compression and eviction across storage tiers but has no public code. PM-KVQ shows progressive mixed-precision reduces cumulative quantization error in long-CoT. TurboQuant (ICLR 2026) addresses inner-product estimation bias compounding across attention computations. 'Not All Bits Are Equal' (ICLR 2026) shows optimal compression strategy is scale-dependent.\\n\\n**Error compounding theory and evidence:** 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves that under k-hop pointer chasing with cache size s, oblivious caches suffer exponential error growth Ω((n/s)^(T-1)). We note this bound applies specifically to k-hop pointer chasing with locality-respecting cache controllers in single-model multi-step reasoning; its extension to agentic tool-use with external observation injection is an analogy, not a formal proof. The empirical evidence from PM-KVQ (cumulative quantization error degrades long-CoT by up to 8%) and 'Hold Onto That Thought' (compression designed for prefill degrades extended-decoding reasoning) provides the primary and more directly applicable motivation for trajectory-aware compression.\\n\\n**Code availability summary for baseline selection:** Of the methods considered as baselines, only R-KV (github.com/Zefan-Cai/R-KV, 1.2k stars) and HqeKV (github.com/skywclouds/HqeKV) have confirmed public implementations. ThinKV has a partial proxy (ThinKPress in NVIDIA kvpress) but no full implementation. SideQuest, EVICPRESS, and ForesightKV have no public code. This directly constrains baseline selection to methods with verified reproducibility.\\n\\nNo prior work formulates a trajectory-level objective for joint quantization-eviction in agentic KV caches with explicit cross-step error accumulation control. The closest works are NGC (trajectory-aware but RL-required, eviction-only, single-model) and MixedDimKV (same Lagrangian technique but per-step objective). TrajComp uniquely combines: (1) joint quant-eviction, (2) trajectory-level multi-step objective, (3) training-free Lagrangian optimization, (4) agentic workflow structure exploitation.\",\n  \"approach\": \"We propose TrajComp (Trajectory-Aware Joint Compression), which formulates a single dual-constrained Lagrangian objective jointly optimizing token retention probabilities and per-token bit allocation under memory and cumulative trajectory-error budgets. We commit to a two-phase evaluation strategy: a focused EMNLP 2026 short paper sprint (ARR May 25 deadline, 13 days), followed by an extended ICLR 2027 full paper.\\n\\n**(1) Cross-step error propagation model:** Unlike ThinKV/HqeKV/MixedDimKV which minimize per-step reconstruction error independently, and unlike NGC which learns trajectory-aware eviction through RL training, TrajComp models error propagation across agent steps in a training-free manner. Compressing token i at step t contributes weighted error proportional to Σ_{s=t+1}^{T} γ^{s-t} × importance_i, where γ is the empirically-calibrated step-wise error propagation rate. The dual-constrained Lagrangian L = Σ_t error_t(s,q) + λ_mem(M(s,q) - B_mem) + λ_err(E_cumul(s,q,γ) - B_err) enables smooth Pareto-optimal tradeoffs via dual gradient descent on both multipliers. Note: MixedDimKV uses Lagrangian dual decomposition with bisection for a single memory constraint and per-step objective; TrajComp extends this to dual constraints (memory + trajectory error) with a cross-step objective, requiring the error propagation model as additional machinery.\\n\\n**γ calibration procedure:** For Qwen3-8B (EMNLP sprint), run N=5 agent trajectories on a τ-bench subset with full (uncompressed) KV cache and with uniformly 4-bit quantized KV cache. At each agent step boundary t, measure KL divergence D_KL(P_full^t || P_compressed^t) of the attention distributions. Compute per-step propagation ratios r_t = D_KL^{t+1} / D_KL^t across all steps and trajectories. Set γ = median(r_t). Based on PM-KVQ's observations of progressive error accumulation, we expect γ ∈ [0.7, 0.95]. Calibration cost: ~2 H100-hours for the EMNLP sprint. For the ICLR extension, expand to N=10 trajectories per model-benchmark pair with sensitivity analysis (~10 H100-hours total for 2 models × 2 agentic benchmarks).\\n\\n**(2) Agent-phase token categorization:** Rather than ThinKV's within-turn thought types, TrajComp defines categories by agentic workflow structure: (a) Persistent anchors — system prompts, instructions, plans — never compressed (analogous to Transactional Attention's structural anchors, but generalized beyond credentials to all instruction-bearing tokens); (b) Active context — current tool output and recent reasoning — retained at 4-bit; (c) Decaying context — older observations — progressively compressed (4-bit → 2-bit → evict) with schedule determined by the Lagrangian solver based on temporal distance and cross-step importance (analogous to TTKV's temporal tiering, but driven by trajectory-level optimization rather than fixed temporal heuristics); (d) Ephemeral tokens — intermediate tool formatting, API boilerplate — immediately evicted.\\n\\n**Phase detection strategy:** For structured agent frameworks (ReAct, function-calling with explicit Thought/Action/Observation tags), use lightweight pattern matching on special tokens and turn boundaries (zero overhead). This covers both evaluation settings: τ-bench uses structured tool-calling, and SWE-agent uses ReAct prompting with explicit delimiters. For the EMNLP sprint, pattern matching suffices for all evaluated benchmarks. For the ICLR extension with free-form reasoning models, fall back to attention entropy thresholds: compute per-token attention entropy at step boundaries; tokens with consistently high entropy across recent steps are classified as ephemeral, tokens with low entropy as active/persistent.\\n\\n**(3) GQA-aware compression:** Qwen3-8B uses Grouped Query Attention (32 query heads, 8 KV heads). TrajComp allocates compression budgets at the KV-head group level, accounting for the fact that compressing a single KV head affects all 4 query heads in its group. For the ICLR extension, DeepSeek-R1-0528-Qwen3-8B uses the same GQA configuration (32 query heads, 8 KV heads, Qwen3 architecture) but with DeepSeek-R1-0528's tokenizer — we verify tokenizer compatibility for phase detection. MLA adaptation (for full DeepSeek-V3/R1 671B models) is left as future work.\\n\\nThe dual gradient descent operates at agent step boundaries (not every token), making it lightweight. A single re-optimization pass over the full KV cache occurs when a new agent step begins.\\n\\n**Wall-clock and throughput reporting:** We report: (a) Lagrangian solver time per agent step as a function of KV cache size — expected to be <10ms for dual gradient descent over ~100K tokens, dominated by importance score computation not the optimization itself; (b) end-to-end latency per agent step (including compression overhead) vs. baselines on H100-80GB; (c) tokens/second throughput at matched compression ratios.\\n\\n---\\n\\n**EMNLP 2026 SHORT PAPER SPRINT (Primary — ARR May 25, 2026)**\\n\\n13-day sprint for a 4-page short paper targeting EMNLP 2026 Findings:\\n\\n**Sprint timeline:**\\n- Day 1-3 (May 12-14): Implement Lagrangian solver + phase detection on HuggingFace Transformers. Integrate R-KV (from public repo, pip-installable) and HqeKV (from public repo) as baselines.\\n- Day 4-5 (May 15-16): γ calibration on Qwen3-8B with 5 τ-bench trajectories. Validate solver convergence.\\n- Day 6-8 (May 17-19): Run experiments — τ-bench full (164 tasks × 3 methods: TrajComp, R-KV, HqeKV), LongBench, MMLU. Collect wall-clock numbers.\\n- Day 9-11 (May 20-22): Write 4-page paper. Focus on: (1) trajectory-level Lagrangian formulation, (2) agent-phase categorization, (3) τ-bench results showing trajectory success rate at matched compression ratios.\\n- Day 12-13 (May 23-24): Polish, add any ablations completed, finalize submission.\\n- Day 14 (May 25): Submit to ARR with EMNLP 2026 venue declaration.\\n\\n**Sprint evaluation scope:**\\n- Model: Qwen3-8B (single model — avoids DeepSeek tokenizer compatibility debugging under time pressure)\\n- Baselines: R-KV (public code, github.com/Zefan-Cai/R-KV, 1.2k stars, pip-installable), HqeKV (public code, github.com/skywclouds/HqeKV) — both with confirmed public implementations\\n- Benchmarks: τ-bench 164 tasks via official harness (primary agentic benchmark — 8B models achieve meaningful success rates on structured customer-service tasks), LongBench (long-context regression), MMLU (general capability regression)\\n- Key metric: trajectory-level success rate at matched compression ratio on τ-bench; standard accuracy on LongBench/MMLU\\n- Compression targets: 4x, 8x, 16x (3 operating points)\\n\\n**Sprint compute budget (~60 H100-hours):**\\n- γ calibration: 5 trajectories × 2 configs × ~5 min ≈ 1h\\n- τ-bench: 164 tasks × 3 methods × 3 compression ratios × ~2 min ≈ 49h\\n- LongBench: ~3h\\n- MMLU: ~1h\\n- Wall-clock benchmarking: ~1h\\n- Development/debugging: ~5h\\n- Total: ~60 H100-hours\\n\\n**Sprint risk mitigation:**\\n- R-KV's mature codebase (1.2k stars, vLLM integration) minimizes baseline setup time\\n- τ-bench has an official evaluation harness — no custom scaffolding needed\\n- Pattern-matching phase detection on τ-bench's structured tool-calling is trivially implementable\\n- If HqeKV integration proves difficult (CUDA kernel compilation), fall back to HqeKV's non-CUDA mode or replace with attention-score-based uniform mixed-precision (4-bit/2-bit partitioning, implementable in <4h)\\n\\n---\\n\\n**ICLR 2027 FULL PAPER EXTENSION (Secondary — expected deadline ~September 2026)**\\n\\nExpands the EMNLP sprint results into a full 8-page paper:\\n\\n- Add model: DeepSeek-R1-0528-Qwen3-8B (same GQA architecture, DeepSeek-R1-0528 tokenizer — verify phase detection compatibility)\\n- Add baseline: Uniform mixed-precision (attention-score-based 4-bit/2-bit partitioning, implementable in <8h — serves as ablation baseline showing the value of trajectory-aware optimization over naive mixed-precision)\\n- Add benchmarks: SWE-bench Lite 50 instances via SWE-agent (ReAct, 30 turns, 16K tokens/turn), AIME 2025, MATH-500, HumanEval, MT-Bench, WikiText/C4 perplexity\\n- Add ablations: phase detection accuracy, γ sensitivity, anchor ratio impact, component-wise ablation\\n- Add attention entropy fallback for phase detection (for future free-form reasoning evaluation)\\n- If ThinKV releases official code before experiments begin, add as 4th baseline\\n\\n**ICLR extension compute (~140 additional H100-hours, ~200h total including sprint):**\\n- SWE-bench Lite: 50 instances × 2 models × 4 methods × ~10 min ≈ 67h\\n- τ-bench extension: 164 tasks × 1 additional model × 4 methods × ~2 min ≈ 22h\\n- Additional benchmarks (AIME, MATH-500, HumanEval, MT-Bench, perplexity): ~20h\\n- Extended γ calibration: ~8h\\n- Ablations: ~15h\\n- Dev/debug buffer: ~10h\\n- Total extension: ~142h → ~200h cumulative\\n\\n**8B model capability consideration:** We acknowledge that 8B models achieve relatively low base success rates on SWE-bench (~17%). For the EMNLP sprint, we avoid SWE-bench entirely, using τ-bench as the primary agentic benchmark where 8B models achieve higher success rates on structured tasks. For the ICLR extension, we supplement binary SWE-bench success with trajectory-quality metrics (steps completed before failure, tool-call coherence, attention distribution divergence from full-cache trajectories).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~60h H100-80GB (EMNLP sprint); ~200h total (including ICLR extension)\",\n      \"gpu_utilization\": \"50-60% effective — τ-bench instances run quickly (~2 min each); gaps filled with MMLU/LongBench evaluation\",\n      \"timeline\": \"13 days for EMNLP sprint; 4 months total for ICLR extension\",\n      \"team\": \"1 researcher with systems ML background\",\n      \"estimated_gpu_cost\": \"$150 (60h × ~$2.50/h EMNLP sprint); $500 total with ICLR extension\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~60h H100-80GB (EMNLP sprint); ~200h total\",\n      \"gpu_utilization\": \"60-70% — agent handles R-KV/HqeKV integration from public repos, τ-bench harness setup, γ calibration runs; human guides Lagrangian formulation and paper writing\",\n      \"timeline\": \"13 days for EMNLP sprint (human: ~2h/day for formulation + writing); 3 months for ICLR extension\",\n      \"team\": \"1 researcher, ~2h/day during sprint, ~45min/day during extension\",\n      \"claude_api_cost\": \"$80-120 for sprint (~800-1200 turns); $300-500 total with extension\",\n      \"estimated_gpu_cost\": \"$150 sprint; $500 total\",\n      \"risk_note\": \"Primary sprint risk: HqeKV CUDA kernel compilation may require debugging. Mitigation: fall back to HqeKV non-CUDA mode or replace with uniform mixed-precision baseline (~4h to implement). R-KV is pip-installable and battle-tested (1.2k stars). τ-bench has an official harness with minimal setup.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~80h H100-80GB (automated sprint with wider γ sweep); ~250h total with ICLR extension\",\n      \"gpu_utilization\": \"55-65% — τ-bench instances create pipeline gaps; agent queues MMLU/LongBench during gaps\",\n      \"timeline\": \"10-12 days for sprint; 4-6 weeks for ICLR extension with 2 concurrent H100s\",\n      \"team\": \"0 (initial 2-hour setup: model download, R-KV pip install, τ-bench harness verification)\",\n      \"claude_api_cost\": \"$150-250 for sprint; $500-800 total with extension\",\n      \"estimated_gpu_cost\": \"$200 sprint; $625 total\",\n      \"speed_bottleneck\": \"τ-bench: 164 tasks × 9 runs (3 methods × 3 compression ratios) × ~2 min ≈ 49h — the dominant sprint cost. Parallelizable across GPUs.\",\n      \"risk_note\": \"Agent may struggle with Lagrangian formulation implementation without human guidance. Recommend human review of solver code before experiment runs (Day 3-4 checkpoint).\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR May 25, 2026 — 13 days from today; 4-page short paper; ~60 H100-hours; commit to EMNLP venue at submission; reviews by June 29, commitment deadline August 2)\",\n    \"ICLR 2027 (expected abstract deadline ~September 19, 2026; 8-page full paper extending EMNLP results with 2nd model, additional baselines, SWE-bench, and ablations; ~200 H100-hours total)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral) — no public code; partial proxy via NVIDIA kvpress (ThinKPress)\",\n    \"HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference (ACL ARR Jan 2026) — **public code: github.com/skywclouds/HqeKV** — EMNLP sprint baseline\",\n    \"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget (arXiv Feb 2026)\",\n    \"NGC: Neural Garbage Collection: Learning to Forget while Learning to Reason (arXiv April 2026, arXiv:2604.18002) — RL-based trajectory-aware KV eviction for single-model reasoning, eviction-only, 2-3x compression on Countdown/AMC/AIME\",\n    \"CapKV: Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective (arXiv April 2026, arXiv:2604.25975) — Information Bottleneck principle with statistical leverage scores, eviction-only, per-step\",\n    \"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation (ICLR 2026 Poster, Samsung, arXiv:2603.10899) — predictive eviction via lookahead tokens + LoRA\",\n    \"TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference (arXiv March 2026, arXiv:2604.19769) — temporal tiering with heterogeneous precision across HBM/DRAM\",\n    \"TRIM-KV / Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs (ICLR 2026, arXiv:2512.03324) — learned per-token retention gates with temporal decay\",\n    \"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory (arXiv May 2026, arXiv:2605.06675) — reverse waterfilling for per-head bit allocation\",\n    \"Transactional Attention: Semantic Sponsorship for KV-Cache Retention (arXiv April 2026, arXiv:2604.11288) — structural anchor protection for value-bearing tokens\",\n    \"Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression [MixedDimKV] (arXiv March 2026, arXiv:2603.20616) — Lagrangian dual decomposition for per-token dimension allocation\",\n    \"PBKV: Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management (arXiv May 2026, arXiv:2605.06472) — prediction-based agent cache scheduling\",\n    \"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows (NeurIPS 2025, arXiv:2507.07400) — workflow-aware prefix caching\",\n    \"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering (Apple, arXiv Sep 2025, arXiv:2509.17396) — episodic multi-turn cache management\",\n    \"SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning (arXiv Feb 2026) — no public code\",\n    \"CodeComp: Structural KV Cache Compression for Agentic Coding (arXiv April 2026)\",\n    \"CacheTTL/Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live (arXiv Nov 2025)\",\n    \"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models (NeurIPS 2025) — **public code: github.com/Zefan-Cai/R-KV, 1.2k stars, vLLM/SGLang/FlashInfer integrations** — EMNLP sprint baseline\",\n    \"How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers (arXiv April 2026, arXiv:2604.17935) — theoretical bounds on cache compression vs. reasoning depth (k-hop pointer chasing; analogy to agentic setting, not direct proof)\",\n    \"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs (arXiv May 2025, OpenReview Oct 2025) — empirical evidence of cumulative quantization error in long-CoT\",\n    \"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning (arXiv Dec 2025, arXiv:2512.12008) — empirical assessment of compression degradation on reasoning tasks\",\n    \"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression (MIT/NVIDIA, arXiv April 2026)\",\n    \"KV Cache Transform Coding [KVTC] for Compact Storage in LLM Inference (NVIDIA, ICLR 2026)\",\n    \"Inference-Time Hyper-Scaling with KV Cache Compression [DMS] (NeurIPS 2025) — public code via HuggingFace + NVIDIA kvpress\",\n    \"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving (Microsoft, arXiv Dec 2025) — no public code\",\n    \"Not All Bits Are Equal: How Model Scale Changes Memory-Optimal Reasoning (ICLR 2026)\",\n    \"TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate (ICLR 2026) — inner-product bias compounding\",\n    \"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution (arXiv Feb 2026, arXiv:2602.03203) — RL-based future-aware eviction, no public code\",\n    \"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices (arXiv Feb 2026, arXiv:2603.04428)\",\n    \"KVComm: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems (arXiv Oct 2025)\",\n    \"Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys (AAAI 2026)\"\n  ],\n  \"description\": \"We propose TrajComp (Trajectory-Aware Joint Compression), a training-free method that jointly optimizes token eviction and per-token bit allocation for KV caches in long-horizon agentic LLM workloads through a dual-constrained Lagrangian objective that explicitly minimizes trajectory-level error accumulation. The empirical motivation comes from PM-KVQ (ICLR 2026), which demonstrates that cumulative quantization error degrades long-CoT reasoning by up to 8% versus progressive strategies, and from 'Hold Onto That Thought' (2025), which shows that compression strategies designed for prefill degrade on extended-decoding reasoning. Theoretical analysis from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves exponential error growth Ω((n/s)^(T-1)) for oblivious cache strategies in k-hop pointer chasing; we note this bound applies to single-model reasoning with locality-respecting cache controllers — its extension to agentic tool-use with external observation injection is a suggestive analogy, not a formal proof.\\n\\nThe landscape includes strong single-turn methods across multiple fronts: joint quant-eviction (ThinKV at 20x — no public code, HqeKV — public code, ARKV), future-aware and trajectory-aware eviction (NGC via RL-based eviction for single-model reasoning achieving 2-3x compression, LookaheadKV via predictive attention), information-theoretic eviction (CapKV via Information Bottleneck with statistical leverage scores), optimal bit allocation (RateQuant via rate-distortion, MixedDimKV via Lagrangian dual), and temporal/structural management (TTKV temporal tiering, TRIM-KV learned retention, Transactional Attention anchor protection). Agentic-specific works (SideQuest, CodeComp, PBKV, KVFlow, EpiCache) address scheduling and eviction but not joint compression. No prior work combines joint quant-eviction with a trajectory-level multi-step objective for agentic workloads.\\n\\nTrajComp fills this gap with two core contributions: (1) A cross-step error propagation model that weights compression decisions by their γ-discounted impact across all future agent steps, formalized as a dual-constrained Lagrangian with separate memory and trajectory-error budget multipliers. γ is calibrated empirically via KL divergence propagation measurement. (2) Agent-phase token categorization (persistent anchors, active context, decaying context, ephemeral tokens) that exploits cross-step importance structure unique to agentic workflows, with pattern-matching detection for structured agent frameworks (ReAct, function-calling). Both contributions are training-free.\\n\\nWe commit to a dual-track evaluation strategy designed to meet both the EMNLP 2026 deadline and resource constraints:\\n\\n**EMNLP 2026 short paper (primary, ARR May 25):** 4-page paper, 13-day sprint, ~60 H100-hours. 1 model (Qwen3-8B, GQA), 2 baselines with confirmed public code (R-KV at github.com/Zefan-Cai/R-KV with 1.2k stars and pip-installable vLLM integration; HqeKV at github.com/skywclouds/HqeKV), 3 benchmarks (τ-bench 164 tasks via official harness as primary agentic benchmark, LongBench, MMLU). Sprint: Day 1-3 implement solver + integrate baselines from public repos, Day 4-5 γ calibration, Day 6-8 run experiments, Day 9-11 write paper, Day 12-13 polish, Day 14 submit. Reports trajectory-level success rate at 4x/8x/16x compression on τ-bench plus standard accuracy on LongBench/MMLU.\\n\\n**ICLR 2027 full paper (extension, ~September 2026):** Expands to 2 models (add DeepSeek-R1-0528-Qwen3-8B — same Qwen3 GQA architecture, DeepSeek-R1-0528 tokenizer), 3 baselines (add uniform mixed-precision; add ThinKV if code releases), 9 benchmarks (add SWE-bench Lite 50 instances via SWE-agent, AIME 2025, MATH-500, HumanEval, MT-Bench, WikiText/C4 perplexity), full ablations, and attention entropy fallback for phase detection. ~200 H100-hours total including sprint work.\",\n  \"project_name\": \"trajcomp_agentic_kvcache\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL NOVELTY GAP: ThinKV (ICLR 2026 Oral) already jointly applies quantization and eviction conditioned on reasoning thought types (reasoning/execution/transition), with temporal adaptation as thoughts evolve. The proposal's claim that 'no prior work formulates a co-optimization objective that jointly learns sparsity masks and per-token precision for reasoning KV caches, conditioned on the temporal phase of reasoning' is false — ThinKV does exactly this, just without a formal Lagrangian.\", \"MISSING CRITICAL COMPETITOR: HqeKV (ACL ARR Jan 2026) proposes an integrated optimizer that jointly selects the optimal compression action (quantization level or eviction) per cached element under memory constraints, with a joint K-V importance metric. This is essentially the same optimization problem TSQC claims to solve first.\", \"MISSING CRITICAL COMPETITOR: ARKV (arXiv Feb 2026) dynamically assigns tokens to three states (Original/Quantization/Eviction) based on per-layer attention dynamics, achieving 4x compression with 97% accuracy — a lighter-weight version of the same joint decision.\", \"MISSING CRITICAL COMPETITOR: TriAttention (MIT/NVIDIA, April 2026) achieves 10.7x KV memory reduction on AIME25 with matched accuracy using a fundamentally different approach (trigonometric compression), setting a very high baseline that TSQC must beat.\", \"MISSING COMPETITOR: KVTC (NVIDIA, ICLR 2026) already achieves 20x compression on reasoning benchmarks (AIME25, MATH-500, LiveCodeBench) — matching TSQC's claimed 15-20x target — through PCA + adaptive quantization + entropy coding, without any sparsity mechanism.\", \"RESOURCE MISMATCH: User specifies ≤200 H100-hours. The proposal estimates in A100-hours (300h manual, 700h auto). While 300 A100-hours ≈ 150 H100-hours for this workload type, the proposal should have been stated in H100-hours per the user's constraint.\", \"TIMELINE RISK: Writing a fused CUDA kernel for joint sparsity-quantization with dual gradient descent in 16 days (for the EMNLP deadline) is unrealistic. Even the proposal acknowledges this is a 'stretch target only.'\", \"COMPRESSION TARGET NOT NOVEL: The claimed 15-20x compression with <2% accuracy loss is already achieved by ThinKV (20x) and KVTC (20x) individually. The 'multiplicative compression' argument (sparsity × quantization) is the same strategy these works already employ.\", \"EVALUATION GAPS: The proposal uses AIME 2025, MATH-500, GPQA, LiveCodeBench but omits LongBench and RULER from the user's required evaluation suite. The user explicitly listed these benchmarks.\", \"The attention-entropy-based phase detector (exploration vs. convergence) is underspecified. 'Not All Bits Are Equal' (ICLR 2026) shows that the optimal compression strategy is scale-dependent — the proposal doesn't address how TSQC adapts across the 8B-27B range.\", \"The landscape section strategically describes ThinKV as treating quantization and eviction 'as separate strategies within a pipeline,' which understates ThinKV's contribution — ThinKV's thought-aware compression is jointly designed even if not formulated as a Lagrangian.\"]\nFeedback: The fundamental problem is that this idea arrives too late to a very crowded space. ThinKV (ICLR 2026 Oral) is the most damaging competitor — it already performs reasoning-phase-aware joint quantization-eviction and achieves 20x compression. To differentiate TSQC, the generator must:\n\n1. **Honestly acknowledge ThinKV as the primary baseline** and clearly articulate why a Lagrangian co-optimization beats ThinKV's pipeline. The current framing that 'no prior work formulates a co-optimization objective' is misleading given ThinKV and HqeKV.\n\n2. **Add HqeKV, ARKV, TriAttention, and KVTC as baselines.** Missing these 2026 works in a May 2026 submission would be flagged by any reviewer.\n\n3. **Reframe the contribution** away from 'first to jointly optimize' (which is false) toward: (a) the Lagrangian formulation yields provably Pareto-optimal tradeoffs whereas ThinKV's pipeline is heuristic — demonstrate this with Pareto frontier plots; (b) the continuous relaxation enables smooth budget interpolation that discrete pipeline approaches cannot.\n\n4. **Address the 'Not All Bits Are Equal' (ICLR 2026) findings** about scale-dependent optimal strategies — how does TSQC handle the 8B vs 27B regime difference?\n\n5. **Include LongBench and RULER** in the evaluation per user requirements. Also add perplexity (Wiki/C4), MMLU, HumanEval, and MT-Bench as specified by the user.\n\n6. **Target AAAI 2027 or ICLR 2027** as primary (as the proposal already suggests), not EMNLP 2026 — 16 days is insufficient for CUDA kernel development + comprehensive evaluation.\n\n7. **Consider pivoting**: given how crowded this space is, the strongest angle might be applying the Lagrangian co-optimization framework to a less-explored setting — e.g., agent-loop KV caches with cross-turn reuse, or multi-modal reasoning KV caches — where ThinKV/HqeKV/ARKV haven't been validated.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"VENUE MISMATCH: User explicitly requested EMNLP 2026 (ARR deadline May 25, 2026). The proposal targets AAAI 2027 (Aug 2026) and ICLR 2027 instead. While Round 1 feedback correctly suggested retargeting, the proposal should still acknowledge the user's requirement and explain why the pivot was necessary, or propose a feasible EMNLP 2026 submission scope.\", \"MISSING COMPETITOR — TTKV (April 2026): Temporal-Tiered KV Cache partitions the cache into temporal tiers with heterogeneous precision, assigning recent KV states to higher-precision tiers based on temporal proximity. This directly overlaps with TrajComp's 'decaying context' category (4-bit → 2-bit → evict based on temporal distance). TTKV must be cited and differentiated.\", \"MISSING COMPETITOR — TRIM-KV / 'Cache What Lasts' (Dec 2025, ICLR 2026): Learns per-token retention scores with exponential temporal decay via lightweight retention gates. This is conceptually similar to TrajComp's importance-weighted temporal decay model, though TRIM-KV doesn't do joint quantization-eviction. Must be cited.\", \"MISSING COMPETITOR — EpiCache (Apple, Sep 2025): Episodic KV cache management for long conversational QA that clusters conversation history into coherent episodes with per-episode compression. This addresses multi-turn KV cache management — a closely related problem. Generator should cite and differentiate.\", \"MISSING COMPETITOR — RateQuant (May 2026): Uses rate-distortion theory for optimal mixed-precision KV cache quantization with per-head closed-form bit allocation. The Lagrangian/rate-distortion framework is conceptually adjacent to TrajComp's dual-constrained optimization. Must be discussed.\", \"MISSING COMPETITOR — Transactional Attention (April 2026): Uses structural anchor patterns to protect value-bearing tokens from eviction, achieving 100% credential retrieval where all attention-based eviction methods fail. TrajComp's 'persistent anchors' category performs a similar function. Should be cited.\", \"MISSING COMPETITOR — PBKV (May 2026) and KVFlow: Prediction-based KV cache management for dynamic agent workflows that predicts future agent invocations to optimize cache retention. These represent the systems-level competing approach to TrajComp's compression-level approach for agentic workloads.\", \"WEAK MOTIVATION EVIDENCE: The core error compounding claim (94.2% → 76.1% over 50 steps at 2-bit) traces to a blog post (dasroot.net), not a peer-reviewed paper. The numbers appear to be from visual planning/robotic manipulation tasks (DINO-WM, Inovo robot), not LLM agent tasks. Using non-peer-reviewed evidence for LLM-irrelevant tasks to motivate the core contribution is risky for a top venue submission.\", \"EVALUATION SCOPE vs COMPUTE BUDGET MISMATCH: Evaluating 4 models × 8+ baselines × 3 agentic benchmarks (SWE-bench Verified ~500 instances, GAIA ~450 tasks, τ-bench) + 8 standard benchmarks is far more than 150 H100-hours. SWE-bench alone at 3-5 min/instance × 500 × 12 configs (4 models × 3 compression levels) ≈ 300-500 GPU-hours just for one baseline comparison. The compute budget must either increase substantially or the evaluation scope must be reduced.\", \"γ ESTIMATION UNDERSPECIFIED: The cross-step error propagation rate γ is described as 'empirically estimated' but no method is given. This is a critical hyperparameter — if γ requires per-model, per-task calibration, it undermines the method's generality and adds substantial hidden compute cost.\", \"PATTERN MATCHING FOR PHASE DETECTION IS FRAGILE: The proposal detects agent phases via 'lightweight pattern matching on special tokens and turn boundaries.' This works for structured agent frameworks but will fail for free-form reasoning models (e.g., DeepSeek-R1) where thinking and acting are interleaved without clear delimiters. SideQuest's model-driven approach is more robust here.\", \"USER REQUIREMENT: evaluation must include perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench — these are now included in the proposal, which addresses Round 1 feedback. However, reporting wall-clock and throughput on H100 is also required and not discussed in the approach section.\"]\nFeedback: The pivot to agentic workloads is the right strategic move — this is genuinely less crowded than single-turn reasoning compression. The cross-step error propagation Lagrangian is a real contribution. However, several issues need addressing:\n\n1. **Cite 6 missing competitors**: TTKV, TRIM-KV, EpiCache, RateQuant, Transactional Attention, and PBKV/KVFlow. Position TrajComp against each: TTKV does temporal tiering but not joint optimization under a trajectory-error budget; TRIM-KV learns temporal decay but only for eviction, not joint quant-eviction; EpiCache does episodic multi-turn management but not cross-step error propagation; RateQuant uses rate-distortion theory but only for single-step bit allocation; Transactional Attention protects structural anchors but without trajectory-level optimization.\n\n2. **Strengthen the core motivation**: Replace the blog post citation (dasroot.net) with peer-reviewed evidence. PM-KVQ (ICLR 2026) demonstrates cumulative quantization error in long-CoT. 'How Much Cache Does Reasoning Need?' (April 2026) provides theoretical bounds on error scaling under KV compression. Use these to justify the trajectory-level objective.\n\n3. **Reduce evaluation scope or increase compute budget**: The current 4-model × 8-baseline × 11-benchmark matrix cannot be completed in 150 H100-hours. Either: (a) focus on 2 models (Qwen3-8B, DeepSeek-R1-Distill-8B) and 3-4 key baselines (ThinKV, HqeKV, SideQuest, CodeComp) with full agentic + standard eval; or (b) request 400+ H100-hours.\n\n4. **Specify γ estimation**: Propose a concrete calibration procedure — e.g., run 10 agent trajectories with and without compression at step boundaries, measure attention distribution divergence propagation, fit γ per model.\n\n5. **Address venue**: Either (a) propose a reduced scope for EMNLP 2026 ARR May 25 submission (2 models, 3 baselines, subset of benchmarks, targeting Findings) or (b) explicitly justify the AAAI 2027 pivot against the user's original requirement.\n\n6. **Add wall-clock and throughput reporting** as the user requires — describe how the Lagrangian solver overhead will be benchmarked and reported relative to baselines.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — ROUND 2 FEEDBACK NOT ADDRESSED: Round 2 gave 6 specific action items: (1) cite TTKV, TRIM-KV, EpiCache, RateQuant, Transactional Attention, PBKV; (2) replace blog post motivation with peer-reviewed evidence; (3) fix compute/scope mismatch; (4) specify γ estimation; (5) address venue; (6) add wall-clock/throughput reporting. None were acted on. This is a serious process failure — reviewers will expect iterative improvement.\", \"MISSING CRITICAL COMPETITOR — ForesightKV (arXiv Feb 2026, OpenReview): Learns long-term contribution of tokens for KV cache eviction in reasoning models via supervised learning + RL. Formulates cache eviction as a Markov Decision Process considering future impact of eviction decisions. This is conceptually parallel to TrajComp's cross-step error propagation model — both consider how current compression decisions affect future steps. ForesightKV must be cited and differentiated (it does eviction only, not joint quant-eviction; it uses RL not Lagrangian optimization; it targets single-turn reasoning, not multi-step agentic workloads).\", \"STILL MISSING 6 COMPETITORS FROM ROUND 2: (1) TTKV (March 2026) — temporal tiering with heterogeneous precision directly overlaps with 'decaying context' category; (2) TRIM-KV/Cache What Lasts (ICLR 2026) — learned per-token retention with temporal decay, conceptually similar to cross-step importance decay; (3) RateQuant (May 2026) — rate-distortion theory for optimal bit allocation, Lagrangian-adjacent framework; (4) Transactional Attention (April 2026) — structural anchor protection for value-bearing tokens, overlaps with 'persistent anchors'; (5) EpiCache (Apple, Sep 2025) — episodic multi-turn cache management; (6) PBKV (June 2026) — prediction-based KV cache for dynamic agent workflows. All confirmed real via independent search.\", \"MISSING COMPETITOR — LookaheadKV (ICLR 2026 Poster, Samsung): Predictive eviction using lookahead tokens + LoRA to predict future attention patterns. Achieves <0.7% performance drop at 81% compression. Relevant because it also considers future token importance, though via prediction rather than trajectory-level optimization.\", \"CORE MOTIVATION STILL FROM BLOG POST: The 94.2% → 76.1% error compounding figure still traces to dasroot.net, a blog post about visual planning/robotic manipulation — NOT LLM agent tasks. Round 2 explicitly flagged this and suggested PM-KVQ (ICLR 2026) and 'How Much Cache Does Reasoning Need?' (April 2026, arXiv:2604.17935) as peer-reviewed alternatives. Neither has been incorporated.\", \"COMPUTE BUDGET vs EVALUATION SCOPE — CRITICAL MISMATCH: Independent estimation shows the evaluation matrix requires 500-2600+ H100-hours: SWE-bench Verified (500 instances × 4 models × multiple configs ≈ 80-120h), RULER (39,000 samples ≈ 260h for 4 models), GAIA (≈120-160h), plus standard benchmarks, plus 8+ baselines each requiring their own evaluation runs. The claimed 150h budget covers roughly 10-25% of this scope. Even the user's 200h constraint requires drastic scope reduction.\", \"γ ERROR PROPAGATION RATE STILL UNSPECIFIED: The cross-step error propagation rate γ is the single most critical hyperparameter — it determines how compression decisions at step t are weighted across future steps. No calibration procedure is given. If γ requires per-model, per-task calibration, this adds substantial hidden compute cost and undermines the method's generality. Round 2 suggested a concrete procedure (10 agent trajectories, measure attention divergence propagation, fit γ) but this was not adopted.\", \"LAGRANGIAN TECHNIQUE OVERLAP WITH MixedDimKV: MixedDimKV (March 2026, cited in the proposal) already formulates KV cache compression as a constrained optimization problem using Lagrangian dual decomposition with bisection search over λ. TrajComp uses the same optimization technique. The differentiation (trajectory-level objective vs per-step objective) is real but the proposal doesn't adequately discuss this overlap or prove the trajectory extension yields meaningfully better solutions.\", \"VENUE MISMATCH PERSISTS: User explicitly requested EMNLP 2026 (ARR May 25, 2026). Proposal targets AAAI 2027 (August 2026, dates NOT YET ANNOUNCED per my search) and ICLR 2027. The pivot is defensible but must be explicitly justified with a feasible reduced-scope EMNLP 2026 option (e.g., 2 models, 3 baselines, focus on agentic benchmarks, target Findings).\", \"PHASE DETECTION FRAGILITY UNADDRESSED: Pattern matching on special tokens and turn boundaries works for structured agent frameworks (e.g., ReAct with explicit Thought/Action/Observation tags) but fails for free-form reasoning models like DeepSeek-R1 where thinking and acting interleave without clear delimiters. SideQuest's model-driven approach is more robust. The proposal needs a fallback strategy or attention-based phase detection.\", \"WALL-CLOCK AND THROUGHPUT REPORTING NOT DISCUSSED: User explicitly requires reporting wall-clock and throughput on H100. The Lagrangian solver overhead at each agent step boundary must be benchmarked and reported relative to baselines. How does re-optimization cost scale with KV cache size and number of agent steps?\"]\nFeedback: The trajectory-level Lagrangian formulation for agentic KV caches remains the genuine contribution here, but this is Round 3 and none of the Round 2 feedback was addressed. The generator must fix this immediately:\n\n1. **Cite all missing competitors with explicit differentiation**: ForesightKV (learns long-term contribution via RL, but eviction-only and single-turn — TrajComp's joint quant-eviction + multi-step Lagrangian is broader), TTKV (temporal tiering but no trajectory-level error budget), TRIM-KV (learned temporal decay but eviction-only), RateQuant (rate-distortion optimal bit allocation but single-step), Transactional Attention (structural anchors but no trajectory optimization), PBKV/KVFlow (prediction-based agent cache scheduling but no compression), LookaheadKV (future-aware eviction but no quantization), MixedDimKV (Lagrangian dual but per-step not trajectory-level). The landscape section must honestly acknowledge that MixedDimKV uses the same Lagrangian technique and clearly articulate why the trajectory-level extension is non-trivial.\n\n2. **Replace blog post motivation NOW**: Use 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) for theoretical error scaling bounds, PM-KVQ for empirical evidence of cumulative quantization error in long-CoT, and ForesightKV's motivation section for evidence that local eviction decisions degrade long-horizon reasoning.\n\n3. **Drastically reduce evaluation scope to fit 200 H100-hours**: Focus on 2 models (Qwen3-8B, DeepSeek-R1-Distill-8B), 4 key baselines (ThinKV, HqeKV, SideQuest, ForesightKV), and 6 benchmarks: 2 agentic (SWE-bench Lite ~300 instances, τ-bench), 2 reasoning (AIME 2025, MATH-500), 1 long-context (LongBench), 1 general (MMLU). Drop GAIA (too expensive), RULER (260 H100-hours alone), and reduce baseline count. This makes ~150-200 H100-hours realistic.\n\n4. **Specify γ calibration concretely**: Run N=10 agent trajectories per model with full KV cache and with compressed KV cache at step boundaries. Measure KL divergence of attention distributions at each step. Fit γ = median(KL_{t+1}/KL_t) across steps and trajectories. Report sensitivity analysis: does γ vary by >20% across tasks? If so, per-task calibration is needed and the cost must be budgeted.\n\n5. **Address phase detection robustness**: For structured agent frameworks (ReAct), use special token patterns. For free-form reasoning (DeepSeek-R1), fall back to attention entropy thresholds or turn-boundary detection. Acknowledge the limitation explicitly and benchmark both strategies.\n\n6. **Add wall-clock/throughput section**: Report Lagrangian solver time per agent step (expected: milliseconds for dual gradient descent over ~100K tokens), end-to-end latency per agent step, and tokens/second throughput. Compare against baselines on H100.\n\n7. **Decide venue**: Either (a) propose a reduced-scope EMNLP 2026 Findings submission (2 models, 3 baselines, 4 benchmarks, 14 days) or (b) explicitly state that AAAI 2027/ICLR 2027 is the target with justification. Do not leave this ambiguous.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"COMPUTE BUDGET REMAINS TIGHT: Independent estimation shows SWE-bench Lite at 2.5 min/instance with 8B models in multi-turn agentic evaluation is 2-5x too optimistic. Multi-turn agent interactions (100+ turns per SWE-bench instance for competitive agents, and 8B models need more turns than frontier models) realistically take 5-15 min/instance. This alone could push SWE-bench from 63h to 125-315h. Combined with inadequate dev/debug buffer (16h for reimplementing 4 baselines is unrealistic — 40-80h is more appropriate), the true compute need is 290-500+ H100-hours. Either reduce SWE-bench instances (e.g., 100 instead of 300), use a simpler agent scaffold, or honestly budget 300-400h.\", \"MISSING COMPETITOR — CapKV (April 2026, arXiv:2604.25975): Uses the Information Bottleneck principle to derive a closed-form mutual information objective for KV cache eviction with capacity-aware scoring. Provides a competing theoretically-grounded framework for principled KV cache management. Should be cited and differentiated (CapKV is eviction-only and per-step; TrajComp does joint quant-eviction with trajectory-level objective).\", \"USER EVALUATION REQUIREMENTS PARTIALLY UNMET: The user explicitly required perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. The proposal drops Wiki/C4 perplexity, HumanEval, RULER, and MT-Bench. While the scope reduction is justified by compute constraints, the proposal should explicitly acknowledge which user-required benchmarks are dropped and why, and suggest how they could be added in a follow-up or with additional compute.\", \"VENUE MISMATCH: The user explicitly requested EMNLP 2026 (ARR May 25, 2026). The proposal correctly identifies this as infeasible at 14 days but the minimal EMNLP 2026 Findings plan ('only if the Lagrangian solver is already implemented') is vague. Either provide a concrete 14-day sprint plan (what exactly would be submitted, which experiments, how many pages) or clearly state this is not the target and the user should accept AAAI 2027 / ICLR 2027 instead.\", \"SWE-BENCH AGENT SCAFFOLD UNSPECIFIED: The proposal evaluates on SWE-bench Lite but never specifies what agent scaffold will be used. The per-instance timing, number of agent steps, and therefore the relevance of trajectory-level compression all depend critically on the agent design. A lightweight single-pass agent (which might justify 2.5 min/instance) would produce short trajectories where trajectory-level optimization may show minimal benefit over per-step methods — undermining the core contribution. A full multi-turn agent scaffold (ReAct with tool use) would better showcase the contribution but costs much more. This tradeoff must be explicitly addressed.\", \"γ SENSITIVITY AND GENERALITY RISK: The γ calibration procedure (10 trajectories, KL divergence ratio) is now concrete, but the proposal notes 'if γ varies by >20% across tasks, use per-benchmark γ.' If γ is indeed task-dependent, this undermines the method's claim of being a general-purpose trajectory-level optimizer. The proposal should discuss what happens if γ varies by 50%+ across benchmarks — does the method degrade gracefully or fail?\"]\nFeedback: This is a substantially improved proposal — all Round 3 feedback items were addressed, the landscape analysis is now comprehensive and honest, and the technical specification is much more concrete. The contribution (trajectory-level Lagrangian for agentic KV caches) fills a genuine gap confirmed by thorough literature search. To reach pass quality:\n\n1. **Fix compute realism**: The SWE-bench timing is the critical weakness. Either (a) reduce to 100 SWE-bench Lite instances (still statistically meaningful, cuts from 63h to ~21h claimed / ~42-100h realistic), (b) explicitly specify a lightweight agent scaffold and acknowledge it produces shorter trajectories, or (c) honestly budget 300-350 H100-hours and justify to the user why 200h is insufficient for agentic benchmarks. Also increase dev/debug buffer to 40-60h.\n\n2. **Cite CapKV** (arXiv:2604.25975) — information-theoretic KV cache eviction. One line in landscape suffices.\n\n3. **Specify the agent scaffold**: Name the exact framework (e.g., SWE-agent, Agentless, OpenHands) and configuration (max turns, max tokens, tools available). This determines both cost and whether trajectory-level optimization has room to help.\n\n4. **Address user eval gaps explicitly**: Add a table showing user-required benchmarks, which are included vs dropped, and compute cost per dropped benchmark. This lets the user make an informed decision about scope.\n\n5. **Strengthen γ robustness**: Add a fallback for high γ variance: if γ varies >50%, degrade gracefully to per-step optimization (which should match MixedDimKV/ThinKV performance). This converts a failure mode into a guaranteed lower bound.\n\n6. **Sharpen EMNLP 2026 decision**: Either commit to a 14-day sprint plan (1 model, 2 baselines, 3 benchmarks, 6-page Findings submission) or explicitly drop EMNLP 2026 from target_venues entirely.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MISSING COMPETITOR — Neural Garbage Collection (arXiv:2604.18002, April 2026): Learns to evict KV cache entries during reasoning via RL, treating eviction decisions as actions within the reasoning chain. While NGC is training-required, eviction-only, and targets single-model reasoning (not agentic tool-use), it directly addresses trajectory-aware KV management and should be cited and differentiated. TrajComp's advantages: training-free, joint quant-eviction, multi-step agentic objective, structural phase exploitation.\", \"STILL MISSING CapKV (arXiv:2604.25975): Round 4 explicitly requested this citation. Information-theoretic KV cache eviction via Information Bottleneck principle. One-line citation and differentiation (eviction-only, per-step, no trajectory objective) would suffice.\", \"USER TIMELINE CONSTRAINT VIOLATED: User specified ≤16 days as a HARD CONSTRAINT. Proposal estimates 2.5-3.5 months (manual). The EMNLP 2026 contingency plan is vague ('only if Lagrangian solver already implemented'). Either propose a concrete 14-day sprint plan with drastically reduced scope (1 model, 2 baselines, 3 benchmarks, short paper) or explicitly acknowledge this constraint cannot be met and justify the venue pivot.\", \"USER-REQUIRED BENCHMARKS DROPPED WITHOUT ACKNOWLEDGMENT: User required perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Proposal keeps only MMLU and LongBench, dropping 4 of 6. Round 4 feedback asked for 'a table showing user-required benchmarks, which are included vs dropped, and compute cost per dropped benchmark.' This table is still missing.\", \"AGENT SCAFFOLD STILL UNSPECIFIED: Round 4 explicitly asked to 'Name the exact framework (e.g., SWE-agent, Agentless, OpenHands) and configuration (max turns, max tokens, tools available).' This determines cost, trajectory length, and whether trajectory-level optimization shows meaningful gains over per-step methods. A single-pass agent (Agentless) would undermine the core contribution; a multi-turn agent (SWE-agent) would exceed the timing estimates.\", \"FORESIGHTKV BASELINE REPRODUCTION COST NOT BUDGETED: ForesightKV requires supervised training + RL fine-tuning (GRPO). This is not a plug-and-play baseline — reproduction requires dataset construction, training infrastructure, and significant GPU time. Either budget 20-40h for reproduction, use their released checkpoint (if available), or replace with a reproducible alternative baseline.\", \"THEORETICAL CLAIM SLIGHTLY OVERSTATED: The proposal cites 'How Much Cache Does Reasoning Need?' for error bound Ω((n/s)^(T-1)) as motivation for agentic trajectory-level compression. My deep read confirms this bound applies to k-hop pointer chasing in single-model multi-step reasoning, not multi-step agentic tool-use workflows. The analogy is reasonable but the proposal should acknowledge the theoretical model doesn't directly map to agentic settings with external tool calls and observation injection.\"]\nFeedback: The proposal has matured significantly — the landscape is now among the most comprehensive I've seen (29+ papers), the γ calibration is concrete, the dual-constrained Lagrangian formulation is clean, and the differentiation from MixedDimKV is well-articulated. The core contribution (trajectory-level joint quant-eviction for agentic KV caches) fills a verified gap. To reach pass quality:\n\n1. **Cite Neural Garbage Collection** (arXiv:2604.18002): 'NGC (April 2026) learns trajectory-aware KV eviction via RL, jointly optimizing reasoning and memory management. TrajComp differs in three ways: training-free (vs. RL-required), joint quant-eviction (vs. eviction-only), and exploits agentic workflow structure (vs. single-model reasoning traces).' Also cite CapKV as requested in Round 4.\n\n2. **Resolve the timeline/venue crisis**: The user's 16-day hard constraint makes EMNLP 2026 the target. Either (a) propose a concrete 14-day sprint: Day 1-3 implement Lagrangian solver on top of vLLM/SGLang, Day 4-6 implement phase detection, Day 7-10 run experiments (1 model: Qwen3-8B, 2 baselines: ThinKV + SideQuest, 3 benchmarks: SWE-bench Lite 50-instance subset + AIME 2025 + MMLU), Day 11-14 write 4-page short paper for EMNLP 2026 Findings. ~60 H100-hours. OR (b) clearly state 'This idea requires AAAI 2027/ICLR 2027 targeting; EMNLP 2026 is not achievable' and accept the user may reject it.\n\n3. **Specify the agent scaffold**: Name it (e.g., 'SWE-agent with ReAct prompting, max 25 turns, max 16K tokens per turn'). This is essential for cost estimates and determines trajectory length.\n\n4. **Add user benchmark gap table**: Show which of the 6 user-required benchmarks are included (MMLU, LongBench) and which are dropped (perplexity, HumanEval, RULER, MT-Bench) with per-benchmark cost estimates. RULER alone would cost ~50-100h for 2 models.\n\n5. **Budget ForesightKV reproduction or replace**: If no public checkpoint exists, replace with a simpler future-aware baseline (e.g., attention-pattern-based eviction with lookahead window) that can be implemented in <8h.\n\n6. **Soften the theoretical analogy**: Note that the Ω((n/s)^(T-1)) bound from 'How Much Cache' applies to k-hop pointer chasing, which is an analogy (not a direct proof) for agentic trajectory error compounding. The empirical evidence from PM-KVQ and 'Hold Onto That Thought' is the stronger motivation.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"FACTUAL ERROR — MLA ARCHITECTURE CLAIM: The proposal states '2 models covering standard attention and MLA' for Qwen3-8B and DeepSeek-R1-Distill-Qwen3-8B. This is incorrect. DeepSeek-R1-Distill-Qwen3-8B uses Qwen3's standard GQA attention architecture, NOT MLA. MLA (Multi-head Latent Attention) is exclusive to the full DeepSeek-V3/R1 (671B MoE). Both evaluation models thus use standard attention variants, and the 'architecture-aware adaptation for MLA' contribution is not testable within the proposed evaluation. Either add a model that actually uses MLA (requires DeepSeek-V3/R1 at 671B, infeasible at 200 H100-hours) or remove the MLA adaptation claim entirely.\", \"STILL MISSING NGC (Round 5 request) AND CapKV (Rounds 4+5 requests): Neural Garbage Collection (arXiv:2604.18002) learns trajectory-aware KV eviction via RL — the closest conceptual competitor for trajectory-aware cache management, despite being eviction-only and training-required. CapKV (arXiv:2604.25975) provides a competing information-theoretic framework for principled KV cache eviction. Both were explicitly requested in previous rounds with suggested one-line differentiations provided. This repeated failure to address explicit reviewer requests is a process concern.\", \"AGENT SCAFFOLD STILL UNSPECIFIED (Rounds 4+5 requests): The exact agent framework (SWE-agent, Agentless, OpenHands) and configuration (max turns, max tokens, tools) for SWE-bench Lite evaluation is never named. This is critical because: (a) a single-pass agent like Agentless produces short trajectories where trajectory-level optimization shows minimal benefit — undermining the core contribution; (b) a multi-turn agent (SWE-agent with 25+ turns) would produce longer trajectories but costs 5-15 min/instance for 8B models, far exceeding the 2.5 min estimate; (c) the trajectory length directly determines whether TrajComp's cross-step optimization has room to outperform per-step methods.\", \"SWE-BENCH TIMING STILL OPTIMISTIC: 2.5 min/instance for multi-turn agentic evaluation with 8B models is 2-3x too low. CacheTTL's own data shows SWE-bench mini-agent traces have 'many turns with short (<2s) tool calls' but 8B models need more reasoning turns than frontier models. Realistic estimates: 5-10 min/instance with a proper multi-turn scaffold, pushing SWE-bench from 63h to 125-250h alone. This makes the 200 H100-hour budget infeasible unless instances are reduced to ~100-150.\", \"FORESIGHTKV BASELINE REPRODUCTION COST UNBUDGETED (Round 5 request): ForesightKV requires supervised training (golden eviction labels) + RL fine-tuning (GRPO). No public checkpoint for Qwen3-8B or DeepSeek-R1-Distill-8B is confirmed. Reproducing it could cost 30-50 H100-hours. Either verify a public checkpoint exists, budget reproduction cost, or replace with a simpler future-aware baseline (e.g., attention-pattern lookahead).\", \"USER-REQUIRED BENCHMARKS GAP TABLE STILL MISSING (Rounds 4+5 requests): User explicitly required perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Proposal keeps MMLU and LongBench, drops 4 of 6. Rounds 4 and 5 asked for a table showing included vs. dropped benchmarks with per-benchmark compute cost estimates. This table is still absent. RULER alone costs ~50-100h for 2 models; HumanEval and MT-Bench are cheap (~2-3h each) and should arguably be included.\", \"VENUE MISMATCH STILL NOT FULLY RESOLVED: User's HARD CONSTRAINT was ≤16 days and EMNLP 2026. The proposal correctly identifies EMNLP 2026 as infeasible but the contingency plan is vague ('only if Lagrangian solver already implemented'). The proposal should either: (a) provide a concrete 14-day sprint plan (1 model, 2 baselines, 3 benchmarks, short paper for EMNLP Findings), or (b) explicitly state the user's 16-day constraint cannot be met and present AAAI 2027 (deadline TBD, expected July-August 2026) as the earliest feasible target.\", \"THEORETICAL ANALOGY STILL SLIGHTLY OVERSTATED: The Ω((n/s)^(T-1)) bound from 'How Much Cache Does Reasoning Need?' applies to k-hop pointer chasing in single-model multi-step reasoning with locality-respecting cache controllers. The paper explicitly does NOT address multi-agent tool-use workflows. The proposal uses this bound to motivate trajectory-level compression for agentic workloads — a reasonable analogy, but the proposal should explicitly note the theoretical model doesn't directly cover agentic settings with external tool calls and observation injection. The empirical evidence (PM-KVQ, 'Hold Onto That Thought') is the stronger motivation.\"]\nFeedback: The proposal has reached a high level of maturity — the landscape analysis is exceptional (29+ papers, honest differentiation), the core contribution is verified as novel, and the technical specification is concrete. Three issues block a pass:\n\n1. **Fix the MLA architecture error immediately**: DeepSeek-R1-Distill-Qwen3-8B uses Qwen3's GQA, not MLA. Remove the MLA adaptation claim from the contributions or replace the model with one that actually uses MLA (impractical at this budget). The simplest fix: state that TrajComp targets standard attention and GQA architectures in this work, with MLA adaptation as future work. Remove 'MLA' from the '2 models covering standard attention and MLA' description.\n\n2. **Cite NGC and CapKV** — this is the third time requested: 'NGC (April 2026, arXiv:2604.18002) learns trajectory-aware KV eviction via RL within single-model reasoning. TrajComp differs: training-free, joint quant-eviction, multi-step agentic objective.' 'CapKV (April 2026, arXiv:2604.25975) derives information-theoretic KV eviction via the Information Bottleneck principle. TrajComp differs: joint quant-eviction with trajectory-level objective vs. per-step information-theoretic eviction.'\n\n3. **Specify the agent scaffold and fix SWE-bench timing**: Name the framework (e.g., 'SWE-agent with ReAct prompting, max 30 turns, 16K tokens/turn'). Then re-estimate per-instance timing realistically (5-8 min for 8B multi-turn) and either reduce instances to 100-150 or increase compute budget to 250-300h. Add HumanEval and MT-Bench (~5h total) to partially address user benchmark requirements.\n\n4. **Add the user benchmark gap table**: |Benchmark|Status|Est. Cost|Reason for Drop| — show MMLU (included), LongBench (included), perplexity (dropped, ~3h, add it), HumanEval (dropped, ~2h, add it), MT-Bench (dropped, ~2h, add it), RULER (dropped, ~100h, compute prohibitive).\n\n5. **Soften the theoretical claim**: Add one sentence noting the Ω((n/s)^(T-1)) bound applies to k-hop pointer chasing, not directly to agentic tool-use, but provides theoretical grounding that cache compression errors compound across reasoning stages.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"PERSISTENT PROCESS FAILURE — 4 ROUNDS OF IGNORED FEEDBACK: NGC (arXiv:2604.18002), CapKV (arXiv:2604.25975), agent scaffold specification, and user benchmark gap table have been explicitly requested in Rounds 4, 5, 6, and now 7. None have been addressed. At Round 7/10, this pattern risks a 'fail' verdict by Round 10 regardless of idea quality, because inability to address reviewer feedback is itself a disqualifying signal for any venue.\", \"FACTUAL ERROR PERSISTS — MLA ARCHITECTURE CLAIM (Round 6 + 7): The evaluation section states '2 models covering standard attention and MLA' for Qwen3-8B and DeepSeek-R1-Distill-8B. This is factually wrong. DeepSeek-R1-Distill-Qwen3-8B uses Qwen3's GQA architecture (32 query heads, 8 KV heads), NOT MLA. MLA is exclusive to the full DeepSeek-V3/R1 671B MoE model. Contribution (3) 'Architecture-aware adaptation for standard attention and MLA architectures' is therefore untestable. The approach section correctly classifies both models as standard attention but contradicts itself in the evaluation scope.\", \"STILL MISSING NGC (4th request): Neural Garbage Collection (arXiv:2604.18002, April 2026) learns trajectory-aware KV eviction via RL, treating eviction as actions within reasoning chains. It achieves 2-3x compression on Countdown/AMC/AIME while jointly optimizing reasoning and memory. This is the closest conceptual competitor for trajectory-aware cache management. TrajComp's advantages (training-free, joint quant-eviction, multi-step agentic objective) must be explicitly stated.\", \"STILL MISSING CapKV (4th request): arXiv:2604.25975 derives capacity-aware KV eviction via the Information Bottleneck principle with statistical leverage scores. Provides a competing theoretically-grounded framework. One-line differentiation (eviction-only, per-step, no trajectory objective) suffices.\", \"AGENT SCAFFOLD STILL UNSPECIFIED (4th request): SWE-bench evaluation without naming the agent framework (SWE-agent, Agentless, OpenHands, etc.) and configuration (max turns, max tokens, tools) is incomplete. This is not a minor detail: (a) Agentless produces single-pass short trajectories where trajectory-level optimization has minimal room to help — undermining the core contribution; (b) SWE-agent with ReAct produces multi-turn trajectories but costs 5-15 min/instance for 8B models; (c) OpenHands with small models achieves only ~12% success rate, raising questions about whether there is enough headroom for meaningful compression comparisons.\", \"SWE-BENCH TIMING 4x TOO OPTIMISTIC: 2.5 min/instance is confirmed unrealistic by independent search — ~10 min/instance is typical for multi-turn agentic evaluation. This pushes SWE-bench from 63h to ~250h alone. With 5 methods × 2 models × 300 instances × 10 min = 500h just for SWE-bench. Either reduce to 50-100 instances or honestly budget 350+ H100-hours.\", \"USER BENCHMARK GAP TABLE STILL MISSING (4th request): User required perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Proposal includes only MMLU and LongBench. HumanEval (~2h) and MT-Bench (~2h) are cheap enough to include. Perplexity on Wiki/C4 is ~3h. RULER is prohibitively expensive (~100h). A simple table showing status/cost/reason-for-drop was requested 4 times.\", \"FORESIGHTKV BASELINE REPRODUCTION UNBUDGETED: Independent search found no public code or checkpoints for ForesightKV. Reproducing supervised training + RL fine-tuning (GRPO) for 2 models could cost 30-50 H100-hours. Either verify a public checkpoint, budget reproduction, or replace with a reproducible alternative (e.g., attention-pattern lookahead baseline).\", \"THEORETICAL CLAIM STILL OVERSTATED: The Ω((n/s)^(T-1)) bound from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) applies specifically to k-hop pointer chasing with locality-respecting cache controllers on single-model multi-step reasoning — NOT multi-step agentic tool-use workflows with external observation injection. The analogy is reasonable but the proposal presents it as direct motivation without this caveat. The empirical evidence (PM-KVQ, 'Hold Onto That Thought') is the stronger and more honest motivation.\", \"8B MODEL CAPABILITY CONCERN FOR AGENTIC BENCHMARKS: OpenHands achieves only ~12% on SWE-bench with models smaller than 32B. If both evaluation models (Qwen3-8B, DeepSeek-R1-Distill-8B) achieve very low base success rates, compression comparisons become statistically noisy and potentially meaningless. Consider including at least one stronger model (e.g., Qwen3-32B) or acknowledging this limitation and focusing on τ-bench where 8B models may perform better.\"]\nFeedback: This is Round 7 of 10. The core contribution — trajectory-level Lagrangian for joint quant-eviction in agentic KV caches — is verified as genuinely novel via extensive independent search. The landscape analysis is exceptional. However, this review MUST issue a strong warning: 4 specific feedback items (NGC, CapKV, agent scaffold, benchmark table) have been requested in every round since Round 4 and remain unaddressed. If this pattern continues through Round 9, the verdict will be 'fail' based on inability to address reviewer feedback, regardless of the idea's theoretical merit.\n\nTo pass in Round 8, the generator MUST address ALL of the following — no exceptions:\n\n1. **Cite NGC and CapKV** (copy-paste ready): 'NGC (April 2026, arXiv:2604.18002) learns trajectory-aware KV eviction via RL within single-model reasoning chains, jointly optimizing reasoning and memory management from task reward alone. TrajComp differs: training-free (vs. RL-required), joint quant-eviction (vs. eviction-only), and exploits agentic workflow structure with explicit step boundaries (vs. single-model reasoning traces).' 'CapKV (April 2026, arXiv:2604.25975) derives information-theoretic KV eviction via the Information Bottleneck principle with capacity-aware scoring. TrajComp differs: joint quant-eviction with trajectory-level objective vs. per-step information-theoretic eviction.'\n\n2. **Fix MLA error**: Change '2 models covering standard attention and MLA' to '2 models using GQA attention.' Remove MLA adaptation from contributions or relabel it as future work. The approach section can mention MLA as a design consideration but must not claim it is evaluated.\n\n3. **Specify agent scaffold**: 'We use SWE-agent with ReAct prompting, max 30 turns, 16K tokens per turn for SWE-bench Lite. For τ-bench, we use the official evaluation harness.' Then re-estimate per-instance timing realistically (8-12 min for 8B multi-turn on SWE-bench) and reduce instances to 100-150 to fit compute budget.\n\n4. **Add user benchmark gap table**: | Benchmark | Status | Est. Cost | Reason | MMLU: included, 5h | LongBench: included, 20h | HumanEval: ADD IT, 2h | MT-Bench: ADD IT, 2h | Perplexity (Wiki/C4): ADD IT, 3h | RULER: dropped, ~100h, compute-prohibitive |\n\n5. **Fix compute budget**: With realistic SWE-bench timing (100 instances × 10 min × 10 configs = ~167h) + τ-bench (~60h) + other benchmarks (~50h) + calibration (~10h) + dev/debug (~40h) = ~327h. Either request 300-350h with justification or cut SWE-bench to 50 instances.\n\n6. **Soften theoretical claim**: Add one sentence: 'We note that this bound applies to k-hop pointer chasing in single-model reasoning; its extension to agentic tool-use with external observation injection is an analogy, not a formal proof. The empirical evidence from PM-KVQ and Hold Onto That Thought provides the primary motivation.'\n\n7. **Address ForesightKV reproduction**: Either confirm a public checkpoint exists or replace with a simpler future-aware baseline (e.g., attention-pattern lookahead with sliding window) that can be implemented in <8h.\n\n### Round 8 review\nVerdict: revise\nIssues: [\"BASELINE REPRODUCTION RISK — ThinKV AND SideQuest HAVE NO PUBLIC CODE: Independent verification confirms neither ThinKV (ICLR 2026 Oral) nor SideQuest (Feb 2026) have released code, checkpoints, or implementations as of May 2026. ThinKV involves custom Triton kernels extending PagedAttention — reimplementation is non-trivial and could cost 20-40 H100-hours per baseline. Only R-KV and HqeKV have confirmed public code. Using 2 baselines without code in a 4-baseline plan creates significant execution risk.\", \"COMPUTE BUDGET 75% OVER USER CONSTRAINT: User specified ≤200 H100-hours as a HARD CONSTRAINT. Proposal requires ~350h. A concrete path to ~200h exists: reduce SWE-bench Lite to 50 instances (saves ~83h), reduce baselines from 4 to 3 by dropping either ThinKV or SideQuest (saves ~30-50h given no public code anyway), and tighten dev/debug buffer to 25h. Revised estimate: 50 SWE-bench × 2 models × 4 methods × 10min ≈ 67h + τ-bench 164 × 2 × 4 × 2min ≈ 44h + standard benchmarks ~40h + calibration 10h + ablations 15h + dev/debug 25h ≈ 201h.\", \"MODEL NAME ERROR: 'DeepSeek-R1-Distill-Qwen3-8B' does not exist. The correct model is 'DeepSeek-R1-0528-Qwen3-8B' (HuggingFace: deepseek-ai/DeepSeek-R1-0528-Qwen3-8B). It uses Qwen3-8B architecture with DeepSeek-R1-0528 tokenizer and achieves 86.0% on AIME 2024. The 'Distill' naming convention was used for Qwen2.5-based distillations, not Qwen3-based ones.\", \"VENUE AND TIMELINE MISMATCH: User's HARD CONSTRAINTS were ≤16 days and EMNLP 2026 (ARR May 25). Proposal explicitly declares EMNLP 2026 'NOT FEASIBLE' and targets AAAI 2027/ICLR 2027 — an honest acknowledgment, but this fundamentally fails to meet user requirements. The proposal should either commit to a drastically reduced EMNLP 2026 Findings sprint plan (1 model, 2 baselines with public code, 3 benchmarks, 4-page short paper, ~60h) or explicitly justify why this idea cannot serve the user's stated deadline.\"]\nFeedback: This is a dramatically improved proposal — all 7 Round 7 feedback items are fully addressed for the first time, the landscape is exceptional (30+ papers), NGC and CapKV are properly cited and differentiated, the MLA error is fixed, the agent scaffold is specified, and the benchmark gap table is included. The core contribution (trajectory-level Lagrangian for agentic KV caches) is confirmed novel via exhaustive search. The proposal is close to pass quality but blocked by feasibility concerns:\n\n1. **Fix baseline plan**: Replace ThinKV and/or SideQuest (no public code) with baselines that have confirmed code. Recommended 3-baseline plan: R-KV (public code, NeurIPS 2025), HqeKV (public code, ACL ARR 2026), and either (a) reimplemented ThinKV with 20-30h budgeted for Triton kernel development, or (b) a simpler proxy: uniform mixed-precision baseline (e.g., 4-bit/2-bit with attention-score-based partitioning) implementable in <8h. If ThinKV code releases before experiments begin (ICLR oral papers often release within months), add it.\n\n2. **Fit within 200 H100-hours**: Reduce SWE-bench Lite to 50 instances (still statistically meaningful for pass-rate differences >5%), reduce baselines to 3 (only those with public code or easy reimplementation), and tighten dev/debug to 25h. This yields ~200h.\n\n3. **Fix model name**: Change 'DeepSeek-R1-Distill-Qwen3-8B' to 'DeepSeek-R1-0528-Qwen3-8B' throughout. Verify tokenizer compatibility since it uses DeepSeek-R1-0528's tokenizer, not Qwen3's default.\n\n4. **Resolve venue**: Either (a) commit to EMNLP 2026 Findings with a concrete 14-day sprint: Day 1-4 implement Lagrangian solver + phase detection on vLLM, Day 5-8 run experiments (Qwen3-8B only, 2 baselines with public code: R-KV + HqeKV, 3 benchmarks: 30 SWE-bench instances + MMLU + LongBench), Day 9-12 write 4-page short paper, Day 13-14 polish. ~60 H100-hours. OR (b) explicitly state EMNLP 2026 is not achievable and present this as an AAAI 2027/ICLR 2027 submission, accepting the user may choose a different idea for their EMNLP deadline.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-12T01:42:53.209Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T01:42:53.209Z",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-12T01:42:53.265Z_

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

## Idea under review (round 9/10)
{
  "title": "Trajectory-Aware Joint Compression for Long-Horizon Agentic KV Caches",
  "core_problem": "Agentic LLM systems (coding agents, research agents, tool-use agents) maintain KV caches that grow across dozens of reasoning-and-action steps, often exceeding 100K tokens. Current KV cache compression methods — including strong joint quantization-eviction approaches like ThinKV, HqeKV, and ARKV, as well as future-aware eviction methods like NGC and LookaheadKV — were designed for single-turn or single-model inference and optimize per-step reconstruction error or per-step eviction quality independently. In multi-step agentic workloads, compression errors compound across planning steps: PM-KVQ (ICLR 2026) demonstrates that directly quantizing KV cache at each decoding step causes cumulative quantization error that degrades long-CoT reasoning by up to 8% versus progressive strategies; 'Hold Onto That Thought' (under review, ICLR 2026) empirically shows that existing KV compression strategies designed for prefill-phase long-context tasks degrade significantly on reasoning tasks requiring extended decoding. Theoretical analysis from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves lower bounds showing exponential error growth Ω((n/s)^(T-1)) for oblivious cache strategies across T reasoning stages in k-hop pointer chasing; we note that this bound applies specifically to single-model multi-step reasoning with locality-respecting cache controllers, not directly to agentic tool-use workflows with external observation injection — the analogy is suggestive but not a formal proof. The empirical evidence from PM-KVQ and 'Hold Onto That Thought' provides the primary, more directly applicable motivation. No existing work formulates joint quantization-eviction that explicitly minimizes cumulative trajectory-level error for agentic workloads.",
  "opportunity": "Two converging trends expose a clear research gap. First, agentic inference is now the dominant LLM deployment pattern (SWE-bench, GAIA, τ-bench), but KV cache compression research overwhelmingly targets single-turn inference. Existing agentic KV cache works address only parts of the problem: SideQuest (Feb 2026) uses model-driven eviction but not quantization; CodeComp (April 2026) leverages structural code priors for eviction only; CacheTTL (Nov 2025) manages cache scheduling without compression; PBKV (May 2026) predicts future agent invocations for cache management but performs no within-request compression; KVFlow (NeurIPS 2025) optimizes prefix caching for multi-agent workflows without compression; EpiCache (Apple, Sep 2025) manages episodic multi-turn cache but targets conversational QA, not agentic tool-use. NGC (April 2026) learns trajectory-aware KV eviction via RL within single-model reasoning chains, jointly optimizing reasoning and memory management from task reward alone — the closest conceptual competitor, but it requires RL training, is eviction-only (no quantization), and operates on single-model reasoning traces without explicit agent step boundaries or external observation injection. CapKV (April 2026) derives information-theoretic KV eviction via the Information Bottleneck principle with capacity-aware scoring — theoretically grounded but eviction-only and per-step.\n\nSecond, single-turn KV cache compression has matured across multiple fronts: (a) joint quantization-eviction via ThinKV (ICLR 2026 Oral, 20x compression), HqeKV (per-element compression actions), ARKV (tri-state assignment); (b) future-aware eviction via NGC (RL-based trajectory-aware eviction for single-model reasoning), LookaheadKV (ICLR 2026, predictive eviction via lookahead tokens + LoRA); (c) optimal bit allocation via RateQuant (rate-distortion reverse waterfilling, May 2026) and MixedDimKV (Lagrangian dual decomposition for per-token dimensions); (d) temporal and structural KV management via TTKV (temporal tiering with heterogeneous precision), TRIM-KV/Cache What Lasts (ICLR 2026, learned retention gates with temporal decay), and Transactional Attention (structural anchor protection for value-bearing tokens); (e) information-theoretic eviction via CapKV (Information Bottleneck with statistical leverage scores). However, none model how compression decisions at step t propagate errors to steps t+1 through T in multi-step agentic workflows with external tool observations. The key insight: in agentic workloads, token importance is cross-step structured in ways that single-turn methods cannot exploit. Instruction and plan tokens maintain importance across all steps; current-step observations are critical but rapidly decay; historical tool outputs become redundant as new observations arrive. This temporal structure, combined with the empirically-grounded error compounding problem (PM-KVQ, 'Hold Onto That Thought'), demands a fundamentally different optimization objective: minimizing trajectory-level degradation rather than per-step reconstruction error.",
  "landscape": "**Joint quantization-eviction (single-turn):** ThinKV (ICLR 2026 Oral) applies thought-adaptive hybrid quantization-eviction achieving 20x compression with <5% KV cache — the strongest single-turn baseline, but no public code as of May 2026 (partial proxy available via NVIDIA's kvpress library as 'ThinKPress'). HqeKV (ACL ARR Jan 2026) provides an integrated optimizer selecting optimal compression actions (quantization level or eviction) per cached element under memory constraints; **public code confirmed** (github.com/skywclouds/HqeKV). ARKV (arXiv Feb 2026) dynamically assigns tokens to Original/Quantization/Eviction states based on per-layer attention statistics. KVTC (ICLR 2026) achieves 20x via PCA + adaptive quantization + entropy coding.\n\n**Constrained optimization for KV compression:** MixedDimKV (March 2026) formulates KV cache compression as a constrained optimization problem using Lagrangian dual decomposition with bisection search over λ, allocating per-token dimensions under a memory budget. This uses the same Lagrangian optimization technique as TrajComp. The critical difference: MixedDimKV minimizes per-step reconstruction error (single-step objective), while TrajComp minimizes trajectory-level error accumulation across T agent steps (multi-step objective). The trajectory extension is non-trivial because: (i) the search space expands from per-step to cross-step — compressing token i at step t affects attention distributions at steps t+1...T; (ii) the objective changes from reconstruction fidelity to trajectory success rate; (iii) the importance model must account for temporal structure (persistent vs. decaying tokens) absent in single-turn settings. RateQuant (May 2026) applies rate-distortion theory with reverse waterfilling for optimal per-head bit allocation — a complementary per-step optimization that TrajComp could incorporate as a sub-routine for within-step bit allocation.\n\n**Trajectory-aware and future-aware eviction:** NGC (April 2026, arXiv:2604.18002) learns trajectory-aware KV eviction via RL, treating both reasoning tokens and cache-eviction decisions as discrete actions sampled from the language model, trained end-to-end from outcome-based task reward alone. On Countdown, AMC, and AIME, NGC achieves 2-3x peak KV cache compression while maintaining strong accuracy. TrajComp differs from NGC in three key ways: (1) training-free (Lagrangian optimization vs. RL training required), (2) joint quantization-eviction (vs. eviction-only), and (3) designed for multi-step agentic workflows with explicit step boundaries and external observation injection (vs. single-model reasoning traces where the model interleaves thinking and eviction). LookaheadKV (ICLR 2026, Samsung) predicts future attention patterns via trainable lookahead tokens + LoRA, achieving <0.7% drop at 81% compression — also eviction-only and single-turn.\n\n**Information-theoretic eviction:** CapKV (April 2026, arXiv:2604.25975) derives capacity-aware KV eviction via the Information Bottleneck principle, using a log-determinant approximation with statistical leverage scores under a linear-Gaussian surrogate of attention. It provides a theoretically grounded mechanism that replaces heuristic selection with capacity-maximization. TrajComp differs: joint quantization-eviction with a trajectory-level multi-step objective vs. CapKV's per-step information-theoretic eviction-only framework.\n\n**Temporal and structural KV management:** TTKV (March 2026) partitions KV cache into temporal tiers with heterogeneous precision across HBM/DRAM, achieving 76% latency reduction on 128K contexts. Its temporal tiering directly overlaps with TrajComp's 'decaying context' category — but TTKV is a system-level memory hierarchy approach without trajectory-aware error optimization. TRIM-KV/Cache What Lasts (ICLR 2026) learns per-token retention gates with temporal decay via distillation — conceptually similar to cross-step importance decay, but training-required, eviction-only, and single-turn. Transactional Attention (April 2026) protects structural anchor tokens (credentials, API keys) from eviction via semantic sponsorship — overlaps with TrajComp's 'persistent anchors' category, but is domain-specific to credential/configuration retention and does not perform compression.\n\n**Agentic KV cache management:** SideQuest (Feb 2026) uses the reasoning model itself to identify dispensable tokens, achieving 65% peak token reduction on agentic tasks — eviction only, no quantization, no public code. CodeComp (April 2026) uses Code Property Graph priors for structure-aware eviction in agentic coding — domain-specific and eviction only. CacheTTL/Continuum (Nov 2025) manages multi-turn cache scheduling with TTL-based retention. PBKV (May 2026) predicts future agent invocations and manages cache across workflow steps — system-level scheduling without within-request compression. KVFlow (NeurIPS 2025) optimizes prefix caching for multi-agent workflows. EpiCache (Apple, Sep 2025) manages episodic multi-turn cache for conversational QA. Agent Memory Below the Prompt (Feb 2026) persists Q4 KV caches across agents on edge devices. KVComm (Oct 2025) enables cross-context KV sharing.\n\n**Other relevant methods:** TriAttention (MIT/NVIDIA, April 2026) achieves 10.7x via trigonometric key importance scoring. R-KV (NeurIPS 2025) achieves 100% accuracy at 10% KV via redundancy-aware eviction with **public code** (github.com/Zefan-Cai/R-KV, 1.2k stars, vLLM/SGLang/FlashInfer integrations). DMS (NeurIPS 2025) achieves 8x with lightweight training. EVICPRESS (Microsoft, Dec 2025) jointly optimizes compression and eviction across storage tiers but has no public code. PM-KVQ shows progressive mixed-precision reduces cumulative quantization error in long-CoT. TurboQuant (ICLR 2026) addresses inner-product estimation bias compounding across attention computations. 'Not All Bits Are Equal' (ICLR 2026) shows optimal compression strategy is scale-dependent.\n\n**Error compounding theory and evidence:** 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves that under k-hop pointer chasing with cache size s, oblivious caches suffer exponential error growth Ω((n/s)^(T-1)). We note this bound applies specifically to k-hop pointer chasing with locality-respecting cache controllers in single-model multi-step reasoning; its extension to agentic tool-use with external observation injection is an analogy, not a formal proof. The empirical evidence from PM-KVQ (cumulative quantization error degrades long-CoT by up to 8%) and 'Hold Onto That Thought' (compression designed for prefill degrades extended-decoding reasoning) provides the primary and more directly applicable motivation for trajectory-aware compression.\n\n**Code availability summary for baseline selection:** Of the methods considered as baselines, only R-KV (github.com/Zefan-Cai/R-KV, 1.2k stars) and HqeKV (github.com/skywclouds/HqeKV) have confirmed public implementations. ThinKV has a partial proxy (ThinKPress in NVIDIA kvpress) but no full implementation. SideQuest, EVICPRESS, and ForesightKV have no public code. This directly constrains baseline selection to methods with verified reproducibility.\n\nNo prior work formulates a trajectory-level objective for joint quantization-eviction in agentic KV caches with explicit cross-step error accumulation control. The closest works are NGC (trajectory-aware but RL-required, eviction-only, single-model) and MixedDimKV (same Lagrangian technique but per-step objective). TrajComp uniquely combines: (1) joint quant-eviction, (2) trajectory-level multi-step objective, (3) training-free Lagrangian optimization, (4) agentic workflow structure exploitation.",
  "approach": "We propose TrajComp (Trajectory-Aware Joint Compression), which formulates a single dual-constrained Lagrangian objective jointly optimizing token retention probabilities and per-token bit allocation under memory and cumulative trajectory-error budgets. We commit to a two-phase evaluation strategy: a focused EMNLP 2026 short paper sprint (ARR May 25 deadline, 13 days), followed by an extended ICLR 2027 full paper.\n\n**(1) Cross-step error propagation model:** Unlike ThinKV/HqeKV/MixedDimKV which minimize per-step reconstruction error independently, and unlike NGC which learns trajectory-aware eviction through RL training, TrajComp models error propagation across agent steps in a training-free manner. Compressing token i at step t contributes weighted error proportional to Σ_{s=t+1}^{T} γ^{s-t} × importance_i, where γ is the empirically-calibrated step-wise error propagation rate. The dual-constrained Lagrangian L = Σ_t error_t(s,q) + λ_mem(M(s,q) - B_mem) + λ_err(E_cumul(s,q,γ) - B_err) enables smooth Pareto-optimal tradeoffs via dual gradient descent on both multipliers. Note: MixedDimKV uses Lagrangian dual decomposition with bisection for a single memory constraint and per-step objective; TrajComp extends this to dual constraints (memory + trajectory error) with a cross-step objective, requiring the error propagation model as additional machinery.\n\n**γ calibration procedure:** For Qwen3-8B (EMNLP sprint), run N=5 agent trajectories on a τ-bench subset with full (uncompressed) KV cache and with uniformly 4-bit quantized KV cache. At each agent step boundary t, measure KL divergence D_KL(P_full^t || P_compressed^t) of the attention distributions. Compute per-step propagation ratios r_t = D_KL^{t+1} / D_KL^t across all steps and trajectories. Set γ = median(r_t). Based on PM-KVQ's observations of progressive error accumulation, we expect γ ∈ [0.7, 0.95]. Calibration cost: ~2 H100-hours for the EMNLP sprint. For the ICLR extension, expand to N=10 trajectories per model-benchmark pair with sensitivity analysis (~10 H100-hours total for 2 models × 2 agentic benchmarks).\n\n**(2) Agent-phase token categorization:** Rather than ThinKV's within-turn thought types, TrajComp defines categories by agentic workflow structure: (a) Persistent anchors — system prompts, instructions, plans — never compressed (analogous to Transactional Attention's structural anchors, but generalized beyond credentials to all instruction-bearing tokens); (b) Active context — current tool output and recent reasoning — retained at 4-bit; (c) Decaying context — older observations — progressively compressed (4-bit → 2-bit → evict) with schedule determined by the Lagrangian solver based on temporal distance and cross-step importance (analogous to TTKV's temporal tiering, but driven by trajectory-level optimization rather than fixed temporal heuristics); (d) Ephemeral tokens — intermediate tool formatting, API boilerplate — immediately evicted.\n\n**Phase detection strategy:** For structured agent frameworks (ReAct, function-calling with explicit Thought/Action/Observation tags), use lightweight pattern matching on special tokens and turn boundaries (zero overhead). This covers both evaluation settings: τ-bench uses structured tool-calling, and SWE-agent uses ReAct prompting with explicit delimiters. For the EMNLP sprint, pattern matching suffices for all evaluated benchmarks. For the ICLR extension with free-form reasoning models, fall back to attention entropy thresholds: compute per-token attention entropy at step boundaries; tokens with consistently high entropy across recent steps are classified as ephemeral, tokens with low entropy as active/persistent.\n\n**(3) GQA-aware compression:** Qwen3-8B uses Grouped Query Attention (32 query heads, 8 KV heads). TrajComp allocates compression budgets at the KV-head group level, accounting for the fact that compressing a single KV head affects all 4 query heads in its group. For the ICLR extension, DeepSeek-R1-0528-Qwen3-8B uses the same GQA configuration (32 query heads, 8 KV heads, Qwen3 architecture) but with DeepSeek-R1-0528's tokenizer — we verify tokenizer compatibility for phase detection. MLA adaptation (for full DeepSeek-V3/R1 671B models) is left as future work.\n\nThe dual gradient descent operates at agent step boundaries (not every token), making it lightweight. A single re-optimization pass over the full KV cache occurs when a new agent step begins.\n\n**Wall-clock and throughput reporting:** We report: (a) Lagrangian solver time per agent step as a function of KV cache size — expected to be <10ms for dual gradient descent over ~100K tokens, dominated by importance score computation not the optimization itself; (b) end-to-end latency per agent step (including compression overhead) vs. baselines on H100-80GB; (c) tokens/second throughput at matched compression ratios.\n\n---\n\n**EMNLP 2026 SHORT PAPER SPRINT (Primary — ARR May 25, 2026)**\n\n13-day sprint for a 4-page short paper targeting EMNLP 2026 Findings:\n\n**Sprint timeline:**\n- Day 1-3 (May 12-14): Implement Lagrangian solver + phase detection on HuggingFace Transformers. Integrate R-KV (from public repo, pip-installable) and HqeKV (from public repo) as baselines.\n- Day 4-5 (May 15-16): γ calibration on Qwen3-8B with 5 τ-bench trajectories. Validate solver convergence.\n- Day 6-8 (May 17-19): Run experiments — τ-bench full (164 tasks × 3 methods: TrajComp, R-KV, HqeKV), LongBench, MMLU. Collect wall-clock numbers.\n- Day 9-11 (May 20-22): Write 4-page paper. Focus on: (1) trajectory-level Lagrangian formulation, (2) agent-phase categorization, (3) τ-bench results showing trajectory success rate at matched compression ratios.\n- Day 12-13 (May 23-24): Polish, add any ablations completed, finalize submission.\n- Day 14 (May 25): Submit to ARR with EMNLP 2026 venue declaration.\n\n**Sprint evaluation scope:**\n- Model: Qwen3-8B (single model — avoids DeepSeek tokenizer compatibility debugging under time pressure)\n- Baselines: R-KV (public code, github.com/Zefan-Cai/R-KV, 1.2k stars, pip-installable), HqeKV (public code, github.com/skywclouds/HqeKV) — both with confirmed public implementations\n- Benchmarks: τ-bench 164 tasks via official harness (primary agentic benchmark — 8B models achieve meaningful success rates on structured customer-service tasks), LongBench (long-context regression), MMLU (general capability regression)\n- Key metric: trajectory-level success rate at matched compression ratio on τ-bench; standard accuracy on LongBench/MMLU\n- Compression targets: 4x, 8x, 16x (3 operating points)\n\n**Sprint compute budget (~60 H100-hours):**\n- γ calibration: 5 trajectories × 2 configs × ~5 min ≈ 1h\n- τ-bench: 164 tasks × 3 methods × 3 compression ratios × ~2 min ≈ 49h\n- LongBench: ~3h\n- MMLU: ~1h\n- Wall-clock benchmarking: ~1h\n- Development/debugging: ~5h\n- Total: ~60 H100-hours\n\n**Sprint risk mitigation:**\n- R-KV's mature codebase (1.2k stars, vLLM integration) minimizes baseline setup time\n- τ-bench has an official evaluation harness — no custom scaffolding needed\n- Pattern-matching phase detection on τ-bench's structured tool-calling is trivially implementable\n- If HqeKV integration proves difficult (CUDA kernel compilation), fall back to HqeKV's non-CUDA mode or replace with attention-score-based uniform mixed-precision (4-bit/2-bit partitioning, implementable in <4h)\n\n---\n\n**ICLR 2027 FULL PAPER EXTENSION (Secondary — expected deadline ~September 2026)**\n\nExpands the EMNLP sprint results into a full 8-page paper:\n\n- Add model: DeepSeek-R1-0528-Qwen3-8B (same GQA architecture, DeepSeek-R1-0528 tokenizer — verify phase detection compatibility)\n- Add baseline: Uniform mixed-precision (attention-score-based 4-bit/2-bit partitioning, implementable in <8h — serves as ablation baseline showing the value of trajectory-aware optimization over naive mixed-precision)\n- Add benchmarks: SWE-bench Lite 50 instances via SWE-agent (ReAct, 30 turns, 16K tokens/turn), AIME 2025, MATH-500, HumanEval, MT-Bench, WikiText/C4 perplexity\n- Add ablations: phase detection accuracy, γ sensitivity, anchor ratio impact, component-wise ablation\n- Add attention entropy fallback for phase detection (for future free-form reasoning evaluation)\n- If ThinKV releases official code before experiments begin, add as 4th baseline\n\n**ICLR extension compute (~140 additional H100-hours, ~200h total including sprint):**\n- SWE-bench Lite: 50 instances × 2 models × 4 methods × ~10 min ≈ 67h\n- τ-bench extension: 164 tasks × 1 additional model × 4 methods × ~2 min ≈ 22h\n- Additional benchmarks (AIME, MATH-500, HumanEval, MT-Bench, perplexity): ~20h\n- Extended γ calibration: ~8h\n- Ablations: ~15h\n- Dev/debug buffer: ~10h\n- Total extension: ~142h → ~200h cumulative\n\n**8B model capability consideration:** We acknowledge that 8B models achieve relatively low base success rates on SWE-bench (~17%). For the EMNLP sprint, we avoid SWE-bench entirely, using τ-bench as the primary agentic benchmark where 8B models achieve higher success rates on structured tasks. For the ICLR extension, we supplement binary SWE-bench success with trajectory-quality metrics (steps completed before failure, tool-call coherence, attention distribution divergence from full-cache trajectories).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~60h H100-80GB (EMNLP sprint); ~200h total (including ICLR extension)",
      "gpu_utilization": "50-60% effective — τ-bench instances run quickly (~2 min each); gaps filled with MMLU/LongBench evaluation",
      "timeline": "13 days for EMNLP sprint; 4 months total for ICLR extension",
      "team": "1 researcher with systems ML background",
      "estimated_gpu_cost": "$150 (60h × ~$2.50/h EMNLP sprint); $500 total with ICLR extension"
    },
    "human_in_loop": {
      "gpu_hours": "~60h H100-80GB (EMNLP sprint); ~200h total",
      "gpu_utilization": "60-70% — agent handles R-KV/HqeKV integration from public repos, τ-bench harness setup, γ calibration runs; human guides Lagrangian formulation and paper writing",
      "timeline": "13 days for EMNLP sprint (human: ~2h/day for formulation + writing); 3 months for ICLR extension",
      "team": "1 researcher, ~2h/day during sprint, ~45min/day during extension",
      "claude_api_cost": "$80-120 for sprint (~800-1200 turns); $300-500 total with extension",
      "estimated_gpu_cost": "$150 sprint; $500 total",
      "risk_note": "Primary sprint risk: HqeKV CUDA kernel compilation may require debugging. Mitigation: fall back to HqeKV non-CUDA mode or replace with uniform mixed-precision baseline (~4h to implement). R-KV is pip-installable and battle-tested (1.2k stars). τ-bench has an official harness with minimal setup."
    },
    "auto_research": {
      "gpu_hours": "~80h H100-80GB (automated sprint with wider γ sweep); ~250h total with ICLR extension",
      "gpu_utilization": "55-65% — τ-bench instances create pipeline gaps; agent queues MMLU/LongBench during gaps",
      "timeline": "10-12 days for sprint; 4-6 weeks for ICLR extension with 2 concurrent H100s",
      "team": "0 (initial 2-hour setup: model download, R-KV pip install, τ-bench harness verification)",
      "claude_api_cost": "$150-250 for sprint; $500-800 total with extension",
      "estimated_gpu_cost": "$200 sprint; $625 total",
      "speed_bottleneck": "τ-bench: 164 tasks × 9 runs (3 methods × 3 compression ratios) × ~2 min ≈ 49h — the dominant sprint cost. Parallelizable across GPUs.",
      "risk_note": "Agent may struggle with Lagrangian formulation implementation without human guidance. Recommend human review of solver code before experiment runs (Day 3-4 checkpoint)."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR May 25, 2026 — 13 days from today; 4-page short paper; ~60 H100-hours; commit to EMNLP venue at submission; reviews by June 29, commitment deadline August 2)",
    "ICLR 2027 (expected abstract deadline ~September 19, 2026; 8-page full paper extending EMNLP results with 2nd model, additional baselines, SWE-bench, and ablations; ~200 H100-hours total)"
  ],
  "level": "solid",
  "key_references": [
    "ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral) — no public code; partial proxy via NVIDIA kvpress (ThinKPress)",
    "HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference (ACL ARR Jan 2026) — **public code: github.com/skywclouds/HqeKV** — EMNLP sprint baseline",
    "ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget (arXiv Feb 2026)",
    "NGC: Neural Garbage Collection: Learning to Forget while Learning to Reason (arXiv April 2026, arXiv:2604.18002) — RL-based trajectory-aware KV eviction for single-model reasoning, eviction-only, 2-3x compression on Countdown/AMC/AIME",
    "CapKV: Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective (arXiv April 2026, arXiv:2604.25975) — Information Bottleneck principle with statistical leverage scores, eviction-only, per-step",
    "LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation (ICLR 2026 Poster, Samsung, arXiv:2603.10899) — predictive eviction via lookahead tokens + LoRA",
    "TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference (arXiv March 2026, arXiv:2604.19769) — temporal tiering with heterogeneous precision across HBM/DRAM",
    "TRIM-KV / Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs (ICLR 2026, arXiv:2512.03324) — learned per-token retention gates with temporal decay",
    "RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory (arXiv May 2026, arXiv:2605.06675) — reverse waterfilling for per-head bit allocation",
    "Transactional Attention: Semantic Sponsorship for KV-Cache Retention (arXiv April 2026, arXiv:2604.11288) — structural anchor protection for value-bearing tokens",
    "Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression [MixedDimKV] (arXiv March 2026, arXiv:2603.20616) — Lagrangian dual decomposition for per-token dimension allocation",
    "PBKV: Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management (arXiv May 2026, arXiv:2605.06472) — prediction-based agent cache scheduling",
    "KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows (NeurIPS 2025, arXiv:2507.07400) — workflow-aware prefix caching",
    "EpiCache: Episodic KV Cache Management for Long Conversational Question Answering (Apple, arXiv Sep 2025, arXiv:2509.17396) — episodic multi-turn cache management",
    "SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning (arXiv Feb 2026) — no public code",
    "CodeComp: Structural KV Cache Compression for Agentic Coding (arXiv April 2026)",
    "CacheTTL/Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live (arXiv Nov 2025)",
    "R-KV: Redundancy-aware KV Cache Compression for Reasoning Models (NeurIPS 2025) — **public code: github.com/Zefan-Cai/R-KV, 1.2k stars, vLLM/SGLang/FlashInfer integrations** — EMNLP sprint baseline",
    "How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers (arXiv April 2026, arXiv:2604.17935) — theoretical bounds on cache compression vs. reasoning depth (k-hop pointer chasing; analogy to agentic setting, not direct proof)",
    "PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs (arXiv May 2025, OpenReview Oct 2025) — empirical evidence of cumulative quantization error in long-CoT",
    "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning (arXiv Dec 2025, arXiv:2512.12008) — empirical assessment of compression degradation on reasoning tasks",
    "TriAttention: Efficient Long Reasoning with Trigonometric KV Compression (MIT/NVIDIA, arXiv April 2026)",
    "KV Cache Transform Coding [KVTC] for Compact Storage in LLM Inference (NVIDIA, ICLR 2026)",
    "Inference-Time Hyper-Scaling with KV Cache Compression [DMS] (NeurIPS 2025) — public code via HuggingFace + NVIDIA kvpress",
    "EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving (Microsoft, arXiv Dec 2025) — no public code",
    "Not All Bits Are Equal: How Model Scale Changes Memory-Optimal Reasoning (ICLR 2026)",
    "TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate (ICLR 2026) — inner-product bias compounding",
    "ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution (arXiv Feb 2026, arXiv:2602.03203) — RL-based future-aware eviction, no public code",
    "Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices (arXiv Feb 2026, arXiv:2603.04428)",
    "KVComm: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems (arXiv Oct 2025)",
    "Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys (AAAI 2026)"
  ],
  "description": "We propose TrajComp (Trajectory-Aware Joint Compression), a training-free method that jointly optimizes token eviction and per-token bit allocation for KV caches in long-horizon agentic LLM workloads through a dual-constrained Lagrangian objective that explicitly minimizes trajectory-level error accumulation. The empirical motivation comes from PM-KVQ (ICLR 2026), which demonstrates that cumulative quantization error degrades long-CoT reasoning by up to 8% versus progressive strategies, and from 'Hold Onto That Thought' (2025), which shows that compression strategies designed for prefill degrade on extended-decoding reasoning. Theoretical analysis from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) proves exponential error growth Ω((n/s)^(T-1)) for oblivious cache strategies in k-hop pointer chasing; we note this bound applies to single-model reasoning with locality-respecting cache controllers — its extension to agentic tool-use with external observation injection is a suggestive analogy, not a formal proof.\n\nThe landscape includes strong single-turn methods across multiple fronts: joint quant-eviction (ThinKV at 20x — no public code, HqeKV — public code, ARKV), future-aware and trajectory-aware eviction (NGC via RL-based eviction for single-model reasoning achieving 2-3x compression, LookaheadKV via predictive attention), information-theoretic eviction (CapKV via Information Bottleneck with statistical leverage scores), optimal bit allocation (RateQuant via rate-distortion, MixedDimKV via Lagrangian dual), and temporal/structural management (TTKV temporal tiering, TRIM-KV learned retention, Transactional Attention anchor protection). Agentic-specific works (SideQuest, CodeComp, PBKV, KVFlow, EpiCache) address scheduling and eviction but not joint compression. No prior work combines joint quant-eviction with a trajectory-level multi-step objective for agentic workloads.\n\nTrajComp fills this gap with two core contributions: (1) A cross-step error propagation model that weights compression decisions by their γ-discounted impact across all future agent steps, formalized as a dual-constrained Lagrangian with separate memory and trajectory-error budget multipliers. γ is calibrated empirically via KL divergence propagation measurement. (2) Agent-phase token categorization (persistent anchors, active context, decaying context, ephemeral tokens) that exploits cross-step importance structure unique to agentic workflows, with pattern-matching detection for structured agent frameworks (ReAct, function-calling). Both contributions are training-free.\n\nWe commit to a dual-track evaluation strategy designed to meet both the EMNLP 2026 deadline and resource constraints:\n\n**EMNLP 2026 short paper (primary, ARR May 25):** 4-page paper, 13-day sprint, ~60 H100-hours. 1 model (Qwen3-8B, GQA), 2 baselines with confirmed public code (R-KV at github.com/Zefan-Cai/R-KV with 1.2k stars and pip-installable vLLM integration; HqeKV at github.com/skywclouds/HqeKV), 3 benchmarks (τ-bench 164 tasks via official harness as primary agentic benchmark, LongBench, MMLU). Sprint: Day 1-3 implement solver + integrate baselines from public repos, Day 4-5 γ calibration, Day 6-8 run experiments, Day 9-11 write paper, Day 12-13 polish, Day 14 submit. Reports trajectory-level success rate at 4x/8x/16x compression on τ-bench plus standard accuracy on LongBench/MMLU.\n\n**ICLR 2027 full paper (extension, ~September 2026):** Expands to 2 models (add DeepSeek-R1-0528-Qwen3-8B — same Qwen3 GQA architecture, DeepSeek-R1-0528 tokenizer), 3 baselines (add uniform mixed-precision; add ThinKV if code releases), 9 benchmarks (add SWE-bench Lite 50 instances via SWE-agent, AIME 2025, MATH-500, HumanEval, MT-Bench, WikiText/C4 perplexity), full ablations, and attention entropy fallback for phase detection. ~200 H100-hours total including sprint work.",
  "project_name": "trajcomp_agentic_kvcache",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL NOVELTY GAP: ThinKV (ICLR 2026 Oral) already jointly applies quantization and eviction conditioned on reasoning thought types (reasoning/execution/transition), with temporal adaptation as thoughts evolve. The proposal's claim that 'no prior work formulates a co-optimization objective that jointly learns sparsity masks and per-token precision for reasoning KV caches, conditioned on the temporal phase of reasoning' is false — ThinKV does exactly this, just without a formal Lagrangian.", "MISSING CRITICAL COMPETITOR: HqeKV (ACL ARR Jan 2026) proposes an integrated optimizer that jointly selects the optimal compression action (quantization level or eviction) per cached element under memory constraints, with a joint K-V importance metric. This is essentially the same optimization problem TSQC claims to solve first.", "MISSING CRITICAL COMPETITOR: ARKV (arXiv Feb 2026) dynamically assigns tokens to three states (Original/Quantization/Eviction) based on per-layer attention dynamics, achieving 4x compression with 97% accuracy — a lighter-weight version of the same joint decision.", "MISSING CRITICAL COMPETITOR: TriAttention (MIT/NVIDIA, April 2026) achieves 10.7x KV memory reduction on AIME25 with matched accuracy using a fundamentally different approach (trigonometric compression), setting a very high baseline that TSQC must beat.", "MISSING COMPETITOR: KVTC (NVIDIA, ICLR 2026) already achieves 20x compression on reasoning benchmarks (AIME25, MATH-500, LiveCodeBench) — matching TSQC's claimed 15-20x target — through PCA + adaptive quantization + entropy coding, without any sparsity mechanism.", "RESOURCE MISMATCH: User specifies ≤200 H100-hours. The proposal estimates in A100-hours (300h manual, 700h auto). While 300 A100-hours ≈ 150 H100-hours for this workload type, the proposal should have been stated in H100-hours per the user's constraint.", "TIMELINE RISK: Writing a fused CUDA kernel for joint sparsity-quantization with dual gradient descent in 16 days (for the EMNLP deadline) is unrealistic. Even the proposal acknowledges this is a 'stretch target only.'", "COMPRESSION TARGET NOT NOVEL: The claimed 15-20x compression with <2% accuracy loss is already achieved by ThinKV (20x) and KVTC (20x) individually. The 'multiplicative compression' argument (sparsity × quantization) is the same strategy these works already employ.", "EVALUATION GAPS: The proposal uses AIME 2025, MATH-500, GPQA, LiveCodeBench but omits LongBench and RULER from the user's required evaluation suite. The user explicitly listed these benchmarks.", "The attention-entropy-based phase detector (exploration vs. convergence) is underspecified. 'Not All Bits Are Equal' (ICLR 2026) shows that the optimal compression strategy is scale-dependent — the proposal doesn't address how TSQC adapts across the 8B-27B range.", "The landscape section strategically describes ThinKV as treating quantization and eviction 'as separate strategies within a pipeline,' which understates ThinKV's contribution — ThinKV's thought-aware compression is jointly designed even if not formulated as a Lagrangian."]
Feedback: The fundamental problem is that this idea arrives too late to a very crowded space. ThinKV (ICLR 2026 Oral) is the most damaging competitor — it already performs reasoning-phase-aware joint quantization-eviction and achieves 20x compression. To differentiate TSQC, the generator must:

1. **Honestly acknowledge ThinKV as the primary baseline** and clearly articulate why a Lagrangian co-optimization beats ThinKV's pipeline. The current framing that 'no prior work formulates a co-optimization objective' is misleading given ThinKV and HqeKV.

2. **Add HqeKV, ARKV, TriAttention, and KVTC as baselines.** Missing these 2026 works in a May 2026 submission would be flagged by any reviewer.

3. **Reframe the contribution** away from 'first to jointly optimize' (which is false) toward: (a) the Lagrangian formulation yields provably Pareto-optimal tradeoffs whereas ThinKV's pipeline is heuristic — demonstrate this with Pareto frontier plots; (b) the continuous relaxation enables smooth budget interpolation that discrete pipeline approaches cannot.

4. **Address the 'Not All Bits Are Equal' (ICLR 2026) findings** about scale-dependent optimal strategies — how does TSQC handle the 8B vs 27B regime difference?

5. **Include LongBench and RULER** in the evaluation per user requirements. Also add perplexity (Wiki/C4), MMLU, HumanEval, and MT-Bench as specified by the user.

6. **Target AAAI 2027 or ICLR 2027** as primary (as the proposal already suggests), not EMNLP 2026 — 16 days is insufficient for CUDA kernel development + comprehensive evaluation.

7. **Consider pivoting**: given how crowded this space is, the strongest angle might be applying the Lagrangian co-optimization framework to a less-explored setting — e.g., agent-loop KV caches with cross-turn reuse, or multi-modal reasoning KV caches — where ThinKV/HqeKV/ARKV haven't been validated.

### Round 2 review
Verdict: revise
Issues: ["VENUE MISMATCH: User explicitly requested EMNLP 2026 (ARR deadline May 25, 2026). The proposal targets AAAI 2027 (Aug 2026) and ICLR 2027 instead. While Round 1 feedback correctly suggested retargeting, the proposal should still acknowledge the user's requirement and explain why the pivot was necessary, or propose a feasible EMNLP 2026 submission scope.", "MISSING COMPETITOR — TTKV (April 2026): Temporal-Tiered KV Cache partitions the cache into temporal tiers with heterogeneous precision, assigning recent KV states to higher-precision tiers based on temporal proximity. This directly overlaps with TrajComp's 'decaying context' category (4-bit → 2-bit → evict based on temporal distance). TTKV must be cited and differentiated.", "MISSING COMPETITOR — TRIM-KV / 'Cache What Lasts' (Dec 2025, ICLR 2026): Learns per-token retention scores with exponential temporal decay via lightweight retention gates. This is conceptually similar to TrajComp's importance-weighted temporal decay model, though TRIM-KV doesn't do joint quantization-eviction. Must be cited.", "MISSING COMPETITOR — EpiCache (Apple, Sep 2025): Episodic KV cache management for long conversational QA that clusters conversation history into coherent episodes with per-episode compression. This addresses multi-turn KV cache management — a closely related problem. Generator should cite and differentiate.", "MISSING COMPETITOR — RateQuant (May 2026): Uses rate-distortion theory for optimal mixed-precision KV cache quantization with per-head closed-form bit allocation. The Lagrangian/rate-distortion framework is conceptually adjacent to TrajComp's dual-constrained optimization. Must be discussed.", "MISSING COMPETITOR — Transactional Attention (April 2026): Uses structural anchor patterns to protect value-bearing tokens from eviction, achieving 100% credential retrieval where all attention-based eviction methods fail. TrajComp's 'persistent anchors' category performs a similar function. Should be cited.", "MISSING COMPETITOR — PBKV (May 2026) and KVFlow: Prediction-based KV cache management for dynamic agent workflows that predicts future agent invocations to optimize cache retention. These represent the systems-level competing approach to TrajComp's compression-level approach for agentic workloads.", "WEAK MOTIVATION EVIDENCE: The core error compounding claim (94.2% → 76.1% over 50 steps at 2-bit) traces to a blog post (dasroot.net), not a peer-reviewed paper. The numbers appear to be from visual planning/robotic manipulation tasks (DINO-WM, Inovo robot), not LLM agent tasks. Using non-peer-reviewed evidence for LLM-irrelevant tasks to motivate the core contribution is risky for a top venue submission.", "EVALUATION SCOPE vs COMPUTE BUDGET MISMATCH: Evaluating 4 models × 8+ baselines × 3 agentic benchmarks (SWE-bench Verified ~500 instances, GAIA ~450 tasks, τ-bench) + 8 standard benchmarks is far more than 150 H100-hours. SWE-bench alone at 3-5 min/instance × 500 × 12 configs (4 models × 3 compression levels) ≈ 300-500 GPU-hours just for one baseline comparison. The compute budget must either increase substantially or the evaluation scope must be reduced.", "γ ESTIMATION UNDERSPECIFIED: The cross-step error propagation rate γ is described as 'empirically estimated' but no method is given. This is a critical hyperparameter — if γ requires per-model, per-task calibration, it undermines the method's generality and adds substantial hidden compute cost.", "PATTERN MATCHING FOR PHASE DETECTION IS FRAGILE: The proposal detects agent phases via 'lightweight pattern matching on special tokens and turn boundaries.' This works for structured agent frameworks but will fail for free-form reasoning models (e.g., DeepSeek-R1) where thinking and acting are interleaved without clear delimiters. SideQuest's model-driven approach is more robust here.", "USER REQUIREMENT: evaluation must include perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench — these are now included in the proposal, which addresses Round 1 feedback. However, reporting wall-clock and throughput on H100 is also required and not discussed in the approach section."]
Feedback: The pivot to agentic workloads is the right strategic move — this is genuinely less crowded than single-turn reasoning compression. The cross-step error propagation Lagrangian is a real contribution. However, several issues need addressing:

1. **Cite 6 missing competitors**: TTKV, TRIM-KV, EpiCache, RateQuant, Transactional Attention, and PBKV/KVFlow. Position TrajComp against each: TTKV does temporal tiering but not joint optimization under a trajectory-error budget; TRIM-KV learns temporal decay but only for eviction, not joint quant-eviction; EpiCache does episodic multi-turn management but not cross-step error propagation; RateQuant uses rate-distortion theory but only for single-step bit allocation; Transactional Attention protects structural anchors but without trajectory-level optimization.

2. **Strengthen the core motivation**: Replace the blog post citation (dasroot.net) with peer-reviewed evidence. PM-KVQ (ICLR 2026) demonstrates cumulative quantization error in long-CoT. 'How Much Cache Does Reasoning Need?' (April 2026) provides theoretical bounds on error scaling under KV compression. Use these to justify the trajectory-level objective.

3. **Reduce evaluation scope or increase compute budget**: The current 4-model × 8-baseline × 11-benchmark matrix cannot be completed in 150 H100-hours. Either: (a) focus on 2 models (Qwen3-8B, DeepSeek-R1-Distill-8B) and 3-4 key baselines (ThinKV, HqeKV, SideQuest, CodeComp) with full agentic + standard eval; or (b) request 400+ H100-hours.

4. **Specify γ estimation**: Propose a concrete calibration procedure — e.g., run 10 agent trajectories with and without compression at step boundaries, measure attention distribution divergence propagation, fit γ per model.

5. **Address venue**: Either (a) propose a reduced scope for EMNLP 2026 ARR May 25 submission (2 models, 3 baselines, subset of benchmarks, targeting Findings) or (b) explicitly justify the AAAI 2027 pivot against the user's original requirement.

6. **Add wall-clock and throughput reporting** as the user requires — describe how the Lagrangian solver overhead will be benchmarked and reported relative to baselines.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL — ROUND 2 FEEDBACK NOT ADDRESSED: Round 2 gave 6 specific action items: (1) cite TTKV, TRIM-KV, EpiCache, RateQuant, Transactional Attention, PBKV; (2) replace blog post motivation with peer-reviewed evidence; (3) fix compute/scope mismatch; (4) specify γ estimation; (5) address venue; (6) add wall-clock/throughput reporting. None were acted on. This is a serious process failure — reviewers will expect iterative improvement.", "MISSING CRITICAL COMPETITOR — ForesightKV (arXiv Feb 2026, OpenReview): Learns long-term contribution of tokens for KV cache eviction in reasoning models via supervised learning + RL. Formulates cache eviction as a Markov Decision Process considering future impact of eviction decisions. This is conceptually parallel to TrajComp's cross-step error propagation model — both consider how current compression decisions affect future steps. ForesightKV must be cited and differentiated (it does eviction only, not joint quant-eviction; it uses RL not Lagrangian optimization; it targets single-turn reasoning, not multi-step agentic workloads).", "STILL MISSING 6 COMPETITORS FROM ROUND 2: (1) TTKV (March 2026) — temporal tiering with heterogeneous precision directly overlaps with 'decaying context' category; (2) TRIM-KV/Cache What Lasts (ICLR 2026) — learned per-token retention with temporal decay, conceptually similar to cross-step importance decay; (3) RateQuant (May 2026) — rate-distortion theory for optimal bit allocation, Lagrangian-adjacent framework; (4) Transactional Attention (April 2026) — structural anchor protection for value-bearing tokens, overlaps with 'persistent anchors'; (5) EpiCache (Apple, Sep 2025) — episodic multi-turn cache management; (6) PBKV (June 2026) — prediction-based KV cache for dynamic agent workflows. All confirmed real via independent search.", "MISSING COMPETITOR — LookaheadKV (ICLR 2026 Poster, Samsung): Predictive eviction using lookahead tokens + LoRA to predict future attention patterns. Achieves <0.7% performance drop at 81% compression. Relevant because it also considers future token importance, though via prediction rather than trajectory-level optimization.", "CORE MOTIVATION STILL FROM BLOG POST: The 94.2% → 76.1% error compounding figure still traces to dasroot.net, a blog post about visual planning/robotic manipulation — NOT LLM agent tasks. Round 2 explicitly flagged this and suggested PM-KVQ (ICLR 2026) and 'How Much Cache Does Reasoning Need?' (April 2026, arXiv:2604.17935) as peer-reviewed alternatives. Neither has been incorporated.", "COMPUTE BUDGET vs EVALUATION SCOPE — CRITICAL MISMATCH: Independent estimation shows the evaluation matrix requires 500-2600+ H100-hours: SWE-bench Verified (500 instances × 4 models × multiple configs ≈ 80-120h), RULER (39,000 samples ≈ 260h for 4 models), GAIA (≈120-160h), plus standard benchmarks, plus 8+ baselines each requiring their own evaluation runs. The claimed 150h budget covers roughly 10-25% of this scope. Even the user's 200h constraint requires drastic scope reduction.", "γ ERROR PROPAGATION RATE STILL UNSPECIFIED: The cross-step error propagation rate γ is the single most critical hyperparameter — it determines how compression decisions at step t are weighted across future steps. No calibration procedure is given. If γ requires per-model, per-task calibration, this adds substantial hidden compute cost and undermines the method's generality. Round 2 suggested a concrete procedure (10 agent trajectories, measure attention divergence propagation, fit γ) but this was not adopted.", "LAGRANGIAN TECHNIQUE OVERLAP WITH MixedDimKV: MixedDimKV (March 2026, cited in the proposal) already formulates KV cache compression as a constrained optimization problem using Lagrangian dual decomposition with bisection search over λ. TrajComp uses the same optimization technique. The differentiation (trajectory-level objective vs per-step objective) is real but the proposal doesn't adequately discuss this overlap or prove the trajectory extension yields meaningfully better solutions.", "VENUE MISMATCH PERSISTS: User explicitly requested EMNLP 2026 (ARR May 25, 2026). Proposal targets AAAI 2027 (August 2026, dates NOT YET ANNOUNCED per my search) and ICLR 2027. The pivot is defensible but must be explicitly justified with a feasible reduced-scope EMNLP 2026 option (e.g., 2 models, 3 baselines, focus on agentic benchmarks, target Findings).", "PHASE DETECTION FRAGILITY UNADDRESSED: Pattern matching on special tokens and turn boundaries works for structured agent frameworks (e.g., ReAct with explicit Thought/Action/Observation tags) but fails for free-form reasoning models like DeepSeek-R1 where thinking and acting interleave without clear delimiters. SideQuest's model-driven approach is more robust. The proposal needs a fallback strategy or attention-based phase detection.", "WALL-CLOCK AND THROUGHPUT REPORTING NOT DISCUSSED: User explicitly requires reporting wall-clock and throughput on H100. The Lagrangian solver overhead at each agent step boundary must be benchmarked and reported relative to baselines. How does re-optimization cost scale with KV cache size and number of agent steps?"]
Feedback: The trajectory-level Lagrangian formulation for agentic KV caches remains the genuine contribution here, but this is Round 3 and none of the Round 2 feedback was addressed. The generator must fix this immediately:

1. **Cite all missing competitors with explicit differentiation**: ForesightKV (learns long-term contribution via RL, but eviction-only and single-turn — TrajComp's joint quant-eviction + multi-step Lagrangian is broader), TTKV (temporal tiering but no trajectory-level error budget), TRIM-KV (learned temporal decay but eviction-only), RateQuant (rate-distortion optimal bit allocation but single-step), Transactional Attention (structural anchors but no trajectory optimization), PBKV/KVFlow (prediction-based agent cache scheduling but no compression), LookaheadKV (future-aware eviction but no quantization), MixedDimKV (Lagrangian dual but per-step not trajectory-level). The landscape section must honestly acknowledge that MixedDimKV uses the same Lagrangian technique and clearly articulate why the trajectory-level extension is non-trivial.

2. **Replace blog post motivation NOW**: Use 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) for theoretical error scaling bounds, PM-KVQ for empirical evidence of cumulative quantization error in long-CoT, and ForesightKV's motivation section for evidence that local eviction decisions degrade long-horizon reasoning.

3. **Drastically reduce evaluation scope to fit 200 H100-hours**: Focus on 2 models (Qwen3-8B, DeepSeek-R1-Distill-8B), 4 key baselines (ThinKV, HqeKV, SideQuest, ForesightKV), and 6 benchmarks: 2 agentic (SWE-bench Lite ~300 instances, τ-bench), 2 reasoning (AIME 2025, MATH-500), 1 long-context (LongBench), 1 general (MMLU). Drop GAIA (too expensive), RULER (260 H100-hours alone), and reduce baseline count. This makes ~150-200 H100-hours realistic.

4. **Specify γ calibration concretely**: Run N=10 agent trajectories per model with full KV cache and with compressed KV cache at step boundaries. Measure KL divergence of attention distributions at each step. Fit γ = median(KL_{t+1}/KL_t) across steps and trajectories. Report sensitivity analysis: does γ vary by >20% across tasks? If so, per-task calibration is needed and the cost must be budgeted.

5. **Address phase detection robustness**: For structured agent frameworks (ReAct), use special token patterns. For free-form reasoning (DeepSeek-R1), fall back to attention entropy thresholds or turn-boundary detection. Acknowledge the limitation explicitly and benchmark both strategies.

6. **Add wall-clock/throughput section**: Report Lagrangian solver time per agent step (expected: milliseconds for dual gradient descent over ~100K tokens), end-to-end latency per agent step, and tokens/second throughput. Compare against baselines on H100.

7. **Decide venue**: Either (a) propose a reduced-scope EMNLP 2026 Findings submission (2 models, 3 baselines, 4 benchmarks, 14 days) or (b) explicitly state that AAAI 2027/ICLR 2027 is the target with justification. Do not leave this ambiguous.

### Round 4 review
Verdict: revise
Issues: ["COMPUTE BUDGET REMAINS TIGHT: Independent estimation shows SWE-bench Lite at 2.5 min/instance with 8B models in multi-turn agentic evaluation is 2-5x too optimistic. Multi-turn agent interactions (100+ turns per SWE-bench instance for competitive agents, and 8B models need more turns than frontier models) realistically take 5-15 min/instance. This alone could push SWE-bench from 63h to 125-315h. Combined with inadequate dev/debug buffer (16h for reimplementing 4 baselines is unrealistic — 40-80h is more appropriate), the true compute need is 290-500+ H100-hours. Either reduce SWE-bench instances (e.g., 100 instead of 300), use a simpler agent scaffold, or honestly budget 300-400h.", "MISSING COMPETITOR — CapKV (April 2026, arXiv:2604.25975): Uses the Information Bottleneck principle to derive a closed-form mutual information objective for KV cache eviction with capacity-aware scoring. Provides a competing theoretically-grounded framework for principled KV cache management. Should be cited and differentiated (CapKV is eviction-only and per-step; TrajComp does joint quant-eviction with trajectory-level objective).", "USER EVALUATION REQUIREMENTS PARTIALLY UNMET: The user explicitly required perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. The proposal drops Wiki/C4 perplexity, HumanEval, RULER, and MT-Bench. While the scope reduction is justified by compute constraints, the proposal should explicitly acknowledge which user-required benchmarks are dropped and why, and suggest how they could be added in a follow-up or with additional compute.", "VENUE MISMATCH: The user explicitly requested EMNLP 2026 (ARR May 25, 2026). The proposal correctly identifies this as infeasible at 14 days but the minimal EMNLP 2026 Findings plan ('only if the Lagrangian solver is already implemented') is vague. Either provide a concrete 14-day sprint plan (what exactly would be submitted, which experiments, how many pages) or clearly state this is not the target and the user should accept AAAI 2027 / ICLR 2027 instead.", "SWE-BENCH AGENT SCAFFOLD UNSPECIFIED: The proposal evaluates on SWE-bench Lite but never specifies what agent scaffold will be used. The per-instance timing, number of agent steps, and therefore the relevance of trajectory-level compression all depend critically on the agent design. A lightweight single-pass agent (which might justify 2.5 min/instance) would produce short trajectories where trajectory-level optimization may show minimal benefit over per-step methods — undermining the core contribution. A full multi-turn agent scaffold (ReAct with tool use) would better showcase the contribution but costs much more. This tradeoff must be explicitly addressed.", "γ SENSITIVITY AND GENERALITY RISK: The γ calibration procedure (10 trajectories, KL divergence ratio) is now concrete, but the proposal notes 'if γ varies by >20% across tasks, use per-benchmark γ.' If γ is indeed task-dependent, this undermines the method's claim of being a general-purpose trajectory-level optimizer. The proposal should discuss what happens if γ varies by 50%+ across benchmarks — does the method degrade gracefully or fail?"]
Feedback: This is a substantially improved proposal — all Round 3 feedback items were addressed, the landscape analysis is now comprehensive and honest, and the technical specification is much more concrete. The contribution (trajectory-level Lagrangian for agentic KV caches) fills a genuine gap confirmed by thorough literature search. To reach pass quality:

1. **Fix compute realism**: The SWE-bench timing is the critical weakness. Either (a) reduce to 100 SWE-bench Lite instances (still statistically meaningful, cuts from 63h to ~21h claimed / ~42-100h realistic), (b) explicitly specify a lightweight agent scaffold and acknowledge it produces shorter trajectories, or (c) honestly budget 300-350 H100-hours and justify to the user why 200h is insufficient for agentic benchmarks. Also increase dev/debug buffer to 40-60h.

2. **Cite CapKV** (arXiv:2604.25975) — information-theoretic KV cache eviction. One line in landscape suffices.

3. **Specify the agent scaffold**: Name the exact framework (e.g., SWE-agent, Agentless, OpenHands) and configuration (max turns, max tokens, tools available). This determines both cost and whether trajectory-level optimization has room to help.

4. **Address user eval gaps explicitly**: Add a table showing user-required benchmarks, which are included vs dropped, and compute cost per dropped benchmark. This lets the user make an informed decision about scope.

5. **Strengthen γ robustness**: Add a fallback for high γ variance: if γ varies >50%, degrade gracefully to per-step optimization (which should match MixedDimKV/ThinKV performance). This converts a failure mode into a guaranteed lower bound.

6. **Sharpen EMNLP 2026 decision**: Either commit to a 14-day sprint plan (1 model, 2 baselines, 3 benchmarks, 6-page Findings submission) or explicitly drop EMNLP 2026 from target_venues entirely.

### Round 5 review
Verdict: revise
Issues: ["MISSING COMPETITOR — Neural Garbage Collection (arXiv:2604.18002, April 2026): Learns to evict KV cache entries during reasoning via RL, treating eviction decisions as actions within the reasoning chain. While NGC is training-required, eviction-only, and targets single-model reasoning (not agentic tool-use), it directly addresses trajectory-aware KV management and should be cited and differentiated. TrajComp's advantages: training-free, joint quant-eviction, multi-step agentic objective, structural phase exploitation.", "STILL MISSING CapKV (arXiv:2604.25975): Round 4 explicitly requested this citation. Information-theoretic KV cache eviction via Information Bottleneck principle. One-line citation and differentiation (eviction-only, per-step, no trajectory objective) would suffice.", "USER TIMELINE CONSTRAINT VIOLATED: User specified ≤16 days as a HARD CONSTRAINT. Proposal estimates 2.5-3.5 months (manual). The EMNLP 2026 contingency plan is vague ('only if Lagrangian solver already implemented'). Either propose a concrete 14-day sprint plan with drastically reduced scope (1 model, 2 baselines, 3 benchmarks, short paper) or explicitly acknowledge this constraint cannot be met and justify the venue pivot.", "USER-REQUIRED BENCHMARKS DROPPED WITHOUT ACKNOWLEDGMENT: User required perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Proposal keeps only MMLU and LongBench, dropping 4 of 6. Round 4 feedback asked for 'a table showing user-required benchmarks, which are included vs dropped, and compute cost per dropped benchmark.' This table is still missing.", "AGENT SCAFFOLD STILL UNSPECIFIED: Round 4 explicitly asked to 'Name the exact framework (e.g., SWE-agent, Agentless, OpenHands) and configuration (max turns, max tokens, tools available).' This determines cost, trajectory length, and whether trajectory-level optimization shows meaningful gains over per-step methods. A single-pass agent (Agentless) would undermine the core contribution; a multi-turn agent (SWE-agent) would exceed the timing estimates.", "FORESIGHTKV BASELINE REPRODUCTION COST NOT BUDGETED: ForesightKV requires supervised training + RL fine-tuning (GRPO). This is not a plug-and-play baseline — reproduction requires dataset construction, training infrastructure, and significant GPU time. Either budget 20-40h for reproduction, use their released checkpoint (if available), or replace with a reproducible alternative baseline.", "THEORETICAL CLAIM SLIGHTLY OVERSTATED: The proposal cites 'How Much Cache Does Reasoning Need?' for error bound Ω((n/s)^(T-1)) as motivation for agentic trajectory-level compression. My deep read confirms this bound applies to k-hop pointer chasing in single-model multi-step reasoning, not multi-step agentic tool-use workflows. The analogy is reasonable but the proposal should acknowledge the theoretical model doesn't directly map to agentic settings with external tool calls and observation injection."]
Feedback: The proposal has matured significantly — the landscape is now among the most comprehensive I've seen (29+ papers), the γ calibration is concrete, the dual-constrained Lagrangian formulation is clean, and the differentiation from MixedDimKV is well-articulated. The core contribution (trajectory-level joint quant-eviction for agentic KV caches) fills a verified gap. To reach pass quality:

1. **Cite Neural Garbage Collection** (arXiv:2604.18002): 'NGC (April 2026) learns trajectory-aware KV eviction via RL, jointly optimizing reasoning and memory management. TrajComp differs in three ways: training-free (vs. RL-required), joint quant-eviction (vs. eviction-only), and exploits agentic workflow structure (vs. single-model reasoning traces).' Also cite CapKV as requested in Round 4.

2. **Resolve the timeline/venue crisis**: The user's 16-day hard constraint makes EMNLP 2026 the target. Either (a) propose a concrete 14-day sprint: Day 1-3 implement Lagrangian solver on top of vLLM/SGLang, Day 4-6 implement phase detection, Day 7-10 run experiments (1 model: Qwen3-8B, 2 baselines: ThinKV + SideQuest, 3 benchmarks: SWE-bench Lite 50-instance subset + AIME 2025 + MMLU), Day 11-14 write 4-page short paper for EMNLP 2026 Findings. ~60 H100-hours. OR (b) clearly state 'This idea requires AAAI 2027/ICLR 2027 targeting; EMNLP 2026 is not achievable' and accept the user may reject it.

3. **Specify the agent scaffold**: Name it (e.g., 'SWE-agent with ReAct prompting, max 25 turns, max 16K tokens per turn'). This is essential for cost estimates and determines trajectory length.

4. **Add user benchmark gap table**: Show which of the 6 user-required benchmarks are included (MMLU, LongBench) and which are dropped (perplexity, HumanEval, RULER, MT-Bench) with per-benchmark cost estimates. RULER alone would cost ~50-100h for 2 models.

5. **Budget ForesightKV reproduction or replace**: If no public checkpoint exists, replace with a simpler future-aware baseline (e.g., attention-pattern-based eviction with lookahead window) that can be implemented in <8h.

6. **Soften the theoretical analogy**: Note that the Ω((n/s)^(T-1)) bound from 'How Much Cache' applies to k-hop pointer chasing, which is an analogy (not a direct proof) for agentic trajectory error compounding. The empirical evidence from PM-KVQ and 'Hold Onto That Thought' is the stronger motivation.

### Round 6 review
Verdict: revise
Issues: ["FACTUAL ERROR — MLA ARCHITECTURE CLAIM: The proposal states '2 models covering standard attention and MLA' for Qwen3-8B and DeepSeek-R1-Distill-Qwen3-8B. This is incorrect. DeepSeek-R1-Distill-Qwen3-8B uses Qwen3's standard GQA attention architecture, NOT MLA. MLA (Multi-head Latent Attention) is exclusive to the full DeepSeek-V3/R1 (671B MoE). Both evaluation models thus use standard attention variants, and the 'architecture-aware adaptation for MLA' contribution is not testable within the proposed evaluation. Either add a model that actually uses MLA (requires DeepSeek-V3/R1 at 671B, infeasible at 200 H100-hours) or remove the MLA adaptation claim entirely.", "STILL MISSING NGC (Round 5 request) AND CapKV (Rounds 4+5 requests): Neural Garbage Collection (arXiv:2604.18002) learns trajectory-aware KV eviction via RL — the closest conceptual competitor for trajectory-aware cache management, despite being eviction-only and training-required. CapKV (arXiv:2604.25975) provides a competing information-theoretic framework for principled KV cache eviction. Both were explicitly requested in previous rounds with suggested one-line differentiations provided. This repeated failure to address explicit reviewer requests is a process concern.", "AGENT SCAFFOLD STILL UNSPECIFIED (Rounds 4+5 requests): The exact agent framework (SWE-agent, Agentless, OpenHands) and configuration (max turns, max tokens, tools) for SWE-bench Lite evaluation is never named. This is critical because: (a) a single-pass agent like Agentless produces short trajectories where trajectory-level optimization shows minimal benefit — undermining the core contribution; (b) a multi-turn agent (SWE-agent with 25+ turns) would produce longer trajectories but costs 5-15 min/instance for 8B models, far exceeding the 2.5 min estimate; (c) the trajectory length directly determines whether TrajComp's cross-step optimization has room to outperform per-step methods.", "SWE-BENCH TIMING STILL OPTIMISTIC: 2.5 min/instance for multi-turn agentic evaluation with 8B models is 2-3x too low. CacheTTL's own data shows SWE-bench mini-agent traces have 'many turns with short (<2s) tool calls' but 8B models need more reasoning turns than frontier models. Realistic estimates: 5-10 min/instance with a proper multi-turn scaffold, pushing SWE-bench from 63h to 125-250h alone. This makes the 200 H100-hour budget infeasible unless instances are reduced to ~100-150.", "FORESIGHTKV BASELINE REPRODUCTION COST UNBUDGETED (Round 5 request): ForesightKV requires supervised training (golden eviction labels) + RL fine-tuning (GRPO). No public checkpoint for Qwen3-8B or DeepSeek-R1-Distill-8B is confirmed. Reproducing it could cost 30-50 H100-hours. Either verify a public checkpoint exists, budget reproduction cost, or replace with a simpler future-aware baseline (e.g., attention-pattern lookahead).", "USER-REQUIRED BENCHMARKS GAP TABLE STILL MISSING (Rounds 4+5 requests): User explicitly required perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Proposal keeps MMLU and LongBench, drops 4 of 6. Rounds 4 and 5 asked for a table showing included vs. dropped benchmarks with per-benchmark compute cost estimates. This table is still absent. RULER alone costs ~50-100h for 2 models; HumanEval and MT-Bench are cheap (~2-3h each) and should arguably be included.", "VENUE MISMATCH STILL NOT FULLY RESOLVED: User's HARD CONSTRAINT was ≤16 days and EMNLP 2026. The proposal correctly identifies EMNLP 2026 as infeasible but the contingency plan is vague ('only if Lagrangian solver already implemented'). The proposal should either: (a) provide a concrete 14-day sprint plan (1 model, 2 baselines, 3 benchmarks, short paper for EMNLP Findings), or (b) explicitly state the user's 16-day constraint cannot be met and present AAAI 2027 (deadline TBD, expected July-August 2026) as the earliest feasible target.", "THEORETICAL ANALOGY STILL SLIGHTLY OVERSTATED: The Ω((n/s)^(T-1)) bound from 'How Much Cache Does Reasoning Need?' applies to k-hop pointer chasing in single-model multi-step reasoning with locality-respecting cache controllers. The paper explicitly does NOT address multi-agent tool-use workflows. The proposal uses this bound to motivate trajectory-level compression for agentic workloads — a reasonable analogy, but the proposal should explicitly note the theoretical model doesn't directly cover agentic settings with external tool calls and observation injection. The empirical evidence (PM-KVQ, 'Hold Onto That Thought') is the stronger motivation."]
Feedback: The proposal has reached a high level of maturity — the landscape analysis is exceptional (29+ papers, honest differentiation), the core contribution is verified as novel, and the technical specification is concrete. Three issues block a pass:

1. **Fix the MLA architecture error immediately**: DeepSeek-R1-Distill-Qwen3-8B uses Qwen3's GQA, not MLA. Remove the MLA adaptation claim from the contributions or replace the model with one that actually uses MLA (impractical at this budget). The simplest fix: state that TrajComp targets standard attention and GQA architectures in this work, with MLA adaptation as future work. Remove 'MLA' from the '2 models covering standard attention and MLA' description.

2. **Cite NGC and CapKV** — this is the third time requested: 'NGC (April 2026, arXiv:2604.18002) learns trajectory-aware KV eviction via RL within single-model reasoning. TrajComp differs: training-free, joint quant-eviction, multi-step agentic objective.' 'CapKV (April 2026, arXiv:2604.25975) derives information-theoretic KV eviction via the Information Bottleneck principle. TrajComp differs: joint quant-eviction with trajectory-level objective vs. per-step information-theoretic eviction.'

3. **Specify the agent scaffold and fix SWE-bench timing**: Name the framework (e.g., 'SWE-agent with ReAct prompting, max 30 turns, 16K tokens/turn'). Then re-estimate per-instance timing realistically (5-8 min for 8B multi-turn) and either reduce instances to 100-150 or increase compute budget to 250-300h. Add HumanEval and MT-Bench (~5h total) to partially address user benchmark requirements.

4. **Add the user benchmark gap table**: |Benchmark|Status|Est. Cost|Reason for Drop| — show MMLU (included), LongBench (included), perplexity (dropped, ~3h, add it), HumanEval (dropped, ~2h, add it), MT-Bench (dropped, ~2h, add it), RULER (dropped, ~100h, compute prohibitive).

5. **Soften the theoretical claim**: Add one sentence noting the Ω((n/s)^(T-1)) bound applies to k-hop pointer chasing, not directly to agentic tool-use, but provides theoretical grounding that cache compression errors compound across reasoning stages.

### Round 7 review
Verdict: revise
Issues: ["PERSISTENT PROCESS FAILURE — 4 ROUNDS OF IGNORED FEEDBACK: NGC (arXiv:2604.18002), CapKV (arXiv:2604.25975), agent scaffold specification, and user benchmark gap table have been explicitly requested in Rounds 4, 5, 6, and now 7. None have been addressed. At Round 7/10, this pattern risks a 'fail' verdict by Round 10 regardless of idea quality, because inability to address reviewer feedback is itself a disqualifying signal for any venue.", "FACTUAL ERROR PERSISTS — MLA ARCHITECTURE CLAIM (Round 6 + 7): The evaluation section states '2 models covering standard attention and MLA' for Qwen3-8B and DeepSeek-R1-Distill-8B. This is factually wrong. DeepSeek-R1-Distill-Qwen3-8B uses Qwen3's GQA architecture (32 query heads, 8 KV heads), NOT MLA. MLA is exclusive to the full DeepSeek-V3/R1 671B MoE model. Contribution (3) 'Architecture-aware adaptation for standard attention and MLA architectures' is therefore untestable. The approach section correctly classifies both models as standard attention but contradicts itself in the evaluation scope.", "STILL MISSING NGC (4th request): Neural Garbage Collection (arXiv:2604.18002, April 2026) learns trajectory-aware KV eviction via RL, treating eviction as actions within reasoning chains. It achieves 2-3x compression on Countdown/AMC/AIME while jointly optimizing reasoning and memory. This is the closest conceptual competitor for trajectory-aware cache management. TrajComp's advantages (training-free, joint quant-eviction, multi-step agentic objective) must be explicitly stated.", "STILL MISSING CapKV (4th request): arXiv:2604.25975 derives capacity-aware KV eviction via the Information Bottleneck principle with statistical leverage scores. Provides a competing theoretically-grounded framework. One-line differentiation (eviction-only, per-step, no trajectory objective) suffices.", "AGENT SCAFFOLD STILL UNSPECIFIED (4th request): SWE-bench evaluation without naming the agent framework (SWE-agent, Agentless, OpenHands, etc.) and configuration (max turns, max tokens, tools) is incomplete. This is not a minor detail: (a) Agentless produces single-pass short trajectories where trajectory-level optimization has minimal room to help — undermining the core contribution; (b) SWE-agent with ReAct produces multi-turn trajectories but costs 5-15 min/instance for 8B models; (c) OpenHands with small models achieves only ~12% success rate, raising questions about whether there is enough headroom for meaningful compression comparisons.", "SWE-BENCH TIMING 4x TOO OPTIMISTIC: 2.5 min/instance is confirmed unrealistic by independent search — ~10 min/instance is typical for multi-turn agentic evaluation. This pushes SWE-bench from 63h to ~250h alone. With 5 methods × 2 models × 300 instances × 10 min = 500h just for SWE-bench. Either reduce to 50-100 instances or honestly budget 350+ H100-hours.", "USER BENCHMARK GAP TABLE STILL MISSING (4th request): User required perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Proposal includes only MMLU and LongBench. HumanEval (~2h) and MT-Bench (~2h) are cheap enough to include. Perplexity on Wiki/C4 is ~3h. RULER is prohibitively expensive (~100h). A simple table showing status/cost/reason-for-drop was requested 4 times.", "FORESIGHTKV BASELINE REPRODUCTION UNBUDGETED: Independent search found no public code or checkpoints for ForesightKV. Reproducing supervised training + RL fine-tuning (GRPO) for 2 models could cost 30-50 H100-hours. Either verify a public checkpoint, budget reproduction, or replace with a reproducible alternative (e.g., attention-pattern lookahead baseline).", "THEORETICAL CLAIM STILL OVERSTATED: The Ω((n/s)^(T-1)) bound from 'How Much Cache Does Reasoning Need?' (arXiv:2604.17935) applies specifically to k-hop pointer chasing with locality-respecting cache controllers on single-model multi-step reasoning — NOT multi-step agentic tool-use workflows with external observation injection. The analogy is reasonable but the proposal presents it as direct motivation without this caveat. The empirical evidence (PM-KVQ, 'Hold Onto That Thought') is the stronger and more honest motivation.", "8B MODEL CAPABILITY CONCERN FOR AGENTIC BENCHMARKS: OpenHands achieves only ~12% on SWE-bench with models smaller than 32B. If both evaluation models (Qwen3-8B, DeepSeek-R1-Distill-8B) achieve very low base success rates, compression comparisons become statistically noisy and potentially meaningless. Consider including at least one stronger model (e.g., Qwen3-32B) or acknowledging this limitation and focusing on τ-bench where 8B models may perform better."]
Feedback: This is Round 7 of 10. The core contribution — trajectory-level Lagrangian for joint quant-eviction in agentic KV caches — is verified as genuinely novel via extensive independent search. The landscape analysis is exceptional. However, this review MUST issue a strong warning: 4 specific feedback items (NGC, CapKV, agent scaffold, benchmark table) have been requested in every round since Round 4 and remain unaddressed. If this pattern continues through Round 9, the verdict will be 'fail' based on inability to address reviewer feedback, regardless of the idea's theoretical merit.

To pass in Round 8, the generator MUST address ALL of the following — no exceptions:

1. **Cite NGC and CapKV** (copy-paste ready): 'NGC (April 2026, arXiv:2604.18002) learns trajectory-aware KV eviction via RL within single-model reasoning chains, jointly optimizing reasoning and memory management from task reward alone. TrajComp differs: training-free (vs. RL-required), joint quant-eviction (vs. eviction-only), and exploits agentic workflow structure with explicit step boundaries (vs. single-model reasoning traces).' 'CapKV (April 2026, arXiv:2604.25975) derives information-theoretic KV eviction via the Information Bottleneck principle with capacity-aware scoring. TrajComp differs: joint quant-eviction with trajectory-level objective vs. per-step information-theoretic eviction.'

2. **Fix MLA error**: Change '2 models covering standard attention and MLA' to '2 models using GQA attention.' Remove MLA adaptation from contributions or relabel it as future work. The approach section can mention MLA as a design consideration but must not claim it is evaluated.

3. **Specify agent scaffold**: 'We use SWE-agent with ReAct prompting, max 30 turns, 16K tokens per turn for SWE-bench Lite. For τ-bench, we use the official evaluation harness.' Then re-estimate per-instance timing realistically (8-12 min for 8B multi-turn on SWE-bench) and reduce instances to 100-150 to fit compute budget.

4. **Add user benchmark gap table**: | Benchmark | Status | Est. Cost | Reason | MMLU: included, 5h | LongBench: included, 20h | HumanEval: ADD IT, 2h | MT-Bench: ADD IT, 2h | Perplexity (Wiki/C4): ADD IT, 3h | RULER: dropped, ~100h, compute-prohibitive |

5. **Fix compute budget**: With realistic SWE-bench timing (100 instances × 10 min × 10 configs = ~167h) + τ-bench (~60h) + other benchmarks (~50h) + calibration (~10h) + dev/debug (~40h) = ~327h. Either request 300-350h with justification or cut SWE-bench to 50 instances.

6. **Soften theoretical claim**: Add one sentence: 'We note that this bound applies to k-hop pointer chasing in single-model reasoning; its extension to agentic tool-use with external observation injection is an analogy, not a formal proof. The empirical evidence from PM-KVQ and Hold Onto That Thought provides the primary motivation.'

7. **Address ForesightKV reproduction**: Either confirm a public checkpoint exists or replace with a simpler future-aware baseline (e.g., attention-pattern lookahead with sliding window) that can be implemented in <8h.

### Round 8 review
Verdict: revise
Issues: ["BASELINE REPRODUCTION RISK — ThinKV AND SideQuest HAVE NO PUBLIC CODE: Independent verification confirms neither ThinKV (ICLR 2026 Oral) nor SideQuest (Feb 2026) have released code, checkpoints, or implementations as of May 2026. ThinKV involves custom Triton kernels extending PagedAttention — reimplementation is non-trivial and could cost 20-40 H100-hours per baseline. Only R-KV and HqeKV have confirmed public code. Using 2 baselines without code in a 4-baseline plan creates significant execution risk.", "COMPUTE BUDGET 75% OVER USER CONSTRAINT: User specified ≤200 H100-hours as a HARD CONSTRAINT. Proposal requires ~350h. A concrete path to ~200h exists: reduce SWE-bench Lite to 50 instances (saves ~83h), reduce baselines from 4 to 3 by dropping either ThinKV or SideQuest (saves ~30-50h given no public code anyway), and tighten dev/debug buffer to 25h. Revised estimate: 50 SWE-bench × 2 models × 4 methods × 10min ≈ 67h + τ-bench 164 × 2 × 4 × 2min ≈ 44h + standard benchmarks ~40h + calibration 10h + ablations 15h + dev/debug 25h ≈ 201h.", "MODEL NAME ERROR: 'DeepSeek-R1-Distill-Qwen3-8B' does not exist. The correct model is 'DeepSeek-R1-0528-Qwen3-8B' (HuggingFace: deepseek-ai/DeepSeek-R1-0528-Qwen3-8B). It uses Qwen3-8B architecture with DeepSeek-R1-0528 tokenizer and achieves 86.0% on AIME 2024. The 'Distill' naming convention was used for Qwen2.5-based distillations, not Qwen3-based ones.", "VENUE AND TIMELINE MISMATCH: User's HARD CONSTRAINTS were ≤16 days and EMNLP 2026 (ARR May 25). Proposal explicitly declares EMNLP 2026 'NOT FEASIBLE' and targets AAAI 2027/ICLR 2027 — an honest acknowledgment, but this fundamentally fails to meet user requirements. The proposal should either commit to a drastically reduced EMNLP 2026 Findings sprint plan (1 model, 2 baselines with public code, 3 benchmarks, 4-page short paper, ~60h) or explicitly justify why this idea cannot serve the user's stated deadline."]
Feedback: This is a dramatically improved proposal — all 7 Round 7 feedback items are fully addressed for the first time, the landscape is exceptional (30+ papers), NGC and CapKV are properly cited and differentiated, the MLA error is fixed, the agent scaffold is specified, and the benchmark gap table is included. The core contribution (trajectory-level Lagrangian for agentic KV caches) is confirmed novel via exhaustive search. The proposal is close to pass quality but blocked by feasibility concerns:

1. **Fix baseline plan**: Replace ThinKV and/or SideQuest (no public code) with baselines that have confirmed code. Recommended 3-baseline plan: R-KV (public code, NeurIPS 2025), HqeKV (public code, ACL ARR 2026), and either (a) reimplemented ThinKV with 20-30h budgeted for Triton kernel development, or (b) a simpler proxy: uniform mixed-precision baseline (e.g., 4-bit/2-bit with attention-score-based partitioning) implementable in <8h. If ThinKV code releases before experiments begin (ICLR oral papers often release within months), add it.

2. **Fit within 200 H100-hours**: Reduce SWE-bench Lite to 50 instances (still statistically meaningful for pass-rate differences >5%), reduce baselines to 3 (only those with public code or easy reimplementation), and tighten dev/debug to 25h. This yields ~200h.

3. **Fix model name**: Change 'DeepSeek-R1-Distill-Qwen3-8B' to 'DeepSeek-R1-0528-Qwen3-8B' throughout. Verify tokenizer compatibility since it uses DeepSeek-R1-0528's tokenizer, not Qwen3's default.

4. **Resolve venue**: Either (a) commit to EMNLP 2026 Findings with a concrete 14-day sprint: Day 1-4 implement Lagrangian solver + phase detection on vLLM, Day 5-8 run experiments (Qwen3-8B only, 2 baselines with public code: R-KV + HqeKV, 3 benchmarks: 30 SWE-bench instances + MMLU + LongBench), Day 9-12 write 4-page short paper, Day 13-14 polish. ~60 H100-hours. OR (b) explicitly state EMNLP 2026 is not achievable and present this as an AAAI 2027/ICLR 2027 submission, accepting the user may choose a different idea for their EMNLP deadline.


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
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "type": "user",
  "uuid": "1ea254b7-b677-4c89-b90c-45899d152dc7",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T01:42:53.257Z_

```json
{
  "parentUuid": "1ea254b7-b677-4c89-b90c-45899d152dc7",
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
  "uuid": "5885b2f6-f963-4fdf-b246-5f955a76c5a6",
  "timestamp": "2026-05-12T01:42:53.257Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T01:42:53.257Z_

```json
{
  "parentUuid": "5885b2f6-f963-4fdf-b246-5f955a76c5a6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "45c6a8a7-d8b6-4c16-8520-93ae33aff160",
  "timestamp": "2026-05-12T01:42:53.257Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
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
  "leafUuid": "45c6a8a7-d8b6-4c16-8520-93ae33aff160",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Trajectory-aware joint KV cache compression for agentic LLMs",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

### Assistant

_source line 8 · 2026-05-12T01:43:14.206Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 9 of 10 for reviewing this ML research idea. Let me carefully analyze what's been addressed from previous rounds and conduct independent verification.

Let me first understand what was requested in Round 8 feedback:
1. Fix baseline plan - replace ThinKV/SideQuest (no public code) with baselines that have confirmed code
2. Fit within 200 H100-hours
3. Fix model name to DeepSeek-R1-0528-Qwen3-8B
4. Resolve venue - either commit to EMNLP 2026 Findings sprint or explicitly pivot


5. Address NGC and CapKV citations and differentiation
6. Fix MLA error regarding GQA
7. Specify agent scaffold details
8. Address benchmark gap table
9. Clarify γ calibration
10. Add caveat to theoretical claim about k-hop pointer chasing

Now examining the current proposal, I can see several key updates: NGC and CapKV are now properly cited with clear differentiation in the landscape and approach sections, the MLA error has been corrected with consistent GQA references throughout, the agent scaffold is now specified with SWE-agent using ReAct and τ-bench official harness, and the model name has been updated to the correct DeepSeek-R1-0528-Qwen3-8B designation.

The dual-track strategy commits to EMNLP 2026 short paper sprint as the primary target with ARR deadline May 25 (13 days), backed by a concrete plan: one model variant, two baselines with public code, three benchmarks, and approximately 60 H100-hours for a 4-page short paper. The ICLR 2027 full paper serves as the secondary extension path, scaling compute to around 200 H100-hours total.

For the sprint, I'm using R-KV and HqeKV as baselines since they have public implementations, while dropping ThinKV and SideQuest due to lack of available code. The benchmark coverage for EMNLP focuses on τ-bench as the primary agentic evaluation, plus LongBench and MMLU, with the ICLR extension adding HumanEval, MT-Bench, perplexity metrics, SWE-bench Lite, AIME 2025, and MATH-500. RULER got cut from the plan since it's too compute-intensive.

Now I'm running independent verification checks on the baselines and benchmarks to confirm feasibility.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45c6a8a7-d8b6-4c16-8520-93ae33aff160",
  "isSidechain": false,
  "requestId": "req_011CawpsB26UTU7GBApDB9EN",
  "type": "assistant",
  "uuid": "7baf1273-b356-4ac7-8c53-eb48b994fa52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFdoUMZD1fRT1atA145Lis",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32613,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1164,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 32613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32613
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

_source line 9 · 2026-05-12T01:43:14.209Z_

I'll conduct independent verification of this Round 9 proposal. Let me search for the key claims and check for any missed competitors or issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7baf1273-b356-4ac7-8c53-eb48b994fa52",
  "isSidechain": false,
  "requestId": "req_011CawpsB26UTU7GBApDB9EN",
  "type": "assistant",
  "uuid": "31e58208-29f2-4d8a-bed6-f01ab2d536d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFdoUMZD1fRT1atA145Lis",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32613,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1164,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 32613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32613
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

_source line 10 · 2026-05-12T01:43:21.826Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013uKud1rJPyhTEGz75ztW63`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify NGC and CapKV papers",
  "prompt": "Search the web to verify these two papers exist and check their details:\n\n1. \"Neural Garbage Collection\" (NGC) - arXiv:2604.18002, April 2026 - claims to learn trajectory-aware KV eviction via RL within single-model reasoning chains. Check: does it exist? What exactly does it do? Is it eviction-only? Does it require RL training?\n\n2. \"CapKV\" - arXiv:2604.25975 - claims to use Information Bottleneck principle for KV cache eviction with capacity-aware scoring. Check: does it exist? What exactly does it do?\n\n3. Also search for any NEW KV cache compression papers from April-May 2026 that might be competitors to a \"trajectory-aware joint quantization-eviction for agentic KV caches\" method. Search: \"KV cache compression agentic 2026\", \"KV cache agent workflow compression 2026\", \"trajectory KV cache 2026\"\n\nUse WebSearch for searches and WebFetch to read key paper abstracts. Report exact findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31e58208-29f2-4d8a-bed6-f01ab2d536d7",
  "isSidechain": false,
  "requestId": "req_011CawpsB26UTU7GBApDB9EN",
  "type": "assistant",
  "uuid": "7caaae15-5807-4d78-aac5-e64806d2a83c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFdoUMZD1fRT1atA145Lis",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32613,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1164,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 32613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32613
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

_source line 11 · 2026-05-12T01:45:20.530Z_

<details><summary>↩ Tool result · `toolu_013uKud1rJPyhTEGz75ztW63`</summary>

```text
Now I have comprehensive findings. Here is my report:

---

## Paper 1: Neural Garbage Collection (NGC) -- arXiv:2604.18002

**Status: CONFIRMED EXISTS.**

- **Exact title:** "Neural Garbage Collection: Learning to Forget while Learning to Reason"
- **Authors:** Michael Y. Li, Jubayer Ibn Hamid, Emily B. Fox, Noah D. Goodman
- **Date:** April 20, 2026
- **What it does:** The model periodically pauses during chain-of-thought reasoning, scores all KV cache blocks via its internal attention mechanism, samples a subset to keep, and permanently deletes the rest. It then continues reasoning on the pruned cache.
- **Eviction-only?** YES -- purely eviction, no quantization component.
- **Requires RL training?** YES -- it uses reinforcement learning end-to-end. Both reasoning tokens and cache-eviction decisions are treated as discrete actions sampled from the LM, optimized jointly from outcome-based task reward alone. No supervised fine-tuning or proxy objectives.
- **Benchmarks:** Countdown, AMC, AIME tasks.
- **Compression:** 2-3x peak KV cache size compression (the abstract says 2-3x; some summaries say 2-5x).
- **Scope:** Single-model reasoning chains only. Not multi-turn or agentic workflows.

## Paper 2: CapKV -- arXiv:2604.25975

**Status: CONFIRMED EXISTS.**

- **Exact title:** "Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective"
- **Authors:** Jiaming Yang, Chenwei Tang, Liangli Zhen, Jiancheng Lv
- **Date:** April 28, 2026
- **What it does:** Derives a closed-form mutual information objective from the Information Bottleneck principle under a linear-Gaussian surrogate of attention. Shows that many existing eviction heuristics are approximations of the same capacity-maximization principle. Introduces CapKV, which uses statistical leverage scores and a log-determinant approximation to select which KV entries to retain.
- **Eviction-only?** YES -- purely eviction-based, no quantization.
- **Training-free?** YES -- no RL or fine-tuning needed; it's a scoring method applied at inference time.
- **Scope:** General long-context benchmarks, not specifically agentic or trajectory-aware.

## Competitor Landscape: April-May 2026 KV Cache Compression Papers

Here are the most relevant recent papers, particularly those that might compete with a "trajectory-aware joint quantization-eviction for agentic KV caches" method:

### Joint Quantization + Eviction (most directly competitive):

1. **HqeKV** (OpenReview, ACL ARR Jan 2026) -- "Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference." Jointly applies quantization and eviction with a joint K-V importance metric and flexible multi-precision conversion policies. NOT trajectory-aware or agentic.

2. **ARKV** (arXiv:2603.08727, March 2026) -- "Adaptive and Resource-Efficient KV Cache Management." Dynamically ranks tokens and assigns them to three states: Original, Quantization, or Eviction, under a strict memory budget. Closest to joint quant-eviction under budget constraints. NOT agentic.

3. **EvicPress** (arXiv:2512.14946) -- "Joint KV-Cache Compression and Eviction for Efficient LLM Serving." Multi-tier storage with lossy compression + adaptive eviction. System-level, not trajectory-aware.

### Agentic-specific:

4. **CodeComp** (arXiv:2604.10235, April 11, 2026) -- "Structural KV Cache Compression for Agentic Coding." Training-free, uses Code Property Graphs for structure-aware eviction in agentic coding pipelines. Eviction-only, code-domain-specific, not joint quant-eviction.

5. **Agent Memory Below the Prompt** (arXiv:2603.04428, Feb 2026) -- Persistent Q4 KV cache for multi-agent LLM inference on edge. Quantizes and persists caches to disk for agent switching. Multi-agent but focused on cache persistence/reload, not compression during inference.

### RL-based eviction (related to NGC):

6. **ForesightKV** (arXiv:2602.03203, Feb 2026) -- Learns to predict which KV pairs to evict for reasoning models using a Markov Decision Process + GRPO. Evaluated on AIME benchmarks. Eviction-only, not joint with quantization.

7. **KV Policy (KVP)** (arXiv:2602.10238, Feb 2026) -- "Learning to Evict from Key-Value Cache." Per-head RL agents for eviction. Eviction-only.

### Quantization-only:

8. **RateQuant** (arXiv:2605.06675, April 2026) -- Mixed-precision KV cache quantization via rate-distortion theory. Per-head optimal bit allocation. Quantization-only, no eviction.

9. **TurboQuant** (Google, ICLR 2026) -- 3-bit KV cache quantization with 6x compression. Quantization-only.

### Key Gap Identified:

**No paper found from April-May 2026 combines ALL of:** (a) trajectory-awareness across multi-step/agentic workflows, (b) joint quantization + eviction, and (c) agentic KV cache management. The closest are HqeKV/ARKV for joint quant-eviction (but not agentic/trajectory-aware) and CodeComp for agentic compression (but eviction-only, code-specific). NGC uses RL for trajectory-aware eviction but is eviction-only within single reasoning chains, not agentic workflows.

Sources:
- [NGC - arXiv:2604.18002](https://arxiv.org/abs/2604.18002)
- [CapKV - arXiv:2604.25975](https://arxiv.org/abs/2604.25975)
- [CodeComp - arXiv:2604.10235](https://arxiv.org/abs/2604.10235)
- [HqeKV - OpenReview](https://openreview.net/forum?id=sLG2XsjSDe)
- [ARKV - arXiv:2603.08727](https://arxiv.org/html/2603.08727)
- [EvicPress - arXiv:2512.14946](https://arxiv.org/html/2512.14946)
- [ForesightKV - arXiv:2602.03203](https://arxiv.org/abs/2602.03203)
- [KV Policy - arXiv:2602.10238](https://arxiv.org/abs/2602.10238)
- [RateQuant - arXiv:2605.06675](https://arxiv.org/abs/2605.06675)
- [Agent Memory Below the Prompt - arXiv:2603.04428](https://arxiv.org/abs/2603.04428)
- [MarkTechPost Top 10 KV Cache Techniques](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)

agentId: a1def3fd557e01d90 (use SendMessage with to: 'a1def3fd557e01d90' to continue this agent)
&lt;usage>total_tokens: 25918
tool_uses: 15
duration_ms: 118696&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7caaae15-5807-4d78-aac5-e64806d2a83c",
  "isSidechain": false,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "type": "user",
  "uuid": "a8d488f9-acc4-4d4d-b0eb-a19ba3714e80",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify these two papers exist and check their details:\n\n1. \"Neural Garbage Collection\" (NGC) - arXiv:2604.18002, April 2026 - claims to learn trajectory-aware KV eviction via RL within single-model reasoning chains. Check: does it exist? What exactly does it do? Is it eviction-only? Does it require RL training?\n\n2. \"CapKV\" - arXiv:2604.25975 - claims to use Information Bottleneck principle for KV cache eviction with capacity-aware scoring. Check: does it exist? What exactly does it do?\n\n3. Also search for any NEW KV cache compression papers from April-May 2026 that might be competitors to a \"trajectory-aware joint quantization-eviction for agentic KV caches\" method. Search: \"KV cache compression agentic 2026\", \"KV cache agent workflow compression 2026\", \"trajectory KV cache 2026\"\n\nUse WebSearch for searches and WebFetch to read key paper abstracts. Report exact findings concisely.",
    "agentId": "a1def3fd557e01d90",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive findings. Here is my report:\n\n---\n\n## Paper 1: Neural Garbage Collection (NGC) -- arXiv:2604.18002\n\n**Status: CONFIRMED EXISTS.**\n\n- **Exact title:** \"Neural Garbage Collection: Learning to Forget while Learning to Reason\"\n- **Authors:** Michael Y. Li, Jubayer Ibn Hamid, Emily B. Fox, Noah D. Goodman\n- **Date:** April 20, 2026\n- **What it does:** The model periodically pauses during chain-of-thought reasoning, scores all KV cache blocks via its internal attention mechanism, samples a subset to keep, and permanently deletes the rest. It then continues reasoning on the pruned cache.\n- **Eviction-only?** YES -- purely eviction, no quantization component.\n- **Requires RL training?** YES -- it uses reinforcement learning end-to-end. Both reasoning tokens and cache-eviction decisions are treated as discrete actions sampled from the LM, optimized jointly from outcome-based task reward alone. No supervised fine-tuning or proxy objectives.\n- **Benchmarks:** Countdown, AMC, AIME tasks.\n- **Compression:** 2-3x peak KV cache size compression (the abstract says 2-3x; some summaries say 2-5x).\n- **Scope:** Single-model reasoning chains only. Not multi-turn or agentic workflows.\n\n## Paper 2: CapKV -- arXiv:2604.25975\n\n**Status: CONFIRMED EXISTS.**\n\n- **Exact title:** \"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective\"\n- **Authors:** Jiaming Yang, Chenwei Tang, Liangli Zhen, Jiancheng Lv\n- **Date:** April 28, 2026\n- **What it does:** Derives a closed-form mutual information objective from the Information Bottleneck principle under a linear-Gaussian surrogate of attention. Shows that many existing eviction heuristics are approximations of the same capacity-maximization principle. Introduces CapKV, which uses statistical leverage scores and a log-determinant approximation to select which KV entries to retain.\n- **Eviction-only?** YES -- purely eviction-based, no quantization.\n- **Training-free?** YES -- no RL or fine-tuning needed; it's a scoring method applied at inference time.\n- **Scope:** General long-context benchmarks, not specifically agentic or trajectory-aware.\n\n## Competitor Landscape: April-May 2026 KV Cache Compression Papers\n\nHere are the most relevant recent papers, particularly those that might compete with a \"trajectory-aware joint quantization-eviction for agentic KV caches\" method:\n\n### Joint Quantization + Eviction (most directly competitive):\n\n1. **HqeKV** (OpenReview, ACL ARR Jan 2026) -- \"Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference.\" Jointly applies quantization and eviction with a joint K-V importance metric and flexible multi-precision conversion policies. NOT trajectory-aware or agentic.\n\n2. **ARKV** (arXiv:2603.08727, March 2026) -- \"Adaptive and Resource-Efficient KV Cache Management.\" Dynamically ranks tokens and assigns them to three states: Original, Quantization, or Eviction, under a strict memory budget. Closest to joint quant-eviction under budget constraints. NOT agentic.\n\n3. **EvicPress** (arXiv:2512.14946) -- \"Joint KV-Cache Compression and Eviction for Efficient LLM Serving.\" Multi-tier storage with lossy compression + adaptive eviction. System-level, not trajectory-aware.\n\n### Agentic-specific:\n\n4. **CodeComp** (arXiv:2604.10235, April 11, 2026) -- \"Structural KV Cache Compression for Agentic Coding.\" Training-free, uses Code Property Graphs for structure-aware eviction in agentic coding pipelines. Eviction-only, code-domain-specific, not joint quant-eviction.\n\n5. **Agent Memory Below the Prompt** (arXiv:2603.04428, Feb 2026) -- Persistent Q4 KV cache for multi-agent LLM inference on edge. Quantizes and persists caches to disk for agent switching. Multi-agent but focused on cache persistence/reload, not compression during inference.\n\n### RL-based eviction (related to NGC):\n\n6. **ForesightKV** (arXiv:2602.03203, Feb 2026) -- Learns to predict which KV pairs to evict for reasoning models using a Markov Decision Process + GRPO. Evaluated on AIME benchmarks. Eviction-only, not joint with quantization.\n\n7. **KV Policy (KVP)** (arXiv:2602.10238, Feb 2026) -- \"Learning to Evict from Key-Value Cache.\" Per-head RL agents for eviction. Eviction-only.\n\n### Quantization-only:\n\n8. **RateQuant** (arXiv:2605.06675, April 2026) -- Mixed-precision KV cache quantization via rate-distortion theory. Per-head optimal bit allocation. Quantization-only, no eviction.\n\n9. **TurboQuant** (Google, ICLR 2026) -- 3-bit KV cache quantization with 6x compression. Quantization-only.\n\n### Key Gap Identified:\n\n**No paper found from April-May 2026 combines ALL of:** (a) trajectory-awareness across multi-step/agentic workflows, (b) joint quantization + eviction, and (c) agentic KV cache management. The closest are HqeKV/ARKV for joint quant-eviction (but not agentic/trajectory-aware) and CodeComp for agentic compression (but eviction-only, code-specific). NGC uses RL for trajectory-aware eviction but is eviction-only within single reasoning chains, not agentic workflows.\n\nSources:\n- [NGC - arXiv:2604.18002](https://arxiv.org/abs/2604.18002)\n- [CapKV - arXiv:2604.25975](https://arxiv.org/abs/2604.25975)\n- [CodeComp - arXiv:2604.10235](https://arxiv.org/abs/2604.10235)\n- [HqeKV - OpenReview](https://openreview.net/forum?id=sLG2XsjSDe)\n- [ARKV - arXiv:2603.08727](https://arxiv.org/html/2603.08727)\n- [EvicPress - arXiv:2512.14946](https://arxiv.org/html/2512.14946)\n- [ForesightKV - arXiv:2602.03203](https://arxiv.org/abs/2602.03203)\n- [KV Policy - arXiv:2602.10238](https://arxiv.org/abs/2602.10238)\n- [RateQuant - arXiv:2605.06675](https://arxiv.org/abs/2605.06675)\n- [Agent Memory Below the Prompt - arXiv:2603.04428](https://arxiv.org/abs/2603.04428)\n- [MarkTechPost Top 10 KV Cache Techniques](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)"
      }
    ],
    "totalDurationMs": 118696,
    "totalTokens": 25918,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2115,
      "cache_read_input_tokens": 21931,
      "output_tokens": 1871,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1871,
          "cache_read_input_tokens": 21931,
          "cache_creation_input_tokens": 2115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2115,
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
  "sourceToolAssistantUUID": "7caaae15-5807-4d78-aac5-e64806d2a83c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-12T01:45:32.114Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UtCsDPn5noJaAmoYra2pQB`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify R-KV and HqeKV code availability",
  "prompt": "Verify the following claims about baseline code availability for a KV cache compression research project:\n\n1. R-KV: Claimed to be at github.com/Zefan-Cai/R-KV with 1.2k stars and pip-installable with vLLM/SGLang integration. Search for this repo and verify: does it exist? How many stars? Is it pip-installable? What frameworks does it integrate with?\n\n2. HqeKV: Claimed to be at github.com/skywclouds/HqeKV with public code. Verify: does this repo exist? Does it have working code? Any CUDA kernel requirements?\n\n3. ThinKV: Claimed to have no public code as of May 2026, with a partial proxy via NVIDIA kvpress library. Verify: is there any public implementation of ThinKV? Check \"ThinKV code\" and \"kvpress ThinKV\".\n\n4. Also check: Does DeepSeek-R1-0528-Qwen3-8B exist on HuggingFace? Search for \"deepseek-ai/DeepSeek-R1-0528-Qwen3-8B\" on huggingface.\n\nUse WebSearch and WebFetch. Report exact findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8d488f9-acc4-4d4d-b0eb-a19ba3714e80",
  "isSidechain": false,
  "requestId": "req_011Cawq42DpM9KBjVCD7ZxdS",
  "type": "assistant",
  "uuid": "dbac727e-6ec1-48c6-b29e-897cab9aae1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q1vkCuzZ1aSgaGUvra447Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3108,
      "cache_read_input_tokens": 44454,
      "output_tokens": 400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 400,
          "cache_read_input_tokens": 44454,
          "cache_creation_input_tokens": 3108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3108
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

_source line 13 · 2026-05-12T01:47:57.660Z_

<details><summary>↩ Tool result · `toolu_01UtCsDPn5noJaAmoYra2pQB`</summary>

```text
Now I have all the information needed. Here are my findings:

---

## Verification Results

### 1. R-KV (github.com/Zefan-Cai/R-KV)

**Claim: 1.2k stars, pip-installable, vLLM/SGLang integration.**

- **Exists?** YES. The repo is live at `github.com/Zefan-Cai/R-KV` and tagged as a NeurIPS 2025 paper.
- **Stars:** **1.2k** -- this matches the claim exactly.
- **Pip-installable?** Partially true. There is a `setup.py` and you install via `pip install -e .` (editable/local install). There is NO public PyPI package (i.e., you cannot run `pip install rkv` from PyPI). So "pip-installable" is accurate only in the sense of local editable install from source.
- **Framework integration:** The repo contains dedicated folders for **vLLM**, **SGLang**, **FlashInfer**, and **HuggingFace**. The claim of vLLM/SGLang integration is **confirmed**, and it actually goes beyond that (FlashInfer + HuggingFace too).

**Verdict: Claim is largely accurate.** Star count matches. Framework integrations confirmed and exceed the claim. The pip-installability is local-only (`pip install -e .`), not from PyPI.

---

### 2. HqeKV (github.com/skywclouds/HqeKV)

**Claim: Public code exists at that URL.**

- **Exists?** YES. The repo is public at `github.com/skywclouds/HqeKV`.
- **Working code?** The repo contains config files, model implementations, a quantization module (`quant/`), test scripts (`tests/`), utility modules, and evaluation scripts. It appears to be functional code, though it only has 2 stars and 1 commit, suggesting it was recently published.
- **CUDA kernel requirements?** YES. The installation instructions explicitly require building custom CUDA kernels: `cd quant && pip install -e .`. This is a hard requirement.
- **Other notes:** Requires Python 3.13 via conda, plus standard dependencies from `requirements.txt`.

**Verdict: Claim is confirmed.** The repo exists and has public code. Notable additional detail: it requires custom CUDA kernel compilation, which could be a deployment friction point.

---

### 3. ThinKV (claimed: no public code as of May 2026, partial proxy via kvpress)

**Claim: No public ThinKV code; kvpress serves as a partial proxy.**

- **Public ThinKV code?** NO standalone public repository was found for ThinKV. The paper (arXiv 2510.01290) was accepted as an **ICLR 2026 Oral**, but no GitHub link appears in any search result, paper page, or OpenReview listing.
- **kvpress as proxy?** This claim needs clarification. NVIDIA's kvpress library contains **ThinKPress**, but this implements the **ThinK** method (arXiv 2407.21018, ICLR 2025) -- a *different* paper that does channel-dimension pruning of keys. **ThinK** (key dimension pruning) is NOT the same as **ThinKV** (thought-adaptive KV cache compression for reasoning models). They are distinct methods by different authors solving different problems:
  - **ThinK** = channel-level pruning of key cache dimensions based on query-driven importance.
  - **ThinKV** = thought-type-aware hybrid quantization + eviction strategy for reasoning models, with a custom PagedAttention kernel.

**Verdict: The claim that no public ThinKV code exists is confirmed.** However, the claim that kvpress ThinKPress serves as a "partial proxy" for ThinKV is **misleading** -- ThinKPress implements ThinK (a completely different method), not ThinKV. They share a similar name but are unrelated approaches.

---

### 4. DeepSeek-R1-0528-Qwen3-8B on HuggingFace

**Claim: Model exists at deepseek-ai/DeepSeek-R1-0528-Qwen3-8B.**

- **Exists?** YES. The model is live at `huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B`.
- **Key details:**
  - **Architecture:** Qwen3-8B base with DeepSeek-R1-0528 tokenizer
  - **Parameters:** 8B, BF16 tensor type
  - **Context length:** 128k tokens
  - **License:** MIT (commercial use + distillation allowed)
  - **Popularity:** ~139,712 downloads/month, ~1.06k likes
  - **Performance:** 86.0% pass@1 on AIME 2024, surpassing Qwen3-8B by +10.0%
  - **Community:** Multiple quantized variants available (GGUF from bartowski, lmstudio-community, unsloth; AWQ 4-bit; abliterated version)

**Verdict: Confirmed.** The model exists and is actively used.

agentId: a44c7415d55f72a83 (use SendMessage with to: 'a44c7415d55f72a83' to continue this agent)
&lt;usage>total_tokens: 22715
tool_uses: 13
duration_ms: 145541&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbac727e-6ec1-48c6-b29e-897cab9aae1f",
  "isSidechain": false,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "type": "user",
  "uuid": "20ebff15-1577-4806-92be-319fb2c3c89a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Verify the following claims about baseline code availability for a KV cache compression research project:\n\n1. R-KV: Claimed to be at github.com/Zefan-Cai/R-KV with 1.2k stars and pip-installable with vLLM/SGLang integration. Search for this repo and verify: does it exist? How many stars? Is it pip-installable? What frameworks does it integrate with?\n\n2. HqeKV: Claimed to be at github.com/skywclouds/HqeKV with public code. Verify: does this repo exist? Does it have working code? Any CUDA kernel requirements?\n\n3. ThinKV: Claimed to have no public code as of May 2026, with a partial proxy via NVIDIA kvpress library. Verify: is there any public implementation of ThinKV? Check \"ThinKV code\" and \"kvpress ThinKV\".\n\n4. Also check: Does DeepSeek-R1-0528-Qwen3-8B exist on HuggingFace? Search for \"deepseek-ai/DeepSeek-R1-0528-Qwen3-8B\" on huggingface.\n\nUse WebSearch and WebFetch. Report exact findings.",
    "agentId": "a44c7415d55f72a83",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Here are my findings:\n\n---\n\n## Verification Results\n\n### 1. R-KV (github.com/Zefan-Cai/R-KV)\n\n**Claim: 1.2k stars, pip-installable, vLLM/SGLang integration.**\n\n- **Exists?** YES. The repo is live at `github.com/Zefan-Cai/R-KV` and tagged as a NeurIPS 2025 paper.\n- **Stars:** **1.2k** -- this matches the claim exactly.\n- **Pip-installable?** Partially true. There is a `setup.py` and you install via `pip install -e .` (editable/local install). There is NO public PyPI package (i.e., you cannot run `pip install rkv` from PyPI). So \"pip-installable\" is accurate only in the sense of local editable install from source.\n- **Framework integration:** The repo contains dedicated folders for **vLLM**, **SGLang**, **FlashInfer**, and **HuggingFace**. The claim of vLLM/SGLang integration is **confirmed**, and it actually goes beyond that (FlashInfer + HuggingFace too).\n\n**Verdict: Claim is largely accurate.** Star count matches. Framework integrations confirmed and exceed the claim. The pip-installability is local-only (`pip install -e .`), not from PyPI.\n\n---\n\n### 2. HqeKV (github.com/skywclouds/HqeKV)\n\n**Claim: Public code exists at that URL.**\n\n- **Exists?** YES. The repo is public at `github.com/skywclouds/HqeKV`.\n- **Working code?** The repo contains config files, model implementations, a quantization module (`quant/`), test scripts (`tests/`), utility modules, and evaluation scripts. It appears to be functional code, though it only has 2 stars and 1 commit, suggesting it was recently published.\n- **CUDA kernel requirements?** YES. The installation instructions explicitly require building custom CUDA kernels: `cd quant && pip install -e .`. This is a hard requirement.\n- **Other notes:** Requires Python 3.13 via conda, plus standard dependencies from `requirements.txt`.\n\n**Verdict: Claim is confirmed.** The repo exists and has public code. Notable additional detail: it requires custom CUDA kernel compilation, which could be a deployment friction point.\n\n---\n\n### 3. ThinKV (claimed: no public code as of May 2026, partial proxy via kvpress)\n\n**Claim: No public ThinKV code; kvpress serves as a partial proxy.**\n\n- **Public ThinKV code?** NO standalone public repository was found for ThinKV. The paper (arXiv 2510.01290) was accepted as an **ICLR 2026 Oral**, but no GitHub link appears in any search result, paper page, or OpenReview listing.\n- **kvpress as proxy?** This claim needs clarification. NVIDIA's kvpress library contains **ThinKPress**, but this implements the **ThinK** method (arXiv 2407.21018, ICLR 2025) -- a *different* paper that does channel-dimension pruning of keys. **ThinK** (key dimension pruning) is NOT the same as **ThinKV** (thought-adaptive KV cache compression for reasoning models). They are distinct methods by different authors solving different problems:\n  - **ThinK** = channel-level pruning of key cache dimensions based on query-driven importance.\n  - **ThinKV** = thought-type-aware hybrid quantization + eviction strategy for reasoning models, with a custom PagedAttention kernel.\n\n**Verdict: The claim that no public ThinKV code exists is confirmed.** However, the claim that kvpress ThinKPress serves as a \"partial proxy\" for ThinKV is **misleading** -- ThinKPress implements ThinK (a completely different method), not ThinKV. They share a similar name but are unrelated approaches.\n\n---\n\n### 4. DeepSeek-R1-0528-Qwen3-8B on HuggingFace\n\n**Claim: Model exists at deepseek-ai/DeepSeek-R1-0528-Qwen3-8B.**\n\n- **Exists?** YES. The model is live at `huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B`.\n- **Key details:**\n  - **Architecture:** Qwen3-8B base with DeepSeek-R1-0528 tokenizer\n  - **Parameters:** 8B, BF16 tensor type\n  - **Context length:** 128k tokens\n  - **License:** MIT (commercial use + distillation allowed)\n  - **Popularity:** ~139,712 downloads/month, ~1.06k likes\n  - **Performance:** 86.0% pass@1 on AIME 2024, surpassing Qwen3-8B by +10.0%\n  - **Community:** Multiple quantized variants available (GGUF from bartowski, lmstudio-community, unsloth; AWQ 4-bit; abliterated version)\n\n**Verdict: Confirmed.** The model exists and is actively used."
      }
    ],
    "totalDurationMs": 145541,
    "totalTokens": 22715,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1897,
      "cache_read_input_tokens": 19531,
      "output_tokens": 1286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1897
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1286,
          "cache_read_input_tokens": 19531,
          "cache_creation_input_tokens": 1897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1897,
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
  "sourceToolAssistantUUID": "dbac727e-6ec1-48c6-b29e-897cab9aae1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "20ebff15-1577-4806-92be-319fb2c3c89a",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Trajectory-aware joint KV cache compression for agentic LLMs",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

### Tool call

_source line 16 · 2026-05-12T01:48:10.911Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BfoV44AYPAZbAabonqQtpX`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify τ-bench and EMNLP 2026 deadline",
  "prompt": "I need to verify several claims for a research proposal review:\n\n1. τ-bench (tau-bench): Search for this benchmark. Is it a real agentic evaluation benchmark? How many tasks does it have (claimed: 164)? Is there an official evaluation harness? Can 8B models achieve meaningful success rates on it? Search \"tau-bench benchmark LLM agent\" and \"tau-bench 164 tasks\".\n\n2. EMNLP 2026 ARR submission deadline: The proposal claims ARR May 25, 2026 deadline. Verify: search \"ACL Rolling Review May 2026 deadline\" and \"EMNLP 2026 submission deadline ARR\". Is May 25, 2026 a real ARR submission deadline?\n\n3. PM-KVQ: Search for this paper - \"PM-KVQ progressive mixed-precision KV cache quantization\". Does it exist? Does it show cumulative quantization error degrades long-CoT reasoning by up to 8%?\n\n4. \"Hold Onto That Thought\" paper (arXiv:2512.12008): Search for this. Does it exist? Does it show KV compression strategies designed for prefill degrade on reasoning tasks?\n\n5. \"How Much Cache Does Reasoning Need?\" (arXiv:2604.17935): Does this paper exist? Does it prove exponential error growth bounds for cache compression?\n\nUse WebSearch and WebFetch. Report exact findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20ebff15-1577-4806-92be-319fb2c3c89a",
  "isSidechain": false,
  "requestId": "req_011CawqFc3c13dkv3ifghpPa",
  "type": "assistant",
  "uuid": "bfd1c9c3-7e04-4b4d-86b6-15b862c35499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBxSbSQ8KtwoybayzQ8ftT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1765,
      "cache_read_input_tokens": 47562,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 438,
          "cache_read_input_tokens": 47562,
          "cache_creation_input_tokens": 1765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1765
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

_source line 17 · 2026-05-12T01:50:50.609Z_

<details><summary>↩ Tool result · `toolu_01BfoV44AYPAZbAabonqQtpX`</summary>

```text
Now I have all the information needed. Let me compile the findings.

---

Here are the verification results for all five claims:

## 1. tau-bench (tau-bench)

**Real benchmark: YES.** tau-bench is a genuine agentic evaluation benchmark from Sierra Research (arXiv:2406.12045), published at NeurIPS/ICLR. It evaluates tool-agent-user interaction in real-world customer service domains.

**164 tasks: CORRECT.** The original benchmark has exactly 164 tasks -- 50 in the airline domain and 114 in the retail domain. This was confirmed via the official tau3-bench task fixes blog post at [taubench.com](https://taubench.com/blog/tau3-task-fixes.html).

**Official evaluation harness: YES.** The GitHub repo ([sierra-research/tau-bench](https://github.com/sierra-research/tau-bench)) includes a `run.py` evaluation script and auto error identification tooling.

**8B models achieving meaningful success rates: DUBIOUS.** No 8B models appear on any official tau-bench leaderboard. The smallest models tested are in the 70B+ range (Llama-3-70B, Mistral-8x22B). One search result mentions that "Self-Challenging framework achieves over a two-fold improvement in Llama-3.1-8B-Instruct," suggesting some researchers have run 8B models on it, but with very low baseline performance requiring special training techniques. Even GPT-4o scores below 50% on average. A claim that 8B models achieve "meaningful" success rates should be treated skeptically without specific citations.

## 2. EMNLP 2026 ARR Submission Deadline

**May 25, 2026: CORRECT.** The official ACL Rolling Review [dates page](http://aclrollingreview.org/dates) lists May 25, 2026 as an ARR submission deadline. The [EMNLP 2026 official Twitter/X account](https://x.com/emnlpmeeting/status/2029508292637061462) confirms this is the ARR submission deadline for EMNLP 2026. Note: since EMNLP and AACL share the May ARR cycle, authors must declare their target conference at submission time (binding choice).

## 3. PM-KVQ

**Paper EXISTS: YES.** "PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs" is a real paper (arXiv:2505.18610) from Tsinghua University, with code on [GitHub](https://github.com/thu-nics/PM-KVQ).

**"Cumulative quantization error degrades long-CoT reasoning by up to 8%": MISLEADING/INVERTED.** The paper does identify cumulative quantization error as a problem with existing methods. However, the "8%" figure is not about degradation -- it is about PM-KVQ's **improvement**: "PM-KVQ improves reasoning benchmark performance by up to 8% over SOTA baselines under the same memory budget." The proposal appears to have reversed the direction of the claim. The paper shows their *solution* gains up to 8%, not that the *problem* causes 8% degradation.

## 4. "Hold Onto That Thought" (arXiv:2512.12008)

**Paper EXISTS: YES.** "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning" is real (arXiv:2512.12008, December 2025). It was presented at NeurIPS 2025 in San Diego.

**"KV compression strategies designed for prefill degrade on reasoning tasks": PARTIALLY ACCURATE but oversimplified.** The paper finds that "several popular strategies are targeted towards the prefill phase" and "their performance is rarely assessed on reasoning tasks requiring long decoding." The actual finding is more nuanced: for non-reasoning models (Llama-3.1-8B-Instruct), "no singular strategy fits all" and performance depends on dataset type. For reasoning models, specific strategies (H2O and a decoding-enabled SnapKV variant) that track important tokens during extended reasoning work well. So the paper shows prefill-focused strategies are *understudied* on reasoning tasks and don't universally work, rather than making a blanket claim that they all "degrade."

## 5. "How Much Cache Does Reasoning Need?" (arXiv:2604.17935)

**Paper EXISTS: YES.** "How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers" by Xiao Wang (April 2026) is real.

**"Proves exponential error growth bounds for cache compression": PARTIALLY CORRECT but incomplete.** The paper proves that **oblivious caches** (e.g., random eviction) exhibit exponential degradation in error probability. However, the paper's key finding is actually a *separation result*: **adaptive locality-respecting caches** (like heavy-hitter eviction) achieve error scaling that is **independent of reasoning depth** (linear, not exponential). Claiming the paper "proves exponential error growth bounds" omits the crucial nuance that this only applies to oblivious strategies, and that adaptive strategies avoid this entirely. The paper shows an Omega((n/s)^(T-1)) separation between the two approaches.

---

**Summary of claim accuracy:**
| Claim | Verdict |
|-------|---------|
| tau-bench is real, 164 tasks, has eval harness | CORRECT |
| 8B models achieve meaningful success on tau-bench | UNSUBSTANTIATED |
| EMNLP 2026 ARR deadline May 25 | CORRECT |
| PM-KVQ shows 8% degradation from cumulative error | MISCHARACTERIZED (8% is improvement of their method, not degradation from the problem) |
| "Hold Onto That Thought" shows prefill compression degrades reasoning | PARTIALLY ACCURATE (oversimplified) |
| arXiv:2604.17935 proves exponential error growth | PARTIALLY CORRECT (only for oblivious caches; adaptive caches avoid it) |

Sources:
- [tau-bench GitHub](https://github.com/sierra-research/tau-bench)
- [tau-bench arXiv paper](https://arxiv.org/abs/2406.12045)
- [tau3-bench task fixes](https://taubench.com/blog/tau3-task-fixes.html)
- [tau-bench official site](https://taubench.com/)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)
- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 Twitter announcement](https://x.com/emnlpmeeting/status/2029508292637061462)
- [PM-KVQ arXiv](https://arxiv.org/abs/2505.18610)
- [PM-KVQ GitHub](https://github.com/thu-nics/PM-KVQ)
- [Hold Onto That Thought arXiv](https://arxiv.org/abs/2512.12008)
- [How Much Cache Does Reasoning Need? arXiv](https://arxiv.org/abs/2604.17935v1)
- [BenchLM tau-bench leaderboard](https://benchlm.ai/benchmarks/tauBench)
- [HAL tau-bench Airline](https://hal.cs.princeton.edu/taubench_airline)

agentId: ab652819781f38e0d (use SendMessage with to: 'ab652819781f38e0d' to continue this agent)
&lt;usage>total_tokens: 26575
tool_uses: 27
duration_ms: 159694&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfd1c9c3-7e04-4b4d-86b6-15b862c35499",
  "isSidechain": false,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "type": "user",
  "uuid": "6c1e2fe1-bcd0-4e86-b469-63c09c37eeed",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify several claims for a research proposal review:\n\n1. τ-bench (tau-bench): Search for this benchmark. Is it a real agentic evaluation benchmark? How many tasks does it have (claimed: 164)? Is there an official evaluation harness? Can 8B models achieve meaningful success rates on it? Search \"tau-bench benchmark LLM agent\" and \"tau-bench 164 tasks\".\n\n2. EMNLP 2026 ARR submission deadline: The proposal claims ARR May 25, 2026 deadline. Verify: search \"ACL Rolling Review May 2026 deadline\" and \"EMNLP 2026 submission deadline ARR\". Is May 25, 2026 a real ARR submission deadline?\n\n3. PM-KVQ: Search for this paper - \"PM-KVQ progressive mixed-precision KV cache quantization\". Does it exist? Does it show cumulative quantization error degrades long-CoT reasoning by up to 8%?\n\n4. \"Hold Onto That Thought\" paper (arXiv:2512.12008): Search for this. Does it exist? Does it show KV compression strategies designed for prefill degrade on reasoning tasks?\n\n5. \"How Much Cache Does Reasoning Need?\" (arXiv:2604.17935): Does this paper exist? Does it prove exponential error growth bounds for cache compression?\n\nUse WebSearch and WebFetch. Report exact findings concisely.",
    "agentId": "ab652819781f38e0d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Let me compile the findings.\n\n---\n\nHere are the verification results for all five claims:\n\n## 1. tau-bench (tau-bench)\n\n**Real benchmark: YES.** tau-bench is a genuine agentic evaluation benchmark from Sierra Research (arXiv:2406.12045), published at NeurIPS/ICLR. It evaluates tool-agent-user interaction in real-world customer service domains.\n\n**164 tasks: CORRECT.** The original benchmark has exactly 164 tasks -- 50 in the airline domain and 114 in the retail domain. This was confirmed via the official tau3-bench task fixes blog post at [taubench.com](https://taubench.com/blog/tau3-task-fixes.html).\n\n**Official evaluation harness: YES.** The GitHub repo ([sierra-research/tau-bench](https://github.com/sierra-research/tau-bench)) includes a `run.py` evaluation script and auto error identification tooling.\n\n**8B models achieving meaningful success rates: DUBIOUS.** No 8B models appear on any official tau-bench leaderboard. The smallest models tested are in the 70B+ range (Llama-3-70B, Mistral-8x22B). One search result mentions that \"Self-Challenging framework achieves over a two-fold improvement in Llama-3.1-8B-Instruct,\" suggesting some researchers have run 8B models on it, but with very low baseline performance requiring special training techniques. Even GPT-4o scores below 50% on average. A claim that 8B models achieve \"meaningful\" success rates should be treated skeptically without specific citations.\n\n## 2. EMNLP 2026 ARR Submission Deadline\n\n**May 25, 2026: CORRECT.** The official ACL Rolling Review [dates page](http://aclrollingreview.org/dates) lists May 25, 2026 as an ARR submission deadline. The [EMNLP 2026 official Twitter/X account](https://x.com/emnlpmeeting/status/2029508292637061462) confirms this is the ARR submission deadline for EMNLP 2026. Note: since EMNLP and AACL share the May ARR cycle, authors must declare their target conference at submission time (binding choice).\n\n## 3. PM-KVQ\n\n**Paper EXISTS: YES.** \"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs\" is a real paper (arXiv:2505.18610) from Tsinghua University, with code on [GitHub](https://github.com/thu-nics/PM-KVQ).\n\n**\"Cumulative quantization error degrades long-CoT reasoning by up to 8%\": MISLEADING/INVERTED.** The paper does identify cumulative quantization error as a problem with existing methods. However, the \"8%\" figure is not about degradation -- it is about PM-KVQ's **improvement**: \"PM-KVQ improves reasoning benchmark performance by up to 8% over SOTA baselines under the same memory budget.\" The proposal appears to have reversed the direction of the claim. The paper shows their *solution* gains up to 8%, not that the *problem* causes 8% degradation.\n\n## 4. \"Hold Onto That Thought\" (arXiv:2512.12008)\n\n**Paper EXISTS: YES.** \"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning\" is real (arXiv:2512.12008, December 2025). It was presented at NeurIPS 2025 in San Diego.\n\n**\"KV compression strategies designed for prefill degrade on reasoning tasks\": PARTIALLY ACCURATE but oversimplified.** The paper finds that \"several popular strategies are targeted towards the prefill phase\" and \"their performance is rarely assessed on reasoning tasks requiring long decoding.\" The actual finding is more nuanced: for non-reasoning models (Llama-3.1-8B-Instruct), \"no singular strategy fits all\" and performance depends on dataset type. For reasoning models, specific strategies (H2O and a decoding-enabled SnapKV variant) that track important tokens during extended reasoning work well. So the paper shows prefill-focused strategies are *understudied* on reasoning tasks and don't universally work, rather than making a blanket claim that they all \"degrade.\"\n\n## 5. \"How Much Cache Does Reasoning Need?\" (arXiv:2604.17935)\n\n**Paper EXISTS: YES.** \"How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers\" by Xiao Wang (April 2026) is real.\n\n**\"Proves exponential error growth bounds for cache compression\": PARTIALLY CORRECT but incomplete.** The paper proves that **oblivious caches** (e.g., random eviction) exhibit exponential degradation in error probability. However, the paper's key finding is actually a *separation result*: **adaptive locality-respecting caches** (like heavy-hitter eviction) achieve error scaling that is **independent of reasoning depth** (linear, not exponential). Claiming the paper \"proves exponential error growth bounds\" omits the crucial nuance that this only applies to oblivious strategies, and that adaptive strategies avoid this entirely. The paper shows an Omega((n/s)^(T-1)) separation between the two approaches.\n\n---\n\n**Summary of claim accuracy:**\n| Claim | Verdict |\n|-------|---------|\n| tau-bench is real, 164 tasks, has eval harness | CORRECT |\n| 8B models achieve meaningful success on tau-bench | UNSUBSTANTIATED |\n| EMNLP 2026 ARR deadline May 25 | CORRECT |\n| PM-KVQ shows 8% degradation from cumulative error | MISCHARACTERIZED (8% is improvement of their method, not degradation from the problem) |\n| \"Hold Onto That Thought\" shows prefill compression degrades reasoning | PARTIALLY ACCURATE (oversimplified) |\n| arXiv:2604.17935 proves exponential error growth | PARTIALLY CORRECT (only for oblivious caches; adaptive caches avoid it) |\n\nSources:\n- [tau-bench GitHub](https://github.com/sierra-research/tau-bench)\n- [tau-bench arXiv paper](https://arxiv.org/abs/2406.12045)\n- [tau3-bench task fixes](https://taubench.com/blog/tau3-task-fixes.html)\n- [tau-bench official site](https://taubench.com/)\n- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)\n- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)\n- [EMNLP 2026 Twitter announcement](https://x.com/emnlpmeeting/status/2029508292637061462)\n- [PM-KVQ arXiv](https://arxiv.org/abs/2505.18610)\n- [PM-KVQ GitHub](https://github.com/thu-nics/PM-KVQ)\n- [Hold Onto That Thought arXiv](https://arxiv.org/abs/2512.12008)\n- [How Much Cache Does Reasoning Need? arXiv](https://arxiv.org/abs/2604.17935v1)\n- [BenchLM tau-bench leaderboard](https://benchlm.ai/benchmarks/tauBench)\n- [HAL tau-bench Airline](https://hal.cs.princeton.edu/taubench_airline)"
      }
    ],
    "totalDurationMs": 159694,
    "totalTokens": 26575,
    "totalToolUseCount": 27,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 24070,
      "output_tokens": 1834,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 670
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1834,
          "cache_read_input_tokens": 24070,
          "cache_creation_input_tokens": 670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 670,
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
      "otherToolCount": 27
    }
  },
  "sourceToolAssistantUUID": "bfd1c9c3-7e04-4b4d-86b6-15b862c35499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-12T01:51:04.289Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015u2ZNeRE47wTDLJt2Qbdcx`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for newest competitors May 2026",
  "prompt": "Search for very recent (April-May 2026) papers that might compete with a method called \"TrajComp\" that does trajectory-aware joint quantization-eviction for agentic KV caches. I need to find papers the proposal might have missed.\n\nSearch these specific queries:\n1. \"KV cache compression multi-turn 2026\" \n2. \"KV cache reasoning long chain-of-thought compression May 2026\"\n3. \"agentic LLM serving efficiency 2026\"\n4. \"KV cache eviction quantization joint optimization 2026\"\n5. \"speculative decoding KV cache agent 2026\"\n\nFor each search, note any papers NOT in this list of already-cited works: ThinKV, HqeKV, ARKV, NGC, CapKV, LookaheadKV, TTKV, TRIM-KV, RateQuant, Transactional Attention, MixedDimKV, PBKV, KVFlow, EpiCache, SideQuest, CodeComp, CacheTTL, R-KV, PM-KVQ, TriAttention, KVTC, DMS, EVICPRESS, TurboQuant, ForesightKV, KVComm, Self-Indexing KVCache.\n\nUse WebSearch. Report any genuinely new competitors that are missing from the proposal. Be concise."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c1e2fe1-bcd0-4e86-b469-63c09c37eeed",
  "isSidechain": false,
  "requestId": "req_011CawqUNCGzUkTG2hWkx8Vx",
  "type": "assistant",
  "uuid": "0317188b-5f72-42ad-9211-9d1e9ccfc858",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjRrzU9hWrwDAmP228dtRS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 49327,
      "output_tokens": 428,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2346,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 428,
          "cache_read_input_tokens": 49327,
          "cache_creation_input_tokens": 2346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2346
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

_source line 19 · 2026-05-12T01:53:45.465Z_

<details><summary>↩ Tool result · `toolu_015u2ZNeRE47wTDLJt2Qbdcx`</summary>

```text
Here is my consolidated report of papers that appear to be genuinely new competitors NOT already in the cited-works list.

---

## New Competitor Papers Not in the Cited List

### Directly Competing (joint quantization-eviction or trajectory/reasoning-aware compression)

1. **LaProx** (arXiv:2605.07234, May 2026) -- "Reformulating KV Cache Eviction Problem for Long-Context LLM Inference." Reformulates eviction as output-aware, layer-wise matrix multiplication approximation. Maintains performance with only 5% of the KV cache. Directly competes on the eviction-policy front.

2. **RLKV** (arXiv:2510.08525, ICLR 2026 Workshop) -- "Which Heads Matter for Reasoning? RL-Guided KV Cache Compression." Uses reinforcement learning to identify reasoning-critical heads, allocating full cache to them while aggressively compressing others. 20-50% cache reduction with near-lossless reasoning. Competes on reasoning-aware compression.

3. **LKV** (arXiv:2605.06676, May 2026) -- "End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction." First fully differentiable KV eviction framework. Learns head-wise budgets end-to-end, achieving 6.6x reduction at 200k context. Competes on learned eviction policy.

4. **eOptShrinkQ** (arXiv:2605.02905, May 2026) -- "Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization." Decomposes KV cache into low-rank shared component + quantized residual using random matrix theory. Saves ~1 bit/entry over TurboQuant. Competes on the quantization side.

5. **Hold Onto That Thought** (arXiv:2512.12008, under review ICLR 2026) -- Benchmarks KV cache compression methods specifically on long-decoding reasoning tasks. Finds heavy-hitter eviction strategies can sometimes *beat* full cache on reasoning. Relevant as a benchmark/analysis paper for reasoning-aware compression claims.

6. **Quantization Dominates Rank Reduction** (arXiv:2604.11501, April 2026) -- Rigorous comparison showing quantization consistently beats low-rank methods at matched storage. Provides theoretical argument (softmax decision-boundary sensitivity). Relevant to any joint quantization-eviction design decisions.

### Agentic / Multi-Turn Specific

7. **Agentix** (NSDI 2026, May 2026) -- "An Efficient Serving Engine for LLM Agents as General Programs." Program-aware scheduling for agentic LLM serving. Not KV-compression per se, but directly addresses agentic serving efficiency and could subsume or complement TrajComp's scheduling.

8. **CacheSlide** (FAST 2026, February 2026) -- "Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving." Identifies Relative-Position-Dependent Caching (RPDC) pattern in agent workflows. 3-4x latency reduction, 4-6x throughput improvement. Directly targets agent-workflow KV reuse.

9. **Agent Memory Below the Prompt** (arXiv:2603.04428, February 2026) -- Persistent Q4 KV cache for multi-agent edge inference. 136x TTFT reduction via disk-persisted quantized caches. Competes on the multi-agent quantized cache management angle.

10. **RocketKV-MT** (ICML 2025, but relevant) -- Multi-turn variant of RocketKV that retains all tokens across turns while constraining per-turn selection. Directly relevant to multi-turn trajectory-aware eviction.

11. **Efficient Serving for Dynamic Agent Workflows** (arXiv:2605.06472, May 2026) -- Note: this paper *is* PBKV, which is already in your cited list. Confirmed not new.

### Advanced Compression Techniques

12. **Attention Matching** (arXiv:2602.16284, February 2026) -- "Fast KV Compaction via Attention Matching." Achieves 50x compaction by constructing compact KVs that reproduce attention outputs. Orders of magnitude faster than gradient-based methods. A very strong competitor for aggressive compression.

13. **Sequential KV Cache Compression via Probabilistic Language Tries** (arXiv:2604.15356, April 2026) -- Exploits sequential redundancy across KV vectors using predictive delta coding. Theoretically achieves ~914x compression beyond TurboQuant's per-vector limit. Radical new direction for quantization.

14. **KVzip** (arXiv:2505.23416, NeurIPS 2025 Oral) -- Query-agnostic eviction using context reconstruction. 3-4x cache reduction. Relevant for multi-turn/multi-query reuse scenarios. Older but high-impact and not in the cited list.

15. **RetentiveKV** (arXiv:2605.04075, May 2026) -- State-space memory for multimodal KV cache eviction. Uses information entropy to avoid premature eviction of visually important tokens. 5x compression. Niche (multimodal) but novel eviction mechanism.

16. **KV Packet** (arXiv:2604.13226, April 2026) -- Recomputation-free context-independent KV caching using trainable soft-token adapters. Eliminates recomputation overhead for cache reuse across different contexts.

17. **QuantSpec** (arXiv:2502.10424, ICML 2025) -- Self-speculative decoding with hierarchical 4-bit quantized KV cache. 2.5x speedup. Relevant if TrajComp interacts with speculative decoding.

18. **CacheFlow** (arXiv:2604.25080, April 2026) -- 3D-parallel KV cache restoration for serving. Reduces TTFT by 10-62%. Systems-level competitor for agentic multi-turn serving.

---

## Summary of Highest-Priority Gaps

The most dangerous omissions from TrajComp's related work are:

- **LKV** and **LaProx** (both May 2026): learned/principled eviction methods that directly compete on the eviction half of joint optimization.
- **eOptShrinkQ** and **Sequential KV Compression via PLTs** (April-May 2026): advanced quantization methods that outperform TurboQuant, competing on the quantization half.
- **CacheSlide** and **Agentix** (FAST/NSDI 2026): systems papers directly targeting agent-workflow KV cache management.
- **Attention Matching** (February 2026): 50x compaction is a fundamentally different and very aggressive compression approach.
- **RLKV** (ICLR 2026): RL-guided reasoning-aware head selection directly overlaps with trajectory-aware reasoning compression.

Sources:
- [LaProx - Reformulating KV Cache Eviction](https://arxiv.org/abs/2605.07234)
- [RLKV - Which Heads Matter for Reasoning](https://arxiv.org/abs/2510.08525)
- [LKV - End-to-End Learning of Head-wise Budgets](https://arxiv.org/abs/2605.06676)
- [eOptShrinkQ](https://arxiv.org/abs/2605.02905)
- [Hold Onto That Thought](https://arxiv.org/abs/2512.12008)
- [Quantization Dominates Rank Reduction](https://arxiv.org/abs/2604.11501)
- [Agentix - NSDI 2026](https://www.usenix.org/conference/nsdi26/presentation/luo)
- [CacheSlide - FAST 2026](https://www.usenix.org/conference/fast26/presentation/liu-yang)
- [Agent Memory Below the Prompt](https://arxiv.org/abs/2603.04428)
- [RocketKV-MT](https://arxiv.org/abs/2502.14051)
- [Attention Matching](https://arxiv.org/abs/2602.16284)
- [Sequential KV Cache Compression via PLTs](https://arxiv.org/abs/2604.15356)
- [KVzip](https://arxiv.org/abs/2505.23416)
- [RetentiveKV](https://arxiv.org/abs/2605.04075)
- [KV Packet](https://arxiv.org/abs/2604.13226)
- [QuantSpec](https://arxiv.org/abs/2502.10424)
- [CacheFlow](https://arxiv.org/abs/2604.25080)
- [Top 10 KV Cache Compression Techniques - MarkTechPost](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)

agentId: aef8cf0a5e74b8ac5 (use SendMessage with to: 'aef8cf0a5e74b8ac5' to continue this agent)
&lt;usage>total_tokens: 37111
tool_uses: 25
duration_ms: 161170&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0317188b-5f72-42ad-9211-9d1e9ccfc858",
  "isSidechain": false,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "type": "user",
  "uuid": "503489dd-cd1a-4f97-9afe-46be587f2cb7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for very recent (April-May 2026) papers that might compete with a method called \"TrajComp\" that does trajectory-aware joint quantization-eviction for agentic KV caches. I need to find papers the proposal might have missed.\n\nSearch these specific queries:\n1. \"KV cache compression multi-turn 2026\" \n2. \"KV cache reasoning long chain-of-thought compression May 2026\"\n3. \"agentic LLM serving efficiency 2026\"\n4. \"KV cache eviction quantization joint optimization 2026\"\n5. \"speculative decoding KV cache agent 2026\"\n\nFor each search, note any papers NOT in this list of already-cited works: ThinKV, HqeKV, ARKV, NGC, CapKV, LookaheadKV, TTKV, TRIM-KV, RateQuant, Transactional Attention, MixedDimKV, PBKV, KVFlow, EpiCache, SideQuest, CodeComp, CacheTTL, R-KV, PM-KVQ, TriAttention, KVTC, DMS, EVICPRESS, TurboQuant, ForesightKV, KVComm, Self-Indexing KVCache.\n\nUse WebSearch. Report any genuinely new competitors that are missing from the proposal. Be concise.",
    "agentId": "aef8cf0a5e74b8ac5",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my consolidated report of papers that appear to be genuinely new competitors NOT already in the cited-works list.\n\n---\n\n## New Competitor Papers Not in the Cited List\n\n### Directly Competing (joint quantization-eviction or trajectory/reasoning-aware compression)\n\n1. **LaProx** (arXiv:2605.07234, May 2026) -- \"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference.\" Reformulates eviction as output-aware, layer-wise matrix multiplication approximation. Maintains performance with only 5% of the KV cache. Directly competes on the eviction-policy front.\n\n2. **RLKV** (arXiv:2510.08525, ICLR 2026 Workshop) -- \"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression.\" Uses reinforcement learning to identify reasoning-critical heads, allocating full cache to them while aggressively compressing others. 20-50% cache reduction with near-lossless reasoning. Competes on reasoning-aware compression.\n\n3. **LKV** (arXiv:2605.06676, May 2026) -- \"End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction.\" First fully differentiable KV eviction framework. Learns head-wise budgets end-to-end, achieving 6.6x reduction at 200k context. Competes on learned eviction policy.\n\n4. **eOptShrinkQ** (arXiv:2605.02905, May 2026) -- \"Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization.\" Decomposes KV cache into low-rank shared component + quantized residual using random matrix theory. Saves ~1 bit/entry over TurboQuant. Competes on the quantization side.\n\n5. **Hold Onto That Thought** (arXiv:2512.12008, under review ICLR 2026) -- Benchmarks KV cache compression methods specifically on long-decoding reasoning tasks. Finds heavy-hitter eviction strategies can sometimes *beat* full cache on reasoning. Relevant as a benchmark/analysis paper for reasoning-aware compression claims.\n\n6. **Quantization Dominates Rank Reduction** (arXiv:2604.11501, April 2026) -- Rigorous comparison showing quantization consistently beats low-rank methods at matched storage. Provides theoretical argument (softmax decision-boundary sensitivity). Relevant to any joint quantization-eviction design decisions.\n\n### Agentic / Multi-Turn Specific\n\n7. **Agentix** (NSDI 2026, May 2026) -- \"An Efficient Serving Engine for LLM Agents as General Programs.\" Program-aware scheduling for agentic LLM serving. Not KV-compression per se, but directly addresses agentic serving efficiency and could subsume or complement TrajComp's scheduling.\n\n8. **CacheSlide** (FAST 2026, February 2026) -- \"Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving.\" Identifies Relative-Position-Dependent Caching (RPDC) pattern in agent workflows. 3-4x latency reduction, 4-6x throughput improvement. Directly targets agent-workflow KV reuse.\n\n9. **Agent Memory Below the Prompt** (arXiv:2603.04428, February 2026) -- Persistent Q4 KV cache for multi-agent edge inference. 136x TTFT reduction via disk-persisted quantized caches. Competes on the multi-agent quantized cache management angle.\n\n10. **RocketKV-MT** (ICML 2025, but relevant) -- Multi-turn variant of RocketKV that retains all tokens across turns while constraining per-turn selection. Directly relevant to multi-turn trajectory-aware eviction.\n\n11. **Efficient Serving for Dynamic Agent Workflows** (arXiv:2605.06472, May 2026) -- Note: this paper *is* PBKV, which is already in your cited list. Confirmed not new.\n\n### Advanced Compression Techniques\n\n12. **Attention Matching** (arXiv:2602.16284, February 2026) -- \"Fast KV Compaction via Attention Matching.\" Achieves 50x compaction by constructing compact KVs that reproduce attention outputs. Orders of magnitude faster than gradient-based methods. A very strong competitor for aggressive compression.\n\n13. **Sequential KV Cache Compression via Probabilistic Language Tries** (arXiv:2604.15356, April 2026) -- Exploits sequential redundancy across KV vectors using predictive delta coding. Theoretically achieves ~914x compression beyond TurboQuant's per-vector limit. Radical new direction for quantization.\n\n14. **KVzip** (arXiv:2505.23416, NeurIPS 2025 Oral) -- Query-agnostic eviction using context reconstruction. 3-4x cache reduction. Relevant for multi-turn/multi-query reuse scenarios. Older but high-impact and not in the cited list.\n\n15. **RetentiveKV** (arXiv:2605.04075, May 2026) -- State-space memory for multimodal KV cache eviction. Uses information entropy to avoid premature eviction of visually important tokens. 5x compression. Niche (multimodal) but novel eviction mechanism.\n\n16. **KV Packet** (arXiv:2604.13226, April 2026) -- Recomputation-free context-independent KV caching using trainable soft-token adapters. Eliminates recomputation overhead for cache reuse across different contexts.\n\n17. **QuantSpec** (arXiv:2502.10424, ICML 2025) -- Self-speculative decoding with hierarchical 4-bit quantized KV cache. 2.5x speedup. Relevant if TrajComp interacts with speculative decoding.\n\n18. **CacheFlow** (arXiv:2604.25080, April 2026) -- 3D-parallel KV cache restoration for serving. Reduces TTFT by 10-62%. Systems-level competitor for agentic multi-turn serving.\n\n---\n\n## Summary of Highest-Priority Gaps\n\nThe most dangerous omissions from TrajComp's related work are:\n\n- **LKV** and **LaProx** (both May 2026): learned/principled eviction methods that directly compete on the eviction half of joint optimization.\n- **eOptShrinkQ** and **Sequential KV Compression via PLTs** (April-May 2026): advanced quantization methods that outperform TurboQuant, competing on the quantization half.\n- **CacheSlide** and **Agentix** (FAST/NSDI 2026): systems papers directly targeting agent-workflow KV cache management.\n- **Attention Matching** (February 2026): 50x compaction is a fundamentally different and very aggressive compression approach.\n- **RLKV** (ICLR 2026): RL-guided reasoning-aware head selection directly overlaps with trajectory-aware reasoning compression.\n\nSources:\n- [LaProx - Reformulating KV Cache Eviction](https://arxiv.org/abs/2605.07234)\n- [RLKV - Which Heads Matter for Reasoning](https://arxiv.org/abs/2510.08525)\n- [LKV - End-to-End Learning of Head-wise Budgets](https://arxiv.org/abs/2605.06676)\n- [eOptShrinkQ](https://arxiv.org/abs/2605.02905)\n- [Hold Onto That Thought](https://arxiv.org/abs/2512.12008)\n- [Quantization Dominates Rank Reduction](https://arxiv.org/abs/2604.11501)\n- [Agentix - NSDI 2026](https://www.usenix.org/conference/nsdi26/presentation/luo)\n- [CacheSlide - FAST 2026](https://www.usenix.org/conference/fast26/presentation/liu-yang)\n- [Agent Memory Below the Prompt](https://arxiv.org/abs/2603.04428)\n- [RocketKV-MT](https://arxiv.org/abs/2502.14051)\n- [Attention Matching](https://arxiv.org/abs/2602.16284)\n- [Sequential KV Cache Compression via PLTs](https://arxiv.org/abs/2604.15356)\n- [KVzip](https://arxiv.org/abs/2505.23416)\n- [RetentiveKV](https://arxiv.org/abs/2605.04075)\n- [KV Packet](https://arxiv.org/abs/2604.13226)\n- [QuantSpec](https://arxiv.org/abs/2502.10424)\n- [CacheFlow](https://arxiv.org/abs/2604.25080)\n- [Top 10 KV Cache Compression Techniques - MarkTechPost](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)"
      }
    ],
    "totalDurationMs": 161170,
    "totalTokens": 37111,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3158,
      "cache_read_input_tokens": 31679,
      "output_tokens": 2273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3158
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2273,
          "cache_read_input_tokens": 31679,
          "cache_creation_input_tokens": 3158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3158,
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
      "otherToolCount": 25
    }
  },
  "sourceToolAssistantUUID": "0317188b-5f72-42ad-9211-9d1e9ccfc858",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
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
  "leafUuid": "503489dd-cd1a-4f97-9afe-46be587f2cb7",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Trajectory-aware joint KV cache compression for agentic LLMs",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

### Assistant

_source line 22 · 2026-05-12T01:55:24.194Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now synthesize all findings and produce my review. Let me assess each dimension carefully.

## What was addressed from Round 8 feedback:

Round 8 had 4 key issues:
1. **Fix baseline plan** - Replace ThinKV/SideQuest (no public code) with baselines that have confirmed code → **ADDRESSED**. The EMNLP sprint now uses only R-KV and HqeKV (both with confirmed public code). ThinKV and SideQuest are dropped from the sprint. This is a good fix.

2. **Fit within 200 H100-hours** → **ADDRESSED**. 

The EMNLP sprint comes in at roughly 60 hours, and extending to ICLR brings the total to around 200 hours—this dual-track approach is well-structured.

3. **Fix model name** → **ADDRESSED**. DeepSeek-R1-0528-Qwen3-8B is the correct name and confirmed to exist on HuggingFace.

4. **Resolve venue** → **ADDRESSED**. The proposal now commits to EMNLP 2026 short paper sprint as PRIMARY (ARR May 25, 13 days), with ICLR 2027 as secondary extension. This is a concrete plan that addresses the user's requirement.

## Checking all previous persistent feedback items:

-

Now I'm verifying that all the major feedback items have been resolved: NGC and CapKV citations are in place, the MLA error is corrected with both models properly described as GQA, the agent scaffold uses SWE-agent with ReAct for the ICLR extension and τ-bench's official harness for the sprint, the benchmark gap table is comprehensive across both phases with RULER explicitly dropped due to compute constraints, and γ calibration has a concrete procedure outlined with KL divergence.

Moving through the remaining checklist—the theoretical k-hop pointer chasing caveat is explicit, phase detection uses pattern matching for structured frameworks with attention entropy as a fallback, wall-clock and throughput metrics are all covered, and ForesightKV has been replaced with reproducible baselines.

But now I'm catching a critical issue: the ThinKV proxy claim about NVIDIA's kvpress library implementing ThinKPress is inaccurate. ThinKPress actually implements ThinK (key dimension pruning from arXiv 2407.21018, ICLR 2025), not ThinKV, so this needs to be corrected or removed entirely.

There's also a mischaracterization with PM-KVQ—the proposal attributes an 8% degradation figure to cumulative quantization error, but that 8% is actually PM-KVQ's improvement over prior work. The underlying claim about cumulative error degrading reasoning is sound, just the specific number is inverted.

For τ-bench, I'm finding a critical issue: the proposal claims 8B models achieve meaningful success rates, but my search shows no 8B models actually appear on the official leaderboard, with even GPT-4o falling below 50%. If Qwen3-8B performs poorly here, the compression comparisons could become statistically unreliable, and the proposal should flag this risk upfront.

I'm also noticing some gaps in the related work—there are papers like CacheSlide and Agentix from recent systems venues that touch on KV optimization, though they approach it from reuse and program-aware serving angles rather than compression.

Looking at the more directly relevant papers, RLKV from the ICLR 2026 Workshop uses RL for reasoning-aware head selection in KV caches, which overlaps with the trajectory-aware compression idea, but it's workshop-level work focused on per-head budgets rather than trajectory-level error propagation, and it only handles eviction without joint quantization. The other candidates like LaProx and LKV are general eviction methods without agentic-specific considerations, so none of these directly compete with the core contribution.

Now assessing the novelty dimension: the trajectory-level Lagrangian formulation for joint quantization-eviction in agentic KV caches appears genuinely novel—no existing work combines all four elements of joint quant-eviction, multi-step trajectory objectives, training-free Lagrangian optimization, and exploitation of agentic workflow structure. The closest competitors like NGC handle trajectories but require RL and only do eviction on single models, while MixedDimKV takes a different approach entirely.

That said, I'm borrowing the Lagrangian optimization technique from MixedDimKV, temporal tiering overlaps with TTKV, and anchor protection echoes Transactional Attention—so the novelty really lies in the specific combination and the trajectory-level extension rather than a fundamentally new algorithmic technique. I'd rate this 4/5.

For feasibility, the positives are solid: the EMNLP sprint plan is concrete and well-scoped, R-KV and HqeKV have public implementations available, the DeepSeek model is on HuggingFace, and I have roughly 60 H100-hours budgeted for experiments.

But there are real risks here. The 8B model's performance on τ-bench is completely unverified—if Qwen3-8B scores below 5%, the entire contribution becomes untestable. HqeKV requires CUDA kernel compilation which could derail things, the 13-day timeline is brutally tight for implementation, calibration, experiments, and writing, and I've made some factual errors like conflating ThinKPress with ThinKV and mischaracterizing the PM-KVQ baseline. Still, stepping back, the sprint plan is actually quite well-thought-out with specific milestones and realistic resource allocation.

Looking at the next phase, there's a day-by-day timeline with fallback strategies for HqeKV, R-KV is proven with 1.2k stars, τ-bench has an official harness, and the ICLR extension gives us a backup plan. The real problem is the 8B claim—the proposal asserts these models achieve meaningful success on structured tasks, but I can't find evidence for that, and even GPT-4o struggles below 50% on τ-bench. If Qwen3-8B only hits 5%, we're comparing marginal differences that are statistically noise, though with 164 tasks across 2 domains there might be enough signal to work with.

The EMNLP sprint hinges on trajectory-level success rates, which requires baseline performance that might not exist. The proposal's claim about 8B models on customer-service tasks is unverified and critical—if it doesn't hold, the whole timeline collapses. Though I'm noticing DeepSeek-R1-0528-Qwen3-8B hits 86% on AIME 2024, which suggests the model class might be more capable than I initially thought.

The real question is whether reasoning ability translates to tool use and multi-turn agent interaction, which is what τ-bench actually tests. The model was optimized for reasoning, not for handling tool calls, so there's still significant uncertainty here. I'm settling on 3/5 for feasibility.

The proposal itself is exceptionally clear—the dual-track structure is well-defined, the landscape analysis covers 30+ papers, and the sprint timeline is concrete with specific daily milestones. The compute budget is transparent. There are minor issues like the ThinKPress/ThinKV confusion, but overall the organization is strong. That's a 4/5 for clarity.

On impact, agentic KV cache compression addresses a real problem as LLMs scale up in deployment contexts.

The trajectory-level framing is a genuine contribution. But the evaluation is constrained to 8B models where baseline performance on agentic tasks might already be too weak to show meaningful gains. A short paper at EMNLP Findings has moderate reach, and the cross-step error propagation model remains largely theoretical without empirical validation that it outperforms simpler per-step approaches. That brings impact to 3.5/5.

The average comes to 3.625, which falls short of the 4.0 threshold. Since this is Round 9 of 10, I need to weigh whether the 8B model risk and the ThinKPress confusion are deal-breakers or manageable issues that warrant revision rather than outright rejection.

Looking at the remaining gaps: the model size limitation is the biggest concern, though the other issues—the ThinKV mischaracterization, the PM-KVQ confusion, missing citations like RLKV and CacheSlide, and the compressed 13-day timeline—are all fixable. The core insight is genuinely novel and the proposal has evolved substantially over seven previous rounds of feedback. The EMNLP sprint plan is the riskier path due to τ-bench performance on smaller models, but the ICLR extension is more solid.

I'm being overly critical here. The proposal has shown real progress, and the EMNLP sprint is actually feasible—it only needs 60 H100-hours, which is well within budget constraints.  The approach itself is training-free, relying on a Lagrangian solver and phase detection, so the implementation risk is lower than I initially thought. The timeline is tight but the scope is deliberately constrained. Even if the 8B model struggles on τ-bench, the LongBench and MMLU results would still demonstrate whether TrajComp maintains quality under compression compared to baselines. The real test is whether trajectory-level optimization can deliver meaningful improvements on these benchmarks—and that's an empirical question, not a fundamental flaw. Revising my assessment: novelty is solid at 4/5 after exhaustive validation, feasibility is 3/5 given the 8B uncertainty and tight timeline but controlled scope, and clarity is exceptional at 4/5.

The core issue is the 8B model performance on τ-bench, which is the biggest unknown. I could provide specific, actionable feedback for one final round: acknowledge the 8B limitation with a contingency plan, correct the ThinKPress factual error, and clarify the PM-KVQ characterization. These are all manageable fixes. The idea is genuinely strong and close to passing—I think one more round of targeted revision is the right call. I'm settling on scores across novelty, feasibility, clarity, and impact that average to 3.625, which points toward a revise verdict. My feedback focuses on the most tractable issues: getting concrete about the 8B model performance risk with backup metrics, correcting the factual errors around ThinKPress and PM-KVQ, and adding RLKV as a reference point—all things the generator should be able to nail in one more iteration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "503489dd-cd1a-4f97-9afe-46be587f2cb7",
  "isSidechain": false,
  "requestId": "req_011CawqhF4X9i7Nu9XtA8QXg",
  "type": "assistant",
  "uuid": "be8ac6f7-51e6-462a-aae9-011a9b47e80e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMDh1h2SuWVb49sV63FmL4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2784,
      "cache_read_input_tokens": 51673,
      "output_tokens": 4257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4257,
          "cache_read_input_tokens": 51673,
          "cache_creation_input_tokens": 2784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2784
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

_source line 23 · 2026-05-12T01:55:24.199Z_

Now let me verify the EMNLP sprint's most critical risk — 8B model performance on τ-bench.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be8ac6f7-51e6-462a-aae9-011a9b47e80e",
  "isSidechain": false,
  "requestId": "req_011CawqhF4X9i7Nu9XtA8QXg",
  "type": "assistant",
  "uuid": "230aafad-ea9a-4278-aca1-45f19d5cd921",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMDh1h2SuWVb49sV63FmL4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2784,
      "cache_read_input_tokens": 51673,
      "output_tokens": 4257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4257,
          "cache_read_input_tokens": 51673,
          "cache_creation_input_tokens": 2784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2784
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

_source line 24 · 2026-05-12T01:55:29.990Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01RuksqvmJPAkVBBSUmKvEfV`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check 8B model performance on τ-bench",
  "prompt": "I need to find out whether 8B parameter LLMs can achieve meaningful success rates on τ-bench (tau-bench), an agentic customer service benchmark with 164 tasks.\n\nSearch for:\n1. \"tau-bench 8B\" or \"tau-bench Qwen3-8B\" or \"tau-bench small model\"\n2. \"tau-bench leaderboard\" or \"tau-bench results\"\n3. Check the tau-bench leaderboard at taubench.com or hal.cs.princeton.edu\n4. Search \"Qwen3-8B agent benchmark\" to see how Qwen3-8B performs on agentic tasks in general\n\nThe key question: if Qwen3-8B is evaluated on τ-bench 164 tasks, what success rate might it achieve? Is it likely above 10%? Above 20%? Would compression comparisons be statistically meaningful?\n\nAlso check: does DeepSeek-R1-0528-Qwen3-8B (a reasoning-focused model) have better agentic capabilities than base Qwen3-8B?\n\nUse WebSearch and WebFetch. Report concise findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "230aafad-ea9a-4278-aca1-45f19d5cd921",
  "isSidechain": false,
  "requestId": "req_011CawqhF4X9i7Nu9XtA8QXg",
  "type": "assistant",
  "uuid": "1674a7c5-43a8-4a80-8841-c1cff41cb7fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMDh1h2SuWVb49sV63FmL4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2784,
      "cache_read_input_tokens": 51673,
      "output_tokens": 4257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4257,
          "cache_read_input_tokens": 51673,
          "cache_creation_input_tokens": 2784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2784
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "1674a7c5-43a8-4a80-8841-c1cff41cb7fe",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Trajectory-aware joint KV cache compression for agentic LLMs",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

### Tool result

_source line 27 · 2026-05-12T01:58:58.211Z_

<details><summary>↩ Tool result · `toolu_01RuksqvmJPAkVBBSUmKvEfV`</summary>

```text
I now have enough data to provide a comprehensive answer. Here are my findings:

---

## Findings: 8B-class LLM Performance on tau-bench

### 1. Direct Evidence: DeepSeek-R1-0528-Qwen3-8B on tau-bench

The most critical finding is that **DeepSeek-R1-0528-Qwen3-8B has been directly evaluated on tau-bench** (from its [HuggingFace model card](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B)):

| Domain | Pass@1 |
|--------|--------|
| **Airline** | **53.5%** |
| **Retail** | **63.9%** |

This is a remarkably strong result for an 8B model. For context, on the same benchmark version:
- GPT-4o scores ~42.8% airline / ~60.3% retail
- GPT-4o-mini scores ~22.5% airline (from the original tau-bench GitHub README)
- GPT-4.1 nano scores 14.0% airline / 22.6% retail (from the official leaderboard)

The DeepSeek-R1-0528-Qwen3-8B model actually **outperforms GPT-4o** on tau-bench, which is extraordinary for an 8B model. It also scores 37.0 on BFCL_v3_MultiTurn.

### 2. Answering: Is Success Rate Above 10%? Above 20%?

**Yes, decisively.** An 8B model (DeepSeek-R1-0528-Qwen3-8B) achieves ~54% airline and ~64% retail, which is far above both the 10% and 20% thresholds. Even the weakest models on the leaderboard (GPT-4.1 nano) achieve 14% airline / 22.6% retail.

For base Qwen3-8B (without DeepSeek R1 distillation), no direct tau-bench score was found, but given that:
- DeepSeek-R1-0528-Qwen3-8B outperforms Qwen3-8B by ~10% on AIME
- The R1 distillation focuses on reasoning/CoT, not specifically tool calling
- Qwen3-8B already has native agentic and tool-calling capabilities

A reasonable estimate is that base Qwen3-8B would score somewhat lower but likely still in the **30-50% range** on tau-bench -- well above 20%.

### 3. DeepSeek-R1-0528-Qwen3-8B vs Base Qwen3-8B

From the HuggingFace model card, comparing the two on available benchmarks:

| Benchmark | DeepSeek-R1-0528-Qwen3-8B | Qwen3-8B | Delta |
|-----------|---------------------------|----------|-------|
| AIME 2024 | 86.0 | 76.0 | +10.0 |
| AIME 2025 | 76.3 | 67.3 | +8.9 |
| GPQA Diamond | 61.1 | 62.0 | -0.9 |
| Tau-Bench Airline | 53.5 | not reported | -- |
| Tau-Bench Retail | 63.9 | not reported | -- |
| BFCL_v3_MultiTurn | 37.0 | not reported | -- |

The R1 distillation dramatically improves math reasoning (+10%) while maintaining or slightly reducing general knowledge (GPQA). For agentic/tool-calling tasks, the R1 variant likely benefits from better chain-of-thought reasoning about when and how to call tools.

### 4. Would Compression Comparisons Be Statistically Meaningful?

**Yes.** With 164 tasks and expected success rates of 30-60%, you would be working with:
- At ~50% success rate: ~82 successes out of 164 tasks
- At ~30% success rate: ~49 successes out of 164 tasks

For comparing two compression levels (e.g., FP16 vs Q4_K_M), the standard error on a 50% rate with n=164 is ~3.9 percentage points, meaning a ~8pp difference would be detectable at p<0.05. This provides reasonable statistical power for meaningful compression comparisons.

However, note that tau-bench has inherent variance (the user simulator introduces randomness). The original paper recommends multiple runs (pass@k). The leaderboard typically uses 5 runs averaged to reduce variance.

### 5. Leaderboard Context (smallest models tested)

From the official tau-bench leaderboards, the smallest-class models that have been evaluated:

| Model | Airline | Retail | Approx Size |
|-------|---------|--------|-------------|
| GPT-4.1 nano | 14.0% | 22.6% | Unknown (small) |
| Claude 3.5 Haiku | 22.8% | 51.0% | Unknown (small) |
| GPT-4.1 mini | 36.0% | 55.8% | Unknown (medium) |
| GPT OSS 20B | -- | 54.8% | 20.9B total / 3.6B active (MoE) |
| o3-mini | 32.4% | 57.6% | Unknown |

No truly open-weight 8B models have appeared on the main leaderboard -- the DeepSeek-R1-0528-Qwen3-8B scores come from DeepSeek's own evaluation reported on HuggingFace.

### Bottom Line

- **Qwen3-8B class models can achieve 50-65% on tau-bench** (based on the DeepSeek-R1 distilled variant's published results)
- **Base Qwen3-8B likely achieves 30-50%**, well above your 10-20% thresholds
- **DeepSeek-R1-0528-Qwen3-8B is the better choice** for agentic tasks -- it has published tau-bench scores and outperforms GPT-4o
- **Compression comparisons would be statistically meaningful** at these success rates with 164 tasks, though multiple runs are recommended

Sources:
- [DeepSeek-R1-0528-Qwen3-8B Model Card (HuggingFace)](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B)
- [tau-bench GitHub Repository](https://github.com/sierra-research/tau-bench)
- [tau-bench Paper (arXiv:2406.12045)](https://arxiv.org/abs/2406.12045)
- [TAU-bench Airline Leaderboard](https://llm-stats.com/benchmarks/tau-bench-airline)
- [TAU-bench Retail Leaderboard](https://llm-stats.com/benchmarks/tau-bench-retail)
- [HAL TAU-bench Airline](https://hal.cs.princeton.edu/taubench_airline)
- [BenchLM TAU-bench](https://benchlm.ai/benchmarks/tauBench)
- [Qwen3-8B HuggingFace](https://huggingface.co/Qwen/Qwen3-8B)
- [Artificial Analysis - DeepSeek R1 Qwen3 8B](https://artificialanalysis.ai/models/deepseek-r1-qwen3-8b)
- [GPT-OSS 20B Benchmarks](https://llm-stats.com/models/gpt-oss-20b)

agentId: a361b6b66b21604d1 (use SendMessage with to: 'a361b6b66b21604d1' to continue this agent)
&lt;usage>total_tokens: 38975
tool_uses: 35
duration_ms: 208214&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1674a7c5-43a8-4a80-8841-c1cff41cb7fe",
  "isSidechain": false,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "type": "user",
  "uuid": "ce3d884d-688c-4f9e-ae52-7f182cb42c4f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find out whether 8B parameter LLMs can achieve meaningful success rates on τ-bench (tau-bench), an agentic customer service benchmark with 164 tasks.\n\nSearch for:\n1. \"tau-bench 8B\" or \"tau-bench Qwen3-8B\" or \"tau-bench small model\"\n2. \"tau-bench leaderboard\" or \"tau-bench results\"\n3. Check the tau-bench leaderboard at taubench.com or hal.cs.princeton.edu\n4. Search \"Qwen3-8B agent benchmark\" to see how Qwen3-8B performs on agentic tasks in general\n\nThe key question: if Qwen3-8B is evaluated on τ-bench 164 tasks, what success rate might it achieve? Is it likely above 10%? Above 20%? Would compression comparisons be statistically meaningful?\n\nAlso check: does DeepSeek-R1-0528-Qwen3-8B (a reasoning-focused model) have better agentic capabilities than base Qwen3-8B?\n\nUse WebSearch and WebFetch. Report concise findings.",
    "agentId": "a361b6b66b21604d1",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have enough data to provide a comprehensive answer. Here are my findings:\n\n---\n\n## Findings: 8B-class LLM Performance on tau-bench\n\n### 1. Direct Evidence: DeepSeek-R1-0528-Qwen3-8B on tau-bench\n\nThe most critical finding is that **DeepSeek-R1-0528-Qwen3-8B has been directly evaluated on tau-bench** (from its [HuggingFace model card](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B)):\n\n| Domain | Pass@1 |\n|--------|--------|\n| **Airline** | **53.5%** |\n| **Retail** | **63.9%** |\n\nThis is a remarkably strong result for an 8B model. For context, on the same benchmark version:\n- GPT-4o scores ~42.8% airline / ~60.3% retail\n- GPT-4o-mini scores ~22.5% airline (from the original tau-bench GitHub README)\n- GPT-4.1 nano scores 14.0% airline / 22.6% retail (from the official leaderboard)\n\nThe DeepSeek-R1-0528-Qwen3-8B model actually **outperforms GPT-4o** on tau-bench, which is extraordinary for an 8B model. It also scores 37.0 on BFCL_v3_MultiTurn.\n\n### 2. Answering: Is Success Rate Above 10%? Above 20%?\n\n**Yes, decisively.** An 8B model (DeepSeek-R1-0528-Qwen3-8B) achieves ~54% airline and ~64% retail, which is far above both the 10% and 20% thresholds. Even the weakest models on the leaderboard (GPT-4.1 nano) achieve 14% airline / 22.6% retail.\n\nFor base Qwen3-8B (without DeepSeek R1 distillation), no direct tau-bench score was found, but given that:\n- DeepSeek-R1-0528-Qwen3-8B outperforms Qwen3-8B by ~10% on AIME\n- The R1 distillation focuses on reasoning/CoT, not specifically tool calling\n- Qwen3-8B already has native agentic and tool-calling capabilities\n\nA reasonable estimate is that base Qwen3-8B would score somewhat lower but likely still in the **30-50% range** on tau-bench -- well above 20%.\n\n### 3. DeepSeek-R1-0528-Qwen3-8B vs Base Qwen3-8B\n\nFrom the HuggingFace model card, comparing the two on available benchmarks:\n\n| Benchmark | DeepSeek-R1-0528-Qwen3-8B | Qwen3-8B | Delta |\n|-----------|---------------------------|----------|-------|\n| AIME 2024 | 86.0 | 76.0 | +10.0 |\n| AIME 2025 | 76.3 | 67.3 | +8.9 |\n| GPQA Diamond | 61.1 | 62.0 | -0.9 |\n| Tau-Bench Airline | 53.5 | not reported | -- |\n| Tau-Bench Retail | 63.9 | not reported | -- |\n| BFCL_v3_MultiTurn | 37.0 | not reported | -- |\n\nThe R1 distillation dramatically improves math reasoning (+10%) while maintaining or slightly reducing general knowledge (GPQA). For agentic/tool-calling tasks, the R1 variant likely benefits from better chain-of-thought reasoning about when and how to call tools.\n\n### 4. Would Compression Comparisons Be Statistically Meaningful?\n\n**Yes.** With 164 tasks and expected success rates of 30-60%, you would be working with:\n- At ~50% success rate: ~82 successes out of 164 tasks\n- At ~30% success rate: ~49 successes out of 164 tasks\n\nFor comparing two compression levels (e.g., FP16 vs Q4_K_M), the standard error on a 50% rate with n=164 is ~3.9 percentage points, meaning a ~8pp difference would be detectable at p<0.05. This provides reasonable statistical power for meaningful compression comparisons.\n\nHowever, note that tau-bench has inherent variance (the user simulator introduces randomness). The original paper recommends multiple runs (pass@k). The leaderboard typically uses 5 runs averaged to reduce variance.\n\n### 5. Leaderboard Context (smallest models tested)\n\nFrom the official tau-bench leaderboards, the smallest-class models that have been evaluated:\n\n| Model | Airline | Retail | Approx Size |\n|-------|---------|--------|-------------|\n| GPT-4.1 nano | 14.0% | 22.6% | Unknown (small) |\n| Claude 3.5 Haiku | 22.8% | 51.0% | Unknown (small) |\n| GPT-4.1 mini | 36.0% | 55.8% | Unknown (medium) |\n| GPT OSS 20B | -- | 54.8% | 20.9B total / 3.6B active (MoE) |\n| o3-mini | 32.4% | 57.6% | Unknown |\n\nNo truly open-weight 8B models have appeared on the main leaderboard -- the DeepSeek-R1-0528-Qwen3-8B scores come from DeepSeek's own evaluation reported on HuggingFace.\n\n### Bottom Line\n\n- **Qwen3-8B class models can achieve 50-65% on tau-bench** (based on the DeepSeek-R1 distilled variant's published results)\n- **Base Qwen3-8B likely achieves 30-50%**, well above your 10-20% thresholds\n- **DeepSeek-R1-0528-Qwen3-8B is the better choice** for agentic tasks -- it has published tau-bench scores and outperforms GPT-4o\n- **Compression comparisons would be statistically meaningful** at these success rates with 164 tasks, though multiple runs are recommended\n\nSources:\n- [DeepSeek-R1-0528-Qwen3-8B Model Card (HuggingFace)](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B)\n- [tau-bench GitHub Repository](https://github.com/sierra-research/tau-bench)\n- [tau-bench Paper (arXiv:2406.12045)](https://arxiv.org/abs/2406.12045)\n- [TAU-bench Airline Leaderboard](https://llm-stats.com/benchmarks/tau-bench-airline)\n- [TAU-bench Retail Leaderboard](https://llm-stats.com/benchmarks/tau-bench-retail)\n- [HAL TAU-bench Airline](https://hal.cs.princeton.edu/taubench_airline)\n- [BenchLM TAU-bench](https://benchlm.ai/benchmarks/tauBench)\n- [Qwen3-8B HuggingFace](https://huggingface.co/Qwen/Qwen3-8B)\n- [Artificial Analysis - DeepSeek R1 Qwen3 8B](https://artificialanalysis.ai/models/deepseek-r1-qwen3-8b)\n- [GPT-OSS 20B Benchmarks](https://llm-stats.com/models/gpt-oss-20b)"
      }
    ],
    "totalDurationMs": 208214,
    "totalTokens": 38975,
    "totalToolUseCount": 35,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1844,
      "cache_read_input_tokens": 35203,
      "output_tokens": 1927,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1844
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1927,
          "cache_read_input_tokens": 35203,
          "cache_creation_input_tokens": 1844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1844,
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
      "otherToolCount": 35
    }
  },
  "sourceToolAssistantUUID": "1674a7c5-43a8-4a80-8841-c1cff41cb7fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-12T02:00:04.351Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important finding. DeepSeek-R1-0528-Qwen3-8B achieves 53.5% airline / 63.9% retail on τ-bench, which is very strong. This means 8B models CAN achieve meaningful success rates on τ-bench, contrary to my initial concern.

However, the proposal uses Qwen3-8B (not DeepSeek-R1-0528-Qwen3-8B) for the EMNLP sprint, reserving DeepSeek-R1-0528-Qwen3-8B for the ICLR extension. 

I'm noticing a potential mismatch here—the sprint is planned around Qwen3-8B to avoid tokenizer compatibility issues, but we only have confirmed τ-bench performance data for the DeepSeek variant. Since DeepSeek-R1-0528-Qwen3-8B has already demonstrated strong results, it might actually be worth reconsidering whether the sprint should use that model instead, despite the tokenizer complexity.

Now I'm catching some factual issues in the proposal itself. The ThinKPress reference is conflating two different techniques—ThinKPress actually implements ThinK (key dimension pruning), not ThinKV (thought-adaptive compression), which is a meaningful distinction. And on the PM-KVQ claim, the 8% figure appears to be mischaracterized—it's PM-KVQ's improvement over baselines, not the degradation it causes.

For the 8B model performance, the proposal correctly cites DeepSeek-R1-0528-Qwen3-8B's strong results on τ-bench, but it's unclear whether base Qwen3-8B (the actual sprint model) achieves similar performance, so that needs clarification. There are also some missing references like RLKV from the ICLR 2026 Workshop on reasoning-aware head selection, though it's more tangential given its focus on per-head budgets rather than trajectory-level optimization.

CacheSlide and Agentix are systems papers addressing agentic serving rather than compression directly, so while they'd strengthen the landscape context, they're not core competitors. Attention Matching is similarly orthogonal—its 50x compaction comes from a fundamentally different approach of constructing compact KVs rather than trajectory-level compression.

Looking at the overall picture, the proposal has genuinely addressed all the persistent feedback from the earlier rounds. The core novelty is solid, the EMNLP sprint timeline is realistic and well-structured, and the related work analysis is thorough. The main remaining issues are just a couple of minor factual corrections needed around ThinKPress and PM-KVQ's degradation claims, plus clarifying the 8B model performance for the actual sprint target.

Rescoring with this in mind: novelty holds at 4/5 since the exhaustive search across 30+ papers confirms no existing work combines trajectory-level joint quantization and eviction for agentic KV caches in this way—NGC requires RL and only handles eviction, MixedDimKV uses the Lagrangian technique but optimizes per-step rather than trajectory-level. Feasibility sits at 3.5/5 given the concrete EMNLP sprint plan is well-scoped at around 60 H100-hours.

The real tension is the model choice: using base Qwen3-8B avoids tokenizer compatibility debugging under time pressure, but DeepSeek-R1-0528-Qwen3-8B has confirmed τ-bench scores of 53-64% while Qwen3-8B's performance on that metric is unknown. R-KV and HqeKV have public code available, and the 13-day timeline is tight but minimal in scope—the main risk is whether the baseline model will actually demonstrate the expected performance gains, though HqeKV's CUDA kernel compilation is a known mitigation point. The clarity is strong with that comprehensive landscape review and structured timeline, though there are a couple of factual missteps. On impact, the work addresses a real problem and offers a fresh perspective on trajectory-level compression, but the 4-page venue limits reach, the empirical advantages over existing methods are still theoretical, and focusing only on 8B models weakens the generalizability argument. Averaging these scores puts it just under 4.0, though the gaps are fixable.

Looking at what's actually blocking: the ThinKPress error only appears in the background section and doesn't touch the method or results. The PM-KVQ characterization issue is in motivation but doesn't undermine the core contribution. Both are real mistakes but neither invalidates the work itself. I'm reconsidering whether these warrant a revise or if I should just pass it through.

The sprint model decision is genuinely a tradeoff—Qwen3-8B is cleaner while DeepSeek-R1-0528-Qwen3-8B has better benchmarks, but the architecture is identical so the method holds either way. My average score sits at 3.875, just under the 4.0 threshold for truly outstanding work. The question is whether this idea actually clears that bar or if these polish issues are symptoms of something more fundamental.

Looking at the strengths: the novelty is real after thorough verification, the dual-constrained Lagrangian with error calibration shows technical depth, the landscape review is comprehensive and honest, and agentic inference is genuinely the deployment reality. The execution plan is concrete and well-scoped with a clear dual-track approach.

But the weaknesses matter—the gains are still theoretical without empirical results, the method itself combines existing techniques rather than introducing something fundamentally new, the scope is modest for a short paper, and limiting evaluation to 8B models reduces the impact claim. This feels like solid work that addresses a real gap, but the contribution is incremental rather than transformative, so the 3.875 score seems appropriately calibrated.

The paper would be acceptable at EMNLP Findings but wouldn't reach oral presentation quality. I should revise with targeted fixes that should push it through Round 10 with modest score improvements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce3d884d-688c-4f9e-ae52-7f182cb42c4f",
  "isSidechain": false,
  "requestId": "req_011Cawr6JEQkf7XBWQGoye9V",
  "type": "assistant",
  "uuid": "f4f3ab8d-e0dd-4f8d-bda0-9e489486cd79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VRbNTxUYa3UXpoXfdzGhmF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6257,
      "cache_read_input_tokens": 54457,
      "output_tokens": 4348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4348,
          "cache_read_input_tokens": 54457,
          "cache_creation_input_tokens": 6257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6257
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

_source line 29 · 2026-05-12T02:00:39.757Z_

All verification is complete. Let me synthesize findings and issue my review.

**Key verification results:**
- NGC and CapKV confirmed real and properly differentiated
- R-KV (1.2k stars) and HqeKV (public code with CUDA kernels) verified
- DeepSeek-R1-0528-Qwen3-8B confirmed on HuggingFace with 53.5%/63.9% τ-bench scores
- EMNLP 2026 ARR May 25 deadline confirmed
- Novelty gap confirmed: no existing work combines trajectory-level joint quant-eviction for agentic KV caches
- Three factual issues discovered

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 4, "rationale": "Confirmed novel after 9 rounds of exhaustive search across 30+ papers. No existing work combines trajectory-level joint quant-eviction for agentic KV caches. NGC (RL-required, eviction-only, single-model), MixedDimKV (same Lagrangian but per-step), and HqeKV (joint quant-eviction but per-step) are the closest, all clearly differentiated."},
    "feasibility": {"score": 3, "rationale": "EMNLP sprint at ~60 H100-hours is well-scoped with confirmed baselines (R-KV, HqeKV). But the sprint uses Qwen3-8B whose τ-bench performance is UNVERIFIED — DeepSeek-R1-0528-Qwen3-8B has confirmed 53-64% success rates but is reserved for the ICLR extension. If Qwen3-8B scores <10% on τ-bench, the primary agentic benchmark is unusable and the 13-day sprint has no recovery path."},
    "clarity": {"score": 4, "rationale": "Exceptional landscape analysis (30+ papers with honest differentiation), concrete day-by-day sprint timeline, well-structured dual-track strategy. Minor factual errors: ThinKPress/ThinKV conflation and PM-KVQ 8% mischaracterization."},
    "impact": {"score": 3, "rationale": "Agentic KV cache compression is important and timely, but a 4-page EMNLP Findings short paper with 8B-only evaluation and hypothetical gains (no empirical validation yet) limits the contribution's visibility and persuasiveness. The trajectory-level perspective is genuinely valuable but incremental — it combines known techniques (Lagrangian from MixedDimKV, temporal tiering from TTKV, anchors from Transactional Attention) in a new context."}
  },
  "issues": [
    "FACTUAL ERROR — ThinKPress ≠ ThinKV: The proposal states 'partial proxy available via NVIDIA's kvpress library as ThinKPress.' Independent verification confirms ThinKPress implements ThinK (arXiv 2407.21018, ICLR 2025 — key dimension pruning), NOT ThinKV (ICLR 2026 Oral — thought-adaptive hybrid quant-eviction). These are completely different methods by different authors. Remove this misleading claim — ThinKV has NO public implementation whatsoever.",
    "FACTUAL ERROR — PM-KVQ 8% FIGURE REVERSED: The proposal states 'PM-KVQ demonstrates that directly quantizing KV cache at each decoding step causes cumulative quantization error that degrades long-CoT reasoning by up to 8% versus progressive strategies.' Independent verification shows the 8% figure is PM-KVQ's IMPROVEMENT over SOTA baselines, not the degradation amount. The direction of the claim is inverted. The overall message (cumulative quantization error is a problem) is correct from PM-KVQ's motivation, but the specific number is misattributed.",
    "SPRINT MODEL RISK — Qwen3-8B τ-bench PERFORMANCE UNVERIFIED: The EMNLP sprint uses Qwen3-8B as the sole model and τ-bench as the primary agentic benchmark. Independent search found NO published τ-bench scores for base Qwen3-8B. DeepSeek-R1-0528-Qwen3-8B achieves 53.5%/63.9% on τ-bench airline/retail (from its HuggingFace model card), but this model is reserved for the ICLR extension due to tokenizer compatibility concerns. If Qwen3-8B scores <15% on τ-bench, compression comparisons would be statistically meaningless with 164 tasks, leaving LongBench and MMLU as the only meaningful results — insufficient for a paper claiming trajectory-level agentic KV compression gains.",
    "MINOR — ADDITIONAL RECENT COMPETITORS: CacheSlide (FAST 2026) addresses cross-position-aware KV cache reuse for agentic workflows with 3-4x latency reduction. RLKV (ICLR 2026 Workshop, arXiv:2510.08525) uses RL for reasoning-aware per-head cache budget allocation. Neither directly competes with TrajComp's joint quant-eviction trajectory-level approach, but both are relevant and should be briefly cited in the landscape."
  ],
  "feedback": "This is Round 9 of 10 — the proposal has matured dramatically and all persistent feedback items from Rounds 1-8 are now fully addressed. The core contribution is verified as genuinely novel. Three targeted fixes for Round 10:\n\n1. **Fix sprint model choice**: Switch the EMNLP sprint model from Qwen3-8B to DeepSeek-R1-0528-Qwen3-8B. Rationale: DeepSeek-R1-0528-Qwen3-8B has CONFIRMED τ-bench scores of 53.5%/63.9% (from its HuggingFace model card), uses the same GQA architecture (32 query heads, 8 KV heads), and is the model where trajectory-level compression matters most (it generates long reasoning traces). The tokenizer difference only affects phase detection pattern matching — τ-bench uses structured tool-calling with explicit delimiters, so pattern matching on turn boundaries works regardless of tokenizer. If you insist on Qwen3-8B, you MUST run a quick τ-bench sanity check (Day 1, ~1 H100-hour, 10 tasks) to verify it achieves >20% success rate before committing 13 days to it.\n\n2. **Fix two factual errors**: (a) Remove the ThinKPress proxy claim — ThinKPress implements ThinK (ICLR 2025, key dimension pruning), NOT ThinKV. State clearly: 'ThinKV has no public code as of May 2026.' (b) Correct PM-KVQ characterization: 'PM-KVQ demonstrates that cumulative quantization error degrades long-CoT reasoning and proposes progressive mixed-precision to achieve up to 8% improvement over direct quantization baselines.'\n\n3. **Add 2 minor citations**: CacheSlide (FAST 2026, cross-position KV reuse for agentic serving — systems-level, no compression) and RLKV (ICLR 2026 Workshop — RL-guided per-head budget for reasoning, eviction-only). One line each in the landscape.\n\nThese three fixes should bring the proposal to pass quality for Round 10. The core idea, landscape, technical approach, dual-track strategy, and resource estimates are all solid.",
  "reason": "Genuinely novel idea with exceptional landscape analysis, but blocked by sprint model risk (Qwen3-8B's unverified τ-bench performance) and two factual errors (ThinKPress/ThinKV conflation, PM-KVQ 8% reversal) — all fixable in one round."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4f3ab8d-e0dd-4f8d-bda0-9e489486cd79",
  "isSidechain": false,
  "requestId": "req_011Cawr6JEQkf7XBWQGoye9V",
  "type": "assistant",
  "uuid": "cfe318e8-9e7d-4238-95d0-873406361198",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VRbNTxUYa3UXpoXfdzGhmF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6257,
      "cache_read_input_tokens": 54457,
      "output_tokens": 4348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4348,
          "cache_read_input_tokens": 54457,
          "cache_creation_input_tokens": 6257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6257
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "cfe318e8-9e7d-4238-95d0-873406361198",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Trajectory-aware joint KV cache compression for agentic LLMs",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "cfe318e8-9e7d-4238-95d0-873406361198",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Trajectory-aware joint KV cache compression for agentic LLMs",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3"
}
```

---
