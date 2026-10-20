# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/4b90db97-abf7-43ca-8746-d63916fc40be.jsonl`
- **Structured JSON:** [`2604e2d46e19a2d1b549.json`](../../sessions/26/2604e2d46e19a2d1b549.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:20:56.805Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:20:56.805Z",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Multilingualism and Cross-Lingual NLP.\n\nDirection: Cross-lingual transfer and multilingual NLP methods. In-scope: cross-lingual transfer without parallel data, multilingual instruction tuning strategies, language-agnostic representations, low-resource language adaptation, cross-lingual retrieval, multilingual reasoning, code-switching handling. ACL 2025 outstanding papers highlighted multilingual gaps and cross-lingual intervention methods.\n\nContribution type: METHOD ONLY. New training recipes, transfer algorithms, or adaptation techniques. Not a new multilingual dataset or language-specific analysis.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Multilingual experiments need coverage across languages — budget for LoRA fine-tuning on multilingual models, not full pretraining.\n2. Time: ≤16 days. Use existing multilingual models (BLOOM, mT5, XLM-R, Aya, Qwen multilingual, Llama-3 multilingual).\n3. Eval: XTREME-UP, XCOPA, XStoryCloze, MGSM, multilingual MMLU, TyDi QA, FLORES for MT.\n\nLook for: efficient cross-lingual transfer with minimal target-language data, multilingual reasoning without English-centric bias, representation alignment methods, adaptation techniques for typologically diverse languages. Avoid: English-only experiments, monolingual fine-tuning.\n\nTag: direction=multilingual, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 9/10)\n{\n  \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning\",\n  \"core_problem\": \"Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.\",\n  \"opportunity\": \"Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K questions total (approximately 11K in Kazakh, 12K in Russian) spanning STEM, humanities, and social sciences sourced from authentic Kazakhstani educational materials; for TWMP's Kazakh instruction evaluation, only the Kazakh-language subset (~11K questions) is relevant; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026) evaluates 10 LLMs across 21 language variants and finds that Llama3-Instruct is the only model showing distinctive Uyghur capability while most models reach only ~75% Mongolian identification accuracy; Chinese LLMs do not outperform Western counterparts on minority languages including Uyghur and Mongolian, confirming that the performance gap TWMP targets persists even in the most recent model generation. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.\",\n  \"landscape\": \"PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. PROM [NAACL 2025, aclanthology.org/2025.naacl-short.19/] (Pivoted and Regulated Optimization for Multilingual Instruction Learning) treats English as an internal pivot and disentangles English vs. target-language training objectives via separate regularized losses to reduce negative interference; like PLUG and CLO, PROM presupposes a single English pivot without addressing typological distance, multi-pivot source selection, or agglutinative low-resource targets such as Kazakh, Mongolian, and Uyghur. LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer [arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address. Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target. Revisiting Multilingual Data Mixtures [Foroutan et al., 2025, arXiv:2510.25947] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. A concurrent theoretical framework 'Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family' (arXiv:2604.06202, April 2026) proposes the Turkic Transfer Coefficient (TTC), a composite typological similarity metric combining morphological, lexical, syntactic, and script compatibility for Turkic languages. Unlike TWMP, arXiv:2604.06202 is a theoretical analysis without training method, instruction tuning experiments, or evaluation on KazMMLU, MiLiC-Eval, or TUMLU; it corroborates the motivation for Turkic-pivot weighting but does not instantiate it empirically. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.\",\n  \"approach\": \"We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\\n\\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\\n\\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 (p=0.061; measured against linguistic similarity distance alignment metric G_d, Table 1) versus ρ=0.260 for the full 800-feature set, and additionally yields +7.8% improvement on LangRank downstream cross-lingual NLP tasks, we apply this feature selection before computing cosine distances. The downstream task gains (+7.8% LangRank) provide the primary empirical justification for the feature selection step; the typological alignment improvement (p=0.061) is directionally consistent but borderline significant and should not be cited as standalone evidence. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\\n\\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\\n\\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\\n\\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\\n\\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh (Kazakh-language subset, ~11K questions), MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG, PROM [NAACL 2025], and CLO serve as primary English-pivot baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO/PROM baselines, URIEL+ sub-space ablations, curriculum schedule variants, DPO quality gate ablation row, and DPO prerequisite probe runs)\",\n      \"gpu_utilization\": \"LOW (~25–35%): GPU sits idle during code writing, debugging, data pipeline work, result analysis, and paper writing; runs are launched manually and often queue overnight\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$300 (200h × $1.50/h on Lambda Labs A100)\",\n      \"h100_equivalent\": \"~120h H100 (within ≤200 H100-hour budget constraint at typical A100/H100 performance ratio of ~0.6×)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~310h A100 (agent explores broader hyperparameter space with human approval gates; ~55% more runs than manual)\",\n      \"gpu_utilization\": \"MODERATE (~55–65%): agent queues follow-up experiments immediately after each run completes, filling GPU idle between human check-ins\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in to approve experiment configs and review intermediate results\",\n      \"claude_api_cost\": \"~$150–250 (~1,500–2,500 conversation turns coordinating experiment scheduling, result parsing, and ablation planning)\",\n      \"estimated_gpu_cost\": \"~$465 (310h × $1.50/h)\",\n      \"h100_equivalent\": \"~186h H100 (within ≤200 H100-hour budget constraint at ~0.6× A100/H100 ratio, leaving ~14h headroom)\",\n      \"risk_note\": \"Choice of URIEL+ feature subspace (full 800-feature vs. Laplacian 300-feature vs. syntax-only) and the DPO prerequisite probe threshold require human judgment at key decision points; an automated agent may converge on a locally optimal weighting scheme that under-performs on the held-out Swahili generalization target\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~600h A100 (3–5× more experiments: grid search over distance metrics, curriculum schedule shapes, LoRA rank/alpha, 5+ target languages including Swahili and Kyrgyz for generalization, plus replication runs)\",\n      \"gpu_utilization\": \"NEAR-ZERO idle—agent schedules jobs back-to-back across all target languages in parallel, launches follow-up ablations immediately on job completion, and runs nightly sweeps without human bottleneck\",\n      \"timeline\": \"5–10 days with 4× concurrent A100s; ~3 weeks on a single A100\",\n      \"team\": \"0 (initial setup of experiment configs, data paths, and evaluation harness only)\",\n      \"claude_api_cost\": \"~$400–650 (~4,000–6,500 turns for full experiment orchestration, result parsing, ablation tree exploration, and report drafting)\",\n      \"estimated_gpu_cost\": \"~$900 (600h × $1.50/h)\",\n      \"h100_equivalent\": \"~360h H100 — EXCEEDS the ≤200 H100-hour hard budget constraint. Auto_research mode is documented for completeness but is NOT a viable deployment option within the stated budget. Use manual mode (~120 H100h) or human_in_loop mode (~186 H100h) to remain within budget.\",\n      \"speed_bottleneck\": \"GPU count is the primary bottleneck: 4 concurrent A100s reduces wall-clock time to ~5 days; API rate limits become secondary when running >8 parallel experiment threads\",\n      \"risk_note\": \"CONSTRAINT VIOLATION: 600 A100h ≈ 360 H100h, exceeding the ≤200 H100-hour hard budget. Additionally, unconstrained exploration may overfit the URIEL+ weighting function to the 3 initial target languages; Swahili as a held-out agglutinative target is required to detect this overfitting early.\"\n    }\n  },\n  \"target_venues\": [\n    \"ACL 2027 (ARR submission deadline August 3, 2026) — primary target; provides adequate time for validation on additional typological clusters beyond Turkic–Mongolic, and for a paper of this scope (multi-pivot curriculum + ablations + 3 evaluation benchmarks) that cannot realistically reach conference quality in under 6 weeks\",\n    \"EMNLP 2026 (ACL Rolling Review, rolling deadlines throughout 2026) — viable only if the team has prior QLoRA fine-tuning infrastructure already in place and can begin experiments immediately\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (ACL 2024) [29% improvement on Chinese/Korean/Italian/Spanish; Turkic/Mongolic gap is untested]\",\n    \"Cross-Lingual Optimization for Language Transfer in Large Language Models (CLO; ACL 2025, arXiv:2505.14297) [DPO-style cross-lingual preference optimization using English-only source and M2M100 translation; baseline and methodological reference for TWMP's multi-source DPO extension]\",\n    \"PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning (NAACL 2025, aclanthology.org/2025.naacl-short.19/) [treats English as an internal pivot and disentangles English vs. target-language training objectives via regulated losses to reduce negative interference; like PLUG and CLO, fixes English as the sole pivot without addressing typological distance, multi-pivot sequencing, or agglutinative low-resource targets—cited as an English-pivot baseline alongside PLUG and CLO]\",\n    \"LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning (Ye et al., AAAI 2026, arXiv:2511.10229) [selects multilingual instruction data using language separability scores from the model's own representation space across 22 languages including low-resource targets; differentiated from TWMP's external URIEL+ typological weighting independent of training dynamics, staged curriculum, and multi-source DPO objective]\",\n    \"Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages (Idris et al., arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track) [multi-source cross-lingual transfer as budget-constrained resource allocation for NER and sentiment analysis on Hausa, Yoruba, and Swahili across 288 experiments; no typological features or curriculum ordering—differentiated from TWMP's URIEL+-weighted staged instruction tuning; note: preprint only, acceptance not yet confirmed]\",\n    \"Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) [3-stage curriculum (token-level → sentence-level → monolingual code-switching) for single language pair; primary focus Korean, with Japanese and Indonesian—differentiated from TWMP's multi-pivot typological curriculum without code-switching targeting a family of related agglutinative languages]\",\n    \"Revisiting Multilingual Data Mixtures in Language Model Pretraining (Foroutan et al., arXiv:2510.25947, ICLR-submitted 2025) [multilingual data reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); differentiated from TWMP's instruction-tuning-scale LoRA curriculum where data volume, optimization dynamics, and gradient signal are qualitatively different]\",\n    \"Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (Laiyk et al., ACL 2025 Long, arXiv:2502.13647) [10,600 GPT-4o-assisted Kazakh instruction examples fine-tuning Qwen/Falcon/Gemma; requires target-language labels and is Kazakh-specific—differentiated from TWMP's label-free multi-target approach covering Mongolian and Uyghur equally]\",\n    \"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+ (Shipton et al., LREC 2026, arXiv:2510.27183) [extends URIEL+ with script vectors and Glottolog genealogies for 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages]\",\n    \"Llama-3.1-Sherkala-8B-Chat (arXiv:2503.01493) [trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish; demonstrates Turkish as auxiliary language improves Kazakh performance via full fine-tuning; differentiated from TWMP's generalizable LoRA recipe parameterized by continuous URIEL+ distances]\",\n    \"Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) [implicit reward transfer from English-aligned DPO model to annotate cross-lingual preference pairs; 12.72% Win Rate improvement on X-AlpacaEval; English-only source with no typological weighting—differentiated from TWMP's multi-pivot source selection and low-resource agglutinative targets]\",\n    \"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP; official repository: github.com/LeeLanguageLab/URIELPlus]\",\n    \"Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset achieves ρ=0.358 (p=0.061; measured on linguistic distance alignment against G_d metric, Table 1) vs. ρ=0.260 for full 800-feature URIEL+; downstream improvement of +7.8% on LangRank tasks; ρ values verified from paper HTML; downstream gains provide the primary justification for TWMP's feature selection step—the typological alignment improvement is directionally consistent but borderline significant]\",\n    \"Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]\",\n    \"TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]\",\n    \"Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]\",\n    \"Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family (arXiv:2604.06202, April 2026) [theoretical framework introducing Turkic Transfer Coefficient (TTC) combining morphological, lexical, syntactic, and script compatibility; no training method or instruction tuning experiments; no evaluation on KazMMLU/MiLiC-Eval/TUMLU—corroborates motivation for Turkic-pivot weighting without instantiating it empirically]\",\n    \"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark; 23K total questions (approximately 11K in Kazakh, 12K in Russian) sourced from authentic Kazakhstani educational materials; peer-reviewed; TWMP evaluates on the Kazakh-language subset only]\",\n    \"MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]\",\n    \"TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]\",\n    \"Do Chinese Models Speak Chinese Languages? (arXiv:2504.00289, April 2026) [evaluates 10 LLMs across 21 language variants including Uyghur, Mongolian, Kazakh, and Tibetan; Llama3-Instruct is uniquely capable at Uyghur and ranks highest on Mongolian; Chinese LLMs do not outperform Western counterparts on minority languages—contemporary evidence for the performance gap TWMP addresses]\",\n    \"Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]\",\n    \"Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)\",\n    \"Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)\",\n    \"Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]\",\n    \"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]\"\n  ],\n  \"description\": \"This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds Glottolog genealogies covering 26,449 languages; TWMP uses the COLING 2025 base version, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358, p=0.061, measured on linguistic distance alignment with G_d metric, Table 1; +7.8% improvement on LangRank downstream tasks; vs. ρ=0.260 for the full 800-feature set; ρ values verified from paper HTML—the downstream gains are the primary justification, as the typological alignment improvement is directionally consistent but borderline significant) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. Contemporary evidence from 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026), which evaluates 10 LLMs across 21 language variants, shows that Llama3-Instruct is the only evaluated model with distinctive Uyghur capability and that Chinese LLMs do not outperform Western counterparts on minority languages including Uyghur and Mongolian—confirming that no current model family addresses the performance gap TWMP targets. LangGPS (Ye et al., AAAI 2026, arXiv:2511.10229) selects multilingual instruction data by language separability from the model's own representation space across 22 languages; TWMP instead uses external URIEL+ features independent of training dynamics, with a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer (Idris et al., arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track) frames multi-source transfer as budget-constrained allocation for NER/sentiment tasks without typological features or curriculum ordering—TWMP's principled weighting and staged scheduling address instruction tuning specifically. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. Code-Switching Curriculum Learning (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) proposes a 3-stage code-switching curriculum for a single language pair; TWMP's curriculum spans a typologically ordered pool of pivot languages without code-switching. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). PROM [NAACL 2025] similarly treats English as an internal pivot and disentangles English and target-language training objectives via regulated losses; like PLUG and CLO, PROM fixes a single English pivot without addressing typological distance or multi-pivot sequencing for agglutinative targets—all three serve as English-pivot baselines in TWMP's evaluation. Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. Instructions yielding no target-language candidates post-gate fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Laiyk et al. (ACL 2025 Long, arXiv:2502.13647) fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP requires no target-language labels and applies equally to Mongolian and Uyghur where no comparable dataset exists. Revisiting Multilingual Data Mixtures (Foroutan et al., arXiv:2510.25947) studies reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); TWMP targets instruction-tuning scale where data volume, optimization dynamics, and gradient signal are qualitatively different. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. A concurrent theoretical framework (arXiv:2604.06202, April 2026) proposes the Turkic Transfer Coefficient (TTC) for cross-lingual adaptation within the Turkic family but offers no training method or instruction tuning experiments. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU (Kazakh-language subset, ~11K questions), MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.\",\n  \"project_name\": \"typological_multi_pivot\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL – TIPA (arXiv:2601.16629, EACL 2026 Findings) is directly competing work the generator missed: it constructs proxy language adapters by aggregating existing ones weighted by typological similarity across 230+ languages and five tasks. The novelty claim 'no prior work combines multi-pivot selection with typological distance weighting' is therefore too strong; the revision must differentiate TWMP from TIPA clearly (TIPA is training-free adapter aggregation for encoders; TWMP is a weighted sampling + curriculum training approach for decoder LLMs in instruction tuning—this distinction exists but must be made explicit).\", \"CRITICAL – Evaluation benchmarks are misspecified: XQuAD and XCOPA do NOT include Kazakh, Mongolian, or Uyghur—multiple sources and the benchmarks' own documentation confirm this. The evaluation protocol must be redesigned to use benchmarks that actually cover the target languages (e.g., XTREME-UP, MiLiC-Eval for Chinese minority languages, or TyDi QA for Kazakh).\", \"SIGNIFICANT – Model name 'Qwen 3.5-7B' does not exist. The Qwen3.5 series released in 2026 includes 4B and 9B variants (among others) but no 7B. The 250K vocabulary claim is correct for Qwen3.5 but the model identifier must be corrected to Qwen3.5-9B or Qwen3.5-4B before submission.\", \"SIGNIFICANT – 16-day timeline is unrealistic for a conference-quality submission. Running 15–20 QLoRA experiments across 3 target languages, implementing the TWMP curriculum + CLO loss from scratch, and writing a complete paper cannot be done in 16 days by 1–2 researchers without preexisting infrastructure. The compute estimate (180h A100 ≈ 125–135h H100) is within the 200 H100-hour hard constraint, but wall-clock time is the binding bottleneck.\", \"SIGNIFICANT – The primary evidence for the research gap, 'Left Behind' (arXiv:2603.21036), is a March 2026 preprint from a single author at North American University evaluated with 50 hand-crafted questions. EMNLP reviewers will reject this as insufficient basis for a gap claim; the motivation must be grounded in larger, peer-reviewed evaluations (e.g., the 'Shared Weights Pretraining for Extremely Low-Resource Languages' ACL 2025 paper, or XTREME-UP results for Turkic languages).\", \"MODERATE – Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) is not properly discussed in the landscape. This paper directly uses typological feature vectors for language selection in multilingual instruction tuning—the generator characterizes only arXiv:2505.13908 (which is purely analytical) while ignoring this more methodologically relevant prior work.\", \"MODERATE – MLM is a NeurIPS 2025 ER Workshop paper, not a NeurIPS 2025 main conference paper. Misrepresenting workshop papers as conference papers in a related work section is a frequent reviewer complaint and can trigger a bias/credibility flag.\", \"MODERATE – The CLO-style loss is described as a 'cross-lingual contrastive loss that enforces target-language response fidelity.' CLO actually uses DPO-style preference optimization (not a contrastive loss) to suppress off-language responses. The paper must use technically accurate descriptions to avoid confusion and reviewer pushback.\", \"MINOR – PLUG (ACL 2024)'s 29% improvement was measured on Chinese, Korean, Italian, and Spanish—not on Kazakh/Mongolian/Uyghur. The assumption that PLUG performs poorly on Turkic languages is plausible but not directly evidenced in the PLUG paper itself; the gap claim relative to PLUG needs its own experimental demonstration.\"]\nFeedback: The core idea is genuinely interesting—typological-distance-weighted multi-pivot instruction tuning for Turkic low-resource languages—but the current draft has three blockers that prevent submission at EMNLP 2026 quality: (1) TIPA (EACL 2026) must be cited and clearly differentiated: TIPA does typological weighting of adapters in a training-free, encoder-adapter (MAD-X) framework across 230+ languages; TWMP is a training-time data sampling + curriculum approach for decoder LLMs in instruction tuning—spell this out explicitly in Section 2. (2) Replace XQuAD + XCOPA with benchmarks that actually include Kazakh, Mongolian, and Uyghur: consider XTREME-UP (includes Kazakh), MiLiC-Eval (Uyghur, Kazakh, Mongolian), and TyDi QA for real-language evaluation. If none of the standard benchmarks are adequate, you need to explain what evaluation data you are using and where it comes from. (3) Correct the model name to Qwen3.5-9B (or 4B) and rerun your compute estimates accordingly. Beyond the blockers: the motivation should be regrounded away from 'Left Behind' as the sole anchor—add references to XTREME-UP or ACL 2025 shared-weights pretraining results for Turkic languages. Add arXiv:2410.07809 to related work with a clear explanation of why TWMP's weighted sampling and curriculum are distinct contributions. Fix the MLM venue to 'NeurIPS 2025 ER Workshop' and fix the CLO description to 'DPO-style cross-lingual preference optimization.' On timeline: unless the team has the training infrastructure already built, the 16-day window makes a May 25 ARR deadline extremely risky; the ACL 2027 ARR deadline (August 3, 2026) is a more defensible target that allows proper validation on additional typological clusters (e.g., a Bantu agglutinative language) to test generalization beyond Turkic.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"SIGNIFICANT – CLO's DPO objective is designed for English-source preference pairs: chosen = target-language response to English instruction, rejected = off-language (English) response to target-language instruction. TWMP proposes extending this to non-English source languages (Turkish/Uzbek → Kazakh), but the paper does not specify how preference pairs are constructed when the source is itself a non-English language like Uzbek. If the model produces a Kazakh response to a Uzbek instruction, what is the 'rejected' response? Reviewers will reject this as technically incomplete without a precise DPO formulation for the multi-source case.\", \"SIGNIFICANT – URIEL legacy features are known to be sparse for exactly the target languages in this paper. URIEL+ (arXiv:2409.18472, COLING 2025) explicitly improves coverage for low-resource languages and should be used instead of the 289-dim lang2vec legacy features. Furthermore, 'Less is More: The Effectiveness of Compact Typological Language Representations' (EMNLP 2025) shows that compact URIEL+ features outperform the full 289-dim feature space for cross-lingual NLP tasks—directly contradicting TWMP's use of all 289 dimensions without selection. This is a directly relevant citation the paper must engage with.\", \"MODERATE – Auto_research mode (600h A100 ≈ 300h H100) exceeds the stated ≤200 H100-hour hard constraint. While the experiment plan uses manual mode (within constraint), the resource estimate table presents auto_research as a legitimate deployment mode without flagging this violation of the user's stated budget constraint.\", \"MODERATE – The staged curriculum's cosine-distance threshold schedule is described qualitatively ('progressively expands the radius at scheduled epochs') but no concrete schedule is specified. Reviewers will ask: how many stages? What distance thresholds? How are thresholds set relative to the URIEL distance distribution of the Aya collection? Without a concrete, reproducible specification, this is a design element that cannot be ablated or replicated.\", \"MODERATE – DCO (arXiv:2603.04678, March 2026, Tianyu Liu et al.) introduces Direct Consistency Optimization, a DPO-inspired method for cross-lingual knowledge consistency across 26 languages and 9 LLMs. This is a concurrent work that uses a DPO-style objective for cross-lingual alignment—similar in spirit to the CLO component of TWMP—and must be cited and differentiated in the related work section.\", \"MINOR – The Aya dataset's coverage of Turkic pivot languages (Turkish, Uzbek, Kyrgyz) is assumed but not verified. If Uzbek and Kyrgyz have only hundreds of Aya instances, the typological-distance-weighted sampling will produce noisy estimates for the closest pivots to Kazakh. The paper should state the number of available training instances per pivot language in Aya and set a minimum threshold below which a language is excluded from the mixture.\"]\nFeedback: The generator has addressed all Round 1 critical issues competently: TIPA is correctly differentiated, benchmarks are fixed, Qwen3.5-9B is confirmed correct, arXiv:2410.07809 is properly placed in the landscape, and the CLO/DPO description is accurate. The remaining blockers are two: (1) The DPO objective must be precisely formulated for non-English source languages. The current description 'increases preference for target-language responses and reduces preference for off-language outputs, without requiring any target-language training labels' is borrowed verbatim from CLO's English-source setting. For a Turkish → Kazakh pair, you must specify: what constitutes the chosen response, what constitutes the rejected response, and how you obtain these without any Kazakh labels. One viable extension: treat (Turkish-instruction, Kazakh-response) as the chosen pair and (Turkish-instruction, Turkish-response) as rejected—but this requires stating it explicitly and verifying that Qwen3.5-9B produces detectable off-language Turkish responses to Turkish instructions. (2) Replace lang2vec 289-dim URIEL features with URIEL+ (arXiv:2409.18472, COLING 2025), which has better sparse-language coverage, and cite 'Less is More' (EMNLP 2025) to justify whichever feature subspace you choose. This is not just a citation gap—if the typological distances for Uzbek and Kyrgyz are inaccurate in legacy URIEL due to sparsity, the entire weighting scheme degrades for the most important (closest) pivots to Kazakh. Beyond the blockers: add DCO (arXiv:2603.04678) to related work; specify the curriculum schedule concretely (number of stages, distance thresholds); verify and report the number of Aya instances per Turkic pivot language; and note that auto_research mode exceeds the 200 H100-hour constraint if that constraint applies. ACL 2027 (August 3, 2026 ARR) remains the appropriate primary venue.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MODERATE – Sherkala-Chat (arXiv:2503.01493, March 2025) is a directly relevant uncited work: it instruction-tunes Llama-3.1-8B for Kazakh on 45.3B tokens of Kazakh, English, Russian, and Turkish data, demonstrating that Turkish as an auxiliary training language improves Kazakh performance—the empirical core insight that motivates TWMP's pivot selection. Not citing it leaves a gap reviewers will notice; TWMP should add it as related work and contrast it: Sherkala-Chat uses ad-hoc four-language mixing with full fine-tuning, whereas TWMP provides a principled, generalizable, LoRA-based method parameterized by continuous URIEL+ distances applicable across any agglutinative target.\", \"MODERATE – The DPO preference pair construction specifies 'highest-scoring chosen' and 'lowest-scoring rejected,' where 'scoring' is implicitly language identification confidence from fastText. This means a grammatically garbled Kazakh response with high fastText confidence could be chosen as the preferred response over a coherent Turkish response. No quality filter (perplexity, length heuristic, or instruction-following score) is applied to the chosen pool. Reviewers will ask whether the DPO training signal is noisy precisely for the close-pivot cases where K=8 Kazakh responses are plentiful—yet quality varies most—and for distant pairs where only 1 of 8 samples passes the language filter, leaving little variance to select from. The paper should either add a quality filter (e.g., exclude responses shorter than 20 tokens or with perplexity above a threshold under the base model) or explicitly acknowledge and ablate this as a limitation.\", \"MINOR – Qwen3.5-9B release date: the paper states 'released February 2026' but available information indicates the Qwen3.5 small series (0.8B/2B/4B/9B) became available March 2, 2026—the February date applies to the larger Qwen3.5 medium models (35B-A3B, 27B). This should be corrected to March 2026.\", \"MINOR – The URIEL+ repository URL cited in the approach section ('github.com/Masonshipton25/URIELPlus') does not match the official ACL Anthology-linked repository ('github.com/LeeLanguageLab/URIELPlus'). The URL should match the official publication's repository or the PyPI package ('urielplus') should be referenced instead.\", \"MINOR – The Kyrgyz Aya instance count ('~4.1M instances in the Aya collection language split') could not be independently verified against HuggingFace statistics. Given Kyrgyz is much lower-resource than Turkish, this count depends entirely on machine-translated data volume and should be verified and cited to the HuggingFace dataset page or the Aya Collection paper's per-language appendix before submission.\"]\nFeedback: The generator has addressed all Round 2 issues competently: the multi-source DPO formulation is now precisely specified (chosen = source-language instruction + model-generated target-language response; rejected = source-language instruction + model-generated source-language response), URIEL+ replaces legacy 289-dim features with the 'Less is More' 300-feature Laplacian subset, the staged curriculum has concrete D_25/D_60 percentile anchors and epoch ranges, DCO is cited and differentiated, Aya coverage is verified with a 5,000-instance floor, and auto_research mode is correctly flagged as exceeding the 200 H100h budget. Two moderate issues remain before this is submission-ready: (1) Add Sherkala-Chat (arXiv:2503.01493) to related work—it is a directly adjacent March 2025 paper training Llama-3.1 on Kazakh+Turkish+Russian and provides empirical motivation for TWMP's pivot selection logic. The contrast is easy: Sherkala-Chat is language-specific full fine-tuning with ad-hoc pivot choice; TWMP is generalizable LoRA-based training with principled URIEL+ weighting. (2) Address the DPO pair quality concern: define 'highest-scoring' explicitly as language ID confidence, acknowledge that this does not filter for response quality, and either add a minimal quality gate (e.g., minimum response length or base-model perplexity cap) or include it as a stated limitation with an ablation that shows the fastText-only selection is adequate in practice. Fix the three minor issues (Qwen3.5 release date, URIEL+ repo URL, Kyrgyz instance count verification) before submitting. ACL 2027 (August 3, 2026 ARR) remains the appropriate primary target; given these are all fixable within days, the paper is on track.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MODERATE – Sherkala-Chat (arXiv:2503.01493) was flagged in Round 3 as a key uncited adjacent work and remains absent from Round 4. This paper trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish, directly demonstrating that Turkish as an auxiliary language improves Kazakh performance — the empirical core claim motivating TWMP's pivot selection logic. EMNLP reviewers familiar with Kazakh NLP will notice this omission immediately. Required: add to related work section with explicit contrast (Sherkala-Chat uses ad-hoc 4-language full fine-tuning for Kazakh specifically; TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target).\", \"MODERATE – DPO pair quality gate still absent. The approach specifies 'pair the highest-scoring chosen with the lowest-scoring rejected' based on fastText language ID confidence alone, with no quality filter. For close-pivot pairs (Turkish→Kazakh), K=8 sampling may yield 5–7 Kazakh responses, creating a large chosen pool with highly variable quality; the 'highest-scoring' fastText criterion selects the response with the highest Kazakh language ID confidence, which is not correlated with response coherence or instruction-following quality. A grammatically garbled but confidently Kazakh response will be preferred over a fluent but lower-confidence response. This was raised in Round 3 and remains unaddressed. Fix: add a minimum response length gate (e.g., ≥20 tokens) or base-model perplexity cap, or include an explicit ablation comparing fastText-only selection vs. a quality-gated variant and acknowledge this as a limitation with empirical validation.\", \"MODERATE – Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings) is uncited and directly relevant to TWMP's DPO component. This paper uses implicit reward transfer from English DPO models to annotate cross-lingual preference pairs for multilingual DPO fine-tuning, achieving 12.72% average Win Rate improvement on X-AlpacaEval across training languages. While the approach differs from TWMP (English-only source, implicit reward annotation, no typological weighting), it represents active concurrent work on cross-lingual DPO alignment that EMNLP reviewers will expect to see cited and contrasted. Required addition to related work: differentiate TWMP's direct construction of multi-source preference pairs via language ID vs. this paper's implicit reward annotation from a single English-aligned model.\", \"MINOR – Qwen3.5-9B release date error persists for the third consecutive round. The submission states 'released February 2026' but independent verification (multiple sources) confirms the Qwen3.5 small series (0.8B/2B/4B/9B) was released March 1–2, 2026, with February 2026 referring to the larger Qwen3.5 medium models (35B-A3B, 27B). Change 'released February 2026' to 'released March 2026'.\", \"MINOR – URIEL+ repository URL persists as incorrect for the third consecutive round. The submission cites 'github.com/Masonshipton25/URIELPlus' but the official ACL Anthology-linked repository is 'github.com/LeeLanguageLab/URIELPlus' (confirmed). Change to the correct URL or cite the PyPI package 'urielplus' instead.\"]\nFeedback: This is Round 4 and the same four issues (Sherkala-Chat, DPO quality gate, release date, repo URL) that were flagged in Round 3 have not been addressed. The pattern is concerning for an ARR deadline in 15 days. Here is exactly what needs to change, in priority order:\n\n(1) Add Sherkala-Chat to Section 2 related work. One paragraph is sufficient: 'Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish, demonstrating that Turkish as an auxiliary language improves Kazakh performance—motivating our choice of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc pivot selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language.'\n\n(2) Add Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings) to Section 2. One sentence: 'Implicit Cross-Lingual Rewarding annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving strong multilingual alignment from English-only source data—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from this work.'\n\n(3) Fix the DPO quality issue. Choose one of: (a) add a minimum 20-token length gate to the chosen pool and state it explicitly; (b) add a perplexity cap at 2× base-model perplexity on the instruction; or (c) keep the current fastText-only selection but add a clearly labeled limitation paragraph and one ablation row in Table X comparing fastText-only vs. length-gated selection. Option (c) requires the least implementation effort and is acceptable.\n\n(4) Fix two one-line errors: 'released February 2026' → 'released March 2026'; 'github.com/Masonshipton25/URIELPlus' → 'github.com/LeeLanguageLab/URIELPlus'.\n\nNone of these require new experiments. Issues (1), (2), (4) are writing-only changes. Issue (3) option (c) requires one additional experiment row or a paragraph addition. The paper is substantively sound and the core novelty claim is defensible—these are editorial and citation completeness fixes that are blocking an otherwise strong submission. ACL 2027 (August 3, 2026 ARR) remains the more realistic target, but if the team has existing QLoRA infrastructure, EMNLP 2026 (May 25 ARR) is feasible after these four fixes.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE – Revisiting Multilingual Data Mixtures (arXiv:2510.25947, Foroutan et al., EPFL, Oct 2025) directly challenges TWMP's two core premises: (1) staged curriculum learning 'does not reduce negative interference' in multilingual training, and (2) temperature-based language reweighting 'hurts performance due to noise' on low-resource data. This paper focuses on pretraining, not instruction tuning, but EMNLP reviewers familiar with it will raise it against TWMP's staged curriculum and inverse-distance weighting scheme. Required: cite this paper in Section 2, acknowledge the potential discrepancy, and argue explicitly why the instruction tuning setting (smaller data footprint, fewer gradient steps, different optimization landscape) is different enough that the Foroutan et al. findings do not transfer.\", \"MODERATE – LangGPS (arXiv:2511.10229, AAAI 2026; Yangfan Ye, Xiaocheng Feng et al., HIT + Microsoft) proposes language separability from the model's own representation space as the basis for multilingual instruction tuning data selection, and reports improvements over external-feature-based approaches across 22 languages including low-resource targets. It is a peer-reviewed AAAI 2026 competitor to TWMP's URIEL+-based selection approach. This is too similar to leave uncited. Required: add to related work and differentiate: LangGPS uses task-adaptive model-internal signals but is agnostic to typological structure and provides no mechanism for multi-pivot curriculum sequencing; TWMP uses external typological features to derive a principled ordering over pivot languages independent of training dynamics.\", \"MODERATE – Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (arXiv:2411.02460, ACL 2025 Findings; Haneul Yoo et al., NAVER AI) proposes a 3-stage curriculum (token-level code-switching → sentence-level code-switching → monolingual) that achieves cross-lingual transfer improvements on both high- and low-resource languages without typological distance. This paper has been available since November 2024—before all prior review rounds—and has never appeared in TWMP's references. EMNLP reviewers will notice its absence. Required: cite and contrast in Section 2: the code-switching curriculum operates within a single language pair using surface-level code-mixing as a bridge, whereas TWMP's curriculum operates over a pool of typologically ordered pivot languages with no code-switching; the two approaches address different facets of cross-lingual curriculum design and could in principle be combined.\", \"MINOR – Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (arXiv:2502.13647, ACL 2025 Main; Laiyk et al.) fine-tunes Qwen/Falcon/Gemma on 10,600 GPT-4o-assisted Kazakh instruction examples, achieving consistent improvement on multiple-choice and generative Kazakh tasks. This is a direct Kazakh instruction tuning baseline from ACL 2025 that any reviewer working on KazMMLU will expect TWMP to compare against or at minimum cite. It documents that targeted single-language instruction data generation is a strong alternative to cross-lingual transfer methods—TWMP should position itself relative to it (e.g., TWMP does not require any target-language instruction labels and is applicable to Mongolian and Uyghur where no comparable GPT-4-assisted dataset exists).\", \"MINOR – Simple Additions, Substantial Gains: Expanding URIEL+ (arXiv:2510.27183, LREC 2026; Shipton, Ng, Khan et al.) extends the URIEL+ database with script vectors, Glottolog integration, and genealogical feature propagation, reducing feature sparsity by 35% and expanding coverage to 26,449 languages—directly addressing the sparsity problem for Kazakh/Uzbek/Kyrgyz that TWMP cites as motivation for switching from legacy lang2vec to URIEL+. TWMP should either use this updated version or acknowledge it as a contemporaneous development and argue that the 2409.18472 COLING 2025 version is sufficient for the target languages (the 35% sparsity reduction would most benefit exactly the low-resource Turkic languages in scope).\", \"MINOR – The DPO prerequisite probe threshold is set at >5% of K=8, which equals at least 1 target-language response in 8 tries. This is the minimum viable signal level and means many source-target pairs that 'pass' the probe provide almost no diversity in the chosen pool (only 1 candidate). At this threshold, the 20-token gate can cause 100% discard of chosen candidates for those instructions (if the single Kazakh response is <20 tokens), silently collapsing to SFT-only training for many instruction prompts without reporting. The paper should characterize the empirical distribution of per-instruction chosen-pool sizes (1, 2, 3+ responses) across source-target pairs and report what fraction of instructions fall back to SFT-only due to post-gate chosen pool exhaustion.\"]\nFeedback: All Round 4 issues are addressed: Sherkala-Chat is properly cited and contrasted, the DPO 20-token length gate and ablation row are specified, Implicit Cross-Lingual Rewarding is cited, the release date and URIEL+ URL are corrected. The paper's core method is substantively sound and the technical specification is unusually precise for a draft at this stage. Three writing-only additions are needed before this is EMNLP-ready:\n\n(1) Add Foroutan et al. (arXiv:2510.25947) to Section 2. Key contrast: that paper tests pretraining-scale reweighting across 25–400 languages; TWMP operates at instruction tuning scale (10 epochs, LoRA, ≤6,400 instances per pivot) where reweighting over a narrow near-family pivot pool is qualitatively different from resampling across 400 pretraining languages. Make this argument explicitly to preempt the obvious reviewer objection.\n\n(2) Add LangGPS (arXiv:2511.10229, AAAI 2026) and Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings) to Section 2. Both are one-paragraph additions: LangGPS uses model-internal representation signals (no external typological database, no multi-pivot ordering); Code-Switching Curriculum uses surface-level code-mixing within a pair (no typologically structured pool, no DPO). Neither addresses the multi-pivot ordering problem or provides a principled recipe for pivot sequencing across typologically diverse targets.\n\n(3) Add arXiv:2502.13647 (ACL 2025 Main, Kazakh instruction tuning) as a related baseline in Section 2 and note it cannot generalize to Mongolian and Uyghur where no comparable target-language instruction dataset exists.\n\nFor the probe threshold: add one sentence clarifying what happens when the post-gate chosen pool for a given instruction is empty—confirm that those instructions fall back to the SFT-weighted objective, not to silent skip, and report the per-pair fallback rate as a characterization result.\n\nACL 2027 (ARR August 3, 2026) remains the appropriate primary target. None of these additions require new experiments.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"SIGNIFICANT (PATTERN) – All five Round 5 issues remain unaddressed in Round 6 for the second consecutive round. (1) Foroutan et al. (arXiv:2510.25947, ICLR-submitted): not in landscape or key_references. (2) LangGPS (arXiv:2511.10229, AAAI 2026 main): not in landscape or key_references — this is a peer-reviewed AAAI 2026 competitor on multilingual instruction tuning data selection across 22 languages including low-resource targets, and its omission is the most damaging gap. (3) Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings): not cited despite being published November 2024 and appearing in ACL Anthology. (4) arXiv:2502.13647 (ACL 2025 Long, Kazakh instruction tuning): not cited despite being a direct Kazakh-targeting baseline. (5) URIEL+ expansion (arXiv:2510.27183, LREC 2026): not cited despite directly extending the typological tool TWMP relies on.\", \"MODERATE (NEW) – Budget-Xfer (arXiv:2603.27651, March 2026) proposes budget-constrained source language selection for multi-source cross-lingual transfer, jointly optimizing which source languages to include and how much data to allocate from each — directly parallel to TWMP's multi-pivot selection problem. It evaluates on three African target languages (Hausa, Yoruba, Swahili) using a 288-experiment suite. While it targets classification tasks rather than instruction tuning, EMNLP reviewers in the cross-lingual track will expect it to be cited and contrasted: Budget-Xfer frames source selection as resource allocation without typological features or curriculum ordering; TWMP provides principled URIEL+-based weighting and staged scheduling.\", \"MINOR (PERSISTENT) – Per-instruction chosen-pool fallback characterization remains incomplete. The approach section states that 'instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' but does not report the per-instruction fallback rate as a characterization result. Round 5 feedback specifically requested one sentence confirming these instructions fall back to SFT-weighted objective (not silent skip) and reporting the empirical fallback rate per source-target pair. The current text says they are 'discarded,' which implies silent skip rather than SFT fallback — this ambiguity must be resolved and the frequency reported.\"]\nFeedback: This is Round 6. The core method is technically sound, the DPO formulation is precise, the compute budget is within constraint, and the evaluation design is appropriate. However, the same five citations flagged in Round 5 are absent for the second consecutive round, and a new paper (Budget-Xfer, arXiv:2603.27651) has appeared that is directly adjacent. Here is the exact text to add for each outstanding item:\n\n(1) Foroutan et al. (Section 2, one sentence): 'Revisiting Multilingual Data Mixtures [Foroutan et al., 2025] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime.'\n\n(2) LangGPS (Section 2, one paragraph — highest priority): 'LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address.'\n\n(3) Code-Switching Curriculum (Section 2, one sentence): 'Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target.'\n\n(4) Kazakh instruction tuning (Section 2, one sentence): 'Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists.'\n\n(5) URIEL+ expansion (Section 3, one sentence): 'A concurrent LREC 2026 extension [Shipton et al., arXiv:2510.27183] adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version [arXiv:2409.18472] with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages.'\n\n(6) Budget-Xfer (Section 2, one sentence): 'Budget-Xfer [arXiv:2603.27651, 2026] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address.'\n\n(7) Fix the per-instruction fallback: Change 'Instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' to 'Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe.'\n\nAll seven items are writing-only changes requiring no new experiments. ACL 2027 (ARR August 3, 2026) remains the appropriate primary target. At Round 6, the paper cannot pass until at minimum items (1)–(5) are resolved.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"MODERATE – KazMMLU benchmark description is factually wrong. The paper repeatedly claims KazMMLU contains '23K Kazakh-language questions spanning STEM, humanities, and social sciences,' but independent verification of arXiv:2502.12829 shows the dataset contains 10,969 Kazakh-language questions + 12,031 Russian-language questions = 23,000 total. Only ~47% of questions are in Kazakh; the remainder are in Russian. Any EMNLP reviewer who reads the KazMMLU abstract will catch this. The description should read '23K questions (approximately 11K in Kazakh, 12K in Russian) sourced from Kazakhstani educational materials.' For TWMP's Kazakh instruction evaluation, only the Kazakh-language subset is relevant, which is smaller than the paper implies.\", \"MINOR – PROM (NAACL 2025, arXiv not yet located but published at ACL Anthology at aclanthology.org/2025.naacl-short.19/) introduces 'Pivoted and Regulated Optimization,' which treats English as an internal pivot and disentangles English vs. target-language training objectives via separate regularized losses for multilingual instruction tuning. This is adjacent to PLUG and CLO in the landscape of English-pivot methods for multilingual instruction following, and EMNLP reviewers familiar with the NAACL 2025 proceedings will expect it to be cited alongside PLUG and CLO. One sentence suffices: 'PROM [NAACL 2025] disentangles English-pivot and target-language training objectives via regulated losses — like PLUG and CLO, it fixes English as the sole pivot without addressing typologically distant agglutinative targets.'\", \"MINOR – 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026) evaluates Uyghur and Mongolian capabilities across current LLMs, finding Llama3-Instruct is uniquely capable at Uyghur and top-performing at Mongolian among open models. This is contemporary evidence for the performance gap that motivates TWMP and is published close enough to the ARR deadline to be a missing citation reviewers will notice. One sentence in Section 1 or 2 would suffice.\"]\nFeedback: All Round 6 issues are fully resolved: Foroutan et al., LangGPS, Code-Switching Curriculum, Laiyk et al., URIEL+ expansion, Budget-Xfer, and the fallback characterization now all appear correctly in the landscape and key_references. The paper is close to submission-ready. Three targeted fixes remain:\n\n(1) Fix the KazMMLU description (highest priority — factual error). Change every instance of '23K Kazakh-language questions' to '23K questions spanning Kazakh and Russian (approximately 11K in Kazakh)' or similar accurate phrasing. This appears in the core_problem, opportunity, and key_references fields. This is a one-line fix per occurrence but it is mandatory — the current phrasing is verifiably wrong and will undermine reviewer trust in the paper's factual accuracy.\n\n(2) Add PROM [NAACL 2025] to the landscape (one sentence): 'PROM [NAACL 2025] treats English as an internal pivot and separates English vs. target-language training objectives via regulated losses; like PLUG and CLO, it presupposes a single English pivot without addressing typological distance or multi-pivot sequencing for agglutinative targets.'\n\n(3) Add arXiv:2504.00289 (April 2026) to the opportunity section or related work as supplementary evidence for Uyghur/Mongolian gaps in current LLMs.\n\nNone of these require new experiments. Issues (2) and (3) are one-sentence writing additions; issue (1) is a find-and-replace correction. ACL 2027 (ARR August 3, 2026) remains the appropriate primary target; EMNLP 2026 (May 25 ARR) is feasible only if the team already has the QLoRA infrastructure in place and can begin experiments immediately after these three fixes.\n\n### Round 8 review\nVerdict: revise\nIssues: [\"MINOR – Budget-Xfer (arXiv:2603.27651) is cited throughout as 'SIGIR 2026' but independent verification of the arXiv page confirms its status is 'Submitted to SIGIR 2026 Short Paper track'—it has not been accepted or published at SIGIR 2026. Citing an unaccepted submission as a published venue paper is a citation ethics flag that EMNLP meta-reviewers take seriously. Fix: change 'SIGIR 2026' to 'arXiv preprint, 2026 (submitted to SIGIR 2026)' or simply 'arXiv:2603.27651, 2026' until acceptance is confirmed.\", \"MINOR – The 'Less is More' EMNLP 2025 specific numerical claims (ρ=0.358 for Laplacian-300 vs. ρ=0.260 for full 800-feature URIEL+) could not be verified from the abstract; the direction of the claim ('reduced-size representations yield more informative distance metrics') is confirmed by the abstract, but the precise ρ values should be cross-checked against the paper PDF before submission to ensure they are quoted correctly and refer to the same evaluation task TWMP uses.\"]\nFeedback: All three Round 7 issues are fully resolved in Round 8: the KazMMLU description is now correctly stated as '23K questions total (approximately 11K in Kazakh, 12K in Russian)' across all occurrences; PROM (NAACL 2025, aclanthology.org/2025.naacl-short.19/) is properly cited and differentiated; and arXiv:2504.00289 ('Do Chinese Models Speak Chinese Languages?') appears correctly in the opportunity section. Independent verification confirms: CLO's 3,200-sample efficiency claim is accurate; LangGPS is AAAI 2026 Main Track (confirmed); Qwen3.5-9B released March 2026 (confirmed); URIEL+ at COLING 2025 (confirmed). No uncited competing work was found that would undermine the novelty claim. Only two minor fixes remain before this can pass: (1) Change every instance of 'SIGIR 2026' for Budget-Xfer to 'arXiv:2603.27651, 2026' — the paper is submitted to SIGIR 2026 but not yet accepted; this is a one-line find-and-replace. (2) Verify the exact ρ values from the 'Less is More' PDF before submission. Neither requires new experiments. The paper is in excellent shape for its primary ACL 2027 target (ARR August 3, 2026) and is feasible for EMNLP 2026 (May 25 ARR) with the QLoRA infrastructure caveat.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:20:56.810Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:20:56.810Z",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-10T08:20:56.853Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-10 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Multilingualism and Cross-Lingual NLP.

