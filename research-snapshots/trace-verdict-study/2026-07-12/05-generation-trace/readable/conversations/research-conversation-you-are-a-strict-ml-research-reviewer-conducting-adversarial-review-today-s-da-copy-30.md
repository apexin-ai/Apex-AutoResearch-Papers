# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-09 (UTC).** Your job: indep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/57d61d9c-5d24-47f2-be2a-4d09a61db58a.jsonl`
- **Structured JSON:** [`bc56de41139b1169845b.json`](../../sessions/bc/bc56de41139b1169845b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-09T21:05:01.078Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-09T21:05:01.078Z",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-09 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.\n\nDirection: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.\n2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.\n3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.\n\nThis is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.\n\nTag: direction=data_governance, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-09?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 8/10)\n{\n  \"title\": \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\",\n  \"core_problem\": \"Current AI-generated text detectors are binary (human vs. AI), but training corpora increasingly contain 'second-generation' synthetic text: AI outputs from models that were themselves trained on AI-generated data. This generational depth is unmeasured and unaddressed by any existing detector. Strong Model Collapse (ICLR 2025) establishes that even non-vanishing fractions (~1%) of synthetic data trigger performance collapse, yet the paper treats all synthetic data equivalently — making no distinction between Gen1 text (one model generation removed from human data) and Gen2+ text (recursively compounded). The depth-dependent contribution to collapse severity is entirely uncharacterized, and no current method can assign a generational depth score to a raw training document. Critically, recent work (arXiv:2605.01647, May 2026) demonstrates a 'Wall of Separation' where AI-AI divergence in character-distribution space is significantly smaller than human-AI divergence — making within-model generational discrimination (Gen1 vs. Gen2 from the same fine-tuned model) a harder detection problem than binary human/AI classification and motivating our use of embedding-space features that target cumulative semantic drift orthogonal to character-level surface signals.\",\n  \"opportunity\": \"By April 2025, 74.2% of newly created web pages contain some AI-generated text — of which 2.5% are fully AI-generated and 71.7% are human-AI blends, where human content has been AI-revised or AI-assisted (Ahrefs, 900K pages, April 2025). These blended documents may occupy an intermediate 'Gen0.5' depth position between Gen0 and Gen1 that depth scoring can address more precisely than binary detection, and they represent the dominant contamination modality at web scale. Complete decontamination is operationally infeasible — there is not enough uncontaminated human text to replace even the fully AI-generated fraction — shifting the practical research question from 'remove all synthetic data' (impossible at web scale) to 'which synthetic documents to prioritize for removal given a fixed filtering budget.' Depth-stratified decontamination addresses this directly: if Gen2+ documents are disproportionately harmful relative to Gen1 documents, preferential removal of deeper-generation text maximizes collapse mitigation per unit of filtering effort. This claim is explicitly scoped to *severity reduction per filtering budget*, not collapse prevention, and is tested in controlled fixed-total-size depth-composition conditions that isolate the effect of contamination depth from dataset volume — making the causal evidence for the governance claim empirically clean. Strong Model Collapse (ICLR 2025) provides the urgency but not the answer — it shows synthetic data is harmful at any non-vanishing fraction but gives no guidance on whether all synthetic data is equally harmful. Crucially, the paper does not distinguish Gen1 from Gen2 synthetic data at all, leaving the depth-dependent harm gradient completely unmeasured. A depth classifier that enables tiered decontamination — or, if depth discrimination fails, definitively establishes that binary filtering suffices — constitutes a concrete empirical contribution with direct governance impact, aligned with EMNLP 2026's special theme 'New Missions for NLP Research,' which explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance.'\",\n  \"landscape\": \"Model collapse from recursive synthetic training is established (Shumailov et al., Nature 2024; Strong Model Collapse, ICLR 2025) and the limiting theory predicts collapse at any non-vanishing synthetic fraction. Mitigation via real-data accumulation (arXiv:2404.01413) or verifier-guided retraining (arXiv:2510.16657) is active. arXiv:2602.10531 ('From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources', February 2026) analyzes the statistical dynamics of iterative training on data contaminated with synthetic samples using a mixture-model framework, showing that improvement over collapsed models is possible when sufficient fresh real data is present; it does not assign generational depth labels to documents or propose a depth-stratified filtering method. Training-side collapse prevention via Truncated Cross-Entropy loss (ForTIFAI, arXiv:2509.08972) selectively ignores high-confidence tokens during training to filter synthetic artifacts — a complementary but orthogonal approach to our upstream corpus-level depth detection: ForTIFAI does not classify documents by generational depth and does not operate pre-training. The closest upstream related work, 'Machine-generated text detection prevents language model collapse' (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025), directly bridges AI-text detection and collapse prevention: it trains encoder-only binary classifiers (evaluating RoBERTa, DeBERTa-v3, and ModernBERT) to distinguish human from AI-generated text, then applies importance resampling — weighting each training document by (1-q(x))^b where q(x) is the classifier's AI-probability score — to up-weight likely human content during recursive training. Experiments across GPT-2 and SmolLM2 (124M–1.7B parameters) demonstrate that binary-classifier-guided resampling prevents collapse and even improves over training on purely human data. Critically, arXiv:2502.15654 treats all AI-generated text as equivalent regardless of generational provenance: importance weights depend only on a single binary human/AI probability, with no distinction between Gen1 text (one fine-tuning cycle removed from human data) and Gen2+ text (recursively compounded). Our work directly addresses this gap: if depth-stratified resampling weights — proportional to estimated generational distance from Gen0 — yield greater collapse-severity reduction per resampled document than flat binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over arXiv:2502.15654's strategy under budget-constrained filtering. The dual null-hypothesis design explicitly covers the scenario where depth discrimination fails (AUC < 0.65), in which case our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant and binary resampling is sufficient — a governance finding with direct practical value. A mathematical framework for how recursive publication compresses text through drift and selection is developed in arXiv:2604.08554 but does not propose a depth classifier. The framework is derived for variable-order n-gram agents and does not address transformer fine-tuning; extension to neural models is an open theoretical question that our experiments probe empirically. AI-generated text detection (arXiv:2303.11156, arXiv:2509.18880) addresses binary classification and reaches AUC ~0.85-0.90 for Gen1 text, uniformly treating all AI-generated text as equivalent regardless of generational provenance. Embedding-based representations show intrinsic separability between AI-generated and human text in compressed embedding spaces (arXiv:2408.10437), motivating our use of embedding-space distance features alongside surface-level signals. 'Understanding Transformers via N-gram Statistics' (arXiv:2407.12034, NeurIPS 2024) provides empirical motivation for applying n-gram-derived theoretical predictions to transformer fine-tuning: transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia, suggesting transformer distributional behavior closely approximates n-gram statistics at the local prediction level — supporting our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level, with our experiments constituting a direct empirical test of this generalization. 'Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection' (arXiv:2605.01647, May 2026) introduces the Letter Distribution Score (LD-Score) and establishes a 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space — with the direct implication that within-model generational divergence (Gen1 vs. Gen2 from the same fine-tuned 0.6B model) is smaller still than cross-model AI-AI divergence. This finding validates our architectural choice to prioritize embedding-space features over character-distribution proxies: our mean cosine distance from Gen0 centroid and within-document embedding variance operate in a representation space where cumulative semantic drift — predicted to accumulate monotonically by arXiv:2604.08554's recursive drift-selection framework — may remain detectable even when surface and character-level signals converge. The pre-specified AUC threshold (0.65) and dual null-hypothesis pivot design explicitly account for the scenario where depth discrimination fails at the document level despite embedding-space features. No paper in the contamination detection surveys (arXiv:2502.14425, arXiv:2406.04244) addresses generation depth as a variable. The closest concurrent work — 'Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models' (arXiv:2511.17602, Nov 2025) — asks whether synthetic data overlaps with evaluation benchmarks, not how many generative cycles deep a document is; generational ancestry is orthogonal to benchmark overlap. 'Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training?' (TrainProVe, CVPR 2025, arXiv:2503.09122) achieves >99% accuracy verifying which text-to-image model generated a given image, using model access and generalization error bounds — differentiation is sharp: TrainProVe operates in the image domain and requires model weights access, while our method operates on raw text documents with no model access, enabling upstream corpus-level pre-filtering. Both address data governance but via entirely complementary mechanisms. 'A Closer Look at Model Collapse' (arXiv:2509.16499, NeurIPS 2025 Spotlight) identifies a generalization-to-memorization transition but studies diffusion models and does not distinguish depth levels in training data.\",\n  \"approach\": \"We build a controlled genealogical corpus by running a 2-step recursive train-generate loop with Qwen3-0.6B (the smallest Qwen3 model, chosen to minimize sequential compute cost while still exhibiting measurable distributional drift per generation), producing text with verified depth labels Gen0 (human, sourced from FineWeb-Edu and C4), Gen1, and Gen2, yielding ~200K labeled documents per depth level across diverse domains. All generated documents are hard-capped at 512 tokens maximum length: this cap is enforced at generation time via the `max_new_tokens=512` parameter, making generation time deterministic and reviewable. At 200K documents × 512 tokens = 102M tokens per generational step, batched A100 inference at 3,000–5,000 tok/s for Qwen3-0.6B yields approximately 6–9 GPU hours per step — consistent with the timeline estimate below. The 512-token cap is scientifically defensible for depth discrimination: surface-level signals (surprisal burstiness, lexical diversity, n-gram entropy) and embedding-space signals (mean cosine distance from Gen0 centroid, within-document window embedding variance) are fully computable over 512-token documents, and ordinal regression classifiers trained on short-document depth signals are directly comparable to the binary detectors in arXiv:2502.15654, which also operate on variable-length web documents.\\n\\nWe disable Qwen3-0.6B thinking mode during all generative steps via the hard switch `enable_thinking=False` in `tokenizer.apply_chat_template`, rather than the soft `/no_think` instruction tag — because GitHub discussion QwenLM/Qwen3 #1329 documents that the 0.6B model lacks sufficient instruction-following capacity to reliably honor `/no_think` when placed in the system prompt, and silent failure would inject `&lt;think>…&lt;/think>` reasoning traces into Gen1/Gen2 documents that are absent from Gen0 human text, making depth levels trivially separable by token-level artifacts rather than genuine semantic drift and invalidating the AUC signal. The `enable_thinking=False` hard switch operates at the tokenizer template level and does not depend on the model's instruction-following capacity. As a final post-hoc verification, every generated document is scanned for `&lt;think>` tokens and discarded if any are found, before corpus inclusion.\\n\\nLimiting to Gen0/Gen1/Gen2 compresses the sequential corpus construction bottleneck to approximately 2 wallclock days: Qwen3-0.6B fine-tuning on a 200K-document sample runs in ~4-6 GPU hours on A100, and generation of 200K new 512-token documents runs in ~6-9 GPU hours, for ~12-15 GPU hours per generational step. The hard sequential dependency spans only 2 steps.\\n\\nWe train a DeBERTa-v3-large ordinal regression classifier jointly on raw text and depth-diagnostic features spanning two categories: (a) surface-level signals — per-token surprisal variance (burstiness), lexical diversity decay (MTLD and type-token ratio), and n-gram entropy compression ratio; and (b) embedding-space signals — (i) mean cosine distance of within-document window embeddings from the pre-computed Gen0 centroid (capturing average depth of embedding drift from human text), and (ii) variance of per-window cosine distances from the Gen0 centroid within the document (capturing within-document heterogeneity of embedding drift). Both embedding features are computed from non-overlapping 128-token window embeddings produced by sentence-transformers/all-MiniLM-L6-v2; feature (i) measures central tendency and feature (ii) measures distributional spread — distinct geometric properties: a Gen2 document may exhibit both higher mean distance from Gen0 and more heterogeneous window-level drift than a Gen1 document, as cumulative generational compression produces uneven semantic displacement within a document. We integrate these five scalar depth-diagnostic features by concatenating them to the DeBERTa-v3-large CLS token representation (1024-dim), then training an ordinal regression head over this joint 1029-dim representation; the Gen0 embedding centroid is precomputed offline from a held-out Gen0 reference set of 10K documents using sentence-transformers/all-MiniLM-L6-v2 and is not updated during classifier training.\\n\\nEmbedding-space features are specifically motivated by the 'Wall of Separation' established in arXiv:2605.01647 (May 2026): AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence (Gen1→Gen2 from the same fine-tuned 0.6B model) is smaller still. Surface-level and character-distribution signals are therefore unlikely to reliably discriminate depth levels in this setting; our mean cosine distance from Gen0 centroid and within-document embedding variance instead target cumulative semantic drift that arXiv:2604.08554's recursive drift-selection framework predicts to accumulate monotonically across generations even when character distributions plateau — providing detection signal orthogonal to surface proxies. The argument is: our embedding-space features target cumulative semantic drift that persists even when surface divergence converges, consistent with the monotonic drift predicted by arXiv:2604.08554 — with the explicit caveat that arXiv:2604.08554 derives this prediction for variable-order n-gram agents, not transformer fine-tuning. We hypothesize the generalization holds because transformer next-token distributions closely approximate n-gram statistics at the local prediction level (arXiv:2407.12034, NeurIPS 2024, reports 68–79% agreement between transformer predictions and n-gram rulesets across two corpora), suggesting transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression, for which cumulative drift is expected to accumulate monotonically. Our classifier and collapse experiments directly test whether this hypothesized generalization from n-gram theory to transformer practice holds empirically.\\n\\nCentral technical risk and dual null-hypothesis design: We pre-specify two complementary pre-registered outcome scenarios to ensure a definitive, interpretable empirical finding under all classifier and collapse experiment outcomes. (Primary null) If the ordinal classifier falls below AUC 0.65 on Gen1/Gen2 discrimination, the finding is publishable: depth beyond Gen1 is linguistically indistinguishable at the document level using current text-level and embedding-level methods, implying binary filtering suffices — consistent with the implicit assumption of arXiv:2502.15654. In this case, the collapse validation experiments automatically pivot to directly comparing binary (Gen0-only) filtering against depth-stratified filtering at fixed corpus size. (Secondary null) If the classifier achieves AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between conditions (b) (100K Gen0 + 100K Gen1) and (c) (67K Gen0 + 67K Gen1 + 66K Gen2) at fixed total corpus size (paired t-test, α = 0.05, across 3 random seeds), we report this as a distinct secondary null outcome: depth detection is feasible but equal-fraction Gen2 contamination causes no additional collapse-severity beyond equal-fraction Gen1 contamination at GPT-2 scale — the marginal harm-per-generation curve is flat at this model size, binary filtering is sufficient for practical governance at small scales, and preferential Gen2 removal yields no measurable advantage at this scale. This finding has direct governance implications while leaving open whether depth stratification provides additional value at larger model scales, explicitly reserved as future work. All four logical combinations of (AUC pass/fail) × (collapse severity parity/non-parity) produce pre-specified, interpretable empirical contributions with distinct governance implications.\\n\\nThe trained classifier is applied zero-shot to real FineWeb and C4 slices to estimate depth-distribution statistics of existing pretraining corpora. Collapse validation uses a GPT-2-scale LM fine-tuned on three fixed-total-size depth-composition conditions (200K training documents each), following the controlled-composition standard of Strong Model Collapse (ICLR 2025): (a) Gen0-only: 200K Gen0; (b) Gen0+Gen1: 100K Gen0 + 100K Gen1; (c) Gen0+Gen1+Gen2: 67K Gen0 + 67K Gen1 + 66K Gen2. These corpora are constructed by subsampling from the already-generated 200K-document pools at each depth level, requiring no additional generation compute. Fixing total corpus size at 200K across all three conditions isolates the causal effect of depth composition from dataset volume: any observed collapse severity difference between conditions reflects contamination depth, not training set size — making the central governance claim ('Gen2 contamination is more harmful per document than Gen1 at equal contamination rate') empirically defensible. Collapse severity is tracked via held-out human-text perplexity and output tail entropy across multiple recursive training generations, explicitly scoped to measuring *severity as a function of depth composition at fixed scale* rather than collapse prevention — consistent with Strong Model Collapse's any-fraction harm finding. GenDepth-Bench is scoped to 2 model families: Qwen3-0.6B (primary) and Llama-3.2-1B (secondary, run through the same recursive loop to test cross-model generalizability of depth signals, explicitly optional — executed only if compute budget permits; see resource estimate). Coverage of 5+ model families is explicitly reserved as future work.\\n\\n16-Day Critical Path (EMNLP 2026 ARR deadline May 25, 2026; today May 9, 2026):\\n— Days 1-2: Environment setup; sample 200K Gen0 docs from FineWeb-Edu/C4 (truncated to 512 tokens); prepare evaluation suite and draft intro/related-work sections.\\n— Days 2-3 (sequential bottleneck step 1): Fine-tune Qwen3-0.6B on Gen0 (~4-6h GPU); generate 200K Gen1 documents at max 512 tokens each (~6-9h GPU; 200K × 512 tokens = 102M tokens ÷ 3,000–5,000 tok/s ≈ 6–9h) with `enable_thinking=False` hard switch and post-hoc `&lt;think>` token scan.\\n— Days 3-4 (sequential bottleneck step 2): Fine-tune Qwen3-0.6B-v2 on Gen1 (~4-6h GPU); generate 200K Gen2 documents at max 512 tokens each (~6-9h GPU) with same thinking-mode controls.\\n— Days 3-8 (PARALLEL TRACK A): DeBERTa-v3-large ordinal training begins with Gen0+Gen1 data at Day 3; adds Gen2 data when available at Day 5; ablations over surface vs. embedding feature subsets.\\n— Days 5-10 (PARALLEL TRACK B): GPT-2-scale collapse experiments begin at Day 5 with fixed-size conditions (a) Gen0-only: 200K Gen0 and (b) Gen0+Gen1: 100K Gen0+100K Gen1 (subsampled from existing pools); add condition (c) Gen0+Gen1+Gen2: 67K each at Day 6 when Gen2 corpus is available. Llama-3.2-1B recursive corpus generation runs in parallel if compute budget is below 160h H100-equivalent at Day 5.\\n— Days 7-9: Full classifier evaluation; if Gen1/Gen2 AUC < 0.65, activate primary null-hypothesis binary filtering comparison experiments; if AUC ≥ 0.65 but collapse severity parity detected between conditions (b) and (c), record secondary null outcome and report governance implications.\\n— Days 9-10: Zero-shot depth scoring on real FineWeb/C4 slices.\\n— Days 10-12: Feature importance ablations; cross-model generalizability check on Llama-3.2-1B-generated corpus (if optional Llama recursive corpus was generated).\\n— Days 12-16: Analysis, writing, revision, and submission.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~210h A100 (40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B, each step generating 200K documents at 512 tokens max = 102M tokens ÷ ~3,500 tok/s average ≈ ~8h per step, ×2 steps = ~16h generation + ~24h fine-tuning over 2 steps + 50h DeBERTa-v3-large fine-tuning and ablations + 120h GPT-2-scale collapse validation experiments across 3 fixed-size depth-composition conditions)\",\n      \"gpu_utilization\": \"High idle rate (~40-60%): GPU waits while researcher designs experiment configs, interprets collapse curves, debugs depth signal quality, and writes between each stage over several months\",\n      \"timeline\": \"4-6 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$370 at $1.75/h blended A100 average (RunPod ~$1.49/h, Lambda ~$2.06/h); approximately 70 H100-equivalent hours\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~320h A100 (agent handles training loop queuing and ablation scheduling; human approves depth-feature selection, collapse experiment design, AUC threshold decision for null-hypothesis activation, and Llama-3.2-1B second-family validation)\",\n      \"gpu_utilization\": \"Moderate idle rate (~15-25%): agent queues overnight runs and fills GPU gaps between sequential generational steps; handles parallel DeBERTa and collapse experiment scheduling\",\n      \"timeline\": \"6-10 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$60-120 (~600-800 agent turns at $0.08-0.15/turn for experiment design, result interpretation, and iteration guidance)\",\n      \"estimated_gpu_cost\": \"~$560 at $1.75/h average A100; approximately 107 H100-equivalent hours\",\n      \"risk_note\": \"Key bottleneck: 2-step sequential corpus construction (train on GenN → generate GenN+1 at 512 tokens max → train again) cannot be parallelized; each step adds ~1 wallclock day with Qwen3-0.6B. The 512-token document cap makes generation time deterministic: 200K × 512 tokens = 102M tokens ÷ 3,000–5,000 tok/s ≈ 6–9h per step, matching the timeline estimate and eliminating schedule uncertainty from variable document lengths. Corpus construction for collapse experiments uses fixed-total-size subsampling (200K per condition) from the already-generated per-depth pools — no additional generation compute required. Pre-specified dual null-hypothesis design (primary: AUC < 0.65; secondary: AUC ≥ 0.65 but collapse severity parity between fixed-size conditions (b) and (c)) means the agent has clear decision rules without requiring researcher judgment to pivot, covering all four logical outcome combinations.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~490h A100 / ~163h H100-equivalent hours (mandatory, within ≤200h hard constraint): 40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B (200K documents × 512 tokens max per step = 102M tokens; at 3,000–5,000 tok/s ≈ 6–9h generation per step, ×2 steps; plus ~12h fine-tuning per step = ~40h total) + 120h DeBERTa-v3-large fine-tuning and ablations with 2x hyperparameter search across depth-feature combinations (surface-only, embedding-only, combined) + 240h GPT-2-scale collapse validation experiments across 3 fixed-total-size depth-composition conditions (Qwen3-0.6B family) with 3 collapse metrics + 90h auxiliary ablations (feature importance, zero-shot FineWeb/C4 scoring, null-hypothesis binary filtering comparison if AUC threshold triggered). Llama-3.2-1B recursive corpus generation and collapse experiments (~60-90h A100 / ~20-30h H100-equivalent) are explicitly optional from the start: executed only if compute budget remains below 160h H100-equivalent at Day 10; otherwise deprioritized to zero-shot depth scoring only, maintaining a genuine 40h safety buffer against the 200h hard ceiling.\",\n      \"gpu_utilization\": \"Near-zero idle (<5%): agent queues hyperparameter sweeps and ablations 24/7, filling GPU cycles between sequential generational construction steps with parallel auxiliary experiments\",\n      \"timeline\": \"13-16 days with 4-6 concurrent A100s\",\n      \"team\": \"0 (4-6h one-time setup: genealogical corpus schema with 512-token document cap, experiment grid, AUC threshold 0.65 for primary null-hypothesis activation, paired t-test criterion for secondary null-hypothesis activation between fixed-size conditions (b) and (c), stopping conditions)\",\n      \"claude_api_cost\": \"$250-400 (~2500-3000 agent turns for experiment orchestration, result analysis, and adaptive exploration)\",\n      \"estimated_gpu_cost\": \"~$856 at $1.75/h average A100 (mandatory only); ~$960 including optional Llama-3.2-1B corpus if budget permits\",\n      \"speed_bottleneck\": \"2-step sequential corpus construction is the hard wallclock floor; the 512-token document cap makes per-step generation time deterministic at ~6-9h (102M tokens ÷ 3,000–5,000 tok/s), eliminating schedule uncertainty; GPU count limits simultaneous ablation breadth during non-sequential phases\",\n      \"risk_note\": \"Corpus construction for collapse experiments uses fixed-total-size subsampling (200K per condition from already-generated per-depth pools) — no additional generation compute. Depth signal may be weak between Gen1 and Gen2 from the same small model — a risk compounded by the 'Wall of Separation' finding (arXiv:2605.01647): AI-AI surface divergence is substantially smaller than human-AI divergence, making within-model generational discrimination harder still. Pre-specified dual null-hypothesis design covers all outcomes: primary null (AUC < 0.65) redirects to binary filtering comparison at fixed corpus size; secondary null (AUC ≥ 0.65 but collapse severity parity between fixed-size conditions (b) and (c)) reports depth detection as feasible but equal-fraction Gen2 contamination as causing no incremental governance harm beyond Gen1 at GPT-2 scale. Embedding-space features (mean cosine distance from Gen0 centroid and within-document embedding variance over 128-token windows) partially mitigate the primary null risk by targeting cumulative semantic drift invisible at the surface level. Budget contingency: Llama-3.2-1B recursive corpus generation is explicitly optional from the start; if compute approaches 160h H100-equivalent during execution, Llama-3.2-1B recursive corpus is deprioritized to zero-shot depth scoring only (no new collapse experiments), saving ~60-90h A100 (~20-30h H100-equivalent) and maintaining a genuine 40h buffer against the 200h hard ceiling.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; special theme 'New Missions for NLP Research' explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance' — near-perfect topical alignment; conference October 24-29, Budapest)\",\n    \"NAACL 2027 (ARR cycle deadline TBD, expected ~late 2026; safe backup with more time for thorough collapse validation experiments and additional model families)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"AI models collapse when trained on recursively generated data (Nature 2024)\",\n    \"Strong Model Collapse (ICLR 2025) — establishes collapse at any non-vanishing synthetic fraction (~1% example); holds total corpus size fixed while varying synthetic fraction (the controlled design our collapse experiments follow); does not distinguish Gen1 from Gen2 synthetic data; this gap is what we fill\",\n    \"Machine-generated text detection prevents language model collapse (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025) — closest upstream prior work: trains binary encoder-only classifiers (evaluating RoBERTa, DeBERTa-v3, ModernBERT) with importance resampling — weights ∝ (1-q(x))^b — to prevent collapse at GPT-2/SmolLM2 scale (124M–1.7B parameters); treats all AI-generated text equivalently without generational depth distinction; our work directly extends this: if depth-stratified resampling weights yield greater collapse-severity reduction per decontamination unit than binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over binary resampling under budget constraints; if not (AUC < 0.65 or collapse severity parity between fixed-size conditions (b) and (c)), our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant\",\n    \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources (arXiv:2602.10531, February 2026) — analyzes the statistical dynamics of iterative training on contaminated data using a mixture-model framework, showing that improvement over collapsed models is possible when sufficient fresh real data is present; does not assign generational depth labels to documents or propose a depth-stratified filtering method\",\n    \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (arXiv:2404.01413)\",\n    \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (arXiv:2510.16657)\",\n    \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Models (arXiv:2509.08972) — training-side collapse prevention via Truncated Cross-Entropy loss; orthogonal to our upstream corpus-level depth detection; does not classify documents by generational depth\",\n    \"Drift and Selection in LLM Text Ecosystems (arXiv:2604.08554) — mathematical framework for how recursive publication compresses text through drift and selection; derived for variable-order n-gram agents (not transformer fine-tuning); does not propose a depth classifier or detection method; motivates our prediction that embedding-space drift accumulates monotonically across generations even when surface distributions plateau, under the hypothesis that transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression — a generalization our experiments directly test\",\n    \"Understanding Transformers via N-gram Statistics (arXiv:2407.12034, NeurIPS 2024) — transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia; provides empirical grounding for our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level\",\n    \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (arXiv:2605.01647, May 2026) — establishes 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space; within-model generational gap (Gen1→Gen2 from same fine-tuned model) is smaller still; directly threatens surface-level discriminability; our counter-argument: embedding-space features (mean cosine distance from Gen0 centroid and within-document window embedding variance, computed over non-overlapping 128-token windows via sentence-transformers/all-MiniLM-L6-v2) target cumulative semantic drift orthogonal to character-distribution signals; the pre-specified dual null-hypothesis design accounts for the possibility that depth discrimination fails despite embedding-space features\",\n    \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective (NeurIPS 2025 Spotlight)\",\n    \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (ACL 2024)\",\n    \"Can AI-Generated Text be Reliably Detected? (arXiv:2303.11156)\",\n    \"Diversity Boosts AI-Generated Text Detection (arXiv:2509.18880)\",\n    \"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models (arXiv:2511.17602) — asks whether synthetic data overlaps with evaluation benchmarks; generational ancestry is orthogonal to benchmark overlap\",\n    \"Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training? (TrainProVe, CVPR 2025, arXiv:2503.09122) — achieves >99% accuracy in image domain using model access and generalization error bounds; differentiation: our method operates on raw text with no model access, enabling upstream corpus-level pre-filtering; different modality and mechanism address the same governance goal\",\n    \"Understanding Generative AI Content with Embedding Models (arXiv:2408.10437) — demonstrates intrinsic separability of AI-generated and human text in compressed embedding space; motivates our use of embedding-space cosine distance and within-document variance features for depth discrimination beyond surface-level signals\",\n    \"Benchmark Data Contamination of Large Language Models: A Survey (arXiv:2406.04244)\",\n    \"A Survey on Data Contamination for Large Language Models (arXiv:2502.14425)\"\n  ],\n  \"description\": \"As web corpora become saturated with AI-generated content (74.2% of new web pages contain some AI text by April 2025, of which 2.5% are fully AI-generated and 71.7% are human-AI blends; Ahrefs, 900K pages), complete decontamination is operationally infeasible, shifting the question to: which synthetic documents cause the most harm and should be removed first? We propose Genealogical Depth Scoring, a method extending binary AI-text detection to ordinal depth classification (Gen0=human, Gen1, Gen2), trained on a controlled corpus produced by 2-step recursive train-generate loops using Qwen3-0.6B with thinking mode disabled via the hard switch `enable_thinking=False` in `tokenizer.apply_chat_template` — rather than the soft `/no_think` instruction tag, which silently fails for the 0.6B model when placed in the system prompt (GitHub QwenLM/Qwen3 discussion #1329) and would introduce `&lt;think>…&lt;/think>` artifacts that make depth levels trivially separable by token-level signals rather than genuine semantic drift — with post-hoc discard of any documents containing `&lt;think>` tokens before corpus inclusion. All generated documents are hard-capped at 512 tokens via `max_new_tokens=512`, yielding 200K × 512 tokens = 102M tokens per generational step; at 3,000–5,000 tok/s for Qwen3-0.6B on A100 this takes approximately 6–9 GPU hours per step, making the generation timeline deterministic and anchored to a verifiable arithmetic bound. The classifier combines DeBERTa-v3-large fine-tuning with two classes of depth-diagnostic features: surface-level signals (surprisal burstiness, lexical diversity decay, n-gram entropy compression ratio) and embedding-space signals — (i) mean cosine distance of within-document window embeddings from the Gen0 centroid, and (ii) variance of per-window cosine distances from the Gen0 centroid within the document, both computed over non-overlapping 128-token windows via sentence-transformers/all-MiniLM-L6-v2. Feature (i) captures average drift from human text in embedding space; feature (ii) captures within-document heterogeneity of that drift — distinct geometric properties (central tendency vs. distributional spread) that together characterize the document's depth signature. These five scalar features are concatenated to the DeBERTa-v3-large CLS token representation (1024-dim) and passed to an ordinal regression head trained over the joint 1029-dim representation; the Gen0 centroid is precomputed offline and not updated during training. The embedding-space features directly address the 'Wall of Separation' documented in arXiv:2605.01647 (May 2026) — AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence is smaller still — by targeting cumulative semantic drift that arXiv:2604.08554 predicts to accumulate monotonically across recursive generations even when surface statistics plateau. Because arXiv:2604.08554 derives this prediction for variable-order n-gram agents rather than transformer fine-tuning, we ground the generalization in arXiv:2407.12034 (NeurIPS 2024), which shows transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions, and treat our classifier and collapse experiments as a direct empirical test of whether this theoretical extension holds. We pre-specify a dual null-hypothesis design: (primary null) if Gen1/Gen2 AUC < 0.65, depth is linguistically indistinguishable and binary filtering suffices; (secondary null) if AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between fixed-size conditions (b) (100K Gen0 + 100K Gen1) and (c) (67K Gen0 + 67K Gen1 + 66K Gen2), equal-fraction Gen2 contamination causes no additional collapse-severity beyond equal-fraction Gen1 contamination at GPT-2 scale — depth detection is feasible but depth-stratified filtering provides no incremental governance benefit at small model scale. All four logical outcomes produce pre-specified, interpretable empirical contributions. Collapse validation compares three fixed-total-size depth-composition conditions (200K documents each: (a) Gen0-only; (b) 100K Gen0+100K Gen1; (c) 67K Gen0+67K Gen1+66K Gen2), constructed by subsampling from the already-generated 200K-document pools at each depth level — no additional generation compute. Fixing total corpus size across all conditions isolates the causal effect of depth composition from dataset volume, making the central governance claim ('Gen2 contamination is more harmful per document than Gen1 at equal contamination rate, supporting preferential Gen2 removal per filtering unit') empirically defensible. Results are framed as *collapse severity as a function of contamination depth composition at fixed scale*, directly informing the real-world budget-constrained decontamination problem. TrainProVe (CVPR 2025) addresses related governance goals via model access in the image domain; ForTIFAI (arXiv:2509.08972) prevents collapse at training time via modified loss; arXiv:2502.15654 (Feb 2025) prevents collapse via binary detection with importance resampling but treats all AI text equivalently without generational depth distinction; arXiv:2602.10531 (Feb 2026) analyzes collapse dynamics statistically via mixture models but does not classify text by generational depth — our work is the first to assign generational depth scores to raw text corpus documents upstream of training, and directly tests whether depth-stratified resampling yields greater collapse-severity reduction per filtering unit than binary resampling. We release GenDepth-Bench covering 2 model families (Qwen3-0.6B primary; Llama-3.2-1B secondary, optional pending compute budget), with 5+ family coverage as explicit future work. Targets EMNLP 2026's special theme on synthetic data feedback loops and data governance.\",\n  \"project_name\": \"gen_depth_decontam\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"FACTUAL ERROR — Model name: 'Qwen3.5-0.5B' does not exist. The smallest Qwen3.5 is 0.8B; the smallest Qwen3 is 0.6B. Must be corrected to Qwen3-0.6B or Qwen3.5-0.8B before any experimental planning.\", \"HARD CONSTRAINT VIOLATION — Auto Research compute estimate (~800 A100h ≈ 267 H100h) exceeds the user's explicitly stated ≤200 H100-hour hard constraint. Manual (~75 H100h) and HIL (~117 H100h) are within budget; auto research must be rescoped or noted as out-of-bounds.\", \"TIMELINE INFEASIBILITY — Sequential corpus construction requires 3–5 days per generational step × 3 steps = 9–15 days minimum, leaving ≤1–7 days for DeBERTa training, collapse validation experiments, and writeup within the 16-day hard deadline. Even the 'auto' mode estimate of '2–4 weeks' exceeds 16 days. The submission timeline is not credible unless the generation chain is compressed to ≤2 days/step with very small models.\", \"CORE HYPOTHESIS LOGIC GAP — Strong Model Collapse (ICLR 2025) establishes that even 0.1% synthetic data fraction triggers collapse. If this threshold holds, then the relevant intervention is removing ALL synthetic data, not tiered removal that tolerates Gen1. The proposal must explicitly argue why tiered filtering is sufficient given this finding, or reframe its claim to 'among contaminated corpora, depth-stratified decontamination is superior to binary decontamination.'\", \"CENTRAL TECHNICAL RISK UNADDRESSED — The classifier must distinguish Gen2 text from Gen1 text generated by the same small model (Qwen3-0.6B). After one generation of fine-tuning on a small corpus, the model changes only marginally — the distributional gap between its Gen1 and Gen2 outputs may be smaller than inter-domain variation within Gen0, making reliable ordinal classification impossible. No preliminary evidence, theoretical bound, or pilot experiment is offered to support the plausibility of this distinguishability.\", \"MISSING RELATED WORK — 'Training Data Provenance Verification: Did Your Model Use Synthetic Data' (CVPR 2025) achieves >99% accuracy determining synthetic vs. real training provenance from model behavior and embeddings. This is not the same as text-level depth scoring, but must be cited and explicitly differentiated since it addresses the same governance goal via a complementary mechanism.\", \"BENCHMARK SCOPE OVERCLAIM — GenDepth-Bench promises '5+ model families' but the experiment design uses a single small model (Qwen3-0.6B) for corpus construction. Covering 5+ model families requires each family to run its own recursive train-generate loop, multiplying the sequential compute requirement 5x and breaking the budget and timeline constraints further.\"]\nFeedback: The core concept (generational depth scoring for corpus decontamination) is genuinely novel and worth pursuing, but the proposal has execution-level failures that need resolution before submission. Priority fixes: (1) Replace 'Qwen3.5-0.5B' with 'Qwen3-0.6B' throughout. (2) Cap Auto Research at ≤600 A100h and revise the estimate to stay within 200 H100-hours. (3) The 16-day timeline requires compressing the sequential chain: use a single model family (Qwen3-0.6B), limit to Gen0/Gen1/Gen2 (2 recursive steps = ~4–6 days), run DeBERTa and collapse experiments in parallel during gap days. Make this explicit in the timeline with a day-by-day critical path. (4) Add a null-hypothesis section: 'If the ordinal classifier fails (Gen1/Gen2 AUC < 0.65), we test whether binary filtering (Gen0-only) outperforms depth-stratified filtering as the baseline intervention, directly testing the hypothesis from Strong Model Collapse.' This converts the central technical risk into a publishable empirical finding regardless of outcome. (5) Cut the GenDepth-Bench scope to 2–3 model families max (achievable within budget) and reserve '5+ families' as future work. (6) Add the CVPR 2025 provenance verification paper and differentiate: your method acts on raw text without model access, while provenance verification requires access to model weights — this is the right framing to distinguish the contributions.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MISSING CITATION — arXiv:2605.01647 ('Beyond Perplexity: Character Distribution Signatures,' May 2026): This paper independently demonstrates a 'Wall of Separation' where AI-AI divergence is significantly smaller than human-AI divergence. Because Gen1 and Gen2 are outputs of the *same* 0.6B model differing by one fine-tuning step, the within-model generational gap is smaller still than cross-model AI-AI divergence. This directly threatens the discriminability hypothesis and must be cited and addressed. The argument should be: cumulative semantic drift in embedding space may still be detectable even when surface statistics converge — but this requires acknowledgment and a direct counter-argument, not silence.\", \"LOGICAL FRAMING GAP — Partial filtering under Strong Model Collapse: Strong Model Collapse (ICLR 2025) establishes collapse at *any non-vanishing* synthetic fraction (~1/1000). After depth-stratified filtering that removes Gen2 but retains Gen1, the corpus still contains a non-vanishing synthetic fraction — which, by the same theory, should still trigger collapse. The proposal must explicitly distinguish between: (a) depth-stratified filtering *reducing collapse severity or delaying onset* even without eliminating it, and (b) the more ambitious but unsupported claim that it prevents collapse. The current framing conflates these and needs to be sharpened to 'severity reduction per filtering budget' rather than 'collapse prevention.'\", \"AUTO RESEARCH TIMELINE INCONSISTENCY — The 16-day critical path is laid out explicitly (Days 1-16), but the auto research resource estimate states '2-3 weeks with 4-6 concurrent A100s.' The upper bound (3 weeks = 21 days) overshoots the deadline. This should read '13-16 days with 4-6 concurrent A100s' based on the critical path arithmetic (550h / 4 GPUs = 137.5h ≈ 5.7 compute-days + 2-day sequential bottleneck + ~4 days writing/analysis).\", \"74% STATISTIC PRECISION — The Ahrefs study (verified: 900K pages, April 2025) found 74.2% of new pages contain *some* AI content, but only 2.5% are fully AI-generated; the remaining 72% are human-AI blends. The proposal's phrasing ('74% of newly created web pages contained AI-generated text') is technically accurate but implies raw AI-generated contamination at 74% scale. This should be clarified — notably, human-AI blends (Gen0.5, partially edited) may sit between Gen0 and Gen1 in depth, which is actually *interesting* for the depth scoring framework and worth noting explicitly.\", \"COMPUTE BUFFER TOO THIN — Auto research at 550h A100 / 183h H100-equivalent leaves only 17 H100-hours of buffer against the 200h hard constraint. If any of the collapse validation experiments (estimated 300h A100 for 6 conditions) requires a single re-run due to training instability, hyperparameter error, or data pipeline failure, the budget is exceeded. The proposal should either (a) specify which experiments are cut if budget is approached, or (b) identify a fallback scope reduction (e.g., drop the Llama-3.2-1B second-family validation to save ~90h).\"]\nFeedback: All five Round 1 issues are resolved. The proposal is substantially improved and the core idea is verified as novel — no competing work on generational depth scoring found across extensive search. Three targeted fixes will raise this to pass: (1) Cite arXiv:2605.01647 and address its implication directly: 'Our embedding-space features target cumulative semantic drift that persists even when surface divergence converges, consistent with the monotonic drift predicted by arXiv:2604.08554' — this is already your argument, just make it explicit against this specific paper. (2) Reframe the partial filtering value: add one sentence explicitly stating 'even under Strong Model Collapse's any-fraction harm finding, depth-stratified filtering reduces expected collapse severity for a fixed decontamination budget by prioritizing highest-harm documents first — a practical governance claim that holds even if perfect decontamination is required for complete collapse prevention.' (3) Fix the auto research timeline to '13-16 days' and add a budget contingency: state that if compute approaches 180h H100-equivalent, the Llama-3.2-1B recursive corpus generation is deprioritized to the zero-shot scoring phase only (no new collapse experiments), saving ~60-90h A100. These three fixes address the only remaining material gaps; the null-hypothesis design, the 16-day critical path, the TrainProVe differentiation, and the GenDepth-Bench scoping are all solid.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"SECONDARY NULL HYPOTHESIS MISSING — The preregistered null-hypothesis design covers one failure mode (Gen1/Gen2 AUC < 0.65 → pivot to binary filtering comparison), but does not pre-specify what is reported if the classifier SUCCEEDS (AUC ≥ 0.65) but the collapse experiments show EQUAL held-out perplexity for Gen0+Gen1 vs Gen0+Gen1+Gen2 corpora. This scenario — 'we can detect depth labels but depth does not predict marginal collapse severity at GPT-2 scale' — is a coherent empirical finding but is currently absent from the design. Without it, reviewers can fault the paper for not pre-committing to how this outcome is interpreted. One or two sentences explicitly naming this secondary null and its interpretation ('depth detection is feasible but depth-stratified filtering provides no incremental benefit over binary filtering at this scale, suggesting the harm-per-generation curve is flat') would close the gap.\", \"MODELING GAP IN EMBEDDING DRIFT ARGUMENT — The monotonic embedding drift prediction cited from arXiv:2604.08554 is derived for variable-order n-gram agents, not for transformer fine-tuning. The proposal applies this theoretical prediction to one fine-tuning step of a 0.6B transformer on 200K documents, which is a substantive analogy not directly supported by that framework. While the empirical design will test this claim, the theoretical motivation should acknowledge the modeling gap (e.g., 'arXiv:2604.08554 establishes monotonic drift for n-gram agents; we hypothesize this generalizes to transformer fine-tuning based on [brief argument], which our experiment directly tests'). Without this acknowledgment, a reviewer may flag the theoretical foundation as overclaimed.\"]\nFeedback: Both remaining issues are fixable with two targeted additions: (1) Add one paragraph (or a row in the null-hypothesis table if one exists) that explicitly pre-specifies the 'classifier succeeds, collapse severity parity' scenario as a secondary null outcome and states what that finding means for practical governance (binary filtering is sufficient; depth stratification provides no incremental value at GPT-2 scale). This completes the preregistered design and removes a reviewer attack surface. (2) In the approach section, add one sentence acknowledging that arXiv:2604.08554's drift framework is derived for n-gram agents and that you are testing whether the monotonic drift prediction extends to transformer fine-tuning — framing your collapse and classifier experiments as a direct empirical test of this generalization. These two additions require no new experiments and can be drafted in under an hour. The core novelty, verified references, budget/timeline credibility, and venue alignment are all solid.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MISSING CITATION — arXiv:2502.15654 'Machine-generated text detection prevents language model collapse' (Drayson, Yilmaz, Lampos; UCL, Feb 2025) is the most directly adjacent prior work: it trains a binary DeBERTa-v3 classifier to distinguish human vs AI text, applies importance resampling to up-weight human content during recursive training, and demonstrates collapse prevention at GPT-2/SmolLM2 scale. This paper is not cited anywhere in the proposal. A reviewer will immediately flag this omission since it directly addresses the same problem (AI text detection to prevent collapse). The differentiation is clear — 2502.15654 uses binary detection and does not distinguish generational depth; the proposed method extends this to ordinal depth scoring enabling tiered filtering — but it must be cited and explicitly differentiated.\", \"COMPUTE MARGIN TOO THIN — Auto research at ~183 H100h equivalent leaves only 17h of buffer against the 200h hard constraint. The contingency trigger at 180h H100-equivalent is well-specified (drop Llama-3.2-1B recursive corpus to zero-shot only), but this saves 20-30h H100-equivalent — meaning the contingency must activate before the budget is exceeded by more than ~3h. Any single failed training run or unexpected GPU contention during the sequential corpus construction bottleneck (Days 2-4) could push total usage past 200h. The proposal should either (a) declare the Llama-3.2-1B recursive corpus as optional from the start with the contingency trigger moved earlier (e.g., at 160h), or (b) estimate auto research at a slightly lower total.\"]\nFeedback: Both Round 3 issues are properly resolved — the secondary null hypothesis (AUC ≥ 0.65 but collapse severity parity) is now explicitly preregistered with a paired t-test criterion and governance interpretation, and the n-gram-to-transformer modeling gap is acknowledged with the NeurIPS 2024 grounding. Two targeted fixes will bring this to pass: (1) Add arXiv:2502.15654 to the landscape and key_references sections. The differentiation sentence writes itself: 'The closest upstream related work (arXiv:2502.15654, Feb 2025) shows that binary AI-text detection via DeBERTa-v3 with importance resampling prevents collapse at GPT-2/SmolLM2 scale, but treats all AI-generated text equivalently regardless of generational depth — leaving open whether depth stratification enables more efficient decontamination per filtering unit, which is the specific question we answer.' (2) Move the Llama-3.2-1B recursive corpus to explicitly optional from the start in auto_research, and set the contingency activation threshold at 160h H100-equivalent rather than 180h, creating a more credible 40h safety margin. These two changes require no new experiments.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MAUVE-STYLE FEATURE ILL-DEFINED AT DOCUMENT LEVEL — MAUVE is a corpus-level metric that estimates KL divergence between two distributions of text embeddings. It requires multiple samples per distribution, not a single document. Applying it as a per-document feature is non-standard and potentially meaningless. The proposal lists 'MAUVE-style distributional divergence' as a depth-diagnostic feature without explaining the per-document operationalization. If this feature simply becomes 'distance of document embedding from Gen0 distribution,' it overlaps substantially with the 'cosine distance from Gen0 centroid' feature already listed. A reviewer will immediately flag this as either technically ill-defined or redundant. Fix: either (a) specify the document-level operationalization explicitly (e.g., 'we compute the negative log-likelihood of a document's embedding under a KDE fit to the Gen0 embedding distribution' or 'we compute the mean embedding of non-overlapping 128-token windows within the document and measure the MAUVE divergence of this within-document distribution from the Gen0 reference distribution'), or (b) rename this feature to accurately reflect what is computed and explain how it differs from the cosine centroid distance.\", \"DEBERTA + HAND-CRAFTED FEATURE INTEGRATION UNSPECIFIED — The approach says the classifier trains 'jointly on raw text and depth-diagnostic features' combining DeBERTa-v3-large with five engineered features from two different representation spaces (surface-level and sentence-transformer embedding space). No architecture is described. Given that DeBERTa produces its own CLS embedding and the sentence-transformer produces a separate embedding vector for the cosine distance computation, the proposal is operating with at least two separate text encoders plus scalar features. How these are merged is entirely unspecified. This is a critical methods gap that affects replicability. Fix: add two sentences specifying the integration architecture (e.g., 'we concatenate the five scalar depth-diagnostic features to the DeBERTa CLS token representation, then train an ordinal regression head over this joint representation; the Gen0 centroid used for cosine distance is computed offline from sentence-transformers/all-MiniLM-L6-v2 embeddings and is not jointly trained').\", \"QWEN3-0.6B THINKING MODE UNSPECIFIED — Qwen3-0.6B supports an explicit thinking mode that generates chain-of-thought reasoning traces within &lt;think>...&lt;/think> tags, which would dramatically alter the character distribution, lexical properties, and statistical footprint of generated text. Whether thinking mode is enabled or disabled during the recursive generation loop must be specified, as it affects: (a) the plausibility of depth signals (thinking traces may be trivially distinguishable), (b) the validity of the Wall of Separation counter-argument (thinking traces produce very different distributions than standard generation), and (c) the external validity of results to real-world web contamination scenarios where thinking traces are absent. This is a one-sentence fix: 'We disable Qwen3-0.6B thinking mode (/no_think) during all generative steps to ensure output text matches real-world web document distributions.'\"]\nFeedback: Three targeted fixes are needed — none require new experiments. (1) MAUVE feature clarification: replace 'MAUVE-style distributional divergence' with a concrete document-level operationalization. The most defensible adaptation is to segment each document into non-overlapping 128-token windows, embed each window via sentence-transformers, and compute the MAUVE divergence between this within-document embedding distribution and the Gen0 reference distribution — this is genuinely distinct from cosine centroid distance as it captures within-document distributional spread, not just central tendency. If this is too complex to implement reliably in 16 days, drop the MAUVE feature and replace it with the variance of within-document embeddings around the Gen0 centroid (a simpler proxy capturing the same distributional geometry idea). (2) DeBERTa integration architecture: add two sentences to the approach specifying that the five scalar features are concatenated to the DeBERTa CLS token, and that the Gen0 centroid is precomputed offline using sentence-transformers and not jointly fine-tuned — this closes the replicability gap without changing the experimental design. (3) Thinking mode: add one sentence specifying that Qwen3 thinking mode is disabled during generation. These three additions require less than an hour of writing and will prevent round-six reviewer rejection on technical specificity grounds.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"EXECUTION RISK — Qwen3-0.6B /no_think system-prompt unreliability: GitHub discussion #1329 documents that Qwen3-0.6B 'lacks sufficient capacity to reliably follow instructions' and /no_think placed in the system prompt silently fails for this specific model size. If thinking mode activates during generation, output text contains &lt;think>...&lt;/think> reasoning traces absent from Gen0 human web text, making Gen1/Gen2 text trivially distinguishable by token-level artifacts rather than genuine semantic drift — inflating AUC and completely invalidating the experimental signal. The current proposal says only 'We disable Qwen3-0.6B thinking mode (/no_think) during all generative steps' without specifying that /no_think must be placed in each user message (not the system prompt). Fix: add one sentence specifying placement — 'We add /no_think to each user message (not the system prompt) during all generative steps, consistent with the workaround documented for Qwen3-0.6B's limited instruction-following capacity at this scale (GitHub QwenLM/Qwen3 discussion #1329).' Alternatively, use the intalio/Qwen3-NoThink-0.6b HuggingFace variant which has thinking mode disabled by default.\", \"METHODOLOGICAL CONFOUND — Corpus size differs across collapse experiment conditions: the three filtering conditions (Gen0-only ≈ 200K documents, Gen0+Gen1 ≈ 400K, Gen0+Gen1+Gen2 ≈ 600K) differ 3× in total training corpus size. Controlled model collapse research (Strong Model Collapse ICLR 2025, arXiv:2404.01413) varies the synthetic fraction while holding total dataset size fixed. Without this control, lower collapse severity in the Gen0-only condition could reflect training data volume effects (smaller dataset → different generalization regime) rather than depth-stratified filtering benefits, directly undermining the central 'severity reduction per filtering budget' governance claim. Fix option A (preferred): run all three conditions on fixed total corpus size (e.g., 200K documents each), varying only Gen0/Gen1/Gen2 composition proportions (e.g., 200K Gen0 vs. 100K Gen0+100K Gen1 vs. 67K Gen0+67K Gen1+66K Gen2). Fix option B (lightweight): explicitly acknowledge the confound as a limitation and reframe the comparison as 'effect of contamination composition on collapse severity' rather than 'severity reduction per filtering budget' — this weakens the governance claim but makes it empirically defensible within 16 days.\"]\nFeedback: The proposal has progressively addressed all five Round 5 issues cleanly. Two new issues require targeted fixes before this can pass. (1) Qwen3-0.6B /no_think placement: add one sentence specifying that /no_think is added to each individual user message (not the system prompt), citing GitHub discussion #1329. This is a one-line fix. Alternatively, switch to intalio/Qwen3-NoThink-0.6b which has thinking mode disabled by default and avoids the placement ambiguity entirely — worth specifying as the primary model choice. (2) Corpus size confound: this is the more significant issue. The cleanest fix within budget is to run all three collapse conditions on the same total corpus size (200K documents each), varying only the Gen0/Gen1/Gen2 mix. This requires no additional generation but does require rerunning collapse experiments on rebalanced corpora — feasible within Days 5-10 if the generation schedule completes on time. If the rebalanced design is too costly, explicitly reframe the comparison: replace 'severity reduction per filtering budget' with 'severity as a function of contamination composition depth' and acknowledge that corpus size varies across conditions as a limitation. The rebalanced design is strongly preferred because the current governance framing ('prioritize Gen2 removal to maximize collapse mitigation per filtering unit') cannot be supported by size-confounded experiments.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"TIMELINE RISK — Document length unspecified in generation estimates: The '6-8 GPU hours to generate 200K documents with Qwen3-0.6B' claim is unanchored to a document length. FineWeb-Edu/C4 documents commonly run 500-2000 tokens; at 1000 tokens × 200K docs = 200M tokens, batched A100 inference at 3000-5000 tok/s for Qwen3-0.6B yields 11-18 hours per generational step — not 6-8 hours. Over 2 sequential steps this adds 6-20 hours to the critical path, potentially cascading into a 2-3 day delay and threatening the May 25 deadline. Fix: explicitly commit to truncating/capping generated documents at 512 tokens maximum length, which (a) brings generation time within the estimate (200K × 512 tokens = 102M tokens ÷ 3000-5000 tok/s ≈ 6-9h), (b) is scientifically defensible for depth discrimination experiments, and (c) should be stated explicitly in the approach section so reviewers can verify the estimate.\", \"MISSING CITATION — arXiv:2602.10531 'From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources' (February 2026) directly analyzes iterative training dynamics on contaminated synthetic data and should be cited in the landscape section. It does not perform depth labeling or classification, so it does not threaten novelty, but its omission is likely to be caught by area chairs familiar with the collapse literature. One sentence differentiating it suffices: 'arXiv:2602.10531 analyzes the statistical dynamics of iterative training on contaminated data but does not assign generational depth labels or propose a depth-stratified filtering method.'\"]\nFeedback: Both Round 6 issues are cleanly resolved: the `enable_thinking=False` tokenizer hard switch plus post-hoc `&lt;think>` token scan properly closes the thinking-mode execution risk, and the fixed-total-size conditions (200K documents per condition, varying only Gen0/Gen1/Gen2 composition) properly close the corpus size confound. Two targeted fixes remain before this can pass: (1) Add an explicit document length cap (e.g., 512 tokens maximum per generated document) to the approach section and re-anchor the '6-8 GPU hour' generation estimate against that length — this makes the timeline defensible for reviewers who will check the arithmetic. (2) Cite arXiv:2602.10531 in the landscape section with a one-sentence differentiation (it analyzes collapse dynamics statistically but does not classify text by generational depth). Both fixes require under 30 minutes of writing and no new experiments.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-09T21:05:01.083Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-09T21:05:01.083Z",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-09T21:05:01.256Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-09 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme "New Missions for NLP Research" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.

Direction: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.

Contribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.
2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.
3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.

This is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.

Tag: direction=data_governance, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].**
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

