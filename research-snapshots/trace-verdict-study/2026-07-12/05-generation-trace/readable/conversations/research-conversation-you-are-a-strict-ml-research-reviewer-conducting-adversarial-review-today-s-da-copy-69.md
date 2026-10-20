# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/0703e2f2-7ac0-4ac2-8162-db16255314e0.jsonl`
- **Structured JSON:** [`50bb6b645dd715eb3140.json`](../../sessions/50/50bb6b645dd715eb3140.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:16:15.728Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:16:15.728Z",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Multilingualism and Cross-Lingual NLP.\n\nDirection: Cross-lingual transfer and multilingual NLP methods. In-scope: cross-lingual transfer without parallel data, multilingual instruction tuning strategies, language-agnostic representations, low-resource language adaptation, cross-lingual retrieval, multilingual reasoning, code-switching handling. ACL 2025 outstanding papers highlighted multilingual gaps and cross-lingual intervention methods.\n\nContribution type: METHOD ONLY. New training recipes, transfer algorithms, or adaptation techniques. Not a new multilingual dataset or language-specific analysis.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Multilingual experiments need coverage across languages — budget for LoRA fine-tuning on multilingual models, not full pretraining.\n2. Time: ≤16 days. Use existing multilingual models (BLOOM, mT5, XLM-R, Aya, Qwen multilingual, Llama-3 multilingual).\n3. Eval: XTREME-UP, XCOPA, XStoryCloze, MGSM, multilingual MMLU, TyDi QA, FLORES for MT.\n\nLook for: efficient cross-lingual transfer with minimal target-language data, multilingual reasoning without English-centric bias, representation alignment methods, adaptation techniques for typologically diverse languages. Avoid: English-only experiments, monolingual fine-tuning.\n\nTag: direction=multilingual, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 4/10)\n{\n  \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning\",\n  \"core_problem\": \"Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.\",\n  \"opportunity\": \"Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K Kazakh-language questions spanning STEM, humanities, and social sciences sourced from authentic educational materials; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.\",\n  \"landscape\": \"PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.\",\n  \"approach\": \"We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\\n\\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\\n\\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/Masonshipton25/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 on typological alignment tasks versus ρ=0.260 for the full 800-feature set while also improving downstream cross-lingual NLP performance, we apply this feature selection before computing cosine distances. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\\n\\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\\n\\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\\n\\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; pair the highest-scoring chosen with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples are discarded. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\\n\\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released February 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh, MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG and CLO serve as primary baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO baselines, URIEL+ sub-space ablations, curriculum schedule variants, and DPO prerequisite probe runs)\",\n      \"gpu_utilization\": \"LOW (~25–35%): GPU sits idle during code writing, debugging, data pipeline work, result analysis, and paper writing; runs are launched manually and often queue overnight\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$300 (200h × $1.50/h on Lambda Labs A100)\",\n      \"h100_equivalent\": \"~120h H100 (within ≤200 H100-hour budget constraint at typical A100/H100 performance ratio of ~0.6×)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~310h A100 (agent explores broader hyperparameter space with human approval gates; ~55% more runs than manual)\",\n      \"gpu_utilization\": \"MODERATE (~55–65%): agent queues follow-up experiments immediately after each run completes, filling GPU idle between human check-ins\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in to approve experiment configs and review intermediate results\",\n      \"claude_api_cost\": \"~$150–250 (~1,500–2,500 conversation turns coordinating experiment scheduling, result parsing, and ablation planning)\",\n      \"estimated_gpu_cost\": \"~$465 (310h × $1.50/h)\",\n      \"h100_equivalent\": \"~186h H100 (within ≤200 H100-hour budget constraint at ~0.6× A100/H100 ratio, leaving ~14h headroom)\",\n      \"risk_note\": \"Choice of URIEL+ feature subspace (full 800-feature vs. Laplacian 300-feature vs. syntax-only) and the DPO prerequisite probe threshold require human judgment at key decision points; an automated agent may converge on a locally optimal weighting scheme that under-performs on the held-out Swahili generalization target\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~600h A100 (3–5× more experiments: grid search over distance metrics, curriculum schedule shapes, LoRA rank/alpha, 5+ target languages including Swahili and Kyrgyz for generalization, plus replication runs)\",\n      \"gpu_utilization\": \"NEAR-ZERO idle—agent schedules jobs back-to-back across all target languages in parallel, launches follow-up ablations immediately on job completion, and runs nightly sweeps without human bottleneck\",\n      \"timeline\": \"5–10 days with 4× concurrent A100s; ~3 weeks on a single A100\",\n      \"team\": \"0 (initial setup of experiment configs, data paths, and evaluation harness only)\",\n      \"claude_api_cost\": \"~$400–650 (~4,000–6,500 turns for full experiment orchestration, result parsing, ablation tree exploration, and report drafting)\",\n      \"estimated_gpu_cost\": \"~$900 (600h × $1.50/h)\",\n      \"h100_equivalent\": \"~360h H100 — EXCEEDS the ≤200 H100-hour hard budget constraint. Auto_research mode is documented for completeness but is NOT a viable deployment option within the stated budget. Use manual mode (~120 H100h) or human_in_loop mode (~186 H100h) to remain within budget.\",\n      \"speed_bottleneck\": \"GPU count is the primary bottleneck: 4 concurrent A100s reduces wall-clock time to ~5 days; API rate limits become secondary when running >8 parallel experiment threads\",\n      \"risk_note\": \"CONSTRAINT VIOLATION: 600 A100h ≈ 360 H100h, exceeding the ≤200 H100-hour hard budget. Additionally, unconstrained exploration may overfit the URIEL+ weighting function to the 3 initial target languages; Swahili as a held-out agglutinative target is required to detect this overfitting early.\"\n    }\n  },\n  \"target_venues\": [\n    \"ACL 2027 (ARR submission deadline August 3, 2026) — primary target; provides adequate time for validation on additional typological clusters beyond Turkic–Mongolic, and for a paper of this scope (multi-pivot curriculum + ablations + 3 evaluation benchmarks) that cannot realistically reach conference quality in under 6 weeks\",\n    \"EMNLP 2026 (ACL Rolling Review, rolling deadlines throughout 2026) — viable only if the team has prior QLoRA fine-tuning infrastructure already in place and can begin experiments immediately\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (ACL 2024) [29% improvement on Chinese/Korean/Italian/Spanish; Turkic/Mongolic gap is untested]\",\n    \"Cross-Lingual Optimization for Language Transfer in Large Language Models (CLO; ACL 2025, arXiv:2505.14297) [DPO-style cross-lingual preference optimization using English-only source and M2M100 translation; baseline and methodological reference for TWMP's multi-source DPO extension]\",\n    \"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP]\",\n    \"Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset (ρ=0.358) outperforms full 800-feature URIEL+ (ρ=0.260) for typological alignment and downstream cross-lingual NLP; justifies TWMP's feature selection step]\",\n    \"Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]\",\n    \"TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]\",\n    \"Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]\",\n    \"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark, 23K questions, peer-reviewed]\",\n    \"MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]\",\n    \"TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]\",\n    \"Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]\",\n    \"Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)\",\n    \"Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)\",\n    \"Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]\",\n    \"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]\"\n  ],\n  \"description\": \"This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358 vs. ρ=0.260 for the full 800-feature set) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B and applying fastText language identification, requiring no target-language training labels. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency per source-target pair; pairs failing this check fall back to SFT-only. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU, MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.\",\n  \"project_name\": \"typological_multi_pivot\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL – TIPA (arXiv:2601.16629, EACL 2026 Findings) is directly competing work the generator missed: it constructs proxy language adapters by aggregating existing ones weighted by typological similarity across 230+ languages and five tasks. The novelty claim 'no prior work combines multi-pivot selection with typological distance weighting' is therefore too strong; the revision must differentiate TWMP from TIPA clearly (TIPA is training-free adapter aggregation for encoders; TWMP is a weighted sampling + curriculum training approach for decoder LLMs in instruction tuning—this distinction exists but must be made explicit).\", \"CRITICAL – Evaluation benchmarks are misspecified: XQuAD and XCOPA do NOT include Kazakh, Mongolian, or Uyghur—multiple sources and the benchmarks' own documentation confirm this. The evaluation protocol must be redesigned to use benchmarks that actually cover the target languages (e.g., XTREME-UP, MiLiC-Eval for Chinese minority languages, or TyDi QA for Kazakh).\", \"SIGNIFICANT – Model name 'Qwen 3.5-7B' does not exist. The Qwen3.5 series released in 2026 includes 4B and 9B variants (among others) but no 7B. The 250K vocabulary claim is correct for Qwen3.5 but the model identifier must be corrected to Qwen3.5-9B or Qwen3.5-4B before submission.\", \"SIGNIFICANT – 16-day timeline is unrealistic for a conference-quality submission. Running 15–20 QLoRA experiments across 3 target languages, implementing the TWMP curriculum + CLO loss from scratch, and writing a complete paper cannot be done in 16 days by 1–2 researchers without preexisting infrastructure. The compute estimate (180h A100 ≈ 125–135h H100) is within the 200 H100-hour hard constraint, but wall-clock time is the binding bottleneck.\", \"SIGNIFICANT – The primary evidence for the research gap, 'Left Behind' (arXiv:2603.21036), is a March 2026 preprint from a single author at North American University evaluated with 50 hand-crafted questions. EMNLP reviewers will reject this as insufficient basis for a gap claim; the motivation must be grounded in larger, peer-reviewed evaluations (e.g., the 'Shared Weights Pretraining for Extremely Low-Resource Languages' ACL 2025 paper, or XTREME-UP results for Turkic languages).\", \"MODERATE – Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) is not properly discussed in the landscape. This paper directly uses typological feature vectors for language selection in multilingual instruction tuning—the generator characterizes only arXiv:2505.13908 (which is purely analytical) while ignoring this more methodologically relevant prior work.\", \"MODERATE – MLM is a NeurIPS 2025 ER Workshop paper, not a NeurIPS 2025 main conference paper. Misrepresenting workshop papers as conference papers in a related work section is a frequent reviewer complaint and can trigger a bias/credibility flag.\", \"MODERATE – The CLO-style loss is described as a 'cross-lingual contrastive loss that enforces target-language response fidelity.' CLO actually uses DPO-style preference optimization (not a contrastive loss) to suppress off-language responses. The paper must use technically accurate descriptions to avoid confusion and reviewer pushback.\", \"MINOR – PLUG (ACL 2024)'s 29% improvement was measured on Chinese, Korean, Italian, and Spanish—not on Kazakh/Mongolian/Uyghur. The assumption that PLUG performs poorly on Turkic languages is plausible but not directly evidenced in the PLUG paper itself; the gap claim relative to PLUG needs its own experimental demonstration.\"]\nFeedback: The core idea is genuinely interesting—typological-distance-weighted multi-pivot instruction tuning for Turkic low-resource languages—but the current draft has three blockers that prevent submission at EMNLP 2026 quality: (1) TIPA (EACL 2026) must be cited and clearly differentiated: TIPA does typological weighting of adapters in a training-free, encoder-adapter (MAD-X) framework across 230+ languages; TWMP is a training-time data sampling + curriculum approach for decoder LLMs in instruction tuning—spell this out explicitly in Section 2. (2) Replace XQuAD + XCOPA with benchmarks that actually include Kazakh, Mongolian, and Uyghur: consider XTREME-UP (includes Kazakh), MiLiC-Eval (Uyghur, Kazakh, Mongolian), and TyDi QA for real-language evaluation. If none of the standard benchmarks are adequate, you need to explain what evaluation data you are using and where it comes from. (3) Correct the model name to Qwen3.5-9B (or 4B) and rerun your compute estimates accordingly. Beyond the blockers: the motivation should be regrounded away from 'Left Behind' as the sole anchor—add references to XTREME-UP or ACL 2025 shared-weights pretraining results for Turkic languages. Add arXiv:2410.07809 to related work with a clear explanation of why TWMP's weighted sampling and curriculum are distinct contributions. Fix the MLM venue to 'NeurIPS 2025 ER Workshop' and fix the CLO description to 'DPO-style cross-lingual preference optimization.' On timeline: unless the team has the training infrastructure already built, the 16-day window makes a May 25 ARR deadline extremely risky; the ACL 2027 ARR deadline (August 3, 2026) is a more defensible target that allows proper validation on additional typological clusters (e.g., a Bantu agglutinative language) to test generalization beyond Turkic.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"SIGNIFICANT – CLO's DPO objective is designed for English-source preference pairs: chosen = target-language response to English instruction, rejected = off-language (English) response to target-language instruction. TWMP proposes extending this to non-English source languages (Turkish/Uzbek → Kazakh), but the paper does not specify how preference pairs are constructed when the source is itself a non-English language like Uzbek. If the model produces a Kazakh response to a Uzbek instruction, what is the 'rejected' response? Reviewers will reject this as technically incomplete without a precise DPO formulation for the multi-source case.\", \"SIGNIFICANT – URIEL legacy features are known to be sparse for exactly the target languages in this paper. URIEL+ (arXiv:2409.18472, COLING 2025) explicitly improves coverage for low-resource languages and should be used instead of the 289-dim lang2vec legacy features. Furthermore, 'Less is More: The Effectiveness of Compact Typological Language Representations' (EMNLP 2025) shows that compact URIEL+ features outperform the full 289-dim feature space for cross-lingual NLP tasks—directly contradicting TWMP's use of all 289 dimensions without selection. This is a directly relevant citation the paper must engage with.\", \"MODERATE – Auto_research mode (600h A100 ≈ 300h H100) exceeds the stated ≤200 H100-hour hard constraint. While the experiment plan uses manual mode (within constraint), the resource estimate table presents auto_research as a legitimate deployment mode without flagging this violation of the user's stated budget constraint.\", \"MODERATE – The staged curriculum's cosine-distance threshold schedule is described qualitatively ('progressively expands the radius at scheduled epochs') but no concrete schedule is specified. Reviewers will ask: how many stages? What distance thresholds? How are thresholds set relative to the URIEL distance distribution of the Aya collection? Without a concrete, reproducible specification, this is a design element that cannot be ablated or replicated.\", \"MODERATE – DCO (arXiv:2603.04678, March 2026, Tianyu Liu et al.) introduces Direct Consistency Optimization, a DPO-inspired method for cross-lingual knowledge consistency across 26 languages and 9 LLMs. This is a concurrent work that uses a DPO-style objective for cross-lingual alignment—similar in spirit to the CLO component of TWMP—and must be cited and differentiated in the related work section.\", \"MINOR – The Aya dataset's coverage of Turkic pivot languages (Turkish, Uzbek, Kyrgyz) is assumed but not verified. If Uzbek and Kyrgyz have only hundreds of Aya instances, the typological-distance-weighted sampling will produce noisy estimates for the closest pivots to Kazakh. The paper should state the number of available training instances per pivot language in Aya and set a minimum threshold below which a language is excluded from the mixture.\"]\nFeedback: The generator has addressed all Round 1 critical issues competently: TIPA is correctly differentiated, benchmarks are fixed, Qwen3.5-9B is confirmed correct, arXiv:2410.07809 is properly placed in the landscape, and the CLO/DPO description is accurate. The remaining blockers are two: (1) The DPO objective must be precisely formulated for non-English source languages. The current description 'increases preference for target-language responses and reduces preference for off-language outputs, without requiring any target-language training labels' is borrowed verbatim from CLO's English-source setting. For a Turkish → Kazakh pair, you must specify: what constitutes the chosen response, what constitutes the rejected response, and how you obtain these without any Kazakh labels. One viable extension: treat (Turkish-instruction, Kazakh-response) as the chosen pair and (Turkish-instruction, Turkish-response) as rejected—but this requires stating it explicitly and verifying that Qwen3.5-9B produces detectable off-language Turkish responses to Turkish instructions. (2) Replace lang2vec 289-dim URIEL features with URIEL+ (arXiv:2409.18472, COLING 2025), which has better sparse-language coverage, and cite 'Less is More' (EMNLP 2025) to justify whichever feature subspace you choose. This is not just a citation gap—if the typological distances for Uzbek and Kyrgyz are inaccurate in legacy URIEL due to sparsity, the entire weighting scheme degrades for the most important (closest) pivots to Kazakh. Beyond the blockers: add DCO (arXiv:2603.04678) to related work; specify the curriculum schedule concretely (number of stages, distance thresholds); verify and report the number of Aya instances per Turkic pivot language; and note that auto_research mode exceeds the 200 H100-hour constraint if that constraint applies. ACL 2027 (August 3, 2026 ARR) remains the appropriate primary venue.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MODERATE – Sherkala-Chat (arXiv:2503.01493, March 2025) is a directly relevant uncited work: it instruction-tunes Llama-3.1-8B for Kazakh on 45.3B tokens of Kazakh, English, Russian, and Turkish data, demonstrating that Turkish as an auxiliary training language improves Kazakh performance—the empirical core insight that motivates TWMP's pivot selection. Not citing it leaves a gap reviewers will notice; TWMP should add it as related work and contrast it: Sherkala-Chat uses ad-hoc four-language mixing with full fine-tuning, whereas TWMP provides a principled, generalizable, LoRA-based method parameterized by continuous URIEL+ distances applicable across any agglutinative target.\", \"MODERATE – The DPO preference pair construction specifies 'highest-scoring chosen' and 'lowest-scoring rejected,' where 'scoring' is implicitly language identification confidence from fastText. This means a grammatically garbled Kazakh response with high fastText confidence could be chosen as the preferred response over a coherent Turkish response. No quality filter (perplexity, length heuristic, or instruction-following score) is applied to the chosen pool. Reviewers will ask whether the DPO training signal is noisy precisely for the close-pivot cases where K=8 Kazakh responses are plentiful—yet quality varies most—and for distant pairs where only 1 of 8 samples passes the language filter, leaving little variance to select from. The paper should either add a quality filter (e.g., exclude responses shorter than 20 tokens or with perplexity above a threshold under the base model) or explicitly acknowledge and ablate this as a limitation.\", \"MINOR – Qwen3.5-9B release date: the paper states 'released February 2026' but available information indicates the Qwen3.5 small series (0.8B/2B/4B/9B) became available March 2, 2026—the February date applies to the larger Qwen3.5 medium models (35B-A3B, 27B). This should be corrected to March 2026.\", \"MINOR – The URIEL+ repository URL cited in the approach section ('github.com/Masonshipton25/URIELPlus') does not match the official ACL Anthology-linked repository ('github.com/LeeLanguageLab/URIELPlus'). The URL should match the official publication's repository or the PyPI package ('urielplus') should be referenced instead.\", \"MINOR – The Kyrgyz Aya instance count ('~4.1M instances in the Aya collection language split') could not be independently verified against HuggingFace statistics. Given Kyrgyz is much lower-resource than Turkish, this count depends entirely on machine-translated data volume and should be verified and cited to the HuggingFace dataset page or the Aya Collection paper's per-language appendix before submission.\"]\nFeedback: The generator has addressed all Round 2 issues competently: the multi-source DPO formulation is now precisely specified (chosen = source-language instruction + model-generated target-language response; rejected = source-language instruction + model-generated source-language response), URIEL+ replaces legacy 289-dim features with the 'Less is More' 300-feature Laplacian subset, the staged curriculum has concrete D_25/D_60 percentile anchors and epoch ranges, DCO is cited and differentiated, Aya coverage is verified with a 5,000-instance floor, and auto_research mode is correctly flagged as exceeding the 200 H100h budget. Two moderate issues remain before this is submission-ready: (1) Add Sherkala-Chat (arXiv:2503.01493) to related work—it is a directly adjacent March 2025 paper training Llama-3.1 on Kazakh+Turkish+Russian and provides empirical motivation for TWMP's pivot selection logic. The contrast is easy: Sherkala-Chat is language-specific full fine-tuning with ad-hoc pivot choice; TWMP is generalizable LoRA-based training with principled URIEL+ weighting. (2) Address the DPO pair quality concern: define 'highest-scoring' explicitly as language ID confidence, acknowledge that this does not filter for response quality, and either add a minimal quality gate (e.g., minimum response length or base-model perplexity cap) or include it as a stated limitation with an ablation that shows the fastText-only selection is adequate in practice. Fix the three minor issues (Qwen3.5 release date, URIEL+ repo URL, Kyrgyz instance count verification) before submitting. ACL 2027 (August 3, 2026 ARR) remains the appropriate primary target; given these are all fixable within days, the paper is on track.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:16:15.733Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:16:15.733Z",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

## Round 1

51 recorded events

### User

_source line 3 · 2026-05-10T07:16:15.774Z_

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

## Idea under review (round 4/10)
{
  "title": "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning",
  "core_problem": "Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.",
  "opportunity": "Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K Kazakh-language questions spanning STEM, humanities, and social sciences sourced from authentic educational materials; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.",
  "landscape": "PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.",
  "approach": "We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\n\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\n\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/Masonshipton25/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 on typological alignment tasks versus ρ=0.260 for the full 800-feature set while also improving downstream cross-lingual NLP performance, we apply this feature selection before computing cosine distances. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\n\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\n\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\n\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; pair the highest-scoring chosen with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples are discarded. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\n\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released February 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh, MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG and CLO serve as primary baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO baselines, URIEL+ sub-space ablations, curriculum schedule variants, and DPO prerequisite probe runs)",
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
    "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP]",
    "Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset (ρ=0.358) outperforms full 800-feature URIEL+ (ρ=0.260) for typological alignment and downstream cross-lingual NLP; justifies TWMP's feature selection step]",
    "Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]",
    "TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]",
    "Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]",
    "KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark, 23K questions, peer-reviewed]",
    "MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]",
    "TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]",
    "Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]",
    "Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)",
    "Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)",
    "Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]",
    "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]"
  ],
  "description": "This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358 vs. ρ=0.260 for the full 800-feature set) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B and applying fastText language identification, requiring no target-language training labels. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency per source-target pair; pairs failing this check fall back to SFT-only. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU, MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.",
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
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "bdc5db3e-069e-4764-a40f-a6a1224f867c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:16:15.770Z_

```json
{
  "parentUuid": "bdc5db3e-069e-4764-a40f-a6a1224f867c",
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
  "uuid": "a1a7a8f6-19fc-45dd-a0fe-a2de5828f9e4",
  "timestamp": "2026-05-10T07:16:15.770Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:16:15.770Z_

```json
{
  "parentUuid": "a1a7a8f6-19fc-45dd-a0fe-a2de5828f9e4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "11fc78d7-360e-4c24-af51-8e9a03dd5f05",
  "timestamp": "2026-05-10T07:16:15.770Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
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
  "leafUuid": "11fc78d7-360e-4c24-af51-8e9a03dd5f05",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Typologically-Weighted Multi-Pivot Instruction Tuning for Turkic Languages",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:16:28.738Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this Round 4 submission of the TWMP paper. I need to independently verify the claims, check for any remaining issues from previous rounds, and assess whether the paper is now ready to pass or still needs revision.

Let me first review what's been addressed from Round 3:
1. Sherkala-Chat (arXiv:2503.01493) needs to be added
2. DPO pair quality concern - needs quality filter or ablation
3. Minor issues: Qwen3.5 release date, URIEL+ repo URL, Kyrgyz instance count

Looking at the current Round 4 submission, let me check what's been addressed:


Sherkala-Chat still isn't appearing in the landscape section or key references, which means that concern remains unresolved. For the DPO pair quality issue, the paper describes using language ID confidence from fastText to separate responses into chosen and rejected pools, then selecting the highest-scoring chosen against the lowest-scoring rejected, but I don't see any quality filtering mechanisms like perplexity thresholds or length constraints being introduced.

There are a few other factual claims I should verify independently: the Qwen3.5 release date listed as February 2026, the URIEL+ repository URL, and the count of Kyrgyz instances in the Aya collection. I'm also going to search for any recent competing work on typological weighting approaches for multilingual instruction tuning that might have been missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11fc78d7-360e-4c24-af51-8e9a03dd5f05",
  "isSidechain": false,
  "requestId": "req_011CatUfopjf2ZBMPEkp5iNJ",
  "type": "assistant",
  "uuid": "1c210440-12cc-4bea-aac8-eb457e93961c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0192WL2AgUahZQm5BPEVJncG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19905,
      "cache_read_input_tokens": 11631,
      "output_tokens": 690,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 690,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 19905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19905
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

_source line 9 · 2026-05-10T07:16:28.751Z_

I'll conduct independent research to verify claims and check for remaining issues in this Round 4 submission. Let me run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c210440-12cc-4bea-aac8-eb457e93961c",
  "isSidechain": false,
  "requestId": "req_011CatUfopjf2ZBMPEkp5iNJ",
  "type": "assistant",
  "uuid": "cc220a57-1941-459b-9910-aeee0382e352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0192WL2AgUahZQm5BPEVJncG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19905,
      "cache_read_input_tokens": 11631,
      "output_tokens": 690,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 690,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 19905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19905
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

_source line 10 · 2026-05-10T07:16:28.848Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QTrtGbtr6cwpk3CTxzxW7j`</summary>

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
  "parentUuid": "cc220a57-1941-459b-9910-aeee0382e352",
  "isSidechain": false,
  "requestId": "req_011CatUfopjf2ZBMPEkp5iNJ",
  "type": "assistant",
  "uuid": "ecf92bcf-4e34-4862-803a-4959c6b67912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0192WL2AgUahZQm5BPEVJncG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19905,
      "cache_read_input_tokens": 11631,
      "output_tokens": 690,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 690,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 19905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19905
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

_source line 11 · 2026-05-10T07:16:28.855Z_

<details><summary>↩ Tool result · `toolu_01QTrtGbtr6cwpk3CTxzxW7j`</summary>

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
  "parentUuid": "ecf92bcf-4e34-4862-803a-4959c6b67912",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "78946096-a1f3-4d65-94d1-b23ed5cfab23",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "ecf92bcf-4e34-4862-803a-4959c6b67912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T07:16:31.627Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me run multiple searches in parallel to verify the key claims in the TWMP paper Round 4.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78946096-a1f3-4d65-94d1-b23ed5cfab23",
  "isSidechain": false,
  "requestId": "req_011CatUgmgn6BQiButGURy1e",
  "type": "assistant",
  "uuid": "28b88eae-e10d-4cd0-afb1-ba7e3a148d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YCwSghyvZsdimZEzh8L5wf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1708,
      "cache_read_input_tokens": 31536,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 31536,
          "cache_creation_input_tokens": 1708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1708
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

_source line 13 · 2026-05-10T07:16:32.462Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ZwR4BgKusm2suUeduZNky`</summary>

```json
{
  "query": "Sherkala-Chat Kazakh LLM instruction tuning arXiv 2503.01493"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28b88eae-e10d-4cd0-afb1-ba7e3a148d9b",
  "isSidechain": false,
  "requestId": "req_011CatUgmgn6BQiButGURy1e",
  "type": "assistant",
  "uuid": "2f72d048-9a75-4397-949a-f301a3d90f1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YCwSghyvZsdimZEzh8L5wf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1708,
      "cache_read_input_tokens": 31536,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 31536,
          "cache_creation_input_tokens": 1708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1708
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

_source line 14 · 2026-05-10T07:16:34.061Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PdHBLFXao61CNfM2evYqaj`</summary>

```json
{
  "query": "typological distance weighted multilingual instruction tuning cross-lingual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f72d048-9a75-4397-949a-f301a3d90f1b",
  "isSidechain": false,
  "requestId": "req_011CatUgmgn6BQiButGURy1e",
  "type": "assistant",
  "uuid": "fcdec688-43c6-4799-96d7-c10764e08ab2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YCwSghyvZsdimZEzh8L5wf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1708,
      "cache_read_input_tokens": 31536,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 31536,
          "cache_creation_input_tokens": 1708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1708
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

_source line 15 · 2026-05-10T07:16:34.228Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BiiDAoHW8CCwsbiD2aGub8`</summary>

```json
{
  "query": "Qwen3.5 small series release date 0.8B 2B 4B 9B March 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcdec688-43c6-4799-96d7-c10764e08ab2",
  "isSidechain": false,
  "requestId": "req_011CatUgmgn6BQiButGURy1e",
  "type": "assistant",
  "uuid": "93fb5fa4-9414-4be3-8794-6e275148202a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YCwSghyvZsdimZEzh8L5wf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1708,
      "cache_read_input_tokens": 31536,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 31536,
          "cache_creation_input_tokens": 1708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1708
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

_source line 16 · 2026-05-10T07:16:37.680Z_

<details><summary>↩ Tool result · `toolu_018ZwR4BgKusm2suUeduZNky`</summary>

```text
Web search results for query: "Sherkala-Chat Kazakh LLM instruction tuning arXiv 2503.01493"

Links: [{"title":"[2503.01493] Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting","url":"https://arxiv.org/abs/2503.01493"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh ...","url":"https://arxiv.org/pdf/2503.01493"},{"title":"Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://arxiv.org/html/2503.01493v1"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting","url":"https://arxiv.org/html/2503.01493"},{"title":"inceptionai/Llama-3.1-Sherkala-8B-Chat · Hugging Face","url":"https://huggingface.co/inceptionai/Llama-3.1-Sherkala-8B-Chat"},{"title":"(PDF) Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://www.researchgate.net/publication/389580277_Llama-31-Sherkala-8B-Chat_An_Open_Large_Language_Model_for_Kazakh"},{"title":"Paper page - Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://huggingface.co/papers/2503.01493"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250301493K/abstract"},{"title":"README.md · inceptionai/Llama-3.1-Sherkala-8B-Chat at main","url":"https://huggingface.co/inceptionai/Llama-3.1-Sherkala-8B-Chat/blob/main/README.md?code=true"},{"title":"Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh | alphaXiv","url":"https://www.alphaxiv.org/ko/overview/2503.01493v1"}]

Based on the search results, here's the information about the Sherkala-Chat paper (arXiv 2503.01493):

## Overview

Llama-3.1-Sherkala-8B-Chat, or Sherkala-Chat (8B) for short, is a state-of-the-art instruction-tuned open generative large language model (LLM) designed for Kazakh.

## Model Details

Adapted from the LLaMA-3.1-8B model, Sherkala-Chat (8B) is trained on 45.3B tokens across Kazakh, English, Russian, and Turkish. With 8 billion parameters, it demonstrates strong knowledge and reasoning abilities in Kazakh, significantly outperforming existing open Kazakh and multilingual models of similar scale while achieving competitive performance in English.

## Instruction Tuning Approach

To ensure effective and responsible alignment, we leverage translated instruction datasets, a Kazakhstan-specific instruction dataset that is automatically constructed and manually verified, and Kazakh-specific safety data.

## Performance

With additional instruction fine-tuning (IFT) and safety tuning, Sherkala-Chat (8B) achieves the highest score of 47.6, making it a new benchmark for state-of-the-art Kazakh language models. This represents a +3.9 point improvement over KazLLM-1.0 (8B), a +9.9 point improvement over Irbis-v0.1 (7B), and a significant lead over all multilingual models.

## Availability

The model is released as an open-weight model, along with a detailed description of its training, alignment, and evaluation, to support research and real-world applications for Kazakh speakers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f72d048-9a75-4397-949a-f301a3d90f1b",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "ff49eb7d-f952-4804-a531-bc936bef7840",
  "toolUseResult": {
    "query": "Sherkala-Chat Kazakh LLM instruction tuning arXiv 2503.01493",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y16Nqs528Ynqujq1yLX8LS",
        "content": [
          {
            "title": "[2503.01493] Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting",
            "url": "https://arxiv.org/abs/2503.01493"
          },
          {
            "title": "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh ...",
            "url": "https://arxiv.org/pdf/2503.01493"
          },
          {
            "title": "Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh",
            "url": "https://arxiv.org/html/2503.01493v1"
          },
          {
            "title": "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting",
            "url": "https://arxiv.org/html/2503.01493"
          },
          {
            "title": "inceptionai/Llama-3.1-Sherkala-8B-Chat · Hugging Face",
            "url": "https://huggingface.co/inceptionai/Llama-3.1-Sherkala-8B-Chat"
          },
          {
            "title": "(PDF) Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh",
            "url": "https://www.researchgate.net/publication/389580277_Llama-31-Sherkala-8B-Chat_An_Open_Large_Language_Model_for_Kazakh"
          },
          {
            "title": "Paper page - Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh",
            "url": "https://huggingface.co/papers/2503.01493"
          },
          {
            "title": "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250301493K/abstract"
          },
          {
            "title": "README.md · inceptionai/Llama-3.1-Sherkala-8B-Chat at main",
            "url": "https://huggingface.co/inceptionai/Llama-3.1-Sherkala-8B-Chat/blob/main/README.md?code=true"
          },
          {
            "title": "Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh | alphaXiv",
            "url": "https://www.alphaxiv.org/ko/overview/2503.01493v1"
          }
        ]
      },
      "Based on the search results, here's the information about the Sherkala-Chat paper (arXiv 2503.01493):\n\n## Overview\n\nLlama-3.1-Sherkala-8B-Chat, or Sherkala-Chat (8B) for short, is a state-of-the-art instruction-tuned open generative large language model (LLM) designed for Kazakh.\n\n## Model Details\n\nAdapted from the LLaMA-3.1-8B model, Sherkala-Chat (8B) is trained on 45.3B tokens across Kazakh, English, Russian, and Turkish. With 8 billion parameters, it demonstrates strong knowledge and reasoning abilities in Kazakh, significantly outperforming existing open Kazakh and multilingual models of similar scale while achieving competitive performance in English.\n\n## Instruction Tuning Approach\n\nTo ensure effective and responsible alignment, we leverage translated instruction datasets, a Kazakhstan-specific instruction dataset that is automatically constructed and manually verified, and Kazakh-specific safety data.\n\n## Performance\n\nWith additional instruction fine-tuning (IFT) and safety tuning, Sherkala-Chat (8B) achieves the highest score of 47.6, making it a new benchmark for state-of-the-art Kazakh language models. This represents a +3.9 point improvement over KazLLM-1.0 (8B), a +9.9 point improvement over Irbis-v0.1 (7B), and a significant lead over all multilingual models.\n\n## Availability\n\nThe model is released as an open-weight model, along with a detailed description of its training, alignment, and evaluation, to support research and real-world applications for Kazakh speakers."
    ],
    "durationSeconds": 5.212519122999998
  },
  "sourceToolAssistantUUID": "2f72d048-9a75-4397-949a-f301a3d90f1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T07:16:41.184Z_

<details><summary>↩ Tool result · `toolu_01PdHBLFXao61CNfM2evYqaj`</summary>

```text
Web search results for query: "typological distance weighted multilingual instruction tuning cross-lingual 2025 2026"

Links: [{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090"},{"title":"Cross-Lingual Stability and Bias in Instruction-Tuned Language","url":"https://arxiv.org/pdf/2510.22823"},{"title":"Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"},{"title":"[2404.04659] Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly","url":"https://arxiv.org/abs/2404.04659"},{"title":"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly","url":"https://arxiv.org/html/2404.04659v1"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854"},{"title":"[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/abs/2402.13703"},{"title":"CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/crossin-efficient-instruction-tuning-approach-cross-lingual"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809"}]

I found several relevant research papers on typological distance, multilingual instruction tuning, and cross-lingual transfer. Here are the key findings:

## Recent Research on Typological Distance and Multilingual Instruction Tuning

Research has investigated various language selection techniques including typological feature vectors and language embeddings derived from semantic typology features. Studies have instruction-tuned models using specific language subsets selected through these techniques, measuring cross-lingual and cross-task performance on natural language understanding and commonsense reasoning tasks.

Recent findings show that alignment, not scale, determines stability: aligned models maintain near-invariant accuracy and balanced calibration across typologically distant and low-resource languages.

## Language Diversity in Multilingual Instruction Tuning

Some studies show that scaling the number of tasks or languages during instruction tuning improves cross-lingual generalization, while others report that just 1–3 fine-tuning languages effectively trigger cross-lingual transfer. Research has found that only 40 multilingual examples integrated in an English tuning set substantially improve multilingual instruction-following, and that diversifying the instruction tuning set with even just 2-4 languages significantly improves cross-lingual generalization.

## Weighted Approaches

Instruction-tuning on parallel instead of monolingual corpora benefits cross-lingual instruction following capabilities by up to 9.9%.

The papers indicate that typological distance is being actively researched as a factor in determining optimal language selection and weighting strategies for multilingual instruction tuning in 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcdec688-43c6-4799-96d7-c10764e08ab2",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "c34d9a37-b5f3-46e4-8c79-bc95c971b25f",
  "toolUseResult": {
    "query": "typological distance weighted multilingual instruction tuning cross-lingual 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MN1NFBtsTQNrx6f3WwyHvp",
        "content": [
          {
            "title": "The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation",
            "url": "https://arxiv.org/html/2505.13090"
          },
          {
            "title": "Cross-Lingual Stability and Bias in Instruction-Tuned Language",
            "url": "https://arxiv.org/pdf/2510.22823"
          },
          {
            "title": "Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"
          },
          {
            "title": "[2404.04659] Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly",
            "url": "https://arxiv.org/abs/2404.04659"
          },
          {
            "title": "Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly",
            "url": "https://arxiv.org/html/2404.04659v1"
          },
          {
            "title": "Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?",
            "url": "https://arxiv.org/html/2402.13703v3"
          },
          {
            "title": "Multilingual Instruction Tuning With Just a Pinch of Multilinguality",
            "url": "https://arxiv.org/html/2401.01854"
          },
          {
            "title": "[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?",
            "url": "https://arxiv.org/abs/2402.13703"
          },
          {
            "title": "CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/crossin-efficient-instruction-tuning-approach-cross-lingual"
          },
          {
            "title": "Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?",
            "url": "https://arxiv.org/html/2410.07809"
          }
        ]
      },
      "I found several relevant research papers on typological distance, multilingual instruction tuning, and cross-lingual transfer. Here are the key findings:\n\n## Recent Research on Typological Distance and Multilingual Instruction Tuning\n\nResearch has investigated various language selection techniques including typological feature vectors and language embeddings derived from semantic typology features. Studies have instruction-tuned models using specific language subsets selected through these techniques, measuring cross-lingual and cross-task performance on natural language understanding and commonsense reasoning tasks.\n\nRecent findings show that alignment, not scale, determines stability: aligned models maintain near-invariant accuracy and balanced calibration across typologically distant and low-resource languages.\n\n## Language Diversity in Multilingual Instruction Tuning\n\nSome studies show that scaling the number of tasks or languages during instruction tuning improves cross-lingual generalization, while others report that just 1–3 fine-tuning languages effectively trigger cross-lingual transfer. Research has found that only 40 multilingual examples integrated in an English tuning set substantially improve multilingual instruction-following, and that diversifying the instruction tuning set with even just 2-4 languages significantly improves cross-lingual generalization.\n\n## Weighted Approaches\n\nInstruction-tuning on parallel instead of monolingual corpora benefits cross-lingual instruction following capabilities by up to 9.9%.\n\nThe papers indicate that typological distance is being actively researched as a factor in determining optimal language selection and weighting strategies for multilingual instruction tuning in 2024-2025."
    ],
    "durationSeconds": 7.118380838000001
  },
  "sourceToolAssistantUUID": "fcdec688-43c6-4799-96d7-c10764e08ab2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T07:16:41.981Z_

<details><summary>↩ Tool result · `toolu_01BiiDAoHW8CCwsbiD2aGub8`</summary>

```text
Web search results for query: "Qwen3.5 small series release date 0.8B 2B 4B 9B March 2026"

Links: [{"title":"Qwen 3.5 Small Model Series Release: Local, private, free | STARTUP EDITION","url":"https://blog.mean.ceo/qwen-3-5-small-model-series-release/"},{"title":"Qwen 3.5 Review 2026: The Full Model Family — From 0.8B Edge to 122B Enterprise - ComputerTech","url":"https://computertech.co/qwen-3-5-review/"},{"title":"Qwen 3.5 Small Models: Alibaba Delivers Compact Multimodal Powerhouses | by Nikhil | Neural Notions | Medium","url":"https://medium.com/neuralnotions/qwen-3-5-small-models-alibaba-delivers-compact-multimodal-powerhouses-9520af4d792e"},{"title":"Qwen 3.5 Small Series Review 2026: 120B Performance on 16GB RAM (9B Model Beats GPT-OSS-120B) - ComputerTech","url":"https://computertech.co/qwen-3-5-small-review-2026/"},{"title":"Qwen3.5 is the large language model series ...","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen 3.5 Small Series Ships Four Models From 0.8B to 9B | Awesome Agents","url":"https://awesomeagents.ai/news/qwen-3-5-small-models-series/"},{"title":"Qwen 3.5 Small Model Series released | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/qwen-3-5-small-model-series-released-7a5ed34fcbb3"},{"title":"Qwen 3.5 Hardware Guide — 0.8B to 397B VRAM & GPUs | Compute Market","url":"https://www.compute-market.com/blog/qwen-3-5-local-hardware-guide-2026"},{"title":"Qwen3.5 small models: Everything you need to know","url":"https://artificialanalysis.ai/articles/qwen3-5-small-models"},{"title":"Alibaba's Qwen3.5 Small Series: How 0.8B Models Now Pack Frontier-Level AI Brains | ThePromptBuddy","url":"https://www.thepromptbuddy.com/prompts/alibaba-s-qwen3-5-small-series-how-0-8b-models-now-pack-frontier-level-ai-brains"}]

Based on the search results, here's what I found about the Qwen3.5 Small Series release:

## Release Date

Alibaba released Qwen 3.5 Small Model Series on March 1, 2026, with four variants: 0.8B, 2B, 4B, and 9B parameters. However, some sources indicate the Qwen team launched the Qwen 3.5 Small Model Series on March 2, 2026, so the release occurred around March 1-2, 2026.

## Model Variants

The small series includes exactly the four model sizes you mentioned:
- **0.8B**: the first sub-1B model in history to support video understanding
- **2B**: runs on any recent iPhone in airplane mode, processing both text and images
- **4B**: purpose-built for lightweight multimodal agents
- **9B**: delivers performance matching models with 120 billion parameters, according to independent benchmarks

The series uses a unified Gated DeltaNet hybrid attention (3:1 linear-to-full ratio), multi-token prediction, 262K native context (1M extended on 9B), and a 248K vocabulary across 201 languages.

All four models are Apache 2.0 licensed, with base versions for fine-tuning, available on Hugging Face and ModelScope.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93fb5fa4-9414-4be3-8794-6e275148202a",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "773ab543-f4a8-4cf1-8136-6db85d7f0a29",
  "toolUseResult": {
    "query": "Qwen3.5 small series release date 0.8B 2B 4B 9B March 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fnt8xZnXA8T6Mr6wmrwjxC",
        "content": [
          {
            "title": "Qwen 3.5 Small Model Series Release: Local, private, free | STARTUP EDITION",
            "url": "https://blog.mean.ceo/qwen-3-5-small-model-series-release/"
          },
          {
            "title": "Qwen 3.5 Review 2026: The Full Model Family — From 0.8B Edge to 122B Enterprise - ComputerTech",
            "url": "https://computertech.co/qwen-3-5-review/"
          },
          {
            "title": "Qwen 3.5 Small Models: Alibaba Delivers Compact Multimodal Powerhouses | by Nikhil | Neural Notions | Medium",
            "url": "https://medium.com/neuralnotions/qwen-3-5-small-models-alibaba-delivers-compact-multimodal-powerhouses-9520af4d792e"
          },
          {
            "title": "Qwen 3.5 Small Series Review 2026: 120B Performance on 16GB RAM (9B Model Beats GPT-OSS-120B) - ComputerTech",
            "url": "https://computertech.co/qwen-3-5-small-review-2026/"
          },
          {
            "title": "Qwen3.5 is the large language model series ...",
            "url": "https://github.com/QwenLM/Qwen3.6"
          },
          {
            "title": "Qwen 3.5 Small Series Ships Four Models From 0.8B to 9B | Awesome Agents",
            "url": "https://awesomeagents.ai/news/qwen-3-5-small-models-series/"
          },
          {
            "title": "Qwen 3.5 Small Model Series released | by Mehul Gupta | Data Science in Your Pocket | Medium",
            "url": "https://medium.com/data-science-in-your-pocket/qwen-3-5-small-model-series-released-7a5ed34fcbb3"
          },
          {
            "title": "Qwen 3.5 Hardware Guide — 0.8B to 397B VRAM & GPUs | Compute Market",
            "url": "https://www.compute-market.com/blog/qwen-3-5-local-hardware-guide-2026"
          },
          {
            "title": "Qwen3.5 small models: Everything you need to know",
            "url": "https://artificialanalysis.ai/articles/qwen3-5-small-models"
          },
          {
            "title": "Alibaba's Qwen3.5 Small Series: How 0.8B Models Now Pack Frontier-Level AI Brains | ThePromptBuddy",
            "url": "https://www.thepromptbuddy.com/prompts/alibaba-s-qwen3-5-small-series-how-0-8b-models-now-pack-frontier-level-ai-brains"
          }
        ]
      },
      "Based on the search results, here's what I found about the Qwen3.5 Small Series release:\n\n## Release Date\n\nAlibaba released Qwen 3.5 Small Model Series on March 1, 2026, with four variants: 0.8B, 2B, 4B, and 9B parameters. However, some sources indicate the Qwen team launched the Qwen 3.5 Small Model Series on March 2, 2026, so the release occurred around March 1-2, 2026.\n\n## Model Variants\n\nThe small series includes exactly the four model sizes you mentioned:\n- **0.8B**: the first sub-1B model in history to support video understanding\n- **2B**: runs on any recent iPhone in airplane mode, processing both text and images\n- **4B**: purpose-built for lightweight multimodal agents\n- **9B**: delivers performance matching models with 120 billion parameters, according to independent benchmarks\n\nThe series uses a unified Gated DeltaNet hybrid attention (3:1 linear-to-full ratio), multi-token prediction, 262K native context (1M extended on 9B), and a 248K vocabulary across 201 languages.\n\nAll four models are Apache 2.0 licensed, with base versions for fine-tuning, available on Hugging Face and ModelScope."
    ],
    "durationSeconds": 7.750442619000001
  },
  "sourceToolAssistantUUID": "93fb5fa4-9414-4be3-8794-6e275148202a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "773ab543-f4a8-4cf1-8136-6db85d7f0a29",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Typologically-Weighted Multi-Pivot Instruction Tuning for Turkic Languages",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