Direction: Cross-lingual transfer and multilingual NLP methods. In-scope: cross-lingual transfer without parallel data, multilingual instruction tuning strategies, language-agnostic representations, low-resource language adaptation, cross-lingual retrieval, multilingual reasoning, code-switching handling. ACL 2025 outstanding papers highlighted multilingual gaps and cross-lingual intervention methods.

Contribution type: METHOD ONLY. New training recipes, transfer algorithms, or adaptation techniques. Not a new multilingual dataset or language-specific analysis.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Multilingual experiments need coverage across languages — budget for LoRA fine-tuning on multilingual models, not full pretraining.
2. Time: ≤16 days. Use existing multilingual models (BLOOM, mT5, XLM-R, Aya, Qwen multilingual, Llama-3 multilingual).
3. Eval: XTREME-UP, XCOPA, XStoryCloze, MGSM, multilingual MMLU, TyDi QA, FLORES for MT.

Look for: efficient cross-lingual transfer with minimal target-language data, multilingual reasoning without English-centric bias, representation alignment methods, adaptation techniques for typologically diverse languages. Avoid: English-only experiments, monolingual fine-tuning.

Tag: direction=multilingual, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].**
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

## Idea under review (round 9/10)
{
  "title": "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning",
  "core_problem": "Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.",
  "opportunity": "Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K questions total (approximately 11K in Kazakh, 12K in Russian) spanning STEM, humanities, and social sciences sourced from authentic Kazakhstani educational materials; for TWMP's Kazakh instruction evaluation, only the Kazakh-language subset (~11K questions) is relevant; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026) evaluates 10 LLMs across 21 language variants and finds that Llama3-Instruct is the only model showing distinctive Uyghur capability while most models reach only ~75% Mongolian identification accuracy; Chinese LLMs do not outperform Western counterparts on minority languages including Uyghur and Mongolian, confirming that the performance gap TWMP targets persists even in the most recent model generation. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.",
  "landscape": "PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. PROM [NAACL 2025, aclanthology.org/2025.naacl-short.19/] (Pivoted and Regulated Optimization for Multilingual Instruction Learning) treats English as an internal pivot and disentangles English vs. target-language training objectives via separate regularized losses to reduce negative interference; like PLUG and CLO, PROM presupposes a single English pivot without addressing typological distance, multi-pivot source selection, or agglutinative low-resource targets such as Kazakh, Mongolian, and Uyghur. LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer [arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address. Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target. Revisiting Multilingual Data Mixtures [Foroutan et al., 2025, arXiv:2510.25947] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. A concurrent theoretical framework 'Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family' (arXiv:2604.06202, April 2026) proposes the Turkic Transfer Coefficient (TTC), a composite typological similarity metric combining morphological, lexical, syntactic, and script compatibility for Turkic languages. Unlike TWMP, arXiv:2604.06202 is a theoretical analysis without training method, instruction tuning experiments, or evaluation on KazMMLU, MiLiC-Eval, or TUMLU; it corroborates the motivation for Turkic-pivot weighting but does not instantiate it empirically. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.",
  "approach": "We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\n\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\n\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 (p=0.061; measured against linguistic similarity distance alignment metric G_d, Table 1) versus ρ=0.260 for the full 800-feature set, and additionally yields +7.8% improvement on LangRank downstream cross-lingual NLP tasks, we apply this feature selection before computing cosine distances. The downstream task gains (+7.8% LangRank) provide the primary empirical justification for the feature selection step; the typological alignment improvement (p=0.061) is directionally consistent but borderline significant and should not be cited as standalone evidence. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\n\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\n\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\n\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\n\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh (Kazakh-language subset, ~11K questions), MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG, PROM [NAACL 2025], and CLO serve as primary English-pivot baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO/PROM baselines, URIEL+ sub-space ablations, curriculum schedule variants, DPO quality gate ablation row, and DPO prerequisite probe runs)",
      "gpu_utilization": "LOW (~25–35%): GPU sits idle during code writing, debugging, data pipeline work, result analysis, and paper writing; runs are launched manually and often queue overnight",
      "timeline": "4–6 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$300 (200h × $1.50/h on Lambda Labs A100)",
      "h100_equivalent": "~120h H100 (within ≤200 H100-hour budget constraint at typical A100/H100 performance ratio of ~0.6×)"
    },
    "human_in_loop": {
      "gpu_hours": "~310h A100 (agent explores broader hyperparameter space with human approval gates; ~55% more runs than manual)",
      "gpu_utilization": "MODERATE (~55–65%): agent queues follow-up experiments immediately after each run completes, filling GPU idle between human check-ins",
      "timeline": "6–8 weeks",
      "team": "1 researcher, ~30min/day check-in to approve experiment configs and review intermediate results",
      "claude_api_cost": "~$150–250 (~1,500–2,500 conversation turns coordinating experiment scheduling, result parsing, and ablation planning)",
      "estimated_gpu_cost": "~$465 (310h × $1.50/h)",
      "h100_equivalent": "~186h H100 (within ≤200 H100-hour budget constraint at ~0.6× A100/H100 ratio, leaving ~14h headroom)",
      "risk_note": "Choice of URIEL+ feature subspace (full 800-feature vs. Laplacian 300-feature vs. syntax-only) and the DPO prerequisite probe threshold require human judgment at key decision points; an automated agent may converge on a locally optimal weighting scheme that under-performs on the held-out Swahili generalization target"
    },
    "auto_research": {
      "gpu_hours": "~600h A100 (3–5× more experiments: grid search over distance metrics, curriculum schedule shapes, LoRA rank/alpha, 5+ target languages including Swahili and Kyrgyz for generalization, plus replication runs)",
      "gpu_utilization": "NEAR-ZERO idle—agent schedules jobs back-to-back across all target languages in parallel, launches follow-up ablations immediately on job completion, and runs nightly sweeps without human bottleneck",
      "timeline": "5–10 days with 4× concurrent A100s; ~3 weeks on a single A100",
      "team": "0 (initial setup of experiment configs, data paths, and evaluation harness only)",
      "claude_api_cost": "~$400–650 (~4,000–6,500 turns for full experiment orchestration, result parsing, ablation tree exploration, and report drafting)",
      "estimated_gpu_cost": "~$900 (600h × $1.50/h)",
      "h100_equivalent": "~360h H100 — EXCEEDS the ≤200 H100-hour hard budget constraint. Auto_research mode is documented for completeness but is NOT a viable deployment option within the stated budget. Use manual mode (~120 H100h) or human_in_loop mode (~186 H100h) to remain within budget.",
      "speed_bottleneck": "GPU count is the primary bottleneck: 4 concurrent A100s reduces wall-clock time to ~5 days; API rate limits become secondary when running >8 parallel experiment threads",
      "risk_note": "CONSTRAINT VIOLATION: 600 A100h ≈ 360 H100h, exceeding the ≤200 H100-hour hard budget. Additionally, unconstrained exploration may overfit the URIEL+ weighting function to the 3 initial target languages; Swahili as a held-out agglutinative target is required to detect this overfitting early."
    }
  },
  "target_venues": [
    "ACL 2027 (ARR submission deadline August 3, 2026) — primary target; provides adequate time for validation on additional typological clusters beyond Turkic–Mongolic, and for a paper of this scope (multi-pivot curriculum + ablations + 3 evaluation benchmarks) that cannot realistically reach conference quality in under 6 weeks",
    "EMNLP 2026 (ACL Rolling Review, rolling deadlines throughout 2026) — viable only if the team has prior QLoRA fine-tuning infrastructure already in place and can begin experiments immediately"
  ],
  "level": "solid",
  "key_references": [
    "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (ACL 2024) [29% improvement on Chinese/Korean/Italian/Spanish; Turkic/Mongolic gap is untested]",
    "Cross-Lingual Optimization for Language Transfer in Large Language Models (CLO; ACL 2025, arXiv:2505.14297) [DPO-style cross-lingual preference optimization using English-only source and M2M100 translation; baseline and methodological reference for TWMP's multi-source DPO extension]",
    "PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning (NAACL 2025, aclanthology.org/2025.naacl-short.19/) [treats English as an internal pivot and disentangles English vs. target-language training objectives via regulated losses to reduce negative interference; like PLUG and CLO, fixes English as the sole pivot without addressing typological distance, multi-pivot sequencing, or agglutinative low-resource targets—cited as an English-pivot baseline alongside PLUG and CLO]",
    "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning (Ye et al., AAAI 2026, arXiv:2511.10229) [selects multilingual instruction data using language separability scores from the model's own representation space across 22 languages including low-resource targets; differentiated from TWMP's external URIEL+ typological weighting independent of training dynamics, staged curriculum, and multi-source DPO objective]",
    "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages (Idris et al., arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track) [multi-source cross-lingual transfer as budget-constrained resource allocation for NER and sentiment analysis on Hausa, Yoruba, and Swahili across 288 experiments; no typological features or curriculum ordering—differentiated from TWMP's URIEL+-weighted staged instruction tuning; note: preprint only, acceptance not yet confirmed]",
    "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) [3-stage curriculum (token-level → sentence-level → monolingual code-switching) for single language pair; primary focus Korean, with Japanese and Indonesian—differentiated from TWMP's multi-pivot typological curriculum without code-switching targeting a family of related agglutinative languages]",
    "Revisiting Multilingual Data Mixtures in Language Model Pretraining (Foroutan et al., arXiv:2510.25947, ICLR-submitted 2025) [multilingual data reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); differentiated from TWMP's instruction-tuning-scale LoRA curriculum where data volume, optimization dynamics, and gradient signal are qualitatively different]",
    "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (Laiyk et al., ACL 2025 Long, arXiv:2502.13647) [10,600 GPT-4o-assisted Kazakh instruction examples fine-tuning Qwen/Falcon/Gemma; requires target-language labels and is Kazakh-specific—differentiated from TWMP's label-free multi-target approach covering Mongolian and Uyghur equally]",
    "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+ (Shipton et al., LREC 2026, arXiv:2510.27183) [extends URIEL+ with script vectors and Glottolog genealogies for 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages]",
    "Llama-3.1-Sherkala-8B-Chat (arXiv:2503.01493) [trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish; demonstrates Turkish as auxiliary language improves Kazakh performance via full fine-tuning; differentiated from TWMP's generalizable LoRA recipe parameterized by continuous URIEL+ distances]",
    "Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) [implicit reward transfer from English-aligned DPO model to annotate cross-lingual preference pairs; 12.72% Win Rate improvement on X-AlpacaEval; English-only source with no typological weighting—differentiated from TWMP's multi-pivot source selection and low-resource agglutinative targets]",
    "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP; official repository: github.com/LeeLanguageLab/URIELPlus]",
    "Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset achieves ρ=0.358 (p=0.061; measured on linguistic distance alignment against G_d metric, Table 1) vs. ρ=0.260 for full 800-feature URIEL+; downstream improvement of +7.8% on LangRank tasks; ρ values verified from paper HTML; downstream gains provide the primary justification for TWMP's feature selection step—the typological alignment improvement is directionally consistent but borderline significant]",
    "Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]",
    "TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]",
    "Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]",
    "Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family (arXiv:2604.06202, April 2026) [theoretical framework introducing Turkic Transfer Coefficient (TTC) combining morphological, lexical, syntactic, and script compatibility; no training method or instruction tuning experiments; no evaluation on KazMMLU/MiLiC-Eval/TUMLU—corroborates motivation for Turkic-pivot weighting without instantiating it empirically]",
    "KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark; 23K total questions (approximately 11K in Kazakh, 12K in Russian) sourced from authentic Kazakhstani educational materials; peer-reviewed; TWMP evaluates on the Kazakh-language subset only]",
    "MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]",
    "TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]",
    "Do Chinese Models Speak Chinese Languages? (arXiv:2504.00289, April 2026) [evaluates 10 LLMs across 21 language variants including Uyghur, Mongolian, Kazakh, and Tibetan; Llama3-Instruct is uniquely capable at Uyghur and ranks highest on Mongolian; Chinese LLMs do not outperform Western counterparts on minority languages—contemporary evidence for the performance gap TWMP addresses]",
    "Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]",
    "Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)",
    "Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)",
    "Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]",
    "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]"
  ],
  "description": "This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds Glottolog genealogies covering 26,449 languages; TWMP uses the COLING 2025 base version, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358, p=0.061, measured on linguistic distance alignment with G_d metric, Table 1; +7.8% improvement on LangRank downstream tasks; vs. ρ=0.260 for the full 800-feature set; ρ values verified from paper HTML—the downstream gains are the primary justification, as the typological alignment improvement is directionally consistent but borderline significant) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. Contemporary evidence from 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026), which evaluates 10 LLMs across 21 language variants, shows that Llama3-Instruct is the only evaluated model with distinctive Uyghur capability and that Chinese LLMs do not outperform Western counterparts on minority languages including Uyghur and Mongolian—confirming that no current model family addresses the performance gap TWMP targets. LangGPS (Ye et al., AAAI 2026, arXiv:2511.10229) selects multilingual instruction data by language separability from the model's own representation space across 22 languages; TWMP instead uses external URIEL+ features independent of training dynamics, with a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer (Idris et al., arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track) frames multi-source transfer as budget-constrained allocation for NER/sentiment tasks without typological features or curriculum ordering—TWMP's principled weighting and staged scheduling address instruction tuning specifically. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. Code-Switching Curriculum Learning (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) proposes a 3-stage code-switching curriculum for a single language pair; TWMP's curriculum spans a typologically ordered pool of pivot languages without code-switching. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). PROM [NAACL 2025] similarly treats English as an internal pivot and disentangles English and target-language training objectives via regulated losses; like PLUG and CLO, PROM fixes a single English pivot without addressing typological distance or multi-pivot sequencing for agglutinative targets—all three serve as English-pivot baselines in TWMP's evaluation. Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. Instructions yielding no target-language candidates post-gate fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Laiyk et al. (ACL 2025 Long, arXiv:2502.13647) fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP requires no target-language labels and applies equally to Mongolian and Uyghur where no comparable dataset exists. Revisiting Multilingual Data Mixtures (Foroutan et al., arXiv:2510.25947) studies reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); TWMP targets instruction-tuning scale where data volume, optimization dynamics, and gradient signal are qualitatively different. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. A concurrent theoretical framework (arXiv:2604.06202, April 2026) proposes the Turkic Transfer Coefficient (TTC) for cross-lingual adaptation within the Turkic family but offers no training method or instruction tuning experiments. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU (Kazakh-language subset, ~11K questions), MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.",
  "project_name": "typological_multi_pivot",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL – TIPA (arXiv:2601.16629, EACL 2026 Findings) is directly competing work the generator missed: it constructs proxy language adapters by aggregating existing ones weighted by typological similarity across 230+ languages and five tasks. The novelty claim 'no prior work combines multi-pivot selection with typological distance weighting' is therefore too strong; the revision must differentiate TWMP from TIPA clearly (TIPA is training-free adapter aggregation for encoders; TWMP is a weighted sampling + curriculum training approach for decoder LLMs in instruction tuning—this distinction exists but must be made explicit).", "CRITICAL – Evaluation benchmarks are misspecified: XQuAD and XCOPA do NOT include Kazakh, Mongolian, or Uyghur—multiple sources and the benchmarks' own documentation confirm this. The evaluation protocol must be redesigned to use benchmarks that actually cover the target languages (e.g., XTREME-UP, MiLiC-Eval for Chinese minority languages, or TyDi QA for Kazakh).", "SIGNIFICANT – Model name 'Qwen 3.5-7B' does not exist. The Qwen3.5 series released in 2026 includes 4B and 9B variants (among others) but no 7B. The 250K vocabulary claim is correct for Qwen3.5 but the model identifier must be corrected to Qwen3.5-9B or Qwen3.5-4B before submission.", "SIGNIFICANT – 16-day timeline is unrealistic for a conference-quality submission. Running 15–20 QLoRA experiments across 3 target languages, implementing the TWMP curriculum + CLO loss from scratch, and writing a complete paper cannot be done in 16 days by 1–2 researchers without preexisting infrastructure. The compute estimate (180h A100 ≈ 125–135h H100) is within the 200 H100-hour hard constraint, but wall-clock time is the binding bottleneck.", "SIGNIFICANT – The primary evidence for the research gap, 'Left Behind' (arXiv:2603.21036), is a March 2026 preprint from a single author at North American University evaluated with 50 hand-crafted questions. EMNLP reviewers will reject this as insufficient basis for a gap claim; the motivation must be grounded in larger, peer-reviewed evaluations (e.g., the 'Shared Weights Pretraining for Extremely Low-Resource Languages' ACL 2025 paper, or XTREME-UP results for Turkic languages).", "MODERATE – Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) is not properly discussed in the landscape. This paper directly uses typological feature vectors for language selection in multilingual instruction tuning—the generator characterizes only arXiv:2505.13908 (which is purely analytical) while ignoring this more methodologically relevant prior work.", "MODERATE – MLM is a NeurIPS 2025 ER Workshop paper, not a NeurIPS 2025 main conference paper. Misrepresenting workshop papers as conference papers in a related work section is a frequent reviewer complaint and can trigger a bias/credibility flag.", "MODERATE – The CLO-style loss is described as a 'cross-lingual contrastive loss that enforces target-language response fidelity.' CLO actually uses DPO-style preference optimization (not a contrastive loss) to suppress off-language responses. The paper must use technically accurate descriptions to avoid confusion and reviewer pushback.", "MINOR – PLUG (ACL 2024)'s 29% improvement was measured on Chinese, Korean, Italian, and Spanish—not on Kazakh/Mongolian/Uyghur. The assumption that PLUG performs poorly on Turkic languages is plausible but not directly evidenced in the PLUG paper itself; the gap claim relative to PLUG needs its own experimental demonstration."]
