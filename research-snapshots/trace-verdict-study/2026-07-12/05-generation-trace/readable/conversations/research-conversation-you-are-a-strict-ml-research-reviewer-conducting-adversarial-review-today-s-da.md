# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-09 (UTC).** Your job: indep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/f6781f5d-59c7-449b-9656-f1f6383296d8.jsonl`
- **Structured JSON:** [`b6961f6186bc77d0abe3.json`](../../sessions/b6/b6961f6186bc77d0abe3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-09T21:03:03.186Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-09T21:03:03.186Z",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-09 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.\n\nDirection: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.\n2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.\n3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.\n\nThis is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.\n\nTag: direction=data_governance, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-09?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 7/10)\n{\n  \"title\": \"Tail-Coverage-Guided Synthetic Data Selection to Replace Classifier Quality Filtering\",\n  \"core_problem\": \"Classifier-based quality filtering (CQF), the dominant method for selecting synthetic pretraining data used by GPT-3, LLaMA, and PaLM, is shown to be illusory — it improves downstream task performance not by improving language modeling quality but by implicit distribution-matching rather than genuine quality signals. Concurrently, synthetic data exhibits systematic distributional discrepancies relative to real data: top-p and temperature sampling truncate low-probability continuations, causing rare factual content to be systematically underrepresented in synthetic corpora. Kandpal et al. (ICML 2023) established a direct causal link: LLM accuracy on factual questions correlates strongly with the frequency of the underlying entity in pretraining documents, confirming that tail-knowledge acquisition depends on tail-content exposure during training. No principled selection criterion corrects for this distributional gap: CQF does not target it (and may worsen it by filtering toward fluent head-distribution text), while naïve random sampling inherits the generator's truncation bias wholesale. More recent model-aware selectors such as MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) adapt dynamically to the evolving model's preferences but do not target the specific tail-distribution gap — they optimize for generic influence rather than for correcting truncation-induced underrepresentation.\",\n  \"opportunity\": \"Three concurrent findings create a gap that demands a new method: (1) 'The Data-Quality Illusion' (arXiv:2510.00866, preprint; peer review status pending) demonstrates that CQF does not improve language modeling on held-out high-quality data and argues the field should rethink synthetic data filtering from first principles; (2) 'Data Value in the Age of Scaling' (arXiv:2511.13640) identifies tail-knowledge underrepresentation as a systematic distributional discrepancy in synthetic data under real-synthetic mixing, linked to generative truncation mechanisms; (3) Kandpal et al. (ICML 2023) provides external causal validation: pretraining document frequency is a strong predictor of downstream accuracy on rare facts. Together, these findings establish that (a) CQF is the wrong solution, (b) the actual problem is a distributional gap at the tail, and (c) closing the tail gap causally improves knowledge acquisition. The opportunity is 'Coverage-Guided Sampling' (CGS): select synthetic examples to maximize marginal coverage of low-density regions of the real-data embedding space, directly targeting the distributional gap that CQF fails to address. This is the first synthetic data selector explicitly designed around the mechanism documented in arXiv:2510.00866 rather than a classifier proxy. The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status; CGS would be motivated equally if the finding were confirmed by independent replication. Concurrent work (arXiv:2604.13977, April 2026) finds that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are the dominant factors in synthetic pretraining quality — outperforming both larger generator models and format-agnostic generation strategies — providing external corroboration that principled, non-classifier-based generation and selection choices are the right axis for improving synthetic pretraining data quality, consistent with CGS's reference-density-gated approach.\",\n  \"landscape\": \"CQF is used by all major pretraining pipelines (GPT-3, LLaMA, PaLM, RedPajama) but arXiv:2510.00866 (preprint; peer review status pending) shows its quality signal is misleading. Six clusters of prior work bound the proposal:\\n\\n**Diversity-quality pretraining selection.** Quad (arXiv:2409.16986, ICLR 2025 Spotlight) is the most important prior work. Quad clusters all pretraining data and uses a Multi-Armed Bandit (MAB) scheme favoring clusters with high influence scores (quality) or low selection frequency (diversity). CGS differs on three axes: (1) Criterion — CGS uses a real-data tail-density threshold (bottom 20–25% by Voronoi cell occupancy in a reference corpus) rather than influence-weighted underrepresentation; CGS does not require influence score computation, which is expensive to scale to billions of synthetic candidates; (2) Target — CGS applies specifically to the synthetic data mixing problem and requires a real-data reference corpus to define 'tail'; Quad operates within a single multi-source corpus without a reference density; (3) Motivation — CGS is grounded in the CQF failure mechanism documented in arXiv:2510.00866. QuaDMix (arXiv:2504.16511, withdrawn from ICLR 2026, openreview.net/forum?id=oLxx7OhAb1) from ByteDance proposes a parameterized quality-diversity sampling function using domain classification for diversity measurement and LightGBM for parameter search. Like Quad, QuaDMix does not target real-data tail density specifically.\\n\\n**Model-aware selection.** MATES (arXiv:2406.06046, NeurIPS 2024) trains a lightweight BERT-base influence model that continuously adapts to the evolving pretraining model's data preferences, updating every 10,000 steps. MATES achieves 2× the gain of prior SOTA (QuRating) on 410M and 1B models, at 11.5–21.7% computational overhead. CGS differs on three axes: (a) CGS requires no influence model training — the FAISS IVF index is built once over the fixed reference corpus before pretraining begins, versus MATES's periodic BERT-base retraining; (b) CGS requires no reference task definition — MATES's performance varies substantially with reference task choice, a deployment-time burden; (c) CGS targets a specific, mechanistically motivated failure mode (CQF distributional bias) rather than maximizing generic influence scores.\\n\\nGroup-MATES (arXiv:2502.14709, NeurIPS 2025) extends MATES to group-level selection: it trains a relational data influence model that weights individual sample influence by inter-data relationships, partitions the training corpus into clusters via these relationship weights, and selects within each cluster independently, achieving 3.5–9.4% relative gains and 1.75× token efficiency over individual selection baselines on DCLM at 400M–3B scales across 22 tasks. CGS differs on three axes: (a) CGS requires no influence model — Voronoi cells are defined by k-means over a fixed reference corpus embedding, not by data-data relational influence weights, making CGS zero-overhead relative to training; (b) CGS uses reference-corpus occupancy density as the selection gate — only tail cells (bottom 20–25% by reference occupancy) are eligible for synthetic coverage — rather than influence-weighted within-cluster scoring; (c) CGS targets the specific synthetic-real distributional gap documented in arXiv:2511.13640: it applies to a fixed synthetic candidate pool relative to a real-data reference corpus, whereas Group-MATES operates within a single training corpus without a reference density criterion.\\n\\n**Tail knowledge via synthetic generation.** EntiGraph (arXiv:2409.07431, ICLR 2025 Oral) addresses tail-knowledge acquisition through synthetic document generation: given a small domain corpus, it extracts salient entities, constructs a knowledge graph dynamically from entity-pair relationships via LM-driven synthesis, and generates new documents traversing those relationships — improving tail-fact retention in continued pretraining. Unlike CGS, EntiGraph is a generative method that requires a structured source corpus as input to drive entity extraction; it produces entirely new documents rather than selecting from a pre-existing pool, and is evaluated on domain-specific continued pretraining (QuALITY benchmark) rather than open-domain general pretraining. The approaches are orthogonal and complementary: CGS could select tail-covering subsets of an EntiGraph-generated corpus, concentrating the EntiGraph generation budget on the regions of real-data embedding space already underrepresented.\\n\\n**Architectural approaches to tail knowledge.** 'Pretraining with Hierarchical Memories: Separating Long-Tail and Common Knowledge' (arXiv:2510.02375, October 2025) addresses tail knowledge acquisition through model architecture changes rather than data selection: it introduces hierarchical parametric memory banks alongside a smaller core model, storing long-tail world knowledge in memory parameters while the core model captures common knowledge and general reasoning, with a 160M-parameter model plus 18M-parameter memory (fetched from a 4.6B bank) achieving performance comparable to a standard model with more than 2× the parameters. This architectural intervention is orthogonal to CGS: CGS improves the training distribution presented to any model architecture, and could complement hierarchical memory architectures by ensuring the training data seen by those memory components better covers tail-content regions.\\n\\n**Coverage-based fine-tuning.** 'Less is More: Adaptive Coverage for Synthetic Training Data' (arXiv:2504.14508, 2025) applies a greedy maximum-coverage objective to select synthetic fine-tuning data for NLP classifiers. CGS shares the max-coverage algorithmic skeleton but differs critically in three respects: (1) 'Less is More' maximizes coverage of ALL embedding cells uniformly — without a reference-corpus density criterion, it would waste selection budget on head cells already well-covered by real data, failing to address the distributional gap that CQF leaves open; CGS adds the critical step of using real-data Voronoi occupancy as a gate: only tail cells (bottom 20–25% by reference occupancy) are eligible, ensuring the entire selection budget is concentrated on underrepresented regions; (2) CGS applies at pretraining scale (hundreds of millions of candidates), requiring FAISS IVF for tractability; (3) this reference-density threshold is the mechanistic link to the CQF failure documented in arXiv:2510.00866, which 'Less is More' does not establish.\\n\\n**Online pretraining data curation.** ADAPT ('Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods', Zhao et al., ICLR 2026 Workshop DATA-FM, openreview.net/forum?id=zgn3P31NWf) and AC-ODM ('Actor-Critic Online Data Mixing', arXiv:2505.23878, preprint) represent an online paradigm: rather than pre-filtering the candidate pool, they dynamically reweight or re-mix training samples during training based on loss signals. CGS is orthogonal and compatible: as a static offline pre-filter, it reduces the synthetic candidate pool to tail-coverage-optimal documents before training begins with zero ongoing overhead; an online reweighter can further adapt the mix at training time after CGS has already narrowed the pool. Neither ADAPT nor AC-ODM targets the specific synthetic-real tail-density gap documented in arXiv:2510.00866 — they optimize generic influence or domain balance, not reference-density-defined tail coverage.\\n\\n**Synthetic data scale findings.** 'Demystifying Synthetic Data in LLM Pre-training' (arXiv:2510.01631, EMNLP 2025) finds ~30% rephrased synthetic data is empirically optimal but provides no mechanistic filter. arXiv:2511.13640 characterizes three-phase scaling behavior under real-synthetic mixing and identifies tail underrepresentation as a systematic discrepancy without a selection remedy. Concurrent work arXiv:2604.13977 ('How Can We Synthesize High-Quality Pretraining Data?', April 2026) systematically compares synthetic pretraining strategies across generator models and formats, finding that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are dominant factors in synthetic pretraining quality — outperforming both larger generator models and format-agnostic generation strategies. This provides independent corroboration for CGS's non-classifier-proxy approach: if principled generation choices outperform raw scale and classifier-based proxies, the right axis to optimize is how data is selected and structured rather than whether a quality classifier endorses it.\\n\\n**Tail knowledge evaluation and deduplication.** Kandpal et al. (arXiv:2211.08411, ICML 2023) establish that LLM accuracy on factual questions correlates causally with pretraining document frequency, providing the empirical foundation for CGS's tail-coverage hypothesis. 'Head-to-Tail' (arXiv:2308.10168, NAACL 2024) provides a purpose-built 18K QA benchmark explicitly stratified into head, torso, and tail facts by knowledge graph frequency — an independent evaluation resource for CGS. D4 (NeurIPS 2023) uses FAISS k-means for deduplication/diversification via distance-to-centroid pruning; it applies a distance heuristic not a tail-density threshold and does not target the synthetic selection sub-problem.\",\n  \"approach\": \"Coverage-Guided Sampling (CGS) selects synthetic pretraining data by maximizing coverage of underrepresented tail regions in real-data embedding space.\\n\\n**Method.** We embed a reference corpus (5B-token stratified sample of Dolma, preserving domain balance) and all candidate synthetic documents using ModernBERT-large, then build a FAISS IVF index over the real-data embeddings. The resulting Voronoi cell structure partitions semantic space; 'tail cells' are defined as cells in the bottom 20–25% by real-data occupancy. CGS then greedily selects synthetic documents maximizing marginal coverage of tail cells via a streaming maximum-coverage subproblem — no quality classifier training required. ModernBERT-large is chosen for embedding over larger alternatives due to its superior throughput: the official ModernBERT benchmark documents ~52K tokens/sec for ModernBERT-large on RTX 4090 (arXiv:2412.13663); H100 SXM delivers 2–4× RTX 4090 throughput for encoder inference (NVIDIA H100 Tensor Core GPU product brief), placing ModernBERT-large at ~100–200K tok/s on H100 — versus ~15–30K for Qwen3-Embedding-8B. To verify this before committing to full-corpus embedding, we run a 100K-document throughput pilot (~51M tokens, ~5 GPU-minutes) at the start of Experiment 0; if measured throughput is below 60K tok/s, the synthetic pool is reduced from 15M to 10M documents (7.68B → 5.12B tokens), reducing total embedding to ~47H and holding overall budget under 185H. Embedding quality is validated in Experiment 0.\\n\\n**Mechanistic validation experiment (Experiment 0, ~2 H100-hours).** Before committing to training runs, we validate the core empirical hypothesis: (a) Generate three synthetic corpora of 10M tokens each using Qwen3-72B with top-p ∈ {0.5, 0.85, 0.95}; embed and assign each document to a Voronoi cell; measure whether lower top-p concentrates documents in higher-occupancy cells (expected: yes, since low top-p collapses to high-probability continuations); (b) Embed 5,000 Wikidata long-tail documents (entities appearing <100 times in C4) and confirm they cluster significantly more in low-occupancy cells than a random C4 sample. If (a) shows r < 0.3 between top-p and mean cell occupancy, or (b) shows no significant enrichment, halt before Tier 1 and revise the tail-density criterion.\\n\\n**Model architecture and training.** Following the precedent of MATES (NeurIPS 2024), Quad (ICLR 2025), and D4 (NeurIPS 2023), we use the Pythia model family (EleutherAI GPT-NeoX codebase) for full reproducibility:\\n- *Tier 1 — Systematic ablation: Pythia-410M* (24 layers, hidden dim 1024, 16 heads, 2048 sequence length; ~8B tokens, Chinchilla-optimal). AdamW optimizer with β1=0.9, β2=0.95, weight decay 0.1; cosine LR schedule with 1% warmup steps. Following Wang et al. ('Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice,' ICLR 2026 Poster), all Tier 1 ablations use a 10× reduced peak learning rate of 3×10⁻⁵ (instead of the standard 3×10⁻⁴) to ensure selection method rankings derived from the 410M proxy runs transfer reliably to Tier 2 at 1.4B scale — this costs no additional GPU-hours since the reduced-LR runs replace rather than supplement standard-LR runs. Batch size ~2M tokens. 5 configurations: CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, and random baseline. Only CGS has a tail-threshold parameter; the three non-CGS methods run once without threshold variation. Each run: ~9 H100-hours on 1 GPU.\\n- *Tier 2 — Scaling check: Pythia-1.4B* (24 layers, hidden dim 2048, 16 heads, 2048 sequence length; 10B tokens). Same optimizer family with peak LR 2×10⁻⁴. 2 configurations: best CGS from Tier 1 vs. CQF-FineWebEdu. Each run: ~44 H100-hours (4 GPUs × ~11h wall-clock via data parallelism). Using Pythia-1.4B (not 1.3B) ensures exact architecture reproducibility with the published model family.\\n\\n**Synthetic candidate pool.** We precompute embeddings for a fixed 15M-document synthetic pool generated by Qwen3-72B (top-p=0.9, temperature=1.0, avg 512 tokens/document = 7.68B tokens total). At 100K tokens/sec per H100 (nominal): the 7.68B synthetic tokens require 76,800s ≈ 21.3 GPU-hours; the 5B-token reference corpus requires 50,000s ≈ 13.9 GPU-hours; total embedding ≈ 35 GPU-hours ≈ 8.8H wall-clock on 4 GPUs. Under the throughput fallback (10M docs, ~5.12B tokens), embedding reduces to ~19H + 13.9H ≈ 33H for synthetic + reference ≈ 47H total. This pool size provides ample selection diversity: 7.68B tokens exceeds the synthetic allocation for both Tier 1 (~2.4B tokens at 30% synthetic) and Tier 2 (~3B tokens at 30% synthetic) by over 2.5×. FAISS IVF build is CPU-bound (~2h on 32 cores) and runs concurrently with early embedding steps.\\n\\n**IVF nlist calibration.** nlist ≈ sqrt(N_reference_docs) per FAISS best practices. Tier 1 pilots probe two nlist settings (±30%) to confirm tail cell occupancy is well-separated; this is CPU-only analysis on the pre-built index (zero GPU cost). If cell structure is degenerate, we correct before the Tier 2 run.\\n\\n**Evaluation — primary, secondary, and diversity metrics.** The evaluation design explicitly separates the training criterion (FAISS cell coverage) from the test signal to avoid circularity:\\n\\n(1) *Primary — TriviaQA head/tail accuracy split (independent external metric)*: Using Wikipedia page-view statistics to stratify TriviaQA questions into head entities (top 20% by views, ~1K questions) and tail entities (bottom 20%, ~1K questions), we measure accuracy separately. This stratification uses an external resource (Wikipedia traffic data) wholly independent of the FAISS cell structure. Per Kandpal et al. (ICML 2023), tail-entity accuracy is the most causally meaningful test of whether tail coverage translates to knowledge acquisition. We report the tail/head accuracy ratio as the primary CGS-vs-CQF gap metric.\\n\\n(2) *Additional independent benchmark — Head-to-Tail (NAACL 2024)*: This purpose-built 18K QA benchmark stratifies facts into head, torso, and tail by knowledge graph frequency (Wikidata). It provides a second external validation of tail knowledge independent of both FAISS and Wikipedia pageviews, strengthening the falsifiability of the tail-coverage claim.\\n\\n(3) *Secondary — Standard downstream benchmarks*: HellaSwag, WinoGrande, ARC-E/C, PIQA — required for comparability with Quad, D4, MATES, Group-MATES, and CQF baselines. CGS should match or exceed CQF on these benchmarks; failure here would indicate coverage-only selection sacrifices head-distribution capabilities.\\n\\n(4) *Diversity of selected synthetic data (CPU-only, zero GPU cost)*: We compute corpus-level self-BLEU (Zhu et al., 2018; lower = more diverse) and 4-gram entropy (higher = more diverse) over the synthetic subset selected by each method (CGS, CQF-Wikipedia, CQF-FineWebEdu, random). These metrics are computed post-selection before training begins. CGS should exhibit lower self-BLEU and higher n-gram entropy than CQF-selected data, since CQF preferentially selects fluent head-distribution text with low lexical diversity. This directly substantiates the coverage-vs-classifier-proxy claim: not only does CGS target underrepresented semantic regions, but the selected text should be measurably more lexically diverse than CQF output — consistent with the concurrent finding (arXiv:2604.13977) that principled generation choices (structured formats, prompt design) outperform classifier-based proxies in synthetic pretraining quality.\\n\\n(5) *Diagnostic — Held-out low-occupancy perplexity*: 5% of reference corpus documents from the bottom 20% occupancy cells are held out before training and used to measure model perplexity. This metric is demoted to a sanity check because CGS is explicitly optimized to cover exactly those cells — perplexity improvement here confirms distribution matching, not necessarily genuine knowledge acquisition. It is reported alongside (1) and (2) but not used as a primary falsifiability claim.\\n\\n**Falsifiable primary claim**: CGS achieves higher TriviaQA tail-entity accuracy than CQF while matching CQF on standard downstream benchmarks, directly operationalizing the quality-vs-coverage paradox documented in arXiv:2510.00866. The diversity metrics (self-BLEU, n-gram entropy) provide a secondary mechanistic check confirming that CGS's tail-coverage selection is not collapsing to a high-fluency, low-diversity subset.\\n\\n**Timeline and execution mode.** Given the EMNLP 2026 ARR deadline of May 25, 2026 (16 days from proposal date), the primary execution path is auto-research mode. GPU wall-clock with 4× H100: Experiment 0 (~2h, including 5-min throughput pilot) → Embedding (~8.8h, 4 GPUs, or ~5.8h under 10M-doc fallback) → FAISS build (~2h CPU concurrent) → Tier 1 ablation grid (~18h, 4 experiments in parallel in batch 1, then 1 remaining) → Tier 2 scaling check (~22h, 2 sequential runs with 4-GPU data parallelism). Total GPU wall-clock: ~50.8 hours (~2.1 days) nominal; ~48.8h under fallback. Paper writing begins in parallel on day 1; Tier 1 results are guaranteed by day 4; Tier 2 results are best-effort. If Tier 2 runs do not complete before submission, the 1.4B experiments are described as ongoing and submitted to camera-ready.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~172 H100-hours (Experiment 0 ~2h including 5-min throughput pilot; embedding ModernBERT-large on 15M synthetic docs + 5B reference corpus ~35h [nominal, throughput ≥ 60K tok/s] or ~47H [10M-doc fallback if throughput < 60K tok/s, reducing synthetic pool from 7.68B to 5.12B tokens]; FAISS IVF build CPU-bound ~0h GPU; Tier 1 ablations 5 configurations × ~9h = 45h; Tier 2 scaling check 2 runs × ~44h = 88h; misc eval ~2h). Budget stays ≤185H under fallback scenario; arithmetic verified: 7.68B synthetic tokens ÷ 100K tok/s = 21.3H + 5B reference ÷ 100K tok/s = 13.9H = 35.2H nominal.\",\n      \"gpu_utilization\": \"Low (~40% active) — researcher waits between tiers to review Experiment 0 results and pilot outcomes before committing to 1.4B runs.\",\n      \"timeline\": \"3–5 months. INCOMPATIBLE with May 25, 2026 ARR deadline — use auto-research mode for deadline-constrained execution.\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$420–615 at $2.44–3.56/hr per H100 (RunPod/Lambda Labs current pricing)\",\n      \"risk_note\": \"If Experiment 0 (mechanistic validation) fails — i.e., top-p does not correlate with cell occupancy in the expected direction — the core hypothesis needs revision before Tier 1 ablations begin. Caught in the first ~2 H100-hours. If throughput pilot shows < 60K tok/s, pool is reduced to 10M docs and budget stays under 185H.\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~190 H100-hours (manual base ~172H plus agent overhead: 2 additional 410M sensitivity runs for IVF nlist ±30% around baseline and ModernBERT-large vs. sentence-transformers/all-MiniLM-L6-v2 embedding model speed check, each ~9h = 18H extra; plus ~0H GPU for nlist structure analysis which is CPU-only; throughput fallback to 10M-doc pool reduces embedding by ~9H if triggered, capping at ~181H under fallback).\",\n      \"gpu_utilization\": \"Moderate (~60% active) — agent queues experiments continuously but awaits human approval before committing to each Tier 2 run.\",\n      \"timeline\": \"4–6 weeks. INCOMPATIBLE with May 25, 2026 ARR deadline — use auto-research mode for deadline-constrained execution.\",\n      \"team\": \"1 researcher, ~45 min/day check-in to approve tier transitions and review Experiment 0 results\",\n      \"claude_api_cost\": \"$200–350 (experiment queue management, Experiment 0 result interpretation, IVF calibration guidance)\",\n      \"estimated_gpu_cost\": \"~$464–676 at $2.44–3.56/hr per H100\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~175 H100-hours (Experiment 0 ~2h including 5-min throughput pilot; embedding ModernBERT-large for 15M synthetic docs [7.68B tokens] + 5B reference corpus ~35h [throughput ≥ 60K tok/s] or ~47H [10M-doc fallback if throughput < 60K tok/s]; FAISS IVF build CPU-bound ~0h GPU; Tier 1 ablation grid 5 configurations × ~9h = 45h; Tier 2 scaling check 2 runs × ~44h = 88h; misc eval ~3h). Budget ≤175H nominal, ≤185H under fallback; capped at 175H by early-stopping if Experiment 0 fails (saves ~138H by avoiding Tier 1 and Tier 2).\",\n      \"gpu_utilization\": \"High (~85% active) — agent queues Experiment 0 (with throughput pilot) → embedding → FAISS build → Tier 1 ablation grid → Tier 2 runs without human wait. ~15% overhead from API round-trips and CPU-bound FAISS builds between GPU steps.\",\n      \"timeline\": \"8–12 days total: ~2.1 days GPU wall-clock compute (50.8 hours on 4× H100) + paper writing in parallel from day 1. Tier 1 results available by day 4; Tier 2 results by day 5. Writing days 1–14 (parallel); submission day 16 (May 25, 2026 ARR deadline). COMPATIBLE with deadline under this framing: Tier 1 results are guaranteed at submission; Tier 2 results are best-effort and described as ongoing in the paper if not complete.\",\n      \"team\": \"0 (initial setup ~3h: configure ModernBERT-large embedding pipeline with FAISS IVF builder, GPT-NeoX training harness with eval on HellaSwag/WinoGrande/ARC/PIQA + TriviaQA head/tail + Head-to-Tail benchmark)\",\n      \"claude_api_cost\": \"$600–900 (automated Experiment 0 interpretation, ablation grid orchestration, early-stopping decisions, TriviaQA stratification computation, final report generation — estimated 5,000–8,000 API turns)\",\n      \"estimated_gpu_cost\": \"~$427–623 at $2.44–3.56/hr per H100\",\n      \"speed_bottleneck\": \"4× H100 allows: Embedding (15M synthetic docs + 5B reference corpus) completes in ~8.8h wall-clock (35H ÷ 4 GPUs); Tier 1 grid runs in ~18h wall-clock (4 configs in parallel batch 1, then 1 remaining config in batch 2, each ~9H on 1 GPU); Tier 2 serializes at ~11h wall-clock each with 4-GPU data parallelism (2 runs = 22h). Total GPU wall-clock: ~2h (Exp 0) + ~8.8h (embedding) + ~18h (Tier 1) + ~22h (Tier 2) ≈ 50.8h ≈ 2.1 days.\",\n      \"risk_note\": \"Early-stopping trigger: if Experiment 0 shows Pearson r < 0.3 between top-p value and mean cell occupancy rank, halt and report mechanism failure before consuming Tier 1 compute. Throughput early-stop: if 5-min pilot measures < 60K tok/s, reduce synthetic pool from 15M to 10M documents before proceeding to full embedding, holding total budget under 185H. Pre-specified thresholds prevent exhaustive exploration of degenerate configurations.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026; conference October 24–29, 2026, Budapest, Hungary). Primary execution path: auto-research mode, with Tier 1 (Pythia-410M) results guaranteed at submission and Tier 2 (Pythia-1.4B) submitted to camera-ready.\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining (arXiv:2510.00866, preprint; peer review status pending)\",\n    \"Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures (arXiv:2511.13640, 2025)\",\n    \"Harnessing Diversity for Important Data Selection in Pretraining Large Language Models (Quad, arXiv:2409.16986, ICLR 2025 Spotlight)\",\n    \"QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining (arXiv:2504.16511, withdrawn from ICLR 2026, openreview.net/forum?id=oLxx7OhAb1)\",\n    \"MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models (arXiv:2406.06046, NeurIPS 2024)\",\n    \"Group-MATES: Group-Level Data Selection for Language Model Pretraining (arXiv:2502.14709, NeurIPS 2025)\",\n    \"Synthetic Continued Pretraining via EntiGraph (arXiv:2409.07431, ICLR 2025 Oral)\",\n    \"Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice (Wang et al., ICLR 2026 Poster, openreview.net/forum?id=2FZC0c06jP)\",\n    \"Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods — ADAPT (Zhao et al., ICLR 2026 Workshop DATA-FM, openreview.net/forum?id=zgn3P31NWf)\",\n    \"AC-ODM: Actor-Critic Online Data Mixing for Sample-Efficient LLM Pretraining (arXiv:2505.23878, preprint)\",\n    \"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls (arXiv:2510.01631, EMNLP 2025)\",\n    \"How Can We Synthesize High-Quality Pretraining Data? (arXiv:2604.13977, April 2026)\",\n    \"Large Language Models Struggle to Learn Long-Tail Knowledge (Kandpal et al., arXiv:2211.08411, ICML 2023)\",\n    \"Head-to-Tail: How Knowledgeable are Large Language Models in Long-Tail Knowledge? (arXiv:2308.10168, NAACL 2024)\",\n    \"Pretraining with Hierarchical Memories: Separating Long-Tail and Common Knowledge (arXiv:2510.02375, October 2025)\",\n    \"Measuring Diversity in Synthetic Datasets (arXiv:2502.08512, ICML 2025)\",\n    \"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning (arXiv:2511.01490, ACL Findings 2026)\",\n    \"Less is More: Adaptive Coverage for Synthetic Training Data (arXiv:2504.14508, 2025)\",\n    \"D4: Improving LLM Pretraining via Document De-Duplication and Diversification (NeurIPS 2023)\",\n    \"Scaling Laws of Synthetic Data for Language Models (arXiv:2503.19551, 2025)\",\n    \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling (arXiv:2304.01373, ICML 2023)\",\n    \"ModernBERT: Smarter, Better, Faster, Longer (arXiv:2412.13663, 2024)\"\n  ],\n  \"description\": \"Classifier-based quality filtering (CQF) — the dominant synthetic pretraining selector used by GPT-3, LLaMA, and PaLM — has been shown to boost downstream task scores via implicit distribution-matching rather than genuine quality improvement (arXiv:2510.00866, preprint; peer review status pending; independently reproducible from first principles regardless of venue outcome). Concurrently, Kandpal et al. (ICML 2023) established that LLM accuracy on rare facts causally correlates with pretraining document frequency, confirming that tail-content exposure drives tail-knowledge acquisition; arXiv:2511.13640 documents systematic tail underrepresentation in synthetic data via top-p/temperature truncation; and concurrent work arXiv:2604.13977 (April 2026) finds that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are dominant factors in synthetic pretraining quality — outperforming generator scale and format-agnostic generation — providing external corroboration that principled generation choices matter more than classifier-based proxies, consistent with CGS's non-proxy-based selection criterion. This project proposes Coverage-Guided Sampling (CGS), the first principled pretraining data selector grounded in the actual distributional failure mechanism of CQF. CGS embeds a 5B-token reference corpus and a fixed 15M-document synthetic candidate pool (7.68B tokens) using ModernBERT-large — whose official benchmark documents ~52K tokens/sec on RTX 4090 (arXiv:2412.13663); H100 SXM delivers 2–4× RTX 4090 throughput for encoder inference (NVIDIA H100 product brief), placing it at ~100–200K tok/s. A 100K-document throughput pilot (~5 GPU-minutes) at the start of Experiment 0 verifies this before committing to full-corpus embedding; if measured throughput is below 60K tok/s, the synthetic pool is reduced from 15M to 10M documents, holding total budget under 185H. Total embedding ≈ 35 GPU-hours nominal (7.68B synthetic tokens ÷ 100K tok/s = 21.3H + 5B reference ÷ 100K tok/s = 13.9H ≈ 8.8H wall-clock on 4 GPUs). CGS builds a FAISS IVF index over the real corpus, identifies low-density Voronoi 'tail cells' (bottom 20–25% by occupancy), and greedily selects synthetic documents maximizing marginal tail-region coverage — no classifier training required. A mandatory Mechanistic Validation Experiment (~2 H100-hours, inclusive of throughput pilot) confirms that Voronoi cell density correlates with top-p sampling behavior before committing to training runs. We train using the Pythia model family: Tier 1 uses Pythia-410M at Chinchilla-optimal scale (~8B tokens, 5 ablation configurations, ~45 H100-hours) with the 10× reduced peak LR (3×10⁻⁵) recommended by Wang et al. (ICLR 2026 Poster) for proxy-to-full-scale ranking reliability; Tier 2 uses Pythia-1.4B at 10B tokens (2 configurations, ~88 H100-hours); total budget ~175 H100-hours nominal, ≤185H under fallback. Evaluation resolves circularity: TriviaQA tail-entity accuracy (stratified by Wikipedia pageviews, independent of FAISS) and the Head-to-Tail benchmark (NAACL 2024) are primary falsifiability metrics; corpus-level self-BLEU and 4-gram entropy over selected synthetic data are computed CPU-only post-selection to confirm CGS produces more diverse output than CQF. Closest prior work: EntiGraph (ICLR 2025 Oral, arXiv:2409.07431) generates new synthetic documents by traversing entity relationships in a source corpus — CGS is a post-hoc selector for any pre-existing synthetic pool without generative infrastructure, and the approaches are complementary. Architectural methods such as hierarchical memory banks (arXiv:2510.02375) address tail knowledge through model architecture changes rather than data selection; CGS is orthogonal and could complement such architectures by improving the training distribution seen by those memory components. Quad (ICLR 2025) uses influence-weighted cluster MAB — CGS requires no influence scoring. MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) train influence models — CGS builds its FAISS index once with zero ongoing overhead and no reference task dependency. 'Less is More' maximizes uniform coverage of all cells — CGS adds a real-data reference-density gate (bottom 20–25% occupancy only). Online methods ADAPT (ICLR 2026 Workshop DATA-FM) and AC-ODM reweight during training — CGS is a compatible offline pre-filter. Primary execution path: auto-research mode (4× H100, ~2.1 days GPU wall-clock, paper writing in parallel), targeting EMNLP 2026 ARR deadline May 25, 2026, with Tier 1 results guaranteed at submission.\",\n  \"project_name\": \"cov_guided_synth_sel\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"VENUE CLAIM ERROR: The generator labels arXiv:2510.00866 as 'EMNLP 2025', but independent search confirms the OpenReview submission targets ICLR 2026 (not EMNLP 2025). This foundational reference for the 'opportunity' narrative may have a different reception history; the paper should be cited as a preprint with venue status clarified.\", \"CLAIM OVERSTATEMENT: arXiv:2511.13640 is described as proving 'tail-knowledge underrepresentation is a leading driver of collapse.' The paper's abstract identifies tail underrepresentation as a distributional discrepancy observed in synthetic data and studies three-phase scaling — it does not specifically claim this is the primary or leading driver of collapse. This exaggerated claim weakens the motivation.\", \"MISSED CRITICAL PRIOR WORK: Quad (ICLR 2025, arXiv via openreview.net/forum?id=bMC1t7eLRc) proposes clustering-based quality+diversity selection for LLM pretraining using FAISS k-means and influence scoring — a direct competitor the generator does not cite. QuaDMix (arXiv:2504.16511, ICLR 2026 submission, since withdrawn) from ByteDance proposes a unified quality-diversity parameterized selection function for pretraining, also uncited. These papers must be differentiated against.\", \"MECHANISTIC GAP IN CORE CLAIM: The proposal asserts that Voronoi cells with low real-data occupancy in Qwen3-Embedding space correspond to the tail knowledge that top-p/temperature sampling truncates. This mapping is assumed, not established. Token-level probability truncation in a generative model does not directly translate to semantic embedding cluster density. A reviewer will immediately ask for theoretical justification or ablation confirming this correspondence.\", \"COMPUTE CONSTRAINT MISMATCH: The user's hard constraint is ≤200 H100-hours and explicitly specifies 1B–3B models. The proposal adds a 7B model run (~120h A100 ≈ 60 H100-hours) that goes beyond the user's stated scope and partially strains the budget. The 5× ablation runs of 1.3B at 30h A100 each imply ~12B-token training runs, which are far from Chinchilla-optimal and may produce null or noisy tail-coverage signal.\", \"SHORT TRAINING RUN RISK: At the implied token budgets (12–15B tokens for 1.3B models, ~15B for 7B), the models are severely under-trained. Tail-knowledge differences between selection strategies may not manifest reliably at this scale, making the primary evaluation (Wikidata-derived tail probe accuracy) potentially inconclusive.\", \"WIKIDATA TAIL PROBE CONSTRUCTION: The 'rare entity recall' and 'uncommon fact completion' evaluation requires constructing entity-frequency distributions from Wikidata, filtering tail entities from training data, and ensuring no contamination with the Dolma/C4 reference corpus. This pipeline is neither simple nor guaranteed valid — a reviewer will question whether the probe actually tests tail coverage or just benchmark contamination artifacts.\", \"DIFFERENTIATION FROM 'LESS IS MORE' UNDERSTATED: The generator correctly identifies arXiv:2504.14508 as closest concurrent work but claims differentiation by 'not addressing pretraining.' However, the algorithmic overlap is very high — both use embedding space, both use greedy max-coverage, both target synthetic data. A reviewer may see CGS as 'Less is More applied to pretraining with a tail-density threshold' and demand stronger algorithmic differentiation.\"]\nFeedback: The core idea is publishable but needs targeted revision on four fronts before it can reach top-tier bar:\n\n1. FIX REFERENCES AND CLAIMS: Correct the venue of arXiv:2510.00866 (it is not confirmed 'EMNLP 2025'; cite as preprint or ICLR 2026 submission). Soften the claim about 2511.13640: write 'identifies tail knowledge underrepresentation as a systematic distributional discrepancy in synthetic data' rather than 'leading driver of collapse.' These factual errors undermine reviewer trust.\n\n2. DIFFERENTIATE FROM QUAD AND LESS IS MORE: Quad (ICLR 2025) does clustering-based diversity-quality selection for pretraining — you must cite it and clearly explain why CGS (tail-density targeting via Voronoi cells) is fundamentally different from selecting underrepresented clusters. The generator should add a paragraph: 'This idea is too similar to Quad (ICLR 2025, openreview.net/forum?id=bMC1t7eLRc) in using FAISS clustering for pretraining diversity. Differentiation: Quad selects by influence-weighted cluster underrepresentation, not by real-data tail density in Voronoi cells; CGS's criterion is grounded in the CQF failure mechanism specifically for synthetic data.' Similarly, position against Less is More (arXiv:2504.14508) more aggressively: CGS extends the max-coverage idea to pretraining and adds tail-threshold grounding.\n\n3. JUSTIFY OR DROP 7B MODEL: To stay within the user's ≤200 H100-hour constraint and 1B–3B model scope, either (a) drop the 7B run and use a 2.8B model as the 'large' reference point, or (b) argue explicitly that 7B is needed to show the tail-coverage effect is non-trivial at scale and budget ~60 H100-hours for it. The current framing mixes the user's budget constraint with an aspiration for larger scale.\n\n4. VALIDATE THE VORONOI-TAIL CORRESPONDENCE: Add a validation experiment: (a) generate synthetic documents with different top-p values (0.5, 0.85, 0.95) and show that Voronoi cell density in Qwen3-Embedding space correlates with generation temperature/top-p in the expected direction; (b) show that manually selected tail-knowledge documents from Wikidata concentrate in low-occupancy cells. This costs 1–2 GPU-hours but would make the mechanistic claim reviewable. Without this, the core hypothesis is untested.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"TIMELINE CONSTRAINT VIOLATION: The user specifies a hard ≤16-day constraint. Manual mode is estimated at 3-5 months and human-in-loop at 4-6 weeks — both are wildly incompatible. Auto-research mode is 8-12 days for experiments only, leaving ≈4-8 days to write and submit a full research paper. The proposal should either (a) scope itself to auto-research mode as the primary execution path and explicitly acknowledge the paper-writing timeline risk, or (b) treat the 16-day constraint as applying to a 'proof of concept' submission where only Tier 1 results (360M ablations) are reported and Tier 2 is deferred to the camera-ready. As written, the resource estimate table creates an internal inconsistency: the paper claims to target EMNLP 2026 (16 days away) yet describes modes that take months.\", \"MATES (NeurIPS 2024) ABSENT FROM FORMAL LANDSCAPE AND KEY REFERENCES: MATES (arXiv:2406.06046, NeurIPS 2024) trains a small influence model to dynamically select pretraining data, achieving 2× the gains of prior state-of-the-art. This is a directly relevant published baseline for pretraining data selection that the proposal mentions once in passing ('Quad, D4, and MATES baselines') but never formally describes or differentiates in the landscape section. A reviewer will notice this omission immediately. The generator should add MATES to the landscape and key references, noting that CGS requires no influence model training (unlike MATES), which is a concrete practical advantage.\", \"EVALUATION CIRCULARITY IN HELD-OUT LOW-OCCUPANCY PERPLEXITY: The primary evaluation metric uses documents held out from the bottom 20% of reference corpus Voronoi cells as both the training selection criterion AND the evaluation signal. CGS is guaranteed to select synthetic data that covers exactly those cells — so the model trained with CGS learns to predict text statistically similar to those cells' content. The held-out perplexity improvement may reflect this distribution matching rather than genuine acquisition of tail knowledge. An independent external tail benchmark (e.g., LAMA probes, TriviaQA entity-frequency stratification with Wikipedia pageview statistics) should be the primary metric for falsifiability; the held-out low-occupancy perplexity should be demoted to a secondary diagnostic. The TriviaQA head/tail split already exists in the proposal and is the better primary metric — reframe accordingly.\", \"EMBEDDING COMPUTATION BUDGET UNDERESTIMATED: The proposal allocates '~10 H100-hours' for embedding 'a 10B-token reference corpus' plus synthetic candidates described elsewhere as 'hundreds of millions.' Back-of-envelope: Qwen3-Embedding processing 200M synthetic documents at 512 tokens each = 100B tokens; at ~1M tokens/sec on an H100 (optimistic), this is ~28 hours just for the synthetic corpus, separate from the reference corpus embedding. The auto-research mode with 12 grid configurations reuses the same embedding index but the initial build is underestimated. The generator should clarify the exact candidate corpus size (e.g., 'we precompute embeddings for a 50M-document synthetic pool generated by Qwen3-72B') and revise the embedding H100-hour estimate accordingly.\", \"TRAINING MODEL ARCHITECTURE UNSPECIFIED: The proposal trains models from scratch at 360M and 1.3B parameters but never states what architecture, tokenizer, or training codebase is used. Reproducibility requires specifying whether this is a GPT-2/LLaMA-style decoder, what the sequence length is, which optimizer and learning rate schedule, and which codebase (nanoGPT, LitGPT, OLMo, etc.). Without this, the method cannot be replicated. The user's requirements specifically mention 'Pythia, OLMo-1B, Qwen-0.5B/1.8B' as small open models — the proposal should either use one of these (OLMo-1B is Chinchilla-optimal-friendly and has a public codebase) or explicitly justify the choice of a custom architecture.\"]\nFeedback: The Round 1 revision was thorough — all eight original issues have been addressed, and the proposal is substantially stronger. Three targeted fixes will make this submission-ready:\n\n1. RESOLVE THE TIMELINE CONTRADICTION: The paper cannot claim to target a 16-day deadline while describing a 3-5 month execution plan. Pick one of two framings: (A) Auto-research framing — declare upfront that the submission is enabled by automated experimentation (8-12 days GPU wall-clock) and that writing proceeds in parallel; explicitly carve the paper into 'Tier 1 results (guaranteed by submission)' and 'Tier 2 results (best-effort, described as ongoing if not complete).' (B) Scoped-to-Tier-1 framing — submit with 360M ablations only, explicitly position Tier 2 as future work, and argue that the 8-config ablation at Chinchilla-optimal scale is sufficient to support the core CGS claims. Either framing is honest; the current hybrid is not.\n\n2. ADD MATES TO THE LANDSCAPE AND DIFFERENTIATE: Add a paragraph: 'MATES (NeurIPS 2024, arXiv:2406.06046) trains a lightweight influence model that continuously adapts to the evolving pretraining model's data preferences, achieving 2× the gain of prior SOTA. CGS differs on two axes: (a) CGS requires no influence model training — the FAISS IVF index is built once over the fixed reference corpus, not updated per training step; (b) CGS targets a specific failure mode (CQF distribution-matching rather than quality) rather than maximizing generic influence. MATES is computationally intensive and applied to general pretraining data; CGS is a lightweight post-hoc selector for synthetic-real mixing pipelines.' Include MATES as a formal key reference.\n\n3. FIX THE EVALUATION CIRCULARITY: Demote 'held-out low-occupancy perplexity' to a sanity check and promote the TriviaQA head/tail split as the primary falsifiable metric. The held-out ppl measures exactly what CGS was optimized to cover — it's not an independent test. The TriviaQA split uses an external resource (Wikipedia page views) to define head/tail entities, making it independent of the FAISS cell structure. Add this framing explicitly in the evaluation section: 'We use the TriviaQA tail-entity accuracy as the primary test of whether tail coverage translates to downstream knowledge acquisition, since it is defined independently of our FAISS cell structure.'\n\n4. SPECIFY THE TRAINING ARCHITECTURE: Use OLMo-1B architecture (open codebase, publicly documented) scaled down to 360M for Tier 1 and use OLMo-1B directly for Tier 2. This satisfies the user's requirement to use open small models and makes the experiments fully reproducible with a widely-known codebase.\n\n5. CLARIFY EMBEDDING BUDGET: State explicitly the size of the synthetic candidate pool (e.g., '50M documents from Qwen3-72B, 512 tokens avg') and revise the 10H embedding estimate to match. If the candidate pool is larger, embed in streaming batches and update the budget accordingly.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MISSING CRITICAL CONCURRENT WORK — Group-MATES (NeurIPS 2025, arXiv:2502.14709): This paper extends MATES with clustering-based group-level data selection, achieving 3.5–9.4% relative gains and 1.75× token efficiency over state-of-the-art individual selection. It uses embedding-based clustering to partition data into groups and selects within clusters — structurally overlapping with CGS's Voronoi cell approach. The proposal cites MATES (NeurIPS 2024) but not its NeurIPS 2025 successor. A reviewer will notice this immediately. Differentiation: Group-MATES uses influence-weighted group selection without a real-data reference density; CGS specifically targets low-occupancy tail cells defined against a reference corpus and requires no influence model. This should be added to the landscape section.\", \"EVALUATION MISSING USER-REQUIRED DIVERSITY METRICS: The user's hard constraints explicitly list 'diversity metrics (self-BLEU, n-gram entropy)' as required evaluation. The proposal evaluates TriviaQA tail/head accuracy, Head-to-Tail benchmark, standard downstream tasks, and held-out perplexity — but includes no diversity metrics for the selected synthetic data. CGS should demonstrate that its tail-targeted selection produces more diverse text than CQF (which selects fluent head-distribution text). Self-BLEU and n-gram entropy of selected synthetic data are cheap to compute (CPU-only, no GPU required) and would directly substantiate the coverage-vs-classifier-proxy claim.\", \"ICLR 2026 VENUE STATUS OF FOUNDATION PAPER UNCONFIRMED: arXiv:2510.00866 ('The Data-Quality Illusion') is submitted to ICLR 2026 (OpenReview ID: vSBACt34gS, modified February 2026) but its acceptance/rejection decision could not be confirmed via independent search. If this paper was rejected from ICLR 2026, the 'opportunity' narrative built around it ('CQF is shown to be illusory... arXiv:2510.00866') is weakened. The proposal should either (a) confirm the status and cite it accordingly, or (b) hedge: 'arXiv:2510.00866, under review; the empirical finding stands independently of peer review status.' The current citation as 'submitted to ICLR 2026' is ambiguous.\", \"LESS-IS-MORE DIFFERENTIATION NEEDS EXPLICIT STATEMENT: The proposal says CGS 'extends Less is More to pretraining scale with a tail-density threshold,' but a reviewer could ask: why not just run Less is More (arXiv:2504.14508) on the pretraining synthetic candidate pool with tail filtering? The proposal must explicitly state: 'Less is More maximizes coverage of ALL embedding cells uniformly — without a reference-corpus density criterion, it would waste selection budget on head cells already well-covered by real data. CGS adds the critical step of using real-data Voronoi occupancy as a gate: only tail cells (bottom 20–25% by reference occupancy) are eligible for synthetic coverage. This reference-density threshold is the mechanistic link to the CQF failure documented in arXiv:2510.00866, which Less is More does not establish.'\", \"ONLINE-METHOD COMPETITORS NOT ACKNOWLEDGED: ICLR 2026 accepted two online pretraining data curation methods — 'Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods' (ADAPT) and 'AC-ODM: Actor-Critic Online Data Mixing' — that are direct competitors to offline approaches like CGS. A reviewer familiar with ICLR 2026 will ask why CGS (a static offline filter) is preferable to online reweighting. The proposal should add one sentence: 'Online methods like ADAPT and AC-ODM adapt during training but cannot target the specific synthetic-real tail gap documented in arXiv:2510.00866, since they optimize generic influence rather than reference-density-defined tail coverage; CGS is a zero-overhead offline pre-filter compatible with any online method.'\"]\nFeedback: The Round 2 revision was comprehensive — all five prior issues are resolved. Three targeted fixes will make this submission-ready:\n\n1. ADD GROUP-MATES TO LANDSCAPE: Insert a differentiation paragraph after the MATES discussion: 'Group-MATES (NeurIPS 2025, arXiv:2502.14709) extends MATES to group-level selection by clustering training data using relational influence weights and selecting within clusters, achieving 3.5–9.4% gains. CGS differs on three axes: (a) CGS requires no influence model — Voronoi cells are defined by k-means over the fixed reference corpus, not by data-data influence weights; (b) CGS uses reference-corpus density as the selection criterion, not influence; (c) CGS targets the synthetic-real distribution gap specifically — Group-MATES operates within a single corpus without a real-data reference.' Add arXiv:2502.14709 to key_references.\n\n2. ADD DIVERSITY METRICS TO EVALUATION: The user hard-requires self-BLEU and n-gram entropy. Add to the evaluation section: 'Diversity of selected synthetic data: we compute corpus-level self-BLEU (lower = more diverse) and 4-gram entropy (higher = more diverse) over the synthetic subset selected by each method. CGS should show lower self-BLEU and higher n-gram entropy than CQF, since CQF preferentially selects fluent head-distribution text with low lexical diversity. This is computed post-selection on CPU before training begins.' These are zero-GPU-cost and directly substantiate the coverage claim.\n\n3. CLARIFY ICLR 2026 STATUS OF 2510.00866: Search or state that the paper's review status is uncertain and hedge accordingly. Change all references to 'submitted to ICLR 2026 (preprint; peer review status pending)' to avoid implying acceptance or publication. The empirical finding is sound regardless of venue; the paper should be defensible as a preprint citation.\n\n4. Add a single sentence addressing online-method competitors (ADAPT/AC-ODM, ICLR 2026) positioning CGS as a compatible pre-filter rather than a competing paradigm.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"EMBEDDING COMPUTE ARITHMETIC ERROR — BUDGET VIOLATION: The '~36 H100-hours' embedding figure is internally inconsistent with the stated throughput. At 100K tok/s per H100 GPU, embedding 25.6B synthetic tokens alone requires 256,000s = 71 GPU-hours; adding 5B reference tokens adds 14H = 85H total. On 4 GPUs: wall-clock = 21.3H, GPU-hours = 85H — NOT 36H. The '36H / 4 GPUs = 9H wall-clock' arithmetic requires 236K tok/s per GPU, which contradicts the stated 100–150K range. The corrected total budget is ~2H (Exp 0) + ~85H (embedding) + ~72H (Tier 1) + ~88H (Tier 2) + ~2H (eval) = ~249H, exceeding the user's hard ≤200H constraint by ~25%. The generator must either: (a) document a higher throughput (e.g., 250K+ tok/s with optimized large-batch encoding on H100) with citations, (b) reduce the synthetic pool to ~15M documents to bring embedding under 30H, or (c) explicitly scope Tier 2 as unfunded and recompute the budget without it (~161H).\", \"PROXY MODEL RELIABILITY UNADDRESSED: 'Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice' (ICLR 2026 Poster, openreview.net/forum?id=2FZC0c06jP) directly shows that conclusions about data selection quality 'can flip with even minor adjustments to training hyperparameters' when using small proxy models. CGS uses Pythia-410M (Tier 1) to determine the winning selection method before scaling to Pythia-1.4B (Tier 2), without any mention of the recommended reduced learning-rate protocol (10–100× smaller than standard) to ensure transfer reliability. The generator should add one sentence in the Tier 1 training setup: 'To improve reliability of proxy-to-full-scale transfer, we follow the protocol of [ICLR 2026 paper] and run Tier 1 with both standard and 10× reduced learning rates; the winning configuration uses the reduced-LR ranking.'\", \"arXiv:2510.00866 STATUS: This foundational paper ('The Data-Quality Illusion'), upon which the entire 'opportunity' narrative is built, does not appear in any ICLR 2026 accepted paper listing despite having been submitted (OpenReview ID: vSBACt34gS). ICLR 2026 decisions are public as of April 2026. Probable rejection. The proposal correctly hedges as 'preprint; peer review status pending,' but the generator should add a sentence that explicitly acknowledges the opportunity narrative holds independently of peer review: 'The empirical finding that CQF improves downstream task performance via distribution-matching rather than genuine quality improvement is independently reproducible; the CGS method does not depend on arXiv:2510.00866 being published at a venue.'\", \"ABLATION GRID DESCRIPTION INCONSISTENCY: The proposal states '8 configurations: (i) CGS vs. CQF-Wikipedia vs. CQF-FineWebEdu vs. random (4 selection methods); (ii) tail threshold 20th vs. 25th percentile.' But only CGS has a tail threshold — the other three methods have no threshold parameter. Crossing 4 methods × 2 thresholds implies that CQF-Wikipedia, CQF-FineWebEdu, and random are each run twice, which is wasteful and unexplained. The generator should clarify: either the grid is 6 runs (CGS-20th, CGS-25th, CQF-Wikipedia, CQF-FineWebEdu, random, plus one additional baseline) or 5 runs (CGS × 2 + 3 others × 1), not 8.\"]\nFeedback: The proposal has addressed all five Round 3 issues cleanly — Group-MATES differentiation, diversity metrics (self-BLEU/n-gram entropy), 2510.00866 status hedge, Less-is-More explicit differentiation, and ADAPT/AC-ODM positioning are all now handled correctly. The method remains novel and the evaluation design is among the strongest aspects of the proposal. Three targeted fixes will make this submission-ready:\n\n1. FIX EMBEDDING COMPUTE AND REBALANCE BUDGET: The '36H embedding' figure has a verifiable arithmetic error — correct it to ~57–85H depending on throughput, or better, document the actual H100 throughput with optimized large-batch inference (claim a specific number like '~250K tok/s with batch=512 on H100 using flash attention') and show the math. If the corrected embedding budget pushes total over 200H, explicitly drop Tier 2 from the funded scope: 'Tier 2 (1.4B) runs proceed only if embedding completes in under 45H; otherwise Tier 2 is deferred to camera-ready per the proposal's early-stop clause.' This keeps the budget under control without changing the method.\n\n2. ADD PROXY RELIABILITY NOTE: Insert one sentence in the training setup: 'Following the protocol of [ICLR 2026 proxy reliability paper], Tier 1 ablations are run at both standard learning rate (3×10⁻⁴) and a 10× reduced rate (3×10⁻⁵); selection method rankings are determined from the reduced-LR runs for reliable Tier 2 transfer.' This costs zero extra GPU-hours (same runs, different LR) and preempts a reviewer familiar with ICLR 2026 data curation work.\n\n3. CLARIFY ABLATION GRID: Specify that the 8 configurations are: (CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, random) = 5 configurations, OR explain what the 6th–8th configurations are (e.g., additional IVF nlist sensitivity runs). As written, '4 methods × 2 thresholds = 8' implies running non-CGS methods with two threshold values, which is a design error.\n\n4. ADD INDEPENDENT VALIDATION SENTENCE: Add: 'The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status; CGS would be motivated equally if the finding were confirmed by independent replication.'\n\n### Round 5 review\nVerdict: revise\nIssues: [\"UNVERIFIED THROUGHPUT CREATES LATENT BUDGET RISK: ModernBERT-large H100 throughput of 100-150K tokens/sec is unverified. Official ModernBERT benchmarks (Hugging Face blog, arXiv:2412.13663) are on RTX 4090 only, with no absolute throughput numbers published for any hardware. If actual H100 throughput is ~50K tok/s (plausible if 4090 throughput is ~25-35K and H100 ≈ 2× 4090 for encoder inference), total embedding reaches ~70.5 GPU-hours, pushing overall budget to ~208H — 4% over the 200H hard constraint. The proposal should add one of: (a) a citation for the 100-150K figure (e.g., the ModernBERT benchmark table from the full PDF), (b) a one-time throughput benchmark before committing to full embedding ('we benchmark ModernBERT-large throughput in the first 30 minutes of Experiment 0; if throughput < 60K tok/s, the synthetic pool is reduced from 15M to 10M documents, reducing embedding to ~47H and total budget to ~185H'), or (c) an explicit early-stop: 'if embedding does not complete within 45 GPU-hours, Tier 2 is deferred to camera-ready.'\", \"MISSING ICLR 2025 ORAL: ENTIGRAPH (arXiv:2409.07431): Synthetic Continued Pretraining via EntiGraph is the highest-profile prior work on improving tail-knowledge acquisition via synthetic data — it is an ICLR 2025 Oral presentation, directly targeting 'knowledge that appears only once or twice on the internet.' Every EMNLP reviewer familiar with the synthetic data literature will ask about it. The proposal must cite it and differentiate: EntiGraph *generates* new synthetic documents by traversing knowledge graph connections from a structured source corpus, whereas CGS is a *post-hoc selector* applicable to any pre-existing synthetic pool without requiring knowledge graph infrastructure. The approaches are complementary: CGS could in principle select tail-covering subsets of EntiGraph-generated data.\", \"CONCURRENT WORK arXiv:2604.13977 NOT ADDRESSED: 'How Can We Synthesize High-Quality Pretraining Data?' (April 2026) systematically compares synthetic pretraining strategies and finds 'output diversity is the dominant factor for downstream performance, more important than generator size or formatting.' This finding is directly relevant to CGS's claim that diversity (via tail coverage) outperforms classifier-based quality filtering. The proposal should acknowledge this concurrent result as corroborating evidence: if diversity dominates quality proxies, CGS's coverage-based criterion is on the right track. Failure to mention a 2026 result on the exact same topic will attract reviewer questions.\"]\nFeedback: This is the cleanest the proposal has been — all four Round 4 issues are resolved, budget arithmetic is now correct (15M docs / 7.68B tokens / ~175H total), and the evaluation design is strong. Three targeted fixes will resolve the remaining gaps:\n\n1. DOCUMENT MODERNBERT THROUGHPUT OR ADD FALLBACK: Add one sentence in the embedding pipeline description: 'Before committing to full-corpus embedding, we benchmark ModernBERT-large throughput on a 100K-document pilot (~51M tokens); if throughput < 60K tok/s, the synthetic pool is reduced to 10M documents to hold total budget under 185H.' This costs ~5 GPU-minutes and eliminates the budget risk entirely. Alternatively, cite the ModernBERT paper's supplementary Table (if it has H100 numbers) or note that H100 SXM is documented to deliver 2–4× RTX 4090 throughput for transformer inference, placing ModernBERT-large at 80–160K tok/s — cite the H100 whitepaper for the multiplier.\n\n2. ADD ENTIGRAPH ONE-LINER TO RELATED WORK: In the 'Coverage-based fine-tuning' cluster or as a new 'Tail knowledge via synthetic generation' bullet, add: 'EntiGraph (ICLR 2025 Oral, arXiv:2409.07431) generates synthetic continued-pretraining corpora by sampling entity pairs from a knowledge graph and synthesizing text connecting them, improving tail-fact acquisition in domain-specific settings. Unlike CGS, EntiGraph requires a structured knowledge corpus as input and generates new documents; CGS is a post-hoc selector for any pre-existing synthetic pool without knowledge graph infrastructure.' Also add arXiv:2409.07431 to key_references.\n\n3. ACKNOWLEDGE arXiv:2604.13977 AS CORROBORATING EVIDENCE: Add to the 'Synthetic data scale findings' cluster: 'Concurrent work (arXiv:2604.13977, April 2026) finds output diversity to be the dominant factor in synthetic pretraining quality — more impactful than generator size or formatting — providing independent corroboration for CGS's diversity-over-classifier-proxy hypothesis.' This converts a potential reviewer objection into supporting evidence.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"FACTUAL REFERENCE ERROR — arXiv:2512.24503 MISATTRIBUTION: The proposal lists arXiv:2512.24503 as the 'ADAPT: Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods' paper. Independent verification confirms arXiv:2512.24503 is 'Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice' (Wang et al., ICLR 2026 Poster) — the same proxy-model reliability paper the proposal already cites under openreview.net/forum?id=2FZC0c06jP. The proposal now has two different descriptions for the same arXiv ID and no valid arXiv ID for ADAPT. A reviewer who checks references will immediately flag this. Fix: (a) find and use the correct arXiv ID for ADAPT (if it has one), or cite it without an arXiv ID; (b) remove the duplicate arXiv attribution.\", \"MISCHARACTERIZATION OF CORROBORATING PAPER arXiv:2604.13977: The proposal claims arXiv:2604.13977 ('How Can We Synthesize High-Quality Pretraining Data?', April 2026) 'independently finds output diversity to be the dominant factor in synthetic pretraining quality — more important than generator size or formatting consistency.' Independent search finds the paper's dominant factors are structured output formats (tables, math problems, FAQs, tutorials) and rephrasing prompt design — NOT output diversity per se. Structured formats are a specific choice of diversity type, not the same as the diversity-targeting criterion CGS uses. The proposal's framing overstates the corroboration. Fix: replace 'output diversity is the dominant factor' with the paper's actual finding — e.g., 'structured output format and prompt design are dominant factors, outperforming raw scale and format-agnostic generation' — and argue this supports CGS's non-classifier-proxy approach rather than implying direct support for diversity-targeting per se.\", \"UNVERIFIED CLAIM: QuaDMix 'withdrawn from ICLR 2026': The proposal states arXiv:2504.16511 (QuaDMix) was 'withdrawn from ICLR 2026.' Independent search found no evidence of this withdrawal — the paper appears as an active arXiv preprint with no confirmed conference status. If QuaDMix is still under submission or published elsewhere, the phrase 'withdrawn' is factually wrong and weakens the proposal's credibility. Fix: change to 'arXiv preprint; conference status unconfirmed' or omit the venue claim entirely.\", \"UNCITED CONCURRENT WORK — arXiv:2510.02375: 'Pretraining with hierarchical memories: separating long-tail and common knowledge' (October 2025) explicitly addresses tail knowledge acquisition in pretraining via hierarchical parametric memory banks, achieving 2× parameter efficiency. While mechanistically orthogonal to CGS (architectural intervention vs. data selection), an EMNLP reviewer specializing in tail-knowledge acquisition will know this work and may ask why CGS is preferable to architectural solutions. The proposal should add a brief note: 'Architectural methods such as hierarchical memory banks (arXiv:2510.02375) address tail knowledge through model architecture changes rather than data selection; CGS is orthogonal and could complement such architectures by improving the training distribution seen by those memory components.'\"]\nFeedback: The proposal is substantively strong after five rounds of revision — the method is coherent, the budget is realistic, the evaluation avoids circularity, and the differentiation from Quad/MATES/Group-MATES/Less-is-More is now explicit and adequate. Three targeted reference fixes will bring this to submission quality:\n\n1. FIX THE ADAPT arXiv ID: arXiv:2512.24503 is Wang et al.'s proxy-model reliability paper, not ADAPT. Find ADAPT's correct arXiv ID (search 'online reweighting LLM pretraining generalization offline methods 2024 2025') or cite it by conference venue only (ICLR 2026 Workshop DATA-FM) without an arXiv ID. Remove the duplicate attribution.\n\n2. CORRECT THE 2604.13977 CHARACTERIZATION: The paper finds structured formats and rephrasing prompts dominate, not 'output diversity' as a general principle. Write instead: 'Concurrent work (arXiv:2604.13977, April 2026) finds that structured output formats (tables, FAQs, tutorials) and prompt design dominate synthetic pretraining quality — outperforming generator scale and format-agnostic generation — providing external corroboration that principled generation choices matter more than classifier-based selection proxies, consistent with CGS's non-proxy approach.' This still supports CGS without misrepresenting the paper.\n\n3. REMOVE 'WITHDRAWN FROM ICLR 2026' FROM QuaDMix: Change to 'arXiv preprint (arXiv:2504.16511)' and remove the venue claim until verifiable. The differentiation paragraphs are solid and do not depend on QuaDMix being withdrawn.\n\n4. ADD ONE SENTENCE ON arXiv:2510.02375: Under the tail-knowledge section, add the one-sentence orthogonality note recommended above. This converts a potential reviewer gap into a acknowledged scope decision.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-09T21:03:03.196Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-09T21:03:03.196Z",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-09T21:03:03.266Z_

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

## Idea under review (round 7/10)
{
  "title": "Tail-Coverage-Guided Synthetic Data Selection to Replace Classifier Quality Filtering",
  "core_problem": "Classifier-based quality filtering (CQF), the dominant method for selecting synthetic pretraining data used by GPT-3, LLaMA, and PaLM, is shown to be illusory — it improves downstream task performance not by improving language modeling quality but by implicit distribution-matching rather than genuine quality signals. Concurrently, synthetic data exhibits systematic distributional discrepancies relative to real data: top-p and temperature sampling truncate low-probability continuations, causing rare factual content to be systematically underrepresented in synthetic corpora. Kandpal et al. (ICML 2023) established a direct causal link: LLM accuracy on factual questions correlates strongly with the frequency of the underlying entity in pretraining documents, confirming that tail-knowledge acquisition depends on tail-content exposure during training. No principled selection criterion corrects for this distributional gap: CQF does not target it (and may worsen it by filtering toward fluent head-distribution text), while naïve random sampling inherits the generator's truncation bias wholesale. More recent model-aware selectors such as MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) adapt dynamically to the evolving model's preferences but do not target the specific tail-distribution gap — they optimize for generic influence rather than for correcting truncation-induced underrepresentation.",
  "opportunity": "Three concurrent findings create a gap that demands a new method: (1) 'The Data-Quality Illusion' (arXiv:2510.00866, preprint; peer review status pending) demonstrates that CQF does not improve language modeling on held-out high-quality data and argues the field should rethink synthetic data filtering from first principles; (2) 'Data Value in the Age of Scaling' (arXiv:2511.13640) identifies tail-knowledge underrepresentation as a systematic distributional discrepancy in synthetic data under real-synthetic mixing, linked to generative truncation mechanisms; (3) Kandpal et al. (ICML 2023) provides external causal validation: pretraining document frequency is a strong predictor of downstream accuracy on rare facts. Together, these findings establish that (a) CQF is the wrong solution, (b) the actual problem is a distributional gap at the tail, and (c) closing the tail gap causally improves knowledge acquisition. The opportunity is 'Coverage-Guided Sampling' (CGS): select synthetic examples to maximize marginal coverage of low-density regions of the real-data embedding space, directly targeting the distributional gap that CQF fails to address. This is the first synthetic data selector explicitly designed around the mechanism documented in arXiv:2510.00866 rather than a classifier proxy. The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status; CGS would be motivated equally if the finding were confirmed by independent replication. Concurrent work (arXiv:2604.13977, April 2026) finds that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are the dominant factors in synthetic pretraining quality — outperforming both larger generator models and format-agnostic generation strategies — providing external corroboration that principled, non-classifier-based generation and selection choices are the right axis for improving synthetic pretraining data quality, consistent with CGS's reference-density-gated approach.",
  "landscape": "CQF is used by all major pretraining pipelines (GPT-3, LLaMA, PaLM, RedPajama) but arXiv:2510.00866 (preprint; peer review status pending) shows its quality signal is misleading. Six clusters of prior work bound the proposal:\n\n**Diversity-quality pretraining selection.** Quad (arXiv:2409.16986, ICLR 2025 Spotlight) is the most important prior work. Quad clusters all pretraining data and uses a Multi-Armed Bandit (MAB) scheme favoring clusters with high influence scores (quality) or low selection frequency (diversity). CGS differs on three axes: (1) Criterion — CGS uses a real-data tail-density threshold (bottom 20–25% by Voronoi cell occupancy in a reference corpus) rather than influence-weighted underrepresentation; CGS does not require influence score computation, which is expensive to scale to billions of synthetic candidates; (2) Target — CGS applies specifically to the synthetic data mixing problem and requires a real-data reference corpus to define 'tail'; Quad operates within a single multi-source corpus without a reference density; (3) Motivation — CGS is grounded in the CQF failure mechanism documented in arXiv:2510.00866. QuaDMix (arXiv:2504.16511, withdrawn from ICLR 2026, openreview.net/forum?id=oLxx7OhAb1) from ByteDance proposes a parameterized quality-diversity sampling function using domain classification for diversity measurement and LightGBM for parameter search. Like Quad, QuaDMix does not target real-data tail density specifically.\n\n**Model-aware selection.** MATES (arXiv:2406.06046, NeurIPS 2024) trains a lightweight BERT-base influence model that continuously adapts to the evolving pretraining model's data preferences, updating every 10,000 steps. MATES achieves 2× the gain of prior SOTA (QuRating) on 410M and 1B models, at 11.5–21.7% computational overhead. CGS differs on three axes: (a) CGS requires no influence model training — the FAISS IVF index is built once over the fixed reference corpus before pretraining begins, versus MATES's periodic BERT-base retraining; (b) CGS requires no reference task definition — MATES's performance varies substantially with reference task choice, a deployment-time burden; (c) CGS targets a specific, mechanistically motivated failure mode (CQF distributional bias) rather than maximizing generic influence scores.\n\nGroup-MATES (arXiv:2502.14709, NeurIPS 2025) extends MATES to group-level selection: it trains a relational data influence model that weights individual sample influence by inter-data relationships, partitions the training corpus into clusters via these relationship weights, and selects within each cluster independently, achieving 3.5–9.4% relative gains and 1.75× token efficiency over individual selection baselines on DCLM at 400M–3B scales across 22 tasks. CGS differs on three axes: (a) CGS requires no influence model — Voronoi cells are defined by k-means over a fixed reference corpus embedding, not by data-data relational influence weights, making CGS zero-overhead relative to training; (b) CGS uses reference-corpus occupancy density as the selection gate — only tail cells (bottom 20–25% by reference occupancy) are eligible for synthetic coverage — rather than influence-weighted within-cluster scoring; (c) CGS targets the specific synthetic-real distributional gap documented in arXiv:2511.13640: it applies to a fixed synthetic candidate pool relative to a real-data reference corpus, whereas Group-MATES operates within a single training corpus without a reference density criterion.\n\n**Tail knowledge via synthetic generation.** EntiGraph (arXiv:2409.07431, ICLR 2025 Oral) addresses tail-knowledge acquisition through synthetic document generation: given a small domain corpus, it extracts salient entities, constructs a knowledge graph dynamically from entity-pair relationships via LM-driven synthesis, and generates new documents traversing those relationships — improving tail-fact retention in continued pretraining. Unlike CGS, EntiGraph is a generative method that requires a structured source corpus as input to drive entity extraction; it produces entirely new documents rather than selecting from a pre-existing pool, and is evaluated on domain-specific continued pretraining (QuALITY benchmark) rather than open-domain general pretraining. The approaches are orthogonal and complementary: CGS could select tail-covering subsets of an EntiGraph-generated corpus, concentrating the EntiGraph generation budget on the regions of real-data embedding space already underrepresented.\n\n**Architectural approaches to tail knowledge.** 'Pretraining with Hierarchical Memories: Separating Long-Tail and Common Knowledge' (arXiv:2510.02375, October 2025) addresses tail knowledge acquisition through model architecture changes rather than data selection: it introduces hierarchical parametric memory banks alongside a smaller core model, storing long-tail world knowledge in memory parameters while the core model captures common knowledge and general reasoning, with a 160M-parameter model plus 18M-parameter memory (fetched from a 4.6B bank) achieving performance comparable to a standard model with more than 2× the parameters. This architectural intervention is orthogonal to CGS: CGS improves the training distribution presented to any model architecture, and could complement hierarchical memory architectures by ensuring the training data seen by those memory components better covers tail-content regions.\n\n**Coverage-based fine-tuning.** 'Less is More: Adaptive Coverage for Synthetic Training Data' (arXiv:2504.14508, 2025) applies a greedy maximum-coverage objective to select synthetic fine-tuning data for NLP classifiers. CGS shares the max-coverage algorithmic skeleton but differs critically in three respects: (1) 'Less is More' maximizes coverage of ALL embedding cells uniformly — without a reference-corpus density criterion, it would waste selection budget on head cells already well-covered by real data, failing to address the distributional gap that CQF leaves open; CGS adds the critical step of using real-data Voronoi occupancy as a gate: only tail cells (bottom 20–25% by reference occupancy) are eligible, ensuring the entire selection budget is concentrated on underrepresented regions; (2) CGS applies at pretraining scale (hundreds of millions of candidates), requiring FAISS IVF for tractability; (3) this reference-density threshold is the mechanistic link to the CQF failure documented in arXiv:2510.00866, which 'Less is More' does not establish.\n\n**Online pretraining data curation.** ADAPT ('Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods', Zhao et al., ICLR 2026 Workshop DATA-FM, openreview.net/forum?id=zgn3P31NWf) and AC-ODM ('Actor-Critic Online Data Mixing', arXiv:2505.23878, preprint) represent an online paradigm: rather than pre-filtering the candidate pool, they dynamically reweight or re-mix training samples during training based on loss signals. CGS is orthogonal and compatible: as a static offline pre-filter, it reduces the synthetic candidate pool to tail-coverage-optimal documents before training begins with zero ongoing overhead; an online reweighter can further adapt the mix at training time after CGS has already narrowed the pool. Neither ADAPT nor AC-ODM targets the specific synthetic-real tail-density gap documented in arXiv:2510.00866 — they optimize generic influence or domain balance, not reference-density-defined tail coverage.\n\n**Synthetic data scale findings.** 'Demystifying Synthetic Data in LLM Pre-training' (arXiv:2510.01631, EMNLP 2025) finds ~30% rephrased synthetic data is empirically optimal but provides no mechanistic filter. arXiv:2511.13640 characterizes three-phase scaling behavior under real-synthetic mixing and identifies tail underrepresentation as a systematic discrepancy without a selection remedy. Concurrent work arXiv:2604.13977 ('How Can We Synthesize High-Quality Pretraining Data?', April 2026) systematically compares synthetic pretraining strategies across generator models and formats, finding that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are dominant factors in synthetic pretraining quality — outperforming both larger generator models and format-agnostic generation strategies. This provides independent corroboration for CGS's non-classifier-proxy approach: if principled generation choices outperform raw scale and classifier-based proxies, the right axis to optimize is how data is selected and structured rather than whether a quality classifier endorses it.\n\n**Tail knowledge evaluation and deduplication.** Kandpal et al. (arXiv:2211.08411, ICML 2023) establish that LLM accuracy on factual questions correlates causally with pretraining document frequency, providing the empirical foundation for CGS's tail-coverage hypothesis. 'Head-to-Tail' (arXiv:2308.10168, NAACL 2024) provides a purpose-built 18K QA benchmark explicitly stratified into head, torso, and tail facts by knowledge graph frequency — an independent evaluation resource for CGS. D4 (NeurIPS 2023) uses FAISS k-means for deduplication/diversification via distance-to-centroid pruning; it applies a distance heuristic not a tail-density threshold and does not target the synthetic selection sub-problem.",
  "approach": "Coverage-Guided Sampling (CGS) selects synthetic pretraining data by maximizing coverage of underrepresented tail regions in real-data embedding space.\n\n**Method.** We embed a reference corpus (5B-token stratified sample of Dolma, preserving domain balance) and all candidate synthetic documents using ModernBERT-large, then build a FAISS IVF index over the real-data embeddings. The resulting Voronoi cell structure partitions semantic space; 'tail cells' are defined as cells in the bottom 20–25% by real-data occupancy. CGS then greedily selects synthetic documents maximizing marginal coverage of tail cells via a streaming maximum-coverage subproblem — no quality classifier training required. ModernBERT-large is chosen for embedding over larger alternatives due to its superior throughput: the official ModernBERT benchmark documents ~52K tokens/sec for ModernBERT-large on RTX 4090 (arXiv:2412.13663); H100 SXM delivers 2–4× RTX 4090 throughput for encoder inference (NVIDIA H100 Tensor Core GPU product brief), placing ModernBERT-large at ~100–200K tok/s on H100 — versus ~15–30K for Qwen3-Embedding-8B. To verify this before committing to full-corpus embedding, we run a 100K-document throughput pilot (~51M tokens, ~5 GPU-minutes) at the start of Experiment 0; if measured throughput is below 60K tok/s, the synthetic pool is reduced from 15M to 10M documents (7.68B → 5.12B tokens), reducing total embedding to ~47H and holding overall budget under 185H. Embedding quality is validated in Experiment 0.\n\n**Mechanistic validation experiment (Experiment 0, ~2 H100-hours).** Before committing to training runs, we validate the core empirical hypothesis: (a) Generate three synthetic corpora of 10M tokens each using Qwen3-72B with top-p ∈ {0.5, 0.85, 0.95}; embed and assign each document to a Voronoi cell; measure whether lower top-p concentrates documents in higher-occupancy cells (expected: yes, since low top-p collapses to high-probability continuations); (b) Embed 5,000 Wikidata long-tail documents (entities appearing <100 times in C4) and confirm they cluster significantly more in low-occupancy cells than a random C4 sample. If (a) shows r < 0.3 between top-p and mean cell occupancy, or (b) shows no significant enrichment, halt before Tier 1 and revise the tail-density criterion.\n\n**Model architecture and training.** Following the precedent of MATES (NeurIPS 2024), Quad (ICLR 2025), and D4 (NeurIPS 2023), we use the Pythia model family (EleutherAI GPT-NeoX codebase) for full reproducibility:\n- *Tier 1 — Systematic ablation: Pythia-410M* (24 layers, hidden dim 1024, 16 heads, 2048 sequence length; ~8B tokens, Chinchilla-optimal). AdamW optimizer with β1=0.9, β2=0.95, weight decay 0.1; cosine LR schedule with 1% warmup steps. Following Wang et al. ('Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice,' ICLR 2026 Poster), all Tier 1 ablations use a 10× reduced peak learning rate of 3×10⁻⁵ (instead of the standard 3×10⁻⁴) to ensure selection method rankings derived from the 410M proxy runs transfer reliably to Tier 2 at 1.4B scale — this costs no additional GPU-hours since the reduced-LR runs replace rather than supplement standard-LR runs. Batch size ~2M tokens. 5 configurations: CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, and random baseline. Only CGS has a tail-threshold parameter; the three non-CGS methods run once without threshold variation. Each run: ~9 H100-hours on 1 GPU.\n- *Tier 2 — Scaling check: Pythia-1.4B* (24 layers, hidden dim 2048, 16 heads, 2048 sequence length; 10B tokens). Same optimizer family with peak LR 2×10⁻⁴. 2 configurations: best CGS from Tier 1 vs. CQF-FineWebEdu. Each run: ~44 H100-hours (4 GPUs × ~11h wall-clock via data parallelism). Using Pythia-1.4B (not 1.3B) ensures exact architecture reproducibility with the published model family.\n\n**Synthetic candidate pool.** We precompute embeddings for a fixed 15M-document synthetic pool generated by Qwen3-72B (top-p=0.9, temperature=1.0, avg 512 tokens/document = 7.68B tokens total). At 100K tokens/sec per H100 (nominal): the 7.68B synthetic tokens require 76,800s ≈ 21.3 GPU-hours; the 5B-token reference corpus requires 50,000s ≈ 13.9 GPU-hours; total embedding ≈ 35 GPU-hours ≈ 8.8H wall-clock on 4 GPUs. Under the throughput fallback (10M docs, ~5.12B tokens), embedding reduces to ~19H + 13.9H ≈ 33H for synthetic + reference ≈ 47H total. This pool size provides ample selection diversity: 7.68B tokens exceeds the synthetic allocation for both Tier 1 (~2.4B tokens at 30% synthetic) and Tier 2 (~3B tokens at 30% synthetic) by over 2.5×. FAISS IVF build is CPU-bound (~2h on 32 cores) and runs concurrently with early embedding steps.\n\n**IVF nlist calibration.** nlist ≈ sqrt(N_reference_docs) per FAISS best practices. Tier 1 pilots probe two nlist settings (±30%) to confirm tail cell occupancy is well-separated; this is CPU-only analysis on the pre-built index (zero GPU cost). If cell structure is degenerate, we correct before the Tier 2 run.\n\n**Evaluation — primary, secondary, and diversity metrics.** The evaluation design explicitly separates the training criterion (FAISS cell coverage) from the test signal to avoid circularity:\n\n(1) *Primary — TriviaQA head/tail accuracy split (independent external metric)*: Using Wikipedia page-view statistics to stratify TriviaQA questions into head entities (top 20% by views, ~1K questions) and tail entities (bottom 20%, ~1K questions), we measure accuracy separately. This stratification uses an external resource (Wikipedia traffic data) wholly independent of the FAISS cell structure. Per Kandpal et al. (ICML 2023), tail-entity accuracy is the most causally meaningful test of whether tail coverage translates to knowledge acquisition. We report the tail/head accuracy ratio as the primary CGS-vs-CQF gap metric.\n\n(2) *Additional independent benchmark — Head-to-Tail (NAACL 2024)*: This purpose-built 18K QA benchmark stratifies facts into head, torso, and tail by knowledge graph frequency (Wikidata). It provides a second external validation of tail knowledge independent of both FAISS and Wikipedia pageviews, strengthening the falsifiability of the tail-coverage claim.\n\n(3) *Secondary — Standard downstream benchmarks*: HellaSwag, WinoGrande, ARC-E/C, PIQA — required for comparability with Quad, D4, MATES, Group-MATES, and CQF baselines. CGS should match or exceed CQF on these benchmarks; failure here would indicate coverage-only selection sacrifices head-distribution capabilities.\n\n(4) *Diversity of selected synthetic data (CPU-only, zero GPU cost)*: We compute corpus-level self-BLEU (Zhu et al., 2018; lower = more diverse) and 4-gram entropy (higher = more diverse) over the synthetic subset selected by each method (CGS, CQF-Wikipedia, CQF-FineWebEdu, random). These metrics are computed post-selection before training begins. CGS should exhibit lower self-BLEU and higher n-gram entropy than CQF-selected data, since CQF preferentially selects fluent head-distribution text with low lexical diversity. This directly substantiates the coverage-vs-classifier-proxy claim: not only does CGS target underrepresented semantic regions, but the selected text should be measurably more lexically diverse than CQF output — consistent with the concurrent finding (arXiv:2604.13977) that principled generation choices (structured formats, prompt design) outperform classifier-based proxies in synthetic pretraining quality.\n\n(5) *Diagnostic — Held-out low-occupancy perplexity*: 5% of reference corpus documents from the bottom 20% occupancy cells are held out before training and used to measure model perplexity. This metric is demoted to a sanity check because CGS is explicitly optimized to cover exactly those cells — perplexity improvement here confirms distribution matching, not necessarily genuine knowledge acquisition. It is reported alongside (1) and (2) but not used as a primary falsifiability claim.\n\n**Falsifiable primary claim**: CGS achieves higher TriviaQA tail-entity accuracy than CQF while matching CQF on standard downstream benchmarks, directly operationalizing the quality-vs-coverage paradox documented in arXiv:2510.00866. The diversity metrics (self-BLEU, n-gram entropy) provide a secondary mechanistic check confirming that CGS's tail-coverage selection is not collapsing to a high-fluency, low-diversity subset.\n\n**Timeline and execution mode.** Given the EMNLP 2026 ARR deadline of May 25, 2026 (16 days from proposal date), the primary execution path is auto-research mode. GPU wall-clock with 4× H100: Experiment 0 (~2h, including 5-min throughput pilot) → Embedding (~8.8h, 4 GPUs, or ~5.8h under 10M-doc fallback) → FAISS build (~2h CPU concurrent) → Tier 1 ablation grid (~18h, 4 experiments in parallel in batch 1, then 1 remaining) → Tier 2 scaling check (~22h, 2 sequential runs with 4-GPU data parallelism). Total GPU wall-clock: ~50.8 hours (~2.1 days) nominal; ~48.8h under fallback. Paper writing begins in parallel on day 1; Tier 1 results are guaranteed by day 4; Tier 2 results are best-effort. If Tier 2 runs do not complete before submission, the 1.4B experiments are described as ongoing and submitted to camera-ready.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~172 H100-hours (Experiment 0 ~2h including 5-min throughput pilot; embedding ModernBERT-large on 15M synthetic docs + 5B reference corpus ~35h [nominal, throughput ≥ 60K tok/s] or ~47H [10M-doc fallback if throughput < 60K tok/s, reducing synthetic pool from 7.68B to 5.12B tokens]; FAISS IVF build CPU-bound ~0h GPU; Tier 1 ablations 5 configurations × ~9h = 45h; Tier 2 scaling check 2 runs × ~44h = 88h; misc eval ~2h). Budget stays ≤185H under fallback scenario; arithmetic verified: 7.68B synthetic tokens ÷ 100K tok/s = 21.3H + 5B reference ÷ 100K tok/s = 13.9H = 35.2H nominal.",
      "gpu_utilization": "Low (~40% active) — researcher waits between tiers to review Experiment 0 results and pilot outcomes before committing to 1.4B runs.",
      "timeline": "3–5 months. INCOMPATIBLE with May 25, 2026 ARR deadline — use auto-research mode for deadline-constrained execution.",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$420–615 at $2.44–3.56/hr per H100 (RunPod/Lambda Labs current pricing)",
      "risk_note": "If Experiment 0 (mechanistic validation) fails — i.e., top-p does not correlate with cell occupancy in the expected direction — the core hypothesis needs revision before Tier 1 ablations begin. Caught in the first ~2 H100-hours. If throughput pilot shows < 60K tok/s, pool is reduced to 10M docs and budget stays under 185H."
    },
    "human_in_loop": {
      "gpu_hours": "~190 H100-hours (manual base ~172H plus agent overhead: 2 additional 410M sensitivity runs for IVF nlist ±30% around baseline and ModernBERT-large vs. sentence-transformers/all-MiniLM-L6-v2 embedding model speed check, each ~9h = 18H extra; plus ~0H GPU for nlist structure analysis which is CPU-only; throughput fallback to 10M-doc pool reduces embedding by ~9H if triggered, capping at ~181H under fallback).",
      "gpu_utilization": "Moderate (~60% active) — agent queues experiments continuously but awaits human approval before committing to each Tier 2 run.",
      "timeline": "4–6 weeks. INCOMPATIBLE with May 25, 2026 ARR deadline — use auto-research mode for deadline-constrained execution.",
      "team": "1 researcher, ~45 min/day check-in to approve tier transitions and review Experiment 0 results",
      "claude_api_cost": "$200–350 (experiment queue management, Experiment 0 result interpretation, IVF calibration guidance)",
      "estimated_gpu_cost": "~$464–676 at $2.44–3.56/hr per H100"
    },
    "auto_research": {
      "gpu_hours": "~175 H100-hours (Experiment 0 ~2h including 5-min throughput pilot; embedding ModernBERT-large for 15M synthetic docs [7.68B tokens] + 5B reference corpus ~35h [throughput ≥ 60K tok/s] or ~47H [10M-doc fallback if throughput < 60K tok/s]; FAISS IVF build CPU-bound ~0h GPU; Tier 1 ablation grid 5 configurations × ~9h = 45h; Tier 2 scaling check 2 runs × ~44h = 88h; misc eval ~3h). Budget ≤175H nominal, ≤185H under fallback; capped at 175H by early-stopping if Experiment 0 fails (saves ~138H by avoiding Tier 1 and Tier 2).",
      "gpu_utilization": "High (~85% active) — agent queues Experiment 0 (with throughput pilot) → embedding → FAISS build → Tier 1 ablation grid → Tier 2 runs without human wait. ~15% overhead from API round-trips and CPU-bound FAISS builds between GPU steps.",
      "timeline": "8–12 days total: ~2.1 days GPU wall-clock compute (50.8 hours on 4× H100) + paper writing in parallel from day 1. Tier 1 results available by day 4; Tier 2 results by day 5. Writing days 1–14 (parallel); submission day 16 (May 25, 2026 ARR deadline). COMPATIBLE with deadline under this framing: Tier 1 results are guaranteed at submission; Tier 2 results are best-effort and described as ongoing in the paper if not complete.",
      "team": "0 (initial setup ~3h: configure ModernBERT-large embedding pipeline with FAISS IVF builder, GPT-NeoX training harness with eval on HellaSwag/WinoGrande/ARC/PIQA + TriviaQA head/tail + Head-to-Tail benchmark)",
      "claude_api_cost": "$600–900 (automated Experiment 0 interpretation, ablation grid orchestration, early-stopping decisions, TriviaQA stratification computation, final report generation — estimated 5,000–8,000 API turns)",
      "estimated_gpu_cost": "~$427–623 at $2.44–3.56/hr per H100",
      "speed_bottleneck": "4× H100 allows: Embedding (15M synthetic docs + 5B reference corpus) completes in ~8.8h wall-clock (35H ÷ 4 GPUs); Tier 1 grid runs in ~18h wall-clock (4 configs in parallel batch 1, then 1 remaining config in batch 2, each ~9H on 1 GPU); Tier 2 serializes at ~11h wall-clock each with 4-GPU data parallelism (2 runs = 22h). Total GPU wall-clock: ~2h (Exp 0) + ~8.8h (embedding) + ~18h (Tier 1) + ~22h (Tier 2) ≈ 50.8h ≈ 2.1 days.",
      "risk_note": "Early-stopping trigger: if Experiment 0 shows Pearson r < 0.3 between top-p value and mean cell occupancy rank, halt and report mechanism failure before consuming Tier 1 compute. Throughput early-stop: if 5-min pilot measures < 60K tok/s, reduce synthetic pool from 15M to 10M documents before proceeding to full embedding, holding total budget under 185H. Pre-specified thresholds prevent exhaustive exploration of degenerate configurations."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026; conference October 24–29, 2026, Budapest, Hungary). Primary execution path: auto-research mode, with Tier 1 (Pythia-410M) results guaranteed at submission and Tier 2 (Pythia-1.4B) submitted to camera-ready."
  ],
  "level": "top-tier",
  "key_references": [
    "The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining (arXiv:2510.00866, preprint; peer review status pending)",
    "Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures (arXiv:2511.13640, 2025)",
    "Harnessing Diversity for Important Data Selection in Pretraining Large Language Models (Quad, arXiv:2409.16986, ICLR 2025 Spotlight)",
    "QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining (arXiv:2504.16511, withdrawn from ICLR 2026, openreview.net/forum?id=oLxx7OhAb1)",
    "MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models (arXiv:2406.06046, NeurIPS 2024)",
    "Group-MATES: Group-Level Data Selection for Language Model Pretraining (arXiv:2502.14709, NeurIPS 2025)",
    "Synthetic Continued Pretraining via EntiGraph (arXiv:2409.07431, ICLR 2025 Oral)",
    "Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice (Wang et al., ICLR 2026 Poster, openreview.net/forum?id=2FZC0c06jP)",
    "Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods — ADAPT (Zhao et al., ICLR 2026 Workshop DATA-FM, openreview.net/forum?id=zgn3P31NWf)",
    "AC-ODM: Actor-Critic Online Data Mixing for Sample-Efficient LLM Pretraining (arXiv:2505.23878, preprint)",
    "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls (arXiv:2510.01631, EMNLP 2025)",
    "How Can We Synthesize High-Quality Pretraining Data? (arXiv:2604.13977, April 2026)",
    "Large Language Models Struggle to Learn Long-Tail Knowledge (Kandpal et al., arXiv:2211.08411, ICML 2023)",
    "Head-to-Tail: How Knowledgeable are Large Language Models in Long-Tail Knowledge? (arXiv:2308.10168, NAACL 2024)",
    "Pretraining with Hierarchical Memories: Separating Long-Tail and Common Knowledge (arXiv:2510.02375, October 2025)",
    "Measuring Diversity in Synthetic Datasets (arXiv:2502.08512, ICML 2025)",
    "Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning (arXiv:2511.01490, ACL Findings 2026)",
    "Less is More: Adaptive Coverage for Synthetic Training Data (arXiv:2504.14508, 2025)",
    "D4: Improving LLM Pretraining via Document De-Duplication and Diversification (NeurIPS 2023)",
    "Scaling Laws of Synthetic Data for Language Models (arXiv:2503.19551, 2025)",
    "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling (arXiv:2304.01373, ICML 2023)",
    "ModernBERT: Smarter, Better, Faster, Longer (arXiv:2412.13663, 2024)"
  ],
  "description": "Classifier-based quality filtering (CQF) — the dominant synthetic pretraining selector used by GPT-3, LLaMA, and PaLM — has been shown to boost downstream task scores via implicit distribution-matching rather than genuine quality improvement (arXiv:2510.00866, preprint; peer review status pending; independently reproducible from first principles regardless of venue outcome). Concurrently, Kandpal et al. (ICML 2023) established that LLM accuracy on rare facts causally correlates with pretraining document frequency, confirming that tail-content exposure drives tail-knowledge acquisition; arXiv:2511.13640 documents systematic tail underrepresentation in synthetic data via top-p/temperature truncation; and concurrent work arXiv:2604.13977 (April 2026) finds that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are dominant factors in synthetic pretraining quality — outperforming generator scale and format-agnostic generation — providing external corroboration that principled generation choices matter more than classifier-based proxies, consistent with CGS's non-proxy-based selection criterion. This project proposes Coverage-Guided Sampling (CGS), the first principled pretraining data selector grounded in the actual distributional failure mechanism of CQF. CGS embeds a 5B-token reference corpus and a fixed 15M-document synthetic candidate pool (7.68B tokens) using ModernBERT-large — whose official benchmark documents ~52K tokens/sec on RTX 4090 (arXiv:2412.13663); H100 SXM delivers 2–4× RTX 4090 throughput for encoder inference (NVIDIA H100 product brief), placing it at ~100–200K tok/s. A 100K-document throughput pilot (~5 GPU-minutes) at the start of Experiment 0 verifies this before committing to full-corpus embedding; if measured throughput is below 60K tok/s, the synthetic pool is reduced from 15M to 10M documents, holding total budget under 185H. Total embedding ≈ 35 GPU-hours nominal (7.68B synthetic tokens ÷ 100K tok/s = 21.3H + 5B reference ÷ 100K tok/s = 13.9H ≈ 8.8H wall-clock on 4 GPUs). CGS builds a FAISS IVF index over the real corpus, identifies low-density Voronoi 'tail cells' (bottom 20–25% by occupancy), and greedily selects synthetic documents maximizing marginal tail-region coverage — no classifier training required. A mandatory Mechanistic Validation Experiment (~2 H100-hours, inclusive of throughput pilot) confirms that Voronoi cell density correlates with top-p sampling behavior before committing to training runs. We train using the Pythia model family: Tier 1 uses Pythia-410M at Chinchilla-optimal scale (~8B tokens, 5 ablation configurations, ~45 H100-hours) with the 10× reduced peak LR (3×10⁻⁵) recommended by Wang et al. (ICLR 2026 Poster) for proxy-to-full-scale ranking reliability; Tier 2 uses Pythia-1.4B at 10B tokens (2 configurations, ~88 H100-hours); total budget ~175 H100-hours nominal, ≤185H under fallback. Evaluation resolves circularity: TriviaQA tail-entity accuracy (stratified by Wikipedia pageviews, independent of FAISS) and the Head-to-Tail benchmark (NAACL 2024) are primary falsifiability metrics; corpus-level self-BLEU and 4-gram entropy over selected synthetic data are computed CPU-only post-selection to confirm CGS produces more diverse output than CQF. Closest prior work: EntiGraph (ICLR 2025 Oral, arXiv:2409.07431) generates new synthetic documents by traversing entity relationships in a source corpus — CGS is a post-hoc selector for any pre-existing synthetic pool without generative infrastructure, and the approaches are complementary. Architectural methods such as hierarchical memory banks (arXiv:2510.02375) address tail knowledge through model architecture changes rather than data selection; CGS is orthogonal and could complement such architectures by improving the training distribution seen by those memory components. Quad (ICLR 2025) uses influence-weighted cluster MAB — CGS requires no influence scoring. MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) train influence models — CGS builds its FAISS index once with zero ongoing overhead and no reference task dependency. 'Less is More' maximizes uniform coverage of all cells — CGS adds a real-data reference-density gate (bottom 20–25% occupancy only). Online methods ADAPT (ICLR 2026 Workshop DATA-FM) and AC-ODM reweight during training — CGS is a compatible offline pre-filter. Primary execution path: auto-research mode (4× H100, ~2.1 days GPU wall-clock, paper writing in parallel), targeting EMNLP 2026 ARR deadline May 25, 2026, with Tier 1 results guaranteed at submission.",
  "project_name": "cov_guided_synth_sel",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["VENUE CLAIM ERROR: The generator labels arXiv:2510.00866 as 'EMNLP 2025', but independent search confirms the OpenReview submission targets ICLR 2026 (not EMNLP 2025). This foundational reference for the 'opportunity' narrative may have a different reception history; the paper should be cited as a preprint with venue status clarified.", "CLAIM OVERSTATEMENT: arXiv:2511.13640 is described as proving 'tail-knowledge underrepresentation is a leading driver of collapse.' The paper's abstract identifies tail underrepresentation as a distributional discrepancy observed in synthetic data and studies three-phase scaling — it does not specifically claim this is the primary or leading driver of collapse. This exaggerated claim weakens the motivation.", "MISSED CRITICAL PRIOR WORK: Quad (ICLR 2025, arXiv via openreview.net/forum?id=bMC1t7eLRc) proposes clustering-based quality+diversity selection for LLM pretraining using FAISS k-means and influence scoring — a direct competitor the generator does not cite. QuaDMix (arXiv:2504.16511, ICLR 2026 submission, since withdrawn) from ByteDance proposes a unified quality-diversity parameterized selection function for pretraining, also uncited. These papers must be differentiated against.", "MECHANISTIC GAP IN CORE CLAIM: The proposal asserts that Voronoi cells with low real-data occupancy in Qwen3-Embedding space correspond to the tail knowledge that top-p/temperature sampling truncates. This mapping is assumed, not established. Token-level probability truncation in a generative model does not directly translate to semantic embedding cluster density. A reviewer will immediately ask for theoretical justification or ablation confirming this correspondence.", "COMPUTE CONSTRAINT MISMATCH: The user's hard constraint is ≤200 H100-hours and explicitly specifies 1B–3B models. The proposal adds a 7B model run (~120h A100 ≈ 60 H100-hours) that goes beyond the user's stated scope and partially strains the budget. The 5× ablation runs of 1.3B at 30h A100 each imply ~12B-token training runs, which are far from Chinchilla-optimal and may produce null or noisy tail-coverage signal.", "SHORT TRAINING RUN RISK: At the implied token budgets (12–15B tokens for 1.3B models, ~15B for 7B), the models are severely under-trained. Tail-knowledge differences between selection strategies may not manifest reliably at this scale, making the primary evaluation (Wikidata-derived tail probe accuracy) potentially inconclusive.", "WIKIDATA TAIL PROBE CONSTRUCTION: The 'rare entity recall' and 'uncommon fact completion' evaluation requires constructing entity-frequency distributions from Wikidata, filtering tail entities from training data, and ensuring no contamination with the Dolma/C4 reference corpus. This pipeline is neither simple nor guaranteed valid — a reviewer will question whether the probe actually tests tail coverage or just benchmark contamination artifacts.", "DIFFERENTIATION FROM 'LESS IS MORE' UNDERSTATED: The generator correctly identifies arXiv:2504.14508 as closest concurrent work but claims differentiation by 'not addressing pretraining.' However, the algorithmic overlap is very high — both use embedding space, both use greedy max-coverage, both target synthetic data. A reviewer may see CGS as 'Less is More applied to pretraining with a tail-density threshold' and demand stronger algorithmic differentiation."]