### Assistant

_source line 21 · 2026-05-10T07:16:59.905Z_

<details><summary>Logged reasoning block</summary>

```text
Good - I've confirmed:
1. Sherkala-Chat (arXiv:2503.01493) is indeed a real paper about Kazakh LLM instruction tuning using Turkish+Russian+English+Kazakh data.
2. The Qwen3.5 Small Series was released March 1-2, 2026, not February 2026 as stated in the paper. The paper states "released February 2026" which is incorrect.

Let me check the current paper text:
- "Qwen3.5-9B (released February 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists)"


- The approach section still contains the same error—it hasn't been corrected from Round 3 to Round 4, so the February date persists when it should read March 2026.

- The URIEL+ repository URL also remains unchanged; it still points to the incorrect GitHub path instead of the correct LeeLanguageLab repository that was flagged before.

- Sherkala-Chat appears to be completely absent from the current submission, which is a more significant oversight since it was noted as a moderate issue in the previous round.

- The DPO pair quality concern persists as well—the approach still lacks any quality filtering mechanism for the chosen responses, another moderate issue that should have been addressed.

Let me now look for other concurrent work that might be directly competing with TWMP's contributions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "773ab543-f4a8-4cf1-8136-6db85d7f0a29",
  "isSidechain": false,
  "requestId": "req_011CatUhjkix9B6wdbZ44PcC",
  "type": "assistant",
  "uuid": "7d45a944-a37a-42d8-88aa-0a97b3a74172",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YGHiSdfuYvbzk8kMmh1XqG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3324,
      "cache_read_input_tokens": 33244,
      "output_tokens": 853,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 853,
          "cache_read_input_tokens": 33244,
          "cache_creation_input_tokens": 3324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3324
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

_source line 22 · 2026-05-10T07:16:59.994Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AUEix8RFQnJjehpLUFGg61`</summary>

