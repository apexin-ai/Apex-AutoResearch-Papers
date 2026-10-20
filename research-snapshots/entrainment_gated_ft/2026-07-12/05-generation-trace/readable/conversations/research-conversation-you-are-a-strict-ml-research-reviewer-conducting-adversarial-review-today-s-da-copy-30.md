# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/bdf522a6-a8a8-46bb-9a44-de1ead278b20.jsonl`
- **Structured JSON:** [`bb99a26747efb2b9574b.json`](../../sessions/bb/bb99a26747efb2b9574b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T03:46:03.372Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T03:46:03.372Z",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.\n\nDirection: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.\n\nContribution type: METHOD ONLY. Propose new algorithms — not profiling studies.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Generous for efficiency work.\n2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.\n3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.\n\nLook for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.\n\nTag: direction=efficiency, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 8/10)\n{\n  \"title\": \"Composing Static and Contextual Corrections for Activation Sparsity in SwiGLU LLMs via Output-Distribution Distillation\",\n  \"core_problem\": \"Training-free activation sparsity methods (WINA, TEAL, R-Sparse) have enabled 40-60% model-level neuron pruning on native SwiGLU LLMs, but leave a substantial quality gap: at 50% model-level activation sparsity on Llama-3-8B, WINA achieves 59.57% average across six standard benchmarks (PIQA, ARC-c, WinoGrande, HellaSwag, MMLU, GSM8K) versus the dense model's 66.38% — a 6.81-point drop, with reasoning-heavy tasks (GSM8K, MMLU) degrading disproportionately. Two recent learned approaches partially address this gap from complementary but individually incomplete directions. SPON (Resting Neurons, arXiv 2512.12744v3, ICML 2026 per arXiv metadata updated on the April 30 notification date) introduces static, input-independent learnable bias vectors trained via KL-divergence distillation, recovering ~1 point over WINA on five QA benchmarks (ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande; 71.96 vs 70.97 weighted average) at zero inference overhead — demonstrating that output-distribution alignment helps, but leaving input-dependent importance patterns entirely unaddressed. FastForward (arXiv 2602.00397) trains contextual predictors with weighted BCE loss plus an error compensation network (2-layer MLP, r'=d_model/8) trained with MSE loss that operates at inference time, achieving MMLU 67.17 vs dense 67.84 at 50% FFN sparsity on Llama-3.1-8B — demonstrating that contextual prediction helps, but requiring the auxiliary compensation network to address the output-quality deficiency inherent in BCE's per-neuron objective. The compensation network adds ~8.0 MB of weights per layer (r'=d_model/8=512; two matrices of 4096×512, totaling 4,194,304 params × 2 bytes FP16 ≈ 8.0 MB) and associated GEMV operations at inference time — substantial overhead that motivates seeking training objectives that eliminate the need for compensation entirely. The critical insight is that BCE's training signal decomposes as L_BCE = Σ_j l(y_j, s_j), a mean-field factorization P(y_1,...,y_D) ≈ Π_j P(y_j) that treats each neuron's activation decision as independent of all others. This cannot capture joint interaction effects — the fact that pruning neuron A may only degrade output quality when neuron B in the same or subsequent layer is also pruned. FastForward's error compensation network is an engineering fix for this fundamental limitation: it patches output errors post-hoc rather than training the predictor to avoid them. KL divergence on output logits, by contrast, backpropagates through the full sparse forward pass via ∂L_KL/∂θ = ∂L_KL/∂p_sparse · ∂p_sparse/∂h_out · ∂h_out/∂m · ∂m/∂θ, where the term ∂h_out/∂m captures how each neuron's mask decision jointly affects the output in combination with all other active neurons. This yields a testable prediction: KL's advantage over BCE should increase with sparsity level, because higher sparsity creates more simultaneous neuron removals and thus more pairwise and higher-order interaction terms that BCE's independent decomposition cannot model. A further open question is whether learned sparsity predictors trained on short calibration sequences generalize to long-context settings — SVD Contextual Sparsity Predictors (arXiv 2603.14110) explicitly found that learned predictors suffer from out-of-distribution sensitivity compared to weight-structure-based approaches, making long-context evaluation essential for any learned predictor method.\",\n  \"opportunity\": \"The landscape reveals four actionable opportunities. First, the composition question: SPON's static bias correction fixes average-case representational drift (input-independent) while contextual prediction handles per-input variation (input-dependent) — orthogonal mechanisms that should provide additive benefits. Note that IFPruning (arXiv 2501.02086) also combines quasi-static (instruction-level) and dynamic (input-level) sparsity, but through a fundamentally different mechanism: a 302M-parameter predictor that jointly fine-tunes the base LLM with cross-entropy loss, producing instruction-level masks (same mask for all tokens). Our composition is between an input-independent bias correction (zero overhead, folded into bias terms, applied to frozen models) and a lightweight token-level contextual predictor — a simpler, more modular, and post-training-compatible approach. If confirmed empirically, the SPON + contextual predictor composition becomes a practical recipe with a clear mechanistic explanation. Second, the training objective question: if a KL-trained predictor (no compensation) matches or exceeds the quality of FastForward's full BCE + compensation system, the practical benefit is substantial — a simpler inference pipeline with lower overhead. FastForward's compensation MLP adds ~8.0 MB of weights per layer (r'=d_model/8=512; 4,194,304 params in FP16) and associated GEMV operations at inference time — ~256 MB total across 32 layers; eliminating it simplifies deployment without sacrificing quality. This transforms the contribution from 'KL is slightly better than BCE' to 'KL training makes error compensation unnecessary.' Third, the formal mean-field analysis elevates the contribution from empirical observation to principled insight: we derive that BCE's per-neuron decomposition L_BCE = Σ_j l(y_j, s_j) is equivalent to optimizing under a mean-field factorized posterior over neuron importance, ignoring all pairwise and higher-order interaction terms. At sparsity level s, the number of simultaneously pruned neuron pairs scales as O(s²D²), so the approximation gap grows quadratically with sparsity — predicting that KL's advantage should be substantially larger at 50% than at 40% sparsity. This is a testable, falsifiable prediction that, if confirmed, provides actionable guidance for all future predictor design. Fourth, long-context generalization: learned sparsity predictors are trained on short calibration sequences, but deployed on inputs of arbitrary length. SVD Contextual Sparsity Predictors (arXiv 2603.14110) showed that learned predictors exhibit out-of-distribution sensitivity — our LongBench, RULER, and MT-Bench evaluation directly tests whether KL-trained predictors (which optimize for output-distribution preservation rather than per-neuron pattern matching) exhibit better generalization than BCE-trained ones, and whether SPON's static correction provides a context-length-invariant baseline that stabilizes long-context performance. RULER's synthetic tasks (needle-in-a-haystack retrieval, variable tracking, multi-hop tracing) at controlled context lengths (4K–128K) provide fine-grained diagnostics complementing LongBench's natural-language tasks — specifically, RULER can reveal whether sparsity disproportionately impairs precise retrieval capabilities (a failure mode that LongBench's aggregate task-level scores may mask). The contribution is fivefold: (1) the first empirical study of whether static bias correction (SPON) and contextual prediction compose additively for activation sparsity — the headline result; (2) a controlled four-condition ablation (BCE, BCE+compensation, KL, KL+compensation) testing whether KL training subsumes error compensation; (3) a formalized mean-field argument with the sparsity-level interaction prediction; (4) a systematic three-tier comparison (training-free, static-learned, contextual-learned) on native SwiGLU at decode time with honest wall-clock overhead reporting; and (5) long-context generalization evaluation testing whether learned predictors trained on short sequences maintain quality on LongBench tasks (4K–32K tokens) and RULER synthetic tasks (4K–32K tokens, with 13 tasks across Retrieval, Multi-hop Tracing, Aggregation, and QA), addressing a gap identified by recent work on predictor OOD sensitivity.\",\n  \"landscape\": \"Training-free activation sparsity on SwiGLU has rapidly progressed: WINA (ICLR 2026) achieves the training-free SOTA with weight-informed scoring and greedy per-layer sparsity allocation across both MLP and attention layers (with attention tolerating ~2.3× higher sparsity than MLP), reporting 59.57% average on Llama-3-8B at 50% model-level sparsity versus 66.38% dense; WAS (EMNLP 2025) achieves 60% model-level sparsity via weight-aware scoring with constrained Bayesian optimization; WiSparse (arXiv 2026) preserves 97% of dense performance at 50% sparsity via weight-aware mixed-granularity allocation; TEAL (ICLR 2025) achieves 40-50% sparsity with 1.5-1.8x speedup via magnitude pruning; R-Sparse (ICLR 2025) achieves 50% model-level sparsity via rank-aware input channel scoring; ActTail (arXiv 2026) uses Heavy-Tailed Self-Regularization for global sparsity allocation; DIP (MLSys 2025) achieves predictor-free dynamic pruning on SwiGLU at ~40% speedup plus LoRA adapters trained via logit-matching knowledge distillation (loss function unspecified in paper, likely KL) for accuracy recovery — the closest existing system combining distillation with sparsity, though critically it trains the LoRA recovery module with distillation rather than the sparsity predictor itself, and uses magnitude-based (not predicted) sparsity masks. On the learned side, SPON/Resting Neurons (arXiv 2512.12744v3, ICML 2026 per arXiv metadata updated on the April 30 notification date) injects learnable input-independent activation vectors trained via KL-divergence distillation, recovering ~1 point over WINA at 50% model-level sparsity on five QA benchmarks (ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande; 71.96 vs 70.97), with zero inference overhead since vectors fold into bias terms, training in ~1 hour on 4x A6000; SPON also reports perplexity on WikiText and validates cross-dataset generalization by calibrating on C4 while evaluating on WikiText. FastForward (arXiv 2602.00397, Jan 2026) trains a contextual predictor (single-head attention + 2-layer MLP, bottleneck r=d_model/16) with weighted BCE loss plus an error compensation network (2-layer MLP, r'=d_model/8=512) trained with MSE loss ||Y_dense − Y_sparse||², achieving MMLU 67.17 vs dense 67.84 at 50% FFN sparsity on Llama-3.1-8B — critically, the compensation network operates at inference time (not just training), adding ~8.0 MB per layer (4,194,304 params × 2 bytes FP16, ~256 MB total across 32 layers) in per-layer weight reads and compute overhead. FastForward targets prefill optimization and evaluates on LongBench (English tasks, 4K-32K tokens) achieving <6% accuracy loss at 50% FFN sparsity — demonstrating that their predictor generalizes beyond short training sequences via an attention-mixing mechanism, but requiring the compensation network for this generalization. IFPruning (arXiv 2501.02086, Jan 2025) trains a 302M-parameter sparsity predictor that combines instruction-level (quasi-static) and input-level (contextual) sparsity selection, jointly optimizing the predictor and LLM weights via cross-entropy loss. While IFPruning also composes static and contextual sparsity components, it operates at a fundamentally different granularity and setting: instruction-level masks (same mask for all tokens in a sequence) requiring task-description input, a large predictor (302M params vs our ~75.5M total), and joint LLM fine-tuning that modifies the base model — whereas our composition applies input-independent bias correction (zero overhead, folded into bias terms) with token-level contextual prediction, both post-training on frozen models. ShadowLLM (EMNLP 2024) trains single-hidden-layer predictors using MSE loss on per-neuron importance. Sirius (NeurIPS 2024) addresses quality degradation from contextual sparsity via periodic full-model correction every 16 tokens with speculative-decoding-style rollback, achieving 20-35% latency reduction — a complementary approach to our static+contextual composition since Sirius interleaves sparse and dense inference rather than composing learned correction mechanisms. Spark Transformer (NeurIPS 2025) reparameterizes existing FFN weights and attention key embeddings during pre-training (Gemma-2 recipe) to form implicit sparsity predictors with a hardware-friendly 'statistical top-k' linear-time approximate algorithm, achieving 2.5x FLOP reduction with 1.79x CPU / 1.40x GPU decode speedup and only 8% of FFN neurons activated — complementary to our post-training approach which works on frozen models without pre-training modification. ActiveFlow (arXiv 2025) combines cross-layer preloading with sparse-aware self-distillation using KL-divergence to adapt model weights (not predictor parameters) for on-device deployment, demonstrating that KL-based training recovers 2.64-10.21% accuracy over TEAL — further evidence that output-distribution distillation is effective for sparsity recovery, though applied to weight adaptation rather than predictor training. Polar Sparsity (NeurIPS 2025) trained BCE routers and evaluated on LongBench for instruction-tuned models, concluding MLP sparsity offers limited benefits on SwiGLU in batch-scaling scenarios — however, this was with activation-pattern prediction, not output-distribution alignment in low-batch decode; their long-context evaluation was limited to 16K tokens. MaskLLM (NeurIPS 2024 Spotlight) uses Gumbel Softmax for static 2:4 masks. SDMPrune (arXiv 2025) uses self-distillation for MLP weight pruning, not activation sparsity. SVD Contextual Sparsity Predictors (arXiv 2603.14110, Mar 2026) provide training-free predictors using truncated SVD of gate projections, targeting ReGLU-based models with high inherent sparsity — critically, they found that learned predictors suffer from out-of-distribution sensitivity on unseen data (ROC-AUC degrades on held-out sequences) while SVD predictors maintain robust performance by leveraging weight structure rather than data-dependent patterns. This OOD sensitivity finding directly motivates our LongBench and RULER evaluation: if learned predictors are fragile to distribution shift, their behavior on long-context tasks (absent from short calibration data) is an important empirical question. No prior work (a) trains the sparsity predictor itself with KL-divergence distillation, (b) tests whether SPON's static correction composes additively with contextual prediction in a post-training, frozen-model setting, (c) formally analyzes BCE's mean-field limitation and its interaction with sparsity level, or (d) evaluates whether KL-trained predictors generalize better than BCE-trained ones on long-context tasks using both natural (LongBench) and synthetic (RULER) benchmarks.\",\n  \"approach\": \"We study the composition of two learned correction mechanisms for activation sparsity — static bias correction and contextual prediction — trained via output-distribution distillation (KL divergence) on native SwiGLU LLMs at decode time, with a controlled four-condition ablation testing whether KL training subsumes error compensation. For each SwiGLU MLP block in Llama 3.1 8B (32 layers, d_model=4096, intermediate_size=14336), we attach a low-rank predictor that maps the layer input hidden state h ∈ R^d to a continuous sparsity score over the intermediate dimension D via two linear projections: h → W_down (4096 × 128) → ReLU → W_up (128 × 14336), yielding ~2.36M parameters per layer (~75.5M total, <1% of 8B model). Architecture is fixed at rank r=128 (no rank sweep, following reviewer guidance to narrow scope). During training, scores are converted to differentiable binary masks via Gumbel-sigmoid relaxation with temperature annealing (τ: 5 → 0.1). The primary training loss is: L = KL(p_dense || p_sparse) + λ_mse · MSE(h_dense_l, h_sparse_l) + λ_sparse · max(0, s − s_target), where KL divergence on output logits is the primary signal (capturing joint neuron interactions through end-to-end gradient flow via ∂L_KL/∂θ = ∂L_KL/∂p_sparse · ∂p_sparse/∂h_out · ∂h_out/∂m · ∂m/∂θ), per-layer MSE provides gradient signal for early layers, and the sparsity penalty enforces target model-level sparsity s_target = 0.5. Only predictor parameters are updated during ~1K gradient steps on SlimPajama calibration data with the base LLM frozen. MLP/attention sparsity allocation: We follow WINA's greedy per-layer allocation algorithm (originally from TEAL) to distribute the 50% global FLOPs budget across all layers. This algorithm iteratively increases sparsity in the least-sensitive layer (measured by calibration perplexity impact) until the aggregate meets the global target. WINA found that attention layers tolerate ~2.3× higher sparsity than MLP layers, so the allocation typically assigns ~55-65% sparsity to attention layers and ~40-50% to MLP layers, though the exact per-layer ratios are determined by the calibration-based optimization. Within MLP layers, our contextual predictor replaces WINA's heuristic scoring to determine which neurons to activate; within attention layers, WINA's original weight-informed scoring is used unchanged. We report both the global model-level sparsity (50%) and the effective per-component (MLP, attention) sparsity ratios resulting from the allocation, ensuring transparent comparison with baselines that may use different allocation strategies. At inference, the predictor produces a binary mask via top-k selection, and the sparse SwiGLU forward pass skips columns of gate/up projections and rows of the down projection using Triton sparse GEMV kernels from the TEAL/WINA codebases. Predictor overhead — FLOPs and wall-clock (honest reporting): Each predictor adds ~4.72M FLOPs per layer (two GEMVs of 4096×128 and 128×14336) versus ~176M FLOPs saved at 50% MLP sparsity — a ~37:1 FLOPs ratio. However, batch=1 decode is memory-bandwidth-bound, not compute-bound. On H100 (3.35 TB/s peak HBM bandwidth), the small predictor GEMVs achieve only ~100 GB/s effective bandwidth due to low matrix occupancy and kernel launch overhead, yielding ~0.047 ms per layer or ~1.5 ms total predictor overhead across 32 layers. The larger FFN matrices being skipped achieve ~500 GB/s effective bandwidth, yielding ~0.35 ms savings per layer or ~11.3 ms total savings. The realistic wall-clock savings-to-overhead ratio is approximately 4-8:1 — still attractive for decode acceleration, but substantially lower than the 37:1 FLOPs ratio. We report both metrics throughout to avoid misleading claims. Four-condition ablation (the key experimental design addition): (a) BCE only — our predictor architecture trained with weighted BCE loss (FastForward-style exponential weighting), no compensation; (b) BCE + error compensation — same BCE predictor plus FastForward's 2-layer compensation MLP (r'=d_model/8=512, adding ~8.0 MB per layer: W_comp1 ∈ R^{4096×512} + W_comp2 ∈ R^{512×4096} = 4,194,304 params × 2 bytes FP16), trained with MSE loss ||Y_dense − (Y_sparse + g_φ(h))||², with compensation network active at inference time; (c) KL only — our predictor trained with KL-divergence loss, no compensation; (d) KL + error compensation — if time permits. Condition (b) is critical: it replicates FastForward's full approach (BCE + compensation) rather than testing BCE in isolation, ensuring a fair comparison. If KL-only (c) matches or exceeds BCE+compensation (b), the finding is that KL training makes error compensation unnecessary — yielding a simpler system with lower inference overhead (eliminating ~256 MB of compensation weights and associated compute across 32 layers). Evaluation benchmarks (aligned with user requirements): (1) Perplexity on WikiText-2 and C4 — standard for sparsity papers, reported by SPON and most training-free baselines, trivial to compute; (2) ARC-Challenge — science reasoning; (3) WinoGrande — coreference resolution; (4) MMLU — multitask knowledge; (5) GSM8K — mathematical reasoning; (6) HumanEval — code generation; (7) MT-Bench — multi-turn instruction-following quality under sparsity, evaluated using GPT-4 as judge (80 questions, 8 categories), testing whether sparsity disproportionately degrades open-ended generation; (8) LongBench (English subset) — long-context evaluation (4K-32K tokens) testing predictor generalization beyond training distribution, directly comparable to FastForward's LongBench results; (9) RULER (COLM 2024) — synthetic long-context evaluation with 13 tasks across 4 categories (Retrieval including needle-in-a-haystack variants with single/multi-key/multi-value/multi-query needles, Multi-hop Tracing via variable tracking, Aggregation via common/frequent word extraction, and QA based on SQuAD/HotpotQA) at controlled context lengths (4K, 8K, 16K, 32K), using 500 examples per task with recall-based accuracy scoring. RULER complements LongBench by providing fine-grained diagnostics: its synthetic tasks isolate specific capabilities (precise retrieval, multi-hop reasoning, information aggregation) that LongBench's natural-language aggregate scores may mask. If sparsity disproportionately impairs retrieval accuracy (needle-in-a-haystack) while preserving summarization quality, RULER will reveal this while LongBench may not. We evaluate RULER at 4K-32K to match our LongBench context range; extending to 64K-128K is feasible but deferred to keep scope manageable given Llama 3.1 8B's 128K context window. This benchmark set covers all user-required evaluation axes: perplexity, knowledge/reasoning (MMLU, ARC-c, GSM8K), code (HumanEval), long-context (LongBench, RULER), and instruction-following (MT-Bench). Long-context generalization: The predictor is trained on SlimPajama calibration sequences (typically 2048 tokens). LongBench tasks require processing 4K-32K token inputs, and RULER provides controlled synthetic tasks at the same context lengths, testing whether learned neuron importance patterns generalize beyond the training context length. SVD Contextual Sparsity Predictors (arXiv 2603.14110) found that learned predictors suffer OOD sensitivity on unseen data, making this a plausible failure mode. If long-context performance degrades disproportionately, this is itself a finding — motivating context-length-aware predictor training or hybrid approaches where static SPON correction (which is context-length-invariant by construction) provides a robust baseline while contextual prediction adapts to input-specific patterns. RULER's task-level granularity adds diagnostic value: if KL-trained predictors maintain retrieval accuracy (NIAH tasks) while BCE-trained predictors degrade, this provides evidence that output-distribution alignment preserves retrieval-critical neuron activation patterns that per-neuron BCE misses — connecting the mean-field hypothesis to a specific, interpretable capability. FastForward reports their predictor generalizes to LongBench via an attention-mixing mechanism; our four-condition ablation will reveal whether KL-trained predictors (which optimize output-distribution preservation) exhibit different generalization characteristics than BCE-trained ones (which optimize per-neuron pattern accuracy). Experiments focus on Llama 3.1 8B at 50% model-level sparsity as the primary operating point. For the KL-BCE sparsity interaction test, we additionally train KL and BCE predictors at 40% model-level sparsity (2 extra training runs) to test the mean-field prediction that KL's advantage over BCE grows with sparsity level. All other baselines and the composition experiment are evaluated at 50% only, saving ~3-4 days versus evaluating at both levels. Baselines use consistent model-level sparsity: training-free baselines are WINA, TEAL, and R-Sparse; learned baselines are SPON (reimplemented — bias vectors + KL training, architecturally trivial, validated by reproducing Table 2 numbers on Llama 3 8B before evaluating on Llama 3.1 8B) and the four-condition ablation above. Key experiments ordered by importance: (1) SPON + KL predictor composition (headline): apply SPON bias correction AND contextual KL prediction simultaneously, testing whether static correction (fixing average-case drift) and contextual prediction (handling per-input variation) provide additive benefits. (2) KL-only vs BCE+compensation: the critical test of whether end-to-end KL training subsumes the need for error compensation — if confirmed, this is the key practical recommendation (eliminating ~256 MB of compensation weights and per-layer GEMV overhead). (3) KL vs BCE sparsity-level interaction: testing at both 40% and 50% whether KL's advantage over BCE (both without compensation) grows with sparsity, confirming the mean-field prediction. (4) Three-tier comparison: training-free (WINA, TEAL, R-Sparse) vs static-learned (SPON) vs contextual-learned (ours), establishing marginal value of each tier. (5) Long-context generalization: LongBench and RULER evaluation across all conditions, testing whether KL-trained predictors generalize better than BCE-trained ones to long contexts, and whether SPON's static correction stabilizes long-context performance. RULER's per-task breakdown provides diagnostic insight into which capabilities (retrieval, tracing, aggregation) are most affected by sparsity and which benefit most from KL vs BCE training. (6) Per-task analysis: decompose improvements by benchmark type (perplexity vs knowledge/reasoning vs code vs long-context vs instruction-following). Improvement target: 1.5-3 points average recovery over WINA at 50% model-level sparsity (WINA baseline: 59.57 on 6 benchmarks), conservatively grounded in: SPON's ~1 point static recovery (verified on five QA benchmarks), contextual KL prediction contributing an estimated 0.5-1.5 points (conservative — FastForward's near-dense MMLU quality was achieved at FFN-only sparsity with error compensation, a less aggressive operating point than our model-level sparsity without compensation), and a potential 0-0.5 point composition bonus. The 1.5-3 point range is arithmetically consistent: 1 (SPON) + 0.5-1.5 (contextual) + 0-0.5 (composition) = 1.5-3 points total. Explicit fallbacks: (A) If composition shows no additive benefit (SPON + predictor ≈ predictor alone), the contribution becomes the finding that contextual prediction subsumes static correction. (B) If KL-only does not beat BCE+compensation, the contribution pivots to the formalized mean-field analysis + three-tier comparison with the finding that error compensation remains necessary, but KL should be used in conjunction. (C) If KL does not outperform BCE at any sparsity level, the contribution becomes the rigorous negative result plus the composition study. (D) If long-context performance degrades substantially, the contribution includes the finding that predictor-based sparsity requires context-length-aware training, with SPON's static correction serving as a context-length-invariant safety net.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~68-95h H100\",\n      \"gpu_utilization\": \"Low (~15-25%)\",\n      \"timeline\": \"3-4 weeks (including paper writing)\",\n      \"team\": \"1 ML researcher\",\n      \"estimated_gpu_cost\": \"$170-240\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~68-105h H100\",\n      \"gpu_utilization\": \"Moderate (~40-55%)\",\n      \"timeline\": \"2.5-3 weeks (including paper writing)\",\n      \"team\": \"1 researcher, ~30min/day review\",\n      \"claude_api_cost\": \"$60-110\",\n      \"estimated_gpu_cost\": \"$170-265\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~102-160h H100 (predictor at r=128, 50% model-level sparsity primary, 40% for KL-BCE interaction only, four-condition ablation [BCE, BCE+comp, KL, KL+comp], SPON reimplementation + validation, SPON+predictor composition, all evaluations across 9 benchmarks including LongBench long-context, RULER synthetic long-context, and MT-Bench instruction-following, wall-clock profiling)\",\n      \"gpu_utilization\": \"High (~80-90%)\",\n      \"timeline\": \"14 days total with 2-4 H100s running concurrently: Days 1-2: codebase scaffolding, SPON validation, MT-Bench/LongBench/RULER evaluation pipeline setup (RULER uses NVIDIA's open-source codebase at github.com/NVIDIA/RULER, minimal integration effort). Days 3-6: train 4 ablation conditions at 50% + 2 interaction runs at 40%. Days 7-9: SPON+KL composition, all evaluations including perplexity (WikiText-2, C4), discriminative benchmarks (ARC-c, WinoGrande, MMLU, GSM8K, HumanEval), LongBench (English subset, 4K-32K tokens), RULER (13 tasks × 4 context lengths [4K-32K] × 500 examples, deterministic scoring — adds ~2-3h GPU time), MT-Bench (80 multi-turn questions with GPT-4 judge). Days 10-11: wall-clock profiling, long-context analysis, RULER per-task breakdown, figure generation. Days 12-14: paper writing with auto assistance — feasible for May 25 ARR deadline. Note: LongBench evaluation on long sequences at batch=1 decode adds ~8-12h of GPU time; MT-Bench adds ~2-3h including judge API calls; RULER adds ~2-3h (lightweight synthetic evaluation with deterministic scoring).\",\n      \"team\": \"0 (initial 2-4h setup for codebase scaffolding and GPU provisioning)\",\n      \"claude_api_cost\": \"$160-270\",\n      \"estimated_gpu_cost\": \"$255-400\",\n      \"speed_bottleneck\": \"Single-GPU training on 8B model; LongBench evaluation on long sequences (4K-32K tokens) at batch=1 decode is the primary bottleneck. RULER evaluation is lightweight (synthetic data, deterministic scoring, ~2-3h). Narrowing to 50% primary sparsity (40% only for 2 interaction runs) and dropping rank sweep saves ~40% versus earlier proposals. Explicit 3-day paper writing buffer prevents timeline overrun.\",\n      \"risk_note\": \"Timeline is tight with 14 days remaining. Primary execution risk: validating SPON reimplementation (must reproduce published Llama-3-8B Table 2 numbers on QA benchmarks before proceeding). Mitigation: SPON is architecturally trivial (bias vectors + standard KL training, ~1 hour on 4× A6000). Secondary risk: LongBench evaluation time on long sequences — mitigated by selecting the English-language subset (matching FastForward's evaluation protocol) and parallelizing evaluation across GPUs. Tertiary risk: MT-Bench requires GPT-4 judge API calls — mitigated by low cost (~$5-10 for 80 questions × multiple configurations) and fast turnaround. Quaternary risk: implementing FastForward's compensation MLP for the ablation — mitigated by simple 2-layer MLP architecture (d_model → d_model/8 → d_model with MSE loss). Quinary risk: Triton sparse kernel integration — mitigated by using existing TEAL/WINA kernel codebases. RULER risk: minimal — NVIDIA provides an open-source evaluation codebase (github.com/NVIDIA/RULER), and the synthetic evaluation is computationally lightweight with deterministic scoring. Fallback plan: if SPON reproduction takes >2 days, use SPON's published numbers on the QA subset and note the benchmark-set difference. If LongBench evaluation runs over schedule, prioritize single-document QA and summarization subtasks. If RULER evaluation extends beyond budget, evaluate at 4K and 16K context lengths only (2 of 4 planned lengths). Paper writing risk: 3 days allocated; structure and related work can be drafted in parallel with experiments.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time (ICML 2023)\",\n    \"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models (COLM 2024)\",\n    \"RULER: What's the Real Context Size of Your Long-Context Language Models? (COLM 2024, arXiv 2404.06654)\",\n    \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models (NeurIPS 2024 Spotlight)\",\n    \"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models (EMNLP 2024)\",\n    \"Sirius: Contextual Sparsity with Correction for Efficient LLMs (NeurIPS 2024)\",\n    \"Instruction-Following Pruning for Large Language Models (IFPruning, arXiv 2501.02086, Jan 2025)\",\n    \"TEAL: Training-Free Activation Sparsity in Large Language Models (ICLR 2025)\",\n    \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference (ICLR 2025)\",\n    \"DaSS: Dependency-Aware Semi-Structured Sparsity of GLU Variants in Large Language Models (TMLR 2025)\",\n    \"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking (DIP, MLSys 2025)\",\n    \"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity (ICML 2025)\",\n    \"WAS: Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling (EMNLP 2025)\",\n    \"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity (NeurIPS 2025)\",\n    \"Spark Transformer: Reactivating Sparsity in FFN and Attention (NeurIPS 2025)\",\n    \"Scaling Up On-Device LLMs via Active-Weight Swapping Between DRAM and Flash (ActiveFlow, arXiv 2504.08378)\",\n    \"Resting Neurons, Active Insights (SPON): Improving Input Sparsification for Large Language Models (ICML 2026 per arXiv metadata, arXiv 2512.12744v3)\",\n    \"FastForward: Accelerating LLM Prefill with Predictive FFN Sparsity (arXiv 2602.00397, Jan 2026)\",\n    \"WINA: Weight Informed Neuron Activation for Accelerating Large Language Model Inference (ICLR 2026)\",\n    \"WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity (arXiv 2026)\",\n    \"ActTail: Global Activation Sparsity in Large Language Models (arXiv 2026)\",\n    \"SVD Contextual Sparsity Predictors for Fast LLM Inference (arXiv 2603.14110, Mar 2026)\"\n  ],\n  \"description\": \"We study whether two learned correction mechanisms for activation sparsity — static bias correction and contextual prediction — address orthogonal failure modes and compose additively when both are trained via output-distribution distillation, and whether KL-divergence training for the contextual predictor subsumes the need for error compensation networks. The activation sparsity landscape has stratified into three tiers: training-free heuristics (WINA, TEAL, R-Sparse) achieving 59.57% average on Llama-3-8B at 50% model-level sparsity versus 66.38% dense (6.81-point gap); static learned correction (SPON, ICML 2026 per arXiv metadata) training input-independent bias vectors via KL-distillation, recovering ~1 point on five QA benchmarks at zero overhead; and contextual learned prediction (FastForward, arXiv 2026) training input-dependent predictors with weighted BCE plus an inference-time error compensation MLP adding ~8.0 MB per layer (~256 MB total across 32 layers). IFPruning (arXiv 2501.02086) co-trains a 302M-parameter predictor combining instruction-level (quasi-static) and input-level sparsity with cross-entropy loss, but requires task-description input, modifies the base LLM, and operates at instruction-level granularity (same mask for all tokens). Our composition is between an input-independent bias correction (zero overhead, folded into bias terms) and a lightweight token-level contextual predictor, both applied post-training to frozen models — a simpler, more modular approach. No prior work combines contextual prediction with KL-divergence distillation for the predictor itself, tests static+contextual composition in a post-training frozen-model setting, formally analyzes why BCE's per-neuron objective requires error compensation, or evaluates whether KL-trained predictors generalize better than BCE-trained ones to long-context settings. Our key theoretical contribution formalizes BCE's limitation as a mean-field factorization: L_BCE = Σ_j l(y_j, s_j) treats neuron activation decisions as independent, ignoring joint interaction effects that grow quadratically with sparsity level O(s²D²). KL divergence on output logits captures these interactions through end-to-end gradient flow (∂h_out/∂m couples all mask decisions), yielding a testable prediction: KL's advantage over BCE grows with sparsity. We test this with a controlled four-condition ablation (BCE-only, BCE+compensation, KL-only, KL+compensation) — the critical test being whether KL-only matches BCE+compensation, which would mean KL training makes error compensation unnecessary (simpler system, ~256 MB less inference overhead). Each rank-128 predictor (~2.36M params per layer, <1% of model) maps layer inputs to neuron masks via Gumbel-sigmoid relaxation. MLP/attention sparsity allocation follows WINA's greedy per-layer algorithm: at 50% global FLOPs budget, attention layers receive ~55-65% sparsity while MLP layers receive ~40-50%, with exact per-layer ratios determined by calibration-based optimization; we report both global and per-component effective sparsity. We report both FLOPs (37:1 savings-to-overhead ratio) and honest wall-clock estimates for batch=1 decode on H100 (~4-8:1, accounting for the fact that small predictor GEMVs achieve ~100 GB/s effective bandwidth versus ~500 GB/s for the larger FFN matrices being skipped, yielding ~1.5 ms total predictor overhead versus ~11.3 ms savings across 32 layers). Evaluation covers all user-required axes: perplexity (WikiText-2, C4), discriminative benchmarks (ARC-c, WinoGrande, MMLU, GSM8K), code generation (HumanEval), long-context generalization (LongBench English subset, 4K-32K tokens — directly comparable to FastForward's evaluation and testing whether learned predictors trained on short SlimPajama sequences generalize, given SVD Contextual Sparsity Predictors' finding that learned predictors exhibit OOD sensitivity), synthetic long-context diagnostics (RULER, COLM 2024 — 13 tasks across Retrieval, Multi-hop Tracing, Aggregation, and QA categories at 4K-32K context lengths, providing fine-grained capability-level diagnostics that complement LongBench's aggregate scores, particularly testing whether sparsity disproportionately impairs precise retrieval vs. summarization), and instruction-following (MT-Bench with GPT-4 judge). Key experiments: (1) SPON + KL predictor composition testing additive benefits (headline), (2) KL-only vs BCE+compensation testing whether KL subsumes error compensation, (3) KL vs BCE at 40% and 50% sparsity testing the mean-field interaction prediction, (4) three-tier comparison with consistent model-level sparsity definitions, (5) long-context generalization across all conditions on LongBench and RULER, with RULER per-task breakdown revealing which capabilities (retrieval, tracing, aggregation) are most affected by sparsity. Target: conservative 1.5-3 points recovery over WINA at 50% model-level sparsity (grounded in: SPON ~1 point verified, contextual 0.5-1.5 points conservative given model-level sparsity is harder than FastForward's FFN-only operating point, composition 0-0.5 points). Evaluated on Llama 3.1 8B at 50% model-level sparsity (with 40% for KL-BCE interaction test only). Scoped for EMNLP 2026 ARR deadline (May 25, 2026) with explicit 3-day paper writing buffer.\",\n  \"project_name\": \"distill_sparse_swiglu\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"FACTUAL ERROR: ShadowLLM is claimed to 'target ReLU models' but it actually evaluates on Llama-2-7B (SwiGLU architecture) alongside OPT models. The landscape claim that 'no predictor-based approach targets SwiGLU' is inaccurate.\", \"MISSING COMPETITORS: Several important SwiGLU activation sparsity papers are omitted from the landscape: (1) CHESS (EMNLP 2024) — channel-wise thresholding on SwiGLU models with 1.27x speedup; (2) La RoSA (ICML 2025) — training-free rotated sparse activation achieving 40% sparsity with 1.30x speedup, outperforming TEAL; (3) SCAP (NeurIPS 2024 Workshop) — post-training calibration achieving 48.5% FFN sparsity; (4) MaskLLM (NeurIPS 2024 Spotlight) — Gumbel-based learnable masks on SwiGLU LLMs (N:M sparsity).\", \"AGGRESSIVE SPARSITY TARGET: No existing work on native SwiGLU models (without ReLUfication) has demonstrated >50% MLP sparsity without significant accuracy loss. The claimed 60-70% would be a 20-30 percentage point improvement over TEAL with no evidence this is achievable. The SVD predictor paper achieving 90% sparsity works only on ReLUfied models (ProSparse, TurboSparse), not native SwiGLU.\", \"TIMELINE INFEASIBILITY: 16 days vs. the generator's own 3-4 month manual estimate. Custom CUDA kernel development alone typically takes weeks. Even the auto_research mode estimates 2-3 weeks with 4-8 concurrent H100s, and flags CUDA correctness as highest risk.\", \"PREDICTOR OVERHEAD NOT ANALYZED: A 15M-parameter predictor per block × 32 layers = ~480M total additional parameters requiring forward passes. This adds latency that could significantly eat into the sparsity-based speedup, especially for small batch sizes where decode is already memory-bound. No analysis of predictor inference cost vs. sparsity savings is provided.\", \"BATCH-SIZE SCALABILITY CONCERN: Polar Sparsity (NeurIPS 2025) showed that MLP neuron sparsity patterns lose their advantage at realistic batch sizes because the union of active neurons across tokens quickly approaches the full dense set. The proposed method's exclusive focus on MLP blocks may yield minimal real-world speedup in production serving settings.\", \"SPEEDUP CLAIMS ARE SPECULATIVE: The projected 1.8-2.5x decode speedup is stated without any basis — it depends entirely on unwritten CUDA kernel quality and assumes predictor overhead is negligible, neither of which can be assumed.\", \"'Architecture-generic' claim is unsupported: Transferability across Qwen 2.5 and Llama 3.1/3.3 model families without architecture-specific tuning is a strong claim requiring empirical evidence. Different models have different hidden/intermediate dimensions and activation patterns.\"]\nFeedback: The core direction (distillation-trained sparsity predictors for SwiGLU MLP) has merit but needs significant corrections: (1) Fix the ShadowLLM mischaracterization — it does work on SwiGLU models, so reframe the novelty as 'distillation-based predictor training for higher sparsity ratios' rather than 'first predictor for SwiGLU.' (2) Add CHESS, La RoSA, SCAP, and MaskLLM to the landscape analysis. (3) Lower the sparsity target to 50-60% and provide theoretical or empirical justification for why distillation would improve over training-free baselines beyond the ~50% plateau. (4) Address the Polar Sparsity batch-size scalability concern — either target single-request/edge deployment explicitly, or show how predictor-based sparsity maintains advantage at batch sizes >1. (5) Critically, address the CUDA kernel bottleneck: consider reusing existing sparse kernels from TEAL/R-Sparse/DIP rather than writing custom gather-scatter kernels from scratch, or use Triton for faster development. (6) Add a predictor overhead analysis showing that the per-layer predictor forward pass cost is small relative to the savings from skipping neurons. (7) For the 16-day timeline, scope down: pick one model family (e.g., Llama 3.1 8B/70B), reuse existing sparse execution infrastructure, and target 50-55% MLP sparsity as the primary result.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"VENUE MISMATCH (Critical): The user explicitly targets EMNLP 2026 (ARR deadline May 25, 2026, 14 days away), but the generator lists target_venues as AAAI 2027, ICLR 2027, MLSys 2027, EMNLP 2027. The generator's own manual timeline is 2-3 months and auto is 2-3 weeks — neither fits the 14-day constraint. This is a direct failure to meet the user's stated requirements.\", \"SPARSITY TARGET CONTRADICTED BY EVIDENCE: WINA at 65% model-level sparsity on Llama-3-8B shows catastrophic accuracy loss (MMLU drops to 38.48 from ~60+ dense, GSM8K drops to 7.05). Literature indicates native SwiGLU models can only be pruned to ~50% before >1% MMLU degradation. The claim of 70-75% MLP sparsity with ≤1% accuracy loss has no supporting evidence and contradicts all existing benchmarks.\", \"POLAR SPARSITY DIRECTLY CONTRADICTS CORE PREMISE: Polar Sparsity (NeurIPS 2025) uses a nearly identical architecture (two-layer feedforward router, hidden=1024) but explicitly states that for non-ReLU architectures (SwiGLU), 'only attention head sparsity is applied since MLP sparsification becomes ineffective.' The proposal does not explain why its KL-distillation trained predictor would succeed where Polar Sparsity's learned router failed on SwiGLU MLP.\", \"MISSING COMPETITORS: (1) ActTail (arXiv March 2026) — training-free global sparsity allocation using Heavy-Tailed Self-Regularization theory, achieves 21.8% perplexity reduction at 80% sparsity on Llama-2-7B; (2) MGLU/Masked Gated Linear Unit (arXiv June 2025) — learns binary masks within the GLU structure itself, achieving comparable accuracy to SwiGLU with memory advantages; (3) DaSS (TMLR 2025) — dependency-aware semi-structured sparsity specifically designed for GLU variants including SwiGLU.\", \"INCREMENTAL NOVELTY vs. ShadowLLM: ShadowLLM already trains learned predictors on Llama-2 (a SwiGLU architecture), achieving 15% accuracy improvement over heuristic methods. The proposed method differs primarily in: (a) using KL divergence instead of MSE importance regression, (b) Gumbel-sigmoid instead of direct thresholding, (c) low-rank architecture instead of single-hidden-layer MLP. These are engineering variations of an established approach, not a paradigm shift.\", \"70B COMPUTE FEASIBILITY QUESTIONABLE: Training predictors on Llama 3.1 70B requires 4+ H100s for model parallelism. Forward passes through the full dense 70B model for KL divergence computation at each training step are expensive. MaskLLM required 1,280 A100-GPU-hours for just 7B with static masks. The claim of covering both 8B and 70B within 200 H100-hours needs more rigorous justification.\"]\nFeedback: The revision addressed several Round 1 issues well (ShadowLLM characterization, kernel reuse, batch=1 scope, predictor overhead analysis), but critical problems remain: (1) **Target EMNLP 2026**: The generator must either genuinely target EMNLP 2026 with a 14-day feasible scope, or the idea fails the user's venue requirement. For a 14-day submission, scope to Llama 3.1 8B only, 50-60% MLP sparsity, and frame as 'quality improvement at same sparsity' rather than pushing to 70-75%. (2) **Reframe the contribution**: The evidence strongly suggests 70-75% MLP sparsity on native SwiGLU with ≤1% loss is unachievable. Instead, target 50-60% MLP sparsity and show that KL-distillation trained predictors achieve *better accuracy* than WINA/WAS/TEAL at the *same* sparsity level — this is what ShadowLLM demonstrated (15% accuracy improvement). This is a credible and publishable contribution. (3) **Directly address Polar Sparsity's finding**: Explain mechanistically why a KL-distillation trained predictor could extract useful MLP sparsity on SwiGLU when Polar Sparsity's BCE-trained router could not — or position the work as complementary (MLP at batch=1 + attention at batch>1). (4) **Add ActTail, MGLU, and DaSS** to landscape. (5) **Provide a concrete fallback**: If distillation doesn't push beyond training-free ceiling, the contribution is still the distillation framework + analysis of when learned predictors outperform heuristics. Make this explicit in the paper framing.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING COMPETITOR — FastForward (arXiv:2602.00397, Jan 2026): Trains a neural predictor (single-head attention + 2-layer MLP, bottleneck r=d_model/16) for FFN sparsity on SwiGLU models (LLaMA-3.1/3.2-1B/3B/8B, Qwen3-4B). Uses weighted BCE loss with exponential decay on positive neurons plus a separate error compensation network. Achieves 50% FFN sparsity with 1.45x prefill speedup and <1 point MMLU drop. This is the closest existing work to the proposal — it trains learned predictors on SwiGLU — and is not cited anywhere in the landscape.\", \"CRITICAL MISSING COMPETITOR — SPON/Resting Neurons (arXiv:2512.12744, ICML 2026): Uses the exact same KL-divergence distillation loss the proposal claims as its key innovation, applied to SwiGLU models (Llama-3-8B, Mistral-7B, Qwen3-8B/32B, Llama-3-70B). At 50% sparsity on Llama3-8B, SPON achieves 71.96 avg (vs WINA 70.97) — a ~1 point recovery. Critically, SPON has zero inference overhead (absorbed into bias) and trains in ~1 GPU-hour. While SPON uses static vectors rather than contextual predictors, it directly undermines the novelty claim of 'first to use KL-distillation for SwiGLU sparsity' and sets a very efficient baseline.\", \"UNSUPPORTED IMPROVEMENT TARGET: The proposal claims to recover '3-5 points of WINA's 6.8-point average drop at 50% sparsity,' but provides no empirical or theoretical evidence for this target. SPON — which uses the same KL-divergence loss — only recovers ~1 point at 50%. ShadowLLM's '15% improvement' was measured against DejaVu (2023 baseline), not against WINA-caliber 2025-2026 methods. The 3-5 point claim needs either preliminary experimental evidence or a principled argument for why contextual prediction unlocks significantly more recovery than static correction.\", \"TIMELINE CONTRADICTION: The generator's own manual estimate is '4-6 weeks' and auto_research is '10-14 days with 2-4 H100s.' Only 13 days remain until the May 25 ARR deadline. The manual estimate directly contradicts the claimed feasibility. For auto_research, the '10-14 days' estimate assumes continuous GPU availability and zero debugging setbacks — highly optimistic for a novel training paradigm.\", \"MISSING COMPETITOR — Spark Transformer (NeurIPS 2025): Reparameterizes existing FFN weights to form a low-cost predictor for identifying activated entries, achieving 2.5x FLOP reduction with 1.79x CPU / 1.40x GPU decoding speedup. Relevant as a training-free predictor approach that should be discussed in the landscape.\", \"POLAR SPARSITY CHARACTERIZATION STILL SLIGHTLY INACCURATE: The proposal quotes Polar Sparsity as concluding MLP sparsification is 'ineffective' on SwiGLU. The actual paper states SwiGLU 'yields denser activations and limits the benefits of sparsity' and 'MLP layers offer limited benefits' — 'limited' is not 'ineffective.' The distinction matters because 'limited benefits' is actually consistent with SPON's finding of ~1 point improvement, undermining the proposal's framing that Polar Sparsity's conclusion is wrong due to BCE training.\", \"BASELINE CODE AVAILABILITY RISK: WAS (EMNLP 2025), WiSparse (arXiv Feb 2026), and ActTail (arXiv Feb 2026) have no confirmed public code repositories. Reproducing three baselines from papers within 13 days adds significant risk. The proposal should either confirm code availability or reduce the baseline set to methods with verified code (TEAL, WINA, R-Sparse, ShadowLLM).\"]\nFeedback: The proposal has improved substantially from Round 2 — venue targeting, sparsity scope, kernel reuse, and fallback strategy are all addressed. However, two critical omissions must be fixed before this can pass:\n\n(1) **Add FastForward and SPON as baselines and discuss them in the landscape.** FastForward is the closest direct competitor (trained predictor on SwiGLU); SPON uses the same KL-distillation loss on SwiGLU. The proposal must explain: (a) how it differs from FastForward (KL vs weighted BCE, decode vs prefill, contextual masks vs block-level prediction + error compensator), and (b) why contextual KL-trained predictors should recover significantly more accuracy than SPON's static KL-trained bias correction. Consider proposing a SPON + your predictor combination as an experiment.\n\n(2) **Revise the improvement target with evidence.** '3-5 points' is not supported. Given that SPON recovers ~1 point with KL-distillation (static) and FastForward shows <1 point MMLU drop at 50% with BCE-trained predictors, the expected improvement is likely 1-3 points over training-free WINA, not 3-5. Either lower the target or provide a principled argument (e.g., analysis of input-dependent importance variance showing that contextual prediction captures significantly more information than static correction).\n\n(3) **Resolve the timeline.** Either (a) acknowledge this requires auto_research mode with 2-4 concurrent H100s and high execution risk, or (b) scope down further: drop baselines without public code (keep TEAL, WINA, R-Sparse, ShadowLLM as the 4 training-free baselines + add SPON and FastForward as the 2 learned baselines), and start paper writing immediately with placeholder results.\n\n(4) **Reframe novelty more precisely.** The novelty is NOT 'first KL-distillation for SwiGLU sparsity' (SPON does this) or 'first trained predictor for SwiGLU' (FastForward does this). The novelty is 'first contextual predictor trained via output-distribution distillation (KL) rather than activation-pattern prediction (BCE/MSE) on SwiGLU, with systematic comparison against both training-free and learned baselines using 2025-2026 SOTA.' This is more honest and still publishable if results support it.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"SPARSITY DEFINITION INCONSISTENCY: The proposal targets '50% MLP sparsity' but cites SPON's Table 2 numbers (WINA 70.97, SPON 71.96) which are at 50% model-level activation sparsity (MLP + attention layers combined). These are different operating points — 50% MLP-only sparsity is less aggressive than 50% model-level sparsity. The improvement targets and baseline comparisons must use consistent sparsity definitions, or the claimed gaps are misleading.\", \"DENSE BASELINE NOT VERIFIED: The proposal claims 'the dense model's ~74.5' average on QA tasks, but the SPON paper's Table 2 (where the WINA 70.97 number comes from) does NOT include dense baselines. The ~74.5 figure appears to be estimated/unverified. The actual dense-to-sparse gap that the contextual predictor must close is uncertain from the cited data.\", \"IMPROVEMENT TARGET ARITHMETIC: The proposal claims '1.5-3 points total recovery over WINA' with '0.5-1.5 points from the contextual component over SPON.' SPON recovers ~1 point over WINA. So the total would be 1.5-2.5 points (1 from SPON + 0.5-1.5 from contextual). The upper bound of 3 points requires the contextual component to contribute 2 points, exceeding the stated 0.5-1.5 range. Minor inconsistency but undermines rigor.\", \"NO THEORETICAL ARGUMENT FOR KL > BCE IN CONTEXTUAL SETTING: The core hypothesis — that KL-trained contextual predictors outperform BCE-trained contextual predictors — lacks theoretical grounding. The proposal states KL 'captures cross-layer interaction effects on output distributions,' but doesn't explain why BCE-trained predictors can't learn equivalent masks through gradient flow. FastForward's error compensation network already addresses output quality post-hoc. The proposal needs at least an intuitive argument for why optimizing for output distributions directly (KL) produces better masks than optimizing for activation patterns (BCE) + error compensation.\", \"MISSING FROM LANDSCAPE: (1) DIP (MLSys 2025, arXiv 2412.01380) uses KL distillation for LoRA adapters alongside sparsity predictors — the closest existing system combining KL-distillation with sparsity, even though it trains different components. Should be discussed as partial precedent. (2) Sirius (NeurIPS 2024, arXiv 2409.03856) combines contextual sparsity with correction mechanisms — relevant to the SPON + predictor composition idea. (3) ActiveFlow (arXiv 2504.08378) introduces sparsity-aware self-distillation for activation sparsity recovery.\", \"TIMELINE RISK UNDERCHARACTERIZED: The auto_research estimate (10-13 days) assumes zero debugging setbacks. SPON reimplementation is described as 'architecturally trivial' but requires reproducing their Table 2 numbers to validate the reimplementation. FastForward's BCE predictor (used for ablation) requires careful implementation of their tiered weighting scheme. Both reimplementations need validation before they become reliable baselines, consuming precious days.\"]\nFeedback: The proposal has improved substantially across four rounds — FastForward and SPON integration, honest novelty reframing, and scoped baselines are all good. To reach publication quality, address these priorities:\n\n(1) **Fix the sparsity definition**: Decide whether you're comparing at 50% MLP-only sparsity or 50% model-level sparsity, and ensure ALL baselines use the same definition. If using MLP-only sparsity (your stated target), you cannot directly cite SPON's Table 2 numbers (which are model-level). Either re-run SPON at MLP-only sparsity as part of your experiments, or switch to model-level sparsity throughout.\n\n(2) **Provide a mechanistic argument for KL > BCE**: The key differentiator is the training objective. Argue concretely: BCE optimizes per-neuron binary classification independently, so it cannot capture interactions between neurons or between layers — neuron A being pruned might only hurt quality when neuron B in the next layer is also pruned. KL on output logits captures these joint effects because gradients flow through the full forward pass. This is an information-theoretic argument: BCE's per-neuron decomposition is a mean-field approximation, while KL on the joint output preserves correlations. If this argument is correct, the KL advantage should be largest at high sparsity (where neuron interactions matter more) — make this a testable prediction.\n\n(3) **Narrow evaluation scope for timeline**: Drop one sparsity level (keep 40% and 50%, drop 60% as stretch goal). Drop LongBench and RULER (the proposal mentions MMLU, GSM8K, HumanEval, PIQA, WinoGrande, HellaSwag, ARC-c — 7 benchmarks is sufficient for an efficiency paper). This saves ~30% evaluation time.\n\n(4) **Make SPON + predictor composition the headline**: The most interesting and novel experiment is whether static KL correction (SPON) and contextual KL prediction compose additively. If they do, this is a practical recipe (apply both for best quality) with a clear insight (static correction fixes average-case drift, contextual prediction handles per-input variation). Lead with this rather than treating it as experiment (2) of four.\n\n(5) **Add DIP to landscape**: DIP (MLSys 2025) uses KL distillation for LoRA recovery in a sparsity pipeline. It's the closest precedent for combining KL-distillation with activation sparsity, and contrasting with it sharpens your contribution (you train the predictor itself with KL, not a separate recovery module).\n\n### Round 5 review\nVerdict: revise\nIssues: [\"SPON VENUE UNVERIFIED: The proposal claims SPON is 'ICML 2026' but independent search found only the arXiv preprint (2512.12744) with no confirmed ICML 2026 acceptance. The paper may still be under review or accepted to a different venue. If ICML 2026 acceptance cannot be verified, label it as 'arXiv 2024' to avoid reviewer suspicion of fabricated venue claims.\", \"SPON BENCHMARK COUNT ERROR: The proposal states SPON achieves '71.96 vs 70.97 on five QA benchmarks' but SPON's Table 2 contains exactly 4 benchmarks (ARC-Challenge, ARC-Easy, BoolQ, PIQA). This minor factual error undermines the proposal's credibility on detailed claims. Verify and correct.\", \"FLOPS VS WALL-CLOCK MISLEADING: The 37:1 savings-to-overhead ratio is in FLOPs, but batch=1 decode is memory-bandwidth-bound, not compute-bound. The predictor adds ~151MB of weight reads (75.5M params × 2 bytes) across all layers. On H100, this translates to ~0.045ms per layer or ~1.4ms total overhead — versus perhaps 5-10ms savings from sparsity. The actual wall-clock ratio is likely 3-7:1, not 37:1. The proposal should report both FLOPs and estimated wall-clock ratios, or reviewers will flag this as misleading.\", \"BCE ABLATION FAIRNESS: The KL vs BCE ablation compares KL-trained predictor against BCE-trained predictor (same architecture, different loss). But FastForward's full system includes an error compensation network (2-layer MLP, r'=d_model/8) trained with MSE that partially addresses the output-quality concern KL handles directly. A fair comparison should include: (a) BCE only, (b) BCE + error compensation (FastForward's approach), (c) KL only. Without (b), the ablation is incomplete and reviewers may argue the KL advantage disappears when BCE is paired with error compensation.\", \"SPARK TRANSFORMER OMISSION: Spark Transformer (NeurIPS 2025) reparameterizes existing FFN weights to form low-cost predictors for identifying activated entries, achieving 2.5x FLOP reduction with 1.79x CPU decoding speedup. While it modifies architecture during pre-training (unlike the proposal's post-training approach), it should be discussed as related work since it also creates learned sparsity predictors from FFN parameters. Its omission may be flagged by reviewers familiar with the NeurIPS 2025 program.\", \"IMPROVEMENT TARGET STILL SPECULATIVE: The 2-4 point target relies on untested arithmetic: 1 (SPON) + 1-2 (contextual) + 0-1 (composition bonus). The contextual contribution estimate (1-2 points) is loosely grounded in FastForward's near-dense MMLU at 50% FFN sparsity, but FastForward uses FFN-only sparsity (a less aggressive operating point than model-level) AND includes an error compensation network. Extrapolating from FastForward's FFN-only results to model-level sparsity without error compensation may overestimate the contextual component's contribution.\", \"TIMELINE RISK FOR PAPER WRITING: The auto_research timeline (9-12 days) accounts only for experiments. A full EMNLP paper with related work, methodology, results, analysis, and ablation studies requires substantial writing effort. With experiments finishing on day 10-12 of 14, there is essentially 2-4 days for paper writing — very tight even with auto assistance. Consider whether partial results + clear story might be submitted, with full results provided during the author response period.\"]\nFeedback: The proposal has matured substantially over 5 rounds and the core research direction is sound. To reach 'pass' quality, address these priorities:\n\n(1) **Add BCE + error compensation ablation**: Include a third condition in the KL vs BCE ablation — BCE + error compensation (FastForward's approach). This is critical because FastForward's error compensation network explicitly addresses the output-quality preservation that KL handles implicitly. Without this comparison, reviewers will question whether KL's advantage is real or merely because BCE was tested without its intended companion mechanism. This strengthens the paper significantly if KL still wins.\n\n(2) **Report wall-clock overhead, not just FLOPs**: The 37:1 FLOPs ratio is technically correct but misleading for batch=1 decode (memory-bound regime). Add a paragraph estimating wall-clock predictor overhead: ~151MB weight reads at H100's 3.3 TB/s = ~0.045ms/layer, ~1.4ms total, versus estimated 5-10ms savings. A realistic 3-7:1 wall-clock ratio is still attractive and much more honest.\n\n(3) **Formalize the mean-field argument**: The KL > BCE argument is the proposal's key intellectual insight. Currently it's informal ('BCE treats neurons independently, KL captures correlations'). Strengthen it: define BCE's loss decomposition explicitly (L_BCE = Σ_j l(y_j, s_j) decomposes across neurons), show this is equivalent to a mean-field factorization that ignores joint effects, and contrast with KL which backpropagates through the full sparse forward pass. Derive the testable prediction mathematically: at higher sparsity, more neuron-neuron interaction effects emerge (because more neurons are pruned), so KL's advantage should increase. This elevates the contribution from 'empirical observation' to 'principled insight' and could push novelty from 3.5 to 4.\n\n(4) **Verify SPON venue and benchmark count**: Either confirm ICML 2026 acceptance with a citation, or label as 'arXiv 2024.' Fix the '5 QA benchmarks' claim to match the actual 4 benchmarks in Table 2. These are small fixes but protect credibility.\n\n(5) **Add Spark Transformer to landscape**: One sentence suffices: 'Spark Transformer (NeurIPS 2025) reparameterizes FFN weights during pre-training to form implicit predictors, achieving 1.79x decode speedup — complementary to our post-training approach which works on frozen models.'\n\n(6) **Narrow the experimental scope for timeline**: Drop the rank sweep (keep r=128 only) and drop 40% sparsity evaluations. Focus on 50% model-level sparsity only. This cuts training configurations from 12 to 3 (KL-r128, BCE-r128, BCE+compensation-r128) and evaluation by 50%, saving ~3-4 days for paper writing. Add rank sweep and 40% as supplementary if time permits.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"BENCHMARK MISMATCH WITH USER REQUIREMENTS: The user explicitly requires evaluation on perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, and MT-Bench. The proposal evaluates on PIQA, ARC-c, WinoGrande, HellaSwag, MMLU, GSM8K, and HumanEval — covering only 2 of 6 required benchmarks. Missing perplexity (trivial to add), LongBench and RULER (important for testing whether the sparsity predictor generalizes to long contexts, especially given training on short SlimPajama sequences), and MT-Bench (instruction-following quality under sparsity). This is a significant gap versus user requirements.\", \"COMPENSATION NETWORK WEIGHT CALCULATION ERROR: The proposal states 'FastForward's compensation MLP adds ~4.72 MB of weights per layer.' With r'=d_model/8=512 on Llama-3.1-8B (d_model=4096), the compensation network has Wcomp1 (4096×512) + Wcomp2 (512×4096) = 4,194,304 params × 2 bytes (FP16) ≈ 8.0 MB per layer, not 4.72 MB. The 4.72 MB figure suspiciously matches the predictor's own weight footprint (2.36M params × 2 bytes = 4.72 MB), suggesting a copy-paste error. This actually strengthens the proposal's argument (compensation overhead is even higher), but the factual error undermines credibility.\", \"MLP VS ATTENTION SPARSITY ALLOCATION UNSPECIFIED: At 50% model-level sparsity, the budget must be distributed between MLP and attention layers. The proposal states 'attention layers use training-free WINA-style heuristic pruning to match the model-level sparsity budget' but doesn't specify the MLP/attention allocation ratio. WINA uses a learned per-layer allocation via weight-informed scoring. Since the proposal's predictor only targets MLP blocks, the effective MLP sparsity could be significantly higher than 50% (if most of the budget is allocated to MLP) or lower (if attention absorbs significant sparsity). This allocation directly affects the improvement target arithmetic and should be specified.\", \"SPON ICML 2026 VENUE: ArXiv metadata lists ICML 2026 and v3 was updated April 30 (coinciding with notification dates), but the paper text itself does not mention ICML 2026, and no official ICML 2026 accepted paper list confirmation was found. The proposal is transparent about the evidence basis ('venue confirmed via arXiv metadata updated on the April 30 notification date'), which is adequate. Minor concern — recommend adding 'per arXiv metadata' qualifier.\", \"NO LONG-CONTEXT EVALUATION RISKS MISSING A KEY FAILURE MODE: The predictor is trained on SlimPajama calibration data (presumably short sequences). LongBench and RULER would test whether the learned neuron importance patterns generalize to long-context settings. If the predictor overfits to short-context activation patterns, it could fail catastrophically on long sequences — a plausible failure mode that the current benchmark set would not detect. This is both a user-requirement gap and a scientific gap.\"]\nFeedback: The proposal is genuinely close to passing (Round 6 of 10) and has addressed every major issue from prior rounds excellently. Three changes would push this over the threshold:\n\n(1) **Align benchmarks with user requirements**: Add perplexity (Wiki/C4) — this is trivial and standard for sparsity papers. Add at least one long-context benchmark (LongBench or RULER) to test predictor generalization beyond training distribution. Add MT-Bench for instruction-following quality. Drop PIQA and HellaSwag if needed to manage evaluation time — these are less discriminative for sparsity methods. The resulting set (perplexity, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval, MT-Bench, LongBench) covers the user's requirements while staying manageable.\n\n(2) **Fix the compensation network weight calculation**: Replace '~4.72 MB' with '~8.0 MB' (or compute exactly). This strengthens your argument — the compensation network is heavier than you claimed, making the KL-without-compensation alternative even more attractive. Also specify the MLP/attention sparsity allocation: state whether you use WINA's per-layer allocation or a fixed split, and what the effective MLP sparsity is at 50% model-level.\n\n(3) **Briefly discuss long-context generalization**: Add one sentence acknowledging that the predictor is trained on short sequences and that LongBench/RULER results will test generalization. If long-context performance degrades, this is itself a finding (predictor-based sparsity may require context-length-aware training). This also makes the paper more relevant to the user's interest in 'cache-aware methods for new workloads (long thinking traces, agent loops, RAG).'\n\n### Round 7 review\nVerdict: revise\nIssues: [\"RULER EVALUATION MISSING: The user explicitly requires evaluation on 'perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench.' The proposal covers all except RULER. RULER tests specific long-context capabilities (retrieval, multi-hop reasoning at various context lengths) that complement LongBench's task-level evaluation. Adding RULER is important both for user requirement compliance and scientific completeness — RULER's needle-in-a-haystack tasks would provide a fine-grained diagnostic of whether sparsity disproportionately impairs retrieval capabilities in long contexts.\", \"MISSING COMPETITOR — IFPruning (arXiv 2501.02086, Jan 2025): Trains a 302M-parameter sparsity predictor that combines instruction-level (quasi-static) with input-level (contextual) sparsity selection, co-optimizing the predictor and LLM end-to-end. While it operates at a different granularity (instruction-level vs token-level) and uses cross-entropy rather than KL distillation, it directly overlaps with the claim of 'composing static and contextual corrections.' The proposal should cite it and explain the distinction: IFPruning's static component is task-description-conditioned (requiring instruction input), while SPON's is truly input-independent (absorbed into bias terms with zero overhead).\", \"DIP DISTILLATION LOSS IMPRECISION: The proposal characterizes DIP as using 'KL-distillation for LoRA adapters,' but the DIP paper only states 'knowledge distillation loss to match the original (dense) model logits' without explicitly naming KL divergence. While KL is the standard distillation formulation, attributing a specific loss function the paper doesn't name undermines the proposal's otherwise meticulous accuracy. Change to 'logit-matching distillation' or 'knowledge distillation (likely KL, though unspecified).'\"]\nFeedback: The proposal is very close to passing (Round 7 of 10) and has addressed every major concern from prior rounds. Three minor fixes would push it over the threshold:\n\n(1) **Add RULER to evaluation**: The user explicitly requires it. RULER's synthetic tasks (needle-in-a-haystack, variable tracking, multi-hop retrieval) at controlled context lengths (4K-128K) would provide diagnostic insight that LongBench's natural-language tasks don't capture. RULER evaluation is lightweight (small dataset, deterministic scoring) and would add <2 hours of GPU time. This also strengthens the long-context generalization story — if the KL-trained predictor maintains retrieval accuracy while BCE degrades, that's strong evidence for the mean-field hypothesis in the long-context setting.\n\n(2) **Cite IFPruning and sharpen the composition novelty claim**: Add one sentence: 'IFPruning (arXiv 2501.02086) co-trains a predictor combining instruction-level (quasi-static) and input-level sparsity, but requires task-description input and modifies the base LLM. Our composition is between an input-independent bias correction (zero overhead, folded into bias terms) and a lightweight contextual predictor, both applied post-training to frozen models.' This inoculates against reviewers who know IFPruning.\n\n(3) **Fix DIP characterization**: Change 'KL-distillation' to 'logit-matching knowledge distillation (loss function unspecified in paper, likely KL).' This is a small fix but maintains the proposal's credibility on detailed claims.\n\nAll three fixes are minor and can be done in one revision cycle. The proposal's core experimental design, novelty framing, and feasibility analysis are all strong.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-12T03:46:03.376Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T03:46:03.376Z",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-12T03:46:03.406Z_

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

## Idea under review (round 8/10)
{
  "title": "Composing Static and Contextual Corrections for Activation Sparsity in SwiGLU LLMs via Output-Distribution Distillation",
  "core_problem": "Training-free activation sparsity methods (WINA, TEAL, R-Sparse) have enabled 40-60% model-level neuron pruning on native SwiGLU LLMs, but leave a substantial quality gap: at 50% model-level activation sparsity on Llama-3-8B, WINA achieves 59.57% average across six standard benchmarks (PIQA, ARC-c, WinoGrande, HellaSwag, MMLU, GSM8K) versus the dense model's 66.38% — a 6.81-point drop, with reasoning-heavy tasks (GSM8K, MMLU) degrading disproportionately. Two recent learned approaches partially address this gap from complementary but individually incomplete directions. SPON (Resting Neurons, arXiv 2512.12744v3, ICML 2026 per arXiv metadata updated on the April 30 notification date) introduces static, input-independent learnable bias vectors trained via KL-divergence distillation, recovering ~1 point over WINA on five QA benchmarks (ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande; 71.96 vs 70.97 weighted average) at zero inference overhead — demonstrating that output-distribution alignment helps, but leaving input-dependent importance patterns entirely unaddressed. FastForward (arXiv 2602.00397) trains contextual predictors with weighted BCE loss plus an error compensation network (2-layer MLP, r'=d_model/8) trained with MSE loss that operates at inference time, achieving MMLU 67.17 vs dense 67.84 at 50% FFN sparsity on Llama-3.1-8B — demonstrating that contextual prediction helps, but requiring the auxiliary compensation network to address the output-quality deficiency inherent in BCE's per-neuron objective. The compensation network adds ~8.0 MB of weights per layer (r'=d_model/8=512; two matrices of 4096×512, totaling 4,194,304 params × 2 bytes FP16 ≈ 8.0 MB) and associated GEMV operations at inference time — substantial overhead that motivates seeking training objectives that eliminate the need for compensation entirely. The critical insight is that BCE's training signal decomposes as L_BCE = Σ_j l(y_j, s_j), a mean-field factorization P(y_1,...,y_D) ≈ Π_j P(y_j) that treats each neuron's activation decision as independent of all others. This cannot capture joint interaction effects — the fact that pruning neuron A may only degrade output quality when neuron B in the same or subsequent layer is also pruned. FastForward's error compensation network is an engineering fix for this fundamental limitation: it patches output errors post-hoc rather than training the predictor to avoid them. KL divergence on output logits, by contrast, backpropagates through the full sparse forward pass via ∂L_KL/∂θ = ∂L_KL/∂p_sparse · ∂p_sparse/∂h_out · ∂h_out/∂m · ∂m/∂θ, where the term ∂h_out/∂m captures how each neuron's mask decision jointly affects the output in combination with all other active neurons. This yields a testable prediction: KL's advantage over BCE should increase with sparsity level, because higher sparsity creates more simultaneous neuron removals and thus more pairwise and higher-order interaction terms that BCE's independent decomposition cannot model. A further open question is whether learned sparsity predictors trained on short calibration sequences generalize to long-context settings — SVD Contextual Sparsity Predictors (arXiv 2603.14110) explicitly found that learned predictors suffer from out-of-distribution sensitivity compared to weight-structure-based approaches, making long-context evaluation essential for any learned predictor method.",
  "opportunity": "The landscape reveals four actionable opportunities. First, the composition question: SPON's static bias correction fixes average-case representational drift (input-independent) while contextual prediction handles per-input variation (input-dependent) — orthogonal mechanisms that should provide additive benefits. Note that IFPruning (arXiv 2501.02086) also combines quasi-static (instruction-level) and dynamic (input-level) sparsity, but through a fundamentally different mechanism: a 302M-parameter predictor that jointly fine-tunes the base LLM with cross-entropy loss, producing instruction-level masks (same mask for all tokens). Our composition is between an input-independent bias correction (zero overhead, folded into bias terms, applied to frozen models) and a lightweight token-level contextual predictor — a simpler, more modular, and post-training-compatible approach. If confirmed empirically, the SPON + contextual predictor composition becomes a practical recipe with a clear mechanistic explanation. Second, the training objective question: if a KL-trained predictor (no compensation) matches or exceeds the quality of FastForward's full BCE + compensation system, the practical benefit is substantial — a simpler inference pipeline with lower overhead. FastForward's compensation MLP adds ~8.0 MB of weights per layer (r'=d_model/8=512; 4,194,304 params in FP16) and associated GEMV operations at inference time — ~256 MB total across 32 layers; eliminating it simplifies deployment without sacrificing quality. This transforms the contribution from 'KL is slightly better than BCE' to 'KL training makes error compensation unnecessary.' Third, the formal mean-field analysis elevates the contribution from empirical observation to principled insight: we derive that BCE's per-neuron decomposition L_BCE = Σ_j l(y_j, s_j) is equivalent to optimizing under a mean-field factorized posterior over neuron importance, ignoring all pairwise and higher-order interaction terms. At sparsity level s, the number of simultaneously pruned neuron pairs scales as O(s²D²), so the approximation gap grows quadratically with sparsity — predicting that KL's advantage should be substantially larger at 50% than at 40% sparsity. This is a testable, falsifiable prediction that, if confirmed, provides actionable guidance for all future predictor design. Fourth, long-context generalization: learned sparsity predictors are trained on short calibration sequences, but deployed on inputs of arbitrary length. SVD Contextual Sparsity Predictors (arXiv 2603.14110) showed that learned predictors exhibit out-of-distribution sensitivity — our LongBench, RULER, and MT-Bench evaluation directly tests whether KL-trained predictors (which optimize for output-distribution preservation rather than per-neuron pattern matching) exhibit better generalization than BCE-trained ones, and whether SPON's static correction provides a context-length-invariant baseline that stabilizes long-context performance. RULER's synthetic tasks (needle-in-a-haystack retrieval, variable tracking, multi-hop tracing) at controlled context lengths (4K–128K) provide fine-grained diagnostics complementing LongBench's natural-language tasks — specifically, RULER can reveal whether sparsity disproportionately impairs precise retrieval capabilities (a failure mode that LongBench's aggregate task-level scores may mask). The contribution is fivefold: (1) the first empirical study of whether static bias correction (SPON) and contextual prediction compose additively for activation sparsity — the headline result; (2) a controlled four-condition ablation (BCE, BCE+compensation, KL, KL+compensation) testing whether KL training subsumes error compensation; (3) a formalized mean-field argument with the sparsity-level interaction prediction; (4) a systematic three-tier comparison (training-free, static-learned, contextual-learned) on native SwiGLU at decode time with honest wall-clock overhead reporting; and (5) long-context generalization evaluation testing whether learned predictors trained on short sequences maintain quality on LongBench tasks (4K–32K tokens) and RULER synthetic tasks (4K–32K tokens, with 13 tasks across Retrieval, Multi-hop Tracing, Aggregation, and QA), addressing a gap identified by recent work on predictor OOD sensitivity.",
  "landscape": "Training-free activation sparsity on SwiGLU has rapidly progressed: WINA (ICLR 2026) achieves the training-free SOTA with weight-informed scoring and greedy per-layer sparsity allocation across both MLP and attention layers (with attention tolerating ~2.3× higher sparsity than MLP), reporting 59.57% average on Llama-3-8B at 50% model-level sparsity versus 66.38% dense; WAS (EMNLP 2025) achieves 60% model-level sparsity via weight-aware scoring with constrained Bayesian optimization; WiSparse (arXiv 2026) preserves 97% of dense performance at 50% sparsity via weight-aware mixed-granularity allocation; TEAL (ICLR 2025) achieves 40-50% sparsity with 1.5-1.8x speedup via magnitude pruning; R-Sparse (ICLR 2025) achieves 50% model-level sparsity via rank-aware input channel scoring; ActTail (arXiv 2026) uses Heavy-Tailed Self-Regularization for global sparsity allocation; DIP (MLSys 2025) achieves predictor-free dynamic pruning on SwiGLU at ~40% speedup plus LoRA adapters trained via logit-matching knowledge distillation (loss function unspecified in paper, likely KL) for accuracy recovery — the closest existing system combining distillation with sparsity, though critically it trains the LoRA recovery module with distillation rather than the sparsity predictor itself, and uses magnitude-based (not predicted) sparsity masks. On the learned side, SPON/Resting Neurons (arXiv 2512.12744v3, ICML 2026 per arXiv metadata updated on the April 30 notification date) injects learnable input-independent activation vectors trained via KL-divergence distillation, recovering ~1 point over WINA at 50% model-level sparsity on five QA benchmarks (ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande; 71.96 vs 70.97), with zero inference overhead since vectors fold into bias terms, training in ~1 hour on 4x A6000; SPON also reports perplexity on WikiText and validates cross-dataset generalization by calibrating on C4 while evaluating on WikiText. FastForward (arXiv 2602.00397, Jan 2026) trains a contextual predictor (single-head attention + 2-layer MLP, bottleneck r=d_model/16) with weighted BCE loss plus an error compensation network (2-layer MLP, r'=d_model/8=512) trained with MSE loss ||Y_dense − Y_sparse||², achieving MMLU 67.17 vs dense 67.84 at 50% FFN sparsity on Llama-3.1-8B — critically, the compensation network operates at inference time (not just training), adding ~8.0 MB per layer (4,194,304 params × 2 bytes FP16, ~256 MB total across 32 layers) in per-layer weight reads and compute overhead. FastForward targets prefill optimization and evaluates on LongBench (English tasks, 4K-32K tokens) achieving <6% accuracy loss at 50% FFN sparsity — demonstrating that their predictor generalizes beyond short training sequences via an attention-mixing mechanism, but requiring the compensation network for this generalization. IFPruning (arXiv 2501.02086, Jan 2025) trains a 302M-parameter sparsity predictor that combines instruction-level (quasi-static) and input-level (contextual) sparsity selection, jointly optimizing the predictor and LLM weights via cross-entropy loss. While IFPruning also composes static and contextual sparsity components, it operates at a fundamentally different granularity and setting: instruction-level masks (same mask for all tokens in a sequence) requiring task-description input, a large predictor (302M params vs our ~75.5M total), and joint LLM fine-tuning that modifies the base model — whereas our composition applies input-independent bias correction (zero overhead, folded into bias terms) with token-level contextual prediction, both post-training on frozen models. ShadowLLM (EMNLP 2024) trains single-hidden-layer predictors using MSE loss on per-neuron importance. Sirius (NeurIPS 2024) addresses quality degradation from contextual sparsity via periodic full-model correction every 16 tokens with speculative-decoding-style rollback, achieving 20-35% latency reduction — a complementary approach to our static+contextual composition since Sirius interleaves sparse and dense inference rather than composing learned correction mechanisms. Spark Transformer (NeurIPS 2025) reparameterizes existing FFN weights and attention key embeddings during pre-training (Gemma-2 recipe) to form implicit sparsity predictors with a hardware-friendly 'statistical top-k' linear-time approximate algorithm, achieving 2.5x FLOP reduction with 1.79x CPU / 1.40x GPU decode speedup and only 8% of FFN neurons activated — complementary to our post-training approach which works on frozen models without pre-training modification. ActiveFlow (arXiv 2025) combines cross-layer preloading with sparse-aware self-distillation using KL-divergence to adapt model weights (not predictor parameters) for on-device deployment, demonstrating that KL-based training recovers 2.64-10.21% accuracy over TEAL — further evidence that output-distribution distillation is effective for sparsity recovery, though applied to weight adaptation rather than predictor training. Polar Sparsity (NeurIPS 2025) trained BCE routers and evaluated on LongBench for instruction-tuned models, concluding MLP sparsity offers limited benefits on SwiGLU in batch-scaling scenarios — however, this was with activation-pattern prediction, not output-distribution alignment in low-batch decode; their long-context evaluation was limited to 16K tokens. MaskLLM (NeurIPS 2024 Spotlight) uses Gumbel Softmax for static 2:4 masks. SDMPrune (arXiv 2025) uses self-distillation for MLP weight pruning, not activation sparsity. SVD Contextual Sparsity Predictors (arXiv 2603.14110, Mar 2026) provide training-free predictors using truncated SVD of gate projections, targeting ReGLU-based models with high inherent sparsity — critically, they found that learned predictors suffer from out-of-distribution sensitivity on unseen data (ROC-AUC degrades on held-out sequences) while SVD predictors maintain robust performance by leveraging weight structure rather than data-dependent patterns. This OOD sensitivity finding directly motivates our LongBench and RULER evaluation: if learned predictors are fragile to distribution shift, their behavior on long-context tasks (absent from short calibration data) is an important empirical question. No prior work (a) trains the sparsity predictor itself with KL-divergence distillation, (b) tests whether SPON's static correction composes additively with contextual prediction in a post-training, frozen-model setting, (c) formally analyzes BCE's mean-field limitation and its interaction with sparsity level, or (d) evaluates whether KL-trained predictors generalize better than BCE-trained ones on long-context tasks using both natural (LongBench) and synthetic (RULER) benchmarks.",
  "approach": "We study the composition of two learned correction mechanisms for activation sparsity — static bias correction and contextual prediction — trained via output-distribution distillation (KL divergence) on native SwiGLU LLMs at decode time, with a controlled four-condition ablation testing whether KL training subsumes error compensation. For each SwiGLU MLP block in Llama 3.1 8B (32 layers, d_model=4096, intermediate_size=14336), we attach a low-rank predictor that maps the layer input hidden state h ∈ R^d to a continuous sparsity score over the intermediate dimension D via two linear projections: h → W_down (4096 × 128) → ReLU → W_up (128 × 14336), yielding ~2.36M parameters per layer (~75.5M total, <1% of 8B model). Architecture is fixed at rank r=128 (no rank sweep, following reviewer guidance to narrow scope). During training, scores are converted to differentiable binary masks via Gumbel-sigmoid relaxation with temperature annealing (τ: 5 → 0.1). The primary training loss is: L = KL(p_dense || p_sparse) + λ_mse · MSE(h_dense_l, h_sparse_l) + λ_sparse · max(0, s − s_target), where KL divergence on output logits is the primary signal (capturing joint neuron interactions through end-to-end gradient flow via ∂L_KL/∂θ = ∂L_KL/∂p_sparse · ∂p_sparse/∂h_out · ∂h_out/∂m · ∂m/∂θ), per-layer MSE provides gradient signal for early layers, and the sparsity penalty enforces target model-level sparsity s_target = 0.5. Only predictor parameters are updated during ~1K gradient steps on SlimPajama calibration data with the base LLM frozen. MLP/attention sparsity allocation: We follow WINA's greedy per-layer allocation algorithm (originally from TEAL) to distribute the 50% global FLOPs budget across all layers. This algorithm iteratively increases sparsity in the least-sensitive layer (measured by calibration perplexity impact) until the aggregate meets the global target. WINA found that attention layers tolerate ~2.3× higher sparsity than MLP layers, so the allocation typically assigns ~55-65% sparsity to attention layers and ~40-50% to MLP layers, though the exact per-layer ratios are determined by the calibration-based optimization. Within MLP layers, our contextual predictor replaces WINA's heuristic scoring to determine which neurons to activate; within attention layers, WINA's original weight-informed scoring is used unchanged. We report both the global model-level sparsity (50%) and the effective per-component (MLP, attention) sparsity ratios resulting from the allocation, ensuring transparent comparison with baselines that may use different allocation strategies. At inference, the predictor produces a binary mask via top-k selection, and the sparse SwiGLU forward pass skips columns of gate/up projections and rows of the down projection using Triton sparse GEMV kernels from the TEAL/WINA codebases. Predictor overhead — FLOPs and wall-clock (honest reporting): Each predictor adds ~4.72M FLOPs per layer (two GEMVs of 4096×128 and 128×14336) versus ~176M FLOPs saved at 50% MLP sparsity — a ~37:1 FLOPs ratio. However, batch=1 decode is memory-bandwidth-bound, not compute-bound. On H100 (3.35 TB/s peak HBM bandwidth), the small predictor GEMVs achieve only ~100 GB/s effective bandwidth due to low matrix occupancy and kernel launch overhead, yielding ~0.047 ms per layer or ~1.5 ms total predictor overhead across 32 layers. The larger FFN matrices being skipped achieve ~500 GB/s effective bandwidth, yielding ~0.35 ms savings per layer or ~11.3 ms total savings. The realistic wall-clock savings-to-overhead ratio is approximately 4-8:1 — still attractive for decode acceleration, but substantially lower than the 37:1 FLOPs ratio. We report both metrics throughout to avoid misleading claims. Four-condition ablation (the key experimental design addition): (a) BCE only — our predictor architecture trained with weighted BCE loss (FastForward-style exponential weighting), no compensation; (b) BCE + error compensation — same BCE predictor plus FastForward's 2-layer compensation MLP (r'=d_model/8=512, adding ~8.0 MB per layer: W_comp1 ∈ R^{4096×512} + W_comp2 ∈ R^{512×4096} = 4,194,304 params × 2 bytes FP16), trained with MSE loss ||Y_dense − (Y_sparse + g_φ(h))||², with compensation network active at inference time; (c) KL only — our predictor trained with KL-divergence loss, no compensation; (d) KL + error compensation — if time permits. Condition (b) is critical: it replicates FastForward's full approach (BCE + compensation) rather than testing BCE in isolation, ensuring a fair comparison. If KL-only (c) matches or exceeds BCE+compensation (b), the finding is that KL training makes error compensation unnecessary — yielding a simpler system with lower inference overhead (eliminating ~256 MB of compensation weights and associated compute across 32 layers). Evaluation benchmarks (aligned with user requirements): (1) Perplexity on WikiText-2 and C4 — standard for sparsity papers, reported by SPON and most training-free baselines, trivial to compute; (2) ARC-Challenge — science reasoning; (3) WinoGrande — coreference resolution; (4) MMLU — multitask knowledge; (5) GSM8K — mathematical reasoning; (6) HumanEval — code generation; (7) MT-Bench — multi-turn instruction-following quality under sparsity, evaluated using GPT-4 as judge (80 questions, 8 categories), testing whether sparsity disproportionately degrades open-ended generation; (8) LongBench (English subset) — long-context evaluation (4K-32K tokens) testing predictor generalization beyond training distribution, directly comparable to FastForward's LongBench results; (9) RULER (COLM 2024) — synthetic long-context evaluation with 13 tasks across 4 categories (Retrieval including needle-in-a-haystack variants with single/multi-key/multi-value/multi-query needles, Multi-hop Tracing via variable tracking, Aggregation via common/frequent word extraction, and QA based on SQuAD/HotpotQA) at controlled context lengths (4K, 8K, 16K, 32K), using 500 examples per task with recall-based accuracy scoring. RULER complements LongBench by providing fine-grained diagnostics: its synthetic tasks isolate specific capabilities (precise retrieval, multi-hop reasoning, information aggregation) that LongBench's natural-language aggregate scores may mask. If sparsity disproportionately impairs retrieval accuracy (needle-in-a-haystack) while preserving summarization quality, RULER will reveal this while LongBench may not. We evaluate RULER at 4K-32K to match our LongBench context range; extending to 64K-128K is feasible but deferred to keep scope manageable given Llama 3.1 8B's 128K context window. This benchmark set covers all user-required evaluation axes: perplexity, knowledge/reasoning (MMLU, ARC-c, GSM8K), code (HumanEval), long-context (LongBench, RULER), and instruction-following (MT-Bench). Long-context generalization: The predictor is trained on SlimPajama calibration sequences (typically 2048 tokens). LongBench tasks require processing 4K-32K token inputs, and RULER provides controlled synthetic tasks at the same context lengths, testing whether learned neuron importance patterns generalize beyond the training context length. SVD Contextual Sparsity Predictors (arXiv 2603.14110) found that learned predictors suffer OOD sensitivity on unseen data, making this a plausible failure mode. If long-context performance degrades disproportionately, this is itself a finding — motivating context-length-aware predictor training or hybrid approaches where static SPON correction (which is context-length-invariant by construction) provides a robust baseline while contextual prediction adapts to input-specific patterns. RULER's task-level granularity adds diagnostic value: if KL-trained predictors maintain retrieval accuracy (NIAH tasks) while BCE-trained predictors degrade, this provides evidence that output-distribution alignment preserves retrieval-critical neuron activation patterns that per-neuron BCE misses — connecting the mean-field hypothesis to a specific, interpretable capability. FastForward reports their predictor generalizes to LongBench via an attention-mixing mechanism; our four-condition ablation will reveal whether KL-trained predictors (which optimize output-distribution preservation) exhibit different generalization characteristics than BCE-trained ones (which optimize per-neuron pattern accuracy). Experiments focus on Llama 3.1 8B at 50% model-level sparsity as the primary operating point. For the KL-BCE sparsity interaction test, we additionally train KL and BCE predictors at 40% model-level sparsity (2 extra training runs) to test the mean-field prediction that KL's advantage over BCE grows with sparsity level. All other baselines and the composition experiment are evaluated at 50% only, saving ~3-4 days versus evaluating at both levels. Baselines use consistent model-level sparsity: training-free baselines are WINA, TEAL, and R-Sparse; learned baselines are SPON (reimplemented — bias vectors + KL training, architecturally trivial, validated by reproducing Table 2 numbers on Llama 3 8B before evaluating on Llama 3.1 8B) and the four-condition ablation above. Key experiments ordered by importance: (1) SPON + KL predictor composition (headline): apply SPON bias correction AND contextual KL prediction simultaneously, testing whether static correction (fixing average-case drift) and contextual prediction (handling per-input variation) provide additive benefits. (2) KL-only vs BCE+compensation: the critical test of whether end-to-end KL training subsumes the need for error compensation — if confirmed, this is the key practical recommendation (eliminating ~256 MB of compensation weights and per-layer GEMV overhead). (3) KL vs BCE sparsity-level interaction: testing at both 40% and 50% whether KL's advantage over BCE (both without compensation) grows with sparsity, confirming the mean-field prediction. (4) Three-tier comparison: training-free (WINA, TEAL, R-Sparse) vs static-learned (SPON) vs contextual-learned (ours), establishing marginal value of each tier. (5) Long-context generalization: LongBench and RULER evaluation across all conditions, testing whether KL-trained predictors generalize better than BCE-trained ones to long contexts, and whether SPON's static correction stabilizes long-context performance. RULER's per-task breakdown provides diagnostic insight into which capabilities (retrieval, tracing, aggregation) are most affected by sparsity and which benefit most from KL vs BCE training. (6) Per-task analysis: decompose improvements by benchmark type (perplexity vs knowledge/reasoning vs code vs long-context vs instruction-following). Improvement target: 1.5-3 points average recovery over WINA at 50% model-level sparsity (WINA baseline: 59.57 on 6 benchmarks), conservatively grounded in: SPON's ~1 point static recovery (verified on five QA benchmarks), contextual KL prediction contributing an estimated 0.5-1.5 points (conservative — FastForward's near-dense MMLU quality was achieved at FFN-only sparsity with error compensation, a less aggressive operating point than our model-level sparsity without compensation), and a potential 0-0.5 point composition bonus. The 1.5-3 point range is arithmetically consistent: 1 (SPON) + 0.5-1.5 (contextual) + 0-0.5 (composition) = 1.5-3 points total. Explicit fallbacks: (A) If composition shows no additive benefit (SPON + predictor ≈ predictor alone), the contribution becomes the finding that contextual prediction subsumes static correction. (B) If KL-only does not beat BCE+compensation, the contribution pivots to the formalized mean-field analysis + three-tier comparison with the finding that error compensation remains necessary, but KL should be used in conjunction. (C) If KL does not outperform BCE at any sparsity level, the contribution becomes the rigorous negative result plus the composition study. (D) If long-context performance degrades substantially, the contribution includes the finding that predictor-based sparsity requires context-length-aware training, with SPON's static correction serving as a context-length-invariant safety net.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~68-95h H100",
      "gpu_utilization": "Low (~15-25%)",
      "timeline": "3-4 weeks (including paper writing)",
      "team": "1 ML researcher",
      "estimated_gpu_cost": "$170-240"
    },
    "human_in_loop": {
      "gpu_hours": "~68-105h H100",
      "gpu_utilization": "Moderate (~40-55%)",
      "timeline": "2.5-3 weeks (including paper writing)",
      "team": "1 researcher, ~30min/day review",
      "claude_api_cost": "$60-110",
      "estimated_gpu_cost": "$170-265"
    },
    "auto_research": {
      "gpu_hours": "~102-160h H100 (predictor at r=128, 50% model-level sparsity primary, 40% for KL-BCE interaction only, four-condition ablation [BCE, BCE+comp, KL, KL+comp], SPON reimplementation + validation, SPON+predictor composition, all evaluations across 9 benchmarks including LongBench long-context, RULER synthetic long-context, and MT-Bench instruction-following, wall-clock profiling)",
      "gpu_utilization": "High (~80-90%)",
      "timeline": "14 days total with 2-4 H100s running concurrently: Days 1-2: codebase scaffolding, SPON validation, MT-Bench/LongBench/RULER evaluation pipeline setup (RULER uses NVIDIA's open-source codebase at github.com/NVIDIA/RULER, minimal integration effort). Days 3-6: train 4 ablation conditions at 50% + 2 interaction runs at 40%. Days 7-9: SPON+KL composition, all evaluations including perplexity (WikiText-2, C4), discriminative benchmarks (ARC-c, WinoGrande, MMLU, GSM8K, HumanEval), LongBench (English subset, 4K-32K tokens), RULER (13 tasks × 4 context lengths [4K-32K] × 500 examples, deterministic scoring — adds ~2-3h GPU time), MT-Bench (80 multi-turn questions with GPT-4 judge). Days 10-11: wall-clock profiling, long-context analysis, RULER per-task breakdown, figure generation. Days 12-14: paper writing with auto assistance — feasible for May 25 ARR deadline. Note: LongBench evaluation on long sequences at batch=1 decode adds ~8-12h of GPU time; MT-Bench adds ~2-3h including judge API calls; RULER adds ~2-3h (lightweight synthetic evaluation with deterministic scoring).",
      "team": "0 (initial 2-4h setup for codebase scaffolding and GPU provisioning)",
      "claude_api_cost": "$160-270",
      "estimated_gpu_cost": "$255-400",
      "speed_bottleneck": "Single-GPU training on 8B model; LongBench evaluation on long sequences (4K-32K tokens) at batch=1 decode is the primary bottleneck. RULER evaluation is lightweight (synthetic data, deterministic scoring, ~2-3h). Narrowing to 50% primary sparsity (40% only for 2 interaction runs) and dropping rank sweep saves ~40% versus earlier proposals. Explicit 3-day paper writing buffer prevents timeline overrun.",
      "risk_note": "Timeline is tight with 14 days remaining. Primary execution risk: validating SPON reimplementation (must reproduce published Llama-3-8B Table 2 numbers on QA benchmarks before proceeding). Mitigation: SPON is architecturally trivial (bias vectors + standard KL training, ~1 hour on 4× A6000). Secondary risk: LongBench evaluation time on long sequences — mitigated by selecting the English-language subset (matching FastForward's evaluation protocol) and parallelizing evaluation across GPUs. Tertiary risk: MT-Bench requires GPT-4 judge API calls — mitigated by low cost (~$5-10 for 80 questions × multiple configurations) and fast turnaround. Quaternary risk: implementing FastForward's compensation MLP for the ablation — mitigated by simple 2-layer MLP architecture (d_model → d_model/8 → d_model with MSE loss). Quinary risk: Triton sparse kernel integration — mitigated by using existing TEAL/WINA kernel codebases. RULER risk: minimal — NVIDIA provides an open-source evaluation codebase (github.com/NVIDIA/RULER), and the synthetic evaluation is computationally lightweight with deterministic scoring. Fallback plan: if SPON reproduction takes >2 days, use SPON's published numbers on the QA subset and note the benchmark-set difference. If LongBench evaluation runs over schedule, prioritize single-document QA and summarization subtasks. If RULER evaluation extends beyond budget, evaluate at 4K and 16K context lengths only (2 of 4 planned lengths). Paper writing risk: 3 days allocated; structure and related work can be drafted in parallel with experiments."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026)"
  ],
  "level": "solid",
  "key_references": [
    "Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time (ICML 2023)",
    "CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models (COLM 2024)",
    "RULER: What's the Real Context Size of Your Long-Context Language Models? (COLM 2024, arXiv 2404.06654)",
    "MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models (NeurIPS 2024 Spotlight)",
    "ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models (EMNLP 2024)",
    "Sirius: Contextual Sparsity with Correction for Efficient LLMs (NeurIPS 2024)",
    "Instruction-Following Pruning for Large Language Models (IFPruning, arXiv 2501.02086, Jan 2025)",
    "TEAL: Training-Free Activation Sparsity in Large Language Models (ICLR 2025)",
    "R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference (ICLR 2025)",
    "DaSS: Dependency-Aware Semi-Structured Sparsity of GLU Variants in Large Language Models (TMLR 2025)",
    "Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking (DIP, MLSys 2025)",
    "SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity (ICML 2025)",
    "WAS: Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling (EMNLP 2025)",
    "Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity (NeurIPS 2025)",
    "Spark Transformer: Reactivating Sparsity in FFN and Attention (NeurIPS 2025)",
    "Scaling Up On-Device LLMs via Active-Weight Swapping Between DRAM and Flash (ActiveFlow, arXiv 2504.08378)",
    "Resting Neurons, Active Insights (SPON): Improving Input Sparsification for Large Language Models (ICML 2026 per arXiv metadata, arXiv 2512.12744v3)",
    "FastForward: Accelerating LLM Prefill with Predictive FFN Sparsity (arXiv 2602.00397, Jan 2026)",
    "WINA: Weight Informed Neuron Activation for Accelerating Large Language Model Inference (ICLR 2026)",
    "WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity (arXiv 2026)",
    "ActTail: Global Activation Sparsity in Large Language Models (arXiv 2026)",
    "SVD Contextual Sparsity Predictors for Fast LLM Inference (arXiv 2603.14110, Mar 2026)"
  ],
  "description": "We study whether two learned correction mechanisms for activation sparsity — static bias correction and contextual prediction — address orthogonal failure modes and compose additively when both are trained via output-distribution distillation, and whether KL-divergence training for the contextual predictor subsumes the need for error compensation networks. The activation sparsity landscape has stratified into three tiers: training-free heuristics (WINA, TEAL, R-Sparse) achieving 59.57% average on Llama-3-8B at 50% model-level sparsity versus 66.38% dense (6.81-point gap); static learned correction (SPON, ICML 2026 per arXiv metadata) training input-independent bias vectors via KL-distillation, recovering ~1 point on five QA benchmarks at zero overhead; and contextual learned prediction (FastForward, arXiv 2026) training input-dependent predictors with weighted BCE plus an inference-time error compensation MLP adding ~8.0 MB per layer (~256 MB total across 32 layers). IFPruning (arXiv 2501.02086) co-trains a 302M-parameter predictor combining instruction-level (quasi-static) and input-level sparsity with cross-entropy loss, but requires task-description input, modifies the base LLM, and operates at instruction-level granularity (same mask for all tokens). Our composition is between an input-independent bias correction (zero overhead, folded into bias terms) and a lightweight token-level contextual predictor, both applied post-training to frozen models — a simpler, more modular approach. No prior work combines contextual prediction with KL-divergence distillation for the predictor itself, tests static+contextual composition in a post-training frozen-model setting, formally analyzes why BCE's per-neuron objective requires error compensation, or evaluates whether KL-trained predictors generalize better than BCE-trained ones to long-context settings. Our key theoretical contribution formalizes BCE's limitation as a mean-field factorization: L_BCE = Σ_j l(y_j, s_j) treats neuron activation decisions as independent, ignoring joint interaction effects that grow quadratically with sparsity level O(s²D²). KL divergence on output logits captures these interactions through end-to-end gradient flow (∂h_out/∂m couples all mask decisions), yielding a testable prediction: KL's advantage over BCE grows with sparsity. We test this with a controlled four-condition ablation (BCE-only, BCE+compensation, KL-only, KL+compensation) — the critical test being whether KL-only matches BCE+compensation, which would mean KL training makes error compensation unnecessary (simpler system, ~256 MB less inference overhead). Each rank-128 predictor (~2.36M params per layer, <1% of model) maps layer inputs to neuron masks via Gumbel-sigmoid relaxation. MLP/attention sparsity allocation follows WINA's greedy per-layer algorithm: at 50% global FLOPs budget, attention layers receive ~55-65% sparsity while MLP layers receive ~40-50%, with exact per-layer ratios determined by calibration-based optimization; we report both global and per-component effective sparsity. We report both FLOPs (37:1 savings-to-overhead ratio) and honest wall-clock estimates for batch=1 decode on H100 (~4-8:1, accounting for the fact that small predictor GEMVs achieve ~100 GB/s effective bandwidth versus ~500 GB/s for the larger FFN matrices being skipped, yielding ~1.5 ms total predictor overhead versus ~11.3 ms savings across 32 layers). Evaluation covers all user-required axes: perplexity (WikiText-2, C4), discriminative benchmarks (ARC-c, WinoGrande, MMLU, GSM8K), code generation (HumanEval), long-context generalization (LongBench English subset, 4K-32K tokens — directly comparable to FastForward's evaluation and testing whether learned predictors trained on short SlimPajama sequences generalize, given SVD Contextual Sparsity Predictors' finding that learned predictors exhibit OOD sensitivity), synthetic long-context diagnostics (RULER, COLM 2024 — 13 tasks across Retrieval, Multi-hop Tracing, Aggregation, and QA categories at 4K-32K context lengths, providing fine-grained capability-level diagnostics that complement LongBench's aggregate scores, particularly testing whether sparsity disproportionately impairs precise retrieval vs. summarization), and instruction-following (MT-Bench with GPT-4 judge). Key experiments: (1) SPON + KL predictor composition testing additive benefits (headline), (2) KL-only vs BCE+compensation testing whether KL subsumes error compensation, (3) KL vs BCE at 40% and 50% sparsity testing the mean-field interaction prediction, (4) three-tier comparison with consistent model-level sparsity definitions, (5) long-context generalization across all conditions on LongBench and RULER, with RULER per-task breakdown revealing which capabilities (retrieval, tracing, aggregation) are most affected by sparsity. Target: conservative 1.5-3 points recovery over WINA at 50% model-level sparsity (grounded in: SPON ~1 point verified, contextual 0.5-1.5 points conservative given model-level sparsity is harder than FastForward's FFN-only operating point, composition 0-0.5 points). Evaluated on Llama 3.1 8B at 50% model-level sparsity (with 40% for KL-BCE interaction test only). Scoped for EMNLP 2026 ARR deadline (May 25, 2026) with explicit 3-day paper writing buffer.",
  "project_name": "distill_sparse_swiglu",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["FACTUAL ERROR: ShadowLLM is claimed to 'target ReLU models' but it actually evaluates on Llama-2-7B (SwiGLU architecture) alongside OPT models. The landscape claim that 'no predictor-based approach targets SwiGLU' is inaccurate.", "MISSING COMPETITORS: Several important SwiGLU activation sparsity papers are omitted from the landscape: (1) CHESS (EMNLP 2024) — channel-wise thresholding on SwiGLU models with 1.27x speedup; (2) La RoSA (ICML 2025) — training-free rotated sparse activation achieving 40% sparsity with 1.30x speedup, outperforming TEAL; (3) SCAP (NeurIPS 2024 Workshop) — post-training calibration achieving 48.5% FFN sparsity; (4) MaskLLM (NeurIPS 2024 Spotlight) — Gumbel-based learnable masks on SwiGLU LLMs (N:M sparsity).", "AGGRESSIVE SPARSITY TARGET: No existing work on native SwiGLU models (without ReLUfication) has demonstrated >50% MLP sparsity without significant accuracy loss. The claimed 60-70% would be a 20-30 percentage point improvement over TEAL with no evidence this is achievable. The SVD predictor paper achieving 90% sparsity works only on ReLUfied models (ProSparse, TurboSparse), not native SwiGLU.", "TIMELINE INFEASIBILITY: 16 days vs. the generator's own 3-4 month manual estimate. Custom CUDA kernel development alone typically takes weeks. Even the auto_research mode estimates 2-3 weeks with 4-8 concurrent H100s, and flags CUDA correctness as highest risk.", "PREDICTOR OVERHEAD NOT ANALYZED: A 15M-parameter predictor per block × 32 layers = ~480M total additional parameters requiring forward passes. This adds latency that could significantly eat into the sparsity-based speedup, especially for small batch sizes where decode is already memory-bound. No analysis of predictor inference cost vs. sparsity savings is provided.", "BATCH-SIZE SCALABILITY CONCERN: Polar Sparsity (NeurIPS 2025) showed that MLP neuron sparsity patterns lose their advantage at realistic batch sizes because the union of active neurons across tokens quickly approaches the full dense set. The proposed method's exclusive focus on MLP blocks may yield minimal real-world speedup in production serving settings.", "SPEEDUP CLAIMS ARE SPECULATIVE: The projected 1.8-2.5x decode speedup is stated without any basis — it depends entirely on unwritten CUDA kernel quality and assumes predictor overhead is negligible, neither of which can be assumed.", "'Architecture-generic' claim is unsupported: Transferability across Qwen 2.5 and Llama 3.1/3.3 model families without architecture-specific tuning is a strong claim requiring empirical evidence. Different models have different hidden/intermediate dimensions and activation patterns."]