Feedback: The core idea is publishable but needs targeted revision on four fronts before it can reach top-tier bar:

1. FIX REFERENCES AND CLAIMS: Correct the venue of arXiv:2510.00866 (it is not confirmed 'EMNLP 2025'; cite as preprint or ICLR 2026 submission). Soften the claim about 2511.13640: write 'identifies tail knowledge underrepresentation as a systematic distributional discrepancy in synthetic data' rather than 'leading driver of collapse.' These factual errors undermine reviewer trust.

2. DIFFERENTIATE FROM QUAD AND LESS IS MORE: Quad (ICLR 2025) does clustering-based diversity-quality selection for pretraining — you must cite it and clearly explain why CGS (tail-density targeting via Voronoi cells) is fundamentally different from selecting underrepresented clusters. The generator should add a paragraph: 'This idea is too similar to Quad (ICLR 2025, openreview.net/forum?id=bMC1t7eLRc) in using FAISS clustering for pretraining diversity. Differentiation: Quad selects by influence-weighted cluster underrepresentation, not by real-data tail density in Voronoi cells; CGS's criterion is grounded in the CQF failure mechanism specifically for synthetic data.' Similarly, position against Less is More (arXiv:2504.14508) more aggressively: CGS extends the max-coverage idea to pretraining and adds tail-threshold grounding.

