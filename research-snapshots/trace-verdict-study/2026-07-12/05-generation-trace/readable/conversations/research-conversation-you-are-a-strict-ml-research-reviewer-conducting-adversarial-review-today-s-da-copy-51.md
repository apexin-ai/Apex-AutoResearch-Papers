# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-09 (UTC).** Your job: indep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 66
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/24715d91-e1d0-4e2b-a114-d4d7d84d7a06.jsonl`
- **Structured JSON:** [`ecd76eca5573eae96a7a.json`](../../sessions/ec/ecd76eca5573eae96a7a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-09T21:28:04.082Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-09T21:28:04.082Z",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-09 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.\n\nDirection: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.\n2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.\n3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.\n\nThis is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.\n\nTag: direction=data_governance, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-09?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 8/10)\n{\n  \"title\": \"Tail-Coverage-Guided Synthetic Data Selection to Replace Classifier Quality Filtering\",\n  \"core_problem\": \"Classifier-based quality filtering (CQF), the dominant method for selecting synthetic pretraining data used by GPT-3, LLaMA, and PaLM, is shown to be illusory — it improves downstream task performance not by improving language modeling quality but by implicit distribution-matching rather than genuine quality signals. Concurrently, synthetic data exhibits systematic distributional discrepancies relative to real data: top-p and temperature sampling truncate low-probability continuations, causing rare factual content to be systematically underrepresented in synthetic corpora. Kandpal et al. (ICML 2023) established a direct causal link: LLM accuracy on factual questions correlates strongly with the frequency of the underlying entity in pretraining documents, confirming that tail-knowledge acquisition depends on tail-content exposure during training. No principled selection criterion corrects for this distributional gap: CQF does not target it (and may worsen it by filtering toward fluent head-distribution text), while naïve random sampling inherits the generator's truncation bias wholesale. More recent model-aware selectors such as MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) adapt dynamically to the evolving model's preferences but do not target the specific tail-distribution gap — they optimize for generic influence rather than for correcting truncation-induced underrepresentation.\",\n  \"opportunity\": \"Three concurrent findings create a gap that demands a new method: (1) 'The Data-Quality Illusion' (arXiv:2510.00866, rejected from ICLR 2026; preprint) demonstrates that CQF does not improve language modeling on held-out high-quality data and argues the field should rethink synthetic data filtering from first principles; (2) 'Data Value in the Age of Scaling' (arXiv:2511.13640) identifies tail-knowledge underrepresentation as a systematic distributional discrepancy in synthetic data under real-synthetic mixing, linked to generative truncation mechanisms; (3) Kandpal et al. (ICML 2023) provides external causal validation: pretraining document frequency is a strong predictor of downstream accuracy on rare facts. Together, these findings establish that (a) CQF is the wrong solution, (b) the actual problem is a distributional gap at the tail, and (c) closing the tail gap causally improves knowledge acquisition. The opportunity is 'Coverage-Guided Sampling' (CGS): select synthetic examples to maximize marginal coverage of low-density regions of the real-data embedding space, directly targeting the distributional gap that CQF fails to address. This is the first synthetic data selector explicitly designed around the mechanism documented in arXiv:2510.00866 rather than a classifier proxy. The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status; CGS would be motivated equally if the finding were confirmed by independent replication. Concurrent work (arXiv:2604.13977, April 2026) finds that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are the dominant factors in synthetic pretraining quality — outperforming both larger generator models and format-agnostic generation strategies — providing external corroboration that principled, non-classifier-based generation and selection choices are the right axis for improving synthetic pretraining data quality, consistent with CGS's reference-density-gated approach.\",\n  \"landscape\": \"CQF is used by all major pretraining pipelines (GPT-3, LLaMA, PaLM, RedPajama) but arXiv:2510.00866 (rejected from ICLR 2026; preprint) shows its quality signal is misleading. Six clusters of prior work bound the proposal:\\n\\n**Diversity-quality pretraining selection.** Quad (arXiv:2409.16986, ICLR 2025 Spotlight) is the most important prior work. Quad clusters all pretraining data and uses a Multi-Armed Bandit (MAB) scheme favoring clusters with high influence scores (quality) or low selection frequency (diversity). CGS differs on three axes: (1) Criterion — CGS uses a real-data tail-density threshold (bottom 20–25% by Voronoi cell occupancy in a reference corpus) rather than influence-weighted underrepresentation; CGS does not require influence score computation, which is expensive to scale to billions of synthetic candidates; (2) Target — CGS applies specifically to the synthetic data mixing problem and requires a real-data reference corpus to define 'tail'; Quad operates within a single multi-source corpus without a reference density; (3) Motivation — CGS is grounded in the CQF failure mechanism documented in arXiv:2510.00866. QuaDMix (arXiv:2504.16511, withdrawn from ICLR 2026, openreview.net/forum?id=oLxx7OhAb1) from ByteDance proposes a parameterized quality-diversity sampling function using domain classification for diversity measurement and LightGBM for parameter search. Like Quad, QuaDMix does not target real-data tail density specifically.\\n\\n**Model-aware selection.** MATES (arXiv:2406.06046, NeurIPS 2024) trains a lightweight BERT-base influence model that continuously adapts to the evolving pretraining model's data preferences, updating every 10,000 steps. MATES achieves 2× the gain of prior SOTA (QuRating) on 410M and 1B models, at 11.5–21.7% computational overhead. CGS differs on three axes: (a) CGS requires no influence model training — the FAISS IVF index is built once over the fixed reference corpus before pretraining begins, versus MATES's periodic BERT-base retraining; (b) CGS requires no reference task definition — MATES's performance varies substantially with reference task choice, a deployment-time burden; (c) CGS targets a specific, mechanistically motivated failure mode (CQF distributional bias) rather than maximizing generic influence scores.\\n\\nGroup-MATES (arXiv:2502.14709, NeurIPS 2025) extends MATES to group-level selection: it trains a relational data influence model that weights individual sample influence by inter-data relationships, partitions the training corpus into clusters via these relationship weights, and selects within each cluster independently, achieving 3.5–9.4% relative gains and 1.75× token efficiency over individual selection baselines on DCLM at 400M–3B scales across 22 tasks. CGS differs on three axes: (a) CGS requires no influence model — Voronoi cells are defined by k-means over a fixed reference corpus embedding, not by data-data relational influence weights, making CGS zero-overhead relative to training; (b) CGS uses reference-corpus occupancy density as the selection gate — only tail cells (bottom 20–25% by reference occupancy) are eligible for synthetic coverage — rather than influence-weighted within-cluster scoring; (c) CGS targets the specific synthetic-real distributional gap documented in arXiv:2511.13640: it applies to a fixed synthetic candidate pool relative to a real-data reference corpus, whereas Group-MATES operates within a single training corpus without a reference density criterion.\\n\\n**Tail knowledge via synthetic generation.** EntiGraph (arXiv:2409.07431, ICLR 2025 Oral) addresses tail-knowledge acquisition through synthetic document generation: given a small domain corpus, it extracts salient entities, constructs a knowledge graph dynamically from entity-pair relationships via LM-driven synthesis, and generates new documents traversing those relationships — improving tail-fact retention in continued pretraining. Unlike CGS, EntiGraph is a generative method that requires a structured source corpus as input to drive entity extraction; it produces entirely new documents rather than selecting from a pre-existing pool, and is evaluated on domain-specific continued pretraining (QuALITY benchmark) rather than open-domain general pretraining. The approaches are orthogonal and complementary: CGS could select tail-covering subsets of an EntiGraph-generated corpus, concentrating the EntiGraph generation budget on the regions of real-data embedding space already underrepresented.\\n\\n**Architectural approaches to tail knowledge.** 'Pretraining with Hierarchical Memories: Separating Long-Tail and Common Knowledge' (arXiv:2510.02375, October 2025) addresses tail knowledge acquisition through model architecture changes rather than data selection: it introduces hierarchical parametric memory banks alongside a smaller core model, storing long-tail world knowledge in memory parameters while the core model captures common knowledge and general reasoning, with a 160M-parameter model plus 18M-parameter memory (fetched from a 4.6B bank) achieving performance comparable to a standard model with more than 2× the parameters. This architectural intervention is orthogonal to CGS: CGS improves the training distribution presented to any model architecture, and could complement hierarchical memory architectures by ensuring the training data seen by those memory components better covers tail-content regions.\\n\\n**Coverage-based fine-tuning.** 'Less is More: Adaptive Coverage for Synthetic Training Data' (arXiv:2504.14508, 2025) applies a greedy maximum-coverage objective to select synthetic fine-tuning data for NLP classifiers. CGS shares the max-coverage algorithmic skeleton but differs critically in three respects: (1) 'Less is More' maximizes coverage of ALL embedding cells uniformly — without a reference-corpus density criterion, it would waste selection budget on head cells already well-covered by real data, failing to address the distributional gap that CQF leaves open; CGS adds the critical step of using real-data Voronoi occupancy as a gate: only tail cells (bottom 20–25% by reference occupancy) are eligible, ensuring the entire selection budget is concentrated on underrepresented regions; (2) CGS applies at pretraining scale (hundreds of millions of candidates), requiring FAISS IVF for tractability; (3) this reference-density threshold is the mechanistic link to the CQF failure documented in arXiv:2510.00866, which 'Less is More' does not establish.\\n\\n**Embedding suitability for pretraining data curation.** 'Analyzing Similarity Metrics for Data Selection for Language Model Pretraining' (arXiv:2502.02494, NeurIPS 2025) systematically evaluates off-the-shelf BERT-style encoders (USE, Gecko, BERT) against specialized LM token embeddings for two tasks: (1) predicting pretraining loss differences between documents (quality-proxy use), and (2) within-corpus diversity curation via cluster-based redundancy reduction. The paper finds that off-the-shelf models underperform for both tasks, with the gap being largest for loss prediction and meaningfully smaller for diversity curation — 'LM Token Embeds performs comparably to Gecko, while outperforming all other off-the-shelf embeddings' in the diversification setting. CGS's use of ModernBERT-large is structurally distinct from both evaluated tasks on three axes: (a) CGS does not use embeddings to predict document quality or model loss — it uses them to partition semantic space into Voronoi cells and measure real-data occupancy, a coverage-mapping task not evaluated in arXiv:2502.02494; (b) CGS's selection criterion operates across two corpora (synthetic candidate pool versus a real-data reference corpus), targeting cross-corpus density gaps rather than within-corpus redundancy reduction — the only application arXiv:2502.02494's diversity experiments address; (c) the validity of ModernBERT-large for CGS's specific structural purpose is directly tested by Experiment 0(b): if Wikidata long-tail documents significantly cluster in low-occupancy Voronoi cells relative to random C4 samples, the embedding partition is operationally correct for CGS regardless of its fitness as a pretraining loss predictor. As a robustness check, Experiment 0 includes a CPU-only comparison: Pythia-410M LM token embeddings (embedding matrix row-averages over document tokens, no forward pass required, per arXiv:2502.02494's construction) are used to build a parallel FAISS IVF index; if both ModernBERT-large and Pythia LM token embeddings agree on which Wikidata long-tail documents cluster in low-occupancy cells, the coverage mapping is robust to embedding choice; if they disagree systematically, we fall back to Pythia LM token embeddings for all downstream experiments, consistent with arXiv:2502.02494's recommendation.\\n\\n**Online pretraining data curation.** ADAPT ('Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods', Zhao et al., ICLR 2026 Workshop DATA-FM, openreview.net/forum?id=zgn3P31NWf) and AC-ODM ('Actor-Critic Online Data Mixing', arXiv:2505.23878, preprint) represent an online paradigm: rather than pre-filtering the candidate pool, they dynamically reweight or re-mix training samples during training based on loss signals. CGS is orthogonal and compatible: as a static offline pre-filter, it reduces the synthetic candidate pool to tail-coverage-optimal documents before training begins with zero ongoing overhead; an online reweighter can further adapt the mix at training time after CGS has already narrowed the pool. Neither ADAPT nor AC-ODM targets the specific synthetic-real tail-density gap documented in arXiv:2510.00866 — they optimize generic influence or domain balance, not reference-density-defined tail coverage.\\n\\n**Synthetic data scale findings.** 'Demystifying Synthetic Data in LLM Pre-training' (arXiv:2510.01631, EMNLP 2025) finds ~30% rephrased synthetic data is empirically optimal but provides no mechanistic filter. arXiv:2511.13640 characterizes three-phase scaling behavior under real-synthetic mixing and identifies tail underrepresentation as a systematic discrepancy without a selection remedy. Concurrent work arXiv:2604.13977 ('How Can We Synthesize High-Quality Pretraining Data?', April 2026) systematically compares synthetic pretraining strategies across generator models and formats, finding that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are dominant factors in synthetic pretraining quality — outperforming both larger generator models and format-agnostic generation strategies. This provides independent corroboration for CGS's non-classifier-proxy approach: if principled generation choices outperform raw scale and classifier-based proxies, the right axis to optimize is how data is selected and structured rather than whether a quality classifier endorses it.\\n\\n**Tail knowledge evaluation and deduplication.** Kandpal et al. (arXiv:2211.08411, ICML 2023) establish that LLM accuracy on factual questions correlates causally with pretraining document frequency, providing the empirical foundation for CGS's tail-coverage hypothesis. 'Head-to-Tail' (arXiv:2308.10168, NAACL 2024) provides a purpose-built 18K QA benchmark explicitly stratified into head, torso, and tail facts by knowledge graph frequency — an independent evaluation resource for CGS. D4 (NeurIPS 2023) uses FAISS k-means for deduplication/diversification via distance-to-centroid pruning; it applies a distance heuristic not a tail-density threshold and does not target the synthetic selection sub-problem.\",\n  \"approach\": \"Coverage-Guided Sampling (CGS) selects synthetic pretraining data by maximizing coverage of underrepresented tail regions in real-data embedding space.\\n\\n**Method.** We embed a reference corpus (5B-token stratified sample of Dolma, preserving domain balance) and all candidate synthetic documents using ModernBERT-large, then build a FAISS IVF index over the real-data embeddings. The resulting Voronoi cell structure partitions semantic space; 'tail cells' are defined as cells in the bottom 20–25% by real-data occupancy. CGS then greedily selects synthetic documents maximizing marginal coverage of tail cells via a streaming maximum-coverage subproblem — no quality classifier training required. ModernBERT-large is chosen for embedding over larger alternatives due to its superior throughput: the official ModernBERT benchmark documents ~52K tokens/sec for ModernBERT-large on RTX 4090 (arXiv:2412.13663); H100 SXM delivers 2–4× RTX 4090 throughput for encoder inference (NVIDIA H100 Tensor Core GPU product brief), placing ModernBERT-large at ~100–200K tok/s on H100 — versus ~15–30K for Qwen3-Embedding-8B. To verify this before committing to full-corpus embedding, we run a 100K-document throughput pilot (~51M tokens, ~5 GPU-minutes) at the start of Experiment 0; if measured throughput is below 60K tok/s, the synthetic pool is reduced from 15M to 10M documents (7.68B → 5.12B tokens), reducing total embedding to ~47H and holding overall budget under 185H. Embedding quality is validated in Experiment 0. arXiv:2502.02494 (NeurIPS 2025) finds that off-the-shelf BERT-style encoders underperform LM token embeddings for pretraining data curation when used as quality proxies or for within-corpus diversity; CGS uses ModernBERT-large for cross-corpus coverage mapping (Voronoi cell occupancy relative to a reference corpus), a structurally distinct task, with operational validity confirmed by Experiment 0(b) and robustness-checked against Pythia LM token embeddings in Experiment 0(c).\\n\\n**Mechanistic validation experiment (Experiment 0, ~2 H100-hours).** Before committing to training runs, we validate the core empirical hypothesis: (a) Generate three synthetic corpora of 10M tokens each using Qwen3-72B with top-p ∈ {0.5, 0.85, 0.95}; embed and assign each document to a Voronoi cell; measure whether lower top-p concentrates documents in higher-occupancy cells (expected: yes, since low top-p collapses to high-probability continuations); (b) Embed 5,000 Wikidata long-tail documents (entities appearing <100 times in C4) and confirm they cluster significantly more in low-occupancy cells than a random C4 sample. (c) As a CPU-only embedding robustness check (zero GPU cost): build a parallel FAISS IVF index using Pythia-410M LM token embeddings (row-averages over the token embedding matrix for each document, no model forward pass required) for 50,000 Wikidata long-tail documents and 50,000 random C4 samples; if the low-occupancy cell assignments from ModernBERT-large and Pythia LM token embeddings agree on ≥85% of Wikidata long-tail documents, ModernBERT-large is confirmed as operationally valid for CGS's coverage mapping; if agreement falls below 85%, all subsequent experiments use Pythia LM token embeddings for Voronoi cell construction. If (a) shows r < 0.3 between top-p and mean cell occupancy, or (b) shows no significant enrichment, halt before Tier 1 and revise the tail-density criterion. If (c) shows below-85% agreement between ModernBERT and Pythia LM token embeddings, switch to Pythia LM token embeddings before proceeding to full embedding (zero additional GPU cost).\\n\\n**Model architecture and training.** Following the precedent of MATES (NeurIPS 2024), Quad (ICLR 2025), and D4 (NeurIPS 2023), we use the Pythia model family (EleutherAI GPT-NeoX codebase) for full reproducibility:\\n- *Tier 1 — Systematic ablation: Pythia-410M* (24 layers, hidden dim 1024, 16 heads, 2048 sequence length; ~8B tokens, Chinchilla-optimal). AdamW optimizer with β1=0.9, β2=0.95, weight decay 0.1; cosine LR schedule with 1% warmup steps. Following Wang et al. ('Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice,' ICLR 2026 Poster), all Tier 1 ablations use a 10× reduced peak learning rate of 3×10⁻⁵ (instead of the standard 3×10⁻⁴) to ensure selection method rankings derived from the 410M proxy runs transfer reliably to Tier 2 at 1.4B scale — this costs no additional GPU-hours since the reduced-LR runs replace rather than supplement standard-LR runs. Batch size ~2M tokens. 5 configurations: CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, and random baseline. Only CGS has a tail-threshold parameter; the three non-CGS methods run once without threshold variation. Each run: ~9 H100-hours on 1 GPU.\\n- *Tier 2 — Scaling check: Pythia-1.4B* (24 layers, hidden dim 2048, 16 heads, 2048 sequence length; 10B tokens). Same optimizer family with peak LR 2×10⁻⁴. 2 configurations: best CGS from Tier 1 vs. CQF-FineWebEdu. Each run: ~44 H100-hours (4 GPUs × ~11h wall-clock via data parallelism). Using Pythia-1.4B (not 1.3B) ensures exact architecture reproducibility with the published model family.\\n\\n**Synthetic candidate pool.** We precompute embeddings for a fixed 15M-document synthetic pool generated by Qwen3-72B (top-p=0.9, temperature=1.0, avg 512 tokens/document = 7.68B tokens total). At 100K tokens/sec per H100 (nominal): the 7.68B synthetic tokens require 76,800s ≈ 21.3 GPU-hours; the 5B-token reference corpus requires 50,000s ≈ 13.9 GPU-hours; total embedding ≈ 35 GPU-hours ≈ 8.8H wall-clock on 4 GPUs. Under the throughput fallback (10M docs, ~5.12B tokens), embedding reduces to ~19H + 13.9H ≈ 33H for synthetic + reference ≈ 47H total. This pool size provides ample selection diversity: 7.68B tokens exceeds the synthetic allocation for both Tier 1 (~2.4B tokens at 30% synthetic) and Tier 2 (~3B tokens at 30% synthetic) by over 2.5×. FAISS IVF build is CPU-bound (~2h on 32 cores) and runs concurrently with early embedding steps.\\n\\n**IVF nlist calibration.** nlist ≈ sqrt(N_reference_docs) per FAISS best practices. Tier 1 pilots probe two nlist settings (±30%) to confirm tail cell occupancy is well-separated; this is CPU-only analysis on the pre-built index (zero GPU cost). If cell structure is degenerate, we correct before the Tier 2 run.\\n\\n**Evaluation — primary, secondary, and diversity metrics.** The evaluation design explicitly separates the training criterion (FAISS cell coverage) from the test signal to avoid circularity:\\n\\n(1) *Primary — TriviaQA head/tail accuracy split (independent external metric)*: Using Wikipedia page-view statistics to stratify TriviaQA questions into head entities (top 20% by views, ~1K questions) and tail entities (bottom 20%, ~1K questions), we measure accuracy separately. This stratification uses an external resource (Wikipedia traffic data) wholly independent of the FAISS cell structure. Per Kandpal et al. (ICML 2023), tail-entity accuracy is the most causally meaningful test of whether tail coverage translates to knowledge acquisition. We report the tail/head accuracy ratio as the primary CGS-vs-CQF gap metric.\\n\\n(2) *Additional independent benchmark — Head-to-Tail (NAACL 2024)*: This purpose-built 18K QA benchmark stratifies facts into head, torso, and tail by knowledge graph frequency (Wikidata). It provides a second external validation of tail knowledge independent of both FAISS and Wikipedia pageviews, strengthening the falsifiability of the tail-coverage claim.\\n\\n(3) *Secondary — Standard downstream benchmarks*: HellaSwag, WinoGrande, ARC-E/C, PIQA — required for comparability with Quad, D4, MATES, Group-MATES, and CQF baselines. CGS should match or exceed CQF on these benchmarks; failure here would indicate coverage-only selection sacrifices head-distribution capabilities.\\n\\n(4) *Diversity of selected synthetic data (CPU-only, zero GPU cost)*: We compute corpus-level self-BLEU (Zhu et al., 2018; lower = more diverse) and 4-gram entropy (higher = more diverse) over the synthetic subset selected by each method (CGS, CQF-Wikipedia, CQF-FineWebEdu, random). These metrics are computed post-selection before training begins. CGS should exhibit lower self-BLEU and higher n-gram entropy than CQF-selected data, since CQF preferentially selects fluent head-distribution text with low lexical diversity. This directly substantiates the coverage-vs-classifier-proxy claim: not only does CGS target underrepresented semantic regions, but the selected text should be measurably more lexically diverse than CQF output — consistent with the concurrent finding (arXiv:2604.13977) that principled generation choices (structured formats, prompt design) outperform classifier-based proxies in synthetic pretraining quality.\\n\\n(5) *Diagnostic — Held-out low-occupancy perplexity*: 5% of reference corpus documents from the bottom 20% occupancy cells are held out before training and used to measure model perplexity. This metric is demoted to a sanity check because CGS is explicitly optimized to cover exactly those cells — perplexity improvement here confirms distribution matching, not necessarily genuine knowledge acquisition. It is reported alongside (1) and (2) but not used as a primary falsifiability claim.\\n\\n**Falsifiable primary claim**: CGS achieves higher TriviaQA tail-entity accuracy than CQF while matching CQF on standard downstream benchmarks, directly operationalizing the quality-vs-coverage paradox documented in arXiv:2510.00866. The diversity metrics (self-BLEU, n-gram entropy) provide a secondary mechanistic check confirming that CGS's tail-coverage selection is not collapsing to a high-fluency, low-diversity subset.\\n\\n**Timeline and execution mode.** Given the EMNLP 2026 ARR deadline of May 25, 2026 (16 days from proposal date), the primary execution path is auto-research mode. GPU wall-clock with 4× H100: Experiment 0 (~2h, including 5-min throughput pilot) → Embedding (~8.8h, 4 GPUs, or ~5.8h under 10M-doc fallback) → FAISS build (~2h CPU concurrent) → Tier 1 ablation grid (~18h, 4 experiments in parallel in batch 1, then 1 remaining) → Tier 2 scaling check (~22h, 2 sequential runs with 4-GPU data parallelism). Total GPU wall-clock: ~50.8 hours (~2.1 days) nominal; ~48.8h under fallback. Paper writing begins in parallel on day 1; Tier 1 results are guaranteed by day 4; Tier 2 results are best-effort. If Tier 2 runs do not complete before submission, the 1.4B experiments are described as ongoing and submitted to camera-ready.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~172 H100-hours (Experiment 0 ~2h including 5-min throughput pilot; embedding ModernBERT-large on 15M synthetic docs + 5B reference corpus ~35h [nominal, throughput ≥ 60K tok/s] or ~47H [10M-doc fallback if throughput < 60K tok/s, reducing synthetic pool from 7.68B to 5.12B tokens]; FAISS IVF build CPU-bound ~0h GPU; Tier 1 ablations 5 configurations × ~9h = 45h; Tier 2 scaling check 2 runs × ~44h = 88h; misc eval ~2h). Budget stays ≤185H under fallback scenario; arithmetic verified: 7.68B synthetic tokens ÷ 100K tok/s = 21.3H + 5B reference ÷ 100K tok/s = 13.9H = 35.2H nominal.\",\n      \"gpu_utilization\": \"Low (~40% active) — researcher waits between tiers to review Experiment 0 results and pilot outcomes before committing to 1.4B runs.\",\n      \"timeline\": \"3–5 months. INCOMPATIBLE with May 25, 2026 ARR deadline — use auto-research mode for deadline-constrained execution.\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$420–615 at $2.44–3.56/hr per H100 (RunPod/Lambda Labs current pricing)\",\n      \"risk_note\": \"If Experiment 0 (mechanistic validation) fails — i.e., top-p does not correlate with cell occupancy in the expected direction — the core hypothesis needs revision before Tier 1 ablations begin. Caught in the first ~2 H100-hours. If throughput pilot shows < 60K tok/s, pool is reduced to 10M docs and budget stays under 185H.\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~190 H100-hours (manual base ~172H plus agent overhead: 2 additional 410M sensitivity runs for IVF nlist ±30% around baseline and ModernBERT-large vs. sentence-transformers/all-MiniLM-L6-v2 embedding model speed check, each ~9h = 18H extra; plus ~0H GPU for nlist structure analysis which is CPU-only; throughput fallback to 10M-doc pool reduces embedding by ~9H if triggered, capping at ~181H under fallback).\",\n      \"gpu_utilization\": \"Moderate (~60% active) — agent queues experiments continuously but awaits human approval before committing to each Tier 2 run.\",\n      \"timeline\": \"4–6 weeks. INCOMPATIBLE with May 25, 2026 ARR deadline — use auto-research mode for deadline-constrained execution.\",\n      \"team\": \"1 researcher, ~45 min/day check-in to approve tier transitions and review Experiment 0 results\",\n      \"claude_api_cost\": \"$200–350 (experiment queue management, Experiment 0 result interpretation, IVF calibration guidance)\",\n      \"estimated_gpu_cost\": \"~$464–676 at $2.44–3.56/hr per H100\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~175 H100-hours (Experiment 0 ~2h including 5-min throughput pilot; embedding ModernBERT-large for 15M synthetic docs [7.68B tokens] + 5B reference corpus ~35h [throughput ≥ 60K tok/s] or ~47H [10M-doc fallback if throughput < 60K tok/s]; FAISS IVF build CPU-bound ~0h GPU; Tier 1 ablation grid 5 configurations × ~9h = 45h; Tier 2 scaling check 2 runs × ~44h = 88h; misc eval ~3h). Budget ≤175H nominal, ≤185H under fallback; capped at 175H by early-stopping if Experiment 0 fails (saves ~138H by avoiding Tier 1 and Tier 2).\",\n      \"gpu_utilization\": \"High (~85% active) — agent queues Experiment 0 (with throughput pilot) → embedding → FAISS build → Tier 1 ablation grid → Tier 2 runs without human wait. ~15% overhead from API round-trips and CPU-bound FAISS builds between GPU steps.\",\n      \"timeline\": \"8–12 days total: ~2.1 days GPU wall-clock compute (50.8 hours on 4× H100) + paper writing in parallel from day 1. Tier 1 results available by day 4; Tier 2 results by day 5. Writing days 1–14 (parallel); submission day 16 (May 25, 2026 ARR deadline). COMPATIBLE with deadline under this framing: Tier 1 results are guaranteed at submission; Tier 2 results are best-effort and described as ongoing in the paper if not complete.\",\n      \"team\": \"0 (initial setup ~3h: configure ModernBERT-large embedding pipeline with FAISS IVF builder, GPT-NeoX training harness with eval on HellaSwag/WinoGrande/ARC/PIQA + TriviaQA head/tail + Head-to-Tail benchmark)\",\n      \"claude_api_cost\": \"$600–900 (automated Experiment 0 interpretation, ablation grid orchestration, early-stopping decisions, TriviaQA stratification computation, final report generation — estimated 5,000–8,000 API turns)\",\n      \"estimated_gpu_cost\": \"~$427–623 at $2.44–3.56/hr per H100\",\n      \"speed_bottleneck\": \"4× H100 allows: Embedding (15M synthetic docs + 5B reference corpus) completes in ~8.8h wall-clock (35H ÷ 4 GPUs); Tier 1 grid runs in ~18h wall-clock (4 configs in parallel batch 1, then 1 remaining config in batch 2, each ~9H on 1 GPU); Tier 2 serializes at ~11h wall-clock each with 4-GPU data parallelism (2 runs = 22h). Total GPU wall-clock: ~2h (Exp 0) + ~8.8h (embedding) + ~18h (Tier 1) + ~22h (Tier 2) ≈ 50.8h ≈ 2.1 days.\",\n      \"risk_note\": \"Early-stopping trigger: if Experiment 0 shows Pearson r < 0.3 between top-p value and mean cell occupancy rank, halt and report mechanism failure before consuming Tier 1 compute. Throughput early-stop: if 5-min pilot measures < 60K tok/s, reduce synthetic pool from 15M to 10M documents before proceeding to full embedding, holding total budget under 185H. Pre-specified thresholds prevent exhaustive exploration of degenerate configurations.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026; conference October 24–29, 2026, Budapest, Hungary). Primary execution path: auto-research mode, with Tier 1 (Pythia-410M) results guaranteed at submission and Tier 2 (Pythia-1.4B) submitted to camera-ready.\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining (arXiv:2510.00866, rejected from ICLR 2026; preprint)\",\n    \"Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures (arXiv:2511.13640, 2025)\",\n    \"Harnessing Diversity for Important Data Selection in Pretraining Large Language Models (Quad, arXiv:2409.16986, ICLR 2025 Spotlight)\",\n    \"QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining (arXiv:2504.16511, withdrawn from ICLR 2026, openreview.net/forum?id=oLxx7OhAb1)\",\n    \"MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models (arXiv:2406.06046, NeurIPS 2024)\",\n    \"Group-MATES: Group-Level Data Selection for Language Model Pretraining (arXiv:2502.14709, NeurIPS 2025)\",\n    \"Synthetic Continued Pretraining via EntiGraph (arXiv:2409.07431, ICLR 2025 Oral)\",\n    \"Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice (Wang et al., ICLR 2026 Poster, openreview.net/forum?id=2FZC0c06jP)\",\n    \"Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods — ADAPT (Zhao et al., ICLR 2026 Workshop DATA-FM, openreview.net/forum?id=zgn3P31NWf)\",\n    \"AC-ODM: Actor-Critic Online Data Mixing for Sample-Efficient LLM Pretraining (arXiv:2505.23878, preprint)\",\n    \"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls (arXiv:2510.01631, EMNLP 2025)\",\n    \"How Can We Synthesize High-Quality Pretraining Data? (arXiv:2604.13977, April 2026)\",\n    \"Large Language Models Struggle to Learn Long-Tail Knowledge (Kandpal et al., arXiv:2211.08411, ICML 2023)\",\n    \"Head-to-Tail: How Knowledgeable are Large Language Models in Long-Tail Knowledge? (arXiv:2308.10168, NAACL 2024)\",\n    \"Pretraining with Hierarchical Memories: Separating Long-Tail and Common Knowledge (arXiv:2510.02375, October 2025)\",\n    \"Measuring Diversity in Synthetic Datasets (arXiv:2502.08512, ICML 2025)\",\n    \"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning (arXiv:2511.01490, ACL Findings 2026)\",\n    \"Less is More: Adaptive Coverage for Synthetic Training Data (arXiv:2504.14508, 2025)\",\n    \"D4: Improving LLM Pretraining via Document De-Duplication and Diversification (NeurIPS 2023)\",\n    \"Scaling Laws of Synthetic Data for Language Models (arXiv:2503.19551, 2025)\",\n    \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling (arXiv:2304.01373, ICML 2023)\",\n    \"ModernBERT: Smarter, Better, Faster, Longer (arXiv:2412.13663, 2024)\",\n    \"Analyzing Similarity Metrics for Data Selection for Language Model Pretraining (arXiv:2502.02494, NeurIPS 2025)\"\n  ],\n  \"description\": \"Classifier-based quality filtering (CQF) — the dominant synthetic pretraining selector used by GPT-3, LLaMA, and PaLM — has been shown to boost downstream task scores via implicit distribution-matching rather than genuine quality improvement (arXiv:2510.00866, rejected from ICLR 2026; preprint; independently reproducible from first principles regardless of venue outcome). Concurrently, Kandpal et al. (ICML 2023) established that LLM accuracy on rare facts causally correlates with pretraining document frequency, confirming that tail-content exposure drives tail-knowledge acquisition; arXiv:2511.13640 documents systematic tail underrepresentation in synthetic data via top-p/temperature truncation; and concurrent work arXiv:2604.13977 (April 2026) finds that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are dominant factors in synthetic pretraining quality — outperforming generator scale and format-agnostic generation — providing external corroboration that principled generation choices matter more than classifier-based proxies, consistent with CGS's non-proxy-based selection criterion. This project proposes Coverage-Guided Sampling (CGS), the first principled pretraining data selector grounded in the actual distributional failure mechanism of CQF. CGS embeds a 5B-token reference corpus and a fixed 15M-document synthetic candidate pool (7.68B tokens) using ModernBERT-large — whose official benchmark documents ~52K tokens/sec on RTX 4090 (arXiv:2412.13663); H100 SXM delivers 2–4× RTX 4090 throughput for encoder inference (NVIDIA H100 product brief), placing it at ~100–200K tok/s. arXiv:2502.02494 (NeurIPS 2025) finds that off-the-shelf BERT-style encoders underperform LM token embeddings for pretraining data quality prediction and within-corpus diversity, but the performance gap is smaller for diversity tasks than loss prediction; CGS's cross-corpus coverage-mapping use (Voronoi cell occupancy relative to a reference corpus) is structurally distinct from both evaluated tasks and validated empirically via Experiment 0(b)/(c). A 100K-document throughput pilot (~5 GPU-minutes) at the start of Experiment 0 verifies throughput before committing to full-corpus embedding; if measured throughput is below 60K tok/s, the synthetic pool is reduced from 15M to 10M documents, holding total budget under 185H. Total embedding ≈ 35 GPU-hours nominal (7.68B synthetic tokens ÷ 100K tok/s = 21.3H + 5B reference ÷ 100K tok/s = 13.9H ≈ 8.8H wall-clock on 4 GPUs). CGS builds a FAISS IVF index over the real corpus, identifies low-density Voronoi 'tail cells' (bottom 20–25% by occupancy), and greedily selects synthetic documents maximizing marginal tail-region coverage — no classifier training required. A mandatory Mechanistic Validation Experiment (~2 H100-hours, inclusive of throughput pilot) confirms that Voronoi cell density correlates with top-p sampling behavior and that ModernBERT-large partitions are operationally valid (or falls back to Pythia LM token embeddings) before committing to training runs. We train using the Pythia model family: Tier 1 uses Pythia-410M at Chinchilla-optimal scale (~8B tokens, 5 ablation configurations, ~45 H100-hours) with the 10× reduced peak LR (3×10⁻⁵) recommended by Wang et al. (ICLR 2026 Poster) for proxy-to-full-scale ranking reliability; Tier 2 uses Pythia-1.4B at 10B tokens (2 configurations, ~88 H100-hours); total budget ~175 H100-hours nominal, ≤185H under fallback. Evaluation resolves circularity: TriviaQA tail-entity accuracy (stratified by Wikipedia pageviews, independent of FAISS) and the Head-to-Tail benchmark (NAACL 2024) are primary falsifiability metrics; corpus-level self-BLEU and 4-gram entropy over selected synthetic data are computed CPU-only post-selection to confirm CGS produces more diverse output than CQF. Closest prior work: EntiGraph (ICLR 2025 Oral, arXiv:2409.07431) generates new synthetic documents by traversing entity relationships in a source corpus — CGS is a post-hoc selector for any pre-existing synthetic pool without generative infrastructure, and the approaches are complementary. Architectural methods such as hierarchical memory banks (arXiv:2510.02375) address tail knowledge through model architecture changes rather than data selection; CGS is orthogonal and could complement such architectures by improving the training distribution seen by those memory components. Quad (ICLR 2025) uses influence-weighted cluster MAB — CGS requires no influence scoring. MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) train influence models — CGS builds its FAISS index once with zero ongoing overhead and no reference task dependency. 'Less is More' maximizes uniform coverage of all cells — CGS adds a real-data reference-density gate (bottom 20–25% occupancy only). Online methods ADAPT (ICLR 2026 Workshop DATA-FM) and AC-ODM reweight during training — CGS is a compatible offline pre-filter. Primary execution path: auto-research mode (4× H100, ~2.1 days GPU wall-clock, paper writing in parallel), targeting EMNLP 2026 ARR deadline May 25, 2026, with Tier 1 results guaranteed at submission.\",\n  \"project_name\": \"cov_guided_synth_sel\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"VENUE CLAIM ERROR: The generator labels arXiv:2510.00866 as 'EMNLP 2025', but independent search confirms the OpenReview submission targets ICLR 2026 (not EMNLP 2025). This foundational reference for the 'opportunity' narrative may have a different reception history; the paper should be cited as a preprint with venue status clarified.\", \"CLAIM OVERSTATEMENT: arXiv:2511.13640 is described as proving 'tail-knowledge underrepresentation is a leading driver of collapse.' The paper's abstract identifies tail underrepresentation as a distributional discrepancy observed in synthetic data and studies three-phase scaling — it does not specifically claim this is the primary or leading driver of collapse. This exaggerated claim weakens the motivation.\", \"MISSED CRITICAL PRIOR WORK: Quad (ICLR 2025, arXiv via openreview.net/forum?id=bMC1t7eLRc) proposes clustering-based quality+diversity selection for LLM pretraining using FAISS k-means and influence scoring — a direct competitor the generator does not cite. QuaDMix (arXiv:2504.16511, ICLR 2026 submission, since withdrawn) from ByteDance proposes a unified quality-diversity parameterized selection function for pretraining, also uncited. These papers must be differentiated against.\", \"MECHANISTIC GAP IN CORE CLAIM: The proposal asserts that Voronoi cells with low real-data occupancy in Qwen3-Embedding space correspond to the tail knowledge that top-p/temperature sampling truncates. This mapping is assumed, not established. Token-level probability truncation in a generative model does not directly translate to semantic embedding cluster density. A reviewer will immediately ask for theoretical justification or ablation confirming this correspondence.\", \"COMPUTE CONSTRAINT MISMATCH: The user's hard constraint is ≤200 H100-hours and explicitly specifies 1B–3B models. The proposal adds a 7B model run (~120h A100 ≈ 60 H100-hours) that goes beyond the user's stated scope and partially strains the budget. The 5× ablation runs of 1.3B at 30h A100 each imply ~12B-token training runs, which are far from Chinchilla-optimal and may produce null or noisy tail-coverage signal.\", \"SHORT TRAINING RUN RISK: At the implied token budgets (12–15B tokens for 1.3B models, ~15B for 7B), the models are severely under-trained. Tail-knowledge differences between selection strategies may not manifest reliably at this scale, making the primary evaluation (Wikidata-derived tail probe accuracy) potentially inconclusive.\", \"WIKIDATA TAIL PROBE CONSTRUCTION: The 'rare entity recall' and 'uncommon fact completion' evaluation requires constructing entity-frequency distributions from Wikidata, filtering tail entities from training data, and ensuring no contamination with the Dolma/C4 reference corpus. This pipeline is neither simple nor guaranteed valid — a reviewer will question whether the probe actually tests tail coverage or just benchmark contamination artifacts.\", \"DIFFERENTIATION FROM 'LESS IS MORE' UNDERSTATED: The generator correctly identifies arXiv:2504.14508 as closest concurrent work but claims differentiation by 'not addressing pretraining.' However, the algorithmic overlap is very high — both use embedding space, both use greedy max-coverage, both target synthetic data. A reviewer may see CGS as 'Less is More applied to pretraining with a tail-density threshold' and demand stronger algorithmic differentiation.\"]\nFeedback: The core idea is publishable but needs targeted revision on four fronts before it can reach top-tier bar:\n\n1. FIX REFERENCES AND CLAIMS: Correct the venue of arXiv:2510.00866 (it is not confirmed 'EMNLP 2025'; cite as preprint or ICLR 2026 submission). Soften the claim about 2511.13640: write 'identifies tail knowledge underrepresentation as a systematic distributional discrepancy in synthetic data' rather than 'leading driver of collapse.' These factual errors undermine reviewer trust.\n\n2. DIFFERENTIATE FROM QUAD AND LESS IS MORE: Quad (ICLR 2025) does clustering-based diversity-quality selection for pretraining — you must cite it and clearly explain why CGS (tail-density targeting via Voronoi cells) is fundamentally different from selecting underrepresented clusters. The generator should add a paragraph: 'This idea is too similar to Quad (ICLR 2025, openreview.net/forum?id=bMC1t7eLRc) in using FAISS clustering for pretraining diversity. Differentiation: Quad selects by influence-weighted cluster underrepresentation, not by real-data tail density in Voronoi cells; CGS's criterion is grounded in the CQF failure mechanism specifically for synthetic data.' Similarly, position against Less is More (arXiv:2504.14508) more aggressively: CGS extends the max-coverage idea to pretraining and adds tail-threshold grounding.\n\n3. JUSTIFY OR DROP 7B MODEL: To stay within the user's ≤200 H100-hour constraint and 1B–3B model scope, either (a) drop the 7B run and use a 2.8B model as the 'large' reference point, or (b) argue explicitly that 7B is needed to show the tail-coverage effect is non-trivial at scale and budget ~60 H100-hours for it. The current framing mixes the user's budget constraint with an aspiration for larger scale.\n\n4. VALIDATE THE VORONOI-TAIL CORRESPONDENCE: Add a validation experiment: (a) generate synthetic documents with different top-p values (0.5, 0.85, 0.95) and show that Voronoi cell density in Qwen3-Embedding space correlates with generation temperature/top-p in the expected direction; (b) show that manually selected tail-knowledge documents from Wikidata concentrate in low-occupancy cells. This costs 1–2 GPU-hours but would make the mechanistic claim reviewable. Without this, the core hypothesis is untested.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"TIMELINE CONSTRAINT VIOLATION: The user specifies a hard ≤16-day constraint. Manual mode is estimated at 3-5 months and human-in-loop at 4-6 weeks — both are wildly incompatible. Auto-research mode is 8-12 days for experiments only, leaving ≈4-8 days to write and submit a full research paper. The proposal should either (a) scope itself to auto-research mode as the primary execution path and explicitly acknowledge the paper-writing timeline risk, or (b) treat the 16-day constraint as applying to a 'proof of concept' submission where only Tier 1 results (360M ablations) are reported and Tier 2 is deferred to the camera-ready. As written, the resource estimate table creates an internal inconsistency: the paper claims to target EMNLP 2026 (16 days away) yet describes modes that take months.\", \"MATES (NeurIPS 2024) ABSENT FROM FORMAL LANDSCAPE AND KEY REFERENCES: MATES (arXiv:2406.06046, NeurIPS 2024) trains a small influence model to dynamically select pretraining data, achieving 2× the gains of prior state-of-the-art. This is a directly relevant published baseline for pretraining data selection that the proposal mentions once in passing ('Quad, D4, and MATES baselines') but never formally describes or differentiates in the landscape section. A reviewer will notice this omission immediately. The generator should add MATES to the landscape and key references, noting that CGS requires no influence model training (unlike MATES), which is a concrete practical advantage.\", \"EVALUATION CIRCULARITY IN HELD-OUT LOW-OCCUPANCY PERPLEXITY: The primary evaluation metric uses documents held out from the bottom 20% of reference corpus Voronoi cells as both the training selection criterion AND the evaluation signal. CGS is guaranteed to select synthetic data that covers exactly those cells — so the model trained with CGS learns to predict text statistically similar to those cells' content. The held-out perplexity improvement may reflect this distribution matching rather than genuine acquisition of tail knowledge. An independent external tail benchmark (e.g., LAMA probes, TriviaQA entity-frequency stratification with Wikipedia pageview statistics) should be the primary metric for falsifiability; the held-out low-occupancy perplexity should be demoted to a secondary diagnostic. The TriviaQA head/tail split already exists in the proposal and is the better primary metric — reframe accordingly.\", \"EMBEDDING COMPUTATION BUDGET UNDERESTIMATED: The proposal allocates '~10 H100-hours' for embedding 'a 10B-token reference corpus' plus synthetic candidates described elsewhere as 'hundreds of millions.' Back-of-envelope: Qwen3-Embedding processing 200M synthetic documents at 512 tokens each = 100B tokens; at ~1M tokens/sec on an H100 (optimistic), this is ~28 hours just for the synthetic corpus, separate from the reference corpus embedding. The auto-research mode with 12 grid configurations reuses the same embedding index but the initial build is underestimated. The generator should clarify the exact candidate corpus size (e.g., 'we precompute embeddings for a 50M-document synthetic pool generated by Qwen3-72B') and revise the embedding H100-hour estimate accordingly.\", \"TRAINING MODEL ARCHITECTURE UNSPECIFIED: The proposal trains models from scratch at 360M and 1.3B parameters but never states what architecture, tokenizer, or training codebase is used. Reproducibility requires specifying whether this is a GPT-2/LLaMA-style decoder, what the sequence length is, which optimizer and learning rate schedule, and which codebase (nanoGPT, LitGPT, OLMo, etc.). Without this, the method cannot be replicated. The user's requirements specifically mention 'Pythia, OLMo-1B, Qwen-0.5B/1.8B' as small open models — the proposal should either use one of these (OLMo-1B is Chinchilla-optimal-friendly and has a public codebase) or explicitly justify the choice of a custom architecture.\"]\nFeedback: The Round 1 revision was thorough — all eight original issues have been addressed, and the proposal is substantially stronger. Three targeted fixes will make this submission-ready:\n\n1. RESOLVE THE TIMELINE CONTRADICTION: The paper cannot claim to target a 16-day deadline while describing a 3-5 month execution plan. Pick one of two framings: (A) Auto-research framing — declare upfront that the submission is enabled by automated experimentation (8-12 days GPU wall-clock) and that writing proceeds in parallel; explicitly carve the paper into 'Tier 1 results (guaranteed by submission)' and 'Tier 2 results (best-effort, described as ongoing if not complete).' (B) Scoped-to-Tier-1 framing — submit with 360M ablations only, explicitly position Tier 2 as future work, and argue that the 8-config ablation at Chinchilla-optimal scale is sufficient to support the core CGS claims. Either framing is honest; the current hybrid is not.\n\n2. ADD MATES TO THE LANDSCAPE AND DIFFERENTIATE: Add a paragraph: 'MATES (NeurIPS 2024, arXiv:2406.06046) trains a lightweight influence model that continuously adapts to the evolving pretraining model's data preferences, achieving 2× the gain of prior SOTA. CGS differs on two axes: (a) CGS requires no influence model training — the FAISS IVF index is built once over the fixed reference corpus, not updated per training step; (b) CGS targets a specific failure mode (CQF distribution-matching rather than quality) rather than maximizing generic influence. MATES is computationally intensive and applied to general pretraining data; CGS is a lightweight post-hoc selector for synthetic-real mixing pipelines.' Include MATES as a formal key reference.\n\n3. FIX THE EVALUATION CIRCULARITY: Demote 'held-out low-occupancy perplexity' to a sanity check and promote the TriviaQA head/tail split as the primary falsifiable metric. The held-out ppl measures exactly what CGS was optimized to cover — it's not an independent test. The TriviaQA split uses an external resource (Wikipedia page views) to define head/tail entities, making it independent of the FAISS cell structure. Add this framing explicitly in the evaluation section: 'We use the TriviaQA tail-entity accuracy as the primary test of whether tail coverage translates to downstream knowledge acquisition, since it is defined independently of our FAISS cell structure.'\n\n4. SPECIFY THE TRAINING ARCHITECTURE: Use OLMo-1B architecture (open codebase, publicly documented) scaled down to 360M for Tier 1 and use OLMo-1B directly for Tier 2. This satisfies the user's requirement to use open small models and makes the experiments fully reproducible with a widely-known codebase.\n\n5. CLARIFY EMBEDDING BUDGET: State explicitly the size of the synthetic candidate pool (e.g., '50M documents from Qwen3-72B, 512 tokens avg') and revise the 10H embedding estimate to match. If the candidate pool is larger, embed in streaming batches and update the budget accordingly.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MISSING CRITICAL CONCURRENT WORK — Group-MATES (NeurIPS 2025, arXiv:2502.14709): This paper extends MATES with clustering-based group-level data selection, achieving 3.5–9.4% relative gains and 1.75× token efficiency over state-of-the-art individual selection. It uses embedding-based clustering to partition data into groups and selects within clusters — structurally overlapping with CGS's Voronoi cell approach. The proposal cites MATES (NeurIPS 2024) but not its NeurIPS 2025 successor. A reviewer will notice this immediately. Differentiation: Group-MATES uses influence-weighted group selection without a real-data reference density; CGS specifically targets low-occupancy tail cells defined against a reference corpus and requires no influence model. This should be added to the landscape section.\", \"EVALUATION MISSING USER-REQUIRED DIVERSITY METRICS: The user's hard constraints explicitly list 'diversity metrics (self-BLEU, n-gram entropy)' as required evaluation. The proposal evaluates TriviaQA tail/head accuracy, Head-to-Tail benchmark, standard downstream tasks, and held-out perplexity — but includes no diversity metrics for the selected synthetic data. CGS should demonstrate that its tail-targeted selection produces more diverse text than CQF (which selects fluent head-distribution text). Self-BLEU and n-gram entropy of selected synthetic data are cheap to compute (CPU-only, no GPU required) and would directly substantiate the coverage-vs-classifier-proxy claim.\", \"ICLR 2026 VENUE STATUS OF FOUNDATION PAPER UNCONFIRMED: arXiv:2510.00866 ('The Data-Quality Illusion') is submitted to ICLR 2026 (OpenReview ID: vSBACt34gS, modified February 2026) but its acceptance/rejection decision could not be confirmed via independent search. If this paper was rejected from ICLR 2026, the 'opportunity' narrative built around it ('CQF is shown to be illusory... arXiv:2510.00866') is weakened. The proposal should either (a) confirm the status and cite it accordingly, or (b) hedge: 'arXiv:2510.00866, under review; the empirical finding stands independently of peer review status.' The current citation as 'submitted to ICLR 2026' is ambiguous.\", \"LESS-IS-MORE DIFFERENTIATION NEEDS EXPLICIT STATEMENT: The proposal says CGS 'extends Less is More to pretraining scale with a tail-density threshold,' but a reviewer could ask: why not just run Less is More (arXiv:2504.14508) on the pretraining synthetic candidate pool with tail filtering? The proposal must explicitly state: 'Less is More maximizes coverage of ALL embedding cells uniformly — without a reference-corpus density criterion, it would waste selection budget on head cells already well-covered by real data. CGS adds the critical step of using real-data Voronoi occupancy as a gate: only tail cells (bottom 20–25% by reference occupancy) are eligible for synthetic coverage. This reference-density threshold is the mechanistic link to the CQF failure documented in arXiv:2510.00866, which Less is More does not establish.'\", \"ONLINE-METHOD COMPETITORS NOT ACKNOWLEDGED: ICLR 2026 accepted two online pretraining data curation methods — 'Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods' (ADAPT) and 'AC-ODM: Actor-Critic Online Data Mixing' — that are direct competitors to offline approaches like CGS. A reviewer familiar with ICLR 2026 will ask why CGS (a static offline filter) is preferable to online reweighting. The proposal should add one sentence: 'Online methods like ADAPT and AC-ODM adapt during training but cannot target the specific synthetic-real tail gap documented in arXiv:2510.00866, since they optimize generic influence rather than reference-density-defined tail coverage; CGS is a zero-overhead offline pre-filter compatible with any online method.'\"]\nFeedback: The Round 2 revision was comprehensive — all five prior issues are resolved. Three targeted fixes will make this submission-ready:\n\n1. ADD GROUP-MATES TO LANDSCAPE: Insert a differentiation paragraph after the MATES discussion: 'Group-MATES (NeurIPS 2025, arXiv:2502.14709) extends MATES to group-level selection by clustering training data using relational influence weights and selecting within clusters, achieving 3.5–9.4% gains. CGS differs on three axes: (a) CGS requires no influence model — Voronoi cells are defined by k-means over the fixed reference corpus, not by data-data influence weights; (b) CGS uses reference-corpus density as the selection criterion, not influence; (c) CGS targets the synthetic-real distribution gap specifically — Group-MATES operates within a single corpus without a real-data reference.' Add arXiv:2502.14709 to key_references.\n\n2. ADD DIVERSITY METRICS TO EVALUATION: The user hard-requires self-BLEU and n-gram entropy. Add to the evaluation section: 'Diversity of selected synthetic data: we compute corpus-level self-BLEU (lower = more diverse) and 4-gram entropy (higher = more diverse) over the synthetic subset selected by each method. CGS should show lower self-BLEU and higher n-gram entropy than CQF, since CQF preferentially selects fluent head-distribution text with low lexical diversity. This is computed post-selection on CPU before training begins.' These are zero-GPU-cost and directly substantiate the coverage claim.\n\n3. CLARIFY ICLR 2026 STATUS OF 2510.00866: Search or state that the paper's review status is uncertain and hedge accordingly. Change all references to 'submitted to ICLR 2026 (preprint; peer review status pending)' to avoid implying acceptance or publication. The empirical finding is sound regardless of venue; the paper should be defensible as a preprint citation.\n\n4. Add a single sentence addressing online-method competitors (ADAPT/AC-ODM, ICLR 2026) positioning CGS as a compatible pre-filter rather than a competing paradigm.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"EMBEDDING COMPUTE ARITHMETIC ERROR — BUDGET VIOLATION: The '~36 H100-hours' embedding figure is internally inconsistent with the stated throughput. At 100K tok/s per H100 GPU, embedding 25.6B synthetic tokens alone requires 256,000s = 71 GPU-hours; adding 5B reference tokens adds 14H = 85H total. On 4 GPUs: wall-clock = 21.3H, GPU-hours = 85H — NOT 36H. The '36H / 4 GPUs = 9H wall-clock' arithmetic requires 236K tok/s per GPU, which contradicts the stated 100–150K range. The corrected total budget is ~2H (Exp 0) + ~85H (embedding) + ~72H (Tier 1) + ~88H (Tier 2) + ~2H (eval) = ~249H, exceeding the user's hard ≤200H constraint by ~25%. The generator must either: (a) document a higher throughput (e.g., 250K+ tok/s with optimized large-batch encoding on H100) with citations, (b) reduce the synthetic pool to ~15M documents to bring embedding under 30H, or (c) explicitly scope Tier 2 as unfunded and recompute the budget without it (~161H).\", \"PROXY MODEL RELIABILITY UNADDRESSED: 'Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice' (ICLR 2026 Poster, openreview.net/forum?id=2FZC0c06jP) directly shows that conclusions about data selection quality 'can flip with even minor adjustments to training hyperparameters' when using small proxy models. CGS uses Pythia-410M (Tier 1) to determine the winning selection method before scaling to Pythia-1.4B (Tier 2), without any mention of the recommended reduced learning-rate protocol (10–100× smaller than standard) to ensure transfer reliability. The generator should add one sentence in the Tier 1 training setup: 'To improve reliability of proxy-to-full-scale transfer, we follow the protocol of [ICLR 2026 paper] and run Tier 1 with both standard and 10× reduced learning rates; the winning configuration uses the reduced-LR ranking.'\", \"arXiv:2510.00866 STATUS: This foundational paper ('The Data-Quality Illusion'), upon which the entire 'opportunity' narrative is built, does not appear in any ICLR 2026 accepted paper listing despite having been submitted (OpenReview ID: vSBACt34gS). ICLR 2026 decisions are public as of April 2026. Probable rejection. The proposal correctly hedges as 'preprint; peer review status pending,' but the generator should add a sentence that explicitly acknowledges the opportunity narrative holds independently of peer review: 'The empirical finding that CQF improves downstream task performance via distribution-matching rather than genuine quality improvement is independently reproducible; the CGS method does not depend on arXiv:2510.00866 being published at a venue.'\", \"ABLATION GRID DESCRIPTION INCONSISTENCY: The proposal states '8 configurations: (i) CGS vs. CQF-Wikipedia vs. CQF-FineWebEdu vs. random (4 selection methods); (ii) tail threshold 20th vs. 25th percentile.' But only CGS has a tail threshold — the other three methods have no threshold parameter. Crossing 4 methods × 2 thresholds implies that CQF-Wikipedia, CQF-FineWebEdu, and random are each run twice, which is wasteful and unexplained. The generator should clarify: either the grid is 6 runs (CGS-20th, CGS-25th, CQF-Wikipedia, CQF-FineWebEdu, random, plus one additional baseline) or 5 runs (CGS × 2 + 3 others × 1), not 8.\"]\nFeedback: The proposal has addressed all five Round 3 issues cleanly — Group-MATES differentiation, diversity metrics (self-BLEU/n-gram entropy), 2510.00866 status hedge, Less-is-More explicit differentiation, and ADAPT/AC-ODM positioning are all now handled correctly. The method remains novel and the evaluation design is among the strongest aspects of the proposal. Three targeted fixes will make this submission-ready:\n\n1. FIX EMBEDDING COMPUTE AND REBALANCE BUDGET: The '36H embedding' figure has a verifiable arithmetic error — correct it to ~57–85H depending on throughput, or better, document the actual H100 throughput with optimized large-batch inference (claim a specific number like '~250K tok/s with batch=512 on H100 using flash attention') and show the math. If the corrected embedding budget pushes total over 200H, explicitly drop Tier 2 from the funded scope: 'Tier 2 (1.4B) runs proceed only if embedding completes in under 45H; otherwise Tier 2 is deferred to camera-ready per the proposal's early-stop clause.' This keeps the budget under control without changing the method.\n\n2. ADD PROXY RELIABILITY NOTE: Insert one sentence in the training setup: 'Following the protocol of [ICLR 2026 proxy reliability paper], Tier 1 ablations are run at both standard learning rate (3×10⁻⁴) and a 10× reduced rate (3×10⁻⁵); selection method rankings are determined from the reduced-LR runs for reliable Tier 2 transfer.' This costs zero extra GPU-hours (same runs, different LR) and preempts a reviewer familiar with ICLR 2026 data curation work.\n\n3. CLARIFY ABLATION GRID: Specify that the 8 configurations are: (CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, random) = 5 configurations, OR explain what the 6th–8th configurations are (e.g., additional IVF nlist sensitivity runs). As written, '4 methods × 2 thresholds = 8' implies running non-CGS methods with two threshold values, which is a design error.\n\n4. ADD INDEPENDENT VALIDATION SENTENCE: Add: 'The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status; CGS would be motivated equally if the finding were confirmed by independent replication.'\n\n### Round 5 review\nVerdict: revise\nIssues: [\"UNVERIFIED THROUGHPUT CREATES LATENT BUDGET RISK: ModernBERT-large H100 throughput of 100-150K tokens/sec is unverified. Official ModernBERT benchmarks (Hugging Face blog, arXiv:2412.13663) are on RTX 4090 only, with no absolute throughput numbers published for any hardware. If actual H100 throughput is ~50K tok/s (plausible if 4090 throughput is ~25-35K and H100 ≈ 2× 4090 for encoder inference), total embedding reaches ~70.5 GPU-hours, pushing overall budget to ~208H — 4% over the 200H hard constraint. The proposal should add one of: (a) a citation for the 100-150K figure (e.g., the ModernBERT benchmark table from the full PDF), (b) a one-time throughput benchmark before committing to full embedding ('we benchmark ModernBERT-large throughput in the first 30 minutes of Experiment 0; if throughput < 60K tok/s, the synthetic pool is reduced from 15M to 10M documents, reducing embedding to ~47H and total budget to ~185H'), or (c) an explicit early-stop: 'if embedding does not complete within 45 GPU-hours, Tier 2 is deferred to camera-ready.'\", \"MISSING ICLR 2025 ORAL: ENTIGRAPH (arXiv:2409.07431): Synthetic Continued Pretraining via EntiGraph is the highest-profile prior work on improving tail-knowledge acquisition via synthetic data — it is an ICLR 2025 Oral presentation, directly targeting 'knowledge that appears only once or twice on the internet.' Every EMNLP reviewer familiar with the synthetic data literature will ask about it. The proposal must cite it and differentiate: EntiGraph *generates* new synthetic documents by traversing knowledge graph connections from a structured source corpus, whereas CGS is a *post-hoc selector* applicable to any pre-existing synthetic pool without requiring knowledge graph infrastructure. The approaches are complementary: CGS could in principle select tail-covering subsets of EntiGraph-generated data.\", \"CONCURRENT WORK arXiv:2604.13977 NOT ADDRESSED: 'How Can We Synthesize High-Quality Pretraining Data?' (April 2026) systematically compares synthetic pretraining strategies and finds 'output diversity is the dominant factor for downstream performance, more important than generator size or formatting.' This finding is directly relevant to CGS's claim that diversity (via tail coverage) outperforms classifier-based quality filtering. The proposal should acknowledge this concurrent result as corroborating evidence: if diversity dominates quality proxies, CGS's coverage-based criterion is on the right track. Failure to mention a 2026 result on the exact same topic will attract reviewer questions.\"]\nFeedback: This is the cleanest the proposal has been — all four Round 4 issues are resolved, budget arithmetic is now correct (15M docs / 7.68B tokens / ~175H total), and the evaluation design is strong. Three targeted fixes will resolve the remaining gaps:\n\n1. DOCUMENT MODERNBERT THROUGHPUT OR ADD FALLBACK: Add one sentence in the embedding pipeline description: 'Before committing to full-corpus embedding, we benchmark ModernBERT-large throughput on a 100K-document pilot (~51M tokens); if throughput < 60K tok/s, the synthetic pool is reduced to 10M documents to hold total budget under 185H.' This costs ~5 GPU-minutes and eliminates the budget risk entirely. Alternatively, cite the ModernBERT paper's supplementary Table (if it has H100 numbers) or note that H100 SXM is documented to deliver 2–4× RTX 4090 throughput for transformer inference, placing ModernBERT-large at 80–160K tok/s — cite the H100 whitepaper for the multiplier.\n\n2. ADD ENTIGRAPH ONE-LINER TO RELATED WORK: In the 'Coverage-based fine-tuning' cluster or as a new 'Tail knowledge via synthetic generation' bullet, add: 'EntiGraph (ICLR 2025 Oral, arXiv:2409.07431) generates synthetic continued-pretraining corpora by sampling entity pairs from a knowledge graph and synthesizing text connecting them, improving tail-fact acquisition in domain-specific settings. Unlike CGS, EntiGraph requires a structured knowledge corpus as input and generates new documents; CGS is a post-hoc selector for any pre-existing synthetic pool without knowledge graph infrastructure.' Also add arXiv:2409.07431 to key_references.\n\n3. ACKNOWLEDGE arXiv:2604.13977 AS CORROBORATING EVIDENCE: Add to the 'Synthetic data scale findings' cluster: 'Concurrent work (arXiv:2604.13977, April 2026) finds output diversity to be the dominant factor in synthetic pretraining quality — more impactful than generator size or formatting — providing independent corroboration for CGS's diversity-over-classifier-proxy hypothesis.' This converts a potential reviewer objection into supporting evidence.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"FACTUAL REFERENCE ERROR — arXiv:2512.24503 MISATTRIBUTION: The proposal lists arXiv:2512.24503 as the 'ADAPT: Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods' paper. Independent verification confirms arXiv:2512.24503 is 'Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice' (Wang et al., ICLR 2026 Poster) — the same proxy-model reliability paper the proposal already cites under openreview.net/forum?id=2FZC0c06jP. The proposal now has two different descriptions for the same arXiv ID and no valid arXiv ID for ADAPT. A reviewer who checks references will immediately flag this. Fix: (a) find and use the correct arXiv ID for ADAPT (if it has one), or cite it without an arXiv ID; (b) remove the duplicate arXiv attribution.\", \"MISCHARACTERIZATION OF CORROBORATING PAPER arXiv:2604.13977: The proposal claims arXiv:2604.13977 ('How Can We Synthesize High-Quality Pretraining Data?', April 2026) 'independently finds output diversity to be the dominant factor in synthetic pretraining quality — more important than generator size or formatting consistency.' Independent search finds the paper's dominant factors are structured output formats (tables, math problems, FAQs, tutorials) and rephrasing prompt design — NOT output diversity per se. Structured formats are a specific choice of diversity type, not the same as the diversity-targeting criterion CGS uses. The proposal's framing overstates the corroboration. Fix: replace 'output diversity is the dominant factor' with the paper's actual finding — e.g., 'structured output format and prompt design are dominant factors, outperforming raw scale and format-agnostic generation' — and argue this supports CGS's non-classifier-proxy approach rather than implying direct support for diversity-targeting per se.\", \"UNVERIFIED CLAIM: QuaDMix 'withdrawn from ICLR 2026': The proposal states arXiv:2504.16511 (QuaDMix) was 'withdrawn from ICLR 2026.' Independent search found no evidence of this withdrawal — the paper appears as an active arXiv preprint with no confirmed conference status. If QuaDMix is still under submission or published elsewhere, the phrase 'withdrawn' is factually wrong and weakens the proposal's credibility. Fix: change to 'arXiv preprint; conference status unconfirmed' or omit the venue claim entirely.\", \"UNCITED CONCURRENT WORK — arXiv:2510.02375: 'Pretraining with hierarchical memories: separating long-tail and common knowledge' (October 2025) explicitly addresses tail knowledge acquisition in pretraining via hierarchical parametric memory banks, achieving 2× parameter efficiency. While mechanistically orthogonal to CGS (architectural intervention vs. data selection), an EMNLP reviewer specializing in tail-knowledge acquisition will know this work and may ask why CGS is preferable to architectural solutions. The proposal should add a brief note: 'Architectural methods such as hierarchical memory banks (arXiv:2510.02375) address tail knowledge through model architecture changes rather than data selection; CGS is orthogonal and could complement such architectures by improving the training distribution seen by those memory components.'\"]\nFeedback: The proposal is substantively strong after five rounds of revision — the method is coherent, the budget is realistic, the evaluation avoids circularity, and the differentiation from Quad/MATES/Group-MATES/Less-is-More is now explicit and adequate. Three targeted reference fixes will bring this to submission quality:\n\n1. FIX THE ADAPT arXiv ID: arXiv:2512.24503 is Wang et al.'s proxy-model reliability paper, not ADAPT. Find ADAPT's correct arXiv ID (search 'online reweighting LLM pretraining generalization offline methods 2024 2025') or cite it by conference venue only (ICLR 2026 Workshop DATA-FM) without an arXiv ID. Remove the duplicate attribution.\n\n2. CORRECT THE 2604.13977 CHARACTERIZATION: The paper finds structured formats and rephrasing prompts dominate, not 'output diversity' as a general principle. Write instead: 'Concurrent work (arXiv:2604.13977, April 2026) finds that structured output formats (tables, FAQs, tutorials) and prompt design dominate synthetic pretraining quality — outperforming generator scale and format-agnostic generation — providing external corroboration that principled generation choices matter more than classifier-based selection proxies, consistent with CGS's non-proxy approach.' This still supports CGS without misrepresenting the paper.\n\n3. REMOVE 'WITHDRAWN FROM ICLR 2026' FROM QuaDMix: Change to 'arXiv preprint (arXiv:2504.16511)' and remove the venue claim until verifiable. The differentiation paragraphs are solid and do not depend on QuaDMix being withdrawn.\n\n4. ADD ONE SENTENCE ON arXiv:2510.02375: Under the tail-knowledge section, add the one-sentence orthogonality note recommended above. This converts a potential reviewer gap into a acknowledged scope decision.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"CRITICAL UNCITED NeurIPS 2025 PAPER — EMBEDDING CHOICE DIRECTLY CHALLENGED: arXiv:2502.02494 ('Analyzing Similarity Metrics for Data Selection for Language Model Pretraining,' NeurIPS 2025) explicitly shows that off-the-shelf BERT-style encoders — the class ModernBERT-large belongs to — systematically underperform domain-specific LM token embeddings for pretraining data curation. The paper finds that retrieval-trained and general-purpose encoders fail to capture training dynamics unique to the pretraining setting, and that simple LM token embeddings from same-corpus models outperform all off-the-shelf alternatives. CGS's entire cell structure depends on ModernBERT-large producing semantically meaningful Voronoi partitions for pretraining data coverage — any reviewer familiar with this NeurIPS 2025 result will immediately ask why a potentially misaligned embedding space is used. The proposal must either: (a) distinguish CGS's structural coverage use (cell occupancy mapping) from the quality-proxy prediction task studied in arXiv:2502.02494, arguing the critique does not transfer; or (b) add an Experiment 0 ablation comparing Voronoi cell structure from ModernBERT-large vs. LM token embeddings from a small Pythia model pretrained on Dolma. Without this, the core structural assumption — that ModernBERT cells align with semantically meaningful tail regions — is undermined by a published NeurIPS 2025 result.\", \"OUTDATED CITATION STATUS — arXiv:2510.00866 REJECTED FROM ICLR 2026: The proposal currently says 'peer review status pending' for arXiv:2510.00866 ('The Data-Quality Illusion'). ICLR 2026 final decisions were announced January 22, 2026, and this paper does not appear in any ICLR 2026 accepted paper list, conference proceedings, or outstanding paper announcements. By May 2026 (the current date), this paper has almost certainly been rejected from ICLR 2026. The phrasing 'peer review status pending' is factually incorrect for a decision that was made four months ago. The proposal should update to 'not accepted at ICLR 2026 (preprint)' or 'rejected from ICLR 2026' while retaining the existing hedge that the empirical finding is independently reproducible regardless of venue.\"]\nFeedback: Two targeted fixes are needed — both are scope-limited and do not require new experiments:\n\n1. ADDRESS arXiv:2502.02494 ON EMBEDDING CHOICE: Add the following to the method description or landscape section: 'arXiv:2502.02494 (NeurIPS 2025) shows that off-the-shelf BERT-style encoders underperform domain-specific LM token embeddings when used as quality proxies for pretraining data selection — because retrieval-optimized embeddings do not capture training dynamics specific to pretraining. CGS's use of ModernBERT-large is structurally different: we use embeddings to define a semantic coverage map (Voronoi cell occupancy) over a reference corpus, not to predict model loss or document quality scores. The cell occupancy criterion requires only that semantically similar documents cluster together in embedding space — a property that BERT-style masked LM pretraining is specifically designed to achieve and that Experiment 0(b) validates: if Wikidata long-tail documents significantly concentrate in low-occupancy cells relative to random C4 samples, the embedding partitioning is operationally correct for CGS's purpose regardless of its fitness as a quality proxy.' Also add arXiv:2502.02494 to key_references.\n\n2. UPDATE CITATION STATUS OF arXiv:2510.00866: Change all instances of 'peer review status pending' to 'rejected from ICLR 2026 (preprint).' The existing hedge sentence — 'The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status' — is good and should be retained. A rejected preprint can still motivate a new method if the finding is independently replicable, which the proposal correctly asserts.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-09T21:28:04.087Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-09T21:28:04.087Z",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

## Round 1

64 recorded events

### User

_source line 3 · 2026-05-09T21:28:04.121Z_

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
  "title": "Tail-Coverage-Guided Synthetic Data Selection to Replace Classifier Quality Filtering",
  "core_problem": "Classifier-based quality filtering (CQF), the dominant method for selecting synthetic pretraining data used by GPT-3, LLaMA, and PaLM, is shown to be illusory — it improves downstream task performance not by improving language modeling quality but by implicit distribution-matching rather than genuine quality signals. Concurrently, synthetic data exhibits systematic distributional discrepancies relative to real data: top-p and temperature sampling truncate low-probability continuations, causing rare factual content to be systematically underrepresented in synthetic corpora. Kandpal et al. (ICML 2023) established a direct causal link: LLM accuracy on factual questions correlates strongly with the frequency of the underlying entity in pretraining documents, confirming that tail-knowledge acquisition depends on tail-content exposure during training. No principled selection criterion corrects for this distributional gap: CQF does not target it (and may worsen it by filtering toward fluent head-distribution text), while naïve random sampling inherits the generator's truncation bias wholesale. More recent model-aware selectors such as MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) adapt dynamically to the evolving model's preferences but do not target the specific tail-distribution gap — they optimize for generic influence rather than for correcting truncation-induced underrepresentation.",
  "opportunity": "Three concurrent findings create a gap that demands a new method: (1) 'The Data-Quality Illusion' (arXiv:2510.00866, rejected from ICLR 2026; preprint) demonstrates that CQF does not improve language modeling on held-out high-quality data and argues the field should rethink synthetic data filtering from first principles; (2) 'Data Value in the Age of Scaling' (arXiv:2511.13640) identifies tail-knowledge underrepresentation as a systematic distributional discrepancy in synthetic data under real-synthetic mixing, linked to generative truncation mechanisms; (3) Kandpal et al. (ICML 2023) provides external causal validation: pretraining document frequency is a strong predictor of downstream accuracy on rare facts. Together, these findings establish that (a) CQF is the wrong solution, (b) the actual problem is a distributional gap at the tail, and (c) closing the tail gap causally improves knowledge acquisition. The opportunity is 'Coverage-Guided Sampling' (CGS): select synthetic examples to maximize marginal coverage of low-density regions of the real-data embedding space, directly targeting the distributional gap that CQF fails to address. This is the first synthetic data selector explicitly designed around the mechanism documented in arXiv:2510.00866 rather than a classifier proxy. The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status; CGS would be motivated equally if the finding were confirmed by independent replication. Concurrent work (arXiv:2604.13977, April 2026) finds that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are the dominant factors in synthetic pretraining quality — outperforming both larger generator models and format-agnostic generation strategies — providing external corroboration that principled, non-classifier-based generation and selection choices are the right axis for improving synthetic pretraining data quality, consistent with CGS's reference-density-gated approach.",
  "landscape": "CQF is used by all major pretraining pipelines (GPT-3, LLaMA, PaLM, RedPajama) but arXiv:2510.00866 (rejected from ICLR 2026; preprint) shows its quality signal is misleading. Six clusters of prior work bound the proposal:\n\n**Diversity-quality pretraining selection.** Quad (arXiv:2409.16986, ICLR 2025 Spotlight) is the most important prior work. Quad clusters all pretraining data and uses a Multi-Armed Bandit (MAB) scheme favoring clusters with high influence scores (quality) or low selection frequency (diversity). CGS differs on three axes: (1) Criterion — CGS uses a real-data tail-density threshold (bottom 20–25% by Voronoi cell occupancy in a reference corpus) rather than influence-weighted underrepresentation; CGS does not require influence score computation, which is expensive to scale to billions of synthetic candidates; (2) Target — CGS applies specifically to the synthetic data mixing problem and requires a real-data reference corpus to define 'tail'; Quad operates within a single multi-source corpus without a reference density; (3) Motivation — CGS is grounded in the CQF failure mechanism documented in arXiv:2510.00866. QuaDMix (arXiv:2504.16511, withdrawn from ICLR 2026, openreview.net/forum?id=oLxx7OhAb1) from ByteDance proposes a parameterized quality-diversity sampling function using domain classification for diversity measurement and LightGBM for parameter search. Like Quad, QuaDMix does not target real-data tail density specifically.\n\n**Model-aware selection.** MATES (arXiv:2406.06046, NeurIPS 2024) trains a lightweight BERT-base influence model that continuously adapts to the evolving pretraining model's data preferences, updating every 10,000 steps. MATES achieves 2× the gain of prior SOTA (QuRating) on 410M and 1B models, at 11.5–21.7% computational overhead. CGS differs on three axes: (a) CGS requires no influence model training — the FAISS IVF index is built once over the fixed reference corpus before pretraining begins, versus MATES's periodic BERT-base retraining; (b) CGS requires no reference task definition — MATES's performance varies substantially with reference task choice, a deployment-time burden; (c) CGS targets a specific, mechanistically motivated failure mode (CQF distributional bias) rather than maximizing generic influence scores.\n\nGroup-MATES (arXiv:2502.14709, NeurIPS 2025) extends MATES to group-level selection: it trains a relational data influence model that weights individual sample influence by inter-data relationships, partitions the training corpus into clusters via these relationship weights, and selects within each cluster independently, achieving 3.5–9.4% relative gains and 1.75× token efficiency over individual selection baselines on DCLM at 400M–3B scales across 22 tasks. CGS differs on three axes: (a) CGS requires no influence model — Voronoi cells are defined by k-means over a fixed reference corpus embedding, not by data-data relational influence weights, making CGS zero-overhead relative to training; (b) CGS uses reference-corpus occupancy density as the selection gate — only tail cells (bottom 20–25% by reference occupancy) are eligible for synthetic coverage — rather than influence-weighted within-cluster scoring; (c) CGS targets the specific synthetic-real distributional gap documented in arXiv:2511.13640: it applies to a fixed synthetic candidate pool relative to a real-data reference corpus, whereas Group-MATES operates within a single training corpus without a reference density criterion.\n\n**Tail knowledge via synthetic generation.** EntiGraph (arXiv:2409.07431, ICLR 2025 Oral) addresses tail-knowledge acquisition through synthetic document generation: given a small domain corpus, it extracts salient entities, constructs a knowledge graph dynamically from entity-pair relationships via LM-driven synthesis, and generates new documents traversing those relationships — improving tail-fact retention in continued pretraining. Unlike CGS, EntiGraph is a generative method that requires a structured source corpus as input to drive entity extraction; it produces entirely new documents rather than selecting from a pre-existing pool, and is evaluated on domain-specific continued pretraining (QuALITY benchmark) rather than open-domain general pretraining. The approaches are orthogonal and complementary: CGS could select tail-covering subsets of an EntiGraph-generated corpus, concentrating the EntiGraph generation budget on the regions of real-data embedding space already underrepresented.\n\n**Architectural approaches to tail knowledge.** 'Pretraining with Hierarchical Memories: Separating Long-Tail and Common Knowledge' (arXiv:2510.02375, October 2025) addresses tail knowledge acquisition through model architecture changes rather than data selection: it introduces hierarchical parametric memory banks alongside a smaller core model, storing long-tail world knowledge in memory parameters while the core model captures common knowledge and general reasoning, with a 160M-parameter model plus 18M-parameter memory (fetched from a 4.6B bank) achieving performance comparable to a standard model with more than 2× the parameters. This architectural intervention is orthogonal to CGS: CGS improves the training distribution presented to any model architecture, and could complement hierarchical memory architectures by ensuring the training data seen by those memory components better covers tail-content regions.\n\n**Coverage-based fine-tuning.** 'Less is More: Adaptive Coverage for Synthetic Training Data' (arXiv:2504.14508, 2025) applies a greedy maximum-coverage objective to select synthetic fine-tuning data for NLP classifiers. CGS shares the max-coverage algorithmic skeleton but differs critically in three respects: (1) 'Less is More' maximizes coverage of ALL embedding cells uniformly — without a reference-corpus density criterion, it would waste selection budget on head cells already well-covered by real data, failing to address the distributional gap that CQF leaves open; CGS adds the critical step of using real-data Voronoi occupancy as a gate: only tail cells (bottom 20–25% by reference occupancy) are eligible, ensuring the entire selection budget is concentrated on underrepresented regions; (2) CGS applies at pretraining scale (hundreds of millions of candidates), requiring FAISS IVF for tractability; (3) this reference-density threshold is the mechanistic link to the CQF failure documented in arXiv:2510.00866, which 'Less is More' does not establish.\n\n**Embedding suitability for pretraining data curation.** 'Analyzing Similarity Metrics for Data Selection for Language Model Pretraining' (arXiv:2502.02494, NeurIPS 2025) systematically evaluates off-the-shelf BERT-style encoders (USE, Gecko, BERT) against specialized LM token embeddings for two tasks: (1) predicting pretraining loss differences between documents (quality-proxy use), and (2) within-corpus diversity curation via cluster-based redundancy reduction. The paper finds that off-the-shelf models underperform for both tasks, with the gap being largest for loss prediction and meaningfully smaller for diversity curation — 'LM Token Embeds performs comparably to Gecko, while outperforming all other off-the-shelf embeddings' in the diversification setting. CGS's use of ModernBERT-large is structurally distinct from both evaluated tasks on three axes: (a) CGS does not use embeddings to predict document quality or model loss — it uses them to partition semantic space into Voronoi cells and measure real-data occupancy, a coverage-mapping task not evaluated in arXiv:2502.02494; (b) CGS's selection criterion operates across two corpora (synthetic candidate pool versus a real-data reference corpus), targeting cross-corpus density gaps rather than within-corpus redundancy reduction — the only application arXiv:2502.02494's diversity experiments address; (c) the validity of ModernBERT-large for CGS's specific structural purpose is directly tested by Experiment 0(b): if Wikidata long-tail documents significantly cluster in low-occupancy Voronoi cells relative to random C4 samples, the embedding partition is operationally correct for CGS regardless of its fitness as a pretraining loss predictor. As a robustness check, Experiment 0 includes a CPU-only comparison: Pythia-410M LM token embeddings (embedding matrix row-averages over document tokens, no forward pass required, per arXiv:2502.02494's construction) are used to build a parallel FAISS IVF index; if both ModernBERT-large and Pythia LM token embeddings agree on which Wikidata long-tail documents cluster in low-occupancy cells, the coverage mapping is robust to embedding choice; if they disagree systematically, we fall back to Pythia LM token embeddings for all downstream experiments, consistent with arXiv:2502.02494's recommendation.\n\n**Online pretraining data curation.** ADAPT ('Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods', Zhao et al., ICLR 2026 Workshop DATA-FM, openreview.net/forum?id=zgn3P31NWf) and AC-ODM ('Actor-Critic Online Data Mixing', arXiv:2505.23878, preprint) represent an online paradigm: rather than pre-filtering the candidate pool, they dynamically reweight or re-mix training samples during training based on loss signals. CGS is orthogonal and compatible: as a static offline pre-filter, it reduces the synthetic candidate pool to tail-coverage-optimal documents before training begins with zero ongoing overhead; an online reweighter can further adapt the mix at training time after CGS has already narrowed the pool. Neither ADAPT nor AC-ODM targets the specific synthetic-real tail-density gap documented in arXiv:2510.00866 — they optimize generic influence or domain balance, not reference-density-defined tail coverage.\n\n**Synthetic data scale findings.** 'Demystifying Synthetic Data in LLM Pre-training' (arXiv:2510.01631, EMNLP 2025) finds ~30% rephrased synthetic data is empirically optimal but provides no mechanistic filter. arXiv:2511.13640 characterizes three-phase scaling behavior under real-synthetic mixing and identifies tail underrepresentation as a systematic discrepancy without a selection remedy. Concurrent work arXiv:2604.13977 ('How Can We Synthesize High-Quality Pretraining Data?', April 2026) systematically compares synthetic pretraining strategies across generator models and formats, finding that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are dominant factors in synthetic pretraining quality — outperforming both larger generator models and format-agnostic generation strategies. This provides independent corroboration for CGS's non-classifier-proxy approach: if principled generation choices outperform raw scale and classifier-based proxies, the right axis to optimize is how data is selected and structured rather than whether a quality classifier endorses it.\n\n**Tail knowledge evaluation and deduplication.** Kandpal et al. (arXiv:2211.08411, ICML 2023) establish that LLM accuracy on factual questions correlates causally with pretraining document frequency, providing the empirical foundation for CGS's tail-coverage hypothesis. 'Head-to-Tail' (arXiv:2308.10168, NAACL 2024) provides a purpose-built 18K QA benchmark explicitly stratified into head, torso, and tail facts by knowledge graph frequency — an independent evaluation resource for CGS. D4 (NeurIPS 2023) uses FAISS k-means for deduplication/diversification via distance-to-centroid pruning; it applies a distance heuristic not a tail-density threshold and does not target the synthetic selection sub-problem.",
  "approach": "Coverage-Guided Sampling (CGS) selects synthetic pretraining data by maximizing coverage of underrepresented tail regions in real-data embedding space.\n\n**Method.** We embed a reference corpus (5B-token stratified sample of Dolma, preserving domain balance) and all candidate synthetic documents using ModernBERT-large, then build a FAISS IVF index over the real-data embeddings. The resulting Voronoi cell structure partitions semantic space; 'tail cells' are defined as cells in the bottom 20–25% by real-data occupancy. CGS then greedily selects synthetic documents maximizing marginal coverage of tail cells via a streaming maximum-coverage subproblem — no quality classifier training required. ModernBERT-large is chosen for embedding over larger alternatives due to its superior throughput: the official ModernBERT benchmark documents ~52K tokens/sec for ModernBERT-large on RTX 4090 (arXiv:2412.13663); H100 SXM delivers 2–4× RTX 4090 throughput for encoder inference (NVIDIA H100 Tensor Core GPU product brief), placing ModernBERT-large at ~100–200K tok/s on H100 — versus ~15–30K for Qwen3-Embedding-8B. To verify this before committing to full-corpus embedding, we run a 100K-document throughput pilot (~51M tokens, ~5 GPU-minutes) at the start of Experiment 0; if measured throughput is below 60K tok/s, the synthetic pool is reduced from 15M to 10M documents (7.68B → 5.12B tokens), reducing total embedding to ~47H and holding overall budget under 185H. Embedding quality is validated in Experiment 0. arXiv:2502.02494 (NeurIPS 2025) finds that off-the-shelf BERT-style encoders underperform LM token embeddings for pretraining data curation when used as quality proxies or for within-corpus diversity; CGS uses ModernBERT-large for cross-corpus coverage mapping (Voronoi cell occupancy relative to a reference corpus), a structurally distinct task, with operational validity confirmed by Experiment 0(b) and robustness-checked against Pythia LM token embeddings in Experiment 0(c).\n\n**Mechanistic validation experiment (Experiment 0, ~2 H100-hours).** Before committing to training runs, we validate the core empirical hypothesis: (a) Generate three synthetic corpora of 10M tokens each using Qwen3-72B with top-p ∈ {0.5, 0.85, 0.95}; embed and assign each document to a Voronoi cell; measure whether lower top-p concentrates documents in higher-occupancy cells (expected: yes, since low top-p collapses to high-probability continuations); (b) Embed 5,000 Wikidata long-tail documents (entities appearing <100 times in C4) and confirm they cluster significantly more in low-occupancy cells than a random C4 sample. (c) As a CPU-only embedding robustness check (zero GPU cost): build a parallel FAISS IVF index using Pythia-410M LM token embeddings (row-averages over the token embedding matrix for each document, no model forward pass required) for 50,000 Wikidata long-tail documents and 50,000 random C4 samples; if the low-occupancy cell assignments from ModernBERT-large and Pythia LM token embeddings agree on ≥85% of Wikidata long-tail documents, ModernBERT-large is confirmed as operationally valid for CGS's coverage mapping; if agreement falls below 85%, all subsequent experiments use Pythia LM token embeddings for Voronoi cell construction. If (a) shows r < 0.3 between top-p and mean cell occupancy, or (b) shows no significant enrichment, halt before Tier 1 and revise the tail-density criterion. If (c) shows below-85% agreement between ModernBERT and Pythia LM token embeddings, switch to Pythia LM token embeddings before proceeding to full embedding (zero additional GPU cost).\n\n**Model architecture and training.** Following the precedent of MATES (NeurIPS 2024), Quad (ICLR 2025), and D4 (NeurIPS 2023), we use the Pythia model family (EleutherAI GPT-NeoX codebase) for full reproducibility:\n- *Tier 1 — Systematic ablation: Pythia-410M* (24 layers, hidden dim 1024, 16 heads, 2048 sequence length; ~8B tokens, Chinchilla-optimal). AdamW optimizer with β1=0.9, β2=0.95, weight decay 0.1; cosine LR schedule with 1% warmup steps. Following Wang et al. ('Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice,' ICLR 2026 Poster), all Tier 1 ablations use a 10× reduced peak learning rate of 3×10⁻⁵ (instead of the standard 3×10⁻⁴) to ensure selection method rankings derived from the 410M proxy runs transfer reliably to Tier 2 at 1.4B scale — this costs no additional GPU-hours since the reduced-LR runs replace rather than supplement standard-LR runs. Batch size ~2M tokens. 5 configurations: CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, and random baseline. Only CGS has a tail-threshold parameter; the three non-CGS methods run once without threshold variation. Each run: ~9 H100-hours on 1 GPU.\n- *Tier 2 — Scaling check: Pythia-1.4B* (24 layers, hidden dim 2048, 16 heads, 2048 sequence length; 10B tokens). Same optimizer family with peak LR 2×10⁻⁴. 2 configurations: best CGS from Tier 1 vs. CQF-FineWebEdu. Each run: ~44 H100-hours (4 GPUs × ~11h wall-clock via data parallelism). Using Pythia-1.4B (not 1.3B) ensures exact architecture reproducibility with the published model family.\n\n**Synthetic candidate pool.** We precompute embeddings for a fixed 15M-document synthetic pool generated by Qwen3-72B (top-p=0.9, temperature=1.0, avg 512 tokens/document = 7.68B tokens total). At 100K tokens/sec per H100 (nominal): the 7.68B synthetic tokens require 76,800s ≈ 21.3 GPU-hours; the 5B-token reference corpus requires 50,000s ≈ 13.9 GPU-hours; total embedding ≈ 35 GPU-hours ≈ 8.8H wall-clock on 4 GPUs. Under the throughput fallback (10M docs, ~5.12B tokens), embedding reduces to ~19H + 13.9H ≈ 33H for synthetic + reference ≈ 47H total. This pool size provides ample selection diversity: 7.68B tokens exceeds the synthetic allocation for both Tier 1 (~2.4B tokens at 30% synthetic) and Tier 2 (~3B tokens at 30% synthetic) by over 2.5×. FAISS IVF build is CPU-bound (~2h on 32 cores) and runs concurrently with early embedding steps.\n\n**IVF nlist calibration.** nlist ≈ sqrt(N_reference_docs) per FAISS best practices. Tier 1 pilots probe two nlist settings (±30%) to confirm tail cell occupancy is well-separated; this is CPU-only analysis on the pre-built index (zero GPU cost). If cell structure is degenerate, we correct before the Tier 2 run.\n\n**Evaluation — primary, secondary, and diversity metrics.** The evaluation design explicitly separates the training criterion (FAISS cell coverage) from the test signal to avoid circularity:\n\n(1) *Primary — TriviaQA head/tail accuracy split (independent external metric)*: Using Wikipedia page-view statistics to stratify TriviaQA questions into head entities (top 20% by views, ~1K questions) and tail entities (bottom 20%, ~1K questions), we measure accuracy separately. This stratification uses an external resource (Wikipedia traffic data) wholly independent of the FAISS cell structure. Per Kandpal et al. (ICML 2023), tail-entity accuracy is the most causally meaningful test of whether tail coverage translates to knowledge acquisition. We report the tail/head accuracy ratio as the primary CGS-vs-CQF gap metric.\n\n(2) *Additional independent benchmark — Head-to-Tail (NAACL 2024)*: This purpose-built 18K QA benchmark stratifies facts into head, torso, and tail by knowledge graph frequency (Wikidata). It provides a second external validation of tail knowledge independent of both FAISS and Wikipedia pageviews, strengthening the falsifiability of the tail-coverage claim.\n\n(3) *Secondary — Standard downstream benchmarks*: HellaSwag, WinoGrande, ARC-E/C, PIQA — required for comparability with Quad, D4, MATES, Group-MATES, and CQF baselines. CGS should match or exceed CQF on these benchmarks; failure here would indicate coverage-only selection sacrifices head-distribution capabilities.\n\n(4) *Diversity of selected synthetic data (CPU-only, zero GPU cost)*: We compute corpus-level self-BLEU (Zhu et al., 2018; lower = more diverse) and 4-gram entropy (higher = more diverse) over the synthetic subset selected by each method (CGS, CQF-Wikipedia, CQF-FineWebEdu, random). These metrics are computed post-selection before training begins. CGS should exhibit lower self-BLEU and higher n-gram entropy than CQF-selected data, since CQF preferentially selects fluent head-distribution text with low lexical diversity. This directly substantiates the coverage-vs-classifier-proxy claim: not only does CGS target underrepresented semantic regions, but the selected text should be measurably more lexically diverse than CQF output — consistent with the concurrent finding (arXiv:2604.13977) that principled generation choices (structured formats, prompt design) outperform classifier-based proxies in synthetic pretraining quality.\n\n(5) *Diagnostic — Held-out low-occupancy perplexity*: 5% of reference corpus documents from the bottom 20% occupancy cells are held out before training and used to measure model perplexity. This metric is demoted to a sanity check because CGS is explicitly optimized to cover exactly those cells — perplexity improvement here confirms distribution matching, not necessarily genuine knowledge acquisition. It is reported alongside (1) and (2) but not used as a primary falsifiability claim.\n\n**Falsifiable primary claim**: CGS achieves higher TriviaQA tail-entity accuracy than CQF while matching CQF on standard downstream benchmarks, directly operationalizing the quality-vs-coverage paradox documented in arXiv:2510.00866. The diversity metrics (self-BLEU, n-gram entropy) provide a secondary mechanistic check confirming that CGS's tail-coverage selection is not collapsing to a high-fluency, low-diversity subset.\n\n**Timeline and execution mode.** Given the EMNLP 2026 ARR deadline of May 25, 2026 (16 days from proposal date), the primary execution path is auto-research mode. GPU wall-clock with 4× H100: Experiment 0 (~2h, including 5-min throughput pilot) → Embedding (~8.8h, 4 GPUs, or ~5.8h under 10M-doc fallback) → FAISS build (~2h CPU concurrent) → Tier 1 ablation grid (~18h, 4 experiments in parallel in batch 1, then 1 remaining) → Tier 2 scaling check (~22h, 2 sequential runs with 4-GPU data parallelism). Total GPU wall-clock: ~50.8 hours (~2.1 days) nominal; ~48.8h under fallback. Paper writing begins in parallel on day 1; Tier 1 results are guaranteed by day 4; Tier 2 results are best-effort. If Tier 2 runs do not complete before submission, the 1.4B experiments are described as ongoing and submitted to camera-ready.",
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
    "The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining (arXiv:2510.00866, rejected from ICLR 2026; preprint)",
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
    "ModernBERT: Smarter, Better, Faster, Longer (arXiv:2412.13663, 2024)",
    "Analyzing Similarity Metrics for Data Selection for Language Model Pretraining (arXiv:2502.02494, NeurIPS 2025)"
  ],
  "description": "Classifier-based quality filtering (CQF) — the dominant synthetic pretraining selector used by GPT-3, LLaMA, and PaLM — has been shown to boost downstream task scores via implicit distribution-matching rather than genuine quality improvement (arXiv:2510.00866, rejected from ICLR 2026; preprint; independently reproducible from first principles regardless of venue outcome). Concurrently, Kandpal et al. (ICML 2023) established that LLM accuracy on rare facts causally correlates with pretraining document frequency, confirming that tail-content exposure drives tail-knowledge acquisition; arXiv:2511.13640 documents systematic tail underrepresentation in synthetic data via top-p/temperature truncation; and concurrent work arXiv:2604.13977 (April 2026) finds that structured output formats (tables, math problems, FAQs, and tutorials) and rephrasing prompt design are dominant factors in synthetic pretraining quality — outperforming generator scale and format-agnostic generation — providing external corroboration that principled generation choices matter more than classifier-based proxies, consistent with CGS's non-proxy-based selection criterion. This project proposes Coverage-Guided Sampling (CGS), the first principled pretraining data selector grounded in the actual distributional failure mechanism of CQF. CGS embeds a 5B-token reference corpus and a fixed 15M-document synthetic candidate pool (7.68B tokens) using ModernBERT-large — whose official benchmark documents ~52K tokens/sec on RTX 4090 (arXiv:2412.13663); H100 SXM delivers 2–4× RTX 4090 throughput for encoder inference (NVIDIA H100 product brief), placing it at ~100–200K tok/s. arXiv:2502.02494 (NeurIPS 2025) finds that off-the-shelf BERT-style encoders underperform LM token embeddings for pretraining data quality prediction and within-corpus diversity, but the performance gap is smaller for diversity tasks than loss prediction; CGS's cross-corpus coverage-mapping use (Voronoi cell occupancy relative to a reference corpus) is structurally distinct from both evaluated tasks and validated empirically via Experiment 0(b)/(c). A 100K-document throughput pilot (~5 GPU-minutes) at the start of Experiment 0 verifies throughput before committing to full-corpus embedding; if measured throughput is below 60K tok/s, the synthetic pool is reduced from 15M to 10M documents, holding total budget under 185H. Total embedding ≈ 35 GPU-hours nominal (7.68B synthetic tokens ÷ 100K tok/s = 21.3H + 5B reference ÷ 100K tok/s = 13.9H ≈ 8.8H wall-clock on 4 GPUs). CGS builds a FAISS IVF index over the real corpus, identifies low-density Voronoi 'tail cells' (bottom 20–25% by occupancy), and greedily selects synthetic documents maximizing marginal tail-region coverage — no classifier training required. A mandatory Mechanistic Validation Experiment (~2 H100-hours, inclusive of throughput pilot) confirms that Voronoi cell density correlates with top-p sampling behavior and that ModernBERT-large partitions are operationally valid (or falls back to Pythia LM token embeddings) before committing to training runs. We train using the Pythia model family: Tier 1 uses Pythia-410M at Chinchilla-optimal scale (~8B tokens, 5 ablation configurations, ~45 H100-hours) with the 10× reduced peak LR (3×10⁻⁵) recommended by Wang et al. (ICLR 2026 Poster) for proxy-to-full-scale ranking reliability; Tier 2 uses Pythia-1.4B at 10B tokens (2 configurations, ~88 H100-hours); total budget ~175 H100-hours nominal, ≤185H under fallback. Evaluation resolves circularity: TriviaQA tail-entity accuracy (stratified by Wikipedia pageviews, independent of FAISS) and the Head-to-Tail benchmark (NAACL 2024) are primary falsifiability metrics; corpus-level self-BLEU and 4-gram entropy over selected synthetic data are computed CPU-only post-selection to confirm CGS produces more diverse output than CQF. Closest prior work: EntiGraph (ICLR 2025 Oral, arXiv:2409.07431) generates new synthetic documents by traversing entity relationships in a source corpus — CGS is a post-hoc selector for any pre-existing synthetic pool without generative infrastructure, and the approaches are complementary. Architectural methods such as hierarchical memory banks (arXiv:2510.02375) address tail knowledge through model architecture changes rather than data selection; CGS is orthogonal and could complement such architectures by improving the training distribution seen by those memory components. Quad (ICLR 2025) uses influence-weighted cluster MAB — CGS requires no influence scoring. MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) train influence models — CGS builds its FAISS index once with zero ongoing overhead and no reference task dependency. 'Less is More' maximizes uniform coverage of all cells — CGS adds a real-data reference-density gate (bottom 20–25% occupancy only). Online methods ADAPT (ICLR 2026 Workshop DATA-FM) and AC-ODM reweight during training — CGS is a compatible offline pre-filter. Primary execution path: auto-research mode (4× H100, ~2.1 days GPU wall-clock, paper writing in parallel), targeting EMNLP 2026 ARR deadline May 25, 2026, with Tier 1 results guaranteed at submission.",
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

### Round 7 review
Verdict: revise
Issues: ["CRITICAL UNCITED NeurIPS 2025 PAPER — EMBEDDING CHOICE DIRECTLY CHALLENGED: arXiv:2502.02494 ('Analyzing Similarity Metrics for Data Selection for Language Model Pretraining,' NeurIPS 2025) explicitly shows that off-the-shelf BERT-style encoders — the class ModernBERT-large belongs to — systematically underperform domain-specific LM token embeddings for pretraining data curation. The paper finds that retrieval-trained and general-purpose encoders fail to capture training dynamics unique to the pretraining setting, and that simple LM token embeddings from same-corpus models outperform all off-the-shelf alternatives. CGS's entire cell structure depends on ModernBERT-large producing semantically meaningful Voronoi partitions for pretraining data coverage — any reviewer familiar with this NeurIPS 2025 result will immediately ask why a potentially misaligned embedding space is used. The proposal must either: (a) distinguish CGS's structural coverage use (cell occupancy mapping) from the quality-proxy prediction task studied in arXiv:2502.02494, arguing the critique does not transfer; or (b) add an Experiment 0 ablation comparing Voronoi cell structure from ModernBERT-large vs. LM token embeddings from a small Pythia model pretrained on Dolma. Without this, the core structural assumption — that ModernBERT cells align with semantically meaningful tail regions — is undermined by a published NeurIPS 2025 result.", "OUTDATED CITATION STATUS — arXiv:2510.00866 REJECTED FROM ICLR 2026: The proposal currently says 'peer review status pending' for arXiv:2510.00866 ('The Data-Quality Illusion'). ICLR 2026 final decisions were announced January 22, 2026, and this paper does not appear in any ICLR 2026 accepted paper list, conference proceedings, or outstanding paper announcements. By May 2026 (the current date), this paper has almost certainly been rejected from ICLR 2026. The phrasing 'peer review status pending' is factually incorrect for a decision that was made four months ago. The proposal should update to 'not accepted at ICLR 2026 (preprint)' or 'rejected from ICLR 2026' while retaining the existing hedge that the empirical finding is independently reproducible regardless of venue."]
Feedback: Two targeted fixes are needed — both are scope-limited and do not require new experiments:

1. ADDRESS arXiv:2502.02494 ON EMBEDDING CHOICE: Add the following to the method description or landscape section: 'arXiv:2502.02494 (NeurIPS 2025) shows that off-the-shelf BERT-style encoders underperform domain-specific LM token embeddings when used as quality proxies for pretraining data selection — because retrieval-optimized embeddings do not capture training dynamics specific to pretraining. CGS's use of ModernBERT-large is structurally different: we use embeddings to define a semantic coverage map (Voronoi cell occupancy) over a reference corpus, not to predict model loss or document quality scores. The cell occupancy criterion requires only that semantically similar documents cluster together in embedding space — a property that BERT-style masked LM pretraining is specifically designed to achieve and that Experiment 0(b) validates: if Wikidata long-tail documents significantly concentrate in low-occupancy cells relative to random C4 samples, the embedding partitioning is operationally correct for CGS's purpose regardless of its fitness as a quality proxy.' Also add arXiv:2502.02494 to key_references.

2. UPDATE CITATION STATUS OF arXiv:2510.00866: Change all instances of 'peer review status pending' to 'rejected from ICLR 2026 (preprint).' The existing hedge sentence — 'The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status' — is good and should be retained. A rejected preprint can still motivate a new method if the finding is independently replicable, which the proposal correctly asserts.


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
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "b4a754d3-5995-4c52-b064-385ef6aa6243",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-09T21:28:04.117Z_

```json
{
  "parentUuid": "b4a754d3-5995-4c52-b064-385ef6aa6243",
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
  "uuid": "e458a469-e640-40b2-a8fc-5cddc46241ec",
  "timestamp": "2026-05-09T21:28:04.117Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-09T21:28:04.117Z_

```json
{
  "parentUuid": "e458a469-e640-40b2-a8fc-5cddc46241ec",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a6af973a-4e7f-4696-8a14-8d4c50d1db04",
  "timestamp": "2026-05-09T21:28:04.117Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
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
  "leafUuid": "a6af973a-4e7f-4696-8a14-8d4c50d1db04",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 8: Coverage-Guided Synthetic Data Selection",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

### Assistant

_source line 8 · 2026-05-09T21:28:33.712Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this carefully. This is round 8/10 of an adversarial review. I need to:

1. Independently verify the claims in this proposal via WebSearch
2. Check if the Round 7 issues have been addressed
3. Find any new issues I haven't caught before
4. Issue a verdict

Let me first understand what Round 7 issues were:
1. CRITICAL UNCITED NeurIPS 2025 PAPER — arXiv:2502.02494 on embedding choice directly challenged


2. OUTDATED CITATION STATUS — arXiv:2510.00866 REJECTED FROM ICLR 2026

Looking at the current proposal (Round 8), I can see both issues appear to have been addressed. The proposal now includes an extensive discussion of arXiv:2502.02494 in the landscape section, explaining how CGS's use of ModernBERT-large differs structurally from the quality-proxy prediction task in that paper, and they've added a CPU-only robustness check comparing ModernBERT-large against Pythia LM token embeddings. For the second issue, the proposal now explicitly acknowledges that arXiv:2510.00866 was rejected from ICLR 2026.

Now I need to verify the remaining claims independently. Let me search for the QuaDMix withdrawal status, check if AC-ODM (arXiv:2505.23878) actually exists, look for any concurrent work, verify the ModernBERT throughput claims, confirm the ADAPT reference, and see if there are any new issues I should flag.

Looking at the landscape section more carefully, I'm seeing the proposal still claims QuaDMix was withdrawn from ICLR 2026, and I need to verify whether that's actually true along with checking the existence and accuracy of several other cited papers. I'm noticing that QuaDMix still has the "withdrawn from ICLR 2026" claim in Round 8, even though Round 6 feedback explicitly flagged this as unverified and requested its removal. This is a persistent issue that wasn't addressed in the revision. Let me dig deeper into what other problems might be lurking in this proposal. I need to verify these key claims independently—let me search for the QuaDMix withdrawal status, check if AC-ODM actually exists, confirm the ModernBERT throughput figures, and see what concurrent work on synthetic data selection has emerged recently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6af973a-4e7f-4696-8a14-8d4c50d1db04",
  "isSidechain": false,
  "requestId": "req_011CashpJpVAeHgy31xF39KZ",
  "type": "assistant",
  "uuid": "61a8d893-6278-471d-b6bc-9ee2a7d3debc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RNLiQBesfPkRBdAYXz9oTC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30201,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30201,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1585,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 30201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30201
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

_source line 9 · 2026-05-09T21:28:33.714Z_

I'll conduct independent verification searches to assess whether Round 7 issues were properly resolved and find any remaining problems before issuing a verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61a8d893-6278-471d-b6bc-9ee2a7d3debc",
  "isSidechain": false,
  "requestId": "req_011CashpJpVAeHgy31xF39KZ",
  "type": "assistant",
  "uuid": "e9853720-805a-4ecb-8a7e-bcd86c8d9bbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RNLiQBesfPkRBdAYXz9oTC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30201,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30201,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1585,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 30201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30201
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

_source line 10 · 2026-05-09T21:28:33.733Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CnPArY44H7uJwYwXFpYRba`</summary>

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
  "parentUuid": "e9853720-805a-4ecb-8a7e-bcd86c8d9bbf",
  "isSidechain": false,
  "requestId": "req_011CashpJpVAeHgy31xF39KZ",
  "type": "assistant",
  "uuid": "c04f8e24-4fea-4cc3-89ea-71c01c61eb4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RNLiQBesfPkRBdAYXz9oTC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30201,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30201,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1585,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 30201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30201
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

_source line 11 · 2026-05-09T21:28:33.743Z_

<details><summary>↩ Tool result · `toolu_01CnPArY44H7uJwYwXFpYRba`</summary>

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
  "parentUuid": "c04f8e24-4fea-4cc3-89ea-71c01c61eb4d",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "958f8408-d98d-4489-a398-10f2bd8ee802",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "c04f8e24-4fea-4cc3-89ea-71c01c61eb4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-09T21:28:35.600Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct independent verification searches in parallel to assess the Round 8 proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "958f8408-d98d-4489-a398-10f2bd8ee802",
  "isSidechain": false,
  "requestId": "req_011CashrVfQYWgfZQUSoDcr5",
  "type": "assistant",
  "uuid": "5442cc38-7f7e-4afa-829b-6d22b9e6550c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ub4zstKno3zCMqoEZk1ydk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 41832,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 250,
          "cache_read_input_tokens": 41832,
          "cache_creation_input_tokens": 2604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2604
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

_source line 13 · 2026-05-09T21:28:36.113Z_

Now I'll run independent verification searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5442cc38-7f7e-4afa-829b-6d22b9e6550c",
  "isSidechain": false,
  "requestId": "req_011CashrVfQYWgfZQUSoDcr5",
  "type": "assistant",
  "uuid": "cf78599c-4828-44e2-9425-2f6e80251d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ub4zstKno3zCMqoEZk1ydk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 41832,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 250,
          "cache_read_input_tokens": 41832,
          "cache_creation_input_tokens": 2604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2604
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

_source line 14 · 2026-05-09T21:28:36.967Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MxPsDZ1xifr59GYhRjTHeG`</summary>

```json
{
  "query": "QuaDMix arXiv 2504.16511 ICLR 2026 withdrawn status ByteDance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf78599c-4828-44e2-9425-2f6e80251d5b",
  "isSidechain": false,
  "requestId": "req_011CashrVfQYWgfZQUSoDcr5",
  "type": "assistant",
  "uuid": "4552d4ee-bc57-4a3c-aa41-48098fd9f869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ub4zstKno3zCMqoEZk1ydk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 41832,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 250,
          "cache_read_input_tokens": 41832,
          "cache_creation_input_tokens": 2604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2604
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

_source line 15 · 2026-05-09T21:28:38.251Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VpUwDAjE7MVLeeAb8SsZak`</summary>

```json
{
  "query": "AC-ODM Actor-Critic Online Data Mixing arXiv 2505.23878 LLM pretraining"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4552d4ee-bc57-4a3c-aa41-48098fd9f869",
  "isSidechain": false,
  "requestId": "req_011CashrVfQYWgfZQUSoDcr5",
  "type": "assistant",
  "uuid": "fbe83969-9162-4b61-abaf-9d7d0b52f68f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ub4zstKno3zCMqoEZk1ydk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 41832,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 250,
          "cache_read_input_tokens": 41832,
          "cache_creation_input_tokens": 2604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2604
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

_source line 16 · 2026-05-09T21:28:39.035Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0145ux7Gsp1j5SVNtAFkBG1Z`</summary>

```json
{
  "query": "ADAPT \"online reweighting\" LLM pretraining \"offline methods\" ICLR 2026 workshop DATA-FM Zhao"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbe83969-9162-4b61-abaf-9d7d0b52f68f",
  "isSidechain": false,
  "requestId": "req_011CashrVfQYWgfZQUSoDcr5",
  "type": "assistant",
  "uuid": "b89c58d2-03d6-4647-b1cd-5644272f3e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ub4zstKno3zCMqoEZk1ydk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 41832,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 250,
          "cache_read_input_tokens": 41832,
          "cache_creation_input_tokens": 2604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2604
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

_source line 17 · 2026-05-09T21:28:41.569Z_

<details><summary>↩ Tool result · `toolu_01MxPsDZ1xifr59GYhRjTHeG`</summary>

```text
Web search results for query: "QuaDMix arXiv 2504.16511 ICLR 2026 withdrawn status ByteDance"

Links: [{"title":"[2504.16511] QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining","url":"https://arxiv.org/abs/2504.16511"},{"title":"QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining","url":"https://arxiv.org/html/2504.16511"},{"title":"GitHub - bytedance/Video-As-Prompt: [ICLR 2026] Official repo for paper \"Video-As-Prompt: Unified Semantic Control for Video Generation\" · GitHub","url":"https://github.com/bytedance/Video-As-Prompt"},{"title":"ICLR Workshop 2026","url":"https://sites.google.com/view/icbinb-2026/home"},{"title":"GitHub - bytedance/Q-Insight: Q-Insight Family: Q-Insight, VQ-Insight and RALI (NeurIPS 2025 Spotlight, AAAI 2026 Oral, and ICLR 2026 Oral) · GitHub","url":"https://github.com/bytedance/Q-Insight"},{"title":"Lei Yang on X: \"Got burned by an Apple ICLR paper — it was withdrawn after my Public Comment. So here’s what happened. Earlier this month, a colleague shared an Apple paper on arXiv with me — it was also under review for ICLR 2026. The benchmark they proposed was perfectly aligned with a https://t.co/ON782SFNjI\" / X","url":"https://x.com/diyerxx/status/1994042370376032701"},{"title":"ICLR 2026 Workshop on AI with Recursive Self-Improvement 1 Workshop Summary","url":"https://openreview.net/pdf?id=OsPQ6zTQXV"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"Seed News - ByteDance Seed Team","url":"https://seed.bytedance.com/en/blog/23-papers-featured-2-interactive-sessions-bytedance-seed-invites-you-to-iclr-2025"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"}]

Based on the search results, I found information about the QuaDMix paper:

QuaDMix is a unified data selection framework that automatically optimizes the data distribution for LLM pretraining while balancing both quality and diversity. The paper is authored by researchers from ByteDance.

The paper is registered on arXiv as paper 2504.16511 with the title "QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining."

However, I did not find specific information in the search results about the withdrawal status of this paper from ICLR 2026. The search results confirm that the paper exists on arXiv and is from ByteDance authors, but there is no indication in the retrieved results that it has been withdrawn from ICLR 2026. To determine the current submission status, you would need to check the OpenReview platform directly for ICLR 2026 submissions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4552d4ee-bc57-4a3c-aa41-48098fd9f869",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "624ccc57-f289-4692-8368-8e191e8bb03d",
  "toolUseResult": {
    "query": "QuaDMix arXiv 2504.16511 ICLR 2026 withdrawn status ByteDance",
    "results": [
      {
        "tool_use_id": "srvtoolu_016pjFP9My1JizjFBkJgayAC",
        "content": [
          {
            "title": "[2504.16511] QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining",
            "url": "https://arxiv.org/abs/2504.16511"
          },
          {
            "title": "QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining",
            "url": "https://arxiv.org/html/2504.16511"
          },
          {
            "title": "GitHub - bytedance/Video-As-Prompt: [ICLR 2026] Official repo for paper \"Video-As-Prompt: Unified Semantic Control for Video Generation\" · GitHub",
            "url": "https://github.com/bytedance/Video-As-Prompt"
          },
          {
            "title": "ICLR Workshop 2026",
            "url": "https://sites.google.com/view/icbinb-2026/home"
          },
          {
            "title": "GitHub - bytedance/Q-Insight: Q-Insight Family: Q-Insight, VQ-Insight and RALI (NeurIPS 2025 Spotlight, AAAI 2026 Oral, and ICLR 2026 Oral) · GitHub",
            "url": "https://github.com/bytedance/Q-Insight"
          },
          {
            "title": "Lei Yang on X: \"Got burned by an Apple ICLR paper — it was withdrawn after my Public Comment. So here’s what happened. Earlier this month, a colleague shared an Apple paper on arXiv with me — it was also under review for ICLR 2026. The benchmark they proposed was perfectly aligned with a https://t.co/ON782SFNjI\" / X",
            "url": "https://x.com/diyerxx/status/1994042370376032701"
          },
          {
            "title": "ICLR 2026 Workshop on AI with Recursive Self-Improvement 1 Workshop Summary",
            "url": "https://openreview.net/pdf?id=OsPQ6zTQXV"
          },
          {
            "title": "Insights from the ICLR Peer Review and Rebuttal Process",
            "url": "https://arxiv.org/pdf/2511.15462"
          },
          {
            "title": "Seed News - ByteDance Seed Team",
            "url": "https://seed.bytedance.com/en/blog/23-papers-featured-2-interactive-sessions-bytedance-seed-invites-you-to-iclr-2025"
          },
          {
            "title": "ICLR 2026 Author Guide",
            "url": "https://iclr.cc/Conferences/2026/AuthorGuide"
          }
        ]
      },
      "Based on the search results, I found information about the QuaDMix paper:\n\nQuaDMix is a unified data selection framework that automatically optimizes the data distribution for LLM pretraining while balancing both quality and diversity. The paper is authored by researchers from ByteDance.\n\nThe paper is registered on arXiv as paper 2504.16511 with the title \"QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining.\"\n\nHowever, I did not find specific information in the search results about the withdrawal status of this paper from ICLR 2026. The search results confirm that the paper exists on arXiv and is from ByteDance authors, but there is no indication in the retrieved results that it has been withdrawn from ICLR 2026. To determine the current submission status, you would need to check the OpenReview platform directly for ICLR 2026 submissions."
    ],
    "durationSeconds": 4.597544018999994
  },
  "sourceToolAssistantUUID": "4552d4ee-bc57-4a3c-aa41-48098fd9f869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-09T21:28:45.785Z_

<details><summary>↩ Tool result · `toolu_0145ux7Gsp1j5SVNtAFkBG1Z`</summary>

```text
Web search results for query: "ADAPT "online reweighting" LLM pretraining "offline methods" ICLR 2026 workshop DATA-FM Zhao"

Links: [{"title":"ICLR 2026 Workshop DATA-FM | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FDATA-FM"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/0597ce794e7108f82929ea4fbb938ac7930e8169.pdf"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"DATA-FM @ ICLR 2026","url":"https://data-fm-iclr2026.github.io/"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"DYNAMIC LOSS-BASED SAMPLE REWEIGHTING FOR ...","url":"https://shiqiang.wang/papers/DS_ICLR2025.pdf"},{"title":"ICLR 2026 Workshop DATA-FM Submissions","url":"https://openreview.net/submissions?page=4&venue=ICLR.cc/2026/Workshop/DATA-FM"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"DATA-FM Workshop @ ICLR 2026 OPEN LLM PROJECTS SHOULD ALLOCATE MORE COM-","url":"https://openreview.net/pdf?id=YdvGgmIJRH"},{"title":"Published as a paper at 3rd DATA-FM workshop @ ICLR 2026, Brazil.","url":"https://openreview.net/pdf?id=UiZwM8yV6o"}]

Based on the search results, I found relevant information about your query. Here's what I discovered:

ADAPT (Adaptive Data reweighting for Pretraining and FineTuning) is a method that aligns training samples with a validation set via similarity-based weighting and consistently outperforms both offline selection/mixing strategies and prior online reweighting methods across large-scale pretraining and instruction tuning setups.

Unlike offline methods that commit to a fixed subset before training begins, ADAPT's framework dynamically adjusts data weights as the model learns, so it naturally adapts to new model states without re-running the data preprocessing and training pipeline from scratch.

ADAPT is compared with Uniform selection and existing file selection methods for LLM pre-training, including Doremi and RegMix. Additionally, the method also compares LinUpper, an online sample reweighting strategy where the sample weight is proportional to the normalized loss but is capped at a predefined α value.

The research appears to be published as a paper at ICLR 2026 and is related to the DATA-FM workshop, which focuses on data and foundation models. The work addresses the important problem of data curation for LLM pretraining by proposing an adaptive online reweighting approach that improves upon static offline methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b89c58d2-03d6-4647-b1cd-5644272f3e0c",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "9806de5e-bf2f-44c0-8727-c65f301706e7",
  "toolUseResult": {
    "query": "ADAPT \"online reweighting\" LLM pretraining \"offline methods\" ICLR 2026 workshop DATA-FM Zhao",
    "results": [
      {
        "tool_use_id": "srvtoolu_011j4uusXYw3zZMJF6KsUc1h",
        "content": [
          {
            "title": "ICLR 2026 Workshop DATA-FM | OpenReview",
            "url": "https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FDATA-FM"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf/0597ce794e7108f82929ea4fbb938ac7930e8169.pdf"
          },
          {
            "title": "ICLR 2026 Schedule",
            "url": "https://iclr.cc/virtual/2026/calendar"
          },
          {
            "title": "DATA-FM @ ICLR 2026",
            "url": "https://data-fm-iclr2026.github.io/"
          },
          {
            "title": "ICLR 2026 Orals",
            "url": "https://iclr.cc/virtual/2026/events/oral"
          },
          {
            "title": "DYNAMIC LOSS-BASED SAMPLE REWEIGHTING FOR ...",
            "url": "https://shiqiang.wang/papers/DS_ICLR2025.pdf"
          },
          {
            "title": "ICLR 2026 Workshop DATA-FM Submissions",
            "url": "https://openreview.net/submissions?page=4&venue=ICLR.cc/2026/Workshop/DATA-FM"
          },
          {
            "title": "Downloads 2026",
            "url": "https://iclr.cc/Downloads/2026"
          },
          {
            "title": "DATA-FM Workshop @ ICLR 2026 OPEN LLM PROJECTS SHOULD ALLOCATE MORE COM-",
            "url": "https://openreview.net/pdf?id=YdvGgmIJRH"
          },
          {
            "title": "Published as a paper at 3rd DATA-FM workshop @ ICLR 2026, Brazil.",
            "url": "https://openreview.net/pdf?id=UiZwM8yV6o"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query. Here's what I discovered:\n\nADAPT (Adaptive Data reweighting for Pretraining and FineTuning) is a method that aligns training samples with a validation set via similarity-based weighting and consistently outperforms both offline selection/mixing strategies and prior online reweighting methods across large-scale pretraining and instruction tuning setups.\n\nUnlike offline methods that commit to a fixed subset before training begins, ADAPT's framework dynamically adjusts data weights as the model learns, so it naturally adapts to new model states without re-running the data preprocessing and training pipeline from scratch.\n\nADAPT is compared with Uniform selection and existing file selection methods for LLM pre-training, including Doremi and RegMix. Additionally, the method also compares LinUpper, an online sample reweighting strategy where the sample weight is proportional to the normalized loss but is capped at a predefined α value.\n\nThe research appears to be published as a paper at ICLR 2026 and is related to the DATA-FM workshop, which focuses on data and foundation models. The work addresses the important problem of data curation for LLM pretraining by proposing an adaptive online reweighting approach that improves upon static offline methods."
    ],
    "durationSeconds": 6.747010794999995
  },
  "sourceToolAssistantUUID": "b89c58d2-03d6-4647-b1cd-5644272f3e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-09T21:28:46.060Z_

<details><summary>↩ Tool result · `toolu_01VpUwDAjE7MVLeeAb8SsZak`</summary>

```text
Web search results for query: "AC-ODM Actor-Critic Online Data Mixing arXiv 2505.23878 LLM pretraining"

Links: [{"title":"[2505.23878] Actor-Critic based Online Data Mixing For Language Model Pre-Training","url":"https://arxiv.org/abs/2505.23878"},{"title":"Actor-Critic based Online Data Mixing For Language Model Pre-Training","url":"https://arxiv.org/html/2505.23878"},{"title":"AC-ODM: Actor–Critic Online Data Mixing for Sample-Efficient LLM Pretraining | OpenReview","url":"https://openreview.net/forum?id=mRjzWksbGR"},{"title":"Actor-Critic based Online Data Mixing For Language Model ...","url":"https://arxiv.org/pdf/2505.23878"},{"title":"A Component-Based Survey of Interactions between Large Language Models and Multi-Armed Bandits","url":"https://arxiv.org/html/2601.12945v2"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=2575&show=50"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=12475&show=50"},{"title":"Efficient Online Data Mixing For Language Model Pre-Training","url":"https://arxiv.org/html/2312.02406v2"},{"title":"ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration","url":"https://arxiv.org/html/2411.00053v3"},{"title":"Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space","url":"https://arxiv.org/html/2512.04601v1"}]

I found the paper for you. Here's what the research is about:

## AC-ODM: Actor-Critic Online Data Mixing

AC-ODM is an actor-critic based online data mixing method which captures the varying domain weights by auxiliary actor-critic networks and considers the intra-domain interactions with the reward function for language model pretraining.

### Key Problem
The coverage and composition of pretraining data significantly impacts LLM generalization, but existing methods did not evolve with training dynamics. The existing online data mixing (ODM) method addressed this limitation by applying the multi-armed bandit algorithm as data sampling strategy, yet it did not consider the intra-domain interactions.

### Key Innovation
The method optimizes an online data mixing policy with the environment provided by a small proxy LLM, then applies the policy to sampling the batch data dynamically during training the target LLM. The solution adopts the deep deterministic policy gradient (DDPG) method, which is applicable when the state space and action space are continuous, and allows for independent execution of the actor for data mixing inference on datasets composed of the same data domains.

### Results
AC-ODM-410M, which invokes the sampling strategy obtained by a proxy LLM with 410M parameters, reaches the optimal validation perplexity of ODM 71% faster, and improves performance on the zero-shot MMLU benchmark by 27.5% of accuracy, about 2.23x better on pass@1 of HumanEval benchmark.

The paper was published on arXiv on May 29, 2025, by authors from the 15th Research Institute of China Electronics Technology Group Corporation and Alibaba Group.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbe83969-9162-4b61-abaf-9d7d0b52f68f",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "7ceb759f-45cb-4788-86b0-9367210fc9b2",
  "toolUseResult": {
    "query": "AC-ODM Actor-Critic Online Data Mixing arXiv 2505.23878 LLM pretraining",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nvq2fDoK5NWjmD3Frt8J8m",
        "content": [
          {
            "title": "[2505.23878] Actor-Critic based Online Data Mixing For Language Model Pre-Training",
            "url": "https://arxiv.org/abs/2505.23878"
          },
          {
            "title": "Actor-Critic based Online Data Mixing For Language Model Pre-Training",
            "url": "https://arxiv.org/html/2505.23878"
          },
          {
            "title": "AC-ODM: Actor–Critic Online Data Mixing for Sample-Efficient LLM Pretraining | OpenReview",
            "url": "https://openreview.net/forum?id=mRjzWksbGR"
          },
          {
            "title": "Actor-Critic based Online Data Mixing For Language Model ...",
            "url": "https://arxiv.org/pdf/2505.23878"
          },
          {
            "title": "A Component-Based Survey of Interactions between Large Language Models and Multi-Armed Bandits",
            "url": "https://arxiv.org/html/2601.12945v2"
          },
          {
            "title": "Machine Learning May 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-05?skip=2575&show=50"
          },
          {
            "title": "Computer Science May 2025",
            "url": "https://www.arxiv.org/list/cs/2025-05?skip=12475&show=50"
          },
          {
            "title": "Efficient Online Data Mixing For Language Model Pre-Training",
            "url": "https://arxiv.org/html/2312.02406v2"
          },
          {
            "title": "ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration",
            "url": "https://arxiv.org/html/2411.00053v3"
          },
          {
            "title": "Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space",
            "url": "https://arxiv.org/html/2512.04601v1"
          }
        ]
      },
      "I found the paper for you. Here's what the research is about:\n\n## AC-ODM: Actor-Critic Online Data Mixing\n\nAC-ODM is an actor-critic based online data mixing method which captures the varying domain weights by auxiliary actor-critic networks and considers the intra-domain interactions with the reward function for language model pretraining.\n\n### Key Problem\nThe coverage and composition of pretraining data significantly impacts LLM generalization, but existing methods did not evolve with training dynamics. The existing online data mixing (ODM) method addressed this limitation by applying the multi-armed bandit algorithm as data sampling strategy, yet it did not consider the intra-domain interactions.\n\n### Key Innovation\nThe method optimizes an online data mixing policy with the environment provided by a small proxy LLM, then applies the policy to sampling the batch data dynamically during training the target LLM. The solution adopts the deep deterministic policy gradient (DDPG) method, which is applicable when the state space and action space are continuous, and allows for independent execution of the actor for data mixing inference on datasets composed of the same data domains.\n\n### Results\nAC-ODM-410M, which invokes the sampling strategy obtained by a proxy LLM with 410M parameters, reaches the optimal validation perplexity of ODM 71% faster, and improves performance on the zero-shot MMLU benchmark by 27.5% of accuracy, about 2.23x better on pass@1 of HumanEval benchmark.\n\nThe paper was published on arXiv on May 29, 2025, by authors from the 15th Research Institute of China Electronics Technology Group Corporation and Alibaba Group."
    ],
    "durationSeconds": 7.806900954999997
  },
  "sourceToolAssistantUUID": "fbe83969-9162-4b61-abaf-9d7d0b52f68f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
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
  "leafUuid": "7ceb759f-45cb-4788-86b0-9367210fc9b2",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 8: Coverage-Guided Synthetic Data Selection",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

### Assistant

_source line 22 · 2026-05-09T21:28:51.961Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me continue with more searches to verify other claims:

1. QuaDMix - the search didn't confirm withdrawal from ICLR 2026. Let me check OpenReview directly.
2. AC-ODM - confirmed to exist at arXiv:2505.23878
3. ADAPT - seems to exist at ICLR 2026 Workshop DATA-FM

Let me now search for:
1. ModernBERT throughput on RTX 4090 (to verify the "~52K tokens/sec" claim)


2. The ADAPT paper's specific reference to verify it's Zhao et al.
3. arXiv:2604.13977 existence and content
4. Any new concurrent work in synthetic data selection 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ceb759f-45cb-4788-86b0-9367210fc9b2",
  "isSidechain": false,
  "requestId": "req_011CashsQ8ZLkoGLtTMM5EAa",
  "type": "assistant",
  "uuid": "88467f88-0bdd-466e-b8d6-616c8c76b415",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N4u8quTPxVbMZ8Ft9SVB5y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 820,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 44436,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 820,
          "output_tokens": 394,
          "cache_read_input_tokens": 44436,
          "cache_creation_input_tokens": 2012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2012
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

_source line 23 · 2026-05-09T21:28:52.250Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B5ik9AhLigy3cm3umnCa6k`</summary>

```json
{
  "query": "ModernBERT-large throughput tokens per second RTX 4090 H100 arXiv 2412.13663 benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88467f88-0bdd-466e-b8d6-616c8c76b415",
  "isSidechain": false,
  "requestId": "req_011CashsQ8ZLkoGLtTMM5EAa",
  "type": "assistant",
  "uuid": "c77516aa-db3e-4e79-bae0-bdd53b62dd7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N4u8quTPxVbMZ8Ft9SVB5y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 820,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 44436,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 820,
          "output_tokens": 394,
          "cache_read_input_tokens": 44436,
          "cache_creation_input_tokens": 2012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2012
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

_source line 24 · 2026-05-09T21:28:53.099Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016xmZqfF4cSRedbUtTkSfta`</summary>

```json
{
  "query": "arXiv 2604.13977 \"synthesize high-quality pretraining data\" structured output formats 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c77516aa-db3e-4e79-bae0-bdd53b62dd7e",
  "isSidechain": false,
  "requestId": "req_011CashsQ8ZLkoGLtTMM5EAa",
  "type": "assistant",
  "uuid": "4af47486-bb04-48dc-a999-510d2cc3dd63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N4u8quTPxVbMZ8Ft9SVB5y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 820,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 44436,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 820,
          "output_tokens": 394,
          "cache_read_input_tokens": 44436,
          "cache_creation_input_tokens": 2012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2012
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

_source line 25 · 2026-05-09T21:28:53.721Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XsRukhvQLcAySgDj9MSX8g`</summary>

```json
{
  "query": "synthetic pretraining data selection tail coverage contamination EMNLP 2026 arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4af47486-bb04-48dc-a999-510d2cc3dd63",
  "isSidechain": false,
  "requestId": "req_011CashsQ8ZLkoGLtTMM5EAa",
  "type": "assistant",
  "uuid": "adb5e308-e8cd-4258-9b4d-c287b5619e33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N4u8quTPxVbMZ8Ft9SVB5y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 820,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 44436,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 820,
          "output_tokens": 394,
          "cache_read_input_tokens": 44436,
          "cache_creation_input_tokens": 2012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2012
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

_source line 26 · 2026-05-09T21:28:57.112Z_

<details><summary>↩ Tool result · `toolu_01B5ik9AhLigy3cm3umnCa6k`</summary>

```text
Web search results for query: "ModernBERT-large throughput tokens per second RTX 4090 H100 arXiv 2412.13663 benchmark"

Links: [{"title":"Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference","url":"https://arxiv.org/html/2412.13663v2"},{"title":"arXiv:2412.13663v2 [cs.CL] 19 Dec 2024","url":"https://arxiv.org/pdf/2412.13663"},{"title":"[2412.13663] Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference","url":"https://arxiv.org/abs/2412.13663"},{"title":"Finally, a Replacement for BERT: Introducing ModernBERT","url":"https://huggingface.co/blog/modernbert"},{"title":"ModernBERT, the BERT of 2024 - by Grigory Sapunov","url":"https://gonzoml.substack.com/p/modernbert-the-bert-of-2024"},{"title":"BioClinical ModernBERT: A State-of-the-Art Long-Context Encoder for Biomedical and Clinical NLP","url":"https://arxiv.org/html/2506.10896v1"},{"title":"ModernBERT: Efficient Long-Context Transformer","url":"https://www.emergentmind.com/topics/modernbert"},{"title":"Large Language Model Inference Acceleration: A Comprehensive Hardware Perspective","url":"https://arxiv.org/html/2410.04466v3"},{"title":"Self-hosted GPT: real response time, token throughput, and cost on L4, L40S and H100 for GPT-OSS-20B · Insights","url":"https://devforth.io/insights/self-hosted-gpt-real-response-time-token-throughput-and-cost-on-l4-l40s-and-h100-for-gpt-oss-20b/"},{"title":"The Definitive GPU Ranking for LLMs: Token Generation & Prompt Processing Performance","url":"https://www.hardware-corner.net/gpu-ranking-local-llm/"}]

I found search results related to the ModernBERT paper (arXiv 2412.13663). The search results confirm that Table 2 presents memory (max batch size) and inference (in thousands of tokens per second) efficiency results on an NVIDIA RTX 4090, averaged over 10 runs.

However, the search results don't provide the specific numerical throughput values for ModernBERT-large on the RTX 4090 or H100. While the paper discusses efficiency benchmarks on these GPUs, the actual throughput numbers aren't displayed in the search result excerpts. The full paper with Table 2 containing the specific tokens-per-second metrics would need to be accessed directly from the arXiv link (https://arxiv.org/html/2412.13663v2) to see the complete benchmark data.

The search results indicate that ModernBERT stands out as the most efficient model overall, and efficiency results on an NVIDIA RTX 4090 show memory and inference metrics in thousands of tokens per second, but the specific numerical values from Table 2 aren't visible in these excerpts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c77516aa-db3e-4e79-bae0-bdd53b62dd7e",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "b0bc3827-7902-4727-b9cb-993475d2ca0e",
  "toolUseResult": {
    "query": "ModernBERT-large throughput tokens per second RTX 4090 H100 arXiv 2412.13663 benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HjjKwfZCc93W4bsWrH439E",
        "content": [
          {
            "title": "Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference",
            "url": "https://arxiv.org/html/2412.13663v2"
          },
          {
            "title": "arXiv:2412.13663v2 [cs.CL] 19 Dec 2024",
            "url": "https://arxiv.org/pdf/2412.13663"
          },
          {
            "title": "[2412.13663] Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference",
            "url": "https://arxiv.org/abs/2412.13663"
          },
          {
            "title": "Finally, a Replacement for BERT: Introducing ModernBERT",
            "url": "https://huggingface.co/blog/modernbert"
          },
          {
            "title": "ModernBERT, the BERT of 2024 - by Grigory Sapunov",
            "url": "https://gonzoml.substack.com/p/modernbert-the-bert-of-2024"
          },
          {
            "title": "BioClinical ModernBERT: A State-of-the-Art Long-Context Encoder for Biomedical and Clinical NLP",
            "url": "https://arxiv.org/html/2506.10896v1"
          },
          {
            "title": "ModernBERT: Efficient Long-Context Transformer",
            "url": "https://www.emergentmind.com/topics/modernbert"
          },
          {
            "title": "Large Language Model Inference Acceleration: A Comprehensive Hardware Perspective",
            "url": "https://arxiv.org/html/2410.04466v3"
          },
          {
            "title": "Self-hosted GPT: real response time, token throughput, and cost on L4, L40S and H100 for GPT-OSS-20B · Insights",
            "url": "https://devforth.io/insights/self-hosted-gpt-real-response-time-token-throughput-and-cost-on-l4-l40s-and-h100-for-gpt-oss-20b/"
          },
          {
            "title": "The Definitive GPU Ranking for LLMs: Token Generation & Prompt Processing Performance",
            "url": "https://www.hardware-corner.net/gpu-ranking-local-llm/"
          }
        ]
      },
      "I found search results related to the ModernBERT paper (arXiv 2412.13663). The search results confirm that Table 2 presents memory (max batch size) and inference (in thousands of tokens per second) efficiency results on an NVIDIA RTX 4090, averaged over 10 runs.\n\nHowever, the search results don't provide the specific numerical throughput values for ModernBERT-large on the RTX 4090 or H100. While the paper discusses efficiency benchmarks on these GPUs, the actual throughput numbers aren't displayed in the search result excerpts. The full paper with Table 2 containing the specific tokens-per-second metrics would need to be accessed directly from the arXiv link (https://arxiv.org/html/2412.13663v2) to see the complete benchmark data.\n\nThe search results indicate that ModernBERT stands out as the most efficient model overall, and efficiency results on an NVIDIA RTX 4090 show memory and inference metrics in thousands of tokens per second, but the specific numerical values from Table 2 aren't visible in these excerpts."
    ],
    "durationSeconds": 4.858087316999998
  },
  "sourceToolAssistantUUID": "c77516aa-db3e-4e79-bae0-bdd53b62dd7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-09T21:28:58.792Z_

<details><summary>↩ Tool result · `toolu_016xmZqfF4cSRedbUtTkSfta`</summary>

```text
Web search results for query: "arXiv 2604.13977 "synthesize high-quality pretraining data" structured output formats 2026"

Links: [{"title":"[2604.13977] How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data","url":"https://arxiv.org/abs/2604.13977"},{"title":"How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data","url":"https://arxiv.org/html/2604.13977"},{"title":"Preprint. Under review. How Can We Synthesize High-Quality Pretraining Data?","url":"https://arxiv.org/pdf/2604.13977"},{"title":"Synthesize-on-Graph: Knowledgeable Synthetic Data Generation for Continued Pre-training of Large Language Models","url":"https://arxiv.org/html/2505.00979v3"},{"title":"Synthetic bootstrapped pretraining","url":"https://arxiv.org/html/2509.15248v1"},{"title":"Bootstrapping Post-training Signals for Open-ended Tasks via Rubric-based Self-play on Pre-training Text","url":"https://arxiv.org/html/2604.20051"},{"title":"Pre-training on Synthetic Driving Data for Trajectory Prediction","url":"https://arxiv.org/html/2309.10121"},{"title":"The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models","url":"https://arxiv.org/html/2604.25359"},{"title":"Aligning Instruction Tuning with Pre-training","url":"https://arxiv.org/html/2501.09368v1"},{"title":"Data-efficient Performance Modeling via Pre-training","url":"https://arxiv.org/html/2501.14438v1"}]

Based on the web search results, I found the arXiv paper you're looking for.

The paper arXiv:2604.13977, titled "How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data," was submitted on April 15, 2026. It addresses the absence of systematic comparisons across design dimensions for synthesizing pretraining data, including rephrasing strategy, generator model, and source data.

The key finding is that structured output formats, such as tables, math problems, FAQs, and tutorials, consistently outperform both curated web baselines and prior synthetic methods.

The research involved conducting extensive controlled experiments, generating over one trillion tokens, to identify critical factors in rephrasing web text into synthetic pretraining data. The analysis also demonstrates that increasing the size of the generator model beyond 1B parameters provides no additional benefit.

Based on these findings, the authors developed FinePhrase, a 486-billion-token open dataset of rephrased web text.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4af47486-bb04-48dc-a999-510d2cc3dd63",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "cd87604f-9372-4cba-a06d-212d92cb7135",
  "toolUseResult": {
    "query": "arXiv 2604.13977 \"synthesize high-quality pretraining data\" structured output formats 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018RTBkTEn1TfdcAZkFLi3w9",
        "content": [
          {
            "title": "[2604.13977] How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data",
            "url": "https://arxiv.org/abs/2604.13977"
          },
          {
            "title": "How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data",
            "url": "https://arxiv.org/html/2604.13977"
          },
          {
            "title": "Preprint. Under review. How Can We Synthesize High-Quality Pretraining Data?",
            "url": "https://arxiv.org/pdf/2604.13977"
          },
          {
            "title": "Synthesize-on-Graph: Knowledgeable Synthetic Data Generation for Continued Pre-training of Large Language Models",
            "url": "https://arxiv.org/html/2505.00979v3"
          },
          {
            "title": "Synthetic bootstrapped pretraining",
            "url": "https://arxiv.org/html/2509.15248v1"
          },
          {
            "title": "Bootstrapping Post-training Signals for Open-ended Tasks via Rubric-based Self-play on Pre-training Text",
            "url": "https://arxiv.org/html/2604.20051"
          },
          {
            "title": "Pre-training on Synthetic Driving Data for Trajectory Prediction",
            "url": "https://arxiv.org/html/2309.10121"
          },
          {
            "title": "The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models",
            "url": "https://arxiv.org/html/2604.25359"
          },
          {
            "title": "Aligning Instruction Tuning with Pre-training",
            "url": "https://arxiv.org/html/2501.09368v1"
          },
          {
            "title": "Data-efficient Performance Modeling via Pre-training",
            "url": "https://arxiv.org/html/2501.14438v1"
          }
        ]
      },
      "Based on the web search results, I found the arXiv paper you're looking for.\n\nThe paper arXiv:2604.13977, titled \"How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data,\" was submitted on April 15, 2026. It addresses the absence of systematic comparisons across design dimensions for synthesizing pretraining data, including rephrasing strategy, generator model, and source data.\n\nThe key finding is that structured output formats, such as tables, math problems, FAQs, and tutorials, consistently outperform both curated web baselines and prior synthetic methods.\n\nThe research involved conducting extensive controlled experiments, generating over one trillion tokens, to identify critical factors in rephrasing web text into synthetic pretraining data. The analysis also demonstrates that increasing the size of the generator model beyond 1B parameters provides no additional benefit.\n\nBased on these findings, the authors developed FinePhrase, a 486-billion-token open dataset of rephrased web text."
    ],
    "durationSeconds": 5.688341329000003
  },
  "sourceToolAssistantUUID": "4af47486-bb04-48dc-a999-510d2cc3dd63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-09T21:29:02.163Z_

<details><summary>↩ Tool result · `toolu_01XsRukhvQLcAySgDj9MSX8g`</summary>

```text
Web search results for query: "synthetic pretraining data selection tail coverage contamination EMNLP 2026 arxiv 2025 2026"

Links: [{"title":"Demystifying Synthetic Data in LLM Pre-training","url":"https://aclanthology.org/2025.emnlp-main.544.pdf"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.544/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://aclanthology.org/2025.emnlp-main.1173.pdf"},{"title":"[2510.01631] Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls","url":"https://arxiv.org/abs/2510.01631"},{"title":"Synthetic Data in LLM Pre-Training","url":"https://www.emergentmind.com/papers/2510.01631"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"}]

I found several relevant papers and resources related to your search query. Here are the key results:

## Main Findings:

**1. "Demystifying Synthetic Data in LLM Pre-training" (EMNLP 2025)**

This paper presents "A Systematic Study of Scaling Laws, Benefits, and Pitfalls" and was published in the 2025 Conference on Empirical Methods in Natural Language Processing. The study conducted a large-scale empirical investigation (>1000 LLMs with >100k GPU hours) using a unified protocol and scaling laws, comparing natural web data, diverse synthetic types (rephrased text, generated textbooks), and mixtures of natural and synthetic data.

Key findings include: Pre-training on 1/3 rephrased synthetic data mixed with 2/3 natural web texts can speed up 5-10x (to reach the same validation loss) at larger data budgets, and training on rephrased synthetic data shows no degradation in performance in foreseeable scales whereas training on mixtures of textbook-style pure-generated synthetic data shows patterns predicted by "model collapse".

**2. Data Contamination Research**

The paper "DCR: Quantifying Data Contamination in LLMs Evaluation" was published in the 2025 Conference on Empirical Methods in Natural Language Processing, addressing contamination measurement frameworks.

**3. EMNLP 2026 Call for Papers**

EMNLP 2026 is explicitly calling for research on data scarcity and limits, contamination, and the consequences of synthetic data feedback loops, and new approaches to data creation, documentation, governance, and consent.

These papers directly address your search topics around synthetic data selection, pretraining, and data contamination concerns in recent conferences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adb5e308-e8cd-4258-9b4d-c287b5619e33",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "2bd70ddb-6548-4a67-aef6-041927cea5cf",
  "toolUseResult": {
    "query": "synthetic pretraining data selection tail coverage contamination EMNLP 2026 arxiv 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FLdAGX6pRvfzi9q2JuBZu8",
        "content": [
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training",
            "url": "https://aclanthology.org/2025.emnlp-main.544.pdf"
          },
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.544/"
          },
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://aclanthology.org/2025.emnlp-main.1173.pdf"
          },
          {
            "title": "[2510.01631] Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls",
            "url": "https://arxiv.org/abs/2510.01631"
          },
          {
            "title": "Synthetic Data in LLM Pre-Training",
            "url": "https://www.emergentmind.com/papers/2510.01631"
          },
          {
            "title": "Machine Learning May 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub",
            "url": "https://github.com/pengr/LLM-Synthetic-Data"
          },
          {
            "title": "Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation",
            "url": "https://arxiv.org/html/2502.17521v2"
          }
        ]
      },
      "I found several relevant papers and resources related to your search query. Here are the key results:\n\n## Main Findings:\n\n**1. \"Demystifying Synthetic Data in LLM Pre-training\" (EMNLP 2025)**\n\nThis paper presents \"A Systematic Study of Scaling Laws, Benefits, and Pitfalls\" and was published in the 2025 Conference on Empirical Methods in Natural Language Processing. The study conducted a large-scale empirical investigation (>1000 LLMs with >100k GPU hours) using a unified protocol and scaling laws, comparing natural web data, diverse synthetic types (rephrased text, generated textbooks), and mixtures of natural and synthetic data.\n\nKey findings include: Pre-training on 1/3 rephrased synthetic data mixed with 2/3 natural web texts can speed up 5-10x (to reach the same validation loss) at larger data budgets, and training on rephrased synthetic data shows no degradation in performance in foreseeable scales whereas training on mixtures of textbook-style pure-generated synthetic data shows patterns predicted by \"model collapse\".\n\n**2. Data Contamination Research**\n\nThe paper \"DCR: Quantifying Data Contamination in LLMs Evaluation\" was published in the 2025 Conference on Empirical Methods in Natural Language Processing, addressing contamination measurement frameworks.\n\n**3. EMNLP 2026 Call for Papers**\n\nEMNLP 2026 is explicitly calling for research on data scarcity and limits, contamination, and the consequences of synthetic data feedback loops, and new approaches to data creation, documentation, governance, and consent.\n\nThese papers directly address your search topics around synthetic data selection, pretraining, and data contamination concerns in recent conferences."
    ],
    "durationSeconds": 8.439133424
  },
  "sourceToolAssistantUUID": "adb5e308-e8cd-4258-9b4d-c287b5619e33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-09T21:29:07.055Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now:
1. Fetch the ModernBERT paper to verify the specific throughput numbers (52K tokens/sec on RTX 4090)
2. Check the QuaDMix OpenReview status
3. Check for the ADAPT paper's correct reference in the OpenReview database

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bd70ddb-6548-4a67-aef6-041927cea5cf",
  "isSidechain": false,
  "requestId": "req_011Cashtas11Ftab4Sgz8heA",
  "type": "assistant",
  "uuid": "3e78e5bf-1052-4df9-917a-113e39403137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EsFY3RGWBvt4AkN6WSkkuP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 46448,
      "output_tokens": 392,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 392,
          "cache_read_input_tokens": 46448,
          "cache_creation_input_tokens": 3820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3820
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

_source line 30 · 2026-05-09T21:29:11.312Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KdFjywAQfRgqXUu2zqS1a1`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.13663v2",
  "prompt": "What is the inference throughput (tokens per second) for ModernBERT-large on RTX 4090? Look for Table 2 or any benchmark table with throughput numbers in thousands of tokens per second. Report the exact numbers from the table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e78e5bf-1052-4df9-917a-113e39403137",
  "isSidechain": false,
  "requestId": "req_011Cashtas11Ftab4Sgz8heA",
  "type": "assistant",
  "uuid": "08ebfe12-c1be-44fa-98df-199cbe237503",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EsFY3RGWBvt4AkN6WSkkuP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 46448,
      "output_tokens": 392,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 392,
          "cache_read_input_tokens": 46448,
          "cache_creation_input_tokens": 3820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3820
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

_source line 31 · 2026-05-09T21:29:11.909Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Su5Mn1DHFwfuD8bjptGi2b`</summary>

```json
{
  "url": "https://openreview.net/forum?id=oLxx7OhAb1",
  "prompt": "What is the status of this ICLR 2026 submission? Is it withdrawn, rejected, or accepted? What is the paper title?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08ebfe12-c1be-44fa-98df-199cbe237503",
  "isSidechain": false,
  "requestId": "req_011Cashtas11Ftab4Sgz8heA",
  "type": "assistant",
  "uuid": "348f93ba-ece2-48be-a981-c25538391014",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EsFY3RGWBvt4AkN6WSkkuP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 46448,
      "output_tokens": 392,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 392,
          "cache_read_input_tokens": 46448,
          "cache_creation_input_tokens": 3820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3820
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

_source line 32 · 2026-05-09T21:29:11.913Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DcKiLsXFtyVThvtUMjabAP`</summary>

```json
{
  "query": "\"coverage guided\" OR \"coverage-guided\" synthetic data selection pretraining 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "348f93ba-ece2-48be-a981-c25538391014",
  "isSidechain": false,
  "requestId": "req_011Cashtas11Ftab4Sgz8heA",
  "type": "assistant",
  "uuid": "6df82809-2f71-4b54-a224-10f1f6705e90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EsFY3RGWBvt4AkN6WSkkuP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 46448,
      "output_tokens": 392,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 392,
          "cache_read_input_tokens": 46448,
          "cache_creation_input_tokens": 3820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3820
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
  "leafUuid": "6df82809-2f71-4b54-a224-10f1f6705e90",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 8: Coverage-Guided Synthetic Data Selection",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

### Tool result

_source line 35 · 2026-05-09T21:29:14.114Z_

<details><summary>↩ Tool result · `toolu_01Su5Mn1DHFwfuD8bjptGi2b`</summary>

```text
# ICLR 2026 Submission Status

**Paper Title:** "QUADMIX: QUALITY-DIVERSITY BALANCED DATA SELECTION FOR EFFICIENT LLM PRETRAINING"

**Status:** The submission was withdrawn. The page explicitly indicates this is an "ICLR 2026 Conference Withdrawn Submission."

The paper proposes a unified framework for data selection in large language model pretraining that aims to balance data quality and diversity simultaneously, reporting an average performance improvement of 7.2% across multiple benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "348f93ba-ece2-48be-a981-c25538391014",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "1bb7c1dd-f758-4677-a061-b8f4907f51e6",
  "toolUseResult": {
    "bytes": 72460,
    "code": 200,
    "codeText": "OK",
    "result": "# ICLR 2026 Submission Status\n\n**Paper Title:** \"QUADMIX: QUALITY-DIVERSITY BALANCED DATA SELECTION FOR EFFICIENT LLM PRETRAINING\"\n\n**Status:** The submission was withdrawn. The page explicitly indicates this is an \"ICLR 2026 Conference Withdrawn Submission.\"\n\nThe paper proposes a unified framework for data selection in large language model pretraining that aims to balance data quality and diversity simultaneously, reporting an average performance improvement of 7.2% across multiple benchmarks.",
    "durationMs": 2203,
    "url": "https://openreview.net/forum?id=oLxx7OhAb1"
  },
  "sourceToolAssistantUUID": "348f93ba-ece2-48be-a981-c25538391014",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-09T21:29:14.744Z_

<details><summary>↩ Tool result · `toolu_01KdFjywAQfRgqXUu2zqS1a1`</summary>

```text
# ModernBERT-Large Inference Throughput on RTX 4090

According to Table 2 in the paper, ModernBERT-large achieves the following throughput on an NVIDIA RTX 4090:

**Short Context (512 tokens):**
- Fixed length: 52.3 thousand tokens/second
- Variable length: 52.9 thousand tokens/second

**Long Context (8192 tokens):**
- Fixed length: 46.8 thousand tokens/second
- Variable length: 49.8 thousand tokens/second

The paper notes that "ModernBERT-large's processing speed at length 8192 (46,801 tokens per second) is closer to that of GTE-en-MLM base (47,507 tokens per second) than it is to GTE-en-MLM-large (16,532 tokens per second)," highlighting ModernBERT's efficiency advantage on longer sequences.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08ebfe12-c1be-44fa-98df-199cbe237503",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "f70c7a8b-f72c-428e-ba43-41e7d011da0e",
  "toolUseResult": {
    "bytes": 436968,
    "code": 200,
    "codeText": "OK",
    "result": "# ModernBERT-Large Inference Throughput on RTX 4090\n\nAccording to Table 2 in the paper, ModernBERT-large achieves the following throughput on an NVIDIA RTX 4090:\n\n**Short Context (512 tokens):**\n- Fixed length: 52.3 thousand tokens/second\n- Variable length: 52.9 thousand tokens/second\n\n**Long Context (8192 tokens):**\n- Fixed length: 46.8 thousand tokens/second\n- Variable length: 49.8 thousand tokens/second\n\nThe paper notes that \"ModernBERT-large's processing speed at length 8192 (46,801 tokens per second) is closer to that of GTE-en-MLM base (47,507 tokens per second) than it is to GTE-en-MLM-large (16,532 tokens per second),\" highlighting ModernBERT's efficiency advantage on longer sequences.",
    "durationMs": 3427,
    "url": "https://arxiv.org/html/2412.13663v2"
  },
  "sourceToolAssistantUUID": "08ebfe12-c1be-44fa-98df-199cbe237503",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-09T21:29:19.143Z_

<details><summary>↩ Tool result · `toolu_01DcKiLsXFtyVThvtUMjabAP`</summary>

```text
Web search results for query: ""coverage guided" OR "coverage-guided" synthetic data selection pretraining 2025 2026 arxiv"

Links: [{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"},{"title":"propella-1: Multi-Property Document Annotation for LLM Data Curation at Scale","url":"https://arxiv.org/html/2602.12414v2"},{"title":"Less is More: Adaptive Coverage for Synthetic Training Data","url":"https://arxiv.org/html/2504.14508v2"},{"title":"Less is More: Adaptive Coverage for Synthetic Training Data Sasan Tavakkol","url":"https://arxiv.org/pdf/2504.14508"},{"title":"[2508.10975] BeyondWeb: Lessons from Scaling Synthetic Data for Trillion-scale Pretraining","url":"https://arxiv.org/abs/2508.10975"},{"title":"[2510.15020] The Coverage Principle: How Pre-Training Enables Post-Training","url":"https://arxiv.org/abs/2510.15020"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls","url":"https://arxiv.org/html/2510.01631v1"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=21225&show=500"},{"title":"[2504.14508] Less is More: Adaptive Coverage for Synthetic Training Data","url":"https://arxiv.org/abs/2504.14508"},{"title":"Empowering Time Series Analysis with Synthetic Data: A Survey and Outlook in the Era of Foundation Models","url":"https://arxiv.org/html/2503.11411v1"}]

Based on the web search results, I found several relevant papers on coverage-guided and coverage-related synthetic data selection for pretraining. Here are the key findings:

## Most Relevant Papers

**1. "Less is More: Adaptive Coverage for Synthetic Training Data"** (arxiv:2504.14508, April 2025)

This study introduces a novel sampling algorithm, based on the maximum coverage problem, to select a representative subset from a synthetically generated dataset. The results demonstrate that training a classifier on this contextually sampled subset achieves superior performance compared to training on the entire dataset, with this "less is more" approach improving model accuracy while reducing the volume of data required.

**2. "The Coverage Principle: How Pre-Training Enables Post-Training"** (arxiv:2510.15020, October 2025)

This paper provides a theoretical perspective on pre-training through the lens of coverage, which quantifies the probability mass the pre-trained model places on high-quality responses, and develops an understanding of the coverage principle, whereby next-token prediction implicitly optimizes toward a model with good coverage.

## Related Work on Synthetic Data for Pretraining

**3. "BeyondWeb: Lessons from Scaling Synthetic Data for Trillion-scale Pretraining"** (arxiv:2508.10975, August 2025)

This paper examines scaling synthetic data for large-scale pretraining, though it doesn't specifically focus on coverage-guided selection.

**4. "Demystifying Synthetic Data in LLM Pre-training"** (arxiv:2510.01631, October 2025)

This systematic study finds that mixing synthetic data types with natural data substantially improves performance over using synthetic data alone.

The most directly relevant result to your query is the "Less is More" paper, which explicitly uses coverage-based methods for selecting representative subsets of synthetic training data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6df82809-2f71-4b54-a224-10f1f6705e90",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "d15e1cde-4799-45fc-b250-45c8f2c59c67",
  "toolUseResult": {
    "query": "\"coverage guided\" OR \"coverage-guided\" synthetic data selection pretraining 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RRAmTFcUvhQ8qz4yoa9HKS",
        "content": [
          {
            "title": "Machine Learning May 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"
          },
          {
            "title": "propella-1: Multi-Property Document Annotation for LLM Data Curation at Scale",
            "url": "https://arxiv.org/html/2602.12414v2"
          },
          {
            "title": "Less is More: Adaptive Coverage for Synthetic Training Data",
            "url": "https://arxiv.org/html/2504.14508v2"
          },
          {
            "title": "Less is More: Adaptive Coverage for Synthetic Training Data Sasan Tavakkol",
            "url": "https://arxiv.org/pdf/2504.14508"
          },
          {
            "title": "[2508.10975] BeyondWeb: Lessons from Scaling Synthetic Data for Trillion-scale Pretraining",
            "url": "https://arxiv.org/abs/2508.10975"
          },
          {
            "title": "[2510.15020] The Coverage Principle: How Pre-Training Enables Post-Training",
            "url": "https://arxiv.org/abs/2510.15020"
          },
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls",
            "url": "https://arxiv.org/html/2510.01631v1"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=21225&show=500"
          },
          {
            "title": "[2504.14508] Less is More: Adaptive Coverage for Synthetic Training Data",
            "url": "https://arxiv.org/abs/2504.14508"
          },
          {
            "title": "Empowering Time Series Analysis with Synthetic Data: A Survey and Outlook in the Era of Foundation Models",
            "url": "https://arxiv.org/html/2503.11411v1"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers on coverage-guided and coverage-related synthetic data selection for pretraining. Here are the key findings:\n\n## Most Relevant Papers\n\n**1. \"Less is More: Adaptive Coverage for Synthetic Training Data\"** (arxiv:2504.14508, April 2025)\n\nThis study introduces a novel sampling algorithm, based on the maximum coverage problem, to select a representative subset from a synthetically generated dataset. The results demonstrate that training a classifier on this contextually sampled subset achieves superior performance compared to training on the entire dataset, with this \"less is more\" approach improving model accuracy while reducing the volume of data required.\n\n**2. \"The Coverage Principle: How Pre-Training Enables Post-Training\"** (arxiv:2510.15020, October 2025)\n\nThis paper provides a theoretical perspective on pre-training through the lens of coverage, which quantifies the probability mass the pre-trained model places on high-quality responses, and develops an understanding of the coverage principle, whereby next-token prediction implicitly optimizes toward a model with good coverage.\n\n## Related Work on Synthetic Data for Pretraining\n\n**3. \"BeyondWeb: Lessons from Scaling Synthetic Data for Trillion-scale Pretraining\"** (arxiv:2508.10975, August 2025)\n\nThis paper examines scaling synthetic data for large-scale pretraining, though it doesn't specifically focus on coverage-guided selection.\n\n**4. \"Demystifying Synthetic Data in LLM Pre-training\"** (arxiv:2510.01631, October 2025)\n\nThis systematic study finds that mixing synthetic data types with natural data substantially improves performance over using synthetic data alone.\n\nThe most directly relevant result to your query is the \"Less is More\" paper, which explicitly uses coverage-based methods for selecting representative subsets of synthetic training data."
    ],
    "durationSeconds": 7.2265979179999995
  },
  "sourceToolAssistantUUID": "6df82809-2f71-4b54-a224-10f1f6705e90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-09T21:29:19.150Z_

```json
{
  "parentUuid": "d15e1cde-4799-45fc-b250-45c8f2c59c67",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3b9e66f4-751c-45d0-bd12-b196a460cace",
  "timestamp": "2026-05-09T21:29:19.150Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 39 · 2026-05-09T21:29:44.492Z_

<details><summary>Logged reasoning block</summary>

```text
Good findings so far:

1. **ModernBERT-large throughput**: Confirmed ~52K tokens/sec on RTX 4090 for short context (512 tokens). The proposal states "~52K tokens/sec for ModernBERT-large on RTX 4090 (arXiv:2412.13663)" - THIS IS CORRECT. The paper confirms 52.3K tokens/sec fixed length at 512 tokens.

2. **QuaDMix withdrawal**: CONFIRMED - The OpenReview page explicitly says it's a "ICLR 2026 Conference Withdrawn Submission." So the proposal is correct to say "withdrawn from ICLR 2026."


3. **arXiv:2604.13977**: Verified to exist, and the proposal accurately describes its findings about structured output formats outperforming baselines. **AC-ODM (arXiv:2505.23878)**: Also confirmed. **Coverage-guided**: I haven't found a concurrent paper specifically focused on coverage-guided sampling for pretraining.

Now I'm noticing a potential issue with the ModernBERT H100 throughput claim in the proposal.

The 52K tokens/sec figure for RTX 4090 checks out at 512 token length, but the assertion that H100 delivers 2-4× faster encoder inference than RTX 4090 lacks direct verification—it's plausible based on NVIDIA specs but I should verify this more carefully. I'm also seeing the budget calculation starts with 7.68B synthetic tokens divided by 100, and I need to trace through the rest of that math.

If H100 throughput is actually in the 104-208K tok/s range (the 2-4× multiplier applied to 52K), then the 7.68B and 5B token divisions work out to roughly 20.5H and 13.4H respectively, totaling around 34H—which aligns with the stated 35H nominal budget. But this only holds if H100 truly delivers that 2× minimum; if it's actually just 52K tok/s, the budget balloons to 69H, which would exceed the 200H threshold. So the critical assumption here is whether that 2-4× H100 advantage claim is accurate.

Looking at the specs, H100 has lower peak compute (67 TFLOPS BF16) than RTX 4090 (82 TFLOPS BF16), but the memory bandwidth gap is massive—3.35 TB/s versus roughly 1 TB/s on the 4090. For encoder inference on small models like ModernBERT-large, the workload is memory-bandwidth constrained rather than compute-bound, so H100's 3.3× bandwidth advantage should translate to roughly 3× throughput improvement. That makes the 2-4× claim seem reasonable, with 2× being the conservative floor.

Now I'm checking whether there's been any recent work on this topic that the proposal might have overlooked—particularly papers from late 2025 through May 2026 on synthetic data selection, Voronoi-based or embedding-driven pretraining data filtering, or direct critiques of the CGS approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b9e66f4-751c-45d0-bd12-b196a460cace",
  "isSidechain": false,
  "requestId": "req_011CashusSvaHXqSNBD8q7VF",
  "type": "assistant",
  "uuid": "43e3e6cf-06d4-4102-9169-35f00dbe483d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RjDziiJVVFwHY7vo94rtRa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1829,
      "cache_read_input_tokens": 50268,
      "output_tokens": 1358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1358,
          "cache_read_input_tokens": 50268,
          "cache_creation_input_tokens": 1829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1829
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

_source line 40 · 2026-05-09T21:29:44.625Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019zwuNtDFptYvQo4GNjDg3i`</summary>

```json
{
  "query": "embedding space Voronoi coverage pretraining data selection LLM 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43e3e6cf-06d4-4102-9169-35f00dbe483d",
  "isSidechain": false,
  "requestId": "req_011CashusSvaHXqSNBD8q7VF",
  "type": "assistant",
  "uuid": "1430f383-31be-4dee-bb50-ab15075f0d16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RjDziiJVVFwHY7vo94rtRa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1829,
      "cache_read_input_tokens": 50268,
      "output_tokens": 1358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1358,
          "cache_read_input_tokens": 50268,
          "cache_creation_input_tokens": 1829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1829
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

_source line 41 · 2026-05-09T21:29:44.798Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AdnYLp3hDQSiJUXAA4Ybrt`</summary>

```json
{
  "query": "\"tail knowledge\" \"long-tail\" synthetic pretraining data selection filtering 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1430f383-31be-4dee-bb50-ab15075f0d16",
  "isSidechain": false,
  "requestId": "req_011CashusSvaHXqSNBD8q7VF",
  "type": "assistant",
  "uuid": "06c474bf-bbb2-4718-8597-cea112bfa035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RjDziiJVVFwHY7vo94rtRa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1829,
      "cache_read_input_tokens": 50268,
      "output_tokens": 1358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1358,
          "cache_read_input_tokens": 50268,
          "cache_creation_input_tokens": 1829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1829
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

_source line 42 · 2026-05-09T21:29:47.257Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JB1gXZAUUuA33TAfStEtb4`</summary>

```json
{
  "url": "https://openreview.net/submissions?page=4&venue=ICLR.cc/2026/Workshop/DATA-FM",
  "prompt": "Find the paper about \"ADAPT\" or \"online reweighting\" or \"offline methods\" in pretraining. Who are the authors (Zhao et al.)? What is the paper's title and OpenReview ID? Also find any other relevant papers on data selection for LLM pretraining."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06c474bf-bbb2-4718-8597-cea112bfa035",
  "isSidechain": false,
  "requestId": "req_011CashusSvaHXqSNBD8q7VF",
  "type": "assistant",
  "uuid": "a9bca007-6ad5-4bdc-a78a-816148c07342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RjDziiJVVFwHY7vo94rtRa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1829,
      "cache_read_input_tokens": 50268,
      "output_tokens": 1358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1358,
          "cache_read_input_tokens": 50268,
          "cache_creation_input_tokens": 1829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1829
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

_source line 43 · 2026-05-09T21:29:51.821Z_

<details><summary>↩ Tool result · `toolu_019zwuNtDFptYvQo4GNjDg3i`</summary>

```text
Web search results for query: "embedding space Voronoi coverage pretraining data selection LLM 2025 2026 arxiv"

Links: [{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=2125&show=2000"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=1875&show=2000"},{"title":"Machine Learning Apr 2025","url":"https://arxiv.org/list/cs.LG/2025-04?skip=75&show=1000"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2405.17428"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Next-Embedding Prediction Makes Strong Vision Learners","url":"https://arxiv.org/html/2512.16922v2"},{"title":"LLMs are Also Effective Embedding Models: An In-depth Overview","url":"https://arxiv.org/html/2412.12591v2"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=450&show=2000"},{"title":"Revealing the Numeracy Gap: An Empirical Investigation of Text Embedding Models","url":"https://arxiv.org/html/2509.05691v1"},{"title":"When Text Embedding Meets Large Language Model: A Comprehensive Survey","url":"https://arxiv.org/html/2412.09165v1"}]

I've searched for papers related to "embedding space Voronoi coverage pretraining data selection LLM" for 2025-2026 on arXiv. Here's what I found:

The search returned several relevant results covering embedding spaces and LLMs from 2025-2026, though I didn't find a specific paper that directly combines all these concepts (Voronoi diagrams, embedding space coverage, and data selection for LLM pretraining).

However, I did find one potentially relevant result: A paper titled "Voronoi-grid-based Pareto Front Learning and Its Application to Collaborative Federated Learning" by Mengmeng Chen, Xiaohu Wu, and others, which appears in the May 2025 Machine Learning arXiv listings.

The search also returned several papers on related topics:

- Papers on embedding models and LLMs, including work on representation learning with LLMs, noting that LLMs with more parameters, larger pretraining corpora, and extended training durations are expected to outperform previous models in capturing richer semantic representations.

- A paper on "Next-Embedding Prediction Makes Strong Vision Learners" discussing how images are decomposed into patches mapped to embeddings, with a causal transformer trained to predict the next embedding.

The specific combination of Voronoi coverage-based data selection for LLM pretraining may be a more specialized topic. If you're looking for that particular work, I'd recommend searching arXiv directly with more specific author names or checking recent preprints from papers on data selection and curriculum learning for LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1430f383-31be-4dee-bb50-ab15075f0d16",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "fc75404a-92df-4029-92ba-9ac7f3e3ac59",
  "toolUseResult": {
    "query": "embedding space Voronoi coverage pretraining data selection LLM 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VwfEW6Kfdn976fArGQbDs8",
        "content": [
          {
            "title": "Machine Learning May 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-05?skip=2125&show=2000"
          },
          {
            "title": "Machine Learning Jun 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-06?skip=1875&show=2000"
          },
          {
            "title": "Machine Learning Apr 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-04?skip=75&show=1000"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2405.17428"
          },
          {
            "title": "ICLR 2025 Papers",
            "url": "https://iclr.cc/virtual/2025/papers.html"
          },
          {
            "title": "Next-Embedding Prediction Makes Strong Vision Learners",
            "url": "https://arxiv.org/html/2512.16922v2"
          },
          {
            "title": "LLMs are Also Effective Embedding Models: An In-depth Overview",
            "url": "https://arxiv.org/html/2412.12591v2"
          },
          {
            "title": "Machine Learning Jul 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-07?skip=450&show=2000"
          },
          {
            "title": "Revealing the Numeracy Gap: An Empirical Investigation of Text Embedding Models",
            "url": "https://arxiv.org/html/2509.05691v1"
          },
          {
            "title": "When Text Embedding Meets Large Language Model: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2412.09165v1"
          }
        ]
      },
      "I've searched for papers related to \"embedding space Voronoi coverage pretraining data selection LLM\" for 2025-2026 on arXiv. Here's what I found:\n\nThe search returned several relevant results covering embedding spaces and LLMs from 2025-2026, though I didn't find a specific paper that directly combines all these concepts (Voronoi diagrams, embedding space coverage, and data selection for LLM pretraining).\n\nHowever, I did find one potentially relevant result: A paper titled \"Voronoi-grid-based Pareto Front Learning and Its Application to Collaborative Federated Learning\" by Mengmeng Chen, Xiaohu Wu, and others, which appears in the May 2025 Machine Learning arXiv listings.\n\nThe search also returned several papers on related topics:\n\n- Papers on embedding models and LLMs, including work on representation learning with LLMs, noting that LLMs with more parameters, larger pretraining corpora, and extended training durations are expected to outperform previous models in capturing richer semantic representations.\n\n- A paper on \"Next-Embedding Prediction Makes Strong Vision Learners\" discussing how images are decomposed into patches mapped to embeddings, with a causal transformer trained to predict the next embedding.\n\nThe specific combination of Voronoi coverage-based data selection for LLM pretraining may be a more specialized topic. If you're looking for that particular work, I'd recommend searching arXiv directly with more specific author names or checking recent preprints from papers on data selection and curriculum learning for LLMs."
    ],
    "durationSeconds": 7.190940843999997
  },
  "sourceToolAssistantUUID": "1430f383-31be-4dee-bb50-ab15075f0d16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-09T21:29:52.016Z_

<details><summary>↩ Tool result · `toolu_01AdnYLp3hDQSiJUXAA4Ybrt`</summary>

```text
Web search results for query: ""tail knowledge" "long-tail" synthetic pretraining data selection filtering 2026 arxiv"

Links: [{"title":"[2510.02375] Pretraining with hierarchical memories: separating long-tail and common knowledge","url":"https://arxiv.org/abs/2510.02375"},{"title":"Pretraining with hierarchical memories: separating long-tail and common knowledge","url":"https://arxiv.org/html/2510.02375v2"},{"title":"Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data","url":"https://www.arxiv.org/pdf/2509.15859"},{"title":"Pretraining with hierarchical memories: separating long-tail ...","url":"https://arxiv.org/pdf/2510.02375"},{"title":"A Systematic Review on Long-Tailed Learning","url":"https://arxiv.org/html/2408.00483v1"},{"title":"Continual Pretraining on Encrypted Synthetic Data for Privacy-Preserving LLMs","url":"https://arxiv.org/pdf/2601.05635"},{"title":"Computer Vision and Pattern Recognition 2025","url":"https://arxiv.org/list/cs.CV/2025?skip=33250&show=1000"},{"title":"Memory as a Markov Matrix: Sample Efficient Knowledge Expansion via Token-to-Dictionary Mapping","url":"https://arxiv.org/html/2605.04308"},{"title":"[2509.15859] Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data","url":"https://arxiv.org/abs/2509.15859"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"}]

Based on the web search results, I found several relevant papers and research related to tail knowledge, long-tail learning, and synthetic data in pretraining contexts:

## Key Findings:

**1. "Pretraining with hierarchical memories: separating long-tail and common knowledge"** (arXiv:2510.02375)

This paper's pretraining learns to store long-tail world knowledge in memory parameters, while a small language model acts as an anchor capturing common knowledge and general reasoning abilities. Through trillion-token-scale experiments, a 160M-parameters model augmented with an 18M-parameters memory fetched from a 4.6B memory bank obtains comparable performance to a regular model with more than 2x the parameters.

**2. "Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data"** (arXiv:2509.15859)

This work proposes a framework that leverages the rich semantic latent space of Vision Foundation Models to generate synthetic data and train a simple linear classifier using a mixture of real and synthetic data for long-tail classification.

**3. Long-Tail Data Handling Approaches**

Representative approaches include data resampling (which balances the number of samples in different classes), data augmentation (which expands the size of training data via transformation operations), and data synthesis (which generates synthetic samples using techniques such as GANs, distribution estimation/transfer methods, and foundation models).

These papers represent recent work (from 2025-2026) addressing challenges in handling tail knowledge and long-tail distributions through various pretraining and data synthesis strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06c474bf-bbb2-4718-8597-cea112bfa035",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "bf9a3f8c-c536-45cf-8a2b-98b82ababfdb",
  "toolUseResult": {
    "query": "\"tail knowledge\" \"long-tail\" synthetic pretraining data selection filtering 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XXuKvEfBZWJej3j3SCTFH3",
        "content": [
          {
            "title": "[2510.02375] Pretraining with hierarchical memories: separating long-tail and common knowledge",
            "url": "https://arxiv.org/abs/2510.02375"
          },
          {
            "title": "Pretraining with hierarchical memories: separating long-tail and common knowledge",
            "url": "https://arxiv.org/html/2510.02375v2"
          },
          {
            "title": "Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data",
            "url": "https://www.arxiv.org/pdf/2509.15859"
          },
          {
            "title": "Pretraining with hierarchical memories: separating long-tail ...",
            "url": "https://arxiv.org/pdf/2510.02375"
          },
          {
            "title": "A Systematic Review on Long-Tailed Learning",
            "url": "https://arxiv.org/html/2408.00483v1"
          },
          {
            "title": "Continual Pretraining on Encrypted Synthetic Data for Privacy-Preserving LLMs",
            "url": "https://arxiv.org/pdf/2601.05635"
          },
          {
            "title": "Computer Vision and Pattern Recognition 2025",
            "url": "https://arxiv.org/list/cs.CV/2025?skip=33250&show=1000"
          },
          {
            "title": "Memory as a Markov Matrix: Sample Efficient Knowledge Expansion via Token-to-Dictionary Mapping",
            "url": "https://arxiv.org/html/2605.04308"
          },
          {
            "title": "[2509.15859] Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data",
            "url": "https://arxiv.org/abs/2509.15859"
          },
          {
            "title": "Machine Learning May 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and research related to tail knowledge, long-tail learning, and synthetic data in pretraining contexts:\n\n## Key Findings:\n\n**1. \"Pretraining with hierarchical memories: separating long-tail and common knowledge\"** (arXiv:2510.02375)\n\nThis paper's pretraining learns to store long-tail world knowledge in memory parameters, while a small language model acts as an anchor capturing common knowledge and general reasoning abilities. Through trillion-token-scale experiments, a 160M-parameters model augmented with an 18M-parameters memory fetched from a 4.6B memory bank obtains comparable performance to a regular model with more than 2x the parameters.\n\n**2. \"Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data\"** (arXiv:2509.15859)\n\nThis work proposes a framework that leverages the rich semantic latent space of Vision Foundation Models to generate synthetic data and train a simple linear classifier using a mixture of real and synthetic data for long-tail classification.\n\n**3. Long-Tail Data Handling Approaches**\n\nRepresentative approaches include data resampling (which balances the number of samples in different classes), data augmentation (which expands the size of training data via transformation operations), and data synthesis (which generates synthetic samples using techniques such as GANs, distribution estimation/transfer methods, and foundation models).\n\nThese papers represent recent work (from 2025-2026) addressing challenges in handling tail knowledge and long-tail distributions through various pretraining and data synthesis strategies."
    ],
    "durationSeconds": 7.215882213999998
  },
  "sourceToolAssistantUUID": "06c474bf-bbb2-4718-8597-cea112bfa035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "bf9a3f8c-c536-45cf-8a2b-98b82ababfdb",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 8: Coverage-Guided Synthetic Data Selection",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

### Tool result

_source line 47 · 2026-05-09T21:29:52.282Z_

<details><summary>↩ Tool result · `toolu_01JB1gXZAUUuA33TAfStEtb4`</summary>

```text
Based on the provided content, I cannot find a paper specifically about "ADAPT," "online reweighting," or "offline methods" in pretraining authored by Zhao et al.

However, the webpage does list several relevant papers on data selection for LLM pretraining:

1. **"OPUS: Towards Principled and Scalable Data Selection for Large Language Model Pre-training in Every Iteration"** (ID: FEfuE1mAB6) - authored by Shaobo Wang and colleagues

2. **"Rethinking Data Selection: The Importance of Coverage over Difficulty in Generative Fine-Tuning"** (ID: qImiy98UhN) - by Lalchand Pandia, Kanishka Misra, and Allyson Ettinger

3. **"Winning the Pruning Gamble: A Unified Approach to Joint Sample and Token Pruning for Efficient Supervised Fine-Tuning"** (ID: 1ZzCzddCpB) - by Shaobo Wang and team members

The paper you're seeking does not appear on this particular page of the ICLR 2026 Workshop DATA-FM submissions list.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9bca007-6ad5-4bdc-a78a-816148c07342",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "910c76f6-81c7-419c-8896-ab78a768f622",
  "toolUseResult": {
    "bytes": 144895,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided content, I cannot find a paper specifically about \"ADAPT,\" \"online reweighting,\" or \"offline methods\" in pretraining authored by Zhao et al.\n\nHowever, the webpage does list several relevant papers on data selection for LLM pretraining:\n\n1. **\"OPUS: Towards Principled and Scalable Data Selection for Large Language Model Pre-training in Every Iteration\"** (ID: FEfuE1mAB6) - authored by Shaobo Wang and colleagues\n\n2. **\"Rethinking Data Selection: The Importance of Coverage over Difficulty in Generative Fine-Tuning\"** (ID: qImiy98UhN) - by Lalchand Pandia, Kanishka Misra, and Allyson Ettinger\n\n3. **\"Winning the Pruning Gamble: A Unified Approach to Joint Sample and Token Pruning for Efficient Supervised Fine-Tuning\"** (ID: 1ZzCzddCpB) - by Shaobo Wang and team members\n\nThe paper you're seeking does not appear on this particular page of the ICLR 2026 Workshop DATA-FM submissions list.",
    "durationMs": 5023,
    "url": "https://openreview.net/submissions?page=4&venue=ICLR.cc/2026/Workshop/DATA-FM"
  },
  "sourceToolAssistantUUID": "a9bca007-6ad5-4bdc-a78a-816148c07342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-09T21:29:55.916Z_

<details><summary>Logged reasoning block</summary>

```text
Let me check the ADAPT paper more carefully. The proposal claims:
- ADAPT is at "ICLR 2026 Workshop DATA-FM, openreview.net/forum?id=zgn3P31NWf"
- By "Zhao et al."

Let me fetch the specific OpenReview link to verify.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "910c76f6-81c7-419c-8896-ab78a768f622",
  "isSidechain": false,
  "requestId": "req_011CashxHLfCExCpQkd3XiAA",
  "type": "assistant",
  "uuid": "2ae7baca-5015-4bff-8ff0-e75fa68be761",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Dy89ZyfTmQ3MMXBkwGjyfn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 52097,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3334,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 52097,
          "cache_creation_input_tokens": 3334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3334
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

_source line 49 · 2026-05-09T21:29:57.411Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011Vs2Wgwgr96E2odeeNVStZ`</summary>

```json
{
  "url": "https://openreview.net/forum?id=zgn3P31NWf",
  "prompt": "What is the title, authors, and venue of this paper? Is it about online reweighting for LLM pretraining or data curation? What is its main contribution?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ae7baca-5015-4bff-8ff0-e75fa68be761",
  "isSidechain": false,
  "requestId": "req_011CashxHLfCExCpQkd3XiAA",
  "type": "assistant",
  "uuid": "c612fbe6-163c-4e17-b201-786b51b71b8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Dy89ZyfTmQ3MMXBkwGjyfn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 52097,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3334,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 52097,
          "cache_creation_input_tokens": 3334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3334
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

_source line 50 · 2026-05-09T21:29:58.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SFpCHFZEvuCg8AMseBCuyT`</summary>

```json
{
  "query": "\"data quality illusion\" \"classifier-based quality filtering\" LLM pretraining arXiv 2510.00866 ICLR 2026 rejected"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c612fbe6-163c-4e17-b201-786b51b71b8a",
  "isSidechain": false,
  "requestId": "req_011CashxHLfCExCpQkd3XiAA",
  "type": "assistant",
  "uuid": "676b667b-d759-4d64-a58a-b8d3a76b1bc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Dy89ZyfTmQ3MMXBkwGjyfn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 52097,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3334,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 52097,
          "cache_creation_input_tokens": 3334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3334
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

_source line 51 · 2026-05-09T21:29:59.224Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019F5r1V6n5N1BRein5pZkxW`</summary>

```json
{
  "query": "EMNLP 2026 ARR deadline May 25 submission deadline synthetic data special theme"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "676b667b-d759-4d64-a58a-b8d3a76b1bc3",
  "isSidechain": false,
  "requestId": "req_011CashxHLfCExCpQkd3XiAA",
  "type": "assistant",
  "uuid": "ada1a8f6-0ecf-4beb-91ec-ccb73235b900",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Dy89ZyfTmQ3MMXBkwGjyfn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 52097,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3334,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 52097,
          "cache_creation_input_tokens": 3334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3334
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

_source line 52 · 2026-05-09T21:30:00.572Z_

<details><summary>↩ Tool result · `toolu_011Vs2Wgwgr96E2odeeNVStZ`</summary>

```text
# Paper Summary

**Title:** "Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods"

**Authors:** Wanru Zhao, Yihong Chen, Yuzhi Tang, Wentao Ma, Shengchao Hu, Shell Xu Hu, Alex Iacob, Abhinav Mehrotra, and Nicholas D. Lane

**Venue:** ICLR 2026 Workshop DATA-FM

**Focus:** The paper addresses both data curation and online reweighting. It specifically proposes that "sample importance is dynamically adjusted during training via loss weighting rather than static preprocessing."

**Main Contribution:** The researchers introduce ADAPT (Adaptive Data reweighting for Pretraining and FineTuning), a framework that performs dynamic online reweighting of training samples using "adaptive per-sample learning rates guided by similarity-based quality signals." This approach preserves dataset diversity while adapting continuously during model training, achieving superior generalization compared to traditional offline selection and mixing methods across instruction tuning and large-scale pretraining tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c612fbe6-163c-4e17-b201-786b51b71b8a",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "7c1d8cda-d268-41d1-8494-7f10b5b4e18f",
  "toolUseResult": {
    "bytes": 69508,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** \"Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods\"\n\n**Authors:** Wanru Zhao, Yihong Chen, Yuzhi Tang, Wentao Ma, Shengchao Hu, Shell Xu Hu, Alex Iacob, Abhinav Mehrotra, and Nicholas D. Lane\n\n**Venue:** ICLR 2026 Workshop DATA-FM\n\n**Focus:** The paper addresses both data curation and online reweighting. It specifically proposes that \"sample importance is dynamically adjusted during training via loss weighting rather than static preprocessing.\"\n\n**Main Contribution:** The researchers introduce ADAPT (Adaptive Data reweighting for Pretraining and FineTuning), a framework that performs dynamic online reweighting of training samples using \"adaptive per-sample learning rates guided by similarity-based quality signals.\" This approach preserves dataset diversity while adapting continuously during model training, achieving superior generalization compared to traditional offline selection and mixing methods across instruction tuning and large-scale pretraining tasks.",
    "durationMs": 3159,
    "url": "https://openreview.net/forum?id=zgn3P31NWf"
  },
  "sourceToolAssistantUUID": "c612fbe6-163c-4e17-b201-786b51b71b8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-09T21:30:05.060Z_

<details><summary>↩ Tool result · `toolu_019F5r1V6n5N1BRein5pZkxW`</summary>

```text
Web search results for query: "EMNLP 2026 ARR deadline May 25 submission deadline synthetic data special theme"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"}]

I found relevant information about EMNLP 2026. Here are the key details:

## ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## Special Theme

EMNLP 2026 has a special theme focused on two areas:

1. **Data as a bottleneck and a responsibility**: Research on data scarcity and limits, contamination, and the consequences of synthetic data feedback loops, and new approaches to data creation, documentation, governance, and consent.

2. **LLMs as research tools**: Rigorous studies of how LLMs can support the research process in hypothesis generation, experiment design, analysis, and peer review support tools without eroding scientific standards.

This special theme is intended to complement the breadth of EMNLP, not narrow it.

## Important Dates

The reviewer registration deadline for all authors is May 27, 2026, with author response and author-reviewer discussion from July 7-13, 2026.

## Review Process

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, where authors submit articles to ARR to receive reviews and meta-reviews, and then commit their reviewed articles to EMNLP 2026 for final acceptance decisions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ada1a8f6-0ecf-4beb-91ec-ccb73235b900",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "af44bcc3-2e65-4aa4-bb14-ec101d4422c9",
  "toolUseResult": {
    "query": "EMNLP 2026 ARR deadline May 25 submission deadline synthetic data special theme",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JqXqM6j62h5f3rKfjd1cwR",
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
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X",
            "url": "https://x.com/emnlpmeeting/status/2029508292637061462"
          },
          {
            "title": "EMNLP 2026 Conference Deadline | Live Countdown Tracker",
            "url": "https://www.getpaperpilot.com/deadlines/emnlp-2026.html"
          },
          {
            "title": "EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin",
            "url": "https://www.getpaperpin.com/deadlines/emnlp26"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"
          },
          {
            "title": "EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X",
            "url": "https://x.com/emnlpmeeting/status/1892259536137785419"
          }
        ]
      },
      "I found relevant information about EMNLP 2026. Here are the key details:\n\n## ARR Submission Deadline\n\nThe ARR submission deadline for EMNLP 2026 is May 25, 2026.\n\n## Special Theme\n\nEMNLP 2026 has a special theme focused on two areas:\n\n1. **Data as a bottleneck and a responsibility**: Research on data scarcity and limits, contamination, and the consequences of synthetic data feedback loops, and new approaches to data creation, documentation, governance, and consent.\n\n2. **LLMs as research tools**: Rigorous studies of how LLMs can support the research process in hypothesis generation, experiment design, analysis, and peer review support tools without eroding scientific standards.\n\nThis special theme is intended to complement the breadth of EMNLP, not narrow it.\n\n## Important Dates\n\nThe reviewer registration deadline for all authors is May 27, 2026, with author response and author-reviewer discussion from July 7-13, 2026.\n\n## Review Process\n\nEMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, where authors submit articles to ARR to receive reviews and meta-reviews, and then commit their reviewed articles to EMNLP 2026 for final acceptance decisions."
    ],
    "durationSeconds": 5.8314493339999895
  },
  "sourceToolAssistantUUID": "ada1a8f6-0ecf-4beb-91ec-ccb73235b900",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-09T21:30:07.333Z_

<details><summary>↩ Tool result · `toolu_01SFpCHFZEvuCg8AMseBCuyT`</summary>

```text
Web search results for query: ""data quality illusion" "classifier-based quality filtering" LLM pretraining arXiv 2510.00866 ICLR 2026 rejected"

Links: [{"title":"[2510.00866] The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining","url":"https://arxiv.org/abs/2510.00866"},{"title":"The data-quality illusion: Rethinking Classifier-based quality filtering for LLM Pretraining","url":"https://arxiv.org/html/2510.00866v1"},{"title":"Paper page - The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining","url":"https://huggingface.co/papers/2510.00866"},{"title":"(PDF) The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining","url":"https://www.researchgate.net/publication/396094723_The_data-quality_illusion_Rethinking_Classifier-based_quality_filtering_for_LLM_Pretraining"},{"title":"[Literature Review] The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining","url":"https://www.themoonlight.io/en/review/the-data-quality-illusion-rethinking-classifier-based-quality-filtering-for-llm-pretraining"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=22100&show=500"},{"title":"HyperCLOVA X 32B Think","url":"https://arxiv.org/html/2601.03286v1"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=100&show=250"},{"title":"The data-quality illusion: Rethinking Classifier-based Quality Filtering for LLM Pretraining | OpenReview","url":"https://openreview.net/forum?id=vSBACt34gS"},{"title":"RETHINKING CLASSIFIER-BASED QUALITY FILTERING ...","url":"https://openreview.net/pdf/dc51db328981b32d91ba5eb0caa17183286e4c7a.pdf"}]

I found the paper! Based on the search results, I can provide you with information about this research:

## Paper Overview

The paper titled "The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining" is arXiv paper 2510.00866. It was submitted on October 1, 2025, with authors including Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, and Pierre Ablin.

## Main Contributions

The paper analyzes Classifier-based Quality Filtering (CQF), which trains a binary classifier to distinguish between pretraining data and a small, high-quality set, assigning each pretraining document a quality score and retaining only the top-scoring ones.

The paper's key finding is notable: while CQF improves downstream task performance, it does not necessarily enhance language modeling on the high-quality dataset, and this paradox is explained by the fact that CQF implicitly filters the high-quality dataset as well.

## Submission Status

The paper was under review as a conference paper at ICLR 2026 (according to the OpenReview submission information). The search results show it's currently a preprint on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "676b667b-d759-4d64-a58a-b8d3a76b1bc3",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "6d688828-e9df-4363-983b-6086ecb2eddb",
  "toolUseResult": {
    "query": "\"data quality illusion\" \"classifier-based quality filtering\" LLM pretraining arXiv 2510.00866 ICLR 2026 rejected",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QxXNN4nvm7EDNXVkUPWQCA",
        "content": [
          {
            "title": "[2510.00866] The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining",
            "url": "https://arxiv.org/abs/2510.00866"
          },
          {
            "title": "The data-quality illusion: Rethinking Classifier-based quality filtering for LLM Pretraining",
            "url": "https://arxiv.org/html/2510.00866v1"
          },
          {
            "title": "Paper page - The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining",
            "url": "https://huggingface.co/papers/2510.00866"
          },
          {
            "title": "(PDF) The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining",
            "url": "https://www.researchgate.net/publication/396094723_The_data-quality_illusion_Rethinking_Classifier-based_quality_filtering_for_LLM_Pretraining"
          },
          {
            "title": "[Literature Review] The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining",
            "url": "https://www.themoonlight.io/en/review/the-data-quality-illusion-rethinking-classifier-based-quality-filtering-for-llm-pretraining"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=22100&show=500"
          },
          {
            "title": "HyperCLOVA X 32B Think",
            "url": "https://arxiv.org/html/2601.03286v1"
          },
          {
            "title": "Machine Learning Oct 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-10?skip=100&show=250"
          },
          {
            "title": "The data-quality illusion: Rethinking Classifier-based Quality Filtering for LLM Pretraining | OpenReview",
            "url": "https://openreview.net/forum?id=vSBACt34gS"
          },
          {
            "title": "RETHINKING CLASSIFIER-BASED QUALITY FILTERING ...",
            "url": "https://openreview.net/pdf/dc51db328981b32d91ba5eb0caa17183286e4c7a.pdf"
          }
        ]
      },
      "I found the paper! Based on the search results, I can provide you with information about this research:\n\n## Paper Overview\n\nThe paper titled \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\" is arXiv paper 2510.00866. It was submitted on October 1, 2025, with authors including Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, and Pierre Ablin.\n\n## Main Contributions\n\nThe paper analyzes Classifier-based Quality Filtering (CQF), which trains a binary classifier to distinguish between pretraining data and a small, high-quality set, assigning each pretraining document a quality score and retaining only the top-scoring ones.\n\nThe paper's key finding is notable: while CQF improves downstream task performance, it does not necessarily enhance language modeling on the high-quality dataset, and this paradox is explained by the fact that CQF implicitly filters the high-quality dataset as well.\n\n## Submission Status\n\nThe paper was under review as a conference paper at ICLR 2026 (according to the OpenReview submission information). The search results show it's currently a preprint on arXiv."
    ],
    "durationSeconds": 8.777246667
  },
  "sourceToolAssistantUUID": "676b667b-d759-4d64-a58a-b8d3a76b1bc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-09T21:33:08.311Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now summarize the key findings from my searches:

1. **ModernBERT throughput**: CONFIRMED - ~52.3K tokens/sec on RTX 4090 at 512 tokens. The proposal's claim of "~52K tokens/sec" is accurate. The H100 "2-4×" multiplier claim is plausible based on memory bandwidth ratios but is not directly cited. However, the proposal now has a throughput pilot test as a safeguard.

2. **QuaDMix withdrawal status**: CONFIRMED - OpenReview explicitly says "ICLR 2026 Conference Withdrawn Submission." The proposal is correct to say "withdrawn from ICLR 2026."


3. **arXiv:2604.13977**: Verified - the paper does show that structured output formats like tables and math problems outperform curated web baselines and prior synthetic methods, matching the proposal's characterization.

4. **AC-ODM and ADAPT**: Both papers exist and are correctly referenced - AC-ODM at arXiv:2505.23878 and ADAPT at the ICLR 2026 Workshop DATA-FM by Wanru Zhao et al.

5. Now checking the EMNLP 2026 ARR deadline...

The May 25, 2026 deadline is confirmed, and the special theme about data contamination and synthetic data feedback loops checks out. For arXiv:2510.00866, the OpenReview submission shows a January 22 decision date, and since it doesn't appear in accepted paper lists, the proposal's characterization of it as "rejected from ICLR 2026; preprint" appears accurate.

Now I'm reviewing what's been fixed across the rounds—the venue claim for 2510.00866 is corrected, QuaDMix's withdrawal status is verified, the landscape section properly differentiates arXiv:2502.02494, and several missing papers and metrics have been added including Group-MATES, diversity measures like self-BLEU and n-gram entropy, plus ADAPT, AC-ODM, EntiGraph, and hierarchical memories. Checking the throughput claims more carefully—the proposal cites an H100 product brief to justify the 2–4× speedup over RTX 4090 for encoder inference, which underpins the 100-200K tok/s estimate, but I need to verify whether that source actually supports this specific claim or if it's an overreach. The throughput pilot helps address that concern. For the synthetic data generation using Qwen3-72B, creating 30M tokens across three corpora would be costly—a 72B model needs substantial compute, likely multiple H100s, and even at reasonable token generation speeds of 200-400 tokens per second, the inference costs add up quickly. I'm realizing there's a distinction between the 7.68B tokens used to generate the fixed 15M-document pool (which is precomputed) and the 30M tokens needed for Experiment 0's three synthetic corpora—these are separate generation tasks, and I need to figure out which one actually fits within the ~2 H100-hour budget. synthetic pool is precomputed separately (not included in Exp 0 runtime), and Exp 0 generates 3 small corpora (10M tokens each = 30M total) for validation purposes.

But what's the cost of generating those 30M tokens? That could be substantial and doesn't seem to be accounted for in the ~2 H100-hour estimate for Experiment 0.

Actually, the "~2 H100-hours" for Experiment 0 is only for the embedding part (to validate the embedding approach). The synthetic generation for the 15M-document pool (7.68B tokens) and the 30M validation tokens would be a separate cost!

Wait, let me re-read: "Total GPU wall-clock: ~2h (Exp 0) + ~8.8h (embedding) + ~18h (Tier 1) + ~22h (Tier 2) ≈ 50.8h ≈ 2.1 days."

The embedding step includes embedding the 15M synthetic docs AND the reference corpus. But where does the GENERATION of the 15M synthetic docs happen? The 7.68B-token synthetic pool needs to be GENERATED first using Qwen3-72B!

I'm realizing the synthetic data generation cost is massive—at typical inference speeds, generating 7.68B tokens with a 72B model would require thousands of GPU-hours, which seems completely infeasible and isn't reflected in the reported timeline. Let me reconsider whether batch inference with optimized setups like vLLM could dramatically improve throughput. 5,000-10,000 tok/s at batch sizes of 256
- At 8,000 tok/s: 7.68B ÷ 8,000 = 960,000s = ~267 H100-hours per GPU pair? That's still too high.

Actually, for generating 7.68B tokens with Qwen3-72B on 4×H100:
- Using vLLM with BF16: Qwen3-72B might achieve ~2,000-5,000 tok/s total on 4×H100
- At 4,000 tok/s total: 7.68B ÷ 4,000 = 1.92M seconds ≈ 533 hours / (4 GPUs) = 133 GPU-hours per GPU... that's still huge.

Wait, I'm realizing the proposal glosses over generating the synthetic data entirely—it just says embeddings are precomputed for a 15M-document pool as if that generation cost doesn't exist. But if this is starting from scratch, generating 7.68B tokens with Qwen3-72B could easily add hundreds of GPU-hours that aren't accounted for in the budget. Unless they're using the API instead of running it locally, or assuming generation is essentially free somehow. Looking back at the resource estimate, it only lists ~175 H100-hours for auto_research, with embedding at ~35 hours, but there's no line item for the actual synthetic data generation. The word "precompute" suggests this is a separate step outside the main 16-day pipeline, but that raises the question of when this data generation actually happens. If they're using an API like Together AI for Qwen3-72B generation, the cost would be substantial—around $6,912 for 7.68B tokens—yet this isn't mentioned in the resource estimates. Alternatively, if they're generating on the H100 cluster itself, the time cost would be prohibitive given the model size and token volume.

Looking at the actual numbers: generating 7.68B tokens on 4×H100s would take roughly 1,200 GPU-hours, which far exceeds the proposal's estimated 175 total GPU hours for the entire auto_research task. This suggests either the proposal is using API generation (with costs hidden in the API budget) or there's a significant budget oversight.

But examining Experiment 0(a) more closely, it only calls for generating 30M tokens across three synthetic corpora—a much smaller subset. Even that would consume around 5 GPU-hours just for generation alone, which is still substantial relative to the overall budget constraints.

The real tension here is that the proposal doesn't explicitly account for where this generation happens. If Qwen3-72B is being called via API, that cost should be itemized separately. If it's running locally on the H100s, the GPU-hour budget is significantly underestimated. I'm noticing this inconsistency hasn't been addressed in the proposal, and I should investigate whether there are existing pre-generated synthetic corpora from Qwen that could sidestep this problem entirely. wasn't mentioned in the budget. Let me verify whether Qwen3-72B is actually available through a cost-effective inference API, since that's a critical assumption for the synthetic data generation cost.

I'm also noticing a few other gaps: the proposal describes selecting 5,000 Wikidata documents based on entity frequency thresholds from C4, but the data preparation work to construct that filtered set—counting frequencies, filtering entities, fetching documents—isn't accounted for in the timeline, though the small dataset size might make it manageable. Additionally, there's a performance assumption about ModernBERT-large throughput on RTX 4090 that I should examine more closely.

The claim that H100 SXM delivers 2–4× the throughput of RTX 4090 for encoder inference depends heavily on batch size and memory bandwidth utilization. Looking at the specs, H100 SXM5 has roughly 3.3× the memory bandwidth advantage over RTX 4090, while the compute advantage is much larger but less relevant since encoder inference is memory-bandwidth-bound rather than compute-bound. So the 2–4× claim seems defensible for this workload.

Now I'm noticing a critical gap: the proposal generates 15M documents using Qwen3-72B but doesn't account for this generation cost at all. That's either ~$6,900+ if done via API, or requires ~1,200 GPU-hours locally—both of which would massively exceed the stated budget. I need to figure out if this is actually the main unresolved issue or if there's something else I'm overlooking in how the proposal structures this. So the wall-clock time for local generation would be around 133 hours across 4 GPUs, which is impractical. This means the proposal must be relying on API-based generation instead. The timeline for auto-research mode is 8-12 days, and API generation could take several days depending on rate limits. The real issue is that while the proposal lists `claude_api_cost` separately, it doesn't actually include the generation API cost in the resource estimates—that's a significant gap that needs to be addressed.

Looking at the proposal text, it mentions generating a 15M-document synthetic pool with Qwen3-72B but never specifies where this happens or what it costs. If done via API, that's roughly $6,900; if done locally, it exceeds the GPU budget. The proposal explicitly calls for Qwen3-72B for generation, so this cost should be accounted for. There might be some wiggle room if they use a smaller model or leverage existing synthetic datasets, but as written, the resource estimate is incomplete.

Now I'm noticing another issue with the core empirical claim...

the proposal hedges by saying the finding about CQF performance gains not matching perplexity improvements is reproducible from first principles and doesn't depend on the paper's peer review status. That's reasonable, but a reviewer might still question what the ICLR 2026 rejection signals about the claim's reliability. The proposal does acknowledge the rejection and includes the replicability hedge, which seems like adequate coverage for a preprint citation, though it could be stronger.

I'm also spotting a new concern—there's a citation to arXiv:2511.13640 that appears to be incomplete or cut off in how it's being referenced. The proposal has been substantially refined through multiple rounds and addresses most concerns—the CGS method is genuinely novel, the budget math checks out, and key citations like QuaDMix's ICLR withdrawal and ModernBERT's throughput are verified. The evaluation plan is solid with TriviaQA as the primary benchmark. However, there's a critical gap: the generation cost for 7.68B tokens using Qwen3-72B isn't accounted for, which would run roughly $6,900 in API fees or hundreds of GPU-hours if computed locally.

The H100 throughput claim against RTX 4090 lacks precise sourcing, and I should independently verify arXiv:2511.13640. But stepping back, the core question is whether the Qwen3 generation cost is a fatal flaw or a disclosure issue—the proposal focuses on the selection method itself rather than generation, so this feels like a resource underestimate that should have been flagged rather than a methodological problem.

I'm realizing the choice of Qwen3-72B is an implementation detail; they could've used smaller models like Qwen3-7B or Mistral-7B instead, which would bring generation costs down to around 21 GPU-hours—totally manageable. But since the proposal explicitly specifies Qwen3-72B and claims only ~2 GPU-hours for generating 30M tokens in Experiment 0, that's only consistent if they're using an API, which they don't mention.

The core issue is real and fixable: the resource estimate doesn't account for the actual cost of generating 7.68B tokens with a 72B model. Given this is Round 8 of 10 and they've addressed nearly everything else, I need to weigh whether this gap is significant enough to push back again or let it pass.

Since the novelty lies in the selection mechanism rather than the generation itself, this could be resolved by clarifying whether they're using an API (and disclosing costs), switching to a smaller generation model, or leveraging pre-existing synthetic data. The previous round's issues have been properly addressed, so I'm inclined toward another focused revision rather than rejection.

Now I'm assessing whether CGS is genuinely novel compared to related work. The key differentiators seem to be the cross-corpus density gap approach, the focus on tail samples rather than just diversity, avoiding the need for influence model training, and the mechanistic grounding in why CQF fails. These elements do appear to constitute real novelty in the space.

The main practical concern is the unaccounted generation cost for the 15M synthetic documents—either around $6,900 in API fees or 500+ GPU-hours locally, both of which exceed what's been disclosed. It's a solvable problem though: I could disclose the API cost, use a smaller generation model, or leverage existing synthetic datasets instead. Since this is round 8 and the issue is fixable rather than fundamental to the method itself, I'm leaning toward a revise verdict with targeted feedback on this specific gap.

But let me think through this more carefully. The resource estimate lists about 175 H100-hours and $427-623 in costs, but that doesn't account for the Qwen3-72B generation—which would add roughly $6,900 via an API like Together AI, bringing the total research cost to around $7,500-7,900. The validation tokens for Experiment 0 would add another $27 or so. These costs should be explicitly included in the resource estimate.

That said, I want to be fair about this—many papers in this space use similar approaches without always fully itemizing every generation cost.

If the proposal switched to Qwen3-7B instead, the math changes significantly. Using an API would cost around $461, or running it locally on an H100 would take roughly 21 GPU-hours. Either way, that's much more feasible within the stated budget.

The core issue is that the proposal explicitly relies on Qwen3-72B for generation quality, yet the resource estimate completely omits this cost. A reviewer will definitely catch that discrepancy. I'm settling on a REVISE verdict with a novelty score of 4.

The method itself is genuinely novel—combining cross-corpus density gap targeting, tail-threshold gating, and the CQF failure mechanism in this way is a real contribution. Feasibility drops to 3 though, since the selection pipeline works within budget but the generation step either costs ~$6,900 via API or requires 500+ GPU-hours locally, neither of which is addressed. Clarity stays at 4 given how detailed and well-structured the proposal is after multiple rounds, and impact is 4 since it tackles a hot EMNLP 2026 special theme with a principled approach.

That averages to 3.75, which falls below the 4.0 threshold, so revise it is. The generation cost is the blocker here.

Actually, the fix is straightforward—swap in a smaller model like Qwen3-7B or Mistral-7B-Instruct instead of the 72B version. The core claim is about selection quality through CGS versus CQF, not about which generation model size you use. Research shows that generation model size matters less than the selection mechanism itself, so this swap shouldn't undermine the proposal's actual contribution. The second issue is that the H100 performance claim relies on a product brief that measures training throughput on matrix multiplication benchmarks, not the actual encoder inference throughput being used here — so that comparison may not be valid.

I'm verifying whether the cited paper actually says that generator models beyond 1B parameters provide no benefit, since if it does, that directly contradicts using Qwen3-72B. The search results confirm this claim is in the paper, which means the resource estimate is using a model choice that the cited literature explicitly argues against. I have enough to formulate my verdict now, with the generation cost discrepancy being the core issue. The generation cost issue is actually fixable with a simple downgrade to Qwen3-7B, which the proposal's own citations support, so maybe feasibility deserves a 4 instead of a 3—the core method is sound, just the implementation choice needs adjustment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d688828-e9df-4363-983b-6086ecb2eddb",
  "isSidechain": false,
  "requestId": "req_011CashyPV2kr6xtADWryrFt",
  "type": "assistant",
  "uuid": "ac8d86a6-5bc6-468a-86fa-0b8117c8e5fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015tFmWBCiAcDw6GuDFujJtL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1024,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 55431,
      "output_tokens": 9845,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1024,
          "output_tokens": 9845,
          "cache_read_input_tokens": 55431,
          "cache_creation_input_tokens": 1567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1567
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

_source line 56 · 2026-05-09T21:33:08.313Z_

Let me verify one more critical claim before issuing my verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac8d86a6-5bc6-468a-86fa-0b8117c8e5fe",
  "isSidechain": false,
  "requestId": "req_011CashyPV2kr6xtADWryrFt",
  "type": "assistant",
  "uuid": "b2d7f5b4-7692-4804-86da-0b0b29be3b49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015tFmWBCiAcDw6GuDFujJtL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1024,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 55431,
      "output_tokens": 9845,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1024,
          "output_tokens": 9845,
          "cache_read_input_tokens": 55431,
          "cache_creation_input_tokens": 1567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1567
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

_source line 57 · 2026-05-09T21:33:09.470Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01A7fz6cLPy29vtQWDaYj8Ko`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.13977",
  "prompt": "Does this paper say anything about the effect of generator model size on synthetic pretraining quality? Specifically, does it say that increasing generator model size beyond a certain parameter count provides no additional benefit? Quote the relevant finding exactly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2d7f5b4-7692-4804-86da-0b0b29be3b49",
  "isSidechain": false,
  "requestId": "req_011CashyPV2kr6xtADWryrFt",
  "type": "assistant",
  "uuid": "134240ae-472a-435f-8c70-67b8df13c5c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015tFmWBCiAcDw6GuDFujJtL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1024,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 55431,
      "output_tokens": 9845,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1024,
          "output_tokens": 9845,
          "cache_read_input_tokens": 55431,
          "cache_creation_input_tokens": 1567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1567
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

_source line 58 · 2026-05-09T21:33:10.272Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MKNqhu7FuDdgpj3NsKYKgj`</summary>

```json
{
  "query": "arXiv 2511.13640 \"data value\" \"scaling\" synthetic real mixture LLM pretraining tail underrepresentation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "134240ae-472a-435f-8c70-67b8df13c5c6",
  "isSidechain": false,
  "requestId": "req_011CashyPV2kr6xtADWryrFt",
  "type": "assistant",
  "uuid": "9f9880dd-e926-472d-aa37-dcb420934591",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015tFmWBCiAcDw6GuDFujJtL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1024,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 55431,
      "output_tokens": 9845,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1024,
          "output_tokens": 9845,
          "cache_read_input_tokens": 55431,
          "cache_creation_input_tokens": 1567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1567
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

_source line 59_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "9f9880dd-e926-472d-aa37-dcb420934591",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 8: Coverage-Guided Synthetic Data Selection",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

### Tool result

_source line 61 · 2026-05-09T21:33:12.124Z_

<details><summary>↩ Tool result · `toolu_01A7fz6cLPy29vtQWDaYj8Ko`</summary>

```text
Yes, the paper addresses this question. According to the abstract, the relevant finding is:

"Notably, increasing the size of the generator model beyond 1B parameters provides no additional benefit."

This indicates that generator models with more than 1 billion parameters do not yield improved results for synthetic pretraining data quality in their study.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "134240ae-472a-435f-8c70-67b8df13c5c6",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "cb0edc02-ae2b-4938-bee8-28db3ef28ffe",
  "toolUseResult": {
    "bytes": 47946,
    "code": 200,
    "codeText": "OK",
    "result": "Yes, the paper addresses this question. According to the abstract, the relevant finding is:\n\n\"Notably, increasing the size of the generator model beyond 1B parameters provides no additional benefit.\"\n\nThis indicates that generator models with more than 1 billion parameters do not yield improved results for synthetic pretraining data quality in their study.",
    "durationMs": 2647,
    "url": "https://arxiv.org/abs/2604.13977"
  },
  "sourceToolAssistantUUID": "134240ae-472a-435f-8c70-67b8df13c5c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-09T21:33:17.790Z_

<details><summary>↩ Tool result · `toolu_01MKNqhu7FuDdgpj3NsKYKgj`</summary>

```text
Web search results for query: "arXiv 2511.13640 "data value" "scaling" synthetic real mixture LLM pretraining tail underrepresentation"

Links: [{"title":"Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real–Synthetic Data Mixtures","url":"https://arxiv.org/html/2511.13640"},{"title":"[2511.13640] Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures","url":"https://arxiv.org/abs/2511.13640"},{"title":"Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation","url":"https://arxiv.org/html/2602.07298"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls","url":"https://arxiv.org/html/2510.01631"},{"title":"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/html/2403.16952v2"},{"title":"[2605.02364] InfoLaw: Information Scaling Laws for Large Language Models with Quality-Weighted Mixture Data and Repetition","url":"https://arxiv.org/abs/2605.02364"},{"title":"Scaling Laws for Optimal Data Mixtures","url":"https://arxiv.org/html/2507.09404v1"},{"title":"RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold","url":"https://arxiv.org/html/2406.14532v1"},{"title":"Scaling Laws of Synthetic Data for Language Models","url":"https://arxiv.org/html/2503.19551v2"},{"title":"[2510.01631] Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls","url":"https://arxiv.org/abs/2510.01631"}]

I found the paper you're looking for! Here's the information about arXiv 2511.13640:

## Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures

This paper is titled "Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures" and was published on November 17, 2025.

### Key Findings:

The paper addresses how synthetic data offers scalability and cost-efficiency, but it often introduces systematic distributional discrepancies, particularly underrepresenting long-tail knowledge due to truncation effects from data generation mechanisms like top-p sampling, temperature scaling, and finite sampling.

**Three-Phase Scaling Behavior:** The authors identify a three-phase scaling behavior characterized by two breakpoints that reflect transitions in model behavior across learning head and tail knowledge.

**Theoretical Contributions:** They derive an LLM generalization bound designed for real and synthetic mixtures, revealing several key factors that govern their generalization performance.

**Data Valuation Method:** Building on their theoretical findings, they propose an effective yet efficient data valuation method that scales to large-scale datasets, with comprehensive experiments across four tasks (image classification, sentiment classification, instruction following, and complex reasoning) demonstrating that their method surpasses state-of-the-art baselines in data valuation with significantly low computational cost.

You can access the full paper at https://arxiv.org/abs/2511.13640 or view the HTML version at https://arxiv.org/html/2511.13640.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f9880dd-e926-472d-aa37-dcb420934591",
  "isSidechain": false,
  "promptId": "1fa12423-3d1a-4e8a-b311-877a01ded964",
  "type": "user",
  "uuid": "f5ae69aa-a8a4-4a05-9f4d-748da6752860",
  "toolUseResult": {
    "query": "arXiv 2511.13640 \"data value\" \"scaling\" synthetic real mixture LLM pretraining tail underrepresentation",
    "results": [
      {
        "tool_use_id": "srvtoolu_018sdqd6s4WYnWzwY5siHR1F",
        "content": [
          {
            "title": "Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real–Synthetic Data Mixtures",
            "url": "https://arxiv.org/html/2511.13640"
          },
          {
            "title": "[2511.13640] Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures",
            "url": "https://arxiv.org/abs/2511.13640"
          },
          {
            "title": "Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation",
            "url": "https://arxiv.org/html/2602.07298"
          },
          {
            "title": "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls",
            "url": "https://arxiv.org/html/2510.01631"
          },
          {
            "title": "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance",
            "url": "https://arxiv.org/html/2403.16952v2"
          },
          {
            "title": "[2605.02364] InfoLaw: Information Scaling Laws for Large Language Models with Quality-Weighted Mixture Data and Repetition",
            "url": "https://arxiv.org/abs/2605.02364"
          },
          {
            "title": "Scaling Laws for Optimal Data Mixtures",
            "url": "https://arxiv.org/html/2507.09404v1"
          },
          {
            "title": "RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold",
            "url": "https://arxiv.org/html/2406.14532v1"
          },
          {
            "title": "Scaling Laws of Synthetic Data for Language Models",
            "url": "https://arxiv.org/html/2503.19551v2"
          },
          {
            "title": "[2510.01631] Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls",
            "url": "https://arxiv.org/abs/2510.01631"
          }
        ]
      },
      "I found the paper you're looking for! Here's the information about arXiv 2511.13640:\n\n## Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures\n\nThis paper is titled \"Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures\" and was published on November 17, 2025.\n\n### Key Findings:\n\nThe paper addresses how synthetic data offers scalability and cost-efficiency, but it often introduces systematic distributional discrepancies, particularly underrepresenting long-tail knowledge due to truncation effects from data generation mechanisms like top-p sampling, temperature scaling, and finite sampling.\n\n**Three-Phase Scaling Behavior:** The authors identify a three-phase scaling behavior characterized by two breakpoints that reflect transitions in model behavior across learning head and tail knowledge.\n\n**Theoretical Contributions:** They derive an LLM generalization bound designed for real and synthetic mixtures, revealing several key factors that govern their generalization performance.\n\n**Data Valuation Method:** Building on their theoretical findings, they propose an effective yet efficient data valuation method that scales to large-scale datasets, with comprehensive experiments across four tasks (image classification, sentiment classification, instruction following, and complex reasoning) demonstrating that their method surpasses state-of-the-art baselines in data valuation with significantly low computational cost.\n\nYou can access the full paper at https://arxiv.org/abs/2511.13640 or view the HTML version at https://arxiv.org/html/2511.13640."
    ],
    "durationSeconds": 7.514785780000035
  },
  "sourceToolAssistantUUID": "9f9880dd-e926-472d-aa37-dcb420934591",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-09T21:33:50.883Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important! I found a significant issue:

arXiv:2511.13640 ("Data Value in the Age of Scaling") is described in the proposal as: "identifies tail-knowledge underrepresentation as a systematic distributional discrepancy in synthetic data under real-synthetic mixing, linked to generative truncation mechanisms"

And from my search, I confirm this is real. The paper DOES say that synthetic data "often introduces systematic distributional discrepancies, particularly underrepresenting long-tail knowledge due to truncation effects from data generation mechanisms like top-p sampling, temperature scaling, and finite sampling."


So the characterization is correct.

Now I'm looking at arXiv:2604.13977, which makes a critical claim: increasing generator model size beyond 1B parameters provides no additional benefit. The proposal cites this as evidence that principled generation choices matter more than classifier-based selection, yet it uses Qwen3-72B—a 72B parameter model—to generate the 15M synthetic document pool. This directly contradicts the cited work's finding that larger models don't help.

This creates a real inconsistency: the proposal's own corroboration says generator size doesn't matter beyond 1B, but it uses a model 72 times larger. If the cited paper is correct, using Qwen3-7B or Qwen3-1.5B would be empirically justified, solve the computational overhead problem, and align with the proposal's own literature. This is a genuine remaining issue I need to factor into my assessment.

Now I'm verifying the proposal's key claims against external sources. I've confirmed several citations check out: QuaDMix's withdrawal from ICLR 2026, ModernBERT's throughput metrics, and the existence of the referenced papers on synthetic data generation and model adaptation. The citations appear to be accurate where I can verify them.

But I'm finding a critical inconsistency: the proposal cites arXiv:2604.13977, which explicitly states that generator models beyond 1B parameters don't provide additional benefits, yet the proposal itself uses Qwen3-72B—a 72 billion parameter model—for generation. Beyond the theoretical contradiction, this creates a massive practical problem: generating 7.68B tokens with a 72B model would cost either around $6,900 in API fees or require 500+ GPU-hours locally, neither of which appears to be accounted for in the proposal's budget or methodology.

The solution is straightforward and supported by the cited literature itself: switch to Qwen3-7B or Qwen3-1.5B for generation instead. This is a one-paragraph fix that resolves both the theoretical contradiction and the budget overrun.

Looking at the overall scoring, the novelty is solid at 4—the cross-corpus tail-density gating approach is genuinely novel and clearly differentiated from existing work like Less is More, Quad, and MATES. The feasibility score of 3 reflects this core issue: while the CGS selection and training pipeline fits within the 200-hour budget, the corpus generation step either becomes infeasible locally or introduces undisclosed costs that contradict the proposal's own cited evidence.

The clarity and impact ratings are both strong at 4, but there's a subtle issue I'm noticing with how the proposal interprets the cited work. The paper arXiv:2604.13977 is being used to argue that "principled generation choices matter more than classifier-based selection," but what it actually demonstrates is that structured output formats are what matter. The proposal's current approach with Qwen3-72B at top-p=0.9 and temperature=1.0 doesn't actually implement the structured formatting that the cited work emphasizes, which weakens the theoretical grounding here.

There's also a direct contradiction: the same cited paper shows that model sizes beyond 1B don't improve generation quality, yet the proposal uses a 72B model. These aren't fatal flaws, but they point to a specific revision needed around the generator configuration and how it aligns with the cited evidence. My verdict is to recommend revision focused on this targeted inconsistency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5ae69aa-a8a4-4a05-9f4d-748da6752860",
  "isSidechain": false,
  "requestId": "req_011CasiDRmb1ew3bXYUL1B8A",
  "type": "assistant",
  "uuid": "46b3c7ce-4f66-48b1-b630-bf33a14da8fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012NuKD8d1iZ8aNjFELfLQFz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11869,
      "cache_read_input_tokens": 56998,
      "output_tokens": 3275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3275,
          "cache_read_input_tokens": 56998,
          "cache_creation_input_tokens": 11869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11869
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

_source line 64 · 2026-05-09T21:34:21.176Z_

I now have sufficient evidence to issue a verdict. The core verification results:

- **QuaDMix "withdrawn from ICLR 2026"**: CONFIRMED via OpenReview
- **ModernBERT-large throughput**: CONFIRMED — 52.3K tok/s on RTX 4090 at 512 tokens (Table 2 of arXiv:2412.13663)
- **arXiv:2604.13977**: EXISTS and confirmed to say "structured output formats consistently outperform... increasing generator model size beyond 1B parameters provides no additional benefit" — the latter claim is a critical finding that contradicts the proposal's own design
- **arXiv:2511.13640**: EXISTS, correctly characterized
- **ADAPT (openreview.net/forum?id=zgn3P31NWf)**: VERIFIED — Wanru Zhao et al., ICLR 2026 Workshop DATA-FM
- **EMNLP 2026 ARR May 25 deadline**: CONFIRMED
- **Both Round 7 issues**: ADDRESSED (arXiv:2502.02494 differentiation is thorough; 2510.00866 now correctly cited as "rejected from ICLR 2026; preprint")

One **critical new issue** discovered: arXiv:2604.13977 (the proposal's own corroborating work) explicitly states *"increasing the size of the generator model beyond 1B parameters provides no additional benefit."* Yet the proposal uses Qwen3-72B (72B parameters) for the 15M-document synthetic pool (7.68B tokens). This is internally inconsistent AND creates a severe budget violation: generating 7.68B tokens with Qwen3-72B locally requires ~500+ GPU-hours (exceeds the 200H budget by >2.5×), or ~$6,900 in API fees entirely absent from the resource estimate.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "CGS's cross-corpus Voronoi tail-density gating is genuinely distinct from all enumerated competitors: Less is More (no reference-density threshold), Quad (influence-weighted MAB, not tail-density), MATES/Group-MATES (influence models, no real-data reference), D4 (distance-to-centroid pruning without cross-corpus reference). No concurrent paper using this specific combination was found across multiple search strategies."
    },
    "feasibility": {
      "score": 3,
      "rationale": "The CGS selection, embedding, and training pipeline fits within 200 H100-hours, but generating the 15M-document Qwen3-72B corpus (7.68B tokens) is either infeasible on-device (≫200 additional GPU-hours) or requires ~$6,900 in API fees that are completely absent from the resource estimate — and is self-contradicted by the proposal's own cited work (arXiv:2604.13977) which shows generator scale beyond 1B provides no quality benefit."
    },
    "clarity": {
      "score": 4,
      "rationale": "After eight rounds of revision the proposal is exceptionally detailed: budget arithmetic is verified, all prior work is differentiated, evaluation circularity is resolved, and the embedding robustness check (Pythia LM token fallback) is well-specified. The Qwen3-72B generator choice is the only remaining internal contradiction."
    },
    "impact": {
      "score": 4,
      "rationale": "CGS directly addresses the EMNLP 2026 special theme on synthetic data quality and data governance with a principled, low-overhead method; the tail-knowledge evaluation framing (TriviaQA head/tail, Head-to-Tail) is compelling and causally motivated."
    }
  },
  "issues": [
    "CRITICAL — GENERATION COST UNACCOUNTED AND INTERNALLY CONTRADICTED BY CITED LITERATURE: The 15M-document synthetic pool (7.68B tokens) is generated by Qwen3-72B, but the resource estimate includes zero GPU-hours or API costs for this generation. On 4×H100 with vLLM, generating 7.68B tokens from a 72B-parameter model requires roughly 500–1,200 H100-hours (depending on batch throughput), which exceeds the user's hard ≤200 H100-hour constraint by 2.5–6×. Via API (e.g., Together AI at ~$0.90/M tokens), the cost is ~$6,900 — entirely absent from estimated_gpu_cost and claude_api_cost. More fundamentally, this choice is directly contradicted by the proposal's own corroborating work: arXiv:2604.13977 explicitly states 'increasing the size of the generator model beyond 1B parameters provides no additional benefit.' Using Qwen3-72B instead of Qwen3-7B or Qwen3-1.5B simultaneously violates the budget, adds undisclosed cost, and is inconsistent with the cited literature the proposal relies on for external validation. The fix is one sentence: switch the generation model to Qwen3-7B (or Qwen3-1.5B), which (a) reduces local generation to ~20–30 GPU-hours at 100K tok/s on a single H100, holding total budget under 200H, (b) is empirically justified by arXiv:2604.13977, and (c) removes the internal contradiction."
  ],
  "feedback": "The proposal has resolved all Round 7 issues cleanly and is otherwise submission-ready. One targeted fix is required:\n\nFIX THE GENERATOR MODEL SIZE — Replace Qwen3-72B with Qwen3-7B (or Qwen3-1.5B) for generating the 15M-document synthetic pool. Rationale: (1) The cited concurrent work arXiv:2604.13977 explicitly states that generator models beyond 1B parameters provide no additional benefit for synthetic pretraining quality — the proposal already cites this as corroborating evidence, so using a 72B model is a direct internal contradiction. (2) Generating 7.68B tokens with Qwen3-72B on local H100s requires ~500+ GPU-hours (violates ≤200H constraint); via API it costs ~$6,900 (undisclosed). (3) With Qwen3-7B at ~100K tok/s on one H100: 7.68B tokens ÷ 100K = 76,800s ≈ 21.3 GPU-hours — fits cleanly within budget. Update the resource estimate to add '~21H for synthetic pool generation (Qwen3-7B, single H100)' bringing the total to ~196H nominal, still under 200H. Optionally, add one sentence noting that the generator model size is held at ≤7B per arXiv:2604.13977's finding, which also helps position CGS as a full-stack low-compute pipeline.",
  "reason": "All Round 7 issues addressed; one critical remaining gap: Qwen3-72B generation cost (~500+ GPU-hours or ~$6,900 API) is entirely unaccounted for in the resource estimate and directly contradicted by the proposal's own cited corroborating work (arXiv:2604.13977) — fixable by switching to Qwen3-7B."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46b3c7ce-4f66-48b1-b630-bf33a14da8fb",
  "isSidechain": false,
  "requestId": "req_011CasiDRmb1ew3bXYUL1B8A",
  "type": "assistant",
  "uuid": "d56338c4-178f-44cc-a087-4b6ade91a216",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012NuKD8d1iZ8aNjFELfLQFz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11869,
      "cache_read_input_tokens": 56998,
      "output_tokens": 3275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3275,
          "cache_read_input_tokens": 56998,
          "cache_creation_input_tokens": 11869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11869
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

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d56338c4-178f-44cc-a087-4b6ade91a216",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 8: Coverage-Guided Synthetic Data Selection",
  "sessionId": "24715d91-e1d0-4e2b-a114-d4d7d84d7a06"
}
```

---
