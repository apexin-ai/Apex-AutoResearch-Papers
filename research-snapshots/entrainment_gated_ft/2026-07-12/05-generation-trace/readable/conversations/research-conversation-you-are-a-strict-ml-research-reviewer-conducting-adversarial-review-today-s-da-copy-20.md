# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-09 (UTC).** Your job: indep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/1ca4ec28-626f-47a3-8b64-c2f9893024cf.jsonl`
- **Structured JSON:** [`042ca0adaea4a8b5357d.json`](../../sessions/04/042ca0adaea4a8b5357d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-09T19:43:13.026Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-09T19:43:13.026Z",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-09 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.\n\nDirection: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.\n\nContribution type: METHOD ONLY. Propose new algorithms — not profiling studies.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Generous for efficiency work.\n2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.\n3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.\n\nLook for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.\n\nTag: direction=efficiency, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-09?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 1/10)\n{\n  \"title\": \"PRM-Score-Gated KV Compression for Efficient Inference-Time Tree Search\",\n  \"core_problem\": \"Test-time compute scaling via PRM-guided tree search (Best-of-N, beam search, MCTS) creates N simultaneous KV cache instances that grow with reasoning depth. Current systems either store full-precision KV for all trajectories (prohibitive memory at N≥8) or apply uniform compression that discards useful state from high-value trajectories alongside low-value ones. No method uses the PRM's trajectory quality signal to set per-trajectory KV compression budgets.\",\n  \"opportunity\": \"PRM step scores are already computed for each trajectory during search; these scores are a direct signal for how much KV precision a trajectory deserves. High-PRM-score trajectories need accurate KV to continue high-quality generation; low-scoring trajectories are likely to be pruned and can tolerate aggressive quantization or eviction without degrading final search quality. A PRM-score-gated compression policy assigns per-trajectory KV bit-widths from {FP16, INT8, INT4} inversely proportional to cumulative PRM score, with lazy dequantization on promotion and cheap discard on pruning. Prefix KV is shared across all trajectories via RadixAttention-style deduplication, reducing the per-trajectory overhead to only the divergent suffix. ETS (Feb 2025, arXiv:2502.13575) shows that purely algorithmic diversity-efficiency tradeoffs leave up to 1.4× throughput on the table — our compression-side approach is orthogonal and composable.\",\n  \"landscape\": \"ETS (Efficient Tree Search, Feb 2025, arXiv:2502.13575) improves inference-time scaling throughput 1.4× via diversity-aware trajectory pruning, identifying KV cache sharing as the bottleneck — but does not exploit PRM scores for per-trajectory compression. 'Inference-Time Hyper-Scaling with KV Cache Compression' (Jun 2025, arXiv:2506.05345) applies KV compression to scale inference compute but uses uniform compression rates not conditioned on per-trajectory verifier confidence. 'Beyond Speedup: Utilizing KV Cache for Sampling and Reasoning' (ICLR 2026, arXiv:2601.20326) repurposes KV caches as lightweight embeddings for path selection — closest in spirit but uses KV as a selector rather than a compressible resource. PM-KVQ (arXiv:2505.18610, NeurIPS 2025) applies progressive mixed-precision quantization to long-CoT LLMs based on transformer-layer sensitivity, not trajectory-level PRM quality. R-KV (arXiv:2505.24133, NeurIPS 2025) compresses KV via attention-based importance and intra-trajectory redundancy scoring but is single-trajectory and ignores multi-trajectory PRM-score differentials. SGLang RadixAttention (NeurIPS 2024, arXiv:2312.07104) enables shared-prefix KV deduplication but does not condition per-trajectory compression on PRM quality. Zero papers found that use PRM scores as a dynamic signal for per-trajectory KV cache compression budget in multi-trajectory tree search.\",\n  \"approach\": \"We implement PRM-Score-Gated KV Compression (PSG-KVC) by extending the open-source ETS codebase (SqueezeAILab/ETS) with a compression oracle that maps each trajectory's cumulative PRM step score to a KV bit-width tier: top-quartile trajectories retain FP16, middle-half use INT8, and bottom-quartile are quantized to INT4 using a fused kernel built on bitsandbytes. Shared prefix KV — covering the problem stem and all common branching-point tokens — is stored at FP16 and deduplicated via RadixAttention, so only the per-trajectory divergent suffix incurs compression; this prefix-sharing alone eliminates the majority of redundant KV storage before quantization is applied. We implement lazy dequantization for promoted trajectories, triggering on any step where a bottom-quartile branch receives a PRM score that elevates it to a higher tier, and immediate full discard for pruned branches so INT4 overhead does not persist past pruning time. An offline calibration sweep on a held-out 20% split of MATH-500 determines the score-percentile thresholds that maintain ≥99% of uncompressed accuracy, and these fixed thresholds are then applied zero-shot to AIME 2024/2025 and LiveBench Math. The policy model is DeepSeek-R1-Distil-Qwen-14B (current SOTA open-source reasoning model), run with N∈{4,8,16,32} beam-search trajectories on 2×A100 80GB nodes, with baselines including ETS + no compression, ETS + uniform INT4 (PM-KVQ style), ETS + attention-score-gated compression (R-KV style), and full-cache beam search.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200h A100 80GB\",\n      \"gpu_utilization\": \"Low (~30–40%): GPU idles while the researcher codes the compression oracle, debugs lazy-dequantization kernel correctness, and manually analyzes ablation results; compute bursts only during experiment runs of 2–5h each\",\n      \"timeline\": \"3–5 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$500–700 at ~$3/h A100 rental (Lambda Labs / Vast.ai)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~150h A100 80GB\",\n      \"gpu_utilization\": \"Moderate (~55–65%): agent queues experiments and writes ablation scripts continuously; human approval gates at kernel validation, threshold calibration, and result interpretation add bounded idle time rather than extended coding cycles\",\n      \"timeline\": \"4–6 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$100–200 (~1,000–2,000 conversation turns at ~$0.10/turn Opus)\",\n      \"estimated_gpu_cost\": \"~$400–500 at ~$3/h A100 rental\",\n      \"risk_note\": \"Lazy dequantization kernel correctness is the key technical risk — precision regressions after mid-search promotion events require human inspection; automatic test harness may miss subtle numerical instability in INT4→FP16 upcasting\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~600h A100 80GB (3–5× more ablations: threshold sweeps across 10+ percentile cuts, all three quantization formats, prefix-sharing on/off, N={4,8,16,32} scaling curves, sensitivity to PRM choice)\",\n      \"gpu_utilization\": \"High (~85–90%): agent schedules experiments 24/7; only inter-run setup (config writing, result parsing) adds brief idle intervals\",\n      \"timeline\": \"1–2 weeks with 4–8 A100s running in parallel\",\n      \"team\": \"0 (initial harness setup ~2h)\",\n      \"claude_api_cost\": \"$200–500 (~3,000–5,000 turns at ~$0.10/turn Opus)\",\n      \"estimated_gpu_cost\": \"~$1,500–2,000 at ~$3/h A100 rental\",\n      \"speed_bottleneck\": \"GPU node count (each 14B-model tree-search run requires 2×A100 80GB, limiting parallelism to GPU pool size) and API key rate limit for Opus at high turn frequency\",\n      \"risk_note\": \"Agent may over-invest in low-yield INT4 quantization format variants without convergence signal; calibration threshold sweep needs a human-defined stopping criterion or the agent will exhaustively grid-search beyond the point of diminishing returns\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR deadline May 25, 2026 — confirmed open)\",\n    \"AAAI 2027 (deadline TBD, historically announced August–September; conference February 2027)\",\n    \"ICLR 2027 (deadline TBD, historically announced September–October; no official CFP yet as of May 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"ETS: Efficient Tree Search for Inference-Time Scaling (arXiv 2025)\",\n    \"Inference-Time Hyper-Scaling with KV Cache Compression (arXiv 2025)\",\n    \"Beyond Speedup: Utilizing KV Cache for Sampling and Reasoning (ICLR 2026)\",\n    \"PM-KVQ: Progressive Mixed-Precision KV Cache Quantization for Long-CoT LLMs (NeurIPS 2025)\",\n    \"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models (NeurIPS 2025)\",\n    \"SGLang: Efficient Execution of Structured Language Model Programs (NeurIPS 2024)\",\n    \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv 2025)\"\n  ],\n  \"description\": \"PRM-Score-Gated KV Compression (PSG-KVC) addresses a critical memory bottleneck in PRM-guided tree search: N parallel trajectories generate N KV caches that grow with reasoning depth, yet current systems apply either full-precision storage (prohibitive at N≥8) or uniform compression that ignores trajectory quality. PSG-KVC repurposes the per-step PRM scores already computed during search as a compression oracle, dynamically assigning per-trajectory KV bit-widths — FP16 for top-quartile, INT8 for mid-range, INT4 for bottom-quartile trajectories — so likely-pruned branches use minimal memory while promising branches retain full precision. Shared prefix KV is deduplicated via RadixAttention, confining per-trajectory storage to the divergent suffix only. Lazy dequantization handles rare low-to-high promotions; immediate discard eliminates INT4 overhead on pruning. Built on the open-source ETS codebase and evaluated with DeepSeek-R1-Distil-Qwen-14B on MATH-500 and AIME 2024/2025, PSG-KVC targets 2–3× KV memory reduction at N=16 with less than 1% accuracy loss versus uncompressed beam search, fully composable with ETS's existing 1.4× algorithmic throughput gain. No prior work conditions per-trajectory KV compression budgets on PRM scores.\",\n  \"project_name\": \"prm_gated_kv_compress\",\n  \"source\": \"web_research\"\n}\n\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-09T19:43:13.031Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-09T19:43:13.031Z",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-09T19:43:13.059Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-09 (UTC).**

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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-09?
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

## Idea under review (round 1/10)
{
  "title": "PRM-Score-Gated KV Compression for Efficient Inference-Time Tree Search",
  "core_problem": "Test-time compute scaling via PRM-guided tree search (Best-of-N, beam search, MCTS) creates N simultaneous KV cache instances that grow with reasoning depth. Current systems either store full-precision KV for all trajectories (prohibitive memory at N≥8) or apply uniform compression that discards useful state from high-value trajectories alongside low-value ones. No method uses the PRM's trajectory quality signal to set per-trajectory KV compression budgets.",
  "opportunity": "PRM step scores are already computed for each trajectory during search; these scores are a direct signal for how much KV precision a trajectory deserves. High-PRM-score trajectories need accurate KV to continue high-quality generation; low-scoring trajectories are likely to be pruned and can tolerate aggressive quantization or eviction without degrading final search quality. A PRM-score-gated compression policy assigns per-trajectory KV bit-widths from {FP16, INT8, INT4} inversely proportional to cumulative PRM score, with lazy dequantization on promotion and cheap discard on pruning. Prefix KV is shared across all trajectories via RadixAttention-style deduplication, reducing the per-trajectory overhead to only the divergent suffix. ETS (Feb 2025, arXiv:2502.13575) shows that purely algorithmic diversity-efficiency tradeoffs leave up to 1.4× throughput on the table — our compression-side approach is orthogonal and composable.",
  "landscape": "ETS (Efficient Tree Search, Feb 2025, arXiv:2502.13575) improves inference-time scaling throughput 1.4× via diversity-aware trajectory pruning, identifying KV cache sharing as the bottleneck — but does not exploit PRM scores for per-trajectory compression. 'Inference-Time Hyper-Scaling with KV Cache Compression' (Jun 2025, arXiv:2506.05345) applies KV compression to scale inference compute but uses uniform compression rates not conditioned on per-trajectory verifier confidence. 'Beyond Speedup: Utilizing KV Cache for Sampling and Reasoning' (ICLR 2026, arXiv:2601.20326) repurposes KV caches as lightweight embeddings for path selection — closest in spirit but uses KV as a selector rather than a compressible resource. PM-KVQ (arXiv:2505.18610, NeurIPS 2025) applies progressive mixed-precision quantization to long-CoT LLMs based on transformer-layer sensitivity, not trajectory-level PRM quality. R-KV (arXiv:2505.24133, NeurIPS 2025) compresses KV via attention-based importance and intra-trajectory redundancy scoring but is single-trajectory and ignores multi-trajectory PRM-score differentials. SGLang RadixAttention (NeurIPS 2024, arXiv:2312.07104) enables shared-prefix KV deduplication but does not condition per-trajectory compression on PRM quality. Zero papers found that use PRM scores as a dynamic signal for per-trajectory KV cache compression budget in multi-trajectory tree search.",
  "approach": "We implement PRM-Score-Gated KV Compression (PSG-KVC) by extending the open-source ETS codebase (SqueezeAILab/ETS) with a compression oracle that maps each trajectory's cumulative PRM step score to a KV bit-width tier: top-quartile trajectories retain FP16, middle-half use INT8, and bottom-quartile are quantized to INT4 using a fused kernel built on bitsandbytes. Shared prefix KV — covering the problem stem and all common branching-point tokens — is stored at FP16 and deduplicated via RadixAttention, so only the per-trajectory divergent suffix incurs compression; this prefix-sharing alone eliminates the majority of redundant KV storage before quantization is applied. We implement lazy dequantization for promoted trajectories, triggering on any step where a bottom-quartile branch receives a PRM score that elevates it to a higher tier, and immediate full discard for pruned branches so INT4 overhead does not persist past pruning time. An offline calibration sweep on a held-out 20% split of MATH-500 determines the score-percentile thresholds that maintain ≥99% of uncompressed accuracy, and these fixed thresholds are then applied zero-shot to AIME 2024/2025 and LiveBench Math. The policy model is DeepSeek-R1-Distil-Qwen-14B (current SOTA open-source reasoning model), run with N∈{4,8,16,32} beam-search trajectories on 2×A100 80GB nodes, with baselines including ETS + no compression, ETS + uniform INT4 (PM-KVQ style), ETS + attention-score-gated compression (R-KV style), and full-cache beam search.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200h A100 80GB",
      "gpu_utilization": "Low (~30–40%): GPU idles while the researcher codes the compression oracle, debugs lazy-dequantization kernel correctness, and manually analyzes ablation results; compute bursts only during experiment runs of 2–5h each",
      "timeline": "3–5 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$500–700 at ~$3/h A100 rental (Lambda Labs / Vast.ai)"
    },
    "human_in_loop": {
      "gpu_hours": "~150h A100 80GB",
      "gpu_utilization": "Moderate (~55–65%): agent queues experiments and writes ablation scripts continuously; human approval gates at kernel validation, threshold calibration, and result interpretation add bounded idle time rather than extended coding cycles",
      "timeline": "4–6 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$100–200 (~1,000–2,000 conversation turns at ~$0.10/turn Opus)",
      "estimated_gpu_cost": "~$400–500 at ~$3/h A100 rental",
      "risk_note": "Lazy dequantization kernel correctness is the key technical risk — precision regressions after mid-search promotion events require human inspection; automatic test harness may miss subtle numerical instability in INT4→FP16 upcasting"
    },
    "auto_research": {
      "gpu_hours": "~600h A100 80GB (3–5× more ablations: threshold sweeps across 10+ percentile cuts, all three quantization formats, prefix-sharing on/off, N={4,8,16,32} scaling curves, sensitivity to PRM choice)",
      "gpu_utilization": "High (~85–90%): agent schedules experiments 24/7; only inter-run setup (config writing, result parsing) adds brief idle intervals",
      "timeline": "1–2 weeks with 4–8 A100s running in parallel",
      "team": "0 (initial harness setup ~2h)",
      "claude_api_cost": "$200–500 (~3,000–5,000 turns at ~$0.10/turn Opus)",
      "estimated_gpu_cost": "~$1,500–2,000 at ~$3/h A100 rental",
      "speed_bottleneck": "GPU node count (each 14B-model tree-search run requires 2×A100 80GB, limiting parallelism to GPU pool size) and API key rate limit for Opus at high turn frequency",
      "risk_note": "Agent may over-invest in low-yield INT4 quantization format variants without convergence signal; calibration threshold sweep needs a human-defined stopping criterion or the agent will exhaustively grid-search beyond the point of diminishing returns"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR deadline May 25, 2026 — confirmed open)",
    "AAAI 2027 (deadline TBD, historically announced August–September; conference February 2027)",
    "ICLR 2027 (deadline TBD, historically announced September–October; no official CFP yet as of May 2026)"
  ],
  "level": "solid",
  "key_references": [
    "ETS: Efficient Tree Search for Inference-Time Scaling (arXiv 2025)",
    "Inference-Time Hyper-Scaling with KV Cache Compression (arXiv 2025)",
    "Beyond Speedup: Utilizing KV Cache for Sampling and Reasoning (ICLR 2026)",
    "PM-KVQ: Progressive Mixed-Precision KV Cache Quantization for Long-CoT LLMs (NeurIPS 2025)",
    "R-KV: Redundancy-aware KV Cache Compression for Reasoning Models (NeurIPS 2025)",
    "SGLang: Efficient Execution of Structured Language Model Programs (NeurIPS 2024)",
    "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv 2025)"
  ],
  "description": "PRM-Score-Gated KV Compression (PSG-KVC) addresses a critical memory bottleneck in PRM-guided tree search: N parallel trajectories generate N KV caches that grow with reasoning depth, yet current systems apply either full-precision storage (prohibitive at N≥8) or uniform compression that ignores trajectory quality. PSG-KVC repurposes the per-step PRM scores already computed during search as a compression oracle, dynamically assigning per-trajectory KV bit-widths — FP16 for top-quartile, INT8 for mid-range, INT4 for bottom-quartile trajectories — so likely-pruned branches use minimal memory while promising branches retain full precision. Shared prefix KV is deduplicated via RadixAttention, confining per-trajectory storage to the divergent suffix only. Lazy dequantization handles rare low-to-high promotions; immediate discard eliminates INT4 overhead on pruning. Built on the open-source ETS codebase and evaluated with DeepSeek-R1-Distil-Qwen-14B on MATH-500 and AIME 2024/2025, PSG-KVC targets 2–3× KV memory reduction at N=16 with less than 1% accuracy loss versus uncompressed beam search, fully composable with ETS's existing 1.4× algorithmic throughput gain. No prior work conditions per-trajectory KV compression budgets on PRM scores.",
  "project_name": "prm_gated_kv_compress",
  "source": "web_research"
}



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
  "promptId": "f3fa5027-4a94-46c0-bb8d-7ed240d28059",
  "type": "user",
  "uuid": "1c3aa44c-2049-4ed3-8ce5-acbf29d4d32f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-09T19:43:13.058Z_