## Idea under review (round 8/10)
{
  "title": "Genealogical Depth Scoring for Recursive Web Corpus Decontamination",
  "core_problem": "Current AI-generated text detectors are binary (human vs. AI), but training corpora increasingly contain 'second-generation' synthetic text: AI outputs from models that were themselves trained on AI-generated data. This generational depth is unmeasured and unaddressed by any existing detector. Strong Model Collapse (ICLR 2025) establishes that even non-vanishing fractions (~1%) of synthetic data trigger performance collapse, yet the paper treats all synthetic data equivalently — making no distinction between Gen1 text (one model generation removed from human data) and Gen2+ text (recursively compounded). The depth-dependent contribution to collapse severity is entirely uncharacterized, and no current method can assign a generational depth score to a raw training document. Critically, recent work (arXiv:2605.01647, May 2026) demonstrates a 'Wall of Separation' where AI-AI divergence in character-distribution space is significantly smaller than human-AI divergence — making within-model generational discrimination (Gen1 vs. Gen2 from the same fine-tuned model) a harder detection problem than binary human/AI classification and motivating our use of embedding-space features that target cumulative semantic drift orthogonal to character-level surface signals.",
  "opportunity": "By April 2025, 74.2% of newly created web pages contain some AI-generated text — of which 2.5% are fully AI-generated and 71.7% are human-AI blends, where human content has been AI-revised or AI-assisted (Ahrefs, 900K pages, April 2025). These blended documents may occupy an intermediate 'Gen0.5' depth position between Gen0 and Gen1 that depth scoring can address more precisely than binary detection, and they represent the dominant contamination modality at web scale. Complete decontamination is operationally infeasible — there is not enough uncontaminated human text to replace even the fully AI-generated fraction — shifting the practical research question from 'remove all synthetic data' (impossible at web scale) to 'which synthetic documents to prioritize for removal given a fixed filtering budget.' Depth-stratified decontamination addresses this directly: if Gen2+ documents are disproportionately harmful relative to Gen1 documents, preferential removal of deeper-generation text maximizes collapse mitigation per unit of filtering effort. This claim is explicitly scoped to *severity reduction per filtering budget*, not collapse prevention, and is tested in controlled fixed-total-size depth-composition conditions that isolate the effect of contamination depth from dataset volume — making the causal evidence for the governance claim empirically clean. Strong Model Collapse (ICLR 2025) provides the urgency but not the answer — it shows synthetic data is harmful at any non-vanishing fraction but gives no guidance on whether all synthetic data is equally harmful. Crucially, the paper does not distinguish Gen1 from Gen2 synthetic data at all, leaving the depth-dependent harm gradient completely unmeasured. A depth classifier that enables tiered decontamination — or, if depth discrimination fails, definitively establishes that binary filtering suffices — constitutes a concrete empirical contribution with direct governance impact, aligned with EMNLP 2026's special theme 'New Missions for NLP Research,' which explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance.'",
  "landscape": "Model collapse from recursive synthetic training is established (Shumailov et al., Nature 2024; Strong Model Collapse, ICLR 2025) and the limiting theory predicts collapse at any non-vanishing synthetic fraction. Mitigation via real-data accumulation (arXiv:2404.01413) or verifier-guided retraining (arXiv:2510.16657) is active. arXiv:2602.10531 ('From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources', February 2026) analyzes the statistical dynamics of iterative training on data contaminated with synthetic samples using a mixture-model framework, showing that improvement over collapsed models is possible when sufficient fresh real data is present; it does not assign generational depth labels to documents or propose a depth-stratified filtering method. Training-side collapse prevention via Truncated Cross-Entropy loss (ForTIFAI, arXiv:2509.08972) selectively ignores high-confidence tokens during training to filter synthetic artifacts — a complementary but orthogonal approach to our upstream corpus-level depth detection: ForTIFAI does not classify documents by generational depth and does not operate pre-training. The closest upstream related work, 'Machine-generated text detection prevents language model collapse' (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025), directly bridges AI-text detection and collapse prevention: it trains encoder-only binary classifiers (evaluating RoBERTa, DeBERTa-v3, and ModernBERT) to distinguish human from AI-generated text, then applies importance resampling — weighting each training document by (1-q(x))^b where q(x) is the classifier's AI-probability score — to up-weight likely human content during recursive training. Experiments across GPT-2 and SmolLM2 (124M–1.7B parameters) demonstrate that binary-classifier-guided resampling prevents collapse and even improves over training on purely human data. Critically, arXiv:2502.15654 treats all AI-generated text as equivalent regardless of generational provenance: importance weights depend only on a single binary human/AI probability, with no distinction between Gen1 text (one fine-tuning cycle removed from human data) and Gen2+ text (recursively compounded). Our work directly addresses this gap: if depth-stratified resampling weights — proportional to estimated generational distance from Gen0 — yield greater collapse-severity reduction per resampled document than flat binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over arXiv:2502.15654's strategy under budget-constrained filtering. The dual null-hypothesis design explicitly covers the scenario where depth discrimination fails (AUC < 0.65), in which case our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant and binary resampling is sufficient — a governance finding with direct practical value. A mathematical framework for how recursive publication compresses text through drift and selection is developed in arXiv:2604.08554 but does not propose a depth classifier. The framework is derived for variable-order n-gram agents and does not address transformer fine-tuning; extension to neural models is an open theoretical question that our experiments probe empirically. AI-generated text detection (arXiv:2303.11156, arXiv:2509.18880) addresses binary classification and reaches AUC ~0.85-0.90 for Gen1 text, uniformly treating all AI-generated text as equivalent regardless of generational provenance. Embedding-based representations show intrinsic separability between AI-generated and human text in compressed embedding spaces (arXiv:2408.10437), motivating our use of embedding-space distance features alongside surface-level signals. 'Understanding Transformers via N-gram Statistics' (arXiv:2407.12034, NeurIPS 2024) provides empirical motivation for applying n-gram-derived theoretical predictions to transformer fine-tuning: transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia, suggesting transformer distributional behavior closely approximates n-gram statistics at the local prediction level — supporting our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level, with our experiments constituting a direct empirical test of this generalization. 'Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection' (arXiv:2605.01647, May 2026) introduces the Letter Distribution Score (LD-Score) and establishes a 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space — with the direct implication that within-model generational divergence (Gen1 vs. Gen2 from the same fine-tuned 0.6B model) is smaller still than cross-model AI-AI divergence. This finding validates our architectural choice to prioritize embedding-space features over character-distribution proxies: our mean cosine distance from Gen0 centroid and within-document embedding variance operate in a representation space where cumulative semantic drift — predicted to accumulate monotonically by arXiv:2604.08554's recursive drift-selection framework — may remain detectable even when surface and character-level signals converge. The pre-specified AUC threshold (0.65) and dual null-hypothesis pivot design explicitly account for the scenario where depth discrimination fails at the document level despite embedding-space features. No paper in the contamination detection surveys (arXiv:2502.14425, arXiv:2406.04244) addresses generation depth as a variable. The closest concurrent work — 'Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models' (arXiv:2511.17602, Nov 2025) — asks whether synthetic data overlaps with evaluation benchmarks, not how many generative cycles deep a document is; generational ancestry is orthogonal to benchmark overlap. 'Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training?' (TrainProVe, CVPR 2025, arXiv:2503.09122) achieves >99% accuracy verifying which text-to-image model generated a given image, using model access and generalization error bounds — differentiation is sharp: TrainProVe operates in the image domain and requires model weights access, while our method operates on raw text documents with no model access, enabling upstream corpus-level pre-filtering. Both address data governance but via entirely complementary mechanisms. 'A Closer Look at Model Collapse' (arXiv:2509.16499, NeurIPS 2025 Spotlight) identifies a generalization-to-memorization transition but studies diffusion models and does not distinguish depth levels in training data.",
  "approach": "We build a controlled genealogical corpus by running a 2-step recursive train-generate loop with Qwen3-0.6B (the smallest Qwen3 model, chosen to minimize sequential compute cost while still exhibiting measurable distributional drift per generation), producing text with verified depth labels Gen0 (human, sourced from FineWeb-Edu and C4), Gen1, and Gen2, yielding ~200K labeled documents per depth level across diverse domains. All generated documents are hard-capped at 512 tokens maximum length: this cap is enforced at generation time via the `max_new_tokens=512` parameter, making generation time deterministic and reviewable. At 200K documents × 512 tokens = 102M tokens per generational step, batched A100 inference at 3,000–5,000 tok/s for Qwen3-0.6B yields approximately 6–9 GPU hours per step — consistent with the timeline estimate below. The 512-token cap is scientifically defensible for depth discrimination: surface-level signals (surprisal burstiness, lexical diversity, n-gram entropy) and embedding-space signals (mean cosine distance from Gen0 centroid, within-document window embedding variance) are fully computable over 512-token documents, and ordinal regression classifiers trained on short-document depth signals are directly comparable to the binary detectors in arXiv:2502.15654, which also operate on variable-length web documents.\n\nWe disable Qwen3-0.6B thinking mode during all generative steps via the hard switch `enable_thinking=False` in `tokenizer.apply_chat_template`, rather than the soft `/no_think` instruction tag — because GitHub discussion QwenLM/Qwen3 #1329 documents that the 0.6B model lacks sufficient instruction-following capacity to reliably honor `/no_think` when placed in the system prompt, and silent failure would inject `&lt;think>…&lt;/think>` reasoning traces into Gen1/Gen2 documents that are absent from Gen0 human text, making depth levels trivially separable by token-level artifacts rather than genuine semantic drift and invalidating the AUC signal. The `enable_thinking=False` hard switch operates at the tokenizer template level and does not depend on the model's instruction-following capacity. As a final post-hoc verification, every generated document is scanned for `&lt;think>` tokens and discarded if any are found, before corpus inclusion.\n\nLimiting to Gen0/Gen1/Gen2 compresses the sequential corpus construction bottleneck to approximately 2 wallclock days: Qwen3-0.6B fine-tuning on a 200K-document sample runs in ~4-6 GPU hours on A100, and generation of 200K new 512-token documents runs in ~6-9 GPU hours, for ~12-15 GPU hours per generational step. The hard sequential dependency spans only 2 steps.\n\nWe train a DeBERTa-v3-large ordinal regression classifier jointly on raw text and depth-diagnostic features spanning two categories: (a) surface-level signals — per-token surprisal variance (burstiness), lexical diversity decay (MTLD and type-token ratio), and n-gram entropy compression ratio; and (b) embedding-space signals — (i) mean cosine distance of within-document window embeddings from the pre-computed Gen0 centroid (capturing average depth of embedding drift from human text), and (ii) variance of per-window cosine distances from the Gen0 centroid within the document (capturing within-document heterogeneity of embedding drift). Both embedding features are computed from non-overlapping 128-token window embeddings produced by sentence-transformers/all-MiniLM-L6-v2; feature (i) measures central tendency and feature (ii) measures distributional spread — distinct geometric properties: a Gen2 document may exhibit both higher mean distance from Gen0 and more heterogeneous window-level drift than a Gen1 document, as cumulative generational compression produces uneven semantic displacement within a document. We integrate these five scalar depth-diagnostic features by concatenating them to the DeBERTa-v3-large CLS token representation (1024-dim), then training an ordinal regression head over this joint 1029-dim representation; the Gen0 embedding centroid is precomputed offline from a held-out Gen0 reference set of 10K documents using sentence-transformers/all-MiniLM-L6-v2 and is not updated during classifier training.\n\nEmbedding-space features are specifically motivated by the 'Wall of Separation' established in arXiv:2605.01647 (May 2026): AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence (Gen1→Gen2 from the same fine-tuned 0.6B model) is smaller still. Surface-level and character-distribution signals are therefore unlikely to reliably discriminate depth levels in this setting; our mean cosine distance from Gen0 centroid and within-document embedding variance instead target cumulative semantic drift that arXiv:2604.08554's recursive drift-selection framework predicts to accumulate monotonically across generations even when character distributions plateau — providing detection signal orthogonal to surface proxies. The argument is: our embedding-space features target cumulative semantic drift that persists even when surface divergence converges, consistent with the monotonic drift predicted by arXiv:2604.08554 — with the explicit caveat that arXiv:2604.08554 derives this prediction for variable-order n-gram agents, not transformer fine-tuning. We hypothesize the generalization holds because transformer next-token distributions closely approximate n-gram statistics at the local prediction level (arXiv:2407.12034, NeurIPS 2024, reports 68–79% agreement between transformer predictions and n-gram rulesets across two corpora), suggesting transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression, for which cumulative drift is expected to accumulate monotonically. Our classifier and collapse experiments directly test whether this hypothesized generalization from n-gram theory to transformer practice holds empirically.\n\nCentral technical risk and dual null-hypothesis design: We pre-specify two complementary pre-registered outcome scenarios to ensure a definitive, interpretable empirical finding under all classifier and collapse experiment outcomes. (Primary null) If the ordinal classifier falls below AUC 0.65 on Gen1/Gen2 discrimination, the finding is publishable: depth beyond Gen1 is linguistically indistinguishable at the document level using current text-level and embedding-level methods, implying binary filtering suffices — consistent with the implicit assumption of arXiv:2502.15654. In this case, the collapse validation experiments automatically pivot to directly comparing binary (Gen0-only) filtering against depth-stratified filtering at fixed corpus size. (Secondary null) If the classifier achieves AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between conditions (b) (100K Gen0 + 100K Gen1) and (c) (67K Gen0 + 67K Gen1 + 66K Gen2) at fixed total corpus size (paired t-test, α = 0.05, across 3 random seeds), we report this as a distinct secondary null outcome: depth detection is feasible but equal-fraction Gen2 contamination causes no additional collapse-severity beyond equal-fraction Gen1 contamination at GPT-2 scale — the marginal harm-per-generation curve is flat at this model size, binary filtering is sufficient for practical governance at small scales, and preferential Gen2 removal yields no measurable advantage at this scale. This finding has direct governance implications while leaving open whether depth stratification provides additional value at larger model scales, explicitly reserved as future work. All four logical combinations of (AUC pass/fail) × (collapse severity parity/non-parity) produce pre-specified, interpretable empirical contributions with distinct governance implications.\n\nThe trained classifier is applied zero-shot to real FineWeb and C4 slices to estimate depth-distribution statistics of existing pretraining corpora. Collapse validation uses a GPT-2-scale LM fine-tuned on three fixed-total-size depth-composition conditions (200K training documents each), following the controlled-composition standard of Strong Model Collapse (ICLR 2025): (a) Gen0-only: 200K Gen0; (b) Gen0+Gen1: 100K Gen0 + 100K Gen1; (c) Gen0+Gen1+Gen2: 67K Gen0 + 67K Gen1 + 66K Gen2. These corpora are constructed by subsampling from the already-generated 200K-document pools at each depth level, requiring no additional generation compute. Fixing total corpus size at 200K across all three conditions isolates the causal effect of depth composition from dataset volume: any observed collapse severity difference between conditions reflects contamination depth, not training set size — making the central governance claim ('Gen2 contamination is more harmful per document than Gen1 at equal contamination rate') empirically defensible. Collapse severity is tracked via held-out human-text perplexity and output tail entropy across multiple recursive training generations, explicitly scoped to measuring *severity as a function of depth composition at fixed scale* rather than collapse prevention — consistent with Strong Model Collapse's any-fraction harm finding. GenDepth-Bench is scoped to 2 model families: Qwen3-0.6B (primary) and Llama-3.2-1B (secondary, run through the same recursive loop to test cross-model generalizability of depth signals, explicitly optional — executed only if compute budget permits; see resource estimate). Coverage of 5+ model families is explicitly reserved as future work.\n\n16-Day Critical Path (EMNLP 2026 ARR deadline May 25, 2026; today May 9, 2026):\n— Days 1-2: Environment setup; sample 200K Gen0 docs from FineWeb-Edu/C4 (truncated to 512 tokens); prepare evaluation suite and draft intro/related-work sections.\n— Days 2-3 (sequential bottleneck step 1): Fine-tune Qwen3-0.6B on Gen0 (~4-6h GPU); generate 200K Gen1 documents at max 512 tokens each (~6-9h GPU; 200K × 512 tokens = 102M tokens ÷ 3,000–5,000 tok/s ≈ 6–9h) with `enable_thinking=False` hard switch and post-hoc `&lt;think>` token scan.\n— Days 3-4 (sequential bottleneck step 2): Fine-tune Qwen3-0.6B-v2 on Gen1 (~4-6h GPU); generate 200K Gen2 documents at max 512 tokens each (~6-9h GPU) with same thinking-mode controls.\n— Days 3-8 (PARALLEL TRACK A): DeBERTa-v3-large ordinal training begins with Gen0+Gen1 data at Day 3; adds Gen2 data when available at Day 5; ablations over surface vs. embedding feature subsets.\n— Days 5-10 (PARALLEL TRACK B): GPT-2-scale collapse experiments begin at Day 5 with fixed-size conditions (a) Gen0-only: 200K Gen0 and (b) Gen0+Gen1: 100K Gen0+100K Gen1 (subsampled from existing pools); add condition (c) Gen0+Gen1+Gen2: 67K each at Day 6 when Gen2 corpus is available. Llama-3.2-1B recursive corpus generation runs in parallel if compute budget is below 160h H100-equivalent at Day 5.\n— Days 7-9: Full classifier evaluation; if Gen1/Gen2 AUC < 0.65, activate primary null-hypothesis binary filtering comparison experiments; if AUC ≥ 0.65 but collapse severity parity detected between conditions (b) and (c), record secondary null outcome and report governance implications.\n— Days 9-10: Zero-shot depth scoring on real FineWeb/C4 slices.\n— Days 10-12: Feature importance ablations; cross-model generalizability check on Llama-3.2-1B-generated corpus (if optional Llama recursive corpus was generated).\n— Days 12-16: Analysis, writing, revision, and submission.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~210h A100 (40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B, each step generating 200K documents at 512 tokens max = 102M tokens ÷ ~3,500 tok/s average ≈ ~8h per step, ×2 steps = ~16h generation + ~24h fine-tuning over 2 steps + 50h DeBERTa-v3-large fine-tuning and ablations + 120h GPT-2-scale collapse validation experiments across 3 fixed-size depth-composition conditions)",
      "gpu_utilization": "High idle rate (~40-60%): GPU waits while researcher designs experiment configs, interprets collapse curves, debugs depth signal quality, and writes between each stage over several months",
      "timeline": "4-6 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$370 at $1.75/h blended A100 average (RunPod ~$1.49/h, Lambda ~$2.06/h); approximately 70 H100-equivalent hours"
    },
    "human_in_loop": {
      "gpu_hours": "~320h A100 (agent handles training loop queuing and ablation scheduling; human approves depth-feature selection, collapse experiment design, AUC threshold decision for null-hypothesis activation, and Llama-3.2-1B second-family validation)",
      "gpu_utilization": "Moderate idle rate (~15-25%): agent queues overnight runs and fills GPU gaps between sequential generational steps; handles parallel DeBERTa and collapse experiment scheduling",
      "timeline": "6-10 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$60-120 (~600-800 agent turns at $0.08-0.15/turn for experiment design, result interpretation, and iteration guidance)",
      "estimated_gpu_cost": "~$560 at $1.75/h average A100; approximately 107 H100-equivalent hours",
      "risk_note": "Key bottleneck: 2-step sequential corpus construction (train on GenN → generate GenN+1 at 512 tokens max → train again) cannot be parallelized; each step adds ~1 wallclock day with Qwen3-0.6B. The 512-token document cap makes generation time deterministic: 200K × 512 tokens = 102M tokens ÷ 3,000–5,000 tok/s ≈ 6–9h per step, matching the timeline estimate and eliminating schedule uncertainty from variable document lengths. Corpus construction for collapse experiments uses fixed-total-size subsampling (200K per condition) from the already-generated per-depth pools — no additional generation compute required. Pre-specified dual null-hypothesis design (primary: AUC < 0.65; secondary: AUC ≥ 0.65 but collapse severity parity between fixed-size conditions (b) and (c)) means the agent has clear decision rules without requiring researcher judgment to pivot, covering all four logical outcome combinations."
    },
    "auto_research": {
      "gpu_hours": "~490h A100 / ~163h H100-equivalent hours (mandatory, within ≤200h hard constraint): 40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B (200K documents × 512 tokens max per step = 102M tokens; at 3,000–5,000 tok/s ≈ 6–9h generation per step, ×2 steps; plus ~12h fine-tuning per step = ~40h total) + 120h DeBERTa-v3-large fine-tuning and ablations with 2x hyperparameter search across depth-feature combinations (surface-only, embedding-only, combined) + 240h GPT-2-scale collapse validation experiments across 3 fixed-total-size depth-composition conditions (Qwen3-0.6B family) with 3 collapse metrics + 90h auxiliary ablations (feature importance, zero-shot FineWeb/C4 scoring, null-hypothesis binary filtering comparison if AUC threshold triggered). Llama-3.2-1B recursive corpus generation and collapse experiments (~60-90h A100 / ~20-30h H100-equivalent) are explicitly optional from the start: executed only if compute budget remains below 160h H100-equivalent at Day 10; otherwise deprioritized to zero-shot depth scoring only, maintaining a genuine 40h safety buffer against the 200h hard ceiling.",
      "gpu_utilization": "Near-zero idle (<5%): agent queues hyperparameter sweeps and ablations 24/7, filling GPU cycles between sequential generational construction steps with parallel auxiliary experiments",
      "timeline": "13-16 days with 4-6 concurrent A100s",
      "team": "0 (4-6h one-time setup: genealogical corpus schema with 512-token document cap, experiment grid, AUC threshold 0.65 for primary null-hypothesis activation, paired t-test criterion for secondary null-hypothesis activation between fixed-size conditions (b) and (c), stopping conditions)",
      "claude_api_cost": "$250-400 (~2500-3000 agent turns for experiment orchestration, result analysis, and adaptive exploration)",
      "estimated_gpu_cost": "~$856 at $1.75/h average A100 (mandatory only); ~$960 including optional Llama-3.2-1B corpus if budget permits",
      "speed_bottleneck": "2-step sequential corpus construction is the hard wallclock floor; the 512-token document cap makes per-step generation time deterministic at ~6-9h (102M tokens ÷ 3,000–5,000 tok/s), eliminating schedule uncertainty; GPU count limits simultaneous ablation breadth during non-sequential phases",
      "risk_note": "Corpus construction for collapse experiments uses fixed-total-size subsampling (200K per condition from already-generated per-depth pools) — no additional generation compute. Depth signal may be weak between Gen1 and Gen2 from the same small model — a risk compounded by the 'Wall of Separation' finding (arXiv:2605.01647): AI-AI surface divergence is substantially smaller than human-AI divergence, making within-model generational discrimination harder still. Pre-specified dual null-hypothesis design covers all outcomes: primary null (AUC < 0.65) redirects to binary filtering comparison at fixed corpus size; secondary null (AUC ≥ 0.65 but collapse severity parity between fixed-size conditions (b) and (c)) reports depth detection as feasible but equal-fraction Gen2 contamination as causing no incremental governance harm beyond Gen1 at GPT-2 scale. Embedding-space features (mean cosine distance from Gen0 centroid and within-document embedding variance over 128-token windows) partially mitigate the primary null risk by targeting cumulative semantic drift invisible at the surface level. Budget contingency: Llama-3.2-1B recursive corpus generation is explicitly optional from the start; if compute approaches 160h H100-equivalent during execution, Llama-3.2-1B recursive corpus is deprioritized to zero-shot depth scoring only (no new collapse experiments), saving ~60-90h A100 (~20-30h H100-equivalent) and maintaining a genuine 40h buffer against the 200h hard ceiling."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; special theme 'New Missions for NLP Research' explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance' — near-perfect topical alignment; conference October 24-29, Budapest)",
    "NAACL 2027 (ARR cycle deadline TBD, expected ~late 2026; safe backup with more time for thorough collapse validation experiments and additional model families)"
  ],
  "level": "solid",
  "key_references": [
    "AI models collapse when trained on recursively generated data (Nature 2024)",
    "Strong Model Collapse (ICLR 2025) — establishes collapse at any non-vanishing synthetic fraction (~1% example); holds total corpus size fixed while varying synthetic fraction (the controlled design our collapse experiments follow); does not distinguish Gen1 from Gen2 synthetic data; this gap is what we fill",
    "Machine-generated text detection prevents language model collapse (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025) — closest upstream prior work: trains binary encoder-only classifiers (evaluating RoBERTa, DeBERTa-v3, ModernBERT) with importance resampling — weights ∝ (1-q(x))^b — to prevent collapse at GPT-2/SmolLM2 scale (124M–1.7B parameters); treats all AI-generated text equivalently without generational depth distinction; our work directly extends this: if depth-stratified resampling weights yield greater collapse-severity reduction per decontamination unit than binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over binary resampling under budget constraints; if not (AUC < 0.65 or collapse severity parity between fixed-size conditions (b) and (c)), our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant",
    "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources (arXiv:2602.10531, February 2026) — analyzes the statistical dynamics of iterative training on contaminated data using a mixture-model framework, showing that improvement over collapsed models is possible when sufficient fresh real data is present; does not assign generational depth labels to documents or propose a depth-stratified filtering method",
    "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (arXiv:2404.01413)",
    "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (arXiv:2510.16657)",
    "ForTIFAI: Fending Off Recursive Training Induced Failure for AI Models (arXiv:2509.08972) — training-side collapse prevention via Truncated Cross-Entropy loss; orthogonal to our upstream corpus-level depth detection; does not classify documents by generational depth",
    "Drift and Selection in LLM Text Ecosystems (arXiv:2604.08554) — mathematical framework for how recursive publication compresses text through drift and selection; derived for variable-order n-gram agents (not transformer fine-tuning); does not propose a depth classifier or detection method; motivates our prediction that embedding-space drift accumulates monotonically across generations even when surface distributions plateau, under the hypothesis that transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression — a generalization our experiments directly test",
    "Understanding Transformers via N-gram Statistics (arXiv:2407.12034, NeurIPS 2024) — transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia; provides empirical grounding for our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level",
    "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (arXiv:2605.01647, May 2026) — establishes 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space; within-model generational gap (Gen1→Gen2 from same fine-tuned model) is smaller still; directly threatens surface-level discriminability; our counter-argument: embedding-space features (mean cosine distance from Gen0 centroid and within-document window embedding variance, computed over non-overlapping 128-token windows via sentence-transformers/all-MiniLM-L6-v2) target cumulative semantic drift orthogonal to character-distribution signals; the pre-specified dual null-hypothesis design accounts for the possibility that depth discrimination fails despite embedding-space features",
    "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective (NeurIPS 2025 Spotlight)",
    "RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (ACL 2024)",
    "Can AI-Generated Text be Reliably Detected? (arXiv:2303.11156)",
    "Diversity Boosts AI-Generated Text Detection (arXiv:2509.18880)",
    "Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models (arXiv:2511.17602) — asks whether synthetic data overlaps with evaluation benchmarks; generational ancestry is orthogonal to benchmark overlap",
    "Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training? (TrainProVe, CVPR 2025, arXiv:2503.09122) — achieves >99% accuracy in image domain using model access and generalization error bounds; differentiation: our method operates on raw text with no model access, enabling upstream corpus-level pre-filtering; different modality and mechanism address the same governance goal",
    "Understanding Generative AI Content with Embedding Models (arXiv:2408.10437) — demonstrates intrinsic separability of AI-generated and human text in compressed embedding space; motivates our use of embedding-space cosine distance and within-document variance features for depth discrimination beyond surface-level signals",
    "Benchmark Data Contamination of Large Language Models: A Survey (arXiv:2406.04244)",
    "A Survey on Data Contamination for Large Language Models (arXiv:2502.14425)"
  ],
  "description": "As web corpora become saturated with AI-generated content (74.2% of new web pages contain some AI text by April 2025, of which 2.5% are fully AI-generated and 71.7% are human-AI blends; Ahrefs, 900K pages), complete decontamination is operationally infeasible, shifting the question to: which synthetic documents cause the most harm and should be removed first? We propose Genealogical Depth Scoring, a method extending binary AI-text detection to ordinal depth classification (Gen0=human, Gen1, Gen2), trained on a controlled corpus produced by 2-step recursive train-generate loops using Qwen3-0.6B with thinking mode disabled via the hard switch `enable_thinking=False` in `tokenizer.apply_chat_template` — rather than the soft `/no_think` instruction tag, which silently fails for the 0.6B model when placed in the system prompt (GitHub QwenLM/Qwen3 discussion #1329) and would introduce `&lt;think>…&lt;/think>` artifacts that make depth levels trivially separable by token-level signals rather than genuine semantic drift — with post-hoc discard of any documents containing `&lt;think>` tokens before corpus inclusion. All generated documents are hard-capped at 512 tokens via `max_new_tokens=512`, yielding 200K × 512 tokens = 102M tokens per generational step; at 3,000–5,000 tok/s for Qwen3-0.6B on A100 this takes approximately 6–9 GPU hours per step, making the generation timeline deterministic and anchored to a verifiable arithmetic bound. The classifier combines DeBERTa-v3-large fine-tuning with two classes of depth-diagnostic features: surface-level signals (surprisal burstiness, lexical diversity decay, n-gram entropy compression ratio) and embedding-space signals — (i) mean cosine distance of within-document window embeddings from the Gen0 centroid, and (ii) variance of per-window cosine distances from the Gen0 centroid within the document, both computed over non-overlapping 128-token windows via sentence-transformers/all-MiniLM-L6-v2. Feature (i) captures average drift from human text in embedding space; feature (ii) captures within-document heterogeneity of that drift — distinct geometric properties (central tendency vs. distributional spread) that together characterize the document's depth signature. These five scalar features are concatenated to the DeBERTa-v3-large CLS token representation (1024-dim) and passed to an ordinal regression head trained over the joint 1029-dim representation; the Gen0 centroid is precomputed offline and not updated during training. The embedding-space features directly address the 'Wall of Separation' documented in arXiv:2605.01647 (May 2026) — AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence is smaller still — by targeting cumulative semantic drift that arXiv:2604.08554 predicts to accumulate monotonically across recursive generations even when surface statistics plateau. Because arXiv:2604.08554 derives this prediction for variable-order n-gram agents rather than transformer fine-tuning, we ground the generalization in arXiv:2407.12034 (NeurIPS 2024), which shows transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions, and treat our classifier and collapse experiments as a direct empirical test of whether this theoretical extension holds. We pre-specify a dual null-hypothesis design: (primary null) if Gen1/Gen2 AUC < 0.65, depth is linguistically indistinguishable and binary filtering suffices; (secondary null) if AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between fixed-size conditions (b) (100K Gen0 + 100K Gen1) and (c) (67K Gen0 + 67K Gen1 + 66K Gen2), equal-fraction Gen2 contamination causes no additional collapse-severity beyond equal-fraction Gen1 contamination at GPT-2 scale — depth detection is feasible but depth-stratified filtering provides no incremental governance benefit at small model scale. All four logical outcomes produce pre-specified, interpretable empirical contributions. Collapse validation compares three fixed-total-size depth-composition conditions (200K documents each: (a) Gen0-only; (b) 100K Gen0+100K Gen1; (c) 67K Gen0+67K Gen1+66K Gen2), constructed by subsampling from the already-generated 200K-document pools at each depth level — no additional generation compute. Fixing total corpus size across all conditions isolates the causal effect of depth composition from dataset volume, making the central governance claim ('Gen2 contamination is more harmful per document than Gen1 at equal contamination rate, supporting preferential Gen2 removal per filtering unit') empirically defensible. Results are framed as *collapse severity as a function of contamination depth composition at fixed scale*, directly informing the real-world budget-constrained decontamination problem. TrainProVe (CVPR 2025) addresses related governance goals via model access in the image domain; ForTIFAI (arXiv:2509.08972) prevents collapse at training time via modified loss; arXiv:2502.15654 (Feb 2025) prevents collapse via binary detection with importance resampling but treats all AI text equivalently without generational depth distinction; arXiv:2602.10531 (Feb 2026) analyzes collapse dynamics statistically via mixture models but does not classify text by generational depth — our work is the first to assign generational depth scores to raw text corpus documents upstream of training, and directly tests whether depth-stratified resampling yields greater collapse-severity reduction per filtering unit than binary resampling. We release GenDepth-Bench covering 2 model families (Qwen3-0.6B primary; Llama-3.2-1B secondary, optional pending compute budget), with 5+ family coverage as explicit future work. Targets EMNLP 2026's special theme on synthetic data feedback loops and data governance.",
  "project_name": "gen_depth_decontam",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["FACTUAL ERROR — Model name: 'Qwen3.5-0.5B' does not exist. The smallest Qwen3.5 is 0.8B; the smallest Qwen3 is 0.6B. Must be corrected to Qwen3-0.6B or Qwen3.5-0.8B before any experimental planning.", "HARD CONSTRAINT VIOLATION — Auto Research compute estimate (~800 A100h ≈ 267 H100h) exceeds the user's explicitly stated ≤200 H100-hour hard constraint. Manual (~75 H100h) and HIL (~117 H100h) are within budget; auto research must be rescoped or noted as out-of-bounds.", "TIMELINE INFEASIBILITY — Sequential corpus construction requires 3–5 days per generational step × 3 steps = 9–15 days minimum, leaving ≤1–7 days for DeBERTa training, collapse validation experiments, and writeup within the 16-day hard deadline. Even the 'auto' mode estimate of '2–4 weeks' exceeds 16 days. The submission timeline is not credible unless the generation chain is compressed to ≤2 days/step with very small models.", "CORE HYPOTHESIS LOGIC GAP — Strong Model Collapse (ICLR 2025) establishes that even 0.1% synthetic data fraction triggers collapse. If this threshold holds, then the relevant intervention is removing ALL synthetic data, not tiered removal that tolerates Gen1. The proposal must explicitly argue why tiered filtering is sufficient given this finding, or reframe its claim to 'among contaminated corpora, depth-stratified decontamination is superior to binary decontamination.'", "CENTRAL TECHNICAL RISK UNADDRESSED — The classifier must distinguish Gen2 text from Gen1 text generated by the same small model (Qwen3-0.6B). After one generation of fine-tuning on a small corpus, the model changes only marginally — the distributional gap between its Gen1 and Gen2 outputs may be smaller than inter-domain variation within Gen0, making reliable ordinal classification impossible. No preliminary evidence, theoretical bound, or pilot experiment is offered to support the plausibility of this distinguishability.", "MISSING RELATED WORK — 'Training Data Provenance Verification: Did Your Model Use Synthetic Data' (CVPR 2025) achieves >99% accuracy determining synthetic vs. real training provenance from model behavior and embeddings. This is not the same as text-level depth scoring, but must be cited and explicitly differentiated since it addresses the same governance goal via a complementary mechanism.", "BENCHMARK SCOPE OVERCLAIM — GenDepth-Bench promises '5+ model families' but the experiment design uses a single small model (Qwen3-0.6B) for corpus construction. Covering 5+ model families requires each family to run its own recursive train-generate loop, multiplying the sequential compute requirement 5x and breaking the budget and timeline constraints further."]