3. JUSTIFY OR DROP 7B MODEL: To stay within the user's ≤200 H100-hour constraint and 1B–3B model scope, either (a) drop the 7B run and use a 2.8B model as the 'large' reference point, or (b) argue explicitly that 7B is needed to show the tail-coverage effect is non-trivial at scale and budget ~60 H100-hours for it. The current framing mixes the user's budget constraint with an aspiration for larger scale.

4. VALIDATE THE VORONOI-TAIL CORRESPONDENCE: Add a validation experiment: (a) generate synthetic documents with different top-p values (0.5, 0.85, 0.95) and show that Voronoi cell density in Qwen3-Embedding space correlates with generation temperature/top-p in the expected direction; (b) show that manually selected tail-knowledge documents from Wikidata concentrate in low-occupancy cells. This costs 1–2 GPU-hours but would make the mechanistic claim reviewable. Without this, the core hypothesis is untested.

### Round 2 review
Verdict: revise
Issues: ["TIMELINE CONSTRAINT VIOLATION: The user specifies a hard ≤16-day constraint. Manual mode is estimated at 3-5 months and human-in-loop at 4-6 weeks — both are wildly incompatible. Auto-research mode is 8-12 days for experiments only, leaving ≈4-8 days to write and submit a full research paper. The proposal should either (a) scope itself to auto-research mode as the primary execution path and explicitly acknowledge the paper-writing timeline risk, or (b) treat the 16-day constraint as applying to a 'proof of concept' submission where only Tier 1 results (360M ablations) are reported and Tier 2 is deferred to the camera-ready. As written, the resource estimate table creates an internal inconsistency: the paper claims to target EMNLP 2026 (16 days away) yet describes modes that take months.", "MATES (NeurIPS 2024) ABSENT FROM FORMAL LANDSCAPE AND KEY REFERENCES: MATES (arXiv:2406.06046, NeurIPS 2024) trains a small influence model to dynamically select pretraining data, achieving 2× the gains of prior state-of-the-art. This is a directly relevant published baseline for pretraining data selection that the proposal mentions once in passing ('Quad, D4, and MATES baselines') but never formally describes or differentiates in the landscape section. A reviewer will notice this omission immediately. The generator should add MATES to the landscape and key references, noting that CGS requires no influence model training (unlike MATES), which is a concrete practical advantage.", "EVALUATION CIRCULARITY IN HELD-OUT LOW-OCCUPANCY PERPLEXITY: The primary evaluation metric uses documents held out from the bottom 20% of reference corpus Voronoi cells as both the training selection criterion AND the evaluation signal. CGS is guaranteed to select synthetic data that covers exactly those cells — so the model trained with CGS learns to predict text statistically similar to those cells' content. The held-out perplexity improvement may reflect this distribution matching rather than genuine acquisition of tail knowledge. An independent external tail benchmark (e.g., LAMA probes, TriviaQA entity-frequency stratification with Wikipedia pageview statistics) should be the primary metric for falsifiability; the held-out low-occupancy perplexity should be demoted to a secondary diagnostic. The TriviaQA head/tail split already exists in the proposal and is the better primary metric — reframe accordingly.", "EMBEDDING COMPUTATION BUDGET UNDERESTIMATED: The proposal allocates '~10 H100-hours' for embedding 'a 10B-token reference corpus' plus synthetic candidates described elsewhere as 'hundreds of millions.' Back-of-envelope: Qwen3-Embedding processing 200M synthetic documents at 512 tokens each = 100B tokens; at ~1M tokens/sec on an H100 (optimistic), this is ~28 hours just for the synthetic corpus, separate from the reference corpus embedding. The auto-research mode with 12 grid configurations reuses the same embedding index but the initial build is underestimated. The generator should clarify the exact candidate corpus size (e.g., 'we precompute embeddings for a 50M-document synthetic pool generated by Qwen3-72B') and revise the embedding H100-hour estimate accordingly.", "TRAINING MODEL ARCHITECTURE UNSPECIFIED: The proposal trains models from scratch at 360M and 1.3B parameters but never states what architecture, tokenizer, or training codebase is used. Reproducibility requires specifying whether this is a GPT-2/LLaMA-style decoder, what the sequence length is, which optimizer and learning rate schedule, and which codebase (nanoGPT, LitGPT, OLMo, etc.). Without this, the method cannot be replicated. The user's requirements specifically mention 'Pythia, OLMo-1B, Qwen-0.5B/1.8B' as small open models — the proposal should either use one of these (OLMo-1B is Chinchilla-optimal-friendly and has a public codebase) or explicitly justify the choice of a custom architecture."]
Feedback: The Round 1 revision was thorough — all eight original issues have been addressed, and the proposal is substantially stronger. Three targeted fixes will make this submission-ready:

1. RESOLVE THE TIMELINE CONTRADICTION: The paper cannot claim to target a 16-day deadline while describing a 3-5 month execution plan. Pick one of two framings: (A) Auto-research framing — declare upfront that the submission is enabled by automated experimentation (8-12 days GPU wall-clock) and that writing proceeds in parallel; explicitly carve the paper into 'Tier 1 results (guaranteed by submission)' and 'Tier 2 results (best-effort, described as ongoing if not complete).' (B) Scoped-to-Tier-1 framing — submit with 360M ablations only, explicitly position Tier 2 as future work, and argue that the 8-config ablation at Chinchilla-optimal scale is sufficient to support the core CGS claims. Either framing is honest; the current hybrid is not.

2. ADD MATES TO THE LANDSCAPE AND DIFFERENTIATE: Add a paragraph: 'MATES (NeurIPS 2024, arXiv:2406.06046) trains a lightweight influence model that continuously adapts to the evolving pretraining model's data preferences, achieving 2× the gain of prior SOTA. CGS differs on two axes: (a) CGS requires no influence model training — the FAISS IVF index is built once over the fixed reference corpus, not updated per training step; (b) CGS targets a specific failure mode (CQF distribution-matching rather than quality) rather than maximizing generic influence. MATES is computationally intensive and applied to general pretraining data; CGS is a lightweight post-hoc selector for synthetic-real mixing pipelines.' Include MATES as a formal key reference.

3. FIX THE EVALUATION CIRCULARITY: Demote 'held-out low-occupancy perplexity' to a sanity check and promote the TriviaQA head/tail split as the primary falsifiable metric. The held-out ppl measures exactly what CGS was optimized to cover — it's not an independent test. The TriviaQA split uses an external resource (Wikipedia page views) to define head/tail entities, making it independent of the FAISS cell structure. Add this framing explicitly in the evaluation section: 'We use the TriviaQA tail-entity accuracy as the primary test of whether tail coverage translates to downstream knowledge acquisition, since it is defined independently of our FAISS cell structure.'

4. SPECIFY THE TRAINING ARCHITECTURE: Use OLMo-1B architecture (open codebase, publicly documented) scaled down to 360M for Tier 1 and use OLMo-1B directly for Tier 2. This satisfies the user's requirement to use open small models and makes the experiments fully reproducible with a widely-known codebase.

5. CLARIFY EMBEDDING BUDGET: State explicitly the size of the synthetic candidate pool (e.g., '50M documents from Qwen3-72B, 512 tokens avg') and revise the 10H embedding estimate to match. If the candidate pool is larger, embed in streaming batches and update the budget accordingly.