```json
{
  "parentUuid": "1c3aa44c-2049-4ed3-8ce5-acbf29d4d32f",
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
  "uuid": "b30b0802-ef98-4152-8a72-133e80dc2458",
  "timestamp": "2026-05-09T19:43:13.058Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-09T19:43:13.058Z_

```json
{
  "parentUuid": "b30b0802-ef98-4152-8a72-133e80dc2458",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "540c0482-af0d-4fe8-aa59-07b915848204",
  "timestamp": "2026-05-09T19:43:13.058Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "540c0482-af0d-4fe8-aa59-07b915848204",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify PRM-gated KV compression idea for EMNLP 2026",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf"
}
```

---

### Assistant

_source line 8 · 2026-05-09T19:43:23.743Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this idea carefully. The proposal is about "PRM-Score-Gated KV Compression for Efficient Inference-Time Tree Search" (PSG-KVC). I need to independently verify claims, check novelty, feasibility, and assess if this meets the user's requirements for EMNLP 2026.

Let me start by searching for the key papers cited and looking for related/competing work that might not have been mentioned.

Key things to verify:
1. Does ETS (arXiv:2502.13575) actually exist and say what's claimed?


2. I should check whether the other cited papers actually exist and match their descriptions—including "Inference-Time Hyper-Scaling with KV Cache Compression" from June 2025, the ICLR 2026 paper on KV cache for sampling and reasoning, PM-KVQ, and R-KV—and identify any concurrent or competing work in this space.

3. The core novelty here seems to be using PRM scores to control KV compression budgets during tree search, which feels like a reasonable engineering contribution but I need to verify whether similar approaches have already been explored.

4. I'm also noting the resource constraint: the user specified ≤200 H100-hours, and the proposal mentions ~200 A100 80GB hours for manual mode, which should be roughly equivalent and acceptable.

Let me search for these papers and related work to validate the claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "540c0482-af0d-4fe8-aa59-07b915848204",
  "isSidechain": false,
  "requestId": "req_011CasZpZphLtobAg1mGMxhE",
  "type": "assistant",
  "uuid": "e42a8012-37d3-4f79-bbe3-8eb7ac4ab4ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JgViaK2BESk5chiwpEKy8z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11810,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1539,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1539,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 11810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11810
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

_source line 9 · 2026-05-09T19:43:23.745Z_

I'll conduct adversarial review by independently verifying the cited papers, searching for competing work, and assessing feasibility. Let me run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e42a8012-37d3-4f79-bbe3-8eb7ac4ab4ca",
  "isSidechain": false,
  "requestId": "req_011CasZpZphLtobAg1mGMxhE",
  "type": "assistant",
  "uuid": "51daff86-60cd-4c49-9bb7-14bc5b48d182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JgViaK2BESk5chiwpEKy8z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11810,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1539,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1539,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 11810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11810
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

_source line 10 · 2026-05-09T19:43:28.195Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KgxXsnijVYrh3G8cvJk1HW`</summary>

```json
{
  "description": "Search for ETS paper and KV cache tree search papers",
  "subagent_type": "Explore",
  "prompt": "Search for the following papers and their actual content. Use WebSearch and WebFetch to verify each paper exists and what it actually says.\n\n1. ETS: \"Efficient Tree Search for Inference-Time Scaling\" arXiv:2502.13575 - Does this paper exist? What does it actually claim about KV cache sharing being a bottleneck?\n\n2. \"Inference-Time Hyper-Scaling with KV Cache Compression\" arXiv:2506.05345 - Does this paper exist?\n\n3. \"Beyond Speedup: Utilizing KV Cache for Sampling and Reasoning\" arXiv:2601.20326 ICLR 2026 - Does this paper exist?\n\n4. PM-KVQ arXiv:2505.18610 - Does this paper exist?\n\n5. R-KV arXiv:2505.24133 - Does this paper exist?\n\nFor each paper, check arxiv.org directly. Report: does the paper exist (yes/no), actual title, and what it says about KV compression in tree search contexts if relevant.\n\nAlso search for: \"PRM score KV cache compression tree search\" and \"process reward model KV compression inference\" to see if there's any prior work combining PRM scores with KV cache compression."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51daff86-60cd-4c49-9bb7-14bc5b48d182",
  "isSidechain": false,
  "requestId": "req_011CasZpZphLtobAg1mGMxhE",
  "type": "assistant",
  "uuid": "f331bbe7-b5cd-4be6-b250-b58f628c2d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JgViaK2BESk5chiwpEKy8z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11810,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1539,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1539,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 11810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11810
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

_source line 11 · 2026-05-09T19:43:34.120Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Aqqpfp2n2xyF6BezFHgXFz`</summary>

```json
{
  "description": "Search for competing/concurrent work on KV cache compression for reasoning/tree search",
  "subagent_type": "Explore",
  "prompt": "You are a research reviewer. Search for papers that might compete with or pre-date an idea about \"using PRM (Process Reward Model) scores to dynamically assign per-trajectory KV cache compression budgets during tree search for inference-time scaling.\"\n\nThe core novelty claim is: No prior work conditions per-trajectory KV compression budgets on PRM scores in multi-trajectory tree search.\n\nPlease search for:\n1. \"KV cache compression tree search inference time scaling 2024 2025 2026\" on arxiv\n2. \"per-trajectory KV cache compression reasoning\" \n3. \"PRM KV cache\" or \"process reward model KV cache\"\n4. \"inference time scaling memory efficiency 2025 2026\"\n5. \"test time compute KV cache quantization 2025\"\n6. \"beam search KV cache memory\" recent papers\n7. \"speculative decoding KV cache compression\" - related approaches\n8. site:openreview.net \"KV cache\" \"tree search\" 2025 2026\n\nFor each result found, report: title, arxiv ID if available, venue, and how it relates to the PSG-KVC idea. Focus on finding papers that might undermine the novelty claim or show the gap has already been addressed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f331bbe7-b5cd-4be6-b250-b58f628c2d0e",
  "isSidechain": false,
  "requestId": "req_011CasZpZphLtobAg1mGMxhE",
  "type": "assistant",
  "uuid": "8bcfc336-38a9-44ee-9b4e-6e07ac217424",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JgViaK2BESk5chiwpEKy8z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11810,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1539,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1539,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 11810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11810
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

_source line 12 · 2026-05-09T19:43:38.473Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SjwDXLVr2U66a14GtTFKSN`</summary>

```json
{
  "description": "Search for EMNLP 2026 requirements and efficient NLP track details",
  "subagent_type": "Explore",
  "prompt": "Search for information about EMNLP 2026 submission requirements:\n1. Is EMNLP 2026 ARR deadline May 25, 2026 correct? Search for \"EMNLP 2026 deadline\" and \"ARR May 2026\"\n2. What tracks does EMNLP 2026 have? Is \"Efficient Methods for NLP\" a track?\n3. Search for \"ACL ARR 2026 May cycle deadline\"\n\nAlso search for:\n4. \"DeepSeek-R1-Distill-Qwen-14B\" - Is this model actually available and what are its specs?\n5. \"ETS SqueezeAILab github\" - Does the open-source ETS codebase actually exist on GitHub?\n6. \"SGLang RadixAttention\" - What does it actually do regarding shared prefix KV?\n\nReport what you find with URLs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bcfc336-38a9-44ee-9b4e-6e07ac217424",
  "isSidechain": false,
  "requestId": "req_011CasZpZphLtobAg1mGMxhE",
  "type": "assistant",
  "uuid": "46d8c060-dc4d-4324-912d-1841dbf9fde2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JgViaK2BESk5chiwpEKy8z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11810,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1539,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1539,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 11810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11810
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

_source line 13 · 2026-05-09T19:43:51.453Z_

<details><summary>↩ Tool result · `toolu_01KgxXsnijVYrh3G8cvJk1HW`</summary>

```text
Excellent. I have comprehensive information on all five papers and the related searches. Let me compile the complete report:

## Paper Verification Results

### 1. ETS: "Efficient Tree Search for Inference-Time Scaling" arXiv:2502.13575
**Exists: YES**
- **Actual Title:** "Efficient Tree Search for Inference-Time Scaling"
- **Key Finding on KV Cache:** The paper explicitly identifies KV cache sharing as a bottleneck, stating that "divergent trajectories have less KV sharing, which means they consume more memory and slow down the search process."
- **Main Claims:** Uses linear programming to balance pruning redundant trajectories for better KV cache sharing while retaining semantic diversity. Claims to achieve "1.8× reduction in average KV cache size" and "1.4× increased throughput" compared to prior approaches.

### 2. "Inference-Time Hyper-Scaling with KV Cache Compression" arXiv:2506.05345
**Exists: YES**
- **Actual Title:** "Inference-Time Hyper-Scaling with KV Cache Compression"
- **Main Topic:** Introduces "Dynamic Memory Sparsification" for KV cache compression during inference. Accepted to NeurIPS 2025.
- **Key Claims:** Achieves "8× compression" with minimal training requirements while maintaining accuracy on reasoning benchmarks.

### 3. "Beyond Speedup: Utilizing KV Cache for Sampling and Reasoning" arXiv:2601.20326
**Exists: YES**
- **Actual Title:** "Beyond Speedup -- Utilizing KV Cache for Sampling and Reasoning"
- **Submission Date:** January 28, 2026
- **Main Topic:** Explores how KV caches can serve beyond acceleration—as lightweight representations for downstream applications including embedding-based chain-of-thought and adaptive reasoning systems. Reports "up to 5.7x reductions in token generation with minimal accuracy degradation."

