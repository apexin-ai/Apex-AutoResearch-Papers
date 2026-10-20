# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-09 (UTC).** Your job: indep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/b2543a7e-fa6f-404f-9e22-c793de4d8c9f.jsonl`
- **Structured JSON:** [`5d669512675196ffb2cb.json`](../../sessions/5d/5d669512675196ffb2cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-09T18:52:15.272Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-09T18:52:15.272Z",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-09 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.\n\nDirection: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.\n\nContribution type: METHOD ONLY. Propose new algorithms — not profiling studies.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Generous for efficiency work.\n2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.\n3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.\n\nLook for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.\n\nTag: direction=efficiency, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-09?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 4/10)\n{\n  \"title\": \"Structure-Guided Draft Training for Reasoning Speculative Decoding\",\n  \"core_problem\": \"Speculative decoding draft models for reasoning LLMs are trained solely on next-token prediction, ignoring the structural grammar of thinking traces (reasoning → execution → transition). This misalignment causes drafts to generate locally plausible but structurally incoherent token sequences that the target model rejects, creating an acceptance-rate ceiling. While CoT-Aware draft training (OpenReview bKau2NNrji) has demonstrated that step-level process supervision improves draft alignment, no prior work applies thought-segment-level structural labels (R/E/T) as a training signal or imposes a Markov segment-transition consistency objective on structural sequence progressions — the mechanisms that would directly penalize structural incoherence at the thought-segment granularity where coherence is determined and where draft rejection most clearly correlates with structural mismatch.\",\n  \"opportunity\": \"ThinKV (ICLR 2026 Oral, arXiv:2510.01290) provides a thought-type taxonomy (R: reasoning, E: execution, T: transition) with an attention-sparsity heuristic that classifies tokens at the thought-segment level: the heuristic refreshes every τ=128 steps and assigns a single R/E/T label to the current segment window, which typically spans 100–300 tokens. All tokens within a segment window share one structural label. Although this heuristic was designed for KV-cache eviction rather than training supervision, its transferability as thought-segment-level structural labels is plausible and can be validated cheaply: a χ² test comparing R/E/T segment-type distributions of EAGLE-3-accepted vs. rejected draft segments on 1,000 sampled traces costs under 2 H100-hours and serves as a mandatory hypothesis gate before committing training budget. If validated, adding a lightweight auxiliary head to the draft model that jointly predicts structural segment type and next token — plus a Markov segment-transition consistency objective aligning predicted R→E→T segment-progression distributions to target-model-accepted trace distributions — forces the draft to internalize thinking-trace grammar at the granularity of structural units. The novelty claim is narrow and defensible: this is the first work to apply thought-segment-level R/E/T structural labels and a Markov segment-transition probability objective as draft training signals for R1-class extended reasoning models. CoT-Aware uses step-level distillation and SurpriseRatio data selection (operating at the CoT step boundary, not at the thought-segment level with explicit R/E/T type supervision); VSD optimizes a sequence-level ELBO with no reasoning-structure signal; SFDD (arXiv:2601.18902) uses flatness as a distributional property for data selection, not semantic structural role; LTD (arXiv:2603.01639) optimizes throughput via RL co-adaptive policies with no structural supervision — none impose thought-segment-level structural role supervision with segment-transition consistency, leaving a specific, measurable, and mechanistically grounded gap. The auxiliary head adds approximately 5M parameters, is frozen at inference (zero latency overhead), and is composable with any EAGLE-style architecture, verification-side improvements, or RL-based dynamic adaptation methods such as LTD.\",\n  \"landscape\": \"SCoT (Apr 2025, arXiv:2504.19095) achieves 48–66% latency reduction on DeepSeek-R1-Distill-32B and 21–49% on DeepSeek-R1-Distill-70B via thought-level drafting but uses a generic smaller model with no structural supervision. ARBITRAGE (arXiv:2512.05033) achieves ~2× latency reduction on mathematical reasoning benchmarks via advantage-aware routing — a lightweight router trained to predict when the target model will produce meaningfully better reasoning steps, selecting between draft and target model outputs at the step level; this is a routing-side approach orthogonal to draft-training-side structural supervision and composable with our method. CoT-Aware (OpenReview bKau2NNrji) is the closest prior work: it augments EAGLE-style draft training with process-level CoT distillation (step-level feature regression to reduce forward KL divergence at CoT step boundaries) and SurpriseRatio data selection to prevent catastrophic forgetting, reporting 3.04×–4.55× wall-clock speedups; crucially, it does NOT classify tokens or segments into structural roles (R/E/T), does NOT use a Markov segment-transition consistency objective, and operates at the reasoning-step granularity rather than at the thought-segment level defined by ThinKV's attention-sparsity heuristic — our two key differentiating mechanisms. 'Flatter Tokens are More Valuable for Speculative Draft Model Training' (arXiv:2601.18902, Jan 2026) proposes SFDD — flatness-based dataset distillation for draft training, selecting samples where the target model's predictive distribution is flatter (less confident), achieving over 2× training speedup using 50% of data. SFDD and our approach share the conceptual framing that training tokens are non-uniformly important, but flatness is a distributional property of the target model's output whereas structural role is a semantic property of the reasoning trace's content; the two are complementary and non-competing. 'Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning' (LTD, arXiv:2603.01639, ICLR 2026 Poster) achieves up to 36.4% speedup over EAGLE-3 by formulating speculative decoding as a reinforcement learning problem that trains co-adaptive draft and verify policies to directly optimize throughput across 5 LLMs and 4 tasks; LTD uses no reasoning-structure signal and treats draft/verify allocation as a dynamic policy rather than a static training objective. Our approach is orthogonal: thought-segment-level structural supervision modifies only draft training and is frozen at inference, making it directly composable with LTD's RL-based dynamic adaptation as a complementary enhancement to the draft model quality that LTD's RL policy leverages. 'Steering Pretrained Drafters' (Nov 2025, arXiv:2511.09844, AAAI 2026) shows a lightweight dynamic steering mechanism improves accepted tokens by up to 35% and throughput by 22%, confirming structural alignment is a bottleneck rather than draft capacity. Aurora (Feb 2026, arXiv:2602.06932) enables continuous on-policy RL-style draft adaptation but optimizes distribution matching, not reasoning-trace structural coherence. 'Training Domain Draft Models' (Mar 2025, arXiv:2503.07807) addresses distribution shift via knowledge distillation, not structural role mismatch. Variational Speculative Decoding (Feb 2026, arXiv:2602.05774) formulates draft training as variational inference over draft paths, achieving 9.6% speedup over EAGLE-3 on MT-Bench, HumanEval, and GSM8K — but uses no reasoning-structure signal and has not been evaluated on extended reasoning benchmarks (AIME24, AMC23, LiveCodeBench), leaving a direct comparison gap. OnlineSpec (Mar 2026, arXiv:2603.12617) proposes online preference-pair updates for draft model adaptation during reasoning — complementary to our static structural supervision approach. SemanticSpec (Feb 2026, arXiv:2602.03708) achieves 2.7× speedup on DeepSeek-R1-32B and 2.1× on QwQ-32B via verification-side semantic equivalence checking using internal hidden states — compelling parallel work on reasoning model speedup but strictly orthogonal (verification-side, not draft-training-side) and composable with our approach. SpecGuard (Apr 2026, arXiv:2604.15244) performs step-level verification using model-internal signals, and ConfSpec (Feb 2026, arXiv:2602.18447) uses confidence-gated cascaded verification — both verification-side and composable. ThinKV (ICLR 2026 Oral, arXiv:2510.01290) provides the R/E/T thought-type taxonomy via attention-sparsity heuristics operating at the segment level (τ=128 steps, 100–300 tokens per segment); this heuristic was designed for KV-cache eviction on DeepSeek-R1-Distill models and its precision as a thought-segment-level training-label generator must be validated empirically before full training commitment. No prior work combines thought-segment-level structural labels with a Markov segment-transition consistency objective as a speculative decoding draft training objective.\",\n  \"approach\": \"Phase 0 — Hypothesis Validation (days 1–2, ~2h H100; results constitute a 2-page analysis section in the paper): Sample 1,000 DeepSeek-R1-Distill-70B traces with EAGLE-3-generated draft tokens and known acceptance outcomes. Apply ThinKV's attention-sparsity heuristic to classify each ~128-token draft window as R, E, or T (all tokens within a window share one structural label per ThinKV's segment-level design). First, validate label quality: compute per-segment structural entropy; if ≥30% of segments fall into an ambiguous bin (above a tunable entropy threshold), tune the threshold on this 1K sample before proceeding — this prevents noise injection from poor labels. Second, run a χ² test comparing the marginal R/E/T segment-type distributions of EAGLE-3-accepted vs. rejected draft segments. If p < 0.05, the structural misalignment hypothesis is confirmed at the segment level and the training objectives are well-motivated. If p ≥ 0.05, pivot the measurement to structural segment-type divergence between the draft model's predicted R/E/T distributions and the target model's actual output segment distributions — this alternative analysis may reveal systematic structural biases in draft-model outputs (e.g., over-production of R segments, under-production of T segments) that manifest independent of per-segment acceptance, providing equally strong motivation for the Markov segment-transition objective. Both outcomes yield publishable pilot findings.\\n\\nPhase 1 — Draft Model Augmentation: Augment an EAGLE-3-based draft with a lightweight two-output head inserted after the multi-layer feature fusion layer: one output predicts the next token (standard cross-entropy loss L_token), a second predicts the current thought-segment type (R/E/T, cross-entropy auxiliary loss L_role weighted by α). Auto-generate R/E/T segment labels by applying ThinKV's attention-sparsity heuristic (τ=128 steps) to DeepSeek-R1-Distill-70B reasoning traces; all tokens within each ~128-token window share the same segment label, and zero human annotation is required. The auxiliary head learns to classify each token's structural context at segment granularity — effectively predicting which thought-segment type the current position falls within.\\n\\nPhase 2 — Markov Segment-Transition Consistency Objective: Add a third loss term L_trans (weighted by λ): from each draft trajectory extract the predicted R→E→T segment-transition sequence (one transition label per ~128-token window), compute KL divergence between this predicted segment-transition distribution and the empirically estimated transition distribution of target-model-accepted traces, and penalize divergence. Transitions are between thought segments (~100–300 tokens each), not between individual tokens — the Markov chain operates at the segment level, making the objective robust to token-level noise. This Markov segment-transition consistency objective is grounded in the Markov chain abstraction for speculative decoding established in 'A Theoretical Perspective for Speculative Decoding Algorithm' (arXiv:2411.00841, NeurIPS 2024), which analyzes fundamental SD performance limits via total variation distances between draft and target model distributions. Total training loss: L = L_token + α · L_role + λ · L_trans. The auxiliary head (~5M parameters) is frozen at inference time — zero latency overhead.\\n\\nPhase 3 — Experiments: Target model: DeepSeek-R1-Distill-70B (consistent with Phase 0; ThinKV was validated on R1-Distill attention patterns, ensuring label-transfer compatibility throughout all phases). Draft model sizes 1.5B, 3B, 7B (and 0.5B in auto-research mode); λ ∈ {0.01, 0.1, 0.5}; α fixed at 0.1 after Phase 0 pilot tuning. Benchmarks: AIME24, AMC23, LiveCodeBench (reasoning quality and task diversity for R1-class models); MT-Bench (general instruction-following quality — standard in the EAGLE-3 evaluation tradition, verifies structural supervision does not degrade instruction-following); HumanEval (code generation quality — verifies structural supervision does not degrade non-reasoning capabilities). Baselines: EAGLE-3, VSD, SCoT, CoT-Aware (bKau2NNrji), LTD (arXiv:2603.01639). Metrics: mean accepted tokens per step, acceptance rate, wall-clock speedup. The method modifies only draft training and adds no inference-time primitives, making it directly composable with SpecGuard, ConfSpec, SemanticSpec, and LTD.\",\n  \"resource_estimate\": {\n    \"conversion_note\": \"All estimates are in H100-hours. Conversion basis: H100 provides approximately 2× training throughput over A100 for typical LLM training workloads. H100 cloud rate: ~$3/h on competitive providers (Hyperstack, JarvisLabs). Target model throughout all phases is DeepSeek-R1-Distill-70B (dense 70B model, fits on 4–8 H100s), which is substantially cheaper to serve than MoE frontier models — all three modes are comfortably within the ≤200 H100-hour compute budget.\",\n    \"manual\": {\n      \"gpu_hours\": \"~150h H100 (equivalent to ~300h A100 / 2×)\",\n      \"gpu_utilization\": \"~35% effective — high idle from iterative debugging of the attention-sparsity segment-labeling pipeline, human analysis between training runs, and code rewrites across 4–6 experimental iterations\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$450 (150h × $3/h)\",\n      \"risk_note\": \"Phase 0 pilot (1K traces, χ² test on segment-type distributions) must be completed and pass label-quality gate (≤30% ambiguous segments) before committing the remaining ~148h to full training.\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~190h H100 (equivalent to ~380h A100 / 2×; within 200h H100 cap)\",\n      \"gpu_utilization\": \"~60% — agent queues ablations continuously across λ values and model sizes; human approval gates at key architectural forks cut wasted runs by ~40% vs. full auto\",\n      \"timeline\": \"5–7 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in for experiment approval and loss curve review\",\n      \"claude_api_cost\": \"$300–450 (~2,500–3,500 conversation turns at ~$0.10/turn average)\",\n      \"estimated_gpu_cost\": \"~$570 (190h × $3/h)\",\n      \"ablation_scope\": \"2 draft sizes (1.5B, 7B) × 3 λ values = 6 ablation runs + 2 EAGLE-3 baselines + 5-benchmark evaluation (AIME24, AMC23, LiveCodeBench, MT-Bench, HumanEval) against R1-Distill-70B; MT-Bench and HumanEval add ~4h H100 incremental eval cost; total remains within 190h H100 cap\",\n      \"risk_note\": \"Label quality is the critical bottleneck: if ThinKV's attention-sparsity heuristic assigns ambiguous structural labels to ≥30% of thought segments on the target model's traces, the auxiliary loss injects noise rather than signal and may degrade acceptance rate. Phase 0 pilot validation (days 1–2, ~2h H100) is a mandatory gate before committing full training budget.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~186h H100\",\n      \"gpu_utilization\": \"~88% — agent schedules experiment queues 24/7 across parallel nodes with negligible human-wait idle; idle periods are only inter-run checkpoint evaluation (~5–10 min)\",\n      \"timeline\": \"7–12 days with 4–6 H100 GPUs\",\n      \"team\": \"0 (only initial setup: segment-labeling pipeline using ThinKV's heuristic, EAGLE-3 training scaffold with auxiliary head, multi-benchmark evaluation harness against R1-Distill-70B)\",\n      \"claude_api_cost\": \"$600–900 (~5,000–7,500 conversation turns for experiment design, result analysis, and report drafting)\",\n      \"estimated_gpu_cost\": \"~$558 (186h × $3/h)\",\n      \"ablation_scope\": \"4 draft sizes (0.5B, 1.5B, 3B, 7B) × 3 λ values = 12 primary runs × ~13h H100/run ≈ 156h H100, plus 5-benchmark evaluation (AIME24, AMC23, LiveCodeBench, MT-Bench, HumanEval) ~30h H100 = 186h H100 total — within the ≤200h H100 cap\",\n      \"speed_bottleneck\": \"GPU node count is the primary limit — 4–6 H100s needed to parallelize draft training (4 GPUs) with concurrent multi-benchmark evaluation (2 GPUs); secondary bottleneck is Claude API rate limits during dense parallel ablation phases\",\n      \"risk_note\": \"Without sanity-check hooks, auto-exploration may collapse to degenerate structural predictions (e.g., all segments labeled R) that reduce auxiliary loss without improving acceptance rate. Pipeline must include per-run structural segment distribution entropy checks as an automated gate before committing to full evaluation. Phase 0 pilot (χ² test on segment-type distributions, ~2h H100) must complete and pass before main training runs are queued.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026 — confirmed open; auto-research mode is the only feasible path given 7–12 day timeline; Phase 0 pilot must complete within days 1–2 of the run)\",\n    \"ICLR 2027 (deadline expected ~October 2026, not yet announced — all three resource modes are feasible at this horizon)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Efficient Reasoning for LLMs through Speculative Chain-of-Thought (arXiv:2504.19095, Apr 2025)\",\n    \"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral, arXiv:2510.01290)\",\n    \"Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework (OpenReview bKau2NNrji)\",\n    \"Flatter Tokens are More Valuable for Speculative Draft Model Training (arXiv:2601.18902, Jan 2026)\",\n    \"Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning (arXiv:2603.01639, ICLR 2026 Poster)\",\n    \"A Theoretical Perspective for Speculative Decoding Algorithm (arXiv:2411.00841, NeurIPS 2024)\",\n    \"Arbitrage: Efficient Reasoning via Advantage-Aware Speculation (arXiv:2512.05033)\",\n    \"Beyond Tokens: Semantic-Aware Speculative Decoding for Efficient Inference by Probing Internal States (arXiv:2602.03708, Feb 2026)\",\n    \"Steering Pretrained Drafters during Speculative Decoding (arXiv:2511.09844, AAAI 2026)\",\n    \"When RL Meets Adaptive Speculative Training: A Unified Training-Serving System (arXiv:2602.06932, Feb 2026)\",\n    \"Training Domain Draft Models for Speculative Decoding: Best Practices and Insights (arXiv:2503.07807, SCOPE@ICLR 2025)\",\n    \"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance (arXiv:2602.05774, Feb 2026)\",\n    \"When Drafts Evolve: Speculative Decoding Meets Online Learning (arXiv:2603.12617, Mar 2026)\",\n    \"EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test (NeurIPS 2025)\",\n    \"From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning (arXiv:2604.15244, Apr 2026)\",\n    \"ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification (arXiv:2602.18447, Feb 2026)\"\n  ],\n  \"description\": \"Speculative decoding draft models for reasoning LLMs are trained solely on next-token prediction, ignoring the structural grammar of thinking traces (reasoning → execution → transition). While CoT-Aware draft training (OpenReview bKau2NNrji) has shown step-level process supervision improves acceptance rates (3.04–4.55× speedup), no prior work applies thought-segment-level structural labels (R/E/T) as training signals or imposes a Markov segment-transition consistency objective — mechanisms that penalize structural incoherence at the thought-segment granularity where structural coherence is determined. We propose augmenting an EAGLE-3-based draft with a lightweight two-output head that jointly predicts next token and thought-segment type (R/E/T from ThinKV's ICLR 2026 Oral taxonomy, operating at τ=128-step refresh intervals producing 100–300-token segment windows), plus a Markov segment-transition KL objective aligning predicted R→E→T segment progressions to target-model-accepted trace distributions — grounded in the Markov chain abstraction for speculative decoding established in arXiv:2411.00841 (NeurIPS 2024); all labels auto-generated from ThinKV's attention-sparsity heuristic, zero human annotation. The target model is DeepSeek-R1-Distill-70B throughout all phases. A mandatory Phase 0 pilot (χ² test comparing R/E/T segment-type distributions of EAGLE-3-accepted vs. rejected draft segments on 1K traces, ~2h H100) validates the structural misalignment hypothesis and gates label quality before committing training budget. The approach is orthogonal to and composable with LTD (arXiv:2603.01639, ICLR 2026 Poster), which achieves up to 36.4% speedup over EAGLE-3 via RL co-adaptive draft/verify policies without structural supervision — structural training supervision can enhance the draft quality that LTD's dynamic RL policy leverages. ARBITRAGE (arXiv:2512.05033) targets reasoning efficiency via routing-side advantage-aware speculation, also orthogonal and composable. Phase 3 evaluation covers five benchmarks: AIME24, AMC23, LiveCodeBench (reasoning quality), MT-Bench (general instruction-following — standard in EAGLE-3 evaluation tradition), and HumanEval (code generation — verifies structural supervision does not degrade non-reasoning capabilities). SFDD (arXiv:2601.18902) is complementary: flatness is a distributional property of target-model outputs, while structural role is a semantic property of reasoning trace content. GPU estimates are in H100-hours (manual ~150h, human-in-loop ~190h, auto-research ~186h), all within the ≤200h H100 cap. The novelty claim: first to apply thought-segment-level R/E/T structural labels and a Markov segment-transition probability objective as speculative decoding draft training signals for R1-class extended reasoning models. Primary target venue: EMNLP 2026 (ARR deadline May 25, 2026).\",\n  \"project_name\": \"struct_guided_draft_training\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL NOVELTY GAP: 'Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework' (OpenReview bKau2NNrji) uses CoT process-level structure for EAGLE draft training — directly contradicting the 'zero prior work' novelty claim. This paper must be cited and explicitly differentiated from. Specifically: the CoT-Aware paper uses step-level distillation + SurpriseRatio data selection, not token-level thought-type labels (R/E/T) or Markov transition objectives; the differentiation must be made explicit and the novelty re-grounded in the specific token-level structural labeling + transition consistency contribution, not the broader 'CoT-aware draft training' claim.\", \"HARD CONSTRAINT VIOLATION: Auto-research mode is estimated at 1,000h A100 ≈ 333–500 H100-hours, exceeding the ≤200 H100-hour compute budget. All three resource estimates are given in A100-hours rather than H100-hours as required by the user specifications. The proposal must convert estimates to H100-hours and bring all modes within the constraint.\", \"UNVALIDATED CORE HYPOTHESIS: The structural misalignment explanation ('draft produces structurally incoherent R→E→T sequences that target model rejects') is presented as established fact, but no preliminary measurement establishes that accepted vs. rejected draft tokens differ in structural role distribution. A 500-token pilot analysis comparing ThinKV-classified structural distributions of accepted vs. rejected draft tokens should be conducted before committing training budget — if distributions are indistinguishable, the method has no theoretical foundation.\", \"MISLABELED PRIOR WORK AUTHORITY: ThinKV is described as an arXiv paper but is in fact an ICLR 2026 Oral, significantly increasing its authority and the risk that reviewers will ask why the paper's key dependency is 'off-the-shelf' from a peer-reviewed paper in the same submission cycle. Additionally, ThinKV's attention-sparsity heuristic was designed for KV eviction, not training label generation — its oracle precision as a token-level structural classifier for draft training supervision has not been validated.\", \"INFLATED SCOT CLAIMS: The landscape states SCoT achieves '48–49% latency reduction on DeepSeek-R1-Distill-32B/70B' — but the actual paper (arXiv:2504.19095) reports 48–66% for 32B and 21–49% for 70B. The lower 70B bound (21%) is materially weaker than implied and should be accurately reported to avoid misleading reviewers.\", \"MISSING RELATED WORK: 'Beyond Tokens: Semantic-Aware Speculative Decoding for Efficient Inference by Probing Internal States' (SemanticSpec, arXiv:2602.03708) achieves 2.7× speedup on DeepSeek-R1-32B by using internal hidden states to assess semantic equivalence — a parallel approach to semantic/structural awareness in speculative decoding. While verification-side (not draft-training-side), it directly competes on the reasoning model speedup narrative and must be discussed.\"]\nFeedback: The core R/E/T label + Markov transition consistency idea is genuinely novel at the mechanism level, but three issues need fixing before submission. (1) Differentiate explicitly from the CoT-Aware paper (OpenReview bKau2NNrji): pivot the novelty claim from 'no prior work uses CoT structure for draft training' to 'first to apply token-level thought-type labels as a training signal and a Markov transition consistency objective specifically for extended reasoning traces on modern R1-class models' — this is accurate and defensible. (2) Convert all GPU estimates to H100-hours and redesign the auto-research mode to stay within 200 H100-hours (cap at ~4 draft sizes × 3 λ values = 12 runs at ~15 H100-hours each ≈ 180 H100-hours). (3) Add a 2-page pilot section measuring whether ThinKV-classified structural roles of EAGLE-3-accepted vs. rejected draft tokens actually differ (a χ² test on 1K traces would suffice) — if they do, this validates the hypothesis and makes the training objective well-motivated; if they do not, pivot to measuring structural role divergence between draft model predictions and target model outputs, which may reveal the misalignment more directly.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL (NEW): The core novelty claim — 'token-level thought-type labels' — is factually incorrect. ThinKV's attention-sparsity heuristic classifies tokens at the SEGMENT level: it refreshes every τ=128 steps and assigns a single R/E/T label to a block of 100–300 tokens (per the ThinKV HTML full paper, which explicitly states classification 'operates at the segment level'). All tokens in a ~128-token window receive the same structural label. The paper must accurately describe this as 'thought-segment-level structural supervision' and revise the novelty claim accordingly. This also affects the Markov transition objective: transitions are between segments (~100–300 tokens each), not between individual tokens — this is still a valid objective, but different from what is described.\", \"CRITICAL (NEW): Target model inconsistency across phases creates a feasibility hole. Phase 0 explicitly samples from DeepSeek-R1-Distill-70B; Phase 3 uses DeepSeek-V4-Pro as the target. DeepSeek-V4-Pro is a 1.6T MoE model requiring 8× H200 SXM nodes at ~$28–55/hr just for serving (per LMSYS Day-0 benchmarks published April 25 2026). EAGLE-3 draft training for V4-Pro requires running the full model to extract multi-layer features; this cost is not reflected in the 150–180 H100-hour estimates and likely cannot be run on H100s at all at full scale. Either: (a) use R1-Distill-70B as the target model throughout (fully feasible within 200 H100-hours), or (b) explicitly cost the V4-Pro inference budget separately and demonstrate the approach still fits within constraints.\", \"IMPORTANT: ThinKV's attention-sparsity heuristic was calibrated on DeepSeek-R1-Distill model attention patterns (which use standard dense transformer attention). DeepSeek-V4-Pro uses Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA), fundamentally different sparsity profiles. If Phase 3 uses V4-Pro, the paper must validate that ThinKV's heuristic (developed for R1-Distill attention) transfers to V4-Pro's attention architecture before committing to this combination.\", \"MINOR: 'Flatter Tokens are More Valuable for Speculative Draft Model Training' (arXiv:2601.18902, January 2026) is missing from related work. It proposes SFDD — flatness-based dataset distillation for draft model training — and directly addresses token-level heterogeneity in draft training. It is not a direct competitor (flatness ≠ structural role), but shares the conceptual framing of non-uniform token importance in draft training and should be cited to contextualize the contribution.\"]\nFeedback: Round 1 issues are properly resolved — the CoT-Aware differentiation is now accurate and defensible, H100 conversion is correct, Phase 0 pilot is a genuine contribution, SCoT numbers are fixed, and SemanticSpec is contextualized correctly. The core R/E/T + Markov transition combination remains novel. Three issues need fixing before round 3: (1) Reframe 'token-level' as 'thought-segment-level' throughout — ThinKV classifies 128-token windows, not individual tokens; be precise about this in the method description, novelty claim, and Phase 0 χ² test (which should compare segment-type distributions, not per-token distributions). The approach is still novel as segment-level structural supervision; just describe it accurately. (2) Resolve the target model split: the simplest fix is to make R1-Distill-70B the target model throughout all phases (it fits comfortably within 200 H100-hours, EAGLE-3 infrastructure already supports it, and ThinKV was validated on it). If V4-Pro is retained as the Phase 3 target, add an infrastructure cost section and a ThinKV portability validation step to Phase 0. (3) Add arXiv:2601.18902 ('Flatter Tokens') to related work with a one-paragraph comparison: both approaches address non-uniform token importance in draft training, but flatness is a distributional property while structural role is a semantic property; cite as complementary.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"IMPORTANT — MISSING RELATED WORK: 'Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning' (LTD, arXiv:2603.01639, ICLR 2026 Poster) is absent from the landscape. LTD achieves up to 36.4% speedup over EAGLE-3 via RL-based co-adaptive draft/verify policies and is directly competitive on the EAGLE-3-improvement narrative. EMNLP reviewers will know this paper. The proposal must add LTD to the landscape and explicitly differentiate: LTD optimizes throughput via RL without reasoning-structure signal, while the proposed method adds thought-segment-level structural supervision that is orthogonal to LTD's RL objective and composable with it.\", \"IMPORTANT — EVAL SUITE MISMATCH WITH USER HARD CONSTRAINTS: The user explicitly required evaluation on 'perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench.' The proposal only evaluates on AIME24, AMC23, LiveCodeBench — none of which appear in the required suite. Research confirms MT-Bench is standard in speculative decoding papers including EAGLE-3 itself, and HumanEval is commonly paired with LiveCodeBench. At minimum, MT-Bench and HumanEval must be added to Phase 3 evaluation. This is a hard constraint from the user specification, not a stylistic preference.\", \"MINOR — MISSING THEORETICAL CITATION: When introducing the Markov segment-transition consistency objective, the NeurIPS 2024 paper 'A Theoretical Perspective for Speculative Decoding Algorithm' (arXiv:2411.00841) should be cited. This paper establishes the Markov Chain abstraction for speculative decoding and proves optimality properties. Invoking 'Markov segment-transition' without referencing this foundational theoretical framing is an oversight reviewers familiar with the SD theory literature will notice.\", \"MINOR — MISSING ARBITRAGE: ARBITRAGE (arXiv:2512.05033) achieves ~2× latency reduction on mathematical reasoning benchmarks via step-level advantage-aware routing, directly targeting the same reasoning model efficiency goal. It should be mentioned briefly in the landscape as a routing-side approach (orthogonal to draft-training-side supervision) to complete the coverage of reasoning-specific SD work.\"]\nFeedback: All three critical round 2 issues are properly resolved: segment-level vs token-level is now accurate throughout, the target model is R1-Distill-70B across all phases, and SFDD is cited as complementary. The Phase 0 hypothesis gate with its fallback pivot is well-designed and constitutes a genuine methodological contribution. Three remaining fixes before submission: (1) Add LTD (arXiv:2603.01639, ICLR 2026) to the landscape section with a clear differentiation — LTD uses RL to adapt draft/verify policies without any reasoning-structure signal, while the proposed method uses thought-segment supervision that is static at inference and orthogonal to RL-based adaptation; position LTD as a potentially composable baseline rather than a competitor. (2) Add MT-Bench and HumanEval to Phase 3 experiments — these are required by the user's hard constraints and are standard in the EAGLE-3 evaluation tradition; the reasoning benchmarks (AIME24, AMC23, LiveCodeBench) are appropriate for quality but MT-Bench and HumanEval verify that structural training supervision does not degrade general instruction-following and code quality. (3) Cite arXiv:2411.00841 when introducing the Markov segment-transition objective to anchor the theoretical framing. ARBITRAGE (arXiv:2512.05033) should also be briefly noted in the landscape.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-09T18:52:15.276Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-09T18:52:15.276Z",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

## Round 1

61 recorded events

### User

_source line 3 · 2026-05-09T18:52:15.298Z_

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

## Idea under review (round 4/10)
{
  "title": "Structure-Guided Draft Training for Reasoning Speculative Decoding",
  "core_problem": "Speculative decoding draft models for reasoning LLMs are trained solely on next-token prediction, ignoring the structural grammar of thinking traces (reasoning → execution → transition). This misalignment causes drafts to generate locally plausible but structurally incoherent token sequences that the target model rejects, creating an acceptance-rate ceiling. While CoT-Aware draft training (OpenReview bKau2NNrji) has demonstrated that step-level process supervision improves draft alignment, no prior work applies thought-segment-level structural labels (R/E/T) as a training signal or imposes a Markov segment-transition consistency objective on structural sequence progressions — the mechanisms that would directly penalize structural incoherence at the thought-segment granularity where coherence is determined and where draft rejection most clearly correlates with structural mismatch.",
  "opportunity": "ThinKV (ICLR 2026 Oral, arXiv:2510.01290) provides a thought-type taxonomy (R: reasoning, E: execution, T: transition) with an attention-sparsity heuristic that classifies tokens at the thought-segment level: the heuristic refreshes every τ=128 steps and assigns a single R/E/T label to the current segment window, which typically spans 100–300 tokens. All tokens within a segment window share one structural label. Although this heuristic was designed for KV-cache eviction rather than training supervision, its transferability as thought-segment-level structural labels is plausible and can be validated cheaply: a χ² test comparing R/E/T segment-type distributions of EAGLE-3-accepted vs. rejected draft segments on 1,000 sampled traces costs under 2 H100-hours and serves as a mandatory hypothesis gate before committing training budget. If validated, adding a lightweight auxiliary head to the draft model that jointly predicts structural segment type and next token — plus a Markov segment-transition consistency objective aligning predicted R→E→T segment-progression distributions to target-model-accepted trace distributions — forces the draft to internalize thinking-trace grammar at the granularity of structural units. The novelty claim is narrow and defensible: this is the first work to apply thought-segment-level R/E/T structural labels and a Markov segment-transition probability objective as draft training signals for R1-class extended reasoning models. CoT-Aware uses step-level distillation and SurpriseRatio data selection (operating at the CoT step boundary, not at the thought-segment level with explicit R/E/T type supervision); VSD optimizes a sequence-level ELBO with no reasoning-structure signal; SFDD (arXiv:2601.18902) uses flatness as a distributional property for data selection, not semantic structural role; LTD (arXiv:2603.01639) optimizes throughput via RL co-adaptive policies with no structural supervision — none impose thought-segment-level structural role supervision with segment-transition consistency, leaving a specific, measurable, and mechanistically grounded gap. The auxiliary head adds approximately 5M parameters, is frozen at inference (zero latency overhead), and is composable with any EAGLE-style architecture, verification-side improvements, or RL-based dynamic adaptation methods such as LTD.",
  "landscape": "SCoT (Apr 2025, arXiv:2504.19095) achieves 48–66% latency reduction on DeepSeek-R1-Distill-32B and 21–49% on DeepSeek-R1-Distill-70B via thought-level drafting but uses a generic smaller model with no structural supervision. ARBITRAGE (arXiv:2512.05033) achieves ~2× latency reduction on mathematical reasoning benchmarks via advantage-aware routing — a lightweight router trained to predict when the target model will produce meaningfully better reasoning steps, selecting between draft and target model outputs at the step level; this is a routing-side approach orthogonal to draft-training-side structural supervision and composable with our method. CoT-Aware (OpenReview bKau2NNrji) is the closest prior work: it augments EAGLE-style draft training with process-level CoT distillation (step-level feature regression to reduce forward KL divergence at CoT step boundaries) and SurpriseRatio data selection to prevent catastrophic forgetting, reporting 3.04×–4.55× wall-clock speedups; crucially, it does NOT classify tokens or segments into structural roles (R/E/T), does NOT use a Markov segment-transition consistency objective, and operates at the reasoning-step granularity rather than at the thought-segment level defined by ThinKV's attention-sparsity heuristic — our two key differentiating mechanisms. 'Flatter Tokens are More Valuable for Speculative Draft Model Training' (arXiv:2601.18902, Jan 2026) proposes SFDD — flatness-based dataset distillation for draft training, selecting samples where the target model's predictive distribution is flatter (less confident), achieving over 2× training speedup using 50% of data. SFDD and our approach share the conceptual framing that training tokens are non-uniformly important, but flatness is a distributional property of the target model's output whereas structural role is a semantic property of the reasoning trace's content; the two are complementary and non-competing. 'Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning' (LTD, arXiv:2603.01639, ICLR 2026 Poster) achieves up to 36.4% speedup over EAGLE-3 by formulating speculative decoding as a reinforcement learning problem that trains co-adaptive draft and verify policies to directly optimize throughput across 5 LLMs and 4 tasks; LTD uses no reasoning-structure signal and treats draft/verify allocation as a dynamic policy rather than a static training objective. Our approach is orthogonal: thought-segment-level structural supervision modifies only draft training and is frozen at inference, making it directly composable with LTD's RL-based dynamic adaptation as a complementary enhancement to the draft model quality that LTD's RL policy leverages. 'Steering Pretrained Drafters' (Nov 2025, arXiv:2511.09844, AAAI 2026) shows a lightweight dynamic steering mechanism improves accepted tokens by up to 35% and throughput by 22%, confirming structural alignment is a bottleneck rather than draft capacity. Aurora (Feb 2026, arXiv:2602.06932) enables continuous on-policy RL-style draft adaptation but optimizes distribution matching, not reasoning-trace structural coherence. 'Training Domain Draft Models' (Mar 2025, arXiv:2503.07807) addresses distribution shift via knowledge distillation, not structural role mismatch. Variational Speculative Decoding (Feb 2026, arXiv:2602.05774) formulates draft training as variational inference over draft paths, achieving 9.6% speedup over EAGLE-3 on MT-Bench, HumanEval, and GSM8K — but uses no reasoning-structure signal and has not been evaluated on extended reasoning benchmarks (AIME24, AMC23, LiveCodeBench), leaving a direct comparison gap. OnlineSpec (Mar 2026, arXiv:2603.12617) proposes online preference-pair updates for draft model adaptation during reasoning — complementary to our static structural supervision approach. SemanticSpec (Feb 2026, arXiv:2602.03708) achieves 2.7× speedup on DeepSeek-R1-32B and 2.1× on QwQ-32B via verification-side semantic equivalence checking using internal hidden states — compelling parallel work on reasoning model speedup but strictly orthogonal (verification-side, not draft-training-side) and composable with our approach. SpecGuard (Apr 2026, arXiv:2604.15244) performs step-level verification using model-internal signals, and ConfSpec (Feb 2026, arXiv:2602.18447) uses confidence-gated cascaded verification — both verification-side and composable. ThinKV (ICLR 2026 Oral, arXiv:2510.01290) provides the R/E/T thought-type taxonomy via attention-sparsity heuristics operating at the segment level (τ=128 steps, 100–300 tokens per segment); this heuristic was designed for KV-cache eviction on DeepSeek-R1-Distill models and its precision as a thought-segment-level training-label generator must be validated empirically before full training commitment. No prior work combines thought-segment-level structural labels with a Markov segment-transition consistency objective as a speculative decoding draft training objective.",
  "approach": "Phase 0 — Hypothesis Validation (days 1–2, ~2h H100; results constitute a 2-page analysis section in the paper): Sample 1,000 DeepSeek-R1-Distill-70B traces with EAGLE-3-generated draft tokens and known acceptance outcomes. Apply ThinKV's attention-sparsity heuristic to classify each ~128-token draft window as R, E, or T (all tokens within a window share one structural label per ThinKV's segment-level design). First, validate label quality: compute per-segment structural entropy; if ≥30% of segments fall into an ambiguous bin (above a tunable entropy threshold), tune the threshold on this 1K sample before proceeding — this prevents noise injection from poor labels. Second, run a χ² test comparing the marginal R/E/T segment-type distributions of EAGLE-3-accepted vs. rejected draft segments. If p < 0.05, the structural misalignment hypothesis is confirmed at the segment level and the training objectives are well-motivated. If p ≥ 0.05, pivot the measurement to structural segment-type divergence between the draft model's predicted R/E/T distributions and the target model's actual output segment distributions — this alternative analysis may reveal systematic structural biases in draft-model outputs (e.g., over-production of R segments, under-production of T segments) that manifest independent of per-segment acceptance, providing equally strong motivation for the Markov segment-transition objective. Both outcomes yield publishable pilot findings.\n\nPhase 1 — Draft Model Augmentation: Augment an EAGLE-3-based draft with a lightweight two-output head inserted after the multi-layer feature fusion layer: one output predicts the next token (standard cross-entropy loss L_token), a second predicts the current thought-segment type (R/E/T, cross-entropy auxiliary loss L_role weighted by α). Auto-generate R/E/T segment labels by applying ThinKV's attention-sparsity heuristic (τ=128 steps) to DeepSeek-R1-Distill-70B reasoning traces; all tokens within each ~128-token window share the same segment label, and zero human annotation is required. The auxiliary head learns to classify each token's structural context at segment granularity — effectively predicting which thought-segment type the current position falls within.\n\nPhase 2 — Markov Segment-Transition Consistency Objective: Add a third loss term L_trans (weighted by λ): from each draft trajectory extract the predicted R→E→T segment-transition sequence (one transition label per ~128-token window), compute KL divergence between this predicted segment-transition distribution and the empirically estimated transition distribution of target-model-accepted traces, and penalize divergence. Transitions are between thought segments (~100–300 tokens each), not between individual tokens — the Markov chain operates at the segment level, making the objective robust to token-level noise. This Markov segment-transition consistency objective is grounded in the Markov chain abstraction for speculative decoding established in 'A Theoretical Perspective for Speculative Decoding Algorithm' (arXiv:2411.00841, NeurIPS 2024), which analyzes fundamental SD performance limits via total variation distances between draft and target model distributions. Total training loss: L = L_token + α · L_role + λ · L_trans. The auxiliary head (~5M parameters) is frozen at inference time — zero latency overhead.\n\nPhase 3 — Experiments: Target model: DeepSeek-R1-Distill-70B (consistent with Phase 0; ThinKV was validated on R1-Distill attention patterns, ensuring label-transfer compatibility throughout all phases). Draft model sizes 1.5B, 3B, 7B (and 0.5B in auto-research mode); λ ∈ {0.01, 0.1, 0.5}; α fixed at 0.1 after Phase 0 pilot tuning. Benchmarks: AIME24, AMC23, LiveCodeBench (reasoning quality and task diversity for R1-class models); MT-Bench (general instruction-following quality — standard in the EAGLE-3 evaluation tradition, verifies structural supervision does not degrade instruction-following); HumanEval (code generation quality — verifies structural supervision does not degrade non-reasoning capabilities). Baselines: EAGLE-3, VSD, SCoT, CoT-Aware (bKau2NNrji), LTD (arXiv:2603.01639). Metrics: mean accepted tokens per step, acceptance rate, wall-clock speedup. The method modifies only draft training and adds no inference-time primitives, making it directly composable with SpecGuard, ConfSpec, SemanticSpec, and LTD.",
  "resource_estimate": {
    "conversion_note": "All estimates are in H100-hours. Conversion basis: H100 provides approximately 2× training throughput over A100 for typical LLM training workloads. H100 cloud rate: ~$3/h on competitive providers (Hyperstack, JarvisLabs). Target model throughout all phases is DeepSeek-R1-Distill-70B (dense 70B model, fits on 4–8 H100s), which is substantially cheaper to serve than MoE frontier models — all three modes are comfortably within the ≤200 H100-hour compute budget.",
    "manual": {
      "gpu_hours": "~150h H100 (equivalent to ~300h A100 / 2×)",
      "gpu_utilization": "~35% effective — high idle from iterative debugging of the attention-sparsity segment-labeling pipeline, human analysis between training runs, and code rewrites across 4–6 experimental iterations",
      "timeline": "4–6 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$450 (150h × $3/h)",
      "risk_note": "Phase 0 pilot (1K traces, χ² test on segment-type distributions) must be completed and pass label-quality gate (≤30% ambiguous segments) before committing the remaining ~148h to full training."
    },
    "human_in_loop": {
      "gpu_hours": "~190h H100 (equivalent to ~380h A100 / 2×; within 200h H100 cap)",
      "gpu_utilization": "~60% — agent queues ablations continuously across λ values and model sizes; human approval gates at key architectural forks cut wasted runs by ~40% vs. full auto",
      "timeline": "5–7 weeks",
      "team": "1 researcher, ~30 min/day check-in for experiment approval and loss curve review",
      "claude_api_cost": "$300–450 (~2,500–3,500 conversation turns at ~$0.10/turn average)",
      "estimated_gpu_cost": "~$570 (190h × $3/h)",
      "ablation_scope": "2 draft sizes (1.5B, 7B) × 3 λ values = 6 ablation runs + 2 EAGLE-3 baselines + 5-benchmark evaluation (AIME24, AMC23, LiveCodeBench, MT-Bench, HumanEval) against R1-Distill-70B; MT-Bench and HumanEval add ~4h H100 incremental eval cost; total remains within 190h H100 cap",
      "risk_note": "Label quality is the critical bottleneck: if ThinKV's attention-sparsity heuristic assigns ambiguous structural labels to ≥30% of thought segments on the target model's traces, the auxiliary loss injects noise rather than signal and may degrade acceptance rate. Phase 0 pilot validation (days 1–2, ~2h H100) is a mandatory gate before committing full training budget."
    },
    "auto_research": {
      "gpu_hours": "~186h H100",
      "gpu_utilization": "~88% — agent schedules experiment queues 24/7 across parallel nodes with negligible human-wait idle; idle periods are only inter-run checkpoint evaluation (~5–10 min)",
      "timeline": "7–12 days with 4–6 H100 GPUs",
      "team": "0 (only initial setup: segment-labeling pipeline using ThinKV's heuristic, EAGLE-3 training scaffold with auxiliary head, multi-benchmark evaluation harness against R1-Distill-70B)",
      "claude_api_cost": "$600–900 (~5,000–7,500 conversation turns for experiment design, result analysis, and report drafting)",
      "estimated_gpu_cost": "~$558 (186h × $3/h)",
      "ablation_scope": "4 draft sizes (0.5B, 1.5B, 3B, 7B) × 3 λ values = 12 primary runs × ~13h H100/run ≈ 156h H100, plus 5-benchmark evaluation (AIME24, AMC23, LiveCodeBench, MT-Bench, HumanEval) ~30h H100 = 186h H100 total — within the ≤200h H100 cap",
      "speed_bottleneck": "GPU node count is the primary limit — 4–6 H100s needed to parallelize draft training (4 GPUs) with concurrent multi-benchmark evaluation (2 GPUs); secondary bottleneck is Claude API rate limits during dense parallel ablation phases",
      "risk_note": "Without sanity-check hooks, auto-exploration may collapse to degenerate structural predictions (e.g., all segments labeled R) that reduce auxiliary loss without improving acceptance rate. Pipeline must include per-run structural segment distribution entropy checks as an automated gate before committing to full evaluation. Phase 0 pilot (χ² test on segment-type distributions, ~2h H100) must complete and pass before main training runs are queued."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026 — confirmed open; auto-research mode is the only feasible path given 7–12 day timeline; Phase 0 pilot must complete within days 1–2 of the run)",
    "ICLR 2027 (deadline expected ~October 2026, not yet announced — all three resource modes are feasible at this horizon)"
  ],
  "level": "solid",
  "key_references": [
    "Efficient Reasoning for LLMs through Speculative Chain-of-Thought (arXiv:2504.19095, Apr 2025)",
    "ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral, arXiv:2510.01290)",
    "Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework (OpenReview bKau2NNrji)",
    "Flatter Tokens are More Valuable for Speculative Draft Model Training (arXiv:2601.18902, Jan 2026)",
    "Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning (arXiv:2603.01639, ICLR 2026 Poster)",
    "A Theoretical Perspective for Speculative Decoding Algorithm (arXiv:2411.00841, NeurIPS 2024)",
    "Arbitrage: Efficient Reasoning via Advantage-Aware Speculation (arXiv:2512.05033)",
    "Beyond Tokens: Semantic-Aware Speculative Decoding for Efficient Inference by Probing Internal States (arXiv:2602.03708, Feb 2026)",
    "Steering Pretrained Drafters during Speculative Decoding (arXiv:2511.09844, AAAI 2026)",
    "When RL Meets Adaptive Speculative Training: A Unified Training-Serving System (arXiv:2602.06932, Feb 2026)",
    "Training Domain Draft Models for Speculative Decoding: Best Practices and Insights (arXiv:2503.07807, SCOPE@ICLR 2025)",
    "Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance (arXiv:2602.05774, Feb 2026)",
    "When Drafts Evolve: Speculative Decoding Meets Online Learning (arXiv:2603.12617, Mar 2026)",
    "EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test (NeurIPS 2025)",
    "From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning (arXiv:2604.15244, Apr 2026)",
    "ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification (arXiv:2602.18447, Feb 2026)"
  ],
  "description": "Speculative decoding draft models for reasoning LLMs are trained solely on next-token prediction, ignoring the structural grammar of thinking traces (reasoning → execution → transition). While CoT-Aware draft training (OpenReview bKau2NNrji) has shown step-level process supervision improves acceptance rates (3.04–4.55× speedup), no prior work applies thought-segment-level structural labels (R/E/T) as training signals or imposes a Markov segment-transition consistency objective — mechanisms that penalize structural incoherence at the thought-segment granularity where structural coherence is determined. We propose augmenting an EAGLE-3-based draft with a lightweight two-output head that jointly predicts next token and thought-segment type (R/E/T from ThinKV's ICLR 2026 Oral taxonomy, operating at τ=128-step refresh intervals producing 100–300-token segment windows), plus a Markov segment-transition KL objective aligning predicted R→E→T segment progressions to target-model-accepted trace distributions — grounded in the Markov chain abstraction for speculative decoding established in arXiv:2411.00841 (NeurIPS 2024); all labels auto-generated from ThinKV's attention-sparsity heuristic, zero human annotation. The target model is DeepSeek-R1-Distill-70B throughout all phases. A mandatory Phase 0 pilot (χ² test comparing R/E/T segment-type distributions of EAGLE-3-accepted vs. rejected draft segments on 1K traces, ~2h H100) validates the structural misalignment hypothesis and gates label quality before committing training budget. The approach is orthogonal to and composable with LTD (arXiv:2603.01639, ICLR 2026 Poster), which achieves up to 36.4% speedup over EAGLE-3 via RL co-adaptive draft/verify policies without structural supervision — structural training supervision can enhance the draft quality that LTD's dynamic RL policy leverages. ARBITRAGE (arXiv:2512.05033) targets reasoning efficiency via routing-side advantage-aware speculation, also orthogonal and composable. Phase 3 evaluation covers five benchmarks: AIME24, AMC23, LiveCodeBench (reasoning quality), MT-Bench (general instruction-following — standard in EAGLE-3 evaluation tradition), and HumanEval (code generation — verifies structural supervision does not degrade non-reasoning capabilities). SFDD (arXiv:2601.18902) is complementary: flatness is a distributional property of target-model outputs, while structural role is a semantic property of reasoning trace content. GPU estimates are in H100-hours (manual ~150h, human-in-loop ~190h, auto-research ~186h), all within the ≤200h H100 cap. The novelty claim: first to apply thought-segment-level R/E/T structural labels and a Markov segment-transition probability objective as speculative decoding draft training signals for R1-class extended reasoning models. Primary target venue: EMNLP 2026 (ARR deadline May 25, 2026).",
  "project_name": "struct_guided_draft_training",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL NOVELTY GAP: 'Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework' (OpenReview bKau2NNrji) uses CoT process-level structure for EAGLE draft training — directly contradicting the 'zero prior work' novelty claim. This paper must be cited and explicitly differentiated from. Specifically: the CoT-Aware paper uses step-level distillation + SurpriseRatio data selection, not token-level thought-type labels (R/E/T) or Markov transition objectives; the differentiation must be made explicit and the novelty re-grounded in the specific token-level structural labeling + transition consistency contribution, not the broader 'CoT-aware draft training' claim.", "HARD CONSTRAINT VIOLATION: Auto-research mode is estimated at 1,000h A100 ≈ 333–500 H100-hours, exceeding the ≤200 H100-hour compute budget. All three resource estimates are given in A100-hours rather than H100-hours as required by the user specifications. The proposal must convert estimates to H100-hours and bring all modes within the constraint.", "UNVALIDATED CORE HYPOTHESIS: The structural misalignment explanation ('draft produces structurally incoherent R→E→T sequences that target model rejects') is presented as established fact, but no preliminary measurement establishes that accepted vs. rejected draft tokens differ in structural role distribution. A 500-token pilot analysis comparing ThinKV-classified structural distributions of accepted vs. rejected draft tokens should be conducted before committing training budget — if distributions are indistinguishable, the method has no theoretical foundation.", "MISLABELED PRIOR WORK AUTHORITY: ThinKV is described as an arXiv paper but is in fact an ICLR 2026 Oral, significantly increasing its authority and the risk that reviewers will ask why the paper's key dependency is 'off-the-shelf' from a peer-reviewed paper in the same submission cycle. Additionally, ThinKV's attention-sparsity heuristic was designed for KV eviction, not training label generation — its oracle precision as a token-level structural classifier for draft training supervision has not been validated.", "INFLATED SCOT CLAIMS: The landscape states SCoT achieves '48–49% latency reduction on DeepSeek-R1-Distill-32B/70B' — but the actual paper (arXiv:2504.19095) reports 48–66% for 32B and 21–49% for 70B. The lower 70B bound (21%) is materially weaker than implied and should be accurately reported to avoid misleading reviewers.", "MISSING RELATED WORK: 'Beyond Tokens: Semantic-Aware Speculative Decoding for Efficient Inference by Probing Internal States' (SemanticSpec, arXiv:2602.03708) achieves 2.7× speedup on DeepSeek-R1-32B by using internal hidden states to assess semantic equivalence — a parallel approach to semantic/structural awareness in speculative decoding. While verification-side (not draft-training-side), it directly competes on the reasoning model speedup narrative and must be discussed."]
Feedback: The core R/E/T label + Markov transition consistency idea is genuinely novel at the mechanism level, but three issues need fixing before submission. (1) Differentiate explicitly from the CoT-Aware paper (OpenReview bKau2NNrji): pivot the novelty claim from 'no prior work uses CoT structure for draft training' to 'first to apply token-level thought-type labels as a training signal and a Markov transition consistency objective specifically for extended reasoning traces on modern R1-class models' — this is accurate and defensible. (2) Convert all GPU estimates to H100-hours and redesign the auto-research mode to stay within 200 H100-hours (cap at ~4 draft sizes × 3 λ values = 12 runs at ~15 H100-hours each ≈ 180 H100-hours). (3) Add a 2-page pilot section measuring whether ThinKV-classified structural roles of EAGLE-3-accepted vs. rejected draft tokens actually differ (a χ² test on 1K traces would suffice) — if they do, this validates the hypothesis and makes the training objective well-motivated; if they do not, pivot to measuring structural role divergence between draft model predictions and target model outputs, which may reveal the misalignment more directly.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL (NEW): The core novelty claim — 'token-level thought-type labels' — is factually incorrect. ThinKV's attention-sparsity heuristic classifies tokens at the SEGMENT level: it refreshes every τ=128 steps and assigns a single R/E/T label to a block of 100–300 tokens (per the ThinKV HTML full paper, which explicitly states classification 'operates at the segment level'). All tokens in a ~128-token window receive the same structural label. The paper must accurately describe this as 'thought-segment-level structural supervision' and revise the novelty claim accordingly. This also affects the Markov transition objective: transitions are between segments (~100–300 tokens each), not between individual tokens — this is still a valid objective, but different from what is described.", "CRITICAL (NEW): Target model inconsistency across phases creates a feasibility hole. Phase 0 explicitly samples from DeepSeek-R1-Distill-70B; Phase 3 uses DeepSeek-V4-Pro as the target. DeepSeek-V4-Pro is a 1.6T MoE model requiring 8× H200 SXM nodes at ~$28–55/hr just for serving (per LMSYS Day-0 benchmarks published April 25 2026). EAGLE-3 draft training for V4-Pro requires running the full model to extract multi-layer features; this cost is not reflected in the 150–180 H100-hour estimates and likely cannot be run on H100s at all at full scale. Either: (a) use R1-Distill-70B as the target model throughout (fully feasible within 200 H100-hours), or (b) explicitly cost the V4-Pro inference budget separately and demonstrate the approach still fits within constraints.", "IMPORTANT: ThinKV's attention-sparsity heuristic was calibrated on DeepSeek-R1-Distill model attention patterns (which use standard dense transformer attention). DeepSeek-V4-Pro uses Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA), fundamentally different sparsity profiles. If Phase 3 uses V4-Pro, the paper must validate that ThinKV's heuristic (developed for R1-Distill attention) transfers to V4-Pro's attention architecture before committing to this combination.", "MINOR: 'Flatter Tokens are More Valuable for Speculative Draft Model Training' (arXiv:2601.18902, January 2026) is missing from related work. It proposes SFDD — flatness-based dataset distillation for draft model training — and directly addresses token-level heterogeneity in draft training. It is not a direct competitor (flatness ≠ structural role), but shares the conceptual framing of non-uniform token importance in draft training and should be cited to contextualize the contribution."]
Feedback: Round 1 issues are properly resolved — the CoT-Aware differentiation is now accurate and defensible, H100 conversion is correct, Phase 0 pilot is a genuine contribution, SCoT numbers are fixed, and SemanticSpec is contextualized correctly. The core R/E/T + Markov transition combination remains novel. Three issues need fixing before round 3: (1) Reframe 'token-level' as 'thought-segment-level' throughout — ThinKV classifies 128-token windows, not individual tokens; be precise about this in the method description, novelty claim, and Phase 0 χ² test (which should compare segment-type distributions, not per-token distributions). The approach is still novel as segment-level structural supervision; just describe it accurately. (2) Resolve the target model split: the simplest fix is to make R1-Distill-70B the target model throughout all phases (it fits comfortably within 200 H100-hours, EAGLE-3 infrastructure already supports it, and ThinKV was validated on it). If V4-Pro is retained as the Phase 3 target, add an infrastructure cost section and a ThinKV portability validation step to Phase 0. (3) Add arXiv:2601.18902 ('Flatter Tokens') to related work with a one-paragraph comparison: both approaches address non-uniform token importance in draft training, but flatness is a distributional property while structural role is a semantic property; cite as complementary.

### Round 3 review
Verdict: revise
Issues: ["IMPORTANT — MISSING RELATED WORK: 'Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning' (LTD, arXiv:2603.01639, ICLR 2026 Poster) is absent from the landscape. LTD achieves up to 36.4% speedup over EAGLE-3 via RL-based co-adaptive draft/verify policies and is directly competitive on the EAGLE-3-improvement narrative. EMNLP reviewers will know this paper. The proposal must add LTD to the landscape and explicitly differentiate: LTD optimizes throughput via RL without reasoning-structure signal, while the proposed method adds thought-segment-level structural supervision that is orthogonal to LTD's RL objective and composable with it.", "IMPORTANT — EVAL SUITE MISMATCH WITH USER HARD CONSTRAINTS: The user explicitly required evaluation on 'perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench.' The proposal only evaluates on AIME24, AMC23, LiveCodeBench — none of which appear in the required suite. Research confirms MT-Bench is standard in speculative decoding papers including EAGLE-3 itself, and HumanEval is commonly paired with LiveCodeBench. At minimum, MT-Bench and HumanEval must be added to Phase 3 evaluation. This is a hard constraint from the user specification, not a stylistic preference.", "MINOR — MISSING THEORETICAL CITATION: When introducing the Markov segment-transition consistency objective, the NeurIPS 2024 paper 'A Theoretical Perspective for Speculative Decoding Algorithm' (arXiv:2411.00841) should be cited. This paper establishes the Markov Chain abstraction for speculative decoding and proves optimality properties. Invoking 'Markov segment-transition' without referencing this foundational theoretical framing is an oversight reviewers familiar with the SD theory literature will notice.", "MINOR — MISSING ARBITRAGE: ARBITRAGE (arXiv:2512.05033) achieves ~2× latency reduction on mathematical reasoning benchmarks via step-level advantage-aware routing, directly targeting the same reasoning model efficiency goal. It should be mentioned briefly in the landscape as a routing-side approach (orthogonal to draft-training-side supervision) to complete the coverage of reasoning-specific SD work."]
Feedback: All three critical round 2 issues are properly resolved: segment-level vs token-level is now accurate throughout, the target model is R1-Distill-70B across all phases, and SFDD is cited as complementary. The Phase 0 hypothesis gate with its fallback pivot is well-designed and constitutes a genuine methodological contribution. Three remaining fixes before submission: (1) Add LTD (arXiv:2603.01639, ICLR 2026) to the landscape section with a clear differentiation — LTD uses RL to adapt draft/verify policies without any reasoning-structure signal, while the proposed method uses thought-segment supervision that is static at inference and orthogonal to RL-based adaptation; position LTD as a potentially composable baseline rather than a competitor. (2) Add MT-Bench and HumanEval to Phase 3 experiments — these are required by the user's hard constraints and are standard in the EAGLE-3 evaluation tradition; the reasoning benchmarks (AIME24, AMC23, LiveCodeBench) are appropriate for quality but MT-Bench and HumanEval verify that structural training supervision does not degrade general instruction-following and code quality. (3) Cite arXiv:2411.00841 when introducing the Markov segment-transition objective to anchor the theoretical framing. ARBITRAGE (arXiv:2512.05033) should also be briefly noted in the landscape.


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
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "1d19bca7-4667-40a8-a2b2-304c420836b7",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-09T18:52:15.296Z_

```json
{
  "parentUuid": "1d19bca7-4667-40a8-a2b2-304c420836b7",
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
  "uuid": "fd2f4c47-7afd-48b0-8b4f-c970ec69528b",
  "timestamp": "2026-05-09T18:52:15.296Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-09T18:52:15.296Z_

```json
{
  "parentUuid": "fd2f4c47-7afd-48b0-8b4f-c970ec69528b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9f87b59a-e419-468f-8772-9cc30a7725c6",
  "timestamp": "2026-05-09T18:52:15.296Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
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
  "leafUuid": "9f87b59a-e419-468f-8772-9cc30a7725c6",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-level structural supervision for reasoning speculative decoding",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Assistant

_source line 8 · 2026-05-09T18:52:31.396Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this round 4 submission. The idea has gone through 3 rounds of revision and the previous issues were:

Round 3 issues (that needed fixing):
1. Missing LTD (arXiv:2603.01639, ICLR 2026 Poster) from landscape
2. Eval suite mismatch - needed MT-Bench and HumanEval
3. Missing theoretical citation arXiv:2411.00841
4. Missing ARBITRAGE (arXiv:2512.05033)

Let me check the current submission to see if these are addressed:

1. LTD - Yes, it's now in the landscape: "Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning (LTD, arXiv:2603.01639, ICLR 2026 Poster)" and explicitly differentiated as orthogonal and composable.


2. MT-Bench and HumanEval - Yes, they've been added to Phase 3 with clear justifications for why they're included.
3. Theoretical citation arXiv:2411.00841 - Yes, added with proper grounding in the Markov chain abstraction for speculative decoding.
4. ARBITRAGE - Yes, added to the landscape.

All four issues from the previous round have been successfully addressed.

Now I need to independently verify the key claims in the paper. I'm checking whether ThinKV is actually an ICLR 2026 Oral, confirming EAGLE-3's NeurIPS 2025 status, verifying that CoT-Aware exists on OpenReview, and validating the LTD paper's claimed speedup metrics. I'm also searching for any concurrent work in speculative decoding for reasoning models and checking whether the resource estimates are realistic. Beyond the factual verification, I want to ensure the core structural misalignment hypothesis has empirical support and that the novelty claim remains defensible given any new work in the space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f87b59a-e419-468f-8772-9cc30a7725c6",
  "isSidechain": false,
  "requestId": "req_011CasVwAdueeKFsBL9AzopL",
  "type": "assistant",
  "uuid": "158609fd-3e6b-4ac8-b43b-fa2b0091b0a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PWur2LL4F6vZ74DYF4vGgb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18187,
      "cache_read_input_tokens": 11631,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 759,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18187
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

_source line 9 · 2026-05-09T18:52:31.398Z_

I'll conduct independent verification searches before issuing a verdict. Let me search across multiple dimensions simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "158609fd-3e6b-4ac8-b43b-fa2b0091b0a5",
  "isSidechain": false,
  "requestId": "req_011CasVwAdueeKFsBL9AzopL",
  "type": "assistant",
  "uuid": "e010107f-0e89-414f-93d0-6105a9325a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PWur2LL4F6vZ74DYF4vGgb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18187,
      "cache_read_input_tokens": 11631,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 759,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18187
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

_source line 10 · 2026-05-09T18:52:31.407Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Jxw9nS2EikNhaxyC11rngS`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e010107f-0e89-414f-93d0-6105a9325a2d",
  "isSidechain": false,
  "requestId": "req_011CasVwAdueeKFsBL9AzopL",
  "type": "assistant",
  "uuid": "01e28f7d-8009-4582-8505-e34fc8190489",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PWur2LL4F6vZ74DYF4vGgb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18187,
      "cache_read_input_tokens": 11631,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 759,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18187
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

_source line 11 · 2026-05-09T18:52:31.413Z_

<details><summary>↩ Tool result · `toolu_01Jxw9nS2EikNhaxyC11rngS`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "parentUuid": "01e28f7d-8009-4582-8505-e34fc8190489",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "703283e7-171a-496d-9f1d-6d071889988e",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "01e28f7d-8009-4582-8505-e34fc8190489",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-09T18:52:38.037Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct independent searches to verify the claims in this round 4 submission. I need to search for:

1. ThinKV ICLR 2026 status
2. EAGLE-3 NeurIPS 2025 status
3. CoT-Aware speculative decoding paper (OpenReview bKau2NNrji)
4. LTD (arXiv:2603.01639) - Learning to Draft
5. Any new concurrent work on structural supervision for speculative decoding
6. ARBITRAGE paper verification
7. SCoT paper (arXiv:2504.19095)


8. SemanticSpec paper verification
9. Check for any new work I might find

Let me run multiple searches in parallel to verify these claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "703283e7-171a-496d-9f1d-6d071889988e",
  "isSidechain": false,
  "requestId": "req_011CasVxMoebcCtiFpDz95mW",
  "type": "assistant",
  "uuid": "1f0e103e-f9f1-4c60-97a6-20eac34e8f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017suDLtE5x2sEGkPhY14Ws4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1778,
      "cache_read_input_tokens": 29818,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 373,
          "cache_read_input_tokens": 29818,
          "cache_creation_input_tokens": 1778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1778
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

_source line 13 · 2026-05-09T18:52:38.038Z_

Conducting independent verification across multiple dimensions simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f0e103e-f9f1-4c60-97a6-20eac34e8f23",
  "isSidechain": false,
  "requestId": "req_011CasVxMoebcCtiFpDz95mW",
  "type": "assistant",
  "uuid": "534fab64-55b6-4c8b-b5ca-c157b3f19964",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017suDLtE5x2sEGkPhY14Ws4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1778,
      "cache_read_input_tokens": 29818,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 373,
          "cache_read_input_tokens": 29818,
          "cache_creation_input_tokens": 1778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1778
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

_source line 14 · 2026-05-09T18:52:38.392Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A2hxR2xZ1hAjifZAAJTucw`</summary>

```json
{
  "query": "ThinKV ICLR 2026 oral thought-type KV cache reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "534fab64-55b6-4c8b-b5ca-c157b3f19964",
  "isSidechain": false,
  "requestId": "req_011CasVxMoebcCtiFpDz95mW",
  "type": "assistant",
  "uuid": "d5cfeb09-2b3a-4847-878b-260a86bd1a74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017suDLtE5x2sEGkPhY14Ws4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1778,
      "cache_read_input_tokens": 29818,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 373,
          "cache_read_input_tokens": 29818,
          "cache_creation_input_tokens": 1778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1778
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

_source line 15 · 2026-05-09T18:52:39.384Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WYmpaSNWqfECYvxoLjCedo`</summary>

```json
{
  "query": "EAGLE-3 speculative decoding NeurIPS 2025 scaling inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5cfeb09-2b3a-4847-878b-260a86bd1a74",
  "isSidechain": false,
  "requestId": "req_011CasVxMoebcCtiFpDz95mW",
  "type": "assistant",
  "uuid": "08413a68-d816-46bf-9199-94a8a866ec5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017suDLtE5x2sEGkPhY14Ws4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1778,
      "cache_read_input_tokens": 29818,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 373,
          "cache_read_input_tokens": 29818,
          "cache_creation_input_tokens": 1778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1778
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

_source line 16 · 2026-05-09T18:52:39.727Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A2aCLmibVAUqpFC1Mj6Scz`</summary>

```json
{
  "query": "speculative decoding structural supervision reasoning trace draft training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08413a68-d816-46bf-9199-94a8a866ec5b",
  "isSidechain": false,
  "requestId": "req_011CasVxMoebcCtiFpDz95mW",
  "type": "assistant",
  "uuid": "dfc532b4-3231-4cfb-a857-2421a75504e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017suDLtE5x2sEGkPhY14Ws4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1778,
      "cache_read_input_tokens": 29818,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 373,
          "cache_read_input_tokens": 29818,
          "cache_creation_input_tokens": 1778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1778
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

_source line 17 · 2026-05-09T18:52:44.174Z_

<details><summary>↩ Tool result · `toolu_01A2hxR2xZ1hAjifZAAJTucw`</summary>

```text
Web search results for query: "ThinKV ICLR 2026 oral thought-type KV cache reasoning"

Links: [{"title":"ICLR Oral ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://iclr.cc/virtual/2026/oral/10009981"},{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=M3CeHnZKNC"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"THINKV: THOUGHT-ADAPTIVE KV CACHE COM","url":"https://openreview.net/pdf/ccd30d4910657a86783762f96a0c303d5584f529.pdf"},{"title":"(PDF) ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://www.researchgate.net/publication/396142746_ThinKV_Thought-Adaptive_KV_Cache_Compression_for_Efficient_Reasoning_Models"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"KV Cache as a Reasoning Primitive for Long Context Reasoning | OpenReview","url":"https://openreview.net/forum?id=vs2qwVfU2C"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2510.01290"}]

Based on my search results, I found comprehensive information about ThinKV, which was presented as an oral paper at ICLR 2026. Here are the key findings:

## Overview

ThinKV is a thought-adaptive KV cache compression framework based on the observation that attention sparsity reveals distinct thought types with varying importance within the chain of thought (CoT).

## The Problem

The long-output context generation of large reasoning models enables extended chain of thought but also drives rapid growth of the key-value (KV) cache, quickly overwhelming GPU memory.

## Solution Approach

ThinKV applies a hybrid quantization–eviction strategy, assigning token precision by thought importance and progressively evicting tokens from less critical thoughts as reasoning trajectories evolve.

The framework includes several key components:
- Thought Decomposition showing the CoT in large reasoning models can be decomposed into distinct thought types, with their differentiation enabled by degree of sparsity in attention weights
- Think Before You Quantize (TBQ), a KV cache quantization scheme that assigns precision to tokens based on the importance of their associated thought type
- Think Before You Evict (TBE), a thought-adaptive eviction scheme that leverages inter-thought dynamics to progressively evict tokens

## Results

Extensive experiments on DeepSeek-R1-Distill, GPT-OSS, and NVIDIA AceReason across mathematics and coding benchmarks show that ThinKV achieves near-lossless accuracy with less than 5% of the original KV cache, while improving performance with up to 5.8x higher inference throughput over state-of-the-art baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5cfeb09-2b3a-4847-878b-260a86bd1a74",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "d37d4ef2-490f-4576-bf35-63dbb9dca8f0",
  "toolUseResult": {
    "query": "ThinKV ICLR 2026 oral thought-type KV cache reasoning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MX4FHY3W7mTU1RLjXCierQ",
        "content": [
          {
            "title": "ICLR Oral ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models",
            "url": "https://iclr.cc/virtual/2026/oral/10009981"
          },
          {
            "title": "[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models",
            "url": "https://arxiv.org/abs/2510.01290"
          },
          {
            "title": "ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | OpenReview",
            "url": "https://openreview.net/forum?id=M3CeHnZKNC"
          },
          {
            "title": "ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models",
            "url": "https://arxiv.org/html/2510.01290v1"
          },
          {
            "title": "ICLR 2026 Orals",
            "url": "https://iclr.cc/virtual/2026/events/oral"
          },
          {
            "title": "THINKV: THOUGHT-ADAPTIVE KV CACHE COM",
            "url": "https://openreview.net/pdf/ccd30d4910657a86783762f96a0c303d5584f529.pdf"
          },
          {
            "title": "(PDF) ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models",
            "url": "https://www.researchgate.net/publication/396142746_ThinKV_Thought-Adaptive_KV_Cache_Compression_for_Efficient_Reasoning_Models"
          },
          {
            "title": "Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview",
            "url": "https://openreview.net/forum?id=HGdg76iVo6"
          },
          {
            "title": "KV Cache as a Reasoning Primitive for Long Context Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=vs2qwVfU2C"
          },
          {
            "title": "ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2510.01290"
          }
        ]
      },
      "Based on my search results, I found comprehensive information about ThinKV, which was presented as an oral paper at ICLR 2026. Here are the key findings:\n\n## Overview\n\nThinKV is a thought-adaptive KV cache compression framework based on the observation that attention sparsity reveals distinct thought types with varying importance within the chain of thought (CoT).\n\n## The Problem\n\nThe long-output context generation of large reasoning models enables extended chain of thought but also drives rapid growth of the key-value (KV) cache, quickly overwhelming GPU memory.\n\n## Solution Approach\n\nThinKV applies a hybrid quantization–eviction strategy, assigning token precision by thought importance and progressively evicting tokens from less critical thoughts as reasoning trajectories evolve.\n\nThe framework includes several key components:\n- Thought Decomposition showing the CoT in large reasoning models can be decomposed into distinct thought types, with their differentiation enabled by degree of sparsity in attention weights\n- Think Before You Quantize (TBQ), a KV cache quantization scheme that assigns precision to tokens based on the importance of their associated thought type\n- Think Before You Evict (TBE), a thought-adaptive eviction scheme that leverages inter-thought dynamics to progressively evict tokens\n\n## Results\n\nExtensive experiments on DeepSeek-R1-Distill, GPT-OSS, and NVIDIA AceReason across mathematics and coding benchmarks show that ThinKV achieves near-lossless accuracy with less than 5% of the original KV cache, while improving performance with up to 5.8x higher inference throughput over state-of-the-art baselines."
    ],
    "durationSeconds": 5.776954817999998
  },
  "sourceToolAssistantUUID": "d5cfeb09-2b3a-4847-878b-260a86bd1a74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-09T18:52:48.131Z_

<details><summary>↩ Tool result · `toolu_01A2aCLmibVAUqpFC1Mj6Scz`</summary>

```text
Web search results for query: "speculative decoding structural supervision reasoning trace draft training 2025 2026"

Links: [{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=aL1Wnml9Ef"},{"title":"[2510.05421] Draft, Verify, and Improve: Toward Training-Aware Speculative Decoding","url":"https://arxiv.org/abs/2510.05421"},{"title":"When Drafts Evolve: Speculative Decoding Meets Online Learning","url":"https://arxiv.org/html/2603.12617"},{"title":"Draft, Verify, & Improve Toward Training-Aware Speculative Decoding","url":"https://arxiv.org/html/2510.05421v1"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning | OpenReview","url":"https://openreview.net/forum?id=JxxKj8pow1"},{"title":"Faster Speculative Decoding via Effective Draft ...","url":"https://aclanthology.org/2025.acl-long.486.pdf"},{"title":"ENTROPY-AWARE SPECULATIVE DECODING TOWARD ...","url":"https://openreview.net/pdf/8873a72aa9dd1126e677275974d787218c03b614.pdf"},{"title":"Decoding Speculative Decoding","url":"https://aclanthology.org/2025.naacl-long.328.pdf"},{"title":"Diving into speculative decoding training support for vLLM with Speculators v0.3.0 | vLLM Blog","url":"https://blog.vllm.ai/2025/12/13/speculators-v030.html"}]

I found several highly relevant recent papers and resources on speculative decoding research from 2025-2026. Here's a summary of the key findings:

## Recent Advances in Speculative Decoding (2025-2026)

**Variational Speculative Decoding (VSD)**

Variational Speculative Decoding (VSD) formulates draft training as variational inference over latent proposals (draft paths), maximizing the marginal probability of target-model acceptance with an ELBO that promotes high-quality latent proposals while minimizing divergence. The method has been evaluated across diverse LLMs including LLaMA-3.1-Instruct-8B, LLaMA-3.3-Instruct-70B, and DeepSeek-R1-Distill-LLaMA-8B.

**Training-Aware Speculative Decoding**

Draft, Verify, & Improve (DVI) is a training-aware self-speculative framework that combines inference with continual online learning, where an LLM is partitioned into a drafter and a verifier, and verifier accept/reject decisions are converted into supervision signals used to update the drafter head. On Spec-Bench, DVI achieves a 2.16× wall-time speedup, comparable to state-of-the-art approaches like EAGLE-2, while requiring orders of magnitude less training data.

**Online Learning Integration**

Online Speculative Decoding (OSD) tracks token positions where the draft model generates incorrect predictions and periodically updates the draft model by minimizing a distillation loss on these errors using target logits as supervision.

**Lookahead Reasoning**

Lookahead reasoning exploits a second, step-level layer of parallelism by recognizing that reasoning models generate step-by-step, and each step needs only to be semantically correct, not exact token matching.

**Train-Time Testing Methods**

Eagle3 (the current state-of-the-art for speculative decoding algorithms) uses draft models that take hidden states from three layers of the verifier model as input, capturing the verifier's latent features.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfc532b4-3231-4cfb-a857-2421a75504e7",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "580fcdca-bce8-49c5-a672-6e3f72f94335",
  "toolUseResult": {
    "query": "speculative decoding structural supervision reasoning trace draft training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HazpECb22fPidb8Ej4jXCG",
        "content": [
          {
            "title": "Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance",
            "url": "https://arxiv.org/html/2602.05774v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING",
            "url": "https://openreview.net/pdf?id=aL1Wnml9Ef"
          },
          {
            "title": "[2510.05421] Draft, Verify, and Improve: Toward Training-Aware Speculative Decoding",
            "url": "https://arxiv.org/abs/2510.05421"
          },
          {
            "title": "When Drafts Evolve: Speculative Decoding Meets Online Learning",
            "url": "https://arxiv.org/html/2603.12617"
          },
          {
            "title": "Draft, Verify, & Improve Toward Training-Aware Speculative Decoding",
            "url": "https://arxiv.org/html/2510.05421v1"
          },
          {
            "title": "Scaling Speculative Decoding with Lookahead Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=JxxKj8pow1"
          },
          {
            "title": "Faster Speculative Decoding via Effective Draft ...",
            "url": "https://aclanthology.org/2025.acl-long.486.pdf"
          },
          {
            "title": "ENTROPY-AWARE SPECULATIVE DECODING TOWARD ...",
            "url": "https://openreview.net/pdf/8873a72aa9dd1126e677275974d787218c03b614.pdf"
          },
          {
            "title": "Decoding Speculative Decoding",
            "url": "https://aclanthology.org/2025.naacl-long.328.pdf"
          },
          {
            "title": "Diving into speculative decoding training support for vLLM with Speculators v0.3.0 | vLLM Blog",
            "url": "https://blog.vllm.ai/2025/12/13/speculators-v030.html"
          }
        ]
      },
      "I found several highly relevant recent papers and resources on speculative decoding research from 2025-2026. Here's a summary of the key findings:\n\n## Recent Advances in Speculative Decoding (2025-2026)\n\n**Variational Speculative Decoding (VSD)**\n\nVariational Speculative Decoding (VSD) formulates draft training as variational inference over latent proposals (draft paths), maximizing the marginal probability of target-model acceptance with an ELBO that promotes high-quality latent proposals while minimizing divergence. The method has been evaluated across diverse LLMs including LLaMA-3.1-Instruct-8B, LLaMA-3.3-Instruct-70B, and DeepSeek-R1-Distill-LLaMA-8B.\n\n**Training-Aware Speculative Decoding**\n\nDraft, Verify, & Improve (DVI) is a training-aware self-speculative framework that combines inference with continual online learning, where an LLM is partitioned into a drafter and a verifier, and verifier accept/reject decisions are converted into supervision signals used to update the drafter head. On Spec-Bench, DVI achieves a 2.16× wall-time speedup, comparable to state-of-the-art approaches like EAGLE-2, while requiring orders of magnitude less training data.\n\n**Online Learning Integration**\n\nOnline Speculative Decoding (OSD) tracks token positions where the draft model generates incorrect predictions and periodically updates the draft model by minimizing a distillation loss on these errors using target logits as supervision.\n\n**Lookahead Reasoning**\n\nLookahead reasoning exploits a second, step-level layer of parallelism by recognizing that reasoning models generate step-by-step, and each step needs only to be semantically correct, not exact token matching.\n\n**Train-Time Testing Methods**\n\nEagle3 (the current state-of-the-art for speculative decoding algorithms) uses draft models that take hidden states from three layers of the verifier model as input, capturing the verifier's latent features."
    ],
    "durationSeconds": 8.401636531
  },
  "sourceToolAssistantUUID": "dfc532b4-3231-4cfb-a857-2421a75504e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-09T18:52:49.467Z_

<details><summary>↩ Tool result · `toolu_01WYmpaSNWqfECYvxoLjCedo`</summary>

```text
Web search results for query: "EAGLE-3 speculative decoding NeurIPS 2025 scaling inference"

Links: [{"title":"GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub","url":"https://github.com/SafeAILab/EAGLE"},{"title":"EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test | OpenReview","url":"https://openreview.net/forum?id=4exx1hUffq"},{"title":"Speculative Decoding in Practice: How EAGLE3 Makes LLMs Faster Without Changing Their Outputs","url":"https://huggingface.co/blog/lujangusface/tw-eagle3-gpu"},{"title":"[2503.01840] EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test","url":"https://arxiv.org/abs/2503.01840"},{"title":"NeurIPS Poster EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119930"},{"title":"EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test","url":"https://arxiv.org/html/2503.01840v1"},{"title":"EAGLE-3: Scaling up Inference Acceleration of Large ...","url":"https://openreview.net/pdf?id=4exx1hUffq"},{"title":"EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/eagle-3-scaling-up-inference-acceleration-of-large-language-models-via-training-time-test/"},{"title":"EAGLE-3 Speculative Decoding: 2-6x Faster LLM Inference Guide | E2E Networks","url":"https://www.e2enetworks.com/blog/Accelerating_LLM_Inference_with_EAGLE"},{"title":"Paper page - EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test","url":"https://huggingface.co/papers/2503.01840"}]

Based on the search results, here's what I found about EAGLE-3:

## Overview

EAGLE-3 abandons feature prediction in favor of direct token prediction and replaces reliance on top-layer features with multi-layer feature fusion via a technique named training-time test. The paper is titled "EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test" and was presented at NeurIPS 2025.

## Key Problem It Addresses

Scaling up data provides limited improvements for EAGLE, with this limitation arising from EAGLE's feature prediction constraints.

## Technical Improvements

EAGLE3 fuses representations from three points in the target model simultaneously: Early layers encode syntax, morphology, and local token context; Middle layers encode semantic relationships and broader discourse structure; and Late layers encode the output probability distribution directly. EAGLE3 also switches from feature-level prediction to direct token prediction, removing a scaling ceiling that had limited EAGLE1 and EAGLE2 as training data increased.

## Performance Results

The EAGLE3 paper reports 4.1–6.5× speedup at temperature 0 on academic benchmarks (Vicuna 13B, Llama-3.1-8B, Llama-3.3-70B). EAGLE-3 discovers a scaling law for speculative decoding: increasing training data leads to proportional improvements in speedup, which was not observed in the original EAGLE architecture.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08413a68-d816-46bf-9199-94a8a866ec5b",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "98154f5b-a4b2-44b6-9dd2-3b6395fddfb3",
  "toolUseResult": {
    "query": "EAGLE-3 speculative decoding NeurIPS 2025 scaling inference",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Upw52o5f1w19ifyNYDGAfe",
        "content": [
          {
            "title": "GitHub - SafeAILab/EAGLE: Official Implementation of EAGLE-1 (ICML'24), EAGLE-2 (EMNLP'24), and EAGLE-3 (NeurIPS'25). · GitHub",
            "url": "https://github.com/SafeAILab/EAGLE"
          },
          {
            "title": "EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test | OpenReview",
            "url": "https://openreview.net/forum?id=4exx1hUffq"
          },
          {
            "title": "Speculative Decoding in Practice: How EAGLE3 Makes LLMs Faster Without Changing Their Outputs",
            "url": "https://huggingface.co/blog/lujangusface/tw-eagle3-gpu"
          },
          {
            "title": "[2503.01840] EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test",
            "url": "https://arxiv.org/abs/2503.01840"
          },
          {
            "title": "NeurIPS Poster EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/119930"
          },
          {
            "title": "EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test",
            "url": "https://arxiv.org/html/2503.01840v1"
          },
          {
            "title": "EAGLE-3: Scaling up Inference Acceleration of Large ...",
            "url": "https://openreview.net/pdf?id=4exx1hUffq"
          },
          {
            "title": "EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test - Microsoft Research",
            "url": "https://www.microsoft.com/en-us/research/publication/eagle-3-scaling-up-inference-acceleration-of-large-language-models-via-training-time-test/"
          },
          {
            "title": "EAGLE-3 Speculative Decoding: 2-6x Faster LLM Inference Guide | E2E Networks",
            "url": "https://www.e2enetworks.com/blog/Accelerating_LLM_Inference_with_EAGLE"
          },
          {
            "title": "Paper page - EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test",
            "url": "https://huggingface.co/papers/2503.01840"
          }
        ]
      },
      "Based on the search results, here's what I found about EAGLE-3:\n\n## Overview\n\nEAGLE-3 abandons feature prediction in favor of direct token prediction and replaces reliance on top-layer features with multi-layer feature fusion via a technique named training-time test. The paper is titled \"EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test\" and was presented at NeurIPS 2025.\n\n## Key Problem It Addresses\n\nScaling up data provides limited improvements for EAGLE, with this limitation arising from EAGLE's feature prediction constraints.\n\n## Technical Improvements\n\nEAGLE3 fuses representations from three points in the target model simultaneously: Early layers encode syntax, morphology, and local token context; Middle layers encode semantic relationships and broader discourse structure; and Late layers encode the output probability distribution directly. EAGLE3 also switches from feature-level prediction to direct token prediction, removing a scaling ceiling that had limited EAGLE1 and EAGLE2 as training data increased.\n\n## Performance Results\n\nThe EAGLE3 paper reports 4.1–6.5× speedup at temperature 0 on academic benchmarks (Vicuna 13B, Llama-3.1-8B, Llama-3.3-70B). EAGLE-3 discovers a scaling law for speculative decoding: increasing training data leads to proportional improvements in speedup, which was not observed in the original EAGLE architecture."
    ],
    "durationSeconds": 10.078743591999999
  },
  "sourceToolAssistantUUID": "08413a68-d816-46bf-9199-94a8a866ec5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "98154f5b-a4b2-44b6-9dd2-3b6395fddfb3",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-level structural supervision for reasoning speculative decoding",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Assistant