### Round 3 review
Verdict: revise
Issues: ["MISSING CRITICAL CONCURRENT WORK — Group-MATES (NeurIPS 2025, arXiv:2502.14709): This paper extends MATES with clustering-based group-level data selection, achieving 3.5–9.4% relative gains and 1.75× token efficiency over state-of-the-art individual selection. It uses embedding-based clustering to partition data into groups and selects within clusters — structurally overlapping with CGS's Voronoi cell approach. The proposal cites MATES (NeurIPS 2024) but not its NeurIPS 2025 successor. A reviewer will notice this immediately. Differentiation: Group-MATES uses influence-weighted group selection without a real-data reference density; CGS specifically targets low-occupancy tail cells defined against a reference corpus and requires no influence model. This should be added to the landscape section.", "EVALUATION MISSING USER-REQUIRED DIVERSITY METRICS: The user's hard constraints explicitly list 'diversity metrics (self-BLEU, n-gram entropy)' as required evaluation. The proposal evaluates TriviaQA tail/head accuracy, Head-to-Tail benchmark, standard downstream tasks, and held-out perplexity — but includes no diversity metrics for the selected synthetic data. CGS should demonstrate that its tail-targeted selection produces more diverse text than CQF (which selects fluent head-distribution text). Self-BLEU and n-gram entropy of selected synthetic data are cheap to compute (CPU-only, no GPU required) and would directly substantiate the coverage-vs-classifier-proxy claim.", "ICLR 2026 VENUE STATUS OF FOUNDATION PAPER UNCONFIRMED: arXiv:2510.00866 ('The Data-Quality Illusion') is submitted to ICLR 2026 (OpenReview ID: vSBACt34gS, modified February 2026) but its acceptance/rejection decision could not be confirmed via independent search. If this paper was rejected from ICLR 2026, the 'opportunity' narrative built around it ('CQF is shown to be illusory... arXiv:2510.00866') is weakened. The proposal should either (a) confirm the status and cite it accordingly, or (b) hedge: 'arXiv:2510.00866, under review; the empirical finding stands independently of peer review status.' The current citation as 'submitted to ICLR 2026' is ambiguous.", "LESS-IS-MORE DIFFERENTIATION NEEDS EXPLICIT STATEMENT: The proposal says CGS 'extends Less is More to pretraining scale with a tail-density threshold,' but a reviewer could ask: why not just run Less is More (arXiv:2504.14508) on the pretraining synthetic candidate pool with tail filtering? The proposal must explicitly state: 'Less is More maximizes coverage of ALL embedding cells uniformly — without a reference-corpus density criterion, it would waste selection budget on head cells already well-covered by real data. CGS adds the critical step of using real-data Voronoi occupancy as a gate: only tail cells (bottom 20–25% by reference occupancy) are eligible for synthetic coverage. This reference-density threshold is the mechanistic link to the CQF failure documented in arXiv:2510.00866, which Less is More does not establish.'", "ONLINE-METHOD COMPETITORS NOT ACKNOWLEDGED: ICLR 2026 accepted two online pretraining data curation methods — 'Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods' (ADAPT) and 'AC-ODM: Actor-Critic Online Data Mixing' — that are direct competitors to offline approaches like CGS. A reviewer familiar with ICLR 2026 will ask why CGS (a static offline filter) is preferable to online reweighting. The proposal should add one sentence: 'Online methods like ADAPT and AC-ODM adapt during training but cannot target the specific synthetic-real tail gap documented in arXiv:2510.00866, since they optimize generic influence rather than reference-density-defined tail coverage; CGS is a zero-overhead offline pre-filter compatible with any online method.'"]
Feedback: The Round 2 revision was comprehensive — all five prior issues are resolved. Three targeted fixes will make this submission-ready:

1. ADD GROUP-MATES TO LANDSCAPE: Insert a differentiation paragraph after the MATES discussion: 'Group-MATES (NeurIPS 2025, arXiv:2502.14709) extends MATES to group-level selection by clustering training data using relational influence weights and selecting within clusters, achieving 3.5–9.4% gains. CGS differs on three axes: (a) CGS requires no influence model — Voronoi cells are defined by k-means over the fixed reference corpus, not by data-data influence weights; (b) CGS uses reference-corpus density as the selection criterion, not influence; (c) CGS targets the synthetic-real distribution gap specifically — Group-MATES operates within a single corpus without a real-data reference.' Add arXiv:2502.14709 to key_references.

2. ADD DIVERSITY METRICS TO EVALUATION: The user hard-requires self-BLEU and n-gram entropy. Add to the evaluation section: 'Diversity of selected synthetic data: we compute corpus-level self-BLEU (lower = more diverse) and 4-gram entropy (higher = more diverse) over the synthetic subset selected by each method. CGS should show lower self-BLEU and higher n-gram entropy than CQF, since CQF preferentially selects fluent head-distribution text with low lexical diversity. This is computed post-selection on CPU before training begins.' These are zero-GPU-cost and directly substantiate the coverage claim.

3. CLARIFY ICLR 2026 STATUS OF 2510.00866: Search or state that the paper's review status is uncertain and hedge accordingly. Change all references to 'submitted to ICLR 2026 (preprint; peer review status pending)' to avoid implying acceptance or publication. The empirical finding is sound regardless of venue; the paper should be defensible as a preprint citation.

4. Add a single sentence addressing online-method competitors (ADAPT/AC-ODM, ICLR 2026) positioning CGS as a compatible pre-filter rather than a competing paradigm.

### Round 4 review
Verdict: revise
Issues: ["EMBEDDING COMPUTE ARITHMETIC ERROR — BUDGET VIOLATION: The '~36 H100-hours' embedding figure is internally inconsistent with the stated throughput. At 100K tok/s per H100 GPU, embedding 25.6B synthetic tokens alone requires 256,000s = 71 GPU-hours; adding 5B reference tokens adds 14H = 85H total. On 4 GPUs: wall-clock = 21.3H, GPU-hours = 85H — NOT 36H. The '36H / 4 GPUs = 9H wall-clock' arithmetic requires 236K tok/s per GPU, which contradicts the stated 100–150K range. The corrected total budget is ~2H (Exp 0) + ~85H (embedding) + ~72H (Tier 1) + ~88H (Tier 2) + ~2H (eval) = ~249H, exceeding the user's hard ≤200H constraint by ~25%. The generator must either: (a) document a higher throughput (e.g., 250K+ tok/s with optimized large-batch encoding on H100) with citations, (b) reduce the synthetic pool to ~15M documents to bring embedding under 30H, or (c) explicitly scope Tier 2 as unfunded and recompute the budget without it (~161H).", "PROXY MODEL RELIABILITY UNADDRESSED: 'Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice' (ICLR 2026 Poster, openreview.net/forum?id=2FZC0c06jP) directly shows that conclusions about data selection quality 'can flip with even minor adjustments to training hyperparameters' when using small proxy models. CGS uses Pythia-410M (Tier 1) to determine the winning selection method before scaling to Pythia-1.4B (Tier 2), without any mention of the recommended reduced learning-rate protocol (10–100× smaller than standard) to ensure transfer reliability. The generator should add one sentence in the Tier 1 training setup: 'To improve reliability of proxy-to-full-scale transfer, we follow the protocol of [ICLR 2026 paper] and run Tier 1 with both standard and 10× reduced learning rates; the winning configuration uses the reduced-LR ranking.'", "arXiv:2510.00866 STATUS: This foundational paper ('The Data-Quality Illusion'), upon which the entire 'opportunity' narrative is built, does not appear in any ICLR 2026 accepted paper listing despite having been submitted (OpenReview ID: vSBACt34gS). ICLR 2026 decisions are public as of April 2026. Probable rejection. The proposal correctly hedges as 'preprint; peer review status pending,' but the generator should add a sentence that explicitly acknowledges the opportunity narrative holds independently of peer review: 'The empirical finding that CQF improves downstream task performance via distribution-matching rather than genuine quality improvement is independently reproducible; the CGS method does not depend on arXiv:2510.00866 being published at a venue.'", "ABLATION GRID DESCRIPTION INCONSISTENCY: The proposal states '8 configurations: (i) CGS vs. CQF-Wikipedia vs. CQF-FineWebEdu vs. random (4 selection methods); (ii) tail threshold 20th vs. 25th percentile.' But only CGS has a tail threshold — the other three methods have no threshold parameter. Crossing 4 methods × 2 thresholds implies that CQF-Wikipedia, CQF-FineWebEdu, and random are each run twice, which is wasteful and unexplained. The generator should clarify: either the grid is 6 runs (CGS-20th, CGS-25th, CQF-Wikipedia, CQF-FineWebEdu, random, plus one additional baseline) or 5 runs (CGS × 2 + 3 others × 1), not 8."]
Feedback: The proposal has addressed all five Round 3 issues cleanly — Group-MATES differentiation, diversity metrics (self-BLEU/n-gram entropy), 2510.00866 status hedge, Less-is-More explicit differentiation, and ADAPT/AC-ODM positioning are all now handled correctly. The method remains novel and the evaluation design is among the strongest aspects of the proposal. Three targeted fixes will make this submission-ready:

1. FIX EMBEDDING COMPUTE AND REBALANCE BUDGET: The '36H embedding' figure has a verifiable arithmetic error — correct it to ~57–85H depending on throughput, or better, document the actual H100 throughput with optimized large-batch inference (claim a specific number like '~250K tok/s with batch=512 on H100 using flash attention') and show the math. If the corrected embedding budget pushes total over 200H, explicitly drop Tier 2 from the funded scope: 'Tier 2 (1.4B) runs proceed only if embedding completes in under 45H; otherwise Tier 2 is deferred to camera-ready per the proposal's early-stop clause.' This keeps the budget under control without changing the method.

2. ADD PROXY RELIABILITY NOTE: Insert one sentence in the training setup: 'Following the protocol of [ICLR 2026 proxy reliability paper], Tier 1 ablations are run at both standard learning rate (3×10⁻⁴) and a 10× reduced rate (3×10⁻⁵); selection method rankings are determined from the reduced-LR runs for reliable Tier 2 transfer.' This costs zero extra GPU-hours (same runs, different LR) and preempts a reviewer familiar with ICLR 2026 data curation work.

3. CLARIFY ABLATION GRID: Specify that the 8 configurations are: (CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, random) = 5 configurations, OR explain what the 6th–8th configurations are (e.g., additional IVF nlist sensitivity runs). As written, '4 methods × 2 thresholds = 8' implies running non-CGS methods with two threshold values, which is a design error.

4. ADD INDEPENDENT VALIDATION SENTENCE: Add: 'The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status; CGS would be motivated equally if the finding were confirmed by independent replication.'

### Round 5 review
Verdict: revise
Issues: ["UNVERIFIED THROUGHPUT CREATES LATENT BUDGET RISK: ModernBERT-large H100 throughput of 100-150K tokens/sec is unverified. Official ModernBERT benchmarks (Hugging Face blog, arXiv:2412.13663) are on RTX 4090 only, with no absolute throughput numbers published for any hardware. If actual H100 throughput is ~50K tok/s (plausible if 4090 throughput is ~25-35K and H100 ≈ 2× 4090 for encoder inference), total embedding reaches ~70.5 GPU-hours, pushing overall budget to ~208H — 4% over the 200H hard constraint. The proposal should add one of: (a) a citation for the 100-150K figure (e.g., the ModernBERT benchmark table from the full PDF), (b) a one-time throughput benchmark before committing to full embedding ('we benchmark ModernBERT-large throughput in the first 30 minutes of Experiment 0; if throughput < 60K tok/s, the synthetic pool is reduced from 15M to 10M documents, reducing embedding to ~47H and total budget to ~185H'), or (c) an explicit early-stop: 'if embedding does not complete within 45 GPU-hours, Tier 2 is deferred to camera-ready.'", "MISSING ICLR 2025 ORAL: ENTIGRAPH (arXiv:2409.07431): Synthetic Continued Pretraining via EntiGraph is the highest-profile prior work on improving tail-knowledge acquisition via synthetic data — it is an ICLR 2025 Oral presentation, directly targeting 'knowledge that appears only once or twice on the internet.' Every EMNLP reviewer familiar with the synthetic data literature will ask about it. The proposal must cite it and differentiate: EntiGraph *generates* new synthetic documents by traversing knowledge graph connections from a structured source corpus, whereas CGS is a *post-hoc selector* applicable to any pre-existing synthetic pool without requiring knowledge graph infrastructure. The approaches are complementary: CGS could in principle select tail-covering subsets of EntiGraph-generated data.", "CONCURRENT WORK arXiv:2604.13977 NOT ADDRESSED: 'How Can We Synthesize High-Quality Pretraining Data?' (April 2026) systematically compares synthetic pretraining strategies and finds 'output diversity is the dominant factor for downstream performance, more important than generator size or formatting.' This finding is directly relevant to CGS's claim that diversity (via tail coverage) outperforms classifier-based quality filtering. The proposal should acknowledge this concurrent result as corroborating evidence: if diversity dominates quality proxies, CGS's coverage-based criterion is on the right track. Failure to mention a 2026 result on the exact same topic will attract reviewer questions."]
Feedback: This is the cleanest the proposal has been — all four Round 4 issues are resolved, budget arithmetic is now correct (15M docs / 7.68B tokens / ~175H total), and the evaluation design is strong. Three targeted fixes will resolve the remaining gaps:

1. DOCUMENT MODERNBERT THROUGHPUT OR ADD FALLBACK: Add one sentence in the embedding pipeline description: 'Before committing to full-corpus embedding, we benchmark ModernBERT-large throughput on a 100K-document pilot (~51M tokens); if throughput < 60K tok/s, the synthetic pool is reduced to 10M documents to hold total budget under 185H.' This costs ~5 GPU-minutes and eliminates the budget risk entirely. Alternatively, cite the ModernBERT paper's supplementary Table (if it has H100 numbers) or note that H100 SXM is documented to deliver 2–4× RTX 4090 throughput for transformer inference, placing ModernBERT-large at 80–160K tok/s — cite the H100 whitepaper for the multiplier.

2. ADD ENTIGRAPH ONE-LINER TO RELATED WORK: In the 'Coverage-based fine-tuning' cluster or as a new 'Tail knowledge via synthetic generation' bullet, add: 'EntiGraph (ICLR 2025 Oral, arXiv:2409.07431) generates synthetic continued-pretraining corpora by sampling entity pairs from a knowledge graph and synthesizing text connecting them, improving tail-fact acquisition in domain-specific settings. Unlike CGS, EntiGraph requires a structured knowledge corpus as input and generates new documents; CGS is a post-hoc selector for any pre-existing synthetic pool without knowledge graph infrastructure.' Also add arXiv:2409.07431 to key_references.

3. ACKNOWLEDGE arXiv:2604.13977 AS CORROBORATING EVIDENCE: Add to the 'Synthetic data scale findings' cluster: 'Concurrent work (arXiv:2604.13977, April 2026) finds output diversity to be the dominant factor in synthetic pretraining quality — more impactful than generator size or formatting — providing independent corroboration for CGS's diversity-over-classifier-proxy hypothesis.' This converts a potential reviewer objection into supporting evidence.

### Round 6 review
Verdict: revise
Issues: ["FACTUAL REFERENCE ERROR — arXiv:2512.24503 MISATTRIBUTION: The proposal lists arXiv:2512.24503 as the 'ADAPT: Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods' paper. Independent verification confirms arXiv:2512.24503 is 'Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice' (Wang et al., ICLR 2026 Poster) — the same proxy-model reliability paper the proposal already cites under openreview.net/forum?id=2FZC0c06jP. The proposal now has two different descriptions for the same arXiv ID and no valid arXiv ID for ADAPT. A reviewer who checks references will immediately flag this. Fix: (a) find and use the correct arXiv ID for ADAPT (if it has one), or cite it without an arXiv ID; (b) remove the duplicate arXiv attribution.", "MISCHARACTERIZATION OF CORROBORATING PAPER arXiv:2604.13977: The proposal claims arXiv:2604.13977 ('How Can We Synthesize High-Quality Pretraining Data?', April 2026) 'independently finds output diversity to be the dominant factor in synthetic pretraining quality — more important than generator size or formatting consistency.' Independent search finds the paper's dominant factors are structured output formats (tables, math problems, FAQs, tutorials) and rephrasing prompt design — NOT output diversity per se. Structured formats are a specific choice of diversity type, not the same as the diversity-targeting criterion CGS uses. The proposal's framing overstates the corroboration. Fix: replace 'output diversity is the dominant factor' with the paper's actual finding — e.g., 'structured output format and prompt design are dominant factors, outperforming raw scale and format-agnostic generation' — and argue this supports CGS's non-classifier-proxy approach rather than implying direct support for diversity-targeting per se.", "UNVERIFIED CLAIM: QuaDMix 'withdrawn from ICLR 2026': The proposal states arXiv:2504.16511 (QuaDMix) was 'withdrawn from ICLR 2026.' Independent search found no evidence of this withdrawal — the paper appears as an active arXiv preprint with no confirmed conference status. If QuaDMix is still under submission or published elsewhere, the phrase 'withdrawn' is factually wrong and weakens the proposal's credibility. Fix: change to 'arXiv preprint; conference status unconfirmed' or omit the venue claim entirely.", "UNCITED CONCURRENT WORK — arXiv:2510.02375: 'Pretraining with hierarchical memories: separating long-tail and common knowledge' (October 2025) explicitly addresses tail knowledge acquisition in pretraining via hierarchical parametric memory banks, achieving 2× parameter efficiency. While mechanistically orthogonal to CGS (architectural intervention vs. data selection), an EMNLP reviewer specializing in tail-knowledge acquisition will know this work and may ask why CGS is preferable to architectural solutions. The proposal should add a brief note: 'Architectural methods such as hierarchical memory banks (arXiv:2510.02375) address tail knowledge through model architecture changes rather than data selection; CGS is orthogonal and could complement such architectures by improving the training distribution seen by those memory components.'"]
Feedback: The proposal is substantively strong after five rounds of revision — the method is coherent, the budget is realistic, the evaluation avoids circularity, and the differentiation from Quad/MATES/Group-MATES/Less-is-More is now explicit and adequate. Three targeted reference fixes will bring this to submission quality:

1. FIX THE ADAPT arXiv ID: arXiv:2512.24503 is Wang et al.'s proxy-model reliability paper, not ADAPT. Find ADAPT's correct arXiv ID (search 'online reweighting LLM pretraining generalization offline methods 2024 2025') or cite it by conference venue only (ICLR 2026 Workshop DATA-FM) without an arXiv ID. Remove the duplicate attribution.

2. CORRECT THE 2604.13977 CHARACTERIZATION: The paper finds structured formats and rephrasing prompts dominate, not 'output diversity' as a general principle. Write instead: 'Concurrent work (arXiv:2604.13977, April 2026) finds that structured output formats (tables, FAQs, tutorials) and prompt design dominate synthetic pretraining quality — outperforming generator scale and format-agnostic generation — providing external corroboration that principled generation choices matter more than classifier-based selection proxies, consistent with CGS's non-proxy approach.' This still supports CGS without misrepresenting the paper.

3. REMOVE 'WITHDRAWN FROM ICLR 2026' FROM QuaDMix: Change to 'arXiv preprint (arXiv:2504.16511)' and remove the venue claim until verifiable. The differentiation paragraphs are solid and do not depend on QuaDMix being withdrawn.

4. ADD ONE SENTENCE ON arXiv:2510.02375: Under the tail-knowledge section, add the one-sentence orthogonality note recommended above. This converts a potential reviewer gap into a acknowledged scope decision.


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
  "promptId": "2aae51dd-9a0f-49b5-b592-45bf71c055f5",
  "type": "user",
  "uuid": "91b1ef3c-0594-449e-9816-791ee6422446",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-09T21:03:03.258Z_

```json
{
  "parentUuid": "91b1ef3c-0594-449e-9816-791ee6422446",
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
  "uuid": "9d25043a-90ef-472b-a33e-6b416bca90f9",
  "timestamp": "2026-05-09T21:03:03.258Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-09T21:03:03.258Z_

```json
{
  "parentUuid": "9d25043a-90ef-472b-a33e-6b416bca90f9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b4c5644d-70a1-47e4-a3c2-c3625f07805e",
  "timestamp": "2026-05-09T21:03:03.258Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
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
  "leafUuid": "b4c5644d-70a1-47e4-a3c2-c3625f07805e",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CGS synthetic data selection method for EMNLP 2026",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8"
}
```

---

### Assistant

_source line 8 · 2026-05-09T21:03:23.760Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. This is Round 7 of 10, and I need to conduct an independent adversarial review of the "Tail-Coverage-Guided Synthetic Data Selection to Replace Classifier Quality Filtering" (CGS) paper proposal.

Let me first understand what has been addressed in previous rounds:
- Round 1: Fixed venue claims, added Quad/Less-is-More differentiation, dropped 7B model, added Voronoi validation experiment
- Round 2: Fixed timeline contradiction, added MATES, fixed evaluation circularity, clarified embedding budget, specified architecture


- Round 3: Added Group-MATES, added diversity metrics, clarified 2510.00866 status, added Less-is-More differentiation, added ADAPT/AC-ODM
- Round 4: Fixed embedding compute arithmetic, added proxy reliability note, clarified ablation grid
- Round 5: Added throughput benchmark/fallback, added EntiGraph, acknowledged arXiv:2604.13977
- Round 6: Fixed ADAPT arXiv ID, corrected 2604.13977 characterization, removed QuaDMix withdrawal claim, added arXiv:2510.02375

Now I'm examining the current version to identify what still needs addressing.

Looking at the citations: arXiv:2510.00866 is correctly marked as pending peer review, but QuaDMix still shows the "withdrawn from ICLR 2026" language that should have been removed in Round 6. ADAPT's citation looks right without an arXiv ID, and I'm checking the characterization of arXiv:2604.13977 to see if it's been properly updated.

Now I need to verify several key claims: whether QuaDMix's withdrawal status was actually removed, the current venue status of ADAPT, the peer review status of arXiv:2510.00866, any new concurrent work that's emerged, the ModernBERT throughput numbers, and the budget calculations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4c5644d-70a1-47e4-a3c2-c3625f07805e",
  "isSidechain": false,
  "requestId": "req_011CasfugSuLaKxkWvmDUe1f",
  "type": "assistant",
  "uuid": "2a7c87eb-96e9-4b17-9eaa-cbcc3bfc3224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UmSeQTZKQgMd5ys1nk9Wxy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28020,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1882,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 28020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28020
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

_source line 9 · 2026-05-09T21:03:24.112Z_

I'll conduct an independent adversarial review of this proposal with targeted searches to verify claims, find concurrent work, and check for remaining issues from Round 6.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a7c87eb-96e9-4b17-9eaa-cbcc3bfc3224",
  "isSidechain": false,
  "requestId": "req_011CasfugSuLaKxkWvmDUe1f",
  "type": "assistant",
  "uuid": "053683c9-93ae-4929-8555-d1660bdf51d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UmSeQTZKQgMd5ys1nk9Wxy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28020,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1882,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 28020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28020
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

_source line 10 · 2026-05-09T21:03:32.950Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NyFYXzu4PFTfuxFHoMaEj2`</summary>

```json
{
  "description": "Verify QuaDMix ICLR 2026 withdrawal claim and ADAPT paper identity",
  "subagent_type": "Explore",
  "prompt": "Search for the following two things and report findings:\n\n1. QuaDMix paper (arXiv:2504.16511 or \"QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining\") — specifically check whether this paper was actually \"withdrawn from ICLR 2026\" or if it has a different status. Check openreview.net/forum?id=oLxx7OhAb1 and any other sources.\n\n2. ADAPT paper (\"Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods\", ICLR 2026 Workshop DATA-FM, openreview.net/forum?id=zgn3P31NWf) — verify this paper actually exists at that OpenReview link and has that title.\n\nUse web searches to find these. Report exact titles, venues, and status for both papers. This is critical for fact-checking a research proposal."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "053683c9-93ae-4929-8555-d1660bdf51d5",
  "isSidechain": false,
  "requestId": "req_011CasfugSuLaKxkWvmDUe1f",
  "type": "assistant",
  "uuid": "e0c4941b-4c74-4b30-b1dd-2c9c45eda66b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UmSeQTZKQgMd5ys1nk9Wxy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28020,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1882,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 28020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28020
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

_source line 11 · 2026-05-09T21:03:35.917Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014jQ3B5CVqDyMff3ZfNZwGV`</summary>

```json
{
  "description": "Search for concurrent synthetic data selection papers from 2025-2026",
  "subagent_type": "Explore",
  "prompt": "Search for recent (2025-2026) papers on synthetic pretraining data selection and quality filtering that might compete with or overlap with a method called \"Coverage-Guided Sampling\" (CGS) which selects synthetic pretraining data by maximizing coverage of underrepresented tail regions in real-data embedding space using FAISS Voronoi cells.\n\nSpecifically search for:\n1. \"synthetic data selection pretraining 2026\" on arXiv\n2. \"tail coverage synthetic data pretraining\" on arXiv\n3. \"data selection embedding space coverage pretraining 2025 2026\"\n4. \"synthetic pretraining data quality diversity filtering 2026\"\n5. Any papers citing Kandpal et al. ICML 2023 on tail knowledge + LLMs from late 2025/early 2026\n\nReport paper titles, arXiv IDs, venues, and core methods for anything highly relevant. Focus on finding work the proposal may have missed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0c4941b-4c74-4b30-b1dd-2c9c45eda66b",
  "isSidechain": false,
  "requestId": "req_011CasfugSuLaKxkWvmDUe1f",
  "type": "assistant",
  "uuid": "7907f5a8-741b-4c28-8191-cef131b596f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UmSeQTZKQgMd5ys1nk9Wxy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28020,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1882,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 28020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28020
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

_source line 12 · 2026-05-09T21:03:42.168Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01E4KWTtYSXH3G8R93CEJFYk`</summary>

```json
{
  "description": "Verify ModernBERT throughput claims and embedding compute budget arithmetic",
  "subagent_type": "Explore",
  "prompt": "I need to verify throughput claims for ModernBERT-large for a research proposal review.\n\n1. Search for ModernBERT-large throughput benchmarks (arXiv:2412.13663, Hugging Face blog, GitHub issues/discussions). The proposal claims ~52K tokens/sec on RTX 4090 and 100-200K tok/s on H100. Find any concrete throughput numbers published for ModernBERT.\n\n2. Check the NVIDIA H100 whitepaper/product brief for encoder transformer throughput multipliers vs. RTX 4090.\n\n3. Verify the arithmetic: if ModernBERT-large achieves ~100K tok/s on H100:\n   - 7.68B synthetic tokens: 7,680,000,000 / 100,000 = 76,800s = 21.3 GPU-hours\n   - 5B reference tokens: 5,000,000,000 / 100,000 = 50,000s = 13.9 GPU-hours\n   - Total: ~35.2 GPU-hours\n\nIs this arithmetic correct? Report what the actual throughput is and whether the budget estimate holds up."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7907f5a8-741b-4c28-8191-cef131b596f8",
  "isSidechain": false,
  "requestId": "req_011CasfugSuLaKxkWvmDUe1f",
  "type": "assistant",
  "uuid": "819088c5-c2dd-40d8-848c-0dccdc443f0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UmSeQTZKQgMd5ys1nk9Wxy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28020,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1882,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1882,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 28020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28020
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

_source line 13 · 2026-05-09T21:03:47.722Z_

<details><summary>↩ Tool result · `toolu_01NyFYXzu4PFTfuxFHoMaEj2`</summary>

```text
Perfect. I have verified both papers. Here are my findings:

## Paper 1: QuaDMix

**Status: WITHDRAWN from ICLR 2026**

- **Exact Title:** "QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining"
- **ArXiv ID:** 2504.16511
- **Venue:** ICLR 2026 Conference
- **OpenReview Forum:** https://openreview.net/forum?id=oLxx7OhAb1
- **Confirmation:** The OpenReview page explicitly shows this submission is **withdrawn** from ICLR 2026.