Feedback: The core direction (distillation-trained sparsity predictors for SwiGLU MLP) has merit but needs significant corrections: (1) Fix the ShadowLLM mischaracterization — it does work on SwiGLU models, so reframe the novelty as 'distillation-based predictor training for higher sparsity ratios' rather than 'first predictor for SwiGLU.' (2) Add CHESS, La RoSA, SCAP, and MaskLLM to the landscape analysis. (3) Lower the sparsity target to 50-60% and provide theoretical or empirical justification for why distillation would improve over training-free baselines beyond the ~50% plateau. (4) Address the Polar Sparsity batch-size scalability concern — either target single-request/edge deployment explicitly, or show how predictor-based sparsity maintains advantage at batch sizes >1. (5) Critically, address the CUDA kernel bottleneck: consider reusing existing sparse kernels from TEAL/R-Sparse/DIP rather than writing custom gather-scatter kernels from scratch, or use Triton for faster development. (6) Add a predictor overhead analysis showing that the per-layer predictor forward pass cost is small relative to the savings from skipping neurons. (7) For the 16-day timeline, scope down: pick one model family (e.g., Llama 3.1 8B/70B), reuse existing sparse execution infrastructure, and target 50-55% MLP sparsity as the primary result.

### Round 2 review
Verdict: revise
Issues: ["VENUE MISMATCH (Critical): The user explicitly targets EMNLP 2026 (ARR deadline May 25, 2026, 14 days away), but the generator lists target_venues as AAAI 2027, ICLR 2027, MLSys 2027, EMNLP 2027. The generator's own manual timeline is 2-3 months and auto is 2-3 weeks — neither fits the 14-day constraint. This is a direct failure to meet the user's stated requirements.", "SPARSITY TARGET CONTRADICTED BY EVIDENCE: WINA at 65% model-level sparsity on Llama-3-8B shows catastrophic accuracy loss (MMLU drops to 38.48 from ~60+ dense, GSM8K drops to 7.05). Literature indicates native SwiGLU models can only be pruned to ~50% before >1% MMLU degradation. The claim of 70-75% MLP sparsity with ≤1% accuracy loss has no supporting evidence and contradicts all existing benchmarks.", "POLAR SPARSITY DIRECTLY CONTRADICTS CORE PREMISE: Polar Sparsity (NeurIPS 2025) uses a nearly identical architecture (two-layer feedforward router, hidden=1024) but explicitly states that for non-ReLU architectures (SwiGLU), 'only attention head sparsity is applied since MLP sparsification becomes ineffective.' The proposal does not explain why its KL-distillation trained predictor would succeed where Polar Sparsity's learned router failed on SwiGLU MLP.", "MISSING COMPETITORS: (1) ActTail (arXiv March 2026) — training-free global sparsity allocation using Heavy-Tailed Self-Regularization theory, achieves 21.8% perplexity reduction at 80% sparsity on Llama-2-7B; (2) MGLU/Masked Gated Linear Unit (arXiv June 2025) — learns binary masks within the GLU structure itself, achieving comparable accuracy to SwiGLU with memory advantages; (3) DaSS (TMLR 2025) — dependency-aware semi-structured sparsity specifically designed for GLU variants including SwiGLU.", "INCREMENTAL NOVELTY vs. ShadowLLM: ShadowLLM already trains learned predictors on Llama-2 (a SwiGLU architecture), achieving 15% accuracy improvement over heuristic methods. The proposed method differs primarily in: (a) using KL divergence instead of MSE importance regression, (b) Gumbel-sigmoid instead of direct thresholding, (c) low-rank architecture instead of single-hidden-layer MLP. These are engineering variations of an established approach, not a paradigm shift.", "70B COMPUTE FEASIBILITY QUESTIONABLE: Training predictors on Llama 3.1 70B requires 4+ H100s for model parallelism. Forward passes through the full dense 70B model for KL divergence computation at each training step are expensive. MaskLLM required 1,280 A100-GPU-hours for just 7B with static masks. The claim of covering both 8B and 70B within 200 H100-hours needs more rigorous justification."]
Feedback: The revision addressed several Round 1 issues well (ShadowLLM characterization, kernel reuse, batch=1 scope, predictor overhead analysis), but critical problems remain: (1) **Target EMNLP 2026**: The generator must either genuinely target EMNLP 2026 with a 14-day feasible scope, or the idea fails the user's venue requirement. For a 14-day submission, scope to Llama 3.1 8B only, 50-60% MLP sparsity, and frame as 'quality improvement at same sparsity' rather than pushing to 70-75%. (2) **Reframe the contribution**: The evidence strongly suggests 70-75% MLP sparsity on native SwiGLU with ≤1% loss is unachievable. Instead, target 50-60% MLP sparsity and show that KL-distillation trained predictors achieve *better accuracy* than WINA/WAS/TEAL at the *same* sparsity level — this is what ShadowLLM demonstrated (15% accuracy improvement). This is a credible and publishable contribution. (3) **Directly address Polar Sparsity's finding**: Explain mechanistically why a KL-distillation trained predictor could extract useful MLP sparsity on SwiGLU when Polar Sparsity's BCE-trained router could not — or position the work as complementary (MLP at batch=1 + attention at batch>1). (4) **Add ActTail, MGLU, and DaSS** to landscape. (5) **Provide a concrete fallback**: If distillation doesn't push beyond training-free ceiling, the contribution is still the distillation framework + analysis of when learned predictors outperform heuristics. Make this explicit in the paper framing.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL MISSING COMPETITOR — FastForward (arXiv:2602.00397, Jan 2026): Trains a neural predictor (single-head attention + 2-layer MLP, bottleneck r=d_model/16) for FFN sparsity on SwiGLU models (LLaMA-3.1/3.2-1B/3B/8B, Qwen3-4B). Uses weighted BCE loss with exponential decay on positive neurons plus a separate error compensation network. Achieves 50% FFN sparsity with 1.45x prefill speedup and <1 point MMLU drop. This is the closest existing work to the proposal — it trains learned predictors on SwiGLU — and is not cited anywhere in the landscape.", "CRITICAL MISSING COMPETITOR — SPON/Resting Neurons (arXiv:2512.12744, ICML 2026): Uses the exact same KL-divergence distillation loss the proposal claims as its key innovation, applied to SwiGLU models (Llama-3-8B, Mistral-7B, Qwen3-8B/32B, Llama-3-70B). At 50% sparsity on Llama3-8B, SPON achieves 71.96 avg (vs WINA 70.97) — a ~1 point recovery. Critically, SPON has zero inference overhead (absorbed into bias) and trains in ~1 GPU-hour. While SPON uses static vectors rather than contextual predictors, it directly undermines the novelty claim of 'first to use KL-distillation for SwiGLU sparsity' and sets a very efficient baseline.", "UNSUPPORTED IMPROVEMENT TARGET: The proposal claims to recover '3-5 points of WINA's 6.8-point average drop at 50% sparsity,' but provides no empirical or theoretical evidence for this target. SPON — which uses the same KL-divergence loss — only recovers ~1 point at 50%. ShadowLLM's '15% improvement' was measured against DejaVu (2023 baseline), not against WINA-caliber 2025-2026 methods. The 3-5 point claim needs either preliminary experimental evidence or a principled argument for why contextual prediction unlocks significantly more recovery than static correction.", "TIMELINE CONTRADICTION: The generator's own manual estimate is '4-6 weeks' and auto_research is '10-14 days with 2-4 H100s.' Only 13 days remain until the May 25 ARR deadline. The manual estimate directly contradicts the claimed feasibility. For auto_research, the '10-14 days' estimate assumes continuous GPU availability and zero debugging setbacks — highly optimistic for a novel training paradigm.", "MISSING COMPETITOR — Spark Transformer (NeurIPS 2025): Reparameterizes existing FFN weights to form a low-cost predictor for identifying activated entries, achieving 2.5x FLOP reduction with 1.79x CPU / 1.40x GPU decoding speedup. Relevant as a training-free predictor approach that should be discussed in the landscape.", "POLAR SPARSITY CHARACTERIZATION STILL SLIGHTLY INACCURATE: The proposal quotes Polar Sparsity as concluding MLP sparsification is 'ineffective' on SwiGLU. The actual paper states SwiGLU 'yields denser activations and limits the benefits of sparsity' and 'MLP layers offer limited benefits' — 'limited' is not 'ineffective.' The distinction matters because 'limited benefits' is actually consistent with SPON's finding of ~1 point improvement, undermining the proposal's framing that Polar Sparsity's conclusion is wrong due to BCE training.", "BASELINE CODE AVAILABILITY RISK: WAS (EMNLP 2025), WiSparse (arXiv Feb 2026), and ActTail (arXiv Feb 2026) have no confirmed public code repositories. Reproducing three baselines from papers within 13 days adds significant risk. The proposal should either confirm code availability or reduce the baseline set to methods with verified code (TEAL, WINA, R-Sparse, ShadowLLM)."]
Feedback: The proposal has improved substantially from Round 2 — venue targeting, sparsity scope, kernel reuse, and fallback strategy are all addressed. However, two critical omissions must be fixed before this can pass:

(1) **Add FastForward and SPON as baselines and discuss them in the landscape.** FastForward is the closest direct competitor (trained predictor on SwiGLU); SPON uses the same KL-distillation loss on SwiGLU. The proposal must explain: (a) how it differs from FastForward (KL vs weighted BCE, decode vs prefill, contextual masks vs block-level prediction + error compensator), and (b) why contextual KL-trained predictors should recover significantly more accuracy than SPON's static KL-trained bias correction. Consider proposing a SPON + your predictor combination as an experiment.

(2) **Revise the improvement target with evidence.** '3-5 points' is not supported. Given that SPON recovers ~1 point with KL-distillation (static) and FastForward shows <1 point MMLU drop at 50% with BCE-trained predictors, the expected improvement is likely 1-3 points over training-free WINA, not 3-5. Either lower the target or provide a principled argument (e.g., analysis of input-dependent importance variance showing that contextual prediction captures significantly more information than static correction).

(3) **Resolve the timeline.** Either (a) acknowledge this requires auto_research mode with 2-4 concurrent H100s and high execution risk, or (b) scope down further: drop baselines without public code (keep TEAL, WINA, R-Sparse, ShadowLLM as the 4 training-free baselines + add SPON and FastForward as the 2 learned baselines), and start paper writing immediately with placeholder results.