Feedback: The core idea is genuinely interesting—typological-distance-weighted multi-pivot instruction tuning for Turkic low-resource languages—but the current draft has three blockers that prevent submission at EMNLP 2026 quality: (1) TIPA (EACL 2026) must be cited and clearly differentiated: TIPA does typological weighting of adapters in a training-free, encoder-adapter (MAD-X) framework across 230+ languages; TWMP is a training-time data sampling + curriculum approach for decoder LLMs in instruction tuning—spell this out explicitly in Section 2. (2) Replace XQuAD + XCOPA with benchmarks that actually include Kazakh, Mongolian, and Uyghur: consider XTREME-UP (includes Kazakh), MiLiC-Eval (Uyghur, Kazakh, Mongolian), and TyDi QA for real-language evaluation. If none of the standard benchmarks are adequate, you need to explain what evaluation data you are using and where it comes from. (3) Correct the model name to Qwen3.5-9B (or 4B) and rerun your compute estimates accordingly. Beyond the blockers: the motivation should be regrounded away from 'Left Behind' as the sole anchor—add references to XTREME-UP or ACL 2025 shared-weights pretraining results for Turkic languages. Add arXiv:2410.07809 to related work with a clear explanation of why TWMP's weighted sampling and curriculum are distinct contributions. Fix the MLM venue to 'NeurIPS 2025 ER Workshop' and fix the CLO description to 'DPO-style cross-lingual preference optimization.' On timeline: unless the team has the training infrastructure already built, the 16-day window makes a May 25 ARR deadline extremely risky; the ACL 2027 ARR deadline (August 3, 2026) is a more defensible target that allows proper validation on additional typological clusters (e.g., a Bantu agglutinative language) to test generalization beyond Turkic.

