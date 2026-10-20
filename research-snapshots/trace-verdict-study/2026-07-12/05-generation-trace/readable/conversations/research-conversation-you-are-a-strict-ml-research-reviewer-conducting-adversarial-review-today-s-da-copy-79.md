# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-09 (UTC).** Your job: indep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/b7fd655f-a099-4ed2-b12d-875beaae4b8c.jsonl`
- **Structured JSON:** [`67d3fca0565b518feecc.json`](../../sessions/67/67d3fca0565b518feecc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-09T20:37:41.341Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-09T20:37:41.341Z",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-09 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.\n\nDirection: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.\n2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.\n3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.\n\nThis is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.\n\nTag: direction=data_governance, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-09?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 5/10)\n{\n  \"title\": \"Tail-Coverage-Guided Synthetic Data Selection to Replace Classifier Quality Filtering\",\n  \"core_problem\": \"Classifier-based quality filtering (CQF), the dominant method for selecting synthetic pretraining data used by GPT-3, LLaMA, and PaLM, is shown to be illusory — it improves downstream task performance not by improving language modeling quality but by implicit distribution-matching rather than genuine quality signals. Concurrently, synthetic data exhibits systematic distributional discrepancies relative to real data: top-p and temperature sampling truncate low-probability continuations, causing rare factual content to be systematically underrepresented in synthetic corpora. Kandpal et al. (ICML 2023) established a direct causal link: LLM accuracy on factual questions correlates strongly with the frequency of the underlying entity in pretraining documents, confirming that tail-knowledge acquisition depends on tail-content exposure during training. No principled selection criterion corrects for this distributional gap: CQF does not target it (and may worsen it by filtering toward fluent head-distribution text), while naïve random sampling inherits the generator's truncation bias wholesale. More recent model-aware selectors such as MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) adapt dynamically to the evolving model's preferences but do not target the specific tail-distribution gap — they optimize for generic influence rather than for correcting truncation-induced underrepresentation.\",\n  \"opportunity\": \"Three concurrent findings create a gap that demands a new method: (1) 'The Data-Quality Illusion' (arXiv:2510.00866, preprint; peer review status pending) demonstrates that CQF does not improve language modeling on held-out high-quality data and argues the field should rethink synthetic data filtering from first principles; (2) 'Data Value in the Age of Scaling' (arXiv:2511.13640) identifies tail-knowledge underrepresentation as a systematic distributional discrepancy in synthetic data under real-synthetic mixing, linked to generative truncation mechanisms; (3) Kandpal et al. (ICML 2023) provides external causal validation: pretraining document frequency is a strong predictor of downstream accuracy on rare facts. Together, these findings establish that (a) CQF is the wrong solution, (b) the actual problem is a distributional gap at the tail, and (c) closing the tail gap causally improves knowledge acquisition. The opportunity is 'Coverage-Guided Sampling' (CGS): select synthetic examples to maximize marginal coverage of low-density regions of the real-data embedding space, directly targeting the distributional gap that CQF fails to address. This is the first synthetic data selector explicitly designed around the mechanism documented in arXiv:2510.00866 rather than a classifier proxy. The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status; CGS would be motivated equally if the finding were confirmed by independent replication.\",\n  \"landscape\": \"CQF is used by all major pretraining pipelines (GPT-3, LLaMA, PaLM, RedPajama) but arXiv:2510.00866 (preprint; peer review status pending) shows its quality signal is misleading. Six clusters of prior work bound the proposal:\\n\\n**Diversity-quality pretraining selection.** Quad (arXiv:2409.16986, ICLR 2025 Spotlight) is the most important prior work. Quad clusters all pretraining data and uses a Multi-Armed Bandit (MAB) scheme favoring clusters with high influence scores (quality) or low selection frequency (diversity). CGS differs on three axes: (1) Criterion — CGS uses a real-data tail-density threshold (bottom 20–25% by Voronoi cell occupancy in a reference corpus) rather than influence-weighted underrepresentation; CGS does not require influence score computation, which is expensive to scale to billions of synthetic candidates; (2) Target — CGS applies specifically to the synthetic data mixing problem and requires a real-data reference corpus to define 'tail'; Quad operates within a single multi-source corpus without a reference density; (3) Motivation — CGS is grounded in the CQF failure mechanism documented in arXiv:2510.00866. QuaDMix (arXiv:2504.16511, preprint, withdrawn from ICLR 2026) from ByteDance proposes a parameterized quality-diversity sampling function using domain classification for diversity measurement and LightGBM for parameter search. Like Quad, QuaDMix does not target real-data tail density specifically.\\n\\n**Model-aware selection.** MATES (arXiv:2406.06046, NeurIPS 2024) trains a lightweight BERT-base influence model that continuously adapts to the evolving pretraining model's data preferences, updating every 10,000 steps. MATES achieves 2× the gain of prior SOTA (QuRating) on 410M and 1B models, at 11.5–21.7% computational overhead. CGS differs on three axes: (a) CGS requires no influence model training — the FAISS IVF index is built once over the fixed reference corpus before pretraining begins, versus MATES's periodic BERT-base retraining; (b) CGS requires no reference task definition — MATES's performance varies substantially with reference task choice, a deployment-time burden; (c) CGS targets a specific, mechanistically motivated failure mode (CQF distributional bias) rather than maximizing generic influence scores.\\n\\nGroup-MATES (arXiv:2502.14709, NeurIPS 2025) extends MATES to group-level selection: it trains a relational data influence model that weights individual sample influence by inter-data relationships, partitions the training corpus into clusters via these relationship weights, and selects within each cluster independently, achieving 3.5–9.4% relative gains and 1.75× token efficiency over individual selection baselines on DCLM at 400M–3B scales across 22 tasks. CGS differs on three axes: (a) CGS requires no influence model — Voronoi cells are defined by k-means over a fixed reference corpus embedding, not by data-data relational influence weights, making CGS zero-overhead relative to training; (b) CGS uses reference-corpus occupancy density as the selection gate — only tail cells (bottom 20–25% by reference occupancy) are eligible for synthetic coverage — rather than influence-weighted within-cluster scoring; (c) CGS targets the specific synthetic-real distributional gap documented in arXiv:2511.13640: it applies to a fixed synthetic candidate pool relative to a real-data reference corpus, whereas Group-MATES operates within a single training corpus without a reference density criterion.\\n\\n**Coverage-based fine-tuning.** 'Less is More: Adaptive Coverage for Synthetic Training Data' (arXiv:2504.14508, 2025) applies a greedy maximum-coverage objective to select synthetic fine-tuning data for NLP classifiers. CGS shares the max-coverage algorithmic skeleton but differs critically in three respects: (1) 'Less is More' maximizes coverage of ALL embedding cells uniformly — without a reference-corpus density criterion, it would waste selection budget on head cells already well-covered by real data, failing to address the distributional gap that CQF leaves open; CGS adds the critical step of using real-data Voronoi occupancy as a gate: only tail cells (bottom 20–25% by reference occupancy) are eligible, ensuring the entire selection budget is concentrated on underrepresented regions; (2) CGS applies at pretraining scale (hundreds of millions of candidates), requiring FAISS IVF for tractability; (3) this reference-density threshold is the mechanistic link to the CQF failure documented in arXiv:2510.00866, which 'Less is More' does not establish.\\n\\n**Online pretraining data curation.** ADAPT ('Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods', arXiv:2512.24503, ICLR 2026 Workshop DATA-FM) and AC-ODM ('Actor-Critic Online Data Mixing', arXiv:2505.23878, preprint) represent an online paradigm: rather than pre-filtering the candidate pool, they dynamically reweight or re-mix training samples during training based on loss signals. CGS is orthogonal and compatible: as a static offline pre-filter, it reduces the synthetic candidate pool to tail-coverage-optimal documents before training begins with zero ongoing overhead; an online reweighter can further adapt the mix at training time after CGS has already narrowed the pool. Neither ADAPT nor AC-ODM targets the specific synthetic-real tail-density gap documented in arXiv:2510.00866 — they optimize generic influence or domain balance, not reference-density-defined tail coverage.\\n\\n**Synthetic data scale findings.** 'Demystifying Synthetic Data in LLM Pre-training' (arXiv:2510.01631, EMNLP 2025) finds ~30% rephrased synthetic data is empirically optimal but provides no mechanistic filter. arXiv:2511.13640 characterizes three-phase scaling behavior under real-synthetic mixing and identifies tail underrepresentation as a systematic discrepancy without a selection remedy.\\n\\n**Tail knowledge evaluation and deduplication.** Kandpal et al. (arXiv:2211.08411, ICML 2023) establish that LLM accuracy on factual questions correlates causally with pretraining document frequency, providing the empirical foundation for CGS's tail-coverage hypothesis. 'Head-to-Tail' (arXiv:2308.10168, NAACL 2024) provides a purpose-built 18K QA benchmark explicitly stratified into head, torso, and tail facts by knowledge graph frequency — an independent evaluation resource for CGS. D4 (NeurIPS 2023) uses FAISS k-means for deduplication/diversification via distance-to-centroid pruning; it applies a distance heuristic not a tail-density threshold and does not target the synthetic selection sub-problem.\",\n  \"approach\": \"Coverage-Guided Sampling (CGS) selects synthetic pretraining data by maximizing coverage of underrepresented tail regions in real-data embedding space.\\n\\n**Method.** We embed a reference corpus (5B-token stratified sample of Dolma, preserving domain balance) and all candidate synthetic documents using ModernBERT-large, then build a FAISS IVF index over the real-data embeddings. The resulting Voronoi cell structure partitions semantic space; 'tail cells' are defined as cells in the bottom 20–25% by real-data occupancy. CGS then greedily selects synthetic documents maximizing marginal coverage of tail cells via a streaming maximum-coverage subproblem — no quality classifier training required. ModernBERT-large is chosen for embedding over larger alternatives due to its ~100–150K tokens/sec throughput on H100 (vs. ~15–30K for Qwen3-Embedding-8B), making 15M-document indexing tractable within the compute budget; embedding quality is validated in Experiment 0.\\n\\n**Mechanistic validation experiment (Experiment 0, ~2 H100-hours).** Before committing to training runs, we validate the core empirical hypothesis: (a) Generate three synthetic corpora of 10M tokens each using Qwen3-72B with top-p ∈ {0.5, 0.85, 0.95}; embed and assign each document to a Voronoi cell; measure whether lower top-p concentrates documents in higher-occupancy cells (expected: yes, since low top-p collapses to high-probability continuations); (b) Embed 5,000 Wikidata long-tail documents (entities appearing <100 times in C4) and confirm they cluster significantly more in low-occupancy cells than a random C4 sample. If (a) shows r < 0.3 between top-p and mean cell occupancy, or (b) shows no significant enrichment, halt before Tier 1 and revise the tail-density criterion.\\n\\n**Model architecture and training.** Following the precedent of MATES (NeurIPS 2024), Quad (ICLR 2025), and D4 (NeurIPS 2023), we use the Pythia model family (EleutherAI GPT-NeoX codebase) for full reproducibility:\\n- *Tier 1 — Systematic ablation: Pythia-410M* (24 layers, hidden dim 1024, 16 heads, 2048 sequence length; ~8B tokens, Chinchilla-optimal). AdamW optimizer with β1=0.9, β2=0.95, weight decay 0.1; cosine LR schedule with 1% warmup steps. Following Wang et al. ('Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice,' ICLR 2026 Poster), all Tier 1 ablations use a 10× reduced peak learning rate of 3×10⁻⁵ (instead of the standard 3×10⁻⁴) to ensure selection method rankings derived from the 410M proxy runs transfer reliably to Tier 2 at 1.4B scale — this costs no additional GPU-hours since the reduced-LR runs replace rather than supplement standard-LR runs. Batch size ~2M tokens. 5 configurations: CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, and random baseline. Only CGS has a tail-threshold parameter; the three non-CGS methods run once without threshold variation. Each run: ~9 H100-hours on 1 GPU.\\n- *Tier 2 — Scaling check: Pythia-1.4B* (24 layers, hidden dim 2048, 16 heads, 2048 sequence length; 10B tokens). Same optimizer family with peak LR 2×10⁻⁴. 2 configurations: best CGS from Tier 1 vs. CQF-FineWebEdu. Each run: ~44 H100-hours (4 GPUs × ~11h wall-clock via data parallelism). Using Pythia-1.4B (not 1.3B) ensures exact architecture reproducibility with the published model family.\\n\\n**Synthetic candidate pool.** We precompute embeddings for a fixed 15M-document synthetic pool generated by Qwen3-72B (top-p=0.9, temperature=1.0, avg 512 tokens/document = 7.68B tokens total). At 100K tokens/sec per H100: the 7.68B synthetic tokens require 76,800s ≈ 21.3 GPU-hours; the 5B-token reference corpus requires 50,000s ≈ 13.9 GPU-hours; total embedding ≈ 35 GPU-hours ≈ 8.8H wall-clock on 4 GPUs. This pool size provides ample selection diversity: 7.68B tokens exceeds the synthetic allocation for both Tier 1 (~2.4B tokens at 30% synthetic) and Tier 2 (~3B tokens at 30% synthetic) by over 2.5×. FAISS IVF build is CPU-bound (~2h on 32 cores) and runs concurrently with early embedding steps.\\n\\n**IVF nlist calibration.** nlist ≈ sqrt(N_reference_docs) per FAISS best practices. Tier 1 pilots probe two nlist settings (±30%) to confirm tail cell occupancy is well-separated; this is CPU-only analysis on the pre-built index (zero GPU cost). If cell structure is degenerate, we correct before the Tier 2 run.\\n\\n**Evaluation — primary, secondary, and diversity metrics.** The evaluation design explicitly separates the training criterion (FAISS cell coverage) from the test signal to avoid circularity:\\n\\n(1) *Primary — TriviaQA head/tail accuracy split (independent external metric)*: Using Wikipedia page-view statistics to stratify TriviaQA questions into head entities (top 20% by views, ~1K questions) and tail entities (bottom 20%, ~1K questions), we measure accuracy separately. This stratification uses an external resource (Wikipedia traffic data) wholly independent of the FAISS cell structure. Per Kandpal et al. (ICML 2023), tail-entity accuracy is the most causally meaningful test of whether tail coverage translates to knowledge acquisition. We report the tail/head accuracy ratio as the primary CGS-vs-CQF gap metric.\\n\\n(2) *Additional independent benchmark — Head-to-Tail (NAACL 2024)*: This purpose-built 18K QA benchmark stratifies facts into head, torso, and tail by knowledge graph frequency (Wikidata). It provides a second external validation of tail knowledge independent of both FAISS and Wikipedia pageviews, strengthening the falsifiability of the tail-coverage claim.\\n\\n(3) *Secondary — Standard downstream benchmarks*: HellaSwag, WinoGrande, ARC-E/C, PIQA — required for comparability with Quad, D4, MATES, Group-MATES, and CQF baselines. CGS should match or exceed CQF on these benchmarks; failure here would indicate coverage-only selection sacrifices head-distribution capabilities.\\n\\n(4) *Diversity of selected synthetic data (CPU-only, zero GPU cost)*: We compute corpus-level self-BLEU (Zhu et al., 2018; lower = more diverse) and 4-gram entropy (higher = more diverse) over the synthetic subset selected by each method (CGS, CQF-Wikipedia, CQF-FineWebEdu, random). These metrics are computed post-selection before training begins. CGS should exhibit lower self-BLEU and higher n-gram entropy than CQF-selected data, since CQF preferentially selects fluent head-distribution text with low lexical diversity. This directly substantiates the coverage-vs-classifier-proxy claim: not only does CGS target underrepresented semantic regions, but the selected text should be measurably more lexically diverse than CQF output.\\n\\n(5) *Diagnostic — Held-out low-occupancy perplexity*: 5% of reference corpus documents from the bottom 20% occupancy cells are held out before training and used to measure model perplexity. This metric is demoted to a sanity check because CGS is explicitly optimized to cover exactly those cells — perplexity improvement here confirms distribution matching, not necessarily genuine knowledge acquisition. It is reported alongside (1) and (2) but not used as a primary falsifiability claim.\\n\\n**Falsifiable primary claim**: CGS achieves higher TriviaQA tail-entity accuracy than CQF while matching CQF on standard downstream benchmarks, directly operationalizing the quality-vs-coverage paradox documented in arXiv:2510.00866. The diversity metrics (self-BLEU, n-gram entropy) provide a secondary mechanistic check confirming that CGS's tail-coverage selection is not collapsing to a high-fluency, low-diversity subset.\\n\\n**Timeline and execution mode.** Given the EMNLP 2026 ARR deadline of May 25, 2026 (16 days from proposal date), the primary execution path is auto-research mode. GPU wall-clock with 4× H100: Experiment 0 (~2h) → Embedding (~8.8h, 4 GPUs) → FAISS build (~2h CPU concurrent) → Tier 1 ablation grid (~18h, 4 experiments in parallel in batch 1, then 1 remaining) → Tier 2 scaling check (~22h, 2 sequential runs with 4-GPU data parallelism). Total GPU wall-clock: ~50.8 hours (~2.1 days). Paper writing begins in parallel on day 1; Tier 1 results are guaranteed by day 4; Tier 2 results are best-effort. If Tier 2 runs do not complete before submission, the 1.4B experiments are described as ongoing and submitted to camera-ready.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~172 H100-hours (Experiment 0 ~2h; embedding ModernBERT-large on 15M synthetic docs + 5B reference corpus ~35h [7.68B synthetic tokens ÷ 100K tok/s = 21.3h; 5B reference ÷ 100K tok/s = 13.9h; total = 35.2h, verified arithmetic]; FAISS IVF build CPU-bound ~0h GPU; Tier 1 ablations 5 configurations × ~9h = 45h; Tier 2 scaling check 2 runs × ~44h = 88h; misc eval ~2h). Synthetic pool reduced from 50M to 15M documents to correct the embedding budget; 7.68B tokens exceeds the synthetic allocation for both training tiers by >2.5×, preserving selection diversity.\",\n      \"gpu_utilization\": \"Low (~40% active) — researcher waits between tiers to review Experiment 0 results and pilot outcomes before committing to 1.4B runs.\",\n      \"timeline\": \"3–5 months. INCOMPATIBLE with May 25, 2026 ARR deadline — use auto-research mode for deadline-constrained execution.\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$420–615 at $2.44–3.56/hr per H100 (RunPod/Lambda Labs current pricing)\",\n      \"risk_note\": \"If Experiment 0 (mechanistic validation) fails — i.e., top-p does not correlate with cell occupancy in the expected direction — the core hypothesis needs revision before Tier 1 ablations begin. Caught in the first ~2 H100-hours.\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~190 H100-hours (manual base ~172H plus agent overhead: 2 additional 410M sensitivity runs for IVF nlist ±30% around baseline and ModernBERT-large vs. sentence-transformers/all-MiniLM-L6-v2 embedding model speed check, each ~9h = 18H extra; plus ~0H GPU for nlist structure analysis which is CPU-only).\",\n      \"gpu_utilization\": \"Moderate (~60% active) — agent queues experiments continuously but awaits human approval before committing to each Tier 2 run.\",\n      \"timeline\": \"4–6 weeks. INCOMPATIBLE with May 25, 2026 ARR deadline — use auto-research mode for deadline-constrained execution.\",\n      \"team\": \"1 researcher, ~45 min/day check-in to approve tier transitions and review Experiment 0 results\",\n      \"claude_api_cost\": \"$200–350 (experiment queue management, Experiment 0 result interpretation, IVF calibration guidance)\",\n      \"estimated_gpu_cost\": \"~$464–676 at $2.44–3.56/hr per H100\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~175 H100-hours (Experiment 0 ~2h + embedding ModernBERT-large for 15M synthetic docs [7.68B tokens] + 5B reference corpus ~35h + FAISS IVF build CPU-bound ~0h GPU + Tier 1 ablation grid 5 configurations × ~9h = 45h + Tier 2 scaling check 2 runs × ~44h = 88h + misc eval ~3h). Capped at 175H by early-stopping if Experiment 0 fails (saves ~138H by avoiding Tier 1 and Tier 2).\",\n      \"gpu_utilization\": \"High (~85% active) — agent queues Experiment 0 → embedding → FAISS build → Tier 1 ablation grid → Tier 2 runs without human wait. ~15% overhead from API round-trips and CPU-bound FAISS builds between GPU steps.\",\n      \"timeline\": \"8–12 days total: ~2.1 days GPU wall-clock compute (50.8 hours on 4× H100) + paper writing in parallel from day 1. Tier 1 results available by day 4; Tier 2 results by day 5. Writing days 1–14 (parallel); submission day 16 (May 25, 2026 ARR deadline). COMPATIBLE with deadline under this framing: Tier 1 results are guaranteed at submission; Tier 2 results are best-effort and described as ongoing in the paper if not complete.\",\n      \"team\": \"0 (initial setup ~3h: configure ModernBERT-large embedding pipeline with FAISS IVF builder, GPT-NeoX training harness with eval on HellaSwag/WinoGrande/ARC/PIQA + TriviaQA head/tail + Head-to-Tail benchmark)\",\n      \"claude_api_cost\": \"$600–900 (automated Experiment 0 interpretation, ablation grid orchestration, early-stopping decisions, TriviaQA stratification computation, final report generation — estimated 5,000–8,000 API turns)\",\n      \"estimated_gpu_cost\": \"~$427–623 at $2.44–3.56/hr per H100\",\n      \"speed_bottleneck\": \"4× H100 allows: Embedding (15M synthetic docs + 5B reference corpus) completes in ~8.8h wall-clock (35H ÷ 4 GPUs); Tier 1 grid runs in ~18h wall-clock (4 configs in parallel batch 1, then 1 remaining config in batch 2, each ~9H on 1 GPU); Tier 2 serializes at ~11h wall-clock each with 4-GPU data parallelism (2 runs = 22h). Total GPU wall-clock: ~2h (Exp 0) + ~8.8h (embedding) + ~18h (Tier 1) + ~22h (Tier 2) ≈ 50.8h ≈ 2.1 days.\",\n      \"risk_note\": \"Early-stopping trigger: if Experiment 0 shows Pearson r < 0.3 between top-p value and mean cell occupancy rank, halt and report mechanism failure before consuming Tier 1 compute. Pre-specified threshold prevents exhaustive exploration of a degenerate configuration.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026; conference October 24–29, 2026, Budapest, Hungary). Primary execution path: auto-research mode, with Tier 1 (Pythia-410M) results guaranteed at submission and Tier 2 (Pythia-1.4B) submitted to camera-ready.\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining (arXiv:2510.00866, preprint; peer review status pending)\",\n    \"Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures (arXiv:2511.13640, 2025)\",\n    \"Harnessing Diversity for Important Data Selection in Pretraining Large Language Models (Quad, arXiv:2409.16986, ICLR 2025 Spotlight)\",\n    \"QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining (arXiv:2504.16511, preprint, withdrawn from ICLR 2026)\",\n    \"MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models (arXiv:2406.06046, NeurIPS 2024)\",\n    \"Group-MATES: Group-Level Data Selection for Language Model Pretraining (arXiv:2502.14709, NeurIPS 2025)\",\n    \"Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice (Wang et al., ICLR 2026 Poster, openreview.net/forum?id=2FZC0c06jP)\",\n    \"Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods — ADAPT (arXiv:2512.24503, ICLR 2026 Workshop DATA-FM)\",\n    \"AC-ODM: Actor-Critic Online Data Mixing for Sample-Efficient LLM Pretraining (arXiv:2505.23878, preprint)\",\n    \"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls (arXiv:2510.01631, EMNLP 2025)\",\n    \"Large Language Models Struggle to Learn Long-Tail Knowledge (Kandpal et al., arXiv:2211.08411, ICML 2023)\",\n    \"Head-to-Tail: How Knowledgeable are Large Language Models in Long-Tail Knowledge? (arXiv:2308.10168, NAACL 2024)\",\n    \"Measuring Diversity in Synthetic Datasets (arXiv:2502.08512, ICML 2025)\",\n    \"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning (arXiv:2511.01490, ACL Findings 2026)\",\n    \"Less is More: Adaptive Coverage for Synthetic Training Data (arXiv:2504.14508, 2025)\",\n    \"D4: Improving LLM Pretraining via Document De-Duplication and Diversification (NeurIPS 2023)\",\n    \"Scaling Laws of Synthetic Data for Language Models (arXiv:2503.19551, 2025)\",\n    \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling (arXiv:2304.01373, ICML 2023)\"\n  ],\n  \"description\": \"Classifier-based quality filtering (CQF) — the dominant synthetic pretraining selector used by GPT-3, LLaMA, and PaLM — has been shown to boost downstream task scores via implicit distribution-matching rather than genuine quality improvement (arXiv:2510.00866, preprint; peer review status pending; independently reproducible from first principles regardless of venue outcome). Concurrently, Kandpal et al. (ICML 2023) established that LLM accuracy on rare facts causally correlates with pretraining document frequency, confirming that tail-content exposure drives tail-knowledge acquisition; and arXiv:2511.13640 documents systematic tail underrepresentation in synthetic data via top-p/temperature truncation. This project proposes Coverage-Guided Sampling (CGS), the first principled pretraining data selector grounded in the actual distributional failure mechanism of CQF. CGS embeds a 5B-token reference corpus and a fixed 15M-document synthetic candidate pool (7.68B tokens) using ModernBERT-large (chosen for ~100–150K tokens/sec throughput on H100, vs. ~15–30K for Qwen3-Embedding-8B; total embedding ≈ 35 GPU-hours: 7.68B synthetic tokens ÷ 100K tok/s = 21.3H + 5B reference ÷ 100K tok/s = 13.9H ≈ 8.8H wall-clock on 4 GPUs), builds a FAISS IVF index over the real corpus, identifies low-density Voronoi 'tail cells' (bottom 20–25% by occupancy), and greedily selects synthetic documents maximizing marginal tail-region coverage — no classifier training required. A mandatory Mechanistic Validation Experiment (~2 H100-hours) confirms that Voronoi cell density correlates with top-p sampling behavior before committing to training runs. We train using the Pythia model family (EleutherAI GPT-NeoX codebase): Tier 1 uses Pythia-410M at Chinchilla-optimal scale (~8B tokens, 5 ablation configurations [CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, random], ~45 H100-hours); following Wang et al. (ICLR 2026 Poster), Tier 1 uses a 10× reduced peak learning rate (3×10⁻⁵) to improve proxy-to-full-scale ranking reliability at zero extra compute cost. Tier 2 uses Pythia-1.4B at 10B tokens (2 configurations, ~88 H100-hours); total budget ~175 H100-hours including ~35 H100-hours for embedding, well within the ≤200H constraint. Evaluation resolves circularity: TriviaQA tail-entity accuracy (stratified by Wikipedia pageviews, independent of FAISS) and the Head-to-Tail benchmark (NAACL 2024) are primary falsifiability metrics; corpus-level self-BLEU and 4-gram entropy over selected synthetic data are computed CPU-only post-selection to confirm CGS produces more diverse output than CQF; held-out low-occupancy perplexity is demoted to a diagnostic. Closest prior work: Quad (ICLR 2025) uses influence-weighted cluster MAB — CGS requires no influence scoring. MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) train influence models — CGS builds its FAISS index once with zero ongoing overhead and no reference task dependency. 'Less is More' maximizes uniform coverage of all cells — CGS adds a real-data reference-density gate (bottom 20–25% occupancy only) establishing the mechanistic link to arXiv:2510.00866. Online methods ADAPT and AC-ODM reweight during training — CGS is a compatible offline pre-filter. Primary execution path: auto-research mode (4× H100, ~2.1 days GPU wall-clock, paper writing in parallel), targeting EMNLP 2026 ARR deadline May 25, 2026, with Tier 1 results guaranteed at submission.\",\n  \"project_name\": \"cov_guided_synth_sel\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"VENUE CLAIM ERROR: The generator labels arXiv:2510.00866 as 'EMNLP 2025', but independent search confirms the OpenReview submission targets ICLR 2026 (not EMNLP 2025). This foundational reference for the 'opportunity' narrative may have a different reception history; the paper should be cited as a preprint with venue status clarified.\", \"CLAIM OVERSTATEMENT: arXiv:2511.13640 is described as proving 'tail-knowledge underrepresentation is a leading driver of collapse.' The paper's abstract identifies tail underrepresentation as a distributional discrepancy observed in synthetic data and studies three-phase scaling — it does not specifically claim this is the primary or leading driver of collapse. This exaggerated claim weakens the motivation.\", \"MISSED CRITICAL PRIOR WORK: Quad (ICLR 2025, arXiv via openreview.net/forum?id=bMC1t7eLRc) proposes clustering-based quality+diversity selection for LLM pretraining using FAISS k-means and influence scoring — a direct competitor the generator does not cite. QuaDMix (arXiv:2504.16511, ICLR 2026 submission, since withdrawn) from ByteDance proposes a unified quality-diversity parameterized selection function for pretraining, also uncited. These papers must be differentiated against.\", \"MECHANISTIC GAP IN CORE CLAIM: The proposal asserts that Voronoi cells with low real-data occupancy in Qwen3-Embedding space correspond to the tail knowledge that top-p/temperature sampling truncates. This mapping is assumed, not established. Token-level probability truncation in a generative model does not directly translate to semantic embedding cluster density. A reviewer will immediately ask for theoretical justification or ablation confirming this correspondence.\", \"COMPUTE CONSTRAINT MISMATCH: The user's hard constraint is ≤200 H100-hours and explicitly specifies 1B–3B models. The proposal adds a 7B model run (~120h A100 ≈ 60 H100-hours) that goes beyond the user's stated scope and partially strains the budget. The 5× ablation runs of 1.3B at 30h A100 each imply ~12B-token training runs, which are far from Chinchilla-optimal and may produce null or noisy tail-coverage signal.\", \"SHORT TRAINING RUN RISK: At the implied token budgets (12–15B tokens for 1.3B models, ~15B for 7B), the models are severely under-trained. Tail-knowledge differences between selection strategies may not manifest reliably at this scale, making the primary evaluation (Wikidata-derived tail probe accuracy) potentially inconclusive.\", \"WIKIDATA TAIL PROBE CONSTRUCTION: The 'rare entity recall' and 'uncommon fact completion' evaluation requires constructing entity-frequency distributions from Wikidata, filtering tail entities from training data, and ensuring no contamination with the Dolma/C4 reference corpus. This pipeline is neither simple nor guaranteed valid — a reviewer will question whether the probe actually tests tail coverage or just benchmark contamination artifacts.\", \"DIFFERENTIATION FROM 'LESS IS MORE' UNDERSTATED: The generator correctly identifies arXiv:2504.14508 as closest concurrent work but claims differentiation by 'not addressing pretraining.' However, the algorithmic overlap is very high — both use embedding space, both use greedy max-coverage, both target synthetic data. A reviewer may see CGS as 'Less is More applied to pretraining with a tail-density threshold' and demand stronger algorithmic differentiation.\"]\nFeedback: The core idea is publishable but needs targeted revision on four fronts before it can reach top-tier bar:\n\n1. FIX REFERENCES AND CLAIMS: Correct the venue of arXiv:2510.00866 (it is not confirmed 'EMNLP 2025'; cite as preprint or ICLR 2026 submission). Soften the claim about 2511.13640: write 'identifies tail knowledge underrepresentation as a systematic distributional discrepancy in synthetic data' rather than 'leading driver of collapse.' These factual errors undermine reviewer trust.\n\n2. DIFFERENTIATE FROM QUAD AND LESS IS MORE: Quad (ICLR 2025) does clustering-based diversity-quality selection for pretraining — you must cite it and clearly explain why CGS (tail-density targeting via Voronoi cells) is fundamentally different from selecting underrepresented clusters. The generator should add a paragraph: 'This idea is too similar to Quad (ICLR 2025, openreview.net/forum?id=bMC1t7eLRc) in using FAISS clustering for pretraining diversity. Differentiation: Quad selects by influence-weighted cluster underrepresentation, not by real-data tail density in Voronoi cells; CGS's criterion is grounded in the CQF failure mechanism specifically for synthetic data.' Similarly, position against Less is More (arXiv:2504.14508) more aggressively: CGS extends the max-coverage idea to pretraining and adds tail-threshold grounding.\n\n3. JUSTIFY OR DROP 7B MODEL: To stay within the user's ≤200 H100-hour constraint and 1B–3B model scope, either (a) drop the 7B run and use a 2.8B model as the 'large' reference point, or (b) argue explicitly that 7B is needed to show the tail-coverage effect is non-trivial at scale and budget ~60 H100-hours for it. The current framing mixes the user's budget constraint with an aspiration for larger scale.\n\n4. VALIDATE THE VORONOI-TAIL CORRESPONDENCE: Add a validation experiment: (a) generate synthetic documents with different top-p values (0.5, 0.85, 0.95) and show that Voronoi cell density in Qwen3-Embedding space correlates with generation temperature/top-p in the expected direction; (b) show that manually selected tail-knowledge documents from Wikidata concentrate in low-occupancy cells. This costs 1–2 GPU-hours but would make the mechanistic claim reviewable. Without this, the core hypothesis is untested.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"TIMELINE CONSTRAINT VIOLATION: The user specifies a hard ≤16-day constraint. Manual mode is estimated at 3-5 months and human-in-loop at 4-6 weeks — both are wildly incompatible. Auto-research mode is 8-12 days for experiments only, leaving ≈4-8 days to write and submit a full research paper. The proposal should either (a) scope itself to auto-research mode as the primary execution path and explicitly acknowledge the paper-writing timeline risk, or (b) treat the 16-day constraint as applying to a 'proof of concept' submission where only Tier 1 results (360M ablations) are reported and Tier 2 is deferred to the camera-ready. As written, the resource estimate table creates an internal inconsistency: the paper claims to target EMNLP 2026 (16 days away) yet describes modes that take months.\", \"MATES (NeurIPS 2024) ABSENT FROM FORMAL LANDSCAPE AND KEY REFERENCES: MATES (arXiv:2406.06046, NeurIPS 2024) trains a small influence model to dynamically select pretraining data, achieving 2× the gains of prior state-of-the-art. This is a directly relevant published baseline for pretraining data selection that the proposal mentions once in passing ('Quad, D4, and MATES baselines') but never formally describes or differentiates in the landscape section. A reviewer will notice this omission immediately. The generator should add MATES to the landscape and key references, noting that CGS requires no influence model training (unlike MATES), which is a concrete practical advantage.\", \"EVALUATION CIRCULARITY IN HELD-OUT LOW-OCCUPANCY PERPLEXITY: The primary evaluation metric uses documents held out from the bottom 20% of reference corpus Voronoi cells as both the training selection criterion AND the evaluation signal. CGS is guaranteed to select synthetic data that covers exactly those cells — so the model trained with CGS learns to predict text statistically similar to those cells' content. The held-out perplexity improvement may reflect this distribution matching rather than genuine acquisition of tail knowledge. An independent external tail benchmark (e.g., LAMA probes, TriviaQA entity-frequency stratification with Wikipedia pageview statistics) should be the primary metric for falsifiability; the held-out low-occupancy perplexity should be demoted to a secondary diagnostic. The TriviaQA head/tail split already exists in the proposal and is the better primary metric — reframe accordingly.\", \"EMBEDDING COMPUTATION BUDGET UNDERESTIMATED: The proposal allocates '~10 H100-hours' for embedding 'a 10B-token reference corpus' plus synthetic candidates described elsewhere as 'hundreds of millions.' Back-of-envelope: Qwen3-Embedding processing 200M synthetic documents at 512 tokens each = 100B tokens; at ~1M tokens/sec on an H100 (optimistic), this is ~28 hours just for the synthetic corpus, separate from the reference corpus embedding. The auto-research mode with 12 grid configurations reuses the same embedding index but the initial build is underestimated. The generator should clarify the exact candidate corpus size (e.g., 'we precompute embeddings for a 50M-document synthetic pool generated by Qwen3-72B') and revise the embedding H100-hour estimate accordingly.\", \"TRAINING MODEL ARCHITECTURE UNSPECIFIED: The proposal trains models from scratch at 360M and 1.3B parameters but never states what architecture, tokenizer, or training codebase is used. Reproducibility requires specifying whether this is a GPT-2/LLaMA-style decoder, what the sequence length is, which optimizer and learning rate schedule, and which codebase (nanoGPT, LitGPT, OLMo, etc.). Without this, the method cannot be replicated. The user's requirements specifically mention 'Pythia, OLMo-1B, Qwen-0.5B/1.8B' as small open models — the proposal should either use one of these (OLMo-1B is Chinchilla-optimal-friendly and has a public codebase) or explicitly justify the choice of a custom architecture.\"]\nFeedback: The Round 1 revision was thorough — all eight original issues have been addressed, and the proposal is substantially stronger. Three targeted fixes will make this submission-ready:\n\n1. RESOLVE THE TIMELINE CONTRADICTION: The paper cannot claim to target a 16-day deadline while describing a 3-5 month execution plan. Pick one of two framings: (A) Auto-research framing — declare upfront that the submission is enabled by automated experimentation (8-12 days GPU wall-clock) and that writing proceeds in parallel; explicitly carve the paper into 'Tier 1 results (guaranteed by submission)' and 'Tier 2 results (best-effort, described as ongoing if not complete).' (B) Scoped-to-Tier-1 framing — submit with 360M ablations only, explicitly position Tier 2 as future work, and argue that the 8-config ablation at Chinchilla-optimal scale is sufficient to support the core CGS claims. Either framing is honest; the current hybrid is not.\n\n2. ADD MATES TO THE LANDSCAPE AND DIFFERENTIATE: Add a paragraph: 'MATES (NeurIPS 2024, arXiv:2406.06046) trains a lightweight influence model that continuously adapts to the evolving pretraining model's data preferences, achieving 2× the gain of prior SOTA. CGS differs on two axes: (a) CGS requires no influence model training — the FAISS IVF index is built once over the fixed reference corpus, not updated per training step; (b) CGS targets a specific failure mode (CQF distribution-matching rather than quality) rather than maximizing generic influence. MATES is computationally intensive and applied to general pretraining data; CGS is a lightweight post-hoc selector for synthetic-real mixing pipelines.' Include MATES as a formal key reference.\n\n3. FIX THE EVALUATION CIRCULARITY: Demote 'held-out low-occupancy perplexity' to a sanity check and promote the TriviaQA head/tail split as the primary falsifiable metric. The held-out ppl measures exactly what CGS was optimized to cover — it's not an independent test. The TriviaQA split uses an external resource (Wikipedia page views) to define head/tail entities, making it independent of the FAISS cell structure. Add this framing explicitly in the evaluation section: 'We use the TriviaQA tail-entity accuracy as the primary test of whether tail coverage translates to downstream knowledge acquisition, since it is defined independently of our FAISS cell structure.'\n\n4. SPECIFY THE TRAINING ARCHITECTURE: Use OLMo-1B architecture (open codebase, publicly documented) scaled down to 360M for Tier 1 and use OLMo-1B directly for Tier 2. This satisfies the user's requirement to use open small models and makes the experiments fully reproducible with a widely-known codebase.\n\n5. CLARIFY EMBEDDING BUDGET: State explicitly the size of the synthetic candidate pool (e.g., '50M documents from Qwen3-72B, 512 tokens avg') and revise the 10H embedding estimate to match. If the candidate pool is larger, embed in streaming batches and update the budget accordingly.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MISSING CRITICAL CONCURRENT WORK — Group-MATES (NeurIPS 2025, arXiv:2502.14709): This paper extends MATES with clustering-based group-level data selection, achieving 3.5–9.4% relative gains and 1.75× token efficiency over state-of-the-art individual selection. It uses embedding-based clustering to partition data into groups and selects within clusters — structurally overlapping with CGS's Voronoi cell approach. The proposal cites MATES (NeurIPS 2024) but not its NeurIPS 2025 successor. A reviewer will notice this immediately. Differentiation: Group-MATES uses influence-weighted group selection without a real-data reference density; CGS specifically targets low-occupancy tail cells defined against a reference corpus and requires no influence model. This should be added to the landscape section.\", \"EVALUATION MISSING USER-REQUIRED DIVERSITY METRICS: The user's hard constraints explicitly list 'diversity metrics (self-BLEU, n-gram entropy)' as required evaluation. The proposal evaluates TriviaQA tail/head accuracy, Head-to-Tail benchmark, standard downstream tasks, and held-out perplexity — but includes no diversity metrics for the selected synthetic data. CGS should demonstrate that its tail-targeted selection produces more diverse text than CQF (which selects fluent head-distribution text). Self-BLEU and n-gram entropy of selected synthetic data are cheap to compute (CPU-only, no GPU required) and would directly substantiate the coverage-vs-classifier-proxy claim.\", \"ICLR 2026 VENUE STATUS OF FOUNDATION PAPER UNCONFIRMED: arXiv:2510.00866 ('The Data-Quality Illusion') is submitted to ICLR 2026 (OpenReview ID: vSBACt34gS, modified February 2026) but its acceptance/rejection decision could not be confirmed via independent search. If this paper was rejected from ICLR 2026, the 'opportunity' narrative built around it ('CQF is shown to be illusory... arXiv:2510.00866') is weakened. The proposal should either (a) confirm the status and cite it accordingly, or (b) hedge: 'arXiv:2510.00866, under review; the empirical finding stands independently of peer review status.' The current citation as 'submitted to ICLR 2026' is ambiguous.\", \"LESS-IS-MORE DIFFERENTIATION NEEDS EXPLICIT STATEMENT: The proposal says CGS 'extends Less is More to pretraining scale with a tail-density threshold,' but a reviewer could ask: why not just run Less is More (arXiv:2504.14508) on the pretraining synthetic candidate pool with tail filtering? The proposal must explicitly state: 'Less is More maximizes coverage of ALL embedding cells uniformly — without a reference-corpus density criterion, it would waste selection budget on head cells already well-covered by real data. CGS adds the critical step of using real-data Voronoi occupancy as a gate: only tail cells (bottom 20–25% by reference occupancy) are eligible for synthetic coverage. This reference-density threshold is the mechanistic link to the CQF failure documented in arXiv:2510.00866, which Less is More does not establish.'\", \"ONLINE-METHOD COMPETITORS NOT ACKNOWLEDGED: ICLR 2026 accepted two online pretraining data curation methods — 'Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods' (ADAPT) and 'AC-ODM: Actor-Critic Online Data Mixing' — that are direct competitors to offline approaches like CGS. A reviewer familiar with ICLR 2026 will ask why CGS (a static offline filter) is preferable to online reweighting. The proposal should add one sentence: 'Online methods like ADAPT and AC-ODM adapt during training but cannot target the specific synthetic-real tail gap documented in arXiv:2510.00866, since they optimize generic influence rather than reference-density-defined tail coverage; CGS is a zero-overhead offline pre-filter compatible with any online method.'\"]\nFeedback: The Round 2 revision was comprehensive — all five prior issues are resolved. Three targeted fixes will make this submission-ready:\n\n1. ADD GROUP-MATES TO LANDSCAPE: Insert a differentiation paragraph after the MATES discussion: 'Group-MATES (NeurIPS 2025, arXiv:2502.14709) extends MATES to group-level selection by clustering training data using relational influence weights and selecting within clusters, achieving 3.5–9.4% gains. CGS differs on three axes: (a) CGS requires no influence model — Voronoi cells are defined by k-means over the fixed reference corpus, not by data-data influence weights; (b) CGS uses reference-corpus density as the selection criterion, not influence; (c) CGS targets the synthetic-real distribution gap specifically — Group-MATES operates within a single corpus without a real-data reference.' Add arXiv:2502.14709 to key_references.\n\n2. ADD DIVERSITY METRICS TO EVALUATION: The user hard-requires self-BLEU and n-gram entropy. Add to the evaluation section: 'Diversity of selected synthetic data: we compute corpus-level self-BLEU (lower = more diverse) and 4-gram entropy (higher = more diverse) over the synthetic subset selected by each method. CGS should show lower self-BLEU and higher n-gram entropy than CQF, since CQF preferentially selects fluent head-distribution text with low lexical diversity. This is computed post-selection on CPU before training begins.' These are zero-GPU-cost and directly substantiate the coverage claim.\n\n3. CLARIFY ICLR 2026 STATUS OF 2510.00866: Search or state that the paper's review status is uncertain and hedge accordingly. Change all references to 'submitted to ICLR 2026 (preprint; peer review status pending)' to avoid implying acceptance or publication. The empirical finding is sound regardless of venue; the paper should be defensible as a preprint citation.\n\n4. Add a single sentence addressing online-method competitors (ADAPT/AC-ODM, ICLR 2026) positioning CGS as a compatible pre-filter rather than a competing paradigm.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"EMBEDDING COMPUTE ARITHMETIC ERROR — BUDGET VIOLATION: The '~36 H100-hours' embedding figure is internally inconsistent with the stated throughput. At 100K tok/s per H100 GPU, embedding 25.6B synthetic tokens alone requires 256,000s = 71 GPU-hours; adding 5B reference tokens adds 14H = 85H total. On 4 GPUs: wall-clock = 21.3H, GPU-hours = 85H — NOT 36H. The '36H / 4 GPUs = 9H wall-clock' arithmetic requires 236K tok/s per GPU, which contradicts the stated 100–150K range. The corrected total budget is ~2H (Exp 0) + ~85H (embedding) + ~72H (Tier 1) + ~88H (Tier 2) + ~2H (eval) = ~249H, exceeding the user's hard ≤200H constraint by ~25%. The generator must either: (a) document a higher throughput (e.g., 250K+ tok/s with optimized large-batch encoding on H100) with citations, (b) reduce the synthetic pool to ~15M documents to bring embedding under 30H, or (c) explicitly scope Tier 2 as unfunded and recompute the budget without it (~161H).\", \"PROXY MODEL RELIABILITY UNADDRESSED: 'Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice' (ICLR 2026 Poster, openreview.net/forum?id=2FZC0c06jP) directly shows that conclusions about data selection quality 'can flip with even minor adjustments to training hyperparameters' when using small proxy models. CGS uses Pythia-410M (Tier 1) to determine the winning selection method before scaling to Pythia-1.4B (Tier 2), without any mention of the recommended reduced learning-rate protocol (10–100× smaller than standard) to ensure transfer reliability. The generator should add one sentence in the Tier 1 training setup: 'To improve reliability of proxy-to-full-scale transfer, we follow the protocol of [ICLR 2026 paper] and run Tier 1 with both standard and 10× reduced learning rates; the winning configuration uses the reduced-LR ranking.'\", \"arXiv:2510.00866 STATUS: This foundational paper ('The Data-Quality Illusion'), upon which the entire 'opportunity' narrative is built, does not appear in any ICLR 2026 accepted paper listing despite having been submitted (OpenReview ID: vSBACt34gS). ICLR 2026 decisions are public as of April 2026. Probable rejection. The proposal correctly hedges as 'preprint; peer review status pending,' but the generator should add a sentence that explicitly acknowledges the opportunity narrative holds independently of peer review: 'The empirical finding that CQF improves downstream task performance via distribution-matching rather than genuine quality improvement is independently reproducible; the CGS method does not depend on arXiv:2510.00866 being published at a venue.'\", \"ABLATION GRID DESCRIPTION INCONSISTENCY: The proposal states '8 configurations: (i) CGS vs. CQF-Wikipedia vs. CQF-FineWebEdu vs. random (4 selection methods); (ii) tail threshold 20th vs. 25th percentile.' But only CGS has a tail threshold — the other three methods have no threshold parameter. Crossing 4 methods × 2 thresholds implies that CQF-Wikipedia, CQF-FineWebEdu, and random are each run twice, which is wasteful and unexplained. The generator should clarify: either the grid is 6 runs (CGS-20th, CGS-25th, CQF-Wikipedia, CQF-FineWebEdu, random, plus one additional baseline) or 5 runs (CGS × 2 + 3 others × 1), not 8.\"]\nFeedback: The proposal has addressed all five Round 3 issues cleanly — Group-MATES differentiation, diversity metrics (self-BLEU/n-gram entropy), 2510.00866 status hedge, Less-is-More explicit differentiation, and ADAPT/AC-ODM positioning are all now handled correctly. The method remains novel and the evaluation design is among the strongest aspects of the proposal. Three targeted fixes will make this submission-ready:\n\n1. FIX EMBEDDING COMPUTE AND REBALANCE BUDGET: The '36H embedding' figure has a verifiable arithmetic error — correct it to ~57–85H depending on throughput, or better, document the actual H100 throughput with optimized large-batch inference (claim a specific number like '~250K tok/s with batch=512 on H100 using flash attention') and show the math. If the corrected embedding budget pushes total over 200H, explicitly drop Tier 2 from the funded scope: 'Tier 2 (1.4B) runs proceed only if embedding completes in under 45H; otherwise Tier 2 is deferred to camera-ready per the proposal's early-stop clause.' This keeps the budget under control without changing the method.\n\n2. ADD PROXY RELIABILITY NOTE: Insert one sentence in the training setup: 'Following the protocol of [ICLR 2026 proxy reliability paper], Tier 1 ablations are run at both standard learning rate (3×10⁻⁴) and a 10× reduced rate (3×10⁻⁵); selection method rankings are determined from the reduced-LR runs for reliable Tier 2 transfer.' This costs zero extra GPU-hours (same runs, different LR) and preempts a reviewer familiar with ICLR 2026 data curation work.\n\n3. CLARIFY ABLATION GRID: Specify that the 8 configurations are: (CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, random) = 5 configurations, OR explain what the 6th–8th configurations are (e.g., additional IVF nlist sensitivity runs). As written, '4 methods × 2 thresholds = 8' implies running non-CGS methods with two threshold values, which is a design error.\n\n4. ADD INDEPENDENT VALIDATION SENTENCE: Add: 'The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status; CGS would be motivated equally if the finding were confirmed by independent replication.'\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-09T20:37:41.346Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-09T20:37:41.346Z",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-09T20:37:41.376Z_

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

## Idea under review (round 5/10)
{
  "title": "Tail-Coverage-Guided Synthetic Data Selection to Replace Classifier Quality Filtering",
  "core_problem": "Classifier-based quality filtering (CQF), the dominant method for selecting synthetic pretraining data used by GPT-3, LLaMA, and PaLM, is shown to be illusory — it improves downstream task performance not by improving language modeling quality but by implicit distribution-matching rather than genuine quality signals. Concurrently, synthetic data exhibits systematic distributional discrepancies relative to real data: top-p and temperature sampling truncate low-probability continuations, causing rare factual content to be systematically underrepresented in synthetic corpora. Kandpal et al. (ICML 2023) established a direct causal link: LLM accuracy on factual questions correlates strongly with the frequency of the underlying entity in pretraining documents, confirming that tail-knowledge acquisition depends on tail-content exposure during training. No principled selection criterion corrects for this distributional gap: CQF does not target it (and may worsen it by filtering toward fluent head-distribution text), while naïve random sampling inherits the generator's truncation bias wholesale. More recent model-aware selectors such as MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) adapt dynamically to the evolving model's preferences but do not target the specific tail-distribution gap — they optimize for generic influence rather than for correcting truncation-induced underrepresentation.",
  "opportunity": "Three concurrent findings create a gap that demands a new method: (1) 'The Data-Quality Illusion' (arXiv:2510.00866, preprint; peer review status pending) demonstrates that CQF does not improve language modeling on held-out high-quality data and argues the field should rethink synthetic data filtering from first principles; (2) 'Data Value in the Age of Scaling' (arXiv:2511.13640) identifies tail-knowledge underrepresentation as a systematic distributional discrepancy in synthetic data under real-synthetic mixing, linked to generative truncation mechanisms; (3) Kandpal et al. (ICML 2023) provides external causal validation: pretraining document frequency is a strong predictor of downstream accuracy on rare facts. Together, these findings establish that (a) CQF is the wrong solution, (b) the actual problem is a distributional gap at the tail, and (c) closing the tail gap causally improves knowledge acquisition. The opportunity is 'Coverage-Guided Sampling' (CGS): select synthetic examples to maximize marginal coverage of low-density regions of the real-data embedding space, directly targeting the distributional gap that CQF fails to address. This is the first synthetic data selector explicitly designed around the mechanism documented in arXiv:2510.00866 rather than a classifier proxy. The core empirical finding of arXiv:2510.00866 — that CQF performance gains on downstream tasks do not correspond to lower perplexity on held-out high-quality text — is reproducible from first principles and does not depend on the paper's peer review status; CGS would be motivated equally if the finding were confirmed by independent replication.",
  "landscape": "CQF is used by all major pretraining pipelines (GPT-3, LLaMA, PaLM, RedPajama) but arXiv:2510.00866 (preprint; peer review status pending) shows its quality signal is misleading. Six clusters of prior work bound the proposal:\n\n**Diversity-quality pretraining selection.** Quad (arXiv:2409.16986, ICLR 2025 Spotlight) is the most important prior work. Quad clusters all pretraining data and uses a Multi-Armed Bandit (MAB) scheme favoring clusters with high influence scores (quality) or low selection frequency (diversity). CGS differs on three axes: (1) Criterion — CGS uses a real-data tail-density threshold (bottom 20–25% by Voronoi cell occupancy in a reference corpus) rather than influence-weighted underrepresentation; CGS does not require influence score computation, which is expensive to scale to billions of synthetic candidates; (2) Target — CGS applies specifically to the synthetic data mixing problem and requires a real-data reference corpus to define 'tail'; Quad operates within a single multi-source corpus without a reference density; (3) Motivation — CGS is grounded in the CQF failure mechanism documented in arXiv:2510.00866. QuaDMix (arXiv:2504.16511, preprint, withdrawn from ICLR 2026) from ByteDance proposes a parameterized quality-diversity sampling function using domain classification for diversity measurement and LightGBM for parameter search. Like Quad, QuaDMix does not target real-data tail density specifically.\n\n**Model-aware selection.** MATES (arXiv:2406.06046, NeurIPS 2024) trains a lightweight BERT-base influence model that continuously adapts to the evolving pretraining model's data preferences, updating every 10,000 steps. MATES achieves 2× the gain of prior SOTA (QuRating) on 410M and 1B models, at 11.5–21.7% computational overhead. CGS differs on three axes: (a) CGS requires no influence model training — the FAISS IVF index is built once over the fixed reference corpus before pretraining begins, versus MATES's periodic BERT-base retraining; (b) CGS requires no reference task definition — MATES's performance varies substantially with reference task choice, a deployment-time burden; (c) CGS targets a specific, mechanistically motivated failure mode (CQF distributional bias) rather than maximizing generic influence scores.\n\nGroup-MATES (arXiv:2502.14709, NeurIPS 2025) extends MATES to group-level selection: it trains a relational data influence model that weights individual sample influence by inter-data relationships, partitions the training corpus into clusters via these relationship weights, and selects within each cluster independently, achieving 3.5–9.4% relative gains and 1.75× token efficiency over individual selection baselines on DCLM at 400M–3B scales across 22 tasks. CGS differs on three axes: (a) CGS requires no influence model — Voronoi cells are defined by k-means over a fixed reference corpus embedding, not by data-data relational influence weights, making CGS zero-overhead relative to training; (b) CGS uses reference-corpus occupancy density as the selection gate — only tail cells (bottom 20–25% by reference occupancy) are eligible for synthetic coverage — rather than influence-weighted within-cluster scoring; (c) CGS targets the specific synthetic-real distributional gap documented in arXiv:2511.13640: it applies to a fixed synthetic candidate pool relative to a real-data reference corpus, whereas Group-MATES operates within a single training corpus without a reference density criterion.\n\n**Coverage-based fine-tuning.** 'Less is More: Adaptive Coverage for Synthetic Training Data' (arXiv:2504.14508, 2025) applies a greedy maximum-coverage objective to select synthetic fine-tuning data for NLP classifiers. CGS shares the max-coverage algorithmic skeleton but differs critically in three respects: (1) 'Less is More' maximizes coverage of ALL embedding cells uniformly — without a reference-corpus density criterion, it would waste selection budget on head cells already well-covered by real data, failing to address the distributional gap that CQF leaves open; CGS adds the critical step of using real-data Voronoi occupancy as a gate: only tail cells (bottom 20–25% by reference occupancy) are eligible, ensuring the entire selection budget is concentrated on underrepresented regions; (2) CGS applies at pretraining scale (hundreds of millions of candidates), requiring FAISS IVF for tractability; (3) this reference-density threshold is the mechanistic link to the CQF failure documented in arXiv:2510.00866, which 'Less is More' does not establish.\n\n**Online pretraining data curation.** ADAPT ('Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods', arXiv:2512.24503, ICLR 2026 Workshop DATA-FM) and AC-ODM ('Actor-Critic Online Data Mixing', arXiv:2505.23878, preprint) represent an online paradigm: rather than pre-filtering the candidate pool, they dynamically reweight or re-mix training samples during training based on loss signals. CGS is orthogonal and compatible: as a static offline pre-filter, it reduces the synthetic candidate pool to tail-coverage-optimal documents before training begins with zero ongoing overhead; an online reweighter can further adapt the mix at training time after CGS has already narrowed the pool. Neither ADAPT nor AC-ODM targets the specific synthetic-real tail-density gap documented in arXiv:2510.00866 — they optimize generic influence or domain balance, not reference-density-defined tail coverage.\n\n**Synthetic data scale findings.** 'Demystifying Synthetic Data in LLM Pre-training' (arXiv:2510.01631, EMNLP 2025) finds ~30% rephrased synthetic data is empirically optimal but provides no mechanistic filter. arXiv:2511.13640 characterizes three-phase scaling behavior under real-synthetic mixing and identifies tail underrepresentation as a systematic discrepancy without a selection remedy.\n\n**Tail knowledge evaluation and deduplication.** Kandpal et al. (arXiv:2211.08411, ICML 2023) establish that LLM accuracy on factual questions correlates causally with pretraining document frequency, providing the empirical foundation for CGS's tail-coverage hypothesis. 'Head-to-Tail' (arXiv:2308.10168, NAACL 2024) provides a purpose-built 18K QA benchmark explicitly stratified into head, torso, and tail facts by knowledge graph frequency — an independent evaluation resource for CGS. D4 (NeurIPS 2023) uses FAISS k-means for deduplication/diversification via distance-to-centroid pruning; it applies a distance heuristic not a tail-density threshold and does not target the synthetic selection sub-problem.",
  "approach": "Coverage-Guided Sampling (CGS) selects synthetic pretraining data by maximizing coverage of underrepresented tail regions in real-data embedding space.\n\n**Method.** We embed a reference corpus (5B-token stratified sample of Dolma, preserving domain balance) and all candidate synthetic documents using ModernBERT-large, then build a FAISS IVF index over the real-data embeddings. The resulting Voronoi cell structure partitions semantic space; 'tail cells' are defined as cells in the bottom 20–25% by real-data occupancy. CGS then greedily selects synthetic documents maximizing marginal coverage of tail cells via a streaming maximum-coverage subproblem — no quality classifier training required. ModernBERT-large is chosen for embedding over larger alternatives due to its ~100–150K tokens/sec throughput on H100 (vs. ~15–30K for Qwen3-Embedding-8B), making 15M-document indexing tractable within the compute budget; embedding quality is validated in Experiment 0.\n\n**Mechanistic validation experiment (Experiment 0, ~2 H100-hours).** Before committing to training runs, we validate the core empirical hypothesis: (a) Generate three synthetic corpora of 10M tokens each using Qwen3-72B with top-p ∈ {0.5, 0.85, 0.95}; embed and assign each document to a Voronoi cell; measure whether lower top-p concentrates documents in higher-occupancy cells (expected: yes, since low top-p collapses to high-probability continuations); (b) Embed 5,000 Wikidata long-tail documents (entities appearing <100 times in C4) and confirm they cluster significantly more in low-occupancy cells than a random C4 sample. If (a) shows r < 0.3 between top-p and mean cell occupancy, or (b) shows no significant enrichment, halt before Tier 1 and revise the tail-density criterion.\n\n**Model architecture and training.** Following the precedent of MATES (NeurIPS 2024), Quad (ICLR 2025), and D4 (NeurIPS 2023), we use the Pythia model family (EleutherAI GPT-NeoX codebase) for full reproducibility:\n- *Tier 1 — Systematic ablation: Pythia-410M* (24 layers, hidden dim 1024, 16 heads, 2048 sequence length; ~8B tokens, Chinchilla-optimal). AdamW optimizer with β1=0.9, β2=0.95, weight decay 0.1; cosine LR schedule with 1% warmup steps. Following Wang et al. ('Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice,' ICLR 2026 Poster), all Tier 1 ablations use a 10× reduced peak learning rate of 3×10⁻⁵ (instead of the standard 3×10⁻⁴) to ensure selection method rankings derived from the 410M proxy runs transfer reliably to Tier 2 at 1.4B scale — this costs no additional GPU-hours since the reduced-LR runs replace rather than supplement standard-LR runs. Batch size ~2M tokens. 5 configurations: CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, and random baseline. Only CGS has a tail-threshold parameter; the three non-CGS methods run once without threshold variation. Each run: ~9 H100-hours on 1 GPU.\n- *Tier 2 — Scaling check: Pythia-1.4B* (24 layers, hidden dim 2048, 16 heads, 2048 sequence length; 10B tokens). Same optimizer family with peak LR 2×10⁻⁴. 2 configurations: best CGS from Tier 1 vs. CQF-FineWebEdu. Each run: ~44 H100-hours (4 GPUs × ~11h wall-clock via data parallelism). Using Pythia-1.4B (not 1.3B) ensures exact architecture reproducibility with the published model family.\n\n**Synthetic candidate pool.** We precompute embeddings for a fixed 15M-document synthetic pool generated by Qwen3-72B (top-p=0.9, temperature=1.0, avg 512 tokens/document = 7.68B tokens total). At 100K tokens/sec per H100: the 7.68B synthetic tokens require 76,800s ≈ 21.3 GPU-hours; the 5B-token reference corpus requires 50,000s ≈ 13.9 GPU-hours; total embedding ≈ 35 GPU-hours ≈ 8.8H wall-clock on 4 GPUs. This pool size provides ample selection diversity: 7.68B tokens exceeds the synthetic allocation for both Tier 1 (~2.4B tokens at 30% synthetic) and Tier 2 (~3B tokens at 30% synthetic) by over 2.5×. FAISS IVF build is CPU-bound (~2h on 32 cores) and runs concurrently with early embedding steps.\n\n**IVF nlist calibration.** nlist ≈ sqrt(N_reference_docs) per FAISS best practices. Tier 1 pilots probe two nlist settings (±30%) to confirm tail cell occupancy is well-separated; this is CPU-only analysis on the pre-built index (zero GPU cost). If cell structure is degenerate, we correct before the Tier 2 run.\n\n**Evaluation — primary, secondary, and diversity metrics.** The evaluation design explicitly separates the training criterion (FAISS cell coverage) from the test signal to avoid circularity:\n\n(1) *Primary — TriviaQA head/tail accuracy split (independent external metric)*: Using Wikipedia page-view statistics to stratify TriviaQA questions into head entities (top 20% by views, ~1K questions) and tail entities (bottom 20%, ~1K questions), we measure accuracy separately. This stratification uses an external resource (Wikipedia traffic data) wholly independent of the FAISS cell structure. Per Kandpal et al. (ICML 2023), tail-entity accuracy is the most causally meaningful test of whether tail coverage translates to knowledge acquisition. We report the tail/head accuracy ratio as the primary CGS-vs-CQF gap metric.\n\n(2) *Additional independent benchmark — Head-to-Tail (NAACL 2024)*: This purpose-built 18K QA benchmark stratifies facts into head, torso, and tail by knowledge graph frequency (Wikidata). It provides a second external validation of tail knowledge independent of both FAISS and Wikipedia pageviews, strengthening the falsifiability of the tail-coverage claim.\n\n(3) *Secondary — Standard downstream benchmarks*: HellaSwag, WinoGrande, ARC-E/C, PIQA — required for comparability with Quad, D4, MATES, Group-MATES, and CQF baselines. CGS should match or exceed CQF on these benchmarks; failure here would indicate coverage-only selection sacrifices head-distribution capabilities.\n\n(4) *Diversity of selected synthetic data (CPU-only, zero GPU cost)*: We compute corpus-level self-BLEU (Zhu et al., 2018; lower = more diverse) and 4-gram entropy (higher = more diverse) over the synthetic subset selected by each method (CGS, CQF-Wikipedia, CQF-FineWebEdu, random). These metrics are computed post-selection before training begins. CGS should exhibit lower self-BLEU and higher n-gram entropy than CQF-selected data, since CQF preferentially selects fluent head-distribution text with low lexical diversity. This directly substantiates the coverage-vs-classifier-proxy claim: not only does CGS target underrepresented semantic regions, but the selected text should be measurably more lexically diverse than CQF output.\n\n(5) *Diagnostic — Held-out low-occupancy perplexity*: 5% of reference corpus documents from the bottom 20% occupancy cells are held out before training and used to measure model perplexity. This metric is demoted to a sanity check because CGS is explicitly optimized to cover exactly those cells — perplexity improvement here confirms distribution matching, not necessarily genuine knowledge acquisition. It is reported alongside (1) and (2) but not used as a primary falsifiability claim.\n\n**Falsifiable primary claim**: CGS achieves higher TriviaQA tail-entity accuracy than CQF while matching CQF on standard downstream benchmarks, directly operationalizing the quality-vs-coverage paradox documented in arXiv:2510.00866. The diversity metrics (self-BLEU, n-gram entropy) provide a secondary mechanistic check confirming that CGS's tail-coverage selection is not collapsing to a high-fluency, low-diversity subset.\n\n**Timeline and execution mode.** Given the EMNLP 2026 ARR deadline of May 25, 2026 (16 days from proposal date), the primary execution path is auto-research mode. GPU wall-clock with 4× H100: Experiment 0 (~2h) → Embedding (~8.8h, 4 GPUs) → FAISS build (~2h CPU concurrent) → Tier 1 ablation grid (~18h, 4 experiments in parallel in batch 1, then 1 remaining) → Tier 2 scaling check (~22h, 2 sequential runs with 4-GPU data parallelism). Total GPU wall-clock: ~50.8 hours (~2.1 days). Paper writing begins in parallel on day 1; Tier 1 results are guaranteed by day 4; Tier 2 results are best-effort. If Tier 2 runs do not complete before submission, the 1.4B experiments are described as ongoing and submitted to camera-ready.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~172 H100-hours (Experiment 0 ~2h; embedding ModernBERT-large on 15M synthetic docs + 5B reference corpus ~35h [7.68B synthetic tokens ÷ 100K tok/s = 21.3h; 5B reference ÷ 100K tok/s = 13.9h; total = 35.2h, verified arithmetic]; FAISS IVF build CPU-bound ~0h GPU; Tier 1 ablations 5 configurations × ~9h = 45h; Tier 2 scaling check 2 runs × ~44h = 88h; misc eval ~2h). Synthetic pool reduced from 50M to 15M documents to correct the embedding budget; 7.68B tokens exceeds the synthetic allocation for both training tiers by >2.5×, preserving selection diversity.",
      "gpu_utilization": "Low (~40% active) — researcher waits between tiers to review Experiment 0 results and pilot outcomes before committing to 1.4B runs.",
      "timeline": "3–5 months. INCOMPATIBLE with May 25, 2026 ARR deadline — use auto-research mode for deadline-constrained execution.",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$420–615 at $2.44–3.56/hr per H100 (RunPod/Lambda Labs current pricing)",
      "risk_note": "If Experiment 0 (mechanistic validation) fails — i.e., top-p does not correlate with cell occupancy in the expected direction — the core hypothesis needs revision before Tier 1 ablations begin. Caught in the first ~2 H100-hours."
    },
    "human_in_loop": {
      "gpu_hours": "~190 H100-hours (manual base ~172H plus agent overhead: 2 additional 410M sensitivity runs for IVF nlist ±30% around baseline and ModernBERT-large vs. sentence-transformers/all-MiniLM-L6-v2 embedding model speed check, each ~9h = 18H extra; plus ~0H GPU for nlist structure analysis which is CPU-only).",
      "gpu_utilization": "Moderate (~60% active) — agent queues experiments continuously but awaits human approval before committing to each Tier 2 run.",
      "timeline": "4–6 weeks. INCOMPATIBLE with May 25, 2026 ARR deadline — use auto-research mode for deadline-constrained execution.",
      "team": "1 researcher, ~45 min/day check-in to approve tier transitions and review Experiment 0 results",
      "claude_api_cost": "$200–350 (experiment queue management, Experiment 0 result interpretation, IVF calibration guidance)",
      "estimated_gpu_cost": "~$464–676 at $2.44–3.56/hr per H100"
    },
    "auto_research": {
      "gpu_hours": "~175 H100-hours (Experiment 0 ~2h + embedding ModernBERT-large for 15M synthetic docs [7.68B tokens] + 5B reference corpus ~35h + FAISS IVF build CPU-bound ~0h GPU + Tier 1 ablation grid 5 configurations × ~9h = 45h + Tier 2 scaling check 2 runs × ~44h = 88h + misc eval ~3h). Capped at 175H by early-stopping if Experiment 0 fails (saves ~138H by avoiding Tier 1 and Tier 2).",
      "gpu_utilization": "High (~85% active) — agent queues Experiment 0 → embedding → FAISS build → Tier 1 ablation grid → Tier 2 runs without human wait. ~15% overhead from API round-trips and CPU-bound FAISS builds between GPU steps.",
      "timeline": "8–12 days total: ~2.1 days GPU wall-clock compute (50.8 hours on 4× H100) + paper writing in parallel from day 1. Tier 1 results available by day 4; Tier 2 results by day 5. Writing days 1–14 (parallel); submission day 16 (May 25, 2026 ARR deadline). COMPATIBLE with deadline under this framing: Tier 1 results are guaranteed at submission; Tier 2 results are best-effort and described as ongoing in the paper if not complete.",
      "team": "0 (initial setup ~3h: configure ModernBERT-large embedding pipeline with FAISS IVF builder, GPT-NeoX training harness with eval on HellaSwag/WinoGrande/ARC/PIQA + TriviaQA head/tail + Head-to-Tail benchmark)",
      "claude_api_cost": "$600–900 (automated Experiment 0 interpretation, ablation grid orchestration, early-stopping decisions, TriviaQA stratification computation, final report generation — estimated 5,000–8,000 API turns)",
      "estimated_gpu_cost": "~$427–623 at $2.44–3.56/hr per H100",
      "speed_bottleneck": "4× H100 allows: Embedding (15M synthetic docs + 5B reference corpus) completes in ~8.8h wall-clock (35H ÷ 4 GPUs); Tier 1 grid runs in ~18h wall-clock (4 configs in parallel batch 1, then 1 remaining config in batch 2, each ~9H on 1 GPU); Tier 2 serializes at ~11h wall-clock each with 4-GPU data parallelism (2 runs = 22h). Total GPU wall-clock: ~2h (Exp 0) + ~8.8h (embedding) + ~18h (Tier 1) + ~22h (Tier 2) ≈ 50.8h ≈ 2.1 days.",
      "risk_note": "Early-stopping trigger: if Experiment 0 shows Pearson r < 0.3 between top-p value and mean cell occupancy rank, halt and report mechanism failure before consuming Tier 1 compute. Pre-specified threshold prevents exhaustive exploration of a degenerate configuration."
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
    "QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining (arXiv:2504.16511, preprint, withdrawn from ICLR 2026)",
    "MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models (arXiv:2406.06046, NeurIPS 2024)",
    "Group-MATES: Group-Level Data Selection for Language Model Pretraining (arXiv:2502.14709, NeurIPS 2025)",
    "Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice (Wang et al., ICLR 2026 Poster, openreview.net/forum?id=2FZC0c06jP)",
    "Rethinking Data Curation in LLM Training: Online Reweighting Offers Better Generalization than Offline Methods — ADAPT (arXiv:2512.24503, ICLR 2026 Workshop DATA-FM)",
    "AC-ODM: Actor-Critic Online Data Mixing for Sample-Efficient LLM Pretraining (arXiv:2505.23878, preprint)",
    "Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls (arXiv:2510.01631, EMNLP 2025)",
    "Large Language Models Struggle to Learn Long-Tail Knowledge (Kandpal et al., arXiv:2211.08411, ICML 2023)",
    "Head-to-Tail: How Knowledgeable are Large Language Models in Long-Tail Knowledge? (arXiv:2308.10168, NAACL 2024)",
    "Measuring Diversity in Synthetic Datasets (arXiv:2502.08512, ICML 2025)",
    "Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning (arXiv:2511.01490, ACL Findings 2026)",
    "Less is More: Adaptive Coverage for Synthetic Training Data (arXiv:2504.14508, 2025)",
    "D4: Improving LLM Pretraining via Document De-Duplication and Diversification (NeurIPS 2023)",
    "Scaling Laws of Synthetic Data for Language Models (arXiv:2503.19551, 2025)",
    "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling (arXiv:2304.01373, ICML 2023)"
  ],
  "description": "Classifier-based quality filtering (CQF) — the dominant synthetic pretraining selector used by GPT-3, LLaMA, and PaLM — has been shown to boost downstream task scores via implicit distribution-matching rather than genuine quality improvement (arXiv:2510.00866, preprint; peer review status pending; independently reproducible from first principles regardless of venue outcome). Concurrently, Kandpal et al. (ICML 2023) established that LLM accuracy on rare facts causally correlates with pretraining document frequency, confirming that tail-content exposure drives tail-knowledge acquisition; and arXiv:2511.13640 documents systematic tail underrepresentation in synthetic data via top-p/temperature truncation. This project proposes Coverage-Guided Sampling (CGS), the first principled pretraining data selector grounded in the actual distributional failure mechanism of CQF. CGS embeds a 5B-token reference corpus and a fixed 15M-document synthetic candidate pool (7.68B tokens) using ModernBERT-large (chosen for ~100–150K tokens/sec throughput on H100, vs. ~15–30K for Qwen3-Embedding-8B; total embedding ≈ 35 GPU-hours: 7.68B synthetic tokens ÷ 100K tok/s = 21.3H + 5B reference ÷ 100K tok/s = 13.9H ≈ 8.8H wall-clock on 4 GPUs), builds a FAISS IVF index over the real corpus, identifies low-density Voronoi 'tail cells' (bottom 20–25% by occupancy), and greedily selects synthetic documents maximizing marginal tail-region coverage — no classifier training required. A mandatory Mechanistic Validation Experiment (~2 H100-hours) confirms that Voronoi cell density correlates with top-p sampling behavior before committing to training runs. We train using the Pythia model family (EleutherAI GPT-NeoX codebase): Tier 1 uses Pythia-410M at Chinchilla-optimal scale (~8B tokens, 5 ablation configurations [CGS-20th percentile, CGS-25th percentile, CQF-Wikipedia, CQF-FineWebEdu, random], ~45 H100-hours); following Wang et al. (ICLR 2026 Poster), Tier 1 uses a 10× reduced peak learning rate (3×10⁻⁵) to improve proxy-to-full-scale ranking reliability at zero extra compute cost. Tier 2 uses Pythia-1.4B at 10B tokens (2 configurations, ~88 H100-hours); total budget ~175 H100-hours including ~35 H100-hours for embedding, well within the ≤200H constraint. Evaluation resolves circularity: TriviaQA tail-entity accuracy (stratified by Wikipedia pageviews, independent of FAISS) and the Head-to-Tail benchmark (NAACL 2024) are primary falsifiability metrics; corpus-level self-BLEU and 4-gram entropy over selected synthetic data are computed CPU-only post-selection to confirm CGS produces more diverse output than CQF; held-out low-occupancy perplexity is demoted to a diagnostic. Closest prior work: Quad (ICLR 2025) uses influence-weighted cluster MAB — CGS requires no influence scoring. MATES (NeurIPS 2024) and Group-MATES (NeurIPS 2025) train influence models — CGS builds its FAISS index once with zero ongoing overhead and no reference task dependency. 'Less is More' maximizes uniform coverage of all cells — CGS adds a real-data reference-density gate (bottom 20–25% occupancy only) establishing the mechanistic link to arXiv:2510.00866. Online methods ADAPT and AC-ODM reweight during training — CGS is a compatible offline pre-filter. Primary execution path: auto-research mode (4× H100, ~2.1 days GPU wall-clock, paper writing in parallel), targeting EMNLP 2026 ARR deadline May 25, 2026, with Tier 1 results guaranteed at submission.",
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
  "promptId": "0af484b0-d64d-437e-a339-81bb41755234",
  "type": "user",
  "uuid": "cdcfaa6a-1620-4246-83c6-d0d7abeb6cca",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-09T20:37:41.373Z_

```json
{
  "parentUuid": "cdcfaa6a-1620-4246-83c6-d0d7abeb6cca",
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
  "uuid": "44d9c582-1f53-4ecd-a1a9-1c69b418fd11",
  "timestamp": "2026-05-09T20:37:41.373Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-09T20:37:41.373Z_

```json
{
  "parentUuid": "44d9c582-1f53-4ecd-a1a9-1c69b418fd11",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ea579794-5dcc-44d1-ad66-0a53d9bb7f38",
  "timestamp": "2026-05-09T20:37:41.373Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
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
  "leafUuid": "ea579794-5dcc-44d1-ad66-0a53d9bb7f38",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Tail-coverage-guided synthetic data selection method",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c"
}
```

---

### Assistant

_source line 8 · 2026-05-09T20:38:14.419Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea for EMNLP 2026 submission. This is Round 5 of 10. The idea is "Tail-Coverage-Guided Synthetic Data Selection to Replace Classifier Quality Filtering" (Coverage-Guided Sampling / CGS).

Let me assess what has been addressed from previous rounds:

**Round 1 issues addressed:**
- Venue claim error for arXiv:2510.00866 - NOW FIXED: cited as "preprint; peer review status pending"
- Claim overstatement about 2511.13640 - NOW FIXED
- Missing Quad and QuaDMix - NOW INCLUDED in landscape


- Mechanistic gap - NOW ADDRESSED with Experiment 0
- Compute constraint mismatch - NOW FIXED (15M docs, not 50M)
- Short training run risk - NOW FIXED with Chinchilla-optimal scale
- Wikidata tail probe - NOW IMPROVED with TriviaQA + Head-to-Tail
- Less is More differentiation - NOW EXPLICIT

**Round 2 issues addressed:**
- Timeline contradiction - NOW FIXED (auto-research mode as primary)
- MATES absent - NOW INCLUDED
- Evaluation circularity - NOW FIXED (held-out perplexity demoted to diagnostic)
- Embedding budget underestimated

**Round 3 issues addressed:**
- Embedding compute - NOW FIXED (15M documents, 7.68B tokens)
- Training architecture - NOW FIXED (Pythia family)
- Group-MATES - NOW INCLUDED
- Diversity metrics - NOW INCLUDED (self-BLEU, n-gram entropy)
- ICLR 2026 status - NOW HEDGED
- Less-is-More differentiation - NOW EXPLICIT
- ADAPT/AC-ODM - NOW ADDRESSED

**Round 4 issues addressed:**
- Embedding compute arithmetic - NOW FIXED: 7.68B synthetic + 5B reference = 12.68B tokens at 100K tok/s = ~35 GPU-hours (21.3h + 13.9h), which is 8.8h wall-clock on 4 GPUs. Synthetic pool reduced to 15M docs × ~512 tokens = 7.68B tokens
- Proxy model reliability - NOW FIXED: uses 10× reduced LR (3×10⁻⁵) for Tier 1
- arXiv:2510.00866 status - NOW ADDRESSED with explicit independence statement
- Ablation grid inconsistency - NOW FIXED: 5 configurations (CGS-20th, CGS-25th, CQF-Wikipedia, CQF-FineWebEdu, random)

The generator has addressed all prior round issues thoroughly. Now I'm doing my own independent verification of the key claims, starting with ModernBERT-large throughput on H100 and the embedding token calculations.

I'm checking the math on the synthetic token generation—15M documents at 512 tokens each gives 7.68B tokens, which at 100K tokens per second on an H100 works out to about 21.3 GPU-hours. I'm also verifying the training costs for Pythia models, whether the referenced papers actually exist and support the claims made, and checking the status of Group-MATES, the Wang et al. proxy reliability paper, and AC-ODM as a recent preprint. Let me search for these to validate everything.

The budget calculations are checking out now—the embedding phase totals around 35.2 GPU-hours, which on 4 GPUs translates to 8.8 hours of wall-clock time. The training tiers come to about 45 GPU-hours for the first tier and 88 for the second, plus a couple hours for the initial experiment and evaluation work. Adding it all up gets me to roughly 173 GPU-hours, which fits comfortably within the 200-hour constraint.

For the timeline, I'm looking at about 2.1 days of wall-clock time across the 4 H100s for the experiments, with paper writing happening in parallel over 16 days total. The first tier should wrap by day 4 and the second by day 5, which gives plenty of buffer before the May 25 EMNLP deadline.

Now I'm digging into what might be off or incomplete. The ModernBERT-large throughput claim of 100-150K tokens per second on an H100 needs verification—with 395M parameters and efficient batching plus flash attention, it sounds reasonable but I should double-check. I'm also noticing the QuaDMix claim about being withdrawn seems to cut off mid-thought.

Beyond that, I need to verify several citations and claims: whether the synthetic data scaling laws paper actually addresses tail coverage gaps, if AC-ODM from May 2025 is real, whether Head-to-Tail from NAACL 2024 exists and matches what's described, and checking that Wang et al. ICLR 2026 poster reference is correct.

I should also search for any papers explicitly doing coverage-guided or tail-density-guided synthetic data selection that might have been missed, and look into what recent work exists on data contamination and synthetic data feedback loops given EMNLP's special theme. Let me start with targeted searches on tail-coverage selection methods, Group-MATES verification, and the latest 2025-2026 synthetic data quality papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea579794-5dcc-44d1-ad66-0a53d9bb7f38",
  "isSidechain": false,
  "requestId": "req_011CasdyVsneG3D9JNh6Kx43",
  "type": "assistant",
  "uuid": "4011634d-ccaf-4bb5-be7c-701b8ce30963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015UQh96WhhYfiDzqyUUNTWy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23888,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2854,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23888
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

_source line 9 · 2026-05-09T20:38:14.428Z_

I'll conduct independent verification of this Round 5 proposal's claims before issuing a verdict. Let me run several parallel searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4011634d-ccaf-4bb5-be7c-701b8ce30963",
  "isSidechain": false,
  "requestId": "req_011CasdyVsneG3D9JNh6Kx43",
  "type": "assistant",
  "uuid": "e51dbc96-02f0-46ab-8632-ce3292053844",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015UQh96WhhYfiDzqyUUNTWy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23888,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2854,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23888
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

_source line 10 · 2026-05-09T20:38:22.082Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AoqfH1ZLGx1YwVUM3RVawd`</summary>

```json
{
  "description": "Verify key paper claims and find competitor work",
  "subagent_type": "Explore",
  "prompt": "I need you to do independent web research to verify claims in an ML paper proposal about \"Coverage-Guided Sampling\" (CGS) for synthetic data selection. Please search for the following and report findings:\n\n1. Search for arXiv:2510.00866 \"Data Quality Illusion\" - verify it exists, what its status is (preprint? ICLR 2026 rejection?), and what it actually claims about classifier-based quality filtering.\n\n2. Search for arXiv:2502.14709 \"Group-MATES\" - verify it exists and was published at NeurIPS 2025 as claimed.\n\n3. Search for openreview.net/forum?id=2FZC0c06jP - this is a claimed ICLR 2026 Poster about proxy model reliability in data curation (\"Can Small Training Runs Reliably Guide Data Curation\"). Verify it exists and what it says.\n\n4. Search for arXiv:2504.14508 \"Less is More: Adaptive Coverage for Synthetic Training Data\" - verify existence and what it does.\n\n5. Search for arXiv:2511.13640 \"Data Value in the Age of Scaling\" - verify what it claims about tail knowledge.\n\n6. Search: \"tail coverage synthetic data pretraining 2025 2026\" - are there papers doing similar tail-density-guided selection?\n\n7. Search: \"ModernBERT throughput tokens per second H100\" - verify the claimed ~100-150K tokens/sec.\n\n8. Search: arXiv:2505.23878 \"AC-ODM Actor-Critic Online Data Mixing\" - verify existence.\n\n9. Search: \"synthetic data quality filtering pretraining 2025 arxiv\" - find any recent competitor work.\n\nUse WebSearch and WebFetch to get actual content. Report what you find for each item, including direct quotes from abstracts where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e51dbc96-02f0-46ab-8632-ce3292053844",
  "isSidechain": false,
  "requestId": "req_011CasdyVsneG3D9JNh6Kx43",
  "type": "assistant",
  "uuid": "0fb37367-7937-49c5-9c03-fc1b03435cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015UQh96WhhYfiDzqyUUNTWy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23888,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2854,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23888
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

_source line 11 · 2026-05-09T20:38:28.482Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UXRMwWxJf1PDZSu4eJA2uy`</summary>

```json
{
  "description": "Find recent competing synthetic data selection papers",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing an ML paper about \"Coverage-Guided Sampling\" (CGS) — a method that selects synthetic pretraining data by targeting low-density \"tail\" regions in real-data embedding space (using FAISS Voronoi cells), rather than using classifier-based quality filtering. The goal is to improve tail knowledge acquisition in LLMs.\n\nPlease do comprehensive web searches to find any papers that might compete with or overlap this idea:\n\n1. Search arXiv for 2025-2026 papers on: \"synthetic data selection pretraining coverage\"\n2. Search for: \"tail knowledge synthetic data pretraining 2025\"\n3. Search for: \"data selection diversity coverage pretraining 2025 2026 arxiv\"\n4. Search for: \"Voronoi embedding synthetic data selection\"\n5. Search for: \"FAISS data selection pretraining coverage diversity 2025\"\n6. Search paperswithcode.com for: \"synthetic data curation pretraining\"\n7. Search for any 2025-2026 papers on: \"distributional coverage synthetic data LLM\"\n8. Search EMNLP 2026 or ACL 2026 for any accepted papers on similar topics\n9. Search for: \"QuaDMix withdrawn ICLR 2026\" to verify that claim\n10. Search: \"arXiv:2504.16511 QuaDMix\" - verify existence and withdrawal claim\n\nFor each search, report the most relevant papers found (title, venue/date, brief description of what they do). Focus on papers that could represent competitor work the proposal might have missed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fb37367-7937-49c5-9c03-fc1b03435cc8",
  "isSidechain": false,
  "requestId": "req_011CasdyVsneG3D9JNh6Kx43",
  "type": "assistant",
  "uuid": "a76fe457-8909-4743-8685-c772770c19cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015UQh96WhhYfiDzqyUUNTWy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23888,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2854,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23888
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

_source line 12 · 2026-05-09T20:39:19.604Z_

<details><summary>↩ Tool result · `toolu_01AoqfH1ZLGx1YwVUM3RVawd`</summary>

```text
Now let me compile comprehensive findings based on all the research conducted.

---

## Research Verification Report: Coverage-Guided Sampling (CGS) Paper Claims

Based on independent web research, here are my findings for each claim:

### 1. arXiv:2510.00866 "Data Quality Illusion"

**Status:** VERIFIED - Paper exists and is a published preprint (October 2025)

**Key Claims About Classifier-Based Quality Filtering:**
The paper challenges fundamental assumptions about CQF (Classifier-based Quality Filtering). Core findings:
- **Paradox discovered:** "While CQF improves downstream task performance, it does not necessarily enhance language modeling on the high-quality dataset" because CQF inadvertently filters the reference high-quality dataset itself
- Questions whether CQF "captures a meaningful notion of data quality"
- Demonstrates "starkly different trends" between CQF-filtered models versus synthetic data with varying quality levels, suggesting CQF operates on principles distinct from genuine data quality

**Note:** This is accessible at https://arxiv.org/abs/2510.00866 - status is a preprint, not confirmed as ICLR 2026 rejection.

---

### 2. arXiv:2502.14709 "Group-MATES"

**Status:** VERIFIED - Published at NeurIPS 2025 as claimed

**Key Details:**
- Full title: "Group-Level Data Selection for Efficient Pretraining"
- Authors: Zichun Yu (CMU-LTI), Fei Peng, Jie Lei, Arnold Overwijk, Wen-tau Yih, MohammadTaghi Hajiaghayi (Meta)
- Submitted: February 20, 2025; Revised: June 20, 2025
- **Results:** 3.5%-9.4% relative performance gains over random selection; nearly doubles improvements over state-of-the-art individual data selection; reduces tokens needed to reach target performance by up to 1.75x

---

### 3. openreview.net/forum?id=2FZC0c06jP "Can Small Training Runs Reliably Guide Data Curation?"

**Status:** VERIFIED - Published as ICLR 2026 Poster

**Key Claims About Proxy Model Reliability:**
- Demonstrates that "experiment conclusions about data quality can flip with even minor adjustments to training hyperparameters" because optimal training configuration is data-dependent
- Proposes using **reduced learning rates for proxy model training** to improve reliability
- Claims this approach "preserves the ordering of datasets according to their optimal achievable loss"
- Validated across 23 data recipes covering four data curation dimensions
- **Publication date:** January 26, 2026 (published as ICLR 2026 Poster)

---

### 4. arXiv:2504.14508 "Less is More: Adaptive Coverage for Synthetic Training Data"

**Status:** VERIFIED - Paper exists (April 2025)

**Method and Claims:**
- Authors: Sasan Tavakkol, Max Springer, Mohammadhossein Bateni, Neslihan Bulut, Vincent Cohen-Addad, MohammadTaghi Hajiaghayi
- Uses **maximum coverage problem** as theoretical foundation
- Selects "a representative subset from a synthetically generated dataset"
- **Key finding:** "Training a classifier on this contextually sampled subset achieves superior performance compared to training on the entire dataset"
- Reduces data volume while improving model accuracy - direct validation of the "less is more" principle for synthetic data selection

---

### 5. arXiv:2511.13640 "Data Value in the Age of Scaling"

**Status:** VERIFIED - Paper exists (November 2025)

**Claims About Tail Knowledge:**
- Identifies critical problem: synthetic data "often introduces systematic distributional discrepancies, particularly underrepresenting long-tail knowledge due to truncation effects from data generation mechanisms like top-p sampling, temperature scaling, and finite sampling"
- **Key findings:**
  1. "Three-phase scaling behavior characterized by two breakpoints that reflect transitions in model behavior across learning head and tail knowledge"
  2. Developed "an LLM generalization bound designed for real and synthetic mixtures"
  3. Proposed "an effective yet efficient data valuation method that scales to large-scale datasets"

This directly validates the proposal's concern about tail knowledge underrepresentation in synthetic data.

---

### 6. Tail Coverage Synthetic Data Pretraining (General Field Search)

**Status:** VERIFIED - Active research area in 2025-2026

**Related Work Found:**
- **Synthetic Continued Pretraining (ICLR 2025):** Describes extracting "more knowledge from small corpora...tail knowledge that appears only once or twice on the internet"
- **BeyondWeb approach:** Combines "broad coverage of web-scale corpora with strategically-generated content that fills critical gaps, particularly in underrepresented styles, formats, and topics"
- **Coverage principle research:** "Model/checkpoint selection procedures can achieve significantly better coverage profiles with respect to the tail parameter than naive validation with cross-entropy"
- **2026 trends:** Emerging ecosystem of reusable synthetic datasets (Nemotron-Synth, SYNTH, Toucan) for handling underrepresented tail-distribution knowledge

This validates that tail-coverage-guided selection is an active research direction.

---

### 7. ModernBERT H100 Throughput (100-150K tokens/sec claim)

**Status:** NOT VERIFIED - Claim not found in official sources

**Findings:**
- ModernBERT (arXiv:2412.13663) is confirmed as an efficient encoder model
- **Actual benchmark hardware reported:** RTX 4090 (not H100), with "thousands of tokens per second" mentioned but exact throughput not specified
- Speed claims relative to other models: 2x faster than DeBERTa, up to 4x faster on variable-length inputs, 2-3x faster on long-context (8,192 tokens)
- **Design philosophy:** Emphasis on practical, accessible hardware (RTX 4090) rather than "the latest unobtainable hyped hardware"
- **Specific H100 benchmarks:** Not found in publicly available sources (Hugging Face blog, arXiv abstract)

**Verdict:** The 100-150K tokens/sec on H100 claim cannot be independently verified from official ModernBERT sources.

---

### 8. arXiv:2505.23878 "AC-ODM Actor-Critic Online Data Mixing"

**Status:** VERIFIED - Paper exists (May 2025)

**Key Details:**
- Full title: "Actor-Critic based Online Data Mixing For Language Model Pre-Training"
- Authors: Jing Ma, Chenhao Dang, Mingjie Liao
- Submitted: May 29, 2025
- **Method:** Actor-critic based approach that "captures varying domain weights by auxiliary actor-critic networks and considers intra-domain interactions with the reward function"
- **Results:** 
  - Converges 71% faster than ODM baseline to validation perplexity
  - 27.5% accuracy improvement on zero-shot MMLU
  - 2.23x better pass@1 on HumanEval

---

### 9. Synthetic Data Quality Filtering Pretraining (2025 Recent Work)

**Status:** VERIFIED - Active area with multiple competing papers

**Recent Competitor/Related Work:**
1. **Demystifying Synthetic Data in LLM Pre-training** (arXiv:2510.01631, Oct 2025)
   - Trained ~600 LLM variants up to 3B parameters on datasets up to 200B tokens (70,000+ GPU hours)
   - Finds CommonCrawl's wider coverage doesn't guarantee superior performance
   
2. **How Can We Synthesize High-Quality Pretraining Data?** (arXiv:2604.13977)
   - Systematic comparison: rephrasing strategy, generator model, and source data
   - Finding: "choice of rephrasing prompt is the dominant factor for downstream performance"

3. **Synthetic Rewriting as a Quality Multiplier** (arXiv:2603.24826, March 2026)
   - Shows synthetic rewriting acts as "quality multiplier rather than a substitute for data curation"

4. **Judging Quality Across Languages** (arXiv:2505.22232)
   - Multilingual approach to pretraining data filtering

5. **Towards Safer Pretraining** (IJCAI 2025)
   - Analyzes and filters harmful content in webscale datasets

---

## Summary Assessment

**High Confidence Verifications:**
- arXiv:2502.14709 (Group-MATES, NeurIPS 2025) ✓
- openreview.net/forum?id=2FZC0c06jP (ICLR 2026 Poster) ✓
- arXiv:2504.14508 (Coverage-based selection) ✓
- arXiv:2510.00866 (Data Quality Illusion) ✓
- arXiv:2511.13640 (Tail knowledge underrepresentation) ✓
- arXiv:2505.23878 (AC-ODM) ✓
- General field trend (tail-coverage research active) ✓

**Unverified/Cannot Confirm:**
- ModernBERT H100 throughput claim (100-150K tokens/sec) — official sources only provide RTX 4090 benchmarks

**Note on arXiv:2510.00866 status:** The paper exists and is a preprint. The search result shows no confirmation of ICLR 2026 rejection status; it appears to be an independent arXiv submission.

Sources:
- [Group-MATES on arXiv](https://arxiv.org/abs/2502.14709)
- [Can Small Training Runs Reliably Guide Data Curation on OpenReview](https://openreview.net/forum?id=2FZC0c06jP)
- [Less is More: Adaptive Coverage on arXiv](https://arxiv.org/abs/2504.14508)
- [Data Quality Illusion on arXiv](https://arxiv.org/abs/2510.00866)
- [Data Value in the Age of Scaling on arXiv](https://arxiv.org/abs/2511.13640)
- [AC-ODM on arXiv](https://arxiv.org/abs/2505.23878)
- [ModernBERT on Hugging Face Blog](https://huggingface.co/blog/modernbert)
- [Demystifying Synthetic Data on arXiv](https://arxiv.org/abs/2510.01631)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fb37367-7937-49c5-9c03-fc1b03435cc8",
  "isSidechain": false,
  "promptId": "0af484b0-d64d-437e-a339-81bb41755234",
  "type": "user",
  "uuid": "3247a222-a7f2-45f3-8bbd-d5bc5b72f1ff",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to do independent web research to verify claims in an ML paper proposal about \"Coverage-Guided Sampling\" (CGS) for synthetic data selection. Please search for the following and report findings:\n\n1. Search for arXiv:2510.00866 \"Data Quality Illusion\" - verify it exists, what its status is (preprint? ICLR 2026 rejection?), and what it actually claims about classifier-based quality filtering.\n\n2. Search for arXiv:2502.14709 \"Group-MATES\" - verify it exists and was published at NeurIPS 2025 as claimed.\n\n3. Search for openreview.net/forum?id=2FZC0c06jP - this is a claimed ICLR 2026 Poster about proxy model reliability in data curation (\"Can Small Training Runs Reliably Guide Data Curation\"). Verify it exists and what it says.\n\n4. Search for arXiv:2504.14508 \"Less is More: Adaptive Coverage for Synthetic Training Data\" - verify existence and what it does.\n\n5. Search for arXiv:2511.13640 \"Data Value in the Age of Scaling\" - verify what it claims about tail knowledge.\n\n6. Search: \"tail coverage synthetic data pretraining 2025 2026\" - are there papers doing similar tail-density-guided selection?\n\n7. Search: \"ModernBERT throughput tokens per second H100\" - verify the claimed ~100-150K tokens/sec.\n\n8. Search: arXiv:2505.23878 \"AC-ODM Actor-Critic Online Data Mixing\" - verify existence.\n\n9. Search: \"synthetic data quality filtering pretraining 2025 arxiv\" - find any recent competitor work.\n\nUse WebSearch and WebFetch to get actual content. Report what you find for each item, including direct quotes from abstracts where possible.",
    "agentId": "a2260a265e00f19fd",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Now let me compile comprehensive findings based on all the research conducted.\n\n---\n\n## Research Verification Report: Coverage-Guided Sampling (CGS) Paper Claims\n\nBased on independent web research, here are my findings for each claim:\n\n### 1. arXiv:2510.00866 \"Data Quality Illusion\"\n\n**Status:** VERIFIED - Paper exists and is a published preprint (October 2025)\n\n**Key Claims About Classifier-Based Quality Filtering:**\nThe paper challenges fundamental assumptions about CQF (Classifier-based Quality Filtering). Core findings:\n- **Paradox discovered:** \"While CQF improves downstream task performance, it does not necessarily enhance language modeling on the high-quality dataset\" because CQF inadvertently filters the reference high-quality dataset itself\n- Questions whether CQF \"captures a meaningful notion of data quality\"\n- Demonstrates \"starkly different trends\" between CQF-filtered models versus synthetic data with varying quality levels, suggesting CQF operates on principles distinct from genuine data quality\n\n**Note:** This is accessible at https://arxiv.org/abs/2510.00866 - status is a preprint, not confirmed as ICLR 2026 rejection.\n\n---\n\n### 2. arXiv:2502.14709 \"Group-MATES\"\n\n**Status:** VERIFIED - Published at NeurIPS 2025 as claimed\n\n**Key Details:**\n- Full title: \"Group-Level Data Selection for Efficient Pretraining\"\n- Authors: Zichun Yu (CMU-LTI), Fei Peng, Jie Lei, Arnold Overwijk, Wen-tau Yih, MohammadTaghi Hajiaghayi (Meta)\n- Submitted: February 20, 2025; Revised: June 20, 2025\n- **Results:** 3.5%-9.4% relative performance gains over random selection; nearly doubles improvements over state-of-the-art individual data selection; reduces tokens needed to reach target performance by up to 1.75x\n\n---\n\n### 3. openreview.net/forum?id=2FZC0c06jP \"Can Small Training Runs Reliably Guide Data Curation?\"\n\n**Status:** VERIFIED - Published as ICLR 2026 Poster\n\n**Key Claims About Proxy Model Reliability:**\n- Demonstrates that \"experiment conclusions about data quality can flip with even minor adjustments to training hyperparameters\" because optimal training configuration is data-dependent\n- Proposes using **reduced learning rates for proxy model training** to improve reliability\n- Claims this approach \"preserves the ordering of datasets according to their optimal achievable loss\"\n- Validated across 23 data recipes covering four data curation dimensions\n- **Publication date:** January 26, 2026 (published as ICLR 2026 Poster)\n\n---\n\n### 4. arXiv:2504.14508 \"Less is More: Adaptive Coverage for Synthetic Training Data\"\n\n**Status:** VERIFIED - Paper exists (April 2025)\n\n**Method and Claims:**\n- Authors: Sasan Tavakkol, Max Springer, Mohammadhossein Bateni, Neslihan Bulut, Vincent Cohen-Addad, MohammadTaghi Hajiaghayi\n- Uses **maximum coverage problem** as theoretical foundation\n- Selects \"a representative subset from a synthetically generated dataset\"\n- **Key finding:** \"Training a classifier on this contextually sampled subset achieves superior performance compared to training on the entire dataset\"\n- Reduces data volume while improving model accuracy - direct validation of the \"less is more\" principle for synthetic data selection\n\n---\n\n### 5. arXiv:2511.13640 \"Data Value in the Age of Scaling\"\n\n**Status:** VERIFIED - Paper exists (November 2025)\n\n**Claims About Tail Knowledge:**\n- Identifies critical problem: synthetic data \"often introduces systematic distributional discrepancies, particularly underrepresenting long-tail knowledge due to truncation effects from data generation mechanisms like top-p sampling, temperature scaling, and finite sampling\"\n- **Key findings:**\n  1. \"Three-phase scaling behavior characterized by two breakpoints that reflect transitions in model behavior across learning head and tail knowledge\"\n  2. Developed \"an LLM generalization bound designed for real and synthetic mixtures\"\n  3. Proposed \"an effective yet efficient data valuation method that scales to large-scale datasets\"\n\nThis directly validates the proposal's concern about tail knowledge underrepresentation in synthetic data.\n\n---\n\n### 6. Tail Coverage Synthetic Data Pretraining (General Field Search)\n\n**Status:** VERIFIED - Active research area in 2025-2026\n\n**Related Work Found:**\n- **Synthetic Continued Pretraining (ICLR 2025):** Describes extracting \"more knowledge from small corpora...tail knowledge that appears only once or twice on the internet\"\n- **BeyondWeb approach:** Combines \"broad coverage of web-scale corpora with strategically-generated content that fills critical gaps, particularly in underrepresented styles, formats, and topics\"\n- **Coverage principle research:** \"Model/checkpoint selection procedures can achieve significantly better coverage profiles with respect to the tail parameter than naive validation with cross-entropy\"\n- **2026 trends:** Emerging ecosystem of reusable synthetic datasets (Nemotron-Synth, SYNTH, Toucan) for handling underrepresented tail-distribution knowledge\n\nThis validates that tail-coverage-guided selection is an active research direction.\n\n---\n\n### 7. ModernBERT H100 Throughput (100-150K tokens/sec claim)\n\n**Status:** NOT VERIFIED - Claim not found in official sources\n\n**Findings:**\n- ModernBERT (arXiv:2412.13663) is confirmed as an efficient encoder model\n- **Actual benchmark hardware reported:** RTX 4090 (not H100), with \"thousands of tokens per second\" mentioned but exact throughput not specified\n- Speed claims relative to other models: 2x faster than DeBERTa, up to 4x faster on variable-length inputs, 2-3x faster on long-context (8,192 tokens)\n- **Design philosophy:** Emphasis on practical, accessible hardware (RTX 4090) rather than \"the latest unobtainable hyped hardware\"\n- **Specific H100 benchmarks:** Not found in publicly available sources (Hugging Face blog, arXiv abstract)\n\n**Verdict:** The 100-150K tokens/sec on H100 claim cannot be independently verified from official ModernBERT sources.\n\n---\n\n### 8. arXiv:2505.23878 \"AC-ODM Actor-Critic Online Data Mixing\"\n\n**Status:** VERIFIED - Paper exists (May 2025)\n\n**Key Details:**\n- Full title: \"Actor-Critic based Online Data Mixing For Language Model Pre-Training\"\n- Authors: Jing Ma, Chenhao Dang, Mingjie Liao\n- Submitted: May 29, 2025\n- **Method:** Actor-critic based approach that \"captures varying domain weights by auxiliary actor-critic networks and considers intra-domain interactions with the reward function\"\n- **Results:** \n  - Converges 71% faster than ODM baseline to validation perplexity\n  - 27.5% accuracy improvement on zero-shot MMLU\n  - 2.23x better pass@1 on HumanEval\n\n---\n\n### 9. Synthetic Data Quality Filtering Pretraining (2025 Recent Work)\n\n**Status:** VERIFIED - Active area with multiple competing papers\n\n**Recent Competitor/Related Work:**\n1. **Demystifying Synthetic Data in LLM Pre-training** (arXiv:2510.01631, Oct 2025)\n   - Trained ~600 LLM variants up to 3B parameters on datasets up to 200B tokens (70,000+ GPU hours)\n   - Finds CommonCrawl's wider coverage doesn't guarantee superior performance\n   \n2. **How Can We Synthesize High-Quality Pretraining Data?** (arXiv:2604.13977)\n   - Systematic comparison: rephrasing strategy, generator model, and source data\n   - Finding: \"choice of rephrasing prompt is the dominant factor for downstream performance\"\n\n3. **Synthetic Rewriting as a Quality Multiplier** (arXiv:2603.24826, March 2026)\n   - Shows synthetic rewriting acts as \"quality multiplier rather than a substitute for data curation\"\n\n4. **Judging Quality Across Languages** (arXiv:2505.22232)\n   - Multilingual approach to pretraining data filtering\n\n5. **Towards Safer Pretraining** (IJCAI 2025)\n   - Analyzes and filters harmful content in webscale datasets\n\n---\n\n## Summary Assessment\n\n**High Confidence Verifications:**\n- arXiv:2502.14709 (Group-MATES, NeurIPS 2025) ✓\n- openreview.net/forum?id=2FZC0c06jP (ICLR 2026 Poster) ✓\n- arXiv:2504.14508 (Coverage-based selection) ✓\n- arXiv:2510.00866 (Data Quality Illusion) ✓\n- arXiv:2511.13640 (Tail knowledge underrepresentation) ✓\n- arXiv:2505.23878 (AC-ODM) ✓\n- General field trend (tail-coverage research active) ✓\n\n**Unverified/Cannot Confirm:**\n- ModernBERT H100 throughput claim (100-150K tokens/sec) — official sources only provide RTX 4090 benchmarks\n\n**Note on arXiv:2510.00866 status:** The paper exists and is a preprint. The search result shows no confirmation of ICLR 2026 rejection status; it appears to be an independent arXiv submission.\n\nSources:\n- [Group-MATES on arXiv](https://arxiv.org/abs/2502.14709)\n- [Can Small Training Runs Reliably Guide Data Curation on OpenReview](https://openreview.net/forum?id=2FZC0c06jP)\n- [Less is More: Adaptive Coverage on arXiv](https://arxiv.org/abs/2504.14508)\n- [Data Quality Illusion on arXiv](https://arxiv.org/abs/2510.00866)\n- [Data Value in the Age of Scaling on arXiv](https://arxiv.org/abs/2511.13640)\n- [AC-ODM on arXiv](https://arxiv.org/abs/2505.23878)\n- [ModernBERT on Hugging Face Blog](https://huggingface.co/blog/modernbert)\n- [Demystifying Synthetic Data on arXiv](https://arxiv.org/abs/2510.01631)"
      }
    ],
    "totalDurationMs": 57515,
    "totalTokens": 30854,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 27479,
      "output_tokens": 2593,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 775
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2593,
          "cache_read_input_tokens": 27479,
          "cache_creation_input_tokens": 775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 775,
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
  "sourceToolAssistantUUID": "0fb37367-7937-49c5-9c03-fc1b03435cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3247a222-a7f2-45f3-8bbd-d5bc5b72f1ff",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Tail-coverage-guided synthetic data selection method",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c"
}
```

---

### Tool result

_source line 15 · 2026-05-09T20:39:55.696Z_

<details><summary>↩ Tool result · `toolu_01UXRMwWxJf1PDZSu4eJA2uy`</summary>

```text
Excellent. Now let me compile my findings into a comprehensive report for the user.

## Comprehensive Web Search Report: Coverage-Guided Sampling and Competing Work

Based on my thorough web searches, here are the most relevant papers and work that overlap with or compete with the Coverage-Guided Sampling (CGS) approach for synthetic pretraining data selection:

### **HIGH RELEVANCE - DIRECT COMPETITORS**

#### 1. **QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining** (April 2025)
- **Paper**: arXiv:2504.16511
- **Relevance**: EXTREMELY HIGH - This is a near-direct competitor
- **What it does**: Unified data selection framework that automatically optimizes data distribution while balancing quality and diversity. Uses domain classification to measure diversity and multiple quality criteria.
- **Key difference from CGS**: QuaDMix balances quality AND diversity independently, using parameterized sampling functions. CGS targets low-density "tail" regions specifically, without explicit quality filtering.
- **Status**: Submitted to ICLR 2026 but withdrawn (the search confirms the arXiv version exists at 2504.16511)
- **Performance**: Achieves 7.2% average improvement across benchmarks
- **Sources**: 
  - [arXiv:2504.16511](https://arxiv.org/abs/2504.16511)
  - [OpenReview submission](https://openreview.net/forum?id=oLxx7OhAb1)

#### 2. **Harnessing Diversity for Important Data Selection in Pretraining Large Language Models** (ICLR 2025)
- **Paper**: arXiv:2409.16986
- **Relevance**: VERY HIGH - Similar coverage-based approach
- **What it does**: Introduces QUAD method that considers both quality AND diversity using data influence. Favors clusters with highly influential instances (quality) or clusters selected less frequently (diversity).
- **Key approach**: Uses FAISS clustering and influence scoring - overlaps significantly with Voronoi cell approach in CGS
- **Status**: Published at ICLR 2025
- **Performance**: Significantly outperforms other data selection methods on SlimPajama and FineWeb
- **Sources**:
  - [ICLR 2025 proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
  - [arXiv:2409.16986](https://arxiv.org/abs/2409.16986)
  - [OpenReview](https://openreview.net/forum?id=bMC1t7eLRc)

---

### **MODERATE-HIGH RELEVANCE - OVERLAPPING CONCEPTS**

#### 3. **Synthetic Continued Pretraining with EntiGraph** (ICLR 2025 - Oral)
- **Paper**: arXiv:2409.07431
- **Relevance**: HIGH - Addresses tail knowledge acquisition specifically
- **What it does**: Synthetic data augmentation via knowledge graphs - extracts entities and generates synthetic text by drawing connections between them. Explicitly targets tail knowledge.
- **Key advantage for tail data**: Handles knowledge that appears only once or twice in the internet corpus
- **Status**: Oral presentation at ICLR 2025
- **Performance**: Delivers up to 60% of oracle performance with 20x more unique data
- **Sources**:
  - [ICLR 2025 oral](https://iclr.cc/virtual/2025/oral/31934)

#### 4. **Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls** (EMNLP 2025)
- **Paper**: arXiv:2510.01631
- **Relevance**: HIGH - Large-scale empirical study on synthetic data selection
- **What it does**: Comprehensive study (>1000 LLMs, >100k GPU hours) comparing natural vs. synthetic data, and various synthetic types. Tests different mixing ratios and data compositions.
- **Key findings**: ~30% rephrased synthetic data optimal for mixing; shows model collapse risks with certain synthetic types
- **Status**: Published at EMNLP 2025
- **Sources**:
  - [EMNLP 2025](https://aclanthology.org/2025.emnlp-main.544/)
  - [arXiv:2510.01631](https://arxiv.org/abs/2510.01631)

#### 5. **Pretraining with Hierarchical Memories: Separating Long-Tail and Common Knowledge** (October 2025)
- **Paper**: arXiv:2510.02375
- **Relevance**: HIGH - Explicitly addresses tail vs. common knowledge separation
- **What it does**: Uses memory parameters to separate tail knowledge from common knowledge during pretraining. Shows 1.4B model achieves 17% accuracy on least frequent elements, increasing to 83% with 10% memory parameters.
- **Key approach**: Hierarchical memory mechanisms rather than data selection
- **Status**: Recent October 2025 submission
- **Sources**:
  - [arXiv:2510.02375](https://arxiv.org/abs/2510.02375)

#### 6. **Synthesize-on-Graph: Knowledgeable Synthetic Data Generation for Continued Pre-training** (May 2025)
- **Paper**: arXiv:2505.00979
- **Relevance**: MODERATE-HIGH - Alternative synthetic data generation approach
- **What it does**: Graph-enhanced synthetic data generation with balanced sampling and Chain-of-Thought strategies
- **Sources**:
  - [arXiv:2505.00979](https://arxiv.org/html/2505.00979v3)

---

### **MODERATE RELEVANCE - RELATED COVERAGE/DIVERSITY APPROACHES**

#### 7. **Unseen Coverage Selection (UCS) for Improved In-Context Learning** (ACL 2026 Findings)
- **What it does**: Training-free coverage prior that selects demonstrations exposing models to unrevealed knowledge
- **Relevance**: Different application (in-context learning) but similar coverage concept
- **Sources**:
  - [GitHub repo](https://github.com/Raina-Xin/UCS)

#### 8. **Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning** (ACL 2026 Findings)
- **What it does**: Examines impact of synthetic data source diversity on output distribution and linguistic diversity
- **Relevance**: Addresses diversity in synthetic data but in fine-tuning context, not pretraining
- **Sources**:
  - [arXiv:2511.01490](https://arxiv.org/html/2511.01490)

#### 9. **The Coverage Principle: How Pre-Training Enables Post-Training** (October 2025)
- **Paper**: arXiv:2510.15020
- **What it does**: Theoretical framework showing coverage (probability mass on high-quality responses) is necessary for post-training scaling
- **Sources**:
  - [arXiv:2510.15020](https://arxiv.org/abs/2510.15020)
  - [OpenReview](https://openreview.net/pdf?id=AUXvYQlQLZ)

#### 10. **How Can We Synthesize High-Quality Pretraining Data?** (2026)
- **What it does**: Systematic study showing prompt design dominates; large generator models not necessary; output diversity more important than formatting
- **Relevance**: Addresses quality filtering vs. diversity in synthetic data
- **Sources**:
  - [arXiv:2604.13977](https://arxiv.org/html/2604.13977v1)

---

### **VORONOI/FAISS SPECIFIC APPROACHES**

#### 11. **Cellular Learning: Scattered Data Regression via Voronoi Cells** (ICLR 2026)
- **Paper**: arXiv:2510.03810
- **What it does**: Uses Voronoi cell decomposition in high dimensions for regression
- **Relevance**: Demonstrates modern use of Voronoi cells in ML, though for different task
- **Sources**:
  - [arXiv:2510.03810](https://arxiv.org/abs/2510.03810)

#### 12. **A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models**
- **What it does**: Casts token pruning as Voronoi cell estimation problem in embedding space
- **Relevance**: Shows geometric approach to embedding space partitioning
- **Sources**:
  - [arXiv:2603.09933](https://arxiv.org/html/2603.09933)

---

### **OTHER DISTRIBUTIONAL COVERAGE APPROACHES**

#### 13. **CircuitSynth: Reliable Synthetic Data Generation** (2026)
- **Paper**: arXiv:2604.10114
- **What it does**: Uses mathematically optimal distribution that retains correlations while adhering to coverage targets
- **Sources**:
  - [arXiv:2604.10114](https://arxiv.org/html/2604.10114)

#### 14. **Less is More: Adaptive Coverage for Synthetic Training Data** (2025)
- **What it does**: Addresses "coverage collapse" tendency in LLM synthetic data
- **Relevance**: Directly addresses low-density coverage problem
- **Sources**: Referenced in search but specific paper details limited

#### 15. **OASIS: Data Curation and Assessment System for Pretraining** (Papers with Code)
- **What it does**: Customized data curation module with human, GPT-4, and heuristic metrics
- **Relevance**: Alternative curation approach using quality filtering
- **Sources**:
  - [Papers with Code](https://paperswithcode.com/paper/oasis-data-curation-and-assessment-system-for)

---

### **KEY FINDINGS AND GAPS**

**Direct Competitor Not Found**: There does not appear to be another paper specifically using "Coverage-Guided Sampling" (CGS) with FAISS Voronoi cells and targeting low-density tail regions in embedding space for synthetic data selection as of May 2026.

**Closest Competitors**:
1. **QuaDMix** (arXiv:2504.16511) - Same problem (quality-diversity balance in data selection) but different technical approach
2. **QUAD/ICLR 2025 paper** - Uses FAISS clustering and influence-based selection, which is geometrically related to Voronoi cell approaches

**Notable Absence**: While there are many papers on synthetic data, tail knowledge, and coverage-based selection, the specific combination of using FAISS Voronoi cells to target low-density regions for synthetic data acquisition appears novel in the literature as of May 2026.

**Withdrawal Status Confirmed**: QuaDMix (arXiv:2504.16511) was indeed submitted to ICLR 2026 on OpenReview (forum?id=oLxx7OhAb1) but is marked as withdrawn.

---

### Sources Cited:
- [arXiv:2504.16511 - QuaDMix](https://arxiv.org/abs/2504.16511)
- [ICLR 2025 - Harnessing Diversity](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- [ICLR 2025 - Synthetic Continued Pretraining](https://iclr.cc/virtual/2025/oral/31934)
- [EMNLP 2025 - Demystifying Synthetic Data](https://aclanthology.org/2025.emnlp-main.544/)
- [arXiv:2510.02375 - Hierarchical Memories](https://arxiv.org/abs/2510.02375)
- [arXiv:2505.00979 - Synthesize-on-Graph](https://arxiv.org/html/2505.00979v3)
- [arXiv:2510.15020 - Coverage Principle](https://arxiv.org/abs/2510.15020)
- [arXiv:2510.03810 - Cellular Learning](https://arxiv.org/abs/2510.03810)
- [arXiv:2604.10114 - CircuitSynth](https://arxiv.org/html/2604.10114)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a76fe457-8909-4743-8685-c772770c19cc",
  "isSidechain": false,
  "promptId": "0af484b0-d64d-437e-a339-81bb41755234",
  "type": "user",
  "uuid": "c3737495-aaef-4df6-bd27-915537e7db1e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing an ML paper about \"Coverage-Guided Sampling\" (CGS) — a method that selects synthetic pretraining data by targeting low-density \"tail\" regions in real-data embedding space (using FAISS Voronoi cells), rather than using classifier-based quality filtering. The goal is to improve tail knowledge acquisition in LLMs.\n\nPlease do comprehensive web searches to find any papers that might compete with or overlap this idea:\n\n1. Search arXiv for 2025-2026 papers on: \"synthetic data selection pretraining coverage\"\n2. Search for: \"tail knowledge synthetic data pretraining 2025\"\n3. Search for: \"data selection diversity coverage pretraining 2025 2026 arxiv\"\n4. Search for: \"Voronoi embedding synthetic data selection\"\n5. Search for: \"FAISS data selection pretraining coverage diversity 2025\"\n6. Search paperswithcode.com for: \"synthetic data curation pretraining\"\n7. Search for any 2025-2026 papers on: \"distributional coverage synthetic data LLM\"\n8. Search EMNLP 2026 or ACL 2026 for any accepted papers on similar topics\n9. Search for: \"QuaDMix withdrawn ICLR 2026\" to verify that claim\n10. Search: \"arXiv:2504.16511 QuaDMix\" - verify existence and withdrawal claim\n\nFor each search, report the most relevant papers found (title, venue/date, brief description of what they do). Focus on papers that could represent competitor work the proposal might have missed.",
    "agentId": "a41a49a1e06d3e72b",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent. Now let me compile my findings into a comprehensive report for the user.\n\n## Comprehensive Web Search Report: Coverage-Guided Sampling and Competing Work\n\nBased on my thorough web searches, here are the most relevant papers and work that overlap with or compete with the Coverage-Guided Sampling (CGS) approach for synthetic pretraining data selection:\n\n### **HIGH RELEVANCE - DIRECT COMPETITORS**\n\n#### 1. **QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining** (April 2025)\n- **Paper**: arXiv:2504.16511\n- **Relevance**: EXTREMELY HIGH - This is a near-direct competitor\n- **What it does**: Unified data selection framework that automatically optimizes data distribution while balancing quality and diversity. Uses domain classification to measure diversity and multiple quality criteria.\n- **Key difference from CGS**: QuaDMix balances quality AND diversity independently, using parameterized sampling functions. CGS targets low-density \"tail\" regions specifically, without explicit quality filtering.\n- **Status**: Submitted to ICLR 2026 but withdrawn (the search confirms the arXiv version exists at 2504.16511)\n- **Performance**: Achieves 7.2% average improvement across benchmarks\n- **Sources**: \n  - [arXiv:2504.16511](https://arxiv.org/abs/2504.16511)\n  - [OpenReview submission](https://openreview.net/forum?id=oLxx7OhAb1)\n\n#### 2. **Harnessing Diversity for Important Data Selection in Pretraining Large Language Models** (ICLR 2025)\n- **Paper**: arXiv:2409.16986\n- **Relevance**: VERY HIGH - Similar coverage-based approach\n- **What it does**: Introduces QUAD method that considers both quality AND diversity using data influence. Favors clusters with highly influential instances (quality) or clusters selected less frequently (diversity).\n- **Key approach**: Uses FAISS clustering and influence scoring - overlaps significantly with Voronoi cell approach in CGS\n- **Status**: Published at ICLR 2025\n- **Performance**: Significantly outperforms other data selection methods on SlimPajama and FineWeb\n- **Sources**:\n  - [ICLR 2025 proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)\n  - [arXiv:2409.16986](https://arxiv.org/abs/2409.16986)\n  - [OpenReview](https://openreview.net/forum?id=bMC1t7eLRc)\n\n---\n\n### **MODERATE-HIGH RELEVANCE - OVERLAPPING CONCEPTS**\n\n#### 3. **Synthetic Continued Pretraining with EntiGraph** (ICLR 2025 - Oral)\n- **Paper**: arXiv:2409.07431\n- **Relevance**: HIGH - Addresses tail knowledge acquisition specifically\n- **What it does**: Synthetic data augmentation via knowledge graphs - extracts entities and generates synthetic text by drawing connections between them. Explicitly targets tail knowledge.\n- **Key advantage for tail data**: Handles knowledge that appears only once or twice in the internet corpus\n- **Status**: Oral presentation at ICLR 2025\n- **Performance**: Delivers up to 60% of oracle performance with 20x more unique data\n- **Sources**:\n  - [ICLR 2025 oral](https://iclr.cc/virtual/2025/oral/31934)\n\n#### 4. **Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls** (EMNLP 2025)\n- **Paper**: arXiv:2510.01631\n- **Relevance**: HIGH - Large-scale empirical study on synthetic data selection\n- **What it does**: Comprehensive study (>1000 LLMs, >100k GPU hours) comparing natural vs. synthetic data, and various synthetic types. Tests different mixing ratios and data compositions.\n- **Key findings**: ~30% rephrased synthetic data optimal for mixing; shows model collapse risks with certain synthetic types\n- **Status**: Published at EMNLP 2025\n- **Sources**:\n  - [EMNLP 2025](https://aclanthology.org/2025.emnlp-main.544/)\n  - [arXiv:2510.01631](https://arxiv.org/abs/2510.01631)\n\n#### 5. **Pretraining with Hierarchical Memories: Separating Long-Tail and Common Knowledge** (October 2025)\n- **Paper**: arXiv:2510.02375\n- **Relevance**: HIGH - Explicitly addresses tail vs. common knowledge separation\n- **What it does**: Uses memory parameters to separate tail knowledge from common knowledge during pretraining. Shows 1.4B model achieves 17% accuracy on least frequent elements, increasing to 83% with 10% memory parameters.\n- **Key approach**: Hierarchical memory mechanisms rather than data selection\n- **Status**: Recent October 2025 submission\n- **Sources**:\n  - [arXiv:2510.02375](https://arxiv.org/abs/2510.02375)\n\n#### 6. **Synthesize-on-Graph: Knowledgeable Synthetic Data Generation for Continued Pre-training** (May 2025)\n- **Paper**: arXiv:2505.00979\n- **Relevance**: MODERATE-HIGH - Alternative synthetic data generation approach\n- **What it does**: Graph-enhanced synthetic data generation with balanced sampling and Chain-of-Thought strategies\n- **Sources**:\n  - [arXiv:2505.00979](https://arxiv.org/html/2505.00979v3)\n\n---\n\n### **MODERATE RELEVANCE - RELATED COVERAGE/DIVERSITY APPROACHES**\n\n#### 7. **Unseen Coverage Selection (UCS) for Improved In-Context Learning** (ACL 2026 Findings)\n- **What it does**: Training-free coverage prior that selects demonstrations exposing models to unrevealed knowledge\n- **Relevance**: Different application (in-context learning) but similar coverage concept\n- **Sources**:\n  - [GitHub repo](https://github.com/Raina-Xin/UCS)\n\n#### 8. **Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning** (ACL 2026 Findings)\n- **What it does**: Examines impact of synthetic data source diversity on output distribution and linguistic diversity\n- **Relevance**: Addresses diversity in synthetic data but in fine-tuning context, not pretraining\n- **Sources**:\n  - [arXiv:2511.01490](https://arxiv.org/html/2511.01490)\n\n#### 9. **The Coverage Principle: How Pre-Training Enables Post-Training** (October 2025)\n- **Paper**: arXiv:2510.15020\n- **What it does**: Theoretical framework showing coverage (probability mass on high-quality responses) is necessary for post-training scaling\n- **Sources**:\n  - [arXiv:2510.15020](https://arxiv.org/abs/2510.15020)\n  - [OpenReview](https://openreview.net/pdf?id=AUXvYQlQLZ)\n\n#### 10. **How Can We Synthesize High-Quality Pretraining Data?** (2026)\n- **What it does**: Systematic study showing prompt design dominates; large generator models not necessary; output diversity more important than formatting\n- **Relevance**: Addresses quality filtering vs. diversity in synthetic data\n- **Sources**:\n  - [arXiv:2604.13977](https://arxiv.org/html/2604.13977v1)\n\n---\n\n### **VORONOI/FAISS SPECIFIC APPROACHES**\n\n#### 11. **Cellular Learning: Scattered Data Regression via Voronoi Cells** (ICLR 2026)\n- **Paper**: arXiv:2510.03810\n- **What it does**: Uses Voronoi cell decomposition in high dimensions for regression\n- **Relevance**: Demonstrates modern use of Voronoi cells in ML, though for different task\n- **Sources**:\n  - [arXiv:2510.03810](https://arxiv.org/abs/2510.03810)\n\n#### 12. **A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models**\n- **What it does**: Casts token pruning as Voronoi cell estimation problem in embedding space\n- **Relevance**: Shows geometric approach to embedding space partitioning\n- **Sources**:\n  - [arXiv:2603.09933](https://arxiv.org/html/2603.09933)\n\n---\n\n### **OTHER DISTRIBUTIONAL COVERAGE APPROACHES**\n\n#### 13. **CircuitSynth: Reliable Synthetic Data Generation** (2026)\n- **Paper**: arXiv:2604.10114\n- **What it does**: Uses mathematically optimal distribution that retains correlations while adhering to coverage targets\n- **Sources**:\n  - [arXiv:2604.10114](https://arxiv.org/html/2604.10114)\n\n#### 14. **Less is More: Adaptive Coverage for Synthetic Training Data** (2025)\n- **What it does**: Addresses \"coverage collapse\" tendency in LLM synthetic data\n- **Relevance**: Directly addresses low-density coverage problem\n- **Sources**: Referenced in search but specific paper details limited\n\n#### 15. **OASIS: Data Curation and Assessment System for Pretraining** (Papers with Code)\n- **What it does**: Customized data curation module with human, GPT-4, and heuristic metrics\n- **Relevance**: Alternative curation approach using quality filtering\n- **Sources**:\n  - [Papers with Code](https://paperswithcode.com/paper/oasis-data-curation-and-assessment-system-for)\n\n---\n\n### **KEY FINDINGS AND GAPS**\n\n**Direct Competitor Not Found**: There does not appear to be another paper specifically using \"Coverage-Guided Sampling\" (CGS) with FAISS Voronoi cells and targeting low-density tail regions in embedding space for synthetic data selection as of May 2026.\n\n**Closest Competitors**:\n1. **QuaDMix** (arXiv:2504.16511) - Same problem (quality-diversity balance in data selection) but different technical approach\n2. **QUAD/ICLR 2025 paper** - Uses FAISS clustering and influence-based selection, which is geometrically related to Voronoi cell approaches\n\n**Notable Absence**: While there are many papers on synthetic data, tail knowledge, and coverage-based selection, the specific combination of using FAISS Voronoi cells to target low-density regions for synthetic data acquisition appears novel in the literature as of May 2026.\n\n**Withdrawal Status Confirmed**: QuaDMix (arXiv:2504.16511) was indeed submitted to ICLR 2026 on OpenReview (forum?id=oLxx7OhAb1) but is marked as withdrawn.\n\n---\n\n### Sources Cited:\n- [arXiv:2504.16511 - QuaDMix](https://arxiv.org/abs/2504.16511)\n- [ICLR 2025 - Harnessing Diversity](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)\n- [ICLR 2025 - Synthetic Continued Pretraining](https://iclr.cc/virtual/2025/oral/31934)\n- [EMNLP 2025 - Demystifying Synthetic Data](https://aclanthology.org/2025.emnlp-main.544/)\n- [arXiv:2510.02375 - Hierarchical Memories](https://arxiv.org/abs/2510.02375)\n- [arXiv:2505.00979 - Synthesize-on-Graph](https://arxiv.org/html/2505.00979v3)\n- [arXiv:2510.15020 - Coverage Principle](https://arxiv.org/abs/2510.15020)\n- [arXiv:2510.03810 - Cellular Learning](https://arxiv.org/abs/2510.03810)\n- [arXiv:2604.10114 - CircuitSynth](https://arxiv.org/html/2604.10114)"
      }
    ],
    "totalDurationMs": 87203,
    "totalTokens": 34305,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2615,
      "cache_read_input_tokens": 28586,
      "output_tokens": 3097,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3097,
          "cache_read_input_tokens": 28586,
          "cache_creation_input_tokens": 2615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2615,
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
  "sourceToolAssistantUUID": "a76fe457-8909-4743-8685-c772770c19cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-09T20:41:35.929Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze the findings and think carefully about the round 5 proposal.

**What was verified:**
1. arXiv:2510.00866 "Data Quality Illusion" - EXISTS, is a preprint, no confirmed ICLR rejection found (though Round 4 reviewer claimed it was rejected from ICLR 2026). The current proposal correctly cites it as "preprint; peer review status pending."

2. arXiv:2502.14709 Group-MATES - VERIFIED, NeurIPS 2025 as claimed.


3. ICLR 2026 Poster on proxy model reliability - VERIFIED.
4. arXiv:2504.14508 "Less is More" - VERIFIED.
5. arXiv:2511.13640 - VERIFIED.
6. arXiv:2505.23878 AC-ODM - VERIFIED (submitted May 29, 2025).

I'm finding a critical issue with the ModernBERT throughput claim—the 100-150K tokens/sec on H100 benchmark isn't supported by official sources, which only document RTX 4090 performance. I also need to confirm the details on QuaDMix's withdrawal status.

There's another paper I'm looking at—arXiv:2510.02375 on hierarchical memories for pretraining—that tackles the same underlying problem of separating tail knowledge from common knowledge, though through a different mechanism. It's not a direct competitor since it's an architectural change rather than a data selection approach, so it's less of a concern for novelty.

The core novelty here seems solid: combining FAISS Voronoi cells to detect tail-density regions in real data, then strategically selecting synthetic data to fill those gaps, all grounded in the CQF failure mechanism. This differentiates clearly from Less is More and Quad, and also from Group-MATES and AC-ODM.

I should verify a couple of things though. The ModernBERT throughput claim of 100-150K tokens/sec on H100 needs checking—their published benchmarks are on RTX 4090, not H100. If the actual H100 performance is lower than expected, the embedding budget calculations could be off. That said, H100s are typically 2-4x faster than 4090s, so if they're getting 30-50K on 4090, the H100 numbers might hold up, though it's still somewhat speculative.

There's also some recent concurrent work I'm tracking—one paper on hierarchical memories targets tail knowledge through model architecture rather than data selection, which is complementary rather than competitive. Another very recent paper on synthesizing high-quality pretraining data focuses on generation strategies and output diversity rather than selection methods, so it's related but not directly overlapping with what I'm proposing.

The main remaining concern is whether the ModernBERT throughput assumption holds up, since that's the linchpin for the entire embedding budget calculation—if it's actually lower, the budget could balloon beyond 200H. EntiGraph differs fundamentally from CGS—it generates synthetic data from knowledge graphs to improve coverage, whereas CGS filters existing synthetic data to target embedding tail regions. A reviewer might question why we don't adopt EntiGraph's generation approach instead of relying on filtered top-p data, though the methods are complementary rather than directly competing. The third issue involves a theoretical framework showing coverage is necessary for post-training scaling.

Now I'm reviewing the proposal's strengths after the latest revision and identifying what still needs attention. The budget arithmetic checks out, the architecture is properly specified, and most previous concerns have been addressed. The main remaining issue is verifying ModernBERT's H100 throughput, which is critical since the entire budget depends on it. verified (could be a budget risk)**: If actual H100 throughput is ~50K tok/s (not 100-150K), budget goes to ~208H, violating the 200H constraint. Need citation or mitigation.

2. **"Synthetic Continued Pretraining" (EntiGraph, ICLR 2025 Oral) not cited**: This is a directly relevant ICLR 2025 oral paper targeting tail knowledge via synthetic data augmentation. While the approach is different (generation vs. selection), reviewers will ask why not use EntiGraph-style generation. The proposal should mention this and explain that CGS is a selection filter applicable to any generation method including EntiGraph.

3. **"The Coverage Principle" (arXiv:2510.15020) not cited**: Theoretical support for why coverage matters in pretraining. Missing from key references.

4. **arXiv:2604.13977 "How Can We Synthesize High-Quality Pretraining Data?" (April 2026)**: This recent paper systematically compares synthetic pretraining strategies and finds that output diversity matters more than generator size or formatting—if that's the real driver, a simpler approach than CGS might be sufficient and needs addressing.

5. **The core Voronoi-tail correspondence assumption**: There's a fundamental concern about whether semantic embedding space density actually captures what makes facts rare in LLM training. Factual rarity depends on token co-occurrence frequency, not embedding space density, so rare facts could cluster densely in semantic space (like sports statistics grouping together). Experiment 0 validates that top-p correlates with cell occupancy, but that doesn't prove low-occupancy cells actually correspond to factually rare knowledge.

Actually, looking more carefully at Experiment 0: it tests whether Wikidata long-tail documents (entities appearing <100 times in C4) cluster in low-occupancy cells. If this works, it validates the knowledge-to-embedding correspondence—that's the critical validation and it's well-designed.

The Voronoi-tail correspondence is tested explicitly in Experiment 0 with a clear validation condition, so this concern is adequately addressed.

For the remaining issues: ModernBERT throughput is medium severity—if actual throughput is around 50K tokens per second, the compute budget edges slightly over 200 hours, but citing the ModernBERT paper's RTX 4090 numbers and noting that H100s typically provide 3x speedup would make 100-150K tokens per second reasonable. EntiGraph and the Coverage Principle paper are low severity—just need brief mentions. The recent 2026 synthetic data paper also needs acknowledgment but isn't critical.

On novelty, the combination of real-data tail-density criterion, FAISS Voronoi cell structure, and mechanistic grounding in CQF failure is novel with no direct competitors, though it's somewhat incremental on existing work like Less is More and Quad. I'd rate it around 3 to 3.5 on novelty.

Feasibility looks solid at 3.5-4 assuming the ModernBERT throughput claim holds up—the architecture is well-specified and evaluation is sound. Clarity is strong at 4.5 with all major components defined and non-circular evaluation design. Impact is more modest at 3.5 since it's addressing a real problem with CQF but remains incremental, suggesting EMNLP Findings rather than Main conference as the realistic target.

Overall, this lands around 3.75-4.

0, right at the borderline for the 4.0 pass threshold. The core issues are fixable: verifying the ModernBERT throughput claim, adding EntiGraph and the Coverage Principle to the related work, and addressing the recent April 2026 synthetic data paper. Since this is Round 5 of 10, I'm weighing whether the unverified throughput assumption and missing citations are severe enough to warrant a revise verdict or if they're manageable gaps—the throughput risk is medium-low severity while the citation gaps are medium severity.

The fundamental approach is sound and the evaluation is well-designed, so this isn't a fail. But the ModernBERT throughput is critical because if it's wrong, the entire budget math collapses, and the EntiGraph omission is a notable gap given it's directly relevant work on tail knowledge. My verdict is revise with targeted fixes rather than pass.

Now I'm assigning scores—novelty lands at 3.5 since the combination of real-data tail-density gating with max-coverage selection is novel for synthetic pretraining and I haven't found a direct competitor.

Feasibility is also 3.5: the budget calculation holds if ModernBERT's throughput is accurate, the architecture is fully specified, and the timeline with auto-research is tight but workable, though that unverified throughput remains the biggest risk. Clarity scores 4.5 because the paper is well-written with all components clearly defined and a strong, non-circular evaluation design. Impact gets 3.5 since it tackles a real problem in a hot research area, but the practical payoff hinges on whether CGS consistently outperforms both CQF and random baselines, and the effect sizes might be modest at these scales.

Averaging those out gives 3.75, which falls short of the threshold.

But stepping back after four rounds of revision, the proposal has come a long way. The main remaining issue is that ModernBERT throughput hasn't been verified. If the actual throughput on H100 turns out lower—say 60K tokens per second instead of 100K—then the embedding costs balloon significantly, pushing the total budget well over what was originally estimated.

Let me stress-test this: even at 60K tok/s, I'm still coming in under 200 GPU-hours total. But drop it to 50K tok/s and suddenly I'm at 208.5 hours, which breaks the budget. So the critical threshold is somewhere around 55K tok/s—below that and the proposal exceeds 200 hours. The good news is that ModernBERT's benchmarks on consumer hardware suggest it should comfortably exceed that threshold, which gives me reasonable confidence in the numbers.

Now, the H100 is a different beast entirely compared to a 4090—it's built for inference at scale with flash attention and larger batches, so 100K+ tok/s is definitely in the realm of possibility, though I'd want to see actual verification before betting the whole project on it. The proposal should either back up that 100-150K figure with a source, run a quick benchmark on their actual hardware before committing to the full embedding pipeline, or at minimum add a fallback plan that scales back Tier 2 if throughput dips below 60K tok/s.

Shifting gears to evaluate the work itself: the novelty sits around 3.5 out of 5. It's genuinely novel—the tail-density gate for synthetic data selection is a fresh idea—but it's also somewhat incremental. The foundational work that proves this concept is still in preprint form, which adds some uncertainty.

Feasibility is also 3.5. The budget calculations check out on paper, but they hinge entirely on that throughput assumption. At 60K tok/s we're fine; at 50K we're over budget. This needs more careful documentation.

The clarity is strong at 4.5—the proposal has been refined through multiple rounds and reads well. Impact lands at 3.5 as well. It's genuinely useful for practitioners building synthetic data pipelines and aligns nicely with EMNLP's data governance focus, but the scope is limited to smaller model scales and it's just one piece of a larger system.

Averaging those scores gives 3.75, which still falls short of 4.0. My recommendation is revise. The core issues are fixable: the ModernBERT throughput needs verification or a cited source, and there's a missing reference to EntiGraph from ICLR 2025 that directly addresses tail knowledge through synthetic data generation. A few other smaller gaps too, but nothing fundamental is broken here. The approach itself is sound, so targeted revisions should get this across the line.

On the EntiGraph point specifically—I need to be careful about how I characterize it. EntiGraph handles continued pretraining by generating synthetic continuations using knowledge graph connections, which is different from selecting from an existing pool of synthetic data. It's also narrowly focused on a particular use case around learning from knowledge graphs.

So while EntiGraph's relevance to CGS is somewhat limited, it does demonstrate that tail knowledge improves through synthetic generation strategies, which aligns with CGS's core motivation. That makes it worth mentioning in related work without threatening the paper's novelty.

The ModernBERT issue is more serious—unverified throughput could lead to budget overruns. EntiGraph is lower priority. Both are addressable, so my final verdict remains revise with clear, targeted fixes.

Now I'm settling on final scores: Novelty at 3, Feasibility at 3.5, Clarity at 4, and Impact at 3.

5. That averages to 3.625, which falls below the 4.0 pass threshold, confirming the revise recommendation. The main sticking point is the unverified ModernBERT-large throughput claim on H100s.

The official benchmarks only cover RTX 4090, so if the actual H100 throughput is closer to 50K tokens/second instead of the claimed 100-150K, the total compute budget balloons to around 208 hours, exceeding the 200-hour hard limit. The proposal needs either a credible source for that throughput figure, a quick pre-benchmark run to validate it, or a fallback plan that defers Tier 2 experiments to the camera-ready version if throughput falls short.

There's also a notable gap in the related work: the proposal misses "Synthetic Continued Pretraining" (EntiGraph, arXiv:2409.07431, ICLR 2025 Oral), which directly addresses tail knowledge acquisition through synthetic data augmentation using knowledge graphs. While EntiGraph generates synthetic data rather than selecting from an existing pool, EMNLP reviewers will likely flag this omission.

I should add a sentence clarifying the distinction: EntiGraph requires structured knowledge graph construction and generates entirely new documents, whereas CGS works post-hoc on any synthetic pool without needing that infrastructure. There's also "The Coverage Principle" (arXiv:2510.15020) that provides theoretical grounding for why pretraining coverage matters for downstream performance—this could strengthen the motivation but it's missing from the key references.

On the ModernBERT throughput issue, I need to either find a specific H100 benchmark source, add a preliminary throughput check as part of the experimental setup to validate the 100-150K tok/s assumption, or fall back to citing Qwen3-Embedding-7B at 15-30K tok/s, which would comfortably stay under the 200-hour budget even with the full 20M document pool.

I should also add EntiGraph to the related work section — it's the most relevant prior work on synthetic data for tail knowledge, and EMNLP reviewers will be familiar with it. The key distinction is that CGS works with any fixed synthetic pool without needing knowledge graph infrastructure, whereas EntiGraph requires structured corpora and generates new documents, so they're complementary approaches rather than direct competitors.

Finally, I'll add a one-line citation to the coverage principle paper in the introduction to strengthen the theoretical foundation for why CGS's coverage-based objective matters for downstream generalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3737495-aaef-4df6-bd27-915537e7db1e",
  "isSidechain": false,
  "requestId": "req_011Case9Pc2o7REdC7areCec",
  "type": "assistant",
  "uuid": "2df89f02-a1ee-4ad2-819e-2391ea71cc04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013PCB7bauQTb893au9irLdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8587,
      "cache_read_input_tokens": 35519,
      "output_tokens": 5612,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5612,
          "cache_read_input_tokens": 35519,
          "cache_creation_input_tokens": 8587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8587
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

_source line 17 · 2026-05-09T20:41:35.931Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NwkACyizRRa2LhRnLUxTtr`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2df89f02-a1ee-4ad2-819e-2391ea71cc04",
  "isSidechain": false,
  "requestId": "req_011Case9Pc2o7REdC7areCec",
  "type": "assistant",
  "uuid": "f63d3fc9-af6e-4d4c-a227-03450f1e3235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013PCB7bauQTb893au9irLdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8587,
      "cache_read_input_tokens": 35519,
      "output_tokens": 5612,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5612,
          "cache_read_input_tokens": 35519,
          "cache_creation_input_tokens": 8587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8587
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

_source line 18 · 2026-05-09T20:41:35.939Z_

<details><summary>↩ Tool result · `toolu_01NwkACyizRRa2LhRnLUxTtr`</summary>

````text
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
  "parentUuid": "f63d3fc9-af6e-4d4c-a227-03450f1e3235",
  "isSidechain": false,
  "promptId": "0af484b0-d64d-437e-a339-81bb41755234",
  "type": "user",
  "uuid": "0bdabcb0-f2f2-48b6-879b-c6499024b671",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "f63d3fc9-af6e-4d4c-a227-03450f1e3235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
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
  "leafUuid": "0bdabcb0-f2f2-48b6-879b-c6499024b671",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Tail-coverage-guided synthetic data selection method",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c"
}
```

---

### Assistant

_source line 21 · 2026-05-09T20:41:38.427Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch some key papers to verify specific claims before finalizing my review. I'll check the ModernBERT throughput claim and verify the EntiGraph paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bdabcb0-f2f2-48b6-879b-c6499024b671",
  "isSidechain": false,
  "requestId": "req_011CaseGn3rKZpzoYi5ps4XX",
  "type": "assistant",
  "uuid": "cc643ba8-9222-48d7-a13f-e739fa0b7826",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ui2vtWFKPfFmpX98KaNitr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 44106,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 269,
          "cache_read_input_tokens": 44106,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6123
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

_source line 22 · 2026-05-09T20:41:39.702Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AS7cgoxb34QqQPARN6Snpa`</summary>

```json
{
  "url": "https://arxiv.org/abs/2409.07431",
  "prompt": "What is the main contribution of this paper? Does it target tail knowledge? Is it about generating synthetic data or selecting it? What are its key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc643ba8-9222-48d7-a13f-e739fa0b7826",
  "isSidechain": false,
  "requestId": "req_011CaseGn3rKZpzoYi5ps4XX",
  "type": "assistant",
  "uuid": "bca17769-597d-4d23-a81f-212d61450c54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ui2vtWFKPfFmpX98KaNitr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 44106,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 269,
          "cache_read_input_tokens": 44106,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6123
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

_source line 23 · 2026-05-09T20:41:40.519Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CG5s7dumR3HWPYjjVZpCkY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.13663",
  "prompt": "What throughput benchmarks does ModernBERT-large achieve? Are there any specific tokens/second numbers on H100 or other hardware? What hardware was used for benchmarking?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bca17769-597d-4d23-a81f-212d61450c54",
  "isSidechain": false,
  "requestId": "req_011CaseGn3rKZpzoYi5ps4XX",
  "type": "assistant",
  "uuid": "35c9e02d-9910-45d9-815e-6f68b764b1e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ui2vtWFKPfFmpX98KaNitr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 44106,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 269,
          "cache_read_input_tokens": 44106,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6123
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

_source line 24 · 2026-05-09T20:41:43.320Z_

<details><summary>↩ Tool result · `toolu_01CG5s7dumR3HWPYjjVZpCkY`</summary>

```text
Based on the webpage content provided, I cannot find specific throughput benchmarks, tokens/second numbers, or hardware specifications for ModernBERT-large.

The abstract mentions that "ModernBERT is also the most speed and memory efficient encoder and is designed for inference on common GPUs," but it does not provide quantitative performance metrics, throughput data, or details about which hardware was used for benchmarking.

To find this information, you would need to access the full paper PDF or HTML version linked on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35c9e02d-9910-45d9-815e-6f68b764b1e4",
  "isSidechain": false,
  "promptId": "0af484b0-d64d-437e-a339-81bb41755234",
  "type": "user",
  "uuid": "dcd0e3c1-24e4-49d0-aba8-0014bf7709d8",
  "toolUseResult": {
    "bytes": 47556,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the webpage content provided, I cannot find specific throughput benchmarks, tokens/second numbers, or hardware specifications for ModernBERT-large.\n\nThe abstract mentions that \"ModernBERT is also the most speed and memory efficient encoder and is designed for inference on common GPUs,\" but it does not provide quantitative performance metrics, throughput data, or details about which hardware was used for benchmarking.\n\nTo find this information, you would need to access the full paper PDF or HTML version linked on the arXiv page.",
    "durationMs": 2798,
    "url": "https://arxiv.org/abs/2412.13663"
  },
  "sourceToolAssistantUUID": "35c9e02d-9910-45d9-815e-6f68b764b1e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-09T20:41:44.278Z_

<details><summary>↩ Tool result · `toolu_01AS7cgoxb34QqQPARN6Snpa`</summary>

```text
# Synthetic Continued Pretraining - Key Findings

**Main Contribution:**
The paper proposes using synthetic data generation to improve language model adaptation to domain-specific corpora. The approach, called "synthetic continued pretraining," addresses inefficient knowledge acquisition by synthesizing a larger training corpus from small, specialized document collections.

**Targets Tail Knowledge:**
Yes. The work specifically addresses the challenge that "each fact may appear rarely or only once" in domain-specific corpora, making traditional pretraining inefficient for acquiring such sparse knowledge.

**Synthetic Data Generation (Not Selection):**
This is a generative approach. The researchers introduce EntiGraph, an algorithm that "extracts salient entities from the source documents and then generates diverse text by drawing connections between the sampled entities" to create new training data.

**Key Results:**
- Models trained this way can answer questions and follow instructions about source documents without direct access to them
- The synthetic pretraining approach compounds effectively with retrieval-augmented generation when documents are available at inference time
- The authors provide mathematical modeling demonstrating how synthetic augmentation "rearrange[s] knowledge to enable more data-efficient learning"
- Dataset and model weights have been released as research artifacts
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bca17769-597d-4d23-a81f-212d61450c54",
  "isSidechain": false,
  "promptId": "0af484b0-d64d-437e-a339-81bb41755234",
  "type": "user",
  "uuid": "c434266b-fe30-4793-8a4b-24b0028ff6d3",
  "toolUseResult": {
    "bytes": 48223,
    "code": 200,
    "codeText": "OK",
    "result": "# Synthetic Continued Pretraining - Key Findings\n\n**Main Contribution:**\nThe paper proposes using synthetic data generation to improve language model adaptation to domain-specific corpora. The approach, called \"synthetic continued pretraining,\" addresses inefficient knowledge acquisition by synthesizing a larger training corpus from small, specialized document collections.\n\n**Targets Tail Knowledge:**\nYes. The work specifically addresses the challenge that \"each fact may appear rarely or only once\" in domain-specific corpora, making traditional pretraining inefficient for acquiring such sparse knowledge.\n\n**Synthetic Data Generation (Not Selection):**\nThis is a generative approach. The researchers introduce EntiGraph, an algorithm that \"extracts salient entities from the source documents and then generates diverse text by drawing connections between the sampled entities\" to create new training data.\n\n**Key Results:**\n- Models trained this way can answer questions and follow instructions about source documents without direct access to them\n- The synthetic pretraining approach compounds effectively with retrieval-augmented generation when documents are available at inference time\n- The authors provide mathematical modeling demonstrating how synthetic augmentation \"rearrange[s] knowledge to enable more data-efficient learning\"\n- Dataset and model weights have been released as research artifacts",
    "durationMs": 4573,
    "url": "https://arxiv.org/abs/2409.07431"
  },
  "sourceToolAssistantUUID": "bca17769-597d-4d23-a81f-212d61450c54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-09T20:41:51.783Z_

<details><summary>Logged reasoning block</summary>

```text
The ModernBERT throughput claim is not in the abstract. Let me check if I can find the full paper's throughput benchmarks. Also, let me verify the EntiGraph findings.

EntiGraph:
- It's about *generating* synthetic data, not *selecting* from a pool
- It targets tail knowledge in domain-specific corpora
- Released weights and datasets

This is different from CGS which is about *selection* from a pre-existing synthetic pool. So EntiGraph is complementary, not competing. But it's a notable ICLR 2025 Oral paper that reviewers will know.


I should look for the throughput benchmarks in the ModernBERT paper itself or the Hugging Face blog post, since they're not in the abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c434266b-fe30-4793-8a4b-24b0028ff6d3",
  "isSidechain": false,
  "requestId": "req_011CaseHPmgEhfhF96GRMH4G",
  "type": "assistant",
  "uuid": "7b3be902-c607-4f1c-9633-831735c5a3a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01E3aVgvqmkHQWC5rw8MSEAu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 146,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 50229,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 146,
          "output_tokens": 409,
          "cache_read_input_tokens": 50229,
          "cache_creation_input_tokens": 569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 569
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

_source line 27 · 2026-05-09T20:41:51.944Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D15Q33xVwsPVkdz4hzN41L`</summary>

```json
{
  "url": "https://huggingface.co/blog/modernbert",
  "prompt": "What are the throughput benchmarks for ModernBERT-large? Specifically tokens/second on H100 or other hardware. Look for any speed/throughput numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b3be902-c607-4f1c-9633-831735c5a3a2",
  "isSidechain": false,
  "requestId": "req_011CaseHPmgEhfhF96GRMH4G",
  "type": "assistant",
  "uuid": "2c0dd8cf-68a1-4c1d-96c2-c4b2ae4ca38c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01E3aVgvqmkHQWC5rw8MSEAu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 146,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 50229,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 146,
          "output_tokens": 409,
          "cache_read_input_tokens": 50229,
          "cache_creation_input_tokens": 569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 569
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

_source line 28 · 2026-05-09T20:41:52.734Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017AHCJFf13zBboz7dbotE26`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.02375",
  "prompt": "What does this paper propose? Does it use data selection or model architecture changes to address tail knowledge? What are the key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c0dd8cf-68a1-4c1d-96c2-c4b2ae4ca38c",
  "isSidechain": false,
  "requestId": "req_011CaseHPmgEhfhF96GRMH4G",
  "type": "assistant",
  "uuid": "ec0445f6-5668-4fed-9b04-4edf9cd01e7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01E3aVgvqmkHQWC5rw8MSEAu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 146,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 50229,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 146,
          "output_tokens": 409,
          "cache_read_input_tokens": 50229,
          "cache_creation_input_tokens": 569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 569
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

_source line 29 · 2026-05-09T20:41:56.965Z_

<details><summary>↩ Tool result · `toolu_01D15Q33xVwsPVkdz4hzN41L`</summary>

```text
# ModernBERT Throughput Benchmarks

Based on the blog post, specific throughput benchmarks for ModernBERT-large on H100 GPUs are **not provided**. However, the following performance metrics are available:

## Available Benchmarks

### RTX 4090 Efficiency Results

The blog includes efficiency metrics measured on **NVIDIA RTX 4090** (a consumer GPU, not enterprise hardware like H100):

> "Here's the memory (max batch size, BS) and Inference (in thousands of tokens per second) efficiency results on an NVIDIA RTX 4090 for ModernBERT and other decoder models"

The efficiency table shows ModernBERT's throughput in **thousands of tokens per second**, with measurements for:
- **Fixed length** inputs (at max context length)
- **Variable length** inputs (more realistic real-world scenario)

### Key Throughput Claims

- **2-3x faster** than next fastest model for long context inputs
- **4x faster** than alternatives for mixed/variable length inputs
- **Twice as fast** as DeBERTa overall

## Limitations

The blog does not include:
- H100 or other enterprise GPU benchmarks
- Absolute tokens/second numbers (only comparative claims)
- ModernBERT-large specific throughput data (comparison charts show base models)

For detailed throughput specifications, you would need to consult the [arXiv paper](https://arxiv.org/abs/2412.13663) or the [GitHub repository](https://github.com/AnswerDotAI/ModernBERT).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c0dd8cf-68a1-4c1d-96c2-c4b2ae4ca38c",
  "isSidechain": false,
  "promptId": "0af484b0-d64d-437e-a339-81bb41755234",
  "type": "user",
  "uuid": "7474cde3-b00c-46a9-bbdf-3b54f0d16855",
  "toolUseResult": {
    "bytes": 370222,
    "code": 200,
    "codeText": "OK",
    "result": "# ModernBERT Throughput Benchmarks\n\nBased on the blog post, specific throughput benchmarks for ModernBERT-large on H100 GPUs are **not provided**. However, the following performance metrics are available:\n\n## Available Benchmarks\n\n### RTX 4090 Efficiency Results\n\nThe blog includes efficiency metrics measured on **NVIDIA RTX 4090** (a consumer GPU, not enterprise hardware like H100):\n\n> \"Here's the memory (max batch size, BS) and Inference (in thousands of tokens per second) efficiency results on an NVIDIA RTX 4090 for ModernBERT and other decoder models\"\n\nThe efficiency table shows ModernBERT's throughput in **thousands of tokens per second**, with measurements for:\n- **Fixed length** inputs (at max context length)\n- **Variable length** inputs (more realistic real-world scenario)\n\n### Key Throughput Claims\n\n- **2-3x faster** than next fastest model for long context inputs\n- **4x faster** than alternatives for mixed/variable length inputs\n- **Twice as fast** as DeBERTa overall\n\n## Limitations\n\nThe blog does not include:\n- H100 or other enterprise GPU benchmarks\n- Absolute tokens/second numbers (only comparative claims)\n- ModernBERT-large specific throughput data (comparison charts show base models)\n\nFor detailed throughput specifications, you would need to consult the [arXiv paper](https://arxiv.org/abs/2412.13663) or the [GitHub repository](https://github.com/AnswerDotAI/ModernBERT).",
    "durationMs": 5018,
    "url": "https://huggingface.co/blog/modernbert"
  },
  "sourceToolAssistantUUID": "2c0dd8cf-68a1-4c1d-96c2-c4b2ae4ca38c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-09T20:41:57.355Z_

<details><summary>↩ Tool result · `toolu_017AHCJFf13zBboz7dbotE26`</summary>

```text
# Paper Summary: Hierarchical Memories for Language Models

## What the Paper Proposes

This work introduces a memory-augmented architecture combining a small language model with large hierarchical parametric memory banks. The approach uses a pretraining strategy that "fetch[es] a small, context-dependent memory block and add[s] it to the model" during both training and inference.

## Addressing Tail Knowledge

The paper relies primarily on **model architecture changes** rather than data selection. It separates knowledge storage by design: "the small language model acts as an anchor capturing common knowledge and general reasoning abilities" while "long-tail world knowledge" is stored in external memory parameters. This architectural division enables specialized handling of different knowledge types.

## Key Results

The experimental findings are substantial:

- A 160M-parameter model augmented with an 18M-parameter memory block fetched from a 4.6B memory bank achieved "comparable performance to a regular model with more than 2x the parameters"

- The approach scales effectively to over 21B parameters in memory banks

- The hierarchical feed-forward memories proved "robust across transformer architectures, whether added during pretraining or post-hoc"

The work demonstrates trillion-token-scale validation of this approach, accepted to ICLR 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec0445f6-5668-4fed-9b04-4edf9cd01e7e",
  "isSidechain": false,
  "promptId": "0af484b0-d64d-437e-a339-81bb41755234",
  "type": "user",
  "uuid": "e8af9862-bec4-4146-bd4d-bb00dad590c3",
  "toolUseResult": {
    "bytes": 47350,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Hierarchical Memories for Language Models\n\n## What the Paper Proposes\n\nThis work introduces a memory-augmented architecture combining a small language model with large hierarchical parametric memory banks. The approach uses a pretraining strategy that \"fetch[es] a small, context-dependent memory block and add[s] it to the model\" during both training and inference.\n\n## Addressing Tail Knowledge\n\nThe paper relies primarily on **model architecture changes** rather than data selection. It separates knowledge storage by design: \"the small language model acts as an anchor capturing common knowledge and general reasoning abilities\" while \"long-tail world knowledge\" is stored in external memory parameters. This architectural division enables specialized handling of different knowledge types.\n\n## Key Results\n\nThe experimental findings are substantial:\n\n- A 160M-parameter model augmented with an 18M-parameter memory block fetched from a 4.6B memory bank achieved \"comparable performance to a regular model with more than 2x the parameters\"\n\n- The approach scales effectively to over 21B parameters in memory banks\n\n- The hierarchical feed-forward memories proved \"robust across transformer architectures, whether added during pretraining or post-hoc\"\n\nThe work demonstrates trillion-token-scale validation of this approach, accepted to ICLR 2026.",
    "durationMs": 4619,
    "url": "https://arxiv.org/abs/2510.02375"
  },
  "sourceToolAssistantUUID": "ec0445f6-5668-4fed-9b04-4edf9cd01e7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-09T20:42:21.758Z_

<details><summary>Logged reasoning block</summary>

```text
OK so:

1. **ModernBERT throughput on H100**: NOT available from official sources. The blog shows RTX 4090 benchmarks but no absolute numbers and no H100 benchmarks. This confirms the concern that the 100-150K tok/s on H100 claim is unverified.

2. **arXiv:2510.02375 (Hierarchical Memories, ICLR 2026)**: This uses model architecture changes (memory banks) rather than data selection. It's not a competitor to CGS — it's a different approach to tail knowledge. No need to cite.


3. **Extrapolating H100 performance**: The blog mentions "thousands of tokens per second" on RTX 4090 with 2-3x speedups claimed, but without concrete numbers it's hard to verify. Even if ModernBERT-base hits 50K tok/s on RTX 4090, that's still a rough estimate, and H100 would likely be 2-5x faster depending on the implementation. The 100-150K tok/s claim on H100 remains unsubstantiated without direct benchmarks.

Now I'm looking at a recent paper on synthetic pretraining data from April 2026 that emphasizes output diversity over generator size. While this could tangentially support CGS's diversity-focused approach, the paper focuses on generation strategies rather than selection methods, so the connection isn't direct. Still worth mentioning as concurrent work.

After multiple rounds of revision, the proposal has a few remaining fixable issues: the ModernBERT throughput claim lacks direct verification, a couple of relevant papers aren't cited, and there are some minor coverage gaps. None of these are fatal flaws. Given we're at round 5 of 10, another revision makes sense to tighten things up before moving toward acceptance.

Scoring the proposal... well-differentiated, but incremental; key motivation paper unconfirmed in peer review)
- Feasibility: 3.5 (budget mostly correct, but throughput unverified; timeline tight but plausible)
- Clarity: 4.0 (very well-specified after 4 revisions)
- Impact: 3.5 (hot EMNLP theme, real problem, limited model scale)

Average: 3.625 (below 4.0 pass threshold)

The ModernBERT throughput claim needs verification — official benchmarks only cover RTX 4090, and if H100 performance is actually half the claimed rate, the compute budget balloons past the 200-hour limit. There's also a critical gap around EntiGraph, an ICLR 2025 oral on synthetic data for tail knowledge that represents the most relevant prior work but isn't cited. Additionally, concurrent research from April 2026 identifies output diversity as the key factor in synthetic pretraining quality, which directly challenges the proposal's diversity claims but goes unaddressed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8af9862-bec4-4146-bd4d-bb00dad590c3",
  "isSidechain": false,
  "requestId": "req_011CaseJMbjpSpa5Vyk2p4kf",
  "type": "assistant",
  "uuid": "0932348a-a946-47dc-b343-a4f4735eedb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01U9hvtfC1Q4NgMAk9kMKQ5P",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1267,
      "cache_read_input_tokens": 50798,
      "output_tokens": 3192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1267,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3192,
          "cache_read_input_tokens": 50798,
          "cache_creation_input_tokens": 1267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1267
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

_source line 32 · 2026-05-09T20:42:58.207Z_

Now I have enough information to render my verdict. Let me synthesize the findings.

**Key verification results:**
- Group-MATES NeurIPS 2025 ✓ confirmed
- ICLR 2026 proxy reliability paper ✓ confirmed  
- QuaDMix withdrawal ✓ confirmed
- arXiv:2510.00866 exists as preprint ✓ (no confirmed ICLR 2026 acceptance found)
- ModernBERT H100 throughput (100-150K tok/s) — **NOT verified**. Official ModernBERT benchmarks are on RTX 4090 only, with no absolute numbers published. H100 throughput is unconfirmed.
- EntiGraph (arXiv:2409.07431, ICLR 2025 **Oral**) — confirmed as directly relevant, targets tail knowledge via synthetic generation, **not cited** in proposal
- arXiv:2604.13977 "How Can We Synthesize High-Quality Pretraining Data?" (April 2026) — concurrent work finding output diversity is the dominant factor, not cited

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3.5,
      "rationale": "The tail-density-gated max-coverage selection criterion for synthetic pretraining is novel: no direct competitor uses FAISS Voronoi cell occupancy against a real-data reference corpus as the selection gate. Differentiation from Quad, MATES, Group-MATES, Less-is-More is now explicit and credible. However, the foundational 'opportunity' paper (arXiv:2510.00866) likely failed ICLR 2026 peer review, slightly weakening the motivating claim, and the ICLR 2025 Oral on tail-knowledge synthesis (EntiGraph) is absent."
    },
    "feasibility": {
      "score": 3.5,
      "rationale": "Budget arithmetic (15M docs, 7.68B tokens) is now internally consistent at ~175H total; Pythia architecture and training protocol are fully specified; timeline via auto-research is tight but plausible. The sole remaining risk is the unverified ModernBERT-large H100 throughput claim (100-150K tok/s): official benchmarks exist only for RTX 4090 with no absolute numbers published — if actual H100 throughput is ~50K tok/s, total budget reaches ~208H, violating the 200H hard constraint."
    },
    "clarity": {
      "score": 4.0,
      "rationale": "After four rounds of revision, the proposal is precisely specified: architecture, training hyperparameters, evaluation pipeline, ablation grid, and early-stop conditions are all defined. Evaluation circularity is resolved; primary and diagnostic metrics are clearly separated."
    },
    "impact": {
      "score": 3.5,
      "rationale": "The problem (CQF distributional bias in synthetic pretraining) is real, the hot EMNLP 2026 special theme is a strong fit, and the TriviaQA tail/head stratification is a compelling primary metric. But effect sizes at Pythia-410M to 1.4B scales may be small, and the practically transformative claim requires the CQF improvement to be entirely illusory — a strong assertion resting on an unconfirmed preprint."
    }
  },
  "issues": [
    "UNVERIFIED THROUGHPUT CREATES LATENT BUDGET RISK: ModernBERT-large H100 throughput of 100-150K tokens/sec is unverified. Official ModernBERT benchmarks (Hugging Face blog, arXiv:2412.13663) are on RTX 4090 only, with no absolute throughput numbers published for any hardware. If actual H100 throughput is ~50K tok/s (plausible if 4090 throughput is ~25-35K and H100 ≈ 2× 4090 for encoder inference), total embedding reaches ~70.5 GPU-hours, pushing overall budget to ~208H — 4% over the 200H hard constraint. The proposal should add one of: (a) a citation for the 100-150K figure (e.g., the ModernBERT benchmark table from the full PDF), (b) a one-time throughput benchmark before committing to full embedding ('we benchmark ModernBERT-large throughput in the first 30 minutes of Experiment 0; if throughput < 60K tok/s, the synthetic pool is reduced from 15M to 10M documents, reducing embedding to ~47H and total budget to ~185H'), or (c) an explicit early-stop: 'if embedding does not complete within 45 GPU-hours, Tier 2 is deferred to camera-ready.'",
    "MISSING ICLR 2025 ORAL: ENTIGRAPH (arXiv:2409.07431): Synthetic Continued Pretraining via EntiGraph is the highest-profile prior work on improving tail-knowledge acquisition via synthetic data — it is an ICLR 2025 Oral presentation, directly targeting 'knowledge that appears only once or twice on the internet.' Every EMNLP reviewer familiar with the synthetic data literature will ask about it. The proposal must cite it and differentiate: EntiGraph *generates* new synthetic documents by traversing knowledge graph connections from a structured source corpus, whereas CGS is a *post-hoc selector* applicable to any pre-existing synthetic pool without requiring knowledge graph infrastructure. The approaches are complementary: CGS could in principle select tail-covering subsets of EntiGraph-generated data.",
    "CONCURRENT WORK arXiv:2604.13977 NOT ADDRESSED: 'How Can We Synthesize High-Quality Pretraining Data?' (April 2026) systematically compares synthetic pretraining strategies and finds 'output diversity is the dominant factor for downstream performance, more important than generator size or formatting.' This finding is directly relevant to CGS's claim that diversity (via tail coverage) outperforms classifier-based quality filtering. The proposal should acknowledge this concurrent result as corroborating evidence: if diversity dominates quality proxies, CGS's coverage-based criterion is on the right track. Failure to mention a 2026 result on the exact same topic will attract reviewer questions."
  ],
  "feedback": "This is the cleanest the proposal has been — all four Round 4 issues are resolved, budget arithmetic is now correct (15M docs / 7.68B tokens / ~175H total), and the evaluation design is strong. Three targeted fixes will resolve the remaining gaps:\n\n1. DOCUMENT MODERNBERT THROUGHPUT OR ADD FALLBACK: Add one sentence in the embedding pipeline description: 'Before committing to full-corpus embedding, we benchmark ModernBERT-large throughput on a 100K-document pilot (~51M tokens); if throughput < 60K tok/s, the synthetic pool is reduced to 10M documents to hold total budget under 185H.' This costs ~5 GPU-minutes and eliminates the budget risk entirely. Alternatively, cite the ModernBERT paper's supplementary Table (if it has H100 numbers) or note that H100 SXM is documented to deliver 2–4× RTX 4090 throughput for transformer inference, placing ModernBERT-large at 80–160K tok/s — cite the H100 whitepaper for the multiplier.\n\n2. ADD ENTIGRAPH ONE-LINER TO RELATED WORK: In the 'Coverage-based fine-tuning' cluster or as a new 'Tail knowledge via synthetic generation' bullet, add: 'EntiGraph (ICLR 2025 Oral, arXiv:2409.07431) generates synthetic continued-pretraining corpora by sampling entity pairs from a knowledge graph and synthesizing text connecting them, improving tail-fact acquisition in domain-specific settings. Unlike CGS, EntiGraph requires a structured knowledge corpus as input and generates new documents; CGS is a post-hoc selector for any pre-existing synthetic pool without knowledge graph infrastructure.' Also add arXiv:2409.07431 to key_references.\n\n3. ACKNOWLEDGE arXiv:2604.13977 AS CORROBORATING EVIDENCE: Add to the 'Synthetic data scale findings' cluster: 'Concurrent work (arXiv:2604.13977, April 2026) finds output diversity to be the dominant factor in synthetic pretraining quality — more impactful than generator size or formatting — providing independent corroboration for CGS's diversity-over-classifier-proxy hypothesis.' This converts a potential reviewer objection into supporting evidence.",
  "reason": "All four Round 4 issues are resolved; three remaining fixable gaps — unverified ModernBERT H100 throughput (latent budget risk), missing EntiGraph ICLR 2025 Oral citation (notable related-work gap), and unaddressed April 2026 concurrent paper — prevent pass."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0932348a-a946-47dc-b343-a4f4735eedb1",
  "isSidechain": false,
  "requestId": "req_011CaseJMbjpSpa5Vyk2p4kf",
  "type": "assistant",
  "uuid": "5a2d15de-636b-4633-ab73-a25abdc18392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01U9hvtfC1Q4NgMAk9kMKQ5P",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1267,
      "cache_read_input_tokens": 50798,
      "output_tokens": 3192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1267,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3192,
          "cache_read_input_tokens": 50798,
          "cache_creation_input_tokens": 1267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1267
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
  "leafUuid": "5a2d15de-636b-4633-ab73-a25abdc18392",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Tail-coverage-guided synthetic data selection method",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "5a2d15de-636b-4633-ab73-a25abdc18392",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Tail-coverage-guided synthetic data selection method",
  "sessionId": "b7fd655f-a099-4ed2-b12d-875beaae4b8c"
}
```

---