### 4. PM-KVQ arXiv:2505.18610
**Exists: YES**
- **Actual Title:** "PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs"
- **Submission Date:** May 24, 2025
- **Main Topic:** Addresses memory efficiency in reasoning-focused LLMs through progressive quantization of KV caches, gradually lowering bit-width per block with positional interpolation for long-context reasoning tasks.

### 5. R-KV arXiv:2505.24133
**Exists: YES**
- **Actual Title:** "R-KV: Redundancy-aware KV Cache Compression for Reasoning Models"
- **Main Topic:** Proposes compression technique specifically for reasoning models. Claims to achieve "nearly 100% of full KV cache performance using only 10% of the KV cache" with significant memory savings and throughput improvements on mathematical reasoning tasks.

## Prior Work Search Results

### "PRM score KV cache compression tree search"
**Status:** No papers explicitly combining all three elements were found in direct search results. However:
- ETS paper (2502.13575) is the primary work on KV cache compression in tree search context
- PRM scores are mentioned as relevant for tree search rewards (weighted majority voting using PRM scores)
- TreeKV (arXiv:2501.04987) uses tree-based KV cache compression methods

### "process reward model KV compression inference"
**Status:** No papers specifically combining PRMs with KV compression found. However, the search revealed:
- RL-guided KV compression approaches exist (RLKV mentioned in OpenReview)
- KV compression for reasoning models is an active area, but mostly focused on token-dropping and head-reallocation methods
- Process Reward Models are used as scoring mechanisms in reasoning systems but appear to be separate from KV compression research

## Key Insight

All five papers exist and are legitimate. However, **there appears to be no published work directly combining PRM scores with KV cache compression in tree search contexts**. The ETS paper combines tree search with KV compression, and PRM scores are used in reasoning systems, but their integration appears to be an open research opportunity rather than a solved problem in the literature.