```json
{
  "query": "URIEL+ repository LeeLanguageLab URIELPlus github 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d45a944-a37a-42d8-88aa-0a97b3a74172",
  "isSidechain": false,
  "requestId": "req_011CatUhjkix9B6wdbZ44PcC",
  "type": "assistant",
  "uuid": "028f0a43-b5be-4fd7-a90b-e0455a5af6f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YGHiSdfuYvbzk8kMmh1XqG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3324,
      "cache_read_input_tokens": 33244,
      "output_tokens": 853,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 853,
          "cache_read_input_tokens": 33244,
          "cache_creation_input_tokens": 3324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3324
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

_source line 23 · 2026-05-10T07:17:00.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mo4DrAezqWMradzuTCkmWY`</summary>

```json
{
  "query": "multi-pivot cross-lingual instruction tuning low resource language 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "028f0a43-b5be-4fd7-a90b-e0455a5af6f8",
  "isSidechain": false,
  "requestId": "req_011CatUhjkix9B6wdbZ44PcC",
  "type": "assistant",
  "uuid": "c264e866-3d61-4b0d-ac6e-c482787feaa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YGHiSdfuYvbzk8kMmh1XqG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3324,
      "cache_read_input_tokens": 33244,
      "output_tokens": 853,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 853,
          "cache_read_input_tokens": 33244,
          "cache_creation_input_tokens": 3324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3324
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

_source line 24 · 2026-05-10T07:17:01.105Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JKV7pHb8NAProyUG5sxsD5`</summary>

