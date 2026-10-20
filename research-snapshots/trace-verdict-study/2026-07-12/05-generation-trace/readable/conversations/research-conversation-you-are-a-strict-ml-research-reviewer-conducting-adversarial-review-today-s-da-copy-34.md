# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/dafd8ad2-3dfd-4271-968b-e119b82cd34e.jsonl`
- **Structured JSON:** [`7edafa42733307780e89.json`](../../sessions/7e/7edafa42733307780e89.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:55:26.124Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:55:26.124Z",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Multilingualism and Cross-Lingual NLP.\n\nDirection: Cross-lingual transfer and multilingual NLP methods. In-scope: cross-lingual transfer without parallel data, multilingual instruction tuning strategies, language-agnostic representations, low-resource language adaptation, cross-lingual retrieval, multilingual reasoning, code-switching handling. ACL 2025 outstanding papers highlighted multilingual gaps and cross-lingual intervention methods.\n\nContribution type: METHOD ONLY. New training recipes, transfer algorithms, or adaptation techniques. Not a new multilingual dataset or language-specific analysis.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Multilingual experiments need coverage across languages — budget for LoRA fine-tuning on multilingual models, not full pretraining.\n2. Time: ≤16 days. Use existing multilingual models (BLOOM, mT5, XLM-R, Aya, Qwen multilingual, Llama-3 multilingual).\n3. Eval: XTREME-UP, XCOPA, XStoryCloze, MGSM, multilingual MMLU, TyDi QA, FLORES for MT.\n\nLook for: efficient cross-lingual transfer with minimal target-language data, multilingual reasoning without English-centric bias, representation alignment methods, adaptation techniques for typologically diverse languages. Avoid: English-only experiments, monolingual fine-tuning.\n\nTag: direction=multilingual, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 7/10)\n{\n  \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning\",\n  \"core_problem\": \"Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.\",\n  \"opportunity\": \"Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K Kazakh-language questions spanning STEM, humanities, and social sciences sourced from authentic educational materials; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.\",\n  \"landscape\": \"PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer [arXiv:2603.27651, SIGIR 2026] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address. Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target. Revisiting Multilingual Data Mixtures [Foroutan et al., 2025, arXiv:2510.25947] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.\",\n  \"approach\": \"We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\\n\\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\\n\\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 on typological alignment tasks versus ρ=0.260 for the full 800-feature set while also improving downstream cross-lingual NLP performance, we apply this feature selection before computing cosine distances. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\\n\\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\\n\\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\\n\\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\\n\\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh, MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG and CLO serve as primary baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO baselines, URIEL+ sub-space ablations, curriculum schedule variants, DPO quality gate ablation row, and DPO prerequisite probe runs)\",\n      \"gpu_utilization\": \"LOW (~25–35%): GPU sits idle during code writing, debugging, data pipeline work, result analysis, and paper writing; runs are launched manually and often queue overnight\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$300 (200h × $1.50/h on Lambda Labs A100)\",\n      \"h100_equivalent\": \"~120h H100 (within ≤200 H100-hour budget constraint at typical A100/H100 performance ratio of ~0.6×)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~310h A100 (agent explores broader hyperparameter space with human approval gates; ~55% more runs than manual)\",\n      \"gpu_utilization\": \"MODERATE (~55–65%): agent queues follow-up experiments immediately after each run completes, filling GPU idle between human check-ins\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in to approve experiment configs and review intermediate results\",\n      \"claude_api_cost\": \"~$150–250 (~1,500–2,500 conversation turns coordinating experiment scheduling, result parsing, and ablation planning)\",\n      \"estimated_gpu_cost\": \"~$465 (310h × $1.50/h)\",\n      \"h100_equivalent\": \"~186h H100 (within ≤200 H100-hour budget constraint at ~0.6× A100/H100 ratio, leaving ~14h headroom)\",\n      \"risk_note\": \"Choice of URIEL+ feature subspace (full 800-feature vs. Laplacian 300-feature vs. syntax-only) and the DPO prerequisite probe threshold require human judgment at key decision points; an automated agent may converge on a locally optimal weighting scheme that under-performs on the held-out Swahili generalization target\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~600h A100 (3–5× more experiments: grid search over distance metrics, curriculum schedule shapes, LoRA rank/alpha, 5+ target languages including Swahili and Kyrgyz for generalization, plus replication runs)\",\n      \"gpu_utilization\": \"NEAR-ZERO idle—agent schedules jobs back-to-back across all target languages in parallel, launches follow-up ablations immediately on job completion, and runs nightly sweeps without human bottleneck\",\n      \"timeline\": \"5–10 days with 4× concurrent A100s; ~3 weeks on a single A100\",\n      \"team\": \"0 (initial setup of experiment configs, data paths, and evaluation harness only)\",\n      \"claude_api_cost\": \"~$400–650 (~4,000–6,500 turns for full experiment orchestration, result parsing, ablation tree exploration, and report drafting)\",\n      \"estimated_gpu_cost\": \"~$900 (600h × $1.50/h)\",\n      \"h100_equivalent\": \"~360h H100 — EXCEEDS the ≤200 H100-hour hard budget constraint. Auto_research mode is documented for completeness but is NOT a viable deployment option within the stated budget. Use manual mode (~120 H100h) or human_in_loop mode (~186 H100h) to remain within budget.\",\n      \"speed_bottleneck\": \"GPU count is the primary bottleneck: 4 concurrent A100s reduces wall-clock time to ~5 days; API rate limits become secondary when running >8 parallel experiment threads\",\n      \"risk_note\": \"CONSTRAINT VIOLATION: 600 A100h ≈ 360 H100h, exceeding the ≤200 H100-hour hard budget. Additionally, unconstrained exploration may overfit the URIEL+ weighting function to the 3 initial target languages; Swahili as a held-out agglutinative target is required to detect this overfitting early.\"\n    }\n  },\n  \"target_venues\": [\n    \"ACL 2027 (ARR submission deadline August 3, 2026) — primary target; provides adequate time for validation on additional typological clusters beyond Turkic–Mongolic, and for a paper of this scope (multi-pivot curriculum + ablations + 3 evaluation benchmarks) that cannot realistically reach conference quality in under 6 weeks\",\n    \"EMNLP 2026 (ACL Rolling Review, rolling deadlines throughout 2026) — viable only if the team has prior QLoRA fine-tuning infrastructure already in place and can begin experiments immediately\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (ACL 2024) [29% improvement on Chinese/Korean/Italian/Spanish; Turkic/Mongolic gap is untested]\",\n    \"Cross-Lingual Optimization for Language Transfer in Large Language Models (CLO; ACL 2025, arXiv:2505.14297) [DPO-style cross-lingual preference optimization using English-only source and M2M100 translation; baseline and methodological reference for TWMP's multi-source DPO extension]\",\n    \"LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning (Ye et al., AAAI 2026, arXiv:2511.10229) [selects multilingual instruction data using language separability scores from the model's own representation space across 22 languages including low-resource targets; differentiated from TWMP's external URIEL+ typological weighting independent of training dynamics, staged curriculum, and multi-source DPO objective]\",\n    \"Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages (Idris et al., SIGIR 2026, arXiv:2603.27651) [multi-source cross-lingual transfer as budget-constrained resource allocation for NER and sentiment analysis on Hausa, Yoruba, and Swahili across 288 experiments; no typological features or curriculum ordering—differentiated from TWMP's URIEL+-weighted staged instruction tuning]\",\n    \"Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) [3-stage curriculum (token-level → sentence-level → monolingual code-switching) for single language pair; primary focus Korean, with Japanese and Indonesian—differentiated from TWMP's multi-pivot typological curriculum without code-switching targeting a family of related agglutinative languages]\",\n    \"Revisiting Multilingual Data Mixtures in Language Model Pretraining (Foroutan et al., arXiv:2510.25947, ICLR-submitted 2025) [multilingual data reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); differentiated from TWMP's instruction-tuning-scale LoRA curriculum where data volume, optimization dynamics, and gradient signal are qualitatively different]\",\n    \"Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (Laiyk et al., ACL 2025 Long, arXiv:2502.13647) [10,600 GPT-4o-assisted Kazakh instruction examples fine-tuning Qwen/Falcon/Gemma; requires target-language labels and is Kazakh-specific—differentiated from TWMP's label-free multi-target approach covering Mongolian and Uyghur equally]\",\n    \"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+ (Shipton et al., LREC 2026, arXiv:2510.27183) [extends URIEL+ with script vectors and Glottolog genealogies for 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages]\",\n    \"Llama-3.1-Sherkala-8B-Chat (arXiv:2503.01493) [trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish; demonstrates Turkish as auxiliary language improves Kazakh performance via full fine-tuning; differentiated from TWMP's generalizable LoRA recipe parameterized by continuous URIEL+ distances]\",\n    \"Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) [implicit reward transfer from English-aligned DPO model to annotate cross-lingual preference pairs; 12.72% Win Rate improvement on X-AlpacaEval; English-only source with no typological weighting—differentiated from TWMP's multi-pivot source selection and low-resource agglutinative targets]\",\n    \"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP; official repository: github.com/LeeLanguageLab/URIELPlus]\",\n    \"Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset (ρ=0.358) outperforms full 800-feature URIEL+ (ρ=0.260) for typological alignment and downstream cross-lingual NLP; justifies TWMP's feature selection step]\",\n    \"Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]\",\n    \"TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]\",\n    \"Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]\",\n    \"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark, 23K questions, peer-reviewed]\",\n    \"MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]\",\n    \"TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]\",\n    \"Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]\",\n    \"Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)\",\n    \"Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)\",\n    \"Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]\",\n    \"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]\"\n  ],\n  \"description\": \"This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds Glottolog genealogies covering 26,449 languages; TWMP uses the COLING 2025 base version, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358 vs. ρ=0.260 for the full 800-feature set) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. LangGPS (Ye et al., AAAI 2026, arXiv:2511.10229) selects multilingual instruction data by language separability from the model's own representation space across 22 languages; TWMP instead uses external URIEL+ features independent of training dynamics, with a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer (Idris et al., SIGIR 2026, arXiv:2603.27651) frames multi-source transfer as budget-constrained allocation for NER/sentiment tasks without typological features or curriculum ordering—TWMP's principled weighting and staged scheduling address instruction tuning specifically. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. Code-Switching Curriculum Learning (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) proposes a 3-stage code-switching curriculum for a single language pair; TWMP's curriculum spans a typologically ordered pool of pivot languages without code-switching. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. Instructions yielding no target-language candidates post-gate fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Laiyk et al. (ACL 2025 Long, arXiv:2502.13647) fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP requires no target-language labels and applies equally to Mongolian and Uyghur where no comparable dataset exists. Revisiting Multilingual Data Mixtures (Foroutan et al., arXiv:2510.25947) studies reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); TWMP targets instruction-tuning scale where data volume, optimization dynamics, and gradient signal are qualitatively different. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU, MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.\",\n  \"project_name\": \"typological_multi_pivot\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL – TIPA (arXiv:2601.16629, EACL 2026 Findings) is directly competing work the generator missed: it constructs proxy language adapters by aggregating existing ones weighted by typological similarity across 230+ languages and five tasks. The novelty claim 'no prior work combines multi-pivot selection with typological distance weighting' is therefore too strong; the revision must differentiate TWMP from TIPA clearly (TIPA is training-free adapter aggregation for encoders; TWMP is a weighted sampling + curriculum training approach for decoder LLMs in instruction tuning—this distinction exists but must be made explicit).\", \"CRITICAL – Evaluation benchmarks are misspecified: XQuAD and XCOPA do NOT include Kazakh, Mongolian, or Uyghur—multiple sources and the benchmarks' own documentation confirm this. The evaluation protocol must be redesigned to use benchmarks that actually cover the target languages (e.g., XTREME-UP, MiLiC-Eval for Chinese minority languages, or TyDi QA for Kazakh).\", \"SIGNIFICANT – Model name 'Qwen 3.5-7B' does not exist. The Qwen3.5 series released in 2026 includes 4B and 9B variants (among others) but no 7B. The 250K vocabulary claim is correct for Qwen3.5 but the model identifier must be corrected to Qwen3.5-9B or Qwen3.5-4B before submission.\", \"SIGNIFICANT – 16-day timeline is unrealistic for a conference-quality submission. Running 15–20 QLoRA experiments across 3 target languages, implementing the TWMP curriculum + CLO loss from scratch, and writing a complete paper cannot be done in 16 days by 1–2 researchers without preexisting infrastructure. The compute estimate (180h A100 ≈ 125–135h H100) is within the 200 H100-hour hard constraint, but wall-clock time is the binding bottleneck.\", \"SIGNIFICANT – The primary evidence for the research gap, 'Left Behind' (arXiv:2603.21036), is a March 2026 preprint from a single author at North American University evaluated with 50 hand-crafted questions. EMNLP reviewers will reject this as insufficient basis for a gap claim; the motivation must be grounded in larger, peer-reviewed evaluations (e.g., the 'Shared Weights Pretraining for Extremely Low-Resource Languages' ACL 2025 paper, or XTREME-UP results for Turkic languages).\", \"MODERATE – Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) is not properly discussed in the landscape. This paper directly uses typological feature vectors for language selection in multilingual instruction tuning—the generator characterizes only arXiv:2505.13908 (which is purely analytical) while ignoring this more methodologically relevant prior work.\", \"MODERATE – MLM is a NeurIPS 2025 ER Workshop paper, not a NeurIPS 2025 main conference paper. Misrepresenting workshop papers as conference papers in a related work section is a frequent reviewer complaint and can trigger a bias/credibility flag.\", \"MODERATE – The CLO-style loss is described as a 'cross-lingual contrastive loss that enforces target-language response fidelity.' CLO actually uses DPO-style preference optimization (not a contrastive loss) to suppress off-language responses. The paper must use technically accurate descriptions to avoid confusion and reviewer pushback.\", \"MINOR – PLUG (ACL 2024)'s 29% improvement was measured on Chinese, Korean, Italian, and Spanish—not on Kazakh/Mongolian/Uyghur. The assumption that PLUG performs poorly on Turkic languages is plausible but not directly evidenced in the PLUG paper itself; the gap claim relative to PLUG needs its own experimental demonstration.\"]\nFeedback: The core idea is genuinely interesting—typological-distance-weighted multi-pivot instruction tuning for Turkic low-resource languages—but the current draft has three blockers that prevent submission at EMNLP 2026 quality: (1) TIPA (EACL 2026) must be cited and clearly differentiated: TIPA does typological weighting of adapters in a training-free, encoder-adapter (MAD-X) framework across 230+ languages; TWMP is a training-time data sampling + curriculum approach for decoder LLMs in instruction tuning—spell this out explicitly in Section 2. (2) Replace XQuAD + XCOPA with benchmarks that actually include Kazakh, Mongolian, and Uyghur: consider XTREME-UP (includes Kazakh), MiLiC-Eval (Uyghur, Kazakh, Mongolian), and TyDi QA for real-language evaluation. If none of the standard benchmarks are adequate, you need to explain what evaluation data you are using and where it comes from. (3) Correct the model name to Qwen3.5-9B (or 4B) and rerun your compute estimates accordingly. Beyond the blockers: the motivation should be regrounded away from 'Left Behind' as the sole anchor—add references to XTREME-UP or ACL 2025 shared-weights pretraining results for Turkic languages. Add arXiv:2410.07809 to related work with a clear explanation of why TWMP's weighted sampling and curriculum are distinct contributions. Fix the MLM venue to 'NeurIPS 2025 ER Workshop' and fix the CLO description to 'DPO-style cross-lingual preference optimization.' On timeline: unless the team has the training infrastructure already built, the 16-day window makes a May 25 ARR deadline extremely risky; the ACL 2027 ARR deadline (August 3, 2026) is a more defensible target that allows proper validation on additional typological clusters (e.g., a Bantu agglutinative language) to test generalization beyond Turkic.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"SIGNIFICANT – CLO's DPO objective is designed for English-source preference pairs: chosen = target-language response to English instruction, rejected = off-language (English) response to target-language instruction. TWMP proposes extending this to non-English source languages (Turkish/Uzbek → Kazakh), but the paper does not specify how preference pairs are constructed when the source is itself a non-English language like Uzbek. If the model produces a Kazakh response to a Uzbek instruction, what is the 'rejected' response? Reviewers will reject this as technically incomplete without a precise DPO formulation for the multi-source case.\", \"SIGNIFICANT – URIEL legacy features are known to be sparse for exactly the target languages in this paper. URIEL+ (arXiv:2409.18472, COLING 2025) explicitly improves coverage for low-resource languages and should be used instead of the 289-dim lang2vec legacy features. Furthermore, 'Less is More: The Effectiveness of Compact Typological Language Representations' (EMNLP 2025) shows that compact URIEL+ features outperform the full 289-dim feature space for cross-lingual NLP tasks—directly contradicting TWMP's use of all 289 dimensions without selection. This is a directly relevant citation the paper must engage with.\", \"MODERATE – Auto_research mode (600h A100 ≈ 300h H100) exceeds the stated ≤200 H100-hour hard constraint. While the experiment plan uses manual mode (within constraint), the resource estimate table presents auto_research as a legitimate deployment mode without flagging this violation of the user's stated budget constraint.\", \"MODERATE – The staged curriculum's cosine-distance threshold schedule is described qualitatively ('progressively expands the radius at scheduled epochs') but no concrete schedule is specified. Reviewers will ask: how many stages? What distance thresholds? How are thresholds set relative to the URIEL distance distribution of the Aya collection? Without a concrete, reproducible specification, this is a design element that cannot be ablated or replicated.\", \"MODERATE – DCO (arXiv:2603.04678, March 2026, Tianyu Liu et al.) introduces Direct Consistency Optimization, a DPO-inspired method for cross-lingual knowledge consistency across 26 languages and 9 LLMs. This is a concurrent work that uses a DPO-style objective for cross-lingual alignment—similar in spirit to the CLO component of TWMP—and must be cited and differentiated in the related work section.\", \"MINOR – The Aya dataset's coverage of Turkic pivot languages (Turkish, Uzbek, Kyrgyz) is assumed but not verified. If Uzbek and Kyrgyz have only hundreds of Aya instances, the typological-distance-weighted sampling will produce noisy estimates for the closest pivots to Kazakh. The paper should state the number of available training instances per pivot language in Aya and set a minimum threshold below which a language is excluded from the mixture.\"]\nFeedback: The generator has addressed all Round 1 critical issues competently: TIPA is correctly differentiated, benchmarks are fixed, Qwen3.5-9B is confirmed correct, arXiv:2410.07809 is properly placed in the landscape, and the CLO/DPO description is accurate. The remaining blockers are two: (1) The DPO objective must be precisely formulated for non-English source languages. The current description 'increases preference for target-language responses and reduces preference for off-language outputs, without requiring any target-language training labels' is borrowed verbatim from CLO's English-source setting. For a Turkish → Kazakh pair, you must specify: what constitutes the chosen response, what constitutes the rejected response, and how you obtain these without any Kazakh labels. One viable extension: treat (Turkish-instruction, Kazakh-response) as the chosen pair and (Turkish-instruction, Turkish-response) as rejected—but this requires stating it explicitly and verifying that Qwen3.5-9B produces detectable off-language Turkish responses to Turkish instructions. (2) Replace lang2vec 289-dim URIEL features with URIEL+ (arXiv:2409.18472, COLING 2025), which has better sparse-language coverage, and cite 'Less is More' (EMNLP 2025) to justify whichever feature subspace you choose. This is not just a citation gap—if the typological distances for Uzbek and Kyrgyz are inaccurate in legacy URIEL due to sparsity, the entire weighting scheme degrades for the most important (closest) pivots to Kazakh. Beyond the blockers: add DCO (arXiv:2603.04678) to related work; specify the curriculum schedule concretely (number of stages, distance thresholds); verify and report the number of Aya instances per Turkic pivot language; and note that auto_research mode exceeds the 200 H100-hour constraint if that constraint applies. ACL 2027 (August 3, 2026 ARR) remains the appropriate primary venue.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MODERATE – Sherkala-Chat (arXiv:2503.01493, March 2025) is a directly relevant uncited work: it instruction-tunes Llama-3.1-8B for Kazakh on 45.3B tokens of Kazakh, English, Russian, and Turkish data, demonstrating that Turkish as an auxiliary training language improves Kazakh performance—the empirical core insight that motivates TWMP's pivot selection. Not citing it leaves a gap reviewers will notice; TWMP should add it as related work and contrast it: Sherkala-Chat uses ad-hoc four-language mixing with full fine-tuning, whereas TWMP provides a principled, generalizable, LoRA-based method parameterized by continuous URIEL+ distances applicable across any agglutinative target.\", \"MODERATE – The DPO preference pair construction specifies 'highest-scoring chosen' and 'lowest-scoring rejected,' where 'scoring' is implicitly language identification confidence from fastText. This means a grammatically garbled Kazakh response with high fastText confidence could be chosen as the preferred response over a coherent Turkish response. No quality filter (perplexity, length heuristic, or instruction-following score) is applied to the chosen pool. Reviewers will ask whether the DPO training signal is noisy precisely for the close-pivot cases where K=8 Kazakh responses are plentiful—yet quality varies most—and for distant pairs where only 1 of 8 samples passes the language filter, leaving little variance to select from. The paper should either add a quality filter (e.g., exclude responses shorter than 20 tokens or with perplexity above a threshold under the base model) or explicitly acknowledge and ablate this as a limitation.\", \"MINOR – Qwen3.5-9B release date: the paper states 'released February 2026' but available information indicates the Qwen3.5 small series (0.8B/2B/4B/9B) became available March 2, 2026—the February date applies to the larger Qwen3.5 medium models (35B-A3B, 27B). This should be corrected to March 2026.\", \"MINOR – The URIEL+ repository URL cited in the approach section ('github.com/Masonshipton25/URIELPlus') does not match the official ACL Anthology-linked repository ('github.com/LeeLanguageLab/URIELPlus'). The URL should match the official publication's repository or the PyPI package ('urielplus') should be referenced instead.\", \"MINOR – The Kyrgyz Aya instance count ('~4.1M instances in the Aya collection language split') could not be independently verified against HuggingFace statistics. Given Kyrgyz is much lower-resource than Turkish, this count depends entirely on machine-translated data volume and should be verified and cited to the HuggingFace dataset page or the Aya Collection paper's per-language appendix before submission.\"]\nFeedback: The generator has addressed all Round 2 issues competently: the multi-source DPO formulation is now precisely specified (chosen = source-language instruction + model-generated target-language response; rejected = source-language instruction + model-generated source-language response), URIEL+ replaces legacy 289-dim features with the 'Less is More' 300-feature Laplacian subset, the staged curriculum has concrete D_25/D_60 percentile anchors and epoch ranges, DCO is cited and differentiated, Aya coverage is verified with a 5,000-instance floor, and auto_research mode is correctly flagged as exceeding the 200 H100h budget. Two moderate issues remain before this is submission-ready: (1) Add Sherkala-Chat (arXiv:2503.01493) to related work—it is a directly adjacent March 2025 paper training Llama-3.1 on Kazakh+Turkish+Russian and provides empirical motivation for TWMP's pivot selection logic. The contrast is easy: Sherkala-Chat is language-specific full fine-tuning with ad-hoc pivot choice; TWMP is generalizable LoRA-based training with principled URIEL+ weighting. (2) Address the DPO pair quality concern: define 'highest-scoring' explicitly as language ID confidence, acknowledge that this does not filter for response quality, and either add a minimal quality gate (e.g., minimum response length or base-model perplexity cap) or include it as a stated limitation with an ablation that shows the fastText-only selection is adequate in practice. Fix the three minor issues (Qwen3.5 release date, URIEL+ repo URL, Kyrgyz instance count verification) before submitting. ACL 2027 (August 3, 2026 ARR) remains the appropriate primary target; given these are all fixable within days, the paper is on track.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MODERATE – Sherkala-Chat (arXiv:2503.01493) was flagged in Round 3 as a key uncited adjacent work and remains absent from Round 4. This paper trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish, directly demonstrating that Turkish as an auxiliary language improves Kazakh performance — the empirical core claim motivating TWMP's pivot selection logic. EMNLP reviewers familiar with Kazakh NLP will notice this omission immediately. Required: add to related work section with explicit contrast (Sherkala-Chat uses ad-hoc 4-language full fine-tuning for Kazakh specifically; TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target).\", \"MODERATE – DPO pair quality gate still absent. The approach specifies 'pair the highest-scoring chosen with the lowest-scoring rejected' based on fastText language ID confidence alone, with no quality filter. For close-pivot pairs (Turkish→Kazakh), K=8 sampling may yield 5–7 Kazakh responses, creating a large chosen pool with highly variable quality; the 'highest-scoring' fastText criterion selects the response with the highest Kazakh language ID confidence, which is not correlated with response coherence or instruction-following quality. A grammatically garbled but confidently Kazakh response will be preferred over a fluent but lower-confidence response. This was raised in Round 3 and remains unaddressed. Fix: add a minimum response length gate (e.g., ≥20 tokens) or base-model perplexity cap, or include an explicit ablation comparing fastText-only selection vs. a quality-gated variant and acknowledge this as a limitation with empirical validation.\", \"MODERATE – Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings) is uncited and directly relevant to TWMP's DPO component. This paper uses implicit reward transfer from English DPO models to annotate cross-lingual preference pairs for multilingual DPO fine-tuning, achieving 12.72% average Win Rate improvement on X-AlpacaEval across training languages. While the approach differs from TWMP (English-only source, implicit reward annotation, no typological weighting), it represents active concurrent work on cross-lingual DPO alignment that EMNLP reviewers will expect to see cited and contrasted. Required addition to related work: differentiate TWMP's direct construction of multi-source preference pairs via language ID vs. this paper's implicit reward annotation from a single English-aligned model.\", \"MINOR – Qwen3.5-9B release date error persists for the third consecutive round. The submission states 'released February 2026' but independent verification (multiple sources) confirms the Qwen3.5 small series (0.8B/2B/4B/9B) was released March 1–2, 2026, with February 2026 referring to the larger Qwen3.5 medium models (35B-A3B, 27B). Change 'released February 2026' to 'released March 2026'.\", \"MINOR – URIEL+ repository URL persists as incorrect for the third consecutive round. The submission cites 'github.com/Masonshipton25/URIELPlus' but the official ACL Anthology-linked repository is 'github.com/LeeLanguageLab/URIELPlus' (confirmed). Change to the correct URL or cite the PyPI package 'urielplus' instead.\"]\nFeedback: This is Round 4 and the same four issues (Sherkala-Chat, DPO quality gate, release date, repo URL) that were flagged in Round 3 have not been addressed. The pattern is concerning for an ARR deadline in 15 days. Here is exactly what needs to change, in priority order:\n\n(1) Add Sherkala-Chat to Section 2 related work. One paragraph is sufficient: 'Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish, demonstrating that Turkish as an auxiliary language improves Kazakh performance—motivating our choice of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc pivot selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language.'\n\n(2) Add Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings) to Section 2. One sentence: 'Implicit Cross-Lingual Rewarding annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving strong multilingual alignment from English-only source data—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from this work.'\n\n(3) Fix the DPO quality issue. Choose one of: (a) add a minimum 20-token length gate to the chosen pool and state it explicitly; (b) add a perplexity cap at 2× base-model perplexity on the instruction; or (c) keep the current fastText-only selection but add a clearly labeled limitation paragraph and one ablation row in Table X comparing fastText-only vs. length-gated selection. Option (c) requires the least implementation effort and is acceptable.\n\n(4) Fix two one-line errors: 'released February 2026' → 'released March 2026'; 'github.com/Masonshipton25/URIELPlus' → 'github.com/LeeLanguageLab/URIELPlus'.\n\nNone of these require new experiments. Issues (1), (2), (4) are writing-only changes. Issue (3) option (c) requires one additional experiment row or a paragraph addition. The paper is substantively sound and the core novelty claim is defensible—these are editorial and citation completeness fixes that are blocking an otherwise strong submission. ACL 2027 (August 3, 2026 ARR) remains the more realistic target, but if the team has existing QLoRA infrastructure, EMNLP 2026 (May 25 ARR) is feasible after these four fixes.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE – Revisiting Multilingual Data Mixtures (arXiv:2510.25947, Foroutan et al., EPFL, Oct 2025) directly challenges TWMP's two core premises: (1) staged curriculum learning 'does not reduce negative interference' in multilingual training, and (2) temperature-based language reweighting 'hurts performance due to noise' on low-resource data. This paper focuses on pretraining, not instruction tuning, but EMNLP reviewers familiar with it will raise it against TWMP's staged curriculum and inverse-distance weighting scheme. Required: cite this paper in Section 2, acknowledge the potential discrepancy, and argue explicitly why the instruction tuning setting (smaller data footprint, fewer gradient steps, different optimization landscape) is different enough that the Foroutan et al. findings do not transfer.\", \"MODERATE – LangGPS (arXiv:2511.10229, AAAI 2026; Yangfan Ye, Xiaocheng Feng et al., HIT + Microsoft) proposes language separability from the model's own representation space as the basis for multilingual instruction tuning data selection, and reports improvements over external-feature-based approaches across 22 languages including low-resource targets. It is a peer-reviewed AAAI 2026 competitor to TWMP's URIEL+-based selection approach. This is too similar to leave uncited. Required: add to related work and differentiate: LangGPS uses task-adaptive model-internal signals but is agnostic to typological structure and provides no mechanism for multi-pivot curriculum sequencing; TWMP uses external typological features to derive a principled ordering over pivot languages independent of training dynamics.\", \"MODERATE – Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (arXiv:2411.02460, ACL 2025 Findings; Haneul Yoo et al., NAVER AI) proposes a 3-stage curriculum (token-level code-switching → sentence-level code-switching → monolingual) that achieves cross-lingual transfer improvements on both high- and low-resource languages without typological distance. This paper has been available since November 2024—before all prior review rounds—and has never appeared in TWMP's references. EMNLP reviewers will notice its absence. Required: cite and contrast in Section 2: the code-switching curriculum operates within a single language pair using surface-level code-mixing as a bridge, whereas TWMP's curriculum operates over a pool of typologically ordered pivot languages with no code-switching; the two approaches address different facets of cross-lingual curriculum design and could in principle be combined.\", \"MINOR – Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (arXiv:2502.13647, ACL 2025 Main; Laiyk et al.) fine-tunes Qwen/Falcon/Gemma on 10,600 GPT-4o-assisted Kazakh instruction examples, achieving consistent improvement on multiple-choice and generative Kazakh tasks. This is a direct Kazakh instruction tuning baseline from ACL 2025 that any reviewer working on KazMMLU will expect TWMP to compare against or at minimum cite. It documents that targeted single-language instruction data generation is a strong alternative to cross-lingual transfer methods—TWMP should position itself relative to it (e.g., TWMP does not require any target-language instruction labels and is applicable to Mongolian and Uyghur where no comparable GPT-4-assisted dataset exists).\", \"MINOR – Simple Additions, Substantial Gains: Expanding URIEL+ (arXiv:2510.27183, LREC 2026; Shipton, Ng, Khan et al.) extends the URIEL+ database with script vectors, Glottolog integration, and genealogical feature propagation, reducing feature sparsity by 35% and expanding coverage to 26,449 languages—directly addressing the sparsity problem for Kazakh/Uzbek/Kyrgyz that TWMP cites as motivation for switching from legacy lang2vec to URIEL+. TWMP should either use this updated version or acknowledge it as a contemporaneous development and argue that the 2409.18472 COLING 2025 version is sufficient for the target languages (the 35% sparsity reduction would most benefit exactly the low-resource Turkic languages in scope).\", \"MINOR – The DPO prerequisite probe threshold is set at >5% of K=8, which equals at least 1 target-language response in 8 tries. This is the minimum viable signal level and means many source-target pairs that 'pass' the probe provide almost no diversity in the chosen pool (only 1 candidate). At this threshold, the 20-token gate can cause 100% discard of chosen candidates for those instructions (if the single Kazakh response is <20 tokens), silently collapsing to SFT-only training for many instruction prompts without reporting. The paper should characterize the empirical distribution of per-instruction chosen-pool sizes (1, 2, 3+ responses) across source-target pairs and report what fraction of instructions fall back to SFT-only due to post-gate chosen pool exhaustion.\"]\nFeedback: All Round 4 issues are addressed: Sherkala-Chat is properly cited and contrasted, the DPO 20-token length gate and ablation row are specified, Implicit Cross-Lingual Rewarding is cited, the release date and URIEL+ URL are corrected. The paper's core method is substantively sound and the technical specification is unusually precise for a draft at this stage. Three writing-only additions are needed before this is EMNLP-ready:\n\n(1) Add Foroutan et al. (arXiv:2510.25947) to Section 2. Key contrast: that paper tests pretraining-scale reweighting across 25–400 languages; TWMP operates at instruction tuning scale (10 epochs, LoRA, ≤6,400 instances per pivot) where reweighting over a narrow near-family pivot pool is qualitatively different from resampling across 400 pretraining languages. Make this argument explicitly to preempt the obvious reviewer objection.\n\n(2) Add LangGPS (arXiv:2511.10229, AAAI 2026) and Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings) to Section 2. Both are one-paragraph additions: LangGPS uses model-internal representation signals (no external typological database, no multi-pivot ordering); Code-Switching Curriculum uses surface-level code-mixing within a pair (no typologically structured pool, no DPO). Neither addresses the multi-pivot ordering problem or provides a principled recipe for pivot sequencing across typologically diverse targets.\n\n(3) Add arXiv:2502.13647 (ACL 2025 Main, Kazakh instruction tuning) as a related baseline in Section 2 and note it cannot generalize to Mongolian and Uyghur where no comparable target-language instruction dataset exists.\n\nFor the probe threshold: add one sentence clarifying what happens when the post-gate chosen pool for a given instruction is empty—confirm that those instructions fall back to the SFT-weighted objective, not to silent skip, and report the per-pair fallback rate as a characterization result.\n\nACL 2027 (ARR August 3, 2026) remains the appropriate primary target. None of these additions require new experiments.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"SIGNIFICANT (PATTERN) – All five Round 5 issues remain unaddressed in Round 6 for the second consecutive round. (1) Foroutan et al. (arXiv:2510.25947, ICLR-submitted): not in landscape or key_references. (2) LangGPS (arXiv:2511.10229, AAAI 2026 main): not in landscape or key_references — this is a peer-reviewed AAAI 2026 competitor on multilingual instruction tuning data selection across 22 languages including low-resource targets, and its omission is the most damaging gap. (3) Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings): not cited despite being published November 2024 and appearing in ACL Anthology. (4) arXiv:2502.13647 (ACL 2025 Long, Kazakh instruction tuning): not cited despite being a direct Kazakh-targeting baseline. (5) URIEL+ expansion (arXiv:2510.27183, LREC 2026): not cited despite directly extending the typological tool TWMP relies on.\", \"MODERATE (NEW) – Budget-Xfer (arXiv:2603.27651, March 2026) proposes budget-constrained source language selection for multi-source cross-lingual transfer, jointly optimizing which source languages to include and how much data to allocate from each — directly parallel to TWMP's multi-pivot selection problem. It evaluates on three African target languages (Hausa, Yoruba, Swahili) using a 288-experiment suite. While it targets classification tasks rather than instruction tuning, EMNLP reviewers in the cross-lingual track will expect it to be cited and contrasted: Budget-Xfer frames source selection as resource allocation without typological features or curriculum ordering; TWMP provides principled URIEL+-based weighting and staged scheduling.\", \"MINOR (PERSISTENT) – Per-instruction chosen-pool fallback characterization remains incomplete. The approach section states that 'instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' but does not report the per-instruction fallback rate as a characterization result. Round 5 feedback specifically requested one sentence confirming these instructions fall back to SFT-weighted objective (not silent skip) and reporting the empirical fallback rate per source-target pair. The current text says they are 'discarded,' which implies silent skip rather than SFT fallback — this ambiguity must be resolved and the frequency reported.\"]\nFeedback: This is Round 6. The core method is technically sound, the DPO formulation is precise, the compute budget is within constraint, and the evaluation design is appropriate. However, the same five citations flagged in Round 5 are absent for the second consecutive round, and a new paper (Budget-Xfer, arXiv:2603.27651) has appeared that is directly adjacent. Here is the exact text to add for each outstanding item:\n\n(1) Foroutan et al. (Section 2, one sentence): 'Revisiting Multilingual Data Mixtures [Foroutan et al., 2025] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime.'\n\n(2) LangGPS (Section 2, one paragraph — highest priority): 'LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address.'\n\n(3) Code-Switching Curriculum (Section 2, one sentence): 'Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target.'\n\n(4) Kazakh instruction tuning (Section 2, one sentence): 'Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists.'\n\n(5) URIEL+ expansion (Section 3, one sentence): 'A concurrent LREC 2026 extension [Shipton et al., arXiv:2510.27183] adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version [arXiv:2409.18472] with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages.'\n\n(6) Budget-Xfer (Section 2, one sentence): 'Budget-Xfer [arXiv:2603.27651, 2026] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address.'\n\n(7) Fix the per-instruction fallback: Change 'Instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' to 'Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe.'\n\nAll seven items are writing-only changes requiring no new experiments. ACL 2027 (ARR August 3, 2026) remains the appropriate primary target. At Round 6, the paper cannot pass until at minimum items (1)–(5) are resolved.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:55:26.129Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:55:26.129Z",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-10T07:55:26.161Z_

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