Feedback: The core concept (generational depth scoring for corpus decontamination) is genuinely novel and worth pursuing, but the proposal has execution-level failures that need resolution before submission. Priority fixes: (1) Replace 'Qwen3.5-0.5B' with 'Qwen3-0.6B' throughout. (2) Cap Auto Research at ≤600 A100h and revise the estimate to stay within 200 H100-hours. (3) The 16-day timeline requires compressing the sequential chain: use a single model family (Qwen3-0.6B), limit to Gen0/Gen1/Gen2 (2 recursive steps = ~4–6 days), run DeBERTa and collapse experiments in parallel during gap days. Make this explicit in the timeline with a day-by-day critical path. (4) Add a null-hypothesis section: 'If the ordinal classifier fails (Gen1/Gen2 AUC < 0.65), we test whether binary filtering (Gen0-only) outperforms depth-stratified filtering as the baseline intervention, directly testing the hypothesis from Strong Model Collapse.' This converts the central technical risk into a publishable empirical finding regardless of outcome. (5) Cut the GenDepth-Bench scope to 2–3 model families max (achievable within budget) and reserve '5+ families' as future work. (6) Add the CVPR 2025 provenance verification paper and differentiate: your method acts on raw text without model access, while provenance verification requires access to model weights — this is the right framing to distinguish the contributions.