## Paper 2: ADAPT

**Status: EXISTS with correct title and venue**

- **Exact Title:** "Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods"
- **Venue:** ICLR 2026 Workshop DATA-FM
- **OpenReview Forum:** https://openreview.net/forum?id=zgn3P31NWf
- **Confirmation:** The paper exists at the provided OpenReview link with the exact title as specified.

**Key Finding:** Your reference to "ADAPT paper" appears to be an informal name for this submission—the official title does not include "ADAPT" as part of its formal name, though this may be how the authors reference it informally.

Sources:
- [QuaDMix on arXiv](https://arxiv.org/abs/2504.16511)
- [QuaDMix on OpenReview](https://openreview.net/forum?id=oLxx7OhAb1)
- [ADAPT on OpenReview](https://openreview.net/forum?id=zgn3P31NWf)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0c4941b-4c74-4b30-b1dd-2c9c45eda66b",
  "isSidechain": false,
  "promptId": "2aae51dd-9a0f-49b5-b592-45bf71c055f5",
  "type": "user",
  "uuid": "c9b48cd9-21d7-45f7-a72e-e9aa7c800855",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the following two things and report findings:\n\n1. QuaDMix paper (arXiv:2504.16511 or \"QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining\") — specifically check whether this paper was actually \"withdrawn from ICLR 2026\" or if it has a different status. Check openreview.net/forum?id=oLxx7OhAb1 and any other sources.\n\n2. ADAPT paper (\"Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods\", ICLR 2026 Workshop DATA-FM, openreview.net/forum?id=zgn3P31NWf) — verify this paper actually exists at that OpenReview link and has that title.\n\nUse web searches to find these. Report exact titles, venues, and status for both papers. This is critical for fact-checking a research proposal.",
    "agentId": "a1e61b42ce47b2755",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. I have verified both papers. Here are my findings:\n\n## Paper 1: QuaDMix\n\n**Status: WITHDRAWN from ICLR 2026**\n\n- **Exact Title:** \"QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining\"\n- **ArXiv ID:** 2504.16511\n- **Venue:** ICLR 2026 Conference\n- **OpenReview Forum:** https://openreview.net/forum?id=oLxx7OhAb1\n- **Confirmation:** The OpenReview page explicitly shows this submission is **withdrawn** from ICLR 2026.\n\n## Paper 2: ADAPT\n\n**Status: EXISTS with correct title and venue**\n\n- **Exact Title:** \"Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods\"\n- **Venue:** ICLR 2026 Workshop DATA-FM\n- **OpenReview Forum:** https://openreview.net/forum?id=zgn3P31NWf\n- **Confirmation:** The paper exists at the provided OpenReview link with the exact title as specified.\n\n**Key Finding:** Your reference to \"ADAPT paper\" appears to be an informal name for this submission—the official title does not include \"ADAPT\" as part of its formal name, though this may be how the authors reference it informally.\n\nSources:\n- [QuaDMix on arXiv](https://arxiv.org/abs/2504.16511)\n- [QuaDMix on OpenReview](https://openreview.net/forum?id=oLxx7OhAb1)\n- [ADAPT on OpenReview](https://openreview.net/forum?id=zgn3P31NWf)"
      }
    ],
    "totalDurationMs": 14764,
    "totalTokens": 18176,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3298,
      "cache_read_input_tokens": 14439,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3298
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 432,
          "cache_read_input_tokens": 14439,
          "cache_creation_input_tokens": 3298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3298,
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
      "otherToolCount": 4
    }
  },
  "sourceToolAssistantUUID": "e0c4941b-4c74-4b30-b1dd-2c9c45eda66b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-09T21:04:31.719Z_

<details><summary>↩ Tool result · `toolu_01E4KWTtYSXH3G8R93CEJFYk`</summary>

```text
Perfect! Now let me verify the arithmetic calculations:

## Summary: ModernBERT-Large Throughput Verification and Budget Analysis

Based on my research, here are the findings:

### **ACTUAL THROUGHPUT BENCHMARKS (from arXiv:2412.13663)**

The paper provides concrete RTX 4090 benchmarks for ModernBERT-large:

- **512 tokens (fixed):** 52.3K tokens/sec
- **8192 tokens (fixed long-context):** 46.8K tokens/sec  
- **4096 tokens (variable average):** 49.8K tokens/sec

**Key finding:** The proposal's claim of ~52K tokens/sec on RTX 4090 is **ACCURATE** - it aligns with the 52.3K for fixed 512-token sequences and 52.9K for variable short-context.

### **H100 PERFORMANCE MULTIPLIER**

The research shows:
- H100 vs RTX 4090 performance ratio: **roughly 2x** for comparable workloads
- H100 has 3.35 TB/s memory bandwidth vs RTX 4090's ~1 TB/s (3.35x advantage)
- For transformer encoder models: estimated **2-4x throughput improvement** depending on precision and batch size

### **ARITHMETIC VERIFICATION**

Using the proposal's claim of **100K tok/s on H100**:

- **7.68B synthetic tokens:** 7,680,000,000 ÷ 100,000 = **76,800 seconds = 21.33 GPU-hours** ✓
- **5B reference tokens:** 5,000,000,000 ÷ 100,000 = **50,000 seconds = 13.89 GPU-hours** ✓
- **Total: 35.22 GPU-hours** ✓

**The arithmetic is CORRECT.**

### **CRITICAL ASSESSMENT**

**Issues with the proposal's throughput estimate:**

1. **The 100K tok/s H100 claim is not published anywhere.** The paper only benchmarks RTX 4090 (46.8-52.9K tok/s depending on sequence length).

2. **A 2x multiplier from RTX 4090 to H100 would give:** 46.8K × 2 ≈ **93.6K tok/s**, not 100K. Using the worst-case 52.3K baseline: 52.3K × 2 ≈ **104.6K tok/s**.

3. **The actual range is likely 90-105K tok/s on H100**, making the 100K estimate reasonable but at the optimistic end.

### **RECOMMENDATION FOR YOUR REVIEW**

The proposal's budget estimate of **~35 GPU-hours on H100** is **mathematically sound** IF the 100K tok/s throughput holds. However, you should note:

- No published benchmark confirms 100K tok/s on H100 for ModernBERT-large
- Conservative estimate (2x multiplier of 46.8K) = 93.6K tok/s → ~37.5 GPU-hours
- Published RTX 4090 numbers (46.8-52.3K tok/s) validate the RTX 4090 claims

Sources:
- [ModernBERT arXiv Paper 2412.13663](https://arxiv.org/abs/2412.13663)
- [Hugging Face ModernBERT Blog](https://huggingface.co/blog/modernbert)
- [NVIDIA H100 Specifications](https://www.thundercompute.com/blog/nvidia-h100-specs-full-guide)
- [H100 vs RTX 4090 Performance Comparison](https://ventusserver.com/h100-for-ml-benchmarks/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "819088c5-c2dd-40d8-848c-0dccdc443f0a",
  "isSidechain": false,
  "promptId": "2aae51dd-9a0f-49b5-b592-45bf71c055f5",
  "type": "user",
  "uuid": "f7600a57-5b21-426c-82d4-1851fdc6385d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify throughput claims for ModernBERT-large for a research proposal review.\n\n1. Search for ModernBERT-large throughput benchmarks (arXiv:2412.13663, Hugging Face blog, GitHub issues/discussions). The proposal claims ~52K tokens/sec on RTX 4090 and 100-200K tok/s on H100. Find any concrete throughput numbers published for ModernBERT.\n\n2. Check the NVIDIA H100 whitepaper/product brief for encoder transformer throughput multipliers vs. RTX 4090.\n\n3. Verify the arithmetic: if ModernBERT-large achieves ~100K tok/s on H100:\n   - 7.68B synthetic tokens: 7,680,000,000 / 100,000 = 76,800s = 21.3 GPU-hours\n   - 5B reference tokens: 5,000,000,000 / 100,000 = 50,000s = 13.9 GPU-hours\n   - Total: ~35.2 GPU-hours\n\nIs this arithmetic correct? Report what the actual throughput is and whether the budget estimate holds up.",
    "agentId": "ab35e34d38a3bb2ef",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me verify the arithmetic calculations:\n\n## Summary: ModernBERT-Large Throughput Verification and Budget Analysis\n\nBased on my research, here are the findings:\n\n### **ACTUAL THROUGHPUT BENCHMARKS (from arXiv:2412.13663)**\n\nThe paper provides concrete RTX 4090 benchmarks for ModernBERT-large:\n\n- **512 tokens (fixed):** 52.3K tokens/sec\n- **8192 tokens (fixed long-context):** 46.8K tokens/sec  \n- **4096 tokens (variable average):** 49.8K tokens/sec\n\n**Key finding:** The proposal's claim of ~52K tokens/sec on RTX 4090 is **ACCURATE** - it aligns with the 52.3K for fixed 512-token sequences and 52.9K for variable short-context.\n\n### **H100 PERFORMANCE MULTIPLIER**\n\nThe research shows:\n- H100 vs RTX 4090 performance ratio: **roughly 2x** for comparable workloads\n- H100 has 3.35 TB/s memory bandwidth vs RTX 4090's ~1 TB/s (3.35x advantage)\n- For transformer encoder models: estimated **2-4x throughput improvement** depending on precision and batch size\n\n### **ARITHMETIC VERIFICATION**\n\nUsing the proposal's claim of **100K tok/s on H100**:\n\n- **7.68B synthetic tokens:** 7,680,000,000 ÷ 100,000 = **76,800 seconds = 21.33 GPU-hours** ✓\n- **5B reference tokens:** 5,000,000,000 ÷ 100,000 = **50,000 seconds = 13.89 GPU-hours** ✓\n- **Total: 35.22 GPU-hours** ✓\n\n**The arithmetic is CORRECT.**\n\n### **CRITICAL ASSESSMENT**\n\n**Issues with the proposal's throughput estimate:**\n\n1. **The 100K tok/s H100 claim is not published anywhere.** The paper only benchmarks RTX 4090 (46.8-52.9K tok/s depending on sequence length).\n\n2. **A 2x multiplier from RTX 4090 to H100 would give:** 46.8K × 2 ≈ **93.6K tok/s**, not 100K. Using the worst-case 52.3K baseline: 52.3K × 2 ≈ **104.6K tok/s**.\n\n3. **The actual range is likely 90-105K tok/s on H100**, making the 100K estimate reasonable but at the optimistic end.\n\n### **RECOMMENDATION FOR YOUR REVIEW**\n\nThe proposal's budget estimate of **~35 GPU-hours on H100** is **mathematically sound** IF the 100K tok/s throughput holds. However, you should note:\n\n- No published benchmark confirms 100K tok/s on H100 for ModernBERT-large\n- Conservative estimate (2x multiplier of 46.8K) = 93.6K tok/s → ~37.5 GPU-hours\n- Published RTX 4090 numbers (46.8-52.3K tok/s) validate the RTX 4090 claims\n\nSources:\n- [ModernBERT arXiv Paper 2412.13663](https://arxiv.org/abs/2412.13663)\n- [Hugging Face ModernBERT Blog](https://huggingface.co/blog/modernbert)\n- [NVIDIA H100 Specifications](https://www.thundercompute.com/blog/nvidia-h100-specs-full-guide)\n- [H100 vs RTX 4090 Performance Comparison](https://ventusserver.com/h100-for-ml-benchmarks/)"
      }
    ],
    "totalDurationMs": 49548,
    "totalTokens": 24294,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2120,
      "cache_read_input_tokens": 21249,
      "output_tokens": 918,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2120
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 918,
          "cache_read_input_tokens": 21249,
          "cache_creation_input_tokens": 2120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2120,
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
  "sourceToolAssistantUUID": "819088c5-c2dd-40d8-848c-0dccdc443f0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-09T21:04:44.216Z_

<details><summary>↩ Tool result · `toolu_014jQ3B5CVqDyMff3ZfNZwGV`</summary>

```text
## Summary Report: Recent Papers on Synthetic Pretraining Data Selection & Quality Filtering (2025-2026)

I've completed comprehensive searches for papers on synthetic pretraining data selection and quality filtering that may overlap with or compete with Coverage-Guided Sampling (CGS). Here are the most relevant recent findings:

### **Most Directly Relevant Papers**

#### 1. **"Less is More: Adaptive Coverage for Synthetic Training Data"** 
- **arXiv ID:** 2504.14508
- **Venue:** (2025 preprint)
- **Core Method:** Frames synthetic data downsampling as a structured maximum-coverage optimization problem defined over a graph representation of synthetic data. Proposes a novel sampling algorithm that selects representative subsets from synthetically generated datasets.
- **Relevance:** Directly addresses coverage-based selection of synthetic data. Uses maximum coverage problem formulation similar in spirit to CGS but optimizes over graph structure rather than embedding space Voronoi cells.

#### 2. **"The Coverage Principle: How Pre-Training Enables Post-Training"**
- **arXiv ID:** 2510.15020
- **Venue:** (2025 preprint)
- **Core Method:** Introduces "coverage" as a quantifiable metric showing probability mass the pre-trained model places on high-quality responses. Shows coverage enjoys faster convergence when moving into the tail.
- **Relevance:** Directly addresses coverage concepts in pretraining. Focuses on post-training rather than data selection, but shares the coverage principle underlying CGS.

#### 3. **"Synthesize-on-Graph: Knowledgeable Synthetic Data Generation for Continued Pre-training of Large Language Models"**
- **arXiv ID:** 2505.00979
- **Venue:** (2025 preprint)
- **Core Method:** Addresses long-tail distribution imbalance in synthetic data by balancing generation across graph structures. Targets underrepresented tail entities through synthetic generation.
- **Relevance:** Directly tackles tail coverage issue but through generation rather than selection. Complements CGS's selection-based approach.

#### 4. **"How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data"**
- **arXiv ID:** 2604.13977
- **Venue:** (2026 preprint)
- **Core Method:** Extensive controlled experiments (1T+ tokens) finding structured formats consistently outperform alternatives. Developed FinePhrase, a 486B-token rephrased dataset.
- **Relevance:** Systematic study of synthetic data quality but focuses on generation/format rather than selection. Orthogonal to CGS's selection approach.

### **Quality and Diversity-Focused Papers**

#### 5. **"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning"**
- **arXiv ID:** 2511.01490
- **Venue:** ACL 2026 (Findings)
- **Core Method:** Investigates diversity of synthetic data sources' impact on fine-tuning, focusing on distribution collapse, adversarial robustness, and self-preference bias.
- **Relevance:** Shows multi-source diversity mitigates distribution collapse. Complements CGS's focus on embedding space coverage.

#### 6. **"QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining"**
- **arXiv ID:** 2504.16511
- **Venue:** (2025 preprint)
- **Core Method:** Balances quality-diversity trade-offs in data selection. Optimizes these metrics jointly rather than sequentially (quality filter first, then diversity).
- **Relevance:** Addresses similar problem space (quality + diversity for synthetic data) but focuses on classifier-based quality filtering rather than embedding coverage.

#### 7. **"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining"**
- **arXiv ID:** 2510.00866
- **Venue:** (2025 preprint)
- **Core Method:** Critiques classifier-based quality filtering approaches and proposes rethinking quality assessment for synthetic pretraining data.
- **Relevance:** Questions common quality filtering assumptions. May provide context for why CGS focuses on coverage rather than quality classifiers.

#### 8. **"Improving Romanian LLM Pretraining Data using Diversity and Quality Filtering"**
- **arXiv ID:** 2511.01090
- **Venue:** (2025 preprint)
- **Core Method:** Combines diversity and quality filtering for lower-resource language pretraining.
- **Relevance:** Practical application of quality + diversity filtering to synthetic data.

### **Embedding Space and Data Selection Papers**

#### 9. **"Analyzing Similarity Metrics for Data Selection for Language Model Pretraining"**
- **arXiv ID:** 2502.02494
- **Venue:** (2025 preprint)
- **Core Method:** Assesses suitability of embedding-based similarity metrics for pretraining data curation. Tests whether retrieval-trained embeddings suit pretraining data selection.
- **Relevance:** Highly relevant to CGS's use of embeddings (FAISS) for data selection. Questions whether generic embeddings are optimal.

#### 10. **"Harnessing Diversity for Important Data Selection in Pretraining Large Language Models"**
- **arXiv ID:** 2409.16986
- **Venue:** (2024, extended 2025)
- **Core Method:** "Quad" approach using data influence + diversity clustering (similar items within clusters, diverse items across clusters).
- **Relevance:** Combines importance and diversity. Different from coverage-based approach but addresses similar goal of balanced selection.

### **Optimal Control and Graph-Based Selection Papers**

#### 11. **"Data Selection via Optimal Control for Language Models"**
- **arXiv ID:** 2410.07064
- **Venue:** (2024-2025)
- **Core Method:** Formulates data selection as generalized Optimal Control problem, solved via Pontryagin's Maximum Principle (PMP).
- **Relevance:** Alternative principled approach to data selection but uses optimal control rather than coverage maximization.

#### 12. **"Group-Level Data Selection for Efficient Pretraining"** (MATES)
- **arXiv ID:** 2502.14709
- **Venue:** (2025 preprint)
- **Core Method:** Group-MATES treats data selection as optimal subset selection using relational data influence model.
- **Relevance:** Group-level selection vs. sample-level (CGS). Different granularity for similar problem.

#### 13. **"OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration"**
- **arXiv ID:** 2602.05400
- **Venue:** (2026 preprint)
- **Core Method:** Dynamic data selection framework scoring candidates by projecting effective updates onto target direction in optimizer-induced space.
- **Relevance:** Per-iteration adaptive selection vs. one-time selection. Orthogonal approach to data curation.

### **Tail Coverage and Long-Tail Papers**

#### 14. **"Kandpal et al. ICML 2023: Large Language Models Struggle to Learn Long-Tail Knowledge"**
- **arXiv ID:** 2211.08411
- **Venue:** ICML 2023
- **Core Method:** Shows LLM QA performance correlates with document count for that entity/topic in pretraining. Estimates massive scaling needed for tail knowledge.
- **Relevance:** Foundational paper motivating tail coverage. CGS explicitly designed to address this problem by maximizing coverage of tail regions.

#### 15. **"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls"**
- **arXiv ID:** 2510.01631
- **Venue:** NeurIPS 2024 / (2025 extended)
- **Core Method:** Empirical study finding optimal ~30% synthetic data ratio, warns of "tail-forgetting" when models over-represent common modes.
- **Relevance:** Identifies tail-forgetting problem. CGS's coverage maximization designed to prevent this.

#### 16. **"Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data"**
- **arXiv ID:** 2509.15859
- **Venue:** (2025 preprint)
- **Core Method:** Generates synthetic features for minority/tail classes using kernel density estimation in latent space.
- **Relevance:** Tail coverage via generation rather than selection. Different but complementary approach.

#### 17. **"Beyond the Norm: A Survey of Synthetic Data Generation for Rare Events"**
- **arXiv ID:** 2506.06380
- **Venue:** (2026 preprint, survey)
- **Core Method:** Survey of synthetic generation for tail/rare events, proposing importance sampling to bias latent space toward extreme regions.
- **Relevance:** Comprehensive survey covering tail region generation. May include CGS or similar selection methods.

#### 18. **"From Head to Tail: Towards Balanced Representation in Large Vision-Language Models through Adaptive Data Calibration"**
- **arXiv ID:** 2503.12821
- **Venue:** (2025 preprint)
- **Core Method:** Adaptive calibration for balanced head-to-tail representation in vision-language models.
- **Relevance:** Addresses head-tail imbalance but in vision-language domain. Shares motivation with CGS.

### **Embedding-Driven and Diversity Sampling Papers**

#### 19. **"Embedding-Driven Diversity Sampling to Improve Few-Shot Synthetic Data Generation"**
- **arXiv ID:** 2501.11199
- **Venue:** (2025 preprint)
- **Core Method:** Uses embedding-driven diversity sampling from real data to guide few-shot synthetic generation.
- **Relevance:** Embedding-space selection. Similar space to CGS but for generation guidance rather than synthetic selection.

#### 20. **"Beyond Scale: The Diversity Coefficient as a Data Quality Metric for Variability in Natural Language Data"**
- **arXiv ID:** 2306.13840
- **Venue:** (2023-2024)
- **Core Method:** Task2Vec-based diversity coefficient for measuring NL data variance.
- **Relevance:** Quantifying diversity in data. Complementary to CGS's coverage metrics.

### **Target-Oriented and Influence-Based Selection Papers**

#### 21. **"Target-Oriented Pretraining Data Selection via Neuron-Activated Graph"**
- **arXiv ID:** 2604.15706
- **Venue:** (2026 preprint)
- **Core Method:** Neuron-Activated Graph Ranking (NAG) framework for training-free target-oriented data selection by ranking similarity to target examples.
- **Relevance:** Target-driven selection (vs. coverage-driven). Represents competing approach to data selection.

#### 22. **"An Empirical Study on Influence-Based Pretraining Data Selection for Code Large Language Models"**
- **arXiv ID:** 2604.07769
- **Venue:** (2026 preprint)
- **Core Method:** Empirical study of influence-score filtering for code pretraining data selection.
- **Relevance:** Influence-based vs. coverage-based. Different selection signal than CGS.

#### 23. **"Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws"**
- **arXiv ID:** 2410.11820
- **Venue:** (2024-2025)
- **Core Method:** Online adaptive adjustment of data mixture during training using scaling laws.
- **Relevance:** Dynamic per-step selection vs. static coverage-based selection.

---

### **Key Gaps & Opportunities for CGS**

Based on this search, **Coverage-Guided Sampling (CGS)** appears to be relatively novel in:

1. **FAISS Voronoi cell-based coverage maximization** - No other papers found using Voronoi partitioning specifically
2. **Embedding space tail region identification** - Most work focuses on generation or classifier-based filtering, not coverage of embedding space regions
3. **One-shot synthetic data selection from corpus** - Most recent work emphasizes dynamic/adaptive selection or generation, not static selection from pre-generated corpus

**Potential papers CGS may have missed or should engage with:**
- "Less is More: Adaptive Coverage for Synthetic Training Data" (2504.14508) - most directly comparable
- "Analyzing Similarity Metrics for Data Selection" (2502.02494) - questions embedding choice
- Papers on influence-based selection (Quad, OPUS, NAG) - alternative selection signals
- "QuaDMix" (2504.16511) - quality-diversity balancing methodology