## Idea under review (round 7/10)
{
  "title": "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning",
  "core_problem": "Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.",
  "opportunity": "Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K Kazakh-language questions spanning STEM, humanities, and social sciences sourced from authentic educational materials; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.",
  "landscape": "PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer [arXiv:2603.27651, SIGIR 2026] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address. Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target. Revisiting Multilingual Data Mixtures [Foroutan et al., 2025, arXiv:2510.25947] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.",
  "approach": "We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\n\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\n\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 on typological alignment tasks versus ρ=0.260 for the full 800-feature set while also improving downstream cross-lingual NLP performance, we apply this feature selection before computing cosine distances. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\n\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\n\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\n\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\n\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh, MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG and CLO serve as primary baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO baselines, URIEL+ sub-space ablations, curriculum schedule variants, DPO quality gate ablation row, and DPO prerequisite probe runs)",
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
    "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning (Ye et al., AAAI 2026, arXiv:2511.10229) [selects multilingual instruction data using language separability scores from the model's own representation space across 22 languages including low-resource targets; differentiated from TWMP's external URIEL+ typological weighting independent of training dynamics, staged curriculum, and multi-source DPO objective]",
    "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages (Idris et al., SIGIR 2026, arXiv:2603.27651) [multi-source cross-lingual transfer as budget-constrained resource allocation for NER and sentiment analysis on Hausa, Yoruba, and Swahili across 288 experiments; no typological features or curriculum ordering—differentiated from TWMP's URIEL+-weighted staged instruction tuning]",
    "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) [3-stage curriculum (token-level → sentence-level → monolingual code-switching) for single language pair; primary focus Korean, with Japanese and Indonesian—differentiated from TWMP's multi-pivot typological curriculum without code-switching targeting a family of related agglutinative languages]",
    "Revisiting Multilingual Data Mixtures in Language Model Pretraining (Foroutan et al., arXiv:2510.25947, ICLR-submitted 2025) [multilingual data reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); differentiated from TWMP's instruction-tuning-scale LoRA curriculum where data volume, optimization dynamics, and gradient signal are qualitatively different]",
    "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (Laiyk et al., ACL 2025 Long, arXiv:2502.13647) [10,600 GPT-4o-assisted Kazakh instruction examples fine-tuning Qwen/Falcon/Gemma; requires target-language labels and is Kazakh-specific—differentiated from TWMP's label-free multi-target approach covering Mongolian and Uyghur equally]",
    "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+ (Shipton et al., LREC 2026, arXiv:2510.27183) [extends URIEL+ with script vectors and Glottolog genealogies for 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages]",
    "Llama-3.1-Sherkala-8B-Chat (arXiv:2503.01493) [trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish; demonstrates Turkish as auxiliary language improves Kazakh performance via full fine-tuning; differentiated from TWMP's generalizable LoRA recipe parameterized by continuous URIEL+ distances]",
    "Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) [implicit reward transfer from English-aligned DPO model to annotate cross-lingual preference pairs; 12.72% Win Rate improvement on X-AlpacaEval; English-only source with no typological weighting—differentiated from TWMP's multi-pivot source selection and low-resource agglutinative targets]",
    "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP; official repository: github.com/LeeLanguageLab/URIELPlus]",
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
  "description": "This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds Glottolog genealogies covering 26,449 languages; TWMP uses the COLING 2025 base version, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358 vs. ρ=0.260 for the full 800-feature set) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. LangGPS (Ye et al., AAAI 2026, arXiv:2511.10229) selects multilingual instruction data by language separability from the model's own representation space across 22 languages; TWMP instead uses external URIEL+ features independent of training dynamics, with a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer (Idris et al., SIGIR 2026, arXiv:2603.27651) frames multi-source transfer as budget-constrained allocation for NER/sentiment tasks without typological features or curriculum ordering—TWMP's principled weighting and staged scheduling address instruction tuning specifically. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. Code-Switching Curriculum Learning (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) proposes a 3-stage code-switching curriculum for a single language pair; TWMP's curriculum spans a typologically ordered pool of pivot languages without code-switching. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. Instructions yielding no target-language candidates post-gate fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Laiyk et al. (ACL 2025 Long, arXiv:2502.13647) fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP requires no target-language labels and applies equally to Mongolian and Uyghur where no comparable dataset exists. Revisiting Multilingual Data Mixtures (Foroutan et al., arXiv:2510.25947) studies reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); TWMP targets instruction-tuning scale where data volume, optimization dynamics, and gradient signal are qualitatively different. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU, MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.",
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
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "type": "user",
  "uuid": "1d5ab01e-a074-40a7-8302-8c1496536697",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:55:26.157Z_

```json
{
  "parentUuid": "1d5ab01e-a074-40a7-8302-8c1496536697",
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
  "uuid": "1285480d-adac-4bac-857a-b242128c4459",
  "timestamp": "2026-05-10T07:55:26.157Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:55:26.157Z_

```json
{
  "parentUuid": "1285480d-adac-4bac-857a-b242128c4459",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "780fddd1-2f04-41ca-ad45-05d92d093c07",
  "timestamp": "2026-05-10T07:55:26.157Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
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
  "leafUuid": "780fddd1-2f04-41ca-ad45-05d92d093c07",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review agent conducting independent verification on Round 7",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:56:04.341Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this carefully. This is Round 7 of 10 reviews of the "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning" (TWMP) paper idea.

Let me first review what's changed from Round 6 to Round 7 by comparing the current idea submission against the Round 6 issues:

**Round 6 Issues (what needed to be fixed):**
1. SIGNIFICANT (PATTERN): Five Round 5 issues still unaddressed:
   - Foroutan et al. (arXiv:2510.25947, ICLR-submitted): not cited
   - LangGPS (arXiv:2511.10229, AAAI 2026 main): not cited
   - Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings): not cited
   - arXiv:2502.13647 (ACL 2025 Long, Kazakh instruction tuning): not cited
   - URIEL+ expansion (arXiv:2510.27183, LREC 2026): not cited
2. MODERATE (NEW): Budget-Xfer (arXiv:2603.27651, March 2026): not cited
3. MINOR (PERSISTENT): Per-instruction chosen-pool fallback characterization incomplete

Now checking the Round 7 submission against the landscape section, and I can see several of these papers have actually been added—Revisiting Multilingual Data Mixtures, LangGPS, and Code-Switching Curriculum are all now present, though the Kazakh instruction tuning paper still needs to be included.

Looking further down the list, Simple Additions and Budget-Xfer are both there now, and the fallback characterization itself has been properly addressed—the submission now explains how instructions with empty post-gate chosen pools fall back to SFT-weighted sampling and reports the per-source-target fallback rate as a characterization result.

It looks like all the Round 6 issues have actually been resolved in this version. Let me verify more carefully by reading the text.

Looking at the landscape section, I'm checking how TWMP compares to related work. Budget-Xfer frames multi-source cross-lingual transfer as a budget allocation problem for specific tasks, but TWMP's typological-distance weighting and staged curriculum provide a more principled ordering mechanism for instruction tuning. Code-Switching Curriculum Learning operates on a single language pair with token-to-monolingual progression, whereas TWMP works across a typologically ordered set of pivot languages targeting related agglutinative languages. Revisiting Multilingual Data Mixtures studies reweighting at pretraining scale across many languages.

The next thinking clarifies that TWMP operates at instruction-tuning scale with different data volumes and optimization dynamics. Laiyk et al. requires target-language instruction labels for Kazakh, but TWMP needs no such labels and generalizes to Mongolian and Uyghur where those datasets don't exist. There's also a concurrent URIEL+ expansion adding script vectors and genealogies.

So the rewrite should be:

TWMP operates at instruction-tuning scale with fundamentally different data volumes and gradient dynamics than pretraining-scale approaches like Revisiting Multilingual Data Mixtures. Unlike Laiyk et al., which requires target-language instruction labels, TWMP needs no such annotations and applies equally to low-resource languages like Mongolian and Uyghur where comparable datasets don't exist. A concurrent URIEL+ extension is also expanding the typological feature space with script vectors and genealogical information. Now I'm doing some independent verification of the key citations and checking whether any new concurrent work has emerged since the last review round. I need to confirm that papers like CLO, LangGPS, and Budget-Xfer actually exist and are correctly cited, then scan for any remaining technical concerns or novelty gaps I might have missed. I need to verify a few key claims about recent papers and datasets—checking whether "Less is More" is actually from EMNLP 2025, confirming the CLO paper exists as described, and looking into whether any recent work has combined typological features with instruction tuning. I should also verify how well the Aya dataset covers Turkic languages since that's relevant to the target languages here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "780fddd1-2f04-41ca-ad45-05d92d093c07",
  "isSidechain": false,
  "requestId": "req_011CatXf5CHLMci5Ht8hGk5e",
  "type": "assistant",
  "uuid": "380bfd30-4d58-4c35-a6df-94731ad21f28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TTTEHcnys8TUoZHBmPkP6J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27631,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4031,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 27631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27631
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

_source line 9 · 2026-05-10T07:56:04.348Z_

I'll conduct independent research to verify claims and identify new issues in Round 7 of this review. Let me run several searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "380bfd30-4d58-4c35-a6df-94731ad21f28",
  "isSidechain": false,
  "requestId": "req_011CatXf5CHLMci5Ht8hGk5e",
  "type": "assistant",
  "uuid": "c08be805-2919-484b-96eb-eac28b429a57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TTTEHcnys8TUoZHBmPkP6J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27631,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4031,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 27631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27631
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

_source line 10 · 2026-05-10T07:56:13.198Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014hJjMxwKujQSDwz3JSYWtr`</summary>

```json
{
  "description": "Verify CLO paper and find new cross-lingual instruction tuning competitors",
  "subagent_type": "Explore",
  "prompt": "Search for and verify the following papers exist as described, and find any new competing papers from late 2025 through May 2026. Use WebSearch and WebFetch tools.\n\n1. Verify CLO paper exists: \"Cross-Lingual Optimization for Language Transfer in Large Language Models\" arXiv:2505.14297 ACL 2025. Search for it and check abstract.\n\n2. Verify \"Less is More: The Effectiveness of Compact Typological Language Representations\" arXiv:2509.20129 EMNLP 2025 exists and confirms Spearman ρ=0.358 for 300-feature URIEL+ vs ρ=0.260 for full 800-feature set.\n\n3. Search for NEW cross-lingual instruction tuning papers from January-May 2026 that combine typological features with multi-pivot data selection. Search:\n   - \"typological distance instruction tuning 2026 site:arxiv.org\"\n   - \"multi-pivot cross-lingual instruction tuning 2026\"\n   - \"URIEL multilingual instruction tuning 2026\"\n   - \"cross-lingual transfer low-resource instruction tuning 2026\"\n\n4. Search for any new papers on multilingual curriculum learning for LLMs in 2026:\n   - \"multilingual curriculum learning LLM 2026 site:arxiv.org\"\n   - \"cross-lingual curriculum instruction tuning arXiv 2026\"\n\n5. Search for recent Kazakh/Mongolian/Uyghur NLP papers from 2026:\n   - \"Kazakh NLP LLM 2026\"\n   - \"Mongolian Uyghur language model 2026 instruction\"\n\nReport what you find for each search, including paper titles, arXiv IDs if available, and whether the claimed paper exists as described. Focus on identifying any papers that closely parallel TWMP's approach of using typological features to weight multi-source instruction data with curriculum scheduling."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c08be805-2919-484b-96eb-eac28b429a57",
  "isSidechain": false,
  "requestId": "req_011CatXf5CHLMci5Ht8hGk5e",
  "type": "assistant",
  "uuid": "6ed70c49-d018-4439-9f6a-e0b74ebf930d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TTTEHcnys8TUoZHBmPkP6J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27631,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4031,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 27631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27631
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

_source line 11 · 2026-05-10T07:56:22.362Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Ef2mSn41hDfya4FLHuawDj`</summary>

```json
{
  "description": "Verify LangGPS and Budget-Xfer papers and search for concurrent work",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing an NLP research paper idea called TWMP (Typologically-Weighted Multi-Pivot). I need to independently verify several cited papers exist and find any competing work. Use WebSearch and WebFetch.\n\n1. Verify LangGPS exists: \"LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning\" arXiv:2511.10229 AAAI 2026. Search for it, check abstract.\n\n2. Verify Budget-Xfer exists: arXiv:2603.27651 SIGIR 2026 on budget-constrained source language selection for cross-lingual transfer to African languages. Search for \"Budget-Xfer cross-lingual African languages SIGIR 2026\" or the arXiv ID.\n\n3. Search for competing papers that combine typological language features (URIEL/URIEL+) with data weighting for cross-lingual NLP:\n   - site:arxiv.org \"URIEL\" \"instruction tuning\" 2025 2026\n   - \"typological features\" \"data selection\" multilingual 2026\n   - \"lang2vec\" OR \"URIEL\" \"cross-lingual transfer\" \"curriculum\" 2025 OR 2026\n\n4. Search Papers With Code for SOTA on Kazakh/Mongolian MMLU-style benchmarks:\n   - site:paperswithcode.com KazMMLU\n   - site:paperswithcode.com MiLiC-Eval\n   - \"Kazakh language model benchmark 2026\"\n\n5. Search for any papers on typological similarity-based adapter aggregation or LoRA merging for multilingual NLP in 2025-2026:\n   - \"typological similarity LoRA\" multilingual 2025 2026\n   - \"TIPA typological adapter\" multilingual 2026\n\nReport all findings including whether the cited papers exist as described, and importantly whether any NEW papers have appeared that would compete with TWMP's novelty claim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ed70c49-d018-4439-9f6a-e0b74ebf930d",
  "isSidechain": false,
  "requestId": "req_011CatXf5CHLMci5Ht8hGk5e",
  "type": "assistant",
  "uuid": "618f5799-c50a-4570-b0df-5a1f41e09f3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TTTEHcnys8TUoZHBmPkP6J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27631,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4031,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 27631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27631
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

_source line 12 · 2026-05-10T07:56:34.529Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TndH3cHqK89PQiYLHFZ6Du`</summary>

```json
{
  "description": "Verify feasibility and check Aya dataset coverage for Turkic languages",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing a research paper idea. I need to verify factual claims about datasets and models. Use WebSearch and WebFetch.\n\n1. Verify Aya dataset coverage of Turkic languages. The paper claims:\n   - Turkish: \"multi-million instances\" in Aya collection\n   - Kyrgyz: \"~4.1M instances\"\n   - Uzbek: \"confirmed present with meaningful coverage\"\n   The minimum threshold for inclusion as a pivot is 5,000 instances.\n   \n   Search: \"Aya collection dataset Turkic languages coverage\" HuggingFace\n   Try: site:huggingface.co \"CohereForAI/aya_collection\" OR \"Aya dataset language statistics\"\n   Also try: \"Aya collection 513M instances 114 languages\" to verify the overall stats\n\n2. Verify Qwen3.5-9B model claims:\n   - Released \"March 2026\" (not February)\n   - 248K-token vocabulary spanning 201 languages\n   - Series is 0.8B/2B/4B/9B (no 7B)\n   Search: \"Qwen3.5 9B release date March 2026\" OR \"Qwen3.5 model specifications\"\n   Try: site:huggingface.co Qwen3.5-9B OR \"Qwen/Qwen3.5-9B\"\n\n3. Verify KazMMLU (arXiv:2502.12829) benchmark claims:\n   - 23K Kazakh questions\n   - Evaluates Llama-3.1, Qwen-2.5, GPT-4, DeepSeek V3\n   - ACL 2025 long paper\n   Search: arXiv:2502.12829 or \"KazMMLU Kazakh benchmark ACL 2025\"\n\n4. Verify MiLiC-Eval (arXiv:2503.01150) claims:\n   - Covers Tibetan, Uyghur, Kazakh, Mongolian\n   - 9 tasks, 24K instances\n   - ACL 2025 Findings\n   - GPT-4o-mini achieves \"only slightly above random on Mongolian tasks\"\n   Search: arXiv:2503.01150 or \"MiLiC-Eval minority languages benchmark\"\n\n5. Search for any recent (2025-2026) papers showing Aya dataset language statistics:\n   - \"Aya collection dataset statistics languages 2024 2025\"\n   - \"CohereForAI Aya language breakdown\"\n\nReport precise findings on whether each claim is verifiable and accurate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "618f5799-c50a-4570-b0df-5a1f41e09f3a",
  "isSidechain": false,
  "requestId": "req_011CatXf5CHLMci5Ht8hGk5e",
  "type": "assistant",
  "uuid": "767b7f4e-a3d4-442a-99fb-c6349e2ea3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TTTEHcnys8TUoZHBmPkP6J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27631,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4031,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 27631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27631
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

_source line 13 · 2026-05-10T07:57:46.533Z_

<details><summary>↩ Tool result · `toolu_014hJjMxwKujQSDwz3JSYWtr`</summary>

```text
Now let me compile my comprehensive findings report:

## Summary of Search Results and Verification

### 1. CLO Paper Verification: VERIFIED ✓

**Paper:** "Cross-Lingual Optimization for Language Transfer in Large Language Models"
- **arXiv ID:** 2505.14297
- **Venue:** ACL 2025
- **Status:** Verified and exists as described
- **Main Contribution:** Proposes Cross-Lingual Optimization (CLO) that efficiently transfers English-centric LLMs to target languages while preserving English capabilities using publicly available English SFT data and translation models.
- **Key Result:** CLO consistently outperforms supervised fine-tuning (SFT), achieving better performance with less data in low-resource scenarios. With only 3,200 samples, CLO surpasses SFT with 6,400 samples.

**Source:** [Cross-Lingual Optimization for Language Transfer in Large Language Models](https://arxiv.org/abs/2505.14297)

---

### 2. Typological Representations Paper Verification: VERIFIED ✓

**Paper:** "Less is More: The Effectiveness of Compact Typological Language Representations"
- **arXiv ID:** 2509.20129
- **Venue:** EMNLP 2025 Main Conference
- **Status:** Verified and exists as described
- **Claimed Results Verified:** The paper indeed confirms that the 300-feature URIEL+ using Laplacian Score method achieves **Spearman ρ = 0.358** compared to the full 800-feature URIEL set achieving **ρ = 0.260** - exactly matching your specifications.
- **Main Contribution:** Proposes a pipeline to optimize the URIEL+ typological feature space through feature selection and imputation, demonstrating that compact typological representations outperform full feature sets on linguistic distance alignment and downstream tasks.

**Source:** [Less is More: The Effectiveness of Compact Typological Language Representations](https://arxiv.org/abs/2509.20129)

---

### 3. NEW PAPERS from 2026 Combining Typological Features with Multi-Source Instruction Data:

#### Highly Relevant - Direct Match:

**A. "Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models"**
- **arXiv ID:** 2602.03551
- **Time:** February 2026
- **Relevance:** Directly analyzes how target language typology drives translation quality in state-of-the-art multilingual translation systems (NLLB-200, Tower+), even after controlling for data resourcedness and script. Released fine-grained typological data for 212 languages in FLORES+ benchmark.
- **Parallel to TWMP:** Similar approach of using typological properties to understand and optimize cross-lingual transfer, though focused on MT quality rather than instruction weighting.

**Source:** [Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models](https://arxiv.org/abs/2602.03551)

**B. "Enhancing Multilingual LLM Pretraining with Model-Based Data Selection"**
- **arXiv ID:** 2502.10361
- **Time:** February 2026
- **Acceptance:** NeurIPS 2025 Datasets and Benchmarks track
- **Relevance:** Develops model-based filtering framework for multilingual datasets addressing data selection across diverse linguistic contexts. Achieved 15% token efficiency on MMLU performance using 1B Llama model.
- **Parallel to TWMP:** Uses model-based selection to weight diverse multilingual data, though not explicitly typology-driven, demonstrates data weighting principles across 20 languages.

**Source:** [Enhancing Multilingual LLM Pretraining with Model-Based Data Selection](https://arxiv.org/abs/2502.10361)

---

### 4. Multilingual Curriculum Learning Papers from 2025-2026:

**A. "TildeOpen LLM: Leveraging Curriculum Learning to Achieve Equitable Language Representation"**
- **arXiv ID:** 2603.08182
- **Time:** March 2026
- **Relevance:** 30B-parameter open model for 34 European languages using curriculum-based training schedule alternating between uniform and natural language distributions. Directly combines curriculum learning with multilingual data weighting.
- **Key Features:** Three-phase curriculum for data sampling, addresses cross-lingual interference
- **Direct Parallel to TWMP:** Combines curriculum scheduling with weighted data distribution for multilingual LLMs

**Source:** [TildeOpen LLM: Leveraging Curriculum Learning to Achieve Equitable Language Representation](https://arxiv.org/html/2603.08182)

**B. "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs"**
- **arXiv ID:** 2411.02460
- **Time:** November 2025 (late 2025)
- **Relevance:** Proposes curriculum learning inspired by human second language acquisition, using progressive code-switching stages (token-level → sentence-level → monolingual). Addresses cross-lingual transfer systematically.
- **Key Method:** Staged curriculum mimicking language learning acquisition

**Source:** [Code-Switching Curriculum Learning for Multilingual Transfer in LLMs](https://arxiv.org/abs/2411.02460)

**C. "Revisiting Multilingual Data Mixtures in Language Model Pretraining"**
- **arXiv ID:** 2510.25947
- **Time:** October 2025
- **Relevance:** Controlled curriculum learning experiments examining cross-lingual competition and knowledge transfer dynamics. Investigates how timing/order of language inclusion affects performance.
- **Finding:** Staging languages through curriculum learning does not mitigate negative interference

**Source:** [Revisiting Multilingual Data Mixtures in Language Model Pretraining](https://arxiv.org/html/2510.25947v1)

**D. "Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics"**
- **arXiv ID:** 2601.21698
- **Time:** January 2026
- **Relevance:** Analyzes three linguistically motivated curricula (Age-of-Acquisition, word frequency, verb variation) to understand learning trajectory changes vs. simple reordering effects.

**Source:** [Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics](https://arxiv.org/abs/2601.21698)

---

### 5. Typological Language Selection for Instruction Tuning (2025-2026):

**A. "Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?"**
- **arXiv ID:** 2410.07809
- **Time:** October 2024 (updated 2025)
- **Relevance:** Proposes selecting diverse languages using linguistic features rather than random selection for instruction tuning. Addresses curse of multilinguality through linguistically-informed selection.
- **Key Method:** Simple algorithm for choosing typologically diverse languages

**Source:** [Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?](https://arxiv.org/abs/2410.07809)

**B. "Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages for Cross-Lingual POS Tagging"**
- **arXiv ID:** 2503.19979
- **Time:** March 2026
- **Relevance:** Takes holistic approach examining dataset-specific and fine-grained typological features for transfer language selection. Finds word overlap, type-token ratio, and genealogical distance as top predictors.
- **Key Finding:** Combination of typological + dataset-dependent features provides best rankings
- **Venue:** NAACL 2025 Workshop on Language Models for Underserved Communities

**Source:** [Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages for Cross-Lingual POS Tagging](https://arxiv.org/html/2503.19979v1)

---

### 6. Kazakh/Mongolian/Uyghur Language Model Papers from 2026:

**A. Kazakh - "Llama-3.1-Sherkala-8B-Chat" (Sherkala-Chat)**
- **arXiv ID:** 2503.01493
- **Time:** March 2026
- **Status:** State-of-the-art instruction-tuned model for Kazakh
- **Details:** Adapted from LLaMA-3.1-8B, trained on 45.3B tokens across Kazakh, English, Russian, Turkish. Significantly outperforms existing open Kazakh models of similar scale.
- **Note:** Related project - KazLLM (8B and 70B versions) developed by ISSAI at Nazarbayev University

**Sources:** 
- [Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting](https://arxiv.org/html/2503.01493)
- [Llama-3.1-Sherkala-8B-Chat on arXiv](https://arxiv.org/abs/2503.01493)

**B. Kazakh - "LLM-Assisted Weak Supervision for Low-Resource Kazakh Sequence Labeling"**
- **Time:** 2026 (MDPI Applied Sciences)
- **Relevance:** Addresses Kazakh NLP via LLM-assisted weak supervision framework generating synthetic annotations for sequence labeling, combined with CRF-refined NER/POS models.

**Source:** [LLM-Assisted Weak Supervision for Low-Resource Kazakh Sequence Labeling: Synthetic Annotation and CRF-Refined NER/POS Models](https://www.mdpi.com/2076-3417/16/8/3632)

**C. Mongolian - "MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs"**
- **arXiv ID:** 2411.09492
- **Time:** November 2024
- **Relevance:** Specialized benchmark for Mongolian based on Modern Mongolian Language Textbook. Finds GPT-4-Turbo best at syntax (90.69%) and knowledge (80.52%), but all models struggle with reasoning (max 29.6%).

**Source:** [MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs](https://arxiv.org/html/2411.09492v1)

**D. Uyghur/Mongolian - "Do Chinese models speak Chinese languages?"**
- **arXiv ID:** 2504.00289
- **Time:** April 2026
- **Relevance:** Evaluates Uyghur and Mongolian capabilities across models. Notes Llama3-Instruct is uniquely good at Uyghur and top-performing in Tibetan/Mongolian. Highlights lower-resource language challenges.

**Source:** [Do Chinese models speak Chinese languages?](https://arxiv.org/html/2504.00289v1)

---

### 6. Most Directly Competing Papers (Closest to TWMP's Approach):

Papers that most closely parallel TWMP's combination of typological features + multi-source data weighting + curriculum scheduling:

1. **TildeOpen LLM** (2603.08182) - Combines curriculum learning with weighted multilingual data distribution
2. **Assessing Impact of Typological Features on MT** (2602.03551) - Uses typological properties to drive model optimization across 212 languages
3. **Linguistically-Informed Multilingual Instruction Tuning** (2410.07809) - Typology-based language selection for instruction tuning
4. **Untangling Typology Influence** (2503.19979) - Fine-grained typological feature weighting for language selection
5. **Code-Switching Curriculum Learning** (2411.02460) - Curriculum approach to cross-lingual transfer

**None of these papers explicitly combine all three elements (typological distance weighting + multi-pivot instruction data + curriculum scheduling) as described for TWMP, suggesting TWMP may represent a novel combination of these approaches.**

Sources:
- [TildeOpen LLM: Leveraging Curriculum Learning to Achieve Equitable Language Representation](https://arxiv.org/html/2603.08182)
- [Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models](https://arxiv.org/abs/2602.03551)
- [Linguistically-Informed Multilingual Instruction Tuning](https://arxiv.org/abs/2410.07809)
- [Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages](https://arxiv.org/html/2503.19979v1)
- [Code-Switching Curriculum Learning for Multilingual Transfer in LLMs](https://arxiv.org/abs/2411.02460)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ed70c49-d018-4439-9f6a-e0b74ebf930d",
  "isSidechain": false,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "type": "user",
  "uuid": "3ed78423-3bf1-4888-97a7-9ccfe47ca04a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify the following papers exist as described, and find any new competing papers from late 2025 through May 2026. Use WebSearch and WebFetch tools.\n\n1. Verify CLO paper exists: \"Cross-Lingual Optimization for Language Transfer in Large Language Models\" arXiv:2505.14297 ACL 2025. Search for it and check abstract.\n\n2. Verify \"Less is More: The Effectiveness of Compact Typological Language Representations\" arXiv:2509.20129 EMNLP 2025 exists and confirms Spearman ρ=0.358 for 300-feature URIEL+ vs ρ=0.260 for full 800-feature set.\n\n3. Search for NEW cross-lingual instruction tuning papers from January-May 2026 that combine typological features with multi-pivot data selection. Search:\n   - \"typological distance instruction tuning 2026 site:arxiv.org\"\n   - \"multi-pivot cross-lingual instruction tuning 2026\"\n   - \"URIEL multilingual instruction tuning 2026\"\n   - \"cross-lingual transfer low-resource instruction tuning 2026\"\n\n4. Search for any new papers on multilingual curriculum learning for LLMs in 2026:\n   - \"multilingual curriculum learning LLM 2026 site:arxiv.org\"\n   - \"cross-lingual curriculum instruction tuning arXiv 2026\"\n\n5. Search for recent Kazakh/Mongolian/Uyghur NLP papers from 2026:\n   - \"Kazakh NLP LLM 2026\"\n   - \"Mongolian Uyghur language model 2026 instruction\"\n\nReport what you find for each search, including paper titles, arXiv IDs if available, and whether the claimed paper exists as described. Focus on identifying any papers that closely parallel TWMP's approach of using typological features to weight multi-source instruction data with curriculum scheduling.",
    "agentId": "a0a0dd5e551224663",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Now let me compile my comprehensive findings report:\n\n## Summary of Search Results and Verification\n\n### 1. CLO Paper Verification: VERIFIED ✓\n\n**Paper:** \"Cross-Lingual Optimization for Language Transfer in Large Language Models\"\n- **arXiv ID:** 2505.14297\n- **Venue:** ACL 2025\n- **Status:** Verified and exists as described\n- **Main Contribution:** Proposes Cross-Lingual Optimization (CLO) that efficiently transfers English-centric LLMs to target languages while preserving English capabilities using publicly available English SFT data and translation models.\n- **Key Result:** CLO consistently outperforms supervised fine-tuning (SFT), achieving better performance with less data in low-resource scenarios. With only 3,200 samples, CLO surpasses SFT with 6,400 samples.\n\n**Source:** [Cross-Lingual Optimization for Language Transfer in Large Language Models](https://arxiv.org/abs/2505.14297)\n\n---\n\n### 2. Typological Representations Paper Verification: VERIFIED ✓\n\n**Paper:** \"Less is More: The Effectiveness of Compact Typological Language Representations\"\n- **arXiv ID:** 2509.20129\n- **Venue:** EMNLP 2025 Main Conference\n- **Status:** Verified and exists as described\n- **Claimed Results Verified:** The paper indeed confirms that the 300-feature URIEL+ using Laplacian Score method achieves **Spearman ρ = 0.358** compared to the full 800-feature URIEL set achieving **ρ = 0.260** - exactly matching your specifications.\n- **Main Contribution:** Proposes a pipeline to optimize the URIEL+ typological feature space through feature selection and imputation, demonstrating that compact typological representations outperform full feature sets on linguistic distance alignment and downstream tasks.\n\n**Source:** [Less is More: The Effectiveness of Compact Typological Language Representations](https://arxiv.org/abs/2509.20129)\n\n---\n\n### 3. NEW PAPERS from 2026 Combining Typological Features with Multi-Source Instruction Data:\n\n#### Highly Relevant - Direct Match:\n\n**A. \"Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models\"**\n- **arXiv ID:** 2602.03551\n- **Time:** February 2026\n- **Relevance:** Directly analyzes how target language typology drives translation quality in state-of-the-art multilingual translation systems (NLLB-200, Tower+), even after controlling for data resourcedness and script. Released fine-grained typological data for 212 languages in FLORES+ benchmark.\n- **Parallel to TWMP:** Similar approach of using typological properties to understand and optimize cross-lingual transfer, though focused on MT quality rather than instruction weighting.\n\n**Source:** [Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models](https://arxiv.org/abs/2602.03551)\n\n**B. \"Enhancing Multilingual LLM Pretraining with Model-Based Data Selection\"**\n- **arXiv ID:** 2502.10361\n- **Time:** February 2026\n- **Acceptance:** NeurIPS 2025 Datasets and Benchmarks track\n- **Relevance:** Develops model-based filtering framework for multilingual datasets addressing data selection across diverse linguistic contexts. Achieved 15% token efficiency on MMLU performance using 1B Llama model.\n- **Parallel to TWMP:** Uses model-based selection to weight diverse multilingual data, though not explicitly typology-driven, demonstrates data weighting principles across 20 languages.\n\n**Source:** [Enhancing Multilingual LLM Pretraining with Model-Based Data Selection](https://arxiv.org/abs/2502.10361)\n\n---\n\n### 4. Multilingual Curriculum Learning Papers from 2025-2026:\n\n**A. \"TildeOpen LLM: Leveraging Curriculum Learning to Achieve Equitable Language Representation\"**\n- **arXiv ID:** 2603.08182\n- **Time:** March 2026\n- **Relevance:** 30B-parameter open model for 34 European languages using curriculum-based training schedule alternating between uniform and natural language distributions. Directly combines curriculum learning with multilingual data weighting.\n- **Key Features:** Three-phase curriculum for data sampling, addresses cross-lingual interference\n- **Direct Parallel to TWMP:** Combines curriculum scheduling with weighted data distribution for multilingual LLMs\n\n**Source:** [TildeOpen LLM: Leveraging Curriculum Learning to Achieve Equitable Language Representation](https://arxiv.org/html/2603.08182)\n\n**B. \"Code-Switching Curriculum Learning for Multilingual Transfer in LLMs\"**\n- **arXiv ID:** 2411.02460\n- **Time:** November 2025 (late 2025)\n- **Relevance:** Proposes curriculum learning inspired by human second language acquisition, using progressive code-switching stages (token-level → sentence-level → monolingual). Addresses cross-lingual transfer systematically.\n- **Key Method:** Staged curriculum mimicking language learning acquisition\n\n**Source:** [Code-Switching Curriculum Learning for Multilingual Transfer in LLMs](https://arxiv.org/abs/2411.02460)\n\n**C. \"Revisiting Multilingual Data Mixtures in Language Model Pretraining\"**\n- **arXiv ID:** 2510.25947\n- **Time:** October 2025\n- **Relevance:** Controlled curriculum learning experiments examining cross-lingual competition and knowledge transfer dynamics. Investigates how timing/order of language inclusion affects performance.\n- **Finding:** Staging languages through curriculum learning does not mitigate negative interference\n\n**Source:** [Revisiting Multilingual Data Mixtures in Language Model Pretraining](https://arxiv.org/html/2510.25947v1)\n\n**D. \"Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics\"**\n- **arXiv ID:** 2601.21698\n- **Time:** January 2026\n- **Relevance:** Analyzes three linguistically motivated curricula (Age-of-Acquisition, word frequency, verb variation) to understand learning trajectory changes vs. simple reordering effects.\n\n**Source:** [Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics](https://arxiv.org/abs/2601.21698)\n\n---\n\n### 5. Typological Language Selection for Instruction Tuning (2025-2026):\n\n**A. \"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?\"**\n- **arXiv ID:** 2410.07809\n- **Time:** October 2024 (updated 2025)\n- **Relevance:** Proposes selecting diverse languages using linguistic features rather than random selection for instruction tuning. Addresses curse of multilinguality through linguistically-informed selection.\n- **Key Method:** Simple algorithm for choosing typologically diverse languages\n\n**Source:** [Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?](https://arxiv.org/abs/2410.07809)\n\n**B. \"Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages for Cross-Lingual POS Tagging\"**\n- **arXiv ID:** 2503.19979\n- **Time:** March 2026\n- **Relevance:** Takes holistic approach examining dataset-specific and fine-grained typological features for transfer language selection. Finds word overlap, type-token ratio, and genealogical distance as top predictors.\n- **Key Finding:** Combination of typological + dataset-dependent features provides best rankings\n- **Venue:** NAACL 2025 Workshop on Language Models for Underserved Communities\n\n**Source:** [Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages for Cross-Lingual POS Tagging](https://arxiv.org/html/2503.19979v1)\n\n---\n\n### 6. Kazakh/Mongolian/Uyghur Language Model Papers from 2026:\n\n**A. Kazakh - \"Llama-3.1-Sherkala-8B-Chat\" (Sherkala-Chat)**\n- **arXiv ID:** 2503.01493\n- **Time:** March 2026\n- **Status:** State-of-the-art instruction-tuned model for Kazakh\n- **Details:** Adapted from LLaMA-3.1-8B, trained on 45.3B tokens across Kazakh, English, Russian, Turkish. Significantly outperforms existing open Kazakh models of similar scale.\n- **Note:** Related project - KazLLM (8B and 70B versions) developed by ISSAI at Nazarbayev University\n\n**Sources:** \n- [Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting](https://arxiv.org/html/2503.01493)\n- [Llama-3.1-Sherkala-8B-Chat on arXiv](https://arxiv.org/abs/2503.01493)\n\n**B. Kazakh - \"LLM-Assisted Weak Supervision for Low-Resource Kazakh Sequence Labeling\"**\n- **Time:** 2026 (MDPI Applied Sciences)\n- **Relevance:** Addresses Kazakh NLP via LLM-assisted weak supervision framework generating synthetic annotations for sequence labeling, combined with CRF-refined NER/POS models.\n\n**Source:** [LLM-Assisted Weak Supervision for Low-Resource Kazakh Sequence Labeling: Synthetic Annotation and CRF-Refined NER/POS Models](https://www.mdpi.com/2076-3417/16/8/3632)\n\n**C. Mongolian - \"MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs\"**\n- **arXiv ID:** 2411.09492\n- **Time:** November 2024\n- **Relevance:** Specialized benchmark for Mongolian based on Modern Mongolian Language Textbook. Finds GPT-4-Turbo best at syntax (90.69%) and knowledge (80.52%), but all models struggle with reasoning (max 29.6%).\n\n**Source:** [MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs](https://arxiv.org/html/2411.09492v1)\n\n**D. Uyghur/Mongolian - \"Do Chinese models speak Chinese languages?\"**\n- **arXiv ID:** 2504.00289\n- **Time:** April 2026\n- **Relevance:** Evaluates Uyghur and Mongolian capabilities across models. Notes Llama3-Instruct is uniquely good at Uyghur and top-performing in Tibetan/Mongolian. Highlights lower-resource language challenges.\n\n**Source:** [Do Chinese models speak Chinese languages?](https://arxiv.org/html/2504.00289v1)\n\n---\n\n### 6. Most Directly Competing Papers (Closest to TWMP's Approach):\n\nPapers that most closely parallel TWMP's combination of typological features + multi-source data weighting + curriculum scheduling:\n\n1. **TildeOpen LLM** (2603.08182) - Combines curriculum learning with weighted multilingual data distribution\n2. **Assessing Impact of Typological Features on MT** (2602.03551) - Uses typological properties to drive model optimization across 212 languages\n3. **Linguistically-Informed Multilingual Instruction Tuning** (2410.07809) - Typology-based language selection for instruction tuning\n4. **Untangling Typology Influence** (2503.19979) - Fine-grained typological feature weighting for language selection\n5. **Code-Switching Curriculum Learning** (2411.02460) - Curriculum approach to cross-lingual transfer\n\n**None of these papers explicitly combine all three elements (typological distance weighting + multi-pivot instruction data + curriculum scheduling) as described for TWMP, suggesting TWMP may represent a novel combination of these approaches.**\n\nSources:\n- [TildeOpen LLM: Leveraging Curriculum Learning to Achieve Equitable Language Representation](https://arxiv.org/html/2603.08182)\n- [Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models](https://arxiv.org/abs/2602.03551)\n- [Linguistically-Informed Multilingual Instruction Tuning](https://arxiv.org/abs/2410.07809)\n- [Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages](https://arxiv.org/html/2503.19979v1)\n- [Code-Switching Curriculum Learning for Multilingual Transfer in LLMs](https://arxiv.org/abs/2411.02460)"
      }
    ],
    "totalDurationMs": 93328,
    "totalTokens": 35432,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 31521,
      "output_tokens": 3179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 726
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 3179,
          "cache_read_input_tokens": 31521,
          "cache_creation_input_tokens": 726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 726,
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
      "otherToolCount": 22
    }
  },
  "sourceToolAssistantUUID": "6ed70c49-d018-4439-9f6a-e0b74ebf930d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
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
  "leafUuid": "3ed78423-3bf1-4888-97a7-9ccfe47ca04a",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Review agent conducting independent verification on Round 7",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e"
}
```

---

### Tool result

_source line 16 · 2026-05-10T07:57:53.089Z_

<details><summary>↩ Tool result · `toolu_01TndH3cHqK89PQiYLHFZ6Du`</summary>

```text
Based on my comprehensive search and verification, here is my detailed fact-check report:

## FACT-CHECK REPORT

### 1. AYA DATASET LANGUAGE COVERAGE (Turkish, Kyrgyz, Uzbek)

**Claim Status: PARTIALLY UNVERIFIABLE**

**Findings:**
- **Overall Aya stats confirmed:** The Aya Collection consists of 513M instances covering 114 languages ✓
- **Turkish inclusion confirmed:** Turkish is included in the dataset with evaluation coverage
- **Kyrgyz: Unconfirmed** - No searchable source found specifying "~4.1M instances" for Kyrgyz. Language code "KK" was not found in Aya documentation
- **Uzbek: Confirmed present** - Explicitly mentioned as one of the underrepresented languages included in the Aya Collection
- **Specific instance counts: NOT FOUND** - The detailed language breakdown table with exact counts for Turkish, Kyrgyz, and Uzbek is not accessible via the HuggingFace dataset card or blog posts that were searchable

**Critical Issue:** The Aya collection language statistics table exists on the HuggingFace dataset card (at https://huggingface.co/datasets/CohereLabs/aya_collection_language_split) but was not fully retrievable. The specific claim of "~4.1M instances" for Kyrgyz could not be verified from public sources.

---

### 2. QWEN3.5-9B MODEL CLAIMS

**Claim Status: MOSTLY ACCURATE WITH CLARIFICATION NEEDED**

**Findings:**
- **Release date claim (March 2026):** The claim is slightly imprecise. The Qwen3.5 series followed a phased release:
  - Qwen3.5 main model: February 16, 2026
  - Qwen3.5-9B small model series: March 1-2, 2026 ✓ (Confirmed)
  - Citation on HuggingFace shows: February 2026
  
  **Verdict:** The paper's claim of "March 2026" is technically correct for the Qwen3.5-9B specifically, but the broader model was released in February.

- **248K-token vocabulary:** CONFIRMED ✓
  - Token embedding: 248,320 tokens (padded)
  - LM Output: 248,320 tokens (padded)

- **201 languages coverage:** CONFIRMED ✓
  - "Expanded support to 201 languages and dialects"

- **Series composition (0.8B/2B/4B/9B, no 7B):** CONFIRMED ✓
  - The Qwen3.5 small series consists of exactly these four models
  - No 7B variant exists

---

### 3. KAZMMU BENCHMARK (arXiv:2502.12829)

**Claim Status: PARTIALLY INACCURATE**

**Findings:**
- **23K Kazakh questions:** INCORRECT/INCOMPLETE
  - The dataset contains **10,969 Kazakh questions** + 12,031 Russian questions = 23,000 total
  - Not "23K Kazakh questions" but 23K total with roughly 48% in Kazakh
  
- **Evaluated models:** CONFIRMED ✓
  - Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 were all evaluated

- **ACL 2025 long paper claim:** UNCONFIRMED
  - The paper is currently an arXiv preprint (arXiv:2502.12829) submitted February 18, 2025
  - The abstract states "Data and code will be made available upon acceptance," indicating it is under review
  - No confirmation found that it was accepted as an ACL 2025 long paper
  - **Status: Likely not yet published at ACL 2025** (appears to still be under review)

---

### 4. MILIC-EVAL (arXiv:2503.01150)

**Claim Status: MOSTLY CONFIRMED**

**Findings:**
- **Languages covered (Tibetan, Uyghur, Kazakh, Mongolian):** CONFIRMED ✓

- **9 tasks, 24K instances:** CONFIRMED ✓

- **ACL 2025 Findings publication:** CONFIRMED ✓
  - This is officially published in ACL 2025 (Findings track)
  - Available at ACL Anthology: https://aclanthology.org/2025.findings-acl.578/

- **GPT-4o-mini on Mongolian tasks:** CONFIRMED with specifics ✓
  - GPT-4o-mini achieved **20.7% average** across Mongolian tasks
  - Random baseline: 13.1%
  - Specific breakdown:
    - Vocabulary Understanding: 30.2%
    - Title Generation: 6.4%
    - Machine Translation (EN→Mongolian): 0.8%
    - Math Reasoning: 7.0%
  - **Verdict:** The claim that it achieves "only slightly above random" is accurate and well-supported

---

### 5. RECENT AYA DATASET STATISTICS (2025-2026)

**Claim Status: NOT FOUND**

No recent (2025-2026) papers were found showing an updated Aya dataset language statistics breakdown. The most recent comprehensive documentation appears to be the original 2024 Aya Dataset paper (arXiv:2402.06619).

---

## SUMMARY TABLE

| Claim | Status | Confidence |
|-------|--------|-----------|
| Aya: Turkish multi-million instances | Confirmed present but no specific count | Medium |
| Aya: Kyrgyz ~4.1M instances | Unverifiable | Low |
| Aya: Uzbek meaningful coverage | Confirmed | High |
| Qwen3.5-9B: March 2026 release | Confirmed (for small series) | High |
| Qwen3.5-9B: 248K vocab, 201 languages | Confirmed | High |
| Qwen3.5: 0.8B/2B/4B/9B (no 7B) | Confirmed | High |
| KazMMLU: 23K Kazakh questions | Incorrect (10.9K Kazakh of 23K total) | High |
| KazMMLU: Llama-3.1, Qwen-2.5, GPT-4, DeepSeek V3 | Confirmed | High |
| KazMMLU: ACL 2025 long paper | Unconfirmed (appears under review) | Low |
| MiLiC-Eval: 4 languages, 9 tasks, 24K instances | Confirmed | High |
| MiLiC-Eval: ACL 2025 Findings | Confirmed | High |
| MiLiC-Eval: GPT-4o-mini slightly above random on Mongolian | Confirmed (20.7% vs 13.1% random) | High |

---

## SOURCES

- [Aya Collection HuggingFace](https://huggingface.co/datasets/CohereLabs/aya_collection)
- [Aya Dataset Paper - arXiv 2402.06619](https://arxiv.org/abs/2402.06619)
- [Qwen3.5-9B HuggingFace](https://huggingface.co/Qwen/Qwen3.5-9B)
- [KazMMLU Paper - arXiv 2502.12829](https://arxiv.org/abs/2502.12829)
- [MiLiC-Eval Paper - arXiv 2503.01150](https://arxiv.org/abs/2503.01150)
- [MiLiC-Eval ACL 2025 Findings](https://aclanthology.org/2025.findings-acl.578/)
- [Cohere AI Aya Initiative](https://cohere.com/research/aya)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "767b7f4e-a3d4-442a-99fb-c6349e2ea3dd",
  "isSidechain": false,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "type": "user",
  "uuid": "3d65df6d-7b8f-4a80-830a-05c83169f3ca",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research paper idea. I need to verify factual claims about datasets and models. Use WebSearch and WebFetch.\n\n1. Verify Aya dataset coverage of Turkic languages. The paper claims:\n   - Turkish: \"multi-million instances\" in Aya collection\n   - Kyrgyz: \"~4.1M instances\"\n   - Uzbek: \"confirmed present with meaningful coverage\"\n   The minimum threshold for inclusion as a pivot is 5,000 instances.\n   \n   Search: \"Aya collection dataset Turkic languages coverage\" HuggingFace\n   Try: site:huggingface.co \"CohereForAI/aya_collection\" OR \"Aya dataset language statistics\"\n   Also try: \"Aya collection 513M instances 114 languages\" to verify the overall stats\n\n2. Verify Qwen3.5-9B model claims:\n   - Released \"March 2026\" (not February)\n   - 248K-token vocabulary spanning 201 languages\n   - Series is 0.8B/2B/4B/9B (no 7B)\n   Search: \"Qwen3.5 9B release date March 2026\" OR \"Qwen3.5 model specifications\"\n   Try: site:huggingface.co Qwen3.5-9B OR \"Qwen/Qwen3.5-9B\"\n\n3. Verify KazMMLU (arXiv:2502.12829) benchmark claims:\n   - 23K Kazakh questions\n   - Evaluates Llama-3.1, Qwen-2.5, GPT-4, DeepSeek V3\n   - ACL 2025 long paper\n   Search: arXiv:2502.12829 or \"KazMMLU Kazakh benchmark ACL 2025\"\n\n4. Verify MiLiC-Eval (arXiv:2503.01150) claims:\n   - Covers Tibetan, Uyghur, Kazakh, Mongolian\n   - 9 tasks, 24K instances\n   - ACL 2025 Findings\n   - GPT-4o-mini achieves \"only slightly above random on Mongolian tasks\"\n   Search: arXiv:2503.01150 or \"MiLiC-Eval minority languages benchmark\"\n\n5. Search for any recent (2025-2026) papers showing Aya dataset language statistics:\n   - \"Aya collection dataset statistics languages 2024 2025\"\n   - \"CohereForAI Aya language breakdown\"\n\nReport precise findings on whether each claim is verifiable and accurate.",
    "agentId": "ad38ba5961e1c35e6",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search and verification, here is my detailed fact-check report:\n\n## FACT-CHECK REPORT\n\n### 1. AYA DATASET LANGUAGE COVERAGE (Turkish, Kyrgyz, Uzbek)\n\n**Claim Status: PARTIALLY UNVERIFIABLE**\n\n**Findings:**\n- **Overall Aya stats confirmed:** The Aya Collection consists of 513M instances covering 114 languages ✓\n- **Turkish inclusion confirmed:** Turkish is included in the dataset with evaluation coverage\n- **Kyrgyz: Unconfirmed** - No searchable source found specifying \"~4.1M instances\" for Kyrgyz. Language code \"KK\" was not found in Aya documentation\n- **Uzbek: Confirmed present** - Explicitly mentioned as one of the underrepresented languages included in the Aya Collection\n- **Specific instance counts: NOT FOUND** - The detailed language breakdown table with exact counts for Turkish, Kyrgyz, and Uzbek is not accessible via the HuggingFace dataset card or blog posts that were searchable\n\n**Critical Issue:** The Aya collection language statistics table exists on the HuggingFace dataset card (at https://huggingface.co/datasets/CohereLabs/aya_collection_language_split) but was not fully retrievable. The specific claim of \"~4.1M instances\" for Kyrgyz could not be verified from public sources.\n\n---\n\n### 2. QWEN3.5-9B MODEL CLAIMS\n\n**Claim Status: MOSTLY ACCURATE WITH CLARIFICATION NEEDED**\n\n**Findings:**\n- **Release date claim (March 2026):** The claim is slightly imprecise. The Qwen3.5 series followed a phased release:\n  - Qwen3.5 main model: February 16, 2026\n  - Qwen3.5-9B small model series: March 1-2, 2026 ✓ (Confirmed)\n  - Citation on HuggingFace shows: February 2026\n  \n  **Verdict:** The paper's claim of \"March 2026\" is technically correct for the Qwen3.5-9B specifically, but the broader model was released in February.\n\n- **248K-token vocabulary:** CONFIRMED ✓\n  - Token embedding: 248,320 tokens (padded)\n  - LM Output: 248,320 tokens (padded)\n\n- **201 languages coverage:** CONFIRMED ✓\n  - \"Expanded support to 201 languages and dialects\"\n\n- **Series composition (0.8B/2B/4B/9B, no 7B):** CONFIRMED ✓\n  - The Qwen3.5 small series consists of exactly these four models\n  - No 7B variant exists\n\n---\n\n### 3. KAZMMU BENCHMARK (arXiv:2502.12829)\n\n**Claim Status: PARTIALLY INACCURATE**\n\n**Findings:**\n- **23K Kazakh questions:** INCORRECT/INCOMPLETE\n  - The dataset contains **10,969 Kazakh questions** + 12,031 Russian questions = 23,000 total\n  - Not \"23K Kazakh questions\" but 23K total with roughly 48% in Kazakh\n  \n- **Evaluated models:** CONFIRMED ✓\n  - Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 were all evaluated\n\n- **ACL 2025 long paper claim:** UNCONFIRMED\n  - The paper is currently an arXiv preprint (arXiv:2502.12829) submitted February 18, 2025\n  - The abstract states \"Data and code will be made available upon acceptance,\" indicating it is under review\n  - No confirmation found that it was accepted as an ACL 2025 long paper\n  - **Status: Likely not yet published at ACL 2025** (appears to still be under review)\n\n---\n\n### 4. MILIC-EVAL (arXiv:2503.01150)\n\n**Claim Status: MOSTLY CONFIRMED**\n\n**Findings:**\n- **Languages covered (Tibetan, Uyghur, Kazakh, Mongolian):** CONFIRMED ✓\n\n- **9 tasks, 24K instances:** CONFIRMED ✓\n\n- **ACL 2025 Findings publication:** CONFIRMED ✓\n  - This is officially published in ACL 2025 (Findings track)\n  - Available at ACL Anthology: https://aclanthology.org/2025.findings-acl.578/\n\n- **GPT-4o-mini on Mongolian tasks:** CONFIRMED with specifics ✓\n  - GPT-4o-mini achieved **20.7% average** across Mongolian tasks\n  - Random baseline: 13.1%\n  - Specific breakdown:\n    - Vocabulary Understanding: 30.2%\n    - Title Generation: 6.4%\n    - Machine Translation (EN→Mongolian): 0.8%\n    - Math Reasoning: 7.0%\n  - **Verdict:** The claim that it achieves \"only slightly above random\" is accurate and well-supported\n\n---\n\n### 5. RECENT AYA DATASET STATISTICS (2025-2026)\n\n**Claim Status: NOT FOUND**\n\nNo recent (2025-2026) papers were found showing an updated Aya dataset language statistics breakdown. The most recent comprehensive documentation appears to be the original 2024 Aya Dataset paper (arXiv:2402.06619).\n\n---\n\n## SUMMARY TABLE\n\n| Claim | Status | Confidence |\n|-------|--------|-----------|\n| Aya: Turkish multi-million instances | Confirmed present but no specific count | Medium |\n| Aya: Kyrgyz ~4.1M instances | Unverifiable | Low |\n| Aya: Uzbek meaningful coverage | Confirmed | High |\n| Qwen3.5-9B: March 2026 release | Confirmed (for small series) | High |\n| Qwen3.5-9B: 248K vocab, 201 languages | Confirmed | High |\n| Qwen3.5: 0.8B/2B/4B/9B (no 7B) | Confirmed | High |\n| KazMMLU: 23K Kazakh questions | Incorrect (10.9K Kazakh of 23K total) | High |\n| KazMMLU: Llama-3.1, Qwen-2.5, GPT-4, DeepSeek V3 | Confirmed | High |\n| KazMMLU: ACL 2025 long paper | Unconfirmed (appears under review) | Low |\n| MiLiC-Eval: 4 languages, 9 tasks, 24K instances | Confirmed | High |\n| MiLiC-Eval: ACL 2025 Findings | Confirmed | High |\n| MiLiC-Eval: GPT-4o-mini slightly above random on Mongolian | Confirmed (20.7% vs 13.1% random) | High |\n\n---\n\n## SOURCES\n\n- [Aya Collection HuggingFace](https://huggingface.co/datasets/CohereLabs/aya_collection)\n- [Aya Dataset Paper - arXiv 2402.06619](https://arxiv.org/abs/2402.06619)\n- [Qwen3.5-9B HuggingFace](https://huggingface.co/Qwen/Qwen3.5-9B)\n- [KazMMLU Paper - arXiv 2502.12829](https://arxiv.org/abs/2502.12829)\n- [MiLiC-Eval Paper - arXiv 2503.01150](https://arxiv.org/abs/2503.01150)\n- [MiLiC-Eval ACL 2025 Findings](https://aclanthology.org/2025.findings-acl.578/)\n- [Cohere AI Aya Initiative](https://cohere.com/research/aya)"
      }
    ],
    "totalDurationMs": 78555,
    "totalTokens": 32027,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 29810,
      "output_tokens": 1964,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 248
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1964,
          "cache_read_input_tokens": 29810,
          "cache_creation_input_tokens": 248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 248,
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
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "767b7f4e-a3d4-442a-99fb-c6349e2ea3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T07:58:02.671Z_

<details><summary>↩ Tool result · `toolu_01Ef2mSn41hDfya4FLHuawDj`</summary>

```text
Excellent. Now I have comprehensive information. Let me compile my findings into a detailed report.

## COMPREHENSIVE VERIFICATION REPORT: TWMP (Typologically-Weighted Multi-Pivot) Paper Review

### 1. VERIFICATION OF CITED PAPERS

#### LangGPS - VERIFIED ✓
**Citation:** "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning" arXiv:2511.10229 AAAI 2026

**Status:** Paper exists and is accurately described
**Abstract:** LangGPS proposes a two-stage pre-selection framework using "language separability"—quantifying how well samples in different languages can be distinguished in the model's representation space. It filters training data based on separability scores, then refines selections using existing methods.
**Key Results:** Tested across six benchmarks and 22 languages; demonstrates improvements in effectiveness for low-resource languages and understanding tasks. Shows that high-separability samples create clearer language boundaries while low-separability samples function as bridges for cross-lingual alignment.
**Source:** [LangGPS on arXiv](https://arxiv.org/abs/2511.10229)

#### Budget-Xfer - VERIFIED ✓
**Citation:** "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages" arXiv:2603.27651 SIGIR 2026

**Status:** Paper exists and is accurately described
**Abstract:** Formulates multi-source cross-lingual transfer as a budget-constrained resource allocation problem. Jointly optimizes which source languages to include AND how much data to allocate from each language, given a fixed annotation budget.
**Key Results:** Evaluated on named entity recognition and sentiment analysis for Hausa, Yoruba, and Swahili using two multilingual models (288 experiments). Demonstrates that multi-source transfer significantly outperforms single-source transfer (Cohen's d = 0.80 to 1.98). Interestingly reveals that embedding similarity (common heuristic for language selection) shows task-dependent effectiveness.
**Source:** [Budget-Xfer on arXiv](https://arxiv.org/abs/2603.27651)

---

### 2. COMPETING/RELATED WORK IDENTIFIED

#### DIRECT COMPETITORS TO TWMP'S CORE NOVELTY:

**A. TIPA (Typologically Informed Parameter Aggregation) - 2026 - STRONG COMPETITOR**
**Citation:** [TIPA: Typologically Informed Parameter Aggregation](https://arxiv.org/abs/2601.16629), Findings of EACL 2026
- **Core Innovation:** Constructs proxy language adapters by **aggregating existing adapters weighted by typological similarity** (zero-shot, training-free)
- **Scope:** Evaluated on 5 NLP tasks across 230+ languages
- **Key Result:** Consistently outperforms baselines like English-only fine-tuning and selecting the closest-language adapter; largest gains for languages lacking dedicated adapters
- **Relation to TWMP:** Directly uses typological similarity for weighting multilingual modules. This is very similar conceptually to TWMP's use of typological weighting for multi-pivot data.
- **Source:** [TIPA on ACL Anthology](https://aclanthology.org/2026.findings-eacl.119/)

**B. URIEL+ Recent Enhancements (2025-2026) - COMPLEMENTARY BUT RELEVANT**
- **"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+"** (arXiv:2510.27183, March 2026)
  - Extends URIEL+ with script vectors for 7,488 languages and integrates Glottolog for 18,710 additional languages
  - Reduces feature sparsity by 14% for script vectors
- **"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+"** (arXiv:2510.19217, March 2026, EACL 2026 Student Workshop)
  - Introduces type-matched language distances with structure-aware representations (speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, latent variables model for typology)
  - Creates robust composite distance for cross-lingual transfer
- **Relation to TWMP:** These improve the typological distance metrics that TWMP would rely on, but don't themselves implement multi-pivot weighting or data selection
- **Sources:** [arXiv:2510.27183](https://arxiv.org/abs/2510.27183), [arXiv:2510.19217](https://arxiv.org/abs/2510.19217)

**C. PROM (Pivoted and Regulated Optimization) - 2025 - RELATED APPROACH**
**Citation:** Published at NAACL 2025 (April, Albuquerque)
- **Core Innovation:** Treats English as an "internal pivot language" and disentangles roles of English vs. target-language data via separate training objectives with regulation between them
- **Problem Addressed:** Negative interference when combining English instruction-tuning data with translated versions
- **Relation to TWMP:** Also uses pivoting concept for multilingual instruction learning, but focuses on English as single pivot rather than multi-pivot weighting scheme
- **Source:** [PROM on ACL Anthology](https://aclanthology.org/2025.naacl-short.19/)

**D. Linguistically-Informed Multilingual Instruction Tuning - 2024**
**Citation:** [Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?](https://arxiv.org/abs/2410.07809), Published in Transactions on Machine Learning Research (November 2025)
- **Approach:** Uses typological feature vectors and k-means clustering to select diverse languages for instruction tuning
- **Finding:** Careful selection based on linguistic diversity outperforms random language selection; addresses "curse of multilinguality"
- **Relation to TWMP:** Also uses typological features for language selection in instruction tuning, but focuses on selecting a subset of languages rather than weighting multiple sources

#### TANGENTIALLY RELATED RECENT WORK:

**E. "Assessing the Impact of Typological Features on Multilingual Machine Translation"** (arXiv:2602.03551, 2026 EACL)
- Analyzes how target language typology drives translation quality in NLLB-200 and Tower+ models
- Releases fine-grained typological properties for 212 languages in FLORES+ benchmark
- Shows that certain typological properties benefit from broader decoding strategies

**F. "Merge and Conquer: Instructing Multilingual Models by Adding Target Language Weights"** (arXiv:2603.28263)
- Merges instruction-tuned LLMs with language-specific base models for multilingual capability
- Avoids continual pre-training and repeated fine-tuning
- Lightweight alternative to traditional adaptation for low-resource languages

**G. Cross-Lingual Expert Language Models (X-ELM)** (arXiv:2401.10440)
- Uses typological structure to specialize expert models for distinct language clusters
- Training along language family hierarchies provides performance benefits
- Multi-source language training with typologically/embedding-based dissimilar triplets outperforms single-language baselines

**H. DATAPROPHET (ICLR 2026)** (arXiv:2603.19688)
- Determines dataset weighting in mixtures using DATAPROPHET scores
- Integrates cross-modal similarity, multimodal perplexity, and dataset diversity
- Training-free, interpretable metric for data weighting

**I. Recent Work on Multi-Source Selection:**
- KazMMLU (arXiv:2502.12829, ACL 2025): First MMLU-style benchmark for Kazakh (23,000 questions)
- Budget-Xfer (as cited above) addresses multi-source optimization for African languages
- PLUG (arXiv:2311.08711, ACL 2024): Leverages English pivot in cross-lingual instruction tuning

---

### 3. BENCHMARKS AND EVALUATION GAPS FOUND

**KazMMLU:** Successfully identified and verified
- First MMLU-style dataset specifically for Kazakh
- 23,000 questions (10,969 Kazakh + 12,031 Russian)
- Presented at ACL 2025; covers STEM, humanities, social sciences
- **Source:** [KazMMLU on arXiv](https://arxiv.org/abs/2502.12829)

**MiLiC-Eval:** Partially verified
- Located on Papers with Code: [MiLiC-Eval: Benchmarking Multilingual LLMs for China's...](https://paperswithcode.com/paper/milic-eval-benchmarking-multilingual-llms-for)
- Appears to be a benchmark for multilingual LLMs, but full details not retrieved

---

### 4. KEY FINDINGS ON NOVELTY

**STRENGTHS OF TWMP'S NOVELTY CLAIM:**

1. **Multi-Pivot Weighting Not Yet Fully Explored:** While TIPA weights adapter aggregation by typological similarity and PROM uses pivot languages, TWMP appears to be the **first systematic approach to combine BOTH concepts**: using multiple typologically-diverse pivot languages with learned or typologically-informed weighting for data selection in instruction tuning.

2. **Data Selection vs. Module Aggregation:** TIPA aggregates existing trained adapters; TWMP appears to weight raw instruction-tuning data before training, which is a different problem.

3. **Pivot Language Strategy Evolution:** PLUG and PROM focus on English as pivot; TWMP's multi-pivot approach with typological weighting is more sophisticated.

**POTENTIAL OVERLAP/CONCERNS:**

1. **TIPA's March 2026 publication (same venue cycle as TWMP):** TIPA demonstrates that typological similarity weighting for multilingual modules is effective. If TWMP's core novelty is similar weighting applied to data rather than adapters, the conceptual distance may be narrow.

2. **Typological feature integration:** Multiple papers (X-ELM, Linguistically-Informed Instruction Tuning, URIEL+ enhancements) all demonstrate value of typological features for language selection/clustering in recent 2025-2026 work.

3. **Data weighting literature:** DATAPROPHET and other data weighting approaches are relatively recent (ICLR 2026), suggesting this is an active research area.

---

### 5. CRITICAL ASSESSMENT

**TWMP appears to have legitimate novelty IF:**
- The combination of typological distance metrics (URIEL/URIEL+) with multi-source pivot language selection for instruction data weighting is novel
- The specific weighting formulation or curriculum learning approach is non-obvious
- Empirical results on Kazakh/Mongolian and other low-resource language benchmarks are strong

**AREAS OF CONCERN:**
1. TIPA (published March 2026 in EACL Findings) demonstrates the effectiveness of typological-similarity-based weighting for multilingual NLP at scale (230+ languages, 5 tasks)
2. The conceptual gap between "weight adapters by typology" (TIPA) and "weight data sources by typology" (TWMP) may not be substantial enough to constitute strong novelty
3. Pivot language selection with typological grounding is well-explored (PLUG, PROM, recent work on language families)

**RECOMMENDATIONS FOR AUTHORS:**
1. Clearly differentiate from TIPA's adapter aggregation approach—emphasize why data-level weighting is fundamentally different/better
2. Demonstrate superiority over simpler baselines combining URIEL+ distances with standard multi-source selection
3. Show that typological weighting outperforms embedding-based or other heuristic weighting (as Budget-Xfer found embedding similarity isn't always better)
4. Provide extensive evaluation on truly low-resource languages (Kazakh, Mongolian, African languages) where the approach should shine

---

## SOURCES

### Verified Cited Papers
- [LangGPS on arXiv](https://arxiv.org/abs/2511.10229)
- [Budget-Xfer on arXiv](https://arxiv.org/abs/2603.27651)

### Major Competing/Related Work (2025-2026)
- [TIPA: Typologically Informed Parameter Aggregation](https://arxiv.org/abs/2601.16629) - EACL 2026 Findings
- [URIEL+ Script Expansion](https://arxiv.org/abs/2510.27183) - March 2026
- [Modality Matching in URIEL+](https://arxiv.org/abs/2510.19217) - EACL 2026 Student Workshop
- [PROM: Pivoted Optimization](https://aclanthology.org/2025.naacl-short.19/) - NAACL 2025
- [Linguistically-Informed Instruction Tuning](https://arxiv.org/abs/2410.07809) - TMLR November 2025
- [Assessing Typological Features in MT](https://arxiv.org/abs/2602.03551) - EACL 2026
- [Merge and Conquer Multilingual Models](https://arxiv.org/abs/2603.28263)
- [Cross-Lingual Expert Language Models](https://arxiv.org/abs/2401.10440)
- [DATAPROPHET Data Weighting](https://arxiv.org/abs/2603.19688) - ICLR 2026
- [KazMMLU Benchmark](https://arxiv.org/abs/2502.12829) - ACL 2025
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "618f5799-c50a-4570-b0df-5a1f41e09f3a",
  "isSidechain": false,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "type": "user",
  "uuid": "0634603a-d391-453e-9536-f851271912a0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing an NLP research paper idea called TWMP (Typologically-Weighted Multi-Pivot). I need to independently verify several cited papers exist and find any competing work. Use WebSearch and WebFetch.\n\n1. Verify LangGPS exists: \"LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning\" arXiv:2511.10229 AAAI 2026. Search for it, check abstract.\n\n2. Verify Budget-Xfer exists: arXiv:2603.27651 SIGIR 2026 on budget-constrained source language selection for cross-lingual transfer to African languages. Search for \"Budget-Xfer cross-lingual African languages SIGIR 2026\" or the arXiv ID.\n\n3. Search for competing papers that combine typological language features (URIEL/URIEL+) with data weighting for cross-lingual NLP:\n   - site:arxiv.org \"URIEL\" \"instruction tuning\" 2025 2026\n   - \"typological features\" \"data selection\" multilingual 2026\n   - \"lang2vec\" OR \"URIEL\" \"cross-lingual transfer\" \"curriculum\" 2025 OR 2026\n\n4. Search Papers With Code for SOTA on Kazakh/Mongolian MMLU-style benchmarks:\n   - site:paperswithcode.com KazMMLU\n   - site:paperswithcode.com MiLiC-Eval\n   - \"Kazakh language model benchmark 2026\"\n\n5. Search for any papers on typological similarity-based adapter aggregation or LoRA merging for multilingual NLP in 2025-2026:\n   - \"typological similarity LoRA\" multilingual 2025 2026\n   - \"TIPA typological adapter\" multilingual 2026\n\nReport all findings including whether the cited papers exist as described, and importantly whether any NEW papers have appeared that would compete with TWMP's novelty claim.",
    "agentId": "af9cb2e5e5a668192",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent. Now I have comprehensive information. Let me compile my findings into a detailed report.\n\n## COMPREHENSIVE VERIFICATION REPORT: TWMP (Typologically-Weighted Multi-Pivot) Paper Review\n\n### 1. VERIFICATION OF CITED PAPERS\n\n#### LangGPS - VERIFIED ✓\n**Citation:** \"LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning\" arXiv:2511.10229 AAAI 2026\n\n**Status:** Paper exists and is accurately described\n**Abstract:** LangGPS proposes a two-stage pre-selection framework using \"language separability\"—quantifying how well samples in different languages can be distinguished in the model's representation space. It filters training data based on separability scores, then refines selections using existing methods.\n**Key Results:** Tested across six benchmarks and 22 languages; demonstrates improvements in effectiveness for low-resource languages and understanding tasks. Shows that high-separability samples create clearer language boundaries while low-separability samples function as bridges for cross-lingual alignment.\n**Source:** [LangGPS on arXiv](https://arxiv.org/abs/2511.10229)\n\n#### Budget-Xfer - VERIFIED ✓\n**Citation:** \"Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages\" arXiv:2603.27651 SIGIR 2026\n\n**Status:** Paper exists and is accurately described\n**Abstract:** Formulates multi-source cross-lingual transfer as a budget-constrained resource allocation problem. Jointly optimizes which source languages to include AND how much data to allocate from each language, given a fixed annotation budget.\n**Key Results:** Evaluated on named entity recognition and sentiment analysis for Hausa, Yoruba, and Swahili using two multilingual models (288 experiments). Demonstrates that multi-source transfer significantly outperforms single-source transfer (Cohen's d = 0.80 to 1.98). Interestingly reveals that embedding similarity (common heuristic for language selection) shows task-dependent effectiveness.\n**Source:** [Budget-Xfer on arXiv](https://arxiv.org/abs/2603.27651)\n\n---\n\n### 2. COMPETING/RELATED WORK IDENTIFIED\n\n#### DIRECT COMPETITORS TO TWMP'S CORE NOVELTY:\n\n**A. TIPA (Typologically Informed Parameter Aggregation) - 2026 - STRONG COMPETITOR**\n**Citation:** [TIPA: Typologically Informed Parameter Aggregation](https://arxiv.org/abs/2601.16629), Findings of EACL 2026\n- **Core Innovation:** Constructs proxy language adapters by **aggregating existing adapters weighted by typological similarity** (zero-shot, training-free)\n- **Scope:** Evaluated on 5 NLP tasks across 230+ languages\n- **Key Result:** Consistently outperforms baselines like English-only fine-tuning and selecting the closest-language adapter; largest gains for languages lacking dedicated adapters\n- **Relation to TWMP:** Directly uses typological similarity for weighting multilingual modules. This is very similar conceptually to TWMP's use of typological weighting for multi-pivot data.\n- **Source:** [TIPA on ACL Anthology](https://aclanthology.org/2026.findings-eacl.119/)\n\n**B. URIEL+ Recent Enhancements (2025-2026) - COMPLEMENTARY BUT RELEVANT**\n- **\"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+\"** (arXiv:2510.27183, March 2026)\n  - Extends URIEL+ with script vectors for 7,488 languages and integrates Glottolog for 18,710 additional languages\n  - Reduces feature sparsity by 14% for script vectors\n- **\"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+\"** (arXiv:2510.19217, March 2026, EACL 2026 Student Workshop)\n  - Introduces type-matched language distances with structure-aware representations (speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, latent variables model for typology)\n  - Creates robust composite distance for cross-lingual transfer\n- **Relation to TWMP:** These improve the typological distance metrics that TWMP would rely on, but don't themselves implement multi-pivot weighting or data selection\n- **Sources:** [arXiv:2510.27183](https://arxiv.org/abs/2510.27183), [arXiv:2510.19217](https://arxiv.org/abs/2510.19217)\n\n**C. PROM (Pivoted and Regulated Optimization) - 2025 - RELATED APPROACH**\n**Citation:** Published at NAACL 2025 (April, Albuquerque)\n- **Core Innovation:** Treats English as an \"internal pivot language\" and disentangles roles of English vs. target-language data via separate training objectives with regulation between them\n- **Problem Addressed:** Negative interference when combining English instruction-tuning data with translated versions\n- **Relation to TWMP:** Also uses pivoting concept for multilingual instruction learning, but focuses on English as single pivot rather than multi-pivot weighting scheme\n- **Source:** [PROM on ACL Anthology](https://aclanthology.org/2025.naacl-short.19/)\n\n**D. Linguistically-Informed Multilingual Instruction Tuning - 2024**\n**Citation:** [Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?](https://arxiv.org/abs/2410.07809), Published in Transactions on Machine Learning Research (November 2025)\n- **Approach:** Uses typological feature vectors and k-means clustering to select diverse languages for instruction tuning\n- **Finding:** Careful selection based on linguistic diversity outperforms random language selection; addresses \"curse of multilinguality\"\n- **Relation to TWMP:** Also uses typological features for language selection in instruction tuning, but focuses on selecting a subset of languages rather than weighting multiple sources\n\n#### TANGENTIALLY RELATED RECENT WORK:\n\n**E. \"Assessing the Impact of Typological Features on Multilingual Machine Translation\"** (arXiv:2602.03551, 2026 EACL)\n- Analyzes how target language typology drives translation quality in NLLB-200 and Tower+ models\n- Releases fine-grained typological properties for 212 languages in FLORES+ benchmark\n- Shows that certain typological properties benefit from broader decoding strategies\n\n**F. \"Merge and Conquer: Instructing Multilingual Models by Adding Target Language Weights\"** (arXiv:2603.28263)\n- Merges instruction-tuned LLMs with language-specific base models for multilingual capability\n- Avoids continual pre-training and repeated fine-tuning\n- Lightweight alternative to traditional adaptation for low-resource languages\n\n**G. Cross-Lingual Expert Language Models (X-ELM)** (arXiv:2401.10440)\n- Uses typological structure to specialize expert models for distinct language clusters\n- Training along language family hierarchies provides performance benefits\n- Multi-source language training with typologically/embedding-based dissimilar triplets outperforms single-language baselines\n\n**H. DATAPROPHET (ICLR 2026)** (arXiv:2603.19688)\n- Determines dataset weighting in mixtures using DATAPROPHET scores\n- Integrates cross-modal similarity, multimodal perplexity, and dataset diversity\n- Training-free, interpretable metric for data weighting\n\n**I. Recent Work on Multi-Source Selection:**\n- KazMMLU (arXiv:2502.12829, ACL 2025): First MMLU-style benchmark for Kazakh (23,000 questions)\n- Budget-Xfer (as cited above) addresses multi-source optimization for African languages\n- PLUG (arXiv:2311.08711, ACL 2024): Leverages English pivot in cross-lingual instruction tuning\n\n---\n\n### 3. BENCHMARKS AND EVALUATION GAPS FOUND\n\n**KazMMLU:** Successfully identified and verified\n- First MMLU-style dataset specifically for Kazakh\n- 23,000 questions (10,969 Kazakh + 12,031 Russian)\n- Presented at ACL 2025; covers STEM, humanities, social sciences\n- **Source:** [KazMMLU on arXiv](https://arxiv.org/abs/2502.12829)\n\n**MiLiC-Eval:** Partially verified\n- Located on Papers with Code: [MiLiC-Eval: Benchmarking Multilingual LLMs for China's...](https://paperswithcode.com/paper/milic-eval-benchmarking-multilingual-llms-for)\n- Appears to be a benchmark for multilingual LLMs, but full details not retrieved\n\n---\n\n### 4. KEY FINDINGS ON NOVELTY\n\n**STRENGTHS OF TWMP'S NOVELTY CLAIM:**\n\n1. **Multi-Pivot Weighting Not Yet Fully Explored:** While TIPA weights adapter aggregation by typological similarity and PROM uses pivot languages, TWMP appears to be the **first systematic approach to combine BOTH concepts**: using multiple typologically-diverse pivot languages with learned or typologically-informed weighting for data selection in instruction tuning.\n\n2. **Data Selection vs. Module Aggregation:** TIPA aggregates existing trained adapters; TWMP appears to weight raw instruction-tuning data before training, which is a different problem.\n\n3. **Pivot Language Strategy Evolution:** PLUG and PROM focus on English as pivot; TWMP's multi-pivot approach with typological weighting is more sophisticated.\n\n**POTENTIAL OVERLAP/CONCERNS:**\n\n1. **TIPA's March 2026 publication (same venue cycle as TWMP):** TIPA demonstrates that typological similarity weighting for multilingual modules is effective. If TWMP's core novelty is similar weighting applied to data rather than adapters, the conceptual distance may be narrow.\n\n2. **Typological feature integration:** Multiple papers (X-ELM, Linguistically-Informed Instruction Tuning, URIEL+ enhancements) all demonstrate value of typological features for language selection/clustering in recent 2025-2026 work.\n\n3. **Data weighting literature:** DATAPROPHET and other data weighting approaches are relatively recent (ICLR 2026), suggesting this is an active research area.\n\n---\n\n### 5. CRITICAL ASSESSMENT\n\n**TWMP appears to have legitimate novelty IF:**\n- The combination of typological distance metrics (URIEL/URIEL+) with multi-source pivot language selection for instruction data weighting is novel\n- The specific weighting formulation or curriculum learning approach is non-obvious\n- Empirical results on Kazakh/Mongolian and other low-resource language benchmarks are strong\n\n**AREAS OF CONCERN:**\n1. TIPA (published March 2026 in EACL Findings) demonstrates the effectiveness of typological-similarity-based weighting for multilingual NLP at scale (230+ languages, 5 tasks)\n2. The conceptual gap between \"weight adapters by typology\" (TIPA) and \"weight data sources by typology\" (TWMP) may not be substantial enough to constitute strong novelty\n3. Pivot language selection with typological grounding is well-explored (PLUG, PROM, recent work on language families)\n\n**RECOMMENDATIONS FOR AUTHORS:**\n1. Clearly differentiate from TIPA's adapter aggregation approach—emphasize why data-level weighting is fundamentally different/better\n2. Demonstrate superiority over simpler baselines combining URIEL+ distances with standard multi-source selection\n3. Show that typological weighting outperforms embedding-based or other heuristic weighting (as Budget-Xfer found embedding similarity isn't always better)\n4. Provide extensive evaluation on truly low-resource languages (Kazakh, Mongolian, African languages) where the approach should shine\n\n---\n\n## SOURCES\n\n### Verified Cited Papers\n- [LangGPS on arXiv](https://arxiv.org/abs/2511.10229)\n- [Budget-Xfer on arXiv](https://arxiv.org/abs/2603.27651)\n\n### Major Competing/Related Work (2025-2026)\n- [TIPA: Typologically Informed Parameter Aggregation](https://arxiv.org/abs/2601.16629) - EACL 2026 Findings\n- [URIEL+ Script Expansion](https://arxiv.org/abs/2510.27183) - March 2026\n- [Modality Matching in URIEL+](https://arxiv.org/abs/2510.19217) - EACL 2026 Student Workshop\n- [PROM: Pivoted Optimization](https://aclanthology.org/2025.naacl-short.19/) - NAACL 2025\n- [Linguistically-Informed Instruction Tuning](https://arxiv.org/abs/2410.07809) - TMLR November 2025\n- [Assessing Typological Features in MT](https://arxiv.org/abs/2602.03551) - EACL 2026\n- [Merge and Conquer Multilingual Models](https://arxiv.org/abs/2603.28263)\n- [Cross-Lingual Expert Language Models](https://arxiv.org/abs/2401.10440)\n- [DATAPROPHET Data Weighting](https://arxiv.org/abs/2603.19688) - ICLR 2026\n- [KazMMLU Benchmark](https://arxiv.org/abs/2502.12829) - ACL 2025"
      }
    ],
    "totalDurationMs": 100304,
    "totalTokens": 38523,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 34389,
      "output_tokens": 3344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 783
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3344,
          "cache_read_input_tokens": 34389,
          "cache_creation_input_tokens": 783,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 783,
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
      "otherToolCount": 26
    }
  },
  "sourceToolAssistantUUID": "618f5799-c50a-4570-b0df-5a1f41e09f3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
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
  "leafUuid": "0634603a-d391-453e-9536-f851271912a0",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Review agent conducting independent verification on Round 7",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e"
}
```

---

### Assistant

_source line 20 · 2026-05-10T07:59:38.616Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive independent research results. Let me synthesize the findings:

## Key Findings from Research:

### 1. Papers VERIFIED as existing:
- CLO (arXiv:2505.14297, ACL 2025) ✓ - exists and is as described
- "Less is More" (arXiv:2509.20129, EMNLP 2025) ✓ - confirmed Spearman ρ=0.358 vs ρ=0.260
- LangGPS (arXiv:2511.10229, AAAI 2026) ✓ - exists as described


- Budget-Xfer (arXiv:2603.27651, SIGIR 2026) ✓ - exists as described

### 2. FACTUAL INACCURACIES FOUND:

I found a significant mischaracterization with KazMMLU - the paper claims "23K Kazakh-language questions" but the actual breakdown is 10,969 Kazakh and 12,031 Russian questions totaling 23,000. So only about 11K are actually in Kazakh, not the full 23K as implied.

There's also an issue with the ACL 2025 acceptance status. The paper was submitted in February 2025 and marked as under review, but the idea description repeatedly calls it an "ACL 2025 long paper" without confirmation. Given that we're now in May 2026, well past when ACL 2025 decisions would have been made, I need to verify whether this paper was actually accepted or if the status is outdated. have taken place by now in late July/August 2025, so these papers should be verifiable—MiLiC-Eval checks out at ACL Anthology, but KazMMLU's acceptance remains unclear. There's also a factual error in the description: it claims "23K Kazakh-language questions" when the dataset actually contains 10,969 Kazakh and 12,031 Russian questions, so it should specify the bilingual composition. I'm also noticing some newer papers that might be relevant, like TildeOpen LLM from March 2026, which uses curriculum-based training with weighted multilingual distributions across a 30B-parameter model.

There's also PROM from NAACL 2025, which takes a pivot-based approach using English as an optimization objective for multilingual instruction learning—this wasn't cited in the paper despite being published before the submission. Two more recent papers caught my attention: one from March 2026 on typological feature weighting for cross-lingual POS tagging, and another from April 2026 examining how Chinese models handle Uyghur and Mongolian.

I'm also noting "Merge and Conquer," which merges instruction-tuned LLMs with language-specific models. Looking at the most relevant competitors, TildeOpen LLM combines curriculum and weighted multilingual data at pretraining scale, but PROM seems particularly relevant since it explicitly disentangles English versus target-language data through separate training objectives—something the current paper should address in its related work.

There's a factual error I need to flag: the paper states KazMMLU contains "23K Kazakh-language questions," but the actual dataset has only about 11K Kazakh questions alongside 12K Russian ones totaling 23K. This mischaracterization is problematic since it underpins part of the motivation, and reviewers will catch it if they check the original dataset paper. I should also highlight that PROM from NAACL 2025 hasn't been flagged in any previous review rounds despite being directly relevant to the paper's approach.

Looking at the remaining uncited work, there are two more papers worth noting: one evaluating Uyghur and Mongolian language models, and another on multilingual training curricula. Despite these gaps, the paper has made substantial progress across seven rounds—the core methodology is solid, citations have been systematically addressed, and the technical details around DPO, compute, and evaluation are now accurate. The main lingering concern is that KazMMLU inaccuracy, which is moderate in severity, along with the PROM citation gap being minor. The paper should be more precise about KazMMLU's composition since roughly half the questions are in Russian rather than Kazakh. Looking at other related work, TildeOpen LLM seems less directly relevant as a pretraining effort for European languages, but PROM is worth comparing more carefully—it uses English as a single pivot with a disentangled training objective, whereas TWMP's approach of selecting multiple typologically-informed pivots with continuous distance weighting and staged curriculum represents a meaningful differentiation.

For the novelty assessment, the combination of URIEL+ typological distance weighting, multi-pivot selection, staged curriculum, and multi-source DPO forms a principled approach where individual components like typological weighting have appeared in prior work but this particular integration is novel.

On feasibility, the method is concrete and grounded in existing infrastructure—URIEL+, Aya, Qwen3.5-9B—with a realistic 4-6 month timeline for the manual mode using 120 H100 hours, putting it within reasonable computational bounds.

The paper demonstrates strong clarity with precise DPO formulations and concrete curriculum thresholds, though the KazMMLU description needs correction. For impact, the work addresses a genuine gap in agglutinative low-resource language support, which could influence how future instruction-tuning approaches handle morphologically complex languages.

But I'm realizing the KazMMLU factual error is more problematic than I initially weighted it. Claiming 23K Kazakh-language questions when only ~11K exist is a significant misstatement that undermines the core motivation—reviewers will definitely catch this. Beyond that, the paper is essentially submission-ready with just a few minor issues to address: the KazMMLU inaccuracy, the uncited PROM reference, and potentially a handful of other small details. Given the pattern of revisions across all previous rounds, I'm checking whether this round can finally clear the bar. Looking at the scores—novelty, feasibility, and clarity all at 4/5, but impact slightly lower at 3.5 to 4/5—the average lands around 3.875, which falls just short of the 4.0 threshold. Combined with the moderate issues still present, this points toward another revision cycle. I'm realizing the KazMMLU citation is genuinely inaccurate—the paper describes 23K Kazakh-language questions when the dataset actually contains around 11K Kazakh questions and 12K Russian ones, which matters for evaluating TWMP's Kazakh instruction tuning. Combined with the missing PROM citation, these are both concrete issues that warrant a "revise" verdict rather than a pass.

For scoring: the novelty is solid at 4/5 given the genuine combination of typological weighting with multi-pivot staging and multi-source DPO, feasibility is 4/5 with well-specified thresholds and realistic scope, but clarity drops to 3.5/5 because of that KazMMLU error in the motivation section.

Actually, reconsidering—the error is isolated to one claim within thousands of words of precise specification. The DPO formulation is exact, the curriculum staging is concrete, and the ablations are clearly defined. I think clarity should be 4/5 overall, with the factual mistake noted as a revision point rather than a fundamental clarity issue. Impact stays at 3.5/5 given the meaningful but somewhat narrow scope for Turkic and Mongolic languages, though the Swahili generalization helps. That puts the average at 3.875, still below the 4.0 threshold, so "revise" remains the right call. The scores feel right at 3.75 average—the paper is nearly there but needs that factual error about KazMMLU corrected. I should verify whether PROM is actually a gap in their related work or if it's already covered. Looking at PROM's approach of using English as a pivot language with separate training objectives, it's clearly distinct from PLUG's cross-lingual instruction generation, so it does seem like a relevant citation they're missing. The remaining issues are relatively minor—a factual error about KazMMLU, an uncited paper (PROM), and a potential addition about Chinese language models—so I'm settling on a revise verdict with a clear path forward. My scores reflect solid novelty and feasibility at 4/5 each, but clarity and impact are slightly lower at 3.5/5 due to the factual concern and the somewhat specialized scope, averaging to 3.75 overall.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0634603a-d391-453e-9536-f851271912a0",
  "isSidechain": false,
  "requestId": "req_011CatXrbidN5aTB7im8ug5s",
  "type": "assistant",
  "uuid": "0ff611c7-d171-43b9-8343-c95b5d58e2ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TUQFdHeWCEezYmQan5c3eE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1990,
      "cache_creation_input_tokens": 10597,
      "cache_read_input_tokens": 39262,
      "output_tokens": 6928,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1990,
          "output_tokens": 6928,
          "cache_read_input_tokens": 39262,
          "cache_creation_input_tokens": 10597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10597
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

_source line 21 · 2026-05-10T08:00:07.973Z_

Now I have sufficient research to complete my independent review. Let me synthesize the findings.

**Research Summary:**
- CLO (arXiv:2505.14297, ACL 2025): VERIFIED ✓
- "Less is More" (arXiv:2509.20129, EMNLP 2025): VERIFIED ✓ — Spearman ρ=0.358 vs ρ=0.260 confirmed
- LangGPS (arXiv:2511.10229, AAAI 2026): VERIFIED ✓
- Budget-Xfer (arXiv:2603.27651, SIGIR 2026): VERIFIED ✓
- MiLiC-Eval (arXiv:2503.01150, ACL 2025 Findings): VERIFIED ✓ — GPT-4o-mini achieves 20.7% on Mongolian vs 13.1% random
- Qwen3.5-9B — March 2026, 248K vocab, 201 languages, 0.8B/2B/4B/9B series: VERIFIED ✓
- **KazMMLU "23K Kazakh-language questions": FACTUALLY INCORRECT** — Dataset has 10,969 Kazakh + 12,031 Russian = 23,000 total; only ~11K questions are in Kazakh
- **PROM (NAACL 2025, "Pivoted and Regulated Optimization")**: Uncited; treats English as pivot with disentangled training objectives for multilingual instruction tuning — directly adjacent to PLUG/CLO landscape

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "The combination of URIEL+ continuous typological distance weighting + multi-pivot staged curriculum + multi-source DPO pair construction is novel as a unified recipe; TIPA and LangGPS use analogous weighting principles but in different modalities (adapter aggregation and model-internal signals respectively), and no prior work applies this combination to agglutinative low-resource instruction tuning."
    },
    "feasibility": {
      "score": 4,
      "rationale": "The method is precisely specified with concrete distance thresholds, prerequisite probe protocol, and fallback handling; manual mode (120 H100h) comfortably fits the ≤200 H100h budget and the 4–6 month timeline to ACL 2027 ARR is realistic."
    },
    "clarity": {
      "score": 3,
      "rationale": "The DPO formulation, curriculum percentile anchors, and fallback characterization are unusually precise for an idea draft, but the KazMMLU description contains a verifiable factual error — the dataset has 10,969 Kazakh + 12,031 Russian = 23,000 total questions, not '23K Kazakh-language questions' — which will be caught by any reviewer who reads the benchmark paper."
    },
    "impact": {
      "score": 4,
      "rationale": "The method targets instruction following for Kazakh (20M speakers), Mongolian (5M), and Uyghur (12M+) with a generalizable URIEL+-parameterized recipe applicable to any agglutinative target language; if results are positive, the contribution is meaningful and the Swahili held-out generalization target strengthens the claim beyond the Turkic cluster."
    }
  },
  "issues": [
    "MODERATE – KazMMLU benchmark description is factually wrong. The paper repeatedly claims KazMMLU contains '23K Kazakh-language questions spanning STEM, humanities, and social sciences,' but independent verification of arXiv:2502.12829 shows the dataset contains 10,969 Kazakh-language questions + 12,031 Russian-language questions = 23,000 total. Only ~47% of questions are in Kazakh; the remainder are in Russian. Any EMNLP reviewer who reads the KazMMLU abstract will catch this. The description should read '23K questions (approximately 11K in Kazakh, 12K in Russian) sourced from Kazakhstani educational materials.' For TWMP's Kazakh instruction evaluation, only the Kazakh-language subset is relevant, which is smaller than the paper implies.",
    "MINOR – PROM (NAACL 2025, arXiv not yet located but published at ACL Anthology at aclanthology.org/2025.naacl-short.19/) introduces 'Pivoted and Regulated Optimization,' which treats English as an internal pivot and disentangles English vs. target-language training objectives via separate regularized losses for multilingual instruction tuning. This is adjacent to PLUG and CLO in the landscape of English-pivot methods for multilingual instruction following, and EMNLP reviewers familiar with the NAACL 2025 proceedings will expect it to be cited alongside PLUG and CLO. One sentence suffices: 'PROM [NAACL 2025] disentangles English-pivot and target-language training objectives via regulated losses — like PLUG and CLO, it fixes English as the sole pivot without addressing typologically distant agglutinative targets.'",
    "MINOR – 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026) evaluates Uyghur and Mongolian capabilities across current LLMs, finding Llama3-Instruct is uniquely capable at Uyghur and top-performing at Mongolian among open models. This is contemporary evidence for the performance gap that motivates TWMP and is published close enough to the ARR deadline to be a missing citation reviewers will notice. One sentence in Section 1 or 2 would suffice."
  ],
  "feedback": "All Round 6 issues are fully resolved: Foroutan et al., LangGPS, Code-Switching Curriculum, Laiyk et al., URIEL+ expansion, Budget-Xfer, and the fallback characterization now all appear correctly in the landscape and key_references. The paper is close to submission-ready. Three targeted fixes remain:\n\n(1) Fix the KazMMLU description (highest priority — factual error). Change every instance of '23K Kazakh-language questions' to '23K questions spanning Kazakh and Russian (approximately 11K in Kazakh)' or similar accurate phrasing. This appears in the core_problem, opportunity, and key_references fields. This is a one-line fix per occurrence but it is mandatory — the current phrasing is verifiably wrong and will undermine reviewer trust in the paper's factual accuracy.\n\n(2) Add PROM [NAACL 2025] to the landscape (one sentence): 'PROM [NAACL 2025] treats English as an internal pivot and separates English vs. target-language training objectives via regulated losses; like PLUG and CLO, it presupposes a single English pivot without addressing typological distance or multi-pivot sequencing for agglutinative targets.'\n\n(3) Add arXiv:2504.00289 (April 2026) to the opportunity section or related work as supplementary evidence for Uyghur/Mongolian gaps in current LLMs.\n\nNone of these require new experiments. Issues (2) and (3) are one-sentence writing additions; issue (1) is a find-and-replace correction. ACL 2027 (ARR August 3, 2026) remains the appropriate primary target; EMNLP 2026 (May 25 ARR) is feasible only if the team already has the QLoRA infrastructure in place and can begin experiments immediately after these three fixes.",
  "reason": "All Round 6 issues resolved; one moderate factual error (KazMMLU 23K total ≠ 23K Kazakh-only) and two minor citation gaps (PROM NAACL 2025, arXiv:2504.00289) block pass; all three are writing-only fixes requiring no new experiments."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ff611c7-d171-43b9-8343-c95b5d58e2ba",
  "isSidechain": false,
  "requestId": "req_011CatXrbidN5aTB7im8ug5s",
  "type": "assistant",
  "uuid": "a4a3765f-d44d-4a0f-85f3-4ec548915fa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TUQFdHeWCEezYmQan5c3eE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1990,
      "cache_creation_input_tokens": 10597,
      "cache_read_input_tokens": 39262,
      "output_tokens": 6928,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1990,
          "output_tokens": 6928,
          "cache_read_input_tokens": 39262,
          "cache_creation_input_tokens": 10597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10597
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a4a3765f-d44d-4a0f-85f3-4ec548915fa6",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Review agent conducting independent verification on Round 7",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a4a3765f-d44d-4a0f-85f3-4ec548915fa6",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Review agent conducting independent verification on Round 7",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e"
}
```

---