### Round 2 review
Verdict: revise
Issues: ["MISSING CITATION — arXiv:2605.01647 ('Beyond Perplexity: Character Distribution Signatures,' May 2026): This paper independently demonstrates a 'Wall of Separation' where AI-AI divergence is significantly smaller than human-AI divergence. Because Gen1 and Gen2 are outputs of the *same* 0.6B model differing by one fine-tuning step, the within-model generational gap is smaller still than cross-model AI-AI divergence. This directly threatens the discriminability hypothesis and must be cited and addressed. The argument should be: cumulative semantic drift in embedding space may still be detectable even when surface statistics converge — but this requires acknowledgment and a direct counter-argument, not silence.", "LOGICAL FRAMING GAP — Partial filtering under Strong Model Collapse: Strong Model Collapse (ICLR 2025) establishes collapse at *any non-vanishing* synthetic fraction (~1/1000). After depth-stratified filtering that removes Gen2 but retains Gen1, the corpus still contains a non-vanishing synthetic fraction — which, by the same theory, should still trigger collapse. The proposal must explicitly distinguish between: (a) depth-stratified filtering *reducing collapse severity or delaying onset* even without eliminating it, and (b) the more ambitious but unsupported claim that it prevents collapse. The current framing conflates these and needs to be sharpened to 'severity reduction per filtering budget' rather than 'collapse prevention.'", "AUTO RESEARCH TIMELINE INCONSISTENCY — The 16-day critical path is laid out explicitly (Days 1-16), but the auto research resource estimate states '2-3 weeks with 4-6 concurrent A100s.' The upper bound (3 weeks = 21 days) overshoots the deadline. This should read '13-16 days with 4-6 concurrent A100s' based on the critical path arithmetic (550h / 4 GPUs = 137.5h ≈ 5.7 compute-days + 2-day sequential bottleneck + ~4 days writing/analysis).", "74% STATISTIC PRECISION — The Ahrefs study (verified: 900K pages, April 2025) found 74.2% of new pages contain *some* AI content, but only 2.5% are fully AI-generated; the remaining 72% are human-AI blends. The proposal's phrasing ('74% of newly created web pages contained AI-generated text') is technically accurate but implies raw AI-generated contamination at 74% scale. This should be clarified — notably, human-AI blends (Gen0.5, partially edited) may sit between Gen0 and Gen1 in depth, which is actually *interesting* for the depth scoring framework and worth noting explicitly.", "COMPUTE BUFFER TOO THIN — Auto research at 550h A100 / 183h H100-equivalent leaves only 17 H100-hours of buffer against the 200h hard constraint. If any of the collapse validation experiments (estimated 300h A100 for 6 conditions) requires a single re-run due to training instability, hyperparameter error, or data pipeline failure, the budget is exceeded. The proposal should either (a) specify which experiments are cut if budget is approached, or (b) identify a fallback scope reduction (e.g., drop the Llama-3.2-1B second-family validation to save ~90h)."]
Feedback: All five Round 1 issues are resolved. The proposal is substantially improved and the core idea is verified as novel — no competing work on generational depth scoring found across extensive search. Three targeted fixes will raise this to pass: (1) Cite arXiv:2605.01647 and address its implication directly: 'Our embedding-space features target cumulative semantic drift that persists even when surface divergence converges, consistent with the monotonic drift predicted by arXiv:2604.08554' — this is already your argument, just make it explicit against this specific paper. (2) Reframe the partial filtering value: add one sentence explicitly stating 'even under Strong Model Collapse's any-fraction harm finding, depth-stratified filtering reduces expected collapse severity for a fixed decontamination budget by prioritizing highest-harm documents first — a practical governance claim that holds even if perfect decontamination is required for complete collapse prevention.' (3) Fix the auto research timeline to '13-16 days' and add a budget contingency: state that if compute approaches 180h H100-equivalent, the Llama-3.2-1B recursive corpus generation is deprioritized to the zero-shot scoring phase only (no new collapse experiments), saving ~60-90h A100. These three fixes address the only remaining material gaps; the null-hypothesis design, the 16-day critical path, the TrainProVe differentiation, and the GenDepth-Bench scoping are all solid.

### Round 3 review
Verdict: revise
Issues: ["SECONDARY NULL HYPOTHESIS MISSING — The preregistered null-hypothesis design covers one failure mode (Gen1/Gen2 AUC < 0.65 → pivot to binary filtering comparison), but does not pre-specify what is reported if the classifier SUCCEEDS (AUC ≥ 0.65) but the collapse experiments show EQUAL held-out perplexity for Gen0+Gen1 vs Gen0+Gen1+Gen2 corpora. This scenario — 'we can detect depth labels but depth does not predict marginal collapse severity at GPT-2 scale' — is a coherent empirical finding but is currently absent from the design. Without it, reviewers can fault the paper for not pre-committing to how this outcome is interpreted. One or two sentences explicitly naming this secondary null and its interpretation ('depth detection is feasible but depth-stratified filtering provides no incremental benefit over binary filtering at this scale, suggesting the harm-per-generation curve is flat') would close the gap.", "MODELING GAP IN EMBEDDING DRIFT ARGUMENT — The monotonic embedding drift prediction cited from arXiv:2604.08554 is derived for variable-order n-gram agents, not for transformer fine-tuning. The proposal applies this theoretical prediction to one fine-tuning step of a 0.6B transformer on 200K documents, which is a substantive analogy not directly supported by that framework. While the empirical design will test this claim, the theoretical motivation should acknowledge the modeling gap (e.g., 'arXiv:2604.08554 establishes monotonic drift for n-gram agents; we hypothesize this generalizes to transformer fine-tuning based on [brief argument], which our experiment directly tests'). Without this acknowledgment, a reviewer may flag the theoretical foundation as overclaimed."]
Feedback: Both remaining issues are fixable with two targeted additions: (1) Add one paragraph (or a row in the null-hypothesis table if one exists) that explicitly pre-specifies the 'classifier succeeds, collapse severity parity' scenario as a secondary null outcome and states what that finding means for practical governance (binary filtering is sufficient; depth stratification provides no incremental value at GPT-2 scale). This completes the preregistered design and removes a reviewer attack surface. (2) In the approach section, add one sentence acknowledging that arXiv:2604.08554's drift framework is derived for n-gram agents and that you are testing whether the monotonic drift prediction extends to transformer fine-tuning — framing your collapse and classifier experiments as a direct empirical test of this generalization. These two additions require no new experiments and can be drafted in under an hour. The core novelty, verified references, budget/timeline credibility, and venue alignment are all solid.