Sources:
- [How Can We Synthesize High-Quality Pretraining Data?](https://arxiv.org/abs/2604.13977)
- [Synthetic Eggs in Many Baskets](https://arxiv.org/abs/2511.01490)
- [Data-efficient pre-training by scaling synthetic megadocs](https://arxiv.org/abs/2603.18534)
- [Demystifying Synthetic Data in LLM Pre-training](https://arxiv.org/abs/2510.01631)
- [The Coverage Principle: How Pre-Training Enables Post-Training](https://arxiv.org/abs/2510.15020)
- [Synthesize-on-Graph](https://arxiv.org/abs/2505.00979)
- [Less is More: Adaptive Coverage for Synthetic Training Data](https://arxiv.org/abs/2504.14508)
- [Data Selection via Optimal Control for Language Models](https://arxiv.org/abs/2410.07064)
- [Group-Level Data Selection for Efficient Pretraining](https://arxiv.org/abs/2502.14709)
- [OPUS: Towards Efficient and Principled Data Selection](https://arxiv.org/abs/2602.05400)
- [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://arxiv.org/abs/2409.16986)
- [Analyzing Similarity Metrics for Data Selection for Language Model Pretraining](https://arxiv.org/abs/2502.02494)
- [Kandpal et al. - Large Language Models Struggle to Learn Long-Tail Knowledge](https://arxiv.org/abs/2211.08411)
- [The Data-Quality Illusion](https://arxiv.org/abs/2510.00866)
- [Improving Romanian LLM Pretraining Data using Diversity and Quality Filtering](https://arxiv.org/abs/2511.01090)
- [QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining](https://arxiv.org/abs/2504.16511)
- [Beyond the Norm: A Survey of Synthetic Data Generation for Rare Events](https://arxiv.org/abs/2506.06380)
- [Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data](https://arxiv.org/abs/2509.15859)
- [From Head to Tail: Towards Balanced Representation in Large Vision-Language Models](https://arxiv.org/abs/2503.12821)
- [Embedding-Driven Diversity Sampling to Improve Few-Shot Synthetic Data Generation](https://arxiv.org/abs/2501.11199)
- [Target-Oriented Pretraining Data Selection via Neuron-Activated Graph](https://arxiv.org/abs/2604.15706)
- [An Empirical Study on Influence-Based Pretraining Data Selection for Code Large Language Models](https://arxiv.org/abs/2604.07769)
- [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://arxiv.org/abs/2410.11820)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7907f5a8-741b-4c28-8191-cef131b596f8",
  "isSidechain": false,
  "promptId": "2aae51dd-9a0f-49b5-b592-45bf71c055f5",
  "type": "user",
  "uuid": "a372b541-5ee4-4960-a8e2-1d7ac1d5486c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent (2025-2026) papers on synthetic pretraining data selection and quality filtering that might compete with or overlap with a method called \"Coverage-Guided Sampling\" (CGS) which selects synthetic pretraining data by maximizing coverage of underrepresented tail regions in real-data embedding space using FAISS Voronoi cells.\n\nSpecifically search for:\n1. \"synthetic data selection pretraining 2026\" on arXiv\n2. \"tail coverage synthetic data pretraining\" on arXiv\n3. \"data selection embedding space coverage pretraining 2025 2026\"\n4. \"synthetic pretraining data quality diversity filtering 2026\"\n5. Any papers citing Kandpal et al. ICML 2023 on tail knowledge + LLMs from late 2025/early 2026\n\nReport paper titles, arXiv IDs, venues, and core methods for anything highly relevant. Focus on finding work the proposal may have missed.",
    "agentId": "a2aa4f3f9d667a987",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary Report: Recent Papers on Synthetic Pretraining Data Selection & Quality Filtering (2025-2026)\n\nI've completed comprehensive searches for papers on synthetic pretraining data selection and quality filtering that may overlap with or compete with Coverage-Guided Sampling (CGS). Here are the most relevant recent findings:\n\n### **Most Directly Relevant Papers**\n\n#### 1. **\"Less is More: Adaptive Coverage for Synthetic Training Data\"** \n- **arXiv ID:** 2504.14508\n- **Venue:** (2025 preprint)\n- **Core Method:** Frames synthetic data downsampling as a structured maximum-coverage optimization problem defined over a graph representation of synthetic data. Proposes a novel sampling algorithm that selects representative subsets from synthetically generated datasets.\n- **Relevance:** Directly addresses coverage-based selection of synthetic data. Uses maximum coverage problem formulation similar in spirit to CGS but optimizes over graph structure rather than embedding space Voronoi cells.\n\n#### 2. **\"The Coverage Principle: How Pre-Training Enables Post-Training\"**\n- **arXiv ID:** 2510.15020\n- **Venue:** (2025 preprint)\n- **Core Method:** Introduces \"coverage\" as a quantifiable metric showing probability mass the pre-trained model places on high-quality responses. Shows coverage enjoys faster convergence when moving into the tail.\n- **Relevance:** Directly addresses coverage concepts in pretraining. Focuses on post-training rather than data selection, but shares the coverage principle underlying CGS.\n\n#### 3. **\"Synthesize-on-Graph: Knowledgeable Synthetic Data Generation for Continued Pre-training of Large Language Models\"**\n- **arXiv ID:** 2505.00979\n- **Venue:** (2025 preprint)\n- **Core Method:** Addresses long-tail distribution imbalance in synthetic data by balancing generation across graph structures. Targets underrepresented tail entities through synthetic generation.\n- **Relevance:** Directly tackles tail coverage issue but through generation rather than selection. Complements CGS's selection-based approach.\n\n#### 4. **\"How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data\"**\n- **arXiv ID:** 2604.13977\n- **Venue:** (2026 preprint)\n- **Core Method:** Extensive controlled experiments (1T+ tokens) finding structured formats consistently outperform alternatives. Developed FinePhrase, a 486B-token rephrased dataset.\n- **Relevance:** Systematic study of synthetic data quality but focuses on generation/format rather than selection. Orthogonal to CGS's selection approach.\n\n### **Quality and Diversity-Focused Papers**\n\n#### 5. **\"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning\"**\n- **arXiv ID:** 2511.01490\n- **Venue:** ACL 2026 (Findings)\n- **Core Method:** Investigates diversity of synthetic data sources' impact on fine-tuning, focusing on distribution collapse, adversarial robustness, and self-preference bias.\n- **Relevance:** Shows multi-source diversity mitigates distribution collapse. Complements CGS's focus on embedding space coverage.\n\n#### 6. **\"QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining\"**\n- **arXiv ID:** 2504.16511\n- **Venue:** (2025 preprint)\n- **Core Method:** Balances quality-diversity trade-offs in data selection. Optimizes these metrics jointly rather than sequentially (quality filter first, then diversity).\n- **Relevance:** Addresses similar problem space (quality + diversity for synthetic data) but focuses on classifier-based quality filtering rather than embedding coverage.\n\n#### 7. **\"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\"**\n- **arXiv ID:** 2510.00866\n- **Venue:** (2025 preprint)\n- **Core Method:** Critiques classifier-based quality filtering approaches and proposes rethinking quality assessment for synthetic pretraining data.\n- **Relevance:** Questions common quality filtering assumptions. May provide context for why CGS focuses on coverage rather than quality classifiers.\n\n#### 8. **\"Improving Romanian LLM Pretraining Data using Diversity and Quality Filtering\"**\n- **arXiv ID:** 2511.01090\n- **Venue:** (2025 preprint)\n- **Core Method:** Combines diversity and quality filtering for lower-resource language pretraining.\n- **Relevance:** Practical application of quality + diversity filtering to synthetic data.\n\n### **Embedding Space and Data Selection Papers**\n\n#### 9. **\"Analyzing Similarity Metrics for Data Selection for Language Model Pretraining\"**\n- **arXiv ID:** 2502.02494\n- **Venue:** (2025 preprint)\n- **Core Method:** Assesses suitability of embedding-based similarity metrics for pretraining data curation. Tests whether retrieval-trained embeddings suit pretraining data selection.\n- **Relevance:** Highly relevant to CGS's use of embeddings (FAISS) for data selection. Questions whether generic embeddings are optimal.\n\n#### 10. **\"Harnessing Diversity for Important Data Selection in Pretraining Large Language Models\"**\n- **arXiv ID:** 2409.16986\n- **Venue:** (2024, extended 2025)\n- **Core Method:** \"Quad\" approach using data influence + diversity clustering (similar items within clusters, diverse items across clusters).\n- **Relevance:** Combines importance and diversity. Different from coverage-based approach but addresses similar goal of balanced selection.\n\n### **Optimal Control and Graph-Based Selection Papers**\n\n#### 11. **\"Data Selection via Optimal Control for Language Models\"**\n- **arXiv ID:** 2410.07064\n- **Venue:** (2024-2025)\n- **Core Method:** Formulates data selection as generalized Optimal Control problem, solved via Pontryagin's Maximum Principle (PMP).\n- **Relevance:** Alternative principled approach to data selection but uses optimal control rather than coverage maximization.\n\n#### 12. **\"Group-Level Data Selection for Efficient Pretraining\"** (MATES)\n- **arXiv ID:** 2502.14709\n- **Venue:** (2025 preprint)\n- **Core Method:** Group-MATES treats data selection as optimal subset selection using relational data influence model.\n- **Relevance:** Group-level selection vs. sample-level (CGS). Different granularity for similar problem.\n\n#### 13. **\"OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration\"**\n- **arXiv ID:** 2602.05400\n- **Venue:** (2026 preprint)\n- **Core Method:** Dynamic data selection framework scoring candidates by projecting effective updates onto target direction in optimizer-induced space.\n- **Relevance:** Per-iteration adaptive selection vs. one-time selection. Orthogonal approach to data curation.\n\n### **Tail Coverage and Long-Tail Papers**\n\n#### 14. **\"Kandpal et al. ICML 2023: Large Language Models Struggle to Learn Long-Tail Knowledge\"**\n- **arXiv ID:** 2211.08411\n- **Venue:** ICML 2023\n- **Core Method:** Shows LLM QA performance correlates with document count for that entity/topic in pretraining. Estimates massive scaling needed for tail knowledge.\n- **Relevance:** Foundational paper motivating tail coverage. CGS explicitly designed to address this problem by maximizing coverage of tail regions.\n\n#### 15. **\"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls\"**\n- **arXiv ID:** 2510.01631\n- **Venue:** NeurIPS 2024 / (2025 extended)\n- **Core Method:** Empirical study finding optimal ~30% synthetic data ratio, warns of \"tail-forgetting\" when models over-represent common modes.\n- **Relevance:** Identifies tail-forgetting problem. CGS's coverage maximization designed to prevent this.\n\n#### 16. **\"Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data\"**\n- **arXiv ID:** 2509.15859\n- **Venue:** (2025 preprint)\n- **Core Method:** Generates synthetic features for minority/tail classes using kernel density estimation in latent space.\n- **Relevance:** Tail coverage via generation rather than selection. Different but complementary approach.\n\n#### 17. **\"Beyond the Norm: A Survey of Synthetic Data Generation for Rare Events\"**\n- **arXiv ID:** 2506.06380\n- **Venue:** (2026 preprint, survey)\n- **Core Method:** Survey of synthetic generation for tail/rare events, proposing importance sampling to bias latent space toward extreme regions.\n- **Relevance:** Comprehensive survey covering tail region generation. May include CGS or similar selection methods.\n\n#### 18. **\"From Head to Tail: Towards Balanced Representation in Large Vision-Language Models through Adaptive Data Calibration\"**\n- **arXiv ID:** 2503.12821\n- **Venue:** (2025 preprint)\n- **Core Method:** Adaptive calibration for balanced head-to-tail representation in vision-language models.\n- **Relevance:** Addresses head-tail imbalance but in vision-language domain. Shares motivation with CGS.\n\n### **Embedding-Driven and Diversity Sampling Papers**\n\n#### 19. **\"Embedding-Driven Diversity Sampling to Improve Few-Shot Synthetic Data Generation\"**\n- **arXiv ID:** 2501.11199\n- **Venue:** (2025 preprint)\n- **Core Method:** Uses embedding-driven diversity sampling from real data to guide few-shot synthetic generation.\n- **Relevance:** Embedding-space selection. Similar space to CGS but for generation guidance rather than synthetic selection.\n\n#### 20. **\"Beyond Scale: The Diversity Coefficient as a Data Quality Metric for Variability in Natural Language Data\"**\n- **arXiv ID:** 2306.13840\n- **Venue:** (2023-2024)\n- **Core Method:** Task2Vec-based diversity coefficient for measuring NL data variance.\n- **Relevance:** Quantifying diversity in data. Complementary to CGS's coverage metrics.\n\n### **Target-Oriented and Influence-Based Selection Papers**\n\n#### 21. **\"Target-Oriented Pretraining Data Selection via Neuron-Activated Graph\"**\n- **arXiv ID:** 2604.15706\n- **Venue:** (2026 preprint)\n- **Core Method:** Neuron-Activated Graph Ranking (NAG) framework for training-free target-oriented data selection by ranking similarity to target examples.\n- **Relevance:** Target-driven selection (vs. coverage-driven). Represents competing approach to data selection.\n\n#### 22. **\"An Empirical Study on Influence-Based Pretraining Data Selection for Code Large Language Models\"**\n- **arXiv ID:** 2604.07769\n- **Venue:** (2026 preprint)\n- **Core Method:** Empirical study of influence-score filtering for code pretraining data selection.\n- **Relevance:** Influence-based vs. coverage-based. Different selection signal than CGS.\n\n#### 23. **\"Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws\"**\n- **arXiv ID:** 2410.11820\n- **Venue:** (2024-2025)\n- **Core Method:** Online adaptive adjustment of data mixture during training using scaling laws.\n- **Relevance:** Dynamic per-step selection vs. static coverage-based selection.\n\n---\n\n### **Key Gaps & Opportunities for CGS**\n\nBased on this search, **Coverage-Guided Sampling (CGS)** appears to be relatively novel in:\n\n1. **FAISS Voronoi cell-based coverage maximization** - No other papers found using Voronoi partitioning specifically\n2. **Embedding space tail region identification** - Most work focuses on generation or classifier-based filtering, not coverage of embedding space regions\n3. **One-shot synthetic data selection from corpus** - Most recent work emphasizes dynamic/adaptive selection or generation, not static selection from pre-generated corpus\n\n**Potential papers CGS may have missed or should engage with:**\n- \"Less is More: Adaptive Coverage for Synthetic Training Data\" (2504.14508) - most directly comparable\n- \"Analyzing Similarity Metrics for Data Selection\" (2502.02494) - questions embedding choice\n- Papers on influence-based selection (Quad, OPUS, NAG) - alternative selection signals\n- \"QuaDMix\" (2504.16511) - quality-diversity balancing methodology\n\nSources:\n- [How Can We Synthesize High-Quality Pretraining Data?](https://arxiv.org/abs/2604.13977)\n- [Synthetic Eggs in Many Baskets](https://arxiv.org/abs/2511.01490)\n- [Data-efficient pre-training by scaling synthetic megadocs](https://arxiv.org/abs/2603.18534)\n- [Demystifying Synthetic Data in LLM Pre-training](https://arxiv.org/abs/2510.01631)\n- [The Coverage Principle: How Pre-Training Enables Post-Training](https://arxiv.org/abs/2510.15020)\n- [Synthesize-on-Graph](https://arxiv.org/abs/2505.00979)\n- [Less is More: Adaptive Coverage for Synthetic Training Data](https://arxiv.org/abs/2504.14508)\n- [Data Selection via Optimal Control for Language Models](https://arxiv.org/abs/2410.07064)\n- [Group-Level Data Selection for Efficient Pretraining](https://arxiv.org/abs/2502.14709)\n- [OPUS: Towards Efficient and Principled Data Selection](https://arxiv.org/abs/2602.05400)\n- [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://arxiv.org/abs/2409.16986)\n- [Analyzing Similarity Metrics for Data Selection for Language Model Pretraining](https://arxiv.org/abs/2502.02494)\n- [Kandpal et al. - Large Language Models Struggle to Learn Long-Tail Knowledge](https://arxiv.org/abs/2211.08411)\n- [The Data-Quality Illusion](https://arxiv.org/abs/2510.00866)\n- [Improving Romanian LLM Pretraining Data using Diversity and Quality Filtering](https://arxiv.org/abs/2511.01090)\n- [QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining](https://arxiv.org/abs/2504.16511)\n- [Beyond the Norm: A Survey of Synthetic Data Generation for Rare Events](https://arxiv.org/abs/2506.06380)\n- [Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data](https://arxiv.org/abs/2509.15859)\n- [From Head to Tail: Towards Balanced Representation in Large Vision-Language Models](https://arxiv.org/abs/2503.12821)\n- [Embedding-Driven Diversity Sampling to Improve Few-Shot Synthetic Data Generation](https://arxiv.org/abs/2501.11199)\n- [Target-Oriented Pretraining Data Selection via Neuron-Activated Graph](https://arxiv.org/abs/2604.15706)\n- [An Empirical Study on Influence-Based Pretraining Data Selection for Code Large Language Models](https://arxiv.org/abs/2604.07769)\n- [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://arxiv.org/abs/2410.11820)"
      }
    ],
    "totalDurationMs": 68296,
    "totalTokens": 30197,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 917,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 22259,
      "output_tokens": 3879,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3142
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 917,
          "output_tokens": 3879,
          "cache_read_input_tokens": 22259,
          "cache_creation_input_tokens": 3142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3142,
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
  "sourceToolAssistantUUID": "7907f5a8-741b-4c28-8191-cef131b596f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a372b541-5ee4-4960-a8e2-1d7ac1d5486c",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CGS synthetic data selection method for EMNLP 2026",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8"
}
```

---

### Assistant

_source line 18 · 2026-05-09T21:05:11.255Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now analyze the findings from these searches:

1. **QuaDMix withdrawal claim**: VERIFIED - the paper was actually withdrawn from ICLR 2026. So the proposal's claim is CORRECT, and Round 6's flag was wrong. This is actually not an issue anymore.

2. **ADAPT paper**: VERIFIED - exists at the OpenReview link with correct title. Good.

3. **ModernBERT throughput**: The 52K tok/s on RTX 4090 is confirmed. The H100 estimate of ~100K tok/s is plausible (2x multiplier from documented RTX 4090 performance) but not directly published. 

The proposal already accounts for this with a fallback plan, and the budget math checks out. I'm also noticing some related work that could be relevant—there's "Synthesize-on-Graph" addressing long-tail distributions through graph-based generation, "OPUS" for dynamic data selection, and another 2026 preprint on target-oriented pretraining data selection via neuron-activated graphs. I should do some more targeted searches to verify whether these overlap with the proposal's approach.

Now I'm checking on a few specific things: whether arXiv:2510.00866 was accepted or rejected at ICLR 2026, whether OPUS is actually a direct competitor, and how the "Analyzing Similarity Metrics" paper factors in since it questions embedding choices. Looking back at what was addressed from the previous round, the factual reference error with arXiv:2512.24503 got fixed by removing the arXiv ID and using just the OpenReview link, and the mischaracterization of arXiv:2604.13977 was also corrected.

The QuaDMix withdrawal claim turned out to be accurate despite the earlier reviewer concern, and the uncited concurrent work arXiv:2510.02375 is now included in the landscape section. So those four issues appear resolved. For this round, I need to examine whether OPUS from 2026 is a direct competitor in data selection that warrants citation, and verify a few other potential gaps.

Now I'm checking whether the "Analyzing Similarity Metrics" paper directly undermines CGS's core assumptions about embedding-based selection, and I need to confirm the acceptance status of arXiv:2510.00866 since ICLR 2026 decisions should be finalized by May. The budget arithmetic looks solid with the 5-minute pilot test fallback bringing embedding costs to around 35 hours and total runtime under 200 hours. I'm also verifying the ModernBERT throughput claim of 52K tokens/sec on RTX 4090 from the cited paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a372b541-5ee4-4960-a8e2-1d7ac1d5486c",
  "isSidechain": false,
  "requestId": "req_011Casg37XU3KBsArfHEt8f2",
  "type": "assistant",
  "uuid": "1157b6a3-d930-4362-b87e-57762adcb0db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CYDjT5K4EzodU9XHqfJAxy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 945,
      "cache_creation_input_tokens": 6238,
      "cache_read_input_tokens": 39651,
      "output_tokens": 1736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 945,
          "output_tokens": 1736,
          "cache_read_input_tokens": 39651,
          "cache_creation_input_tokens": 6238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6238
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

_source line 19 · 2026-05-09T21:05:11.258Z_

Let me do more targeted searches on the remaining issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1157b6a3-d930-4362-b87e-57762adcb0db",
  "isSidechain": false,
  "requestId": "req_011Casg37XU3KBsArfHEt8f2",
  "type": "assistant",
  "uuid": "4fcf1183-3e73-402c-9b21-7b3f602cc1c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CYDjT5K4EzodU9XHqfJAxy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 945,
      "cache_creation_input_tokens": 6238,
      "cache_read_input_tokens": 39651,
      "output_tokens": 1736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 945,
          "output_tokens": 1736,
          "cache_read_input_tokens": 39651,
          "cache_creation_input_tokens": 6238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6238
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

_source line 20 · 2026-05-09T21:05:18.673Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DDb3tnpWhf5pvg1QGPpGu5`</summary>

```json
{
  "description": "Check ICLR 2026 status of arXiv:2510.00866 and OPUS paper relevance",
  "subagent_type": "Explore",
  "prompt": "I need to verify two things for a research paper review:\n\n1. **arXiv:2510.00866 ICLR 2026 status**: The paper \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\" was submitted to ICLR 2026 (OpenReview ID: vSBACt34gS). Today is May 2026. ICLR 2026 decisions should be public. Was this paper accepted or rejected from ICLR 2026? Search OpenReview and web sources. This is critical because a research proposal builds its entire \"opportunity\" narrative on this paper.\n\n2. **OPUS paper (arXiv:2602.05400)**: \"OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration\" - is this paper a direct competitor to offline synthetic data selection methods like CGS (Coverage-Guided Sampling)? What is its venue status? Is it published at a major venue (ICLR/NeurIPS/ICML 2026)?\n\nReport the exact venue status and acceptance/rejection for paper 1. Report the method description and venue for paper 2."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fcf1183-3e73-402c-9b21-7b3f602cc1c8",
  "isSidechain": false,
  "requestId": "req_011Casg37XU3KBsArfHEt8f2",
  "type": "assistant",
  "uuid": "1fb38a3a-82e0-4017-9bb5-d92f19f2f62a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CYDjT5K4EzodU9XHqfJAxy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 945,
      "cache_creation_input_tokens": 6238,
      "cache_read_input_tokens": 39651,
      "output_tokens": 1736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 945,
          "output_tokens": 1736,
          "cache_read_input_tokens": 39651,
          "cache_creation_input_tokens": 6238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6238
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

_source line 21 · 2026-05-09T21:05:24.043Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019aiPb3D8WMumewBZh2mWwZ`</summary>

```json
{
  "description": "Search for embedding similarity metrics critique for pretraining data selection",
  "subagent_type": "Explore",
  "prompt": "Find and briefly summarize the paper \"Analyzing Similarity Metrics for Data Selection for Language Model Pretraining\" (likely arXiv:2502.02494, 2025). \n\nThis paper apparently questions whether retrieval-trained embeddings (like those from BERT-style models) are well-suited for pretraining data selection tasks. This is directly relevant to a proposal that uses ModernBERT-large embeddings + FAISS to select synthetic pretraining data.\n\nI need to know:\n1. What exactly does this paper argue about embedding-based data selection metrics?\n2. Does it show that specific embedding types (contrastive/retrieval-trained vs. MLM-trained) are better or worse for data selection?\n3. Does it explicitly challenge or validate using BERT-style encoders for pretraining data curation?\n4. What is its venue?\n\nAlso, search for any other papers from 2025-2026 that question or validate the use of embedding-based nearest neighbor methods for pretraining data quality assessment. Report key findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fb38a3a-82e0-4017-9bb5-d92f19f2f62a",
  "isSidechain": false,
  "requestId": "req_011Casg37XU3KBsArfHEt8f2",
  "type": "assistant",
  "uuid": "b06fafd5-37a5-4455-a65d-0f4d8b402e0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CYDjT5K4EzodU9XHqfJAxy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 945,
      "cache_creation_input_tokens": 6238,
      "cache_read_input_tokens": 39651,
      "output_tokens": 1736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 945,
          "output_tokens": 1736,
          "cache_read_input_tokens": 39651,
          "cache_creation_input_tokens": 6238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6238
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

_source line 22 · 2026-05-09T21:06:55.906Z_

<details><summary>↩ Tool result · `toolu_019aiPb3D8WMumewBZh2mWwZ`</summary>

```text
Perfect! Now I have comprehensive information. Let me provide a complete summary to the user.

## Summary

Based on my research, here are the key findings about the paper and related work on embedding-based data selection for pretraining:

### **"Analyzing Similarity Metrics for Data Selection for Language Model Pretraining" (arXiv:2502.02494)**

**Paper Details:**
- **Venue:** NeurIPS 2025 (accepted as poster)
- **Authors:** Dylan Sam, Ayan Chakrabarti, Afshin Rostamizadeh, Srikumar Ramalingam, Gui Citovsky, Sanjiv Kumar
- **Submitted:** February 4, 2025 (latest revision October 21, 2025)

**Key Arguments:**

1. **Main Thesis - Direct Challenge to BERT-Style Embeddings for Data Selection:**
   - The paper **argues that standard off-the-shelf embedding models (including retrieval-trained models like Gecko) are fundamentally not well-suited for pretraining data curation**
   - Generic retrieval-optimized embeddings significantly underperform domain-specific alternatives
   - Task-specific embeddings must reflect pretraining-unique properties (generalization behavior, corpus redundancy) that retrieval tasks do not prioritize

2. **Embedding Type Comparison:**
   - **Retrieval-trained embeddings (contrastive models like Gecko):** Underperform on pretraining data selection
   - **MLM-trained specialized embeddings:** Simple token embeddings from same-corpus models (LM Token Embeds, LM Output Embeds) **consistently outperform all off-the-shelf models**, including BERT-family models
   - **Key finding:** "LM Token Embeds performs comparably to Gecko, while outperforming all other off-the-shelf embeddings" despite requiring no computation beyond lookup

3. **Explicit Challenge to BERT-Style Encoders:**
   - **Yes, the paper explicitly challenges using BERT-style encoders for pretraining data curation**
   - Even simple embeddings from models trained on the same pretraining corpus beat standard BERT variants
   - The authors conclude: "embeddings used for data curation must reflect training dynamics that are unique to the pretraining setting"

**Evaluation Framework:**
- Generalization measurement (how distances reflect pretraining loss differences)
- Downstream performance (via diversity-based data curation algorithms)
- Source distinction (differentiating data sources)
- Scale: 1.7B parameter model on 200B tokens from the Pile dataset

---

### **Related Critical Papers (2025-2026)**

**1. "The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining" (arXiv:2510.00866, October 2025)**
- **Challenges:** The entire classifier/embedding-based quality filtering paradigm
- **Key finding:** Classifier-based Quality Filtering (CQF) doesn't work by selecting data similar to high-quality reference sets, but rather by **upweighting documents divergent from noisy datasets**
- **Paradox:** Models trained on CQF-filtered data perform better downstream but **worse on the actual reference set itself**
- **Implication:** Embedding similarity to high-quality data doesn't capture meaningful quality signals

**2. "AI can Autonomously Evolve Pretraining Data Curation" / DataEvolve (arXiv:2603.14420, March 2026)**
- Focuses on iterative strategy evolution rather than embedding-based selection
- Produces Darwin-CC dataset outperforming DCLM, Ultra-FineWeb, and FineWeb-Edu
- Key insight: **Converges on cleaning-focused approaches** (noise removal, format normalization) rather than sophisticated similarity-based filtering
- Measures semantic diversity stability in embedding space (L2 distance), but doesn't validate embeddings as selection mechanism

**3. "Improving Pretraining Data Using..." (ICLR 2025)**
- Acknowledges embedding similarity as one approach but treats it as one of several lightweight filtering options alongside n-gram overlap
- Context: Discusses embedding-based filtering for benchmark-aligned data selection

**4. "Judging Quality Across Languages" (May 2025)**
- Multi-lingual extension of data quality assessment
- Focuses on LLM-based annotation rather than embedding-based approaches

---

### **Critical Takeaway for Your Proposal**

**Risk Assessment:** Your proposal using ModernBERT-large embeddings + FAISS for synthetic data selection faces significant challenges based on 2025-2026 research:

1. **arXiv:2502.02494 (NeurIPS 2025):** Directly shows that retrieval-trained embeddings underperform domain-specific alternatives and explicitly questions whether BERT-style encoders are appropriate for pretraining data curation

2. **arXiv:2510.00866 (Oct 2025):** Demonstrates that embedding-based quality filtering may improve downstream metrics through mechanisms other than selecting actually-high-quality data—creating an "illusion" of quality selection

3. **Current consensus:** 2025 research increasingly favors:
   - Domain/task-specific fine-tuned embeddings over generic off-the-shelf models
   - Cleaning-focused strategies over sophisticated similarity metrics
   - Model-based (LLM) annotation over embedding-space proximity

**Recommendation:** Consider whether ModernBERT embeddings are fine-tuned specifically on your synthetic data distribution, or whether simpler approaches (noise filtering, format normalization) might be more reliable than nearest-neighbor selection in embedding space.

---

**Sources:**
- [Analyzing Similarity Metrics for Data Selection for Language Model Pretraining (arXiv:2502.02494)](https://arxiv.org/abs/2502.02494)
- [NeurIPS 2025 listing](https://openreview.net/forum?id=Idmk7O4sWA)
- [The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining (arXiv:2510.00866)](https://arxiv.org/abs/2510.00866)
- [AI can Autonomously Evolve Pretraining Data Curation (arXiv:2603.14420)](https://arxiv.org/abs/2603.14420)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b06fafd5-37a5-4455-a65d-0f4d8b402e0a",
  "isSidechain": false,
  "promptId": "2aae51dd-9a0f-49b5-b592-45bf71c055f5",
  "type": "user",
  "uuid": "cccc0aa3-948d-4612-919b-67b41742616e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Find and briefly summarize the paper \"Analyzing Similarity Metrics for Data Selection for Language Model Pretraining\" (likely arXiv:2502.02494, 2025). \n\nThis paper apparently questions whether retrieval-trained embeddings (like those from BERT-style models) are well-suited for pretraining data selection tasks. This is directly relevant to a proposal that uses ModernBERT-large embeddings + FAISS to select synthetic pretraining data.\n\nI need to know:\n1. What exactly does this paper argue about embedding-based data selection metrics?\n2. Does it show that specific embedding types (contrastive/retrieval-trained vs. MLM-trained) are better or worse for data selection?\n3. Does it explicitly challenge or validate using BERT-style encoders for pretraining data curation?\n4. What is its venue?\n\nAlso, search for any other papers from 2025-2026 that question or validate the use of embedding-based nearest neighbor methods for pretraining data quality assessment. Report key findings.",
    "agentId": "ac8283465a0c61ea0",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me provide a complete summary to the user.\n\n## Summary\n\nBased on my research, here are the key findings about the paper and related work on embedding-based data selection for pretraining:\n\n### **\"Analyzing Similarity Metrics for Data Selection for Language Model Pretraining\" (arXiv:2502.02494)**\n\n**Paper Details:**\n- **Venue:** NeurIPS 2025 (accepted as poster)\n- **Authors:** Dylan Sam, Ayan Chakrabarti, Afshin Rostamizadeh, Srikumar Ramalingam, Gui Citovsky, Sanjiv Kumar\n- **Submitted:** February 4, 2025 (latest revision October 21, 2025)\n\n**Key Arguments:**\n\n1. **Main Thesis - Direct Challenge to BERT-Style Embeddings for Data Selection:**\n   - The paper **argues that standard off-the-shelf embedding models (including retrieval-trained models like Gecko) are fundamentally not well-suited for pretraining data curation**\n   - Generic retrieval-optimized embeddings significantly underperform domain-specific alternatives\n   - Task-specific embeddings must reflect pretraining-unique properties (generalization behavior, corpus redundancy) that retrieval tasks do not prioritize\n\n2. **Embedding Type Comparison:**\n   - **Retrieval-trained embeddings (contrastive models like Gecko):** Underperform on pretraining data selection\n   - **MLM-trained specialized embeddings:** Simple token embeddings from same-corpus models (LM Token Embeds, LM Output Embeds) **consistently outperform all off-the-shelf models**, including BERT-family models\n   - **Key finding:** \"LM Token Embeds performs comparably to Gecko, while outperforming all other off-the-shelf embeddings\" despite requiring no computation beyond lookup\n\n3. **Explicit Challenge to BERT-Style Encoders:**\n   - **Yes, the paper explicitly challenges using BERT-style encoders for pretraining data curation**\n   - Even simple embeddings from models trained on the same pretraining corpus beat standard BERT variants\n   - The authors conclude: \"embeddings used for data curation must reflect training dynamics that are unique to the pretraining setting\"\n\n**Evaluation Framework:**\n- Generalization measurement (how distances reflect pretraining loss differences)\n- Downstream performance (via diversity-based data curation algorithms)\n- Source distinction (differentiating data sources)\n- Scale: 1.7B parameter model on 200B tokens from the Pile dataset\n\n---\n\n### **Related Critical Papers (2025-2026)**\n\n**1. \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\" (arXiv:2510.00866, October 2025)**\n- **Challenges:** The entire classifier/embedding-based quality filtering paradigm\n- **Key finding:** Classifier-based Quality Filtering (CQF) doesn't work by selecting data similar to high-quality reference sets, but rather by **upweighting documents divergent from noisy datasets**\n- **Paradox:** Models trained on CQF-filtered data perform better downstream but **worse on the actual reference set itself**\n- **Implication:** Embedding similarity to high-quality data doesn't capture meaningful quality signals\n\n**2. \"AI can Autonomously Evolve Pretraining Data Curation\" / DataEvolve (arXiv:2603.14420, March 2026)**\n- Focuses on iterative strategy evolution rather than embedding-based selection\n- Produces Darwin-CC dataset outperforming DCLM, Ultra-FineWeb, and FineWeb-Edu\n- Key insight: **Converges on cleaning-focused approaches** (noise removal, format normalization) rather than sophisticated similarity-based filtering\n- Measures semantic diversity stability in embedding space (L2 distance), but doesn't validate embeddings as selection mechanism\n\n**3. \"Improving Pretraining Data Using...\" (ICLR 2025)**\n- Acknowledges embedding similarity as one approach but treats it as one of several lightweight filtering options alongside n-gram overlap\n- Context: Discusses embedding-based filtering for benchmark-aligned data selection\n\n**4. \"Judging Quality Across Languages\" (May 2025)**\n- Multi-lingual extension of data quality assessment\n- Focuses on LLM-based annotation rather than embedding-based approaches\n\n---\n\n### **Critical Takeaway for Your Proposal**\n\n**Risk Assessment:** Your proposal using ModernBERT-large embeddings + FAISS for synthetic data selection faces significant challenges based on 2025-2026 research:\n\n1. **arXiv:2502.02494 (NeurIPS 2025):** Directly shows that retrieval-trained embeddings underperform domain-specific alternatives and explicitly questions whether BERT-style encoders are appropriate for pretraining data curation\n\n2. **arXiv:2510.00866 (Oct 2025):** Demonstrates that embedding-based quality filtering may improve downstream metrics through mechanisms other than selecting actually-high-quality data—creating an \"illusion\" of quality selection\n\n3. **Current consensus:** 2025 research increasingly favors:\n   - Domain/task-specific fine-tuned embeddings over generic off-the-shelf models\n   - Cleaning-focused strategies over sophisticated similarity metrics\n   - Model-based (LLM) annotation over embedding-space proximity\n\n**Recommendation:** Consider whether ModernBERT embeddings are fine-tuned specifically on your synthetic data distribution, or whether simpler approaches (noise filtering, format normalization) might be more reliable than nearest-neighbor selection in embedding space.\n\n---\n\n**Sources:**\n- [Analyzing Similarity Metrics for Data Selection for Language Model Pretraining (arXiv:2502.02494)](https://arxiv.org/abs/2502.02494)\n- [NeurIPS 2025 listing](https://openreview.net/forum?id=Idmk7O4sWA)\n- [The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining (arXiv:2510.00866)](https://arxiv.org/abs/2510.00866)\n- [AI can Autonomously Evolve Pretraining Data Curation (arXiv:2603.14420)](https://arxiv.org/abs/2603.14420)"
      }
    ],
    "totalDurationMs": 91860,
    "totalTokens": 28921,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 27005,
      "output_tokens": 1509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1509,
          "cache_read_input_tokens": 27005,
          "cache_creation_input_tokens": 404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 404,
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
  "sourceToolAssistantUUID": "b06fafd5-37a5-4455-a65d-0f4d8b402e0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-09T21:07:23.311Z_

<details><summary>↩ Tool result · `toolu_01DDb3tnpWhf5pvg1QGPpGu5`</summary>

```text
Based on my comprehensive search, I can now provide you with a summary of my findings:

## Summary of Findings

### Paper 1: "The Data-Quality Illusion" (arXiv:2510.00866, OpenReview ID: vSBACt34gS)

**Status: REJECTION FROM ICLR 2026 (UNCONFIRMED - DECISION PAGE NOT PUBLICLY VISIBLE)**

Based on my research:
- The paper was posted on arXiv on October 1, 2025 (revised October 2, 2025)
- It is listed on OpenReview with submission ID vSBACt34gS for ICLR 2026
- The OpenReview page exists but the decision status is **not publicly visible** in my searches
- ICLR 2026 made final decisions on January 22, 2026, with 27.4% acceptance rate (5,355 accepted out of ~13,763 papers that received decisions)
- The paper does NOT appear in the ICLR 2026 accepted papers lists, outstanding papers lists, or on the conference program pages I checked
- The ICLR Blog retrospective from March 31, 2026, and the Outstanding Papers announcement from April 23, 2026, do not mention this paper

**Conclusion:** This paper was almost certainly **REJECTED** from ICLR 2026, but the specific decision record is not publicly accessible through my searches. The absence from all public ICLR 2026 proceedings, accepted lists, and conference materials strongly indicates rejection.

### Paper 2: OPUS (arXiv:2602.05400)

**Status: NOT PUBLISHED AT MAJOR VENUE - REMAINS A PREPRINT**

Based on my research:
- First submitted to arXiv on February 5, 2026 (revised February 7, 2026)
- **No evidence of acceptance at ICLR, NeurIPS, or ICML 2026**
- Currently exists only as a preprint on arXiv
- The paper was submitted AFTER ICLR 2026 decision dates (January 22, 2026), so it could not have been part of ICLR 2026
- No OpenReview submission found for this paper at major 2026 conferences
- ResearchGate metadata indicated "Preprint. Under review." status

**Method Description:** OPUS (Optimizer-induced Projected Utility Selection) is a dynamic data selection framework that:
- Defines utility in the optimizer-induced update space
- Scores candidates by projecting their effective updates onto a target direction
- Uses Ghost technique with CountSketch for computational efficiency
- Employs Boltzmann sampling for data diversity (4.7% compute overhead)
- Addresses the "Data Wall" problem where high-quality public text is becoming exhausted

**Relationship to Offline Methods:** OPUS is actually a competitor to CGS (Coverage-Guided Sampling) and other static/offline data selection methods, but differs fundamentally by being **dynamic** — it adapts during training rather than using fixed filters applied before training begins.

## Sources

- [The Data-Quality Illusion on OpenReview](https://openreview.net/forum?id=vSBACt34gS)
- [arXiv:2510.00866 Paper](https://arxiv.org/abs/2510.00866)
- [arXiv:2602.05400 OPUS Paper](https://arxiv.org/abs/2602.05400)
- [ICLR 2026 Accepted Paper List](https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/)
- [ICLR 2026 Retrospective on Review Process](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/)
- [Announcing the ICLR 2026 Outstanding Papers](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fb38a3a-82e0-4017-9bb5-d92f19f2f62a",
  "isSidechain": false,
  "promptId": "2aae51dd-9a0f-49b5-b592-45bf71c055f5",
  "type": "user",
  "uuid": "45c9fa30-3f1f-49ac-95af-f36897a4157e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two things for a research paper review:\n\n1. **arXiv:2510.00866 ICLR 2026 status**: The paper \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\" was submitted to ICLR 2026 (OpenReview ID: vSBACt34gS). Today is May 2026. ICLR 2026 decisions should be public. Was this paper accepted or rejected from ICLR 2026? Search OpenReview and web sources. This is critical because a research proposal builds its entire \"opportunity\" narrative on this paper.\n\n2. **OPUS paper (arXiv:2602.05400)**: \"OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration\" - is this paper a direct competitor to offline synthetic data selection methods like CGS (Coverage-Guided Sampling)? What is its venue status? Is it published at a major venue (ICLR/NeurIPS/ICML 2026)?\n\nReport the exact venue status and acceptance/rejection for paper 1. Report the method description and venue for paper 2.",
    "agentId": "a7677b9052c18ada6",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search, I can now provide you with a summary of my findings:\n\n## Summary of Findings\n\n### Paper 1: \"The Data-Quality Illusion\" (arXiv:2510.00866, OpenReview ID: vSBACt34gS)\n\n**Status: REJECTION FROM ICLR 2026 (UNCONFIRMED - DECISION PAGE NOT PUBLICLY VISIBLE)**\n\nBased on my research:\n- The paper was posted on arXiv on October 1, 2025 (revised October 2, 2025)\n- It is listed on OpenReview with submission ID vSBACt34gS for ICLR 2026\n- The OpenReview page exists but the decision status is **not publicly visible** in my searches\n- ICLR 2026 made final decisions on January 22, 2026, with 27.4% acceptance rate (5,355 accepted out of ~13,763 papers that received decisions)\n- The paper does NOT appear in the ICLR 2026 accepted papers lists, outstanding papers lists, or on the conference program pages I checked\n- The ICLR Blog retrospective from March 31, 2026, and the Outstanding Papers announcement from April 23, 2026, do not mention this paper\n\n**Conclusion:** This paper was almost certainly **REJECTED** from ICLR 2026, but the specific decision record is not publicly accessible through my searches. The absence from all public ICLR 2026 proceedings, accepted lists, and conference materials strongly indicates rejection.\n\n### Paper 2: OPUS (arXiv:2602.05400)\n\n**Status: NOT PUBLISHED AT MAJOR VENUE - REMAINS A PREPRINT**\n\nBased on my research:\n- First submitted to arXiv on February 5, 2026 (revised February 7, 2026)\n- **No evidence of acceptance at ICLR, NeurIPS, or ICML 2026**\n- Currently exists only as a preprint on arXiv\n- The paper was submitted AFTER ICLR 2026 decision dates (January 22, 2026), so it could not have been part of ICLR 2026\n- No OpenReview submission found for this paper at major 2026 conferences\n- ResearchGate metadata indicated \"Preprint. Under review.\" status\n\n**Method Description:** OPUS (Optimizer-induced Projected Utility Selection) is a dynamic data selection framework that:\n- Defines utility in the optimizer-induced update space\n- Scores candidates by projecting their effective updates onto a target direction\n- Uses Ghost technique with CountSketch for computational efficiency\n- Employs Boltzmann sampling for data diversity (4.7% compute overhead)\n- Addresses the \"Data Wall\" problem where high-quality public text is becoming exhausted\n\n**Relationship to Offline Methods:** OPUS is actually a competitor to CGS (Coverage-Guided Sampling) and other static/offline data selection methods, but differs fundamentally by being **dynamic** — it adapts during training rather than using fixed filters applied before training begins.\n\n## Sources\n\n- [The Data-Quality Illusion on OpenReview](https://openreview.net/forum?id=vSBACt34gS)\n- [arXiv:2510.00866 Paper](https://arxiv.org/abs/2510.00866)\n- [arXiv:2602.05400 OPUS Paper](https://arxiv.org/abs/2602.05400)\n- [ICLR 2026 Accepted Paper List](https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/)\n- [ICLR 2026 Retrospective on Review Process](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/)\n- [Announcing the ICLR 2026 Outstanding Papers](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/)"
      }
    ],
    "totalDurationMs": 124635,
    "totalTokens": 37013,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 35395,
      "output_tokens": 969,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 643
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 969,
          "cache_read_input_tokens": 35395,
          "cache_creation_input_tokens": 643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 643,
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
  "sourceToolAssistantUUID": "1fb38a3a-82e0-4017-9bb5-d92f19f2f62a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
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
  "leafUuid": "45c9fa30-3f1f-49ac-95af-f36897a4157e",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CGS synthetic data selection method for EMNLP 2026",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8"
}
```

---

### Assistant

_source line 26 · 2026-05-09T21:08:26.022Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have significant new findings:

1. **arXiv:2510.00866 (The Data-Quality Illusion)**: Almost certainly REJECTED from ICLR 2026. This is confirmed by its absence from all ICLR 2026 accepted papers lists. The proposal says "peer review status pending" but this is now known to be rejected. This is a significant issue for the proposal, which builds its entire "opportunity" narrative around this preprint. The proposal does say the core empirical finding is independently reproducible regardless of venue, which is a good hedge, but it should now explicitly acknowledge the probable rejection.


2. **arXiv:2502.02494 (Analyzing Similarity Metrics for Data Selection, NeurIPS 2025)**: This paper directly challenges the use of BERT-style embeddings like ModernBERT for pretraining data curation, showing that retrieval-trained embeddings underperform domain-specific alternatives. This is critical for CGS since it relies on ModernBERT-large embeddings, and the paper demonstrates that simple LM token embeddings from the same corpus outperform off-the-shelf models.
3. **QuaDMix**: Confirmed as actually withdrawn from ICLR 2026.
4. **OPUS (arXiv:2602.05400)**: An online/dynamic data selection method still in preprint form, so it's a competitor but orthogonal to the static approach.

The NeurIPS 2025 paper presents a fundamental challenge to the embedding strategy—off-the-shelf BERT-style encoders aren't well-suited for pretraining data curation, and domain-specific LM token embeddings consistently outperform them, which directly undermines ModernBERT-large's suitability for this task.

For the second critical issue, the proposal cites arXiv:2510.00866 as "peer review status pending," but it almost certainly was rejected from ICLR 2026 given the decision timeline, so the citation status should be updated to reflect that rejection rather than leaving it ambiguous.

Moving through the remaining Round 6 fixes, I'm verifying each one: QuaDMix's withdrawal status checks out, the ADAPT citation is now properly formatted without the arXiv ID, the characterization of arXiv:2604.13977 has been corrected to focus on structured outputs and prompt design, and arXiv:2510.02375 is now included in the landscape analysis.

Evaluating the proposal holistically, the novelty scores around 4/5—the Voronoi cell occupancy approach for selecting tail-covering synthetic data is genuinely novel and the differentiation from competing methods is now clearer, though the embedding choice criticism remains a meaningful limitation. On feasibility, the budget math works out to roughly 175 hours within the 200-hour limit and there's a throughput fallback plan, but the NeurIPS 2025 paper on ModernBERT embeddings introduces some uncertainty about whether the embedding assumptions hold up.

The proposal reads clearly after multiple revisions with strong evaluation design and no circular dependencies, though the foundation paper's apparent ICLR 2026 rejection and the embedding choice concern—directly challenged by recent work showing off-the-shelf BERT embeddings underperform domain-specific alternatives—are both significant issues that could undermine the results.

The embedding methodology is the critical problem here: a NeurIPS 2025 paper directly contradicts the choice of ModernBERT-large for data curation, so the proposal either needs to switch to language model-trained embeddings or include a controlled comparison. Beyond that, the citation status for the foundation paper needs updating since it's almost certainly rejected by now, and the recent similarity metrics paper should be cited in the landscape given its direct relevance to whether BERT-style embeddings work for pretraining data selection.

I'm weighing whether these issues push toward a revise verdict—the embedding challenge from a NeurIPS paper is methodologically significant enough that any reviewer familiar with that work will immediately flag it as a concern. immediately ask: "Why ModernBERT-large? NeurIPS 2025 showed LM token embeddings outperform off-the-shelf BERT models for this exact task." This could be a fatal reviewer objection.

However, there's a possible response: CGS uses ModernBERT for semantic coverage mapping, not for quality filtering - the criterion (tail cell occupancy) is different from the quality-proxy criterion that arXiv:2502.02494 tested. The paper tested "does this embedding predict pretraining loss differences" (quality proxy), whereas CGS uses embeddings purely for structural coverage mapping. This is a subtle but potentially valid distinction.

Still, a reviewer would want to see this distinction made explicit, or an ablation comparing ModernBERT vs. LM token embeddings for the Voronoi cell coverage task specifically.

Given that this is Round 7 of 10, the embedding choice concern is addressable with one paragraph clarifying the distinction from arXiv:2502.02494, and the overall proposal has matured significantly with budget, timeline, and differentiation all resolved, I should recommend revision. My scores would be: Novelty 4, Feasibility 3, Clarity 4, Impact 3.5, averaging 3.625 - solidly in "revise" territory. me now structure my review.

Wait, I should also check: does the proposal actually address any of the issues I'm raising? Let me re-read the current proposal more carefully.

Looking at the proposal again:

1. **arXiv:2502.02494**: Not cited anywhere in the proposal. This is a NeurIPS 2025 paper that directly challenges BERT-style embedding for pretraining data curation. This is a genuine miss.

2. **arXiv:2510.00866 status**: The proposal says "preprint; peer review status pending" which is now incorrect since ICLR 2026 decisions are out (January 2026) and the paper is not in the accepted list. Should say "rejected from ICLR 2026" or at minimum "not accepted at ICLR 2026."

3. **ModernBERT embedding choice justification**: The proposal justifies ModernBERT-large based on throughput advantages, but doesn't actually argue why it's the right embedding for semantic coverage mapping.

The embedding choice matters because CGS uses embeddings to define Voronoi cells and identify under-covered semantic regions, which is structurally different from the quality prediction task that arXiv:2502.02494 examines. Still, the concern holds: if the embedding space doesn't capture semantic similarity relevant to tail knowledge, the coverage cells might not correspond to meaningful regions.

I think the embedding critique is legitimate and would come up in review. The proposal should address it directly.

Also, I notice arXiv:2505.00979 (Synthesize-on-Graph, May 2025) tackles the same tail distribution problem through generation rather than selection, making it complementary rather than directly competing. It's less critical to cite than arXiv:2502.02494, but worth noting.

Now I'm ready to finalize my verdict: this needs revision. The critical issue is the missing engagement with arXiv:2502.02494, the moderate issue is the outdated citation status for arXiv:2510.00866, and the minor issue is the embedding justification needing more rigor.

Looking at the scoring: novelty holds at 4 since the core criterion is solid, feasibility drops to 3 because the embedding validity concern could undermine the results if Voronoi cells don't capture tail semantics accurately, clarity stays at 4, and impact is 3.5 given the foundation paper rejection and contingency on embedding choice. That averages to 3.625, confirming the revise recommendation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45c9fa30-3f1f-49ac-95af-f36897a4157e",
  "isSidechain": false,
  "requestId": "req_011CasgEqkmnUFYHi2UzTCqc",
  "type": "assistant",
  "uuid": "850abb2e-cbe6-4703-8e57-562ba2bd886d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014oZndtsQEwaL9uXUsG2Kiv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1535,
      "cache_creation_input_tokens": 3674,
      "cache_read_input_tokens": 45889,
      "output_tokens": 4737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1535,
          "output_tokens": 4737,
          "cache_read_input_tokens": 45889,
          "cache_creation_input_tokens": 3674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3674
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

_source line 27 · 2026-05-09T21:09:02.879Z_

Now I have the research I need. Let me synthesize all findings into my verdict.

**Key findings from independent verification:**

1. **QuaDMix "withdrawn" claim**: VERIFIED CORRECT — confirmed withdrawn from ICLR 2026 via OpenReview. Round 6 reviewer was wrong to flag this; the proposal was accurate.

2. **arXiv:2510.00866 ("The Data-Quality Illusion") status**: Almost certainly **rejected** from ICLR 2026 — absent from all ICLR 2026 accepted paper lists, accepted papers announced, and conference proceedings. ICLR 2026 decisions were announced January 22, 2026. The proposal's current phrasing "peer review status pending" is now factually incorrect.

3. **arXiv:2502.02494 (NeurIPS 2025, "Analyzing Similarity Metrics for Data Selection")**: This NeurIPS 2025 paper is **not cited in the proposal** and directly challenges CGS's embedding choice. It shows that off-the-shelf BERT-style encoders (including retrieval-trained models) systematically underperform domain-specific LM token embeddings for pretraining data curation, because they don't capture pretraining-relevant training dynamics. CGS relies on ModernBERT-large (an off-the-shelf encoder) without addressing this finding.

4. **Budget arithmetic**: Verified correct. ModernBERT-large at ~52K tok/s on RTX 4090 (confirmed from arXiv:2412.13663), ~100K tok/s estimate on H100 is plausible. 35H embedding arithmetic is correct. Total ~175H is under 200H constraint.

5. **ADAPT, OPUS, all other references**: ADAPT verified at OpenReview. No critical missed concurrent work beyond items 2-3 above.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "The CGS criterion — real-data Voronoi occupancy as a tail-density gate for synthetic selection — is genuinely distinct from Quad (influence-weighted MAB), MATES/Group-MATES (influence models), and Less-is-More (uniform coverage without reference density). Six rounds of iteration have sharpened differentiation to a defensible level."
    },
    "feasibility": {
      "score": 3,
      "rationale": "Budget arithmetic is now correct (~175H under 200H) and the throughput fallback (5-min pilot) handles uncertainty. However, arXiv:2502.02494 (NeurIPS 2025) shows off-the-shelf BERT-style encoders like ModernBERT-large systematically underperform domain-specific LM token embeddings for pretraining data curation — directly challenging whether CGS's Voronoi cells reflect semantically meaningful tail regions rather than retrieval-space artifacts."
    },
    "clarity": {
      "score": 4,
      "rationale": "After seven rounds the proposal is well-structured with explicit mechanistic claims, a clear evaluation hierarchy avoiding circularity, and crisp differentiation paragraphs for all major prior work."
    },
    "impact": {
      "score": 3,
      "rationale": "The opportunity narrative depends heavily on arXiv:2510.00866, which was almost certainly rejected from ICLR 2026 (not appearing in any ICLR 2026 accepted paper lists; decisions announced January 22, 2026). The method remains motivated independently, but the flagship 'CQF is illusory' claim rests on an unvetted preprint, limiting the field's confidence in the proposed solution."
    }
  },
  "issues": [
    "CRITICAL UNCITED NeurIPS 2025 PAPER — EMBEDDING CHOICE DIRECTLY CHALLENGED: arXiv:2502.02494 ('Analyzing Similarity Metrics for Data Selection for Language Model Pretraining,' NeurIPS 2025) explicitly shows that off-the-shelf BERT-style encoders — the class ModernBERT-large belongs to — systematically underperform domain-specific LM token embeddings for pretraining data curation. The paper finds that retrieval-trained and general-purpose encoders fail to capture training dynamics unique to the pretraining setting, and that simple LM token embeddings from same-corpus models outperform all off-the-shelf alternatives. CGS's entire cell structure depends on ModernBERT-large producing semantically meaningful Voronoi partitions for pretraining data coverage — any reviewer familiar with this NeurIPS 2025 result will immediately ask why a potentially misaligned embedding space is used. The proposal must either: (a) distinguish CGS's structural coverage use (cell occupancy mapping) from the quality-proxy prediction task studied in arXiv:2502.02494, arguing the critique does not transfer; or (b) add an Experiment 0 ablation comparing Voronoi cell structure from ModernBERT-large vs. LM token embeddings from a small Pythia model pretrained on Dolma. Without this, the core structural assumption — that ModernBERT cells align with semantically meaningful tail regions — is undermined by a published NeurIPS 2025 result.",
    "OUTDATED CITATION STATUS — arXiv:2510.00866 REJECTED FROM ICLR 2026: The proposal currently says 'peer review status pending' for arXiv:2510.00866 ('The Data-Quality Illusion'). ICLR 2026 final decisions were announced January 22, 2026, and this paper does not appear in any ICLR 2026 accepted paper list, conference proceedings, or outstanding paper announcements. By May 2026 (the current date), this paper has almost certainly been rejected from ICLR 2026. The phrasing 'peer review status pending' is factually incorrect for a decision that was made four months ago. The proposal should update to 'not accepted at ICLR 2026 (preprint)' or 'rejected from ICLR 2026' while retaining the existing hedge that the empirical finding is independently reproducible regardless of venue."
  ],
  "feedback": "Two targeted fixes are needed — both are scope-limited and do not require new experiments:\n\n1. ADDRESS arXiv:2502.02494 ON EMBEDDING CHOICE: Add the following to the method description or landscape section: 'arXiv:2502.02494 (NeurIPS 2025) shows that off-the-shelf BERT-style encoders underperform domain-specific LM token embeddings when used as quality proxies for pretraining data selection — because retrieval-optimized embeddings do not capture training dynamics specific to pretraining. CGS's use of ModernBERT-large is structurally different: we use embeddings to define a semantic coverage map (Voronoi cell occupancy) over a reference corpus, not to predict model loss or document quality scores. The cell occupancy criterion requires only that semantically similar documents cluster together in embedding space — a property that BERT-style masked LM pretraining is specifically designed to achieve and that Experiment 0(b) validates: if Wikidata long-tail documents significantly concentrate in low-occupancy cells relative to random C4 samples, the embedding partitioning is operationally correct for CGS's purpose regardless of its fitness as a quality proxy.' Also add arXiv:2502.02494 to key_references.\n\n2. UPDATE CITATION STATUS OF arXiv:2510.00866: Change all instances of 'peer review status pending' to 'rejected from ICLR 2026 (preprint).' The existing hedge sentence — 'The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status' — is good and should be retained. A rejected preprint can still motivate a new method if the finding is independently replicable, which the proposal correctly asserts.",
  "reason": "Two fixable issues remain: a NeurIPS 2025 paper (arXiv:2502.02494) directly challenges BERT-style embedding suitability for pretraining data curation and must be addressed, and the foundational opportunity paper (arXiv:2510.00866) was rejected from ICLR 2026 four months ago but is still cited as 'peer review status pending.'"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "850abb2e-cbe6-4703-8e57-562ba2bd886d",
  "isSidechain": false,
  "requestId": "req_011CasgEqkmnUFYHi2UzTCqc",
  "type": "assistant",
  "uuid": "21cc1f0c-7cb5-462e-82b9-4420ef373575",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014oZndtsQEwaL9uXUsG2Kiv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1535,
      "cache_creation_input_tokens": 3674,
      "cache_read_input_tokens": 45889,
      "output_tokens": 4737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1535,
          "output_tokens": 4737,
          "cache_read_input_tokens": 45889,
          "cache_creation_input_tokens": 3674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3674
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "21cc1f0c-7cb5-462e-82b9-4420ef373575",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CGS synthetic data selection method for EMNLP 2026",
  "sessionId": "f6781f5d-59c7-449b-9656-f1f6383296d8"
}
```

---