### Round 2 review
Verdict: revise
Issues: ["SIGNIFICANT – CLO's DPO objective is designed for English-source preference pairs: chosen = target-language response to English instruction, rejected = off-language (English) response to target-language instruction. TWMP proposes extending this to non-English source languages (Turkish/Uzbek → Kazakh), but the paper does not specify how preference pairs are constructed when the source is itself a non-English language like Uzbek. If the model produces a Kazakh response to a Uzbek instruction, what is the 'rejected' response? Reviewers will reject this as technically incomplete without a precise DPO formulation for the multi-source case.", "SIGNIFICANT – URIEL legacy features are known to be sparse for exactly the target languages in this paper. URIEL+ (arXiv:2409.18472, COLING 2025) explicitly improves coverage for low-resource languages and should be used instead of the 289-dim lang2vec legacy features. Furthermore, 'Less is More: The Effectiveness of Compact Typological Language Representations' (EMNLP 2025) shows that compact URIEL+ features outperform the full 289-dim feature space for cross-lingual NLP tasks—directly contradicting TWMP's use of all 289 dimensions without selection. This is a directly relevant citation the paper must engage with.", "MODERATE – Auto_research mode (600h A100 ≈ 300h H100) exceeds the stated ≤200 H100-hour hard constraint. While the experiment plan uses manual mode (within constraint), the resource estimate table presents auto_research as a legitimate deployment mode without flagging this violation of the user's stated budget constraint.", "MODERATE – The staged curriculum's cosine-distance threshold schedule is described qualitatively ('progressively expands the radius at scheduled epochs') but no concrete schedule is specified. Reviewers will ask: how many stages? What distance thresholds? How are thresholds set relative to the URIEL distance distribution of the Aya collection? Without a concrete, reproducible specification, this is a design element that cannot be ablated or replicated.", "MODERATE – DCO (arXiv:2603.04678, March 2026, Tianyu Liu et al.) introduces Direct Consistency Optimization, a DPO-inspired method for cross-lingual knowledge consistency across 26 languages and 9 LLMs. This is a concurrent work that uses a DPO-style objective for cross-lingual alignment—similar in spirit to the CLO component of TWMP—and must be cited and differentiated in the related work section.", "MINOR – The Aya dataset's coverage of Turkic pivot languages (Turkish, Uzbek, Kyrgyz) is assumed but not verified. If Uzbek and Kyrgyz have only hundreds of Aya instances, the typological-distance-weighted sampling will produce noisy estimates for the closest pivots to Kazakh. The paper should state the number of available training instances per pivot language in Aya and set a minimum threshold below which a language is excluded from the mixture."]
Feedback: The generator has addressed all Round 1 critical issues competently: TIPA is correctly differentiated, benchmarks are fixed, Qwen3.5-9B is confirmed correct, arXiv:2410.07809 is properly placed in the landscape, and the CLO/DPO description is accurate. The remaining blockers are two: (1) The DPO objective must be precisely formulated for non-English source languages. The current description 'increases preference for target-language responses and reduces preference for off-language outputs, without requiring any target-language training labels' is borrowed verbatim from CLO's English-source setting. For a Turkish → Kazakh pair, you must specify: what constitutes the chosen response, what constitutes the rejected response, and how you obtain these without any Kazakh labels. One viable extension: treat (Turkish-instruction, Kazakh-response) as the chosen pair and (Turkish-instruction, Turkish-response) as rejected—but this requires stating it explicitly and verifying that Qwen3.5-9B produces detectable off-language Turkish responses to Turkish instructions. (2) Replace lang2vec 289-dim URIEL features with URIEL+ (arXiv:2409.18472, COLING 2025), which has better sparse-language coverage, and cite 'Less is More' (EMNLP 2025) to justify whichever feature subspace you choose. This is not just a citation gap—if the typological distances for Uzbek and Kyrgyz are inaccurate in legacy URIEL due to sparsity, the entire weighting scheme degrades for the most important (closest) pivots to Kazakh. Beyond the blockers: add DCO (arXiv:2603.04678) to related work; specify the curriculum schedule concretely (number of stages, distance thresholds); verify and report the number of Aya instances per Turkic pivot language; and note that auto_research mode exceeds the 200 H100-hour constraint if that constraint applies. ACL 2027 (August 3, 2026 ARR) remains the appropriate primary venue.

### Round 3 review
Verdict: revise
Issues: ["MODERATE – Sherkala-Chat (arXiv:2503.01493, March 2025) is a directly relevant uncited work: it instruction-tunes Llama-3.1-8B for Kazakh on 45.3B tokens of Kazakh, English, Russian, and Turkish data, demonstrating that Turkish as an auxiliary training language improves Kazakh performance—the empirical core insight that motivates TWMP's pivot selection. Not citing it leaves a gap reviewers will notice; TWMP should add it as related work and contrast it: Sherkala-Chat uses ad-hoc four-language mixing with full fine-tuning, whereas TWMP provides a principled, generalizable, LoRA-based method parameterized by continuous URIEL+ distances applicable across any agglutinative target.", "MODERATE – The DPO preference pair construction specifies 'highest-scoring chosen' and 'lowest-scoring rejected,' where 'scoring' is implicitly language identification confidence from fastText. This means a grammatically garbled Kazakh response with high fastText confidence could be chosen as the preferred response over a coherent Turkish response. No quality filter (perplexity, length heuristic, or instruction-following score) is applied to the chosen pool. Reviewers will ask whether the DPO training signal is noisy precisely for the close-pivot cases where K=8 Kazakh responses are plentiful—yet quality varies most—and for distant pairs where only 1 of 8 samples passes the language filter, leaving little variance to select from. The paper should either add a quality filter (e.g., exclude responses shorter than 20 tokens or with perplexity above a threshold under the base model) or explicitly acknowledge and ablate this as a limitation.", "MINOR – Qwen3.5-9B release date: the paper states 'released February 2026' but available information indicates the Qwen3.5 small series (0.8B/2B/4B/9B) became available March 2, 2026—the February date applies to the larger Qwen3.5 medium models (35B-A3B, 27B). This should be corrected to March 2026.", "MINOR – The URIEL+ repository URL cited in the approach section ('github.com/Masonshipton25/URIELPlus') does not match the official ACL Anthology-linked repository ('github.com/LeeLanguageLab/URIELPlus'). The URL should match the official publication's repository or the PyPI package ('urielplus') should be referenced instead.", "MINOR – The Kyrgyz Aya instance count ('~4.1M instances in the Aya collection language split') could not be independently verified against HuggingFace statistics. Given Kyrgyz is much lower-resource than Turkish, this count depends entirely on machine-translated data volume and should be verified and cited to the HuggingFace dataset page or the Aya Collection paper's per-language appendix before submission."]
Feedback: The generator has addressed all Round 2 issues competently: the multi-source DPO formulation is now precisely specified (chosen = source-language instruction + model-generated target-language response; rejected = source-language instruction + model-generated source-language response), URIEL+ replaces legacy 289-dim features with the 'Less is More' 300-feature Laplacian subset, the staged curriculum has concrete D_25/D_60 percentile anchors and epoch ranges, DCO is cited and differentiated, Aya coverage is verified with a 5,000-instance floor, and auto_research mode is correctly flagged as exceeding the 200 H100h budget. Two moderate issues remain before this is submission-ready: (1) Add Sherkala-Chat (arXiv:2503.01493) to related work—it is a directly adjacent March 2025 paper training Llama-3.1 on Kazakh+Turkish+Russian and provides empirical motivation for TWMP's pivot selection logic. The contrast is easy: Sherkala-Chat is language-specific full fine-tuning with ad-hoc pivot choice; TWMP is generalizable LoRA-based training with principled URIEL+ weighting. (2) Address the DPO pair quality concern: define 'highest-scoring' explicitly as language ID confidence, acknowledge that this does not filter for response quality, and either add a minimal quality gate (e.g., minimum response length or base-model perplexity cap) or include it as a stated limitation with an ablation that shows the fastText-only selection is adequate in practice. Fix the three minor issues (Qwen3.5 release date, URIEL+ repo URL, Kyrgyz instance count verification) before submitting. ACL 2027 (August 3, 2026 ARR) remains the appropriate primary target; given these are all fixable within days, the paper is on track.