```json
{
  "query": "Aya dataset Kyrgyz Turkish Uzbek Azerbaijani language coverage instances HuggingFace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c264e866-3d61-4b0d-ac6e-c482787feaa2",
  "isSidechain": false,
  "requestId": "req_011CatUhjkix9B6wdbZ44PcC",
  "type": "assistant",
  "uuid": "f8df4da0-63bf-4243-866e-c6e00712a849",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YGHiSdfuYvbzk8kMmh1XqG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3324,
      "cache_read_input_tokens": 33244,
      "output_tokens": 853,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 853,
          "cache_read_input_tokens": 33244,
          "cache_creation_input_tokens": 3324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3324
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

_source line 25 · 2026-05-10T07:17:05.232Z_

<details><summary>↩ Tool result · `toolu_01AUEix8RFQnJjehpLUFGg61`</summary>

```text
Web search results for query: "URIEL+ repository LeeLanguageLab URIELPlus github 2025"

Links: [{"title":"GitHub - LeeLanguageLab/URIELPlus: URIEL+ knowledge base for natural language processing · GitHub","url":"https://github.com/LeeLanguageLab/URIELPlus"},{"title":"uriel (Uriel) · GitHub","url":"https://github.com/uriel"},{"title":"0x557269656C (Uriel) · GitHub","url":"https://github.com/0x557269656C"},{"title":"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base","url":"https://arxiv.org/html/2409.18472v3"},{"title":"urielplus · PyPI","url":"https://pypi.org/project/urielplus/"},{"title":"URIEL+: Enhancing Linguistic Inclusion and Usability in a ...","url":"https://aclanthology.org/2025.coling-main.463.pdf"},{"title":"UrielLRh (Uriel) · GitHub","url":"https://github.com/UrielLRh"},{"title":"ImUrX (Uriel) · GitHub","url":"https://github.com/ImUrX"},{"title":"My Github pages | urielch.github.io","url":"https://urielch.github.io/"},{"title":"uriel-frankel (Uriel Frankel) · GitHub","url":"https://github.com/uriel-frankel"}]

Based on the search results, here's what I found about the URIEL+ repository:

## URIEL+ Repository Overview

URIEL+ is an enhanced version of URIEL and lang2vec addressing limitations in the original system. 

**Repository Details:**
- **Location:** https://github.com/LeeLanguageLab/URIELPlus
- **Lab:** LeeLanguageLab
- **Publication:** The work was presented at the 31st International Conference on Computational Linguistics in January 2025 in Abu Dhabi, UAE

**Key Features:**

URIEL+ expands typological feature coverage for 2898 languages and improves user experience with robust, customizable distance calculations. Despite URIEL being frequently cited, it was limited in terms of linguistic inclusion and overall usability.

**Available Distribution:**
The package is also available on PyPI (Python Package Index) as "urielplus" for easy installation.

**Purpose:**
URIEL enables seamless integration into machine learning models, facilitating large-scale analysis and supporting diverse tasks, with URIEL+ improving upon these capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "028f0a43-b5be-4fd7-a90b-e0455a5af6f8",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "e54ff063-22cc-4278-ae6f-417106dc149e",
  "toolUseResult": {
    "query": "URIEL+ repository LeeLanguageLab URIELPlus github 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pq8dFUBNdPoVwtNNkvco84",
        "content": [
          {
            "title": "GitHub - LeeLanguageLab/URIELPlus: URIEL+ knowledge base for natural language processing · GitHub",
            "url": "https://github.com/LeeLanguageLab/URIELPlus"
          },
          {
            "title": "uriel (Uriel) · GitHub",
            "url": "https://github.com/uriel"
          },
          {
            "title": "0x557269656C (Uriel) · GitHub",
            "url": "https://github.com/0x557269656C"
          },
          {
            "title": "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base",
            "url": "https://arxiv.org/html/2409.18472v3"
          },
          {
            "title": "urielplus · PyPI",
            "url": "https://pypi.org/project/urielplus/"
          },
          {
            "title": "URIEL+: Enhancing Linguistic Inclusion and Usability in a ...",
            "url": "https://aclanthology.org/2025.coling-main.463.pdf"
          },
          {
            "title": "UrielLRh (Uriel) · GitHub",
            "url": "https://github.com/UrielLRh"
          },
          {
            "title": "ImUrX (Uriel) · GitHub",
            "url": "https://github.com/ImUrX"
          },
          {
            "title": "My Github pages | urielch.github.io",
            "url": "https://urielch.github.io/"
          },
          {
            "title": "uriel-frankel (Uriel Frankel) · GitHub",
            "url": "https://github.com/uriel-frankel"
          }
        ]
      },
      "Based on the search results, here's what I found about the URIEL+ repository:\n\n## URIEL+ Repository Overview\n\nURIEL+ is an enhanced version of URIEL and lang2vec addressing limitations in the original system. \n\n**Repository Details:**\n- **Location:** https://github.com/LeeLanguageLab/URIELPlus\n- **Lab:** LeeLanguageLab\n- **Publication:** The work was presented at the 31st International Conference on Computational Linguistics in January 2025 in Abu Dhabi, UAE\n\n**Key Features:**\n\nURIEL+ expands typological feature coverage for 2898 languages and improves user experience with robust, customizable distance calculations. Despite URIEL being frequently cited, it was limited in terms of linguistic inclusion and overall usability.\n\n**Available Distribution:**\nThe package is also available on PyPI (Python Package Index) as \"urielplus\" for easy installation.\n\n**Purpose:**\nURIEL enables seamless integration into machine learning models, facilitating large-scale analysis and supporting diverse tasks, with URIEL+ improving upon these capabilities."
    ],
    "durationSeconds": 5.233174831999997
  },
  "sourceToolAssistantUUID": "028f0a43-b5be-4fd7-a90b-e0455a5af6f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T07:17:07.294Z_

<details><summary>↩ Tool result · `toolu_01JKV7pHb8NAProyUG5sxsD5`</summary>

```text
Web search results for query: "Aya dataset Kyrgyz Turkish Uzbek Azerbaijani language coverage instances HuggingFace"

Links: [{"title":"CohereLabs/aya_collection_language_split · Datasets at Hugging Face","url":"https://huggingface.co/datasets/CohereLabs/aya_collection_language_split"},{"title":"CohereLabs/aya-101 · Hugging Face","url":"https://huggingface.co/CohereLabs/aya-101"},{"title":"ISSAI · GitHub","url":"https://github.com/IS2AI"},{"title":"Paper page - Aya Dataset: An Open-Access Collection for Multilingual Instruction Tuning","url":"https://huggingface.co/papers/2402.06619"},{"title":"Dataset Catalog | Open Trusted Data Initiative","url":"https://the-ai-alliance.github.io/open-trusted-data-initiative/catalog/"},{"title":"CohereLabs/aya_dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/CohereLabs/aya_dataset"},{"title":"SEACrowd/aya_dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SEACrowd/aya_dataset"},{"title":"Aya Datasets - a CohereLabs Collection","url":"https://huggingface.co/collections/CohereLabs/aya-datasets"},{"title":"GitHub - alexeyev/awesome-kyrgyz-nlp: Kyrgyz language processing software, models and datasets.","url":"https://github.com/alexeyev/awesome-kyrgyz-nlp"},{"title":"[2402.06619] Aya Dataset: An Open-Access Collection for Multilingual Instruction Tuning","url":"https://arxiv.org/abs/2402.06619"}]

Based on the search results, here's information about the Aya dataset's coverage of the languages you mentioned:

## Language Coverage

The Aya Collection includes coverage for Kyrgyz (4.13M rows), North Azerbaijani (4.12M rows), and Northern Uzbek (4.12M rows). Additionally, the collection incorporates instruction-style templates from fluent speakers and applies them to a curated list of datasets, as well as translations of instruction-style datasets into 101 languages.

## Overall Dataset Scale

The Aya Collection is a massive multilingual collection consisting of 513 million instances of prompts and completions covering a wide range of tasks. The Aya Dataset itself (the human-curated component) contains a total of 204k human-annotated prompt-completion pairs along with the demographics data of the annotators, and spans 65 languages (71 including dialects & scripts).

Regarding Turkish specifically, while the search results confirm it's part of the broader Aya initiative (as evidenced by example code showing Turkish translation), the exact instance count for Turkish wasn't specified in the language breakdown table excerpt provided.

These datasets are available on HuggingFace through the CohereLabs organization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8df4da0-63bf-4243-866e-c6e00712a849",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "cace07f5-a6be-4fc9-8949-a6675789bb34",
  "toolUseResult": {
    "query": "Aya dataset Kyrgyz Turkish Uzbek Azerbaijani language coverage instances HuggingFace",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nq4wME3crBAzy4RYxGU5Ag",
        "content": [
          {
            "title": "CohereLabs/aya_collection_language_split · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/CohereLabs/aya_collection_language_split"
          },
          {
            "title": "CohereLabs/aya-101 · Hugging Face",
            "url": "https://huggingface.co/CohereLabs/aya-101"
          },
          {
            "title": "ISSAI · GitHub",
            "url": "https://github.com/IS2AI"
          },
          {
            "title": "Paper page - Aya Dataset: An Open-Access Collection for Multilingual Instruction Tuning",
            "url": "https://huggingface.co/papers/2402.06619"
          },
          {
            "title": "Dataset Catalog | Open Trusted Data Initiative",
            "url": "https://the-ai-alliance.github.io/open-trusted-data-initiative/catalog/"
          },
          {
            "title": "CohereLabs/aya_dataset · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/CohereLabs/aya_dataset"
          },
          {
            "title": "SEACrowd/aya_dataset · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/SEACrowd/aya_dataset"
          },
          {
            "title": "Aya Datasets - a CohereLabs Collection",
            "url": "https://huggingface.co/collections/CohereLabs/aya-datasets"
          },
          {
            "title": "GitHub - alexeyev/awesome-kyrgyz-nlp: Kyrgyz language processing software, models and datasets.",
            "url": "https://github.com/alexeyev/awesome-kyrgyz-nlp"
          },
          {
            "title": "[2402.06619] Aya Dataset: An Open-Access Collection for Multilingual Instruction Tuning",
            "url": "https://arxiv.org/abs/2402.06619"
          }
        ]
      },
      "Based on the search results, here's information about the Aya dataset's coverage of the languages you mentioned:\n\n## Language Coverage\n\nThe Aya Collection includes coverage for Kyrgyz (4.13M rows), North Azerbaijani (4.12M rows), and Northern Uzbek (4.12M rows). Additionally, the collection incorporates instruction-style templates from fluent speakers and applies them to a curated list of datasets, as well as translations of instruction-style datasets into 101 languages.\n\n## Overall Dataset Scale\n\nThe Aya Collection is a massive multilingual collection consisting of 513 million instances of prompts and completions covering a wide range of tasks. The Aya Dataset itself (the human-curated component) contains a total of 204k human-annotated prompt-completion pairs along with the demographics data of the annotators, and spans 65 languages (71 including dialects & scripts).\n\nRegarding Turkish specifically, while the search results confirm it's part of the broader Aya initiative (as evidenced by example code showing Turkish translation), the exact instance count for Turkish wasn't specified in the language breakdown table excerpt provided.\n\nThese datasets are available on HuggingFace through the CohereLabs organization."
    ],
    "durationSeconds": 6.185614495000002
  },
  "sourceToolAssistantUUID": "f8df4da0-63bf-4243-866e-c6e00712a849",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T07:17:08.779Z_

<details><summary>↩ Tool result · `toolu_01Mo4DrAezqWMradzuTCkmWY`</summary>

```text
Web search results for query: "multi-pivot cross-lingual instruction tuning low resource language 2025 2026 arXiv"