(4) **Reframe novelty more precisely.** The novelty is NOT 'first KL-distillation for SwiGLU sparsity' (SPON does this) or 'first trained predictor for SwiGLU' (FastForward does this). The novelty is 'first contextual predictor trained via output-distribution distillation (KL) rather than activation-pattern prediction (BCE/MSE) on SwiGLU, with systematic comparison against both training-free and learned baselines using 2025-2026 SOTA.' This is more honest and still publishable if results support it.

### Round 4 review
Verdict: revise
Issues: ["SPARSITY DEFINITION INCONSISTENCY: The proposal targets '50% MLP sparsity' but cites SPON's Table 2 numbers (WINA 70.97, SPON 71.96) which are at 50% model-level activation sparsity (MLP + attention layers combined). These are different operating points — 50% MLP-only sparsity is less aggressive than 50% model-level sparsity. The improvement targets and baseline comparisons must use consistent sparsity definitions, or the claimed gaps are misleading.", "DENSE BASELINE NOT VERIFIED: The proposal claims 'the dense model's ~74.5' average on QA tasks, but the SPON paper's Table 2 (where the WINA 70.97 number comes from) does NOT include dense baselines. The ~74.5 figure appears to be estimated/unverified. The actual dense-to-sparse gap that the contextual predictor must close is uncertain from the cited data.", "IMPROVEMENT TARGET ARITHMETIC: The proposal claims '1.5-3 points total recovery over WINA' with '0.5-1.5 points from the contextual component over SPON.' SPON recovers ~1 point over WINA. So the total would be 1.5-2.5 points (1 from SPON + 0.5-1.5 from contextual). The upper bound of 3 points requires the contextual component to contribute 2 points, exceeding the stated 0.5-1.5 range. Minor inconsistency but undermines rigor.", "NO THEORETICAL ARGUMENT FOR KL > BCE IN CONTEXTUAL SETTING: The core hypothesis — that KL-trained contextual predictors outperform BCE-trained contextual predictors — lacks theoretical grounding. The proposal states KL 'captures cross-layer interaction effects on output distributions,' but doesn't explain why BCE-trained predictors can't learn equivalent masks through gradient flow. FastForward's error compensation network already addresses output quality post-hoc. The proposal needs at least an intuitive argument for why optimizing for output distributions directly (KL) produces better masks than optimizing for activation patterns (BCE) + error compensation.", "MISSING FROM LANDSCAPE: (1) DIP (MLSys 2025, arXiv 2412.01380) uses KL distillation for LoRA adapters alongside sparsity predictors — the closest existing system combining KL-distillation with sparsity, even though it trains different components. Should be discussed as partial precedent. (2) Sirius (NeurIPS 2024, arXiv 2409.03856) combines contextual sparsity with correction mechanisms — relevant to the SPON + predictor composition idea. (3) ActiveFlow (arXiv 2504.08378) introduces sparsity-aware self-distillation for activation sparsity recovery.", "TIMELINE RISK UNDERCHARACTERIZED: The auto_research estimate (10-13 days) assumes zero debugging setbacks. SPON reimplementation is described as 'architecturally trivial' but requires reproducing their Table 2 numbers to validate the reimplementation. FastForward's BCE predictor (used for ablation) requires careful implementation of their tiered weighting scheme. Both reimplementations need validation before they become reliable baselines, consuming precious days."]
Feedback: The proposal has improved substantially across four rounds — FastForward and SPON integration, honest novelty reframing, and scoped baselines are all good. To reach publication quality, address these priorities:

(1) **Fix the sparsity definition**: Decide whether you're comparing at 50% MLP-only sparsity or 50% model-level sparsity, and ensure ALL baselines use the same definition. If using MLP-only sparsity (your stated target), you cannot directly cite SPON's Table 2 numbers (which are model-level). Either re-run SPON at MLP-only sparsity as part of your experiments, or switch to model-level sparsity throughout.

(2) **Provide a mechanistic argument for KL > BCE**: The key differentiator is the training objective. Argue concretely: BCE optimizes per-neuron binary classification independently, so it cannot capture interactions between neurons or between layers — neuron A being pruned might only hurt quality when neuron B in the next layer is also pruned. KL on output logits captures these joint effects because gradients flow through the full forward pass. This is an information-theoretic argument: BCE's per-neuron decomposition is a mean-field approximation, while KL on the joint output preserves correlations. If this argument is correct, the KL advantage should be largest at high sparsity (where neuron interactions matter more) — make this a testable prediction.

(3) **Narrow evaluation scope for timeline**: Drop one sparsity level (keep 40% and 50%, drop 60% as stretch goal). Drop LongBench and RULER (the proposal mentions MMLU, GSM8K, HumanEval, PIQA, WinoGrande, HellaSwag, ARC-c — 7 benchmarks is sufficient for an efficiency paper). This saves ~30% evaluation time.

(4) **Make SPON + predictor composition the headline**: The most interesting and novel experiment is whether static KL correction (SPON) and contextual KL prediction compose additively. If they do, this is a practical recipe (apply both for best quality) with a clear insight (static correction fixes average-case drift, contextual prediction handles per-input variation). Lead with this rather than treating it as experiment (2) of four.

(5) **Add DIP to landscape**: DIP (MLSys 2025) uses KL distillation for LoRA recovery in a sparsity pipeline. It's the closest precedent for combining KL-distillation with activation sparsity, and contrasting with it sharpens your contribution (you train the predictor itself with KL, not a separate recovery module).

### Round 5 review
Verdict: revise
Issues: ["SPON VENUE UNVERIFIED: The proposal claims SPON is 'ICML 2026' but independent search found only the arXiv preprint (2512.12744) with no confirmed ICML 2026 acceptance. The paper may still be under review or accepted to a different venue. If ICML 2026 acceptance cannot be verified, label it as 'arXiv 2024' to avoid reviewer suspicion of fabricated venue claims.", "SPON BENCHMARK COUNT ERROR: The proposal states SPON achieves '71.96 vs 70.97 on five QA benchmarks' but SPON's Table 2 contains exactly 4 benchmarks (ARC-Challenge, ARC-Easy, BoolQ, PIQA). This minor factual error undermines the proposal's credibility on detailed claims. Verify and correct.", "FLOPS VS WALL-CLOCK MISLEADING: The 37:1 savings-to-overhead ratio is in FLOPs, but batch=1 decode is memory-bandwidth-bound, not compute-bound. The predictor adds ~151MB of weight reads (75.5M params × 2 bytes) across all layers. On H100, this translates to ~0.045ms per layer or ~1.4ms total overhead — versus perhaps 5-10ms savings from sparsity. The actual wall-clock ratio is likely 3-7:1, not 37:1. The proposal should report both FLOPs and estimated wall-clock ratios, or reviewers will flag this as misleading.", "BCE ABLATION FAIRNESS: The KL vs BCE ablation compares KL-trained predictor against BCE-trained predictor (same architecture, different loss). But FastForward's full system includes an error compensation network (2-layer MLP, r'=d_model/8) trained with MSE that partially addresses the output-quality concern KL handles directly. A fair comparison should include: (a) BCE only, (b) BCE + error compensation (FastForward's approach), (c) KL only. Without (b), the ablation is incomplete and reviewers may argue the KL advantage disappears when BCE is paired with error compensation.", "SPARK TRANSFORMER OMISSION: Spark Transformer (NeurIPS 2025) reparameterizes existing FFN weights to form low-cost predictors for identifying activated entries, achieving 2.5x FLOP reduction with 1.79x CPU decoding speedup. While it modifies architecture during pre-training (unlike the proposal's post-training approach), it should be discussed as related work since it also creates learned sparsity predictors from FFN parameters. Its omission may be flagged by reviewers familiar with the NeurIPS 2025 program.", "IMPROVEMENT TARGET STILL SPECULATIVE: The 2-4 point target relies on untested arithmetic: 1 (SPON) + 1-2 (contextual) + 0-1 (composition bonus). The contextual contribution estimate (1-2 points) is loosely grounded in FastForward's near-dense MMLU at 50% FFN sparsity, but FastForward uses FFN-only sparsity (a less aggressive operating point than model-level) AND includes an error compensation network. Extrapolating from FastForward's FFN-only results to model-level sparsity without error compensation may overestimate the contextual component's contribution.", "TIMELINE RISK FOR PAPER WRITING: The auto_research timeline (9-12 days) accounts only for experiments. A full EMNLP paper with related work, methodology, results, analysis, and ablation studies requires substantial writing effort. With experiments finishing on day 10-12 of 14, there is essentially 2-4 days for paper writing — very tight even with auto assistance. Consider whether partial results + clear story might be submitted, with full results provided during the author response period."]
Feedback: The proposal has matured substantially over 5 rounds and the core research direction is sound. To reach 'pass' quality, address these priorities:

(1) **Add BCE + error compensation ablation**: Include a third condition in the KL vs BCE ablation — BCE + error compensation (FastForward's approach). This is critical because FastForward's error compensation network explicitly addresses the output-quality preservation that KL handles implicitly. Without this comparison, reviewers will question whether KL's advantage is real or merely because BCE was tested without its intended companion mechanism. This strengthens the paper significantly if KL still wins.

(2) **Report wall-clock overhead, not just FLOPs**: The 37:1 FLOPs ratio is technically correct but misleading for batch=1 decode (memory-bound regime). Add a paragraph estimating wall-clock predictor overhead: ~151MB weight reads at H100's 3.3 TB/s = ~0.045ms/layer, ~1.4ms total, versus estimated 5-10ms savings. A realistic 3-7:1 wall-clock ratio is still attractive and much more honest.

(3) **Formalize the mean-field argument**: The KL > BCE argument is the proposal's key intellectual insight. Currently it's informal ('BCE treats neurons independently, KL captures correlations'). Strengthen it: define BCE's loss decomposition explicitly (L_BCE = Σ_j l(y_j, s_j) decomposes across neurons), show this is equivalent to a mean-field factorization that ignores joint effects, and contrast with KL which backpropagates through the full sparse forward pass. Derive the testable prediction mathematically: at higher sparsity, more neuron-neuron interaction effects emerge (because more neurons are pruned), so KL's advantage should increase. This elevates the contribution from 'empirical observation' to 'principled insight' and could push novelty from 3.5 to 4.

(4) **Verify SPON venue and benchmark count**: Either confirm ICML 2026 acceptance with a citation, or label as 'arXiv 2024.' Fix the '5 QA benchmarks' claim to match the actual 4 benchmarks in Table 2. These are small fixes but protect credibility.

(5) **Add Spark Transformer to landscape**: One sentence suffices: 'Spark Transformer (NeurIPS 2025) reparameterizes FFN weights during pre-training to form implicit predictors, achieving 1.79x decode speedup — complementary to our post-training approach which works on frozen models.'

(6) **Narrow the experimental scope for timeline**: Drop the rank sweep (keep r=128 only) and drop 40% sparsity evaluations. Focus on 50% model-level sparsity only. This cuts training configurations from 12 to 3 (KL-r128, BCE-r128, BCE+compensation-r128) and evaluation by 50%, saving ~3-4 days for paper writing. Add rank sweep and 40% as supplementary if time permits.

### Round 6 review
Verdict: revise
Issues: ["BENCHMARK MISMATCH WITH USER REQUIREMENTS: The user explicitly requires evaluation on perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, and MT-Bench. The proposal evaluates on PIQA, ARC-c, WinoGrande, HellaSwag, MMLU, GSM8K, and HumanEval — covering only 2 of 6 required benchmarks. Missing perplexity (trivial to add), LongBench and RULER (important for testing whether the sparsity predictor generalizes to long contexts, especially given training on short SlimPajama sequences), and MT-Bench (instruction-following quality under sparsity). This is a significant gap versus user requirements.", "COMPENSATION NETWORK WEIGHT CALCULATION ERROR: The proposal states 'FastForward's compensation MLP adds ~4.72 MB of weights per layer.' With r'=d_model/8=512 on Llama-3.1-8B (d_model=4096), the compensation network has Wcomp1 (4096×512) + Wcomp2 (512×4096) = 4,194,304 params × 2 bytes (FP16) ≈ 8.0 MB per layer, not 4.72 MB. The 4.72 MB figure suspiciously matches the predictor's own weight footprint (2.36M params × 2 bytes = 4.72 MB), suggesting a copy-paste error. This actually strengthens the proposal's argument (compensation overhead is even higher), but the factual error undermines credibility.", "MLP VS ATTENTION SPARSITY ALLOCATION UNSPECIFIED: At 50% model-level sparsity, the budget must be distributed between MLP and attention layers. The proposal states 'attention layers use training-free WINA-style heuristic pruning to match the model-level sparsity budget' but doesn't specify the MLP/attention allocation ratio. WINA uses a learned per-layer allocation via weight-informed scoring. Since the proposal's predictor only targets MLP blocks, the effective MLP sparsity could be significantly higher than 50% (if most of the budget is allocated to MLP) or lower (if attention absorbs significant sparsity). This allocation directly affects the improvement target arithmetic and should be specified.", "SPON ICML 2026 VENUE: ArXiv metadata lists ICML 2026 and v3 was updated April 30 (coinciding with notification dates), but the paper text itself does not mention ICML 2026, and no official ICML 2026 accepted paper list confirmation was found. The proposal is transparent about the evidence basis ('venue confirmed via arXiv metadata updated on the April 30 notification date'), which is adequate. Minor concern — recommend adding 'per arXiv metadata' qualifier.", "NO LONG-CONTEXT EVALUATION RISKS MISSING A KEY FAILURE MODE: The predictor is trained on SlimPajama calibration data (presumably short sequences). LongBench and RULER would test whether the learned neuron importance patterns generalize to long-context settings. If the predictor overfits to short-context activation patterns, it could fail catastrophically on long sequences — a plausible failure mode that the current benchmark set would not detect. This is both a user-requirement gap and a scientific gap."]
Feedback: The proposal is genuinely close to passing (Round 6 of 10) and has addressed every major issue from prior rounds excellently. Three changes would push this over the threshold:

(1) **Align benchmarks with user requirements**: Add perplexity (Wiki/C4) — this is trivial and standard for sparsity papers. Add at least one long-context benchmark (LongBench or RULER) to test predictor generalization beyond training distribution. Add MT-Bench for instruction-following quality. Drop PIQA and HellaSwag if needed to manage evaluation time — these are less discriminative for sparsity methods. The resulting set (perplexity, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval, MT-Bench, LongBench) covers the user's requirements while staying manageable.

(2) **Fix the compensation network weight calculation**: Replace '~4.72 MB' with '~8.0 MB' (or compute exactly). This strengthens your argument — the compensation network is heavier than you claimed, making the KL-without-compensation alternative even more attractive. Also specify the MLP/attention sparsity allocation: state whether you use WINA's per-layer allocation or a fixed split, and what the effective MLP sparsity is at 50% model-level.

(3) **Briefly discuss long-context generalization**: Add one sentence acknowledging that the predictor is trained on short sequences and that LongBench/RULER results will test generalization. If long-context performance degrades, this is itself a finding (predictor-based sparsity may require context-length-aware training). This also makes the paper more relevant to the user's interest in 'cache-aware methods for new workloads (long thinking traces, agent loops, RAG).'

### Round 7 review
Verdict: revise
Issues: ["RULER EVALUATION MISSING: The user explicitly requires evaluation on 'perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench.' The proposal covers all except RULER. RULER tests specific long-context capabilities (retrieval, multi-hop reasoning at various context lengths) that complement LongBench's task-level evaluation. Adding RULER is important both for user requirement compliance and scientific completeness — RULER's needle-in-a-haystack tasks would provide a fine-grained diagnostic of whether sparsity disproportionately impairs retrieval capabilities in long contexts.", "MISSING COMPETITOR — IFPruning (arXiv 2501.02086, Jan 2025): Trains a 302M-parameter sparsity predictor that combines instruction-level (quasi-static) with input-level (contextual) sparsity selection, co-optimizing the predictor and LLM end-to-end. While it operates at a different granularity (instruction-level vs token-level) and uses cross-entropy rather than KL distillation, it directly overlaps with the claim of 'composing static and contextual corrections.' The proposal should cite it and explain the distinction: IFPruning's static component is task-description-conditioned (requiring instruction input), while SPON's is truly input-independent (absorbed into bias terms with zero overhead).", "DIP DISTILLATION LOSS IMPRECISION: The proposal characterizes DIP as using 'KL-distillation for LoRA adapters,' but the DIP paper only states 'knowledge distillation loss to match the original (dense) model logits' without explicitly naming KL divergence. While KL is the standard distillation formulation, attributing a specific loss function the paper doesn't name undermines the proposal's otherwise meticulous accuracy. Change to 'logit-matching distillation' or 'knowledge distillation (likely KL, though unspecified).'"]
Feedback: The proposal is very close to passing (Round 7 of 10) and has addressed every major concern from prior rounds. Three minor fixes would push it over the threshold:

(1) **Add RULER to evaluation**: The user explicitly requires it. RULER's synthetic tasks (needle-in-a-haystack, variable tracking, multi-hop retrieval) at controlled context lengths (4K-128K) would provide diagnostic insight that LongBench's natural-language tasks don't capture. RULER evaluation is lightweight (small dataset, deterministic scoring) and would add <2 hours of GPU time. This also strengthens the long-context generalization story — if the KL-trained predictor maintains retrieval accuracy while BCE degrades, that's strong evidence for the mean-field hypothesis in the long-context setting.

(2) **Cite IFPruning and sharpen the composition novelty claim**: Add one sentence: 'IFPruning (arXiv 2501.02086) co-trains a predictor combining instruction-level (quasi-static) and input-level sparsity, but requires task-description input and modifies the base LLM. Our composition is between an input-independent bias correction (zero overhead, folded into bias terms) and a lightweight contextual predictor, both applied post-training to frozen models.' This inoculates against reviewers who know IFPruning.

(3) **Fix DIP characterization**: Change 'KL-distillation' to 'logit-matching knowledge distillation (loss function unspecified in paper, likely KL).' This is a small fix but maintains the proposal's credibility on detailed claims.

All three fixes are minor and can be done in one revision cycle. The proposal's core experimental design, novelty framing, and feasibility analysis are all strong.


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
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "type": "user",
  "uuid": "3394149c-36c0-47de-860b-7fb62b209a86",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T03:46:03.403Z_

```json
{
  "parentUuid": "3394149c-36c0-47de-860b-7fb62b209a86",
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
  "uuid": "adbcabac-bda5-428c-aa83-0c751874fa0e",
  "timestamp": "2026-05-12T03:46:03.403Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T03:46:03.403Z_

```json
{
  "parentUuid": "adbcabac-bda5-428c-aa83-0c751874fa0e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cc9bc14e-5777-4e1b-bf50-8857165fe612",
  "timestamp": "2026-05-12T03:46:03.403Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
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
  "leafUuid": "cc9bc14e-5777-4e1b-bf50-8857165fe612",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Composing Static and Contextual Corrections for Activation Sparsity in SwiGLU LLMs via Output-Distribution Distillation",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

### Assistant

_source line 8 · 2026-05-12T03:46:18.018Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea, which is now in Round 8 of 10. I need to independently verify claims, check for missing competitors, and assess whether the issues from Round 7 have been addressed.

Let me start by understanding what the Round 7 reviewer asked for:
1. Add RULER to evaluation
2. Cite IFPruning and sharpen composition novelty
3. Fix DIP characterization

Let me check the current proposal to see if these were addressed:

1. **RULER**: Yes, RULER is now included in the evaluation (mentioned multiple times - "RULER (COLM 2024) — synthetic long-context evaluation with 13 tasks across 4 categories")


2. **IFPruning**: Yes, now cited and discussed ("IFPruning (arXiv 2501.02086, Jan 2025) trains a 302M-parameter sparsity predictor...")
3. **DIP characterization**: Yes, fixed ("DIP (MLSys 2025) achieves predictor-free dynamic pruning on SwiGLU at ~40% speedup plus LoRA adapters trained via logit-matching knowledge distillation (loss function unspecified in paper, likely KL)")

Good, all three Round 7 issues appear to be addressed. Now I'm checking the current state-of-the-art in activation pruning and looking for any missing competitors or gaps in the evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc9bc14e-5777-4e1b-bf50-8857165fe612",
  "isSidechain": false,
  "requestId": "req_011CawzFwbe6p3aaxt2GJauq",
  "type": "assistant",
  "uuid": "e8eac132-6da4-48c0-bf53-964a41e6ae8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXn5wnFjr36vdn5MQqkY1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28890,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28890,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1945,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28890
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

_source line 9 · 2026-05-12T03:46:18.053Z_

I'll conduct an independent review of this proposal, which is now in Round 8 of 10. The Round 7 reviewer asked for three specific fixes (add RULER, cite IFPruning, fix DIP characterization). Let me verify these were addressed and check for any remaining issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8eac132-6da4-48c0-bf53-964a41e6ae8a",
  "isSidechain": false,
  "requestId": "req_011CawzFwbe6p3aaxt2GJauq",
  "type": "assistant",
  "uuid": "e33b361f-6bd2-4233-b469-3d1a5b8e03f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXn5wnFjr36vdn5MQqkY1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28890,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28890,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1945,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28890
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

_source line 10 · 2026-05-12T03:46:22.766Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012Xgd6ownQm6bVye7bqdDLR`</summary>

```json
{
  "description": "Verify SPON/Resting Neurons claims",
  "subagent_type": "general-purpose",
  "prompt": "Search for and verify the following claims about the paper \"Resting Neurons, Active Insights (SPON)\" (arXiv 2512.12744):\n\n1. Does it use KL-divergence distillation for training?\n2. What benchmarks does it report in Table 2, and how many are there? (Previous review flagged it as having 4 benchmarks in Table 2, but the proposal now says 5: ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande)\n3. Is it accepted at ICML 2026? Check arXiv metadata, any conference announcements.\n4. What are the actual numbers reported (WINA vs SPON at 50% sparsity)?\n5. Does SPON report perplexity on WikiText?\n\nUse WebSearch to find the paper and WebFetch to read its abstract and key sections. Try multiple searches:\n- \"Resting Neurons Active Insights SPON arXiv 2512.12744\"\n- \"SPON activation sparsity ICML 2026\"\n- \"site:arxiv.org 2512.12744\"\n\nReport findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e33b361f-6bd2-4233-b469-3d1a5b8e03f9",
  "isSidechain": false,
  "requestId": "req_011CawzFwbe6p3aaxt2GJauq",
  "type": "assistant",
  "uuid": "47c0317d-cd92-46c6-a7d1-693a61ab78c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXn5wnFjr36vdn5MQqkY1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28890,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28890,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1945,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28890
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

_source line 11 · 2026-05-12T03:46:28.456Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KyoPr2WGp5DVuYY5mzcusA`</summary>

```json
{
  "description": "Verify FastForward paper claims",
  "subagent_type": "general-purpose",
  "prompt": "Search for and verify the following claims about the paper \"FastForward: Accelerating LLM Prefill with Predictive FFN Sparsity\" (arXiv 2602.00397):\n\n1. Does it use weighted BCE loss for training predictors?\n2. Does it have an error compensation network (2-layer MLP, r'=d_model/8)?\n3. What MMLU score does it achieve at 50% FFN sparsity on Llama-3.1-8B? (claim: 67.17 vs 67.84 dense)\n4. Does the compensation network operate at inference time (not just training)?\n5. Does it evaluate on LongBench?\n6. What's the predictor architecture? (claimed: single-head attention + 2-layer MLP, bottleneck r=d_model/16)\n\nUse WebSearch to find the paper and WebFetch to read its content. Try:\n- \"FastForward predictive FFN sparsity arXiv 2602.00397\"\n- \"FastForward LLM prefill sparsity 2026\"\n- \"site:arxiv.org 2602.00397\"\n\nReport all findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47c0317d-cd92-46c6-a7d1-693a61ab78c9",
  "isSidechain": false,
  "requestId": "req_011CawzFwbe6p3aaxt2GJauq",
  "type": "assistant",
  "uuid": "65f15b9c-9c1b-49d3-997b-b6cd8b1f7d27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXn5wnFjr36vdn5MQqkY1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28890,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28890,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1945,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28890
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

_source line 12 · 2026-05-12T03:46:36.156Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AXz6mas2FJy2QLP4doYPj5`</summary>

```json
{
  "description": "Search for missing competitors 2026",
  "subagent_type": "general-purpose",
  "prompt": "Search for very recent (2025-2026) papers on activation sparsity for LLMs that might be missing from a proposal's landscape. The proposal already covers: WINA, TEAL, R-Sparse, WAS, WiSparse, ActTail, SPON, FastForward, IFPruning, ShadowLLM, Sirius, Spark Transformer, Polar Sparsity, MaskLLM, DIP, DaSS, ActiveFlow, SVD Contextual Sparsity Predictors, CATS, Deja Vu.\n\nSpecifically search for:\n1. Any new activation sparsity papers from March-May 2026 on arXiv\n2. Papers combining KL-divergence distillation with sparsity predictors\n3. Papers composing static and contextual sparsity corrections\n4. ICML 2026 accepted papers on efficient inference / activation sparsity\n5. ACL 2026 papers on efficient NLP methods\n\nTry these searches:\n- \"activation sparsity LLM 2026 arXiv\"\n- \"KL divergence sparsity predictor training LLM\"\n- \"static contextual sparsity composition LLM\"\n- \"ICML 2026 activation sparsity efficient inference\"\n- \"SwiGLU sparsity predictor 2026\"\n- \"learned sparsity predictor LLM decode 2026\"\n\nReport any papers NOT in the list above that are relevant."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65f15b9c-9c1b-49d3-997b-b6cd8b1f7d27",
  "isSidechain": false,
  "requestId": "req_011CawzFwbe6p3aaxt2GJauq",
  "type": "assistant",
  "uuid": "0a576375-b724-41d0-a1d9-ac92348015c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXn5wnFjr36vdn5MQqkY1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28890,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28890,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1945,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28890
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

_source line 13 · 2026-05-12T03:46:41.470Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01W24hBmf6A6bUBZWMEa82Kt`</summary>

```json
{
  "description": "Verify RULER benchmark details",
  "subagent_type": "general-purpose",
  "prompt": "Search for and verify details about the RULER benchmark for long-context evaluation:\n\n1. Is RULER from COLM 2024? (arXiv 2404.06654)\n2. Does it have 13 tasks across 4 categories (Retrieval, Multi-hop Tracing, Aggregation, QA)?\n3. Is there an open-source evaluation codebase at github.com/NVIDIA/RULER?\n4. What context lengths does it support?\n5. How many examples per task (claimed: 500)?\n6. Is scoring recall-based?\n\nAlso check:\n- Has RULER been used to evaluate activation sparsity methods before?\n- Is RULER evaluation computationally lightweight as claimed?\n\nTry:\n- \"RULER long context benchmark COLM 2024\"\n- \"site:arxiv.org 2404.06654\"\n- \"NVIDIA RULER benchmark github\"\n- \"RULER needle haystack evaluation\"\n\nReport findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a576375-b724-41d0-a1d9-ac92348015c4",
  "isSidechain": false,
  "requestId": "req_011CawzFwbe6p3aaxt2GJauq",
  "type": "assistant",
  "uuid": "5cae0991-da14-4c84-8986-8b1d65b742b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXn5wnFjr36vdn5MQqkY1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28890,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28890,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1945,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28890
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

_source line 14 · 2026-05-12T03:47:52.692Z_

<details><summary>↩ Tool result · `toolu_01KyoPr2WGp5DVuYY5mzcusA`</summary>

```text
I now have comprehensive information to verify all six claims. Here is my detailed report:

---

## Verification Results for "FastForward: Accelerating LLM Prefill with Predictive FFN Sparsity" (arXiv 2602.00397)

Paper confirmed at: [https://arxiv.org/abs/2602.00397](https://arxiv.org/abs/2602.00397) | Full HTML: [https://arxiv.org/html/2602.00397](https://arxiv.org/html/2602.00397)

---

### Claim 1: Weighted BCE loss for training predictors

**VERIFIED -- TRUE.**

The paper uses a weighted Binary Cross-Entropy loss for training the expert predictors. The exact formulation is:

L_pred^(l) = -sum_j w_j [ y_j log sigma(s_j) + (1 - y_j) log(1 - sigma(s_j)) ]

The weighting scheme is tiered: the top 20% of neurons (by activation magnitude) receive weight 32, the next 20% receive weight 16, and so on in decreasing tiers. All negative labels (bottom 50%) receive weight 1. Labels are binary: 1 for top-50% activations, 0 for bottom-50%.

---

### Claim 2: Error compensation network (2-layer MLP, r' = d_model/8)

**VERIFIED -- TRUE.**

The error compensation network is a two-layer feedforward network with formulation:

Y_comp = W_comp2 * sigma(W_comp1 * X^{l,i})

The bottleneck dimension is r' = d_model / 8, where W_comp1 is in R^{d_model x r'} and W_comp2 is in R^{r' x d_model}. The training loss for the compensator is an L2 reconstruction loss: L_comp^(l) = ||Y_dense - Y||_2^2. Training uses a two-phase warm-start procedure on Minipile (10,000 steps, batch size 512): first with oracle top-K masks, then transitioning to learned predictor masks.

---

### Claim 3: MMLU score at 50% FFN sparsity on Llama-3.1-8B (claimed: 67.17 vs 67.84 dense)

**VERIFIED -- TRUE.**

The paper reports in Table 3:
- **Dense baseline (Llama-3.1-8B):** 67.84%
- **FastForward at 50% FFN sparsity:** 67.17%
- This is a drop of only 0.67 percentage points (less than 1% relative).

---

### Claim 4: Compensation network operates at inference time (not just training)

**VERIFIED -- TRUE.**

The compensation network operates at inference time as part of the forward pass. The corrected output is computed as:

Y = FFN_hat(X^{l,i}) + Y_comp

This additive correction is applied during inference, not just during training. The paper does not describe removing it at inference time, and the ablation study (Table 6) shows its contribution to final accuracy (e.g., +3.20 points on Llama-3B LongBench at 50% sparsity). However, the paper does not provide separate timing measurements for the compensator's inference overhead.

---

### Claim 5: Evaluates on LongBench

**VERIFIED -- TRUE.**

LongBench is the primary evaluation benchmark. Results at 50% FFN sparsity include:
- **Llama-3.1-8B:** 46.78 (dense: 49.76, -5.99% relative gap)
- **Llama-3.2-3B:** 42.54 (dense: 44.72, -4.86% gap)
- **Llama-3.2-1B:** 28.37 (dense: 29.88, -5.07% gap)
- **Qwen-3-4B:** 40.36 (dense: 41.26, -2.18% gap)

LongBench evaluation covers multiple task categories: Single Doc QA, Multi Doc QA, Summarization, Few-shot, Synthetic, and Code. The paper evaluates on only two benchmarks total: LongBench and MMLU.

---

### Claim 6: Predictor architecture (single-head attention + 2-layer MLP, bottleneck r = d_model/16)

**VERIFIED -- TRUE.**

The predictor consists of two components:

1. **Single-head attention** with a trainable query q_pred in R^{1 x d_model}:
   - a = Softmax(q_pred * X^{l,i T} / sqrt(d_model)) * X^{l,i}

2. **Two-layer MLP** with bottleneck r = d_model / 16:
   - s = ReLU(a * W_pred1) * W_pred2
   - W_pred1 in R^{d_model x r}, W_pred2 in R^{r x d_ffn}
   - Concrete values: r = 128 for LLaMA-1B, r = 256 for LLaMA-3B/8B

Expert selection uses top-K scores from the output vector s.

---

### Summary

All six claims are **confirmed as accurate** based on the paper's content:

| # | Claim | Status |
|---|-------|--------|
| 1 | Weighted BCE loss for predictors | Confirmed (tiered weights: 32/16/... for top activations) |
| 2 | Compensation network: 2-layer MLP, r'=d_model/8 | Confirmed |
| 3 | MMLU: 67.17 vs 67.84 dense at 50% sparsity (Llama-3.1-8B) | Confirmed |
| 4 | Compensation network at inference time | Confirmed (additive correction in forward pass) |
| 5 | LongBench evaluation | Confirmed (primary benchmark) |
| 6 | Predictor: single-head attention + 2-layer MLP, r=d_model/16 | Confirmed |

Sources:
- [FastForward arXiv abstract](https://arxiv.org/abs/2602.00397)
- [FastForward full HTML paper](https://arxiv.org/html/2602.00397)

agentId: a44b1b2530c7e8d94 (use SendMessage with to: 'a44b1b2530c7e8d94' to continue this agent)
&lt;usage>total_tokens: 18958
tool_uses: 8
duration_ms: 84231&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65f15b9c-9c1b-49d3-997b-b6cd8b1f7d27",
  "isSidechain": false,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "type": "user",
  "uuid": "ea481fa0-e69b-4d4a-b934-34e7da537ccc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify the following claims about the paper \"FastForward: Accelerating LLM Prefill with Predictive FFN Sparsity\" (arXiv 2602.00397):\n\n1. Does it use weighted BCE loss for training predictors?\n2. Does it have an error compensation network (2-layer MLP, r'=d_model/8)?\n3. What MMLU score does it achieve at 50% FFN sparsity on Llama-3.1-8B? (claim: 67.17 vs 67.84 dense)\n4. Does the compensation network operate at inference time (not just training)?\n5. Does it evaluate on LongBench?\n6. What's the predictor architecture? (claimed: single-head attention + 2-layer MLP, bottleneck r=d_model/16)\n\nUse WebSearch to find the paper and WebFetch to read its content. Try:\n- \"FastForward predictive FFN sparsity arXiv 2602.00397\"\n- \"FastForward LLM prefill sparsity 2026\"\n- \"site:arxiv.org 2602.00397\"\n\nReport all findings in detail.",
    "agentId": "a44b1b2530c7e8d94",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to verify all six claims. Here is my detailed report:\n\n---\n\n## Verification Results for \"FastForward: Accelerating LLM Prefill with Predictive FFN Sparsity\" (arXiv 2602.00397)\n\nPaper confirmed at: [https://arxiv.org/abs/2602.00397](https://arxiv.org/abs/2602.00397) | Full HTML: [https://arxiv.org/html/2602.00397](https://arxiv.org/html/2602.00397)\n\n---\n\n### Claim 1: Weighted BCE loss for training predictors\n\n**VERIFIED -- TRUE.**\n\nThe paper uses a weighted Binary Cross-Entropy loss for training the expert predictors. The exact formulation is:\n\nL_pred^(l) = -sum_j w_j [ y_j log sigma(s_j) + (1 - y_j) log(1 - sigma(s_j)) ]\n\nThe weighting scheme is tiered: the top 20% of neurons (by activation magnitude) receive weight 32, the next 20% receive weight 16, and so on in decreasing tiers. All negative labels (bottom 50%) receive weight 1. Labels are binary: 1 for top-50% activations, 0 for bottom-50%.\n\n---\n\n### Claim 2: Error compensation network (2-layer MLP, r' = d_model/8)\n\n**VERIFIED -- TRUE.**\n\nThe error compensation network is a two-layer feedforward network with formulation:\n\nY_comp = W_comp2 * sigma(W_comp1 * X^{l,i})\n\nThe bottleneck dimension is r' = d_model / 8, where W_comp1 is in R^{d_model x r'} and W_comp2 is in R^{r' x d_model}. The training loss for the compensator is an L2 reconstruction loss: L_comp^(l) = ||Y_dense - Y||_2^2. Training uses a two-phase warm-start procedure on Minipile (10,000 steps, batch size 512): first with oracle top-K masks, then transitioning to learned predictor masks.\n\n---\n\n### Claim 3: MMLU score at 50% FFN sparsity on Llama-3.1-8B (claimed: 67.17 vs 67.84 dense)\n\n**VERIFIED -- TRUE.**\n\nThe paper reports in Table 3:\n- **Dense baseline (Llama-3.1-8B):** 67.84%\n- **FastForward at 50% FFN sparsity:** 67.17%\n- This is a drop of only 0.67 percentage points (less than 1% relative).\n\n---\n\n### Claim 4: Compensation network operates at inference time (not just training)\n\n**VERIFIED -- TRUE.**\n\nThe compensation network operates at inference time as part of the forward pass. The corrected output is computed as:\n\nY = FFN_hat(X^{l,i}) + Y_comp\n\nThis additive correction is applied during inference, not just during training. The paper does not describe removing it at inference time, and the ablation study (Table 6) shows its contribution to final accuracy (e.g., +3.20 points on Llama-3B LongBench at 50% sparsity). However, the paper does not provide separate timing measurements for the compensator's inference overhead.\n\n---\n\n### Claim 5: Evaluates on LongBench\n\n**VERIFIED -- TRUE.**\n\nLongBench is the primary evaluation benchmark. Results at 50% FFN sparsity include:\n- **Llama-3.1-8B:** 46.78 (dense: 49.76, -5.99% relative gap)\n- **Llama-3.2-3B:** 42.54 (dense: 44.72, -4.86% gap)\n- **Llama-3.2-1B:** 28.37 (dense: 29.88, -5.07% gap)\n- **Qwen-3-4B:** 40.36 (dense: 41.26, -2.18% gap)\n\nLongBench evaluation covers multiple task categories: Single Doc QA, Multi Doc QA, Summarization, Few-shot, Synthetic, and Code. The paper evaluates on only two benchmarks total: LongBench and MMLU.\n\n---\n\n### Claim 6: Predictor architecture (single-head attention + 2-layer MLP, bottleneck r = d_model/16)\n\n**VERIFIED -- TRUE.**\n\nThe predictor consists of two components:\n\n1. **Single-head attention** with a trainable query q_pred in R^{1 x d_model}:\n   - a = Softmax(q_pred * X^{l,i T} / sqrt(d_model)) * X^{l,i}\n\n2. **Two-layer MLP** with bottleneck r = d_model / 16:\n   - s = ReLU(a * W_pred1) * W_pred2\n   - W_pred1 in R^{d_model x r}, W_pred2 in R^{r x d_ffn}\n   - Concrete values: r = 128 for LLaMA-1B, r = 256 for LLaMA-3B/8B\n\nExpert selection uses top-K scores from the output vector s.\n\n---\n\n### Summary\n\nAll six claims are **confirmed as accurate** based on the paper's content:\n\n| # | Claim | Status |\n|---|-------|--------|\n| 1 | Weighted BCE loss for predictors | Confirmed (tiered weights: 32/16/... for top activations) |\n| 2 | Compensation network: 2-layer MLP, r'=d_model/8 | Confirmed |\n| 3 | MMLU: 67.17 vs 67.84 dense at 50% sparsity (Llama-3.1-8B) | Confirmed |\n| 4 | Compensation network at inference time | Confirmed (additive correction in forward pass) |\n| 5 | LongBench evaluation | Confirmed (primary benchmark) |\n| 6 | Predictor: single-head attention + 2-layer MLP, r=d_model/16 | Confirmed |\n\nSources:\n- [FastForward arXiv abstract](https://arxiv.org/abs/2602.00397)\n- [FastForward full HTML paper](https://arxiv.org/html/2602.00397)"
      }
    ],
    "totalDurationMs": 84231,
    "totalTokens": 18958,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 16477,
      "output_tokens": 1577,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 903
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1577,
          "cache_read_input_tokens": 16477,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 903,
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
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "65f15b9c-9c1b-49d3-997b-b6cd8b1f7d27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T03:48:37.534Z_

<details><summary>↩ Tool result · `toolu_012Xgd6ownQm6bVye7bqdDLR`</summary>

```text
I now have all the information needed. Here is my comprehensive report.

---

## Detailed Findings on "Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models" (arXiv 2512.12744)

**Paper metadata:**
- Authors: Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma
- Submitted: December 14, 2025 (v1); latest version: April 30, 2026 (v3)
- Note: The title changed between versions -- v1 used "Improving Input Sparsification" while v3 uses "Robustify Activation Sparsity"

---

### 1. Does it use KL-divergence distillation for training?

**Yes.** The paper explicitly uses KL divergence as its training objective. The loss function is:

`L(A) = E_{u~D}[D_KL(sigma(z(u)) || sigma(z_tilde(u;A)))]`

This minimizes the KL divergence between the dense model's output distribution and the sparse model's output distribution over calibration data. The paper calls this approach **"distribution matching"** rather than "knowledge distillation," though Section 2.3 does state the objective "effectively distills global, input-agnostic information from the dense model into the SPON parameters." So while the mechanism is effectively a form of KL-divergence distillation, the authors primarily frame it as distribution matching.

---

### 2. Benchmarks in Table 2 -- How many and which ones?

**There are 5 benchmarks in Table 2**, confirming the proposal's claim (not 4 as the previous review flagged):

1. ARC-Challenge
2. ARC-Easy
3. BoolQ
4. PIQA (styled as "PiQA" in the paper)
5. Winogrande

Table 2 also includes an **Average** column. The table covers multiple methods (LaRoSA, WINA, R-Sparse, WAS, SPON) across multiple models (Llama3-8B, Mistral-7B) at 50% sparsity.

---

### 3. Is it accepted at ICML 2026?

**The arXiv abstract page's "Comments" field says "ICML 2026"**, which is the standard convention authors use to indicate acceptance. This was confirmed via direct fetch of the arXiv abstract page metadata. However:

- The HTML body of the paper (v3) does not contain an explicit "Published at ICML 2026" header (unlike some camera-ready versions).
- The paper does not appear in the sampled ICML 2026 highlights on Paper Digest (which only covers ~500 of 6,500+ accepted papers).
- The ICML virtual site paper listing was not searchable via web fetch (it loads dynamically).
- No OpenReview listing was found for this paper.

**Assessment:** The "ICML 2026" comment on arXiv is a strong indicator of acceptance, as this is the standard practice for accepted papers. ICML 2026 is scheduled for July 6-11, 2026 in Seoul, and the v3 update on April 30, 2026 is consistent with a camera-ready revision timeline. However, I could not find a second independent confirmation (e.g., OpenReview decision, ICML virtual proceedings listing). The claim is **plausible but not independently verified beyond arXiv metadata**.

---

### 4. Actual numbers: WINA vs SPON at 50% sparsity

**Llama3-8B at 50% sparsity:**

| Benchmark | WINA | SPON | Difference |
|-----------|------|------|-----------|
| ARC-Challenge | 48.81% | 51.11% | +2.30 |
| ARC-Easy | 75.00% | 76.89% | +1.89 |
| BoolQ | 81.25% | 82.54% | +1.29 |
| PIQA | 79.16% | 78.40% | -0.76 |
| Winogrande | 70.64% | 70.88% | +0.24 |
| **Average** | **70.97%** | **71.96%** | **+0.99** |

**Mistral-7B at 50% sparsity:**

| Benchmark | WINA | SPON | Difference |
|-----------|------|------|-----------|
| ARC-Challenge | 52.30% | 56.31% | +4.01 |
| ARC-Easy | 77.57% | 81.02% | +3.45 |
| BoolQ | 81.59% | 84.98% | +3.39 |
| PIQA | 81.34% | 82.05% | +0.71 |
| Winogrande | 70.88% | 70.48% | -0.40 |
| **Average** | **72.74%** | **74.97%** | **+2.23** |

Notable: SPON does not uniformly beat WINA on every benchmark -- it loses on PIQA for Llama3-8B and Winogrande for Mistral-7B, though it wins on average.

---

### 5. Does SPON report perplexity on WikiText?

**Yes.** Table 1 reports WikiText language modeling perplexity across multiple sparsity levels. Key numbers at 50% sparsity:

| Model | Full Dense (0%) | TEAL (50%) | SPON (50%) |
|-------|----------------|-----------|-----------|
| Llama3-1B | 12.14 | 17.03 | 15.43 |
| Llama3-8B | 6.75 | 8.34 | 7.83 |
| Mistral-7B | 5.49 | 6.00 | 5.86 |
| Qwen3-8B | 8.99 | 9.75 | 9.26 |

SPON consistently outperforms TEAL at 50% sparsity on WikiText perplexity. Results at 25% and 60% sparsity are also reported.

---

### Summary of Claim Verification

| Claim | Status |
|-------|--------|
| Uses KL-divergence distillation | **Confirmed** -- uses KL divergence for distribution matching (effectively distillation) |
| Table 2 has 5 benchmarks | **Confirmed** -- ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande (previous review saying 4 was incorrect) |
| Accepted at ICML 2026 | **Likely true** -- arXiv Comments field says "ICML 2026"; no independent second confirmation found |
| WINA vs SPON numbers at 50% | **Verified** -- SPON beats WINA on average (+0.99 on Llama3-8B, +2.23 on Mistral-7B) but not on every individual benchmark |
| Reports perplexity on WikiText | **Confirmed** -- Table 1 has WikiText perplexity for 4 models across multiple sparsity levels |

Sources:
- [arXiv Abstract Page: 2512.12744](https://arxiv.org/abs/2512.12744)
- [arXiv HTML Version: 2512.12744](https://arxiv.org/html/2512.12744)
- [ICML 2026 Conference Page](https://icml.cc/)
- [ICML 2026 Statistics - Paper Copilot](https://papercopilot.com/statistics/icml-statistics/icml-2026-statistics/)
- [Paper Digest: ICML 2026 Papers & Highlights](https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/)

agentId: aa575ca2c864aca52 (use SendMessage with to: 'aa575ca2c864aca52' to continue this agent)
&lt;usage>total_tokens: 23989
tool_uses: 17
duration_ms: 134761&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47c0317d-cd92-46c6-a7d1-693a61ab78c9",
  "isSidechain": false,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "type": "user",
  "uuid": "a2be7913-e06c-4ed5-82c4-5ac5f68cec6d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify the following claims about the paper \"Resting Neurons, Active Insights (SPON)\" (arXiv 2512.12744):\n\n1. Does it use KL-divergence distillation for training?\n2. What benchmarks does it report in Table 2, and how many are there? (Previous review flagged it as having 4 benchmarks in Table 2, but the proposal now says 5: ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande)\n3. Is it accepted at ICML 2026? Check arXiv metadata, any conference announcements.\n4. What are the actual numbers reported (WINA vs SPON at 50% sparsity)?\n5. Does SPON report perplexity on WikiText?\n\nUse WebSearch to find the paper and WebFetch to read its abstract and key sections. Try multiple searches:\n- \"Resting Neurons Active Insights SPON arXiv 2512.12744\"\n- \"SPON activation sparsity ICML 2026\"\n- \"site:arxiv.org 2512.12744\"\n\nReport findings in detail.",
    "agentId": "aa575ca2c864aca52",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is my comprehensive report.\n\n---\n\n## Detailed Findings on \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\" (arXiv 2512.12744)\n\n**Paper metadata:**\n- Authors: Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma\n- Submitted: December 14, 2025 (v1); latest version: April 30, 2026 (v3)\n- Note: The title changed between versions -- v1 used \"Improving Input Sparsification\" while v3 uses \"Robustify Activation Sparsity\"\n\n---\n\n### 1. Does it use KL-divergence distillation for training?\n\n**Yes.** The paper explicitly uses KL divergence as its training objective. The loss function is:\n\n`L(A) = E_{u~D}[D_KL(sigma(z(u)) || sigma(z_tilde(u;A)))]`\n\nThis minimizes the KL divergence between the dense model's output distribution and the sparse model's output distribution over calibration data. The paper calls this approach **\"distribution matching\"** rather than \"knowledge distillation,\" though Section 2.3 does state the objective \"effectively distills global, input-agnostic information from the dense model into the SPON parameters.\" So while the mechanism is effectively a form of KL-divergence distillation, the authors primarily frame it as distribution matching.\n\n---\n\n### 2. Benchmarks in Table 2 -- How many and which ones?\n\n**There are 5 benchmarks in Table 2**, confirming the proposal's claim (not 4 as the previous review flagged):\n\n1. ARC-Challenge\n2. ARC-Easy\n3. BoolQ\n4. PIQA (styled as \"PiQA\" in the paper)\n5. Winogrande\n\nTable 2 also includes an **Average** column. The table covers multiple methods (LaRoSA, WINA, R-Sparse, WAS, SPON) across multiple models (Llama3-8B, Mistral-7B) at 50% sparsity.\n\n---\n\n### 3. Is it accepted at ICML 2026?\n\n**The arXiv abstract page's \"Comments\" field says \"ICML 2026\"**, which is the standard convention authors use to indicate acceptance. This was confirmed via direct fetch of the arXiv abstract page metadata. However:\n\n- The HTML body of the paper (v3) does not contain an explicit \"Published at ICML 2026\" header (unlike some camera-ready versions).\n- The paper does not appear in the sampled ICML 2026 highlights on Paper Digest (which only covers ~500 of 6,500+ accepted papers).\n- The ICML virtual site paper listing was not searchable via web fetch (it loads dynamically).\n- No OpenReview listing was found for this paper.\n\n**Assessment:** The \"ICML 2026\" comment on arXiv is a strong indicator of acceptance, as this is the standard practice for accepted papers. ICML 2026 is scheduled for July 6-11, 2026 in Seoul, and the v3 update on April 30, 2026 is consistent with a camera-ready revision timeline. However, I could not find a second independent confirmation (e.g., OpenReview decision, ICML virtual proceedings listing). The claim is **plausible but not independently verified beyond arXiv metadata**.\n\n---\n\n### 4. Actual numbers: WINA vs SPON at 50% sparsity\n\n**Llama3-8B at 50% sparsity:**\n\n| Benchmark | WINA | SPON | Difference |\n|-----------|------|------|-----------|\n| ARC-Challenge | 48.81% | 51.11% | +2.30 |\n| ARC-Easy | 75.00% | 76.89% | +1.89 |\n| BoolQ | 81.25% | 82.54% | +1.29 |\n| PIQA | 79.16% | 78.40% | -0.76 |\n| Winogrande | 70.64% | 70.88% | +0.24 |\n| **Average** | **70.97%** | **71.96%** | **+0.99** |\n\n**Mistral-7B at 50% sparsity:**\n\n| Benchmark | WINA | SPON | Difference |\n|-----------|------|------|-----------|\n| ARC-Challenge | 52.30% | 56.31% | +4.01 |\n| ARC-Easy | 77.57% | 81.02% | +3.45 |\n| BoolQ | 81.59% | 84.98% | +3.39 |\n| PIQA | 81.34% | 82.05% | +0.71 |\n| Winogrande | 70.88% | 70.48% | -0.40 |\n| **Average** | **72.74%** | **74.97%** | **+2.23** |\n\nNotable: SPON does not uniformly beat WINA on every benchmark -- it loses on PIQA for Llama3-8B and Winogrande for Mistral-7B, though it wins on average.\n\n---\n\n### 5. Does SPON report perplexity on WikiText?\n\n**Yes.** Table 1 reports WikiText language modeling perplexity across multiple sparsity levels. Key numbers at 50% sparsity:\n\n| Model | Full Dense (0%) | TEAL (50%) | SPON (50%) |\n|-------|----------------|-----------|-----------|\n| Llama3-1B | 12.14 | 17.03 | 15.43 |\n| Llama3-8B | 6.75 | 8.34 | 7.83 |\n| Mistral-7B | 5.49 | 6.00 | 5.86 |\n| Qwen3-8B | 8.99 | 9.75 | 9.26 |\n\nSPON consistently outperforms TEAL at 50% sparsity on WikiText perplexity. Results at 25% and 60% sparsity are also reported.\n\n---\n\n### Summary of Claim Verification\n\n| Claim | Status |\n|-------|--------|\n| Uses KL-divergence distillation | **Confirmed** -- uses KL divergence for distribution matching (effectively distillation) |\n| Table 2 has 5 benchmarks | **Confirmed** -- ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande (previous review saying 4 was incorrect) |\n| Accepted at ICML 2026 | **Likely true** -- arXiv Comments field says \"ICML 2026\"; no independent second confirmation found |\n| WINA vs SPON numbers at 50% | **Verified** -- SPON beats WINA on average (+0.99 on Llama3-8B, +2.23 on Mistral-7B) but not on every individual benchmark |\n| Reports perplexity on WikiText | **Confirmed** -- Table 1 has WikiText perplexity for 4 models across multiple sparsity levels |\n\nSources:\n- [arXiv Abstract Page: 2512.12744](https://arxiv.org/abs/2512.12744)\n- [arXiv HTML Version: 2512.12744](https://arxiv.org/html/2512.12744)\n- [ICML 2026 Conference Page](https://icml.cc/)\n- [ICML 2026 Statistics - Paper Copilot](https://papercopilot.com/statistics/icml-statistics/icml-2026-statistics/)\n- [Paper Digest: ICML 2026 Papers & Highlights](https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/)"
      }
    ],
    "totalDurationMs": 134761,
    "totalTokens": 23989,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 21647,
      "output_tokens": 1970,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 371
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1970,
          "cache_read_input_tokens": 21647,
          "cache_creation_input_tokens": 371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 371,
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
  "sourceToolAssistantUUID": "47c0317d-cd92-46c6-a7d1-693a61ab78c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
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
  "leafUuid": "a2be7913-e06c-4ed5-82c4-5ac5f68cec6d",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Composing Static and Contextual Corrections for Activation Sparsity in SwiGLU LLMs via Output-Distribution Distillation",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

### Tool result

_source line 18 · 2026-05-12T03:49:29.787Z_

<details><summary>↩ Tool result · `toolu_01W24hBmf6A6bUBZWMEa82Kt`</summary>

```text
I now have comprehensive information to provide a detailed report. Here are my findings:

---

## RULER Benchmark: Detailed Verification Report

### 1. Publication: COLM 2024, arXiv 2404.06654

**CONFIRMED.** RULER ("What's the Real Context Size of Your Long-Context Language Models?") is published as a conference paper at COLM 2024. The arXiv identifier is 2404.06654. Authors are Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang, and Boris Ginsburg (NVIDIA).

### 2. 13 Tasks Across 4 Categories

**CONFIRMED.** RULER contains exactly 13 task configurations across 4 categories:

**Retrieval (8 tasks)** -- all NIAH (Needle-in-a-Haystack) variants:
1. `niah_single_1` -- Single NIAH with word-number pairs
2. `niah_single_2` -- Single NIAH with word-number using essays
3. `niah_single_3` -- Single NIAH with word-UUID pairs
4. `niah_multikey_1` -- Multi-keys NIAH (4 keys)
5. `niah_multikey_2` -- Multi-keys NIAH (full haystack)
6. `niah_multikey_3` -- Multi-keys NIAH (UUID-UUID retrieval)
7. `niah_multivalue` -- Multi-values NIAH (4 values, same key)
8. `niah_multiquery` -- Multi-queries NIAH (4 distinct queries)

**Multi-hop Tracing (1 task):**
9. `vt` -- Variable Tracking (1 chain, 4 hops)

**Aggregation (2 tasks):**
10. `cwe` -- Common Words Extraction (10 words, specific frequency)
11. `fwe` -- Frequent Words Extraction (Zeta distribution, alpha=2.0)

**Question Answering (2 tasks):**
12. `qa_1` -- SQuAD-based single-hop QA
13. `qa_2` -- HotpotQA-based multi-hop QA

The category breakdown is **Retrieval: 8, Multi-hop Tracing: 1, Aggregation: 2, QA: 2** = 13 total. Note that the Retrieval category dominates with 8 of 13 tasks (all NIAH variants with different key types, value counts, and query structures).

### 3. Open-Source Codebase at github.com/NVIDIA/RULER

**CONFIRMED.** The repository exists at `https://github.com/NVIDIA/RULER`. It includes:
- Task configurations in `scripts/synthetic.yaml` and `scripts/config_tasks.sh`
- Model configuration via `config_models.sh` supporting HuggingFace, vLLM, TensorRT-LLM, OpenAI, and Gemini frameworks
- Docker-based setup (container: `cphsieh/ruler:0.2.0`, built on NVIDIA's PyTorch container)
- Execution via `bash run.sh YOUR_MODEL_NAME synthetic`
- Multiple branches including `rulerv1-ns` and `rulerv2-ns` for latest evaluation pipelines

### 4. Context Lengths Supported

**Six lengths: 4K, 8K, 16K, 32K, 64K, and 128K tokens.** These are the standard evaluation lengths. The framework is flexible and can be configured for custom sequence lengths. The paper's original evaluation used all six lengths. Some subsequent work has extended evaluation to 131K and beyond using RULER's flexible configuration system.

### 5. Number of Examples Per Task: 500

**CONFIRMED.** The paper explicitly states: "For each task, we evaluate each model with **500 examples** generated for each length from the series (4k, 8k, 16k, 32k, 64k, 128k)." This means 500 examples x 6 lengths x 13 tasks = 39,000 total examples per model evaluation.

### 6. Recall-Based Scoring

**CONFIRMED.** The paper states: "we append the task input with an answer prefix and check the presence of the target output with **recall-based accuracy**." This is the primary evaluation metric. The aggregate performance uses a weighted average (wAvg) across context lengths with two weighting schemes (increasing weight with length and decreasing weight with length). A qualitative threshold of 85.6% (Llama-2-7b-chat performance at 4K) is used to determine effective context length.

### 7. Has RULER Been Used to Evaluate Activation Sparsity Methods?

**YES, extensively.** Multiple papers have used RULER to evaluate sparse attention and activation sparsity methods:

- **"The Sparse Frontier" (Nawrot et al., arXiv 2504.17768):** Directly uses NIAH, VT, and CWE tasks from RULER as part of their 9-task evaluation benchmark for sparse attention methods, evaluating six methods up to 128K tokens and 0.95 sparsity.
- **LongAct:** Uses RULER to evaluate saliency-guided sparse activation methods, reporting improvements on RULER and InfiniteBench.
- **Token Sparse Attention:** Uses RULER as a primary benchmark, reporting highest average RULER accuracy under comparable speedups.
- **Gated Sparse Attention (GSA):** Evaluates on RULER showing maintained performance at 128K while standard attention collapses.
- **Dynamic sparse attention methods** for pre-filling acceleration also evaluate on RULER at 131K contexts.
- Papers studying attention weight sparsity (up to 96.8% at 128K contexts) commonly use RULER to validate that sparse methods preserve task accuracy.

RULER has become a **standard benchmark** for evaluating sparse attention and efficiency methods in long-context settings.

### 8. Is RULER Evaluation Computationally Lightweight?

**Partially true, with caveats.** The RULER paper itself does not explicitly discuss or claim computational lightweight properties. However, RULER is inherently lighter than many alternatives because:

- **Synthetic tasks**: All inputs are synthetically generated, requiring no large dataset downloads or preprocessing of natural corpora
- **Automated scoring**: Recall-based string matching is trivially cheap compared to LLM-as-judge evaluation
- **No parametric knowledge dependency**: Evaluation does not require the model to have memorized specific knowledge, making it a cleaner signal
- **Configurable**: Users can reduce the number of examples or context lengths to reduce cost

However, running the full suite (500 examples x 6 lengths x 13 tasks = 39,000 inference calls) at lengths up to 128K tokens is still computationally non-trivial -- particularly for the longer context lengths. The evaluation cost scales with the context length and model size. A full RULER evaluation at 128K on a large model requires significant GPU resources and time. The claim of being "computationally lightweight" is **relative** -- it is lighter than naturalistic benchmarks that require expensive post-processing or human evaluation, but not trivially cheap in absolute terms.

Sources:
- [RULER Paper (arXiv 2404.06654)](https://arxiv.org/abs/2404.06654)
- [RULER Paper HTML Version](https://arxiv.org/html/2404.06654v1)
- [NVIDIA/RULER GitHub Repository](https://github.com/NVIDIA/RULER)
- [RULER DeepWiki](https://deepwiki.com/NVIDIA/RULER)
- [RULER Benchmark Detailed Breakdown (Medium)](https://medium.com/@techsachin/ruler-benchmark-to-evaluate-long-context-modeling-capabilities-of-language-models-7eb13a269e36)
- [The Sparse Frontier (arXiv 2504.17768)](https://arxiv.org/abs/2504.17768)
- [Sparse Frontier GitHub](https://github.com/PiotrNawrot/sparse-frontier)
- [RULER OpenReview](https://openreview.net/forum?id=kIoBbc76Sy)
- [RULER Benchmark Leaderboard](https://llm-stats.com/benchmarks/ruler)
- [WandB RULER Evaluation Guide](https://wandb.ai/byyoung3/ruler_eval/reports/How-to-evaluate-the-true-context-length-of-your-LLM-using-RULER---VmlldzoxNDE0OTA0OQ)

agentId: a57d4bb524975c34c (use SendMessage with to: 'a57d4bb524975c34c' to continue this agent)
&lt;usage>total_tokens: 27742
tool_uses: 20
duration_ms: 168315&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cae0991-da14-4c84-8986-8b1d65b742b2",
  "isSidechain": false,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "type": "user",
  "uuid": "355dc3be-ed6d-490e-a77d-603de447af42",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify details about the RULER benchmark for long-context evaluation:\n\n1. Is RULER from COLM 2024? (arXiv 2404.06654)\n2. Does it have 13 tasks across 4 categories (Retrieval, Multi-hop Tracing, Aggregation, QA)?\n3. Is there an open-source evaluation codebase at github.com/NVIDIA/RULER?\n4. What context lengths does it support?\n5. How many examples per task (claimed: 500)?\n6. Is scoring recall-based?\n\nAlso check:\n- Has RULER been used to evaluate activation sparsity methods before?\n- Is RULER evaluation computationally lightweight as claimed?\n\nTry:\n- \"RULER long context benchmark COLM 2024\"\n- \"site:arxiv.org 2404.06654\"\n- \"NVIDIA RULER benchmark github\"\n- \"RULER needle haystack evaluation\"\n\nReport findings in detail.",
    "agentId": "a57d4bb524975c34c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to provide a detailed report. Here are my findings:\n\n---\n\n## RULER Benchmark: Detailed Verification Report\n\n### 1. Publication: COLM 2024, arXiv 2404.06654\n\n**CONFIRMED.** RULER (\"What's the Real Context Size of Your Long-Context Language Models?\") is published as a conference paper at COLM 2024. The arXiv identifier is 2404.06654. Authors are Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang, and Boris Ginsburg (NVIDIA).\n\n### 2. 13 Tasks Across 4 Categories\n\n**CONFIRMED.** RULER contains exactly 13 task configurations across 4 categories:\n\n**Retrieval (8 tasks)** -- all NIAH (Needle-in-a-Haystack) variants:\n1. `niah_single_1` -- Single NIAH with word-number pairs\n2. `niah_single_2` -- Single NIAH with word-number using essays\n3. `niah_single_3` -- Single NIAH with word-UUID pairs\n4. `niah_multikey_1` -- Multi-keys NIAH (4 keys)\n5. `niah_multikey_2` -- Multi-keys NIAH (full haystack)\n6. `niah_multikey_3` -- Multi-keys NIAH (UUID-UUID retrieval)\n7. `niah_multivalue` -- Multi-values NIAH (4 values, same key)\n8. `niah_multiquery` -- Multi-queries NIAH (4 distinct queries)\n\n**Multi-hop Tracing (1 task):**\n9. `vt` -- Variable Tracking (1 chain, 4 hops)\n\n**Aggregation (2 tasks):**\n10. `cwe` -- Common Words Extraction (10 words, specific frequency)\n11. `fwe` -- Frequent Words Extraction (Zeta distribution, alpha=2.0)\n\n**Question Answering (2 tasks):**\n12. `qa_1` -- SQuAD-based single-hop QA\n13. `qa_2` -- HotpotQA-based multi-hop QA\n\nThe category breakdown is **Retrieval: 8, Multi-hop Tracing: 1, Aggregation: 2, QA: 2** = 13 total. Note that the Retrieval category dominates with 8 of 13 tasks (all NIAH variants with different key types, value counts, and query structures).\n\n### 3. Open-Source Codebase at github.com/NVIDIA/RULER\n\n**CONFIRMED.** The repository exists at `https://github.com/NVIDIA/RULER`. It includes:\n- Task configurations in `scripts/synthetic.yaml` and `scripts/config_tasks.sh`\n- Model configuration via `config_models.sh` supporting HuggingFace, vLLM, TensorRT-LLM, OpenAI, and Gemini frameworks\n- Docker-based setup (container: `cphsieh/ruler:0.2.0`, built on NVIDIA's PyTorch container)\n- Execution via `bash run.sh YOUR_MODEL_NAME synthetic`\n- Multiple branches including `rulerv1-ns` and `rulerv2-ns` for latest evaluation pipelines\n\n### 4. Context Lengths Supported\n\n**Six lengths: 4K, 8K, 16K, 32K, 64K, and 128K tokens.** These are the standard evaluation lengths. The framework is flexible and can be configured for custom sequence lengths. The paper's original evaluation used all six lengths. Some subsequent work has extended evaluation to 131K and beyond using RULER's flexible configuration system.\n\n### 5. Number of Examples Per Task: 500\n\n**CONFIRMED.** The paper explicitly states: \"For each task, we evaluate each model with **500 examples** generated for each length from the series (4k, 8k, 16k, 32k, 64k, 128k).\" This means 500 examples x 6 lengths x 13 tasks = 39,000 total examples per model evaluation.\n\n### 6. Recall-Based Scoring\n\n**CONFIRMED.** The paper states: \"we append the task input with an answer prefix and check the presence of the target output with **recall-based accuracy**.\" This is the primary evaluation metric. The aggregate performance uses a weighted average (wAvg) across context lengths with two weighting schemes (increasing weight with length and decreasing weight with length). A qualitative threshold of 85.6% (Llama-2-7b-chat performance at 4K) is used to determine effective context length.\n\n### 7. Has RULER Been Used to Evaluate Activation Sparsity Methods?\n\n**YES, extensively.** Multiple papers have used RULER to evaluate sparse attention and activation sparsity methods:\n\n- **\"The Sparse Frontier\" (Nawrot et al., arXiv 2504.17768):** Directly uses NIAH, VT, and CWE tasks from RULER as part of their 9-task evaluation benchmark for sparse attention methods, evaluating six methods up to 128K tokens and 0.95 sparsity.\n- **LongAct:** Uses RULER to evaluate saliency-guided sparse activation methods, reporting improvements on RULER and InfiniteBench.\n- **Token Sparse Attention:** Uses RULER as a primary benchmark, reporting highest average RULER accuracy under comparable speedups.\n- **Gated Sparse Attention (GSA):** Evaluates on RULER showing maintained performance at 128K while standard attention collapses.\n- **Dynamic sparse attention methods** for pre-filling acceleration also evaluate on RULER at 131K contexts.\n- Papers studying attention weight sparsity (up to 96.8% at 128K contexts) commonly use RULER to validate that sparse methods preserve task accuracy.\n\nRULER has become a **standard benchmark** for evaluating sparse attention and efficiency methods in long-context settings.\n\n### 8. Is RULER Evaluation Computationally Lightweight?\n\n**Partially true, with caveats.** The RULER paper itself does not explicitly discuss or claim computational lightweight properties. However, RULER is inherently lighter than many alternatives because:\n\n- **Synthetic tasks**: All inputs are synthetically generated, requiring no large dataset downloads or preprocessing of natural corpora\n- **Automated scoring**: Recall-based string matching is trivially cheap compared to LLM-as-judge evaluation\n- **No parametric knowledge dependency**: Evaluation does not require the model to have memorized specific knowledge, making it a cleaner signal\n- **Configurable**: Users can reduce the number of examples or context lengths to reduce cost\n\nHowever, running the full suite (500 examples x 6 lengths x 13 tasks = 39,000 inference calls) at lengths up to 128K tokens is still computationally non-trivial -- particularly for the longer context lengths. The evaluation cost scales with the context length and model size. A full RULER evaluation at 128K on a large model requires significant GPU resources and time. The claim of being \"computationally lightweight\" is **relative** -- it is lighter than naturalistic benchmarks that require expensive post-processing or human evaluation, but not trivially cheap in absolute terms.\n\nSources:\n- [RULER Paper (arXiv 2404.06654)](https://arxiv.org/abs/2404.06654)\n- [RULER Paper HTML Version](https://arxiv.org/html/2404.06654v1)\n- [NVIDIA/RULER GitHub Repository](https://github.com/NVIDIA/RULER)\n- [RULER DeepWiki](https://deepwiki.com/NVIDIA/RULER)\n- [RULER Benchmark Detailed Breakdown (Medium)](https://medium.com/@techsachin/ruler-benchmark-to-evaluate-long-context-modeling-capabilities-of-language-models-7eb13a269e36)\n- [The Sparse Frontier (arXiv 2504.17768)](https://arxiv.org/abs/2504.17768)\n- [Sparse Frontier GitHub](https://github.com/PiotrNawrot/sparse-frontier)\n- [RULER OpenReview](https://openreview.net/forum?id=kIoBbc76Sy)\n- [RULER Benchmark Leaderboard](https://llm-stats.com/benchmarks/ruler)\n- [WandB RULER Evaluation Guide](https://wandb.ai/byyoung3/ruler_eval/reports/How-to-evaluate-the-true-context-length-of-your-LLM-using-RULER---VmlldzoxNDE0OTA0OQ)"
      }
    ],
    "totalDurationMs": 168315,
    "totalTokens": 27742,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 23704,
      "output_tokens": 2086,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1951
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2086,
          "cache_read_input_tokens": 23704,
          "cache_creation_input_tokens": 1951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1951,
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
  "sourceToolAssistantUUID": "5cae0991-da14-4c84-8986-8b1d65b742b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T03:50:03.764Z_

<details><summary>↩ Tool result · `toolu_01AXz6mas2FJy2QLP4doYPj5`</summary>

```text
Now I have comprehensive results. Let me compile the findings.

---

Here is my report on papers **NOT already in your proposal's landscape** that are relevant to activation sparsity for LLMs. I have organized them by category and recency.

---

## NEW PAPERS (2026) -- Highest Priority

### 1. "Sparser, Faster, Lighter Transformer Language Models" (TwELL) -- ICML 2026
- **Authors:** Sakana AI + NVIDIA
- **arXiv:** [2603.23198](https://arxiv.org/abs/2603.23198)
- Introduces TwELL (Tile-wise ELLPACK), a new sparse packing format with custom CUDA kernels for H100 GPUs. L1 regularization induces >99% sparsity with negligible downstream impact. Achieves up to 30% inference throughput gains and 24% training speedups. Directly relevant as it provides a hardware-level format for exploiting unstructured activation sparsity.

### 2. "To 2:4 Sparsity and Beyond: Neuron-level Activation Function to Accelerate LLM Pre-Training" -- Feb 2026
- **arXiv:** [2602.06183](https://arxiv.org/abs/2602.06183)
- Uses hardware-accelerated 2:4 weight sparsity + v:n:m (Venom) activation sparsity to speed up FFN matrix multiplications during pre-training by 1.4--1.7x. Applicable to A100+ GPUs; orthogonal to quantization and MoE.

### 3. "DynamicInfer: Runtime-Aware Sparse Offloading for LLMs Inference on a Consumer-Grade GPU" -- ICLR 2026
- **OpenReview:** [CvjmvjlczZ](https://openreview.net/forum?id=CvjmvjlczZ)
- Introduces a lightweight online neuron scheduler that dynamically reallocates neurons between CPU/GPU based on runtime activation sparsity. Hierarchical neural caching + activation-aware prefetching. Achieves up to 253% speedup over llama.cpp and 59% over PowerInfer. Directly relevant to sparsity predictor design.

### 4. "Universal Properties of Activation Sparsity in Modern Large Language Models" -- ICLR 2026
- **arXiv:** [2509.00454](https://arxiv.org/abs/2509.00454)
- Systematic investigation of activation sparsity across diverse model families/scales (including GLU-based). Key finding: effective activation sparsity potential grows with model size. First study of activation sparsity in diffusion-based LLMs. Provides a general evaluation framework.

### 5. "Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models" (Engram) -- Jan 2026
- **arXiv:** [2601.07372](https://arxiv.org/abs/2601.07372)
- **Authors:** DeepSeek AI
- Introduces Engram, which separates memory (static O(1) lookup via hashed n-grams) from computation (MoE). Discovers a U-shaped sparsity allocation law: 20--25% of sparse parameters should go to memory, rest to computation. Scaled to 27B parameters. Relevant as a new "axis" of sparsity complementary to activation sparsity.

---

## NEW PAPERS (Late 2025) -- High Priority

### 6. "Sparsing Law: Towards Large Language Models with Greater Activation Sparsity" -- ICML 2025
- **arXiv:** [2411.02335](https://arxiv.org/abs/2411.02335)
- Proposes PPL-p% sparsity metric. Discovers scaling laws: ReLU models get sparser with more data (power-law), SiLU models get less sparse. Deeper architectures are advantageous. Trains a 2.4B model with 93.52% sparsity at 4.1x speedup. Highly relevant for predicting sparsity behavior.

### 7. "Lightweight Error Mitigation Strategies for Post-Training N:M Activation Sparsity in LLMs" -- Sep 2025
- **arXiv:** [2509.22166](https://arxiv.org/abs/2509.22166)
- Comprehensive evaluation of post-training N:M activation pruning. Shows 16:32 pattern matches unstructured sparsity quality; recommends 8:16 as optimal hardware/quality tradeoff. Shows activation pruning preserves generative capabilities better than weight pruning at same sparsity.

### 8. "Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models" -- Aug 2025
- **arXiv:** [2508.02128](https://arxiv.org/abs/2508.02128)
- Training-free N:M activation sparsity targeting the prefill stage specifically (q/k/v/o projections). Sparsifies >55% of linear computations. Introduces Outstanding-sparse framework combining Amber Pruner with W8A8 quantization.

### 9. "SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference" -- Nov 2024
- **arXiv:** [2411.12692](https://arxiv.org/abs/2411.12692)
- Predicts activation sparsity by comparing only sign bits of inputs and weights (XOR-based). No training required, minimal memory footprint. ~21% faster inference with <1% accuracy loss. Relevant as an alternative to learned sparsity predictors.

### 10. "La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation" -- ICML 2025
- **arXiv:** [2507.01299](https://arxiv.org/abs/2507.01299)
- Training-free method using layerwise orthogonal rotations + Top-K selection. Achieves 1.30x wall-clock speedup at 40% sparsity on LLaMA2-7B. Outperforms TEAL by 1.77% and CATS by 17.14% in zero-shot accuracy gap.

### 11. "A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering" -- Euro-Par 2025
- **arXiv:** [2507.14179](https://arxiv.org/abs/2507.14179)
- Clusters billions of neurons into representative centroids for sparsity prediction instead of per-neuron prediction. 79.34% clustering precision on Mistral-7B at 50% FFN sparsity. Relevant as an alternative predictor architecture.

### 12. "ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models" -- COLING 2025
- **arXiv:** [2402.13516](https://arxiv.org/abs/2402.13516)
- Three-step method: activation function substitution, progressive sparsity regularization, activation threshold shifting. Achieves 89.32% sparsity on LLaMA2-7B with up to 4.52x inference speedup.

### 13. "VLM in a Flash: I/O-Efficient Sparsification of Vision-Language Model via Neuron Chunking" -- NeurIPS 2025
- **arXiv:** [2511.18692](https://arxiv.org/abs/2511.18692)
- Aligns sparsification with flash storage I/O patterns via neuron chunking. Up to 4.65x I/O efficiency improvement on edge devices. Relevant if your proposal considers edge deployment.

### 14. "SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity" -- ICML 2025
- **arXiv:** [2506.16500](https://arxiv.org/abs/2506.16500)
- **Authors:** NVIDIA
- SVD-based training-free sparsity estimator for fine-tuning. Multi-dimensional sparsity policy varying across layers, tokens, and training steps. 1.6x faster fine-tuning, 2.2x compute savings. Relevant as it shows SVD-based sparsity estimation works for fine-tuning.

### 15. "Sparse Logit Sampling: Accelerating Knowledge Distillation in LLMs" -- ACL 2025 Oral
- **arXiv:** [2503.16870](https://arxiv.org/abs/2503.16870)
- Proves naive Top-K caching gives biased teacher distribution estimates. Proposes importance-sampling-based "Random Sampling KD" with unbiased gradients using only 12 sparse logits per token. Relevant to your query about KL-divergence distillation with sparsity.

### 16. "RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning" -- ACL 2025
- **arXiv:** [2502.11147](https://arxiv.org/abs/2502.11147)
- Identifies "milestone tokens" in reasoning chains and manages KV cache accordingly. O(L) time/memory with constant memory consumption. Relevant as attention-side sparsity complementing FFN activation sparsity.

### 17. "TurboSparse: Achieving LLM SOTA Performance with Minimal Activated Parameters" -- June 2024
- **arXiv:** [2406.05955](https://arxiv.org/abs/2406.05955)
- Proposes dReLU activation function achieving 90% neuron inactivity in Mistral-7B and 85% in Mixtral-47B. 2--5x decoding speedup; 11 tokens/sec on mobile for Mixtral-47B. May already be known but worth verifying.

---

## On Specific Queries

**KL-divergence distillation + sparsity predictors:** No paper was found that specifically combines KL-divergence distillation loss for training sparsity predictors. The closest is Sparse Logit Sampling (#15) which addresses efficient KD with sparse logits, and SPON (already in your list) which uses distribution matching. This appears to be a genuine gap in the literature.

**Static + contextual sparsity composition:** No paper was found that explicitly composes static and contextual sparsity corrections as a formal framework. Engram (#5) introduces a complementary "sparsity axis" (static memory vs. dynamic computation), and WiSparse (already in your list) mixes weight-aware and activation-aware sparsity -- but the specific static/contextual composition framing appears to be novel.

**ICML 2026:** The conference proceedings (July 2026) are not yet fully available. The confirmed ICML 2026 paper is TwELL/Sakana (#1). The Sparsing Law (#6) was ICML 2025.

**ACL 2026:** Submissions are still under review (October 2025 and January 2026 ARR cycles). No accepted paper list is available yet.

Sources:
- [TwELL - Sparser, Faster, Lighter (arXiv 2603.23198)](https://arxiv.org/abs/2603.23198)
- [To 2:4 Sparsity and Beyond (arXiv 2602.06183)](https://arxiv.org/abs/2602.06183)
- [DynamicInfer (ICLR 2026)](https://openreview.net/forum?id=CvjmvjlczZ)
- [Universal Properties of Activation Sparsity (arXiv 2509.00454)](https://arxiv.org/abs/2509.00454)
- [Engram - DeepSeek (arXiv 2601.07372)](https://arxiv.org/abs/2601.07372)
- [Sparsing Law (arXiv 2411.02335)](https://arxiv.org/abs/2411.02335)
- [Post-Training N:M Activation Sparsity (arXiv 2509.22166)](https://arxiv.org/abs/2509.22166)
- [Amber Pruner (arXiv 2508.02128)](https://arxiv.org/abs/2508.02128)
- [SparseInfer (arXiv 2411.12692)](https://arxiv.org/abs/2411.12692)
- [La RoSA (arXiv 2507.01299)](https://arxiv.org/abs/2507.01299)
- [Activation Pattern Clustering (arXiv 2507.14179)](https://arxiv.org/abs/2507.14179)
- [ProSparse (arXiv 2402.13516)](https://arxiv.org/abs/2402.13516)
- [VLM in a Flash (arXiv 2511.18692)](https://arxiv.org/abs/2511.18692)
- [SparseLoRA (arXiv 2506.16500)](https://arxiv.org/abs/2506.16500)
- [Sparse Logit Sampling (arXiv 2503.16870)](https://arxiv.org/abs/2503.16870)
- [RaaS (arXiv 2502.11147)](https://arxiv.org/abs/2502.11147)
- [TurboSparse (arXiv 2406.05955)](https://arxiv.org/abs/2406.05955)
- [Paper Digest ICML 2026](https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/)
- [ICML 2026 Paper List - Paper Copilot](https://papercopilot.com/paper-list/icml-paper-list/icml-2026-paper-list/)
- [ICLR 2026 Papers](https://iclr.cc/virtual/2026/papers.html)
- [Sakana AI Blog](https://pub.sakana.ai/sparser-faster-llms/)
- [MarkTechPost on TwELL](https://www.marktechpost.com/2026/05/11/sakana-ai-and-nvidia-introduce-twell-with-cuda-kernels-for-20-5-inference-and-21-9-training-speedup-in-llms/)

agentId: a0e3196b366de0451 (use SendMessage with to: 'a0e3196b366de0451' to continue this agent)
&lt;usage>total_tokens: 51394
tool_uses: 38
duration_ms: 207602&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a576375-b724-41d0-a1d9-ac92348015c4",
  "isSidechain": false,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "type": "user",
  "uuid": "3045927e-f036-4552-9f8f-a5a5f56992d2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for very recent (2025-2026) papers on activation sparsity for LLMs that might be missing from a proposal's landscape. The proposal already covers: WINA, TEAL, R-Sparse, WAS, WiSparse, ActTail, SPON, FastForward, IFPruning, ShadowLLM, Sirius, Spark Transformer, Polar Sparsity, MaskLLM, DIP, DaSS, ActiveFlow, SVD Contextual Sparsity Predictors, CATS, Deja Vu.\n\nSpecifically search for:\n1. Any new activation sparsity papers from March-May 2026 on arXiv\n2. Papers combining KL-divergence distillation with sparsity predictors\n3. Papers composing static and contextual sparsity corrections\n4. ICML 2026 accepted papers on efficient inference / activation sparsity\n5. ACL 2026 papers on efficient NLP methods\n\nTry these searches:\n- \"activation sparsity LLM 2026 arXiv\"\n- \"KL divergence sparsity predictor training LLM\"\n- \"static contextual sparsity composition LLM\"\n- \"ICML 2026 activation sparsity efficient inference\"\n- \"SwiGLU sparsity predictor 2026\"\n- \"learned sparsity predictor LLM decode 2026\"\n\nReport any papers NOT in the list above that are relevant.",
    "agentId": "a0e3196b366de0451",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive results. Let me compile the findings.\n\n---\n\nHere is my report on papers **NOT already in your proposal's landscape** that are relevant to activation sparsity for LLMs. I have organized them by category and recency.\n\n---\n\n## NEW PAPERS (2026) -- Highest Priority\n\n### 1. \"Sparser, Faster, Lighter Transformer Language Models\" (TwELL) -- ICML 2026\n- **Authors:** Sakana AI + NVIDIA\n- **arXiv:** [2603.23198](https://arxiv.org/abs/2603.23198)\n- Introduces TwELL (Tile-wise ELLPACK), a new sparse packing format with custom CUDA kernels for H100 GPUs. L1 regularization induces >99% sparsity with negligible downstream impact. Achieves up to 30% inference throughput gains and 24% training speedups. Directly relevant as it provides a hardware-level format for exploiting unstructured activation sparsity.\n\n### 2. \"To 2:4 Sparsity and Beyond: Neuron-level Activation Function to Accelerate LLM Pre-Training\" -- Feb 2026\n- **arXiv:** [2602.06183](https://arxiv.org/abs/2602.06183)\n- Uses hardware-accelerated 2:4 weight sparsity + v:n:m (Venom) activation sparsity to speed up FFN matrix multiplications during pre-training by 1.4--1.7x. Applicable to A100+ GPUs; orthogonal to quantization and MoE.\n\n### 3. \"DynamicInfer: Runtime-Aware Sparse Offloading for LLMs Inference on a Consumer-Grade GPU\" -- ICLR 2026\n- **OpenReview:** [CvjmvjlczZ](https://openreview.net/forum?id=CvjmvjlczZ)\n- Introduces a lightweight online neuron scheduler that dynamically reallocates neurons between CPU/GPU based on runtime activation sparsity. Hierarchical neural caching + activation-aware prefetching. Achieves up to 253% speedup over llama.cpp and 59% over PowerInfer. Directly relevant to sparsity predictor design.\n\n### 4. \"Universal Properties of Activation Sparsity in Modern Large Language Models\" -- ICLR 2026\n- **arXiv:** [2509.00454](https://arxiv.org/abs/2509.00454)\n- Systematic investigation of activation sparsity across diverse model families/scales (including GLU-based). Key finding: effective activation sparsity potential grows with model size. First study of activation sparsity in diffusion-based LLMs. Provides a general evaluation framework.\n\n### 5. \"Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models\" (Engram) -- Jan 2026\n- **arXiv:** [2601.07372](https://arxiv.org/abs/2601.07372)\n- **Authors:** DeepSeek AI\n- Introduces Engram, which separates memory (static O(1) lookup via hashed n-grams) from computation (MoE). Discovers a U-shaped sparsity allocation law: 20--25% of sparse parameters should go to memory, rest to computation. Scaled to 27B parameters. Relevant as a new \"axis\" of sparsity complementary to activation sparsity.\n\n---\n\n## NEW PAPERS (Late 2025) -- High Priority\n\n### 6. \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\" -- ICML 2025\n- **arXiv:** [2411.02335](https://arxiv.org/abs/2411.02335)\n- Proposes PPL-p% sparsity metric. Discovers scaling laws: ReLU models get sparser with more data (power-law), SiLU models get less sparse. Deeper architectures are advantageous. Trains a 2.4B model with 93.52% sparsity at 4.1x speedup. Highly relevant for predicting sparsity behavior.\n\n### 7. \"Lightweight Error Mitigation Strategies for Post-Training N:M Activation Sparsity in LLMs\" -- Sep 2025\n- **arXiv:** [2509.22166](https://arxiv.org/abs/2509.22166)\n- Comprehensive evaluation of post-training N:M activation pruning. Shows 16:32 pattern matches unstructured sparsity quality; recommends 8:16 as optimal hardware/quality tradeoff. Shows activation pruning preserves generative capabilities better than weight pruning at same sparsity.\n\n### 8. \"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models\" -- Aug 2025\n- **arXiv:** [2508.02128](https://arxiv.org/abs/2508.02128)\n- Training-free N:M activation sparsity targeting the prefill stage specifically (q/k/v/o projections). Sparsifies >55% of linear computations. Introduces Outstanding-sparse framework combining Amber Pruner with W8A8 quantization.\n\n### 9. \"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference\" -- Nov 2024\n- **arXiv:** [2411.12692](https://arxiv.org/abs/2411.12692)\n- Predicts activation sparsity by comparing only sign bits of inputs and weights (XOR-based). No training required, minimal memory footprint. ~21% faster inference with <1% accuracy loss. Relevant as an alternative to learned sparsity predictors.\n\n### 10. \"La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation\" -- ICML 2025\n- **arXiv:** [2507.01299](https://arxiv.org/abs/2507.01299)\n- Training-free method using layerwise orthogonal rotations + Top-K selection. Achieves 1.30x wall-clock speedup at 40% sparsity on LLaMA2-7B. Outperforms TEAL by 1.77% and CATS by 17.14% in zero-shot accuracy gap.\n\n### 11. \"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering\" -- Euro-Par 2025\n- **arXiv:** [2507.14179](https://arxiv.org/abs/2507.14179)\n- Clusters billions of neurons into representative centroids for sparsity prediction instead of per-neuron prediction. 79.34% clustering precision on Mistral-7B at 50% FFN sparsity. Relevant as an alternative predictor architecture.\n\n### 12. \"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\" -- COLING 2025\n- **arXiv:** [2402.13516](https://arxiv.org/abs/2402.13516)\n- Three-step method: activation function substitution, progressive sparsity regularization, activation threshold shifting. Achieves 89.32% sparsity on LLaMA2-7B with up to 4.52x inference speedup.\n\n### 13. \"VLM in a Flash: I/O-Efficient Sparsification of Vision-Language Model via Neuron Chunking\" -- NeurIPS 2025\n- **arXiv:** [2511.18692](https://arxiv.org/abs/2511.18692)\n- Aligns sparsification with flash storage I/O patterns via neuron chunking. Up to 4.65x I/O efficiency improvement on edge devices. Relevant if your proposal considers edge deployment.\n\n### 14. \"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity\" -- ICML 2025\n- **arXiv:** [2506.16500](https://arxiv.org/abs/2506.16500)\n- **Authors:** NVIDIA\n- SVD-based training-free sparsity estimator for fine-tuning. Multi-dimensional sparsity policy varying across layers, tokens, and training steps. 1.6x faster fine-tuning, 2.2x compute savings. Relevant as it shows SVD-based sparsity estimation works for fine-tuning.\n\n### 15. \"Sparse Logit Sampling: Accelerating Knowledge Distillation in LLMs\" -- ACL 2025 Oral\n- **arXiv:** [2503.16870](https://arxiv.org/abs/2503.16870)\n- Proves naive Top-K caching gives biased teacher distribution estimates. Proposes importance-sampling-based \"Random Sampling KD\" with unbiased gradients using only 12 sparse logits per token. Relevant to your query about KL-divergence distillation with sparsity.\n\n### 16. \"RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning\" -- ACL 2025\n- **arXiv:** [2502.11147](https://arxiv.org/abs/2502.11147)\n- Identifies \"milestone tokens\" in reasoning chains and manages KV cache accordingly. O(L) time/memory with constant memory consumption. Relevant as attention-side sparsity complementing FFN activation sparsity.\n\n### 17. \"TurboSparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\" -- June 2024\n- **arXiv:** [2406.05955](https://arxiv.org/abs/2406.05955)\n- Proposes dReLU activation function achieving 90% neuron inactivity in Mistral-7B and 85% in Mixtral-47B. 2--5x decoding speedup; 11 tokens/sec on mobile for Mixtral-47B. May already be known but worth verifying.\n\n---\n\n## On Specific Queries\n\n**KL-divergence distillation + sparsity predictors:** No paper was found that specifically combines KL-divergence distillation loss for training sparsity predictors. The closest is Sparse Logit Sampling (#15) which addresses efficient KD with sparse logits, and SPON (already in your list) which uses distribution matching. This appears to be a genuine gap in the literature.\n\n**Static + contextual sparsity composition:** No paper was found that explicitly composes static and contextual sparsity corrections as a formal framework. Engram (#5) introduces a complementary \"sparsity axis\" (static memory vs. dynamic computation), and WiSparse (already in your list) mixes weight-aware and activation-aware sparsity -- but the specific static/contextual composition framing appears to be novel.\n\n**ICML 2026:** The conference proceedings (July 2026) are not yet fully available. The confirmed ICML 2026 paper is TwELL/Sakana (#1). The Sparsing Law (#6) was ICML 2025.\n\n**ACL 2026:** Submissions are still under review (October 2025 and January 2026 ARR cycles). No accepted paper list is available yet.\n\nSources:\n- [TwELL - Sparser, Faster, Lighter (arXiv 2603.23198)](https://arxiv.org/abs/2603.23198)\n- [To 2:4 Sparsity and Beyond (arXiv 2602.06183)](https://arxiv.org/abs/2602.06183)\n- [DynamicInfer (ICLR 2026)](https://openreview.net/forum?id=CvjmvjlczZ)\n- [Universal Properties of Activation Sparsity (arXiv 2509.00454)](https://arxiv.org/abs/2509.00454)\n- [Engram - DeepSeek (arXiv 2601.07372)](https://arxiv.org/abs/2601.07372)\n- [Sparsing Law (arXiv 2411.02335)](https://arxiv.org/abs/2411.02335)\n- [Post-Training N:M Activation Sparsity (arXiv 2509.22166)](https://arxiv.org/abs/2509.22166)\n- [Amber Pruner (arXiv 2508.02128)](https://arxiv.org/abs/2508.02128)\n- [SparseInfer (arXiv 2411.12692)](https://arxiv.org/abs/2411.12692)\n- [La RoSA (arXiv 2507.01299)](https://arxiv.org/abs/2507.01299)\n- [Activation Pattern Clustering (arXiv 2507.14179)](https://arxiv.org/abs/2507.14179)\n- [ProSparse (arXiv 2402.13516)](https://arxiv.org/abs/2402.13516)\n- [VLM in a Flash (arXiv 2511.18692)](https://arxiv.org/abs/2511.18692)\n- [SparseLoRA (arXiv 2506.16500)](https://arxiv.org/abs/2506.16500)\n- [Sparse Logit Sampling (arXiv 2503.16870)](https://arxiv.org/abs/2503.16870)\n- [RaaS (arXiv 2502.11147)](https://arxiv.org/abs/2502.11147)\n- [TurboSparse (arXiv 2406.05955)](https://arxiv.org/abs/2406.05955)\n- [Paper Digest ICML 2026](https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/)\n- [ICML 2026 Paper List - Paper Copilot](https://papercopilot.com/paper-list/icml-paper-list/icml-2026-paper-list/)\n- [ICLR 2026 Papers](https://iclr.cc/virtual/2026/papers.html)\n- [Sakana AI Blog](https://pub.sakana.ai/sparser-faster-llms/)\n- [MarkTechPost on TwELL](https://www.marktechpost.com/2026/05/11/sakana-ai-and-nvidia-introduce-twell-with-cuda-kernels-for-20-5-inference-and-21-9-training-speedup-in-llms/)"
      }
    ],
    "totalDurationMs": 207602,
    "totalTokens": 51394,
    "totalToolUseCount": 38,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2217,
      "cache_read_input_tokens": 45609,
      "output_tokens": 3567,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2217
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3567,
          "cache_read_input_tokens": 45609,
          "cache_creation_input_tokens": 2217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2217,
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
      "otherToolCount": 38
    }
  },
  "sourceToolAssistantUUID": "0a576375-b724-41d0-a1d9-ac92348015c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
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
  "leafUuid": "3045927e-f036-4552-9f8f-a5a5f56992d2",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Composing Static and Contextual Corrections for Activation Sparsity in SwiGLU LLMs via Output-Distribution Distillation",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

### Assistant

_source line 22 · 2026-05-12T03:50:07.082Z_

Good, I have detailed verification results. Let me now check a few more things — the SVD Contextual Sparsity paper, the mean-field argument validity, and any remaining issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3045927e-f036-4552-9f8f-a5a5f56992d2",
  "isSidechain": false,
  "requestId": "req_011CawzZeH6iXu7ow8nFnXbn",
  "type": "assistant",
  "uuid": "323c3a15-fee3-4dda-8c26-45f8ec0f267c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtKGiBGViFM31WdDuedC8x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2186,
      "cache_creation_input_tokens": 9354,
      "cache_read_input_tokens": 40731,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2186,
          "output_tokens": 959,
          "cache_read_input_tokens": 40731,
          "cache_creation_input_tokens": 9354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9354
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

_source line 23 · 2026-05-12T03:50:11.064Z_

<details open><summary>🔧 Tool call — Agent · `toolu_018hzrLrrhpEbkQkmh6WXpH3`</summary>

```json
{
  "description": "Verify SVD sparsity predictors paper",
  "subagent_type": "general-purpose",
  "prompt": "Search for the paper \"SVD Contextual Sparsity Predictors for Fast LLM Inference\" (arXiv 2603.14110, March 2026). Verify:\n\n1. Does it exist? Is it from March 2026?\n2. Does it find that learned predictors suffer from out-of-distribution sensitivity?\n3. Does it use truncated SVD of gate projections?\n4. Does it target ReGLU-based models specifically?\n5. What models does it evaluate on?\n\nTry:\n- \"SVD contextual sparsity predictors arXiv 2603.14110\"\n- \"site:arxiv.org 2603.14110\"\n\nReport findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "323c3a15-fee3-4dda-8c26-45f8ec0f267c",
  "isSidechain": false,
  "requestId": "req_011CawzZeH6iXu7ow8nFnXbn",
  "type": "assistant",
  "uuid": "df6334f4-2573-479e-b95e-0ab4e8930886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtKGiBGViFM31WdDuedC8x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2186,
      "cache_creation_input_tokens": 9354,
      "cache_read_input_tokens": 40731,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2186,
          "output_tokens": 959,
          "cache_read_input_tokens": 40731,
          "cache_creation_input_tokens": 9354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9354
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

_source line 24 · 2026-05-12T03:50:17.561Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01ApVHS8uzjcA8snif6UhJtu`</summary>

```json
{
  "description": "Check WINA baseline numbers",
  "subagent_type": "general-purpose",
  "prompt": "Search for and verify claims about WINA (Weight Informed Neuron Activation) paper, ICLR 2026:\n\n1. Does WINA report 59.57% average on Llama-3-8B at 50% model-level sparsity across PIQA, ARC-c, WinoGrande, HellaSwag, MMLU, GSM8K?\n2. Is the dense model baseline 66.38% on the same benchmarks?\n3. Does WINA use a greedy per-layer sparsity allocation algorithm?\n4. Does WINA find that attention layers tolerate ~2.3x higher sparsity than MLP layers?\n\nTry:\n- \"WINA weight informed neuron activation ICLR 2026\"\n- \"site:arxiv.org WINA weight informed neuron activation\"\n\nReport findings in detail, especially the exact benchmark numbers if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df6334f4-2573-479e-b95e-0ab4e8930886",
  "isSidechain": false,
  "requestId": "req_011CawzZeH6iXu7ow8nFnXbn",
  "type": "assistant",
  "uuid": "0132f1f3-94e2-4fea-a18f-20946418960c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtKGiBGViFM31WdDuedC8x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2186,
      "cache_creation_input_tokens": 9354,
      "cache_read_input_tokens": 40731,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2186,
          "output_tokens": 959,
          "cache_read_input_tokens": 40731,
          "cache_creation_input_tokens": 9354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9354
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

_source line 25 · 2026-05-12T03:50:24.269Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HniqNjEkETcWM2RMpEgNwW`</summary>

```json
{
  "description": "Search for anti-evidence KL vs BCE",
  "subagent_type": "general-purpose",
  "prompt": "I'm reviewing a research proposal that claims KL-divergence is better than BCE (binary cross-entropy) for training sparsity predictors in LLMs, arguing that BCE's per-neuron independent decomposition is a \"mean-field approximation\" that misses joint neuron interactions. Search for evidence FOR and AGAINST this claim:\n\n1. Are there papers comparing KL vs BCE for training sparsity predictors or masks?\n2. Are there papers showing BCE-trained predictors work just as well or better than distillation-based approaches?\n3. Is the \"mean-field factorization\" argument for BCE's limitation well-established in the literature?\n4. Are there theoretical analyses of per-neuron vs joint optimization for neural network pruning/sparsity?\n5. Has anyone shown that BCE + error compensation (like FastForward) matches or exceeds KL-based approaches?\n\nTry:\n- \"KL divergence vs BCE sparsity prediction neural network\"\n- \"mean field approximation neuron pruning\"\n- \"joint optimization sparsity mask distillation\"\n- \"output distribution distillation vs binary classification sparsity\"\n- \"error compensation sparsity predictor LLM\"\n\nReport any evidence that contradicts or supports the mean-field argument."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0132f1f3-94e2-4fea-a18f-20946418960c",
  "isSidechain": false,
  "requestId": "req_011CawzZeH6iXu7ow8nFnXbn",
  "type": "assistant",
  "uuid": "ac57dc77-8208-44b5-acab-1755f91b19c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtKGiBGViFM31WdDuedC8x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2186,
      "cache_creation_input_tokens": 9354,
      "cache_read_input_tokens": 40731,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2186,
          "output_tokens": 959,
          "cache_read_input_tokens": 40731,
          "cache_creation_input_tokens": 9354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9354
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

_source line 26 · 2026-05-12T03:50:50.465Z_

<details><summary>↩ Tool result · `toolu_018hzrLrrhpEbkQkmh6WXpH3`</summary>

```text
Here are the findings for each of your questions:

---

**1. Does the paper exist? Is it from March 2026?**

Yes, confirmed. The paper "SVD Contextual Sparsity Predictors for Fast LLM Inference" exists at arXiv:2603.14110. It was submitted on **March 14, 2026**. Authors: Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, and C.C. Korikov.

**2. Does it find that learned predictors suffer from out-of-distribution sensitivity?**

Yes. The paper explicitly states: *"Trained predictors may suffer from out-of-distribution sensitivity due to their data-dependent nature, while SVD predictors directly leverage the LLM's internal weight structure."* This is a key motivation for their training-free SVD-based approach over learned predictors like Deja Vu and PowerInfer.

**3. Does it use truncated SVD of gate projections?**

Yes. The core method uses "truncation-aware singular value decomposition (SVD) of the gate projection matrix" to build lightweight, training-free sparse pattern predictors. This is the central technical contribution of the paper.

**4. Does it target ReGLU-based models specifically?**

Yes. The paper explicitly targets ReGLU-activated feed-forward networks (FFNs) within LLMs. It notes that "a key characteristic of ReGLU-based LLMs is dynamic (or contextual) sparsity," leveraging the fact that ReLU gating zeroes out neurons whose computations can be safely skipped.

**5. What models does it evaluate on?**

Three 7B-parameter sparse models:
- **ProSparse-LLaMA2-7B**
- **SparseQwen2-7B** (instruction-tuned)
- **TurboSparse-Mistral-Instruct** (instruction-tuned)

The experiments demonstrate up to **1.8x end-to-end decoding speedup** at ~90% FFN activation sparsity, with less than 1% degradation on benchmarks involving complex math and code generation. The framework supports inference on both CUDA and CANN devices.

---

Sources:
- [arXiv abstract page: 2603.14110](https://arxiv.org/abs/2603.14110)
- [arXiv HTML full paper: 2603.14110](https://arxiv.org/html/2603.14110)

agentId: a9d21ee8a60f2959b (use SendMessage with to: 'a9d21ee8a60f2959b' to continue this agent)
&lt;usage>total_tokens: 15449
tool_uses: 6
duration_ms: 39397&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df6334f4-2573-479e-b95e-0ab4e8930886",
  "isSidechain": false,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "type": "user",
  "uuid": "ac5a75cb-ec47-46de-9187-ae99566d948d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the paper \"SVD Contextual Sparsity Predictors for Fast LLM Inference\" (arXiv 2603.14110, March 2026). Verify:\n\n1. Does it exist? Is it from March 2026?\n2. Does it find that learned predictors suffer from out-of-distribution sensitivity?\n3. Does it use truncated SVD of gate projections?\n4. Does it target ReGLU-based models specifically?\n5. What models does it evaluate on?\n\nTry:\n- \"SVD contextual sparsity predictors arXiv 2603.14110\"\n- \"site:arxiv.org 2603.14110\"\n\nReport findings.",
    "agentId": "a9d21ee8a60f2959b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings for each of your questions:\n\n---\n\n**1. Does the paper exist? Is it from March 2026?**\n\nYes, confirmed. The paper \"SVD Contextual Sparsity Predictors for Fast LLM Inference\" exists at arXiv:2603.14110. It was submitted on **March 14, 2026**. Authors: Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, and C.C. Korikov.\n\n**2. Does it find that learned predictors suffer from out-of-distribution sensitivity?**\n\nYes. The paper explicitly states: *\"Trained predictors may suffer from out-of-distribution sensitivity due to their data-dependent nature, while SVD predictors directly leverage the LLM's internal weight structure.\"* This is a key motivation for their training-free SVD-based approach over learned predictors like Deja Vu and PowerInfer.\n\n**3. Does it use truncated SVD of gate projections?**\n\nYes. The core method uses \"truncation-aware singular value decomposition (SVD) of the gate projection matrix\" to build lightweight, training-free sparse pattern predictors. This is the central technical contribution of the paper.\n\n**4. Does it target ReGLU-based models specifically?**\n\nYes. The paper explicitly targets ReGLU-activated feed-forward networks (FFNs) within LLMs. It notes that \"a key characteristic of ReGLU-based LLMs is dynamic (or contextual) sparsity,\" leveraging the fact that ReLU gating zeroes out neurons whose computations can be safely skipped.\n\n**5. What models does it evaluate on?**\n\nThree 7B-parameter sparse models:\n- **ProSparse-LLaMA2-7B**\n- **SparseQwen2-7B** (instruction-tuned)\n- **TurboSparse-Mistral-Instruct** (instruction-tuned)\n\nThe experiments demonstrate up to **1.8x end-to-end decoding speedup** at ~90% FFN activation sparsity, with less than 1% degradation on benchmarks involving complex math and code generation. The framework supports inference on both CUDA and CANN devices.\n\n---\n\nSources:\n- [arXiv abstract page: 2603.14110](https://arxiv.org/abs/2603.14110)\n- [arXiv HTML full paper: 2603.14110](https://arxiv.org/html/2603.14110)"
      }
    ],
    "totalDurationMs": 39397,
    "totalTokens": 15449,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 11906,
      "output_tokens": 600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 600,
          "cache_read_input_tokens": 11906,
          "cache_creation_input_tokens": 2942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2942,
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
  "sourceToolAssistantUUID": "df6334f4-2573-479e-b95e-0ab4e8930886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T03:52:28.167Z_

<details><summary>↩ Tool result · `toolu_01ApVHS8uzjcA8snif6UhJtu`</summary>

```text
Now I have a thorough picture. Let me compile my findings.

Here is my detailed analysis of each claim about the WINA paper:

---

## Paper Confirmed

WINA (Weight Informed Neuron Activation) is a real paper accepted at ICLR 2026, authored by Sihan Chen et al. from Microsoft and collaborating universities. It is available as arXiv:2505.19427 and on OpenReview (id: l7Vb3yxmuz). The GitHub repository is at [github.com/microsoft/wina](https://github.com/microsoft/wina).

---

## Claim 1: WINA reports 59.57% average on Llama-3-8B at 50% model-level sparsity across PIQA, ARC-c, WinoGrande, HellaSwag, MMLU, GSM8K

**VERIFIED -- TRUE.** Table 3 of the paper reports the following WINA results at 50% model-level sparsity on Llama-3-8B:

| Benchmark | Score |
|-----------|-------|
| PIQA | 78.35 |
| ARC-c | 49.06 |
| WinoGrande | 70.32 |
| HellaSwag | 75.12 |
| MMLU | 55.26 |
| GSM8K | 29.34 |
| **Average** | **59.57** |

This outperforms TEAL (58.51 avg) by +1.06% and TEAL-transform (59.19 avg) by +0.38%.

---

## Claim 2: The dense model baseline is 66.38% on the same benchmarks

**VERIFIED -- TRUE.** The dense baseline (0% sparsity) for Llama-3-8B from Table 3 is:

| Benchmark | Score |
|-----------|-------|
| PIQA | 80.79 |
| ARC-c | 53.33 |
| WinoGrande | 72.61 |
| HellaSwag | 79.17 |
| MMLU | 62.20 |
| GSM8K | 50.19 |
| **Average** | **66.38** |

---

## Claim 3: WINA uses a greedy per-layer sparsity allocation algorithm

**PARTIALLY TRUE -- but requires clarification.** WINA does use a greedy per-layer sparsity allocation algorithm, but it is **not WINA's own contribution**. The paper explicitly states:

> "To further improve performance, we assign layer-specific sparsity ratios instead of a uniform sparsity across the model. Given a global sparsity target, we leverage the **greedy algorithm proposed in TEAL** to iteratively configure per-layer sparsity levels such that the aggregate sparsity meets the global budget."

The greedy algorithm was proposed by TEAL and adopted by WINA. The GitHub repo also confirms this, offering a `--greedy` flag that enables sparsity allocation "through the greedy algorithm proposed in TEAL." So it is accurate to say WINA **uses** a greedy per-layer sparsity allocation algorithm, but inaccurate to say WINA **proposes** one.

---

## Claim 4: WINA finds that attention layers tolerate ~2.3x higher sparsity than MLP layers

**NOT VERIFIED -- likely conflated or fabricated.** After thorough searching:

- The actual paper text (arXiv HTML version) contains **no mention of "2.3" in the context of attention vs. MLP sparsity ratios**.
- The paper's appendices contain only mathematical proofs, with no layer-wise sparsity analysis comparing attention and MLP layers.
- No figures in the paper show per-layer sparsity distributions comparing attention vs. MLP layers.
- One blog post title mentions "2.3x Speed Boost" in its headline about WINA, which appears to refer to **inference speed improvement**, not a sparsity tolerance ratio. This is likely the source of confusion.
- A web search snippet did surface the claim "Attention layers tolerate 2.3x higher sparsity than FFN layers without performance loss," but this appears to originate from an AI-generated blog summary (xugj520.cn/Efficient Coder), not from the paper itself. The blog's content could not be verified as it failed to load.

The paper's core contribution is a better neuron importance scoring mechanism (combining hidden state magnitudes with weight norms), not a layer-type sparsity analysis. The 2.3x attention-vs-MLP claim does not appear to be a finding reported in the WINA paper.

---

## Summary

| Claim | Verdict |
|-------|---------|
| 59.57% average at 50% sparsity on Llama-3-8B | **Confirmed** |
| 66.38% dense baseline | **Confirmed** |
| Greedy per-layer sparsity allocation | **Confirmed (but borrowed from TEAL, not WINA's own)** |
| Attention layers tolerate ~2.3x higher sparsity than MLP | **Not found in the paper; likely from an unreliable secondary source** |

Sources:
- [WINA arXiv paper (HTML)](https://arxiv.org/html/2505.19427v1)
- [WINA arXiv abstract](https://arxiv.org/abs/2505.19427)
- [WINA OpenReview](https://openreview.net/forum?id=l7Vb3yxmuz)
- [WINA GitHub repository](https://github.com/microsoft/wina)
- [Microsoft Research page](https://www.microsoft.com/en-us/research/publication/wina-weight-informed-neuron-activation-for-accelerating-large-language-model-inference/)
- [MarkTechPost article](https://www.marktechpost.com/2025/05/31/this-ai-paper-from-microsoft-introduces-wina-a-training-free-sparse-activation-framework-for-efficient-large-language-model-inference/)

agentId: a82aaa5cff3ab6d39 (use SendMessage with to: 'a82aaa5cff3ab6d39' to continue this agent)
&lt;usage>total_tokens: 24196
tool_uses: 18
duration_ms: 130603&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0132f1f3-94e2-4fea-a18f-20946418960c",
  "isSidechain": false,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "type": "user",
  "uuid": "302facfa-6544-4a56-8ea6-d25d66f8a914",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify claims about WINA (Weight Informed Neuron Activation) paper, ICLR 2026:\n\n1. Does WINA report 59.57% average on Llama-3-8B at 50% model-level sparsity across PIQA, ARC-c, WinoGrande, HellaSwag, MMLU, GSM8K?\n2. Is the dense model baseline 66.38% on the same benchmarks?\n3. Does WINA use a greedy per-layer sparsity allocation algorithm?\n4. Does WINA find that attention layers tolerate ~2.3x higher sparsity than MLP layers?\n\nTry:\n- \"WINA weight informed neuron activation ICLR 2026\"\n- \"site:arxiv.org WINA weight informed neuron activation\"\n\nReport findings in detail, especially the exact benchmark numbers if available.",
    "agentId": "a82aaa5cff3ab6d39",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a thorough picture. Let me compile my findings.\n\nHere is my detailed analysis of each claim about the WINA paper:\n\n---\n\n## Paper Confirmed\n\nWINA (Weight Informed Neuron Activation) is a real paper accepted at ICLR 2026, authored by Sihan Chen et al. from Microsoft and collaborating universities. It is available as arXiv:2505.19427 and on OpenReview (id: l7Vb3yxmuz). The GitHub repository is at [github.com/microsoft/wina](https://github.com/microsoft/wina).\n\n---\n\n## Claim 1: WINA reports 59.57% average on Llama-3-8B at 50% model-level sparsity across PIQA, ARC-c, WinoGrande, HellaSwag, MMLU, GSM8K\n\n**VERIFIED -- TRUE.** Table 3 of the paper reports the following WINA results at 50% model-level sparsity on Llama-3-8B:\n\n| Benchmark | Score |\n|-----------|-------|\n| PIQA | 78.35 |\n| ARC-c | 49.06 |\n| WinoGrande | 70.32 |\n| HellaSwag | 75.12 |\n| MMLU | 55.26 |\n| GSM8K | 29.34 |\n| **Average** | **59.57** |\n\nThis outperforms TEAL (58.51 avg) by +1.06% and TEAL-transform (59.19 avg) by +0.38%.\n\n---\n\n## Claim 2: The dense model baseline is 66.38% on the same benchmarks\n\n**VERIFIED -- TRUE.** The dense baseline (0% sparsity) for Llama-3-8B from Table 3 is:\n\n| Benchmark | Score |\n|-----------|-------|\n| PIQA | 80.79 |\n| ARC-c | 53.33 |\n| WinoGrande | 72.61 |\n| HellaSwag | 79.17 |\n| MMLU | 62.20 |\n| GSM8K | 50.19 |\n| **Average** | **66.38** |\n\n---\n\n## Claim 3: WINA uses a greedy per-layer sparsity allocation algorithm\n\n**PARTIALLY TRUE -- but requires clarification.** WINA does use a greedy per-layer sparsity allocation algorithm, but it is **not WINA's own contribution**. The paper explicitly states:\n\n> \"To further improve performance, we assign layer-specific sparsity ratios instead of a uniform sparsity across the model. Given a global sparsity target, we leverage the **greedy algorithm proposed in TEAL** to iteratively configure per-layer sparsity levels such that the aggregate sparsity meets the global budget.\"\n\nThe greedy algorithm was proposed by TEAL and adopted by WINA. The GitHub repo also confirms this, offering a `--greedy` flag that enables sparsity allocation \"through the greedy algorithm proposed in TEAL.\" So it is accurate to say WINA **uses** a greedy per-layer sparsity allocation algorithm, but inaccurate to say WINA **proposes** one.\n\n---\n\n## Claim 4: WINA finds that attention layers tolerate ~2.3x higher sparsity than MLP layers\n\n**NOT VERIFIED -- likely conflated or fabricated.** After thorough searching:\n\n- The actual paper text (arXiv HTML version) contains **no mention of \"2.3\" in the context of attention vs. MLP sparsity ratios**.\n- The paper's appendices contain only mathematical proofs, with no layer-wise sparsity analysis comparing attention and MLP layers.\n- No figures in the paper show per-layer sparsity distributions comparing attention vs. MLP layers.\n- One blog post title mentions \"2.3x Speed Boost\" in its headline about WINA, which appears to refer to **inference speed improvement**, not a sparsity tolerance ratio. This is likely the source of confusion.\n- A web search snippet did surface the claim \"Attention layers tolerate 2.3x higher sparsity than FFN layers without performance loss,\" but this appears to originate from an AI-generated blog summary (xugj520.cn/Efficient Coder), not from the paper itself. The blog's content could not be verified as it failed to load.\n\nThe paper's core contribution is a better neuron importance scoring mechanism (combining hidden state magnitudes with weight norms), not a layer-type sparsity analysis. The 2.3x attention-vs-MLP claim does not appear to be a finding reported in the WINA paper.\n\n---\n\n## Summary\n\n| Claim | Verdict |\n|-------|---------|\n| 59.57% average at 50% sparsity on Llama-3-8B | **Confirmed** |\n| 66.38% dense baseline | **Confirmed** |\n| Greedy per-layer sparsity allocation | **Confirmed (but borrowed from TEAL, not WINA's own)** |\n| Attention layers tolerate ~2.3x higher sparsity than MLP | **Not found in the paper; likely from an unreliable secondary source** |\n\nSources:\n- [WINA arXiv paper (HTML)](https://arxiv.org/html/2505.19427v1)\n- [WINA arXiv abstract](https://arxiv.org/abs/2505.19427)\n- [WINA OpenReview](https://openreview.net/forum?id=l7Vb3yxmuz)\n- [WINA GitHub repository](https://github.com/microsoft/wina)\n- [Microsoft Research page](https://www.microsoft.com/en-us/research/publication/wina-weight-informed-neuron-activation-for-accelerating-large-language-model-inference/)\n- [MarkTechPost article](https://www.marktechpost.com/2025/05/31/this-ai-paper-from-microsoft-introduces-wina-a-training-free-sparse-activation-framework-for-efficient-large-language-model-inference/)"
      }
    ],
    "totalDurationMs": 130603,
    "totalTokens": 24196,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 20973,
      "output_tokens": 1489,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1733
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1489,
          "cache_read_input_tokens": 20973,
          "cache_creation_input_tokens": 1733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1733,
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
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "0132f1f3-94e2-4fea-a18f-20946418960c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T03:54:01.589Z_

<details><summary>↩ Tool result · `toolu_01HniqNjEkETcWM2RMpEgNwW`</summary>

```text
I now have comprehensive evidence across all five questions. Here is my synthesized report.

---

## Evidence Report: KL-Divergence vs BCE for Training Sparsity Predictors in LLMs

### 1. Papers Comparing KL vs BCE for Training Sparsity Predictors or Masks

**No direct head-to-head comparison exists in the literature.** This is the most important finding. I could not locate any paper that directly benchmarks KL-divergence (output distribution matching) against BCE (per-neuron binary classification) as competing loss functions for training the same sparsity predictor architecture. The two approaches are used in largely separate research traditions:

- **BCE-based predictors** are the dominant paradigm for activation sparsity prediction. **DejaVu** (ICML 2023, [arXiv 2310.17157](https://arxiv.org/abs/2310.17157)) trains its two-layer MLP sparsity predictor explicitly with `torch.nn.functional.binary_cross_entropy`, treating each neuron as an independent binary classification target. This approach is inherited by **PowerInfer** ([arXiv 2312.12456](https://arxiv.org/pdf/2312.12456)), **ShadowLLM** ([arXiv 2406.16635](https://arxiv.org/abs/2406.16635)), and **FastForward** ([arXiv 2602.00397](https://arxiv.org/abs/2602.00397)).

- **KL-divergence** is used in a fundamentally different context -- full-model knowledge distillation (teacher-student output distribution matching) rather than neuron-level mask prediction. Papers like **MiniLLM** ([arXiv 2306.08543](https://arxiv.org/abs/2306.08543)) and NVIDIA's pruning+distillation work use KL to match the entire output vocabulary distribution of a pruned/sparse model to a dense teacher.

The absence of a direct comparison is itself noteworthy -- the proposal's central claim lacks direct empirical validation in the literature.

---

### 2. Evidence That BCE-Trained Predictors Work Well

**Strong evidence that BCE-trained predictors achieve excellent results:**

- **DejaVu** reports predictor validation accuracy of **>99% in shallow layers**, dropping to ~93% in deep layers, with **no accuracy loss at ~50% sparsity** on zero-shot downstream tasks. The predictor is trained with pure BCE loss.

- **FastForward** uses **weighted BCE** (with exponentially decaying weights for top activations) plus an **error compensation network**. It achieves **up to 1.45x speedup at 50% FFN sparsity with <6% accuracy loss** on LongBench across LLaMA and Qwen models up to 8B.

- **ShadowLLM** (EMNLP 2024) uses a BCE-style predictor and achieves **15% improvement in end-to-end accuracy over DejaVu** and **20% speed-up**, validated on models up to 30B parameters.

- **SVD Contextual Sparsity Predictors** ([arXiv 2603.14110](https://arxiv.org/html/2603.14110)) achieve **up to 1.8x decoding time reduction with <1% benchmark degradation** at 90% sparsity -- and they are entirely training-free, sidestepping the loss function question altogether.

These results demonstrate that the BCE paradigm (or even training-free approaches) can deliver competitive practical outcomes without needing KL-based output distribution matching.

---

### 3. The "Mean-Field Factorization" Argument: Is It Well-Established?

**The theoretical concept is well-established in Bayesian deep learning but has NOT been applied to sparsity predictor loss functions in the literature.** The proposal appears to be drawing an analogy rather than citing established work:

**Supporting the theoretical framework (mean-field limitations are real):**

- The OATML blog post ["Is Mean-Field Good Enough for Variational Inference in Bayesian Neural Networks?"](https://oatml.cs.ox.ac.uk/blog/2020/11/29/liberty_or_depth.html) (Oxford, 2020) shows that mean-field VI works surprisingly well in deep networks but fails in single-layer or very wide networks.

- **Coker et al. (2022)** proved that ["Wide Mean-Field Bayesian Neural Networks Ignore the Data"](https://arxiv.org/abs/2202.11670) -- as width grows, the mean-field variational posterior converges to the prior, completely ignoring the data. This is a rigorous theoretical result published at AISTATS.

- **Daxberger et al. (2023)** ([arXiv 2305.03395](https://arxiv.org/abs/2305.03395)) showed that replacing mean-field VI with **normalizing flows** for latent binary variable BNNs yields **sparser networks with better predictive power**, and notably performs better "at variable selection in a logistic regression setting with **highly correlated variables**."

**However, the analogy to BCE sparsity predictors is a stretch:**

The mean-field factorization in Bayesian pruning refers to approximating the posterior over weights with independent Gaussians per weight. BCE for sparsity prediction is a different thing -- it is a supervised learning objective, not a variational inference procedure. The per-neuron independence in BCE is an assumption about the loss decomposition, not a variational approximation to a posterior. While the analogy has intuitive appeal ("treating neurons independently misses joint structure"), it conflates two different mathematical frameworks.

---

### 4. Per-Neuron vs Joint Optimization: Theoretical and Empirical Evidence

**Evidence that neuron correlations matter:**

- **Neuralink** (ASPLOS 2025, [arXiv 2410.19274](https://arxiv.org/abs/2410.19274)) directly exploits **neuron co-activation patterns** -- neurons that frequently activate together -- for efficient memory layout and I/O. This demonstrates that joint activation structure exists and is practically exploitable.

- **Activation Pattern Clustering** ([arXiv 2507.14179](https://arxiv.org/html/2507.14179v1)) notes that "a primary limitation was the inability to account for the unique distribution and correlation of active neurons, leading to suboptimal centroid assignments." This supports the idea that ignoring correlations has costs.

- From computational neuroscience, Schneidman et al. (2006) in [Nature](https://pubmed.ncbi.nlm.nih.gov/16625187/) showed that "weak pairwise correlations imply strongly correlated network states in a neural population" -- even weak pairwise neuron correlations produce strong collective effects. This is the strongest theoretical support for the proposal's argument.

**Evidence that per-neuron independence works well enough in practice:**

- DejaVu's >99% per-neuron prediction accuracy with simple BCE suggests that for most neurons, activation is highly predictable from the input alone, and the marginal/independent prediction may already capture most of the variance.

- Multiple training-free methods (GRIFFIN, SparseInfer, SVD predictors) achieve competitive results without modeling joint neuron distributions at all, suggesting that individual neuron behavior is sufficiently predictable from local information.

- **Joint optimization via distillation** (e.g., OpenVINO's JPQD framework) does show benefits, but these combine pruning + quantization + distillation holistically rather than comparing loss functions for a fixed predictor architecture.

---

### 5. BCE + Error Compensation (FastForward) vs KL-Based Approaches

**FastForward demonstrates that BCE + error compensation is highly effective, but no direct comparison with KL-based alternatives exists:**

- FastForward's architecture explicitly addresses the limitation that BCE predictors may introduce errors by adding a **dedicated error compensation network** that corrects sparsity-induced errors at the token level. The compensator "applies corrections only along the most confident direction, resulting in weak but consistent adjustments."

- The system achieves **1.45x speedup with <6% accuracy loss** -- competitive with any reported sparsity method.

- Importantly, the error compensation mechanism is a pragmatic engineering solution to the exact problem the proposal identifies (per-neuron predictions missing joint effects), but it addresses it post-hoc rather than through the loss function. This suggests BCE + compensation may be a viable alternative to changing the loss function entirely.

- No paper I found compares "BCE predictor + error compensation" against "KL-based output distillation predictor" on the same benchmarks.

---

## Summary Assessment

| Claim in the Proposal | Evidence Status |
|---|---|
| KL is better than BCE for sparsity predictors | **No direct empirical evidence found** -- no paper compares them head-to-head |
| BCE's per-neuron decomposition is a "mean-field approximation" | **Loose analogy, not established terminology** -- mean-field VI is a different mathematical framework than supervised BCE |
| BCE misses joint neuron interactions | **Theoretically plausible** (neuron co-activation is real), but **practically, BCE predictors achieve >99% accuracy** |
| Mean-field limitations are well-established | **Yes, in Bayesian deep learning** (Coker et al., OATML), but the transfer to sparsity predictor loss functions is the proposal's own novel claim |
| Error compensation can fix BCE's limitations | **FastForward provides evidence this works** but no comparison with KL alternatives exists |

**Bottom line:** The proposal's argument has theoretical plausibility -- neuron co-activations exist and mean-field approximations have known limitations. However, the specific claim that KL is better than BCE for sparsity predictors is **unsupported by existing empirical literature**. The practical success of BCE-based predictors (DejaVu, ShadowLLM, FastForward) and even training-free methods suggests that per-neuron independence may be a surprisingly good approximation for this specific task. The "mean-field" framing is an analogy borrowed from Bayesian inference, not an established result about BCE sparsity predictor losses.

Sources:
- [DejaVu: Contextual Sparsity for Efficient LLMs](https://arxiv.org/abs/2310.17157)
- [FastForward: Accelerating LLM Prefill with Predictive FFN Sparsity](https://arxiv.org/abs/2602.00397)
- [ShadowLLM: Predictor-based Contextual Sparsity](https://arxiv.org/abs/2406.16635)
- [SVD Contextual Sparsity Predictors](https://arxiv.org/html/2603.14110)
- [PowerInfer: Fast LLM Serving](https://arxiv.org/pdf/2312.12456)
- [Is Mean-Field Good Enough for VI in BNNs? (OATML)](https://oatml.cs.ox.ac.uk/blog/2020/11/29/liberty_or_depth.html)
- [Wide Mean-Field Bayesian Neural Networks Ignore the Data](https://arxiv.org/abs/2202.11670)
- [Sparsifying BNNs with Latent Binary Variables and Normalizing Flows](https://arxiv.org/abs/2305.03395)
- [Neuralink: Neuron Co-Activation Linking](https://arxiv.org/abs/2410.19274)
- [Activation Pattern Clustering for LLM Sparsity](https://arxiv.org/html/2507.14179v1)
- [GRIFFIN: Training-Free MoE for Efficient LLM Generation](https://arxiv.org/html/2408.11393v1)
- [SparseInfer: Training-Free Activation Sparsity Prediction](https://arxiv.org/html/2411.12692v1)
- [Sparsity in Deep Learning Survey (Hoefler et al.)](https://arxiv.org/abs/2102.00554)
- [On LLM Knowledge Distillation: Forward KL vs Reverse KL (ICLR 2025)](https://iclr-blogposts.github.io/2025/blog/llm-knowledge-distil/)
- [Weak Pairwise Correlations Imply Strongly Correlated Network States (Schneidman et al.)](https://pubmed.ncbi.nlm.nih.gov/16625187/)
- [Joint Pruning, Quantization and Distillation (OpenVINO)](https://blog.openvino.ai/blog-posts/joint-pruning-quantization-and-distillation-for-efficient-inference-of-transformers)
- [MiniLLM: On-Policy Distillation of Large Language Models](https://arxiv.org/abs/2306.08543)
- [Polar Sparsity: High Throughput Batched LLM Inferencing](https://arxiv.org/pdf/2505.14884)

agentId: a9e90b1ccc8687918 (use SendMessage with to: 'a9e90b1ccc8687918' to continue this agent)
&lt;usage>total_tokens: 44595
tool_uses: 32
duration_ms: 217317&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac57dc77-8208-44b5-acab-1755f91b19c3",
  "isSidechain": false,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "type": "user",
  "uuid": "19df7ba4-a59d-4a57-87db-c2cc00b2c2bf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research proposal that claims KL-divergence is better than BCE (binary cross-entropy) for training sparsity predictors in LLMs, arguing that BCE's per-neuron independent decomposition is a \"mean-field approximation\" that misses joint neuron interactions. Search for evidence FOR and AGAINST this claim:\n\n1. Are there papers comparing KL vs BCE for training sparsity predictors or masks?\n2. Are there papers showing BCE-trained predictors work just as well or better than distillation-based approaches?\n3. Is the \"mean-field factorization\" argument for BCE's limitation well-established in the literature?\n4. Are there theoretical analyses of per-neuron vs joint optimization for neural network pruning/sparsity?\n5. Has anyone shown that BCE + error compensation (like FastForward) matches or exceeds KL-based approaches?\n\nTry:\n- \"KL divergence vs BCE sparsity prediction neural network\"\n- \"mean field approximation neuron pruning\"\n- \"joint optimization sparsity mask distillation\"\n- \"output distribution distillation vs binary classification sparsity\"\n- \"error compensation sparsity predictor LLM\"\n\nReport any evidence that contradicts or supports the mean-field argument.",
    "agentId": "a9e90b1ccc8687918",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive evidence across all five questions. Here is my synthesized report.\n\n---\n\n## Evidence Report: KL-Divergence vs BCE for Training Sparsity Predictors in LLMs\n\n### 1. Papers Comparing KL vs BCE for Training Sparsity Predictors or Masks\n\n**No direct head-to-head comparison exists in the literature.** This is the most important finding. I could not locate any paper that directly benchmarks KL-divergence (output distribution matching) against BCE (per-neuron binary classification) as competing loss functions for training the same sparsity predictor architecture. The two approaches are used in largely separate research traditions:\n\n- **BCE-based predictors** are the dominant paradigm for activation sparsity prediction. **DejaVu** (ICML 2023, [arXiv 2310.17157](https://arxiv.org/abs/2310.17157)) trains its two-layer MLP sparsity predictor explicitly with `torch.nn.functional.binary_cross_entropy`, treating each neuron as an independent binary classification target. This approach is inherited by **PowerInfer** ([arXiv 2312.12456](https://arxiv.org/pdf/2312.12456)), **ShadowLLM** ([arXiv 2406.16635](https://arxiv.org/abs/2406.16635)), and **FastForward** ([arXiv 2602.00397](https://arxiv.org/abs/2602.00397)).\n\n- **KL-divergence** is used in a fundamentally different context -- full-model knowledge distillation (teacher-student output distribution matching) rather than neuron-level mask prediction. Papers like **MiniLLM** ([arXiv 2306.08543](https://arxiv.org/abs/2306.08543)) and NVIDIA's pruning+distillation work use KL to match the entire output vocabulary distribution of a pruned/sparse model to a dense teacher.\n\nThe absence of a direct comparison is itself noteworthy -- the proposal's central claim lacks direct empirical validation in the literature.\n\n---\n\n### 2. Evidence That BCE-Trained Predictors Work Well\n\n**Strong evidence that BCE-trained predictors achieve excellent results:**\n\n- **DejaVu** reports predictor validation accuracy of **>99% in shallow layers**, dropping to ~93% in deep layers, with **no accuracy loss at ~50% sparsity** on zero-shot downstream tasks. The predictor is trained with pure BCE loss.\n\n- **FastForward** uses **weighted BCE** (with exponentially decaying weights for top activations) plus an **error compensation network**. It achieves **up to 1.45x speedup at 50% FFN sparsity with <6% accuracy loss** on LongBench across LLaMA and Qwen models up to 8B.\n\n- **ShadowLLM** (EMNLP 2024) uses a BCE-style predictor and achieves **15% improvement in end-to-end accuracy over DejaVu** and **20% speed-up**, validated on models up to 30B parameters.\n\n- **SVD Contextual Sparsity Predictors** ([arXiv 2603.14110](https://arxiv.org/html/2603.14110)) achieve **up to 1.8x decoding time reduction with <1% benchmark degradation** at 90% sparsity -- and they are entirely training-free, sidestepping the loss function question altogether.\n\nThese results demonstrate that the BCE paradigm (or even training-free approaches) can deliver competitive practical outcomes without needing KL-based output distribution matching.\n\n---\n\n### 3. The \"Mean-Field Factorization\" Argument: Is It Well-Established?\n\n**The theoretical concept is well-established in Bayesian deep learning but has NOT been applied to sparsity predictor loss functions in the literature.** The proposal appears to be drawing an analogy rather than citing established work:\n\n**Supporting the theoretical framework (mean-field limitations are real):**\n\n- The OATML blog post [\"Is Mean-Field Good Enough for Variational Inference in Bayesian Neural Networks?\"](https://oatml.cs.ox.ac.uk/blog/2020/11/29/liberty_or_depth.html) (Oxford, 2020) shows that mean-field VI works surprisingly well in deep networks but fails in single-layer or very wide networks.\n\n- **Coker et al. (2022)** proved that [\"Wide Mean-Field Bayesian Neural Networks Ignore the Data\"](https://arxiv.org/abs/2202.11670) -- as width grows, the mean-field variational posterior converges to the prior, completely ignoring the data. This is a rigorous theoretical result published at AISTATS.\n\n- **Daxberger et al. (2023)** ([arXiv 2305.03395](https://arxiv.org/abs/2305.03395)) showed that replacing mean-field VI with **normalizing flows** for latent binary variable BNNs yields **sparser networks with better predictive power**, and notably performs better \"at variable selection in a logistic regression setting with **highly correlated variables**.\"\n\n**However, the analogy to BCE sparsity predictors is a stretch:**\n\nThe mean-field factorization in Bayesian pruning refers to approximating the posterior over weights with independent Gaussians per weight. BCE for sparsity prediction is a different thing -- it is a supervised learning objective, not a variational inference procedure. The per-neuron independence in BCE is an assumption about the loss decomposition, not a variational approximation to a posterior. While the analogy has intuitive appeal (\"treating neurons independently misses joint structure\"), it conflates two different mathematical frameworks.\n\n---\n\n### 4. Per-Neuron vs Joint Optimization: Theoretical and Empirical Evidence\n\n**Evidence that neuron correlations matter:**\n\n- **Neuralink** (ASPLOS 2025, [arXiv 2410.19274](https://arxiv.org/abs/2410.19274)) directly exploits **neuron co-activation patterns** -- neurons that frequently activate together -- for efficient memory layout and I/O. This demonstrates that joint activation structure exists and is practically exploitable.\n\n- **Activation Pattern Clustering** ([arXiv 2507.14179](https://arxiv.org/html/2507.14179v1)) notes that \"a primary limitation was the inability to account for the unique distribution and correlation of active neurons, leading to suboptimal centroid assignments.\" This supports the idea that ignoring correlations has costs.\n\n- From computational neuroscience, Schneidman et al. (2006) in [Nature](https://pubmed.ncbi.nlm.nih.gov/16625187/) showed that \"weak pairwise correlations imply strongly correlated network states in a neural population\" -- even weak pairwise neuron correlations produce strong collective effects. This is the strongest theoretical support for the proposal's argument.\n\n**Evidence that per-neuron independence works well enough in practice:**\n\n- DejaVu's >99% per-neuron prediction accuracy with simple BCE suggests that for most neurons, activation is highly predictable from the input alone, and the marginal/independent prediction may already capture most of the variance.\n\n- Multiple training-free methods (GRIFFIN, SparseInfer, SVD predictors) achieve competitive results without modeling joint neuron distributions at all, suggesting that individual neuron behavior is sufficiently predictable from local information.\n\n- **Joint optimization via distillation** (e.g., OpenVINO's JPQD framework) does show benefits, but these combine pruning + quantization + distillation holistically rather than comparing loss functions for a fixed predictor architecture.\n\n---\n\n### 5. BCE + Error Compensation (FastForward) vs KL-Based Approaches\n\n**FastForward demonstrates that BCE + error compensation is highly effective, but no direct comparison with KL-based alternatives exists:**\n\n- FastForward's architecture explicitly addresses the limitation that BCE predictors may introduce errors by adding a **dedicated error compensation network** that corrects sparsity-induced errors at the token level. The compensator \"applies corrections only along the most confident direction, resulting in weak but consistent adjustments.\"\n\n- The system achieves **1.45x speedup with <6% accuracy loss** -- competitive with any reported sparsity method.\n\n- Importantly, the error compensation mechanism is a pragmatic engineering solution to the exact problem the proposal identifies (per-neuron predictions missing joint effects), but it addresses it post-hoc rather than through the loss function. This suggests BCE + compensation may be a viable alternative to changing the loss function entirely.\n\n- No paper I found compares \"BCE predictor + error compensation\" against \"KL-based output distillation predictor\" on the same benchmarks.\n\n---\n\n## Summary Assessment\n\n| Claim in the Proposal | Evidence Status |\n|---|---|\n| KL is better than BCE for sparsity predictors | **No direct empirical evidence found** -- no paper compares them head-to-head |\n| BCE's per-neuron decomposition is a \"mean-field approximation\" | **Loose analogy, not established terminology** -- mean-field VI is a different mathematical framework than supervised BCE |\n| BCE misses joint neuron interactions | **Theoretically plausible** (neuron co-activation is real), but **practically, BCE predictors achieve >99% accuracy** |\n| Mean-field limitations are well-established | **Yes, in Bayesian deep learning** (Coker et al., OATML), but the transfer to sparsity predictor loss functions is the proposal's own novel claim |\n| Error compensation can fix BCE's limitations | **FastForward provides evidence this works** but no comparison with KL alternatives exists |\n\n**Bottom line:** The proposal's argument has theoretical plausibility -- neuron co-activations exist and mean-field approximations have known limitations. However, the specific claim that KL is better than BCE for sparsity predictors is **unsupported by existing empirical literature**. The practical success of BCE-based predictors (DejaVu, ShadowLLM, FastForward) and even training-free methods suggests that per-neuron independence may be a surprisingly good approximation for this specific task. The \"mean-field\" framing is an analogy borrowed from Bayesian inference, not an established result about BCE sparsity predictor losses.\n\nSources:\n- [DejaVu: Contextual Sparsity for Efficient LLMs](https://arxiv.org/abs/2310.17157)\n- [FastForward: Accelerating LLM Prefill with Predictive FFN Sparsity](https://arxiv.org/abs/2602.00397)\n- [ShadowLLM: Predictor-based Contextual Sparsity](https://arxiv.org/abs/2406.16635)\n- [SVD Contextual Sparsity Predictors](https://arxiv.org/html/2603.14110)\n- [PowerInfer: Fast LLM Serving](https://arxiv.org/pdf/2312.12456)\n- [Is Mean-Field Good Enough for VI in BNNs? (OATML)](https://oatml.cs.ox.ac.uk/blog/2020/11/29/liberty_or_depth.html)\n- [Wide Mean-Field Bayesian Neural Networks Ignore the Data](https://arxiv.org/abs/2202.11670)\n- [Sparsifying BNNs with Latent Binary Variables and Normalizing Flows](https://arxiv.org/abs/2305.03395)\n- [Neuralink: Neuron Co-Activation Linking](https://arxiv.org/abs/2410.19274)\n- [Activation Pattern Clustering for LLM Sparsity](https://arxiv.org/html/2507.14179v1)\n- [GRIFFIN: Training-Free MoE for Efficient LLM Generation](https://arxiv.org/html/2408.11393v1)\n- [SparseInfer: Training-Free Activation Sparsity Prediction](https://arxiv.org/html/2411.12692v1)\n- [Sparsity in Deep Learning Survey (Hoefler et al.)](https://arxiv.org/abs/2102.00554)\n- [On LLM Knowledge Distillation: Forward KL vs Reverse KL (ICLR 2025)](https://iclr-blogposts.github.io/2025/blog/llm-knowledge-distil/)\n- [Weak Pairwise Correlations Imply Strongly Correlated Network States (Schneidman et al.)](https://pubmed.ncbi.nlm.nih.gov/16625187/)\n- [Joint Pruning, Quantization and Distillation (OpenVINO)](https://blog.openvino.ai/blog-posts/joint-pruning-quantization-and-distillation-for-efficient-inference-of-transformers)\n- [MiniLLM: On-Policy Distillation of Large Language Models](https://arxiv.org/abs/2306.08543)\n- [Polar Sparsity: High Throughput Batched LLM Inferencing](https://arxiv.org/pdf/2505.14884)"
      }
    ],
    "totalDurationMs": 217317,
    "totalTokens": 44595,
    "totalToolUseCount": 32,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1003,
      "cache_read_input_tokens": 40459,
      "output_tokens": 3132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1003
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3132,
          "cache_read_input_tokens": 40459,
          "cache_creation_input_tokens": 1003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1003,
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
  "sourceToolAssistantUUID": "ac57dc77-8208-44b5-acab-1755f91b19c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "19df7ba4-a59d-4a57-87db-c2cc00b2c2bf",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Composing Static and Contextual Corrections for Activation Sparsity in SwiGLU LLMs via Output-Distribution Distillation",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

### Assistant

_source line 31 · 2026-05-12T03:56:24.041Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize all findings and form my judgment.

## Key Findings from Verification

### Round 7 Issues — Were They Addressed?
1. **RULER added**: YES — RULER is now included in the evaluation with detailed description (13 tasks, 4 categories, 4K-32K tokens, 500 examples per task).
2. **IFPruning cited**: YES — now cited and distinguished from the proposal's approach.
3. **DIP characterization fixed**: YES — changed to "logit-matching knowledge distillation (loss function unspecified in paper, likely KL)."

All three Round 7 issues are addressed.


### Factual Verification

I'm checking the core claims across both papers. SPON's KL-divergence approach, the five benchmarks in Table 2, and the performance numbers all check out against the paper. The ICML 2026 timeline appears consistent with the arXiv metadata. FastForward's claims are also verifying correctly.

For WINA, the 50% sparsity results and dense baseline match what's reported, and the greedy allocation strategy is confirmed though it's adapted from TEAL rather than original to WINA. However, I can't find direct verification in the paper for the claim about attention tolerating roughly 2.3x higher sparsity than MLPs—that seems to come from a less reliable source.

I'm also noting that SVD Contextual Sparsity Predictors exists as a March 2026 work.

Moving to RULER, the benchmark itself is confirmed from COLM 2024 with its 13 tasks split across retrieval, multi-hop, aggregation, and QA categories. The GitHub repository and 500 examples per task check out, along with the recall-based scoring approach. The "computationally lightweight" claim is partially accurate—the synthetic data and deterministic scoring are efficient, but running the full evaluation at long context lengths does add computational overhead.

Now I'm noticing several relevant papers that didn't make it into the proposal. TwELL uses a tile-wise sparse format with custom CUDA kernels for H100s, which is a different technical approach but still in the sparse inference space. DynamicInfer targets a different deployment scenario with runtime-aware offloading across consumer GPUs and CPUs. There's also a systematic study of activation sparsity patterns across model families that provides useful background context. La RoSA was mentioned in earlier rounds as a training-free approach but seems to have been left out of the current landscape section, possibly intentionally depending on how it fits the scope.

Beyond those, there are a few other methods worth noting: SparseInfer uses sign-bit prediction as an alternative to learned predictors, Sparsing Law establishes scaling relationships for activation sparsity, and Sparse Logit Sampling applies sparse techniques to knowledge distillation with KL divergence. Most of these feel tangential rather than directly competitive—the training-free methods don't really challenge the proposal's learned predictor approach, the hardware optimizations are complementary, and several target different model architectures entirely.

But there's a more pressing concern: the claim about attention layers tolerating roughly 2.3x higher sparsity than MLP layers doesn't appear to hold up under scrutiny.

The proposal relies on this ratio to justify how sparsity should be allocated between attention and MLP components, but it's actually using WINA's greedy per-layer algorithm to determine the allocation empirically anyway, so the specific number matters less for the method itself than for how it's framed.

Looking at the mean-field argument more carefully, I notice there's no existing comparison between KL and BCE for sparsity prediction in the literature. The "mean-field factorization" framing is something the proposal introduces as an analogy rather than established theory. Neuron co-activation is definitely real—Neuralink's work confirms that—but BCE predictors already achieve over 99% per-neuron accuracy, and FastForward's approach combining BCE with error compensation works remarkably well. This actually strengthens the proposal's position since the controlled ablation comparing KL versus BCE becomes genuinely novel, though the theoretical justification is weaker than presented—it's more of an intuitive analogy than a rigorous proof.

Evaluating the core criteria: novelty-wise, this is the first work training contextual sparsity predictors with KL-divergence (SPON used KL but only for static bias vectors), the first direct KL versus BCE ablation for this application, and the first study composing SPON with contextual predictors. The mean-field formalization is novel though somewhat loose. That puts novelty around 3.5 to 4 out of 5—the combination is genuinely new even if the pieces exist separately.

For feasibility, the timeline is extremely tight with 14 days to the ARR deadline and auto_research estimating 14 days as well. Compute-wise, the project needs 102 to 160 H100-hours and has a 200 H100-hour budget, so that's workable. SPON reimplementation is straightforward—just bias vectors trained with KL—and the FastForward compensation MLP is simple to add.

RULER integration is straightforward since NVIDIA provides open-source code, though the 2.3x attention sparsity claim from the WINA paper is unverified; the proposal will determine this empirically through WINA's greedy allocation. The tight timeline is the main risk given the ambitious experimental scope for two weeks.

The proposal itself is very detailed and well-structured with a clear four-condition ablation design, honest reporting of both wall-clock and FLOPs overhead, and thoughtful fallback plans. If KL training subsumes error compensation, that eliminates roughly 256 MB of deployment overhead and simplifies the system. The composition recipe of SPON plus contextual predictor is practically useful, and the mean-field analysis could provide theoretical guidance for future work.

Now I'm checking the specific factual claims — the WINA paper doesn't actually report the 2.3x sparsity figure, so that's a mischaracterization in the proposal description, though the empirical approach using WINA's greedy allocation still works. The competitor landscape looks reasonable with no critical omissions, and the SPON benchmark count of five is correctly cited.

The timeline is the real constraint here — fourteen days with auto_research is tight, especially with the paper writing buffer built in, though feasible with multiple H100s running in parallel. The improvement target of 1.5-3 points is grounded conservatively in SPON's verified gains plus reasonable contextual estimates. The mean-field framing is novel but somewhat informal as terminology, though the underlying mathematical argument appears sound.

There's a factual issue though: the 2.3x number cited in the approach isn't actually in the WINA paper, which a reviewer could catch. Setting that aside, the experimental design itself is solid — the four-condition ablation and composition study are well-structured, the novelty claims are appropriately scoped, and the fallback strategies are clearly articulated. All the Round 7 concerns have been addressed, and the benchmarks align with what was requested.

The 2.3x claim is a minor factual error that doesn't undermine the method since the approach relies on WINA's empirically calibrated greedy allocation regardless of the specific ratio. The timeline is genuinely tight at 14 days, but the proposal acknowledges this with concrete fallback plans. The mean-field argument is more of an interesting analogy than an established result, but the core direction is sound and addresses a real gap in the literature.

Scoring across dimensions: novelty lands at 3.5 since the combination of KL-trained contextual predictor, SPON composition, and mean-field analysis is novel but incremental—each component exists elsewhere, and the contribution is primarily in how they're combined and compared. Feasibility is also 3.5, with the tight timeline being the main constraint despite the ambitious scope. Clarity is strong at 4.5 given the exceptionally well-articulated proposal, clear experimental design, and explicit fallback strategies. Impact comes in at 3.5 because while the practical benefits are meaningful if the hypotheses hold, the expected improvements of 1.5-3 points are modest. This averages to 3.75, which falls short of the 4.0 pass threshold.

But I'm reconsidering this. We're in Round 8 of 10, and the issues are becoming increasingly minor. The core direction is fundamentally sound. Looking more carefully at novelty: this is actually the first work to train contextual sparsity predictors using KL divergence on output logits rather than static bias, to test SPON and contextual predictor composition together, to formalize the mean-field argument explaining BCE's limitations, and to provide a controlled four-condition ablation across BCE, BCE with composition, KL, and KL with composition. These are genuinely novel contributions—the four-condition ablation especially represents the kind of rigorous controlled comparison the community needs. I'd revise novelty up to 3.5-4. On feasibility, the timeline is tight but not impossible, and the fallback strategies provide real insurance. - SPON reimplementation is "architecturally trivial" (confirmed — bias vectors)
- FastForward compensation is a simple 2-layer MLP
- Triton kernels reused from TEAL/WINA
- RULER has an open-source codebase
- 2-4 concurrent H100s available
- Explicit fallback plans

I'd put feasibility at 3.5. The 14-day timeline with 3 days for paper writing is genuinely risky.

**Clarity**: 4.5. This is one of the most detailed and well-organized proposals I've reviewed.

**Impact**: 3.5. The practical recommendation (use KL, skip compensation) would be useful if confirmed. The composition recipe is practical. But the improvement magnitude is modest.

Average: 3.75. Below 4.0 threshold.

But reconsidering whether this actually fits EMNLP's Efficient Methods track — the controlled ablations, practical recipes with honest overhead reporting, and comprehensive evaluation across 9 benchmarks all align well with what that venue values. The novelty is solid too: first KL-trained contextual predictor, first composition study, first KL versus BCE ablation, plus the mean-field analysis and long-context generalization work together as a coherent package addressing multiple open questions. The main constraint remains the timeline risk, though the scope is manageable with the available resources. is narrowed appropriately and fallbacks are clear.
- Clarity: 4.5 — Exceptionally well-articulated.
- Impact: 3.5 — Practically useful if hypotheses confirm; modest improvement magnitude.

Average: 3.875. Still below 4.0.

The main remaining issues are the 2.3x attention sparsity claim that I need to verify more carefully, the tight 14-day timeline putting completion at risk, the mean-field framing being presented as more established than it actually is, and the absence of preliminary results to validate the core hypothesis. This is round 8 of 10, and while the proposal has improved substantially, these are revise-level issues rather than fundamental failures. The direction is sound and the experimental design is well-controlled, so I should issue a revise verdict with specific guidance. Let me reconsider the 2.3x claim though — the proposal cites WINA's differentiation between attention and MLP layer sparsity, and while the exact 2.3x figure isn't explicitly stated in the paper, the greedy allocation algorithm does assign different per-layer sparsity ratios as shown in their results. The core contribution feels incremental—it's essentially combining existing techniques like KL distillation, contextual prediction, and composition in a new way. My honest assessment puts novelty, feasibility, and impact each around 3.5, with clarity at 4.5, averaging to 3.75, which falls short of the 4.0 bar. But I should step back and think about what actual EMNLP reviewers would make of this work.

For the Efficient Methods track, there's real value here: the controlled ablation showing KL outperforms BCE for sparsity predictors, the practical recipe of combining static and contextual corrections, comprehensive evaluation on long-context tasks, transparent wall-clock timing, and the mean-field formalization with testable predictions. The modest improvement margins (1.5-3 points) aren't the weakness I initially thought—for an efficiency paper, the insight matters more than raw numbers. EMNLP Findings seems achievable; Main would require a more striking result.

Scoring this out: Novelty 3.5, Feasibility 3.5, Clarity 4.5, Impact 3.5 puts me at 3.75, below the 4.0 threshold, so revision is needed. The issues are fairly straightforward though. One thing worth flagging is the RULER evaluation stopping at 32K instead of extending to 64K-128K where the most interesting failure modes would surface, but that's a reasonable timeline tradeoff. The factual error about the 2.3x claim is the most concrete problem to fix, and the rest are minor framing and scope concerns.

Looking back at my concerns more carefully, I need to distinguish between actual issues and nitpicks. The 2.3x claim is definitely a factual error that hurts credibility if someone checks the source. The newly discovered competing papers are mostly tangential and don't directly challenge the core contribution. And the mean-field analogy, while presented as an original insight rather than an established result, is framed appropriately as a testable prediction with solid mathematical grounding.

The timeline constraint and RULER's limited scope are both acknowledged limitations rather than hidden flaws. Weighing everything together—the four-condition ablation plus composition analysis is genuinely novel, the execution is feasible despite timeline risks, the writing is clear, and the practical impact is solid if modest—this feels like solid EMNLP Findings material, probably landing around 3.9 overall.

At Round 8 of 10, the remaining issues are minor enough that I can see a clear path forward: fix the 2.3x factual error and amplify how the work simplifies the field by eliminating compensation networks entirely. That should push it over 4.0. Otherwise, I should be honest that this is a well-executed efficiency paper that's competitive for Findings but not quite Main conference caliber.

Looking at the actual scores more carefully—averaging 3.75-3.875—they're below the 4.0 threshold even accounting for agent inflation. The individual ratings make sense: the novelty is solid but incremental, feasibility is reasonable with some timeline risk, clarity is genuinely excellent, and impact is useful but modest. This profile fits EMNLP Findings perfectly, which means I need to decide whether to push for Main with targeted revisions or accept the Findings tier.

Since we're at Round 8 of 10 and the gaps are fixable, I should recommend "revise" with concrete guidance: strengthening the novelty narrative to better articulate what's genuinely new, tightening the feasibility timeline to reduce risk, and amplifying the impact claims with more compelling evidence. The realistic path forward is Findings acceptance with a shot at Main if those three areas improve meaningfully.

Actually, reconsidering the novelty score—the systematic four-condition ablation, the composition study combining SPON with contextual prediction, the long-context evaluation against established benchmarks, and the mean-field formalization all represent genuine contributions that fit well within EMNLP's efficiency methods track, where careful empirical work with novel experimental design is valued.

Let me settle on Novelty 4, Feasibility 3.5, Clarity 4.5, Impact 3.5, averaging 3.875. That's still just under the threshold, so the honest call is "revise" with targeted improvements. The core issue isn't the novelty or the approach—it's the timeline risk and modest expected impact. But if I isolate the one concrete factual error about the 2.3x attention sparsity claim and fix that, the question becomes whether the paper would actually pass at EMNLP if the results came through as expected. That hinges on whether the KL-only approach can match the BCE+compensation baseline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19df7ba4-a59d-4a57-87db-c2cc00b2c2bf",
  "isSidechain": false,
  "requestId": "req_011CawzsB5yx3TdGyWLXtX6u",
  "type": "assistant",
  "uuid": "1c705986-9655-4610-98d3-47ba3fb98db0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfefvVSmSBoDoKdr9oorMc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8670,
      "cache_read_input_tokens": 50085,
      "output_tokens": 6840,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6840,
          "cache_read_input_tokens": 50085,
          "cache_creation_input_tokens": 8670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8670
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

_source line 32 · 2026-05-12T03:56:24.416Z_

Now let me check one final thing — the specific 2.3x attention sparsity claim from WINA, which my verification found may be unsubstantiated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c705986-9655-4610-98d3-47ba3fb98db0",
  "isSidechain": false,
  "requestId": "req_011CawzsB5yx3TdGyWLXtX6u",
  "type": "assistant",
  "uuid": "ad8bf00a-d0c5-4b3d-8d95-fa60ce6e7cae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfefvVSmSBoDoKdr9oorMc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8670,
      "cache_read_input_tokens": 50085,
      "output_tokens": 6840,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6840,
          "cache_read_input_tokens": 50085,
          "cache_creation_input_tokens": 8670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8670
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

_source line 33 · 2026-05-12T03:56:33.881Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Rgu6BD6tpHvvAU5f6BHVh1`</summary>

```json
{
  "description": "Verify WINA attention vs MLP sparsity",
  "subagent_type": "general-purpose",
  "prompt": "I need to verify a specific claim: \"WINA found that attention layers tolerate ~2.3× higher sparsity than MLP layers.\"\n\nThe WINA paper is \"Weight Informed Neuron Activation for Accelerating Large Language Model Inference\" (ICLR 2026, arXiv 2505.19427).\n\nA previous search found that the paper does NOT contain the \"2.3x\" number. But I need to verify more carefully:\n\n1. Fetch the WINA paper HTML at https://arxiv.org/html/2505.19427v1 and search for any discussion of attention vs MLP sparsity ratios, per-layer sparsity allocation results, or the number \"2.3\"\n2. Check if the paper's figures or tables show per-layer sparsity distributions\n3. Check the TEAL paper (which WINA borrows its greedy allocation from) — does TEAL report attention vs MLP sparsity ratios?\n\nThis is important because if the 2.3x claim is not in the paper, citing \"WINA found\" is a factual error.\n\nReport exactly what the papers say about attention vs MLP sparsity allocation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad8bf00a-d0c5-4b3d-8d95-fa60ce6e7cae",
  "isSidechain": false,
  "requestId": "req_011CawzsB5yx3TdGyWLXtX6u",
  "type": "assistant",
  "uuid": "efd0efaa-fe6a-449a-8f67-11bbc564057a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfefvVSmSBoDoKdr9oorMc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8670,
      "cache_read_input_tokens": 50085,
      "output_tokens": 6840,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6840,
          "cache_read_input_tokens": 50085,
          "cache_creation_input_tokens": 8670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8670
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "efd0efaa-fe6a-449a-8f67-11bbc564057a",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Composing Static and Contextual Corrections for Activation Sparsity in SwiGLU LLMs via Output-Distribution Distillation",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

### Tool result

_source line 36 · 2026-05-12T03:59:05.260Z_

<details><summary>↩ Tool result · `toolu_01Rgu6BD6tpHvvAU5f6BHVh1`</summary>

```text
I now have comprehensive evidence. Here is my complete report.

---

## Verification Result: The "2.3x" Claim is NOT in the WINA Paper

### What the WINA paper (arXiv 2505.19427) actually says

The WINA paper contains **zero discussion** of attention layers vs. MLP layers having different sparsity tolerances. It does not contain the number "2.3" in any context — not as a sparsity ratio, not as a speedup, not anywhere.

The paper's only mention of per-layer sparsity allocation is this single sentence in Section 4.1 (Experimental Setup):

> "Given a global sparsity target, we leverage the greedy algorithm proposed in TEAL to iteratively configure per-layer sparsity levels such that the aggregate sparsity meets the global budget."

That is the entirety of what WINA says about layer-wise sparsity allocation. It delegates the mechanism to TEAL and reports no findings about differential sparsity tolerance between layer types.

I verified all 5 tables and 2 figures in the WINA paper. None show per-layer sparsity distributions, attention vs. MLP comparisons, or the number 2.3.

### What the TEAL paper (arXiv 2408.14690) actually says

The TEAL paper is the origin of the greedy allocation algorithm that WINA uses. TEAL **does** have a relevant analysis in Section 5.4.2 ("Block-wise Greedy Sparsities") and Figure 7, which shows greedy sparsity allocations for Llama-3-70B at 50% model-level sparsity.

Key findings from TEAL's Section 5.4.2 (verbatim quotes):

- **Attention layers:** "W_q, W_k exhibit high sparsifiability in Block 0, followed by a sharp decline. W_o's sparsifiability varies dynamically: it starts at 50-60%, peaks at 80-90% mid-model, then returns to 50-60% in the final blocks."

- **MLP layers:** "Across all blocks, W_down is more sparsifiable than W_gate, which is more sparsifiable than W_up."

Critically, TEAL's Figure 7 actually suggests the **opposite** of the claimed finding: **MLP parameters appear MORE sparsifiable than attention parameters** on average (MLP layers typically show 40-80% sparsity, while attention layers typically show 20-60% sparsity across blocks). However, TEAL never computes or states an aggregate ratio between the two. It never mentions "2.3x" or any similar ratio. Its analysis is purely qualitative and per-weight-matrix, not aggregated by layer type.

### Where the "2.3x" claim likely originates

A web search reveals the "2.3x" number appears on an AI-generated blog post at `xugj520.cn/en/archives/wina-framework-llm-inference.html` with the title "How WINA Framework Accelerates LLM Inference: 40% Memory Reduction & 2.3x Speed Boost." This appears to be an LLM-generated summary that fabricated or hallucinated specific numbers not present in the paper. The "2.3x speed boost" in that blog title likely also has no basis in the paper — WINA reports FLOPs reductions (up to ~60-63%), not wall-clock speedups, and no number close to 2.3 appears in any of its tables.

### Conclusion

**The claim "WINA found that attention layers tolerate ~2.3x higher sparsity than MLP layers" is a factual error on multiple levels:**

1. The number "2.3" does not appear anywhere in the WINA paper.
2. WINA does not report any findings about attention vs. MLP sparsity tolerance — it simply uses TEAL's greedy allocation without analyzing the results.
3. The TEAL paper (which does analyze per-layer sparsity) does not state any such ratio either.
4. To the extent TEAL's Figure 7 shows a pattern, it suggests MLP layers are **more** sparsifiable than attention layers, which is the **opposite direction** from the claim.
5. The "2.3x" number appears to originate from an AI-generated blog post that fabricated details not present in the source paper.

Citing "WINA found" for this claim would be a factual misattribution of a fabricated statistic.

agentId: a179e328ee8acd67a (use SendMessage with to: 'a179e328ee8acd67a' to continue this agent)
&lt;usage>total_tokens: 23829
tool_uses: 17
duration_ms: 151374&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efd0efaa-fe6a-449a-8f67-11bbc564057a",
  "isSidechain": false,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "type": "user",
  "uuid": "a2c521c8-98fa-4c2d-9492-8b2a533d9660",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify a specific claim: \"WINA found that attention layers tolerate ~2.3× higher sparsity than MLP layers.\"\n\nThe WINA paper is \"Weight Informed Neuron Activation for Accelerating Large Language Model Inference\" (ICLR 2026, arXiv 2505.19427).\n\nA previous search found that the paper does NOT contain the \"2.3x\" number. But I need to verify more carefully:\n\n1. Fetch the WINA paper HTML at https://arxiv.org/html/2505.19427v1 and search for any discussion of attention vs MLP sparsity ratios, per-layer sparsity allocation results, or the number \"2.3\"\n2. Check if the paper's figures or tables show per-layer sparsity distributions\n3. Check the TEAL paper (which WINA borrows its greedy allocation from) — does TEAL report attention vs MLP sparsity ratios?\n\nThis is important because if the 2.3x claim is not in the paper, citing \"WINA found\" is a factual error.\n\nReport exactly what the papers say about attention vs MLP sparsity allocation.",
    "agentId": "a179e328ee8acd67a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive evidence. Here is my complete report.\n\n---\n\n## Verification Result: The \"2.3x\" Claim is NOT in the WINA Paper\n\n### What the WINA paper (arXiv 2505.19427) actually says\n\nThe WINA paper contains **zero discussion** of attention layers vs. MLP layers having different sparsity tolerances. It does not contain the number \"2.3\" in any context — not as a sparsity ratio, not as a speedup, not anywhere.\n\nThe paper's only mention of per-layer sparsity allocation is this single sentence in Section 4.1 (Experimental Setup):\n\n> \"Given a global sparsity target, we leverage the greedy algorithm proposed in TEAL to iteratively configure per-layer sparsity levels such that the aggregate sparsity meets the global budget.\"\n\nThat is the entirety of what WINA says about layer-wise sparsity allocation. It delegates the mechanism to TEAL and reports no findings about differential sparsity tolerance between layer types.\n\nI verified all 5 tables and 2 figures in the WINA paper. None show per-layer sparsity distributions, attention vs. MLP comparisons, or the number 2.3.\n\n### What the TEAL paper (arXiv 2408.14690) actually says\n\nThe TEAL paper is the origin of the greedy allocation algorithm that WINA uses. TEAL **does** have a relevant analysis in Section 5.4.2 (\"Block-wise Greedy Sparsities\") and Figure 7, which shows greedy sparsity allocations for Llama-3-70B at 50% model-level sparsity.\n\nKey findings from TEAL's Section 5.4.2 (verbatim quotes):\n\n- **Attention layers:** \"W_q, W_k exhibit high sparsifiability in Block 0, followed by a sharp decline. W_o's sparsifiability varies dynamically: it starts at 50-60%, peaks at 80-90% mid-model, then returns to 50-60% in the final blocks.\"\n\n- **MLP layers:** \"Across all blocks, W_down is more sparsifiable than W_gate, which is more sparsifiable than W_up.\"\n\nCritically, TEAL's Figure 7 actually suggests the **opposite** of the claimed finding: **MLP parameters appear MORE sparsifiable than attention parameters** on average (MLP layers typically show 40-80% sparsity, while attention layers typically show 20-60% sparsity across blocks). However, TEAL never computes or states an aggregate ratio between the two. It never mentions \"2.3x\" or any similar ratio. Its analysis is purely qualitative and per-weight-matrix, not aggregated by layer type.\n\n### Where the \"2.3x\" claim likely originates\n\nA web search reveals the \"2.3x\" number appears on an AI-generated blog post at `xugj520.cn/en/archives/wina-framework-llm-inference.html` with the title \"How WINA Framework Accelerates LLM Inference: 40% Memory Reduction & 2.3x Speed Boost.\" This appears to be an LLM-generated summary that fabricated or hallucinated specific numbers not present in the paper. The \"2.3x speed boost\" in that blog title likely also has no basis in the paper — WINA reports FLOPs reductions (up to ~60-63%), not wall-clock speedups, and no number close to 2.3 appears in any of its tables.\n\n### Conclusion\n\n**The claim \"WINA found that attention layers tolerate ~2.3x higher sparsity than MLP layers\" is a factual error on multiple levels:**\n\n1. The number \"2.3\" does not appear anywhere in the WINA paper.\n2. WINA does not report any findings about attention vs. MLP sparsity tolerance — it simply uses TEAL's greedy allocation without analyzing the results.\n3. The TEAL paper (which does analyze per-layer sparsity) does not state any such ratio either.\n4. To the extent TEAL's Figure 7 shows a pattern, it suggests MLP layers are **more** sparsifiable than attention layers, which is the **opposite direction** from the claim.\n5. The \"2.3x\" number appears to originate from an AI-generated blog post that fabricated details not present in the source paper.\n\nCiting \"WINA found\" for this claim would be a factual misattribution of a fabricated statistic."
      }
    ],
    "totalDurationMs": 151374,
    "totalTokens": 23829,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 22154,
      "output_tokens": 1061,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 613
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1061,
          "cache_read_input_tokens": 22154,
          "cache_creation_input_tokens": 613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 613,
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
  "sourceToolAssistantUUID": "efd0efaa-fe6a-449a-8f67-11bbc564057a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-12T03:59:05.267Z_

```json
{
  "parentUuid": "a2c521c8-98fa-4c2d-9492-8b2a533d9660",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9e28515a-d74c-4bf1-8a16-431e7e017210",
  "timestamp": "2026-05-12T03:59:05.267Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-12T03:59:59.219Z_

Now I have comprehensive verification results. Let me synthesize my findings into the review.

**Key findings from my independent verification:**

1. **SPON claims**: All verified (KL-divergence, 5 benchmarks in Table 2 confirmed, ICML 2026 plausible via arXiv metadata, numbers match)
2. **FastForward claims**: All 6 claims verified exactly
3. **WINA baseline numbers**: 59.57% and 66.38% dense confirmed
4. **WINA 2.3x attention claim**: **FABRICATED** — not in WINA paper, not in TEAL paper. Likely from an AI-generated blog hallucination. TEAL's Figure 7 actually suggests MLP layers are *more* sparsifiable than attention.
5. **RULER benchmark**: All details confirmed (13 tasks, 4 categories, 500 examples, NVIDIA codebase)
6. **SVD Contextual Sparsity Predictors**: All claims confirmed
7. **No critical missing competitors** that would undermine novelty — newly found papers (TwELL, DynamicInfer, Sparsing Law) are tangential
8. **KL vs BCE comparison**: No prior head-to-head exists, confirming the ablation's novelty. But the "mean-field" framing is an original analogy, not established terminology.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 4, "rationale": "The four-condition ablation (BCE, BCE+comp, KL, KL+comp), SPON+contextual composition, and mean-field formalization with testable sparsity-level prediction are genuinely novel contributions that no prior work provides. The controlled comparison is exactly what the community needs, even though individual components (KL distillation, contextual prediction) exist separately."},
    "feasibility": {"score": 3, "rationale": "14 days to ARR deadline with 102-160 H100-hours of experiments plus 3 days for paper writing is high-risk. The scope (9 benchmarks, 4 ablation conditions, 2 sparsity levels for interaction test, SPON reimplementation+validation, composition experiments, long-context evaluation including RULER's 13×4×500=26K examples) is ambitious even with 2-4 concurrent H100s and auto assistance."},
    "clarity": {"score": 5, "rationale": "Exceptionally well-articulated proposal with transparent overhead reporting (both FLOPs and wall-clock), precise experimental design, explicit fallback strategies, and honest qualification of claims (e.g., SPON venue, improvement target arithmetic). Among the best-organized proposals I have reviewed."},
    "impact": {"score": 3, "rationale": "The practical recommendation (use KL, skip compensation to eliminate ~256 MB overhead) is useful if confirmed, and the composition recipe is actionable. However, the expected improvement magnitude (1.5-3 points over WINA) is modest, and the work applies to a narrow operating point (batch=1 decode, 50% model-level sparsity on 8B models)."}
  },
  "issues": [
    "FACTUAL ERROR — WINA 2.3x ATTENTION SPARSITY CLAIM IS FABRICATED: The proposal states 'WINA found that attention layers tolerate ~2.3× higher sparsity than MLP layers' and uses this to justify MLP/attention sparsity allocation. Independent verification confirms: (1) the number '2.3' does not appear anywhere in the WINA paper; (2) WINA reports no findings about attention vs MLP sparsity tolerance — it simply uses TEAL's greedy allocation; (3) TEAL's own Figure 7 actually suggests MLP layers are MORE sparsifiable than attention, the opposite direction; (4) the '2.3x' originates from an AI-generated blog that fabricated details. This error appears in both the approach and description sections. If a reviewer checks the WINA paper and cannot find this claim, it damages the paper's credibility on all other detailed claims.",
    "TIMELINE-SCOPE TENSION: The auto_research timeline (14 days) includes 9 benchmarks, 4 ablation conditions at 50% sparsity, 2 additional runs at 40% for KL-BCE interaction, SPON reimplementation+validation, composition experiments, LongBench evaluation (4K-32K at batch=1 — estimated 8-12h alone), RULER evaluation (13 tasks × 4 context lengths × 500 examples), MT-Bench with GPT-4 judge, and wall-clock profiling — all with a 3-day paper writing buffer. This leaves effectively 11 days for all experiments. If ANY component takes longer than expected (SPON validation, kernel integration, long-context evaluation), the timeline collapses. Consider: (a) making RULER a stretch goal (evaluate at 4K and 16K only if time permits), (b) reducing LongBench to single-doc QA and summarization subtasks as the proposal's own fallback suggests, or (c) dropping the 40% sparsity interaction test entirely and arguing the mean-field prediction via a per-layer analysis at 50% instead.",
    "MEAN-FIELD FRAMING OVERSTATED: The proposal calls the mean-field argument 'our key theoretical contribution' and 'a formalized mean-field argument.' Independent search confirms: (a) no prior work applies the mean-field factorization framework to BCE sparsity predictor losses — this is the proposal's own novel analogy, not established terminology; (b) the BCE decomposition L_BCE = Σ_j l(y_j, s_j) is a loss decomposition, not a variational inference procedure — calling it 'mean-field' borrows terminology from Bayesian deep learning in a way reviewers may challenge; (c) DejaVu achieves >99% per-neuron prediction accuracy with pure BCE, suggesting the independent decomposition is a surprisingly good approximation in practice. Recommend: frame as 'an information-theoretic analogy to mean-field factorization' with appropriate caveats, and emphasize the testable prediction (KL advantage grows with sparsity) as the contribution rather than the formalism itself."
  ],
  "feedback": "The proposal has matured enormously over 8 rounds and the core research direction is strong. Three specific fixes would push this to pass:\n\n(1) **Fix the 2.3x fabrication (critical)**: Remove all instances of 'WINA found that attention layers tolerate ~2.3× higher sparsity than MLP layers.' Replace with: 'We use TEAL's greedy per-layer allocation algorithm (adopted by WINA) to distribute the 50% global FLOPs budget across all layers. The algorithm iteratively increases sparsity in the least-sensitive layer (measured by calibration perplexity impact) until the aggregate meets the global target. We report both the global model-level sparsity and the effective per-component (MLP, attention) sparsity ratios resulting from the allocation.' Do NOT cite a specific ratio — let the empirical allocation speak for itself.\n\n(2) **Soften the mean-field framing**: Change 'our key theoretical contribution formalizes BCE's limitation as a mean-field factorization' to 'we observe that BCE's per-neuron decomposition is analogous to a mean-field factorization that ignores joint neuron interactions, and derive a testable prediction: KL's advantage over BCE should increase with sparsity level because higher sparsity creates more simultaneous neuron removals.' The testable prediction is the real contribution, not the formalism. Add a brief caveat acknowledging that BCE predictors achieve high per-neuron accuracy (>99% in DejaVu), so the practical significance of the interaction terms is an empirical question — which is exactly what the ablation tests.\n\n(3) **De-risk the timeline**: Either (a) make RULER a conditional addition ('if time permits, we extend to RULER for fine-grained diagnostics; the core evaluation is perplexity + 5 discriminative benchmarks + LongBench + MT-Bench'), or (b) reduce RULER to 2 context lengths (4K, 16K) and 3 representative tasks (one from each category). The full 13×4×500 RULER evaluation is valuable but not essential for the paper's core claims about KL vs BCE and composition. Prioritize completing the four-condition ablation + composition + LongBench — these are the experiments that reviewers will judge the paper on.\n\nAll three fixes are straightforward. The experimental design, novelty framing (first KL-trained contextual predictor + first controlled KL/BCE ablation + first composition study), benchmark coverage, and fallback strategies are all strong. With these fixes, the proposal should pass in Round 9.",
  "reason": "One fabricated claim (WINA 2.3x), overstated mean-field formalism, and timeline-scope tension prevent passing despite otherwise excellent proposal quality."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e28515a-d74c-4bf1-8a16-431e7e017210",
  "isSidechain": false,
  "requestId": "req_011Cax1FZNnbUyD6QRvQ9Q4D",
  "type": "assistant",
  "uuid": "07218400-6f09-431d-b25a-df5b9bc4e8c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdyvcUswQ44ez4rovb7b49",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8071,
      "cache_read_input_tokens": 58755,
      "output_tokens": 2142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2142,
          "cache_read_input_tokens": 58755,
          "cache_creation_input_tokens": 8071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8071
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "07218400-6f09-431d-b25a-df5b9bc4e8c3",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Composing Static and Contextual Corrections for Activation Sparsity in SwiGLU LLMs via Output-Distribution Distillation",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20"
}
```

---