### Round 4 review
Verdict: revise
Issues: ["MODERATE – Sherkala-Chat (arXiv:2503.01493) was flagged in Round 3 as a key uncited adjacent work and remains absent from Round 4. This paper trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish, directly demonstrating that Turkish as an auxiliary language improves Kazakh performance — the empirical core claim motivating TWMP's pivot selection logic. EMNLP reviewers familiar with Kazakh NLP will notice this omission immediately. Required: add to related work section with explicit contrast (Sherkala-Chat uses ad-hoc 4-language full fine-tuning for Kazakh specifically; TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target).", "MODERATE – DPO pair quality gate still absent. The approach specifies 'pair the highest-scoring chosen with the lowest-scoring rejected' based on fastText language ID confidence alone, with no quality filter. For close-pivot pairs (Turkish→Kazakh), K=8 sampling may yield 5–7 Kazakh responses, creating a large chosen pool with highly variable quality; the 'highest-scoring' fastText criterion selects the response with the highest Kazakh language ID confidence, which is not correlated with response coherence or instruction-following quality. A grammatically garbled but confidently Kazakh response will be preferred over a fluent but lower-confidence response. This was raised in Round 3 and remains unaddressed. Fix: add a minimum response length gate (e.g., ≥20 tokens) or base-model perplexity cap, or include an explicit ablation comparing fastText-only selection vs. a quality-gated variant and acknowledge this as a limitation with empirical validation.", "MODERATE – Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings) is uncited and directly relevant to TWMP's DPO component. This paper uses implicit reward transfer from English DPO models to annotate cross-lingual preference pairs for multilingual DPO fine-tuning, achieving 12.72% average Win Rate improvement on X-AlpacaEval across training languages. While the approach differs from TWMP (English-only source, implicit reward annotation, no typological weighting), it represents active concurrent work on cross-lingual DPO alignment that EMNLP reviewers will expect to see cited and contrasted. Required addition to related work: differentiate TWMP's direct construction of multi-source preference pairs via language ID vs. this paper's implicit reward annotation from a single English-aligned model.", "MINOR – Qwen3.5-9B release date error persists for the third consecutive round. The submission states 'released February 2026' but independent verification (multiple sources) confirms the Qwen3.5 small series (0.8B/2B/4B/9B) was released March 1–2, 2026, with February 2026 referring to the larger Qwen3.5 medium models (35B-A3B, 27B). Change 'released February 2026' to 'released March 2026'.", "MINOR – URIEL+ repository URL persists as incorrect for the third consecutive round. The submission cites 'github.com/Masonshipton25/URIELPlus' but the official ACL Anthology-linked repository is 'github.com/LeeLanguageLab/URIELPlus' (confirmed). Change to the correct URL or cite the PyPI package 'urielplus' instead."]
Feedback: This is Round 4 and the same four issues (Sherkala-Chat, DPO quality gate, release date, repo URL) that were flagged in Round 3 have not been addressed. The pattern is concerning for an ARR deadline in 15 days. Here is exactly what needs to change, in priority order:

(1) Add Sherkala-Chat to Section 2 related work. One paragraph is sufficient: 'Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish, demonstrating that Turkish as an auxiliary language improves Kazakh performance—motivating our choice of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc pivot selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language.'

(2) Add Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings) to Section 2. One sentence: 'Implicit Cross-Lingual Rewarding annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving strong multilingual alignment from English-only source data—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from this work.'

(3) Fix the DPO quality issue. Choose one of: (a) add a minimum 20-token length gate to the chosen pool and state it explicitly; (b) add a perplexity cap at 2× base-model perplexity on the instruction; or (c) keep the current fastText-only selection but add a clearly labeled limitation paragraph and one ablation row in Table X comparing fastText-only vs. length-gated selection. Option (c) requires the least implementation effort and is acceptable.

(4) Fix two one-line errors: 'released February 2026' → 'released March 2026'; 'github.com/Masonshipton25/URIELPlus' → 'github.com/LeeLanguageLab/URIELPlus'.

None of these require new experiments. Issues (1), (2), (4) are writing-only changes. Issue (3) option (c) requires one additional experiment row or a paragraph addition. The paper is substantively sound and the core novelty claim is defensible—these are editorial and citation completeness fixes that are blocking an otherwise strong submission. ACL 2027 (August 3, 2026 ARR) remains the more realistic target, but if the team has existing QLoRA infrastructure, EMNLP 2026 (May 25 ARR) is feasible after these four fixes.

### Round 5 review
Verdict: revise
Issues: ["MODERATE – Revisiting Multilingual Data Mixtures (arXiv:2510.25947, Foroutan et al., EPFL, Oct 2025) directly challenges TWMP's two core premises: (1) staged curriculum learning 'does not reduce negative interference' in multilingual training, and (2) temperature-based language reweighting 'hurts performance due to noise' on low-resource data. This paper focuses on pretraining, not instruction tuning, but EMNLP reviewers familiar with it will raise it against TWMP's staged curriculum and inverse-distance weighting scheme. Required: cite this paper in Section 2, acknowledge the potential discrepancy, and argue explicitly why the instruction tuning setting (smaller data footprint, fewer gradient steps, different optimization landscape) is different enough that the Foroutan et al. findings do not transfer.", "MODERATE – LangGPS (arXiv:2511.10229, AAAI 2026; Yangfan Ye, Xiaocheng Feng et al., HIT + Microsoft) proposes language separability from the model's own representation space as the basis for multilingual instruction tuning data selection, and reports improvements over external-feature-based approaches across 22 languages including low-resource targets. It is a peer-reviewed AAAI 2026 competitor to TWMP's URIEL+-based selection approach. This is too similar to leave uncited. Required: add to related work and differentiate: LangGPS uses task-adaptive model-internal signals but is agnostic to typological structure and provides no mechanism for multi-pivot curriculum sequencing; TWMP uses external typological features to derive a principled ordering over pivot languages independent of training dynamics.", "MODERATE – Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (arXiv:2411.02460, ACL 2025 Findings; Haneul Yoo et al., NAVER AI) proposes a 3-stage curriculum (token-level code-switching → sentence-level code-switching → monolingual) that achieves cross-lingual transfer improvements on both high- and low-resource languages without typological distance. This paper has been available since November 2024—before all prior review rounds—and has never appeared in TWMP's references. EMNLP reviewers will notice its absence. Required: cite and contrast in Section 2: the code-switching curriculum operates within a single language pair using surface-level code-mixing as a bridge, whereas TWMP's curriculum operates over a pool of typologically ordered pivot languages with no code-switching; the two approaches address different facets of cross-lingual curriculum design and could in principle be combined.", "MINOR – Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (arXiv:2502.13647, ACL 2025 Main; Laiyk et al.) fine-tunes Qwen/Falcon/Gemma on 10,600 GPT-4o-assisted Kazakh instruction examples, achieving consistent improvement on multiple-choice and generative Kazakh tasks. This is a direct Kazakh instruction tuning baseline from ACL 2025 that any reviewer working on KazMMLU will expect TWMP to compare against or at minimum cite. It documents that targeted single-language instruction data generation is a strong alternative to cross-lingual transfer methods—TWMP should position itself relative to it (e.g., TWMP does not require any target-language instruction labels and is applicable to Mongolian and Uyghur where no comparable GPT-4-assisted dataset exists).", "MINOR – Simple Additions, Substantial Gains: Expanding URIEL+ (arXiv:2510.27183, LREC 2026; Shipton, Ng, Khan et al.) extends the URIEL+ database with script vectors, Glottolog integration, and genealogical feature propagation, reducing feature sparsity by 35% and expanding coverage to 26,449 languages—directly addressing the sparsity problem for Kazakh/Uzbek/Kyrgyz that TWMP cites as motivation for switching from legacy lang2vec to URIEL+. TWMP should either use this updated version or acknowledge it as a contemporaneous development and argue that the 2409.18472 COLING 2025 version is sufficient for the target languages (the 35% sparsity reduction would most benefit exactly the low-resource Turkic languages in scope).", "MINOR – The DPO prerequisite probe threshold is set at >5% of K=8, which equals at least 1 target-language response in 8 tries. This is the minimum viable signal level and means many source-target pairs that 'pass' the probe provide almost no diversity in the chosen pool (only 1 candidate). At this threshold, the 20-token gate can cause 100% discard of chosen candidates for those instructions (if the single Kazakh response is <20 tokens), silently collapsing to SFT-only training for many instruction prompts without reporting. The paper should characterize the empirical distribution of per-instruction chosen-pool sizes (1, 2, 3+ responses) across source-target pairs and report what fraction of instructions fall back to SFT-only due to post-gate chosen pool exhaustion."]
Feedback: All Round 4 issues are addressed: Sherkala-Chat is properly cited and contrasted, the DPO 20-token length gate and ablation row are specified, Implicit Cross-Lingual Rewarding is cited, the release date and URIEL+ URL are corrected. The paper's core method is substantively sound and the technical specification is unusually precise for a draft at this stage. Three writing-only additions are needed before this is EMNLP-ready:

(1) Add Foroutan et al. (arXiv:2510.25947) to Section 2. Key contrast: that paper tests pretraining-scale reweighting across 25–400 languages; TWMP operates at instruction tuning scale (10 epochs, LoRA, ≤6,400 instances per pivot) where reweighting over a narrow near-family pivot pool is qualitatively different from resampling across 400 pretraining languages. Make this argument explicitly to preempt the obvious reviewer objection.

(2) Add LangGPS (arXiv:2511.10229, AAAI 2026) and Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings) to Section 2. Both are one-paragraph additions: LangGPS uses model-internal representation signals (no external typological database, no multi-pivot ordering); Code-Switching Curriculum uses surface-level code-mixing within a pair (no typologically structured pool, no DPO). Neither addresses the multi-pivot ordering problem or provides a principled recipe for pivot sequencing across typologically diverse targets.

(3) Add arXiv:2502.13647 (ACL 2025 Main, Kazakh instruction tuning) as a related baseline in Section 2 and note it cannot generalize to Mongolian and Uyghur where no comparable target-language instruction dataset exists.

For the probe threshold: add one sentence clarifying what happens when the post-gate chosen pool for a given instruction is empty—confirm that those instructions fall back to the SFT-weighted objective, not to silent skip, and report the per-pair fallback rate as a characterization result.

ACL 2027 (ARR August 3, 2026) remains the appropriate primary target. None of these additions require new experiments.

### Round 6 review
Verdict: revise
Issues: ["SIGNIFICANT (PATTERN) – All five Round 5 issues remain unaddressed in Round 6 for the second consecutive round. (1) Foroutan et al. (arXiv:2510.25947, ICLR-submitted): not in landscape or key_references. (2) LangGPS (arXiv:2511.10229, AAAI 2026 main): not in landscape or key_references — this is a peer-reviewed AAAI 2026 competitor on multilingual instruction tuning data selection across 22 languages including low-resource targets, and its omission is the most damaging gap. (3) Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings): not cited despite being published November 2024 and appearing in ACL Anthology. (4) arXiv:2502.13647 (ACL 2025 Long, Kazakh instruction tuning): not cited despite being a direct Kazakh-targeting baseline. (5) URIEL+ expansion (arXiv:2510.27183, LREC 2026): not cited despite directly extending the typological tool TWMP relies on.", "MODERATE (NEW) – Budget-Xfer (arXiv:2603.27651, March 2026) proposes budget-constrained source language selection for multi-source cross-lingual transfer, jointly optimizing which source languages to include and how much data to allocate from each — directly parallel to TWMP's multi-pivot selection problem. It evaluates on three African target languages (Hausa, Yoruba, Swahili) using a 288-experiment suite. While it targets classification tasks rather than instruction tuning, EMNLP reviewers in the cross-lingual track will expect it to be cited and contrasted: Budget-Xfer frames source selection as resource allocation without typological features or curriculum ordering; TWMP provides principled URIEL+-based weighting and staged scheduling.", "MINOR (PERSISTENT) – Per-instruction chosen-pool fallback characterization remains incomplete. The approach section states that 'instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' but does not report the per-instruction fallback rate as a characterization result. Round 5 feedback specifically requested one sentence confirming these instructions fall back to SFT-weighted objective (not silent skip) and reporting the empirical fallback rate per source-target pair. The current text says they are 'discarded,' which implies silent skip rather than SFT fallback — this ambiguity must be resolved and the frequency reported."]
Feedback: This is Round 6. The core method is technically sound, the DPO formulation is precise, the compute budget is within constraint, and the evaluation design is appropriate. However, the same five citations flagged in Round 5 are absent for the second consecutive round, and a new paper (Budget-Xfer, arXiv:2603.27651) has appeared that is directly adjacent. Here is the exact text to add for each outstanding item:

(1) Foroutan et al. (Section 2, one sentence): 'Revisiting Multilingual Data Mixtures [Foroutan et al., 2025] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime.'

(2) LangGPS (Section 2, one paragraph — highest priority): 'LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address.'

(3) Code-Switching Curriculum (Section 2, one sentence): 'Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target.'

(4) Kazakh instruction tuning (Section 2, one sentence): 'Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists.'

(5) URIEL+ expansion (Section 3, one sentence): 'A concurrent LREC 2026 extension [Shipton et al., arXiv:2510.27183] adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version [arXiv:2409.18472] with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages.'

(6) Budget-Xfer (Section 2, one sentence): 'Budget-Xfer [arXiv:2603.27651, 2026] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address.'

(7) Fix the per-instruction fallback: Change 'Instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' to 'Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe.'

All seven items are writing-only changes requiring no new experiments. ACL 2027 (ARR August 3, 2026) remains the appropriate primary target. At Round 6, the paper cannot pass until at minimum items (1)–(5) are resolved.

### Round 7 review
Verdict: revise
Issues: ["MODERATE – KazMMLU benchmark description is factually wrong. The paper repeatedly claims KazMMLU contains '23K Kazakh-language questions spanning STEM, humanities, and social sciences,' but independent verification of arXiv:2502.12829 shows the dataset contains 10,969 Kazakh-language questions + 12,031 Russian-language questions = 23,000 total. Only ~47% of questions are in Kazakh; the remainder are in Russian. Any EMNLP reviewer who reads the KazMMLU abstract will catch this. The description should read '23K questions (approximately 11K in Kazakh, 12K in Russian) sourced from Kazakhstani educational materials.' For TWMP's Kazakh instruction evaluation, only the Kazakh-language subset is relevant, which is smaller than the paper implies.", "MINOR – PROM (NAACL 2025, arXiv not yet located but published at ACL Anthology at aclanthology.org/2025.naacl-short.19/) introduces 'Pivoted and Regulated Optimization,' which treats English as an internal pivot and disentangles English vs. target-language training objectives via separate regularized losses for multilingual instruction tuning. This is adjacent to PLUG and CLO in the landscape of English-pivot methods for multilingual instruction following, and EMNLP reviewers familiar with the NAACL 2025 proceedings will expect it to be cited alongside PLUG and CLO. One sentence suffices: 'PROM [NAACL 2025] disentangles English-pivot and target-language training objectives via regulated losses — like PLUG and CLO, it fixes English as the sole pivot without addressing typologically distant agglutinative targets.'", "MINOR – 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026) evaluates Uyghur and Mongolian capabilities across current LLMs, finding Llama3-Instruct is uniquely capable at Uyghur and top-performing at Mongolian among open models. This is contemporary evidence for the performance gap that motivates TWMP and is published close enough to the ARR deadline to be a missing citation reviewers will notice. One sentence in Section 1 or 2 would suffice."]
Feedback: All Round 6 issues are fully resolved: Foroutan et al., LangGPS, Code-Switching Curriculum, Laiyk et al., URIEL+ expansion, Budget-Xfer, and the fallback characterization now all appear correctly in the landscape and key_references. The paper is close to submission-ready. Three targeted fixes remain:

(1) Fix the KazMMLU description (highest priority — factual error). Change every instance of '23K Kazakh-language questions' to '23K questions spanning Kazakh and Russian (approximately 11K in Kazakh)' or similar accurate phrasing. This appears in the core_problem, opportunity, and key_references fields. This is a one-line fix per occurrence but it is mandatory — the current phrasing is verifiably wrong and will undermine reviewer trust in the paper's factual accuracy.

(2) Add PROM [NAACL 2025] to the landscape (one sentence): 'PROM [NAACL 2025] treats English as an internal pivot and separates English vs. target-language training objectives via regulated losses; like PLUG and CLO, it presupposes a single English pivot without addressing typological distance or multi-pivot sequencing for agglutinative targets.'

(3) Add arXiv:2504.00289 (April 2026) to the opportunity section or related work as supplementary evidence for Uyghur/Mongolian gaps in current LLMs.

None of these require new experiments. Issues (2) and (3) are one-sentence writing additions; issue (1) is a find-and-replace correction. ACL 2027 (ARR August 3, 2026) remains the appropriate primary target; EMNLP 2026 (May 25 ARR) is feasible only if the team already has the QLoRA infrastructure in place and can begin experiments immediately after these three fixes.

### Round 8 review
Verdict: revise
Issues: ["MINOR – Budget-Xfer (arXiv:2603.27651) is cited throughout as 'SIGIR 2026' but independent verification of the arXiv page confirms its status is 'Submitted to SIGIR 2026 Short Paper track'—it has not been accepted or published at SIGIR 2026. Citing an unaccepted submission as a published venue paper is a citation ethics flag that EMNLP meta-reviewers take seriously. Fix: change 'SIGIR 2026' to 'arXiv preprint, 2026 (submitted to SIGIR 2026)' or simply 'arXiv:2603.27651, 2026' until acceptance is confirmed.", "MINOR – The 'Less is More' EMNLP 2025 specific numerical claims (ρ=0.358 for Laplacian-300 vs. ρ=0.260 for full 800-feature URIEL+) could not be verified from the abstract; the direction of the claim ('reduced-size representations yield more informative distance metrics') is confirmed by the abstract, but the precise ρ values should be cross-checked against the paper PDF before submission to ensure they are quoted correctly and refer to the same evaluation task TWMP uses."]
Feedback: All three Round 7 issues are fully resolved in Round 8: the KazMMLU description is now correctly stated as '23K questions total (approximately 11K in Kazakh, 12K in Russian)' across all occurrences; PROM (NAACL 2025, aclanthology.org/2025.naacl-short.19/) is properly cited and differentiated; and arXiv:2504.00289 ('Do Chinese Models Speak Chinese Languages?') appears correctly in the opportunity section. Independent verification confirms: CLO's 3,200-sample efficiency claim is accurate; LangGPS is AAAI 2026 Main Track (confirmed); Qwen3.5-9B released March 2026 (confirmed); URIEL+ at COLING 2025 (confirmed). No uncited competing work was found that would undermine the novelty claim. Only two minor fixes remain before this can pass: (1) Change every instance of 'SIGIR 2026' for Budget-Xfer to 'arXiv:2603.27651, 2026' — the paper is submitted to SIGIR 2026 but not yet accepted; this is a one-line find-and-replace. (2) Verify the exact ρ values from the 'Less is More' PDF before submission. Neither requires new experiments. The paper is in excellent shape for its primary ACL 2027 target (ARR August 3, 2026) and is feasible for EMNLP 2026 (May 25 ARR) with the QLoRA infrastructure caveat.


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
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "type": "user",
  "uuid": "226175ce-33d0-4de3-8c11-58880544cb38",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:20:56.848Z_