Links: [{"title":"[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/abs/2311.08711"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"[2510.07074] LuxInstruct: A Cross-Lingual Instruction Tuning Dataset For Luxembourgish","url":"https://arxiv.org/abs/2510.07074"},{"title":"From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora","url":"https://arxiv.org/html/2505.14045v4"},{"title":"LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks","url":"https://arxiv.org/html/2412.12499v1"},{"title":"Cross-lingual Collapse: How Language-Centric Foundation Models Shape Reasoning in Large Language Models","url":"https://arxiv.org/html/2506.05850v2"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/pdf/2311.08711"},{"title":"BayLing 2: A Multilingual Large Language Model with Efficient Language Alignment","url":"https://arxiv.org/html/2411.16300"},{"title":"Multilingual Large Language Models: A Systematic Survey","url":"https://arxiv.org/html/2411.11072v1"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning - Paper Detail","url":"https://deeplearn.org/arxiv/431549/plug:-leveraging-pivot-language-in-cross-lingual-instruction-tuning"}]

I found several relevant research papers on arXiv related to your query. Here are the most pertinent results:

## Key Papers Found:

**1. PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (2311.08711)**
This approach utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages. It trains the model to first process instructions in the pivot language, and then produce responses in the target language.

**2. BayLing 2: A Multilingual Large Language Model with Efficient Language Alignment (2411.16300)**
BayLing 2 designates Chinese and English, two high-resource languages, as pivot languages and applies cross-lingual tasks to align 100+ languages to these pivot languages, which facilitates the capabilities transfer from high-resource languages to low-resource languages.

**3. LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks (2412.12499)**
This two-stage instruction tuning framework for enhancing low-resource language tasks integrates an additional language alignment layer into the LLM to adapt a pre-trained multilingual encoder.

**4. From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora (2505.14045)**
Continued pretraining and instruction tuning on large-scale multilingual data have proven to be effective in scaling large language models (LLMs) to low-resource languages.

**5. LuxInstruct: A Cross-Lingual Instruction Tuning Dataset For Luxembourgish (2510.07074)**
Low-resource languages such as Luxembourgish face severe limitations due to the lack of high-quality instruction datasets, and traditional reliance on machine translation often introduces semantic misalignment and cultural inaccuracies.

These papers represent recent advances in cross-lingual instruction tuning techniques specifically designed to address challenges in low-resource language processing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c264e866-3d61-4b0d-ac6e-c482787feaa2",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "9335bcbb-92d8-49de-b0c0-bf972e70da5a",
  "toolUseResult": {
    "query": "multi-pivot cross-lingual instruction tuning low resource language 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A5QuVpeWiyKXkuvvXTaJHG",
        "content": [
          {
            "title": "[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning",
            "url": "https://arxiv.org/abs/2311.08711"
          },
          {
            "title": "Revisiting Multilingual Data Mixtures in Language Model Pretraining",
            "url": "https://arxiv.org/html/2510.25947v1"
          },
          {
            "title": "[2510.07074] LuxInstruct: A Cross-Lingual Instruction Tuning Dataset For Luxembourgish",
            "url": "https://arxiv.org/abs/2510.07074"
          },
          {
            "title": "From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora",
            "url": "https://arxiv.org/html/2505.14045v4"
          },
          {
            "title": "LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks",
            "url": "https://arxiv.org/html/2412.12499v1"
          },
          {
            "title": "Cross-lingual Collapse: How Language-Centric Foundation Models Shape Reasoning in Large Language Models",
            "url": "https://arxiv.org/html/2506.05850v2"
          },
          {
            "title": "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning",
            "url": "https://arxiv.org/pdf/2311.08711"
          },
          {
            "title": "BayLing 2: A Multilingual Large Language Model with Efficient Language Alignment",
            "url": "https://arxiv.org/html/2411.16300"
          },
          {
            "title": "Multilingual Large Language Models: A Systematic Survey",
            "url": "https://arxiv.org/html/2411.11072v1"
          },
          {
            "title": "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning - Paper Detail",
            "url": "https://deeplearn.org/arxiv/431549/plug:-leveraging-pivot-language-in-cross-lingual-instruction-tuning"
          }
        ]
      },
      "I found several relevant research papers on arXiv related to your query. Here are the most pertinent results:\n\n## Key Papers Found:\n\n**1. PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (2311.08711)**\nThis approach utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages. It trains the model to first process instructions in the pivot language, and then produce responses in the target language.\n\n**2. BayLing 2: A Multilingual Large Language Model with Efficient Language Alignment (2411.16300)**\nBayLing 2 designates Chinese and English, two high-resource languages, as pivot languages and applies cross-lingual tasks to align 100+ languages to these pivot languages, which facilitates the capabilities transfer from high-resource languages to low-resource languages.\n\n**3. LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks (2412.12499)**\nThis two-stage instruction tuning framework for enhancing low-resource language tasks integrates an additional language alignment layer into the LLM to adapt a pre-trained multilingual encoder.\n\n**4. From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora (2505.14045)**\nContinued pretraining and instruction tuning on large-scale multilingual data have proven to be effective in scaling large language models (LLMs) to low-resource languages.\n\n**5. LuxInstruct: A Cross-Lingual Instruction Tuning Dataset For Luxembourgish (2510.07074)**\nLow-resource languages such as Luxembourgish face severe limitations due to the lack of high-quality instruction datasets, and traditional reliance on machine translation often introduces semantic misalignment and cultural inaccuracies.\n\nThese papers represent recent advances in cross-lingual instruction tuning techniques specifically designed to address challenges in low-resource language processing."
    ],
    "durationSeconds": 8.163492504000002
  },
  "sourceToolAssistantUUID": "c264e866-3d61-4b0d-ac6e-c482787feaa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T07:17:37.268Z_

<details><summary>Logged reasoning block</summary>

```text
Good findings:
1. URIEL+ repository is at github.com/LeeLanguageLab/URIELPlus - the paper cites github.com/Masonshipton25/URIELPlus which is WRONG. This minor issue from Round 3 was NOT fixed.

2. Aya dataset has Kyrgyz at 4.13M rows, North Azerbaijani at 4.12M rows, Northern Uzbek at 4.12M rows. The paper says "Kyrgyz (~4.1M instances in the Aya collection language split)" - this is CORRECT. 

The Kyrgyz instance count checks out. I'm not finding any major competing work on multi-pivot cross-lingual instruction tuning that the paper hasn't already discussed. Now I need to verify whether Sherkala-Chat made it into the Round 4 submission by checking the landscape section and references more carefully.

Looking at the existing coverage, PLUG established that English-pivot instruction generation helps with multilingual instruction following, though it only tested on typologically similar languages like Chinese, Korean, Italian, and Spanish. TWMP directly tests whether this advantage extends to agglutinative languages with non-Latin scripts like Kazakh, Mongolian, and Uyghur—something PLUG didn't explore. CLO uses DPO-style preference optimization with machine-translated data but keeps English as the fixed source language without exploring how typological distance affects source selection. Family Matters demonstrates that typological proximity matters through language transfer and LoRA merging for Faroese, but it's just a single-language case study without a generalizable training approach. There's also empirical analysis of language family and morphology effects, but again, no proposed training methodology.

Now I'm seeing that Multi-Linguistic LoRA Merging separates task and language adapters but doesn't leverage typological features to weight or parameterize the language adapter. There's also a concurrent DPO-inspired method that enforces factual consistency across 26 languages and 9 LLMs. I'm checking the references to see if Sherkala-Chat appears, and I'm finding a 2026 preprint on cross-lingual transfer for low-resource languages that seems relevant but appears to be a single-author work with limited scope.

Looking at the DPO approach more closely, I notice the paper pairs highest-scoring chosen responses with lowest-scoring rejected ones, discarding instructions that don't yield enough target-language candidates. But there's no explicit quality threshold—no minimum response length or perplexity cap—which was flagged as a moderate issue before. I should also scan for any other competing methods I might have overlooked.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9335bcbb-92d8-49de-b0c0-bf972e70da5a",
  "isSidechain": false,
  "requestId": "req_011CatUjiKDEw14cFpV4aQRf",
  "type": "assistant",
  "uuid": "a25c6de3-97db-4130-a7db-ed17364f03a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DAcvqQpsZ2dJPaQebvCAar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 784,
      "cache_creation_input_tokens": 2540,
      "cache_read_input_tokens": 36568,
      "output_tokens": 1023,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2540,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 784,
          "output_tokens": 1023,
          "cache_read_input_tokens": 36568,
          "cache_creation_input_tokens": 2540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2540
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

_source line 29 · 2026-05-10T07:17:37.357Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T58Gwx2pBq2J7LkTNj5j9k`</summary>

```json
{
  "query": "cross-lingual DPO preference optimization low resource language instruction following 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a25c6de3-97db-4130-a7db-ed17364f03a0",
  "isSidechain": false,
  "requestId": "req_011CatUjiKDEw14cFpV4aQRf",
  "type": "assistant",
  "uuid": "12f55654-e7a9-471e-b8a6-413294637509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DAcvqQpsZ2dJPaQebvCAar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 784,
      "cache_creation_input_tokens": 2540,
      "cache_read_input_tokens": 36568,
      "output_tokens": 1023,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2540,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 784,
          "output_tokens": 1023,
          "cache_read_input_tokens": 36568,
          "cache_creation_input_tokens": 2540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2540
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

_source line 30 · 2026-05-10T07:17:37.365Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EXAji2uFZUVXtPohVL6QL2`</summary>

```json
{
  "query": "Kazakh Mongolian Uyghur multilingual LLM fine-tuning agglutinative instruction tuning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12f55654-e7a9-471e-b8a6-413294637509",
  "isSidechain": false,
  "requestId": "req_011CatUjiKDEw14cFpV4aQRf",
  "type": "assistant",
  "uuid": "7b6b713c-0704-4b12-8333-64dcb0e76b4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DAcvqQpsZ2dJPaQebvCAar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 784,
      "cache_creation_input_tokens": 2540,
      "cache_read_input_tokens": 36568,
      "output_tokens": 1023,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2540,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 784,
          "output_tokens": 1023,
          "cache_read_input_tokens": 36568,
          "cache_creation_input_tokens": 2540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2540
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "7b6b713c-0704-4b12-8333-64dcb0e76b4d",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Typologically-Weighted Multi-Pivot Instruction Tuning for Turkic Languages",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

### Tool result

_source line 33 · 2026-05-10T07:17:45.231Z_

<details><summary>↩ Tool result · `toolu_01T58Gwx2pBq2J7LkTNj5j9k`</summary>

```text
Web search results for query: "cross-lingual DPO preference optimization low resource language instruction following 2026"

Links: [{"title":"Cross-Lingual Optimization for Language Transfer in Large Language Models","url":"https://arxiv.org/html/2505.14297"},{"title":"[2503.04647] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://arxiv.org/abs/2503.04647"},{"title":"Adapting Multilingual LLMs to Low-Resource Languages using Continued Pre-training and Synthetic Corpus","url":"https://arxiv.org/html/2410.14815"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1088/"},{"title":"Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://arxiv.org/pdf/2305.18290"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | Request PDF","url":"https://www.researchgate.net/publication/389649128_Implicit_Cross-Lingual_Rewarding_for_Efficient_Multilingual_Preference_Alignment"},{"title":"LLMs Beyond English: Scaling the Multilingual Capability of LLMs with Cross-Lingual Feedback","url":"https://arxiv.org/html/2406.01771v1"},{"title":"Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"},{"title":"The Post-Training Frontier: RLHF, DPO and Modern Preference Optimization CS224R","url":"https://cs224r.stanford.edu/slides/09_cs224r_rlhf_2026.pdf"},{"title":"LANGUAGE IMBALANCE DRIVEN REWARDING FOR ...","url":"https://openreview.net/pdf?id=Kak2ZH5Itp"}]

I found several highly relevant research papers on cross-lingual DPO (Direct Preference Optimization) for low-resource language instruction following. Here are the key findings:

## Recent Approaches (2025-2026)

A Cross-Lingual Optimization (CLO) strategy aims to effectively transfer LLMs to a target language using translated data. It modifies the Direct Preference Optimization approach to increase the preference for responding in the same language as the input while reducing the preference for responding in different languages. In a resource-limited environment using 6,400 English seed data points and accessible translation models across five LLMs, this method demonstrates superiority in instruction-following ability and NLP benchmarks.

Another recent approach involves capturing learned preferences from well-aligned English models through implicit rewards and transferring them to other languages via iterative training, where an implicit reward model derived from English DPO-aligned models annotates preference relations in cross-lingual instruction-following pairs for multilingual DPO fine-tuning. This approach resulted in a 12.72% average improvement in Win Rate across all training languages on the X-AlpacaEval leaderboard.

## Low-Resource Language Adaptation

Using English-only instruction corpora has been shown to enhance instruction-following capabilities in low-resource languages like Hindi, highlighting cross-lingual transferability of these skills. Mixed-language alignment combining English and target language data can enhance generalization in low-resource settings.

These recent works address the critical challenge of data scarcity in multilingual preference alignment by leveraging cross-lingual transfer mechanisms combined with DPO-based optimization strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12f55654-e7a9-471e-b8a6-413294637509",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "76b87d4f-0896-4af8-a5c5-7b094d789dae",
  "toolUseResult": {
    "query": "cross-lingual DPO preference optimization low resource language instruction following 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0182Khxv9JrgPWc4u7Jm8S2V",
        "content": [
          {
            "title": "Cross-Lingual Optimization for Language Transfer in Large Language Models",
            "url": "https://arxiv.org/html/2505.14297"
          },
          {
            "title": "[2503.04647] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment",
            "url": "https://arxiv.org/abs/2503.04647"
          },
          {
            "title": "Adapting Multilingual LLMs to Low-Resource Languages using Continued Pre-training and Synthetic Corpus",
            "url": "https://arxiv.org/html/2410.14815"
          },
          {
            "title": "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.1088/"
          },
          {
            "title": "Direct Preference Optimization: Your Language Model is Secretly a Reward Model",
            "url": "https://arxiv.org/pdf/2305.18290"
          },
          {
            "title": "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | Request PDF",
            "url": "https://www.researchgate.net/publication/389649128_Implicit_Cross-Lingual_Rewarding_for_Efficient_Multilingual_Preference_Alignment"
          },
          {
            "title": "LLMs Beyond English: Scaling the Multilingual Capability of LLMs with Cross-Lingual Feedback",
            "url": "https://arxiv.org/html/2406.01771v1"
          },
          {
            "title": "Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"
          },
          {
            "title": "The Post-Training Frontier: RLHF, DPO and Modern Preference Optimization CS224R",
            "url": "https://cs224r.stanford.edu/slides/09_cs224r_rlhf_2026.pdf"
          },
          {
            "title": "LANGUAGE IMBALANCE DRIVEN REWARDING FOR ...",
            "url": "https://openreview.net/pdf?id=Kak2ZH5Itp"
          }
        ]
      },
      "I found several highly relevant research papers on cross-lingual DPO (Direct Preference Optimization) for low-resource language instruction following. Here are the key findings:\n\n## Recent Approaches (2025-2026)\n\nA Cross-Lingual Optimization (CLO) strategy aims to effectively transfer LLMs to a target language using translated data. It modifies the Direct Preference Optimization approach to increase the preference for responding in the same language as the input while reducing the preference for responding in different languages. In a resource-limited environment using 6,400 English seed data points and accessible translation models across five LLMs, this method demonstrates superiority in instruction-following ability and NLP benchmarks.\n\nAnother recent approach involves capturing learned preferences from well-aligned English models through implicit rewards and transferring them to other languages via iterative training, where an implicit reward model derived from English DPO-aligned models annotates preference relations in cross-lingual instruction-following pairs for multilingual DPO fine-tuning. This approach resulted in a 12.72% average improvement in Win Rate across all training languages on the X-AlpacaEval leaderboard.\n\n## Low-Resource Language Adaptation\n\nUsing English-only instruction corpora has been shown to enhance instruction-following capabilities in low-resource languages like Hindi, highlighting cross-lingual transferability of these skills. Mixed-language alignment combining English and target language data can enhance generalization in low-resource settings.\n\nThese recent works address the critical challenge of data scarcity in multilingual preference alignment by leveraging cross-lingual transfer mechanisms combined with DPO-based optimization strategies."
    ],
    "durationSeconds": 7.868820694999988
  },
  "sourceToolAssistantUUID": "12f55654-e7a9-471e-b8a6-413294637509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T07:17:47.104Z_

<details><summary>↩ Tool result · `toolu_01EXAji2uFZUVXtPohVL6QL2`</summary>