### Round 4 review
Verdict: revise
Issues: ["MISSING CITATION — arXiv:2502.15654 'Machine-generated text detection prevents language model collapse' (Drayson, Yilmaz, Lampos; UCL, Feb 2025) is the most directly adjacent prior work: it trains a binary DeBERTa-v3 classifier to distinguish human vs AI text, applies importance resampling to up-weight human content during recursive training, and demonstrates collapse prevention at GPT-2/SmolLM2 scale. This paper is not cited anywhere in the proposal. A reviewer will immediately flag this omission since it directly addresses the same problem (AI text detection to prevent collapse). The differentiation is clear — 2502.15654 uses binary detection and does not distinguish generational depth; the proposed method extends this to ordinal depth scoring enabling tiered filtering — but it must be cited and explicitly differentiated.", "COMPUTE MARGIN TOO THIN — Auto research at ~183 H100h equivalent leaves only 17h of buffer against the 200h hard constraint. The contingency trigger at 180h H100-equivalent is well-specified (drop Llama-3.2-1B recursive corpus to zero-shot only), but this saves 20-30h H100-equivalent — meaning the contingency must activate before the budget is exceeded by more than ~3h. Any single failed training run or unexpected GPU contention during the sequential corpus construction bottleneck (Days 2-4) could push total usage past 200h. The proposal should either (a) declare the Llama-3.2-1B recursive corpus as optional from the start with the contingency trigger moved earlier (e.g., at 160h), or (b) estimate auto research at a slightly lower total."]
Feedback: Both Round 3 issues are properly resolved — the secondary null hypothesis (AUC ≥ 0.65 but collapse severity parity) is now explicitly preregistered with a paired t-test criterion and governance interpretation, and the n-gram-to-transformer modeling gap is acknowledged with the NeurIPS 2024 grounding. Two targeted fixes will bring this to pass: (1) Add arXiv:2502.15654 to the landscape and key_references sections. The differentiation sentence writes itself: 'The closest upstream related work (arXiv:2502.15654, Feb 2025) shows that binary AI-text detection via DeBERTa-v3 with importance resampling prevents collapse at GPT-2/SmolLM2 scale, but treats all AI-generated text equivalently regardless of generational depth — leaving open whether depth stratification enables more efficient decontamination per filtering unit, which is the specific question we answer.' (2) Move the Llama-3.2-1B recursive corpus to explicitly optional from the start in auto_research, and set the contingency activation threshold at 160h H100-equivalent rather than 180h, creating a more credible 40h safety margin. These two changes require no new experiments.

### Round 5 review
Verdict: revise
Issues: ["MAUVE-STYLE FEATURE ILL-DEFINED AT DOCUMENT LEVEL — MAUVE is a corpus-level metric that estimates KL divergence between two distributions of text embeddings. It requires multiple samples per distribution, not a single document. Applying it as a per-document feature is non-standard and potentially meaningless. The proposal lists 'MAUVE-style distributional divergence' as a depth-diagnostic feature without explaining the per-document operationalization. If this feature simply becomes 'distance of document embedding from Gen0 distribution,' it overlaps substantially with the 'cosine distance from Gen0 centroid' feature already listed. A reviewer will immediately flag this as either technically ill-defined or redundant. Fix: either (a) specify the document-level operationalization explicitly (e.g., 'we compute the negative log-likelihood of a document's embedding under a KDE fit to the Gen0 embedding distribution' or 'we compute the mean embedding of non-overlapping 128-token windows within the document and measure the MAUVE divergence of this within-document distribution from the Gen0 reference distribution'), or (b) rename this feature to accurately reflect what is computed and explain how it differs from the cosine centroid distance.", "DEBERTA + HAND-CRAFTED FEATURE INTEGRATION UNSPECIFIED — The approach says the classifier trains 'jointly on raw text and depth-diagnostic features' combining DeBERTa-v3-large with five engineered features from two different representation spaces (surface-level and sentence-transformer embedding space). No architecture is described. Given that DeBERTa produces its own CLS embedding and the sentence-transformer produces a separate embedding vector for the cosine distance computation, the proposal is operating with at least two separate text encoders plus scalar features. How these are merged is entirely unspecified. This is a critical methods gap that affects replicability. Fix: add two sentences specifying the integration architecture (e.g., 'we concatenate the five scalar depth-diagnostic features to the DeBERTa CLS token representation, then train an ordinal regression head over this joint representation; the Gen0 centroid used for cosine distance is computed offline from sentence-transformers/all-MiniLM-L6-v2 embeddings and is not jointly trained').", "QWEN3-0.6B THINKING MODE UNSPECIFIED — Qwen3-0.6B supports an explicit thinking mode that generates chain-of-thought reasoning traces within &lt;think>...&lt;/think> tags, which would dramatically alter the character distribution, lexical properties, and statistical footprint of generated text. Whether thinking mode is enabled or disabled during the recursive generation loop must be specified, as it affects: (a) the plausibility of depth signals (thinking traces may be trivially distinguishable), (b) the validity of the Wall of Separation counter-argument (thinking traces produce very different distributions than standard generation), and (c) the external validity of results to real-world web contamination scenarios where thinking traces are absent. This is a one-sentence fix: 'We disable Qwen3-0.6B thinking mode (/no_think) during all generative steps to ensure output text matches real-world web document distributions.'"]
Feedback: Three targeted fixes are needed — none require new experiments. (1) MAUVE feature clarification: replace 'MAUVE-style distributional divergence' with a concrete document-level operationalization. The most defensible adaptation is to segment each document into non-overlapping 128-token windows, embed each window via sentence-transformers, and compute the MAUVE divergence between this within-document embedding distribution and the Gen0 reference distribution — this is genuinely distinct from cosine centroid distance as it captures within-document distributional spread, not just central tendency. If this is too complex to implement reliably in 16 days, drop the MAUVE feature and replace it with the variance of within-document embeddings around the Gen0 centroid (a simpler proxy capturing the same distributional geometry idea). (2) DeBERTa integration architecture: add two sentences to the approach specifying that the five scalar features are concatenated to the DeBERTa CLS token, and that the Gen0 centroid is precomputed offline using sentence-transformers and not jointly fine-tuned — this closes the replicability gap without changing the experimental design. (3) Thinking mode: add one sentence specifying that Qwen3 thinking mode is disabled during generation. These three additions require less than an hour of writing and will prevent round-six reviewer rejection on technical specificity grounds.

### Round 6 review
Verdict: revise
Issues: ["EXECUTION RISK — Qwen3-0.6B /no_think system-prompt unreliability: GitHub discussion #1329 documents that Qwen3-0.6B 'lacks sufficient capacity to reliably follow instructions' and /no_think placed in the system prompt silently fails for this specific model size. If thinking mode activates during generation, output text contains &lt;think>...&lt;/think> reasoning traces absent from Gen0 human web text, making Gen1/Gen2 text trivially distinguishable by token-level artifacts rather than genuine semantic drift — inflating AUC and completely invalidating the experimental signal. The current proposal says only 'We disable Qwen3-0.6B thinking mode (/no_think) during all generative steps' without specifying that /no_think must be placed in each user message (not the system prompt). Fix: add one sentence specifying placement — 'We add /no_think to each user message (not the system prompt) during all generative steps, consistent with the workaround documented for Qwen3-0.6B's limited instruction-following capacity at this scale (GitHub QwenLM/Qwen3 discussion #1329).' Alternatively, use the intalio/Qwen3-NoThink-0.6b HuggingFace variant which has thinking mode disabled by default.", "METHODOLOGICAL CONFOUND — Corpus size differs across collapse experiment conditions: the three filtering conditions (Gen0-only ≈ 200K documents, Gen0+Gen1 ≈ 400K, Gen0+Gen1+Gen2 ≈ 600K) differ 3× in total training corpus size. Controlled model collapse research (Strong Model Collapse ICLR 2025, arXiv:2404.01413) varies the synthetic fraction while holding total dataset size fixed. Without this control, lower collapse severity in the Gen0-only condition could reflect training data volume effects (smaller dataset → different generalization regime) rather than depth-stratified filtering benefits, directly undermining the central 'severity reduction per filtering budget' governance claim. Fix option A (preferred): run all three conditions on fixed total corpus size (e.g., 200K documents each), varying only Gen0/Gen1/Gen2 composition proportions (e.g., 200K Gen0 vs. 100K Gen0+100K Gen1 vs. 67K Gen0+67K Gen1+66K Gen2). Fix option B (lightweight): explicitly acknowledge the confound as a limitation and reframe the comparison as 'effect of contamination composition on collapse severity' rather than 'severity reduction per filtering budget' — this weakens the governance claim but makes it empirically defensible within 16 days."]
Feedback: The proposal has progressively addressed all five Round 5 issues cleanly. Two new issues require targeted fixes before this can pass. (1) Qwen3-0.6B /no_think placement: add one sentence specifying that /no_think is added to each individual user message (not the system prompt), citing GitHub discussion #1329. This is a one-line fix. Alternatively, switch to intalio/Qwen3-NoThink-0.6b which has thinking mode disabled by default and avoids the placement ambiguity entirely — worth specifying as the primary model choice. (2) Corpus size confound: this is the more significant issue. The cleanest fix within budget is to run all three collapse conditions on the same total corpus size (200K documents each), varying only the Gen0/Gen1/Gen2 mix. This requires no additional generation but does require rerunning collapse experiments on rebalanced corpora — feasible within Days 5-10 if the generation schedule completes on time. If the rebalanced design is too costly, explicitly reframe the comparison: replace 'severity reduction per filtering budget' with 'severity as a function of contamination composition depth' and acknowledge that corpus size varies across conditions as a limitation. The rebalanced design is strongly preferred because the current governance framing ('prioritize Gen2 removal to maximize collapse mitigation per filtering unit') cannot be supported by size-confounded experiments.

### Round 7 review
Verdict: revise
Issues: ["TIMELINE RISK — Document length unspecified in generation estimates: The '6-8 GPU hours to generate 200K documents with Qwen3-0.6B' claim is unanchored to a document length. FineWeb-Edu/C4 documents commonly run 500-2000 tokens; at 1000 tokens × 200K docs = 200M tokens, batched A100 inference at 3000-5000 tok/s for Qwen3-0.6B yields 11-18 hours per generational step — not 6-8 hours. Over 2 sequential steps this adds 6-20 hours to the critical path, potentially cascading into a 2-3 day delay and threatening the May 25 deadline. Fix: explicitly commit to truncating/capping generated documents at 512 tokens maximum length, which (a) brings generation time within the estimate (200K × 512 tokens = 102M tokens ÷ 3000-5000 tok/s ≈ 6-9h), (b) is scientifically defensible for depth discrimination experiments, and (c) should be stated explicitly in the approach section so reviewers can verify the estimate.", "MISSING CITATION — arXiv:2602.10531 'From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources' (February 2026) directly analyzes iterative training dynamics on contaminated synthetic data and should be cited in the landscape section. It does not perform depth labeling or classification, so it does not threaten novelty, but its omission is likely to be caught by area chairs familiar with the collapse literature. One sentence differentiating it suffices: 'arXiv:2602.10531 analyzes the statistical dynamics of iterative training on contaminated data but does not assign generational depth labels or propose a depth-stratified filtering method.'"]
Feedback: Both Round 6 issues are cleanly resolved: the `enable_thinking=False` tokenizer hard switch plus post-hoc `&lt;think>` token scan properly closes the thinking-mode execution risk, and the fixed-total-size conditions (200K documents per condition, varying only Gen0/Gen1/Gen2 composition) properly close the corpus size confound. Two targeted fixes remain before this can pass: (1) Add an explicit document length cap (e.g., 512 tokens maximum per generated document) to the approach section and re-anchor the '6-8 GPU hour' generation estimate against that length — this makes the timeline defensible for reviewers who will check the arithmetic. (2) Cite arXiv:2602.10531 in the landscape section with a one-sentence differentiation (it analyzes collapse dynamics statistically but does not classify text by generational depth). Both fixes require under 30 minutes of writing and no new experiments.


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
  "promptId": "b7cb083a-c29c-412a-9da3-a7aaa46c6957",
  "type": "user",
  "uuid": "b020477b-038d-4341-918e-762c64f060f8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-09T21:05:01.250Z_

```json
{
  "parentUuid": "b020477b-038d-4341-918e-762c64f060f8",
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
  "uuid": "827b1c06-2bdb-4d91-9f3e-da651a4c21ed",
  "timestamp": "2026-05-09T21:05:01.250Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-09T21:05:01.250Z_

```json
{
  "parentUuid": "827b1c06-2bdb-4d91-9f3e-da651a4c21ed",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8de90492-0b2c-488f-ab79-ffb3dd3d9eec",
  "timestamp": "2026-05-09T21:05:01.250Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
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
  "leafUuid": "8de90492-0b2c-488f-ab79-ffb3dd3d9eec",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Genealogical depth scoring for recursive text decontamination",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a"
}
```

---

### Assistant

_source line 8 · 2026-05-09T21:05:27.104Z_

<details><summary>Logged reasoning block</summary>

```text
This is round 8 of 10 for reviewing the "Genealogical Depth Scoring for Recursive Web Corpus Decontamination" paper idea. Let me carefully analyze what has been addressed from previous rounds and what new issues may exist.

From the previous review history:
- Round 7 issues were:
  1. TIMELINE RISK — Document length unspecified in generation estimates (needs 512-token cap)
  2. MISSING CITATION — arXiv:2602.10531 (From Collapse to Improvement)

Looking at the current proposal (round 8), I need to check if both of these have been addressed:


Both issues appear to be resolved. The approach section now specifies the 512-token hard cap with explicit parameter details and computational estimates showing 6–9 GPU hours per generational step on A100s, and the missing citation for arXiv:2602.10531 on evolutionary dynamics of iterative training has been added to the references.

Now I need to verify these claims independently and search for any competing or similar work that might have been overlooked. Let me start by checking whether the key papers actually exist—arXiv:2605.01647 on the Wall of Separation, arXiv:2602.10531 on evolutionary dynamics, and arXiv:2502.15654 on machine-generated text detection preventing collapse.

Looking at the proposal more carefully, I can see it's been through substantial iteration and now addresses the major concerns: the correct model specification, realistic compute budgets with contingency, a clear 16-day timeline, appropriate framing around severity reduction rather than prevention, proper differentiation from related work, and a dual null-hypothesis design that tests both filtering sufficiency and detection performance thresholds.

The technical details are also solidified—the embedding variance features replacing MAUVE, the DeBERTa architecture with concatenated scalars, the thinking mode configuration for Qwen3, fixed corpus sizes, and citations to the Wall of Separation and other relevant papers. The 512-token document cap with generation time anchoring to arithmetic operations provides concrete grounding for the experimental setup.

Now I'm doing independent verification to catch any remaining issues—checking whether there are papers on generational depth scoring I've overlooked, confirming the arXiv citations are accurate, validating the compute estimates, and scanning for other potential gaps in the methodology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8de90492-0b2c-488f-ab79-ffb3dd3d9eec",
  "isSidechain": false,
  "requestId": "req_011Casg4PFYUJLqNHbLp3XPt",
  "type": "assistant",
  "uuid": "c3d4fb5d-127d-43fb-925c-3df105483f5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DY3aSga6r8tzzrGGTX3LjM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25587,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2162,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 25587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25587
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

_source line 9 · 2026-05-09T21:05:27.128Z_

I'll conduct independent verification searches before issuing my verdict. Let me run several targeted searches to check novelty, verify key references, and find potential competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3d4fb5d-127d-43fb-925c-3df105483f5a",
  "isSidechain": false,
  "requestId": "req_011Casg4PFYUJLqNHbLp3XPt",
  "type": "assistant",
  "uuid": "5bed1d53-6446-4e31-8fe8-b11903b2d8fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DY3aSga6r8tzzrGGTX3LjM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25587,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2162,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 25587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25587
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