Sources:
- [ETS: Efficient Tree Search for Inference-Time Scaling](https://arxiv.org/html/2502.13575)
- [Inference-Time Hyper-Scaling with KV Cache Compression](https://arxiv.org/html/2506.05345v1)
- [Beyond Speedup -- Utilizing KV Cache for Sampling and Reasoning](https://arxiv.org/abs/2601.20326)
- [PM-KVQ: Progressive Mixed-precision KV Cache Quantization](https://arxiv.org/abs/2505.18610)
- [R-KV: Redundancy-aware KV Cache Compression](https://arxiv.org/abs/2505.24133)
- [TreeKV: Smooth Key-Value Cache Compression with Tree Structures](https://arxiv.org/abs/2501.04987)
- [Top 10 KV Cache Compression Techniques](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)
- [Awesome KV Cache Compression Repository](https://github.com/October2001/Awesome-KV-Cache-Compression)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f331bbe7-b5cd-4be6-b250-b58f628c2d0e",
  "isSidechain": false,
  "promptId": "f3fa5027-4a94-46c0-bb8d-7ed240d28059",
  "type": "user",
  "uuid": "841da9da-6317-4bc5-bd12-ffd99fed2399",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the following papers and their actual content. Use WebSearch and WebFetch to verify each paper exists and what it actually says.\n\n1. ETS: \"Efficient Tree Search for Inference-Time Scaling\" arXiv:2502.13575 - Does this paper exist? What does it actually claim about KV cache sharing being a bottleneck?\n\n2. \"Inference-Time Hyper-Scaling with KV Cache Compression\" arXiv:2506.05345 - Does this paper exist?\n\n3. \"Beyond Speedup: Utilizing KV Cache for Sampling and Reasoning\" arXiv:2601.20326 ICLR 2026 - Does this paper exist?\n\n4. PM-KVQ arXiv:2505.18610 - Does this paper exist?\n\n5. R-KV arXiv:2505.24133 - Does this paper exist?\n\nFor each paper, check arxiv.org directly. Report: does the paper exist (yes/no), actual title, and what it says about KV compression in tree search contexts if relevant.\n\nAlso search for: \"PRM score KV cache compression tree search\" and \"process reward model KV compression inference\" to see if there's any prior work combining PRM scores with KV cache compression.",
    "agentId": "abfb2ab5636fbc82e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent. I have comprehensive information on all five papers and the related searches. Let me compile the complete report:\n\n## Paper Verification Results\n\n### 1. ETS: \"Efficient Tree Search for Inference-Time Scaling\" arXiv:2502.13575\n**Exists: YES**\n- **Actual Title:** \"Efficient Tree Search for Inference-Time Scaling\"\n- **Key Finding on KV Cache:** The paper explicitly identifies KV cache sharing as a bottleneck, stating that \"divergent trajectories have less KV sharing, which means they consume more memory and slow down the search process.\"\n- **Main Claims:** Uses linear programming to balance pruning redundant trajectories for better KV cache sharing while retaining semantic diversity. Claims to achieve \"1.8× reduction in average KV cache size\" and \"1.4× increased throughput\" compared to prior approaches.\n\n### 2. \"Inference-Time Hyper-Scaling with KV Cache Compression\" arXiv:2506.05345\n**Exists: YES**\n- **Actual Title:** \"Inference-Time Hyper-Scaling with KV Cache Compression\"\n- **Main Topic:** Introduces \"Dynamic Memory Sparsification\" for KV cache compression during inference. Accepted to NeurIPS 2025.\n- **Key Claims:** Achieves \"8× compression\" with minimal training requirements while maintaining accuracy on reasoning benchmarks.\n\n### 3. \"Beyond Speedup: Utilizing KV Cache for Sampling and Reasoning\" arXiv:2601.20326\n**Exists: YES**\n- **Actual Title:** \"Beyond Speedup -- Utilizing KV Cache for Sampling and Reasoning\"\n- **Submission Date:** January 28, 2026\n- **Main Topic:** Explores how KV caches can serve beyond acceleration—as lightweight representations for downstream applications including embedding-based chain-of-thought and adaptive reasoning systems. Reports \"up to 5.7x reductions in token generation with minimal accuracy degradation.\"\n\n### 4. PM-KVQ arXiv:2505.18610\n**Exists: YES**\n- **Actual Title:** \"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs\"\n- **Submission Date:** May 24, 2025\n- **Main Topic:** Addresses memory efficiency in reasoning-focused LLMs through progressive quantization of KV caches, gradually lowering bit-width per block with positional interpolation for long-context reasoning tasks.\n\n### 5. R-KV arXiv:2505.24133\n**Exists: YES**\n- **Actual Title:** \"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models\"\n- **Main Topic:** Proposes compression technique specifically for reasoning models. Claims to achieve \"nearly 100% of full KV cache performance using only 10% of the KV cache\" with significant memory savings and throughput improvements on mathematical reasoning tasks.\n\n## Prior Work Search Results\n\n### \"PRM score KV cache compression tree search\"\n**Status:** No papers explicitly combining all three elements were found in direct search results. However:\n- ETS paper (2502.13575) is the primary work on KV cache compression in tree search context\n- PRM scores are mentioned as relevant for tree search rewards (weighted majority voting using PRM scores)\n- TreeKV (arXiv:2501.04987) uses tree-based KV cache compression methods\n\n### \"process reward model KV compression inference\"\n**Status:** No papers specifically combining PRMs with KV compression found. However, the search revealed:\n- RL-guided KV compression approaches exist (RLKV mentioned in OpenReview)\n- KV compression for reasoning models is an active area, but mostly focused on token-dropping and head-reallocation methods\n- Process Reward Models are used as scoring mechanisms in reasoning systems but appear to be separate from KV compression research\n\n## Key Insight\n\nAll five papers exist and are legitimate. However, **there appears to be no published work directly combining PRM scores with KV cache compression in tree search contexts**. The ETS paper combines tree search with KV compression, and PRM scores are used in reasoning systems, but their integration appears to be an open research opportunity rather than a solved problem in the literature.\n\nSources:\n- [ETS: Efficient Tree Search for Inference-Time Scaling](https://arxiv.org/html/2502.13575)\n- [Inference-Time Hyper-Scaling with KV Cache Compression](https://arxiv.org/html/2506.05345v1)\n- [Beyond Speedup -- Utilizing KV Cache for Sampling and Reasoning](https://arxiv.org/abs/2601.20326)\n- [PM-KVQ: Progressive Mixed-precision KV Cache Quantization](https://arxiv.org/abs/2505.18610)\n- [R-KV: Redundancy-aware KV Cache Compression](https://arxiv.org/abs/2505.24133)\n- [TreeKV: Smooth Key-Value Cache Compression with Tree Structures](https://arxiv.org/abs/2501.04987)\n- [Top 10 KV Cache Compression Techniques](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)\n- [Awesome KV Cache Compression Repository](https://github.com/October2001/Awesome-KV-Cache-Compression)"
      }
    ],
    "totalDurationMs": 23254,
    "totalTokens": 22409,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 924,
      "cache_creation_input_tokens": 3306,
      "cache_read_input_tokens": 16873,
      "output_tokens": 1306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3306
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 924,
          "output_tokens": 1306,
          "cache_read_input_tokens": 16873,
          "cache_creation_input_tokens": 3306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3306,
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
  "sourceToolAssistantUUID": "f331bbe7-b5cd-4be6-b250-b58f628c2d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-09T19:43:58.740Z_

<details><summary>↩ Tool result · `toolu_01SjwDXLVr2U66a14GtTFKSN`</summary>

```text
## Summary of Findings

Based on my searches, here's what I found regarding your questions:

### EMNLP 2026 Submission Requirements

**1. ARR Deadline - May 25, 2026**
Yes, this is **correct**. The EMNLP 2026 official announcement confirms the ARR Submission Deadline is **May 25, 2026** (with author registration due by May 27, 2026 EoD AoE). This was posted by the official EMNLP meeting account.

**2. EMNLP 2026 Tracks**
Yes, "Efficient Methods for NLP" is **confirmed as a track/research area**. EMNLP 2026 includes the following main tracks:
- Main Research Track
- Theme Track: New Missions for NLP Research
- Industry Track
- System Demonstrations Track

Research areas include: Efficient Methods for NLP, Ethics/Bias/Fairness, Information Extraction, Language Modeling, LLM Agents, Machine Translation, Multilingualism, and many others.

**3. ACL ARR 2026 May Cycle Deadline**
The May 2026 ARR cycle deadline is **May 25, 2026** - confirmed to be aligned with both EMNLP and AACL conferences, requiring explicit declaration of which conference at submission time.

### Technical Model & Library Searches

**4. DeepSeek-R1-Distill-Qwen-14B - YES, Available**
This model **actually exists and is available**. It's a 14B parameter model that:
- Has 130k token context window
- Achieves 93.9% accuracy on MATH-500 and 69.7% pass rate on AIME 2024
- Is open weights under Apache 2.0 license (commercial use allowed)
- Available on Hugging Face, LM Studio, Ollama, and NVIDIA Build

**5. ETS SqueezeAILab GitHub - YES, Exists**
The open-source ETS (Efficient Tree Search for Inference-Time Scaling) codebase **does exist** on GitHub at https://github.com/SqueezeAILab/ETS. It's designed for inference-time scaling with KV cache sharing to reduce memory consumption.

**6. SGLang RadixAttention - Confirmed**
RadixAttention in SGLang **does handle shared prefix KV cache reuse**. It:
- Maintains an LRU cache of KV cache entries in a radix tree structure
- Allows different prompts with the same prefix to share intermediate KV cache
- Reduces memory usage and computation of prefill
- Achieves up to 5-6.4x higher throughput compared to existing systems

Sources:
- [EMNLP 2026 Official Website](https://2026.emnlp.org/)
- [EMNLP 2026 ARR Deadline Announcement](https://x.com/emnlpmeeting/status/2029508292637061462)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)
- [DeepSeek-R1-Distill-Qwen-14B on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B)
- [ETS GitHub Repository](https://github.com/SqueezeAILab/ETS)
- [SGLang GitHub](https://github.com/sgl-project/sglang)
- [LMSYS Blog on RadixAttention](https://www.lmsys.org/blog/2024-01-17-sglang/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46d8c060-dc4d-4324-912d-1841dbf9fde2",
  "isSidechain": false,
  "promptId": "f3fa5027-4a94-46c0-bb8d-7ed240d28059",
  "type": "user",
  "uuid": "e8a4662b-ac89-4cba-9f3f-8c3dc119459e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for information about EMNLP 2026 submission requirements:\n1. Is EMNLP 2026 ARR deadline May 25, 2026 correct? Search for \"EMNLP 2026 deadline\" and \"ARR May 2026\"\n2. What tracks does EMNLP 2026 have? Is \"Efficient Methods for NLP\" a track?\n3. Search for \"ACL ARR 2026 May cycle deadline\"\n\nAlso search for:\n4. \"DeepSeek-R1-Distill-Qwen-14B\" - Is this model actually available and what are its specs?\n5. \"ETS SqueezeAILab github\" - Does the open-source ETS codebase actually exist on GitHub?\n6. \"SGLang RadixAttention\" - What does it actually do regarding shared prefix KV?\n\nReport what you find with URLs.",
    "agentId": "a135c34762a7751fa",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Findings\n\nBased on my searches, here's what I found regarding your questions:\n\n### EMNLP 2026 Submission Requirements\n\n**1. ARR Deadline - May 25, 2026**\nYes, this is **correct**. The EMNLP 2026 official announcement confirms the ARR Submission Deadline is **May 25, 2026** (with author registration due by May 27, 2026 EoD AoE). This was posted by the official EMNLP meeting account.\n\n**2. EMNLP 2026 Tracks**\nYes, \"Efficient Methods for NLP\" is **confirmed as a track/research area**. EMNLP 2026 includes the following main tracks:\n- Main Research Track\n- Theme Track: New Missions for NLP Research\n- Industry Track\n- System Demonstrations Track\n\nResearch areas include: Efficient Methods for NLP, Ethics/Bias/Fairness, Information Extraction, Language Modeling, LLM Agents, Machine Translation, Multilingualism, and many others.\n\n**3. ACL ARR 2026 May Cycle Deadline**\nThe May 2026 ARR cycle deadline is **May 25, 2026** - confirmed to be aligned with both EMNLP and AACL conferences, requiring explicit declaration of which conference at submission time.\n\n### Technical Model & Library Searches\n\n**4. DeepSeek-R1-Distill-Qwen-14B - YES, Available**\nThis model **actually exists and is available**. It's a 14B parameter model that:\n- Has 130k token context window\n- Achieves 93.9% accuracy on MATH-500 and 69.7% pass rate on AIME 2024\n- Is open weights under Apache 2.0 license (commercial use allowed)\n- Available on Hugging Face, LM Studio, Ollama, and NVIDIA Build\n\n**5. ETS SqueezeAILab GitHub - YES, Exists**\nThe open-source ETS (Efficient Tree Search for Inference-Time Scaling) codebase **does exist** on GitHub at https://github.com/SqueezeAILab/ETS. It's designed for inference-time scaling with KV cache sharing to reduce memory consumption.\n\n**6. SGLang RadixAttention - Confirmed**\nRadixAttention in SGLang **does handle shared prefix KV cache reuse**. It:\n- Maintains an LRU cache of KV cache entries in a radix tree structure\n- Allows different prompts with the same prefix to share intermediate KV cache\n- Reduces memory usage and computation of prefill\n- Achieves up to 5-6.4x higher throughput compared to existing systems\n\nSources:\n- [EMNLP 2026 Official Website](https://2026.emnlp.org/)\n- [EMNLP 2026 ARR Deadline Announcement](https://x.com/emnlpmeeting/status/2029508292637061462)\n- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)\n- [DeepSeek-R1-Distill-Qwen-14B on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B)\n- [ETS GitHub Repository](https://github.com/SqueezeAILab/ETS)\n- [SGLang GitHub](https://github.com/sgl-project/sglang)\n- [LMSYS Blog on RadixAttention](https://www.lmsys.org/blog/2024-01-17-sglang/)"
      }
    ],
    "totalDurationMs": 20264,
    "totalTokens": 24634,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6936,
      "cache_read_input_tokens": 16796,
      "output_tokens": 895,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 895,
          "cache_read_input_tokens": 16796,
          "cache_creation_input_tokens": 6936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6936,
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
  "sourceToolAssistantUUID": "46d8c060-dc4d-4324-912d-1841dbf9fde2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e8a4662b-ac89-4cba-9f3f-8c3dc119459e",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify PRM-gated KV compression idea for EMNLP 2026",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf"
}
```

---

### Tool result

_source line 17 · 2026-05-09T19:45:49.659Z_

<details><summary>↩ Tool result · `toolu_01Aqqpfp2n2xyF6BezFHgXFz`</summary>

```text
Perfect. Now I have comprehensive information. Let me compile the final report for the user.

## Research Literature Review: PRM-Guided Per-Trajectory KV Cache Compression

Based on my comprehensive search of arxiv, OpenReview, and conference proceedings for 2024-2026, here is a detailed assessment of the novelty landscape for your proposed idea: **"Using PRM scores to dynamically assign per-trajectory KV cache compression budgets during tree search."**

### CRITICAL FINDINGS

Your novelty claim appears to hold, but with important caveats. No single paper explicitly combines all three elements—(1) PRM scoring, (2) KV cache budget allocation, and (3) per-trajectory/per-path decisions in tree search. However, there is **substantial adjacent work** that addresses subsets of this problem:

---

## Papers Found by Category

### A. CLOSEST COMPETITORS: PRM + Resource Allocation + Tree Search

**1. ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search**
- **Title:** ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search
- **Venue:** OpenReview (appears to be NeurIPS/ICLR submission)
- **Core Contribution:** Combines process rewards with MCTS* tree search to infer step-level rewards without per-step annotations. Uses rewards as value targets and to guide selection of high-quality traces for policy training.
- **Relevance to PSG-KVC:** This is your closest competitor. It uses PRM scores to guide tree search exploration and resource allocation (trajectory selection). **Key difference:** Focuses on training trajectory selection, not KV cache compression budget allocation per trajectory.
- **Threat Level:** MEDIUM — Shows PRMs can be effectively used for per-trajectory decisions in tree search, but does not address memory/cache compression.

**2. Reward-Guided Speculative Decoding for Efficient LLM Reasoning**
- **ArXiv ID:** 2501.19324
- **Authors:** Baohao Liao, Yuhui Xu, Hanze Dong, Junnan Li, Christof Monz, Silvio Savarese, Doyen Sahoo, Caiming Xiong
- **Core Contribution:** Uses process reward models to dynamically decide whether to invoke expensive target models in speculative decoding. Achieves 4.4x efficiency gains with PRM-guided decisions during inference.
- **Relevance to PSG-KVC:** Demonstrates PRM-guided inference-time resource allocation (which model to run). **Key difference:** Not about KV cache specifically, but shows PRM can steer computational choices during generation.
- **Threat Level:** MEDIUM — Validates that PRM scores can guide inference-time efficiency trade-offs, but not specifically for KV cache compression budgets.

---

### B. KV CACHE COMPRESSION + ADAPTIVE BUDGET ALLOCATION (No PRM)

**3. Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference**
- **ArXiv ID:** 2407.11550
- **Authors:** Yuan Feng, Junlin Lv, Yukun Cao, Xike Xie, S. Kevin Zhou
- **Core Contribution:** First head-wise adaptive budget allocation for KV cache. Dynamically reallocates budgets from heads with sparse attention to those with dispersed attention.
- **Relevance to PSG-KVC:** Demonstrates adaptive budget allocation principle for KV cache, but allocation is **per-head**, not per-trajectory in tree search.
- **Threat Level:** LOW — Shows adaptive KV budget allocation exists, but not trajectory-aware or reward-guided.

**4. Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle**
- **ArXiv ID:** 2601.16986
- **Authors:** Zihan Wang, Cheng Tang, Lei Gong, Cheng Li, Chao Wang, et al.
- **Core Contribution:** Layer-wise and head-wise KV cache budget allocation based on importance scores (CRF-based). Optimizes for CoT reasoning tasks.
- **Relevance to PSG-KVC:** Adaptive budget allocation for reasoning, but allocation mechanism is based on token importance scores, not PRM signals or trajectory-specific values.
- **Threat Level:** LOW — Adaptive reasoning-aware KV budgets, but not trajectory-aware or PRM-guided.

**5. R-KV: Redundancy-aware KV Cache Compression for Reasoning Models**
- **ArXiv ID:** 2505.24133
- **Authors:** Zefan Cai, Wen Xiao, Hanshi Sun, et al.
- **Core Contribution:** Ranks tokens on-the-fly for importance and redundancy in reasoning models. Achieves 10-34% cache with full accuracy on reasoning benchmarks.
- **Relevance to PSG-KVC:** Demonstrates token importance-based compression for reasoning, but not per-trajectory or PRM-guided.
- **Threat Level:** LOW — Effective reasoning compression, but static compression strategy, not adaptive per-trajectory.

---

### C. TREE SEARCH + RESOURCE ALLOCATION (No KV Cache Focus)

**6. Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents (BAVT)**
- **ArXiv ID:** 2603.12634
- **Authors:** Yushu Li, Wenlong Deng, Jiajin Li, Xiaoxiao Li
- **Core Contribution:** Principled node selection mechanism in tree search that uses "remaining resource ratio as scaling exponent over node values." Transitions from exploration to exploitation as budgets deplete per trajectory.
- **Relevance to PSG-KVC:** **Closest to your concept in terms of per-trajectory resource allocation philosophy**, but resource is computation/tool calls, not specifically KV cache compression budget.
- **Threat Level:** MEDIUM-HIGH — Demonstrates that per-trajectory resource budgeting based on value signals is effective. Could be extended to KV cache.

**7. Adaptive Uncertainty-Aware Tree Search for Robust Reasoning**
- **ArXiv ID:** 2602.06493
- **Authors:** Zeen Song, Zihao Ma, Wenwen Qiang, Changwen Zheng, Gang Hua
- **Core Contribution:** Identifies that PRMs fail on out-of-distribution paths. Uses uncertainty estimation (MC Dropout) + RL-based controller to adaptively allocate compute budgets in tree search.
- **Relevance to PSG-KVC:** Uses PRM signals with adaptive allocation, BUT focuses on detecting unreliable PRMs and using uncertainty, not conditioning cache budget on PRM scores.
- **Threat Level:** MEDIUM — Shows PRM-based adaptive allocation in tree search, but for a different resource (compute/exploration budget).

**8. Dynamic Parallel Tree Search for Efficient LLM Reasoning**
- **ArXiv ID:** 2502.16235
- **Authors:** Yifu Ding, Wentao Jiang, Shunyu Liu, et al.
- **Core Contribution:** Fine-grained cache management to enable flexible parallelism across arbitrary reasoning paths. 2-4x efficiency improvements through dynamic path focus.
- **Relevance to PSG-KVC:** **Explicitly mentions "fine-grained cache management" per path in tree search**. This is the closest practical competitor, but cache management appears to be about **sharing/reuse** not compression budget allocation.
- **Threat Level:** MEDIUM-HIGH — Directly addresses per-path cache optimization in tree search, but likely focuses on memory reuse rather than compression budget.

---

### D. KV CACHE COMPRESSION + INFERENCE-TIME SCALING

**9. Inference-Time Hyper-Scaling with KV Cache Compression**
- **ArXiv ID:** 2506.05345
- **Authors:** Adrian Łańcucki, Konrad Staniszewski, Piotr Nawrot, Edoardo Ponti
- **Venue:** NeurIPS 2025
- **Core Contribution:** Dynamic Memory Sparsification (DMS) — compresses KV cache 8x with minimal training. Enables longer reasoning chains within fixed compute budgets. Used in o1 and R1 models.
- **Relevance to PSG-KVC:** Directly addresses KV cache compression for inference-time scaling, but uses **uniform/learned compression strategy**, not per-trajectory or PRM-guided.
- **Threat Level:** MEDIUM — Major work on KV compression for scaling, but not adaptive per-trajectory.

**10. Hold Onto That Thought: Assessing KV Cache Compression On Reasoning**
- **ArXiv ID:** 2512.12008
- **Authors:** Minghui Liu, Aadi Palnitkar, Tahseen Rabbani, et al.
- **Venue:** arXiv
- **Core Contribution:** Benchmarks KV cache compression strategies (H2O, SnapKV, etc.) specifically on reasoning tasks. Finds no single strategy fits all; aggressive eviction at low budgets can lengthen reasoning traces.
- **Relevance to PSG-KVC:** Validates that cache compression behavior varies with task/trajectory, but does not propose per-trajectory adaptive allocation based on PRM.
- **Threat Level:** LOW-MEDIUM — Empirical finding that compression needs vary, but no PRM-based adaptive solution.

---

### E. SPECULATIVE DECODING + KV CACHE (Related Inference Efficiency)

**11. SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection**
- **ArXiv ID:** 2605.02888
- **Author:** Shikhar Shukla
- **Core Contribution:** Dynamically selects speculation length (γ) based on KV cache compression level. Shows that compression and speculation are coupled—different compression levels need different speculation lengths.
- **Relevance to PSG-KVC:** Demonstrates that cache state influences inference-time decisions, but adaptation is based on **fixed compression state**, not trajectory-dependent PRM scores.
- **Threat Level:** LOW — Shows cache compression influences resource decisions, but not trajectory-adaptive.

**12. Efficient Beam Search for Large Language Models Using Trie-Based Decoding**
- **ArXiv ID:** 2502.00085
- **Venue:** EMNLP 2025
- **Core Contribution:** Prefix-tree based beam search sharing single KV cache across beams with common prefixes. Achieves 4-8x memory savings.
- **Relevance to PSG-KVC:** Per-path KV cache optimization (prefix sharing), but memory optimization is structural (sharing), not compression budget adaptation.
- **Threat Level:** LOW — Efficient KV management for beam search, but not PRM-guided compression budgets.

---

### F. PAPERS ON TREE SEARCH + PRM (No Memory/Cache Element)

**13. Principle Process Reward For Search Agents**
- **Venue:** OpenReview
- **Relevance:** PRM for guiding search exploration, not memory management.
- **Threat Level:** LOW

**14. Process Reward Models That Think**
- **Venue:** OpenReview
- **Relevance:** General PRM framework, not specific to resource allocation.
- **Threat Level:** LOW

---

### G. ADDITIONAL CONTEXT: Hierarchical/Input-Adaptive Allocation

**15. Hierarchical Budget Policy Optimization for Adaptive Reasoning**
- **ArXiv ID:** 2507.15844
- **Core Contribution:** RL framework that partitions exploration space into budget-constrained hierarchies with differentiated rewards.
- **Relevance to PSG-KVC:** Budget allocation based on value signals, but not specifically KV cache compression or PRM-guided.
- **Threat Level:** LOW

**16. Input-Adaptive Allocation of LM Computation**
- **Venue:** ICLR 2025
- **Core Contribution:** Predicts required computation per query and allocates resources adaptively.
- **Relevance to PSG-KVC:** Input-adaptive resource allocation, but not specifically KV cache or per-trajectory in tree search.
- **Threat Level:** LOW

---

## Summary Assessment

### The Novelty Gap

**Your core claim:** "No prior work conditions per-trajectory KV compression budgets on PRM scores in multi-trajectory tree search."

**Verdict: CLAIM APPEARS VALID** with the following observations:

1. **PRM + Tree Search** exists (ReST-MCTS*, UATS, reward-guided speculative decoding) but is **not** applied to KV cache compression budgets.

2. **Adaptive KV Cache Budgets** exist (Ada-KV, Crystal-KV) but are **not** per-trajectory or PRM-guided. They are per-head or per-layer.

3. **Per-Trajectory Resource Allocation** exists (BAVT, DPTS) but applies to computation/tool budget, **not** KV cache compression.

4. **KV Cache Compression for Inference Scaling** exists (DMS, R-KV) but uses **uniform/learned** strategies, not per-trajectory PRM-based allocation.

The **intersection of all four elements** (KV cache compression + adaptive budgets + per-trajectory + PRM-guided) does not appear in the literature.

### Key Risks/Gaps to Address

1. **Dynamic Parallel Tree Search (DPTS, arxiv 2502.16235)** explicitly mentions "fine-grained cache management" per reasoning path. Verify this doesn't already condition cache allocation on trajectory state/quality signals.

2. **BAVT's per-trajectory resource allocation principle** (arxiv 2603.12634) is very similar philosophically to what you're proposing, just applied to a different resource. Document how cache compression budget differs in application.

3. **Confirm no papers combine:**
   - PRM scoring signals
   - KV cache compression (not just management/sharing)
   - Per-trajectory conditional budgets
   - Tree search/multi-trajectory setting

---

## Sources

- [Inference-Time Hyper-Scaling with KV Cache Compression](https://arxiv.org/abs/2506.05345)
- [Hold Onto That Thought: Assessing KV Cache Compression On Reasoning](https://arxiv.org/abs/2512.12008)
- [R-KV: Redundancy-aware KV Cache Compression for Reasoning Models](https://arxiv.org/abs/2505.24133)
- [Efficient Beam Search for Large Language Models Using Trie-Based Decoding](https://arxiv.org/abs/2502.00085)
- [SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection](https://arxiv.org/abs/2605.02888)
- [How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers](https://arxiv.org/abs/2604.17935)
- [LongFlow: Efficient KV Cache Compression for Reasoning Models](https://arxiv.org/abs/2603.11504)
- [Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference](https://arxiv.org/abs/2407.11550)
- [Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle](https://arxiv.org/abs/2601.16986)
- [Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents](https://arxiv.org/abs/2603.12634)
- [Adaptive Uncertainty-Aware Tree Search for Robust Reasoning](https://arxiv.org/abs/2602.06493)
- [Dynamic Parallel Tree Search for Efficient LLM Reasoning](https://arxiv.org/abs/2502.16235)
- [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://openreview.net/forum?id=8rcFOqEud5)
- [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://arxiv.org/abs/2501.19324)
- [Hierarchical Budget Policy Optimization for Adaptive Reasoning](https://arxiv.org/abs/2507.15844)
- [Input-Adaptive Allocation of LM Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bcfc336-38a9-44ee-9b4e-6e07ac217424",
  "isSidechain": false,
  "promptId": "f3fa5027-4a94-46c0-bb8d-7ed240d28059",
  "type": "user",
  "uuid": "b24a994f-03dc-44b5-a245-f51239d6a3aa",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are a research reviewer. Search for papers that might compete with or pre-date an idea about \"using PRM (Process Reward Model) scores to dynamically assign per-trajectory KV cache compression budgets during tree search for inference-time scaling.\"\n\nThe core novelty claim is: No prior work conditions per-trajectory KV compression budgets on PRM scores in multi-trajectory tree search.\n\nPlease search for:\n1. \"KV cache compression tree search inference time scaling 2024 2025 2026\" on arxiv\n2. \"per-trajectory KV cache compression reasoning\" \n3. \"PRM KV cache\" or \"process reward model KV cache\"\n4. \"inference time scaling memory efficiency 2025 2026\"\n5. \"test time compute KV cache quantization 2025\"\n6. \"beam search KV cache memory\" recent papers\n7. \"speculative decoding KV cache compression\" - related approaches\n8. site:openreview.net \"KV cache\" \"tree search\" 2025 2026\n\nFor each result found, report: title, arxiv ID if available, venue, and how it relates to the PSG-KVC idea. Focus on finding papers that might undermine the novelty claim or show the gap has already been addressed.",
    "agentId": "a1e6e71bf8f34a96e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now I have comprehensive information. Let me compile the final report for the user.\n\n## Research Literature Review: PRM-Guided Per-Trajectory KV Cache Compression\n\nBased on my comprehensive search of arxiv, OpenReview, and conference proceedings for 2024-2026, here is a detailed assessment of the novelty landscape for your proposed idea: **\"Using PRM scores to dynamically assign per-trajectory KV cache compression budgets during tree search.\"**\n\n### CRITICAL FINDINGS\n\nYour novelty claim appears to hold, but with important caveats. No single paper explicitly combines all three elements—(1) PRM scoring, (2) KV cache budget allocation, and (3) per-trajectory/per-path decisions in tree search. However, there is **substantial adjacent work** that addresses subsets of this problem:\n\n---\n\n## Papers Found by Category\n\n### A. CLOSEST COMPETITORS: PRM + Resource Allocation + Tree Search\n\n**1. ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search**\n- **Title:** ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search\n- **Venue:** OpenReview (appears to be NeurIPS/ICLR submission)\n- **Core Contribution:** Combines process rewards with MCTS* tree search to infer step-level rewards without per-step annotations. Uses rewards as value targets and to guide selection of high-quality traces for policy training.\n- **Relevance to PSG-KVC:** This is your closest competitor. It uses PRM scores to guide tree search exploration and resource allocation (trajectory selection). **Key difference:** Focuses on training trajectory selection, not KV cache compression budget allocation per trajectory.\n- **Threat Level:** MEDIUM — Shows PRMs can be effectively used for per-trajectory decisions in tree search, but does not address memory/cache compression.\n\n**2. Reward-Guided Speculative Decoding for Efficient LLM Reasoning**\n- **ArXiv ID:** 2501.19324\n- **Authors:** Baohao Liao, Yuhui Xu, Hanze Dong, Junnan Li, Christof Monz, Silvio Savarese, Doyen Sahoo, Caiming Xiong\n- **Core Contribution:** Uses process reward models to dynamically decide whether to invoke expensive target models in speculative decoding. Achieves 4.4x efficiency gains with PRM-guided decisions during inference.\n- **Relevance to PSG-KVC:** Demonstrates PRM-guided inference-time resource allocation (which model to run). **Key difference:** Not about KV cache specifically, but shows PRM can steer computational choices during generation.\n- **Threat Level:** MEDIUM — Validates that PRM scores can guide inference-time efficiency trade-offs, but not specifically for KV cache compression budgets.\n\n---\n\n### B. KV CACHE COMPRESSION + ADAPTIVE BUDGET ALLOCATION (No PRM)\n\n**3. Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference**\n- **ArXiv ID:** 2407.11550\n- **Authors:** Yuan Feng, Junlin Lv, Yukun Cao, Xike Xie, S. Kevin Zhou\n- **Core Contribution:** First head-wise adaptive budget allocation for KV cache. Dynamically reallocates budgets from heads with sparse attention to those with dispersed attention.\n- **Relevance to PSG-KVC:** Demonstrates adaptive budget allocation principle for KV cache, but allocation is **per-head**, not per-trajectory in tree search.\n- **Threat Level:** LOW — Shows adaptive KV budget allocation exists, but not trajectory-aware or reward-guided.\n\n**4. Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle**\n- **ArXiv ID:** 2601.16986\n- **Authors:** Zihan Wang, Cheng Tang, Lei Gong, Cheng Li, Chao Wang, et al.\n- **Core Contribution:** Layer-wise and head-wise KV cache budget allocation based on importance scores (CRF-based). Optimizes for CoT reasoning tasks.\n- **Relevance to PSG-KVC:** Adaptive budget allocation for reasoning, but allocation mechanism is based on token importance scores, not PRM signals or trajectory-specific values.\n- **Threat Level:** LOW — Adaptive reasoning-aware KV budgets, but not trajectory-aware or PRM-guided.\n\n**5. R-KV: Redundancy-aware KV Cache Compression for Reasoning Models**\n- **ArXiv ID:** 2505.24133\n- **Authors:** Zefan Cai, Wen Xiao, Hanshi Sun, et al.\n- **Core Contribution:** Ranks tokens on-the-fly for importance and redundancy in reasoning models. Achieves 10-34% cache with full accuracy on reasoning benchmarks.\n- **Relevance to PSG-KVC:** Demonstrates token importance-based compression for reasoning, but not per-trajectory or PRM-guided.\n- **Threat Level:** LOW — Effective reasoning compression, but static compression strategy, not adaptive per-trajectory.\n\n---\n\n### C. TREE SEARCH + RESOURCE ALLOCATION (No KV Cache Focus)\n\n**6. Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents (BAVT)**\n- **ArXiv ID:** 2603.12634\n- **Authors:** Yushu Li, Wenlong Deng, Jiajin Li, Xiaoxiao Li\n- **Core Contribution:** Principled node selection mechanism in tree search that uses \"remaining resource ratio as scaling exponent over node values.\" Transitions from exploration to exploitation as budgets deplete per trajectory.\n- **Relevance to PSG-KVC:** **Closest to your concept in terms of per-trajectory resource allocation philosophy**, but resource is computation/tool calls, not specifically KV cache compression budget.\n- **Threat Level:** MEDIUM-HIGH — Demonstrates that per-trajectory resource budgeting based on value signals is effective. Could be extended to KV cache.\n\n**7. Adaptive Uncertainty-Aware Tree Search for Robust Reasoning**\n- **ArXiv ID:** 2602.06493\n- **Authors:** Zeen Song, Zihao Ma, Wenwen Qiang, Changwen Zheng, Gang Hua\n- **Core Contribution:** Identifies that PRMs fail on out-of-distribution paths. Uses uncertainty estimation (MC Dropout) + RL-based controller to adaptively allocate compute budgets in tree search.\n- **Relevance to PSG-KVC:** Uses PRM signals with adaptive allocation, BUT focuses on detecting unreliable PRMs and using uncertainty, not conditioning cache budget on PRM scores.\n- **Threat Level:** MEDIUM — Shows PRM-based adaptive allocation in tree search, but for a different resource (compute/exploration budget).\n\n**8. Dynamic Parallel Tree Search for Efficient LLM Reasoning**\n- **ArXiv ID:** 2502.16235\n- **Authors:** Yifu Ding, Wentao Jiang, Shunyu Liu, et al.\n- **Core Contribution:** Fine-grained cache management to enable flexible parallelism across arbitrary reasoning paths. 2-4x efficiency improvements through dynamic path focus.\n- **Relevance to PSG-KVC:** **Explicitly mentions \"fine-grained cache management\" per path in tree search**. This is the closest practical competitor, but cache management appears to be about **sharing/reuse** not compression budget allocation.\n- **Threat Level:** MEDIUM-HIGH — Directly addresses per-path cache optimization in tree search, but likely focuses on memory reuse rather than compression budget.\n\n---\n\n### D. KV CACHE COMPRESSION + INFERENCE-TIME SCALING\n\n**9. Inference-Time Hyper-Scaling with KV Cache Compression**\n- **ArXiv ID:** 2506.05345\n- **Authors:** Adrian Łańcucki, Konrad Staniszewski, Piotr Nawrot, Edoardo Ponti\n- **Venue:** NeurIPS 2025\n- **Core Contribution:** Dynamic Memory Sparsification (DMS) — compresses KV cache 8x with minimal training. Enables longer reasoning chains within fixed compute budgets. Used in o1 and R1 models.\n- **Relevance to PSG-KVC:** Directly addresses KV cache compression for inference-time scaling, but uses **uniform/learned compression strategy**, not per-trajectory or PRM-guided.\n- **Threat Level:** MEDIUM — Major work on KV compression for scaling, but not adaptive per-trajectory.\n\n**10. Hold Onto That Thought: Assessing KV Cache Compression On Reasoning**\n- **ArXiv ID:** 2512.12008\n- **Authors:** Minghui Liu, Aadi Palnitkar, Tahseen Rabbani, et al.\n- **Venue:** arXiv\n- **Core Contribution:** Benchmarks KV cache compression strategies (H2O, SnapKV, etc.) specifically on reasoning tasks. Finds no single strategy fits all; aggressive eviction at low budgets can lengthen reasoning traces.\n- **Relevance to PSG-KVC:** Validates that cache compression behavior varies with task/trajectory, but does not propose per-trajectory adaptive allocation based on PRM.\n- **Threat Level:** LOW-MEDIUM — Empirical finding that compression needs vary, but no PRM-based adaptive solution.\n\n---\n\n### E. SPECULATIVE DECODING + KV CACHE (Related Inference Efficiency)\n\n**11. SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection**\n- **ArXiv ID:** 2605.02888\n- **Author:** Shikhar Shukla\n- **Core Contribution:** Dynamically selects speculation length (γ) based on KV cache compression level. Shows that compression and speculation are coupled—different compression levels need different speculation lengths.\n- **Relevance to PSG-KVC:** Demonstrates that cache state influences inference-time decisions, but adaptation is based on **fixed compression state**, not trajectory-dependent PRM scores.\n- **Threat Level:** LOW — Shows cache compression influences resource decisions, but not trajectory-adaptive.\n\n**12. Efficient Beam Search for Large Language Models Using Trie-Based Decoding**\n- **ArXiv ID:** 2502.00085\n- **Venue:** EMNLP 2025\n- **Core Contribution:** Prefix-tree based beam search sharing single KV cache across beams with common prefixes. Achieves 4-8x memory savings.\n- **Relevance to PSG-KVC:** Per-path KV cache optimization (prefix sharing), but memory optimization is structural (sharing), not compression budget adaptation.\n- **Threat Level:** LOW — Efficient KV management for beam search, but not PRM-guided compression budgets.\n\n---\n\n### F. PAPERS ON TREE SEARCH + PRM (No Memory/Cache Element)\n\n**13. Principle Process Reward For Search Agents**\n- **Venue:** OpenReview\n- **Relevance:** PRM for guiding search exploration, not memory management.\n- **Threat Level:** LOW\n\n**14. Process Reward Models That Think**\n- **Venue:** OpenReview\n- **Relevance:** General PRM framework, not specific to resource allocation.\n- **Threat Level:** LOW\n\n---\n\n### G. ADDITIONAL CONTEXT: Hierarchical/Input-Adaptive Allocation\n\n**15. Hierarchical Budget Policy Optimization for Adaptive Reasoning**\n- **ArXiv ID:** 2507.15844\n- **Core Contribution:** RL framework that partitions exploration space into budget-constrained hierarchies with differentiated rewards.\n- **Relevance to PSG-KVC:** Budget allocation based on value signals, but not specifically KV cache compression or PRM-guided.\n- **Threat Level:** LOW\n\n**16. Input-Adaptive Allocation of LM Computation**\n- **Venue:** ICLR 2025\n- **Core Contribution:** Predicts required computation per query and allocates resources adaptively.\n- **Relevance to PSG-KVC:** Input-adaptive resource allocation, but not specifically KV cache or per-trajectory in tree search.\n- **Threat Level:** LOW\n\n---\n\n## Summary Assessment\n\n### The Novelty Gap\n\n**Your core claim:** \"No prior work conditions per-trajectory KV compression budgets on PRM scores in multi-trajectory tree search.\"\n\n**Verdict: CLAIM APPEARS VALID** with the following observations:\n\n1. **PRM + Tree Search** exists (ReST-MCTS*, UATS, reward-guided speculative decoding) but is **not** applied to KV cache compression budgets.\n\n2. **Adaptive KV Cache Budgets** exist (Ada-KV, Crystal-KV) but are **not** per-trajectory or PRM-guided. They are per-head or per-layer.\n\n3. **Per-Trajectory Resource Allocation** exists (BAVT, DPTS) but applies to computation/tool budget, **not** KV cache compression.\n\n4. **KV Cache Compression for Inference Scaling** exists (DMS, R-KV) but uses **uniform/learned** strategies, not per-trajectory PRM-based allocation.\n\nThe **intersection of all four elements** (KV cache compression + adaptive budgets + per-trajectory + PRM-guided) does not appear in the literature.\n\n### Key Risks/Gaps to Address\n\n1. **Dynamic Parallel Tree Search (DPTS, arxiv 2502.16235)** explicitly mentions \"fine-grained cache management\" per reasoning path. Verify this doesn't already condition cache allocation on trajectory state/quality signals.\n\n2. **BAVT's per-trajectory resource allocation principle** (arxiv 2603.12634) is very similar philosophically to what you're proposing, just applied to a different resource. Document how cache compression budget differs in application.\n\n3. **Confirm no papers combine:**\n   - PRM scoring signals\n   - KV cache compression (not just management/sharing)\n   - Per-trajectory conditional budgets\n   - Tree search/multi-trajectory setting\n\n---\n\n## Sources\n\n- [Inference-Time Hyper-Scaling with KV Cache Compression](https://arxiv.org/abs/2506.05345)\n- [Hold Onto That Thought: Assessing KV Cache Compression On Reasoning](https://arxiv.org/abs/2512.12008)\n- [R-KV: Redundancy-aware KV Cache Compression for Reasoning Models](https://arxiv.org/abs/2505.24133)\n- [Efficient Beam Search for Large Language Models Using Trie-Based Decoding](https://arxiv.org/abs/2502.00085)\n- [SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection](https://arxiv.org/abs/2605.02888)\n- [How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers](https://arxiv.org/abs/2604.17935)\n- [LongFlow: Efficient KV Cache Compression for Reasoning Models](https://arxiv.org/abs/2603.11504)\n- [Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference](https://arxiv.org/abs/2407.11550)\n- [Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle](https://arxiv.org/abs/2601.16986)\n- [Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents](https://arxiv.org/abs/2603.12634)\n- [Adaptive Uncertainty-Aware Tree Search for Robust Reasoning](https://arxiv.org/abs/2602.06493)\n- [Dynamic Parallel Tree Search for Efficient LLM Reasoning](https://arxiv.org/abs/2502.16235)\n- [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://openreview.net/forum?id=8rcFOqEud5)\n- [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://arxiv.org/abs/2501.19324)\n- [Hierarchical Budget Policy Optimization for Adaptive Reasoning](https://arxiv.org/abs/2507.15844)\n- [Input-Adaptive Allocation of LM Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf)"
      }
    ],
    "totalDurationMs": 135536,
    "totalTokens": 43879,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 255,
      "cache_creation_input_tokens": 530,
      "cache_read_input_tokens": 39084,
      "output_tokens": 4010,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 530
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 255,
          "output_tokens": 4010,
          "cache_read_input_tokens": 39084,
          "cache_creation_input_tokens": 530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 530,
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
  "sourceToolAssistantUUID": "8bcfc336-38a9-44ee-9b4e-6e07ac217424",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-09T19:46:48.837Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do a few more targeted searches to pressure test the novelty claim, especially checking for:
1. "Dynamic Parallel Tree Search" (DPTS, arxiv 2502.16235) - does this do per-path cache management?
2. Are there any very recent papers (early 2026) combining PRM with KV compression?
3. What about SpecKV and LongFlow?

Also, I want to assess the feasibility more carefully:
- The paper uses 2×A100 80GB for the 14B model, which makes sense
- The user asked for ≤200 H100-hours, but the proposal says ~200h A100 (manual mode). A100 hours vs H100 hours - H100 is roughly 2-3x faster than A100, so 200 A100 hours ≈ 70-100 H100 hours. This should be within budget.


- But there's a major timeline mismatch: the proposal estimates 3-5 months for manual implementation, yet the user has only 16 days before the deadline. The proposal also mentions 4-6 weeks for human-in-loop mode, which is still longer than available. This is a critical constraint that makes the feasibility questionable.
- The only approach that might work within 16 days is the auto research mode at 1-2 weeks, but that's extremely tight and assumes sufficient GPU resources are available.
- However, the auto research mode requires ~600 A100-hours (roughly 240 H100-hours), which already exceeds the 200 H100-hour budget constraint.
- So even the fastest approach violates the compute budget, and I haven't accounted for the time needed to write the actual paper.
- I'm also questioning whether running DeepSeek-R1-Distil-Qwen-14B with tree search (N=16 trajectories) on 2×A100 80GB is even feasible—the memory requirements for maintaining 16 KV caches simultaneously might exceed what's available.

The core technical approach is to use PRM scores to dynamically allocate KV cache compression levels across trajectories during tree search: high-scoring paths stay in FP16, mid-range ones drop to INT8, and low-scoring ones compress to INT4. But there's a critical calibration problem—the PRM thresholds are trained on MATH-500, which is significantly easier than AIME, so the score distributions won't align when applied to the harder dataset. Additionally, PRM scores themselves are noisy and don't perfectly predict final answer correctness, especially on difficult problems, so a trajectory with weak intermediate scores might still lead to a correct solution.

The lazy dequantization mechanism for promoting low-scoring trajectories from INT4 back to FP16 introduces implementation complexity and potential artifacts. Integrating this into ETS's existing RadixAttention and custom beam search infrastructure is a substantial engineering effort within a tight 16-day timeline. The claim about maintaining 99% of uncompressed accuracy also feels arbitrary without rigorous calibration across datasets.

Looking at the novelty angle, the search results suggest that using PRM scores to gate per-trajectory KV compression in tree search is genuinely novel—prior work like Ada-KV, Crystal-KV, R-KV, and PM-KVQ all approach the problem differently.

That said, the core contribution reads as a fairly straightforward combination of existing techniques: PRM-guided pruning, per-trajectory resource allocation (which BAVT and DPTS already explore), and standard KV quantization. The intuition that higher-PRM trajectories warrant better KV precision is somewhat obvious once you have both signals available, which could invite criticism about incremental engineering. For EMNLP 2026's Efficient Methods track, the venue seems appropriate, but the empirical gains—2-3× KV memory reduction with under 1% accuracy loss—aren't particularly striking.

Looking at feasibility more carefully, there's a real timeline crunch: manual or human-in-the-loop approaches don't fit a 16-day window, and the automatic mode risks exceeding the compute budget. The method itself is simple (threshold-based compression), which is both a strength for clarity and a weakness for novelty. Overall, I'd rate this as 3/5 on novelty (genuine gap but obvious solution), 2/5 on feasibility (serious timeline and compute constraints), 4/5 on clarity, and 3/5 on impact—useful for practitioners but fundamentally incremental.

Actually, I should double-check the compute budget comparison. The proposal mentions A100s but the constraint is stated in H100-hours. Since H100s are roughly 2× faster for inference than A100s, 200 H100-hours is more like 100 H100-equivalent hours when accounting for the A100 hardware being used.

The manual mode fits within that adjusted budget, but it requires 3-5 months. The auto research mode could theoretically fit the 16-day timeline but would need around 300 H100-equivalent hours, exceeding the budget. However, with the ETS codebase already available and focused effort, there might be a path: implementing the compression oracle in a few days, running experiments over a week, and writing in parallel could compress the timeline significantly.

But the generator's own estimates suggest this would still take longer than 16 days, which creates a real tension. The core problems are that the timeline and compute budget don't align well with either approach, the novelty feels incremental for a top-tier venue, the lazy dequantization implementation carries technical risk, and there's a potential distribution shift issue with the PRM scores between the calibration and evaluation datasets that could undermine the results.

I should also verify the paper dates—arXiv:2506.05345 from June 2025 is about a year old now in May 2026, which checks out, and the January 2026 ICLR paper is recent enough. Looking at the Dynamic Parallel Tree Search work, the fine-grained cache management per path needs closer scrutiny.

Given all this, my assessment is that the work needs revision. The PRM-score-gated KV compression is genuinely novel and hasn't appeared in prior work, but the timeline estimates from the generator itself contradict the feasibility claim, and there are too many unresolved technical and methodological concerns. HIL (4-6 weeks) don't fit the 16-day requirement. Only auto research (1-2 weeks) fits, but at 600 A100 hours ≈ 300 H100 hours, it exceeds the 200 H100-hour compute constraint. There's a fundamental tension: you can't do this fast enough manually within the compute budget.

The core insight—using PRM scores to gate KV budget—is somewhat obvious once you have the pieces, which limits novelty. Technical risks around lazy dequantization and calibration transfer across datasets are real concerns. Looking at the overall assessment, novelty is around 3/5, feasibility drops to 2/5 due to the timeline-compute conflict, and impact is incremental at 3/5. This puts the whole thing well below a 4.0 threshold, so I need to rethink the approach.

Let me check if DPTS has already tackled the KV cache management angle I'm considering.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b24a994f-03dc-44b5-a245-f51239d6a3aa",
  "isSidechain": false,
  "requestId": "req_011Casa27JbHNNXDyKHChYD9",
  "type": "assistant",
  "uuid": "4a44d1f9-6ca6-45b6-9b1d-ae168585e6bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RJVeiu7PZz5GYL45GQpWoD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 922,
      "cache_creation_input_tokens": 6901,
      "cache_read_input_tokens": 23441,
      "output_tokens": 3358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 922,
          "output_tokens": 3358,
          "cache_read_input_tokens": 23441,
          "cache_creation_input_tokens": 6901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6901
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

_source line 19 · 2026-05-09T19:46:49.057Z_

Let me do one more targeted search on the most critical competitor paper and the timeline/feasibility concerns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a44d1f9-6ca6-45b6-9b1d-ae168585e6bb",
  "isSidechain": false,
  "requestId": "req_011Casa27JbHNNXDyKHChYD9",
  "type": "assistant",
  "uuid": "e4ac3752-cd6a-4f23-9687-651f10005f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RJVeiu7PZz5GYL45GQpWoD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 922,
      "cache_creation_input_tokens": 6901,
      "cache_read_input_tokens": 23441,
      "output_tokens": 3358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 922,
          "output_tokens": 3358,
          "cache_read_input_tokens": 23441,
          "cache_creation_input_tokens": 6901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6901
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

_source line 20 · 2026-05-09T19:46:53.298Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XRQJD111pSXWfrgbc5Hu9U`</summary>

```json
{
  "description": "Check Dynamic Parallel Tree Search paper and feasibility",
  "subagent_type": "Explore",
  "prompt": "Please search for and read these specific papers to understand their contribution:\n\n1. \"Dynamic Parallel Tree Search for Efficient LLM Reasoning\" arXiv:2502.16235 - Fetch the abstract from https://arxiv.org/abs/2502.16235 and tell me:\n   - Does it do per-trajectory KV cache compression budget allocation based on quality/reward signals?\n   - Does it use any form of quantization (INT4/INT8) for KV caches?\n   - Is the \"fine-grained cache management\" they mention actually KV compression or just prefix sharing?\n\n2. Also fetch or search for \"LongFlow: Efficient KV Cache Compression for Reasoning Models\" arXiv:2603.11504 - what does this paper do?\n\n3. Search for \"BAVT budget-aware value tree search\" arXiv:2603.12634 - does this paper apply per-trajectory budget to KV cache or just to computation?\n\n4. Finally, search for recent papers (2025-2026) that combine: \"quantization\" AND \"tree search\" AND \"reasoning\" on arxiv to find any we might have missed.\n\nPlease fetch the arxiv abstract pages directly for papers 1-3 to get accurate information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4ac3752-cd6a-4f23-9687-651f10005f1c",
  "isSidechain": false,
  "requestId": "req_011Casa27JbHNNXDyKHChYD9",
  "type": "assistant",
  "uuid": "db4b73c9-9464-4d2d-8098-e1f3e012bb69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RJVeiu7PZz5GYL45GQpWoD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 922,
      "cache_creation_input_tokens": 6901,
      "cache_read_input_tokens": 23441,
      "output_tokens": 3358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 922,
          "output_tokens": 3358,
          "cache_read_input_tokens": 23441,
          "cache_creation_input_tokens": 6901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6901
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "db4b73c9-9464-4d2d-8098-e1f3e012bb69",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify PRM-gated KV compression idea for EMNLP 2026",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf"
}
```

---

### Tool result

_source line 23 · 2026-05-09T19:48:05.167Z_

<details><summary>↩ Tool result · `toolu_01XRQJD111pSXWfrgbc5Hu9U`</summary>

```text
Excellent! Now I have comprehensive information. Let me provide you with a detailed summary of my findings:

## Summary of Research Findings

### Paper 1: "Dynamic Parallel Tree Search for Efficient LLM Reasoning" (arXiv:2502.16235)

**Answers to your specific questions:**

1. **Per-trajectory KV cache compression budget allocation?** NO. DPTS uses a single adaptive parallelism queue size calculated globally: "|P| = (O_max - O_init) / (O_peak - O_init)" based on overall available GPU memory. There is no per-trajectory reward-based budget allocation.

2. **Quantization (INT4/INT8)?** NO. The paper contains no references to quantization techniques for KV caches.

3. **Fine-grained cache management type?** It is NOT true KV compression. The "fine-grained cache management" consists of three simple techniques:
   - **Isolated Storage**: Each node retains only its own KV cache (not complete sequences)
   - **Padding Strategy**: Left-padding with zeros for shorter KV caches to enable parallel processing
   - **Memory Cleanup**: Releasing KV cache when leaf nodes terminate or all children branches are finished
   
   The authors themselves acknowledge this as "a simple but straightforward padding technique" rather than compression. They note that more advanced techniques like DEFT could be "orthogonal" to their work.

---

### Paper 2: "LongFlow: Efficient KV Cache Compression for Reasoning Models" (arXiv:2603.11504)

LongFlow addresses memory issues in long-output reasoning models with the following approach:

- **Main Mechanism**: Uses **token eviction** (not quantization) during generation
- **Importance Metric**: Derives importance scores from intermediate attention computation results using only the current query, avoiding expensive re-evaluation
- **Custom Kernel**: Fuses FlashAttention, importance estimation, and token eviction into a single optimized operator
- **Performance**: Achieves 11.8x throughput improvement with 80% KV cache compression with minimal accuracy impact
- **Key Innovation**: Unlike existing long-input/short-output methods, it addresses long-output reasoning scenarios with negligible computational overhead

---

### Paper 3: "BAVT: Budget-Aware Value Tree Search" (arXiv:2603.12634)

**Budget allocation scope:** Budget is applied to **tool calls and token generation ONLY**, NOT to KV cache or computation.

- **Resource Dimensions**: Tracks tool invocations and output tokens as state variables
- **Dynamic Allocation Strategy**: Uses a budget-conditioned node selection with scaling exponent αt = 1/rt (where rt is remaining budget ratio)
  - When budget is abundant (rt ≈ 1): promotes diverse exploration
  - When budget depletes (rt → 0): concentrates probability on highest-value branches
- **Key Finding**: BAVT at 5 tool calls outperforms baselines at 20 tool calls, showing allocation strategy beats brute-force scaling

---

### Related Papers on Quantization + Tree Search + Reasoning

I found several highly relevant 2025-2026 papers that address your search criteria:

1. **"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression"** (arXiv:2510.08525)
   - Uses RL to identify attention heads critical for reasoning
   - Allocates full KV cache to critical heads while aggressively compressing others
   - Achieves 20-50% cache reduction with 1.21x speedup

2. **"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models"** (arXiv:2505.24133)
   - Targets redundant tokens specifically in reasoning models
   - Preserves 100% performance with only 10% of KV cache
   - Achieves 6.6x throughput improvement (method details not specified in abstract)

3. **"ETS: Efficient Tree Search for Inference-Time Scaling"** (arXiv:2502.13575)
   - Promotes KV cache sharing through linear programming cost model
   - Penalizes node retention while maintaining semantic diversity
   - Achieves 1.8x KV cache size reduction and 1.4x throughput improvement

4. **"How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers"** (arXiv:2604.17935)
   - Theoretical analysis of k-hop reasoning under shared KV cache of size s
   - Studies fundamental tradeoffs between transformer depth and cache compression
   - Shows adaptive locality-respecting caches outperform random eviction

5. **"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models"** (arXiv:2602.03203)
   - Training-based framework using supervised and RL learning
   - Predicts which KV pairs to evict based on future attention scores
   - Outperforms prior methods at half the cache budget

6. **"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning"** (arXiv:2512.12008)
   - Benchmarks compression strategies on long-reasoning tasks
   - Finds H2O and SnapKV variants work best for reasoning traces
   - Reveals tradeoff: cache eviction at low budgets can produce longer reasoning traces

7. **"Quantization Hurts Reasoning? An Empirical Study on Quantized Reasoning Models"** (arXiv:2504.04823)
   - Evaluates W4A8, W8A8 quantization on reasoning models
   - **Explicitly covers KV cache quantization** across bit-widths
   - Findings: W8A8 and W4A16 are lossless; lower bit-widths introduce significant accuracy risks

8. **"Unifying Tree Search Algorithm and Reward Design for LLM Reasoning"** (arXiv:2510.09988)
   - Survey covering tree search algorithms and reward design
   - Identifies caching as a key optimization mechanism (tree structure caching and sequence caching)
   - Discusses distinction between test-time scaling and self-improvement paradigms

---

### Key Findings Summary

**None of the papers 1-3 explicitly combine per-trajectory KV cache compression budget allocation with quantization.** Here's what the landscape shows:

- **DPTS (Paper 1)**: Simple padding-based cache isolation, no compression or quantization
- **LongFlow (Paper 2)**: Token eviction via importance scoring, not quantization
- **BAVT (Paper 3)**: Budget allocation for tool/token resources, not KV cache

**The closest you get to per-trajectory KV optimization:**
- **RLKV** (head-selective compression based on reasoning quality)
- **ETS** (tree-aware KV sharing with semantic diversity constraints)

**Quantization research is separate:**
- **Quantization Hurts Reasoning** paper focuses on weight/activation/KV cache quantization but doesn't specifically address tree search scenarios

The field appears to have separated concerns: quantization research targets general reasoning performance degradation, while tree search optimization focuses on prefix/cache sharing and importance-based eviction without combining with quantization.

---

### Sources

- [Dynamic Parallel Tree Search for Efficient LLM Reasoning](https://arxiv.org/abs/2502.16235)
- [LongFlow: Efficient KV Cache Compression for Reasoning Models](https://arxiv.org/abs/2603.11504)
- [BAVT: Budget-Aware Value Tree Search](https://arxiv.org/abs/2603.12634)
- [Which Heads Matter for Reasoning? RL-Guided KV Cache Compression](https://arxiv.org/abs/2510.08525)
- [R-KV: Redundancy-aware KV Cache Compression for Reasoning Models](https://arxiv.org/abs/2505.24133)
- [ETS: Efficient Tree Search for Inference-Time Scaling](https://arxiv.org/abs/2502.13575)
- [How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers](https://arxiv.org/abs/2604.17935)
- [ForesightKV: Optimizing KV Cache Eviction for Reasoning Models](https://arxiv.org/abs/2602.03203)
- [Hold Onto That Thought: Assessing KV Cache Compression On Reasoning](https://arxiv.org/abs/2512.12008)
- [Quantization Hurts Reasoning? An Empirical Study on Quantized Reasoning Models](https://arxiv.org/abs/2504.04823)
- [Unifying Tree Search Algorithm and Reward Design for LLM Reasoning: A Survey](https://arxiv.org/html/2510.09988v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db4b73c9-9464-4d2d-8098-e1f3e012bb69",
  "isSidechain": false,
  "promptId": "f3fa5027-4a94-46c0-bb8d-7ed240d28059",
  "type": "user",
  "uuid": "9699d9cf-f1de-4b7b-9e0f-2ac68155ffed",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Please search for and read these specific papers to understand their contribution:\n\n1. \"Dynamic Parallel Tree Search for Efficient LLM Reasoning\" arXiv:2502.16235 - Fetch the abstract from https://arxiv.org/abs/2502.16235 and tell me:\n   - Does it do per-trajectory KV cache compression budget allocation based on quality/reward signals?\n   - Does it use any form of quantization (INT4/INT8) for KV caches?\n   - Is the \"fine-grained cache management\" they mention actually KV compression or just prefix sharing?\n\n2. Also fetch or search for \"LongFlow: Efficient KV Cache Compression for Reasoning Models\" arXiv:2603.11504 - what does this paper do?\n\n3. Search for \"BAVT budget-aware value tree search\" arXiv:2603.12634 - does this paper apply per-trajectory budget to KV cache or just to computation?\n\n4. Finally, search for recent papers (2025-2026) that combine: \"quantization\" AND \"tree search\" AND \"reasoning\" on arxiv to find any we might have missed.\n\nPlease fetch the arxiv abstract pages directly for papers 1-3 to get accurate information.",
    "agentId": "aec1eaf519b9e57b7",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now I have comprehensive information. Let me provide you with a detailed summary of my findings:\n\n## Summary of Research Findings\n\n### Paper 1: \"Dynamic Parallel Tree Search for Efficient LLM Reasoning\" (arXiv:2502.16235)\n\n**Answers to your specific questions:**\n\n1. **Per-trajectory KV cache compression budget allocation?** NO. DPTS uses a single adaptive parallelism queue size calculated globally: \"|P| = (O_max - O_init) / (O_peak - O_init)\" based on overall available GPU memory. There is no per-trajectory reward-based budget allocation.\n\n2. **Quantization (INT4/INT8)?** NO. The paper contains no references to quantization techniques for KV caches.\n\n3. **Fine-grained cache management type?** It is NOT true KV compression. The \"fine-grained cache management\" consists of three simple techniques:\n   - **Isolated Storage**: Each node retains only its own KV cache (not complete sequences)\n   - **Padding Strategy**: Left-padding with zeros for shorter KV caches to enable parallel processing\n   - **Memory Cleanup**: Releasing KV cache when leaf nodes terminate or all children branches are finished\n   \n   The authors themselves acknowledge this as \"a simple but straightforward padding technique\" rather than compression. They note that more advanced techniques like DEFT could be \"orthogonal\" to their work.\n\n---\n\n### Paper 2: \"LongFlow: Efficient KV Cache Compression for Reasoning Models\" (arXiv:2603.11504)\n\nLongFlow addresses memory issues in long-output reasoning models with the following approach:\n\n- **Main Mechanism**: Uses **token eviction** (not quantization) during generation\n- **Importance Metric**: Derives importance scores from intermediate attention computation results using only the current query, avoiding expensive re-evaluation\n- **Custom Kernel**: Fuses FlashAttention, importance estimation, and token eviction into a single optimized operator\n- **Performance**: Achieves 11.8x throughput improvement with 80% KV cache compression with minimal accuracy impact\n- **Key Innovation**: Unlike existing long-input/short-output methods, it addresses long-output reasoning scenarios with negligible computational overhead\n\n---\n\n### Paper 3: \"BAVT: Budget-Aware Value Tree Search\" (arXiv:2603.12634)\n\n**Budget allocation scope:** Budget is applied to **tool calls and token generation ONLY**, NOT to KV cache or computation.\n\n- **Resource Dimensions**: Tracks tool invocations and output tokens as state variables\n- **Dynamic Allocation Strategy**: Uses a budget-conditioned node selection with scaling exponent αt = 1/rt (where rt is remaining budget ratio)\n  - When budget is abundant (rt ≈ 1): promotes diverse exploration\n  - When budget depletes (rt → 0): concentrates probability on highest-value branches\n- **Key Finding**: BAVT at 5 tool calls outperforms baselines at 20 tool calls, showing allocation strategy beats brute-force scaling\n\n---\n\n### Related Papers on Quantization + Tree Search + Reasoning\n\nI found several highly relevant 2025-2026 papers that address your search criteria:\n\n1. **\"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression\"** (arXiv:2510.08525)\n   - Uses RL to identify attention heads critical for reasoning\n   - Allocates full KV cache to critical heads while aggressively compressing others\n   - Achieves 20-50% cache reduction with 1.21x speedup\n\n2. **\"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models\"** (arXiv:2505.24133)\n   - Targets redundant tokens specifically in reasoning models\n   - Preserves 100% performance with only 10% of KV cache\n   - Achieves 6.6x throughput improvement (method details not specified in abstract)\n\n3. **\"ETS: Efficient Tree Search for Inference-Time Scaling\"** (arXiv:2502.13575)\n   - Promotes KV cache sharing through linear programming cost model\n   - Penalizes node retention while maintaining semantic diversity\n   - Achieves 1.8x KV cache size reduction and 1.4x throughput improvement\n\n4. **\"How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers\"** (arXiv:2604.17935)\n   - Theoretical analysis of k-hop reasoning under shared KV cache of size s\n   - Studies fundamental tradeoffs between transformer depth and cache compression\n   - Shows adaptive locality-respecting caches outperform random eviction\n\n5. **\"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models\"** (arXiv:2602.03203)\n   - Training-based framework using supervised and RL learning\n   - Predicts which KV pairs to evict based on future attention scores\n   - Outperforms prior methods at half the cache budget\n\n6. **\"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning\"** (arXiv:2512.12008)\n   - Benchmarks compression strategies on long-reasoning tasks\n   - Finds H2O and SnapKV variants work best for reasoning traces\n   - Reveals tradeoff: cache eviction at low budgets can produce longer reasoning traces\n\n7. **\"Quantization Hurts Reasoning? An Empirical Study on Quantized Reasoning Models\"** (arXiv:2504.04823)\n   - Evaluates W4A8, W8A8 quantization on reasoning models\n   - **Explicitly covers KV cache quantization** across bit-widths\n   - Findings: W8A8 and W4A16 are lossless; lower bit-widths introduce significant accuracy risks\n\n8. **\"Unifying Tree Search Algorithm and Reward Design for LLM Reasoning\"** (arXiv:2510.09988)\n   - Survey covering tree search algorithms and reward design\n   - Identifies caching as a key optimization mechanism (tree structure caching and sequence caching)\n   - Discusses distinction between test-time scaling and self-improvement paradigms\n\n---\n\n### Key Findings Summary\n\n**None of the papers 1-3 explicitly combine per-trajectory KV cache compression budget allocation with quantization.** Here's what the landscape shows:\n\n- **DPTS (Paper 1)**: Simple padding-based cache isolation, no compression or quantization\n- **LongFlow (Paper 2)**: Token eviction via importance scoring, not quantization\n- **BAVT (Paper 3)**: Budget allocation for tool/token resources, not KV cache\n\n**The closest you get to per-trajectory KV optimization:**\n- **RLKV** (head-selective compression based on reasoning quality)\n- **ETS** (tree-aware KV sharing with semantic diversity constraints)\n\n**Quantization research is separate:**\n- **Quantization Hurts Reasoning** paper focuses on weight/activation/KV cache quantization but doesn't specifically address tree search scenarios\n\nThe field appears to have separated concerns: quantization research targets general reasoning performance degradation, while tree search optimization focuses on prefix/cache sharing and importance-based eviction without combining with quantization.\n\n---\n\n### Sources\n\n- [Dynamic Parallel Tree Search for Efficient LLM Reasoning](https://arxiv.org/abs/2502.16235)\n- [LongFlow: Efficient KV Cache Compression for Reasoning Models](https://arxiv.org/abs/2603.11504)\n- [BAVT: Budget-Aware Value Tree Search](https://arxiv.org/abs/2603.12634)\n- [Which Heads Matter for Reasoning? RL-Guided KV Cache Compression](https://arxiv.org/abs/2510.08525)\n- [R-KV: Redundancy-aware KV Cache Compression for Reasoning Models](https://arxiv.org/abs/2505.24133)\n- [ETS: Efficient Tree Search for Inference-Time Scaling](https://arxiv.org/abs/2502.13575)\n- [How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers](https://arxiv.org/abs/2604.17935)\n- [ForesightKV: Optimizing KV Cache Eviction for Reasoning Models](https://arxiv.org/abs/2602.03203)\n- [Hold Onto That Thought: Assessing KV Cache Compression On Reasoning](https://arxiv.org/abs/2512.12008)\n- [Quantization Hurts Reasoning? An Empirical Study on Quantized Reasoning Models](https://arxiv.org/abs/2504.04823)\n- [Unifying Tree Search Algorithm and Reward Design for LLM Reasoning: A Survey](https://arxiv.org/html/2510.09988v1)"
      }
    ],
    "totalDurationMs": 71864,
    "totalTokens": 28253,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1411,
      "cache_read_input_tokens": 24721,
      "output_tokens": 2114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2114,
          "cache_read_input_tokens": 24721,
          "cache_creation_input_tokens": 1411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1411,
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
  "sourceToolAssistantUUID": "db4b73c9-9464-4d2d-8098-e1f3e012bb69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-09T19:48:28.957Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have a comprehensive picture. Let me synthesize my findings and produce the verdict.

Key findings:
1. **All cited papers exist** - good, the generator didn't fabricate references.
2. **Novelty claim is mostly valid**: No paper explicitly combines PRM scores with per-trajectory KV cache quantization in tree search. However, there's a paper I need to flag: "Which Heads Matter for Reasoning? RL-Guided KV Cache Compression" (arXiv:2510.08525) which uses RL to identify and differentially compress KV by importance. This is closer to the idea than the generator acknowledged.


3. **DPTS and BAVT don't actually address the core proposal** - DPTS only handles basic cache isolation while BAVT focuses on token budgeting, neither doing the kind of compression or PRM-gating the proposal describes.

Now I'm seeing a major tension: the timeline constraints are incompatible with the compute requirements. Manual and HIL modes both need months, which far exceeds the 16-day window, and while auto research mode could theoretically fit in 1-2 weeks, it demands 600 A100 hours—that's a massive computational cost that raises serious feasibility questions.

There's also a critical concern about quantization degrading reasoning performance, especially for INT4 KV cache compression. Beyond that, I'm noticing the generator overlooked some relevant work—there's an RL-guided compression approach that actually does differentially compress based on reasoning quality, and ForesightKV uses learning to predict which KV pairs matter most.

The calibration transfer is a real problem too: thresholds tuned on MATH-500 won't transfer cleanly to AIME 2024/2025 since the PRM score distributions are completely different. And stepping back, the core contribution feels incremental—it's essentially combining known techniques (PRM-guided search + KV quantization) with the fairly obvious insight that weaker trajectories should compress more. That's solid engineering work, but might not meet the bar for a top-tier venue. Finally, even though ETS has open-source code, integrating per-trajectory quantization with bitsandbytes isn't necessarily straightforward, and the lazy dequantization kernel implementation details are unclear.

Looking at the overall assessment: novelty is around 3/5 since the gap exists but the combination is somewhat obvious, feasibility drops to 2/5 because no experimental mode actually fits both the 16-day timeline and the 200 H100-hour budget simultaneously, clarity is solid at 4/5, and impact is 3/5—useful but incremental. That averages to 3.0, which means I should revise. The key issue is that the auto research mode, which is the only one compatible with the timeline, needs roughly 240-300 H100 hours, blowing past the 200-hour constraint. I need to redesign the experiments to actually fit within those bounds.

Beyond the budget problem, I should incorporate the "Quantization Hurts Reasoning" paper as a critical risk—I need to show that INT4 quantization doesn't tank performance even for weaker reasoning trajectories. The calibration threshold transfer from MATH-500 to AIME also needs either solid justification or should be redone on a harder task. I should also acknowledge the RL-guided KV work as a closer related baseline than I initially credited. Finally, I need to pare down the experimental scope to make everything feasible within the constraints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9699d9cf-f1de-4b7b-9e0f-2ac68155ffed",
  "isSidechain": false,
  "requestId": "req_011CasaC6dSkJQz8dsSTMExw",
  "type": "assistant",
  "uuid": "9a629bdb-4258-4586-94a4-d09e4ff32270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01E7Nwbeyx31fCsWWvNasDF4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6396,
      "cache_read_input_tokens": 30342,
      "output_tokens": 3306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6396,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3306,
          "cache_read_input_tokens": 30342,
          "cache_creation_input_tokens": 6396,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6396
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

_source line 25 · 2026-05-09T19:49:10.240Z_

Now I have enough information to produce a comprehensive verdict. Let me synthesize all findings.

**Key verified facts:**
1. All 6 core cited papers exist and say roughly what's claimed
2. EMNLP 2026 ARR deadline May 25 is confirmed; "Efficient Methods for NLP" is a valid track
3. DeepSeek-R1-Distill-Qwen-14B is available open-weights; ETS codebase exists on GitHub
4. DPTS (2502.16235): only does padding-based cache isolation, no quantization or PRM-gating — not a threat
5. Novel uncited competitor found: **"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression"** (arXiv:2510.08525) — uses RL to differentially compress KV by reasoning importance
6. Critical threat: **"Quantization Hurts Reasoning?"** (arXiv:2504.04823) shows INT4 KV quantization introduces significant accuracy risks in reasoning models
7. **Timeline-compute conflict**: Manual (3-5 months) and HIL (4-6 weeks) don't fit the 16-day window. Auto research (1-2 weeks) fits but uses ~600 A100-hours ≈ 240-300 H100-hours, **exceeding the 200 H100-hour hard constraint**.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The specific combination of PRM-score-gated per-trajectory KV quantization in tree search is genuinely not in the literature. However, the conceptual leap is incremental — once you have PRM scores and KV compression, differentially allocating compression by score is the obvious engineering step. The paper 'Which Heads Matter for Reasoning? RL-Guided KV Cache Compression' (arXiv:2510.08525) uses a quality-signal-based differential compression for reasoning and is closer to PSG-KVC than the generator acknowledged; it must be discussed and differentiated."
    },
    "feasibility": {
      "score": 2,
      "rationale": "There is a hard conflict: the only timeline-compatible mode (auto research, 1-2 weeks) uses ~600 A100-hours ≈ 240-300 H100-hours, violating the ≤200 H100-hour constraint; manual/HIL modes fit the compute budget but take 3-5 months or 4-6 weeks, violating the 16-day deadline. Additionally, 'Quantization Hurts Reasoning?' (arXiv:2504.04823) directly shows INT4 KV cache quantization introduces significant accuracy degradation for reasoning models — the generator must demonstrate that even bottom-quartile trajectories survive INT4 without unacceptable quality collapse before this premise holds."
    },
    "clarity": {
      "score": 4,
      "rationale": "The idea is explained clearly with a concrete mechanism, layered ablation plan, and well-structured baselines. The landscape section is thorough and the calibration procedure is explicit."
    },
    "impact": {
      "score": 3,
      "rationale": "2-3× KV memory reduction composable with ETS's 1.4× throughput gain is a useful systems contribution, but the benefit is bounded by the fact that beam search N≥16 is rarely used outside specialized math-reasoning pipelines. The method doesn't generalize beyond PRM-guided tree search, limiting broader impact."
    }
  },
  "issues": [
    "CRITICAL — Timeline-compute conflict: The generator's own resource estimates show that no single mode satisfies both constraints simultaneously. Manual/HIL modes satisfy ≤200 H100-hours but take 3-5 months or 4-6 weeks (far beyond 16 days). Auto research mode fits 1-2 weeks but uses ~600 A100-hours ≈ 240-300 H100-hours, exceeding the 200 H100-hour hard constraint. The generator must either (a) redesign the experiment scope so a 16-day manual effort uses <200 H100-hours, or (b) explicitly acknowledge the tradeoff and propose a minimal-viable experiment set.",
    "CRITICAL — INT4 quantization accuracy risk for reasoning: 'Quantization Hurts Reasoning? An Empirical Study on Quantized Reasoning Models' (arXiv:2504.04823) finds that below W8A8/W4A16, reasoning accuracy degrades significantly with KV quantization. The PSG-KVC proposal applies INT4 to bottom-quartile trajectories and claims <1% accuracy loss — but this claim is unvalidated. If INT4 causes reasoning collapse even for trajectories expected to be pruned, those trajectories may be discarded prematurely rather than through legitimate low PRM scores, creating a confound in the accuracy measurements.",
    "Uncited related work — RL-Guided KV Cache Compression: 'Which Heads Matter for Reasoning? RL-Guided KV Cache Compression' (arXiv:2510.08525) uses a quality-signal-based differential KV compression strategy for reasoning models, allocating full precision to critical heads and aggressively compressing others. This is closer to PSG-KVC conceptually than any paper in the landscape section. The generator must differentiate PSG-KVC from this work (the key difference is trajectory-level vs. head-level allocation, and PRM signal vs. RL signal) or risk reviewer rejection for insufficient novelty discussion.",
    "Calibration transfer problem: Fixed score-percentile thresholds are calibrated on MATH-500 (median difficulty ~AMC/AIME-12 level) and applied zero-shot to AIME 2024/2025 (much harder). PRM score distributions will be dramatically different — on hard problems, all trajectories may fall into 'bottom quartile' by MATH-500 thresholds, triggering universal INT4 compression. The generator proposes no adaptive thresholding mechanism to handle distribution shift.",
    "Missing baseline: ForesightKV (arXiv:2602.03203) uses supervised/RL learning to predict optimal KV eviction for reasoning models and achieves strong results. This is a stronger baseline than R-KV-style attention-score eviction and should be included to fairly benchmark the value of the PRM signal versus learned eviction predictors.",
    "Engineering risk underestimated: Lazy dequantization on mid-search promotion (INT4→FP16 upcasting at an arbitrary search step) requires modifying the KV cache buffer in-place during active beam expansion. This is not a standard bitsandbytes operation — it requires custom CUDA kernel work that could easily consume 5-7 of the 16 available days to get numerically correct. The proposal treats this as a known-difficulty item but does not account for the debugging time in any mode's timeline.",
    "Venue-contribution fit: The paper's primary contribution is a systems-engineering method (a threshold oracle + compression tier assignment). EMNLP Efficient Methods track historically accepts papers with strong empirical NLP task evaluations (MMLU, MT-Bench, LongBench per the user's requirements), not just math reasoning (MATH-500, AIME). The generator should add at least one general NLP task evaluation to support the 'Efficient Methods for NLP' framing."
  ],
  "feedback": "The core idea (PRM-score-gated per-trajectory KV quantization in tree search) is novel and the literature gap is real. To get to 'pass', the generator must address four things: (1) Resolve the timeline-compute conflict by designing a focused 16-day experiment plan that uses ≤200 H100-hours — concretely, cut the auto-research mode's ablation scope to N∈{4,8,16} on MATH-500 + one AIME split only, targeting ~120 H100-hours; (2) Add an empirical validation that INT4 KV cache quantization is acceptable for low-PRM-score reasoning trajectories — the 'Quantization Hurts Reasoning?' paper (arXiv:2504.04823) is a direct challenge that must be addressed with a preliminary INT4 accuracy characterization; (3) Add 'Which Heads Matter for Reasoning? RL-Guided KV Cache Compression' (arXiv:2510.08525) to the landscape and explicitly differentiate PSG-KVC (trajectory-level + PRM signal) from head-level + RL-signal approaches; (4) Replace the fixed calibration thresholds with a simple online percentile tracker that adapts to the empirical PRM score distribution at each search step — this costs one day of implementation and eliminates the distribution-shift failure mode. Additionally, add one general NLP task evaluation (e.g., MT-Bench with DeepSeek-R1-Distill-Qwen-14B) to satisfy the EMNLP Efficient Methods track framing. The method is publishable in Findings if these issues are addressed; Main track requires the impact case to be stronger.",
  "reason": "Genuine novelty gap exists but idea has a hard timeline-compute conflict (no mode satisfies both ≤16 days AND ≤200 H100-hours), a critical unvalidated assumption that INT4 KV quantization is safe for reasoning trajectories, and an uncited related competitor that must be differentiated."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a629bdb-4258-4586-94a4-d09e4ff32270",
  "isSidechain": false,
  "requestId": "req_011CasaC6dSkJQz8dsSTMExw",
  "type": "assistant",
  "uuid": "2155dfb2-b7f3-4689-9fa8-a943ccc1d1c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01E7Nwbeyx31fCsWWvNasDF4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6396,
      "cache_read_input_tokens": 30342,
      "output_tokens": 3306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6396,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3306,
          "cache_read_input_tokens": 30342,
          "cache_creation_input_tokens": 6396,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6396
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "2155dfb2-b7f3-4689-9fa8-a943ccc1d1c7",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify PRM-gated KV compression idea for EMNLP 2026",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "2155dfb2-b7f3-4689-9fa8-a943ccc1d1c7",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify PRM-gated KV compression idea for EMNLP 2026",
  "sessionId": "1ca4ec28-626f-47a3-8b64-c2f9893024cf"
}
```

---