```text
Web search results for query: "Kazakh Mongolian Uyghur multilingual LLM fine-tuning agglutinative instruction tuning 2025 2026"

Links: [{"title":"Fine-Tuning Large Language Models for Kazakh Text Simplification | MDPI","url":"https://www.mdpi.com/2076-3417/15/15/8344"},{"title":"MiLiC-Eval: Benchmarking Multilingual LLMs for China’s Minority Languages","url":"https://arxiv.org/html/2503.01150v1"},{"title":"The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization","url":"https://www.mdpi.com/2504-2289/9/5/137"},{"title":"Low-Resource Text Classification via Cross-Lingual Language Model Fine-Tuning | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-030-63031-7_17"},{"title":"Pre-training Language Model for Mongolian with Agglutinative Linguistic Knowledge Injection | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/10649807/10649898/10650812.pdf"},{"title":"Low-Resource Text Classiﬁcation via Cross-lingual Language Model Fine-tuning","url":"https://aclanthology.org/2020.ccl-1.92.pdf"},{"title":"Fine-Tuning Methods and Dataset Structures for Multilingual Neural Machine Translation: A Kazakh–English–Russian Case Study in the IT Domain","url":"https://www.mdpi.com/2079-9292/14/15/3126"},{"title":"adaptMLLM: Fine-Tuning Multilingual Language Models on Low-Resource Languages with Integrated LLM Playgrounds","url":"https://www.mdpi.com/2078-2489/14/12/638"},{"title":"Research on morphological knowledge-guided low-resource agglutinative languages-Chinese translation | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-01780-5"},{"title":"(PDF) The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization","url":"https://www.researchgate.net/publication/391931330_The_Development_of_Small-Scale_Language_Models_for_Low-Resource_Languages_with_a_Focus_on_Kazakh_and_Direct_Preference_Optimization"}]

I found several highly relevant research papers and studies from 2025-2026 on multilingual LLM fine-tuning for Kazakh, Mongolian, and Uyghur with focus on agglutinative language handling. Here are the key findings:

## Recent Research (2025-2026)

### 1. **Kazakh Text Simplification with Agglutinative Handling**
Recent work addresses Kazakh-specific error analysis through detailed human evaluation to identify error categories reflecting linguistic features unique to Kazakh, such as agglutinative morphology and flexible syntax. A generative approach for Kazakh text simplification involves fine-tuning multilingual large language models.

### 2. **Multilingual LLM Benchmarking for Minority Languages**
Research addresses minority languages spoken in China, such as Tibetan, Uyghur, Kazakh, and Mongolian. A comprehensive framework tracks how a model's abilities evolve as it learns a new language, providing deeper insights into various language adaptation techniques.

### 3. **Kazakh-Specific Language Model Development**
Recent work compiles rigorously cleaned Kazakh corpora and designs tokenizers that respect the language's agglutinative morphology, mixed-script usage, and diacritics. The model is built in two stages: causal language modeling from scratch followed by instruction tuning, with alignment further refined using Direct Preference Optimization (DPO).

### 4. **Mongolian Agglutinative Knowledge Injection**
Research proposes novel pre-training methods for Mongolian that incorporate a three-stage agglutinative knowledge injection strategy, with early-stage injection converting word sequences to fine-grained sub-word tokens and middle-stage injection designing morphological knowledge-based masking strategies.

### 5. **Machine Translation for Low-Resource Agglutinative Languages**
Studies explore fine-tuning methods and dataset structures for multilingual neural machine translation, comparing single-stage and two-stage fine-tuning approaches for Kazakh, English, and Russian.

### 6. **Morphological Knowledge for Translation**
Kazakh, Uyghur, and Uzbek are characterized as typical low-resource agglutinative languages formed by a combination of a root and derivation affix or several inflection affixes.

These recent papers demonstrate significant progress in addressing the unique morphological and structural challenges of agglutinative languages through specialized fine-tuning and instruction tuning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b6b713c-0704-4b12-8333-64dcb0e76b4d",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "fedee9f5-f516-40c7-b786-b5f39d91bc10",
  "toolUseResult": {
    "query": "Kazakh Mongolian Uyghur multilingual LLM fine-tuning agglutinative instruction tuning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pz6c2bs9uhi4TZmkAF6L79",
        "content": [
          {
            "title": "Fine-Tuning Large Language Models for Kazakh Text Simplification | MDPI",
            "url": "https://www.mdpi.com/2076-3417/15/15/8344"
          },
          {
            "title": "MiLiC-Eval: Benchmarking Multilingual LLMs for China’s Minority Languages",
            "url": "https://arxiv.org/html/2503.01150v1"
          },
          {
            "title": "The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization",
            "url": "https://www.mdpi.com/2504-2289/9/5/137"
          },
          {
            "title": "Low-Resource Text Classification via Cross-Lingual Language Model Fine-Tuning | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/978-3-030-63031-7_17"
          },
          {
            "title": "Pre-training Language Model for Mongolian with Agglutinative Linguistic Knowledge Injection | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/iel8/10649807/10649898/10650812.pdf"
          },
          {
            "title": "Low-Resource Text Classiﬁcation via Cross-lingual Language Model Fine-tuning",
            "url": "https://aclanthology.org/2020.ccl-1.92.pdf"
          },
          {
            "title": "Fine-Tuning Methods and Dataset Structures for Multilingual Neural Machine Translation: A Kazakh–English–Russian Case Study in the IT Domain",
            "url": "https://www.mdpi.com/2079-9292/14/15/3126"
          },
          {
            "title": "adaptMLLM: Fine-Tuning Multilingual Language Models on Low-Resource Languages with Integrated LLM Playgrounds",
            "url": "https://www.mdpi.com/2078-2489/14/12/638"
          },
          {
            "title": "Research on morphological knowledge-guided low-resource agglutinative languages-Chinese translation | Complex & Intelligent Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s40747-025-01780-5"
          },
          {
            "title": "(PDF) The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization",
            "url": "https://www.researchgate.net/publication/391931330_The_Development_of_Small-Scale_Language_Models_for_Low-Resource_Languages_with_a_Focus_on_Kazakh_and_Direct_Preference_Optimization"
          }
        ]
      },
      "I found several highly relevant research papers and studies from 2025-2026 on multilingual LLM fine-tuning for Kazakh, Mongolian, and Uyghur with focus on agglutinative language handling. Here are the key findings:\n\n## Recent Research (2025-2026)\n\n### 1. **Kazakh Text Simplification with Agglutinative Handling**\nRecent work addresses Kazakh-specific error analysis through detailed human evaluation to identify error categories reflecting linguistic features unique to Kazakh, such as agglutinative morphology and flexible syntax. A generative approach for Kazakh text simplification involves fine-tuning multilingual large language models.\n\n### 2. **Multilingual LLM Benchmarking for Minority Languages**\nResearch addresses minority languages spoken in China, such as Tibetan, Uyghur, Kazakh, and Mongolian. A comprehensive framework tracks how a model's abilities evolve as it learns a new language, providing deeper insights into various language adaptation techniques.\n\n### 3. **Kazakh-Specific Language Model Development**\nRecent work compiles rigorously cleaned Kazakh corpora and designs tokenizers that respect the language's agglutinative morphology, mixed-script usage, and diacritics. The model is built in two stages: causal language modeling from scratch followed by instruction tuning, with alignment further refined using Direct Preference Optimization (DPO).\n\n### 4. **Mongolian Agglutinative Knowledge Injection**\nResearch proposes novel pre-training methods for Mongolian that incorporate a three-stage agglutinative knowledge injection strategy, with early-stage injection converting word sequences to fine-grained sub-word tokens and middle-stage injection designing morphological knowledge-based masking strategies.\n\n### 5. **Machine Translation for Low-Resource Agglutinative Languages**\nStudies explore fine-tuning methods and dataset structures for multilingual neural machine translation, comparing single-stage and two-stage fine-tuning approaches for Kazakh, English, and Russian.\n\n### 6. **Morphological Knowledge for Translation**\nKazakh, Uyghur, and Uzbek are characterized as typical low-resource agglutinative languages formed by a combination of a root and derivation affix or several inflection affixes.\n\nThese recent papers demonstrate significant progress in addressing the unique morphological and structural challenges of agglutinative languages through specialized fine-tuning and instruction tuning approaches."
    ],
    "durationSeconds": 9.736038958999998
  },
  "sourceToolAssistantUUID": "7b6b713c-0704-4b12-8333-64dcb0e76b4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-10T07:17:47.109Z_

```json
{
  "parentUuid": "fedee9f5-f516-40c7-b786-b5f39d91bc10",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ee32a4c9-c793-4c31-839d-27041fa789d4",
  "timestamp": "2026-05-10T07:17:47.109Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 36 · 2026-05-10T07:17:54.899Z_

<details><summary>Logged reasoning block</summary>

```text
I found an interesting new paper: "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment" (arXiv:2503.04647, ACL 2025 Findings). This paper uses implicit rewards from English DPO-aligned models and transfers them to other languages through cross-lingual DPO training. This seems quite related to TWMP's DPO component but hasn't been cited by the generator. Let me search for more about this.

Also: "The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization" is directly relevant - it uses DPO for Kazakh, which is the exact target language of TWMP.


I'm digging deeper into the implicit cross-lingual rewarding approach to understand how it might compare to TWMP's methodology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee32a4c9-c793-4c31-839d-27041fa789d4",
  "isSidechain": false,
  "requestId": "req_011CatUnYPzdHkybbkg1FbTc",
  "type": "assistant",
  "uuid": "86dc57ee-ee87-436e-a2d4-36d4cc540359",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MDDU1oz43N93pbypJrZi27",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4118,
      "cache_read_input_tokens": 39108,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 39108,
          "cache_creation_input_tokens": 4118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4118
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

_source line 37 · 2026-05-10T07:17:54.918Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UhvpQdrPCcXgSqKbV4srgs`</summary>

```json
{
  "query": "arXiv 2503.04647 \"Implicit Cross-Lingual Rewarding\" multilingual preference alignment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86dc57ee-ee87-436e-a2d4-36d4cc540359",
  "isSidechain": false,
  "requestId": "req_011CatUnYPzdHkybbkg1FbTc",
  "type": "assistant",
  "uuid": "cc802e96-256a-4ecd-b7f9-d99676d0054f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MDDU1oz43N93pbypJrZi27",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4118,
      "cache_read_input_tokens": 39108,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 39108,
          "cache_creation_input_tokens": 4118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4118
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

_source line 38 · 2026-05-10T07:17:55.346Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AKwHmEoLqcnm2RNKvNCs2w`</summary>

```json
{
  "query": "Sherkala-Chat arXiv 2503.01493 Turkish auxiliary language Kazakh LLM instruction tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc802e96-256a-4ecd-b7f9-d99676d0054f",
  "isSidechain": false,
  "requestId": "req_011CatUnYPzdHkybbkg1FbTc",
  "type": "assistant",
  "uuid": "5f27843d-04b0-4ff4-a468-cecd31435f36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MDDU1oz43N93pbypJrZi27",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4118,
      "cache_read_input_tokens": 39108,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 39108,
          "cache_creation_input_tokens": 4118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4118
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

_source line 39 · 2026-05-10T07:18:00.071Z_

<details><summary>↩ Tool result · `toolu_01AKwHmEoLqcnm2RNKvNCs2w`</summary>

```text
Web search results for query: "Sherkala-Chat arXiv 2503.01493 Turkish auxiliary language Kazakh LLM instruction tuning"

Links: [{"title":"[2503.01493] Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting","url":"https://arxiv.org/abs/2503.01493"},{"title":"Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://arxiv.org/html/2503.01493v1"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting","url":"https://arxiv.org/html/2503.01493"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh ...","url":"https://arxiv.org/pdf/2503.01493"},{"title":"Paper page - Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://huggingface.co/papers/2503.01493"},{"title":"(PDF) Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://www.researchgate.net/publication/389580277_Llama-31-Sherkala-8B-Chat_An_Open_Large_Language_Model_for_Kazakh"},{"title":"inceptionai/Llama-3.1-Sherkala-8B-Chat · Hugging Face","url":"https://huggingface.co/inceptionai/Llama-3.1-Sherkala-8B-Chat"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250301493K/abstract"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting | OpenReview","url":"https://openreview.net/forum?id=wRcTCcb0H5"},{"title":"Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh | alphaXiv","url":"https://www.alphaxiv.org/ko/overview/2503.01493v1"}]

Based on the search results, here's what I found about the paper:

## Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh

Llama-3.1-Sherkala-8B-Chat, or Sherkala-Chat (8B) for short, is a state-of-the-art instruction-tuned open generative large language model (LLM) designed for Kazakh.

### Training Data and Languages

Sherkala-Chat (8B) is trained on 45.3B tokens across Kazakh, English, Russian, and Turkish. According to the paper, Turkish contributes additional linguistic features relevant to the broader Turkic language family.

### Model Architecture and Approach

The model continuously pretrains from the LLaMA-3.1 model, and includes a custom tokenizer that balances Kazakh and English, expanding the vocabulary by 25% to capture Kazakh-specific words and expressions more effectively.

### Instruction Tuning and Safety

The model leverages translated instruction datasets, a Kazakhstan-specific instruction dataset that is automatically constructed and manually verified, and Kazakh-specific safety data.

### Performance

With 8 billion parameters, it demonstrates strong knowledge and reasoning abilities in Kazakh, significantly outperforming existing open Kazakh and multilingual models of similar scale while achieving competitive performance in English.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f27843d-04b0-4ff4-a468-cecd31435f36",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "6defeda7-f242-41b2-917e-e9bc902554da",
  "toolUseResult": {
    "query": "Sherkala-Chat arXiv 2503.01493 Turkish auxiliary language Kazakh LLM instruction tuning",
    "results": [
      {
        "tool_use_id": "srvtoolu_018SApyfA1xg7CP74eKUXwX1",
        "content": [
          {
            "title": "[2503.01493] Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting",
            "url": "https://arxiv.org/abs/2503.01493"
          },
          {
            "title": "Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh",
            "url": "https://arxiv.org/html/2503.01493v1"
          },
          {
            "title": "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting",
            "url": "https://arxiv.org/html/2503.01493"
          },
          {
            "title": "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh ...",
            "url": "https://arxiv.org/pdf/2503.01493"
          },
          {
            "title": "Paper page - Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh",
            "url": "https://huggingface.co/papers/2503.01493"
          },
          {
            "title": "(PDF) Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh",
            "url": "https://www.researchgate.net/publication/389580277_Llama-31-Sherkala-8B-Chat_An_Open_Large_Language_Model_for_Kazakh"
          },
          {
            "title": "inceptionai/Llama-3.1-Sherkala-8B-Chat · Hugging Face",
            "url": "https://huggingface.co/inceptionai/Llama-3.1-Sherkala-8B-Chat"
          },
          {
            "title": "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250301493K/abstract"
          },
          {
            "title": "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting | OpenReview",
            "url": "https://openreview.net/forum?id=wRcTCcb0H5"
          },
          {
            "title": "Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh | alphaXiv",
            "url": "https://www.alphaxiv.org/ko/overview/2503.01493v1"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\n## Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh\n\nLlama-3.1-Sherkala-8B-Chat, or Sherkala-Chat (8B) for short, is a state-of-the-art instruction-tuned open generative large language model (LLM) designed for Kazakh.\n\n### Training Data and Languages\n\nSherkala-Chat (8B) is trained on 45.3B tokens across Kazakh, English, Russian, and Turkish. According to the paper, Turkish contributes additional linguistic features relevant to the broader Turkic language family.\n\n### Model Architecture and Approach\n\nThe model continuously pretrains from the LLaMA-3.1 model, and includes a custom tokenizer that balances Kazakh and English, expanding the vocabulary by 25% to capture Kazakh-specific words and expressions more effectively.\n\n### Instruction Tuning and Safety\n\nThe model leverages translated instruction datasets, a Kazakhstan-specific instruction dataset that is automatically constructed and manually verified, and Kazakh-specific safety data.\n\n### Performance\n\nWith 8 billion parameters, it demonstrates strong knowledge and reasoning abilities in Kazakh, significantly outperforming existing open Kazakh and multilingual models of similar scale while achieving competitive performance in English."
    ],
    "durationSeconds": 4.719505128000004
  },
  "sourceToolAssistantUUID": "5f27843d-04b0-4ff4-a468-cecd31435f36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T07:18:01.374Z_

<details><summary>↩ Tool result · `toolu_01UhvpQdrPCcXgSqKbV4srgs`</summary>

```text
Web search results for query: "arXiv 2503.04647 "Implicit Cross-Lingual Rewarding" multilingual preference alignment"

Links: [{"title":"[2503.04647] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://arxiv.org/abs/2503.04647"},{"title":"GitHub - ZNLP/Implicit-Cross-Lingual-Rewarding: [ACL 2025 Findings] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://github.com/ZNLP/Implicit-Cross-Lingual-Rewarding"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | Request PDF","url":"https://www.researchgate.net/publication/389649128_Implicit_Cross-Lingual_Rewarding_for_Efficient_Multilingual_Preference_Alignment"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual ...","url":"https://www.alphaxiv.org/es/overview/2503.04647v1"},{"title":"[Literature Review] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://www.themoonlight.io/en/review/implicit-cross-lingual-rewarding-for-efficient-multilingual-preference-alignment"},{"title":"Multilingual Preference Alignment via Cross-Lingual Rewarding: A Novel Approach to Language Model Training – The Science Archive","url":"https://thesciencearchive.org/2503-04647v1/"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/implicit-cross-lingual-rewarding-efficient-multilingual-preference"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1088/"},{"title":"arXiv:2503.04647v2 [cs.CL] 5 Jun 2025 Implicit Cross-Lingual Rewarding","url":"https://nlpr-web.ia.ac.cn/cip/ZongPublications/2025/2025-YangWen-FindingsACL.pdf"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://powerdrill.ai/discover/summary-implicit-cross-lingual-rewarding-for-efficient-cm7z9eplok8ty07rs74lrxt4r"}]

I found the paper! Here's what I found about arXiv 2503.04647 "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment":

## Overview
The paper was submitted on March 6, 2025, with a revised version on June 5, 2025, and it was published in the Findings of the Association for Computational Linguistics: ACL 2025.

## Authors
The paper is authored by Wen Yang, Junhong Wu, Chen Wang, Chengqing Zong, and Jiajun Zhang.

## Main Contribution
While Direct Preference Optimization (DPO) has enabled significant progress in aligning English LLMs, multilingual preference alignment is hampered by data scarcity. To address this, the authors propose a novel approach that captures learned preferences from well-aligned English models by implicit rewards and transfers them to other languages through iterative training.

## Methodology
The approach derives an implicit reward model from the logits of an English DPO-aligned model and its corresponding reference model. This reward model is then leveraged to annotate preference relations in cross-lingual instruction-following pairs, using English instructions to evaluate multilingual responses. The annotated data is subsequently used for multilingual DPO fine-tuning, facilitating preference knowledge transfer from English to other languages.

A GitHub repository for the project is available at ZNLP/Implicit-Cross-Lingual-Rewarding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc802e96-256a-4ecd-b7f9-d99676d0054f",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "aaf0accc-ecfd-41fd-b4c1-a90b4ad30f38",
  "toolUseResult": {
    "query": "arXiv 2503.04647 \"Implicit Cross-Lingual Rewarding\" multilingual preference alignment",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PT2vHXAV7waRuXjTNhmfWX",
        "content": [
          {
            "title": "[2503.04647] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment",
            "url": "https://arxiv.org/abs/2503.04647"
          },
          {
            "title": "GitHub - ZNLP/Implicit-Cross-Lingual-Rewarding: [ACL 2025 Findings] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment",
            "url": "https://github.com/ZNLP/Implicit-Cross-Lingual-Rewarding"
          },
          {
            "title": "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | Request PDF",
            "url": "https://www.researchgate.net/publication/389649128_Implicit_Cross-Lingual_Rewarding_for_Efficient_Multilingual_Preference_Alignment"
          },
          {
            "title": "Implicit Cross-Lingual Rewarding for Efficient Multilingual ...",
            "url": "https://www.alphaxiv.org/es/overview/2503.04647v1"
          },
          {
            "title": "[Literature Review] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment",
            "url": "https://www.themoonlight.io/en/review/implicit-cross-lingual-rewarding-for-efficient-multilingual-preference-alignment"
          },
          {
            "title": "Multilingual Preference Alignment via Cross-Lingual Rewarding: A Novel Approach to Language Model Training – The Science Archive",
            "url": "https://thesciencearchive.org/2503-04647v1/"
          },
          {
            "title": "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/implicit-cross-lingual-rewarding-efficient-multilingual-preference"
          },
          {
            "title": "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.1088/"
          },
          {
            "title": "arXiv:2503.04647v2 [cs.CL] 5 Jun 2025 Implicit Cross-Lingual Rewarding",
            "url": "https://nlpr-web.ia.ac.cn/cip/ZongPublications/2025/2025-YangWen-FindingsACL.pdf"
          },
          {
            "title": "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment",
            "url": "https://powerdrill.ai/discover/summary-implicit-cross-lingual-rewarding-for-efficient-cm7z9eplok8ty07rs74lrxt4r"
          }
        ]
      },
      "I found the paper! Here's what I found about arXiv 2503.04647 \"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment\":\n\n## Overview\nThe paper was submitted on March 6, 2025, with a revised version on June 5, 2025, and it was published in the Findings of the Association for Computational Linguistics: ACL 2025.\n\n## Authors\nThe paper is authored by Wen Yang, Junhong Wu, Chen Wang, Chengqing Zong, and Jiajun Zhang.\n\n## Main Contribution\nWhile Direct Preference Optimization (DPO) has enabled significant progress in aligning English LLMs, multilingual preference alignment is hampered by data scarcity. To address this, the authors propose a novel approach that captures learned preferences from well-aligned English models by implicit rewards and transfers them to other languages through iterative training.\n\n## Methodology\nThe approach derives an implicit reward model from the logits of an English DPO-aligned model and its corresponding reference model. This reward model is then leveraged to annotate preference relations in cross-lingual instruction-following pairs, using English instructions to evaluate multilingual responses. The annotated data is subsequently used for multilingual DPO fine-tuning, facilitating preference knowledge transfer from English to other languages.\n\nA GitHub repository for the project is available at ZNLP/Implicit-Cross-Lingual-Rewarding."
    ],
    "durationSeconds": 6.451789640000003
  },
  "sourceToolAssistantUUID": "cc802e96-256a-4ecd-b7f9-d99676d0054f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "aaf0accc-ecfd-41fd-b4c1-a90b4ad30f38",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Typologically-Weighted Multi-Pivot Instruction Tuning for Turkic Languages",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

### Assistant

_source line 43 · 2026-05-10T07:18:36.808Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clearer picture. Let me summarize what I found:

1. **Sherkala-Chat (arXiv:2503.01493)** - confirmed as a real paper with Turkish+English+Russian+Kazakh training. This was flagged as a MODERATE uncited issue in Round 3 and has NOT been added to the Round 4 submission.

2. **Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings)** - This is a relevant uncited paper that uses cross-lingual DPO-style alignment with implicit rewards from English DPO models transferred to other languages. 

The approach differs from TWMP's method—while TWMP relies on multi-pivot source selection and direct preference pair construction, this paper transfers implicit reward signals from English DPO models to other languages, so it definitely warrants citation.

3. **URIEL+ repository** - confirmed at github.com/LeeLanguageLab/URIELPlus, but the paper still incorrectly cites github.com/Masonshipton25/URIELPlus. This MINOR issue from Round 3 remains unfixed.

4. **Qwen3.5-9B release date** - confirmed as March 2, 2026, not February 2026 as stated.

5. **Kyrgyz Aya count** - confirmed as ~4.13M rows, which aligns with the paper's claim of "~4.1M instances".

Looking at what should have been addressed from Round 3, I'm seeing four issues that persist: Sherkala-Chat (arXiv:2503.01493) still isn't included, the DPO pair quality gate remains absent with only fastText language ID in place, the Qwen3.5 release date is still wrong, and the URIEL+ repository URL is still incorrect.

There's also a newly uncited paper I should flag: Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings) which applies cross-lingual DPO with implicit reward transfer from English to other languages—this belongs in the related work section.

Evaluating the paper's overall quality: the core novelty of combining URIEL+ weighted multi-pivot curriculum with multi-source DPO is solid and distinct from prior work, though the missing citations create gaps. The resource estimates seem feasible within budget constraints and the methodology is well-specified with concrete thresholds. The writing is clear with precise formulations and baselines defined. The impact would be meaningful for Turkic and Mongolic communities, though the evaluation scope across three language families may limit broader generalizability claims. What concerns me is that we're in Round 4 and the generator still hasn't fixed the previously flagged issues—particularly the two moderate ones around Sherkala-Chat and DPO quality filtering that have been flagged multiple times.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaf0accc-ecfd-41fd-b4c1-a90b4ad30f38",
  "isSidechain": false,
  "requestId": "req_011CatUobGfJ2z6tfyfyDaFo",
  "type": "assistant",
  "uuid": "476fdbce-4c9d-494a-b7b0-7a00a728a906",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FNAGG9r9nstodvt7wvWte4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1006,
      "cache_creation_input_tokens": 1394,
      "cache_read_input_tokens": 43226,
      "output_tokens": 1281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1006,
          "output_tokens": 1281,
          "cache_read_input_tokens": 43226,
          "cache_creation_input_tokens": 1394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1394
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

_source line 44 · 2026-05-10T07:18:37.636Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015j1Q2Nmh7YdWdELeyVVCiq`</summary>

```json
{
  "query": "\"Implicit Cross-Lingual Rewarding\" 2503.04647 multilingual DPO preference alignment low resource"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "476fdbce-4c9d-494a-b7b0-7a00a728a906",
  "isSidechain": false,
  "requestId": "req_011CatUobGfJ2z6tfyfyDaFo",
  "type": "assistant",
  "uuid": "dd74b9b3-6eb4-4220-bf04-210cbc9891f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FNAGG9r9nstodvt7wvWte4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1006,
      "cache_creation_input_tokens": 1394,
      "cache_read_input_tokens": 43226,
      "output_tokens": 1281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1006,
          "output_tokens": 1281,
          "cache_read_input_tokens": 43226,
          "cache_creation_input_tokens": 1394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1394
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

_source line 45 · 2026-05-10T07:18:38.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013BnFSA6716rbZ9mZhX2wLC`</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline May 2026 multilingual cross-lingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd74b9b3-6eb4-4220-bf04-210cbc9891f4",
  "isSidechain": false,
  "requestId": "req_011CatUobGfJ2z6tfyfyDaFo",
  "type": "assistant",
  "uuid": "82359bea-7643-4f15-a95f-9ffacdb6891e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FNAGG9r9nstodvt7wvWte4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1006,
      "cache_creation_input_tokens": 1394,
      "cache_read_input_tokens": 43226,
      "output_tokens": 1281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1006,
          "output_tokens": 1281,
          "cache_read_input_tokens": 43226,
          "cache_creation_input_tokens": 1394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1394
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

_source line 46 · 2026-05-10T07:18:42.030Z_

<details><summary>↩ Tool result · `toolu_013BnFSA6716rbZ9mZhX2wLC`</summary>

```text
Web search results for query: "EMNLP 2026 ARR submission deadline May 2026 multilingual cross-lingual"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the web search results, here are the key details about EMNLP 2026 ARR submission:

## ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## Important Dates (May 2026)

- ARR submission deadline (long & short papers): May 25, 2026
- Reviewer registration deadline for ALL authors: May 27, 2026

## Critical Update for EMNLP 2026

Since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time, and this choice will be binding.

## Key Details

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

For specific information about multilingual and cross-lingual research topics, you would need to check the full Call for Papers at the official EMNLP 2026 website, as the search results don't specify particular topic areas beyond general NLP research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82359bea-7643-4f15-a95f-9ffacdb6891e",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "277d823f-1f99-439c-890f-672a350f3f0e",
  "toolUseResult": {
    "query": "EMNLP 2026 ARR submission deadline May 2026 multilingual cross-lingual",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VP7RjARiyUeSaQuekXkX5B",
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
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "EMNLP 2026 (@emnlpmeeting) / Posts / X",
            "url": "https://x.com/emnlpmeeting?lang=en"
          },
          {
            "title": "emnlp 2026 - AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/conference/?id=emnlp26"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X",
            "url": "https://x.com/emnlpmeeting/status/2047754845919031450"
          }
        ]
      },
      "Based on the web search results, here are the key details about EMNLP 2026 ARR submission:\n\n## ARR Submission Deadline\n\nThe ARR submission deadline for EMNLP 2026 is May 25, 2026.\n\n## Important Dates (May 2026)\n\n- ARR submission deadline (long & short papers): May 25, 2026\n- Reviewer registration deadline for ALL authors: May 27, 2026\n\n## Critical Update for EMNLP 2026\n\nSince EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time, and this choice will be binding.\n\n## Key Details\n\nEMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.\n\nFor specific information about multilingual and cross-lingual research topics, you would need to check the full Call for Papers at the official EMNLP 2026 website, as the search results don't specify particular topic areas beyond general NLP research."
    ],
    "durationSeconds": 3.937234995999985
  },
  "sourceToolAssistantUUID": "82359bea-7643-4f15-a95f-9ffacdb6891e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-10T07:18:43.934Z_

<details><summary>↩ Tool result · `toolu_015j1Q2Nmh7YdWdELeyVVCiq`</summary>

```text
Web search results for query: ""Implicit Cross-Lingual Rewarding" 2503.04647 multilingual DPO preference alignment low resource"

Links: [{"title":"[2503.04647] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://arxiv.org/abs/2503.04647"},{"title":"GitHub - ZNLP/Implicit-Cross-Lingual-Rewarding: [ACL 2025 Findings] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://github.com/ZNLP/Implicit-Cross-Lingual-Rewarding"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | Request PDF","url":"https://www.researchgate.net/publication/389649128_Implicit_Cross-Lingual_Rewarding_for_Efficient_Multilingual_Preference_Alignment"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual ...","url":"https://www.alphaxiv.org/es/overview/2503.04647v1"},{"title":"Multilingual Preference Alignment via Cross-Lingual Rewarding: A Novel Approach to Language Model Training – The Science Archive","url":"https://thesciencearchive.org/2503-04647v1/"},{"title":"[Literature Review] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://www.themoonlight.io/en/review/implicit-cross-lingual-rewarding-for-efficient-multilingual-preference-alignment"},{"title":"arXiv:2503.04647v2 [cs.CL] 5 Jun 2025 Implicit Cross-Lingual Rewarding","url":"https://nlpr-web.ia.ac.cn/cip/ZongPublications/2025/2025-YangWen-FindingsACL.pdf"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1088/"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/implicit-cross-lingual-rewarding-efficient-multilingual-preference"},{"title":"(PDF) CAPO: Confidence Aware Preference Optimization Learning for Multilingual Preferences","url":"https://www.researchgate.net/publication/397521711_CAPO_Confidence_Aware_Preference_Optimization_Learning_for_Multilingual_Preferences"}]

I found comprehensive information about the paper you're searching for. Here's what I found:

## Paper Overview

"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment" addresses how Direct Preference Optimization (DPO) has enabled significant progress in aligning English LLMs, but multilingual preference alignment is hampered by data scarcity.

## Main Approach

The paper proposes a novel approach that captures learned preferences from well-aligned English models by implicit rewards and transfers them to other languages through iterative training. More specifically, the reward model is leveraged to annotate preference relations in cross-lingual instruction-following pairs, using English instructions to evaluate multilingual responses, and the annotated data is subsequently used for multilingual DPO fine-tuning, facilitating preference knowledge transfer from English to other languages.

## Key Results

The method achieved strong performance on multilingual NLP benchmarks, including the Multilingual ARC challenge, HellaSwag, MMLU, TruthfulQA MC1, and TruthfulQA MC2.

## Publication Details

The paper is authored by Wen Yang, Junhong Wu, Chen Wang, Chengqing Zong, and Jiajun Zhang, and was published in Findings of the Association for Computational Linguistics: ACL 2025. You can find the arXiv version and code repository linked in the search results above.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd74b9b3-6eb4-4220-bf04-210cbc9891f4",
  "isSidechain": false,
  "promptId": "25b1b961-90d8-4ae0-b8e1-2c5c056381d6",
  "type": "user",
  "uuid": "a7ad4a33-18ba-484b-9ea9-dee4605ed7c3",
  "toolUseResult": {
    "query": "\"Implicit Cross-Lingual Rewarding\" 2503.04647 multilingual DPO preference alignment low resource",
    "results": [
      {
        "tool_use_id": "srvtoolu_013NSLi8Yofn8MxuysNEvpK4",
        "content": [
          {
            "title": "[2503.04647] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment",
            "url": "https://arxiv.org/abs/2503.04647"
          },
          {
            "title": "GitHub - ZNLP/Implicit-Cross-Lingual-Rewarding: [ACL 2025 Findings] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment",
            "url": "https://github.com/ZNLP/Implicit-Cross-Lingual-Rewarding"
          },
          {
            "title": "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | Request PDF",
            "url": "https://www.researchgate.net/publication/389649128_Implicit_Cross-Lingual_Rewarding_for_Efficient_Multilingual_Preference_Alignment"
          },
          {
            "title": "Implicit Cross-Lingual Rewarding for Efficient Multilingual ...",
            "url": "https://www.alphaxiv.org/es/overview/2503.04647v1"
          },
          {
            "title": "Multilingual Preference Alignment via Cross-Lingual Rewarding: A Novel Approach to Language Model Training – The Science Archive",
            "url": "https://thesciencearchive.org/2503-04647v1/"
          },
          {
            "title": "[Literature Review] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment",
            "url": "https://www.themoonlight.io/en/review/implicit-cross-lingual-rewarding-for-efficient-multilingual-preference-alignment"
          },
          {
            "title": "arXiv:2503.04647v2 [cs.CL] 5 Jun 2025 Implicit Cross-Lingual Rewarding",
            "url": "https://nlpr-web.ia.ac.cn/cip/ZongPublications/2025/2025-YangWen-FindingsACL.pdf"
          },
          {
            "title": "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.1088/"
          },
          {
            "title": "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/implicit-cross-lingual-rewarding-efficient-multilingual-preference"
          },
          {
            "title": "(PDF) CAPO: Confidence Aware Preference Optimization Learning for Multilingual Preferences",
            "url": "https://www.researchgate.net/publication/397521711_CAPO_Confidence_Aware_Preference_Optimization_Learning_for_Multilingual_Preferences"
          }
        ]
      },
      "I found comprehensive information about the paper you're searching for. Here's what I found:\n\n## Paper Overview\n\n\"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment\" addresses how Direct Preference Optimization (DPO) has enabled significant progress in aligning English LLMs, but multilingual preference alignment is hampered by data scarcity.\n\n## Main Approach\n\nThe paper proposes a novel approach that captures learned preferences from well-aligned English models by implicit rewards and transfers them to other languages through iterative training. More specifically, the reward model is leveraged to annotate preference relations in cross-lingual instruction-following pairs, using English instructions to evaluate multilingual responses, and the annotated data is subsequently used for multilingual DPO fine-tuning, facilitating preference knowledge transfer from English to other languages.\n\n## Key Results\n\nThe method achieved strong performance on multilingual NLP benchmarks, including the Multilingual ARC challenge, HellaSwag, MMLU, TruthfulQA MC1, and TruthfulQA MC2.\n\n## Publication Details\n\nThe paper is authored by Wen Yang, Junhong Wu, Chen Wang, Chengqing Zong, and Jiajun Zhang, and was published in Findings of the Association for Computational Linguistics: ACL 2025. You can find the arXiv version and code repository linked in the search results above."
    ],
    "durationSeconds": 6.292574449999986
  },
  "sourceToolAssistantUUID": "dd74b9b3-6eb4-4220-bf04-210cbc9891f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-10T07:19:11.967Z_

<details><summary>Logged reasoning block</summary>

```text
Key findings:
1. EMNLP 2026 ARR deadline is May 25, 2026 (confirmed) - this is in 15 days from today (May 10, 2026).

2. The "Implicit Cross-Lingual Rewarding" paper (arXiv:2503.04647, ACL 2025 Findings) is a real and relevant paper that uses cross-lingual DPO for multilingual preference alignment - it's not cited in the TWMP paper. However, its approach is different from TWMP: it uses English as the sole source language with an implicit reward model to transfer to other languages. 

TWMP's approach with multi-pivot source selection and typological distance weighting is distinct, but the paper should still cite this work. Now I'm checking what issues from the previous round weren't addressed in the latest submission - there are several unresolved problems including missing citations for Sherkala-Chat, incomplete documentation of the DPO pair quality gate, outdated release date information for Qwen3.5, and an incomplete repository URL.

Beyond those carryover issues, I've spotted a new moderate-level problem: Implicit Cross-Lingual Rewarding from ACL 2025 Findings isn't cited and deserves comparison with TWMP's DPO methodology. The submission targets ACL 2027 primarily with EMNLP 2026 as a backup, and the May 25, 2026 ARR deadline checks out as valid.

Looking at the novelty score, the core contribution still stands as genuinely differentiated, but these citation gaps—particularly Sherkala-Chat's direct empirical evidence for Turkish-to-Kazakh transfer and the missing Implicit Cross-Lingual Rewarding comparison—undermine the related work section's comprehensiveness.

The feasibility looks solid at 4/5 with well-defined thresholds and verified resource constraints, though the DPO quality concern remains: without filtering chosen responses, the training signal could become noisy. Clarity sits at 3.5/5 since the "highest-scoring" criterion for DPO still needs clearer definition, the URIEL+ repository URL is incorrect, and the Qwen3.5 release date error chips away at credibility. Impact potential is also 3.5/5, contingent on whether the approach actually delivers on its cross-lingual transfer promises.

The evaluation across Turkic and Mongolic languages is well-motivated, but using only Swahili as a held-out generalization test limits how much I can claim about broader applicability beyond these agglutinative families. Averaging the scores gives 3.625, which falls short of the 4.0 pass threshold. The same issues keep surfacing across review rounds: Sherkala-Chat remains unaddressed after two flags, the DPO quality problem persists, and there's uncited related work on implicit cross-lingual rewarding that should be acknowledged. Despite solid progress over four rounds, these targeted gaps need resolution before this clears the bar.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7ad4a33-18ba-484b-9ea9-dee4605ed7c3",
  "isSidechain": false,
  "requestId": "req_011CatUrj9WkhshUE23Zvmgj",
  "type": "assistant",
  "uuid": "8c0ff4ca-3ac7-4a42-a222-f6319792094b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01M3rdJdeACiNS1oNgeqNjby",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 3329,
      "cache_read_input_tokens": 44620,
      "output_tokens": 3555,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 929,
          "output_tokens": 3555,
          "cache_read_input_tokens": 44620,
          "cache_creation_input_tokens": 3329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3329
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

_source line 49 · 2026-05-10T07:20:01.931Z_

Now I have enough evidence to render a verdict. Let me compile my findings.

**Summary of independent verification:**

1. **Sherkala-Chat** (arXiv:2503.01493): Confirmed real — Llama-3.1-8B trained on 45.3B tokens of Kazakh+English+Russian+Turkish, with Turkish explicitly contributing Turkic linguistic features. Still **absent** from Round 4 submission despite 2 consecutive rounds of flagging.

2. **URIEL+ repo URL**: Confirmed official repo is `github.com/LeeLanguageLab/URIELPlus`. The submission still cites `github.com/Masonshipton25/URIELPlus` — **not fixed** across 2 rounds.

3. **Qwen3.5-9B release date**: Confirmed March 1–2, 2026. Paper still says "February 2026" — **not fixed** across 2 rounds.

4. **Kyrgyz Aya count**: Independently confirmed ~4.13M rows on HuggingFace — paper's claim of "~4.1M instances" is **accurate**. This minor issue is now resolved.

5. **Implicit Cross-Lingual Rewarding** (arXiv:2503.04647, ACL 2025 Findings): A newly identified uncited paper that uses cross-lingual DPO with implicit reward transfer from English to other languages for multilingual preference alignment. Related to TWMP's DPO component; requires citation and differentiation.

6. **DPO pair quality gate**: Still absent — "highest-scoring chosen" relies solely on fastText language ID confidence with no quality filter. **Not fixed** across 2 rounds.

7. **EMNLP 2026 ARR deadline**: May 25, 2026 confirmed valid; 15 days from today.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The URIEL+ weighted multi-pivot curriculum plus multi-source DPO extension remains genuinely differentiated from TIPA, arXiv:2410.07809, and CLO, but the persistent omission of Sherkala-Chat (a directly adjacent Turkish+Kazakh transfer paper) and Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings, cross-lingual DPO for multilingual alignment) leaves holes that EMNLP reviewers will flag and that could materially weaken the novelty argument."
    },
    "feasibility": {
      "score": 4,
      "rationale": "Resource estimates are internally consistent and budget-compliant for manual (~120 H100h) and human-in-loop (~186 H100h) modes; the 5,000-instance Aya floor and 500-instruction prerequisite probe are concrete safeguards. The unaddressed DPO pair quality issue introduces noise risk for close-pivot language pairs with many low-quality K=8 candidates."
    },
    "clarity": {
      "score": 3,
      "rationale": "The staged curriculum (D_25/D_60 percentile anchors) and multi-source DPO objective are now precisely specified, but 'highest-scoring chosen' still lacks a definition of the scoring criterion, the wrong URIEL+ repo URL persists, and the incorrect Qwen3.5 release date remains — three small errors that collectively undermine reproducibility credibility."
    },
    "impact": {
      "score": 4,
      "rationale": "Targeting three ACL 2025 peer-reviewed benchmarks covering Kazakh, Mongolian, and Uyghur — language families where GPT-4 and Llama-3.1 underperform substantially — addresses a high-value gap; the Swahili generalization target strengthens the cross-family claim beyond Turkic."
    }
  },
  "issues": [
    "MODERATE – Sherkala-Chat (arXiv:2503.01493) was flagged in Round 3 as a key uncited adjacent work and remains absent from Round 4. This paper trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish, directly demonstrating that Turkish as an auxiliary language improves Kazakh performance — the empirical core claim motivating TWMP's pivot selection logic. EMNLP reviewers familiar with Kazakh NLP will notice this omission immediately. Required: add to related work section with explicit contrast (Sherkala-Chat uses ad-hoc 4-language full fine-tuning for Kazakh specifically; TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target).",
    "MODERATE – DPO pair quality gate still absent. The approach specifies 'pair the highest-scoring chosen with the lowest-scoring rejected' based on fastText language ID confidence alone, with no quality filter. For close-pivot pairs (Turkish→Kazakh), K=8 sampling may yield 5–7 Kazakh responses, creating a large chosen pool with highly variable quality; the 'highest-scoring' fastText criterion selects the response with the highest Kazakh language ID confidence, which is not correlated with response coherence or instruction-following quality. A grammatically garbled but confidently Kazakh response will be preferred over a fluent but lower-confidence response. This was raised in Round 3 and remains unaddressed. Fix: add a minimum response length gate (e.g., ≥20 tokens) or base-model perplexity cap, or include an explicit ablation comparing fastText-only selection vs. a quality-gated variant and acknowledge this as a limitation with empirical validation.",
    "MODERATE – Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings) is uncited and directly relevant to TWMP's DPO component. This paper uses implicit reward transfer from English DPO models to annotate cross-lingual preference pairs for multilingual DPO fine-tuning, achieving 12.72% average Win Rate improvement on X-AlpacaEval across training languages. While the approach differs from TWMP (English-only source, implicit reward annotation, no typological weighting), it represents active concurrent work on cross-lingual DPO alignment that EMNLP reviewers will expect to see cited and contrasted. Required addition to related work: differentiate TWMP's direct construction of multi-source preference pairs via language ID vs. this paper's implicit reward annotation from a single English-aligned model.",
    "MINOR – Qwen3.5-9B release date error persists for the third consecutive round. The submission states 'released February 2026' but independent verification (multiple sources) confirms the Qwen3.5 small series (0.8B/2B/4B/9B) was released March 1–2, 2026, with February 2026 referring to the larger Qwen3.5 medium models (35B-A3B, 27B). Change 'released February 2026' to 'released March 2026'.",
    "MINOR – URIEL+ repository URL persists as incorrect for the third consecutive round. The submission cites 'github.com/Masonshipton25/URIELPlus' but the official ACL Anthology-linked repository is 'github.com/LeeLanguageLab/URIELPlus' (confirmed). Change to the correct URL or cite the PyPI package 'urielplus' instead."
  ],
  "feedback": "This is Round 4 and the same four issues (Sherkala-Chat, DPO quality gate, release date, repo URL) that were flagged in Round 3 have not been addressed. The pattern is concerning for an ARR deadline in 15 days. Here is exactly what needs to change, in priority order:\n\n(1) Add Sherkala-Chat to Section 2 related work. One paragraph is sufficient: 'Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish, demonstrating that Turkish as an auxiliary language improves Kazakh performance—motivating our choice of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc pivot selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language.'\n\n(2) Add Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings) to Section 2. One sentence: 'Implicit Cross-Lingual Rewarding annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving strong multilingual alignment from English-only source data—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from this work.'\n\n(3) Fix the DPO quality issue. Choose one of: (a) add a minimum 20-token length gate to the chosen pool and state it explicitly; (b) add a perplexity cap at 2× base-model perplexity on the instruction; or (c) keep the current fastText-only selection but add a clearly labeled limitation paragraph and one ablation row in Table X comparing fastText-only vs. length-gated selection. Option (c) requires the least implementation effort and is acceptable.\n\n(4) Fix two one-line errors: 'released February 2026' → 'released March 2026'; 'github.com/Masonshipton25/URIELPlus' → 'github.com/LeeLanguageLab/URIELPlus'.\n\nNone of these require new experiments. Issues (1), (2), (4) are writing-only changes. Issue (3) option (c) requires one additional experiment row or a paragraph addition. The paper is substantively sound and the core novelty claim is defensible—these are editorial and citation completeness fixes that are blocking an otherwise strong submission. ACL 2027 (August 3, 2026 ARR) remains the more realistic target, but if the team has existing QLoRA infrastructure, EMNLP 2026 (May 25 ARR) is feasible after these four fixes.",
  "reason": "Four issues from Round 3 remain unaddressed after two consecutive rounds of flagging: Sherkala-Chat omission, DPO pair quality gate, Qwen3.5 release date error, and wrong URIEL+ repo URL; plus a newly identified uncited relevant work (Implicit Cross-Lingual Rewarding, ACL 2025 Findings). Average score 3.5 is below the 4.0 pass threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c0ff4ca-3ac7-4a42-a222-f6319792094b",
  "isSidechain": false,
  "requestId": "req_011CatUrj9WkhshUE23Zvmgj",
  "type": "assistant",
  "uuid": "ca8bc227-7c31-4985-a10a-e603595ce5e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01M3rdJdeACiNS1oNgeqNjby",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 3329,
      "cache_read_input_tokens": 44620,
      "output_tokens": 3555,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 929,
          "output_tokens": 3555,
          "cache_read_input_tokens": 44620,
          "cache_creation_input_tokens": 3329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3329
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

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ca8bc227-7c31-4985-a10a-e603595ce5e2",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Typologically-Weighted Multi-Pivot Instruction Tuning for Turkic Languages",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ca8bc227-7c31-4985-a10a-e603595ce5e2",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Typologically-Weighted Multi-Pivot Instruction Tuning for Turkic Languages",
  "sessionId": "0703e2f2-7ac0-4ac2-8162-db16255314e0"
}
```

---