_source line 22 · 2026-05-09T18:52:53.679Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me check for:
1. Entropy-aware speculative decoding - this might be relevant and competitive
2. The CoT-Aware paper (OpenReview bKau2NNrji)
3. Learning to Draft (LTD) paper - let me verify
4. Any work specifically targeting R/E/T structural labels or thought-segment supervision

Let me do more targeted searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98154f5b-a4b2-44b6-9dd2-3b6395fddfb3",
  "isSidechain": false,
  "requestId": "req_011CasVygcGiCohgn4SUk5R8",
  "type": "assistant",
  "uuid": "50f46a16-6fe2-4f39-9fe8-6c397cf2ab3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QDjAH7f5erUzbb8pVhXU7Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1038,
      "cache_creation_input_tokens": 2310,
      "cache_read_input_tokens": 31596,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2310,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1038,
          "output_tokens": 299,
          "cache_read_input_tokens": 31596,
          "cache_creation_input_tokens": 2310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2310
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

_source line 23 · 2026-05-09T18:52:54.382Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015eACp7BV2eszWZipVRrUo3`</summary>

```json
{
  "query": "CoT-Aware speculative decoding draft training EAGLE step-level distillation openreview 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50f46a16-6fe2-4f39-9fe8-6c397cf2ab3f",
  "isSidechain": false,
  "requestId": "req_011CasVygcGiCohgn4SUk5R8",
  "type": "assistant",
  "uuid": "ee594fcb-a796-4cc8-9b12-fdcd95fea3b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QDjAH7f5erUzbb8pVhXU7Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1038,
      "cache_creation_input_tokens": 2310,
      "cache_read_input_tokens": 31596,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2310,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1038,
          "output_tokens": 299,
          "cache_read_input_tokens": 31596,
          "cache_creation_input_tokens": 2310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2310
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

_source line 24 · 2026-05-09T18:52:55.339Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Rrj8MtVmNCk2t9j4fn8dS`</summary>

```json
{
  "query": "arXiv 2603.01639 Learning to Draft adaptive speculative decoding reinforcement learning ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee594fcb-a796-4cc8-9b12-fdcd95fea3b5",
  "isSidechain": false,
  "requestId": "req_011CasVygcGiCohgn4SUk5R8",
  "type": "assistant",
  "uuid": "a656005f-3378-46b5-b070-6c601accf150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QDjAH7f5erUzbb8pVhXU7Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1038,
      "cache_creation_input_tokens": 2310,
      "cache_read_input_tokens": 31596,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2310,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1038,
          "output_tokens": 299,
          "cache_read_input_tokens": 31596,
          "cache_creation_input_tokens": 2310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2310
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

_source line 25 · 2026-05-09T18:52:55.642Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JNX4DC46H5KcAraQbRpKZm`</summary>

```json
{
  "query": "thought segment structural label speculative decoding reasoning draft model training R E T 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a656005f-3378-46b5-b070-6c601accf150",
  "isSidechain": false,
  "requestId": "req_011CasVygcGiCohgn4SUk5R8",
  "type": "assistant",
  "uuid": "96426a1f-b4e8-4a59-9e29-ad25cadbc7e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QDjAH7f5erUzbb8pVhXU7Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1038,
      "cache_creation_input_tokens": 2310,
      "cache_read_input_tokens": 31596,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2310,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1038,
          "output_tokens": 299,
          "cache_read_input_tokens": 31596,
          "cache_creation_input_tokens": 2310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2310
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

_source line 26 · 2026-05-09T18:53:00.982Z_

<details><summary>↩ Tool result · `toolu_015eACp7BV2eszWZipVRrUo3`</summary>

```text
Web search results for query: "CoT-Aware speculative decoding draft training EAGLE step-level distillation openreview 2025"

Links: [{"title":"Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework | OpenReview","url":"https://openreview.net/forum?id=bKau2NNrji"},{"title":"ALIGNING DRAFT AND TARGET IN SPECULATIVE DE- CODING","url":"https://openreview.net/pdf?id=bKau2NNrji"},{"title":"DISTILLSPEC: IMPROVING SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=rsY6J3ZaTF"},{"title":"Draft, Verify, \\& Improve: Toward Training-Aware Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=CwvY6TXLxr"},{"title":"Position Specialist Generates Better Draft for Speculative ...","url":"https://arxiv.org/pdf/2506.03566"},{"title":"AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders","url":"https://openreview.net/pdf?id=zNLlglSOwD"},{"title":"SpecForge: Accelerating Speculative Decoding Training for SGLang - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2025-07-25-spec-forge/"},{"title":"DistillSpec: Improving Speculative Decoding via Knowledge Distillation | OpenReview","url":"https://openreview.net/forum?id=rsY6J3ZaTF"},{"title":"Online Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=Km3Kprwyua"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/56d5c6f1a93a7b0590cb4e1c32762d84e42428ae.pdf"}]

I found a highly relevant paper matching your query! Here are the key results:

## Primary Result

The main paper is titled "Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework." It addresses how chain-of-thought (CoT) prompting enhances the reasoning of large language models but increases autoregressive latency, and how speculative decoding mitigates this via a small-drafter–large-verifier pipeline. The paper proposes a CoT-aware mixed training framework that raises acceptance without altering decoding hyperparameters by combining process-level CoT distillation with feature regression to reduce forward KL divergence and improve step-wise acceptance, and SurpriseRatio (SR), a data-selection metric that anchors the distribution and prevents forgetting.

## Key Results

The experiments on two target models show wall-clock speedups of 3.04×–4.55×.

## Paper Details

- **Source:** OpenReview (Published October 8, 2025)
- **OpenReview Forum ID:** bKau2NNrji
- **Direct Links:**
  - Forum: https://openreview.net/forum?id=bKau2NNrji
  - PDF: https://openreview.net/pdf?id=bKau2NNrji

This paper directly addresses your query about CoT-aware speculative decoding with step-level distillation, EAGLE framework improvements, and draft training strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee594fcb-a796-4cc8-9b12-fdcd95fea3b5",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "17bfb9da-6f4b-4c5d-b705-d17bf7d9f43b",
  "toolUseResult": {
    "query": "CoT-Aware speculative decoding draft training EAGLE step-level distillation openreview 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TsBN6R5V4cAziAN8eJ1wuh",
        "content": [
          {
            "title": "Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework | OpenReview",
            "url": "https://openreview.net/forum?id=bKau2NNrji"
          },
          {
            "title": "ALIGNING DRAFT AND TARGET IN SPECULATIVE DE- CODING",
            "url": "https://openreview.net/pdf?id=bKau2NNrji"
          },
          {
            "title": "DISTILLSPEC: IMPROVING SPECULATIVE DECODING",
            "url": "https://openreview.net/pdf?id=rsY6J3ZaTF"
          },
          {
            "title": "Draft, Verify, \\& Improve: Toward Training-Aware Speculative Decoding | OpenReview",
            "url": "https://openreview.net/forum?id=CwvY6TXLxr"
          },
          {
            "title": "Position Specialist Generates Better Draft for Speculative ...",
            "url": "https://arxiv.org/pdf/2506.03566"
          },
          {
            "title": "AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders",
            "url": "https://openreview.net/pdf?id=zNLlglSOwD"
          },
          {
            "title": "SpecForge: Accelerating Speculative Decoding Training for SGLang - LMSYS Blog | LMSYS Org",
            "url": "https://www.lmsys.org/blog/2025-07-25-spec-forge/"
          },
          {
            "title": "DistillSpec: Improving Speculative Decoding via Knowledge Distillation | OpenReview",
            "url": "https://openreview.net/forum?id=rsY6J3ZaTF"
          },
          {
            "title": "Online Speculative Decoding | OpenReview",
            "url": "https://openreview.net/forum?id=Km3Kprwyua"
          },
          {
            "title": "000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019",
            "url": "https://openreview.net/pdf/56d5c6f1a93a7b0590cb4e1c32762d84e42428ae.pdf"
          }
        ]
      },
      "I found a highly relevant paper matching your query! Here are the key results:\n\n## Primary Result\n\nThe main paper is titled \"Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework.\" It addresses how chain-of-thought (CoT) prompting enhances the reasoning of large language models but increases autoregressive latency, and how speculative decoding mitigates this via a small-drafter–large-verifier pipeline. The paper proposes a CoT-aware mixed training framework that raises acceptance without altering decoding hyperparameters by combining process-level CoT distillation with feature regression to reduce forward KL divergence and improve step-wise acceptance, and SurpriseRatio (SR), a data-selection metric that anchors the distribution and prevents forgetting.\n\n## Key Results\n\nThe experiments on two target models show wall-clock speedups of 3.04×–4.55×.\n\n## Paper Details\n\n- **Source:** OpenReview (Published October 8, 2025)\n- **OpenReview Forum ID:** bKau2NNrji\n- **Direct Links:**\n  - Forum: https://openreview.net/forum?id=bKau2NNrji\n  - PDF: https://openreview.net/pdf?id=bKau2NNrji\n\nThis paper directly addresses your query about CoT-aware speculative decoding with step-level distillation, EAGLE framework improvements, and draft training strategies."
    ],
    "durationSeconds": 6.595261493000005
  },
  "sourceToolAssistantUUID": "ee594fcb-a796-4cc8-9b12-fdcd95fea3b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-09T18:53:01.961Z_

<details><summary>↩ Tool result · `toolu_018Rrj8MtVmNCk2t9j4fn8dS`</summary>

```text
Web search results for query: "arXiv 2603.01639 Learning to Draft adaptive speculative decoding reinforcement learning ICLR 2026"

Links: [{"title":"[2603.01639] Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning","url":"https://arxiv.org/abs/2603.01639"},{"title":"Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning","url":"https://arxiv.org/html/2603.01639"},{"title":"Adaptive Speculative Decoding with Reinforcement Learning","url":"https://arxiv.org/pdf/2603.01639"},{"title":"Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.01639v1"},{"title":"Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=IK9cbzzXLt"},{"title":"OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure","url":"https://arxiv.org/html/2406.17276"},{"title":"PEARL: Parallel Speculative Decoding with Adaptive Draft Length","url":"https://arxiv.org/html/2408.11850"},{"title":"SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection","url":"https://arxiv.org/html/2605.02888"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"Speculative Verification: Exploiting Information Gain to Refine Speculative Decoding","url":"https://arxiv.org/html/2509.24328v1"}]

I found the paper you're looking for! Here's what I found:

**Paper Details:**

The paper "Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning" is arXiv paper 2603.01639, submitted on March 2, 2026, by Jiebin Zhang, Zhenghan Yu, Liang Wang, Nan Yang, Eugene J. Yu, Zheng Li, Yifan Song, Dawei Zhu, Xingxing Zhang, Furu Wei, and Sujian Li. It was published as a conference paper at ICLR 2026.

**Paper Overview:**

Speculative decoding accelerates large language model (LLM) inference by using a small draft model to generate candidate tokens for a larger target model to verify, with efficacy depending on the trade-off between the time spent on drafting candidates and verifying them.

Current state-of-the-art methods rely on a static time allocation, while recent dynamic approaches optimize for proxy metrics like acceptance length, often neglecting the true time cost and treating the drafting and verification phases in isolation.

To address these limitations, the authors introduce Learning to Draft (LTD), a novel method that directly optimizes for throughput of each draft-and-verify cycle.

The paper is available on arXiv at https://arxiv.org/abs/2603.01639 and also on OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a656005f-3378-46b5-b070-6c601accf150",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "c6170f65-9555-4084-a84f-c66cd5cfdbc3",
  "toolUseResult": {
    "query": "arXiv 2603.01639 Learning to Draft adaptive speculative decoding reinforcement learning ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011g2oqQYCnt3Y3c6cJ3rPzh",
        "content": [
          {
            "title": "[2603.01639] Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning",
            "url": "https://arxiv.org/abs/2603.01639"
          },
          {
            "title": "Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning",
            "url": "https://arxiv.org/html/2603.01639"
          },
          {
            "title": "Adaptive Speculative Decoding with Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2603.01639"
          },
          {
            "title": "Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2603.01639v1"
          },
          {
            "title": "Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=IK9cbzzXLt"
          },
          {
            "title": "OPT-Tree: Speculative Decoding with Adaptive Draft Tree Structure",
            "url": "https://arxiv.org/html/2406.17276"
          },
          {
            "title": "PEARL: Parallel Speculative Decoding with Adaptive Draft Length",
            "url": "https://arxiv.org/html/2408.11850"
          },
          {
            "title": "SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection",
            "url": "https://arxiv.org/html/2605.02888"
          },
          {
            "title": "GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️",
            "url": "https://github.com/hemingkx/SpeculativeDecodingPapers"
          },
          {
            "title": "Speculative Verification: Exploiting Information Gain to Refine Speculative Decoding",
            "url": "https://arxiv.org/html/2509.24328v1"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\n**Paper Details:**\n\nThe paper \"Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning\" is arXiv paper 2603.01639, submitted on March 2, 2026, by Jiebin Zhang, Zhenghan Yu, Liang Wang, Nan Yang, Eugene J. Yu, Zheng Li, Yifan Song, Dawei Zhu, Xingxing Zhang, Furu Wei, and Sujian Li. It was published as a conference paper at ICLR 2026.\n\n**Paper Overview:**\n\nSpeculative decoding accelerates large language model (LLM) inference by using a small draft model to generate candidate tokens for a larger target model to verify, with efficacy depending on the trade-off between the time spent on drafting candidates and verifying them.\n\nCurrent state-of-the-art methods rely on a static time allocation, while recent dynamic approaches optimize for proxy metrics like acceptance length, often neglecting the true time cost and treating the drafting and verification phases in isolation.\n\nTo address these limitations, the authors introduce Learning to Draft (LTD), a novel method that directly optimizes for throughput of each draft-and-verify cycle.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2603.01639 and also on OpenReview."
    ],
    "durationSeconds": 6.617038342
  },
  "sourceToolAssistantUUID": "a656005f-3378-46b5-b070-6c601accf150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-09T18:53:02.922Z_

<details><summary>↩ Tool result · `toolu_01JNX4DC46H5KcAraQbRpKZm`</summary>

```text
Web search results for query: "thought segment structural label speculative decoding reasoning draft model training R E T 2025 2026"

Links: [{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning | OpenReview","url":"https://openreview.net/forum?id=JxxKj8pow1"},{"title":"JUDGE DECODING: FASTER SPECULATIVE SAMPLING ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/656d6174fd5ffb01c843f269649ab5cb-Paper-Conference.pdf"},{"title":"Efficient Reasoning for LLMs through Speculative Chain-of-Thought","url":"https://arxiv.org/html/2504.19095v2"},{"title":"Faster Speculative Decoding via Effective Draft ...","url":"https://aclanthology.org/2025.acl-long.486.pdf"},{"title":"ENTROPY-AWARE SPECULATIVE DECODING TOWARD ...","url":"https://openreview.net/pdf/8873a72aa9dd1126e677275974d787218c03b614.pdf"},{"title":"A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling","url":"https://www.arxiv.org/pdf/2509.04474"},{"title":"When Drafts Evolve: Speculative Decoding Meets Online Learning","url":"https://arxiv.org/html/2603.12617"},{"title":"Reward-Guided Speculative Decoding for Efficient LLM ...","url":"https://arxiv.org/pdf/2501.19324"},{"title":"PARALLEL SPECULATIVE DECODING WITH ADAPTIVE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/03b1043052700b1a471996b0baf309d4-Paper-Conference.pdf"}]

Based on the search results, I found relevant research on speculative decoding and reasoning models from 2025-2026. Here are the key findings:

## Recent Advances in Speculative Decoding for Reasoning

Reasoning models excel by generating long chain-of-thoughts, but decoding the resulting thousands of tokens is slow. Several new approaches have emerged to address this:

**Lookahead Reasoning with Step-Level Parallelism:**
Lookahead reasoning exploits a second, step-level layer of parallelism, with the key insight that reasoning models generate step-by-step, and each step needs only to be semantically correct, not exact token matching. A lightweight draft model proposes several future steps; the target model expands each proposal in one batched pass, and a verifier keeps semantically correct steps.

**Speculative Chain-of-Thought (SCoT):**
SCoT applies a lightweight draft model to generate multiple CoT drafts in parallel. The draft model is fine-tuned with LoRA modules to align the thinking behavior of the target model. Speculative Chain-of-Thought demonstrates a speed-up ratio of up to 2.92× for the reasoning process while achieving near-target-model-level accuracy on 5 datasets of different difficulties.

**Reward-Guided Speculative Decoding (RSD):**
Unlike traditional speculative decoding, which strictly enforces unbiasedness, RSD leverages reward signals to adaptively select high-value draft outputs rather than discarding mismatched tokens outright.

These approaches represent the latest work in accelerating LLM reasoning through advanced speculative decoding techniques in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96426a1f-b4e8-4a59-9e29-ad25cadbc7e0",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "ce0d1671-44e3-4fb3-9ee6-0875e2ff20f5",
  "toolUseResult": {
    "query": "thought segment structural label speculative decoding reasoning draft model training R E T 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014gkfMSp81f6p9ebceu6awn",
        "content": [
          {
            "title": "Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance",
            "url": "https://arxiv.org/html/2602.05774v1"
          },
          {
            "title": "Scaling Speculative Decoding with Lookahead Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=JxxKj8pow1"
          },
          {
            "title": "JUDGE DECODING: FASTER SPECULATIVE SAMPLING ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/656d6174fd5ffb01c843f269649ab5cb-Paper-Conference.pdf"
          },
          {
            "title": "Efficient Reasoning for LLMs through Speculative Chain-of-Thought",
            "url": "https://arxiv.org/html/2504.19095v2"
          },
          {
            "title": "Faster Speculative Decoding via Effective Draft ...",
            "url": "https://aclanthology.org/2025.acl-long.486.pdf"
          },
          {
            "title": "ENTROPY-AWARE SPECULATIVE DECODING TOWARD ...",
            "url": "https://openreview.net/pdf/8873a72aa9dd1126e677275974d787218c03b614.pdf"
          },
          {
            "title": "A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling",
            "url": "https://www.arxiv.org/pdf/2509.04474"
          },
          {
            "title": "When Drafts Evolve: Speculative Decoding Meets Online Learning",
            "url": "https://arxiv.org/html/2603.12617"
          },
          {
            "title": "Reward-Guided Speculative Decoding for Efficient LLM ...",
            "url": "https://arxiv.org/pdf/2501.19324"
          },
          {
            "title": "PARALLEL SPECULATIVE DECODING WITH ADAPTIVE ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/03b1043052700b1a471996b0baf309d4-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, I found relevant research on speculative decoding and reasoning models from 2025-2026. Here are the key findings:\n\n## Recent Advances in Speculative Decoding for Reasoning\n\nReasoning models excel by generating long chain-of-thoughts, but decoding the resulting thousands of tokens is slow. Several new approaches have emerged to address this:\n\n**Lookahead Reasoning with Step-Level Parallelism:**\nLookahead reasoning exploits a second, step-level layer of parallelism, with the key insight that reasoning models generate step-by-step, and each step needs only to be semantically correct, not exact token matching. A lightweight draft model proposes several future steps; the target model expands each proposal in one batched pass, and a verifier keeps semantically correct steps.\n\n**Speculative Chain-of-Thought (SCoT):**\nSCoT applies a lightweight draft model to generate multiple CoT drafts in parallel. The draft model is fine-tuned with LoRA modules to align the thinking behavior of the target model. Speculative Chain-of-Thought demonstrates a speed-up ratio of up to 2.92× for the reasoning process while achieving near-target-model-level accuracy on 5 datasets of different difficulties.\n\n**Reward-Guided Speculative Decoding (RSD):**\nUnlike traditional speculative decoding, which strictly enforces unbiasedness, RSD leverages reward signals to adaptively select high-value draft outputs rather than discarding mismatched tokens outright.\n\nThese approaches represent the latest work in accelerating LLM reasoning through advanced speculative decoding techniques in 2025-2026."
    ],
    "durationSeconds": 7.277944449000002
  },
  "sourceToolAssistantUUID": "96426a1f-b4e8-4a59-9e29-ad25cadbc7e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-09T18:53:13.081Z_

<details><summary>Logged reasoning block</summary>

```text
I'm not finding any paper that directly applies thought-segment structural labels (R/E/T) to speculative decoding draft training. This is a good sign for novelty.

Let me now look at some more specific searches:
1. Entropy-aware speculative decoding paper - this appeared in the search and might be competitive
2. New competitive work that might have appeared after Round 3
3. The "Position Specialist Generates Better Draft" paper from 2506.03566 (May 2026) - this might be new and relevant
4. The SpecKV paper (arXiv:2605.02888) - this appeared in May 2026


5. Now I'm checking these papers to see if any of them already explore similar ideas around structural guidance for draft generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce0d1671-44e3-4fb3-9ee6-0875e2ff20f5",
  "isSidechain": false,
  "requestId": "req_011CasVzg63QqqDUEK7V21EQ",
  "type": "assistant",
  "uuid": "794f1880-5ab4-48c9-9154-3bdf4179a46e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Nts8Z4hULFMQyUwAbRyyqz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4075,
      "cache_read_input_tokens": 33906,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 345,
          "cache_read_input_tokens": 33906,
          "cache_creation_input_tokens": 4075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4075
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

_source line 30 · 2026-05-09T18:53:13.150Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WwR9Lxn9oje38KQLxAmr3N`</summary>

```json
{
  "query": "entropy-aware speculative decoding reasoning structure draft training openreview 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "794f1880-5ab4-48c9-9154-3bdf4179a46e",
  "isSidechain": false,
  "requestId": "req_011CasVzg63QqqDUEK7V21EQ",
  "type": "assistant",
  "uuid": "44cd63ac-2a17-4b75-90ff-ed5d91acec6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Nts8Z4hULFMQyUwAbRyyqz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4075,
      "cache_read_input_tokens": 33906,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 345,
          "cache_read_input_tokens": 33906,
          "cache_creation_input_tokens": 4075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4075
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

_source line 31 · 2026-05-09T18:53:13.160Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UvaebwcGYgrXYdhJqHfYru`</summary>

```json
{
  "query": "arXiv 2506.03566 position specialist draft speculative decoding 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44cd63ac-2a17-4b75-90ff-ed5d91acec6f",
  "isSidechain": false,
  "requestId": "req_011CasVzg63QqqDUEK7V21EQ",
  "type": "assistant",
  "uuid": "2c8bb957-14ed-4436-9ee8-34f9805bf975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Nts8Z4hULFMQyUwAbRyyqz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4075,
      "cache_read_input_tokens": 33906,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 345,
          "cache_read_input_tokens": 33906,
          "cache_creation_input_tokens": 4075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4075
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

_source line 32 · 2026-05-09T18:53:13.191Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VUE4RqJk2tjeim4KYiguH9`</summary>

```json
{
  "query": "EMNLP 2026 ARR deadline May 2026 submission deadline confirmed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c8bb957-14ed-4436-9ee8-34f9805bf975",
  "isSidechain": false,
  "requestId": "req_011CasVzg63QqqDUEK7V21EQ",
  "type": "assistant",
  "uuid": "afbe12e1-fe39-4fd1-b0a0-e5eb60af39bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Nts8Z4hULFMQyUwAbRyyqz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4075,
      "cache_read_input_tokens": 33906,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 345,
          "cache_read_input_tokens": 33906,
          "cache_creation_input_tokens": 4075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4075
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "afbe12e1-fe39-4fd1-b0a0-e5eb60af39bf",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-level structural supervision for reasoning speculative decoding",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Tool result

_source line 35 · 2026-05-09T18:53:18.253Z_

<details><summary>↩ Tool result · `toolu_01VUE4RqJk2tjeim4KYiguH9`</summary>

```text
Web search results for query: "EMNLP 2026 ARR deadline May 2026 submission deadline confirmed"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on my search results, here's what I found regarding EMNLP 2026 ARR submission deadlines in May 2026:

## Key Deadline Information

The ARR submission deadline for EMNLP 2026 (for both long and short papers) is May 25, 2026.

## Additional Important Dates

After submission, all authors must complete the reviewer registration form by May 27, 2026. The author response and author-reviewer discussion period is July 7-13, 2026, with meta reviews released on July 30, 2026.

## Important Policy Note

Since the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026 - papers that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

The submission deadline has been officially confirmed in the EMNLP 2026 Call for Papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afbe12e1-fe39-4fd1-b0a0-e5eb60af39bf",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "dc1015ac-f2d5-4217-a2d7-7feb6c5662a1",
  "toolUseResult": {
    "query": "EMNLP 2026 ARR deadline May 2026 submission deadline confirmed",
    "results": [
      {
        "tool_use_id": "srvtoolu_015zbJ75PzsArWzhT4ZyGUht",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "Dates and Venues",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X",
            "url": "https://x.com/emnlpmeeting/status/2029508292637061462"
          },
          {
            "title": "EMNLP 2026 (@emnlpmeeting) / Posts / X",
            "url": "https://x.com/emnlpmeeting?lang=en"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "emnlp 2026 - AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/conference/?id=emnlp26"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X",
            "url": "https://x.com/emnlpmeeting/status/2047754845919031450"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"
          }
        ]
      },
      "Based on my search results, here's what I found regarding EMNLP 2026 ARR submission deadlines in May 2026:\n\n## Key Deadline Information\n\nThe ARR submission deadline for EMNLP 2026 (for both long and short papers) is May 25, 2026.\n\n## Additional Important Dates\n\nAfter submission, all authors must complete the reviewer registration form by May 27, 2026. The author response and author-reviewer discussion period is July 7-13, 2026, with meta reviews released on July 30, 2026.\n\n## Important Policy Note\n\nSince the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026 - papers that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.\n\nThe submission deadline has been officially confirmed in the EMNLP 2026 Call for Papers."
    ],
    "durationSeconds": 5.058477016999998
  },
  "sourceToolAssistantUUID": "afbe12e1-fe39-4fd1-b0a0-e5eb60af39bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-09T18:53:19.925Z_

<details><summary>↩ Tool result · `toolu_01UvaebwcGYgrXYdhJqHfYru`</summary>

```text
Web search results for query: "arXiv 2506.03566 position specialist draft speculative decoding 2026"

Links: [{"title":"[2506.03566] POSS: Position Specialist Generates Better Draft for Speculative Decoding","url":"https://arxiv.org/abs/2506.03566"},{"title":"Position Specialist Generates Better Draft for Speculative ...","url":"https://arxiv.org/pdf/2506.03566"},{"title":"PosS:Position Specialist Generates Better Draft for Speculative Decoding","url":"https://arxiv.org/html/2506.03566"},{"title":"Paper page - POSS: Position Specialist Generates Better Draft for Speculative Decoding","url":"https://huggingface.co/papers/2506.03566"},{"title":"GitHub - shrango/PosS: PosS is a speculative decoding method with position-specialized draft layers generating high-quality drafts. · GitHub","url":"https://github.com/shrango/PosS"},{"title":"Computation and Language Jun 2025","url":"https://www.arxiv.org/list/cs.CL/2025-06?skip=350&show=25"},{"title":"■(\"\") Speculative Decoding via Hybrid Drafting and Rollback-Aware Branch Parallelism","url":"https://arxiv.org/html/2506.01979"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/html/2506.19830"},{"title":"Speculative Decoding with CTC-based Draft Model for LLM Inference Acceleration","url":"https://arxiv.org/html/2412.00061v1"},{"title":"Utility-Driven Speculative Decoding for Mixture-of-Experts","url":"https://arxiv.org/html/2506.20675"}]

I found the paper for you! Here are the key details about arXiv 2506.03566:

**Title:** POSS: Position Specialist Generates Better Draft for Speculative Decoding

**Main Contribution:** The paper proposes Position Specialists (PosS), which consist of multiple position-specialized draft layers to generate tokens at assigned position(s). Position specialists greatly improve token acceptance rate at later positions per drafting round, as each specialist only needs to focus on handling a certain level of draft model feature deviation.

**Problem Addressed:** Existing methods suffer from the degrading quality of draft token predictions at later positions, due to error accumulation in draft model generated features.

**Results:** POSS surpasses the strong baseline HASS on average acceptance length by up to 4.5% (from 4.62 to 4.83) and on speed-up ratio by up to 5.7% (from 2.97x to 3.14x).

**Authors:** Langlin Huang, Chengsong Huang, Jixuan Leng, Di Huang, and Jiaxin Huang

**Submission Date:** June 4, 2025

The paper is available on arXiv with a PDF version, HTML version, and there's also a GitHub repository with the code implementation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c8bb957-14ed-4436-9ee8-34f9805bf975",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "ec5595fa-f00a-48f4-b2df-f4f3cdfaee6f",
  "toolUseResult": {
    "query": "arXiv 2506.03566 position specialist draft speculative decoding 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ChXHkQgMjqq5twZDC5MDSk",
        "content": [
          {
            "title": "[2506.03566] POSS: Position Specialist Generates Better Draft for Speculative Decoding",
            "url": "https://arxiv.org/abs/2506.03566"
          },
          {
            "title": "Position Specialist Generates Better Draft for Speculative ...",
            "url": "https://arxiv.org/pdf/2506.03566"
          },
          {
            "title": "PosS:Position Specialist Generates Better Draft for Speculative Decoding",
            "url": "https://arxiv.org/html/2506.03566"
          },
          {
            "title": "Paper page - POSS: Position Specialist Generates Better Draft for Speculative Decoding",
            "url": "https://huggingface.co/papers/2506.03566"
          },
          {
            "title": "GitHub - shrango/PosS: PosS is a speculative decoding method with position-specialized draft layers generating high-quality drafts. · GitHub",
            "url": "https://github.com/shrango/PosS"
          },
          {
            "title": "Computation and Language Jun 2025",
            "url": "https://www.arxiv.org/list/cs.CL/2025-06?skip=350&show=25"
          },
          {
            "title": "■(\"\") Speculative Decoding via Hybrid Drafting and Rollback-Aware Branch Parallelism",
            "url": "https://arxiv.org/html/2506.01979"
          },
          {
            "title": "Scaling Speculative Decoding with Lookahead Reasoning",
            "url": "https://arxiv.org/html/2506.19830"
          },
          {
            "title": "Speculative Decoding with CTC-based Draft Model for LLM Inference Acceleration",
            "url": "https://arxiv.org/html/2412.00061v1"
          },
          {
            "title": "Utility-Driven Speculative Decoding for Mixture-of-Experts",
            "url": "https://arxiv.org/html/2506.20675"
          }
        ]
      },
      "I found the paper for you! Here are the key details about arXiv 2506.03566:\n\n**Title:** POSS: Position Specialist Generates Better Draft for Speculative Decoding\n\n**Main Contribution:** The paper proposes Position Specialists (PosS), which consist of multiple position-specialized draft layers to generate tokens at assigned position(s). Position specialists greatly improve token acceptance rate at later positions per drafting round, as each specialist only needs to focus on handling a certain level of draft model feature deviation.\n\n**Problem Addressed:** Existing methods suffer from the degrading quality of draft token predictions at later positions, due to error accumulation in draft model generated features.\n\n**Results:** POSS surpasses the strong baseline HASS on average acceptance length by up to 4.5% (from 4.62 to 4.83) and on speed-up ratio by up to 5.7% (from 2.97x to 3.14x).\n\n**Authors:** Langlin Huang, Chengsong Huang, Jixuan Leng, Di Huang, and Jiaxin Huang\n\n**Submission Date:** June 4, 2025\n\nThe paper is available on arXiv with a PDF version, HTML version, and there's also a GitHub repository with the code implementation."
    ],
    "durationSeconds": 6.762081453000006
  },
  "sourceToolAssistantUUID": "2c8bb957-14ed-4436-9ee8-34f9805bf975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-09T18:53:20.244Z_

<details><summary>↩ Tool result · `toolu_01WwR9Lxn9oje38KQLxAmr3N`</summary>

```text
Web search results for query: "entropy-aware speculative decoding reasoning structure draft training openreview 2026"

Links: [{"title":"ENTROPY-AWARE SPECULATIVE DECODING TOWARD ...","url":"https://openreview.net/pdf/8873a72aa9dd1126e677275974d787218c03b614.pdf"},{"title":"Entropy-Aware Speculative Decoding Toward Improved LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=pPa5mIFj5p"},{"title":"TRAINING-FREE LOOSELY SPECULATIVE DECODING","url":"https://openreview.net/pdf/80207abf423159aa729279976811c32dd2f2ea23.pdf"},{"title":"Training-Free Loosely Speculative Decoding: Accepting Semantically Correct Drafts Beyond Exact Match | OpenReview","url":"https://openreview.net/forum?id=JjoTg34YiU"},{"title":"SELF SPECULATIVE DECODING FOR DIFFUSION ...","url":"https://openreview.net/pdf?id=rKJ7A30lQQ"},{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"ENTROPY-AWARE SPECULATIVE DECODING TOWARD IMPROVED LLM REASONING","url":"https://www.arxiv.org/pdf/2512.23765"},{"title":"Entropy-Aware Speculative Decoding Toward Improved LLM Reasoning","url":"https://arxiv.org/html/2512.23765"},{"title":"[2512.23765] Entropy-Aware Speculative Decoding Toward Improved LLM Reasoning","url":"https://arxiv.org/abs/2512.23765"},{"title":"Draft, Verify, \\& Improve: Toward Training-Aware Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=CwvY6TXLxr"}]

I found several relevant papers on entropy-aware speculative decoding and reasoning structures. Here are the key results:

## Entropy-Aware Speculative Decoding (EASD)

The most directly relevant paper is **Entropy-Aware Speculative Decoding (EASD), a training-free enhancement that incorporates a dynamic entropy-based penalty to standard speculative decoding.

**Key Mechanism:** The method employs the entropy of the sampling distribution to quantify model uncertainty. When both models exhibit high entropy with substantial overlap among their top-N predictions, the corresponding token is rejected and re-sampled by the target LLM, preventing low-confidence errors from propagating.

**Performance:** Experiments across multiple reasoning benchmarks demonstrate that EASD consistently outperforms existing SD methods and, in most cases, surpasses the target LLM itself. The efficiency of EASD is comparable to that of SD.

**Evaluation:** The method uses Qwen2.5-7B-Instruct, Qwen2.5-32B-Instruct, and Qwen2.5-72B-Instruct models as draft and target models, with the Skywork-o1-Open-PRM-Qwen-2.5-1.5B model for experiments involving process reward models.

The paper is available on OpenReview (dated December 3, 2025) and represents recent work on improving reasoning performance through entropy-aware token selection in speculative decoding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44cd63ac-2a17-4b75-90ff-ed5d91acec6f",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "5fd71362-18b1-4352-8c64-f44a3c8abe40",
  "toolUseResult": {
    "query": "entropy-aware speculative decoding reasoning structure draft training openreview 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012V1b2GqFbHw2XhPai7krzi",
        "content": [
          {
            "title": "ENTROPY-AWARE SPECULATIVE DECODING TOWARD ...",
            "url": "https://openreview.net/pdf/8873a72aa9dd1126e677275974d787218c03b614.pdf"
          },
          {
            "title": "Entropy-Aware Speculative Decoding Toward Improved LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=pPa5mIFj5p"
          },
          {
            "title": "TRAINING-FREE LOOSELY SPECULATIVE DECODING",
            "url": "https://openreview.net/pdf/80207abf423159aa729279976811c32dd2f2ea23.pdf"
          },
          {
            "title": "Training-Free Loosely Speculative Decoding: Accepting Semantically Correct Drafts Beyond Exact Match | OpenReview",
            "url": "https://openreview.net/forum?id=JjoTg34YiU"
          },
          {
            "title": "SELF SPECULATIVE DECODING FOR DIFFUSION ...",
            "url": "https://openreview.net/pdf?id=rKJ7A30lQQ"
          },
          {
            "title": "Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance",
            "url": "https://arxiv.org/html/2602.05774v1"
          },
          {
            "title": "ENTROPY-AWARE SPECULATIVE DECODING TOWARD IMPROVED LLM REASONING",
            "url": "https://www.arxiv.org/pdf/2512.23765"
          },
          {
            "title": "Entropy-Aware Speculative Decoding Toward Improved LLM Reasoning",
            "url": "https://arxiv.org/html/2512.23765"
          },
          {
            "title": "[2512.23765] Entropy-Aware Speculative Decoding Toward Improved LLM Reasoning",
            "url": "https://arxiv.org/abs/2512.23765"
          },
          {
            "title": "Draft, Verify, \\& Improve: Toward Training-Aware Speculative Decoding | OpenReview",
            "url": "https://openreview.net/forum?id=CwvY6TXLxr"
          }
        ]
      },
      "I found several relevant papers on entropy-aware speculative decoding and reasoning structures. Here are the key results:\n\n## Entropy-Aware Speculative Decoding (EASD)\n\nThe most directly relevant paper is **Entropy-Aware Speculative Decoding (EASD), a training-free enhancement that incorporates a dynamic entropy-based penalty to standard speculative decoding.\n\n**Key Mechanism:** The method employs the entropy of the sampling distribution to quantify model uncertainty. When both models exhibit high entropy with substantial overlap among their top-N predictions, the corresponding token is rejected and re-sampled by the target LLM, preventing low-confidence errors from propagating.\n\n**Performance:** Experiments across multiple reasoning benchmarks demonstrate that EASD consistently outperforms existing SD methods and, in most cases, surpasses the target LLM itself. The efficiency of EASD is comparable to that of SD.\n\n**Evaluation:** The method uses Qwen2.5-7B-Instruct, Qwen2.5-32B-Instruct, and Qwen2.5-72B-Instruct models as draft and target models, with the Skywork-o1-Open-PRM-Qwen-2.5-1.5B model for experiments involving process reward models.\n\nThe paper is available on OpenReview (dated December 3, 2025) and represents recent work on improving reasoning performance through entropy-aware token selection in speculative decoding."
    ],
    "durationSeconds": 7.089713127000003
  },
  "sourceToolAssistantUUID": "44cd63ac-2a17-4b75-90ff-ed5d91acec6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-09T18:53:20.247Z_

```json
{
  "parentUuid": "5fd71362-18b1-4352-8c64-f44a3c8abe40",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e2e169ee-622c-4184-8497-690bc4cdf477",
  "timestamp": "2026-05-09T18:53:20.247Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 39 · 2026-05-09T18:53:27.191Z_

<details><summary>Logged reasoning block</summary>

```text
Good. So the venue deadline is confirmed - EMNLP 2026 ARR deadline is May 25, 2026. That's valid.

Now let me check:
1. The POSS paper (arXiv:2506.03566) - this is from June 4, 2025 but appeared in a search for 2026. It's a speculative decoding paper with position specialization. It doesn't seem to directly conflict with the proposed method's structural supervision approach.

2. Entropy-aware speculative decoding (arXiv:2512.23765) - this is a training-free method using entropy-based penalties. 

Neither of these papers directly addresses structural training supervision with R/E/T labels, so I should search more specifically for concurrent work in that area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2e169ee-622c-4184-8497-690bc4cdf477",
  "isSidechain": false,
  "requestId": "req_011CasW1xBwnHfvuy8JrrZcg",
  "type": "assistant",
  "uuid": "ac486cd6-d15b-4516-876e-a22f109c011f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01M1BZD43we1bzPhE6jSvry2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1775,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 37981,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1775,
          "output_tokens": 325,
          "cache_read_input_tokens": 37981,
          "cache_creation_input_tokens": 1355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1355
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

_source line 40 · 2026-05-09T18:53:27.250Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0171n9Da5HFAJx5uXqmfmjYf`</summary>

```json
{
  "query": "reasoning type classification speculative decoding draft training semantic role supervision 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac486cd6-d15b-4516-876e-a22f109c011f",
  "isSidechain": false,
  "requestId": "req_011CasW1xBwnHfvuy8JrrZcg",
  "type": "assistant",
  "uuid": "692023f4-6069-4a5c-8ff1-9a5058b6920f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01M1BZD43we1bzPhE6jSvry2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1775,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 37981,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1775,
          "output_tokens": 325,
          "cache_read_input_tokens": 37981,
          "cache_creation_input_tokens": 1355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1355
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

_source line 41 · 2026-05-09T18:53:27.255Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LPFNcQecuoQ41KNyMyCxxh`</summary>

```json
{
  "query": "DeepSeek R1 speculative decoding draft model reasoning structure alignment 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "692023f4-6069-4a5c-8ff1-9a5058b6920f",
  "isSidechain": false,
  "requestId": "req_011CasW1xBwnHfvuy8JrrZcg",
  "type": "assistant",
  "uuid": "f16e2845-fe64-4a88-bad8-0a1be131e7b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01M1BZD43we1bzPhE6jSvry2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1775,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 37981,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1775,
          "output_tokens": 325,
          "cache_read_input_tokens": 37981,
          "cache_creation_input_tokens": 1355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1355
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

_source line 42 · 2026-05-09T18:53:35.162Z_

<details><summary>↩ Tool result · `toolu_01LPFNcQecuoQ41KNyMyCxxh`</summary>

```text
Web search results for query: "DeepSeek R1 speculative decoding draft model reasoning structure alignment 2025 2026 arxiv"

Links: [{"title":"Efficient Reasoning for LLMs through Speculative Chain-of-Thought","url":"https://arxiv.org/html/2504.19095v2"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/html/2506.19830v1"},{"title":"alamios/DeepSeek-R1-DRAFT-Qwen2.5-0.5B · Hugging Face","url":"https://huggingface.co/alamios/DeepSeek-R1-DRAFT-Qwen2.5-0.5B"},{"title":"Boosting DeepSeek-R1’s Speed with Customized Speculative Decoding","url":"https://www.together.ai/blog/customized-speculative-decoding"},{"title":"Aman's AI Journal • Primers • DeepSeek-R1","url":"https://aman.ai/primers/ai/deepseek-R1/"},{"title":"Turbocharge Deepseek-R1 in vLLM with Speculative Decoding | by Moser Sandro | Medium","url":"https://medium.com/@moser.sandro2/turbocharge-deepseek-r1-in-vllm-with-speculative-decoding-f6480ac612c9"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via","url":"https://arxiv.org/pdf/2501.12948"},{"title":"deepseek-ai/DeepSeek-R1 · Draft model as accelerator for DeepSeek-R1?","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1/discussions/174"},{"title":"Self-Distilling DeepSeek-R1 with Turbo Speculation - 2x Inference","url":"https://predibase.com/blog/predibase.com/blog/deepseek-r1-self-distillation-turbo-speculation"},{"title":"SGLang Speculative Decoding Tutorial: How to Deploy DeepSeek Models and Achieve 1.4× Throughput – With Benchmarks","url":"https://company.hpc-ai.com/blog/sglang-speculative-decoding-tutorial"}]

Based on the search results, here's what I found regarding DeepSeek R1 speculative decoding, draft models, and reasoning structure alignment:

## Key Findings

### Speculative Decoding with DeepSeek-R1

DeepSeek-R1 is a large reasoning language model that has recently attracted widespread attention due to its impressive task-solving abilities. Speculative decoding speeds up LLM decoding by using a smaller, faster "speculator" model to speculate the next few tokens, which are then verified in parallel by the larger "target" model.

### Multi-Token Prediction (MTP) as Built-in Draft Model

A notable finding is that DeepSeek-R1/V3 models don't need separate draft models — they are trained with a technique called Multi-Token Prediction (MTP) (also known as next-n prediction). The MTP module can serve directly as the draft model, simplifying deployment.

### Thinking Behavior Alignment

Recent research addresses alignment of reasoning structures. Speculative Chain-of-Thought (SCoT) reduces reasoning latency through large and small model collaboration, conducting thought-level drafting using a lightweight draft model. The proposed thinking behavior alignment improves the efficiency of drafting and the draft selection strategy maintains the prediction accuracy of the target model for complex tasks.

### Step-Level Reasoning Speculation

More recent work explores step-level speculation beyond token-level: Over 50% of DeepSeek-R1 32B's reasoning steps can be replaced with semantically equivalent ones from another smaller model with minimal impact on overall task accuracy, with deviations typically not exceeding 2%. Lookahead Reasoning alone achieves speedups ranging from 1.04x to 1.71x across various benchmarks, and when combined with n-gram speculative decoding, the total speedup reaches up to 2.11x.

### Performance Improvements

SCoT demonstrates an average speed-up ratio of 2.3× and 1.6× for reasoning models on reasoning latency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f16e2845-fe64-4a88-bad8-0a1be131e7b7",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "3e31cb65-0a74-4758-98d2-9c45802a59dc",
  "toolUseResult": {
    "query": "DeepSeek R1 speculative decoding draft model reasoning structure alignment 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XGfxyDC8u4TcSQcVRbYixK",
        "content": [
          {
            "title": "Efficient Reasoning for LLMs through Speculative Chain-of-Thought",
            "url": "https://arxiv.org/html/2504.19095v2"
          },
          {
            "title": "Scaling Speculative Decoding with Lookahead Reasoning",
            "url": "https://arxiv.org/html/2506.19830v1"
          },
          {
            "title": "alamios/DeepSeek-R1-DRAFT-Qwen2.5-0.5B · Hugging Face",
            "url": "https://huggingface.co/alamios/DeepSeek-R1-DRAFT-Qwen2.5-0.5B"
          },
          {
            "title": "Boosting DeepSeek-R1’s Speed with Customized Speculative Decoding",
            "url": "https://www.together.ai/blog/customized-speculative-decoding"
          },
          {
            "title": "Aman's AI Journal • Primers • DeepSeek-R1",
            "url": "https://aman.ai/primers/ai/deepseek-R1/"
          },
          {
            "title": "Turbocharge Deepseek-R1 in vLLM with Speculative Decoding | by Moser Sandro | Medium",
            "url": "https://medium.com/@moser.sandro2/turbocharge-deepseek-r1-in-vllm-with-speculative-decoding-f6480ac612c9"
          },
          {
            "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via",
            "url": "https://arxiv.org/pdf/2501.12948"
          },
          {
            "title": "deepseek-ai/DeepSeek-R1 · Draft model as accelerator for DeepSeek-R1?",
            "url": "https://huggingface.co/deepseek-ai/DeepSeek-R1/discussions/174"
          },
          {
            "title": "Self-Distilling DeepSeek-R1 with Turbo Speculation - 2x Inference",
            "url": "https://predibase.com/blog/predibase.com/blog/deepseek-r1-self-distillation-turbo-speculation"
          },
          {
            "title": "SGLang Speculative Decoding Tutorial: How to Deploy DeepSeek Models and Achieve 1.4× Throughput – With Benchmarks",
            "url": "https://company.hpc-ai.com/blog/sglang-speculative-decoding-tutorial"
          }
        ]
      },
      "Based on the search results, here's what I found regarding DeepSeek R1 speculative decoding, draft models, and reasoning structure alignment:\n\n## Key Findings\n\n### Speculative Decoding with DeepSeek-R1\n\nDeepSeek-R1 is a large reasoning language model that has recently attracted widespread attention due to its impressive task-solving abilities. Speculative decoding speeds up LLM decoding by using a smaller, faster \"speculator\" model to speculate the next few tokens, which are then verified in parallel by the larger \"target\" model.\n\n### Multi-Token Prediction (MTP) as Built-in Draft Model\n\nA notable finding is that DeepSeek-R1/V3 models don't need separate draft models — they are trained with a technique called Multi-Token Prediction (MTP) (also known as next-n prediction). The MTP module can serve directly as the draft model, simplifying deployment.\n\n### Thinking Behavior Alignment\n\nRecent research addresses alignment of reasoning structures. Speculative Chain-of-Thought (SCoT) reduces reasoning latency through large and small model collaboration, conducting thought-level drafting using a lightweight draft model. The proposed thinking behavior alignment improves the efficiency of drafting and the draft selection strategy maintains the prediction accuracy of the target model for complex tasks.\n\n### Step-Level Reasoning Speculation\n\nMore recent work explores step-level speculation beyond token-level: Over 50% of DeepSeek-R1 32B's reasoning steps can be replaced with semantically equivalent ones from another smaller model with minimal impact on overall task accuracy, with deviations typically not exceeding 2%. Lookahead Reasoning alone achieves speedups ranging from 1.04x to 1.71x across various benchmarks, and when combined with n-gram speculative decoding, the total speedup reaches up to 2.11x.\n\n### Performance Improvements\n\nSCoT demonstrates an average speed-up ratio of 2.3× and 1.6× for reasoning models on reasoning latency."
    ],
    "durationSeconds": 7.904292982999992
  },
  "sourceToolAssistantUUID": "f16e2845-fe64-4a88-bad8-0a1be131e7b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3e31cb65-0a74-4758-98d2-9c45802a59dc",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-level structural supervision for reasoning speculative decoding",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Tool result

_source line 45 · 2026-05-09T18:53:35.422Z_

<details><summary>↩ Tool result · `toolu_0171n9Da5HFAJx5uXqmfmjYf`</summary>

```text
Web search results for query: "reasoning type classification speculative decoding draft training semantic role supervision 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=aL1Wnml9Ef"},{"title":"Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework | OpenReview","url":"https://openreview.net/forum?id=bKau2NNrji"},{"title":"Draft, Verify, & Improve Toward Training-Aware Speculative Decoding","url":"https://arxiv.org/html/2510.05421v1"},{"title":"Training Domain Draft Models for Speculative Decoding: Best Practices and Insights","url":"https://arxiv.org/html/2503.07807v1"},{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"[2510.05421] Draft, Verify, and Improve: Toward Training-Aware Speculative Decoding","url":"https://arxiv.org/abs/2510.05421"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/pdf/2506.19830"},{"title":"An Empirical Study of Speculative Decoding on Software Engineering Tasks","url":"https://arxiv.org/html/2604.26469v1"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning | OpenReview","url":"https://openreview.net/forum?id=JxxKj8pow1"},{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"}]

I found several relevant research papers and resources related to your search query. Here are the key findings:

## Recent Advances in Speculative Decoding (2026)

A notable 2026 ICLR paper introduces Speculative Speculative Decoding (SSD), which parallelizes speculation and verification operations. While verification is ongoing, the draft model predicts likely verification outcomes and prepares speculations pre-emptively for them, eliminating drafting overhead entirely if the verification outcome matches the prediction.

## Chain-of-Thought and Semantic Role-Guided Training

Recent work addresses training-based speculative decoding methods for chain-of-thought (CoT) reasoning, proposing a CoT-aware mixed training framework that combines process-level CoT distillation with feature regression, and uses SurpriseRatio (SR) as a data-selection metric to prevent catastrophic forgetting under CoT supervision.

## Reasoning-Level Speculative Decoding

A novel approach enables speculation at the reasoning step level, where a model can guess and verify the next few reasoning steps rather than just tokens, with step proposals and verification being independent and executable in parallel.

## Variational Approaches to Draft Training

Variational Speculative Decoding (VSD) reformulates draft model training as a variational inference problem, treating the draft path as a latent proposal and maximizing the marginal likelihood of target model acceptance, with an Evidence Lower Bound (ELBO) serving as the training objective.

## Domain-Specific Training Insights

Empirical studies show that offline distillation consistently outperforms online distillation, as offline distillation leverages supervision from all completion tokens, providing richer learning signals for the draft model.

These research directions highlight recent progress in making speculative decoding more efficient through better training strategies, semantic-level reasoning supervision, and improved draft-target alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "692023f4-6069-4a5c-8ff1-9a5058b6920f",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "afe95429-fc40-4d0b-beba-29a2336cbf09",
  "toolUseResult": {
    "query": "reasoning type classification speculative decoding draft training semantic role supervision 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S7JWPYHGBSUDGMfhgzMWH8",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING",
            "url": "https://openreview.net/pdf?id=aL1Wnml9Ef"
          },
          {
            "title": "Aligning Draft and Target in Speculative Decoding: A CoT-Aware and SR-Guided Mixed Framework | OpenReview",
            "url": "https://openreview.net/forum?id=bKau2NNrji"
          },
          {
            "title": "Draft, Verify, & Improve Toward Training-Aware Speculative Decoding",
            "url": "https://arxiv.org/html/2510.05421v1"
          },
          {
            "title": "Training Domain Draft Models for Speculative Decoding: Best Practices and Insights",
            "url": "https://arxiv.org/html/2503.07807v1"
          },
          {
            "title": "Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance",
            "url": "https://arxiv.org/html/2602.05774v1"
          },
          {
            "title": "[2510.05421] Draft, Verify, and Improve: Toward Training-Aware Speculative Decoding",
            "url": "https://arxiv.org/abs/2510.05421"
          },
          {
            "title": "Scaling Speculative Decoding with Lookahead Reasoning",
            "url": "https://arxiv.org/pdf/2506.19830"
          },
          {
            "title": "An Empirical Study of Speculative Decoding on Software Engineering Tasks",
            "url": "https://arxiv.org/html/2604.26469v1"
          },
          {
            "title": "Scaling Speculative Decoding with Lookahead Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=JxxKj8pow1"
          },
          {
            "title": "Speculative Decoding: Types and Optimizations",
            "url": "https://www.aussieai.com/research/speculative-decoding"
          }
        ]
      },
      "I found several relevant research papers and resources related to your search query. Here are the key findings:\n\n## Recent Advances in Speculative Decoding (2026)\n\nA notable 2026 ICLR paper introduces Speculative Speculative Decoding (SSD), which parallelizes speculation and verification operations. While verification is ongoing, the draft model predicts likely verification outcomes and prepares speculations pre-emptively for them, eliminating drafting overhead entirely if the verification outcome matches the prediction.\n\n## Chain-of-Thought and Semantic Role-Guided Training\n\nRecent work addresses training-based speculative decoding methods for chain-of-thought (CoT) reasoning, proposing a CoT-aware mixed training framework that combines process-level CoT distillation with feature regression, and uses SurpriseRatio (SR) as a data-selection metric to prevent catastrophic forgetting under CoT supervision.\n\n## Reasoning-Level Speculative Decoding\n\nA novel approach enables speculation at the reasoning step level, where a model can guess and verify the next few reasoning steps rather than just tokens, with step proposals and verification being independent and executable in parallel.\n\n## Variational Approaches to Draft Training\n\nVariational Speculative Decoding (VSD) reformulates draft model training as a variational inference problem, treating the draft path as a latent proposal and maximizing the marginal likelihood of target model acceptance, with an Evidence Lower Bound (ELBO) serving as the training objective.\n\n## Domain-Specific Training Insights\n\nEmpirical studies show that offline distillation consistently outperforms online distillation, as offline distillation leverages supervision from all completion tokens, providing richer learning signals for the draft model.\n\nThese research directions highlight recent progress in making speculative decoding more efficient through better training strategies, semantic-level reasoning supervision, and improved draft-target alignment."
    ],
    "durationSeconds": 8.168811365000002
  },
  "sourceToolAssistantUUID": "692023f4-6069-4a5c-8ff1-9a5058b6920f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-09T18:53:43.351Z_

<details><summary>Logged reasoning block</summary>

```text
I found a new paper: "Scaling Speculative Decoding with Lookahead Reasoning" (arXiv:2506.19830). Let me check this more carefully - it seems to be from June 2026 and might be concurrent work.

Also, let me check the "Speculative Speculative Decoding" paper from ICLR 2026.

But more importantly, I need to check if any of these papers specifically use structural supervision with reasoning type labels (R/E/T) for draft training. None of the search results suggest this specific combination, which supports the novelty claim.

Let me now check:


I should look more closely at the recent papers that might be related - particularly the "Scaling Speculative Decoding with Lookahead Reasoning" paper from June 2026 and the AdaSPEC paper on selective knowledge distillation for speculative decoders, since these could be competing approaches in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afe95429-fc40-4d0b-beba-29a2336cbf09",
  "isSidechain": false,
  "requestId": "req_011CasW353E8BUHqauJRsbmx",
  "type": "assistant",
  "uuid": "00eb2f81-7493-4a17-b419-421ac0ee612b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CciXi4ry8VsFztqCcVx5Fu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1109,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 39336,
      "output_tokens": 482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3041,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1109,
          "output_tokens": 482,
          "cache_read_input_tokens": 39336,
          "cache_creation_input_tokens": 3041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3041
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

_source line 47 · 2026-05-09T18:53:43.354Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RqQw164eWZCNpL427exCAd`</summary>

```json
{
  "query": "arXiv 2506.19830 scaling speculative decoding lookahead reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00eb2f81-7493-4a17-b419-421ac0ee612b",
  "isSidechain": false,
  "requestId": "req_011CasW353E8BUHqauJRsbmx",
  "type": "assistant",
  "uuid": "ad740f89-420b-4e29-be87-ac2c06454eac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CciXi4ry8VsFztqCcVx5Fu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1109,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 39336,
      "output_tokens": 482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3041,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1109,
          "output_tokens": 482,
          "cache_read_input_tokens": 39336,
          "cache_creation_input_tokens": 3041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3041
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

_source line 48 · 2026-05-09T18:53:45.055Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0143Loxfu5Wa8NrEVcXDt2SY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.19095",
  "prompt": "What is the core method of SCoT? Does it use any structural labels (R/E/T or similar) for thought-type supervision during draft training? What speedups does it achieve on DeepSeek-R1-Distill-32B and 70B?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad740f89-420b-4e29-be87-ac2c06454eac",
  "isSidechain": false,
  "requestId": "req_011CasW353E8BUHqauJRsbmx",
  "type": "assistant",
  "uuid": "dbdca861-7b6e-463e-9422-de6430ba5816",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CciXi4ry8VsFztqCcVx5Fu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1109,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 39336,
      "output_tokens": 482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3041,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1109,
          "output_tokens": 482,
          "cache_read_input_tokens": 39336,
          "cache_creation_input_tokens": 3041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3041
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

_source line 49 · 2026-05-09T18:53:49.284Z_

<details><summary>↩ Tool result · `toolu_01RqQw164eWZCNpL427exCAd`</summary>

```text
Web search results for query: "arXiv 2506.19830 scaling speculative decoding lookahead reasoning 2026"

Links: [{"title":"[2506.19830] Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/abs/2506.19830"},{"title":"arXiv:2506.19830v1 [cs.LG] 24 Jun 2025 Scaling Speculative Decoding with","url":"https://arxiv.org/pdf/2506.19830"},{"title":"[PDF] Scaling Speculative Decoding with Lookahead Reasoning | Semantic Scholar","url":"https://api.semanticscholar.org/arXiv:2506.19830"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/html/2506.19830"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=10150&show=25"},{"title":"GitHub - hao-ai-lab/LookaheadReasoning: [NeurIPS 2025] Scaling Speculative Decoding with Lookahead Reasoning","url":"https://github.com/hao-ai-lab/LookaheadReasoning"},{"title":"Paper page - Scaling Speculative Decoding with Lookahead Reasoning","url":"https://huggingface.co/papers/2506.19830"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning | Hao AI Lab @ UCSD","url":"https://haoailab.com/blogs/lookaheadreasoning/"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning | OpenReview","url":"https://openreview.net/forum?id=JxxKj8pow1"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=2050&show=25"}]

I found the paper! Here are the results for arXiv 2506.19830:

**Title:** Scaling Speculative Decoding with Lookahead Reasoning

**Authors:** Yichao Fu, Rui Ge, Zelei Shao, Zhijie Deng, Hao Zhang

**Submission Date:** Submitted on 24 Jun 2025

**Overview:**
Reasoning models excel by generating long chain-of-thoughts, but decoding the resulting thousands of tokens is slow. Token-level speculative decoding (SD) helps, but its benefit is capped, because the chance that an entire γ-token guess is correct falls exponentially as γ grows, meaning allocating more compute for longer token drafts faces an algorithmic ceiling.

**Proposed Solution:**
The paper introduces Lookahead Reasoning, which exploits a second, step-level layer of parallelism, based on the insight that reasoning models generate step-by-step, and each step needs only to be semantically correct, not exact token matching.

**Key Results:**
Lookahead Reasoning improves the speedup of Token-level speculative decoding from 1.4x to 2.1x while preserving answer quality, and its speedup scales better with additional GPU throughput.

The paper is available on arXiv at https://arxiv.org/abs/2506.19830.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad740f89-420b-4e29-be87-ac2c06454eac",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "fcc68aba-250d-44a0-82a2-e836ba743670",
  "toolUseResult": {
    "query": "arXiv 2506.19830 scaling speculative decoding lookahead reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EdernUH8zaAC39zTzaH88v",
        "content": [
          {
            "title": "[2506.19830] Scaling Speculative Decoding with Lookahead Reasoning",
            "url": "https://arxiv.org/abs/2506.19830"
          },
          {
            "title": "arXiv:2506.19830v1 [cs.LG] 24 Jun 2025 Scaling Speculative Decoding with",
            "url": "https://arxiv.org/pdf/2506.19830"
          },
          {
            "title": "[PDF] Scaling Speculative Decoding with Lookahead Reasoning | Semantic Scholar",
            "url": "https://api.semanticscholar.org/arXiv:2506.19830"
          },
          {
            "title": "Scaling Speculative Decoding with Lookahead Reasoning",
            "url": "https://arxiv.org/html/2506.19830"
          },
          {
            "title": "Computer Science Jun 2025",
            "url": "https://arxiv.org/list/cs/2025-06?skip=10150&show=25"
          },
          {
            "title": "GitHub - hao-ai-lab/LookaheadReasoning: [NeurIPS 2025] Scaling Speculative Decoding with Lookahead Reasoning",
            "url": "https://github.com/hao-ai-lab/LookaheadReasoning"
          },
          {
            "title": "Paper page - Scaling Speculative Decoding with Lookahead Reasoning",
            "url": "https://huggingface.co/papers/2506.19830"
          },
          {
            "title": "Scaling Speculative Decoding with Lookahead Reasoning | Hao AI Lab @ UCSD",
            "url": "https://haoailab.com/blogs/lookaheadreasoning/"
          },
          {
            "title": "Scaling Speculative Decoding with Lookahead Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=JxxKj8pow1"
          },
          {
            "title": "Machine Learning Jun 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-06?skip=2050&show=25"
          }
        ]
      },
      "I found the paper! Here are the results for arXiv 2506.19830:\n\n**Title:** Scaling Speculative Decoding with Lookahead Reasoning\n\n**Authors:** Yichao Fu, Rui Ge, Zelei Shao, Zhijie Deng, Hao Zhang\n\n**Submission Date:** Submitted on 24 Jun 2025\n\n**Overview:**\nReasoning models excel by generating long chain-of-thoughts, but decoding the resulting thousands of tokens is slow. Token-level speculative decoding (SD) helps, but its benefit is capped, because the chance that an entire γ-token guess is correct falls exponentially as γ grows, meaning allocating more compute for longer token drafts faces an algorithmic ceiling.\n\n**Proposed Solution:**\nThe paper introduces Lookahead Reasoning, which exploits a second, step-level layer of parallelism, based on the insight that reasoning models generate step-by-step, and each step needs only to be semantically correct, not exact token matching.\n\n**Key Results:**\nLookahead Reasoning improves the speedup of Token-level speculative decoding from 1.4x to 2.1x while preserving answer quality, and its speedup scales better with additional GPU throughput.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2506.19830."
    ],
    "durationSeconds": 5.926164929999999
  },
  "sourceToolAssistantUUID": "ad740f89-420b-4e29-be87-ac2c06454eac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-09T18:53:49.534Z_

<details><summary>↩ Tool result · `toolu_0143Loxfu5Wa8NrEVcXDt2SY`</summary>

```text
# Speculative Chain-of-Thought (SCoT) Overview

## Core Method

SCoT reduces reasoning latency through collaboration between large and small models. The approach involves: "thought-level drafting using a lightweight draft model. Then it selects the best CoT draft and corrects the error cases with the target model."

The paper mentions "thinking behavior alignment" to enhance drafting efficiency and employs "draft selection strategy" to preserve prediction accuracy on complex tasks.

## Structural Labels

The provided abstract does not specify whether SCoT uses structural labels (such as R/E/T categories) for supervising thought types during draft training. This information is unavailable in the excerpt.

## Performance Speedups

The method achieves notable efficiency gains:

- **DeepSeek-R1-Distill-Qwen-32B**: 48%–66% latency reduction
- **DeepSeek-R1-Distill-Llama-70B**: 21%–49% latency reduction

These improvements were demonstrated across multiple benchmarks (GSM8K, MATH, GaoKao, CollegeMath, and Olympiad datasets) while maintaining near-target-model-level performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbdca861-7b6e-463e-9422-de6430ba5816",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "cccd543a-8515-45ae-8adc-f0a3fb8a331e",
  "toolUseResult": {
    "bytes": 46848,
    "code": 200,
    "codeText": "OK",
    "result": "# Speculative Chain-of-Thought (SCoT) Overview\n\n## Core Method\n\nSCoT reduces reasoning latency through collaboration between large and small models. The approach involves: \"thought-level drafting using a lightweight draft model. Then it selects the best CoT draft and corrects the error cases with the target model.\"\n\nThe paper mentions \"thinking behavior alignment\" to enhance drafting efficiency and employs \"draft selection strategy\" to preserve prediction accuracy on complex tasks.\n\n## Structural Labels\n\nThe provided abstract does not specify whether SCoT uses structural labels (such as R/E/T categories) for supervising thought types during draft training. This information is unavailable in the excerpt.\n\n## Performance Speedups\n\nThe method achieves notable efficiency gains:\n\n- **DeepSeek-R1-Distill-Qwen-32B**: 48%–66% latency reduction\n- **DeepSeek-R1-Distill-Llama-70B**: 21%–49% latency reduction\n\nThese improvements were demonstrated across multiple benchmarks (GSM8K, MATH, GaoKao, CollegeMath, and Olympiad datasets) while maintaining near-target-model-level performance.",
    "durationMs": 4474,
    "url": "https://arxiv.org/abs/2504.19095"
  },
  "sourceToolAssistantUUID": "dbdca861-7b6e-463e-9422-de6430ba5816",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-09T18:55:57.231Z_

<details><summary>Logged reasoning block</summary>

```text
Good. So I've verified that:
1. ThinKV is indeed ICLR 2026 Oral - confirmed
2. EAGLE-3 is NeurIPS 2025 - confirmed
3. CoT-Aware paper (OpenReview bKau2NNrji) exists and is real - confirmed
4. LTD (arXiv:2603.01639) exists and is ICLR 2026 - confirmed
5. SCoT achieves 48-66% latency reduction on 32B and 21-49% on 70B - this matches the correctly revised claims in the proposal


6. The Lookahead Reasoning paper uses step-level semantic verification for parallelism, which is distinct from the thought-segment R/E/T labeling approach. I haven't found any existing work that applies structural R/E/T labels at the thought-segment level for speculative decoding draft training, so the novelty claim holds up.

Now I'm assessing how the Round 3 issues have been resolved, starting with the LTD paper confirmation.

All the previous concerns appear to be addressed. Now I need to check a couple of newer papers that surfaced in my searches—SpecKV from May 2026 and AdaSPEC—to see if either one directly competes with what's being proposed here.

The Lookahead Reasoning paper does touch on speculative decoding for reasoning models, but it's focused on semantic verification at the step level rather than the structural label approach for draft training that this proposal uses, so there's meaningful differentiation there. On the resource side, I'm working through the feasibility of the budget constraints—Phase 0 looks reasonable for collecting traces on the target model, but Phase 1 gets trickier since training an EAGLE-3-style draft requires direct access to the target model's internal features, which raises questions about whether that's actually available in the proposed setup.

For the auto-research mode, running 12 iterations with roughly 13 hours of H100 time per iteration plus evaluation adds up to around 186 hours total, which feels optimistic but potentially doable. The real bottleneck is that the 70B target model itself needs 4 H100s just to serve, so the cost of generating training data for the draft model compounds quickly. The evaluation suite has expanded to include MT-Bench and HumanEval alongside the math benchmarks, though I'm noticing the original constraints mentioned perplexity as a metric and I need to check whether that's still being tracked. I see the tension here—the user explicitly required those benchmarks, and the Round 3 review flagged that the proposal is missing several of them. LongBench and RULER are designed for long-context evaluation, which might seem tangential to speculative decoding on reasoning models, but the user's requirements are clear and non-negotiable. I need to acknowledge that MT-Bench and HumanEval have been added, but perplexity, MMLU, LongBench, and RULER still need to be included to fully satisfy the stated evaluation criteria. constraint from the user specification, not a stylistic preference."

The round 3 review said "at minimum, MT-Bench and HumanEval must be added" - the generator did exactly this. However, the full constraint includes perplexity, MMLU, LongBench, and RULER which are still missing. 

But wait - the round 3 review only identified "at minimum, MT-Bench and HumanEval" as the required addition and didn't explicitly say MMLU/LongBench/RULER/perplexity must be added. The generator addressed the specific feedback, not the full original constraint.

Should I now raise this as a new issue? I think I should flag that perplexity (Wiki/C4), MMLU, LongBench, and RULER are still missing from the eval suite per the user's explicit hard constraints. This might be legitimate for a reasoning-focused paper, but the generator should explicitly justify why these are omitted or include them.

Looking at this more carefully, I'm reconsidering whether all these benchmarks are actually necessary. Perplexity on Wiki/C4 isn't standard for speculative decoding papers, and MMLU isn't typically included either. LongBench and RULER could be relevant since reasoning models produce longer outputs, but for a paper focused on speculative decoding with reasoning LLMs, the core evals should be reasoning benchmarks, general quality metrics, code quality, and wall-clock speedup - which are mostly covered now. LongBench and RULER might be nice to have but aren't critical.

I should note that the reviewer already identified the minimum required additions and those have been addressed, so I'll treat this as partially resolved. The remaining metrics from the original constraint are still missing, but I'll flag this as a minor issue since the core feedback has been incorporated.

Also worth noting: there's a concurrent paper called Lookahead Reasoning that tackles the same problem of slow speculative decoding for reasoning models, though it uses step-level semantic verification rather than draft training structural supervision.

The Phase 0 χ² test design looks sound as a segment-level analysis with fallback pivots. I should verify whether AdaSPEC is a direct competitor, and then do a final check on resource estimates. The Lookahead Reasoning paper was submitted in June 2025 and accepted to NeurIPS 2025—it's distinct from this proposal since it focuses on semantic correctness verification rather than structural labels during draft training. Since it's a NeurIPS 2025 paper, reviewers will likely be aware of it, and the proposal should probably acknowledge this related work in the landscape.

Looking at the overall state, all the round 1, 2, and 3 issues have been addressed. The core novelty around structural labels and Markov transition consistency for speculative decoding appears defensible with no direct competitors identified. The Phase 0 gate is well-designed, resource estimates are reasonable, the venue deadline is confirmed, and key references check out. The only remaining gap is that the Lookahead Reasoning paper—which achieves 1.4x to 2.1x speedup through step-level parallelism for reasoning models—should be cited as related work targeting the same problem space, even though the mechanisms differ.

There are also a few minor evaluation gaps: Perplexity, MMLU, LongBench, and RULER are still missing from the benchmark suite despite the user's hard constraints, though MT-Bench and HumanEval were added in round 3. The Phase 3 resource estimate of ~30 hours on H100 for evaluation needs clarification on whether it covers running DeepSeek-R1-Distill-70B across all five benchmarks, which seems plausible but should be explicitly confirmed.

After four rounds of iteration with all major issues resolved, this looks ready to move forward.

The core contribution is genuinely novel—applying segment-level R/E/T labels with Markov transition consistency to speculative decoding draft training hasn't been done before. It's feasible within the 200 H100-hour budget, well-motivated with a proper Phase 0 gate, and addresses a real gap in the literature with clear differentiation from existing work. The novelty scores around 4/5 for the specific combination of techniques, even though individual components aren't entirely new.

Feasibility sits at 3.5/5—the resource estimates are reasonable but somewhat optimistic, particularly around the 70B target model serving costs during training and the assumed 88% GPU utilization. The Phase 0 gate helps mitigate the risk of wasted compute if early results don't pan out. Clarity is strong at 4/5 with the proposal well-articulated and the Phase 0 logic sound. Impact lands at 3.5/5—if successful, this would meaningfully improve speculative decoding for reasoning models through structural supervision, though the expected gains in marginal acceptance rates are modest.

The average comes to 3.75, which falls below the 4.0 threshold for acceptance. I'm flagging two substantive issues: the missing Lookahead Reasoning paper from NeurIPS 2025 that should be addressed, and some evaluation metrics that don't fully align with the user's hard constraints. The evaluation metrics themselves—mean accepted tokens per step, acceptance rate, wall-clock speedup—are appropriate for speculative decoding work, but there's a gap in how comprehensively they're being applied.

I'm realizing that LongBench and RULER could actually be quite valuable here since reasoning models generate very long thinking traces, and if this method improves structural coherence in those traces, those benchmarks would be ideal testbeds. Their absence is a real limitation. I'm also concerned about the statistical power of the Phase 0 hypothesis test—with 1K traces and multiple segment-level decisions per trace, I need to think through whether the χ² test has enough granularity to detect meaningful differences in the R/E/T distributions.

There's another issue: if Phase 0 fails to show statistical significance, the fallback of comparing draft vs. target model distributions is weaker conceptually—it shifts from "structural mismatch causes rejection" to just "the distributions differ," which is a less direct justification for the training objective. The paper needs to be clearer about what threshold of evidence is sufficient to proceed.

I'm also checking whether AdaSPEC is a direct competitor here, and I'm noticing a critical gap in the related work—there's a recent paper on speculative decoding with lookahead reasoning that should be included in the landscape.

Now let me finalize my assessment of the issues. The missing citation on step-level semantic correctness for reasoning speedup is significant enough that EMNLP reviewers will catch it, and the paper should position this work as orthogonal to that approach. Beyond that, the evaluation is incomplete—the user's constraints explicitly call for perplexity benchmarks, MMLU, LongBench, and RULER, but LongBench and RULER are missing. These are especially important for validating that the thought-segment supervision actually helps with long reasoning traces. Finally, the χ² test on just 1K traces might lack sufficient statistical power. power if each trace has only a few structural segment transitions. The paper should specify the expected number of segment-level comparisons (not just trace-level), and potentially increase the sample to 2K-3K traces if the average accepted/rejected segment count per trace is low.

**Scoring:**
- Novelty: 4/5 (The R/E/T segment-label + Markov transition objective combination is genuinely novel; no direct competitor found despite multiple independent searches)
- Feasibility: 3.5/5 (Resource budget is tight but plausible; Phase 0 gate is excellent risk management; 70B serving overhead during draft training is a real bottleneck that the estimates may undercount)
- Clarity: 4/5 (Well-articulated differentiation from all cited work; Phase 0 gate logic is clear and sound)
- Impact: 3.5/5 (Addressing structural coherence in reasoning traces is meaningful, but expected performance gain may be incremental over EAGLE-3 baselines; composability narrative is strong)

Average: 3.75 — below the 4.0 pass threshold, so this needs revision. The issues are relatively minor though: one missing related work citation and incomplete evaluation coverage for the user's hard constraint metrics. Another round should get this across the line.

Let me reconsider the feasibility score more carefully. The auto-research mode estimates 186h H100 for 12 runs (roughly 13h per run, plus 30h for evaluation), but there's a critical constraint I'm underweighting: the 70B model needs to stay running during draft training for feature extraction.

Running the 70B model on 4 H100s costs around $12–16 per hour just for serving, and training a 7B draft model in parallel requires additional GPUs. If I assume 6 H100s per run (4 for the target model, 2 for draft training), that's 78 H100-hours per run, scaling to roughly 936 H100-hours across all 12 runs—significantly higher than the stated 156h estimate.

The discrepancy hinges on how "H100-hours" is defined. In ML, it typically means total GPU-hours summed across all cards, so 4 H100s × 13h = 52 H100-hours per run, which still totals around 624 H100-hours across 12 runs, well above the 200h budget. I need to clarify whether the original estimate accounts for the actual parallelism required or if there's a mismatch in how the resource calculation was framed. 4 H100s running for 13 hours = 52 H100-GPU-hours, then 12 runs = 624 H100-GPU-hours. This would far exceed the cap.

But actually, the standard ML convention is that "H100-hours" = total compute in terms of individual GPU-hours. So if you use 4 H100s for 13 hours, that's 52 H100-hours. The proposal claiming 12 runs × 13h ≈ 156h is only valid if each run uses exactly 1 H100, which is impossible for a 70B target model.

This is actually the feasibility issue from Round 1 that was supposedly fixed. The fix proposed 12 runs at ~15 H100-hours each ≈ 180 H100-hours total. But now the estimate says "12 primary runs × ~13h H100/run ≈ 156h H100" — and I need to figure out what "13h H100/run" actually means. If it's 13 total H100-GPU-hours per run, that's impossible on a 70B model. If it's 13 hours wall-clock time on 4 H100s, that's 52 H100-GPU-hours per run, totaling 624 — way over budget. Or maybe it's only counting draft model training time, not the full run.

Actually, thinking about EAGLE-style training: you pre-generate features from the target model once, then train the draft model on those pre-computed features. The pre-generation is a one-time cost of maybe 8-16 H100-GPU-hours, and then each draft training run is much cheaper — perhaps 1-3 hours on 1-2 H100s. So the total would be around 16 H100-GPU-hours for pre-generation plus 12 runs at maybe 2-6 H100-GPU-hours each, totaling somewhere in the 40-88 H100-GPU-hour range, which fits the budget.

Now I'm working through the actual breakdown: the feature pre-computation is 16 H100-GPU-hours, the 12 draft training runs come to 72 H100-GPU-hours, and evaluation of the 70B model at 4 H100s for 30 hours adds another 120 H100-GPU-hours. That puts us at 208 total, just barely over the cap. But if they batch the evaluation or optimize the trace sampling phase, they could probably squeeze it down to fit within the 200 H100-GPU-hour limit.

The real question is what "~13h H100/run" actually means—whether it's wall-clock time multiplied by GPU count or something else entirely. Given that this proposal has already gone through multiple rounds of review, I'm inclined to assume the authors know what they're doing, though the resource accounting methodology really should be spelled out more clearly to avoid this kind of confusion.

Looking at their actual breakdown in the auto_research mode section, they're claiming 12 primary runs at roughly 13 H100-hours each for about 156 H100-hours, plus another 30 H100-hours for evaluation across 5 benchmarks, totaling 186 H100-hours. The ambiguity creeps in when I try to work backwards—if they're training a 7B draft model on 2 H100s while the 70B target runs on 4 H100s, the math gets complicated depending on whether these runs happen sequentially or in parallel. Let me verify the math: 144-192 for training plus 8-16 for data generation plus 30 for evaluation gets me to 182-238 H100-hours, which pushes past the stated budget. But if I interpret the 156h estimate as total H100-GPU-hours across all 12 runs, that's about 13 hours per run—which works out if each run uses 2 H100s for 6.5 hours of wall-clock time. That's plausible for a lightly fine-tuned 7B model, so the resource estimates check out. I'd rate the feasibility as a 3.

5 out of 5 since the numbers are reasonable but the GPU allocation versus wall-clock time distinction creates some ambiguity, and the actual serving costs for the 70B target model remain hard to pin down without implementation.

Looking at the overall assessment: there's solid novelty here, the feasibility is plausible, the writing is clear, and the impact is moderate. But I'm flagging three issues—most importantly, the paper misses Lookahead Reasoning from the recent landscape, and it's also missing LongBench and RULER from the evaluation suite despite those being explicitly listed as hard constraints. The Phase 0 statistical power also needs more precision around the actual number of segment-level observations. Averaging these scores puts me below the 4.0 threshold, so the verdict is revise with specific guidance on addressing these gaps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cccd543a-8515-45ae-8adc-f0a3fb8a331e",
  "isSidechain": false,
  "requestId": "req_011CasW47Neb5pZqoZdgqGMb",
  "type": "assistant",
  "uuid": "089c073d-c241-4f32-ac11-a8a14bd955af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JQQKMsX7X672XNUL9PHKRg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 42377,
      "output_tokens": 6861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6861,
          "cache_read_input_tokens": 42377,
          "cache_creation_input_tokens": 2763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2763
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

_source line 52 · 2026-05-09T18:55:57.292Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01154qBaAfXiuQEBvPZRTGQR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.19830",
  "prompt": "What is the core method of this paper? Does it use structural labels for reasoning types (R/E/T or similar)? What speedups does it achieve and on which models/benchmarks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "089c073d-c241-4f32-ac11-a8a14bd955af",
  "isSidechain": false,
  "requestId": "req_011CasW47Neb5pZqoZdgqGMb",
  "type": "assistant",
  "uuid": "e5a00829-41c4-4e97-a1e6-ddf53dbfdc8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JQQKMsX7X672XNUL9PHKRg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 42377,
      "output_tokens": 6861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6861,
          "cache_read_input_tokens": 42377,
          "cache_creation_input_tokens": 2763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2763
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

_source line 53 · 2026-05-09T18:55:57.300Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AmMffzdcn2CCFqWxdfgwgX`</summary>

```json
{
  "query": "AdaSPEC selective knowledge distillation speculative decoding 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5a00829-41c4-4e97-a1e6-ddf53dbfdc8e",
  "isSidechain": false,
  "requestId": "req_011CasW47Neb5pZqoZdgqGMb",
  "type": "assistant",
  "uuid": "69ff944d-759b-4c1c-8a3c-17132d7bda27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JQQKMsX7X672XNUL9PHKRg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 42377,
      "output_tokens": 6861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6861,
          "cache_read_input_tokens": 42377,
          "cache_creation_input_tokens": 2763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2763
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

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "69ff944d-759b-4c1c-8a3c-17132d7bda27",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-level structural supervision for reasoning speculative decoding",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Tool result

_source line 56 · 2026-05-09T18:56:01.511Z_

<details><summary>↩ Tool result · `toolu_01154qBaAfXiuQEBvPZRTGQR`</summary>

```text
# Summary of "Scaling Speculative Decoding with Lookahead Reasoning"

## Core Method

The paper introduces **Lookahead Reasoning**, which adds a step-level parallelism layer to token-level speculative decoding. As described, "a lightweight draft model proposes several future steps; the target model expands each proposal in one batched pass, and a verifier keeps semantically correct steps" while regenerating failures.

The key innovation is recognizing that reasoning models work step-by-step, where "each step needs only to be semantically correct, not exact token matching," rather than requiring exact token matches.

## Structural Labels

The paper does not appear to use structural reasoning labels (like R/E/T notation) based on the abstract provided.

## Performance Results

The method achieves:
- **Speedup improvement**: From 1.4x to 2.1x on speculative decoding
- **Answer quality**: Preserved across benchmarks
- **Scaling behavior**: Better speedup with additional GPU throughput

## Benchmarks Tested

Results are reported on:
- GSM8K
- AIME
- Other unspecified benchmarks

The authors note their speedup "scales better with additional GPU throughput," indicating improved hardware efficiency compared to traditional speculative decoding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5a00829-41c4-4e97-a1e6-ddf53dbfdc8e",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "0bff8024-4d5f-437a-af5a-77e50f9c67b3",
  "toolUseResult": {
    "bytes": 47258,
    "code": 200,
    "codeText": "OK",
    "result": "# Summary of \"Scaling Speculative Decoding with Lookahead Reasoning\"\n\n## Core Method\n\nThe paper introduces **Lookahead Reasoning**, which adds a step-level parallelism layer to token-level speculative decoding. As described, \"a lightweight draft model proposes several future steps; the target model expands each proposal in one batched pass, and a verifier keeps semantically correct steps\" while regenerating failures.\n\nThe key innovation is recognizing that reasoning models work step-by-step, where \"each step needs only to be semantically correct, not exact token matching,\" rather than requiring exact token matches.\n\n## Structural Labels\n\nThe paper does not appear to use structural reasoning labels (like R/E/T notation) based on the abstract provided.\n\n## Performance Results\n\nThe method achieves:\n- **Speedup improvement**: From 1.4x to 2.1x on speculative decoding\n- **Answer quality**: Preserved across benchmarks\n- **Scaling behavior**: Better speedup with additional GPU throughput\n\n## Benchmarks Tested\n\nResults are reported on:\n- GSM8K\n- AIME\n- Other unspecified benchmarks\n\nThe authors note their speedup \"scales better with additional GPU throughput,\" indicating improved hardware efficiency compared to traditional speculative decoding.",
    "durationMs": 4214,
    "url": "https://arxiv.org/abs/2506.19830"
  },
  "sourceToolAssistantUUID": "e5a00829-41c4-4e97-a1e6-ddf53dbfdc8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-09T18:56:05.369Z_

<details><summary>↩ Tool result · `toolu_01AmMffzdcn2CCFqWxdfgwgX`</summary>

```text
Web search results for query: "AdaSPEC selective knowledge distillation speculative decoding 2025 2026"

Links: [{"title":"AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders | OpenReview","url":"https://openreview.net/forum?id=zNLlglSOwD"},{"title":"[2510.19779] AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders","url":"https://arxiv.org/abs/2510.19779"},{"title":"GitHub - yuezhouhu/adaspec: A selective knowledge distillation algorithm for efficient speculative decoders · GitHub","url":"https://github.com/yuezhouhu/adaspec"},{"title":"AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders","url":"https://openreview.net/pdf?id=zNLlglSOwD"},{"title":"NeurIPS Poster AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/115055"},{"title":"Paper page - AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders","url":"https://huggingface.co/papers/2510.19779"},{"title":"AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoding","url":"https://neurips.cc/media/neurips-2025/Slides/115055.pdf"},{"title":"(PDF) AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders","url":"https://www.researchgate.net/publication/396790231_AdaSPEC_Selective_Knowledge_Distillation_for_Efficient_Speculative_Decoders"},{"title":"[PDF] AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AdaSPEC:-Selective-Knowledge-Distillation-for-Hu-Guo/9c265d9b32dbb9dec1d24d03f6a749a965481a69"},{"title":"AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders - DEV Community","url":"https://dev.to/paperium/adaspec-selective-knowledge-distillation-for-efficient-speculative-decoders-53a5"}]

Based on the search results, here's comprehensive information about AdaSPEC:

## Overview

AdaSPEC is a novel method for selective knowledge distillation in speculative decoding that incorporates selective token filtering into the knowledge distillation process by using a reference model to identify and filter out difficult-to-fit tokens, enabling the distillation of a draft model that better aligns with the target model on simpler tokens.

## Problem It Addresses

Speculative decoding accelerates large language model inference by employing a small draft model to generate predictions, which are then verified by a larger target model. While the effectiveness of SD hinges on the alignment between these models (typically enhanced by Knowledge Distillation), conventional KD methods aim to minimize the KL divergence between the draft and target models across all tokens—a goal misaligned with SD's true objective of maximizing token acceptance rate.

## Technical Approach

AdaSPEC introduces a two-stage selective knowledge distillation framework where a reference model (initialized identically to the draft model) is first distilled from the target model using standard knowledge distillation to serve as a proxy to estimate token-wise learning difficulty. During distillation of the actual draft model, AdaSPEC computes the KL divergence loss for each token and calculates the loss gap, with tokens having larger gaps considered easier to learn, then selects the top-k% of these "easy" tokens to train the draft model.

## Performance Results

AdaSPEC consistently outperforms the state-of-the-art DistillSpec method, achieving higher acceptance rates across all tasks (up to 15%). On various tasks, AdaSPEC exhibits 10-20% speed-up.

## Publication Status

The paper has been accepted as a Spotlight at NeurIPS 2025. The code is publicly available at https://github.com/yuezhouhu/adaspec.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69ff944d-759b-4c1c-8a3c-17132d7bda27",
  "isSidechain": false,
  "promptId": "102c5516-16db-4498-aa3b-415c653c38d9",
  "type": "user",
  "uuid": "14ce64fe-4036-4ca8-9bee-b3dd0f9bf310",
  "toolUseResult": {
    "query": "AdaSPEC selective knowledge distillation speculative decoding 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CJUV7AAxiYmGC15Vc3LgTR",
        "content": [
          {
            "title": "AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders | OpenReview",
            "url": "https://openreview.net/forum?id=zNLlglSOwD"
          },
          {
            "title": "[2510.19779] AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders",
            "url": "https://arxiv.org/abs/2510.19779"
          },
          {
            "title": "GitHub - yuezhouhu/adaspec: A selective knowledge distillation algorithm for efficient speculative decoders · GitHub",
            "url": "https://github.com/yuezhouhu/adaspec"
          },
          {
            "title": "AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders",
            "url": "https://openreview.net/pdf?id=zNLlglSOwD"
          },
          {
            "title": "NeurIPS Poster AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/115055"
          },
          {
            "title": "Paper page - AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders",
            "url": "https://huggingface.co/papers/2510.19779"
          },
          {
            "title": "AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoding",
            "url": "https://neurips.cc/media/neurips-2025/Slides/115055.pdf"
          },
          {
            "title": "(PDF) AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders",
            "url": "https://www.researchgate.net/publication/396790231_AdaSPEC_Selective_Knowledge_Distillation_for_Efficient_Speculative_Decoders"
          },
          {
            "title": "[PDF] AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/AdaSPEC:-Selective-Knowledge-Distillation-for-Hu-Guo/9c265d9b32dbb9dec1d24d03f6a749a965481a69"
          },
          {
            "title": "AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders - DEV Community",
            "url": "https://dev.to/paperium/adaspec-selective-knowledge-distillation-for-efficient-speculative-decoders-53a5"
          }
        ]
      },
      "Based on the search results, here's comprehensive information about AdaSPEC:\n\n## Overview\n\nAdaSPEC is a novel method for selective knowledge distillation in speculative decoding that incorporates selective token filtering into the knowledge distillation process by using a reference model to identify and filter out difficult-to-fit tokens, enabling the distillation of a draft model that better aligns with the target model on simpler tokens.\n\n## Problem It Addresses\n\nSpeculative decoding accelerates large language model inference by employing a small draft model to generate predictions, which are then verified by a larger target model. While the effectiveness of SD hinges on the alignment between these models (typically enhanced by Knowledge Distillation), conventional KD methods aim to minimize the KL divergence between the draft and target models across all tokens—a goal misaligned with SD's true objective of maximizing token acceptance rate.\n\n## Technical Approach\n\nAdaSPEC introduces a two-stage selective knowledge distillation framework where a reference model (initialized identically to the draft model) is first distilled from the target model using standard knowledge distillation to serve as a proxy to estimate token-wise learning difficulty. During distillation of the actual draft model, AdaSPEC computes the KL divergence loss for each token and calculates the loss gap, with tokens having larger gaps considered easier to learn, then selects the top-k% of these \"easy\" tokens to train the draft model.\n\n## Performance Results\n\nAdaSPEC consistently outperforms the state-of-the-art DistillSpec method, achieving higher acceptance rates across all tasks (up to 15%). On various tasks, AdaSPEC exhibits 10-20% speed-up.\n\n## Publication Status\n\nThe paper has been accepted as a Spotlight at NeurIPS 2025. The code is publicly available at https://github.com/yuezhouhu/adaspec."
    ],
    "durationSeconds": 8.065894786999998
  },
  "sourceToolAssistantUUID": "69ff944d-759b-4c1c-8a3c-17132d7bda27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-09T18:56:42.808Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have more comprehensive information. Let me assess the AdaSPEC paper - it uses selective knowledge distillation based on token-wise learning difficulty (loss gap from a reference model), which is different from the proposed method's structural supervision. The proposals are non-competing: AdaSPEC selects "easy" tokens based on loss gap, while the proposed method adds R/E/T structural role supervision. They're complementary, not competing.

For Lookahead Reasoning (arXiv:2506.19830, NeurIPS 2025) - it achieves 1.4x→2.1x speedup via step-level semantic verification of reasoning steps. 

The proposal doesn't cite this paper, but it should be - it's the most recent NeurIPS 2025 work on reasoning speedup through speculative methods, operates at the step level (orthogonal to the draft training structural approach), and EMNLP reviewers will definitely be aware of it. I should also check if anything recent combines structural labels with speculative decoding, though I think I have enough to form my assessment now. Let me verify the key claims I've confirmed so far.

I've now verified most of the major citations - ThinKV's ICLR 2026 oral status, EAGLE-3 at NeurIPS 2025, the CoT-Aware paper, LTD's arxiv and poster acceptance, and the SCoT performance numbers. The EMNLP 2026 deadline checks out too. ARBITRAGE is characterized reasonably even if I haven't directly verified it, and I haven't found a direct competitor for the specific R/E/T label plus Markov transition consistency combination. Some claims like the SemanticSpec paper remain unverified but seem plausible.

Looking at what's missing from the landscape, Lookahead Reasoning from NeurIPS 2025 is a notable gap for reasoning model speedup, and AdaSPEC from the same conference could serve as a complementary citation for selective knowledge distillation in draft training. The evaluation suite still lacks LongBench and RULER per the user's requirements, which remains a constraint to address.

Now scoring the core contribution: the novelty of the R/E/T labeling scheme with Markov transitions is solid at 4/5, though feasibility drops to 3.5/5 due to ambiguity around resource calculations and the real overhead of 70B model serving. The clarity is strong at 4/5 with a well-designed Phase 0 gate, but impact sits at 3.5/5 since the gains may be incremental over EAGLE-3's already competitive baseline. This averages to 3.75, suggesting another revision cycle is needed to push above 4.0.

The key gaps to address are adding the Lookahead Reasoning citation, expanding the evaluation suite to include perplexity benchmarks on Wiki/C4, MMLU, LongBench, and RULER to fully satisfy the user's hard constraints, and mentioning AdaSPEC. Looking at the eval mismatch more carefully—the proposal currently covers only 2 of 6 required benchmarks, so I need to integrate the missing four while keeping the existing ones like MT-Bench and HumanEval that were already added in the previous round. of which appear in the required suite" issue. The current proposal still doesn't include 4 of the 6 required metrics.

I'm questioning whether these metrics actually fit a speculative decoding paper though. Perplexity and MMLU aren't standard for SD research—they'd require running the full draft + verification pipeline on those benchmarks, which is atypical. LongBench and RULER could make sense for testing long-context reasoning, but they're not typical SD evaluation targets either.

For EMNLP 2026 efficiency papers, the focus should really be on speedup metrics like acceptance rate and wall-clock time on standard benchmarks. The proposal's choice of AIME24, AMC23, LiveCodeBench, MT-Bench, and HumanEval is actually more aligned with speculative decoding research on reasoning models than the user's required set.

That said, the user explicitly required these benchmarks, so I need to flag the gap. The previous reviewer mentioned "at minimum, MT-Bench and HumanEval," suggesting some flexibility, but the full constraint still isn't met. I'll mark LongBench and RULER as minor missing items since they could be relevant for long-context reasoning, and perplexity/MMLU as very minor since they're less standard for SD papers.

The verdict should be revise, with the key remaining issue being the Lookahead Reasoning paper that needs to be addressed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14ce64fe-4036-4ca8-9bee-b3dd0f9bf310",
  "isSidechain": false,
  "requestId": "req_011CasWE89p3FgQu82VWNZJx",
  "type": "assistant",
  "uuid": "f790f539-3972-4b24-a64f-36ac656a5f61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0116g7kDefWTRK3sxSzf8nLu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8270,
      "cache_read_input_tokens": 45140,
      "output_tokens": 3915,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8270,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3915,
          "cache_read_input_tokens": 45140,
          "cache_creation_input_tokens": 8270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8270
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

_source line 59 · 2026-05-09T18:57:22.989Z_

Now I have sufficient information for a thorough verdict. Let me compile my findings.

**Verified claims:**
- ThinKV ICLR 2026 Oral: ✓ confirmed (iclr.cc/virtual/2026/oral/10009981)
- EAGLE-3 NeurIPS 2025: ✓ confirmed (neurips.cc/virtual/2025/poster/119930)
- CoT-Aware (OpenReview bKau2NNrji): ✓ exists, correctly characterized
- LTD (arXiv:2603.01639, ICLR 2026 Poster): ✓ confirmed
- SCoT 48–66% on 32B, 21–49% on 70B: ✓ confirmed
- EMNLP 2026 ARR deadline May 25, 2026: ✓ confirmed
- No direct competitor found applying R/E/T segment labels + Markov transition objective to speculative decoding draft training

**Missing from landscape (found independently):**
- Lookahead Reasoning (arXiv:2506.19830, NeurIPS 2025) — achieves 1.4×→2.1× speedup for reasoning models via step-level semantic correctness; closely related to the proposal's target problem
- AdaSPEC (arXiv:2510.19779, NeurIPS 2025 Spotlight) — selective KD for draft training based on token-wise learning difficulty; directly related to non-uniform token importance in draft training

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "The specific combination of thought-segment-level R/E/T structural labels plus a Markov segment-transition consistency objective for speculative decoding draft training finds no direct precedent across multiple independent searches. Differentiation from CoT-Aware (step-level process supervision without structural role taxonomy), SFDD (flatness ≠ structural role), LTD (RL without structural signal), and SCoT (generic smaller model, no structural supervision) is now accurate and defensible."
    },
    "feasibility": {
      "score": 3,
      "rationale": "Resource accounting is ambiguous: the auto-research ablation claims '12 runs × ~13h H100/run ≈ 156h H100' but does not clarify whether 13h is wall-clock × 1 GPU or total GPU-hours summed across cards. With DeepSeek-R1-Distill-70B requiring 4–8 H100s for serving alone, each training run using 2 additional H100s for the draft model implies 6–10 H100s × 6–8h wall-clock = 36–80 H100-hours per run; 12 runs would yield 432–960 H100-hours far exceeding the 200h cap — unless EAGLE-style feature pre-generation is done in one shared pass and draft training is counted separately; this interpretation is never made explicit and leaves the feasibility claim underspecified."
    },
    "clarity": {
      "score": 4,
      "rationale": "The differentiation from prior work is now precise and consistently scoped to the segment level; the Phase 0 gate with its χ² primary path and structural-bias fallback is methodologically sound and constitutes a genuine publishable contribution regardless of main experiment outcome."
    },
    "impact": {
      "score": 3,
      "rationale": "Improving acceptance rate for reasoning LLMs via structural draft supervision targets a real and growing deployment problem; however, EAGLE-3 already achieves 4.1–6.5× speedup on general tasks, and the marginal gain from structural supervision on reasoning traces is uncertain — the field may shift toward step-level semantic methods (Lookahead Reasoning achieves 2.1× on top of token-level SD) or RL-adaptive policies (LTD), making the auxiliary-head approach incremental by comparison."
    }
  },
  "issues": [
    "IMPORTANT — MISSING RELATED WORK: 'Scaling Speculative Decoding with Lookahead Reasoning' (arXiv:2506.19830, NeurIPS 2025, Yichao Fu et al., Hao AI Lab UCSD) is absent from the landscape. This paper achieves 1.4×→2.1× speedup for reasoning models by exploiting step-level semantic correctness — each reasoning step needs only to be semantically correct, not an exact token match — which is the closest competing narrative for 'reasoning-aware speculative decoding.' EMNLP 2026 reviewers familiar with reasoning efficiency will notice its absence. It should be added as a complementary step-level semantic approach that is orthogonal to draft-training structural supervision (reasoning step correctness ≠ token-segment-level R/E/T training signal) and composable with the proposed method.",
    "IMPORTANT — RESOURCE ACCOUNTING AMBIGUITY: The auto-research estimate '12 runs × ~13h H100/run ≈ 156h H100' is numerically inconsistent unless 13h H100/run means total GPU-hours summed across all cards per run. With DeepSeek-R1-Distill-70B requiring 4 H100s for serving, and 2 additional H100s for draft training, a single run on 6 H100s for ~2–3h wall-clock yields 12–18 H100-hours — consistent with the ~13h estimate only if the target model's serving cost is excluded (pre-computed once and shared). The proposal must explicitly state: (a) how the 70B target model's serving cost is amortized across runs (single pre-generation pass vs. per-run inference), (b) the assumed GPU count per run, and (c) whether '13h H100/run' is wall-clock hours or total GPU-hours. Without this, the constraint adherence claim cannot be verified and reviewers will challenge it.",
    "MINOR — INCOMPLETE EVAL COVERAGE: The user's hard constraint explicitly lists perplexity (Wiki/C4), MMLU, LongBench, and RULER alongside HumanEval and MT-Bench. LongBench and RULER are particularly relevant for reasoning models — reasoning traces are long outputs, and demonstrating that thought-segment structural supervision generalizes to long-context evaluation settings (LongBench) and extreme-length position fidelity (RULER) would strengthen the paper. Perplexity (Wiki/C4) could validate that the auxiliary training does not degrade general LM quality. Even if these metrics are not standard in SD papers, their inclusion or explicit justification for exclusion is required by the user's specification.",
    "MINOR — MISSING RELATED WORK: 'AdaSPEC: Selective Knowledge Distillation for Efficient Speculative Decoders' (arXiv:2510.19779, NeurIPS 2025 Spotlight) proposes selective token filtering in knowledge distillation for draft models based on token-wise learning difficulty — directly related to the non-uniform token importance framing shared with both the proposed method and SFDD. It should be cited alongside SFDD as a complementary approach: AdaSPEC uses loss gap from a reference model to identify easy vs. hard tokens, while the proposed method uses structural role. Both are non-competing, but AdaSPEC's NeurIPS 2025 Spotlight status means reviewers will notice its absence if the paper discusses token-level importance in draft training."
  ],
  "feedback": "Round 1–3 issues are fully resolved and the core contribution — thought-segment-level R/E/T structural supervision with a Markov segment-transition KL objective for speculative decoding draft training — remains genuinely novel with no direct competitors found across independent searches. Three targeted fixes before submission: (1) Add Lookahead Reasoning (arXiv:2506.19830, NeurIPS 2025) to the landscape — position it as a step-level semantic correctness approach (orthogonal to token-segment structural training) that achieves 1.4×→2.1× speedup for reasoning models; this is the most closely related NeurIPS 2025 paper on reasoning model speedup via speculative-style methods and its absence will be noticed by reviewers. (2) Make the resource accounting explicit: state clearly that the 70B target model features are pre-generated once in a shared pass (cost once, amortized across all 12 runs), and that '13h H100/run' refers to draft model training only on 2 H100s — give the GPU count per phase explicitly so the 186h H100 total is verifiable from first principles. (3) Add LongBench and RULER to Phase 3 evaluation (they are in the user's hard constraint eval list and are germane to reasoning models with long outputs); cite AdaSPEC (arXiv:2510.19779, NeurIPS 2025 Spotlight) alongside SFDD in the related work section on non-uniform token importance for draft training.",
  "reason": "All three prior rounds' issues resolved; three remaining fixable gaps — missing Lookahead Reasoning (NeurIPS 2025) from landscape, opaque resource accounting that leaves the 200h budget claim unverifiable, and incomplete eval coverage per user's hard constraint — keep average score at 3.75 (below 4.0 pass threshold)."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f790f539-3972-4b24-a64f-36ac656a5f61",
  "isSidechain": false,
  "requestId": "req_011CasWE89p3FgQu82VWNZJx",
  "type": "assistant",
  "uuid": "5aad172a-6daf-4d7c-b02f-0eaaff9f5d52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0116g7kDefWTRK3sxSzf8nLu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8270,
      "cache_read_input_tokens": 45140,
      "output_tokens": 3915,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8270,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3915,
          "cache_read_input_tokens": 45140,
          "cache_creation_input_tokens": 8270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8270
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

_source line 60_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "5aad172a-6daf-4d7c-b02f-0eaaff9f5d52",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-level structural supervision for reasoning speculative decoding",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "5aad172a-6daf-4d7c-b02f-0eaaff9f5d52",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Segment-level structural supervision for reasoning speculative decoding",
  "sessionId": "b2543a7e-fa6f-404f-9e22-c793de4d8c9f"
}
```

---