_source line 10 · 2026-05-09T21:05:39.593Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TyVtxJHs74LSP6sQuLWn4J`</summary>

```json
{
  "description": "Verify key paper references and search for competing work on generational depth scoring",
  "subagent_type": "Explore",
  "prompt": "I need you to search for papers related to a research idea about \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination.\" This paper proposes to score AI-generated text by generational depth (Gen0=human, Gen1=AI-generated, Gen2=AI trained on AI-generated text and then generating more text), build an ordinal classifier using DeBERTa-v3 + embedding features to distinguish these generations, and use this for corpus decontamination.\n\nPlease search for:\n\n1. First, search for \"arxiv 2605.01647\" - does a paper called \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\" exist? Search: `site:arxiv.org 2605.01647`\n\n2. Search for \"arxiv 2502.15654\" - does a paper called \"Machine-generated text detection prevents language model collapse\" by Drayson, Yilmaz, Lampos (UCL, Feb 2025) exist? Search: `arxiv.org 2502.15654 machine-generated text detection language model collapse`\n\n3. Search for \"arxiv 2602.10531\" - does \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\" (Feb 2026) exist?\n\n4. Search for any papers on \"generational depth\" OR \"generation depth scoring\" for AI-generated text: `site:arxiv.org generational depth AI text detection 2025 2026`\n\n5. Search for competing work: `arxiv recursive AI text generation depth classification 2025 2026`\n\n6. Search for: `model collapse generational synthetic data depth detection 2025 2026`\n\n7. Search for: `site:arxiv.org second generation synthetic data training collapse`\n\n8. Check if there's any paper on \"multi-generation AI text\" detection: `arxiv multi-generation AI generated text detection`\n\nFor each search, use WebSearch and report what you find - whether papers exist, their titles, authors, and relevance to the research idea."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bed1d53-6446-4e31-8fe8-b11903b2d8fb",
  "isSidechain": false,
  "requestId": "req_011Casg4PFYUJLqNHbLp3XPt",
  "type": "assistant",
  "uuid": "e2d1c303-f22e-46c0-b8d7-3a9209f8e78b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DY3aSga6r8tzzrGGTX3LjM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25587,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2162,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 25587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25587
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

_source line 11 · 2026-05-09T21:05:45.977Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Fe11P5bgVUJuFcSyFBmUa1`</summary>

```json
{
  "description": "Search for Qwen3-0.6B thinking mode specifics and compute feasibility",
  "subagent_type": "Explore",
  "prompt": "I need to verify some technical claims in a research proposal about AI model collapse and synthetic data detection. Please search for:\n\n1. Search for Qwen3-0.6B capabilities and thinking mode: `Qwen3 0.6B thinking mode enable_thinking tokenizer` - does the `enable_thinking=False` parameter exist in `tokenizer.apply_chat_template` for Qwen3? \n\n2. Search: `site:github.com QwenLM Qwen3 no_think 0.6B instruction following` - is there a GitHub discussion about Qwen3-0.6B failing to follow /no_think instructions?\n\n3. Search: `Qwen3 0.6B inference speed tokens per second A100` - what is the realistic inference speed of Qwen3-0.6B on an A100 GPU?\n\n4. Search: `DeBERTa-v3-large ordinal regression fine-tuning GPU hours` - how much compute does DeBERTa-v3-large fine-tuning typically require?\n\n5. Search: `arxiv 2604.08554 drift selection LLM text ecosystems` - does this paper exist? What does it say about n-gram agents and recursive text generation?\n\n6. Search: `arxiv 2407.12034 transformers n-gram statistics NeurIPS 2024` - does this paper exist and does it show 68-79% agreement between transformer predictions and n-gram rulesets?\n\n7. Search: `FineWeb-Edu dataset availability HuggingFace` - is FineWeb-Edu actually available and accessible?\n\nReport findings for each search query including whether the claims in the proposal are verified or contradicted."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2d1c303-f22e-46c0-b8d7-3a9209f8e78b",
  "isSidechain": false,
  "requestId": "req_011Casg4PFYUJLqNHbLp3XPt",
  "type": "assistant",
  "uuid": "d299d7cf-8d3f-4889-ab68-a1f5d2181cf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DY3aSga6r8tzzrGGTX3LjM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25587,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2162,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 25587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25587
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

_source line 12 · 2026-05-09T21:06:07.671Z_

<details><summary>↩ Tool result · `toolu_01TyVtxJHs74LSP6sQuLWn4J`</summary>

```text
Based on my comprehensive search, here's what I found regarding papers related to your genealogical depth scoring research idea:

## Search Results Summary

### 1. **2605.01647 - "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection"** ✓ EXISTS
This paper was published in May 2026 by researchers at University of Maryland, College Park. It focuses on training-free AI text detection methods based on character distribution signatures, showing that AI models create a distinct "Wall of Separation" from human text patterns. However, this appears to focus on binary detection rather than generational depth classification.

**Link:** [Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection](https://arxiv.org/abs/2605.01647)

### 2. **2502.15654 - "Machine-generated text detection prevents language model collapse"** ✓ EXISTS
This February 2025 paper by Drayson, Yilmaz, and Lampos (UCL) directly addresses your research problem space. It investigates how machine-generated text detection can prevent model collapse by analyzing text characteristics across sequential model generations and how decoding strategy impacts collapse.

**Link:** [Machine-generated text detection prevents language model collapse](https://arxiv.org/abs/2502.15654)

### 3. **2602.10531 - "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources"** ✓ EXISTS
This February 2026 paper by Soham Bakshi and Sunrit Chakraborty provides theoretical analysis of generational training dynamics. It demonstrates that with proper mixture weights of true vs. synthetic data, models can avoid collapse even with contaminated training data—directly relevant to your generational depth concept.

**Link:** [From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources](https://arxiv.org/abs/2602.10531)

### 4. **Search for "generational depth" AI text detection** ✗ NOT FOUND
No papers specifically titled or focused on "generational depth" or "generation depth scoring" were found in recent arXiv papers (2025-2026). However, several detection papers exist on related topics including "Diversity Boosts AI-Generated Text Detection" and others addressing multi-model scenarios.

### 5. **Recursive AI text generation and depth classification** ✓ FOUND RELATED WORK
The "Recursive Language Models" (RLM) paper (2512.24601, Dec 2025) by MIT CSAIL researchers uses a depth classification system where models at depth 0 spawn sub-models at depth 1, depth 2, etc. While not about generational AI text detection per se, it demonstrates practical depth-based classification architectures.

**Link:** [Recursive Language Models](https://arxiv.org/abs/2512.24601)

### 6. **Model collapse and generational synthetic data** ✓ MULTIPLE PAPERS FOUND
Several highly relevant papers on generational synthetic data training exist:
- [How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse](https://arxiv.org/abs/2404.05090)
- [Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World](https://arxiv.org/abs/2410.16713)
- [Multi-modal Synthetic Data Training and Model Collapse: Insights from VLMs and Diffusion Models](https://arxiv.org/abs/2505.08803)
- [Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657)

These papers analyze generational effects of training on progressively synthetic data but don't focus on classification/detection at specific generational depths.

### 7. **Multi-generation AI-generated text detection** ✓ GROWING AREA
Recent work on multi-generation detection includes:
- [AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification](https://arxiv.org/abs/2505.11550) - includes multiclass classification tasks
- [A Comprehensive Dataset for Human vs. AI Generated Text Detection](https://arxiv.org/abs/2510.22874) - RAID and M4 datasets with multiple LLMs
- [DeTeCtive: Detecting AI-generated Text via Multi-Level Contrastive Learning](https://arxiv.org/abs/2410.20964)

## Conclusion

Your genealogical depth scoring idea appears to be **novel and timely**. While there is substantial research on:
- Model collapse from synthetic data training (generational effects)
- AI text detection (binary classification)
- Multi-generation synthetic data dynamics
- Model verification approaches

**I found no existing papers specifically proposing ordinal/multi-class classification of AI text by generational depth (Gen0 → Gen1 → Gen2 → ...) using methods like DeBERTa-v3 with embedding features for corpus decontamination.** The closest work is the Drayson et al. (2502.15654) paper on text characteristics across generations, but this focuses on prevention rather than classification-based detection.

Your approach of building an **ordinal classifier to distinguish generational depth** combined with **corpus decontamination** represents an innovative contribution to the field.

Sources:
- [Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection](https://arxiv.org/abs/2605.01647)
- [Machine-generated text detection prevents language model collapse](https://arxiv.org/abs/2502.15654)
- [From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources](https://arxiv.org/abs/2602.10531)
- [Recursive Language Models](https://arxiv.org/abs/2512.24601)
- [How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse](https://arxiv.org/abs/2404.05090)
- [Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World](https://arxiv.org/abs/2410.16713)
- [Multi-modal Synthetic Data Training and Model Collapse: Insights from VLMs and Diffusion Models](https://arxiv.org/abs/2505.08803)
- [Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657)
- [AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification](https://arxiv.org/abs/2505.11550)
- [A Comprehensive Dataset for Human vs. AI Generated Text Detection](https://arxiv.org/abs/2510.22874)
- [DeTeCtive: Detecting AI-generated Text via Multi-Level Contrastive Learning](https://arxiv.org/abs/2410.20964)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2d1c303-f22e-46c0-b8d7-3a9209f8e78b",
  "isSidechain": false,
  "promptId": "b7cb083a-c29c-412a-9da3-a7aaa46c6957",
  "type": "user",
  "uuid": "0059504e-b2b5-468e-99c2-b3f1b266a78a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to search for papers related to a research idea about \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination.\" This paper proposes to score AI-generated text by generational depth (Gen0=human, Gen1=AI-generated, Gen2=AI trained on AI-generated text and then generating more text), build an ordinal classifier using DeBERTa-v3 + embedding features to distinguish these generations, and use this for corpus decontamination.\n\nPlease search for:\n\n1. First, search for \"arxiv 2605.01647\" - does a paper called \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\" exist? Search: `site:arxiv.org 2605.01647`\n\n2. Search for \"arxiv 2502.15654\" - does a paper called \"Machine-generated text detection prevents language model collapse\" by Drayson, Yilmaz, Lampos (UCL, Feb 2025) exist? Search: `arxiv.org 2502.15654 machine-generated text detection language model collapse`\n\n3. Search for \"arxiv 2602.10531\" - does \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\" (Feb 2026) exist?\n\n4. Search for any papers on \"generational depth\" OR \"generation depth scoring\" for AI-generated text: `site:arxiv.org generational depth AI text detection 2025 2026`\n\n5. Search for competing work: `arxiv recursive AI text generation depth classification 2025 2026`\n\n6. Search for: `model collapse generational synthetic data depth detection 2025 2026`\n\n7. Search for: `site:arxiv.org second generation synthetic data training collapse`\n\n8. Check if there's any paper on \"multi-generation AI text\" detection: `arxiv multi-generation AI generated text detection`\n\nFor each search, use WebSearch and report what you find - whether papers exist, their titles, authors, and relevance to the research idea.",
    "agentId": "ac9bfe49da90e9964",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search, here's what I found regarding papers related to your genealogical depth scoring research idea:\n\n## Search Results Summary\n\n### 1. **2605.01647 - \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\"** ✓ EXISTS\nThis paper was published in May 2026 by researchers at University of Maryland, College Park. It focuses on training-free AI text detection methods based on character distribution signatures, showing that AI models create a distinct \"Wall of Separation\" from human text patterns. However, this appears to focus on binary detection rather than generational depth classification.\n\n**Link:** [Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection](https://arxiv.org/abs/2605.01647)\n\n### 2. **2502.15654 - \"Machine-generated text detection prevents language model collapse\"** ✓ EXISTS\nThis February 2025 paper by Drayson, Yilmaz, and Lampos (UCL) directly addresses your research problem space. It investigates how machine-generated text detection can prevent model collapse by analyzing text characteristics across sequential model generations and how decoding strategy impacts collapse.\n\n**Link:** [Machine-generated text detection prevents language model collapse](https://arxiv.org/abs/2502.15654)\n\n### 3. **2602.10531 - \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"** ✓ EXISTS\nThis February 2026 paper by Soham Bakshi and Sunrit Chakraborty provides theoretical analysis of generational training dynamics. It demonstrates that with proper mixture weights of true vs. synthetic data, models can avoid collapse even with contaminated training data—directly relevant to your generational depth concept.\n\n**Link:** [From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources](https://arxiv.org/abs/2602.10531)\n\n### 4. **Search for \"generational depth\" AI text detection** ✗ NOT FOUND\nNo papers specifically titled or focused on \"generational depth\" or \"generation depth scoring\" were found in recent arXiv papers (2025-2026). However, several detection papers exist on related topics including \"Diversity Boosts AI-Generated Text Detection\" and others addressing multi-model scenarios.\n\n### 5. **Recursive AI text generation and depth classification** ✓ FOUND RELATED WORK\nThe \"Recursive Language Models\" (RLM) paper (2512.24601, Dec 2025) by MIT CSAIL researchers uses a depth classification system where models at depth 0 spawn sub-models at depth 1, depth 2, etc. While not about generational AI text detection per se, it demonstrates practical depth-based classification architectures.\n\n**Link:** [Recursive Language Models](https://arxiv.org/abs/2512.24601)\n\n### 6. **Model collapse and generational synthetic data** ✓ MULTIPLE PAPERS FOUND\nSeveral highly relevant papers on generational synthetic data training exist:\n- [How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse](https://arxiv.org/abs/2404.05090)\n- [Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World](https://arxiv.org/abs/2410.16713)\n- [Multi-modal Synthetic Data Training and Model Collapse: Insights from VLMs and Diffusion Models](https://arxiv.org/abs/2505.08803)\n- [Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657)\n\nThese papers analyze generational effects of training on progressively synthetic data but don't focus on classification/detection at specific generational depths.\n\n### 7. **Multi-generation AI-generated text detection** ✓ GROWING AREA\nRecent work on multi-generation detection includes:\n- [AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification](https://arxiv.org/abs/2505.11550) - includes multiclass classification tasks\n- [A Comprehensive Dataset for Human vs. AI Generated Text Detection](https://arxiv.org/abs/2510.22874) - RAID and M4 datasets with multiple LLMs\n- [DeTeCtive: Detecting AI-generated Text via Multi-Level Contrastive Learning](https://arxiv.org/abs/2410.20964)\n\n## Conclusion\n\nYour genealogical depth scoring idea appears to be **novel and timely**. While there is substantial research on:\n- Model collapse from synthetic data training (generational effects)\n- AI text detection (binary classification)\n- Multi-generation synthetic data dynamics\n- Model verification approaches\n\n**I found no existing papers specifically proposing ordinal/multi-class classification of AI text by generational depth (Gen0 → Gen1 → Gen2 → ...) using methods like DeBERTa-v3 with embedding features for corpus decontamination.** The closest work is the Drayson et al. (2502.15654) paper on text characteristics across generations, but this focuses on prevention rather than classification-based detection.\n\nYour approach of building an **ordinal classifier to distinguish generational depth** combined with **corpus decontamination** represents an innovative contribution to the field.\n\nSources:\n- [Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection](https://arxiv.org/abs/2605.01647)\n- [Machine-generated text detection prevents language model collapse](https://arxiv.org/abs/2502.15654)\n- [From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources](https://arxiv.org/abs/2602.10531)\n- [Recursive Language Models](https://arxiv.org/abs/2512.24601)\n- [How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse](https://arxiv.org/abs/2404.05090)\n- [Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World](https://arxiv.org/abs/2410.16713)\n- [Multi-modal Synthetic Data Training and Model Collapse: Insights from VLMs and Diffusion Models](https://arxiv.org/abs/2505.08803)\n- [Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657)\n- [AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification](https://arxiv.org/abs/2505.11550)\n- [A Comprehensive Dataset for Human vs. AI Generated Text Detection](https://arxiv.org/abs/2510.22874)\n- [DeTeCtive: Detecting AI-generated Text via Multi-Level Contrastive Learning](https://arxiv.org/abs/2410.20964)"
      }
    ],
    "totalDurationMs": 28067,
    "totalTokens": 24458,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1805,
      "cache_creation_input_tokens": 6285,
      "cache_read_input_tokens": 14698,
      "output_tokens": 1670,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6285
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1805,
          "output_tokens": 1670,
          "cache_read_input_tokens": 14698,
          "cache_creation_input_tokens": 6285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6285,
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
  "sourceToolAssistantUUID": "e2d1c303-f22e-46c0-b8d7-3a9209f8e78b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-09T21:06:24.721Z_

<details><summary>↩ Tool result · `toolu_01Fe11P5bgVUJuFcSyFBmUa1`</summary>

```text
## Summary of Verification Results

Based on my comprehensive search, here are the findings for each claim in your research proposal:

### 1. **Qwen3-0.6B `enable_thinking` Parameter** ✓ VERIFIED
The `enable_thinking=False` parameter **does exist** in `tokenizer.apply_chat_template()` for Qwen3. The parameter is documented and can be set to `False` to disable thinking mode. The default is `True`.

**Sources:**
- [Qwen3 - How to Run & Fine-tune (Unsloth)](https://unsloth.ai/docs/models/models/qwen3-how-to-run-and-fine-tune)
- [How to set enable_thinking=False in vllm deploy cmd (GitHub Discussion)](https://github.com/QwenLM/Qwen3/discussions/1300)

### 2. **Qwen3-0.6B /no_think Instruction Issue** ⚠ PARTIALLY CONFIRMED
There **is** a documented GitHub discussion (Discussion #1329) titled "Can't disable thinking when using qwen3-0.6b with /nothink" which confirms the model has issues reliably following the `/no_think` instruction. The search results indicate this is related to the model's limited capacity at 0.6B parameters.

**Sources:**
- [Can't disable thinking when using qwen3-0.6b with /nothink (GitHub Discussion #1329)](https://github.com/QwenLM/Qwen3/discussions/1329)

### 3. **Qwen3-0.6B Inference Speed on A100** ⚠ INCOMPLETE INFORMATION
Specific inference speed benchmarks for Qwen3-0.6B on A100 GPUs are not explicitly documented in public sources. General API measurements show approximately 188.9 tokens/second through Alibaba's API, but this is not hardware-specific A100 data. The Qwen documentation mentions they conduct speed benchmarks, but specific A100 figures are not publicly detailed.

**Sources:**
- [Speed Benchmark - Qwen Documentation](https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html)
- [Qwen3 0.6B Analysis (Artificial Analysis)](https://artificialanalysis.ai/models/qwen3-0.6b-instruct)

### 4. **DeBERTa-v3-large Ordinal Regression GPU Hours** ⚠ NOT SPECIFICALLY DOCUMENTED
No specific information exists for ordinal regression fine-tuning with DeBERTa-v3-large. One concrete example shows fine-tuning on SQuAD v2.0 took 15 hours on a Titan RTX 24GB GPU, but ordinal regression specifics are not documented.

**Sources:**
- [DeBERTa Implementation (GitHub)](https://github.com/microsoft/DeBERTa)
- [microsoft/deberta-v3-large (Hugging Face Model Card)](https://huggingface.co/microsoft/deberta-v3-large)

### 5. **arXiv 2604.08554 "Drift and selection in LLM text ecosystems"** ✓ VERIFIED
The paper **exists** and is authored by Søren Riis. It develops an "exactly solvable mathematical framework based on variable-order n-gram agents" and discusses drift and selection forces in recursive text generation.

**Key claim verified:** The paper is indeed based on "variable-order n-gram agents" as mentioned in your proposal.

**Sources:**
- [Drift and selection in LLM text ecosystems (arXiv 2604.08554)](https://arxiv.org/abs/2604.08554)
- [Full HTML version](https://arxiv.org/html/2604.08554)

### 6. **arXiv 2407.12034 "Understanding Transformers via N-gram Statistics"** ✓ VERIFIED WITH EXACT AGREEMENT FIGURES
The paper **exists** and was accepted to NeurIPS 2024. The **68-79% agreement figure is accurately cited**. The paper specifically states: "for 79% and 68% of LLM next-token distributions on TinyStories and Wikipedia, respectively, their top-1 predictions agree with those provided by our N-gram rulesets."

**Sources:**
- [Understanding Transformers via N-gram Statistics (arXiv 2407.12034)](https://arxiv.org/abs/2407.12034)
- [NeurIPS 2024 Poster](https://neurips.cc/virtual/2024/poster/94849)
- [Full paper HTML](https://arxiv.org/html/2407.12034)

### 7. **FineWeb-Edu Dataset Availability** ✓ VERIFIED
FineWeb-Edu **is actively available** on HuggingFace. It contains 1.3T tokens from educational web pages filtered from the larger FineWeb dataset. Two variants are available with different thresholds.

**Sources:**
- [HuggingFaceFW/fineweb-edu (Hugging Face Datasets)](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)
- [FineWeb-Edu Alternative Variant](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-score-2)
- [FineWeb Blog and Resources](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1)

---

## Overall Assessment

Your proposal's key technical claims are **well-supported by existing literature**:
- The papers cited (2604.08554 and 2407.12034) exist and are accurately described
- The n-gram framework claims are verified
- The 68-79% agreement figures are precisely cited
- FineWeb-Edu is accessible as described
- The Qwen3 parameter and instruction-following issues are documented

The only gaps are specific hardware-level benchmarks for Qwen3-0.6B on A100 and precise GPU requirements for DeBERTa ordinal regression, which appear to be implementation-dependent metrics not widely published in standardized form.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d299d7cf-8d3f-4889-ab68-a1f5d2181cf3",
  "isSidechain": false,
  "promptId": "b7cb083a-c29c-412a-9da3-a7aaa46c6957",
  "type": "user",
  "uuid": "e0c9ab5c-facc-40fb-ab93-90975e684dcb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify some technical claims in a research proposal about AI model collapse and synthetic data detection. Please search for:\n\n1. Search for Qwen3-0.6B capabilities and thinking mode: `Qwen3 0.6B thinking mode enable_thinking tokenizer` - does the `enable_thinking=False` parameter exist in `tokenizer.apply_chat_template` for Qwen3? \n\n2. Search: `site:github.com QwenLM Qwen3 no_think 0.6B instruction following` - is there a GitHub discussion about Qwen3-0.6B failing to follow /no_think instructions?\n\n3. Search: `Qwen3 0.6B inference speed tokens per second A100` - what is the realistic inference speed of Qwen3-0.6B on an A100 GPU?\n\n4. Search: `DeBERTa-v3-large ordinal regression fine-tuning GPU hours` - how much compute does DeBERTa-v3-large fine-tuning typically require?\n\n5. Search: `arxiv 2604.08554 drift selection LLM text ecosystems` - does this paper exist? What does it say about n-gram agents and recursive text generation?\n\n6. Search: `arxiv 2407.12034 transformers n-gram statistics NeurIPS 2024` - does this paper exist and does it show 68-79% agreement between transformer predictions and n-gram rulesets?\n\n7. Search: `FineWeb-Edu dataset availability HuggingFace` - is FineWeb-Edu actually available and accessible?\n\nReport findings for each search query including whether the claims in the proposal are verified or contradicted.",
    "agentId": "a5c9388da966821bf",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Verification Results\n\nBased on my comprehensive search, here are the findings for each claim in your research proposal:\n\n### 1. **Qwen3-0.6B `enable_thinking` Parameter** ✓ VERIFIED\nThe `enable_thinking=False` parameter **does exist** in `tokenizer.apply_chat_template()` for Qwen3. The parameter is documented and can be set to `False` to disable thinking mode. The default is `True`.\n\n**Sources:**\n- [Qwen3 - How to Run & Fine-tune (Unsloth)](https://unsloth.ai/docs/models/models/qwen3-how-to-run-and-fine-tune)\n- [How to set enable_thinking=False in vllm deploy cmd (GitHub Discussion)](https://github.com/QwenLM/Qwen3/discussions/1300)\n\n### 2. **Qwen3-0.6B /no_think Instruction Issue** ⚠ PARTIALLY CONFIRMED\nThere **is** a documented GitHub discussion (Discussion #1329) titled \"Can't disable thinking when using qwen3-0.6b with /nothink\" which confirms the model has issues reliably following the `/no_think` instruction. The search results indicate this is related to the model's limited capacity at 0.6B parameters.\n\n**Sources:**\n- [Can't disable thinking when using qwen3-0.6b with /nothink (GitHub Discussion #1329)](https://github.com/QwenLM/Qwen3/discussions/1329)\n\n### 3. **Qwen3-0.6B Inference Speed on A100** ⚠ INCOMPLETE INFORMATION\nSpecific inference speed benchmarks for Qwen3-0.6B on A100 GPUs are not explicitly documented in public sources. General API measurements show approximately 188.9 tokens/second through Alibaba's API, but this is not hardware-specific A100 data. The Qwen documentation mentions they conduct speed benchmarks, but specific A100 figures are not publicly detailed.\n\n**Sources:**\n- [Speed Benchmark - Qwen Documentation](https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html)\n- [Qwen3 0.6B Analysis (Artificial Analysis)](https://artificialanalysis.ai/models/qwen3-0.6b-instruct)\n\n### 4. **DeBERTa-v3-large Ordinal Regression GPU Hours** ⚠ NOT SPECIFICALLY DOCUMENTED\nNo specific information exists for ordinal regression fine-tuning with DeBERTa-v3-large. One concrete example shows fine-tuning on SQuAD v2.0 took 15 hours on a Titan RTX 24GB GPU, but ordinal regression specifics are not documented.\n\n**Sources:**\n- [DeBERTa Implementation (GitHub)](https://github.com/microsoft/DeBERTa)\n- [microsoft/deberta-v3-large (Hugging Face Model Card)](https://huggingface.co/microsoft/deberta-v3-large)\n\n### 5. **arXiv 2604.08554 \"Drift and selection in LLM text ecosystems\"** ✓ VERIFIED\nThe paper **exists** and is authored by Søren Riis. It develops an \"exactly solvable mathematical framework based on variable-order n-gram agents\" and discusses drift and selection forces in recursive text generation.\n\n**Key claim verified:** The paper is indeed based on \"variable-order n-gram agents\" as mentioned in your proposal.\n\n**Sources:**\n- [Drift and selection in LLM text ecosystems (arXiv 2604.08554)](https://arxiv.org/abs/2604.08554)\n- [Full HTML version](https://arxiv.org/html/2604.08554)\n\n### 6. **arXiv 2407.12034 \"Understanding Transformers via N-gram Statistics\"** ✓ VERIFIED WITH EXACT AGREEMENT FIGURES\nThe paper **exists** and was accepted to NeurIPS 2024. The **68-79% agreement figure is accurately cited**. The paper specifically states: \"for 79% and 68% of LLM next-token distributions on TinyStories and Wikipedia, respectively, their top-1 predictions agree with those provided by our N-gram rulesets.\"\n\n**Sources:**\n- [Understanding Transformers via N-gram Statistics (arXiv 2407.12034)](https://arxiv.org/abs/2407.12034)\n- [NeurIPS 2024 Poster](https://neurips.cc/virtual/2024/poster/94849)\n- [Full paper HTML](https://arxiv.org/html/2407.12034)\n\n### 7. **FineWeb-Edu Dataset Availability** ✓ VERIFIED\nFineWeb-Edu **is actively available** on HuggingFace. It contains 1.3T tokens from educational web pages filtered from the larger FineWeb dataset. Two variants are available with different thresholds.\n\n**Sources:**\n- [HuggingFaceFW/fineweb-edu (Hugging Face Datasets)](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)\n- [FineWeb-Edu Alternative Variant](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-score-2)\n- [FineWeb Blog and Resources](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1)\n\n---\n\n## Overall Assessment\n\nYour proposal's key technical claims are **well-supported by existing literature**:\n- The papers cited (2604.08554 and 2407.12034) exist and are accurately described\n- The n-gram framework claims are verified\n- The 68-79% agreement figures are precisely cited\n- FineWeb-Edu is accessible as described\n- The Qwen3 parameter and instruction-following issues are documented\n\nThe only gaps are specific hardware-level benchmarks for Qwen3-0.6B on A100 and precise GPU requirements for DeBERTa ordinal regression, which appear to be implementation-dependent metrics not widely published in standardized form."
      }
    ],
    "totalDurationMs": 38739,
    "totalTokens": 24443,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 21171,
      "output_tokens": 1504,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1761
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1504,
          "cache_read_input_tokens": 21171,
          "cache_creation_input_tokens": 1761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1761,
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
  "sourceToolAssistantUUID": "d299d7cf-8d3f-4889-ab68-a1f5d2181cf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e0c9ab5c-facc-40fb-ab93-90975e684dcb",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Genealogical depth scoring for recursive text decontamination",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a"
}
```

---

### Assistant

_source line 16 · 2026-05-09T21:09:34.035Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the searches confirm that the key papers exist and are correctly cited. Let me now do a few more targeted searches to:
1. Look for any new competing work that might have emerged between rounds 7 and 8 (May 2026)
2. Check whether the proposal's central assumption is valid - that Gen1 vs Gen2 text from the same 0.6B model is actually distinguishable
3. Verify the auto research compute estimate (163 H100 hours)
4. Look for any new EMNLP 2026 relevant papers

Let me also think through the proposal carefully now.

**What's been fixed from Round 7:**


The token cap is now explicitly stated with the math worked out, and the recent competing work is properly cited and distinguished. Now I'm checking the compute breakdown: the corpus generation estimate of 40 hours checks out, but the 120 hours allocated for DeBERTa fine-tuning and ablations seems potentially inflated.

The 240 hours for GPT-2-scale collapse validation across three conditions looks especially high given that GPT-2 is only around 117M parameters, and the 90 hours for auxiliary ablations adds more overhead. This totals roughly 490 A100-hours or 163 H100-equivalent hours, which fits within the 200-hour hard constraint when mandatory work is 163 hours plus 20-30 hours of optional Llama experiments, landing at 183-193 hours with some contingency buffer.

But I'm noticing an inconsistency in how the auto_research estimate frames this—it lists 490 A100-hours as equivalent to 163 H100-equivalent hours mandatory, but the conversion math doesn't quite line up when I divide 490 by 3.

Actually, let me recalculate: if H100 is roughly 3x faster than A100, then 490 ÷ 3 ≈ 163 H100-equivalent hours, which checks out. So the mandatory 163 hours sits within the 200-hour constraint with a 37-hour buffer, and adding the optional Llama work (60-90 A100-hours = 20-30 H100-equivalent) brings the total to 183-193 hours. The issue is that the contingency triggers at 160 H100-equivalent hours, but the mandatory work alone is already 163 hours—so the contingency should have already been triggered before even starting the optional Llama experiments. ), which is contradictory. Wait, let me re-read.

"executed only if compute budget remains below 160h H100-equivalent at Day 10; otherwise deprioritized to zero-shot depth scoring only, maintaining a genuine 40h safety buffer against the 200h hard ceiling"

So the plan is:
- Mandatory work: 163h H100-equivalent
- Optional Llama: 20-30h H100-equivalent
- Total with optional: 183-193h H100-equivalent

But the contingency says "if compute budget remains below 160h H100-equivalent at Day 10" - this means "if usage is below 160h." Since mandatory alone is 163h, by Day 10, usage would be above 160h already (since most mandatory experiments would have run). This means the optional Llama work would always be deprioritized! That seems contradictory.

Actually, I think I'm misunderstanding the timeline. The mandatory work is spread across concurrent runs over 10 days, so not all 163h H100-equivalent would be consumed by Day 10 if some ablations haven't finished yet. The 160h threshold is checking whether we're still under budget at that checkpoint, and if we are, we can proceed with the optional work. If we've already burned through more than 160h by then, we scale back to just the zero-shot scoring to preserve the safety margin.

That makes more sense - it's a mid-project checkpoint to decide whether to proceed with optional experiments or conserve resources. The proposal is sound enough.

Now looking at the remaining technical concerns: the core risk is whether a 0.6B model can meaningfully distinguish between Gen1 and Gen2 outputs after just one fine-tuning step on 200K documents. The Wall of Separation paper suggests AI-AI divergence is already quite small, and within-model generational divergence would be even smaller. The dual null-hypothesis design provides a fallback if the experiment fails, but the fundamental question remains whether the classification AUC will be meaningful at all at this scale. There's also a concern about whether the 240h A100 estimate for GPT-2-scale collapse validation across three conditions is realistic. 200K documents at 512 tokens = 102M tokens typically takes a few hours at most, not 80h per condition.
   - The 120h for DeBERTa ablations also seems high but is plausible with hyperparameter search.

3. **"Qwen3.5" issue**: Wait, the proposal correctly uses "Qwen3-0.6B" throughout - this was fixed in Round 1.

4. **Key new papers I should look for**: The search found arXiv:2505.11550 "AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification" - is this relevant? And "Multi-modal Synthetic Data Training and Model Collapse" arXiv:2505.08803 from May 2026.

Let me think more carefully about what new issues might emerge in round 8 that weren't caught in round 7:

**Potential new Issue 1**: The compute estimate breaks down correctly to 490h A100 total (40h corpus generation + 120h DeBERTa ablations + 240h GPT-2-scale validation + 90h auxiliary), but when I trace through the GPT-2-scale collapse validation with 9 training runs on 102M tokens each, the per-run timing doesn't quite add up to the claimed 240h allocation.

**Potential new Issue 2**: arXiv:2505.11550 might be relevant for multiclass classification of generational depth, but the search results don't specify if it actually distinguishes between different levels of collapse.

**Potential new Issue 3**: The "MAUVE-" metric discussion seems cut off in the proposal.

**Potential new Issue 4**: The proposal references "Strong Model Collapse (ICLR 2025)" multiple times but doesn't include the arXiv identifier—I'm trying to verify if this corresponds to arXiv:2405.05086 by Nicolas Flammarion et al., which was accepted to ICLR 2025.

**Potential new Issue 5**: Looking at the compute budget more carefully, the mandatory portion requires 163h H100-equivalent, which already exceeds the 160h contingency threshold by Day 10, so the optional Llama component would automatically be cut regardless—this is actually the intended behavior.

But re-reading the contingency language, it's ambiguous whether "remains below 160h" refers to actual usage so far or projected total usage. If it's actual usage at Day 10, then with most mandatory compute already consumed (140-150h of 163h), there's a narrow window where Llama could still be included, though this creates a marginally tight constraint that's worth noting but not a dealbreaker. that doesn't quite make sense either since the mandatory is already 163h.

OR it means "if actual compute usage at Day 10 is below 160h H100-equivalent" - meaning if experiments have been running efficiently and you're under 160h by Day 10, then add Llama. This makes more sense as a dynamic decision point.

Either way, this was flagged in Round 4 and was resolved by changing the threshold from 180h to 160h and making Llama "explicitly optional from the start." The auto_research section reads:

"Llama-3.2-1B recursive corpus generation and collapse experiments (~60-90h A100 / ~20-30h H100-equivalent) are explicitly optional from the start: executed only if compute budget remains below 160h H100-equivalent at Day 10; otherwise deprioritized to zero-shot depth scoring only, maintaining a genuine 40h safety buffer against the 200h hard ceiling."

This is not quite logically consistent - if mandatory is 163h H100-equivalent, how can budget remain below 160h at Day 10? Unless some of the 163h mandatory compute runs concurrently and the measurement is different, but that's a minor bookkeeping issue that doesn't affect the core research design.

Now I'm checking what genuinely new issues might exist in Round 8. The 512-token cap is fixed, arXiv:2602.10531 is cited. For potential new problems, the proposal cites arXiv:2604.08554 on drift in LLM text ecosystems and addresses it appropriately. I'm also examining whether the proposal handles the "Wall of Separation" counter-argument consistently - the claim that surface-level signals won't work is confirmed by arXiv:2605.01647, but I need to verify the embedding-space approach is properly justified.

The logical chain connecting transformers to n-gram statistics through arXiv:2407.12034 (showing 68-79% agreement), then linking that to monotonic drift accumulation from arXiv:2604.08554, seems sound and correctly acknowledges the modeling gap. Now I'm looking at whether using GPT-2-scale models for the collapse validation experiments is appropriate given the research goals.

There's also a statistical power concern with the proposed paired t-test design across only 3 random seeds. With such a small sample size, detecting modest effect sizes (like a 10% perplexity difference between contamination conditions) would be unlikely, so failing to reject the null hypothesis might just reflect insufficient statistical power rather than a true null effect.

The ordinal regression approach for DeBERTa isn't clearly specified either—the proposal mentions training an ordinal regression head over the joint representation but doesn't clarify whether this uses standard softmax classification, Coral regression, or another method, which could be a point of confusion for reviewers.

I'm also checking a recent paper on AI-generated text detection that might directly overlap with this work's multi-class classification approach.

Looking at my overall assessment: the proposal has genuinely improved across multiple rounds, the key citations check out, and the novelty claim holds—no existing work combines ordinal generational depth scoring for corpus decontamination. The main remaining technical question is whether the model can actually distinguish between first and second-generation synthetic text.

I'm noting a few minor methodological gaps: the statistical power with only 3 seeds is limited, the ordinal regression head isn't fully specified, and there's a small inconsistency in the compute budget description. I should also verify whether that one paper on AI-generated text detection actually addresses generational depth classification, but given how far this proposal has come through revision, I'm fairly confident it's addressing a genuine gap in the literature.

Now I'm weighing the overall scores: the novelty is solid at 4/5 since no competing work exists on ordinal generational depth scoring, though there's still some uncertainty about whether the same 0.6B model can actually discriminate between Gen1 and Gen2. The feasibility sits at 3.5/5—the 16-day timeline is aggressive but the dual null-hypothesis structure ensures a publishable result regardless of outcome, and the 512-token cap keeps generation deterministic. Clarity is strong at 4/5 with the concrete architecture and day-by-day critical path well-defined. Impact lands at 3.5/5 given the solid alignment with EMNLP's special theme and real governance applications. The question now is whether this passes or needs another round of revision.

The average comes to about 3.75/5, which falls short of the 4.0 threshold. But before I conclude it needs revision, I should check whether there are any genuinely critical issues that emerged in this round. I'm particularly concerned about a recent paper on AI-generated text detection that the search agent flagged but isn't cited in the proposal—I need to verify whether it actually addresses generational depth classification. There's also the statistical power question with only 3 seeds for the paired t-test, which is quite underpowered, though this concern carried over from the previous round.

Looking back at the design history, the 3-seed limitation has been there since Round 3 as part of the 16-day compute budget constraint. With only 2 degrees of freedom, detecting even a 20% difference in collapse severity becomes nearly impossible if variance is high. This is a real methodological weakness—the secondary null about collapse severity parity might not actually be null, just undetectable with this sample size. The proposal does acknowledge this as an explicit trade-off, but it's worth flagging whether this undermines the core claims about effect existence.

Actually, 3 seeds aligns with standard practice in the collapse literature, so this isn't unusual. Let me search more carefully for competing work on generational depth scoring to see if the novelty claim holds up. Based on what I'm finding, no other paper has tackled this specific angle, and the proposal has addressed all the Round 7 concerns. The core contribution appears genuinely novel.

Now I'm weighing whether to pass or request revisions. The methodology is well-specified, the timeline is tight but feasible with parallel work, and the dual null-hypothesis design ensures a publishable result regardless of outcome. The main hesitations are whether arXiv:2505.11550 needs citation if it covers related classification work, the statistical power of paired t-tests with 3 seeds, and a few minor specification gaps like the ordinal regression head type. But these feel like polish rather than fundamental issues.

Scoring it out: the novelty is genuinely strong at 4/5—ordinal generational depth scoring for decontamination hasn't been proposed before, though the critical unknown is whether Gen1/Gen2 discriminability will actually be detectable. Feasibility lands at 4/5 now that the critical path is anchored, despite the tight 16-day window and some concerns about statistical power and compute scaling relative to the 25M-token corpus. Clarity is solid at 4/5 with the architecture well-specified through DeBERTa and scalar outputs.

For impact, I'm settling on 4/5—the EMNLP 2026 governance angle is genuinely important and the dual null-hypothesis ensures publishability, but the limitation to GPT-2 scale and the possibility of a negative finding (that simple filtering suffices) tempers the external validity. Now I'm second-guessing whether these scores are running too high given the instruction about agent inflation.

Novelty holds at 4/5—the depth-stratified decontamination question is clearly the right one to ask in the model collapse space. For feasibility, I'm landing on 3.5/5 because while the 16-day timeline is aggressive and the three seeds for collapse validation feel underpowered, the compute budget fits within constraints. The real bottleneck is whether the model can actually distinguish between Gen1 and Gen2 outputs—that's the core uncertainty that keeps this from being a solid 4.

Clarity scores 4/5 with the dual null hypotheses, day-by-day critical path, and concrete compute estimates all well-specified, though the ordinal regression approach could be more explicit. Impact lands at 3.5/5 because while this addresses a genuine governance question and aligns with EMNLP 2026 priorities, the small scale (GPT-2, 0.6B generators) and potential null findings limit the upside. The 74.2% contamination statistic does ground this in real-world relevance though.

Averaging these out gives 3.75, which falls short of the 4.0 pass threshold and points toward revision. The question is what actually moves the needle here.

Given this is round 8 of 10, I'm focusing on the most critical remaining gaps: whether arXiv:2505.11550 already tackles generational depth classification (which would make it a direct competitor requiring citation), the underpowered 3-seed paired t-test setup, and the minor ordinal regression specification gap. The arXiv paper check is the priority since that determines whether there's a citation obligation.

Looking at the search results more carefully, arXiv:2505.11550 classifies text as human versus AI-generated and potentially identifies which model generated it—but that's fundamentally different from my approach of classifying by generational depth, which measures how many recursive training iterations removed from human text the content is. So this isn't a direct competitor after all. Now I should also consider whether to track down that other paper on multi-modal synthetic data and model collapse. , May 2026). This seems to be about image models (VLMs, diffusion), not text, so probably not relevant.

At this point, I think the proposal is close to passing. The main remaining weaknesses are:
1. The statistical power issue (3 seeds) - inherent to compute budget
2. The ordinal regression type unspecified - minor
3. The core technical risk (Gen1/Gen2 discriminability from 0.6B model) remains an open empirical question

These are known limitations, not new critical issues. The proposal has a good dual null-hypothesis design that handles the failure cases.

**My verdict: revise** with specific feedback:

Issues to flag:
1. **New paper: arXiv:2505.11550** - "AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification" (May 2026) should be checked and potentially cited, though it's likely orthogonal to this work since it focuses on model identity classification rather than generational depth. An area chair might still raise it as a concern. (Minor issue)

2. **Statistical power of 3-seed paired t-test**: With N=3, df=2, the critical t-value for α=0.05 two-tailed is 4.303, requiring a very large effect size (Cohen's d ≈ 2.5) to achieve 80% power. If collapse severity differs modestly between conditions (b) and (c), the secondary null finding about collapse severity parity might just reflect insufficient power rather than a genuine null effect. The proposal should acknowledge this limitation explicitly. (Minor issue)

3. **Ordinal regression head type unspecified**: The approach mentions "ordinal regression head" without specifying which variant—whether it's Coral-loss based, proportional odds model, or something simpler. softmax over 3 ordered classes). This affects replicability. (Minor issue, one sentence fix)

Actually, on reconsideration, let me think about what truly warrants a "revise" vs "pass" verdict at round 8.

The round 7 feedback said: "Both fixes require under 30 minutes of writing and no new experiments." The round 8 proposal has addressed both fixes. The question is: are there genuinely new issues that weren't present in round 7 or that emerge from reading the round 8 proposal?

I've found three potential issues, all minor:
1. arXiv:2505.11550 - needs to be checked (probably not a direct competitor)
2. Statistical power of 3-seed test - inherent to compute budget, should be acknowledged
3. Ordinal regression type unspecified

None of these are critical issues. The proposal has a novel, verified idea with well-specified methodology, correct compute estimates within budget, strong venue alignment, a dual null-hypothesis design covering all outcomes, and confirmed existence of all cited papers.

Now I'm weighing whether the remaining issues are truly critical or just minor. Looking at my scoring: Novelty is 4, Clarity is 4, Impact is 4, but Feasibility is 3.5 due to the tight 16-day timeline and uncertain discriminability. That averages to 3.875, which falls below the 4.0 pass threshold. The core question is whether that feasibility score should actually be 4.0 given the sequential bottleneck constraints.

The deterministic generation times and dual null-hypothesis design do mitigate risk substantially. But the discriminability uncertainty is real, and the "Wall of Separation" directly challenges whether Gen1 and Gen2 outputs from the same model are actually distinguishable. I think 3.5 is the right call here—it reflects genuine uncertainty without being overly pessimistic.

So my verdict is revise, and I should flag the three minor issues that need addressing.

Actually, wait—let me think through the compute contingency more carefully. The "160h H100-equivalent at Day 10" trigger doesn't quite align with the timeline. By Day 10, we're only partway through the mandatory experiments: corpus construction wraps early, DeBERTa runs through Day 8, and the collapse experiments are just ramping up. So the contingency threshold needs to account for the fact that not all 163h of mandatory compute would have been spent yet. This is a real inconsistency that should be clarified in the revision. Looking at the compute timeline more carefully — the contingency logic hinges on staying below 160h by Day 10, which means the cumulative usage at that checkpoint, not the final projection. By that point, the corpus work, DeBERTa experiments, and collapse studies would total around 103-108h H100-equivalent, leaving room for the optional Llama work while staying within the 200h budget overall.

Now I'm evaluating the proposal's statistical rigor and finding two key issues that need addressing. The secondary hypothesis test using only three seeds has extremely low power — with a critical t-value of 4.303, it would require an implausibly large effect size to reject the null, so the proposal should acknowledge upfront that non-rejection might reflect insufficient statistical power rather than a true null result. Additionally, the ordinal regression head is mentioned but the specific implementation method isn't defined, whether that's CORAL loss, ordinal binary cross-entropy decomposition, or proportional odds logistic regression. I'm realizing the ordinal regression head type is actually a genuine gap that wasn't caught in previous rounds—the architecture was specified (concatenating features to CLS for a 1029-dim representation) but not which method to use (softmax, CORAL, regression). The ForTIFAI paper timing checks out since it's been referenced since Round 4. Now I'm settling on final scores: novelty at 4/5 for the ordinal generational depth approach with no competing work, and feasibility at 3...

5/5 given the aggressive 16-day timeline and uncertainty around the "Wall of Separation" discriminability, though the dual null-hypothesis framing and deterministic 512-token cap help mitigate risk. Clarity drops to 4/5 specifically because of that unspecified head type, and impact stays strong at 4/5 for EMNLP 2026 alignment. That averages to 3.875, below the 4.0 threshold, so revision is needed. The main issues are the statistical power problem—three seeds gives only 2 degrees of freedom with a critical t-value of 4.303, making the paired t-test underpowered for detecting moderate effects—and the ordinal head specification gap that needs explicit clarification on whether it's CORAL, softmax ordinal regression, or another approach.

Both are fixable with targeted one-sentence additions. Before I finalize the JSON, let me quickly check arXiv:2505.11550 to make sure it's not a direct competitor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0c9ab5c-facc-40fb-ab93-90975e684dcb",
  "isSidechain": false,
  "requestId": "req_011CasgAXN7uYvoHrAvsWdb2",
  "type": "assistant",
  "uuid": "0daef8a1-2838-4676-9979-efb7aa5c5b7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GQ3pxiw5SKmU3nRVMtMWQQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5386,
      "cache_read_input_tokens": 37218,
      "output_tokens": 9580,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9580,
          "cache_read_input_tokens": 37218,
          "cache_creation_input_tokens": 5386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5386
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

_source line 17 · 2026-05-09T21:09:34.037Z_

Let me do one more targeted search to check the potentially relevant May 2026 paper and look for any other new competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0daef8a1-2838-4676-9979-efb7aa5c5b7e",
  "isSidechain": false,
  "requestId": "req_011CasgAXN7uYvoHrAvsWdb2",
  "type": "assistant",
  "uuid": "3e111af6-7e50-4136-ab4b-e45f6380d590",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GQ3pxiw5SKmU3nRVMtMWQQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5386,
      "cache_read_input_tokens": 37218,
      "output_tokens": 9580,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9580,
          "cache_read_input_tokens": 37218,
          "cache_creation_input_tokens": 5386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5386
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

_source line 18 · 2026-05-09T21:09:42.368Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011gZCi6HUxMG2mP7Hg5haSy`</summary>

```json
{
  "description": "Check arXiv:2505.11550 and search for other May 2026 competing papers",
  "subagent_type": "Explore",
  "prompt": "I need to check a specific paper and search for competing work to a research idea about \"generational depth scoring\" for AI text detection. The core idea is classifying AI-generated text by generational depth (Gen0=human, Gen1=AI-generated, Gen2=AI trained on AI outputs generating more text) to prioritize corpus decontamination.\n\nPlease do the following:\n\n1. Search for arXiv:2505.11550 - \"AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification\" (May 2026). Use WebSearch: `arxiv 2505.11550 AI-generated text detection multiclass classification`. What does this paper classify? Does it classify by GENERATIONAL DEPTH (which recursive generation step) or by WHICH MODEL generated the text? Report as much detail as you can find.\n\n2. Search for any papers on \"recursive generation depth\" + \"text classification\": `arxiv recursive generation depth AI text classification 2025 2026`\n\n3. Search: `arxiv second-generation synthetic text detection 2025 2026`\n\n4. Search for ordinal regression for AI text classification: `arxiv ordinal regression AI-generated text detection`\n\n5. Search: `site:openreview.net generational depth synthetic data EMNLP 2026` OR `site:openreview.net model collapse detection 2026`\n\n6. Search: `arxiv CORAL ordinal regression text classification DeBERTa` to understand typical implementation of ordinal regression heads for NLP tasks.\n\nPlease be thorough and report what you find for each search. I specifically need to know if arXiv:2505.11550 does generational depth classification (classifying by number of recursive training steps) vs. just classifying by which AI model produced the text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e111af6-7e50-4136-ab4b-e45f6380d590",
  "isSidechain": false,
  "requestId": "req_011CasgAXN7uYvoHrAvsWdb2",
  "type": "assistant",
  "uuid": "145b93d5-75f1-4912-becf-dde103ac1e1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GQ3pxiw5SKmU3nRVMtMWQQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5386,
      "cache_read_input_tokens": 37218,
      "output_tokens": 9580,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9580,
          "cache_read_input_tokens": 37218,
          "cache_creation_input_tokens": 5386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5386
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "145b93d5-75f1-4912-becf-dde103ac1e1a",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Genealogical depth scoring for recursive text decontamination",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a"
}
```

---

### Tool result

_source line 21 · 2026-05-09T21:10:49.660Z_

<details><summary>↩ Tool result · `toolu_011gZCi6HUxMG2mP7Hg5haSy`</summary>

```text
Perfect. Now let me compile a comprehensive report of my findings.

## Summary of Research on Generational Depth Scoring for AI-Generated Text Detection

Based on my thorough search, here's what I found regarding your research idea and competing work:

### 1. **ArXiv:2505.11550 - CRITICAL FINDING**

**Classification Approach: MODEL ATTRIBUTION (NOT Generational Depth)**

The paper ["AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification" (arXiv:2505.11550)](https://arxiv.org/abs/2505.11550) does **NOT** classify by generational depth. Instead:

- **Task A (Binary):** Distinguishes human-authored vs. AI-generated text
- **Task B (Multiclass):** Performs **model attribution** with 7 classes: Gemma-2-7B, GPT-4-o, Human, LLaMA-8B, Mistral-7B, Qwen-2-72B, and Yi-large

The multiclass labels represent different LLM sources plus human text, not recursive generation steps (Gen0, Gen1, Gen2, etc.). This means 2505.11550 is solving a different problem from your generational depth scoring idea.

### 2. **Recursive Generation & Generational Depth Research (HIGHLY RELEVANT)**

I found substantial recent work on recursive training and generation degradation that directly supports the motivation for your approach:

- **["Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training" (arXiv:2509.04796)](https://arxiv.org/abs/2509.04796)** - Shows a three-stage knowledge collapse phenomenon where factual accuracy deteriorates while fluency persists during recursive training
- **["Human–AI Co-Evolution and Epistemic Collapse: A Dynamical Systems Perspective" (arXiv:2605.06347)](https://arxiv.org/html/2605.06347v1)** - Analyzes coupled feedback loops between humans and models leading to distributional degeneration
- **["From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources" (arXiv:2602.10531)](https://arxiv.org/abs/2602.10531)** - February 2026 paper on iterative training with contaminated/synthetic data
- **["A theoretical basis for model collapse in recursive training" (arXiv:2506.09401)](https://arxiv.org/abs/2506.09401)** - Provides theoretical foundations for understanding recursive generation failures

These papers establish that **recursive generation creates detectable quality degradation patterns**, which is the foundation for your generational depth scoring idea.

### 3. **Model Collapse & Data Decontamination**

Several papers address preventing model collapse through data filtering:

- **["Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence" (arXiv:2510.16657)](https://arxiv.org/abs/2510.16657)** - October 2025 paper proposing synthetic data verification to prevent collapse
- **["Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" (arXiv:2404.01413)](https://arxiv.org/abs/2404.01413)** - Shows mixing real and synthetic data can prevent collapse
- **["A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective" (arXiv:2509.16499)](https://arxiv.org/html/2509.16499v1)** - Analyzes collapse mechanisms

**Key insight:** These papers discuss data contamination remediation but don't specifically address **detecting and scoring generational depth** for corpus decontamination prioritization—your novel angle.

### 4. **AI-Generated Text Detection (Baseline Methods)**

- **["Diversity Boosts AI-Generated Text Detection" (arXiv:2509.18880)](https://arxiv.org/abs/2509.18880)** - February 2026 paper proposing DivEye framework using surprisal-based features. Shows human text has richer variability than LLM outputs (relevant to your degradation hypothesis)
- **["A Comprehensive Dataset for Human vs. AI Generated Text Detection" (arXiv:2510.22874)](https://arxiv.org/abs/2510.22874)** - March 2026 multimodel dataset with 58,000+ samples
- **["Can AI-Generated Text be Reliably Detected?" (arXiv:2303.11156)](https://arxiv.org/abs/2303.11156)** - Foundational work on detectability limits

### 5. **Ordinal Regression Methods (Technical Implementation)**

I found limited papers combining ordinal regression with NLP specifically:

- **["Rank consistent ordinal regression for neural networks with application to age estimation" (arXiv:1901.07884)](https://arxiv.org/abs/1901.07884)** - Core CORAL paper establishing rank-consistent ordinal regression
- **["Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities" (arXiv:2111.08851)](https://arxiv.org/abs/2111.08851)** - Extended CORAL framework
- **[CORAL-PyTorch implementations on GitHub](https://github.com/Raschka-research-group/coral-pytorch)** - Reference implementations available

**Note:** I did not find papers combining CORAL ordinal regression with DeBERTa for text classification, suggesting this could be a novel technical contribution.

### 6. **Quality Degradation & Generation Levels**

- **["Quality Degradation Attack in Synthetic Data" (arXiv:2601.02947)](https://arxiv.org/abs/2601.02947)** - January 2026 paper on quality degradation in synthetic data generation pipelines
- **["Controlled Automatic Task-Specific Synthetic Data Generation for Hallucination Detection" (arXiv:2410.12278)](https://arxiv.org/html/2410.12278)** - Shows hallucinations increase in multi-generation synthetic pipelines

### 7. **OpenReview & Workshop Results**

I searched OpenReview for papers on "generational depth" but found no directly matching papers. However, I found:

- **["Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"](https://openreview.net/forum?id=Xr5iINA3zU)** - Discusses feedback loops in self-generating systems
- **ICLR 2026 Workshop on AI with Recursive Self-Improvement** - Indicates this is an emerging research area

### Key Findings & Competitive Landscape

**Your research idea appears NOVEL:**

1. **2505.11550 is NOT competing work** - It classifies by model attribution, not generational depth
2. **No papers found explicitly classifying by generational depth** (Gen0, Gen1, Gen2 recursive levels) specifically for corpus decontamination prioritization
3. **Strong theoretical foundation exists** for why generational depth matters (model collapse, epistemic degradation, knowledge decay papers from 2025-2026)
4. **Technical gap:** Ordinal regression (CORAL) is established for ranking problems, but combining it with modern NLP architectures (DeBERTa) for generational depth classification appears unexplored

**Closest related work:**
- Knowledge Collapse detection (but not by generational depth classification)
- Model attribution detection (2505.11550, but different task)
- Diversity/quality-based detection (DivEye) - orthogonal approach
- Hallucination detection in synthetic data - related but different focus

**Recommendation:** Your generational depth scoring idea appears to be filling a genuine gap in the literature. The motivation is well-supported by 2025-2026 research on model collapse and recursive training degradation, but the specific problem of **classifying text by recursive generation depth for decontamination prioritization** does not appear to be addressed in existing work.

Sources:
- [arXiv:2505.11550 - AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification](https://arxiv.org/abs/2505.11550)
- [arXiv:2509.04796 - Knowledge Collapse in LLMs](https://arxiv.org/abs/2509.04796)
- [arXiv:2605.06347 - Human–AI Co-Evolution and Epistemic Collapse](https://arxiv.org/html/2605.06347v1)
- [arXiv:2602.10531 - From Collapse to Improvement](https://arxiv.org/abs/2602.10531)
- [arXiv:2506.09401 - A theoretical basis for model collapse in recursive training](https://arxiv.org/abs/2506.09401)
- [arXiv:2510.16657 - Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657)
- [arXiv:2509.18880 - Diversity Boosts AI-Generated Text Detection](https://arxiv.org/abs/2509.18880)
- [arXiv:2510.22874 - A Comprehensive Dataset for Human vs. AI Generated Text Detection](https://arxiv.org/abs/2510.22874)
- [arXiv:2303.11156 - Can AI-Generated Text be Reliably Detected?](https://arxiv.org/abs/2303.11156)
- [arXiv:1901.07884 - Rank consistent ordinal regression for neural networks](https://arxiv.org/abs/1901.07884)
- [arXiv:2111.08851 - Deep Neural Networks for Rank-Consistent Ordinal Regression](https://arxiv.org/abs/2111.08851)
- [arXiv:2601.02947 - Quality Degradation Attack in Synthetic Data](https://arxiv.org/abs/2601.02947)
- [OpenReview - Collapse or Thrive? Perils and Promises of Synthetic Data](https://openreview.net/forum?id=Xr5iINA3zU)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "145b93d5-75f1-4912-becf-dde103ac1e1a",
  "isSidechain": false,
  "promptId": "b7cb083a-c29c-412a-9da3-a7aaa46c6957",
  "type": "user",
  "uuid": "6b1a9c7f-e321-4ee6-a4f4-b9e81a8da856",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to check a specific paper and search for competing work to a research idea about \"generational depth scoring\" for AI text detection. The core idea is classifying AI-generated text by generational depth (Gen0=human, Gen1=AI-generated, Gen2=AI trained on AI outputs generating more text) to prioritize corpus decontamination.\n\nPlease do the following:\n\n1. Search for arXiv:2505.11550 - \"AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification\" (May 2026). Use WebSearch: `arxiv 2505.11550 AI-generated text detection multiclass classification`. What does this paper classify? Does it classify by GENERATIONAL DEPTH (which recursive generation step) or by WHICH MODEL generated the text? Report as much detail as you can find.\n\n2. Search for any papers on \"recursive generation depth\" + \"text classification\": `arxiv recursive generation depth AI text classification 2025 2026`\n\n3. Search: `arxiv second-generation synthetic text detection 2025 2026`\n\n4. Search for ordinal regression for AI text classification: `arxiv ordinal regression AI-generated text detection`\n\n5. Search: `site:openreview.net generational depth synthetic data EMNLP 2026` OR `site:openreview.net model collapse detection 2026`\n\n6. Search: `arxiv CORAL ordinal regression text classification DeBERTa` to understand typical implementation of ordinal regression heads for NLP tasks.\n\nPlease be thorough and report what you find for each search. I specifically need to know if arXiv:2505.11550 does generational depth classification (classifying by number of recursive training steps) vs. just classifying by which AI model produced the text.",
    "agentId": "a907931b560a9fbbc",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now let me compile a comprehensive report of my findings.\n\n## Summary of Research on Generational Depth Scoring for AI-Generated Text Detection\n\nBased on my thorough search, here's what I found regarding your research idea and competing work:\n\n### 1. **ArXiv:2505.11550 - CRITICAL FINDING**\n\n**Classification Approach: MODEL ATTRIBUTION (NOT Generational Depth)**\n\nThe paper [\"AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification\" (arXiv:2505.11550)](https://arxiv.org/abs/2505.11550) does **NOT** classify by generational depth. Instead:\n\n- **Task A (Binary):** Distinguishes human-authored vs. AI-generated text\n- **Task B (Multiclass):** Performs **model attribution** with 7 classes: Gemma-2-7B, GPT-4-o, Human, LLaMA-8B, Mistral-7B, Qwen-2-72B, and Yi-large\n\nThe multiclass labels represent different LLM sources plus human text, not recursive generation steps (Gen0, Gen1, Gen2, etc.). This means 2505.11550 is solving a different problem from your generational depth scoring idea.\n\n### 2. **Recursive Generation & Generational Depth Research (HIGHLY RELEVANT)**\n\nI found substantial recent work on recursive training and generation degradation that directly supports the motivation for your approach:\n\n- **[\"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\" (arXiv:2509.04796)](https://arxiv.org/abs/2509.04796)** - Shows a three-stage knowledge collapse phenomenon where factual accuracy deteriorates while fluency persists during recursive training\n- **[\"Human–AI Co-Evolution and Epistemic Collapse: A Dynamical Systems Perspective\" (arXiv:2605.06347)](https://arxiv.org/html/2605.06347v1)** - Analyzes coupled feedback loops between humans and models leading to distributional degeneration\n- **[\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\" (arXiv:2602.10531)](https://arxiv.org/abs/2602.10531)** - February 2026 paper on iterative training with contaminated/synthetic data\n- **[\"A theoretical basis for model collapse in recursive training\" (arXiv:2506.09401)](https://arxiv.org/abs/2506.09401)** - Provides theoretical foundations for understanding recursive generation failures\n\nThese papers establish that **recursive generation creates detectable quality degradation patterns**, which is the foundation for your generational depth scoring idea.\n\n### 3. **Model Collapse & Data Decontamination**\n\nSeveral papers address preventing model collapse through data filtering:\n\n- **[\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\" (arXiv:2510.16657)](https://arxiv.org/abs/2510.16657)** - October 2025 paper proposing synthetic data verification to prevent collapse\n- **[\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\" (arXiv:2404.01413)](https://arxiv.org/abs/2404.01413)** - Shows mixing real and synthetic data can prevent collapse\n- **[\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\" (arXiv:2509.16499)](https://arxiv.org/html/2509.16499v1)** - Analyzes collapse mechanisms\n\n**Key insight:** These papers discuss data contamination remediation but don't specifically address **detecting and scoring generational depth** for corpus decontamination prioritization—your novel angle.\n\n### 4. **AI-Generated Text Detection (Baseline Methods)**\n\n- **[\"Diversity Boosts AI-Generated Text Detection\" (arXiv:2509.18880)](https://arxiv.org/abs/2509.18880)** - February 2026 paper proposing DivEye framework using surprisal-based features. Shows human text has richer variability than LLM outputs (relevant to your degradation hypothesis)\n- **[\"A Comprehensive Dataset for Human vs. AI Generated Text Detection\" (arXiv:2510.22874)](https://arxiv.org/abs/2510.22874)** - March 2026 multimodel dataset with 58,000+ samples\n- **[\"Can AI-Generated Text be Reliably Detected?\" (arXiv:2303.11156)](https://arxiv.org/abs/2303.11156)** - Foundational work on detectability limits\n\n### 5. **Ordinal Regression Methods (Technical Implementation)**\n\nI found limited papers combining ordinal regression with NLP specifically:\n\n- **[\"Rank consistent ordinal regression for neural networks with application to age estimation\" (arXiv:1901.07884)](https://arxiv.org/abs/1901.07884)** - Core CORAL paper establishing rank-consistent ordinal regression\n- **[\"Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities\" (arXiv:2111.08851)](https://arxiv.org/abs/2111.08851)** - Extended CORAL framework\n- **[CORAL-PyTorch implementations on GitHub](https://github.com/Raschka-research-group/coral-pytorch)** - Reference implementations available\n\n**Note:** I did not find papers combining CORAL ordinal regression with DeBERTa for text classification, suggesting this could be a novel technical contribution.\n\n### 6. **Quality Degradation & Generation Levels**\n\n- **[\"Quality Degradation Attack in Synthetic Data\" (arXiv:2601.02947)](https://arxiv.org/abs/2601.02947)** - January 2026 paper on quality degradation in synthetic data generation pipelines\n- **[\"Controlled Automatic Task-Specific Synthetic Data Generation for Hallucination Detection\" (arXiv:2410.12278)](https://arxiv.org/html/2410.12278)** - Shows hallucinations increase in multi-generation synthetic pipelines\n\n### 7. **OpenReview & Workshop Results**\n\nI searched OpenReview for papers on \"generational depth\" but found no directly matching papers. However, I found:\n\n- **[\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"](https://openreview.net/forum?id=Xr5iINA3zU)** - Discusses feedback loops in self-generating systems\n- **ICLR 2026 Workshop on AI with Recursive Self-Improvement** - Indicates this is an emerging research area\n\n### Key Findings & Competitive Landscape\n\n**Your research idea appears NOVEL:**\n\n1. **2505.11550 is NOT competing work** - It classifies by model attribution, not generational depth\n2. **No papers found explicitly classifying by generational depth** (Gen0, Gen1, Gen2 recursive levels) specifically for corpus decontamination prioritization\n3. **Strong theoretical foundation exists** for why generational depth matters (model collapse, epistemic degradation, knowledge decay papers from 2025-2026)\n4. **Technical gap:** Ordinal regression (CORAL) is established for ranking problems, but combining it with modern NLP architectures (DeBERTa) for generational depth classification appears unexplored\n\n**Closest related work:**\n- Knowledge Collapse detection (but not by generational depth classification)\n- Model attribution detection (2505.11550, but different task)\n- Diversity/quality-based detection (DivEye) - orthogonal approach\n- Hallucination detection in synthetic data - related but different focus\n\n**Recommendation:** Your generational depth scoring idea appears to be filling a genuine gap in the literature. The motivation is well-supported by 2025-2026 research on model collapse and recursive training degradation, but the specific problem of **classifying text by recursive generation depth for decontamination prioritization** does not appear to be addressed in existing work.\n\nSources:\n- [arXiv:2505.11550 - AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification](https://arxiv.org/abs/2505.11550)\n- [arXiv:2509.04796 - Knowledge Collapse in LLMs](https://arxiv.org/abs/2509.04796)\n- [arXiv:2605.06347 - Human–AI Co-Evolution and Epistemic Collapse](https://arxiv.org/html/2605.06347v1)\n- [arXiv:2602.10531 - From Collapse to Improvement](https://arxiv.org/abs/2602.10531)\n- [arXiv:2506.09401 - A theoretical basis for model collapse in recursive training](https://arxiv.org/abs/2506.09401)\n- [arXiv:2510.16657 - Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657)\n- [arXiv:2509.18880 - Diversity Boosts AI-Generated Text Detection](https://arxiv.org/abs/2509.18880)\n- [arXiv:2510.22874 - A Comprehensive Dataset for Human vs. AI Generated Text Detection](https://arxiv.org/abs/2510.22874)\n- [arXiv:2303.11156 - Can AI-Generated Text be Reliably Detected?](https://arxiv.org/abs/2303.11156)\n- [arXiv:1901.07884 - Rank consistent ordinal regression for neural networks](https://arxiv.org/abs/1901.07884)\n- [arXiv:2111.08851 - Deep Neural Networks for Rank-Consistent Ordinal Regression](https://arxiv.org/abs/2111.08851)\n- [arXiv:2601.02947 - Quality Degradation Attack in Synthetic Data](https://arxiv.org/abs/2601.02947)\n- [OpenReview - Collapse or Thrive? Perils and Promises of Synthetic Data](https://openreview.net/forum?id=Xr5iINA3zU)"
      }
    ],
    "totalDurationMs": 67287,
    "totalTokens": 28468,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 719,
      "cache_creation_input_tokens": 1884,
      "cache_read_input_tokens": 23385,
      "output_tokens": 2480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 719,
          "output_tokens": 2480,
          "cache_read_input_tokens": 23385,
          "cache_creation_input_tokens": 1884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1884,
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
  "sourceToolAssistantUUID": "145b93d5-75f1-4912-becf-dde103ac1e1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-09T21:11:54.613Z_

<details><summary>Logged reasoning block</summary>

```text
The research confirms:
1. arXiv:2505.11550 classifies by model attribution (which AI model generated it), not generational depth. It is NOT a direct competitor.
2. No papers found on generational depth scoring for corpus decontamination - novelty confirmed.
3. The CORAL ordinal regression framework exists (arXiv:1901.07884, arXiv:2111.08851) and is available as a library.
4. Several new papers found: arXiv:2509.04796 (Knowledge Collapse in LLMs), arXiv:2506.09401 (theoretical basis for model collapse), arXiv:2605.06347 (Human-AI Co-Evolution).


5. Now I'm evaluating which of these papers warrant citations: the knowledge collapse work shows the three-stage phenomenon under recursive training, the theoretical paper provides foundational grounding for model collapse mechanisms, and the human-AI co-evolution piece connects to the web contamination problem space.

But I need to be careful about timing—some of these papers are dated June 2026, which would be after the May 25 submission deadline, so they wouldn't be available to cite anyway.

Looking at what's actually relevant: the September 2025 paper on knowledge collapse in recursive training provides good motivation even though it's not directly about generational depth scoring, and the May 2026 paper on human-AI co-evolution offers a dynamical systems angle that could strengthen the theoretical framing. loops. Should it be cited? It's potentially relevant to the motivation but doesn't do generational depth scoring.

4. **arXiv:2601.02947 "Quality Degradation Attack in Synthetic Data"** (January 2026) - quality degradation in synthetic data. Should it be cited? Possibly, but it seems to be about attacks rather than natural web contamination.

Given all my research, I now have a clear picture:
- The proposal is genuinely novel: no competing work on ordinal generational depth scoring for corpus decontamination.
- All round 7 issues are addressed.
- New papers found: arXiv:2509.04796 (Knowledge Collapse, Sep 2025) and arXiv:2601.02947 (Quality Degradation, Jan 2026) might be worth citing in the landscape, but are not direct competitors.
- arXiv:2505.11550 is NOT a direct competitor (model attribution vs. generational depth).

Now I'm identifying two concrete issues for round 8. First, the statistical test is severely underpowered—with only 3 random seeds and a critical t-value of 4.303, the paired t-test at α=0.05 won't detect modest effect sizes, so the proposal needs to acknowledge that failing to reject the secondary null might just reflect insufficient power rather than a true null result. Second, the ordinal regression head is mentioned but never specified—I need to flag that the proposal should clarify whether it's using CORAL-loss with auxiliary classifiers, proportional odds logistic regression, or some other implementation method for replicability.

I'm weighing whether these are critical enough to warrant a "revise" recommendation. The statistical power issue is methodologically legitimate but fixable in one sentence. The ordinal regression specification is a replicability gap but also a one-sentence fix. Neither seems to undermine the core novelty or validity of the approach, so I'm leaning toward flagging them as minor issues rather than critical ones.

Now I'm reconsidering the overall scores. The feasibility rating sits at 3.5 due to the 16-day timeline with sequential dependencies and the underpowered paired t-test with only 3 seeds. Even with the minor fixes, that constraint keeps the average below 4.0. The question is whether the feasibility concerns are severe enough to justify staying with "revise" or if the strong novelty and impact scores warrant an upgrade to "pass." for 4/5 feasibility:
- 512-token cap with deterministic arithmetic (6-9h per step)
- Parallel tracks for DeBERTa and collapse experiments
- Dual null-hypothesis ensures publishability regardless of outcome
- All critical resources verified (FineWeb-Edu, Qwen3-0.6B, DeBERTa-v3-large)
- Sequential bottleneck compressed to 2 steps × 2 days = 4 days, leaving 12 days for everything else

Arguments for 3.5/5 feasibility:
- Gen1/Gen2 discriminability from 0.6B model is genuinely uncertain ("Wall of Separation" directly challenges it)
- 3-seed test underpowered for secondary null
- 16 days is very tight for completion, submission prep, and potential revisions
- DeBERTa 120h ablations may be an overestimate, but better to be conservative

I'm settling on 3.5 as the fair rating. The core issue is whether we can actually demonstrate discriminability within the timeline, and while the dual null-hypothesis protects against a null result, proving a positive finding with AUC ≥ 0.65 and meaningful collapse differences is genuinely uncertain. Now I'm reconsidering whether a "revise" verdict is warranted at round 8 of 10—the remaining issues are fairly minor, mostly around ordinal regression specification and statistical power acknowledgment. The real question is whether these gaps would actually trigger a rejection at EMNLP, or if they're just polish. which ordinal regression method did you use?" but would probably not reject solely on this basis without implementation details. It's a clarification issue.

2. **Statistical power of 3-seed test**: A reviewer MIGHT argue that the secondary null finding is underpowered, but the proposal explicitly acknowledges it's at GPT-2 scale with limited compute. This is a known limitation, not a methodology error.

3. **arXiv:2509.04796**: A missing citation that a reviewer familiar with the literature might notice.

None of these are "reject" criteria at EMNLP on their own. They're clarification/completeness issues.

Let me think through the scoring threshold. The rules say "pass" requires an average of 4.0 or higher with no critical issues. My current average is 3.875, which falls short. Even if I bump clarity to 4.5 or feasibility to 4, I'd only reach exactly 4.0, and I genuinely think feasibility sits at 3.5 rather than 4. So the verdict is revise.

The main issues I need to flag are the unspecified ordinal regression head type, which creates a replicability gap since the approach mentions concatenating 5 scalar features but doesn't detail how they're converted to rankings. DeBERTa CLS token (1029-dim joint representation) and training an "ordinal regression head," but does not specify which ordinal regression method. For 3 ordered classes (Gen0, Gen1, Gen2), common implementations include: (a) CORAL-loss based with 2 auxiliary binary classifiers (arXiv:1901.07884, arXiv:2111.08851), (b) proportional odds logistic regression with 2 threshold parameters, or (c) 3-class softmax with ordinal loss. These differ in their assumptions about boundary structure. One sentence specifying the implementation (e.g., "We use CORAL-loss based ordinal regression following arXiv:2111.08851, decomposing the 3-class problem into 2 binary classifiers with shared feature weights and independently trained bias terms") closes this replicability gap.

2. With only 3 random seeds (df=2, critical t=4.303), the secondary null test for severity parity between conditions has power below 20% for Cohen's d < 2.0, meaning moderate contamination effects could easily go undetected. A brief acknowledgment that the test is primarily sensitive to large effect sizes would preempt reviewer concerns about the null finding being an artifact of underpowering.

3. A recent paper on knowledge collapse in LLMs shows that fluency can mask factual accuracy failures during recursive synthetic training, which is relevant context for understanding the contamination mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b1a9c7f-e321-4ee6-a4f4-b9e81a8da856",
  "isSidechain": false,
  "requestId": "req_011CasgW44MmWh14bZVwqqnC",
  "type": "assistant",
  "uuid": "1a9cfe1d-cb62-400f-bece-67b34162ee4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XaFmxgqxf27yLsww3eWAMb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12060,
      "cache_read_input_tokens": 42604,
      "output_tokens": 4809,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4809,
          "cache_read_input_tokens": 42604,
          "cache_creation_input_tokens": 12060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12060
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

_source line 23 · 2026-05-09T21:12:29.657Z_

Based on my independent research, I can now issue my verdict. Key findings:

- **arXiv:2505.11550** is NOT a direct competitor — it classifies by model attribution (which AI model), not generational depth. Not a citation issue.
- **arXiv:2605.01647, arXiv:2502.15654, arXiv:2602.10531, arXiv:2604.08554, arXiv:2407.12034** all verified to exist with claims accurately represented.
- **Novelty confirmed**: No paper does ordinal generational depth scoring for corpus decontamination.
- **New uncited paper found**: arXiv:2509.04796 "Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training" (Sep 2025) — relevant supporting motivation.
- **Round 7 issues fully addressed**: 512-token cap with arithmetic anchor (200K × 512 tokens ÷ 3,000–5,000 tok/s = 6–9h), arXiv:2602.10531 cited and differentiated.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "Confirmed novel across extensive search: no paper proposes ordinal generational depth scoring for corpus decontamination. Differentiation from all adjacent work (arXiv:2502.15654 binary detection, arXiv:2511.17602 benchmark overlap, TrainProVe image domain) is well-argued and accurate. arXiv:2505.11550 is model attribution (not depth), not a competitor."
    },
    "feasibility": {
      "score": 3,
      "rationale": "The 512-token cap with anchored arithmetic (6–9h per step) and dual null-hypothesis design improve credibility significantly, but three real concerns remain: (1) Gen1/Gen2 discriminability from the same 0.6B model is genuinely uncertain given the 'Wall of Separation' — the embedding-space counter-argument is plausible but unproven; (2) the secondary null paired t-test with 3 seeds (df=2, critical t=4.303) is severely underpowered for moderate effect sizes (Cohen's d < 2.0); (3) 16 days including parallel DeBERTa + collapse + writeup remains aggressive even with the optimized critical path."
    },
    "clarity": {
      "score": 4,
      "rationale": "The approach is well-specified: DeBERTa + 5 scalar features concatenated to CLS (1029-dim), dual null-hypothesis with pre-specified AUC threshold and paired t-test criterion, day-by-day critical path, fixed-total-size collapse conditions. The one remaining gap is the ordinal regression head type, which is unspecified despite the integration architecture being clear."
    },
    "impact": {
      "score": 4,
      "rationale": "Near-perfect alignment with EMNLP 2026 special theme 'New Missions for NLP Research' on synthetic data feedback loops and data governance. The budget-constrained decontamination framing addresses a real operational problem. Dual null-hypothesis ensures a publishable governance contribution regardless of outcome, though scale limitations (GPT-2, 0.6B generator) restrict external validity."
    }
  },
  "issues": [
    "REPLICABILITY GAP — Ordinal regression head type unspecified: The approach specifies concatenating 5 scalar features to the DeBERTa-v3-large CLS token (1029-dim joint representation) and training an 'ordinal regression head,' but does not specify which ordinal regression method. For 3 ordered classes (Gen0, Gen1, Gen2), common implementations differ in boundary-structure assumptions: (a) CORAL-loss based with 2 auxiliary binary classifiers (arXiv:1901.07884; arXiv:2111.08851), (b) proportional odds logistic regression with 2 threshold parameters, or (c) 3-class softmax with ordinal label weighting. Reviewers checking replicability will notice this gap. Fix: add one sentence specifying the implementation, e.g., 'We use CORAL-loss based ordinal regression (arXiv:2111.08851) decomposing the 3-class problem into 2 binary classifiers with shared feature weights and independently trained bias terms over the 1029-dim joint representation.' This closes the replicability gap without any experimental change.",
    "STATISTICAL POWER ACKNOWLEDGMENT MISSING — Secondary null hypothesis is underpowered: The pre-specified secondary null criterion (paired t-test, α=0.05, N=3 seeds, df=2) has a critical t-value of 4.303, providing power < 20% for Cohen's d < 2.0. If Gen2 contamination causes a real but moderate increase in collapse severity (e.g., 10–20% worse perplexity), 3 seeds cannot detect it, and non-rejection would falsely validate the 'depth stratification provides no incremental benefit' conclusion. This is the weakest statistical link in the pre-registered design and a reviewer will attack it. Fix: add one sentence explicitly acknowledging the limitation, e.g., 'We note that with 3 seeds the secondary null test is powered primarily to detect large effect sizes; non-rejection at this scale does not rule out moderate depth effects detectable with more seeds, which we reserve as future work at larger compute budgets.' This converts a reviewer attack surface into a transparent acknowledged limitation.",
    "MISSING CITATION — arXiv:2509.04796 'Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training' (September 2025): This paper demonstrates a three-stage recursive training phenomenon where surface fluency persists while factual accuracy collapses — providing complementary empirical support for the claim that deeper-generation text causes qualitatively distinct harm that perplexity alone may understate. An area chair familiar with the model collapse literature (likely at EMNLP 2026 given the special theme) may flag its absence. One citation line in the landscape section suffices: 'arXiv:2509.04796 shows that factual accuracy collapses faster than perplexity in recursive synthetic training — motivating depth-stratified decontamination as a mechanism to preferentially remove documents at generational depths where factual quality is most degraded; it does not classify documents by generational depth or propose a depth-stratified filtering method.'"
  ],
  "feedback": "All seven Round 7 issues are resolved: the 512-token document cap is explicitly stated with anchored arithmetic (200K × 512 tokens ÷ 3,000–5,000 tok/s = 6–9h per step), arXiv:2602.10531 is cited and differentiated, and all prior round issues remain correctly addressed. Three targeted fixes will complete this proposal: (1) Specify the ordinal regression head implementation — add one sentence naming the method (recommend CORAL-loss based, citing arXiv:2111.08851, since it is rank-consistent and well-tested for 3-class ordinal problems with PyTorch implementations readily available). (2) Add one sentence acknowledging the 3-seed secondary null test is powered for large effect sizes only, explicitly reserving higher-powered validation as future work. (3) Add arXiv:2509.04796 to the landscape with a one-line differentiation. All three fixes require under 30 minutes of writing and zero new experiments. Independent novelty verification confirms no competing work on generational depth scoring for corpus decontamination exists through May 2026.",
  "reason": "All Round 7 issues are addressed and novelty is confirmed, but three minor gaps remain: unspecified ordinal regression head type (replicability), unacknowledged statistical power limitation of 3-seed secondary null test, and missing arXiv:2509.04796 citation; average score 3.75/5 below the 4.0 pass threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a9cfe1d-cb62-400f-bece-67b34162ee4b",
  "isSidechain": false,
  "requestId": "req_011CasgW44MmWh14bZVwqqnC",
  "type": "assistant",
  "uuid": "3420475f-3b11-4818-add2-fac9f851468f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XaFmxgqxf27yLsww3eWAMb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12060,
      "cache_read_input_tokens": 42604,
      "output_tokens": 4809,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4809,
          "cache_read_input_tokens": 42604,
          "cache_creation_input_tokens": 12060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12060
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3420475f-3b11-4818-add2-fac9f851468f",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Genealogical depth scoring for recursive text decontamination",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3420475f-3b11-4818-add2-fac9f851468f",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Genealogical depth scoring for recursive text decontamination",
  "sessionId": "57d61d9c-5d24-47f2-be2a-4d09a61db58a"
}
```

---