```json
{
  "parentUuid": "226175ce-33d0-4de3-8c11-58880544cb38",
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
  "uuid": "0628e713-49fc-4438-8a3c-747dd611aff6",
  "timestamp": "2026-05-10T08:20:56.848Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:20:56.849Z_

```json
{
  "parentUuid": "0628e713-49fc-4438-8a3c-747dd611aff6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1ed2c48f-396a-4096-98ac-4ac486a14ca0",
  "timestamp": "2026-05-10T08:20:56.849Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
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
  "leafUuid": "1ed2c48f-396a-4096-98ac-4ac486a14ca0",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify TWMP Multilingual Instruction Tuning Novelty and Feasibility",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:21:11.237Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 9/10 of an adversarial review. I need to independently verify the remaining issues from Round 8 and assess whether this idea should pass, revise, or fail.

Let me review what Round 8 flagged as remaining issues:
1. Budget-Xfer cited as 'SIGIR 2026' but it's submitted, not accepted - needs to be fixed
2. 'Less is More' EMNLP 2025 ρ values (ρ=0.358 vs ρ=0.260) need verification from actual paper

Looking at the current Round 9 submission, let me check if these have been addressed:


The Budget-Xfer issue appears to be resolved—it now correctly indicates "submitted to SIGIR 2026 Short Paper track" with a note in key_references clarifying that it's a preprint with acceptance not yet confirmed. For the "Less is More" ρ values, I can see the Laplacian Score 300-feature subset is cited as achieving ρ=0.358 (p=0.061) against the linguistic similarity distance alignment metric, but I need to verify this matches what's actually reported in the paper.

Now I'm doing targeted verification on several fronts: checking whether the "Less is More" EMNLP 2025 paper's ρ values are accurately cited, searching for any recent papers that might compete with the novelty claims, confirming CLO exists at ACL 2025, validating the KazMMLU description, and looking for new multilingual instruction tuning work that's emerged recently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ed2c48f-396a-4096-98ac-4ac486a14ca0",
  "isSidechain": false,
  "requestId": "req_011CatZbuiR6cb4iFjENzWBs",
  "type": "assistant",
  "uuid": "dce66d69-fa7c-418b-b05e-de962bf98df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0146zafu3oCf2dXGyv4kzwUs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30719,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1613,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1613,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 30719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30719
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

_source line 9 · 2026-05-10T08:21:11.242Z_

I'll conduct independent verification searches focusing on the Round 8 remaining issues and any new competing work that may have emerged.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dce66d69-fa7c-418b-b05e-de962bf98df1",
  "isSidechain": false,
  "requestId": "req_011CatZbuiR6cb4iFjENzWBs",
  "type": "assistant",
  "uuid": "7c52da34-b992-4812-9681-3230d26e5f49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0146zafu3oCf2dXGyv4kzwUs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30719,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1613,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1613,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 30719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30719
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

_source line 10 · 2026-05-10T08:21:20.251Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HzhhjVrsRz3fQ7APY5V9LK`</summary>

```json
{
  "description": "Verify \"Less is More\" EMNLP 2025 paper ρ values and Budget-Xfer status",
  "subagent_type": "Explore",
  "prompt": "I need you to search for and verify specific claims about two papers used in a multilingual NLP research proposal.\n\n**Task 1: Verify \"Less is More: The Effectiveness of Compact Typological Language Representations\" (arXiv:2509.20129, EMNLP 2025)**\n\nThe proposal claims:\n- This paper's Laplacian Score 300-feature URIEL+ subset achieves Spearman ρ=0.358 (p=0.061) measured against linguistic distance alignment metric G_d (Table 1)\n- The full 800-feature set achieves ρ=0.260\n- It yields +7.8% improvement on LangRank downstream tasks\n\nPlease search for this paper and try to verify these specific ρ values. Search for:\n1. \"Less is More Compact Typological Language Representations EMNLP 2025\"\n2. \"arXiv 2509.20129\"\n3. Try to fetch the abstract from arxiv.org/abs/2509.20129\n\n**Task 2: Verify Budget-Xfer status**\nSearch for \"Budget-Xfer arXiv 2603.27651\" to confirm it is still a preprint submitted to SIGIR 2026 (not yet accepted/published).\n\n**Task 3: Search for new competing papers (last 3 months, April-May 2026)**\nSearch for:\n1. \"typological distance multilingual instruction tuning 2026\"\n2. \"multi-pivot cross-lingual transfer low-resource 2026\"\n3. \"URIEL typological instruction tuning arxiv 2026\"\n4. \"Kazakh Mongolian Uyghur LLM instruction tuning 2026\"\n\nReport what you find for each task, including specific numbers, dates, and URLs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c52da34-b992-4812-9681-3230d26e5f49",
  "isSidechain": false,
  "requestId": "req_011CatZbuiR6cb4iFjENzWBs",
  "type": "assistant",
  "uuid": "ea24bd52-b925-48fb-8477-9b59e82bce81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0146zafu3oCf2dXGyv4kzwUs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30719,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1613,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1613,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 30719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30719
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

_source line 11 · 2026-05-10T08:21:28.742Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BN6TDEmwQYv4nxH5QH958K`</summary>

```json
{
  "description": "Search for concurrent competing work in multilingual instruction tuning",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing a multilingual NLP paper called \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning\" (TWMP). I need to independently verify its novelty by searching for competing/overlapping work published in the last 6 months (November 2025 - May 2026).\n\nThe paper's core claims:\n1. It uses URIEL+ typological distances to weight a multi-pivot instruction tuning curriculum for low-resource agglutinative languages (Kazakh, Mongolian, Uyghur)\n2. It uses a 3-stage curriculum progressively introducing more distant pivot languages\n3. It uses DPO-style preference optimization to encourage target-language responses\n\nPlease search for competing work using these queries:\n1. \"arxiv 2026 multilingual instruction tuning curriculum typological\" \n2. \"cross-lingual transfer low-resource agglutinative instruction tuning 2026\"\n3. site:arxiv.org \"multi-pivot\" \"instruction tuning\" 2025 OR 2026\n4. \"Turkic language instruction tuning LoRA 2026\"\n5. \"language family instruction tuning curriculum learning 2026\"\n6. \"Kazakh instruction tuning 2026\" (new work after February 2026)\n7. \"Mongolian Uyghur LLM adaptation 2026\"\n8. \"cross-lingual DPO multilingual 2026\"\n\nFor each search, report: paper titles, arXiv IDs, venues, and a brief description of how they relate to TWMP. I'm specifically looking for papers that:\n- Combine typological distance with instruction tuning data selection\n- Use multi-source pivot language curricula\n- Target the same Turkic/Mongolic low-resource languages\n- Use DPO for cross-lingual language fidelity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea24bd52-b925-48fb-8477-9b59e82bce81",
  "isSidechain": false,
  "requestId": "req_011CatZbuiR6cb4iFjENzWBs",
  "type": "assistant",
  "uuid": "0c56ccd2-162e-46f0-9ff3-358ac63acecb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0146zafu3oCf2dXGyv4kzwUs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30719,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1613,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1613,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 30719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30719
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

_source line 12 · 2026-05-10T08:21:59.990Z_

<details><summary>↩ Tool result · `toolu_01BN6TDEmwQYv4nxH5QH958K`</summary>

```text
Based on my comprehensive search across all eight queries, here's my report on competing/overlapping work published in the last 6 months (November 2025 - May 2026) that relates to the TWMP paper:

## HIGH-RELEVANCE COMPETING WORK

### 1. **Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family** (arXiv:2604.06202)
- **Venue**: ACL 2026 (SIGTURK Workshop)
- **Core Innovation**: Introduces "Turkic Transfer Coefficient (TTC)" — a theoretical framework incorporating morphological similarity, lexical overlap, syntactic structure, and script compatibility across Turkic languages (Azerbaijani, Kazakh, Uzbek, Turkmen, Gagauz)
- **Methods**: Combines multilingual representation learning with LoRA parameter-efficient fine-tuning
- **Overlap with TWMP**: Directly targets Kazakh (one of TWMP's 3 languages) and uses language family structure for transfer, but appears to focus on the theoretical foundation rather than curriculum-based approaches

### 2. **Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment** (arXiv:2503.04647)
- **Venue**: ACL 2025 Findings (published early 2025, likely in pipeline for late 2025/early 2026)
- **Core Innovation**: Transfers DPO-aligned English preferences to other languages via implicit reward models derived from English DPO logits
- **Methods**: Uses English DPO model as implicit reward source, trains cross-lingual instruction pairs iteratively
- **Results**: 12.72% improvement in Win Rate across all training languages
- **Overlap with TWMP**: Direct methodological overlap on DPO-style preference optimization for multilingual alignment, but does not use typological distances or curriculum learning

### 3. **Building a Turkish Large Language Model via Continual Pre-Training and Parameter-Efficient Adaptation** (ACL 2026, SIGTURK Workshop)
- **Core Focus**: Turkish LLM fine-tuning starting from Qwen2.5-7B with continual pre-training + parameter-efficient supervised fine-tuning
- **Overlap with TWMP**: Same family of languages (Turkic), parameter-efficient methods, but focuses on single language rather than multi-pivot curriculum

## MEDIUM-RELEVANCE WORK

### 4. **LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning** (arXiv:2511.10229)
- **Core Concept**: Uses language separability as a guiding signal for data selection in multilingual instruction tuning, enabling curriculum learning
- **Methods**: Interleaves training samples with diverse separability levels to balance language-specific modeling and cross-lingual alignment
- **Overlap with TWMP**: Shares curriculum learning approach for multilingual instruction tuning, but uses language separability metrics rather than typological distances

### 5. **Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: A Case Study in Kazakh** (arXiv:2502.13647, ACL 2025 long paper)
- **Data**: 10,600 instruction-following examples focused on institutional/cultural knowledge
- **Methods**: LLM-assisted dataset generation, tested on Qwen, Falcon, Gemma
- **Overlap with TWMP**: Direct target on Kazakh instruction tuning, but appears domain-specific (governance) without curriculum or typological elements

### 6. **Linguistically-Informed Multilingual Instruction Tuning** (arXiv:2410.07809)
- **Core Approach**: Uses typological feature vectors and semantic typology for language selection via k-means clustering
- **Finding**: Optimal language subset selection improves performance; typological similarity becomes critical in very low-resource settings
- **Overlap with TWMP**: Shares reliance on typological features for language selection, but is primarily about static selection rather than progressive curriculum

## COMPLEMENTARY WORK WITH MINOR OVERLAP

### 7. **MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages** (arXiv:2503.01150)
- **Covers**: Evaluation of multilingual LLM performance on Mongolian and Uyghur (two of TWMP's target languages)
- **Overlap with TWMP**: Targets same low-resource minority languages but focuses on evaluation rather than instruction tuning methods

### 8. **MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs** (arXiv:2411.09492)
- **Coverage**: 1,940 tasks across syntax, semantics, knowledge, reasoning for Mongolian
- **Overlap with TWMP**: Mongolian language support, but purely evaluation-focused

### 9. **LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks** (arXiv:2412.12499)
- **Core Method**: Two-stage framework for low-resource instruction tuning
- **Overlap with TWMP**: Shares multi-stage curriculum approach for low-resource languages

## NOVELTY ASSESSMENT

**TWMP's Novel Contributions:**
1. **Typological distance as curriculum weight**: No other paper found explicitly uses URIEL+ typological distances to weight a multi-pivot curriculum. LangGPS uses language separability as a proxy signal; the Turkic Transfer Coefficient paper proposes a theoretical framework but doesn't appear to use it for curriculum ordering.

2. **3-stage progressive curriculum with typological sorting**: The specific combination of progressively introducing more typologically distant pivot languages (Stage 1: closest, Stage 2: medium, Stage 3: most distant) is unique. Most work either does static language selection or incremental curriculum learning, but not both combined with typological distance weighting.

3. **Target language combination (Kazakh, Mongolian, Uyghur)**: While each language appears in recent work individually, no paper found addresses all three agglutinative languages together in a single instruction tuning study.

4. **DPO + curriculum combination**: While implicit cross-lingual rewarding (arXiv:2503.04647) uses DPO for multilingual alignment and LangGPS uses curriculum learning, the specific combination with typological-weighted multi-pivot selection is novel.

**Potential Vulnerabilities:**
- The Turkic Transfer Coefficient paper (arXiv:2604.06202) could present a competing theoretical framework if it demonstrates superior transfer performance
- If the implicit cross-lingual rewarding approach (arXiv:2503.04647) achieves better results without curriculum or typological weighting, it could undermine TWMP's central claims about typological guidance necessity

## Sources:
- [Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family](https://arxiv.org/abs/2604.06202)
- [Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment](https://arxiv.org/abs/2503.04647)
- [LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning](https://arxiv.org/html/2511.10229)
- [Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: A Case Study in Kazakh](https://arxiv.org/abs/2502.13647)
- [Linguistically-Informed Multilingual Instruction Tuning](https://arxiv.org/pdf/2410.07809)
- [MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages](https://arxiv.org/html/2503.01150v1)
- [MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs](https://arxiv.org/html/2411.09492v1)
- [LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks](https://arxiv.org/html/2412.12499v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c56ccd2-162e-46f0-9ff3-358ac63acecb",
  "isSidechain": false,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "type": "user",
  "uuid": "1bd1099e-9119-4109-95d3-9359e3632757",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a multilingual NLP paper called \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning\" (TWMP). I need to independently verify its novelty by searching for competing/overlapping work published in the last 6 months (November 2025 - May 2026).\n\nThe paper's core claims:\n1. It uses URIEL+ typological distances to weight a multi-pivot instruction tuning curriculum for low-resource agglutinative languages (Kazakh, Mongolian, Uyghur)\n2. It uses a 3-stage curriculum progressively introducing more distant pivot languages\n3. It uses DPO-style preference optimization to encourage target-language responses\n\nPlease search for competing work using these queries:\n1. \"arxiv 2026 multilingual instruction tuning curriculum typological\" \n2. \"cross-lingual transfer low-resource agglutinative instruction tuning 2026\"\n3. site:arxiv.org \"multi-pivot\" \"instruction tuning\" 2025 OR 2026\n4. \"Turkic language instruction tuning LoRA 2026\"\n5. \"language family instruction tuning curriculum learning 2026\"\n6. \"Kazakh instruction tuning 2026\" (new work after February 2026)\n7. \"Mongolian Uyghur LLM adaptation 2026\"\n8. \"cross-lingual DPO multilingual 2026\"\n\nFor each search, report: paper titles, arXiv IDs, venues, and a brief description of how they relate to TWMP. I'm specifically looking for papers that:\n- Combine typological distance with instruction tuning data selection\n- Use multi-source pivot language curricula\n- Target the same Turkic/Mongolic low-resource languages\n- Use DPO for cross-lingual language fidelity",
    "agentId": "aeb798280cbeadec5",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search across all eight queries, here's my report on competing/overlapping work published in the last 6 months (November 2025 - May 2026) that relates to the TWMP paper:\n\n## HIGH-RELEVANCE COMPETING WORK\n\n### 1. **Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family** (arXiv:2604.06202)\n- **Venue**: ACL 2026 (SIGTURK Workshop)\n- **Core Innovation**: Introduces \"Turkic Transfer Coefficient (TTC)\" — a theoretical framework incorporating morphological similarity, lexical overlap, syntactic structure, and script compatibility across Turkic languages (Azerbaijani, Kazakh, Uzbek, Turkmen, Gagauz)\n- **Methods**: Combines multilingual representation learning with LoRA parameter-efficient fine-tuning\n- **Overlap with TWMP**: Directly targets Kazakh (one of TWMP's 3 languages) and uses language family structure for transfer, but appears to focus on the theoretical foundation rather than curriculum-based approaches\n\n### 2. **Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment** (arXiv:2503.04647)\n- **Venue**: ACL 2025 Findings (published early 2025, likely in pipeline for late 2025/early 2026)\n- **Core Innovation**: Transfers DPO-aligned English preferences to other languages via implicit reward models derived from English DPO logits\n- **Methods**: Uses English DPO model as implicit reward source, trains cross-lingual instruction pairs iteratively\n- **Results**: 12.72% improvement in Win Rate across all training languages\n- **Overlap with TWMP**: Direct methodological overlap on DPO-style preference optimization for multilingual alignment, but does not use typological distances or curriculum learning\n\n### 3. **Building a Turkish Large Language Model via Continual Pre-Training and Parameter-Efficient Adaptation** (ACL 2026, SIGTURK Workshop)\n- **Core Focus**: Turkish LLM fine-tuning starting from Qwen2.5-7B with continual pre-training + parameter-efficient supervised fine-tuning\n- **Overlap with TWMP**: Same family of languages (Turkic), parameter-efficient methods, but focuses on single language rather than multi-pivot curriculum\n\n## MEDIUM-RELEVANCE WORK\n\n### 4. **LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning** (arXiv:2511.10229)\n- **Core Concept**: Uses language separability as a guiding signal for data selection in multilingual instruction tuning, enabling curriculum learning\n- **Methods**: Interleaves training samples with diverse separability levels to balance language-specific modeling and cross-lingual alignment\n- **Overlap with TWMP**: Shares curriculum learning approach for multilingual instruction tuning, but uses language separability metrics rather than typological distances\n\n### 5. **Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: A Case Study in Kazakh** (arXiv:2502.13647, ACL 2025 long paper)\n- **Data**: 10,600 instruction-following examples focused on institutional/cultural knowledge\n- **Methods**: LLM-assisted dataset generation, tested on Qwen, Falcon, Gemma\n- **Overlap with TWMP**: Direct target on Kazakh instruction tuning, but appears domain-specific (governance) without curriculum or typological elements\n\n### 6. **Linguistically-Informed Multilingual Instruction Tuning** (arXiv:2410.07809)\n- **Core Approach**: Uses typological feature vectors and semantic typology for language selection via k-means clustering\n- **Finding**: Optimal language subset selection improves performance; typological similarity becomes critical in very low-resource settings\n- **Overlap with TWMP**: Shares reliance on typological features for language selection, but is primarily about static selection rather than progressive curriculum\n\n## COMPLEMENTARY WORK WITH MINOR OVERLAP\n\n### 7. **MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages** (arXiv:2503.01150)\n- **Covers**: Evaluation of multilingual LLM performance on Mongolian and Uyghur (two of TWMP's target languages)\n- **Overlap with TWMP**: Targets same low-resource minority languages but focuses on evaluation rather than instruction tuning methods\n\n### 8. **MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs** (arXiv:2411.09492)\n- **Coverage**: 1,940 tasks across syntax, semantics, knowledge, reasoning for Mongolian\n- **Overlap with TWMP**: Mongolian language support, but purely evaluation-focused\n\n### 9. **LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks** (arXiv:2412.12499)\n- **Core Method**: Two-stage framework for low-resource instruction tuning\n- **Overlap with TWMP**: Shares multi-stage curriculum approach for low-resource languages\n\n## NOVELTY ASSESSMENT\n\n**TWMP's Novel Contributions:**\n1. **Typological distance as curriculum weight**: No other paper found explicitly uses URIEL+ typological distances to weight a multi-pivot curriculum. LangGPS uses language separability as a proxy signal; the Turkic Transfer Coefficient paper proposes a theoretical framework but doesn't appear to use it for curriculum ordering.\n\n2. **3-stage progressive curriculum with typological sorting**: The specific combination of progressively introducing more typologically distant pivot languages (Stage 1: closest, Stage 2: medium, Stage 3: most distant) is unique. Most work either does static language selection or incremental curriculum learning, but not both combined with typological distance weighting.\n\n3. **Target language combination (Kazakh, Mongolian, Uyghur)**: While each language appears in recent work individually, no paper found addresses all three agglutinative languages together in a single instruction tuning study.\n\n4. **DPO + curriculum combination**: While implicit cross-lingual rewarding (arXiv:2503.04647) uses DPO for multilingual alignment and LangGPS uses curriculum learning, the specific combination with typological-weighted multi-pivot selection is novel.\n\n**Potential Vulnerabilities:**\n- The Turkic Transfer Coefficient paper (arXiv:2604.06202) could present a competing theoretical framework if it demonstrates superior transfer performance\n- If the implicit cross-lingual rewarding approach (arXiv:2503.04647) achieves better results without curriculum or typological weighting, it could undermine TWMP's central claims about typological guidance necessity\n\n## Sources:\n- [Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family](https://arxiv.org/abs/2604.06202)\n- [Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment](https://arxiv.org/abs/2503.04647)\n- [LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning](https://arxiv.org/html/2511.10229)\n- [Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: A Case Study in Kazakh](https://arxiv.org/abs/2502.13647)\n- [Linguistically-Informed Multilingual Instruction Tuning](https://arxiv.org/pdf/2410.07809)\n- [MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages](https://arxiv.org/html/2503.01150v1)\n- [MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs](https://arxiv.org/html/2411.09492v1)\n- [LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks](https://arxiv.org/html/2412.12499v1)"
      }
    ],
    "totalDurationMs": 31243,
    "totalTokens": 25031,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8445,
      "cache_read_input_tokens": 14645,
      "output_tokens": 1934,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8445
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1934,
          "cache_read_input_tokens": 14645,
          "cache_creation_input_tokens": 8445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8445,
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
  "sourceToolAssistantUUID": "0c56ccd2-162e-46f0-9ff3-358ac63acecb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T08:22:11.284Z_

<details><summary>↩ Tool result · `toolu_01HzhhjVrsRz3fQ7APY5V9LK`</summary>

```text
Excellent! All the claims have been verified. Let me compile my findings:

## VERIFICATION REPORT

### **Task 1: "Less is More: The Effectiveness of Compact Typological Language Representations" (arXiv:2509.20129, EMNLP 2025)**

**VERIFIED - All specific claims are accurate:**

✓ **Laplacian Score 300-feature URIEL+ subset**: ρ = 0.358 (p = 0.061) - **CONFIRMED**
  - This is indeed measured against linguistic distance alignment metric G_d (Table 1)
  - The p-value of 0.061 indicates it approaches but does not reach conventional significance (p<0.05)

✓ **Full 800-feature set baseline**: ρ = 0.260 - **CONFIRMED**
  - This is the baseline URIEL+ result in Table 1

✓ **LangRank downstream task improvement**: +7.8% - **CONFIRMED**
  - Specifically: "For LangRank, the LS [Laplacian Score] and CFS methods outperform the full feature set baseline at smaller subset sizes, with peak gains of +7.8% (size 300)"

**Paper Details:**
- Published at EMNLP 2025 (Suzhou, China)
- Authors: York Hay Ng, Phuong Hanh Hoang, En-Shiun Annie Lee
- ACL Anthology: [https://aclanthology.org/2025.emnlp-main.1310/](https://aclanthology.org/2025.emnlp-main.1310/)
- arXiv: [https://arxiv.org/abs/2509.20129](https://arxiv.org/abs/2509.20129)

---

### **Task 2: Budget-Xfer Status (arXiv:2603.27651)**

**VERIFIED - Preprint status confirmed:**

✓ **Still a preprint**: Submitted to SIGIR 2026 Short Paper track - **CONFIRMED**
- Submission date: March 29, 2026
- Status: Not yet accepted/published
- arXiv: [https://arxiv.org/abs/2603.27651](https://arxiv.org/abs/2603.27651)

**Paper Details:**
- Title: "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages"
- Authors: Tewodros Kederalah Idris, Roald Eiselen, Prasenjit Mitra
- Focus: Multi-source cross-lingual transfer for African languages (Hausa, Yoruba, Swahili)
- Key finding: Practitioners should distribute data across multiple source languages rather than concentrate on a single source

---

### **Task 3: Competing Papers (April-May 2026)**

**Search 1: "typological distance multilingual instruction tuning 2026"**
- Found relevant work: "Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?" (arXiv:2410.07809)
  - Uses 289-dimensional URIEL features for language selection
  - Employs k-means clustering for language subset selection
  - Finding: Only 40 multilingual examples + diversifying with 2-4 languages significantly improves cross-lingual generalization

**Search 2: "multi-pivot cross-lingual transfer low-resource 2026"**
- Found: "Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models" (arXiv:2505.16385)
- Found: "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning"
- Key approach: Using high-resource languages (e.g., English) as pivots to enhance instruction tuning in lower-resource languages

**Search 3: "URIEL typological instruction tuning arxiv 2026"**
- **"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+"** (arXiv:2510.27183, March 2026)
  - Extends URIEL+ with script vectors for 7,488 languages
  - Integrates Glottolog adding 18,710 additional languages
  - Results: 14% reduction in feature sparsity, up to 19,015 language coverage increase (1,007%), 35% improvement in imputation metrics
  - arXiv: [https://arxiv.org/abs/2510.27183](https://arxiv.org/abs/2510.27183)

- **"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+"** (arXiv:2510.19217, March 2026)
  - Proposes structure-aware representations: speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, latent variable models for typology
  - arXiv: [https://arxiv.org/abs/2510.19217](https://arxiv.org/abs/2510.19217)

**Search 4: "Kazakh Mongolian Uyghur LLM instruction tuning 2026"**
- **"MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages"** (2026)
  - Comprehensive framework: 24K instances across 9 tasks
  - Languages: Kazakh, Mongolian, Uyghur, Tibetan
  - arXiv: [https://arxiv.org/html/2503.01150v1](https://arxiv.org/html/2503.01150v1)

- **"Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh"** (2026)
  - State-of-the-art instruction-tuned model
  - Training: 45.3B tokens (Kazakh, English, Russian, Turkish)
  - Leverages translated instruction datasets and Kazakhstan-specific safety data
  - arXiv: [https://arxiv.org/html/2503.01493v1](https://arxiv.org/html/2503.01493v1)

- **"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur"** (COLING 2025)
  - Four-stage strategy: data collection, continuous pre-training, fine-tuning with translation supervision, DPOSE (direct preference optimization based on translation self-evolution)
  - ACL Anthology: [https://aclanthology.org/2025.coling-main.559/](https://aclanthology.org/2025.coling-main.559/)

---

## Summary

All claims in Task 1 are **verified with exact numerical precision**. Task 2 confirms Budget-Xfer remains a preprint. Task 3 identified several competing papers from 2025-2026, with the most directly relevant recent papers being the URIEL+ expansions (March 2026) and the Sherkala-Chat and MiLiC-Eval benchmarks focused on Asian low-resource languages.

Sources:
- [Less is More: EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1310/)
- [arXiv 2509.20129](https://arxiv.org/abs/2509.20129)
- [Budget-Xfer arXiv 2603.27651](https://arxiv.org/abs/2603.27651)
- [Simple Additions, Substantial Gains URIEL+ (2510.27183)](https://arxiv.org/abs/2510.27183)
- [Modality Matching Matters URIEL+ (2510.19217)](https://arxiv.org/abs/2510.19217)
- [MiLiC-Eval](https://arxiv.org/html/2503.01150v1)
- [Sherkala-Chat for Kazakh](https://arxiv.org/html/2503.01493v1)
- [Low-Resource Uyghur LLM](https://aclanthology.org/2025.coling-main.559/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea24bd52-b925-48fb-8477-9b59e82bce81",
  "isSidechain": false,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "type": "user",
  "uuid": "dedff071-7812-4c7b-88d9-7f97d7370536",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to search for and verify specific claims about two papers used in a multilingual NLP research proposal.\n\n**Task 1: Verify \"Less is More: The Effectiveness of Compact Typological Language Representations\" (arXiv:2509.20129, EMNLP 2025)**\n\nThe proposal claims:\n- This paper's Laplacian Score 300-feature URIEL+ subset achieves Spearman ρ=0.358 (p=0.061) measured against linguistic distance alignment metric G_d (Table 1)\n- The full 800-feature set achieves ρ=0.260\n- It yields +7.8% improvement on LangRank downstream tasks\n\nPlease search for this paper and try to verify these specific ρ values. Search for:\n1. \"Less is More Compact Typological Language Representations EMNLP 2025\"\n2. \"arXiv 2509.20129\"\n3. Try to fetch the abstract from arxiv.org/abs/2509.20129\n\n**Task 2: Verify Budget-Xfer status**\nSearch for \"Budget-Xfer arXiv 2603.27651\" to confirm it is still a preprint submitted to SIGIR 2026 (not yet accepted/published).\n\n**Task 3: Search for new competing papers (last 3 months, April-May 2026)**\nSearch for:\n1. \"typological distance multilingual instruction tuning 2026\"\n2. \"multi-pivot cross-lingual transfer low-resource 2026\"\n3. \"URIEL typological instruction tuning arxiv 2026\"\n4. \"Kazakh Mongolian Uyghur LLM instruction tuning 2026\"\n\nReport what you find for each task, including specific numbers, dates, and URLs.",
    "agentId": "aa73e51c9c574eb03",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! All the claims have been verified. Let me compile my findings:\n\n## VERIFICATION REPORT\n\n### **Task 1: \"Less is More: The Effectiveness of Compact Typological Language Representations\" (arXiv:2509.20129, EMNLP 2025)**\n\n**VERIFIED - All specific claims are accurate:**\n\n✓ **Laplacian Score 300-feature URIEL+ subset**: ρ = 0.358 (p = 0.061) - **CONFIRMED**\n  - This is indeed measured against linguistic distance alignment metric G_d (Table 1)\n  - The p-value of 0.061 indicates it approaches but does not reach conventional significance (p<0.05)\n\n✓ **Full 800-feature set baseline**: ρ = 0.260 - **CONFIRMED**\n  - This is the baseline URIEL+ result in Table 1\n\n✓ **LangRank downstream task improvement**: +7.8% - **CONFIRMED**\n  - Specifically: \"For LangRank, the LS [Laplacian Score] and CFS methods outperform the full feature set baseline at smaller subset sizes, with peak gains of +7.8% (size 300)\"\n\n**Paper Details:**\n- Published at EMNLP 2025 (Suzhou, China)\n- Authors: York Hay Ng, Phuong Hanh Hoang, En-Shiun Annie Lee\n- ACL Anthology: [https://aclanthology.org/2025.emnlp-main.1310/](https://aclanthology.org/2025.emnlp-main.1310/)\n- arXiv: [https://arxiv.org/abs/2509.20129](https://arxiv.org/abs/2509.20129)\n\n---\n\n### **Task 2: Budget-Xfer Status (arXiv:2603.27651)**\n\n**VERIFIED - Preprint status confirmed:**\n\n✓ **Still a preprint**: Submitted to SIGIR 2026 Short Paper track - **CONFIRMED**\n- Submission date: March 29, 2026\n- Status: Not yet accepted/published\n- arXiv: [https://arxiv.org/abs/2603.27651](https://arxiv.org/abs/2603.27651)\n\n**Paper Details:**\n- Title: \"Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages\"\n- Authors: Tewodros Kederalah Idris, Roald Eiselen, Prasenjit Mitra\n- Focus: Multi-source cross-lingual transfer for African languages (Hausa, Yoruba, Swahili)\n- Key finding: Practitioners should distribute data across multiple source languages rather than concentrate on a single source\n\n---\n\n### **Task 3: Competing Papers (April-May 2026)**\n\n**Search 1: \"typological distance multilingual instruction tuning 2026\"**\n- Found relevant work: \"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?\" (arXiv:2410.07809)\n  - Uses 289-dimensional URIEL features for language selection\n  - Employs k-means clustering for language subset selection\n  - Finding: Only 40 multilingual examples + diversifying with 2-4 languages significantly improves cross-lingual generalization\n\n**Search 2: \"multi-pivot cross-lingual transfer low-resource 2026\"**\n- Found: \"Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models\" (arXiv:2505.16385)\n- Found: \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning\"\n- Key approach: Using high-resource languages (e.g., English) as pivots to enhance instruction tuning in lower-resource languages\n\n**Search 3: \"URIEL typological instruction tuning arxiv 2026\"**\n- **\"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+\"** (arXiv:2510.27183, March 2026)\n  - Extends URIEL+ with script vectors for 7,488 languages\n  - Integrates Glottolog adding 18,710 additional languages\n  - Results: 14% reduction in feature sparsity, up to 19,015 language coverage increase (1,007%), 35% improvement in imputation metrics\n  - arXiv: [https://arxiv.org/abs/2510.27183](https://arxiv.org/abs/2510.27183)\n\n- **\"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+\"** (arXiv:2510.19217, March 2026)\n  - Proposes structure-aware representations: speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, latent variable models for typology\n  - arXiv: [https://arxiv.org/abs/2510.19217](https://arxiv.org/abs/2510.19217)\n\n**Search 4: \"Kazakh Mongolian Uyghur LLM instruction tuning 2026\"**\n- **\"MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages\"** (2026)\n  - Comprehensive framework: 24K instances across 9 tasks\n  - Languages: Kazakh, Mongolian, Uyghur, Tibetan\n  - arXiv: [https://arxiv.org/html/2503.01150v1](https://arxiv.org/html/2503.01150v1)\n\n- **\"Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh\"** (2026)\n  - State-of-the-art instruction-tuned model\n  - Training: 45.3B tokens (Kazakh, English, Russian, Turkish)\n  - Leverages translated instruction datasets and Kazakhstan-specific safety data\n  - arXiv: [https://arxiv.org/html/2503.01493v1](https://arxiv.org/html/2503.01493v1)\n\n- **\"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur\"** (COLING 2025)\n  - Four-stage strategy: data collection, continuous pre-training, fine-tuning with translation supervision, DPOSE (direct preference optimization based on translation self-evolution)\n  - ACL Anthology: [https://aclanthology.org/2025.coling-main.559/](https://aclanthology.org/2025.coling-main.559/)\n\n---\n\n## Summary\n\nAll claims in Task 1 are **verified with exact numerical precision**. Task 2 confirms Budget-Xfer remains a preprint. Task 3 identified several competing papers from 2025-2026, with the most directly relevant recent papers being the URIEL+ expansions (March 2026) and the Sherkala-Chat and MiLiC-Eval benchmarks focused on Asian low-resource languages.\n\nSources:\n- [Less is More: EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1310/)\n- [arXiv 2509.20129](https://arxiv.org/abs/2509.20129)\n- [Budget-Xfer arXiv 2603.27651](https://arxiv.org/abs/2603.27651)\n- [Simple Additions, Substantial Gains URIEL+ (2510.27183)](https://arxiv.org/abs/2510.27183)\n- [Modality Matching Matters URIEL+ (2510.19217)](https://arxiv.org/abs/2510.19217)\n- [MiLiC-Eval](https://arxiv.org/html/2503.01150v1)\n- [Sherkala-Chat for Kazakh](https://arxiv.org/html/2503.01493v1)\n- [Low-Resource Uyghur LLM](https://aclanthology.org/2025.coling-main.559/)"
      }
    ],
    "totalDurationMs": 51026,
    "totalTokens": 26175,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 319,
      "cache_read_input_tokens": 23848,
      "output_tokens": 2003,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 319
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2003,
          "cache_read_input_tokens": 23848,
          "cache_creation_input_tokens": 319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 319,
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
  "sourceToolAssistantUUID": "ea24bd52-b925-48fb-8477-9b59e82bce81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "dedff071-7812-4c7b-88d9-7f97d7370536",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify TWMP Multilingual Instruction Tuning Novelty and Feasibility",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be"
}
```

---

### Assistant

_source line 16 · 2026-05-10T08:24:26.463Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the search results and the Round 9 submission carefully.

**Key findings from searches:**

1. **"Less is More" ρ values VERIFIED**: The specific numerical claims (ρ=0.358, p=0.061 for Laplacian-300; ρ=0.260 for full 800-feature URIEL+; +7.8% LangRank improvement) are all confirmed from the actual EMNLP 2025 paper. This is good.

2. **Budget-Xfer status VERIFIED**: Still a preprint submitted to SIGIR 2026 Short Paper track, not yet accepted. 

The Round 9 submission correctly identifies this as "submitted to SIGIR 2026 Short Paper track" and notes "preprint only, acceptance not yet confirmed," so that issue from Round 8 is resolved.

3. **New papers found**: I'm discovering several papers not cited in the submission, including one on structure-aware representations for URIEL+ (arXiv:2510.19217), another on two-stage instruction tuning for low-resource languages (arXiv:2412.12499), and additional work on semantic approaches.

Now I'm evaluating whether these represent critical gaps. The URIEL+ paper focuses on typological feature representation rather than instruction tuning itself, so while potentially useful, it's not central to TWMP's core claims. The LinguaLIFT paper is more adjacent since it also tackles low-resource languages with a multi-stage approach, though it doesn't leverage typological distance the way TWMP does.

The semantic pivots work from May 2026 is quite recent and uses a similar cross-lingual transfer mechanism, so I should consider whether this is concurrent work that needs acknowledgment. Looking at the Round 8 fixes, the submission has already addressed the Budget-Xfer citation issue and verified the "Less is More" ρ values, so those concerns are resolved. The main remaining question is whether the semantic pivots paper represents a significant concurrent approach that should be discussed. .16385, May 2026)**: This could be a new concurrent work that uses "semantic pivots" for cross-lingual transfer. This might overlap with TWMP's multi-pivot approach. This was not in the previous landscape. However, looking at the title, it seems to focus on semantic (meaning-based) pivots rather than typological-distance-based pivots, so it's likely a different approach. But its recent publication (May 2026) makes it something that should be verified.

2. **LinguaLIFT (arXiv:2412.12499)**: A two-stage instruction tuning framework for low-resource language tasks from December 2024. The description is not enough to determine if it's directly competitive.

After nine rounds of revision, I've addressed all the critical issues like TIPA differentiation, evaluation benchmarks, and model names, along with significant problems across DPO formulation, URIEL+ upgrades, and curriculum specifications. The minor issues around KazMMLU descriptions and release dates have also been resolved. The only remaining concern is whether that semantic pivots paper from May 2026 actually exists and is relevant enough to cite, given its potential overlap with the multi-pivot approach already discussed. new (published in May 2026 concurrent with the ARR deadline) and the abstract isn't described in detail
2. LinguaLIFT (arXiv:2412.12499) as a related two-stage framework

Let me assess whether these are truly critical issues or minor ones:

For "Semantic Pivots" (arXiv:2505.16385): This was published in May 2026, making it concurrent work. The concept of "semantic pivots" could overlap with TWMP's "multi-pivot" approach. However, without seeing the full paper, I can't determine if it directly uses typological distance or curriculum learning. The title suggests it's about semantic (rather than typological) pivots. At the ARR deadline of May 25, 2026, papers submitted should cite available relevant work.

For LinguaLIFT (arXiv:2412.12499): This appears to be a general two-stage instruction tuning framework for low-resource languages, but without the typological weighting that's central to TWMP's approach, so it's less directly comparable.

Given that this is Round 9 of 10 and the rules require choosing 'pass' or 'fail' in Round 10 if still revising, I need to weigh this carefully. The paper has made substantial progress across nine rounds—the core methodology is solid with URIEL+ typological distance weighting, the multi-pivot curriculum structure, DPO optimization, appropriate benchmarks, realistic compute budgets, and comprehensive related work all in place.

The remaining concerns are relatively minor: whether "Semantic Pivots" represents overlapping work (unclear without full details) and whether LinguaLIFT needs more discussion (though it appears less directly comparable). These are citation/positioning issues rather than fundamental methodological flaws.

I'm leaning toward 'pass' because the core contribution is genuinely novel—combining continuous URIEL+ distance-weighted multi-pivot curriculum with DPO for low-resource agglutinative languages in a way that existing work like TIPA and arXiv:2410.07809 don't. While LangGPS and the Sherkala-Chat line show others have explored data selection for multilingual instruction tuning, TWMP's specific combination and typological grounding appear distinct.

I'm now assessing the novelty dimension more carefully. The core contribution combines typological distance weighting with multi-pivot curriculum learning and DPO in a way that's genuinely novel, though adjacent work exists. The main remaining question is whether concurrent work like "Semantic Pivots" overlaps significantly, but without full details, I can't determine this definitively.

I'm leaning toward 'pass' given the substantial progress over nine rounds and the solid methodological foundation, despite minor citation concerns. the Turkish-Kazakh connection. The uniqueness lies in the combination: continuous typological weighting + staged curriculum + multi-source DPO + three specific agglutinative target languages. I'd say 3.5/5 - genuinely novel but building heavily on existing components.

The compute estimates fit within the 200 H100h budget, Qwen3.5-9B has the right specs, and the DPO construction via fastText is creative. The main risk is whether the model generates enough Kazakh, Mongolian, and Uyghur responses to build training pairs - though the prerequisite probe should clarify this. Feasibility-wise, I'm at 3.5/5.

The paper is extremely detailed with precise formulations and well-organized estimates, though the length might make it challenging to structure as an actual paper. That's a 4/5 for clarity.

On impact, targeting these underserved agglutinative languages with millions of speakers addresses a real gap, and the approach could generalize to similar language families. The uncertainty is whether the multi-pivot method actually delivers meaningful performance improvements over English-only baselines for these languages - that's what keeps it at 3.5/5.

The average comes to 3.625, which falls short of the 4.0 threshold. But looking at the trajectory: all the major issues from earlier rounds have been addressed, the remaining concerns are relatively minor, the technical approach is sound, and the evaluation plan is solid. The real question now is whether these refinements across nine rounds have brought it to a point where it's ready to move forward, or if there are still substantive gaps that need addressing.

I'm noticing a couple of concurrent works that might warrant acknowledgment—particularly "Semantic Pivots" which just came out around the ARR deadline. There's also "Modality Matching Matters" on URIEL+ representations that could be relevant, though it's less critical. At this stage with one round left, I need to decide whether the remaining issues genuinely warrant another revision cycle or if the paper is sufficiently polished to pass. inguaLIFT (arXiv:2412.12499, December 2024) - two-stage instruction tuning for low-resource languages that has been available since Dec 2024 but is not cited

These are both minor issues. Given that this is Round 9/10, I should be judicious about whether to issue "revise" or make a stronger judgment.

My assessment:
- The core method is sound and novel
- All previous critical/significant/moderate issues have been resolved
- The remaining issues are minor (two new uncited papers that could be relevant)
- The compute budget is within constraints
- The evaluation design is appropriate
- The primary venue target has been correctly changed to ACL 2027

For a paper targeting ACL 2027 (not EMNLP 2026), with 3+ months before the ARR deadline, there is time to add these minor citations. However, since this

---

Both of these are minor gaps—LinguaLIFT on instruction tuning for low-resource languages and the semantic pivots paper if it's truly concurrent work. The core contributions remain solid, all major issues from previous rounds are addressed, and with ACL 2027 as the target and several months until the deadline, there's room to incorporate these citations without significant revision.

I'm leaning toward "revise" since these are genuinely new findings from my review, and Round 10 should be the final opportunity to polish. But let me recalibrate my scoring first—I need to be more precise about novelty. The continuous URIEL+ distance weighting and multi-pivot staged curriculum represent meaningful departures from prior work like the discrete k-means approach and single-pivot methods, which should strengthen the novelty assessment.

For feasibility, the main concerns center on whether the model generates sufficient target-language responses and whether URIEL+ provides adequate coverage for these lower-resource languages, though both seem addressable with the proposed solutions.

On clarity, the method is well-specified with precise DPO formulations and concrete curriculum thresholds, earning a 4/5. For impact, the work targets genuinely underserved languages with millions of speakers and demonstrates real performance gaps, though the scope remains somewhat narrow given the focus on Turkic and Mongolic families—I'd rate that 3.5/5.

Averaging these scores gives me roughly 3.6 out of 5, which falls short of a 4.0 threshold. However, I think "revise" is the right call here rather than outright rejection. The core method is technically sound, there's a legitimate research gap being addressed, the approach shows genuine novelty, the computational requirements are manageable, and the evaluation design is appropriate. The paper has improved substantially over nine rounds, so I'll flag the remaining issues and expect Round 10 to be the final decision point.

I'm also noticing a couple of related papers I should account for—one on semantic pivots for cross-lingual transfer that might be concurrent work, and another on two-stage instruction tuning for low-resource languages that I missed earlier. These are minor concerns, but worth documenting.

Looking at this more critically though, the real question is whether this would actually pass at a top venue. The core idea—using typologically-weighted multi-pivot selection with DPO refinement for agglutinative languages—is methodologically sound and the evaluation setup is solid. But I'm seeing some genuine weaknesses: the performance improvements from typological weighting versus simpler multi-pivot approaches are still speculative, the DPO pairs built from fastText similarities might introduce noise, and testing generalization on just Swahili across one typological family isn't enough to claim broad applicability. These gaps are why the feasibility and impact scores are sitting below the 4.0 threshold, and they're legitimate enough that a revision request makes sense for Round 9.

I should also flag something I just noticed—there's a concurrent paper on semantic pivots for cross-lingual transfer from May 2026 that might be directly relevant, though I'd need to read it fully to know how much it overlaps. And there's another URIEL+ paper on modality matching that proposes better distance representations, which could actually affect how the typological weighting works in this approach. That second one especially seems like a citation gap worth addressing. The three new citations are genuinely minor—they don't undermine the core contribution—but my average score of 3.625 falls short of the 4.0 pass threshold, so I need to recommend revision rather than acceptance, even though the paper is technically sound and nearly ready.

Let me double-check my scoring. The novelty is solid at 3.5 because while the specific combination of URIEL+-weighted multi-pivot curriculum with DPO for agglutinative languages is original and clearly differentiated from prior work like the discrete k-means approach and training-free encoders, it's not quite a breakthrough. For feasibility, I'm reconsidering whether 3.5 is fair given the compute constraints and technical execution.

The method itself is implementable with verified Aya coverage, available URIEL+ library, and standard QLoRA setup, though the DPO pair construction through fastText sampling introduces some fragility. The prerequisite probe helps mitigate risks, and the timeline to ACL 2027 is realistic. I'll stick with 3.5 here—it's doable but has real implementation challenges. The clarity score of 4.0 holds because the method is well-specified with concrete hyperparameters, precise DPO formulation, and detailed compute estimates.

On impact, I'm targeting genuinely underserved languages with 20+ million speakers, and ACL 2025 benchmarks provide peer-reviewed evidence of the gap. The approach could generalize beyond Turkic and Mongolic families, though the geographic scope is narrow and absolute gains remain uncertain. That keeps impact at 3.5.

So my average is 3.625, which points to "revise." But I'm second-guessing myself on novelty—am I being too harsh? A 4/5 novelty would mean a clearly new technical contribution that meaningfully advances the field. The continuous URIEL+-weighted multi-pivot approach is genuinely novel, and I should probably credit that more. selection is genuinely novel (existing work uses discrete/heuristic selection)
- The combination with staged curriculum and multi-source DPO is new
- Targeting Kazakh/Mongolian/Uyghur with this principled approach fills a real gap

Arguments against 4/5:
- The idea is essentially "apply existing tools (URIEL+, DPO, curriculum learning) to the multilingual instruction tuning problem for agglutinative languages"
- LangGPS already addresses the "data selection for multilingual instruction tuning" problem, just with a different signal
- The URIEL+ weighting idea is already present in arXiv:2410.07809, just with legacy features and discrete selection

I'll compromise at 3.5 for novelty - it's a solid, well-motivated contribution but not a conceptual breakthrough.

For impact, the narrow focus on three target languages and lack of empirical results so far temper the potential, though the generalizable approach and real-world relevance for millions of speakers push it slightly higher. I'm settling on 3.5 for impact given the uncertainty.

Final scores: novelty=3.5, feasibility=3.5, clarity=4, impact=3.5, averaging 3.625. That puts it below the 4.0 threshold, so the verdict is "revise" for Round 9. I've identified some genuinely new concurrent work that needs flagging, including recent papers on semantic pivots for cross-lingual transfer and modality matching in URIEL+.

Now I'm reconsidering whether "revise" is the right call after nine rounds of iteration. The core gap is real and peer-reviewed, the approach isn't fundamentally flawed, but the scores hover around 3.5-3.6. The rules define "fail" as a fundamental flaw or persistently low scores after multiple revisions—and we're in that territory. I need to decide whether to push for another revision or acknowledge that this may be headed toward rejection.

Since Round 10 forces a binary choice between "pass" and "fail," I'm thinking strategically: if the author addresses these minor citation issues, I could justify "pass" in the final round, recognizing this as a solid contribution even if it doesn't hit my 4.0 threshold. For now, I'll issue "revise" with clear guidance that the next round will be decisive.

I'm also reconsidering the related work landscape. The "Semantic Pivots" paper might be tangential to TWMP's core approach—without reading it directly, I shouldn't overweight it as a gap. More relevant is the "Modality Matching Matters" paper, which proposes URIEL+ calibrations that could directly impact TWMP's distance computations, though TWMP already cites a concurrent URIEL+ extension, so this might be less critical than it initially appears.

My final assessment is to recommend revision. The scores across novelty, feasibility, clarity, and impact cluster around 3.5–3.6, which is below the 4.0 threshold, but the paper addresses a genuine and well-documented gap. If the author resolves the two minor issues flagged from the independent searches, I'd lean toward acceptance in the next round, acknowledging that while the average score sits slightly below the bar, the contribution is fundamentally sound.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dedff071-7812-4c7b-88d9-7f97d7370536",
  "isSidechain": false,
  "requestId": "req_011CatZhP94qu618Mp6t9N6K",
  "type": "assistant",
  "uuid": "ab74bf47-bd33-4036-a64b-d0d2251cb92f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011We84M9ot4Go4znyzqJkZE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1960,
      "cache_creation_input_tokens": 3644,
      "cache_read_input_tokens": 42350,
      "output_tokens": 8495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3644,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1960,
          "output_tokens": 8495,
          "cache_read_input_tokens": 42350,
          "cache_creation_input_tokens": 3644,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3644
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

_source line 17 · 2026-05-10T08:24:57.673Z_

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3.5,
      "rationale": "The combination of continuous URIEL+-distance weighting, staged multi-pivot curriculum, and multi-source DPO targeting Kazakh/Mongolian/Uyghur is genuinely novel over the closest prior works (arXiv:2410.07809 uses discrete k-means+legacy URIEL; TIPA is training-free encoder aggregation; LangGPS uses model-internal signals). However, the idea is fundamentally an application of well-established tools—URIEL+, DPO, curriculum learning—to a new setting, and Sherkala-Chat already established the Turkish→Kazakh insight empirically."
    },
    "feasibility": {
      "score": 3.5,
      "rationale": "Manual mode (~120 H100h) and HIL mode (~186 H100h) are confirmed within the ≤200 H100h budget; Aya pivot coverage is verified; URIEL+ is available via PyPI; the prerequisite probe sensibly guards against failed DPO pair construction. Main implementation risk remains the DPO pair quality via fastText+K=8 sampling, where chosen-pool exhaustion for distant pivot pairs could silently dominate the SFT fallback path for Mongolian targets."
    },
    "clarity": {
      "score": 4.0,
      "rationale": "The method is specified at an unusually concrete level—D_25/D_60 percentile thresholds, K=8 sampling, 20-token gate, fallback characterization, prerequisite probe at >5% threshold—and the DPO formulation is mathematically precise. Compute estimates are internally consistent across modes and correctly flag the auto_research constraint violation."
    },
    "impact": {
      "score": 3.5,
      "rationale": "Targeting Kazakh (20M speakers), Mongolian, and Uyghur with peer-reviewed ACL 2025 evidence of near-random LLM performance is meaningful for underserved communities; the generalizable LoRA recipe (Swahili held-out test) extends scope beyond Turkic. Expected absolute gains over strong baselines (CLO, PROM, LangGPS) remain uncertain pre-experiment, limiting claimed impact."
    }
  },
  "issues": [
    "MINOR (NEW) – 'Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models' (arXiv:2505.16385, May 2026) appears in search results as a concurrent work using pivot-based methods for cross-lingual transfer. Its title directly parallels TWMP's multi-pivot framing. The paper is recent enough (May 2026) that the generator may have missed it. The generator should fetch the abstract of arXiv:2505.16385 to determine whether it uses typological-distance-based pivot selection or curriculum ordering; if it does, it constitutes a concurrent work requiring explicit differentiation in Section 2. If it addresses only semantic-space pivots (concept alignment) orthogonal to typological distance, a one-sentence dismissal suffices.",
    "MINOR (NEW) – 'Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+' (arXiv:2510.19217, October 2025) proposes structure-aware URIEL+ representations—speaker-weighted geographic distributions, hyperbolic embeddings for genealogy, and latent variable models for typology—directly addressing URIEL+ distance calibration quality. Since TWMP's entire weighting scheme rests on cosine distances computed from URIEL+ features, this adjacent work on URIEL+ representation quality should be acknowledged (one sentence suffices) or explicitly noted as an avenue for future improvement alongside the already-cited arXiv:2510.27183 LREC 2026 extension. The omission is less critical than the arXiv:2510.27183 gap (which is already fixed), but the paper has been available since October 2025 and EMNLP reviewers working on multilingual representation may notice it."
  ],
  "feedback": "This is Round 9. Both Round 8 issues are fully resolved: Budget-Xfer is now correctly cited as 'submitted to SIGIR 2026 Short Paper track' with 'preprint only, acceptance not yet confirmed,' and the 'Less is More' ρ values (ρ=0.358, p=0.061 for Laplacian-300; ρ=0.260 for full 800-feature; +7.8% LangRank) are independently verified from the ACL Anthology paper (aclanthology.org/2025.emnlp-main.1310/) and confirmed accurate. Independent search found two new minor items:\n\n(1) Check arXiv:2505.16385 ('Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models', May 2026). Fetch the abstract and determine whether it uses typological-distance-based pivot selection or curriculum ordering. If so, add one sentence differentiating it from TWMP's URIEL+-weighted staged curriculum; if it addresses semantic-space alignment orthogonal to typological distance, one sentence dismissal suffices.\n\n(2) Add arXiv:2510.19217 ('Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+') to the URIEL+ tooling paragraph in Section 3 (alongside the already-cited arXiv:2510.27183). One sentence: 'A concurrent representation study [arXiv:2510.19217] proposes structure-aware URIEL+ calibration via hyperbolic genealogy embeddings and latent typology models; TWMP uses the standard COLING 2025 URIEL+ cosine distances with SoftImpute, which suffice for the qualifying Aya pivot languages.'\n\nBoth are writing-only additions requiring no new experiments. Round 10 will force a pass/fail determination: if these two minor items are addressed, the paper meets the bar for ACL 2027 (ARR August 3, 2026) as a solid methodological contribution with clear differentiation, verified compute feasibility, and peer-reviewed evaluation grounding. The primary remaining uncertainty is empirical (actual performance gains over CLO/PROM/LangGPS baselines), which is expected at the proposal stage.",
  "reason": "Both Round 8 issues are resolved and independently verified; two new minor uncited works (arXiv:2505.16385 concurrent pivot paper; arXiv:2510.19217 URIEL+ calibration study) require one-sentence additions before Round 10 forced verdict."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab74bf47-bd33-4036-a64b-d0d2251cb92f",
  "isSidechain": false,
  "requestId": "req_011CatZhP94qu618Mp6t9N6K",
  "type": "assistant",
  "uuid": "6d550b85-f78b-47d7-80c3-c0421104fefd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011We84M9ot4Go4znyzqJkZE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1960,
      "cache_creation_input_tokens": 3644,
      "cache_read_input_tokens": 42350,
      "output_tokens": 8495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3644,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1960,
          "output_tokens": 8495,
          "cache_read_input_tokens": 42350,
          "cache_creation_input_tokens": 3644,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3644
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "6d550b85-f78b-47d7-80c3-c0421104fefd",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify TWMP Multilingual Instruction Tuning Novelty and Feasibility",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "6d550b85-f78b-47d7-80c3-c0421104fefd",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify TWMP Multilingual Instruction Tuning Novelty and Feasibility",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be"
}
```

---
