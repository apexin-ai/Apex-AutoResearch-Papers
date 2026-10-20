# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a.jsonl`
- **Structured JSON:** [`e7f85b7bc52824526333.json`](../../sessions/e7/e7f85b7bc52824526333.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:41:58.346Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:41:58.346Z",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Multilingualism and Cross-Lingual NLP.\n\nDirection: Cross-lingual transfer and multilingual NLP methods. In-scope: cross-lingual transfer without parallel data, multilingual instruction tuning strategies, language-agnostic representations, low-resource language adaptation, cross-lingual retrieval, multilingual reasoning, code-switching handling. ACL 2025 outstanding papers highlighted multilingual gaps and cross-lingual intervention methods.\n\nContribution type: METHOD ONLY. New training recipes, transfer algorithms, or adaptation techniques. Not a new multilingual dataset or language-specific analysis.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Multilingual experiments need coverage across languages — budget for LoRA fine-tuning on multilingual models, not full pretraining.\n2. Time: ≤16 days. Use existing multilingual models (BLOOM, mT5, XLM-R, Aya, Qwen multilingual, Llama-3 multilingual).\n3. Eval: XTREME-UP, XCOPA, XStoryCloze, MGSM, multilingual MMLU, TyDi QA, FLORES for MT.\n\nLook for: efficient cross-lingual transfer with minimal target-language data, multilingual reasoning without English-centric bias, representation alignment methods, adaptation techniques for typologically diverse languages. Avoid: English-only experiments, monolingual fine-tuning.\n\nTag: direction=multilingual, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 6/10)\n{\n  \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning\",\n  \"core_problem\": \"Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.\",\n  \"opportunity\": \"Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K Kazakh-language questions spanning STEM, humanities, and social sciences sourced from authentic educational materials; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.\",\n  \"landscape\": \"PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.\",\n  \"approach\": \"We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\\n\\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\\n\\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 on typological alignment tasks versus ρ=0.260 for the full 800-feature set while also improving downstream cross-lingual NLP performance, we apply this feature selection before computing cosine distances. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\\n\\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\\n\\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\\n\\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter are discarded. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\\n\\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh, MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG and CLO serve as primary baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO baselines, URIEL+ sub-space ablations, curriculum schedule variants, DPO quality gate ablation row, and DPO prerequisite probe runs)\",\n      \"gpu_utilization\": \"LOW (~25–35%): GPU sits idle during code writing, debugging, data pipeline work, result analysis, and paper writing; runs are launched manually and often queue overnight\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$300 (200h × $1.50/h on Lambda Labs A100)\",\n      \"h100_equivalent\": \"~120h H100 (within ≤200 H100-hour budget constraint at typical A100/H100 performance ratio of ~0.6×)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~310h A100 (agent explores broader hyperparameter space with human approval gates; ~55% more runs than manual)\",\n      \"gpu_utilization\": \"MODERATE (~55–65%): agent queues follow-up experiments immediately after each run completes, filling GPU idle between human check-ins\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in to approve experiment configs and review intermediate results\",\n      \"claude_api_cost\": \"~$150–250 (~1,500–2,500 conversation turns coordinating experiment scheduling, result parsing, and ablation planning)\",\n      \"estimated_gpu_cost\": \"~$465 (310h × $1.50/h)\",\n      \"h100_equivalent\": \"~186h H100 (within ≤200 H100-hour budget constraint at ~0.6× A100/H100 ratio, leaving ~14h headroom)\",\n      \"risk_note\": \"Choice of URIEL+ feature subspace (full 800-feature vs. Laplacian 300-feature vs. syntax-only) and the DPO prerequisite probe threshold require human judgment at key decision points; an automated agent may converge on a locally optimal weighting scheme that under-performs on the held-out Swahili generalization target\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~600h A100 (3–5× more experiments: grid search over distance metrics, curriculum schedule shapes, LoRA rank/alpha, 5+ target languages including Swahili and Kyrgyz for generalization, plus replication runs)\",\n      \"gpu_utilization\": \"NEAR-ZERO idle—agent schedules jobs back-to-back across all target languages in parallel, launches follow-up ablations immediately on job completion, and runs nightly sweeps without human bottleneck\",\n      \"timeline\": \"5–10 days with 4× concurrent A100s; ~3 weeks on a single A100\",\n      \"team\": \"0 (initial setup of experiment configs, data paths, and evaluation harness only)\",\n      \"claude_api_cost\": \"~$400–650 (~4,000–6,500 turns for full experiment orchestration, result parsing, ablation tree exploration, and report drafting)\",\n      \"estimated_gpu_cost\": \"~$900 (600h × $1.50/h)\",\n      \"h100_equivalent\": \"~360h H100 — EXCEEDS the ≤200 H100-hour hard budget constraint. Auto_research mode is documented for completeness but is NOT a viable deployment option within the stated budget. Use manual mode (~120 H100h) or human_in_loop mode (~186 H100h) to remain within budget.\",\n      \"speed_bottleneck\": \"GPU count is the primary bottleneck: 4 concurrent A100s reduces wall-clock time to ~5 days; API rate limits become secondary when running >8 parallel experiment threads\",\n      \"risk_note\": \"CONSTRAINT VIOLATION: 600 A100h ≈ 360 H100h, exceeding the ≤200 H100-hour hard budget. Additionally, unconstrained exploration may overfit the URIEL+ weighting function to the 3 initial target languages; Swahili as a held-out agglutinative target is required to detect this overfitting early.\"\n    }\n  },\n  \"target_venues\": [\n    \"ACL 2027 (ARR submission deadline August 3, 2026) — primary target; provides adequate time for validation on additional typological clusters beyond Turkic–Mongolic, and for a paper of this scope (multi-pivot curriculum + ablations + 3 evaluation benchmarks) that cannot realistically reach conference quality in under 6 weeks\",\n    \"EMNLP 2026 (ACL Rolling Review, rolling deadlines throughout 2026) — viable only if the team has prior QLoRA fine-tuning infrastructure already in place and can begin experiments immediately\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (ACL 2024) [29% improvement on Chinese/Korean/Italian/Spanish; Turkic/Mongolic gap is untested]\",\n    \"Cross-Lingual Optimization for Language Transfer in Large Language Models (CLO; ACL 2025, arXiv:2505.14297) [DPO-style cross-lingual preference optimization using English-only source and M2M100 translation; baseline and methodological reference for TWMP's multi-source DPO extension]\",\n    \"Llama-3.1-Sherkala-8B-Chat (arXiv:2503.01493) [trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish; demonstrates Turkish as auxiliary language improves Kazakh performance via full fine-tuning; differentiated from TWMP's generalizable LoRA recipe parameterized by continuous URIEL+ distances]\",\n    \"Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) [implicit reward transfer from English-aligned DPO model to annotate cross-lingual preference pairs; 12.72% Win Rate improvement on X-AlpacaEval; English-only source with no typological weighting—differentiated from TWMP's multi-pivot source selection and low-resource agglutinative targets]\",\n    \"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP; official repository: github.com/LeeLanguageLab/URIELPlus]\",\n    \"Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset (ρ=0.358) outperforms full 800-feature URIEL+ (ρ=0.260) for typological alignment and downstream cross-lingual NLP; justifies TWMP's feature selection step]\",\n    \"Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]\",\n    \"TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]\",\n    \"Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]\",\n    \"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark, 23K questions, peer-reviewed]\",\n    \"MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]\",\n    \"TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]\",\n    \"Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]\",\n    \"Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)\",\n    \"Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)\",\n    \"Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]\",\n    \"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]\"\n  ],\n  \"description\": \"This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358 vs. ρ=0.260 for the full 800-feature set) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU, MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.\",\n  \"project_name\": \"typological_multi_pivot\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL – TIPA (arXiv:2601.16629, EACL 2026 Findings) is directly competing work the generator missed: it constructs proxy language adapters by aggregating existing ones weighted by typological similarity across 230+ languages and five tasks. The novelty claim 'no prior work combines multi-pivot selection with typological distance weighting' is therefore too strong; the revision must differentiate TWMP from TIPA clearly (TIPA is training-free adapter aggregation for encoders; TWMP is a weighted sampling + curriculum training approach for decoder LLMs in instruction tuning—this distinction exists but must be made explicit).\", \"CRITICAL – Evaluation benchmarks are misspecified: XQuAD and XCOPA do NOT include Kazakh, Mongolian, or Uyghur—multiple sources and the benchmarks' own documentation confirm this. The evaluation protocol must be redesigned to use benchmarks that actually cover the target languages (e.g., XTREME-UP, MiLiC-Eval for Chinese minority languages, or TyDi QA for Kazakh).\", \"SIGNIFICANT – Model name 'Qwen 3.5-7B' does not exist. The Qwen3.5 series released in 2026 includes 4B and 9B variants (among others) but no 7B. The 250K vocabulary claim is correct for Qwen3.5 but the model identifier must be corrected to Qwen3.5-9B or Qwen3.5-4B before submission.\", \"SIGNIFICANT – 16-day timeline is unrealistic for a conference-quality submission. Running 15–20 QLoRA experiments across 3 target languages, implementing the TWMP curriculum + CLO loss from scratch, and writing a complete paper cannot be done in 16 days by 1–2 researchers without preexisting infrastructure. The compute estimate (180h A100 ≈ 125–135h H100) is within the 200 H100-hour hard constraint, but wall-clock time is the binding bottleneck.\", \"SIGNIFICANT – The primary evidence for the research gap, 'Left Behind' (arXiv:2603.21036), is a March 2026 preprint from a single author at North American University evaluated with 50 hand-crafted questions. EMNLP reviewers will reject this as insufficient basis for a gap claim; the motivation must be grounded in larger, peer-reviewed evaluations (e.g., the 'Shared Weights Pretraining for Extremely Low-Resource Languages' ACL 2025 paper, or XTREME-UP results for Turkic languages).\", \"MODERATE – Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) is not properly discussed in the landscape. This paper directly uses typological feature vectors for language selection in multilingual instruction tuning—the generator characterizes only arXiv:2505.13908 (which is purely analytical) while ignoring this more methodologically relevant prior work.\", \"MODERATE – MLM is a NeurIPS 2025 ER Workshop paper, not a NeurIPS 2025 main conference paper. Misrepresenting workshop papers as conference papers in a related work section is a frequent reviewer complaint and can trigger a bias/credibility flag.\", \"MODERATE – The CLO-style loss is described as a 'cross-lingual contrastive loss that enforces target-language response fidelity.' CLO actually uses DPO-style preference optimization (not a contrastive loss) to suppress off-language responses. The paper must use technically accurate descriptions to avoid confusion and reviewer pushback.\", \"MINOR – PLUG (ACL 2024)'s 29% improvement was measured on Chinese, Korean, Italian, and Spanish—not on Kazakh/Mongolian/Uyghur. The assumption that PLUG performs poorly on Turkic languages is plausible but not directly evidenced in the PLUG paper itself; the gap claim relative to PLUG needs its own experimental demonstration.\"]\nFeedback: The core idea is genuinely interesting—typological-distance-weighted multi-pivot instruction tuning for Turkic low-resource languages—but the current draft has three blockers that prevent submission at EMNLP 2026 quality: (1) TIPA (EACL 2026) must be cited and clearly differentiated: TIPA does typological weighting of adapters in a training-free, encoder-adapter (MAD-X) framework across 230+ languages; TWMP is a training-time data sampling + curriculum approach for decoder LLMs in instruction tuning—spell this out explicitly in Section 2. (2) Replace XQuAD + XCOPA with benchmarks that actually include Kazakh, Mongolian, and Uyghur: consider XTREME-UP (includes Kazakh), MiLiC-Eval (Uyghur, Kazakh, Mongolian), and TyDi QA for real-language evaluation. If none of the standard benchmarks are adequate, you need to explain what evaluation data you are using and where it comes from. (3) Correct the model name to Qwen3.5-9B (or 4B) and rerun your compute estimates accordingly. Beyond the blockers: the motivation should be regrounded away from 'Left Behind' as the sole anchor—add references to XTREME-UP or ACL 2025 shared-weights pretraining results for Turkic languages. Add arXiv:2410.07809 to related work with a clear explanation of why TWMP's weighted sampling and curriculum are distinct contributions. Fix the MLM venue to 'NeurIPS 2025 ER Workshop' and fix the CLO description to 'DPO-style cross-lingual preference optimization.' On timeline: unless the team has the training infrastructure already built, the 16-day window makes a May 25 ARR deadline extremely risky; the ACL 2027 ARR deadline (August 3, 2026) is a more defensible target that allows proper validation on additional typological clusters (e.g., a Bantu agglutinative language) to test generalization beyond Turkic.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"SIGNIFICANT – CLO's DPO objective is designed for English-source preference pairs: chosen = target-language response to English instruction, rejected = off-language (English) response to target-language instruction. TWMP proposes extending this to non-English source languages (Turkish/Uzbek → Kazakh), but the paper does not specify how preference pairs are constructed when the source is itself a non-English language like Uzbek. If the model produces a Kazakh response to a Uzbek instruction, what is the 'rejected' response? Reviewers will reject this as technically incomplete without a precise DPO formulation for the multi-source case.\", \"SIGNIFICANT – URIEL legacy features are known to be sparse for exactly the target languages in this paper. URIEL+ (arXiv:2409.18472, COLING 2025) explicitly improves coverage for low-resource languages and should be used instead of the 289-dim lang2vec legacy features. Furthermore, 'Less is More: The Effectiveness of Compact Typological Language Representations' (EMNLP 2025) shows that compact URIEL+ features outperform the full 289-dim feature space for cross-lingual NLP tasks—directly contradicting TWMP's use of all 289 dimensions without selection. This is a directly relevant citation the paper must engage with.\", \"MODERATE – Auto_research mode (600h A100 ≈ 300h H100) exceeds the stated ≤200 H100-hour hard constraint. While the experiment plan uses manual mode (within constraint), the resource estimate table presents auto_research as a legitimate deployment mode without flagging this violation of the user's stated budget constraint.\", \"MODERATE – The staged curriculum's cosine-distance threshold schedule is described qualitatively ('progressively expands the radius at scheduled epochs') but no concrete schedule is specified. Reviewers will ask: how many stages? What distance thresholds? How are thresholds set relative to the URIEL distance distribution of the Aya collection? Without a concrete, reproducible specification, this is a design element that cannot be ablated or replicated.\", \"MODERATE – DCO (arXiv:2603.04678, March 2026, Tianyu Liu et al.) introduces Direct Consistency Optimization, a DPO-inspired method for cross-lingual knowledge consistency across 26 languages and 9 LLMs. This is a concurrent work that uses a DPO-style objective for cross-lingual alignment—similar in spirit to the CLO component of TWMP—and must be cited and differentiated in the related work section.\", \"MINOR – The Aya dataset's coverage of Turkic pivot languages (Turkish, Uzbek, Kyrgyz) is assumed but not verified. If Uzbek and Kyrgyz have only hundreds of Aya instances, the typological-distance-weighted sampling will produce noisy estimates for the closest pivots to Kazakh. The paper should state the number of available training instances per pivot language in Aya and set a minimum threshold below which a language is excluded from the mixture.\"]\nFeedback: The generator has addressed all Round 1 critical issues competently: TIPA is correctly differentiated, benchmarks are fixed, Qwen3.5-9B is confirmed correct, arXiv:2410.07809 is properly placed in the landscape, and the CLO/DPO description is accurate. The remaining blockers are two: (1) The DPO objective must be precisely formulated for non-English source languages. The current description 'increases preference for target-language responses and reduces preference for off-language outputs, without requiring any target-language training labels' is borrowed verbatim from CLO's English-source setting. For a Turkish → Kazakh pair, you must specify: what constitutes the chosen response, what constitutes the rejected response, and how you obtain these without any Kazakh labels. One viable extension: treat (Turkish-instruction, Kazakh-response) as the chosen pair and (Turkish-instruction, Turkish-response) as rejected—but this requires stating it explicitly and verifying that Qwen3.5-9B produces detectable off-language Turkish responses to Turkish instructions. (2) Replace lang2vec 289-dim URIEL features with URIEL+ (arXiv:2409.18472, COLING 2025), which has better sparse-language coverage, and cite 'Less is More' (EMNLP 2025) to justify whichever feature subspace you choose. This is not just a citation gap—if the typological distances for Uzbek and Kyrgyz are inaccurate in legacy URIEL due to sparsity, the entire weighting scheme degrades for the most important (closest) pivots to Kazakh. Beyond the blockers: add DCO (arXiv:2603.04678) to related work; specify the curriculum schedule concretely (number of stages, distance thresholds); verify and report the number of Aya instances per Turkic pivot language; and note that auto_research mode exceeds the 200 H100-hour constraint if that constraint applies. ACL 2027 (August 3, 2026 ARR) remains the appropriate primary venue.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MODERATE – Sherkala-Chat (arXiv:2503.01493, March 2025) is a directly relevant uncited work: it instruction-tunes Llama-3.1-8B for Kazakh on 45.3B tokens of Kazakh, English, Russian, and Turkish data, demonstrating that Turkish as an auxiliary training language improves Kazakh performance—the empirical core insight that motivates TWMP's pivot selection. Not citing it leaves a gap reviewers will notice; TWMP should add it as related work and contrast it: Sherkala-Chat uses ad-hoc four-language mixing with full fine-tuning, whereas TWMP provides a principled, generalizable, LoRA-based method parameterized by continuous URIEL+ distances applicable across any agglutinative target.\", \"MODERATE – The DPO preference pair construction specifies 'highest-scoring chosen' and 'lowest-scoring rejected,' where 'scoring' is implicitly language identification confidence from fastText. This means a grammatically garbled Kazakh response with high fastText confidence could be chosen as the preferred response over a coherent Turkish response. No quality filter (perplexity, length heuristic, or instruction-following score) is applied to the chosen pool. Reviewers will ask whether the DPO training signal is noisy precisely for the close-pivot cases where K=8 Kazakh responses are plentiful—yet quality varies most—and for distant pairs where only 1 of 8 samples passes the language filter, leaving little variance to select from. The paper should either add a quality filter (e.g., exclude responses shorter than 20 tokens or with perplexity above a threshold under the base model) or explicitly acknowledge and ablate this as a limitation.\", \"MINOR – Qwen3.5-9B release date: the paper states 'released February 2026' but available information indicates the Qwen3.5 small series (0.8B/2B/4B/9B) became available March 2, 2026—the February date applies to the larger Qwen3.5 medium models (35B-A3B, 27B). This should be corrected to March 2026.\", \"MINOR – The URIEL+ repository URL cited in the approach section ('github.com/Masonshipton25/URIELPlus') does not match the official ACL Anthology-linked repository ('github.com/LeeLanguageLab/URIELPlus'). The URL should match the official publication's repository or the PyPI package ('urielplus') should be referenced instead.\", \"MINOR – The Kyrgyz Aya instance count ('~4.1M instances in the Aya collection language split') could not be independently verified against HuggingFace statistics. Given Kyrgyz is much lower-resource than Turkish, this count depends entirely on machine-translated data volume and should be verified and cited to the HuggingFace dataset page or the Aya Collection paper's per-language appendix before submission.\"]\nFeedback: The generator has addressed all Round 2 issues competently: the multi-source DPO formulation is now precisely specified (chosen = source-language instruction + model-generated target-language response; rejected = source-language instruction + model-generated source-language response), URIEL+ replaces legacy 289-dim features with the 'Less is More' 300-feature Laplacian subset, the staged curriculum has concrete D_25/D_60 percentile anchors and epoch ranges, DCO is cited and differentiated, Aya coverage is verified with a 5,000-instance floor, and auto_research mode is correctly flagged as exceeding the 200 H100h budget. Two moderate issues remain before this is submission-ready: (1) Add Sherkala-Chat (arXiv:2503.01493) to related work—it is a directly adjacent March 2025 paper training Llama-3.1 on Kazakh+Turkish+Russian and provides empirical motivation for TWMP's pivot selection logic. The contrast is easy: Sherkala-Chat is language-specific full fine-tuning with ad-hoc pivot choice; TWMP is generalizable LoRA-based training with principled URIEL+ weighting. (2) Address the DPO pair quality concern: define 'highest-scoring' explicitly as language ID confidence, acknowledge that this does not filter for response quality, and either add a minimal quality gate (e.g., minimum response length or base-model perplexity cap) or include it as a stated limitation with an ablation that shows the fastText-only selection is adequate in practice. Fix the three minor issues (Qwen3.5 release date, URIEL+ repo URL, Kyrgyz instance count verification) before submitting. ACL 2027 (August 3, 2026 ARR) remains the appropriate primary target; given these are all fixable within days, the paper is on track.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MODERATE – Sherkala-Chat (arXiv:2503.01493) was flagged in Round 3 as a key uncited adjacent work and remains absent from Round 4. This paper trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish, directly demonstrating that Turkish as an auxiliary language improves Kazakh performance — the empirical core claim motivating TWMP's pivot selection logic. EMNLP reviewers familiar with Kazakh NLP will notice this omission immediately. Required: add to related work section with explicit contrast (Sherkala-Chat uses ad-hoc 4-language full fine-tuning for Kazakh specifically; TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target).\", \"MODERATE – DPO pair quality gate still absent. The approach specifies 'pair the highest-scoring chosen with the lowest-scoring rejected' based on fastText language ID confidence alone, with no quality filter. For close-pivot pairs (Turkish→Kazakh), K=8 sampling may yield 5–7 Kazakh responses, creating a large chosen pool with highly variable quality; the 'highest-scoring' fastText criterion selects the response with the highest Kazakh language ID confidence, which is not correlated with response coherence or instruction-following quality. A grammatically garbled but confidently Kazakh response will be preferred over a fluent but lower-confidence response. This was raised in Round 3 and remains unaddressed. Fix: add a minimum response length gate (e.g., ≥20 tokens) or base-model perplexity cap, or include an explicit ablation comparing fastText-only selection vs. a quality-gated variant and acknowledge this as a limitation with empirical validation.\", \"MODERATE – Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings) is uncited and directly relevant to TWMP's DPO component. This paper uses implicit reward transfer from English DPO models to annotate cross-lingual preference pairs for multilingual DPO fine-tuning, achieving 12.72% average Win Rate improvement on X-AlpacaEval across training languages. While the approach differs from TWMP (English-only source, implicit reward annotation, no typological weighting), it represents active concurrent work on cross-lingual DPO alignment that EMNLP reviewers will expect to see cited and contrasted. Required addition to related work: differentiate TWMP's direct construction of multi-source preference pairs via language ID vs. this paper's implicit reward annotation from a single English-aligned model.\", \"MINOR – Qwen3.5-9B release date error persists for the third consecutive round. The submission states 'released February 2026' but independent verification (multiple sources) confirms the Qwen3.5 small series (0.8B/2B/4B/9B) was released March 1–2, 2026, with February 2026 referring to the larger Qwen3.5 medium models (35B-A3B, 27B). Change 'released February 2026' to 'released March 2026'.\", \"MINOR – URIEL+ repository URL persists as incorrect for the third consecutive round. The submission cites 'github.com/Masonshipton25/URIELPlus' but the official ACL Anthology-linked repository is 'github.com/LeeLanguageLab/URIELPlus' (confirmed). Change to the correct URL or cite the PyPI package 'urielplus' instead.\"]\nFeedback: This is Round 4 and the same four issues (Sherkala-Chat, DPO quality gate, release date, repo URL) that were flagged in Round 3 have not been addressed. The pattern is concerning for an ARR deadline in 15 days. Here is exactly what needs to change, in priority order:\n\n(1) Add Sherkala-Chat to Section 2 related work. One paragraph is sufficient: 'Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish, demonstrating that Turkish as an auxiliary language improves Kazakh performance—motivating our choice of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc pivot selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language.'\n\n(2) Add Implicit Cross-Lingual Rewarding (arXiv:2503.04647, ACL 2025 Findings) to Section 2. One sentence: 'Implicit Cross-Lingual Rewarding annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving strong multilingual alignment from English-only source data—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from this work.'\n\n(3) Fix the DPO quality issue. Choose one of: (a) add a minimum 20-token length gate to the chosen pool and state it explicitly; (b) add a perplexity cap at 2× base-model perplexity on the instruction; or (c) keep the current fastText-only selection but add a clearly labeled limitation paragraph and one ablation row in Table X comparing fastText-only vs. length-gated selection. Option (c) requires the least implementation effort and is acceptable.\n\n(4) Fix two one-line errors: 'released February 2026' → 'released March 2026'; 'github.com/Masonshipton25/URIELPlus' → 'github.com/LeeLanguageLab/URIELPlus'.\n\nNone of these require new experiments. Issues (1), (2), (4) are writing-only changes. Issue (3) option (c) requires one additional experiment row or a paragraph addition. The paper is substantively sound and the core novelty claim is defensible—these are editorial and citation completeness fixes that are blocking an otherwise strong submission. ACL 2027 (August 3, 2026 ARR) remains the more realistic target, but if the team has existing QLoRA infrastructure, EMNLP 2026 (May 25 ARR) is feasible after these four fixes.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE – Revisiting Multilingual Data Mixtures (arXiv:2510.25947, Foroutan et al., EPFL, Oct 2025) directly challenges TWMP's two core premises: (1) staged curriculum learning 'does not reduce negative interference' in multilingual training, and (2) temperature-based language reweighting 'hurts performance due to noise' on low-resource data. This paper focuses on pretraining, not instruction tuning, but EMNLP reviewers familiar with it will raise it against TWMP's staged curriculum and inverse-distance weighting scheme. Required: cite this paper in Section 2, acknowledge the potential discrepancy, and argue explicitly why the instruction tuning setting (smaller data footprint, fewer gradient steps, different optimization landscape) is different enough that the Foroutan et al. findings do not transfer.\", \"MODERATE – LangGPS (arXiv:2511.10229, AAAI 2026; Yangfan Ye, Xiaocheng Feng et al., HIT + Microsoft) proposes language separability from the model's own representation space as the basis for multilingual instruction tuning data selection, and reports improvements over external-feature-based approaches across 22 languages including low-resource targets. It is a peer-reviewed AAAI 2026 competitor to TWMP's URIEL+-based selection approach. This is too similar to leave uncited. Required: add to related work and differentiate: LangGPS uses task-adaptive model-internal signals but is agnostic to typological structure and provides no mechanism for multi-pivot curriculum sequencing; TWMP uses external typological features to derive a principled ordering over pivot languages independent of training dynamics.\", \"MODERATE – Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (arXiv:2411.02460, ACL 2025 Findings; Haneul Yoo et al., NAVER AI) proposes a 3-stage curriculum (token-level code-switching → sentence-level code-switching → monolingual) that achieves cross-lingual transfer improvements on both high- and low-resource languages without typological distance. This paper has been available since November 2024—before all prior review rounds—and has never appeared in TWMP's references. EMNLP reviewers will notice its absence. Required: cite and contrast in Section 2: the code-switching curriculum operates within a single language pair using surface-level code-mixing as a bridge, whereas TWMP's curriculum operates over a pool of typologically ordered pivot languages with no code-switching; the two approaches address different facets of cross-lingual curriculum design and could in principle be combined.\", \"MINOR – Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (arXiv:2502.13647, ACL 2025 Main; Laiyk et al.) fine-tunes Qwen/Falcon/Gemma on 10,600 GPT-4o-assisted Kazakh instruction examples, achieving consistent improvement on multiple-choice and generative Kazakh tasks. This is a direct Kazakh instruction tuning baseline from ACL 2025 that any reviewer working on KazMMLU will expect TWMP to compare against or at minimum cite. It documents that targeted single-language instruction data generation is a strong alternative to cross-lingual transfer methods—TWMP should position itself relative to it (e.g., TWMP does not require any target-language instruction labels and is applicable to Mongolian and Uyghur where no comparable GPT-4-assisted dataset exists).\", \"MINOR – Simple Additions, Substantial Gains: Expanding URIEL+ (arXiv:2510.27183, LREC 2026; Shipton, Ng, Khan et al.) extends the URIEL+ database with script vectors, Glottolog integration, and genealogical feature propagation, reducing feature sparsity by 35% and expanding coverage to 26,449 languages—directly addressing the sparsity problem for Kazakh/Uzbek/Kyrgyz that TWMP cites as motivation for switching from legacy lang2vec to URIEL+. TWMP should either use this updated version or acknowledge it as a contemporaneous development and argue that the 2409.18472 COLING 2025 version is sufficient for the target languages (the 35% sparsity reduction would most benefit exactly the low-resource Turkic languages in scope).\", \"MINOR – The DPO prerequisite probe threshold is set at >5% of K=8, which equals at least 1 target-language response in 8 tries. This is the minimum viable signal level and means many source-target pairs that 'pass' the probe provide almost no diversity in the chosen pool (only 1 candidate). At this threshold, the 20-token gate can cause 100% discard of chosen candidates for those instructions (if the single Kazakh response is <20 tokens), silently collapsing to SFT-only training for many instruction prompts without reporting. The paper should characterize the empirical distribution of per-instruction chosen-pool sizes (1, 2, 3+ responses) across source-target pairs and report what fraction of instructions fall back to SFT-only due to post-gate chosen pool exhaustion.\"]\nFeedback: All Round 4 issues are addressed: Sherkala-Chat is properly cited and contrasted, the DPO 20-token length gate and ablation row are specified, Implicit Cross-Lingual Rewarding is cited, the release date and URIEL+ URL are corrected. The paper's core method is substantively sound and the technical specification is unusually precise for a draft at this stage. Three writing-only additions are needed before this is EMNLP-ready:\n\n(1) Add Foroutan et al. (arXiv:2510.25947) to Section 2. Key contrast: that paper tests pretraining-scale reweighting across 25–400 languages; TWMP operates at instruction tuning scale (10 epochs, LoRA, ≤6,400 instances per pivot) where reweighting over a narrow near-family pivot pool is qualitatively different from resampling across 400 pretraining languages. Make this argument explicitly to preempt the obvious reviewer objection.\n\n(2) Add LangGPS (arXiv:2511.10229, AAAI 2026) and Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings) to Section 2. Both are one-paragraph additions: LangGPS uses model-internal representation signals (no external typological database, no multi-pivot ordering); Code-Switching Curriculum uses surface-level code-mixing within a pair (no typologically structured pool, no DPO). Neither addresses the multi-pivot ordering problem or provides a principled recipe for pivot sequencing across typologically diverse targets.\n\n(3) Add arXiv:2502.13647 (ACL 2025 Main, Kazakh instruction tuning) as a related baseline in Section 2 and note it cannot generalize to Mongolian and Uyghur where no comparable target-language instruction dataset exists.\n\nFor the probe threshold: add one sentence clarifying what happens when the post-gate chosen pool for a given instruction is empty—confirm that those instructions fall back to the SFT-weighted objective, not to silent skip, and report the per-pair fallback rate as a characterization result.\n\nACL 2027 (ARR August 3, 2026) remains the appropriate primary target. None of these additions require new experiments.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:41:58.353Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:41:58.353Z",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

## Round 1

67 recorded events

### User

_source line 3 · 2026-05-10T07:41:58.382Z_

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

## Idea under review (round 6/10)
{
  "title": "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning",
  "core_problem": "Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.",
  "opportunity": "Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K Kazakh-language questions spanning STEM, humanities, and social sciences sourced from authentic educational materials; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.",
  "landscape": "PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.",
  "approach": "We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\n\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\n\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 on typological alignment tasks versus ρ=0.260 for the full 800-feature set while also improving downstream cross-lingual NLP performance, we apply this feature selection before computing cosine distances. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\n\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\n\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\n\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter are discarded. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\n\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh, MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG and CLO serve as primary baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.",
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
  "description": "This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358 vs. ρ=0.260 for the full 800-feature set) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU, MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.",
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
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "87e9a004-e9d5-4ba7-8db5-6ce426a20098",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:41:58.377Z_

```json
{
  "parentUuid": "87e9a004-e9d5-4ba7-8db5-6ce426a20098",
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
  "uuid": "7e60ade2-805e-43f0-bd13-84c88eebbfcc",
  "timestamp": "2026-05-10T07:41:58.377Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:41:58.377Z_

```json
{
  "parentUuid": "7e60ade2-805e-43f0-bd13-84c88eebbfcc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d2dc9644-12a8-4233-8f79-02b07d887556",
  "timestamp": "2026-05-10T07:41:58.377Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
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
  "leafUuid": "d2dc9644-12a8-4233-8f79-02b07d887556",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-pivot curriculum instruction tuning for agglutinative languages",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:42:24.898Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this Round 6 submission of "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning" (TWMP). I need to independently verify claims, find competing work, and assess whether the Round 5 issues have been addressed.

Let me first analyze what Round 5 requested:
1. Add Foroutan et al. (arXiv:2510.25947) - MODERATE


2. Add LangGPS (arXiv:2511.10229, AAAI 2026) - MODERATE
3. Add Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings) - MODERATE
4. Add arXiv:2502.13647 (ACL 2025 Main, Kazakh instruction tuning) - MINOR
5. Add Simple Additions, Substantial Gains: Expanding URIEL+ (arXiv:2510.27183) - MINOR
6. DPO prerequisite probe threshold characterization - MINOR

Now I'm checking the current submission to see what's been addressed.

Looking at the landscape section, I can see several papers are now cited: Sherkala-Chat, CLO, Implicit Cross-Lingual Rewarding, "Family Matters," "Cross-Linguistic Transfer in Multilingual NLP," Multi-Linguistic LoRA Merging (correctly labeled as NeurIPS 2025 ER Workshop), and DCO. But I need to verify whether Foroutan et al. (arXiv:2510.25947) from the previous round's feedback is actually mentioned in the landscape or approach sections.

Checking through the landscape and key_references, I don't see Foroutan et al. explicitly cited. The same issue persists for several other papers: LangGPS (arXiv:2511.10229, AAAI 2026), Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings), Kazakh instruction tuning (arXiv:2502.13647), and Simple Additions, Substantial Gains (arXiv:2510.27183) are all still missing from the submission. The approach section does mention the probe for DPO prerequisite characterization, but I need to verify the full context there.

Let me look more carefully at what's actually in Round 6 versus what was in Round 5. The DPO quality gate is described in the approach—they run a 500-instruction probe per language pair on the base model and exclude any pair that doesn't meet the ≥20-token gate threshold in >5% of samples, falling back to SFT-weighted sampling instead. However, the submission doesn't specify the actual distribution of chosen-pool sizes per instruction or how often the fallback was triggered.

I'm also noticing some key citations are missing from Round 6—Foroutan et al., LangGPS, the Code-Switching Curriculum work, and a couple of arXiv papers that seem relevant to the approach. I should verify whether these are actually critical omissions or if the paper adequately covers the conceptual ground they address.

Let me search for current competing work and independently verify the core claims to see if there are other recent approaches I should flag.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2dc9644-12a8-4233-8f79-02b07d887556",
  "isSidechain": false,
  "requestId": "req_011CatWdX9KFnB4UgYZJH4T3",
  "type": "assistant",
  "uuid": "d62ec0bf-12fb-47d7-9995-ef38f4bf7e1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HKk5pyJ36dp881z1CqDhxF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24145,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1271,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 24145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24145
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

_source line 9 · 2026-05-10T07:42:24.900Z_

I'll conduct independent research to verify the Round 6 submission's claims and check whether Round 5 issues have been addressed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d62ec0bf-12fb-47d7-9995-ef38f4bf7e1a",
  "isSidechain": false,
  "requestId": "req_011CatWdX9KFnB4UgYZJH4T3",
  "type": "assistant",
  "uuid": "1497f98b-204e-48c0-b3b1-9f14d124e81e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HKk5pyJ36dp881z1CqDhxF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24145,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1271,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 24145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24145
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

_source line 10 · 2026-05-10T07:42:25.134Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011SHmoZV2oSDFbGbRKB3wUD`</summary>

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
  "parentUuid": "1497f98b-204e-48c0-b3b1-9f14d124e81e",
  "isSidechain": false,
  "requestId": "req_011CatWdX9KFnB4UgYZJH4T3",
  "type": "assistant",
  "uuid": "fca79610-8c26-44c3-a124-43d545d6c847",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HKk5pyJ36dp881z1CqDhxF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24145,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1271,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 24145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24145
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

_source line 11 · 2026-05-10T07:42:25.140Z_

<details><summary>↩ Tool result · `toolu_011SHmoZV2oSDFbGbRKB3wUD`</summary>

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
  "parentUuid": "fca79610-8c26-44c3-a124-43d545d6c847",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "155d7d3c-95f6-476d-9644-52745c30ea69",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "fca79610-8c26-44c3-a124-43d545d6c847",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T07:42:32.942Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me run multiple independent searches to verify the Round 6 submission's claims and check for new competing work. I'll focus on:

1. Whether the Round 5 issues are addressed in the Round 6 text (I already noted they appear not to be)
2. New competing work that may have emerged
3. Verifying key claims about the existing papers

Let me search in parallel for:
- Foroutan et al. multilingual data mixtures (verify it's a real paper and what it actually says)
- LangGPS (verify it's real)
- Code-switching curriculum learning


- Recent cross-lingual instruction tuning work from 2025-2026 and any TWMP-adjacent approaches
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "155d7d3c-95f6-476d-9644-52745c30ea69",
  "isSidechain": false,
  "requestId": "req_011CatWfVkXmGgpokGRApQvN",
  "type": "assistant",
  "uuid": "3c5df547-df56-4ec3-8ece-dfd784bfa40d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012BPnC2QPZr9UCwNqF9q4q2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2288,
      "cache_read_input_tokens": 35776,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 411,
          "cache_read_input_tokens": 35776,
          "cache_creation_input_tokens": 2288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2288
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

_source line 13 · 2026-05-10T07:42:32.947Z_

I'll run parallel searches on the key issues: verifying Round 5 missing citations exist, checking for new competing work, and assessing the current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c5df547-df56-4ec3-8ece-dfd784bfa40d",
  "isSidechain": false,
  "requestId": "req_011CatWfVkXmGgpokGRApQvN",
  "type": "assistant",
  "uuid": "c00f254b-2658-4c76-b30d-e1c3fd105d31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012BPnC2QPZr9UCwNqF9q4q2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2288,
      "cache_read_input_tokens": 35776,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 411,
          "cache_read_input_tokens": 35776,
          "cache_creation_input_tokens": 2288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2288
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

_source line 14 · 2026-05-10T07:42:33.778Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012F49f7SvTzFtagsdEKTqj2`</summary>

```json
{
  "query": "arXiv:2510.25947 Foroutan multilingual data mixtures curriculum pretraining 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c00f254b-2658-4c76-b30d-e1c3fd105d31",
  "isSidechain": false,
  "requestId": "req_011CatWfVkXmGgpokGRApQvN",
  "type": "assistant",
  "uuid": "6a4081f9-e282-4f5a-beee-a08013c2366c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012BPnC2QPZr9UCwNqF9q4q2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2288,
      "cache_read_input_tokens": 35776,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 411,
          "cache_read_input_tokens": 35776,
          "cache_creation_input_tokens": 2288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2288
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

_source line 15 · 2026-05-10T07:42:34.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0111qWgSirzfTjbvrSe6nnqq`</summary>

```json
{
  "query": "LangGPS arXiv:2511.10229 language separability multilingual instruction tuning AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a4081f9-e282-4f5a-beee-a08013c2366c",
  "isSidechain": false,
  "requestId": "req_011CatWfVkXmGgpokGRApQvN",
  "type": "assistant",
  "uuid": "13e341e9-8b2a-4c10-806b-6b9b61da0c6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012BPnC2QPZr9UCwNqF9q4q2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2288,
      "cache_read_input_tokens": 35776,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 411,
          "cache_read_input_tokens": 35776,
          "cache_creation_input_tokens": 2288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2288
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

_source line 16 · 2026-05-10T07:42:34.940Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FA8eH4jmKJXn4c9n5ex1F2`</summary>

```json
{
  "query": "code-switching curriculum learning cross-lingual transfer LLMs arXiv 2411.02460 ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13e341e9-8b2a-4c10-806b-6b9b61da0c6f",
  "isSidechain": false,
  "requestId": "req_011CatWfVkXmGgpokGRApQvN",
  "type": "assistant",
  "uuid": "34e30f23-8439-44b4-a06e-bc4d1bd6fb80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012BPnC2QPZr9UCwNqF9q4q2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2288,
      "cache_read_input_tokens": 35776,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 411,
          "cache_read_input_tokens": 35776,
          "cache_creation_input_tokens": 2288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2288
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

_source line 17 · 2026-05-10T07:42:41.734Z_

<details><summary>↩ Tool result · `toolu_0111qWgSirzfTjbvrSe6nnqq`</summary>

```text
Web search results for query: "LangGPS arXiv:2511.10229 language separability multilingual instruction tuning AAAI 2026"

Links: [{"title":"[2511.10229] LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning","url":"https://arxiv.org/abs/2511.10229"},{"title":"LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning","url":"https://arxiv.org/html/2511.10229"},{"title":"Computation and Language 2025","url":"https://www.arxiv.org/list/cs.CL/2025?skip=15550&show=1000"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models","url":"https://arxiv.org/html/2406.16783v1"},{"title":"[2401.01854] Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/abs/2401.01854"},{"title":"[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/abs/2402.13703"},{"title":"BayLing 2: A Multilingual Large Language Model with Efficient Language Alignment","url":"https://arxiv.org/html/2411.16300"},{"title":"AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment","url":"https://arxiv.org/html/2509.24338"},{"title":"Language Surgery in Multilingual Large Language Models","url":"https://arxiv.org/html/2506.12450v2"}]

Based on the search results, I found detailed information about the LangGPS paper:

## LangGPS: Language Separability Guided Data Pre-Selection

LangGPS is a lightweight two-stage pre-selection framework guided by language separability which quantifies how well samples in different languages can be distinguished in the model's representation space.

**Problem Statement:**
Joint multilingual instruction tuning is a widely adopted approach to improve the multilingual instruction-following ability and downstream performance of large language models (LLMs), but the resulting multilingual capability remains highly sensitive to the composition and selection of the training data. Existing selection methods, often based on features like text quality, diversity, or task relevance, typically overlook the intrinsic linguistic structure of multilingual data.

**Approach:**
LangGPS first filters training data based on separability scores and then refines the subset using existing selection methods.

**Results:**
Extensive experiments across six benchmarks and 22 languages demonstrate that applying LangGPS on top of existing selection methods improves their effectiveness and generalizability in multilingual training, especially for understanding tasks and low-resource languages.

**Key Insights:**
Highly separable samples facilitate the formation of clearer language boundaries and support faster adaptation, while low-separability samples tend to function as bridges for cross-lingual alignment. Language separability can also serve as an effective signal for multilingual curriculum learning, where interleaving samples with diverse separability levels yields stable and generalizable gains.

**Publication Status:**
The paper has been accepted to the AAAI 2026 Main Track.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13e341e9-8b2a-4c10-806b-6b9b61da0c6f",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "875835ed-8249-450d-b06d-ddce89a2d4d5",
  "toolUseResult": {
    "query": "LangGPS arXiv:2511.10229 language separability multilingual instruction tuning AAAI 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LEgxnNcBN7kN5wwbd8jtZv",
        "content": [
          {
            "title": "[2511.10229] LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning",
            "url": "https://arxiv.org/abs/2511.10229"
          },
          {
            "title": "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning",
            "url": "https://arxiv.org/html/2511.10229"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://www.arxiv.org/list/cs.CL/2025?skip=15550&show=1000"
          },
          {
            "title": "Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?",
            "url": "https://arxiv.org/html/2402.13703v3"
          },
          {
            "title": "M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models",
            "url": "https://arxiv.org/html/2406.16783v1"
          },
          {
            "title": "[2401.01854] Multilingual Instruction Tuning With Just a Pinch of Multilinguality",
            "url": "https://arxiv.org/abs/2401.01854"
          },
          {
            "title": "[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?",
            "url": "https://arxiv.org/abs/2402.13703"
          },
          {
            "title": "BayLing 2: A Multilingual Large Language Model with Efficient Language Alignment",
            "url": "https://arxiv.org/html/2411.16300"
          },
          {
            "title": "AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment",
            "url": "https://arxiv.org/html/2509.24338"
          },
          {
            "title": "Language Surgery in Multilingual Large Language Models",
            "url": "https://arxiv.org/html/2506.12450v2"
          }
        ]
      },
      "Based on the search results, I found detailed information about the LangGPS paper:\n\n## LangGPS: Language Separability Guided Data Pre-Selection\n\nLangGPS is a lightweight two-stage pre-selection framework guided by language separability which quantifies how well samples in different languages can be distinguished in the model's representation space.\n\n**Problem Statement:**\nJoint multilingual instruction tuning is a widely adopted approach to improve the multilingual instruction-following ability and downstream performance of large language models (LLMs), but the resulting multilingual capability remains highly sensitive to the composition and selection of the training data. Existing selection methods, often based on features like text quality, diversity, or task relevance, typically overlook the intrinsic linguistic structure of multilingual data.\n\n**Approach:**\nLangGPS first filters training data based on separability scores and then refines the subset using existing selection methods.\n\n**Results:**\nExtensive experiments across six benchmarks and 22 languages demonstrate that applying LangGPS on top of existing selection methods improves their effectiveness and generalizability in multilingual training, especially for understanding tasks and low-resource languages.\n\n**Key Insights:**\nHighly separable samples facilitate the formation of clearer language boundaries and support faster adaptation, while low-separability samples tend to function as bridges for cross-lingual alignment. Language separability can also serve as an effective signal for multilingual curriculum learning, where interleaving samples with diverse separability levels yields stable and generalizable gains.\n\n**Publication Status:**\nThe paper has been accepted to the AAAI 2026 Main Track."
    ],
    "durationSeconds": 7.434130255000004
  },
  "sourceToolAssistantUUID": "13e341e9-8b2a-4c10-806b-6b9b61da0c6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T07:42:42.361Z_

<details><summary>↩ Tool result · `toolu_012F49f7SvTzFtagsdEKTqj2`</summary>

```text
Web search results for query: "arXiv:2510.25947 Foroutan multilingual data mixtures curriculum pretraining 2025"

Links: [{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"[2510.25947] Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/abs/2510.25947"},{"title":"(PDF) Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://www.researchgate.net/publication/397087634_Revisiting_Multilingual_Data_Mixtures_in_Language_Model_Pretraining"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251025947F/abstract"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining | OpenReview","url":"https://openreview.net/forum?id=IKJyRyHpHV"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining | alphaXiv","url":"https://www.alphaxiv.org/abs/2510.25947v1"},{"title":"ATLAS : Adaptive Transfer Scaling Laws for Multilingual Pretraining, Finetuning, and Decoding the Curse of Multilinguality","url":"https://arxiv.org/html/2510.22037"},{"title":"Enhancing Multilingual LLM Pretraining with Model-Based Data Selection","url":"https://arxiv.org/pdf/2502.10361"},{"title":"Multilingual Web Pretraining Data","url":"https://www.emergentmind.com/topics/multilingual-web-pretraining-data"},{"title":"The Role of Mixed-Language Documents for Multilingual Large Language Model Pretraining","url":"https://arxiv.org/html/2601.00364"}]

I found the paper you're looking for! Here's what I found:

## Paper Overview

The paper titled "Revisiting Multilingual Data Mixtures in Language Model Pretraining" by Negar Foroutan and 3 other authors investigates the impact of different multilingual data mixtures in pretraining large language models, addressing concerns about potential trade-offs between language coverage and model performance (i.e., the curse of multilinguality).

## Key Findings

The researchers investigated these assumptions by training 1.1B and 3B parameter LLMs on diverse multilingual corpora, varying the number of languages from 25 to 400.

Their key finding is that combining English and multilingual data does not necessarily degrade the in-language performance of either group, provided that languages have a sufficient number of tokens included in the pretraining corpus.

The study also observes that using English as a pivot language (i.e., a high-resource language that serves as a catalyst for multilingual generalization) yields benefits across language families.

## Paper Details

- **arXiv ID:** 2510.25947
- **Publication Date:** October 29, 2025
- **Authors:** Negar Foroutan, Paul Teiletche, Ayush Kumar Tarun, Antoine Bosselut (EPFL, Lausanne, Switzerland)
- **Status:** Under review

The paper is accessible on arXiv at https://arxiv.org/abs/2510.25947


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a4081f9-e282-4f5a-beee-a08013c2366c",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "6c5c2efd-c6bb-4ca3-83cd-6a5cee0e9a85",
  "toolUseResult": {
    "query": "arXiv:2510.25947 Foroutan multilingual data mixtures curriculum pretraining 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J9EF6jqt2LZgvFPWjVE8P9",
        "content": [
          {
            "title": "Revisiting Multilingual Data Mixtures in Language Model Pretraining",
            "url": "https://arxiv.org/html/2510.25947v1"
          },
          {
            "title": "[2510.25947] Revisiting Multilingual Data Mixtures in Language Model Pretraining",
            "url": "https://arxiv.org/abs/2510.25947"
          },
          {
            "title": "(PDF) Revisiting Multilingual Data Mixtures in Language Model Pretraining",
            "url": "https://www.researchgate.net/publication/397087634_Revisiting_Multilingual_Data_Mixtures_in_Language_Model_Pretraining"
          },
          {
            "title": "Revisiting Multilingual Data Mixtures in Language Model Pretraining - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv251025947F/abstract"
          },
          {
            "title": "Revisiting Multilingual Data Mixtures in Language Model Pretraining | OpenReview",
            "url": "https://openreview.net/forum?id=IKJyRyHpHV"
          },
          {
            "title": "Revisiting Multilingual Data Mixtures in Language Model Pretraining | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2510.25947v1"
          },
          {
            "title": "ATLAS : Adaptive Transfer Scaling Laws for Multilingual Pretraining, Finetuning, and Decoding the Curse of Multilinguality",
            "url": "https://arxiv.org/html/2510.22037"
          },
          {
            "title": "Enhancing Multilingual LLM Pretraining with Model-Based Data Selection",
            "url": "https://arxiv.org/pdf/2502.10361"
          },
          {
            "title": "Multilingual Web Pretraining Data",
            "url": "https://www.emergentmind.com/topics/multilingual-web-pretraining-data"
          },
          {
            "title": "The Role of Mixed-Language Documents for Multilingual Large Language Model Pretraining",
            "url": "https://arxiv.org/html/2601.00364"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\n## Paper Overview\n\nThe paper titled \"Revisiting Multilingual Data Mixtures in Language Model Pretraining\" by Negar Foroutan and 3 other authors investigates the impact of different multilingual data mixtures in pretraining large language models, addressing concerns about potential trade-offs between language coverage and model performance (i.e., the curse of multilinguality).\n\n## Key Findings\n\nThe researchers investigated these assumptions by training 1.1B and 3B parameter LLMs on diverse multilingual corpora, varying the number of languages from 25 to 400.\n\nTheir key finding is that combining English and multilingual data does not necessarily degrade the in-language performance of either group, provided that languages have a sufficient number of tokens included in the pretraining corpus.\n\nThe study also observes that using English as a pivot language (i.e., a high-resource language that serves as a catalyst for multilingual generalization) yields benefits across language families.\n\n## Paper Details\n\n- **arXiv ID:** 2510.25947\n- **Publication Date:** October 29, 2025\n- **Authors:** Negar Foroutan, Paul Teiletche, Ayush Kumar Tarun, Antoine Bosselut (EPFL, Lausanne, Switzerland)\n- **Status:** Under review\n\nThe paper is accessible on arXiv at https://arxiv.org/abs/2510.25947"
    ],
    "durationSeconds": 8.577722363000001
  },
  "sourceToolAssistantUUID": "6a4081f9-e282-4f5a-beee-a08013c2366c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
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
  "leafUuid": "6c5c2efd-c6bb-4ca3-83cd-6a5cee0e9a85",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-pivot curriculum instruction tuning for agglutinative languages",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Tool result

_source line 21 · 2026-05-10T07:42:45.815Z_

<details><summary>↩ Tool result · `toolu_01FA8eH4jmKJXn4c9n5ex1F2`</summary>

```text
Web search results for query: "code-switching curriculum learning cross-lingual transfer LLMs arXiv 2411.02460 ACL 2025"

Links: [{"title":"[2411.02460] Code-Switching Curriculum Learning for Multilingual Transfer in LLMs","url":"https://arxiv.org/abs/2411.02460"},{"title":"Code-Switching Curriculum Learning for Multilingual ...","url":"https://aclanthology.org/2025.findings-acl.407.pdf"},{"title":"(PDF) Code-Switching Curriculum Learning for Multilingual Transfer in LLMs","url":"https://www.researchgate.net/publication/385560207_Code-Switching_Curriculum_Learning_for_Multilingual_Transfer_in_LLMs"},{"title":"Code-Switching Curriculum Learning for Multilingual Transfer in LLMs | OpenReview","url":"https://openreview.net/forum?id=YKnko6lYde"},{"title":"Investigating and Scaling up Code-Switching for ...","url":"https://aclanthology.org/2025.findings-acl.575.pdf"},{"title":"Investigating and Scaling up Code-Switching for","url":"https://arxiv.org/pdf/2504.01801"},{"title":"Code-Switching Curriculum Learning for Multilingual Transfer in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.407/"},{"title":"[Quick Review] Code-Switching Curriculum Learning for Multilingual Transfer in LLMs","url":"https://liner.com/review/codeswitching-curriculum-learning-for-multilingual-transfer-in-llms"},{"title":"[Literature Review] Code-Switching Curriculum Learning for Multilingual Transfer in LLMs","url":"https://www.themoonlight.io/en/review/code-switching-curriculum-learning-for-multilingual-transfer-in-llms"},{"title":"Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training","url":"https://arxiv.org/html/2504.20484"}]

Based on the search results, I found comprehensive information about this research paper:

## Paper Summary

The paper proposes code-switching curriculum learning (CSCL) to enhance cross-lingual transfer for LLMs, inspired by the human process of second language acquisition, particularly code-switching—the practice of language alternation in a conversation.

## Motivation

Large language models (LLMs) now exhibit near human-level performance in various tasks, but their performance drops drastically after a handful of high-resource languages due to the imbalance in pre-training data.

## Methodology

CSCL mimics the stages of human language learning by progressively training models with a curriculum consisting of 1) token-level code-switching, 2) sentence-level code-switching, and 3) monolingual corpora.

## Key Results

Using Qwen 2 as their underlying model, the authors demonstrate the efficacy of the CSCL in improving language transfer to Korean, achieving significant performance gains compared to monolingual continual pre-training methods. The findings are extended to various languages, including Japanese (high-resource) and Indonesian (low-resource), and using two additional models (Gemma 2 and Phi 3.5).

## Ablation Studies

Ablation studies reveal that both token- and sentence-level code-switching significantly enhance cross-lingual transfer and that curriculum learning amplifies these effects.

## Additional Benefits

CSCL mitigates spurious correlations between language resources and safety alignment, presenting a robust, efficient framework for more equitable language transfer in LLMs. CSCL is effective for low-resource settings where high-quality, monolingual corpora for language transfer are hardly available.

The paper was published in the Findings of ACL 2025 and has been on arXiv since November 2024 (arXiv:2411.02460).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34e30f23-8439-44b4-a06e-bc4d1bd6fb80",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "a0e844d1-d39d-40a4-8ce2-d5919cd26f5e",
  "toolUseResult": {
    "query": "code-switching curriculum learning cross-lingual transfer LLMs arXiv 2411.02460 ACL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M9Lpp7j7Ag2QX5mFthS1R6",
        "content": [
          {
            "title": "[2411.02460] Code-Switching Curriculum Learning for Multilingual Transfer in LLMs",
            "url": "https://arxiv.org/abs/2411.02460"
          },
          {
            "title": "Code-Switching Curriculum Learning for Multilingual ...",
            "url": "https://aclanthology.org/2025.findings-acl.407.pdf"
          },
          {
            "title": "(PDF) Code-Switching Curriculum Learning for Multilingual Transfer in LLMs",
            "url": "https://www.researchgate.net/publication/385560207_Code-Switching_Curriculum_Learning_for_Multilingual_Transfer_in_LLMs"
          },
          {
            "title": "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=YKnko6lYde"
          },
          {
            "title": "Investigating and Scaling up Code-Switching for ...",
            "url": "https://aclanthology.org/2025.findings-acl.575.pdf"
          },
          {
            "title": "Investigating and Scaling up Code-Switching for",
            "url": "https://arxiv.org/pdf/2504.01801"
          },
          {
            "title": "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.407/"
          },
          {
            "title": "[Quick Review] Code-Switching Curriculum Learning for Multilingual Transfer in LLMs",
            "url": "https://liner.com/review/codeswitching-curriculum-learning-for-multilingual-transfer-in-llms"
          },
          {
            "title": "[Literature Review] Code-Switching Curriculum Learning for Multilingual Transfer in LLMs",
            "url": "https://www.themoonlight.io/en/review/code-switching-curriculum-learning-for-multilingual-transfer-in-llms"
          },
          {
            "title": "Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training",
            "url": "https://arxiv.org/html/2504.20484"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about this research paper:\n\n## Paper Summary\n\nThe paper proposes code-switching curriculum learning (CSCL) to enhance cross-lingual transfer for LLMs, inspired by the human process of second language acquisition, particularly code-switching—the practice of language alternation in a conversation.\n\n## Motivation\n\nLarge language models (LLMs) now exhibit near human-level performance in various tasks, but their performance drops drastically after a handful of high-resource languages due to the imbalance in pre-training data.\n\n## Methodology\n\nCSCL mimics the stages of human language learning by progressively training models with a curriculum consisting of 1) token-level code-switching, 2) sentence-level code-switching, and 3) monolingual corpora.\n\n## Key Results\n\nUsing Qwen 2 as their underlying model, the authors demonstrate the efficacy of the CSCL in improving language transfer to Korean, achieving significant performance gains compared to monolingual continual pre-training methods. The findings are extended to various languages, including Japanese (high-resource) and Indonesian (low-resource), and using two additional models (Gemma 2 and Phi 3.5).\n\n## Ablation Studies\n\nAblation studies reveal that both token- and sentence-level code-switching significantly enhance cross-lingual transfer and that curriculum learning amplifies these effects.\n\n## Additional Benefits\n\nCSCL mitigates spurious correlations between language resources and safety alignment, presenting a robust, efficient framework for more equitable language transfer in LLMs. CSCL is effective for low-resource settings where high-quality, monolingual corpora for language transfer are hardly available.\n\nThe paper was published in the Findings of ACL 2025 and has been on arXiv since November 2024 (arXiv:2411.02460)."
    ],
    "durationSeconds": 10.871626615
  },
  "sourceToolAssistantUUID": "34e30f23-8439-44b4-a06e-bc4d1bd6fb80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T07:43:02.287Z_

<details><summary>Logged reasoning block</summary>

```text
Good. All three Round 5 moderate citations are confirmed to exist and are relevant. Now let me check:
1. Whether these are addressed in the Round 6 submission
2. The Kazakh instruction tuning paper (arXiv:2502.13647)
3. URIEL+ expansion (arXiv:2510.27183)
4. New competing work since Round 5

Looking at the Round 6 submission text carefully, I need to check the landscape and key_references sections:

**Landscape section mentions:**
- PLUG (ACL 2024)
- CLO (arXiv:2505.14297; ACL 2025)


- Sherkala-Chat (arXiv:2503.01493)
- Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings)
- Family Matters (arXiv:2510.00810)
- Cross-Linguistic Transfer in Multilingual NLP (arXiv:2505.13908, 2025)
- Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop)
- Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678)
- TIPA (arXiv:2601.16629; EACL 2026 Findings)
- Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809)

I'm also noting several papers that haven't made it into the landscape yet: Foroutan et al., LangGPS, the Code-Switching Curriculum work, recent Kazakh instruction tuning research, and the URIEL+ expansion. Now I'm going through the key references to see what else should be included.

None of these five papers from the previous round appear in the key references, which means they're still gaps in the current landscape. I should search for any newer competing work that's emerged since then.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0e844d1-d39d-40a4-8ce2-d5919cd26f5e",
  "isSidechain": false,
  "requestId": "req_011CatWh1nakQLUxxELb5TX2",
  "type": "assistant",
  "uuid": "c6abe18d-0143-4105-ad99-a469e3ca7294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WNPohiJo84e6TLHx15AtDn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3187,
      "cache_read_input_tokens": 38064,
      "output_tokens": 754,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 754,
          "cache_read_input_tokens": 38064,
          "cache_creation_input_tokens": 3187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3187
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

_source line 23 · 2026-05-10T07:43:02.301Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015LMQjjbNy5sDxT9eojFgay`</summary>

```json
{
  "query": "typological distance multilingual instruction tuning cross-lingual transfer 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6abe18d-0143-4105-ad99-a469e3ca7294",
  "isSidechain": false,
  "requestId": "req_011CatWh1nakQLUxxELb5TX2",
  "type": "assistant",
  "uuid": "429bd2a8-2b69-44f3-94e6-595f9cd73b0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WNPohiJo84e6TLHx15AtDn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3187,
      "cache_read_input_tokens": 38064,
      "output_tokens": 754,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 754,
          "cache_read_input_tokens": 38064,
          "cache_creation_input_tokens": 3187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3187
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

_source line 24 · 2026-05-10T07:43:02.789Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W8RT8wm3Xt6ukWddASpS3E`</summary>

```json
{
  "query": "Kazakh Mongolian Uyghur low-resource instruction tuning LLM 2025 2026 cross-lingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "429bd2a8-2b69-44f3-94e6-595f9cd73b0c",
  "isSidechain": false,
  "requestId": "req_011CatWh1nakQLUxxELb5TX2",
  "type": "assistant",
  "uuid": "28e9fab3-c669-4bcb-bc11-6a3a01acb3a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WNPohiJo84e6TLHx15AtDn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3187,
      "cache_read_input_tokens": 38064,
      "output_tokens": 754,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 754,
          "cache_read_input_tokens": 38064,
          "cache_creation_input_tokens": 3187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3187
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

_source line 25 · 2026-05-10T07:43:10.573Z_

<details><summary>↩ Tool result · `toolu_015LMQjjbNy5sDxT9eojFgay`</summary>

```text
Web search results for query: "typological distance multilingual instruction tuning cross-lingual transfer 2025 2026 arXiv"

Links: [{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090"},{"title":"[2505.13908] Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology","url":"https://arxiv.org/abs/2505.13908"},{"title":"Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages","url":"https://arxiv.org/html/2603.27651"},{"title":"Cross-Lingual Stability and Bias in Instruction-Tuned Language","url":"https://arxiv.org/pdf/2510.22823"},{"title":"Zero-shot Cross-lingual Transfer Learning with Multiple Source and Target Languages for Information Extraction: Language Selection and Adversarial Training","url":"https://arxiv.org/html/2411.08785"},{"title":"Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809"},{"title":"Rethinking what Matters: Effective and Robust Multilingual Realignment for Low-Resource Languages","url":"https://arxiv.org/html/2511.06497"},{"title":"[2404.04659] Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly","url":"https://arxiv.org/abs/2404.04659"},{"title":"[2501.00045] Improving Low-Resource Machine Translation via Cross-Linguistic Transfer from Typologically Similar High-Resource Languages","url":"https://arxiv.org/abs/2501.00045"}]

I found several highly relevant research papers on arXiv related to your search query about typological distance, multilingual instruction tuning, and cross-lingual transfer from 2025-2026. Here are the key findings:

## Recent Papers (2025-2026)

Research on multilingual fine-tuning strategies presents conflicting evidence, with some studies showing that scaling the number of tasks or languages during instruction tuning improves cross-lingual generalization, while others report that just 1–3 fine-tuning languages effectively trigger cross-lingual transfer.

Cross-lingual transfer has become a crucial aspect of multilingual NLP, as it allows for models trained on resource-rich languages to be applied to low-resource languages more effectively.

### Key Studies:

1. **Language Diversity in Fine-Tuning (2025)** - A systematic investigation across 132 translation directions shows that fine-tuning on broader language sets consistently improves translation across all categories: fully supervised, partially supervised, and zero-shot pairs.

2. **Cross-Linguistic Transfer and Language Families (May 2025)** - An arXiv paper (2505.13908) examines the role of language families and morphology in multilingual NLP cross-lingual transfer.

3. **Budget-Constrained Source Language Selection (2026)** - Selection strategies have been explored, including typological distance from linguistic databases.

4. **Instruction-Tuned Language Stability (2024-2025)** - Research shows that alignment, not scale, determines stability: aligned models maintain near-invariant accuracy across typologically distant and low-resource languages.

5. **Linguistically-Informed Multilingual Instruction Tuning (October 2024)** - Language selection techniques range from common methods such as typological feature vectors to less conventional but promising approaches, including language embeddings derived from semantic typology features.

6. **Low-Resource Machine Translation (2025)** - Studies examine cross-linguistic effectiveness of transfer learning for low-resource machine translation by fine-tuning models on typologically similar high-resource languages, with the hypothesis that linguistic similarity enables efficient adaptation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "429bd2a8-2b69-44f3-94e6-595f9cd73b0c",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "277a632b-8056-4ebc-9667-eec6475c6a56",
  "toolUseResult": {
    "query": "typological distance multilingual instruction tuning cross-lingual transfer 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NXHdXufDi8fdtgD8CMuh2a",
        "content": [
          {
            "title": "The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation",
            "url": "https://arxiv.org/html/2505.13090"
          },
          {
            "title": "[2505.13908] Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology",
            "url": "https://arxiv.org/abs/2505.13908"
          },
          {
            "title": "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages",
            "url": "https://arxiv.org/html/2603.27651"
          },
          {
            "title": "Cross-Lingual Stability and Bias in Instruction-Tuned Language",
            "url": "https://arxiv.org/pdf/2510.22823"
          },
          {
            "title": "Zero-shot Cross-lingual Transfer Learning with Multiple Source and Target Languages for Information Extraction: Language Selection and Adversarial Training",
            "url": "https://arxiv.org/html/2411.08785"
          },
          {
            "title": "Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"
          },
          {
            "title": "Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?",
            "url": "https://arxiv.org/html/2410.07809"
          },
          {
            "title": "Rethinking what Matters: Effective and Robust Multilingual Realignment for Low-Resource Languages",
            "url": "https://arxiv.org/html/2511.06497"
          },
          {
            "title": "[2404.04659] Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly",
            "url": "https://arxiv.org/abs/2404.04659"
          },
          {
            "title": "[2501.00045] Improving Low-Resource Machine Translation via Cross-Linguistic Transfer from Typologically Similar High-Resource Languages",
            "url": "https://arxiv.org/abs/2501.00045"
          }
        ]
      },
      "I found several highly relevant research papers on arXiv related to your search query about typological distance, multilingual instruction tuning, and cross-lingual transfer from 2025-2026. Here are the key findings:\n\n## Recent Papers (2025-2026)\n\nResearch on multilingual fine-tuning strategies presents conflicting evidence, with some studies showing that scaling the number of tasks or languages during instruction tuning improves cross-lingual generalization, while others report that just 1–3 fine-tuning languages effectively trigger cross-lingual transfer.\n\nCross-lingual transfer has become a crucial aspect of multilingual NLP, as it allows for models trained on resource-rich languages to be applied to low-resource languages more effectively.\n\n### Key Studies:\n\n1. **Language Diversity in Fine-Tuning (2025)** - A systematic investigation across 132 translation directions shows that fine-tuning on broader language sets consistently improves translation across all categories: fully supervised, partially supervised, and zero-shot pairs.\n\n2. **Cross-Linguistic Transfer and Language Families (May 2025)** - An arXiv paper (2505.13908) examines the role of language families and morphology in multilingual NLP cross-lingual transfer.\n\n3. **Budget-Constrained Source Language Selection (2026)** - Selection strategies have been explored, including typological distance from linguistic databases.\n\n4. **Instruction-Tuned Language Stability (2024-2025)** - Research shows that alignment, not scale, determines stability: aligned models maintain near-invariant accuracy across typologically distant and low-resource languages.\n\n5. **Linguistically-Informed Multilingual Instruction Tuning (October 2024)** - Language selection techniques range from common methods such as typological feature vectors to less conventional but promising approaches, including language embeddings derived from semantic typology features.\n\n6. **Low-Resource Machine Translation (2025)** - Studies examine cross-linguistic effectiveness of transfer learning for low-resource machine translation by fine-tuning models on typologically similar high-resource languages, with the hypothesis that linguistic similarity enables efficient adaptation."
    ],
    "durationSeconds": 8.255872195999997
  },
  "sourceToolAssistantUUID": "429bd2a8-2b69-44f3-94e6-595f9cd73b0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T07:43:11.252Z_

<details><summary>↩ Tool result · `toolu_01W8RT8wm3Xt6ukWddASpS3E`</summary>

```text
Web search results for query: "Kazakh Mongolian Uyghur low-resource instruction tuning LLM 2025 2026 cross-lingual"

Links: [{"title":"The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization","url":"https://www.mdpi.com/2504-2289/9/5/137"},{"title":"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.559/"},{"title":"MiLiC-Eval: Benchmarking Multilingual LLMs for China’s Minority Languages","url":"https://arxiv.org/html/2503.01150v1"},{"title":"Fine-Tuning Large Language Models for Kazakh Text Simplification | MDPI","url":"https://www.mdpi.com/2076-3417/15/15/8344"},{"title":"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur | OpenReview","url":"https://openreview.net/forum?id=YVwThg7sQi"},{"title":"MiLiC-Eval: Benchmarking Multilingual LLMs for China's ...","url":"https://aclanthology.org/2025.findings-acl.578.pdf"},{"title":"Low-Resource Language Expansion and Translation ...","url":"https://aclanthology.org/2025.coling-main.559.pdf"},{"title":"[2502.13647] Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh","url":"https://arxiv.org/abs/2502.13647"},{"title":"Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.706/"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting | OpenReview","url":"https://openreview.net/forum?id=wRcTCcb0H5"}]

I found several recent research papers and projects addressing low-resource instruction tuning for Kazakh, Mongolian, and Uyghur languages. Here are the key findings:

## Recent Work on Kazakh LLMs

A 1.94B parameter LLaMA-based model has been developed for Kazakh that demonstrates strong, culturally aligned performance without massive infrastructure. The model was built in two stages: causal language modeling from scratch followed by instruction tuning.

Sherkala-Chat (8B), a state-of-the-art instruction-tuned LLM designed for Kazakh, is trained on 45.3B tokens across Kazakh, English, Russian, and Turkish, and demonstrates strong knowledge and reasoning abilities in Kazakh.

A large-scale (10,600 samples) instruction-following dataset has been introduced covering key institutional and cultural knowledge relevant to Kazakhstan.

## Work on Uyghur Language Expansion

Research demonstrates how to efficiently expand low-resource languages for large language models using Uyghur as an example through a four-stage process: collecting and pre-processing monolingual data, conducting continuous pre-training, fine-tuning with less parallel corpora using translation supervision, and proposing direct preference optimization based on translation self-evolution (DPOSE).

## Cross-Lingual Benchmarking

MiLiC-Eval is a comprehensive framework with 24K instances across 9 tasks focusing on 4 Minority Languages in China (including Uyghur, Kazakh, Mongolian, and Tibetan). Research includes continual pretraining of Qwen-2.5-0.5B on corpora for Uyghur and Mongolian.

These projects collectively represent significant efforts in 2025-2026 to advance instruction tuning and cross-lingual capabilities for these underrepresented low-resource languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28e9fab3-c669-4bcb-bc11-6a3a01acb3a6",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "1ebf46f0-56f2-43f0-880d-760391e101f3",
  "toolUseResult": {
    "query": "Kazakh Mongolian Uyghur low-resource instruction tuning LLM 2025 2026 cross-lingual",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GzCWuVte5Gr6dEEbK9NJm9",
        "content": [
          {
            "title": "The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization",
            "url": "https://www.mdpi.com/2504-2289/9/5/137"
          },
          {
            "title": "Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur - ACL Anthology",
            "url": "https://aclanthology.org/2025.coling-main.559/"
          },
          {
            "title": "MiLiC-Eval: Benchmarking Multilingual LLMs for China’s Minority Languages",
            "url": "https://arxiv.org/html/2503.01150v1"
          },
          {
            "title": "Fine-Tuning Large Language Models for Kazakh Text Simplification | MDPI",
            "url": "https://www.mdpi.com/2076-3417/15/15/8344"
          },
          {
            "title": "Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur | OpenReview",
            "url": "https://openreview.net/forum?id=YVwThg7sQi"
          },
          {
            "title": "MiLiC-Eval: Benchmarking Multilingual LLMs for China's ...",
            "url": "https://aclanthology.org/2025.findings-acl.578.pdf"
          },
          {
            "title": "Low-Resource Language Expansion and Translation ...",
            "url": "https://aclanthology.org/2025.coling-main.559.pdf"
          },
          {
            "title": "[2502.13647] Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh",
            "url": "https://arxiv.org/abs/2502.13647"
          },
          {
            "title": "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.706/"
          },
          {
            "title": "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting | OpenReview",
            "url": "https://openreview.net/forum?id=wRcTCcb0H5"
          }
        ]
      },
      "I found several recent research papers and projects addressing low-resource instruction tuning for Kazakh, Mongolian, and Uyghur languages. Here are the key findings:\n\n## Recent Work on Kazakh LLMs\n\nA 1.94B parameter LLaMA-based model has been developed for Kazakh that demonstrates strong, culturally aligned performance without massive infrastructure. The model was built in two stages: causal language modeling from scratch followed by instruction tuning.\n\nSherkala-Chat (8B), a state-of-the-art instruction-tuned LLM designed for Kazakh, is trained on 45.3B tokens across Kazakh, English, Russian, and Turkish, and demonstrates strong knowledge and reasoning abilities in Kazakh.\n\nA large-scale (10,600 samples) instruction-following dataset has been introduced covering key institutional and cultural knowledge relevant to Kazakhstan.\n\n## Work on Uyghur Language Expansion\n\nResearch demonstrates how to efficiently expand low-resource languages for large language models using Uyghur as an example through a four-stage process: collecting and pre-processing monolingual data, conducting continuous pre-training, fine-tuning with less parallel corpora using translation supervision, and proposing direct preference optimization based on translation self-evolution (DPOSE).\n\n## Cross-Lingual Benchmarking\n\nMiLiC-Eval is a comprehensive framework with 24K instances across 9 tasks focusing on 4 Minority Languages in China (including Uyghur, Kazakh, Mongolian, and Tibetan). Research includes continual pretraining of Qwen-2.5-0.5B on corpora for Uyghur and Mongolian.\n\nThese projects collectively represent significant efforts in 2025-2026 to advance instruction tuning and cross-lingual capabilities for these underrepresented low-resource languages."
    ],
    "durationSeconds": 8.459452164000002
  },
  "sourceToolAssistantUUID": "28e9fab3-c669-4bcb-bc11-6a3a01acb3a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T07:43:21.576Z_

<details><summary>Logged reasoning block</summary>

```text
Good. I've confirmed several things:
1. The Foroutan et al. paper exists (arXiv:2510.25947)
2. LangGPS exists (arXiv:2511.10229)
3. Code-Switching Curriculum exists (arXiv:2411.02460)
4. arXiv:2502.13647 exists (Kazakh instruction tuning at ACL 2025 Long)

Let me now look at whether the Round 5 feedback items are addressed in the Round 6 submission. Based on my careful reading, they are NOT:


None of these four papers appear in the landscape section or key references, and the URIEL+ expansion paper (arXiv:2510.27183) isn't mentioned at all. I also found another relevant paper on budget-constrained source language selection for cross-lingual transfer to African languages that could be worth considering.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ebf46f0-56f2-43f0-880d-760391e101f3",
  "isSidechain": false,
  "requestId": "req_011CatWitXpjz26ZWh2b3QG7",
  "type": "assistant",
  "uuid": "89a1c520-9d96-4186-bb3f-52e9e623f037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PQYAt56GDsu3JtH8vRLM6H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2850,
      "cache_read_input_tokens": 41251,
      "output_tokens": 526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2850,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 526,
          "cache_read_input_tokens": 41251,
          "cache_creation_input_tokens": 2850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2850
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

_source line 28 · 2026-05-10T07:43:21.955Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BtPM3LSDD6fu3SVJ6cSaUF`</summary>

```json
{
  "query": "Budget-Xfer source language selection cross-lingual transfer African languages arXiv 2603.27651"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89a1c520-9d96-4186-bb3f-52e9e623f037",
  "isSidechain": false,
  "requestId": "req_011CatWitXpjz26ZWh2b3QG7",
  "type": "assistant",
  "uuid": "ca21fa9a-28a4-4556-83c1-914f99374c12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PQYAt56GDsu3JtH8vRLM6H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2850,
      "cache_read_input_tokens": 41251,
      "output_tokens": 526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2850,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 526,
          "cache_read_input_tokens": 41251,
          "cache_creation_input_tokens": 2850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2850
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

_source line 29 · 2026-05-10T07:43:22.368Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NYJ4CEmgLAqtbLdMm3J4Q7`</summary>

```json
{
  "query": "multilingual instruction tuning pivot language typological curriculum 2026 arXiv new method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca21fa9a-28a4-4556-83c1-914f99374c12",
  "isSidechain": false,
  "requestId": "req_011CatWitXpjz26ZWh2b3QG7",
  "type": "assistant",
  "uuid": "fb7bfac1-8eb5-40d5-b61d-f50efd9dfc7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PQYAt56GDsu3JtH8vRLM6H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2850,
      "cache_read_input_tokens": 41251,
      "output_tokens": 526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2850,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 526,
          "cache_read_input_tokens": 41251,
          "cache_creation_input_tokens": 2850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2850
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "fb7bfac1-8eb5-40d5-b61d-f50efd9dfc7d",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-pivot curriculum instruction tuning for agglutinative languages",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Tool result

_source line 32 · 2026-05-10T07:43:29.916Z_

<details><summary>↩ Tool result · `toolu_01NYJ4CEmgLAqtbLdMm3J4Q7`</summary>

```text
Web search results for query: "multilingual instruction tuning pivot language typological curriculum 2026 arXiv new method"

Links: [{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809v1"},{"title":"Linguistically-Informed Multilingual Instruction Tuning","url":"https://arxiv.org/pdf/2410.07809"},{"title":"[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/abs/2311.08711"},{"title":"[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/abs/2402.13703"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854v4"},{"title":"[2401.01854] Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/abs/2401.01854"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"How Many Languages Make Good Multilingual Instruction Tuning? A Case Study on BLOOM","url":"https://arxiv.org/html/2404.04850v2"},{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090v2"}]

I found several relevant research papers on multilingual instruction tuning with connections to pivot languages and typological considerations. Here are the key findings:

## Recent Research on Multilingual Instruction Tuning

**Pivot Language and Typological Approaches:**

English can serve as a broadly effective pivot language, but in very low-resource settings, typological similarity becomes increasingly important. Using multiple pivots that balance breadth and proximity provides the most consistent benefits across language families.

One approach proposed is pivot language guided generation (PLUG), which utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages.

**Linguistically-Informed Language Selection:**

Research hypothesizes that optimum language subset selection for multilingual instruction tuning can be achieved in a linguistically informed manner, investigating various language selection techniques including typological feature vectors and semantic typology features.

**Curriculum Learning Approaches:**

The research explores whether curriculum learning among pivot languages could lead to greater multilingual generalization. One curriculum-based training strategy divides training into phases, with 0-25% using only English data, followed by 25-50% introducing three additional high-resource languages—Arabic, Chinese, and Russian—as pivot languages.

**Cross-lingual Instruction Following:**

Results demonstrate that instruction-tuning on parallel instead of monolingual corpora benefits cross-lingual instruction following capabilities by up to 9.9%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb7bfac1-8eb5-40d5-b61d-f50efd9dfc7d",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "4a461e6b-c686-45b4-bafc-13efac2dc280",
  "toolUseResult": {
    "query": "multilingual instruction tuning pivot language typological curriculum 2026 arXiv new method",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Euu3TFGjyPBU2rkx4UBoGo",
        "content": [
          {
            "title": "Revisiting Multilingual Data Mixtures in Language Model Pretraining",
            "url": "https://arxiv.org/html/2510.25947v1"
          },
          {
            "title": "Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?",
            "url": "https://arxiv.org/html/2410.07809v1"
          },
          {
            "title": "Linguistically-Informed Multilingual Instruction Tuning",
            "url": "https://arxiv.org/pdf/2410.07809"
          },
          {
            "title": "[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning",
            "url": "https://arxiv.org/abs/2311.08711"
          },
          {
            "title": "[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?",
            "url": "https://arxiv.org/abs/2402.13703"
          },
          {
            "title": "Multilingual Instruction Tuning With Just a Pinch of Multilinguality",
            "url": "https://arxiv.org/html/2401.01854v4"
          },
          {
            "title": "[2401.01854] Multilingual Instruction Tuning With Just a Pinch of Multilinguality",
            "url": "https://arxiv.org/abs/2401.01854"
          },
          {
            "title": "Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?",
            "url": "https://arxiv.org/html/2402.13703v3"
          },
          {
            "title": "How Many Languages Make Good Multilingual Instruction Tuning? A Case Study on BLOOM",
            "url": "https://arxiv.org/html/2404.04850v2"
          },
          {
            "title": "The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation",
            "url": "https://arxiv.org/html/2505.13090v2"
          }
        ]
      },
      "I found several relevant research papers on multilingual instruction tuning with connections to pivot languages and typological considerations. Here are the key findings:\n\n## Recent Research on Multilingual Instruction Tuning\n\n**Pivot Language and Typological Approaches:**\n\nEnglish can serve as a broadly effective pivot language, but in very low-resource settings, typological similarity becomes increasingly important. Using multiple pivots that balance breadth and proximity provides the most consistent benefits across language families.\n\nOne approach proposed is pivot language guided generation (PLUG), which utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages.\n\n**Linguistically-Informed Language Selection:**\n\nResearch hypothesizes that optimum language subset selection for multilingual instruction tuning can be achieved in a linguistically informed manner, investigating various language selection techniques including typological feature vectors and semantic typology features.\n\n**Curriculum Learning Approaches:**\n\nThe research explores whether curriculum learning among pivot languages could lead to greater multilingual generalization. One curriculum-based training strategy divides training into phases, with 0-25% using only English data, followed by 25-50% introducing three additional high-resource languages—Arabic, Chinese, and Russian—as pivot languages.\n\n**Cross-lingual Instruction Following:**\n\nResults demonstrate that instruction-tuning on parallel instead of monolingual corpora benefits cross-lingual instruction following capabilities by up to 9.9%."
    ],
    "durationSeconds": 7.544507715000014
  },
  "sourceToolAssistantUUID": "fb7bfac1-8eb5-40d5-b61d-f50efd9dfc7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T07:43:30.097Z_

<details><summary>↩ Tool result · `toolu_01BtPM3LSDD6fu3SVJ6cSaUF`</summary>

```text
Web search results for query: "Budget-Xfer source language selection cross-lingual transfer African languages arXiv 2603.27651"

Links: [{"title":"[2603.27651] Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages","url":"https://arxiv.org/abs/2603.27651"},{"title":"Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages","url":"https://arxiv.org/html/2603.27651"},{"title":"Multi-Source Cross-Lingual Model Transfer: Learning What to Share | Request PDF","url":"https://www.researchgate.net/publication/335780754_Multi-Source_Cross-Lingual_Model_Transfer_Learning_What_to_Share"},{"title":"Choosing Transfer Languages for Cross-Lingual Learning | Request PDF","url":"https://www.researchgate.net/publication/335779022_Choosing_Transfer_Languages_for_Cross-Lingual_Learning"},{"title":"[2409.10965] Cross-lingual transfer of multilingual models on low resource African Languages","url":"https://arxiv.org/abs/2409.10965"},{"title":"(PDF) Cross-Lingual Transfer Learning for Low-Resource NLP Tasks: Leveraging Multilingual Pretrained Models","url":"https://www.researchgate.net/publication/387003964_Cross-Lingual_Transfer_Learning_for_Low-Resource_NLP_Tasks_Leveraging_Multilingual_Pretrained_Models"},{"title":"Cross-lingual transfer of multilingual models on low resource African Languages","url":"https://arxiv.org/html/2409.10965v1"},{"title":"(PDF) Cross-lingual transfer of multilingual models on low resource African Languages","url":"https://www.researchgate.net/publication/384085211_Cross-lingual_transfer_of_multilingual_models_on_low_resource_African_Languages"},{"title":"[2601.03168] Can Embedding Similarity Predict Cross-Lingual Transfer? A Systematic Study on African Languages","url":"https://arxiv.org/abs/2601.03168"},{"title":"Can Embedding Similarity Predict Cross-Lingual Transfer? A Systematic Study on African Languages","url":"https://arxiv.org/html/2601.03168v1"}]

I found the paper you're looking for. Budget-Xfer is a framework that formulates multi-source cross-lingual transfer as a budget-constrained resource allocation problem, which jointly optimizes which source languages to include and how much data to allocate from each.

The work addresses a key issue in cross-lingual transfer learning: existing comparisons of source language selection strategies do not control for total training data, confounding language selection effects with data quantity effects.

The researchers evaluated four allocation strategies across named entity recognition and sentiment analysis for three African target languages (Hausa, Yoruba, Swahili) using two multilingual models, conducting 288 experiments. Their results show that multi-source transfer significantly outperforms single-source transfer.

The paper was submitted to arXiv on March 29, 2026, with the identifier 2603.27651.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca21fa9a-28a4-4556-83c1-914f99374c12",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "db1ff165-4e7f-407c-a345-198621cf8db0",
  "toolUseResult": {
    "query": "Budget-Xfer source language selection cross-lingual transfer African languages arXiv 2603.27651",
    "results": [
      {
        "tool_use_id": "srvtoolu_019VTsx6REEkuXDLdVsWF6tB",
        "content": [
          {
            "title": "[2603.27651] Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages",
            "url": "https://arxiv.org/abs/2603.27651"
          },
          {
            "title": "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages",
            "url": "https://arxiv.org/html/2603.27651"
          },
          {
            "title": "Multi-Source Cross-Lingual Model Transfer: Learning What to Share | Request PDF",
            "url": "https://www.researchgate.net/publication/335780754_Multi-Source_Cross-Lingual_Model_Transfer_Learning_What_to_Share"
          },
          {
            "title": "Choosing Transfer Languages for Cross-Lingual Learning | Request PDF",
            "url": "https://www.researchgate.net/publication/335779022_Choosing_Transfer_Languages_for_Cross-Lingual_Learning"
          },
          {
            "title": "[2409.10965] Cross-lingual transfer of multilingual models on low resource African Languages",
            "url": "https://arxiv.org/abs/2409.10965"
          },
          {
            "title": "(PDF) Cross-Lingual Transfer Learning for Low-Resource NLP Tasks: Leveraging Multilingual Pretrained Models",
            "url": "https://www.researchgate.net/publication/387003964_Cross-Lingual_Transfer_Learning_for_Low-Resource_NLP_Tasks_Leveraging_Multilingual_Pretrained_Models"
          },
          {
            "title": "Cross-lingual transfer of multilingual models on low resource African Languages",
            "url": "https://arxiv.org/html/2409.10965v1"
          },
          {
            "title": "(PDF) Cross-lingual transfer of multilingual models on low resource African Languages",
            "url": "https://www.researchgate.net/publication/384085211_Cross-lingual_transfer_of_multilingual_models_on_low_resource_African_Languages"
          },
          {
            "title": "[2601.03168] Can Embedding Similarity Predict Cross-Lingual Transfer? A Systematic Study on African Languages",
            "url": "https://arxiv.org/abs/2601.03168"
          },
          {
            "title": "Can Embedding Similarity Predict Cross-Lingual Transfer? A Systematic Study on African Languages",
            "url": "https://arxiv.org/html/2601.03168v1"
          }
        ]
      },
      "I found the paper you're looking for. Budget-Xfer is a framework that formulates multi-source cross-lingual transfer as a budget-constrained resource allocation problem, which jointly optimizes which source languages to include and how much data to allocate from each.\n\nThe work addresses a key issue in cross-lingual transfer learning: existing comparisons of source language selection strategies do not control for total training data, confounding language selection effects with data quantity effects.\n\nThe researchers evaluated four allocation strategies across named entity recognition and sentiment analysis for three African target languages (Hausa, Yoruba, Swahili) using two multilingual models, conducting 288 experiments. Their results show that multi-source transfer significantly outperforms single-source transfer.\n\nThe paper was submitted to arXiv on March 29, 2026, with the identifier 2603.27651."
    ],
    "durationSeconds": 8.138550464999993
  },
  "sourceToolAssistantUUID": "ca21fa9a-28a4-4556-83c1-914f99374c12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-10T07:43:30.102Z_

```json
{
  "parentUuid": "db1ff165-4e7f-407c-a345-198621cf8db0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a9a9e137-481e-4d58-94d7-8f36c419afe0",
  "timestamp": "2026-05-10T07:43:30.102Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 35 · 2026-05-10T07:43:56.650Z_

<details><summary>Logged reasoning block</summary>

```text
Let me check the Budget-Xfer paper (arXiv:2603.27651) more carefully. It's from March 2026 and directly addresses budget-constrained source language selection for cross-lingual transfer using multi-source transfer. This is closely related to TWMP's multi-pivot selection problem.

Key points about Budget-Xfer:
- Published March 29, 2026 (after the earlier review rounds)
- Addresses multi-source cross-lingual transfer for African languages (not Turkic)
- Formulates it as a budget-constrained resource allocation problem


- Demonstrates that multi-source transfer substantially outperforms single-source approaches on NER and sentiment analysis tasks, though it doesn't leverage typological distance or instruction tuning like TWMP does.

This is adjacent to TWMP but with meaningful differences—it's the kind of work EMNLP reviewers might reference. Now I'm going back through the Round 6 submission to verify whether the critical issues from Round 5 were actually addressed. The most concerning pattern I'm seeing is that all five major issues appear to remain unaddressed, starting with the missing citation to Foroutan et al. (arXiv:2510.25947).

I'm also noticing a new work from March 2026—Budget-Xfer (arXiv:2603.27651)—that aligns closely with TWMP's theme and should probably be discussed. Beyond the citation gaps, I need to check whether the DPO probe characterization concern from Round 5 has been resolved and if the Aya data coverage is now properly handled. Looking at the approach section, the prerequisite probe is described as a characterization result for close Turkic pivots...

but Round 5 specifically asked for clarification on what happens when the post-gate pool is empty for an instruction—whether it falls back to the SFT-weighted objective or gets silently skipped, plus a per-pair fallback rate as a characterization result. The Round 6 approach says instructions with no target-language candidates after filtering are discarded, but that doesn't directly address the fallback rate characterization that was requested. I'm checking whether the paper adequately addresses the Round 5 feedback about fallback mechanisms—specifically whether instructions that fail the length filter are truly discarded or if there's an SFT fallback I missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9a9e137-481e-4d58-94d7-8f36c419afe0",
  "isSidechain": false,
  "requestId": "req_011CatWkH6AqzEu48z2mWFD3",
  "type": "assistant",
  "uuid": "15ad3ab9-0816-4aea-94d8-c8781de1edba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LiCZHxQUuFJg7x7fsoPCm3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 843,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 44101,
      "output_tokens": 1032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 843,
          "output_tokens": 1032,
          "cache_read_input_tokens": 44101,
          "cache_creation_input_tokens": 1438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1438
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

_source line 36 · 2026-05-10T07:43:56.687Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VcQe4tMwztesbmKEZcktJQ`</summary>

```json
{
  "query": "URIEL+ expansion arXiv 2510.27183 script vectors Glottolog genealogical 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15ad3ab9-0816-4aea-94d8-c8781de1edba",
  "isSidechain": false,
  "requestId": "req_011CatWkH6AqzEu48z2mWFD3",
  "type": "assistant",
  "uuid": "c6afd7fa-dec6-436b-855c-651c80a29041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LiCZHxQUuFJg7x7fsoPCm3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 843,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 44101,
      "output_tokens": 1032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 843,
          "output_tokens": 1032,
          "cache_read_input_tokens": 44101,
          "cache_creation_input_tokens": 1438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1438
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

_source line 37 · 2026-05-10T07:43:56.696Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RkEJzGeKAZ6K5eNrDM86A7`</summary>

```json
{
  "query": "multi-pivot cross-lingual instruction tuning source language selection weighted DPO 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6afd7fa-dec6-436b-855c-651c80a29041",
  "isSidechain": false,
  "requestId": "req_011CatWkH6AqzEu48z2mWFD3",
  "type": "assistant",
  "uuid": "f12361e6-2c53-41d7-9062-8d5b02c6e081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LiCZHxQUuFJg7x7fsoPCm3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 843,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 44101,
      "output_tokens": 1032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 843,
          "output_tokens": 1032,
          "cache_read_input_tokens": 44101,
          "cache_creation_input_tokens": 1438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1438
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

_source line 38 · 2026-05-10T07:44:03.123Z_

<details><summary>↩ Tool result · `toolu_01VcQe4tMwztesbmKEZcktJQ`</summary>

```text
Web search results for query: "URIEL+ expansion arXiv 2510.27183 script vectors Glottolog genealogical 2025"

Links: [{"title":"[2510.27183] Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+","url":"https://arxiv.org/abs/2510.27183"},{"title":"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+","url":"https://arxiv.org/html/2510.27183"},{"title":"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/html/2510.19217"},{"title":"URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors - ACL Anthology","url":"https://aclanthology.org/E17-2002/"},{"title":"[Paper-NLP] URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors - Wenxin Hou","url":"https://houwx.net/posts/2020/01/blog-post-18/"},{"title":"(PDF) URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors","url":"https://www.researchgate.net/publication/318740987_URIEL_and_lang2vec_Representing_languages_as_typological_geographical_and_phylogenetic_vectors"},{"title":"[PDF] URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/URIEL-and-lang2vec:-Representing-languages-as-and-Levin-Littell/e3a824e59ac66ceaaa420e0de4f2b5d809231f6e"},{"title":"(PDF) URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors","url":"https://www.academia.edu/87901461/URIEL_and_lang2vec_Representing_languages_as_typological_geographical_and_phylogenetic_vectors"},{"title":"Less is More: The Effectiveness of Compact Typological Language Representations","url":"https://arxiv.org/html/2509.20129"},{"title":"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base","url":"https://arxiv.org/html/2409.18472v3"}]

I found the paper! Here's what the search revealed about arXiv 2510.27183:

## Paper Summary

The URIEL+ linguistic knowledge base supports multilingual research by encoding languages through geographic, genetic, and typological vectors. However, data sparsity (e.g. missing feature types, incomplete language entries, and limited genealogical coverage) remains prevalent.

## Key Expansions

The paper addresses these limitations through three main improvements:

1. **Script Vectors**: Script vectors are introduced to represent writing system properties for 7,488 languages

2. **Glottolog Integration**: Glottolog is integrated to add 18,710 additional languages

3. **Genealogical Expansion**: Lineage imputation is expanded for 26,449 languages by propagating typological and script features across genealogies

## Impact

These improvements reduce feature sparsity by 14% for script vectors, increase language coverage by up to 19,015 languages (1,007%), and boost imputation quality metrics by up to 35%.

The paper (titled "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+") was published on March 18, 2026, and demonstrates how genealogically-informed feature propagation can substantially improve linguistic knowledge base coverage, particularly for low-resource languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6afd7fa-dec6-436b-855c-651c80a29041",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "11442ae7-2e8f-4681-9f5c-dad9b7b8c3b1",
  "toolUseResult": {
    "query": "URIEL+ expansion arXiv 2510.27183 script vectors Glottolog genealogical 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_012exfURi2hsqMWDuf8amwhk",
        "content": [
          {
            "title": "[2510.27183] Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+",
            "url": "https://arxiv.org/abs/2510.27183"
          },
          {
            "title": "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+",
            "url": "https://arxiv.org/html/2510.27183"
          },
          {
            "title": "Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+",
            "url": "https://arxiv.org/html/2510.19217"
          },
          {
            "title": "URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors - ACL Anthology",
            "url": "https://aclanthology.org/E17-2002/"
          },
          {
            "title": "[Paper-NLP] URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors - Wenxin Hou",
            "url": "https://houwx.net/posts/2020/01/blog-post-18/"
          },
          {
            "title": "(PDF) URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors",
            "url": "https://www.researchgate.net/publication/318740987_URIEL_and_lang2vec_Representing_languages_as_typological_geographical_and_phylogenetic_vectors"
          },
          {
            "title": "[PDF] URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/URIEL-and-lang2vec:-Representing-languages-as-and-Levin-Littell/e3a824e59ac66ceaaa420e0de4f2b5d809231f6e"
          },
          {
            "title": "(PDF) URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors",
            "url": "https://www.academia.edu/87901461/URIEL_and_lang2vec_Representing_languages_as_typological_geographical_and_phylogenetic_vectors"
          },
          {
            "title": "Less is More: The Effectiveness of Compact Typological Language Representations",
            "url": "https://arxiv.org/html/2509.20129"
          },
          {
            "title": "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base",
            "url": "https://arxiv.org/html/2409.18472v3"
          }
        ]
      },
      "I found the paper! Here's what the search revealed about arXiv 2510.27183:\n\n## Paper Summary\n\nThe URIEL+ linguistic knowledge base supports multilingual research by encoding languages through geographic, genetic, and typological vectors. However, data sparsity (e.g. missing feature types, incomplete language entries, and limited genealogical coverage) remains prevalent.\n\n## Key Expansions\n\nThe paper addresses these limitations through three main improvements:\n\n1. **Script Vectors**: Script vectors are introduced to represent writing system properties for 7,488 languages\n\n2. **Glottolog Integration**: Glottolog is integrated to add 18,710 additional languages\n\n3. **Genealogical Expansion**: Lineage imputation is expanded for 26,449 languages by propagating typological and script features across genealogies\n\n## Impact\n\nThese improvements reduce feature sparsity by 14% for script vectors, increase language coverage by up to 19,015 languages (1,007%), and boost imputation quality metrics by up to 35%.\n\nThe paper (titled \"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+\") was published on March 18, 2026, and demonstrates how genealogically-informed feature propagation can substantially improve linguistic knowledge base coverage, particularly for low-resource languages."
    ],
    "durationSeconds": 6.430133081000007
  },
  "sourceToolAssistantUUID": "c6afd7fa-dec6-436b-855c-651c80a29041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "11442ae7-2e8f-4681-9f5c-dad9b7b8c3b1",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-pivot curriculum instruction tuning for agglutinative languages",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Tool result

_source line 41 · 2026-05-10T07:44:04.905Z_

<details><summary>↩ Tool result · `toolu_01RkEJzGeKAZ6K5eNrDM86A7`</summary>

```text
Web search results for query: "multi-pivot cross-lingual instruction tuning source language selection weighted DPO 2025 2026"

Links: [{"title":"[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/abs/2311.08711"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10517622-plug-leveraging-pivot-language-cross-lingual-instruction-tuning"},{"title":"GitHub - ytyz1307zzh/PLUG: Code for the ACL 2024 paper \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning\"","url":"https://github.com/ytyz1307zzh/PLUG"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning | Request PDF","url":"https://www.researchgate.net/publication/384213466_PLUG_Leveraging_Pivot_Language_in_Cross-Lingual_Instruction_Tuning"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.379/"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231108711Z/abstract"},{"title":"Leveraging Pivot Language in Cross-Lingual Instruction ...","url":"https://aclanthology.org/2024.acl-long.379.pdf"},{"title":"[2503.04647] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://arxiv.org/abs/2503.04647"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854"},{"title":"Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"}]

Based on the web search results, I found several relevant research papers related to cross-lingual instruction tuning and DPO (Direct Preference Optimization):

## Key Research Findings:

### 1. **PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (2024)**
PLUG proposes an approach that utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages. It trains the model to first process instructions in the pivot language, and then produce responses in the target language. The approach introduces X-AlpacaEval, a benchmark of instructions in 4 languages (Chinese, Korean, Italian, and Spanish), each annotated by professional translators.

### 2. **Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment (2025)**
This recent paper (March 2025) directly addresses weighted DPO for cross-lingual scenarios. The approach captures learned preferences from well-aligned English models by implicit rewards and transfers them to other languages through iterative training. Specifically, it derives an implicit reward model from the logits of an English DPO-aligned model and its corresponding reference model, which is then leveraged to annotate preference relations in cross-lingual instruction-following pairs, using English instructions to evaluate multilingual responses. Fine-tuning Llama3 for two iterations resulted in a 12.72% average improvement in Win Rate and a 5.97% increase in Length Control Win Rate across all training languages on the X-AlpacaEval leaderboard.

### 3. **Source Language Selection in Multilingual Instruction Tuning**
Research shows that capable multilingual instruction-following models can be tuned even with a minimal amount of multilingual data, and only 40 multilingual examples integrated in an English tuning set substantially improve multilingual instruction-following.

These papers represent recent advances in multi-pivot cross-lingual approaches with preference optimization methods from 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f12361e6-2c53-41d7-9062-8d5b02c6e081",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "f3fec2a5-0bb9-4543-b61f-1cc0228d5bfa",
  "toolUseResult": {
    "query": "multi-pivot cross-lingual instruction tuning source language selection weighted DPO 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VAQjxejZGc16ePxSVRSom4",
        "content": [
          {
            "title": "[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning",
            "url": "https://arxiv.org/abs/2311.08711"
          },
          {
            "title": "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning | NSF Public Access Repository",
            "url": "https://par.nsf.gov/biblio/10517622-plug-leveraging-pivot-language-cross-lingual-instruction-tuning"
          },
          {
            "title": "GitHub - ytyz1307zzh/PLUG: Code for the ACL 2024 paper \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning\"",
            "url": "https://github.com/ytyz1307zzh/PLUG"
          },
          {
            "title": "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning | Request PDF",
            "url": "https://www.researchgate.net/publication/384213466_PLUG_Leveraging_Pivot_Language_in_Cross-Lingual_Instruction_Tuning"
          },
          {
            "title": "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning - ACL Anthology",
            "url": "https://aclanthology.org/2024.acl-long.379/"
          },
          {
            "title": "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv231108711Z/abstract"
          },
          {
            "title": "Leveraging Pivot Language in Cross-Lingual Instruction ...",
            "url": "https://aclanthology.org/2024.acl-long.379.pdf"
          },
          {
            "title": "[2503.04647] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment",
            "url": "https://arxiv.org/abs/2503.04647"
          },
          {
            "title": "Multilingual Instruction Tuning With Just a Pinch of Multilinguality",
            "url": "https://arxiv.org/html/2401.01854"
          },
          {
            "title": "Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"
          }
        ]
      },
      "Based on the web search results, I found several relevant research papers related to cross-lingual instruction tuning and DPO (Direct Preference Optimization):\n\n## Key Research Findings:\n\n### 1. **PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (2024)**\nPLUG proposes an approach that utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages. It trains the model to first process instructions in the pivot language, and then produce responses in the target language. The approach introduces X-AlpacaEval, a benchmark of instructions in 4 languages (Chinese, Korean, Italian, and Spanish), each annotated by professional translators.\n\n### 2. **Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment (2025)**\nThis recent paper (March 2025) directly addresses weighted DPO for cross-lingual scenarios. The approach captures learned preferences from well-aligned English models by implicit rewards and transfers them to other languages through iterative training. Specifically, it derives an implicit reward model from the logits of an English DPO-aligned model and its corresponding reference model, which is then leveraged to annotate preference relations in cross-lingual instruction-following pairs, using English instructions to evaluate multilingual responses. Fine-tuning Llama3 for two iterations resulted in a 12.72% average improvement in Win Rate and a 5.97% increase in Length Control Win Rate across all training languages on the X-AlpacaEval leaderboard.\n\n### 3. **Source Language Selection in Multilingual Instruction Tuning**\nResearch shows that capable multilingual instruction-following models can be tuned even with a minimal amount of multilingual data, and only 40 multilingual examples integrated in an English tuning set substantially improve multilingual instruction-following.\n\nThese papers represent recent advances in multi-pivot cross-lingual approaches with preference optimization methods from 2024-2025."
    ],
    "durationSeconds": 8.206922044999999
  },
  "sourceToolAssistantUUID": "f12361e6-2c53-41d7-9062-8d5b02c6e081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T07:44:13.894Z_

<details><summary>Logged reasoning block</summary>

```text
Good. I now have a comprehensive picture. Let me also check whether the "Rethinking what Matters" paper (arXiv:2511.06497) is relevant to TWMP.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3fec2a5-0bb9-4543-b61f-1cc0228d5bfa",
  "isSidechain": false,
  "requestId": "req_011CatWnr5rAXDM8RpkV8WQk",
  "type": "assistant",
  "uuid": "75a7f6ab-11ff-4245-ad34-f312ec6dfaa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JVrHg6bg1J43ymY2SmNmRo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3968,
      "cache_read_input_tokens": 45539,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3968,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 45539,
          "cache_creation_input_tokens": 3968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3968
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

_source line 43 · 2026-05-10T07:44:14.771Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G5htgArEeHhcHXbTC3v4Xg`</summary>

```json
{
  "query": "arXiv 2511.06497 rethinking multilingual realignment low-resource languages 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75a7f6ab-11ff-4245-ad34-f312ec6dfaa5",
  "isSidechain": false,
  "requestId": "req_011CatWnr5rAXDM8RpkV8WQk",
  "type": "assistant",
  "uuid": "a9cce7c7-c3c5-44c6-b9c2-d395d4d89bac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JVrHg6bg1J43ymY2SmNmRo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3968,
      "cache_read_input_tokens": 45539,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3968,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 45539,
          "cache_creation_input_tokens": 3968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3968
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

_source line 44 · 2026-05-10T07:44:15.992Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LRmr5kbjpriZpJhipD51S5`</summary>

```json
{
  "query": "Foroutan 2510.25947 curriculum multilingual staged training negative interference findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9cce7c7-c3c5-44c6-b9c2-d395d4d89bac",
  "isSidechain": false,
  "requestId": "req_011CatWnr5rAXDM8RpkV8WQk",
  "type": "assistant",
  "uuid": "46304bed-0ce2-4c44-b9ab-4c000efaaa72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JVrHg6bg1J43ymY2SmNmRo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3968,
      "cache_read_input_tokens": 45539,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3968,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 45539,
          "cache_creation_input_tokens": 3968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3968
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

_source line 45 · 2026-05-10T07:44:20.878Z_

<details><summary>↩ Tool result · `toolu_01G5htgArEeHhcHXbTC3v4Xg`</summary>

```text
Web search results for query: "arXiv 2511.06497 rethinking multilingual realignment low-resource languages 2025"

Links: [{"title":"[2511.06497] Rethinking what Matters: Effective and Robust Multilingual Realignment for Low-Resource Languages","url":"https://arxiv.org/abs/2511.06497"},{"title":"Rethinking what Matters: Effective and Robust Multilingual Realignment for Low-Resource Languages","url":"https://arxiv.org/html/2511.06497"},{"title":"How Does Alignment Enhance LLMs’ Multilingual Capabilities? A Language Neurons Perspective","url":"https://arxiv.org/html/2505.21505"},{"title":"Aligning Large Language Models to Low-Resource Languages through LLM-Based Selective Translation: A Systematic Study","url":"https://arxiv.org/html/2507.14304v1"},{"title":"[2602.16660v1] Align Once, Benefit Multilingually: Enforcing Multilingual Consistency for LLM Safety Alignment","url":"https://arxiv.org/abs/2602.16660v1"},{"title":"Targeted Multilingual Adaptation for Low-resource Language Families","url":"https://arxiv.org/html/2405.12413v1"},{"title":"[2507.14304] Aligning Large Language Models to Low-Resource Languages through LLM-Based Selective Translation: A Systematic Study","url":"https://arxiv.org/abs/2507.14304"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"[2410.14815] Adapting Multilingual LLMs to Low-Resource Languages using Continued Pre-training and Synthetic Corpus","url":"https://arxiv.org/abs/2410.14815"},{"title":"Understanding Cross-Lingual Alignment—A Survey","url":"https://arxiv.org/html/2404.06228v2"}]

Based on the search results, I found the paper you're looking for:

**Paper Details:**

arXiv paper 2511.06497, titled "Rethinking what Matters: Effective and Robust Multilingual Realignment for Low-Resource Languages," was submitted on November 9, 2025, by authors Quang Phuoc Nguyen, David Anugraha, Felix Gaschi, Jun Bin Cheng, and En-Shiun Annie Lee.

**Abstract Summary:**

The paper addresses how realignment is a promising strategy to improve cross-lingual transfer in multilingual language models, but empirical results are mixed and often unreliable, particularly for typologically distant or low-resource languages compared to English.

Additionally, word realignment tools often rely on high-quality parallel data, which can be scarce or noisy for many low-resource languages.

The authors conduct an extensive empirical study to investigate whether realignment truly benefits from using all available languages, or if strategically selected subsets can offer comparable or even improved cross-lingual transfer.

Their key finding indicates that effective realignment does not require exhaustive language coverage and can reduce data collection overhead, while remaining both efficient and robust when guided by informed language selection.

The paper is available on arXiv at https://arxiv.org/abs/2511.06497


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9cce7c7-c3c5-44c6-b9c2-d395d4d89bac",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "feda14d8-6988-494a-ba48-f6967a8b668e",
  "toolUseResult": {
    "query": "arXiv 2511.06497 rethinking multilingual realignment low-resource languages 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FV8H9Atf1YxSq1AcsWHXfQ",
        "content": [
          {
            "title": "[2511.06497] Rethinking what Matters: Effective and Robust Multilingual Realignment for Low-Resource Languages",
            "url": "https://arxiv.org/abs/2511.06497"
          },
          {
            "title": "Rethinking what Matters: Effective and Robust Multilingual Realignment for Low-Resource Languages",
            "url": "https://arxiv.org/html/2511.06497"
          },
          {
            "title": "How Does Alignment Enhance LLMs’ Multilingual Capabilities? A Language Neurons Perspective",
            "url": "https://arxiv.org/html/2505.21505"
          },
          {
            "title": "Aligning Large Language Models to Low-Resource Languages through LLM-Based Selective Translation: A Systematic Study",
            "url": "https://arxiv.org/html/2507.14304v1"
          },
          {
            "title": "[2602.16660v1] Align Once, Benefit Multilingually: Enforcing Multilingual Consistency for LLM Safety Alignment",
            "url": "https://arxiv.org/abs/2602.16660v1"
          },
          {
            "title": "Targeted Multilingual Adaptation for Low-resource Language Families",
            "url": "https://arxiv.org/html/2405.12413v1"
          },
          {
            "title": "[2507.14304] Aligning Large Language Models to Low-Resource Languages through LLM-Based Selective Translation: A Systematic Study",
            "url": "https://arxiv.org/abs/2507.14304"
          },
          {
            "title": "Revisiting Multilingual Data Mixtures in Language Model Pretraining",
            "url": "https://arxiv.org/html/2510.25947v1"
          },
          {
            "title": "[2410.14815] Adapting Multilingual LLMs to Low-Resource Languages using Continued Pre-training and Synthetic Corpus",
            "url": "https://arxiv.org/abs/2410.14815"
          },
          {
            "title": "Understanding Cross-Lingual Alignment—A Survey",
            "url": "https://arxiv.org/html/2404.06228v2"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Paper Details:**\n\narXiv paper 2511.06497, titled \"Rethinking what Matters: Effective and Robust Multilingual Realignment for Low-Resource Languages,\" was submitted on November 9, 2025, by authors Quang Phuoc Nguyen, David Anugraha, Felix Gaschi, Jun Bin Cheng, and En-Shiun Annie Lee.\n\n**Abstract Summary:**\n\nThe paper addresses how realignment is a promising strategy to improve cross-lingual transfer in multilingual language models, but empirical results are mixed and often unreliable, particularly for typologically distant or low-resource languages compared to English.\n\nAdditionally, word realignment tools often rely on high-quality parallel data, which can be scarce or noisy for many low-resource languages.\n\nThe authors conduct an extensive empirical study to investigate whether realignment truly benefits from using all available languages, or if strategically selected subsets can offer comparable or even improved cross-lingual transfer.\n\nTheir key finding indicates that effective realignment does not require exhaustive language coverage and can reduce data collection overhead, while remaining both efficient and robust when guided by informed language selection.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2511.06497"
    ],
    "durationSeconds": 6.103910287000006
  },
  "sourceToolAssistantUUID": "a9cce7c7-c3c5-44c6-b9c2-d395d4d89bac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-10T07:44:21.440Z_

<details><summary>↩ Tool result · `toolu_01LRmr5kbjpriZpJhipD51S5`</summary>

```text
Web search results for query: "Foroutan 2510.25947 curriculum multilingual staged training negative interference findings"

Links: [{"title":"[2510.25947] Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/abs/2510.25947"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947"},{"title":"mmBERT: Advanced Multilingual Encoder Model","url":"https://www.emergentmind.com/topics/mmbert"},{"title":"[2510.10159] BabyBabelLM: A Multilingual Benchmark of Developmentally Plausible Training Data","url":"https://arxiv.org/abs/2510.10159"},{"title":"Instructing and Assessing Multilingual Learners (IAML)","url":"https://www.theptc.org/eal-iamll"},{"title":"[2506.15304] ConLID: Supervised Contrastive Learning for Low-Resource Language Identification","url":"https://arxiv.org/abs/2506.15304"},{"title":"Full article: Teaching modern foreign languages in multilingual classrooms: an examination of Key Stage 2 teachers’ experiences","url":"https://www.tandfonline.com/doi/full/10.1080/09571736.2018.1448432"},{"title":"Multilingual Education Program | Academics/Curriculum","url":"https://www.fcps.org/academics/mep"},{"title":"Multilingual Education - Mastery Schools","url":"https://masterycharter.org/multilingual-education"},{"title":"Enhancing Access to Workforce Training: A Guide to Supporting Multilingual Learners’ Participation in Integrated Education and Training | Adult Education and Literacy | U.S. Department of Education","url":"https://lincs.ed.gov/professional-development/resource-collections/profile-9521"}]

I found the paper! The study titled "Revisiting Multilingual Data Mixtures in Language Model Pretraining" by Negar Foroutan and colleagues investigates the impact of different multilingual data mixtures in pretraining large language models, addressing concerns about trade-offs between language coverage and model performance (the curse of multilinguality).

The researchers trained 1.1B and 3B parameter LLMs on diverse multilingual corpora, varying the number of languages from 25 to 400.

Regarding your specific query about "negative interference findings," the search results show that the study found that combining English and multilingual data does not necessarily degrade the in-language performance of either group, provided that languages have a sufficient number of tokens included in the pretraining corpus. This suggests the research challenges assumptions about negative interference between languages during multilingual training. Additionally, the study observes that using English as a pivot language yields benefits across language families.

The paper was submitted on October 29, 2025, and is available on arXiv as document 2510.25947.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46304bed-0ce2-4c44-b9ab-4c000efaaa72",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "ccf1a339-9d1b-44d3-8c4f-16cf3e232d2d",
  "toolUseResult": {
    "query": "Foroutan 2510.25947 curriculum multilingual staged training negative interference findings",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TRjFoQYy4NB4he3tKzcqeP",
        "content": [
          {
            "title": "[2510.25947] Revisiting Multilingual Data Mixtures in Language Model Pretraining",
            "url": "https://arxiv.org/abs/2510.25947"
          },
          {
            "title": "Revisiting Multilingual Data Mixtures in Language Model Pretraining",
            "url": "https://arxiv.org/html/2510.25947"
          },
          {
            "title": "mmBERT: Advanced Multilingual Encoder Model",
            "url": "https://www.emergentmind.com/topics/mmbert"
          },
          {
            "title": "[2510.10159] BabyBabelLM: A Multilingual Benchmark of Developmentally Plausible Training Data",
            "url": "https://arxiv.org/abs/2510.10159"
          },
          {
            "title": "Instructing and Assessing Multilingual Learners (IAML)",
            "url": "https://www.theptc.org/eal-iamll"
          },
          {
            "title": "[2506.15304] ConLID: Supervised Contrastive Learning for Low-Resource Language Identification",
            "url": "https://arxiv.org/abs/2506.15304"
          },
          {
            "title": "Full article: Teaching modern foreign languages in multilingual classrooms: an examination of Key Stage 2 teachers’ experiences",
            "url": "https://www.tandfonline.com/doi/full/10.1080/09571736.2018.1448432"
          },
          {
            "title": "Multilingual Education Program | Academics/Curriculum",
            "url": "https://www.fcps.org/academics/mep"
          },
          {
            "title": "Multilingual Education - Mastery Schools",
            "url": "https://masterycharter.org/multilingual-education"
          },
          {
            "title": "Enhancing Access to Workforce Training: A Guide to Supporting Multilingual Learners’ Participation in Integrated Education and Training | Adult Education and Literacy | U.S. Department of Education",
            "url": "https://lincs.ed.gov/professional-development/resource-collections/profile-9521"
          }
        ]
      },
      "I found the paper! The study titled \"Revisiting Multilingual Data Mixtures in Language Model Pretraining\" by Negar Foroutan and colleagues investigates the impact of different multilingual data mixtures in pretraining large language models, addressing concerns about trade-offs between language coverage and model performance (the curse of multilinguality).\n\nThe researchers trained 1.1B and 3B parameter LLMs on diverse multilingual corpora, varying the number of languages from 25 to 400.\n\nRegarding your specific query about \"negative interference findings,\" the search results show that the study found that combining English and multilingual data does not necessarily degrade the in-language performance of either group, provided that languages have a sufficient number of tokens included in the pretraining corpus. This suggests the research challenges assumptions about negative interference between languages during multilingual training. Additionally, the study observes that using English as a pivot language yields benefits across language families.\n\nThe paper was submitted on October 29, 2025, and is available on arXiv as document 2510.25947."
    ],
    "durationSeconds": 5.375253606000013
  },
  "sourceToolAssistantUUID": "46304bed-0ce2-4c44-b9ab-4c000efaaa72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-10T07:44:30.218Z_

<details><summary>Logged reasoning block</summary>

```text
Interesting! The search summary says the Foroutan et al. paper actually found that "combining English and multilingual data does not necessarily degrade in-language performance" and that "English as a pivot yields benefits across language families." This is somewhat different from what the Round 5 review said - Round 5 said Foroutan et al. showed that "staged curriculum learning does not reduce negative interference" and "temperature-based language reweighting hurts performance due to noise."

Let me check the actual paper to get the real findings. But actually, looking at the OpenReview link for this paper: it's "under review." The key question is what the paper actually says about curriculum and reweighting.


The Round 5 reviewer's claims about curriculum learning and reweighting don't seem to match what the search results describe about the paper's actual findings on combining English and multilingual data. I need to look at the paper's abstract directly to see what it really concludes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccf1a339-9d1b-44d3-8c4f-16cf3e232d2d",
  "isSidechain": false,
  "requestId": "req_011CatWp4cCHfEQSuuRasyLZ",
  "type": "assistant",
  "uuid": "9bb91881-6d7d-4642-98fd-78310e571d1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L3FfujyA2BZW3AMHwBpHRX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1803,
      "cache_read_input_tokens": 49507,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 49507,
          "cache_creation_input_tokens": 1803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1803
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

_source line 48 · 2026-05-10T07:44:30.823Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015mmfCkpscvjN11KeX9e9E1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.25947",
  "prompt": "What are the key findings about staged curriculum learning and temperature-based language reweighting? Does the paper show that curriculum learning does not help, or that language reweighting hurts performance? Summarize the main claims relevant to multilingual instruction tuning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bb91881-6d7d-4642-98fd-78310e571d1f",
  "isSidechain": false,
  "requestId": "req_011CatWp4cCHfEQSuuRasyLZ",
  "type": "assistant",
  "uuid": "1d9e5fed-37ce-4bd1-bb09-413fecfa0f7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L3FfujyA2BZW3AMHwBpHRX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1803,
      "cache_read_input_tokens": 49507,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 49507,
          "cache_creation_input_tokens": 1803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1803
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

_source line 49 · 2026-05-10T07:44:31.408Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01USR6HHDMdZK3F9Gk7GgLid`</summary>

```json
{
  "query": "cross-lingual instruction tuning Turkic agglutinative languages 2026 arXiv new competing work"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d9e5fed-37ce-4bd1-bb09-413fecfa0f7d",
  "isSidechain": false,
  "requestId": "req_011CatWp4cCHfEQSuuRasyLZ",
  "type": "assistant",
  "uuid": "dc53dbe3-5079-40cd-be55-4edf7171c587",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L3FfujyA2BZW3AMHwBpHRX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1803,
      "cache_read_input_tokens": 49507,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 49507,
          "cache_creation_input_tokens": 1803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1803
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
  "leafUuid": "dc53dbe3-5079-40cd-be55-4edf7171c587",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-pivot curriculum instruction tuning for agglutinative languages",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Tool result

_source line 52 · 2026-05-10T07:44:39.670Z_

<details><summary>↩ Tool result · `toolu_01USR6HHDMdZK3F9Gk7GgLid`</summary>

```text
Web search results for query: "cross-lingual instruction tuning Turkic agglutinative languages 2026 arXiv new competing work"

Links: [{"title":"Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/html/2604.06202"},{"title":"[2604.06202] Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/abs/2604.06202"},{"title":"TurkicNLP: An NLP Toolkit for Turkic Languages","url":"https://arxiv.org/html/2602.19174"},{"title":"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models","url":"https://arxiv.org/html/2603.21036"},{"title":"Multilingual end-to-end ASR for low-resource Turkic languages with common alphabets | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-64848-1"},{"title":"Proceedings of the Second Workshop Natural Language Processing for Turkic Languages (SIGTURK 2026) - ACL Anthology","url":"https://aclanthology.org/volumes/2026.sigturk-1/"},{"title":"Morphology-Aware Segmentation and Tokenization for Turkic Languages: A CSE-Guided Framework (The Kazakh Case)","url":"https://www.mdpi.com/2078-2489/17/2/128"},{"title":"Recent Advancements and Challenges of Turkic Central Asian Language Processing","url":"https://arxiv.org/html/2407.05006"},{"title":"[2604.11096] Efficient Training for Cross-lingual Speech Language Models","url":"https://arxiv.org/abs/2604.11096"},{"title":"Diffutron: A Masked Diffusion Language Model for Turkish Language","url":"https://arxiv.org/html/2603.20466"}]

Based on the search results, I found several relevant papers from 2026 on arXiv addressing cross-lingual work with Turkic and agglutinative languages:

## Primary Finding

A theoretical framework paper proposes studying cross-lingual transfer and parameter-efficient adaptation of multilingual LLMs within the Turkic language family, focusing on Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz. The paper integrates insights from multilingual representation learning and parameter-efficient fine-tuning techniques such as Low-Rank Adaptation (LoRA), and introduces the Turkic Transfer Coefficient (TTC), a theoretical measure incorporating morphological similarity, lexical overlap, syntactic structure, and script compatibility across Turkic languages. This paper (arXiv:2604.06202) was published in March 2026.

## Competing/Related Work

Several competing or related works from early 2026 include:

1. **TurkicNLP Toolkit** (arXiv:2602.19174, March 2026): Addresses the shared typological features of Turkic languages such as agglutinative morphology, vowel harmony, and subject-object-verb (SOV) word order.

2. **Cross-Lingual Transfer Assessment** (arXiv:2603.21036, March 2026): Notes that Turkic and Mongolic languages remain particularly underexplored despite their typological diversity—agglutinative morphology, Cyrillic and Latin script variation, and rich cultural traditions.

3. **Diffutron for Turkish** (arXiv:2603.20466, March 2026): A lightweight and parameter-efficient masked diffusion language model specifically tailored for Turkish.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc53dbe3-5079-40cd-be55-4edf7171c587",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "8e2f77ab-74a6-49fe-9cfe-e0fd0210a8bb",
  "toolUseResult": {
    "query": "cross-lingual instruction tuning Turkic agglutinative languages 2026 arXiv new competing work",
    "results": [
      {
        "tool_use_id": "srvtoolu_013yoD6wFwyVnL8CPfpTxwbB",
        "content": [
          {
            "title": "Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models",
            "url": "https://arxiv.org/html/2604.06202"
          },
          {
            "title": "[2604.06202] Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models",
            "url": "https://arxiv.org/abs/2604.06202"
          },
          {
            "title": "TurkicNLP: An NLP Toolkit for Turkic Languages",
            "url": "https://arxiv.org/html/2602.19174"
          },
          {
            "title": "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models",
            "url": "https://arxiv.org/html/2603.21036"
          },
          {
            "title": "Multilingual end-to-end ASR for low-resource Turkic languages with common alphabets | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-024-64848-1"
          },
          {
            "title": "Proceedings of the Second Workshop Natural Language Processing for Turkic Languages (SIGTURK 2026) - ACL Anthology",
            "url": "https://aclanthology.org/volumes/2026.sigturk-1/"
          },
          {
            "title": "Morphology-Aware Segmentation and Tokenization for Turkic Languages: A CSE-Guided Framework (The Kazakh Case)",
            "url": "https://www.mdpi.com/2078-2489/17/2/128"
          },
          {
            "title": "Recent Advancements and Challenges of Turkic Central Asian Language Processing",
            "url": "https://arxiv.org/html/2407.05006"
          },
          {
            "title": "[2604.11096] Efficient Training for Cross-lingual Speech Language Models",
            "url": "https://arxiv.org/abs/2604.11096"
          },
          {
            "title": "Diffutron: A Masked Diffusion Language Model for Turkish Language",
            "url": "https://arxiv.org/html/2603.20466"
          }
        ]
      },
      "Based on the search results, I found several relevant papers from 2026 on arXiv addressing cross-lingual work with Turkic and agglutinative languages:\n\n## Primary Finding\n\nA theoretical framework paper proposes studying cross-lingual transfer and parameter-efficient adaptation of multilingual LLMs within the Turkic language family, focusing on Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz. The paper integrates insights from multilingual representation learning and parameter-efficient fine-tuning techniques such as Low-Rank Adaptation (LoRA), and introduces the Turkic Transfer Coefficient (TTC), a theoretical measure incorporating morphological similarity, lexical overlap, syntactic structure, and script compatibility across Turkic languages. This paper (arXiv:2604.06202) was published in March 2026.\n\n## Competing/Related Work\n\nSeveral competing or related works from early 2026 include:\n\n1. **TurkicNLP Toolkit** (arXiv:2602.19174, March 2026): Addresses the shared typological features of Turkic languages such as agglutinative morphology, vowel harmony, and subject-object-verb (SOV) word order.\n\n2. **Cross-Lingual Transfer Assessment** (arXiv:2603.21036, March 2026): Notes that Turkic and Mongolic languages remain particularly underexplored despite their typological diversity—agglutinative morphology, Cyrillic and Latin script variation, and rich cultural traditions.\n\n3. **Diffutron for Turkish** (arXiv:2603.20466, March 2026): A lightweight and parameter-efficient masked diffusion language model specifically tailored for Turkish."
    ],
    "durationSeconds": 8.258845686000015
  },
  "sourceToolAssistantUUID": "dc53dbe3-5079-40cd-be55-4edf7171c587",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-10T07:44:43.004Z_

<details><summary>↩ Tool result · `toolu_015mmfCkpscvjN11KeX9e9E1`</summary>

```text
# Response

Based on the provided arXiv page content, I cannot address your specific questions about staged curriculum learning, temperature-based language reweighting, or multilingual instruction tuning.

The page displays only the abstract and metadata for the paper "Revisiting Multilingual Data Mixtures in Language Model Pretraining." The abstract focuses on findings about multilingual data mixtures during pretraining—specifically that combining English with multilingual data doesn't necessarily hurt performance, that English can serve effectively as a pivot language, and that increased language count doesn't produce a significant "curse of multilinguality."

However, your questions reference findings about curriculum learning and language reweighting strategies, which are not mentioned in the abstract. The full paper content would be needed to address those specific claims about instruction tuning approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d9e5fed-37ce-4bd1-bb09-413fecfa0f7d",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "f2fb0720-7d2c-41e8-a008-90f5c63969ab",
  "toolUseResult": {
    "bytes": 46842,
    "code": 200,
    "codeText": "OK",
    "result": "# Response\n\nBased on the provided arXiv page content, I cannot address your specific questions about staged curriculum learning, temperature-based language reweighting, or multilingual instruction tuning.\n\nThe page displays only the abstract and metadata for the paper \"Revisiting Multilingual Data Mixtures in Language Model Pretraining.\" The abstract focuses on findings about multilingual data mixtures during pretraining—specifically that combining English with multilingual data doesn't necessarily hurt performance, that English can serve effectively as a pivot language, and that increased language count doesn't produce a significant \"curse of multilinguality.\"\n\nHowever, your questions reference findings about curriculum learning and language reweighting strategies, which are not mentioned in the abstract. The full paper content would be needed to address those specific claims about instruction tuning approaches.",
    "durationMs": 12178,
    "url": "https://arxiv.org/abs/2510.25947"
  },
  "sourceToolAssistantUUID": "1d9e5fed-37ce-4bd1-bb09-413fecfa0f7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-10T07:44:49.752Z_

<details><summary>Logged reasoning block</summary>

```text
Very interesting! There's a new paper from March 2026: "Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models" (arXiv:2604.06202). This paper:

1. Studies cross-lingual transfer and parameter-efficient adaptation within the Turkic language family
2. Focuses on Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz (similar language targets to TWMP)


3. Builds on multilingual representation learning and LoRA techniques, introducing the Turkic Transfer Coefficient—a metric that measures morphological similarity, lexical overlap, syntactic structure, and script compatibility across these languages

This looks remarkably aligned with TWMP's approach, so I should pull the paper to see how closely their methodology matches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2fb0720-7d2c-41e8-a008-90f5c63969ab",
  "isSidechain": false,
  "requestId": "req_011CatWqeqWNCc7LohjsGTVN",
  "type": "assistant",
  "uuid": "187752bf-7696-494c-8c10-02ad504a062c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012MWAL9ki7D1a5udRYAbzQn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 958,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 51310,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 958,
          "output_tokens": 411,
          "cache_read_input_tokens": 51310,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 55 · 2026-05-10T07:44:50.641Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JuPqApyn56Uq1uXnXzg7UZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.06202",
  "prompt": "What is the main method proposed? Does it propose a training recipe or algorithm for cross-lingual transfer in Turkic languages? Does it use typological distance/similarity to weight or select pivot languages? Is it purely theoretical or does it include experiments? What are its contributions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "187752bf-7696-494c-8c10-02ad504a062c",
  "isSidechain": false,
  "requestId": "req_011CatWqeqWNCc7LohjsGTVN",
  "type": "assistant",
  "uuid": "072647c6-bb83-4520-a3b5-107b51b0172f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012MWAL9ki7D1a5udRYAbzQn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 958,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 51310,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 958,
          "output_tokens": 411,
          "cache_read_input_tokens": 51310,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 56 · 2026-05-10T07:44:51.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LgvBmEWgdFZLM5ucNyapdV`</summary>

```json
{
  "query": "weighted language sampling cross-lingual LoRA low-resource Kazakh Mongolian fine-tuning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "072647c6-bb83-4520-a3b5-107b51b0172f",
  "isSidechain": false,
  "requestId": "req_011CatWqeqWNCc7LohjsGTVN",
  "type": "assistant",
  "uuid": "e0e24734-bec0-44d9-951f-4c2df919c7c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012MWAL9ki7D1a5udRYAbzQn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 958,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 51310,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 958,
          "output_tokens": 411,
          "cache_read_input_tokens": 51310,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 57 · 2026-05-10T07:44:55.959Z_

<details><summary>↩ Tool result · `toolu_01JuPqApyn56Uq1uXnXzg7UZ`</summary>

```text
# Summary of the Paper

**Nature of Contribution:**
This appears to be a purely theoretical framework paper rather than one presenting concrete algorithms or training recipes. The abstract indicates it proposes "a theoretical framework for studying cross-lingual transfer and parameter-efficient adaptation" but doesn't describe implemented experiments.

**Main Method:**
The framework integrates "multilingual representation learning and parameter-efficient fine-tuning techniques such as Low-Rank Adaptation (LoRA)" to develop conceptual models. However, no specific algorithmic procedure is detailed in the available content.

**Use of Typological Similarity:**
Yes—the paper introduces the Turkic Transfer Coefficient (TTC), described as "a theoretical measure incorporating morphological similarity, lexical overlap, syntactic structure, and script compatibility across Turkic languages." This explicitly leverages typological distance to characterize transfer potential between related languages.

**Experimental Content:**
The submission notes "22 pages, no figures, 1 table," suggesting minimal empirical validation. The paper appears conceptual rather than experimental.

**Key Contributions:**
- A scaling model relating adaptation performance to model capacity, data size, and module expressivity
- The TTC metric for formalizing transfer potential among Turkic languages
- Identification of "structural limits of parameter-efficient adaptation in extremely low-resource scenarios"

The work targets five Turkic languages (Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz) but seems positioned as theoretical groundwork rather than a practical implementation guide.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "072647c6-bb83-4520-a3b5-107b51b0172f",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "e48caa53-f999-4a57-9ac4-e49a26e8570e",
  "toolUseResult": {
    "bytes": 46944,
    "code": 200,
    "codeText": "OK",
    "result": "# Summary of the Paper\n\n**Nature of Contribution:**\nThis appears to be a purely theoretical framework paper rather than one presenting concrete algorithms or training recipes. The abstract indicates it proposes \"a theoretical framework for studying cross-lingual transfer and parameter-efficient adaptation\" but doesn't describe implemented experiments.\n\n**Main Method:**\nThe framework integrates \"multilingual representation learning and parameter-efficient fine-tuning techniques such as Low-Rank Adaptation (LoRA)\" to develop conceptual models. However, no specific algorithmic procedure is detailed in the available content.\n\n**Use of Typological Similarity:**\nYes—the paper introduces the Turkic Transfer Coefficient (TTC), described as \"a theoretical measure incorporating morphological similarity, lexical overlap, syntactic structure, and script compatibility across Turkic languages.\" This explicitly leverages typological distance to characterize transfer potential between related languages.\n\n**Experimental Content:**\nThe submission notes \"22 pages, no figures, 1 table,\" suggesting minimal empirical validation. The paper appears conceptual rather than experimental.\n\n**Key Contributions:**\n- A scaling model relating adaptation performance to model capacity, data size, and module expressivity\n- The TTC metric for formalizing transfer potential among Turkic languages\n- Identification of \"structural limits of parameter-efficient adaptation in extremely low-resource scenarios\"\n\nThe work targets five Turkic languages (Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz) but seems positioned as theoretical groundwork rather than a practical implementation guide.",
    "durationMs": 5313,
    "url": "https://arxiv.org/abs/2604.06202"
  },
  "sourceToolAssistantUUID": "072647c6-bb83-4520-a3b5-107b51b0172f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T07:44:59.407Z_

<details><summary>↩ Tool result · `toolu_01LgvBmEWgdFZLM5ucNyapdV`</summary>

```text
Web search results for query: "weighted language sampling cross-lingual LoRA low-resource Kazakh Mongolian fine-tuning 2025 2026"

Links: [{"title":"Published in Transactions on Machine Learning Research (11/2025)","url":"https://openreview.net/pdf?id=oapsbIO1Bd"},{"title":"Final Report - Fine Tuning Methods for Low-resource Languages","url":"https://arxiv.org/html/2510.04139v1"},{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"Large and Small models for collaborative cross-lingual data augmentation in entity relationship extraction for low-resource languages | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-025-00055-w"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nZeVKeeFYf9"},{"title":"Efficient Fine-Tuning with LoRA: A Guide to Optimal Parameter Selection for Large Language Models","url":"https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms"},{"title":"Optimizing translation for low-resource languages: Efficient fine-tuning with custom prompt engineering in large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666827025000325"},{"title":"Fine-Tuning Large Language Models for Kazakh Text Simplification | MDPI","url":"https://www.mdpi.com/2076-3417/15/15/8344"},{"title":"Bhaasha, Bhāṣā, Zaban: A Survey for Low-Resourced Languages in South Asia – Current Stage and Challenges","url":"https://arxiv.org/html/2509.11570v1"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/html/2106.09685v2"}]

Based on the search results, I found several relevant papers and resources related to your query about weighted language sampling, cross-lingual LoRA, and low-resource language fine-tuning for Kazakh and Mongolian:

## Key Findings:

### COMPASS: Distribution-Guided Data Selection for Cross-Lingual LoRA
A recent paper (November 2025) presents COMPASS, a distribution-guided method that constructs judiciously selected training subsets for language-specific parameter-efficient fine-tuning (PEFT) modules, including LoRA adapters, to enhance cross-lingual transfer. The research posits that naively fine-tuning adapters on all available data is suboptimal.

### Kazakh Language Adaptation
A 2025 paper addresses text simplification for Kazakh, a morphologically rich, low-resource language, by introducing KazSim, an instruction-tuned model built on multilingual large language models. The research applies LoRA to all models, which introduces small trainable matrices into the attention and feed-forward layers of the transformer without modifying the original weights, allowing for efficient training of large models on limited hardware.

### Mongolian and Kazakh as Agglutinative Languages
Mongolian, Kazakh, Uyghur, and Hungarian are agglutinative languages that typically use suffixes or prefixes to convey grammatical functions, resulting in highly complex morphological variations. A collaborative cross-lingual data augmentation framework for entity relationship extraction named LS-CLDARE has been proposed to address challenges in low-resource language processing.

### General LoRA Overview
LoRA freezes pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, reducing trainable parameters by 10,000 times and GPU memory requirements by 3 times compared to fine-tuning GPT-3 175B.

These recent 2025-2026 sources demonstrate active research combining LoRA, cross-lingual approaches, and low-resource language adaptation, particularly for morphologically complex languages like Kazakh and Mongolian.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0e24734-bec0-44d9-951f-4c2df919c7c6",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "b5b5787a-d9d5-44af-a9c2-5d77ae48a94d",
  "toolUseResult": {
    "query": "weighted language sampling cross-lingual LoRA low-resource Kazakh Mongolian fine-tuning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016cnS8qTZzseUgTnSSe52EW",
        "content": [
          {
            "title": "Published in Transactions on Machine Learning Research (11/2025)",
            "url": "https://openreview.net/pdf?id=oapsbIO1Bd"
          },
          {
            "title": "Final Report - Fine Tuning Methods for Low-resource Languages",
            "url": "https://arxiv.org/html/2510.04139v1"
          },
          {
            "title": "[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models",
            "url": "https://arxiv.org/abs/2106.09685"
          },
          {
            "title": "Large and Small models for collaborative cross-lingual data augmentation in entity relationship extraction for low-resource languages | Journal of King Saud University Computer and Information Sciences | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s44443-025-00055-w"
          },
          {
            "title": "LoRA: Low-Rank Adaptation of Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=nZeVKeeFYf9"
          },
          {
            "title": "Efficient Fine-Tuning with LoRA: A Guide to Optimal Parameter Selection for Large Language Models",
            "url": "https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms"
          },
          {
            "title": "Optimizing translation for low-resource languages: Efficient fine-tuning with custom prompt engineering in large language models - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S2666827025000325"
          },
          {
            "title": "Fine-Tuning Large Language Models for Kazakh Text Simplification | MDPI",
            "url": "https://www.mdpi.com/2076-3417/15/15/8344"
          },
          {
            "title": "Bhaasha, Bhāṣā, Zaban: A Survey for Low-Resourced Languages in South Asia – Current Stage and Challenges",
            "url": "https://arxiv.org/html/2509.11570v1"
          },
          {
            "title": "LoRA: Low-Rank Adaptation of Large Language Models",
            "url": "https://arxiv.org/html/2106.09685v2"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and resources related to your query about weighted language sampling, cross-lingual LoRA, and low-resource language fine-tuning for Kazakh and Mongolian:\n\n## Key Findings:\n\n### COMPASS: Distribution-Guided Data Selection for Cross-Lingual LoRA\nA recent paper (November 2025) presents COMPASS, a distribution-guided method that constructs judiciously selected training subsets for language-specific parameter-efficient fine-tuning (PEFT) modules, including LoRA adapters, to enhance cross-lingual transfer. The research posits that naively fine-tuning adapters on all available data is suboptimal.\n\n### Kazakh Language Adaptation\nA 2025 paper addresses text simplification for Kazakh, a morphologically rich, low-resource language, by introducing KazSim, an instruction-tuned model built on multilingual large language models. The research applies LoRA to all models, which introduces small trainable matrices into the attention and feed-forward layers of the transformer without modifying the original weights, allowing for efficient training of large models on limited hardware.\n\n### Mongolian and Kazakh as Agglutinative Languages\nMongolian, Kazakh, Uyghur, and Hungarian are agglutinative languages that typically use suffixes or prefixes to convey grammatical functions, resulting in highly complex morphological variations. A collaborative cross-lingual data augmentation framework for entity relationship extraction named LS-CLDARE has been proposed to address challenges in low-resource language processing.\n\n### General LoRA Overview\nLoRA freezes pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, reducing trainable parameters by 10,000 times and GPU memory requirements by 3 times compared to fine-tuning GPT-3 175B.\n\nThese recent 2025-2026 sources demonstrate active research combining LoRA, cross-lingual approaches, and low-resource language adaptation, particularly for morphologically complex languages like Kazakh and Mongolian."
    ],
    "durationSeconds": 8.112738183000008
  },
  "sourceToolAssistantUUID": "e0e24734-bec0-44d9-951f-4c2df919c7c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-10T07:45:06.475Z_

<details><summary>Logged reasoning block</summary>

```text
Interesting - the paper on COMPASS (November 2025) is "a distribution-guided method that constructs judiciously selected training subsets for language-specific PEFT modules, including LoRA adapters, to enhance cross-lingual transfer." Let me search for this paper specifically.

Also, the theoretical framework paper (arXiv:2604.06202) on Turkic languages seems to be purely theoretical with no experiments (22 pages, no figures) - so it's not a direct empirical competitor to TWMP but could be cited.


I should look up the COMPASS paper directly to see what it actually proposes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5b5787a-d9d5-44af-a9c2-5d77ae48a94d",
  "isSidechain": false,
  "requestId": "req_011CatWrrxJByPp5XeJQGijQ",
  "type": "assistant",
  "uuid": "dc527ee7-44d8-43e8-b2d0-b8ea1baa6373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013r8EnekHyAQpW6UqCo2Egh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2797,
      "cache_read_input_tokens": 51988,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 51988,
          "cache_creation_input_tokens": 2797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2797
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

_source line 60 · 2026-05-10T07:45:06.516Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014sQEUqHk81FxQbZ8WmLKnm`</summary>

```json
{
  "query": "COMPASS distribution-guided data selection cross-lingual LoRA cross-lingual transfer TMLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc527ee7-44d8-43e8-b2d0-b8ea1baa6373",
  "isSidechain": false,
  "requestId": "req_011CatWrrxJByPp5XeJQGijQ",
  "type": "assistant",
  "uuid": "1ebb79c0-1bc4-44cb-8a51-6ed5017957b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013r8EnekHyAQpW6UqCo2Egh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2797,
      "cache_read_input_tokens": 51988,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 51988,
          "cache_creation_input_tokens": 2797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2797
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

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "1ebb79c0-1bc4-44cb-8a51-6ed5017957b3",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-pivot curriculum instruction tuning for agglutinative languages",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Tool result

_source line 63 · 2026-05-10T07:45:11.222Z_

<details><summary>↩ Tool result · `toolu_014sQEUqHk81FxQbZ8WmLKnm`</summary>

```text
Web search results for query: "COMPASS distribution-guided data selection cross-lingual LoRA cross-lingual transfer TMLR 2025"

Links: [{"title":"Cross-LoRA: A Data-Free LoRA Transfer Framework across Heterogeneous LLMs","url":"https://arxiv.org/html/2508.05232v1"},{"title":"GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer","url":"https://arxiv.org/html/2601.06702"},{"title":"Mixture of Experts in Large Language Models Danyang Zhang","url":"https://arxiv.org/pdf/2507.11181"},{"title":"A survey on LoRA of large language models | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40663-9"},{"title":"TreeLoRA: Efficient Continual Learning via Layer-Wise LoRAs","url":"https://www.lamda.nju.edu.cn/qianyy/paper/ICML25_TreeLoRA.pdf"},{"title":"Hierarchical-Task-Aware Multi-modal Mixture of ...","url":"https://aclanthology.org/2025.acl-long.1379.pdf"},{"title":"Adaptive LoRA Merge with Parameter Pruning for Low- ...","url":"https://aclanthology.org/2025.findings-acl.990.pdf"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Collaborative Multi-LoRA Experts with Achievement-based Multi-Tasks Loss for","url":"https://www.ijcai.org/proceedings/2025/0772.pdf"},{"title":"Dynamic Mixture of Curriculum LoRA Experts for Continual ...","url":"https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Dynamic%20Mixture%20of%20Curriculum%20LoRA%20Experts%20for%20Continual%20Multimodal%20Instruction%20Tuning.pdf"}]

Based on the search results, I found information about related work on cross-lingual transfer and LoRA methods, but I did not find a specific paper or resource that exactly matches the query you provided for "COMPASS distribution-guided data selection cross-lingual LoRA TMLR 2025." 

The search returned results about various LoRA-related papers from 2025, including:
- Cross-LoRA for LoRA transfer across heterogeneous LLMs
- GRASP LoRA for cross-lingual transfer with adapter sparsity
- Other LoRA variants for different applications

However, none of these appear to be the specific "COMPASS" paper with distribution-guided data selection that you're looking for, and none are identified as being published in TMLR (Transactions on Machine Learning Research) 2025.

Would you like me to:
1. Search with different keywords or a modified query?
2. Search for more recent TMLR 2025 publications?
3. Search for the paper by authors' names if you have them?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ebb79c0-1bc4-44cb-8a51-6ed5017957b3",
  "isSidechain": false,
  "promptId": "f3d9955d-1fe6-4f6f-a214-0eebfd89fb25",
  "type": "user",
  "uuid": "2ab60803-f816-4091-a1fb-6385c40d64b3",
  "toolUseResult": {
    "query": "COMPASS distribution-guided data selection cross-lingual LoRA cross-lingual transfer TMLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_016dwqHH7UxmywbGtCFL8DWo",
        "content": [
          {
            "title": "Cross-LoRA: A Data-Free LoRA Transfer Framework across Heterogeneous LLMs",
            "url": "https://arxiv.org/html/2508.05232v1"
          },
          {
            "title": "GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer",
            "url": "https://arxiv.org/html/2601.06702"
          },
          {
            "title": "Mixture of Experts in Large Language Models Danyang Zhang",
            "url": "https://arxiv.org/pdf/2507.11181"
          },
          {
            "title": "A survey on LoRA of large language models | Frontiers of Computer Science | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11704-024-40663-9"
          },
          {
            "title": "TreeLoRA: Efficient Continual Learning via Layer-Wise LoRAs",
            "url": "https://www.lamda.nju.edu.cn/qianyy/paper/ICML25_TreeLoRA.pdf"
          },
          {
            "title": "Hierarchical-Task-Aware Multi-modal Mixture of ...",
            "url": "https://aclanthology.org/2025.acl-long.1379.pdf"
          },
          {
            "title": "Adaptive LoRA Merge with Parameter Pruning for Low- ...",
            "url": "https://aclanthology.org/2025.findings-acl.990.pdf"
          },
          {
            "title": "Accepted Main Conference Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/main_papers/"
          },
          {
            "title": "Collaborative Multi-LoRA Experts with Achievement-based Multi-Tasks Loss for",
            "url": "https://www.ijcai.org/proceedings/2025/0772.pdf"
          },
          {
            "title": "Dynamic Mixture of Curriculum LoRA Experts for Continual ...",
            "url": "https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Dynamic%20Mixture%20of%20Curriculum%20LoRA%20Experts%20for%20Continual%20Multimodal%20Instruction%20Tuning.pdf"
          }
        ]
      },
      "Based on the search results, I found information about related work on cross-lingual transfer and LoRA methods, but I did not find a specific paper or resource that exactly matches the query you provided for \"COMPASS distribution-guided data selection cross-lingual LoRA TMLR 2025.\" \n\nThe search returned results about various LoRA-related papers from 2025, including:\n- Cross-LoRA for LoRA transfer across heterogeneous LLMs\n- GRASP LoRA for cross-lingual transfer with adapter sparsity\n- Other LoRA variants for different applications\n\nHowever, none of these appear to be the specific \"COMPASS\" paper with distribution-guided data selection that you're looking for, and none are identified as being published in TMLR (Transactions on Machine Learning Research) 2025.\n\nWould you like me to:\n1. Search with different keywords or a modified query?\n2. Search for more recent TMLR 2025 publications?\n3. Search for the paper by authors' names if you have them?"
    ],
    "durationSeconds": 4.7028189619999905
  },
  "sourceToolAssistantUUID": "1ebb79c0-1bc4-44cb-8a51-6ed5017957b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-10T07:46:22.483Z_

<details><summary>Logged reasoning block</summary>

```text
The COMPASS paper wasn't found easily. Let me see what else I should check. 

Now let me step back and compile my findings for the review:

**Round 5 Issues Status in Round 6:**

1. **Foroutan et al. (arXiv:2510.25947)** - STILL MISSING from Round 6. The paper exists and is about pretraining (not instruction tuning), but the Round 5 reviewer said EMNLP reviewers familiar with it will raise it against TWMP's staged curriculum and reweighting. This remains unaddressed.


2. **LangGPS (arXiv:2511.10229, AAAI 2026)** - Also absent from Round 6. It covers multilingual instruction tuning data selection using language separability guidance, making it a direct AAAI 2026 competitor that needs citation and differentiation.
3. **Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings)** and **Kazakh instruction tuning (arXiv:2502.13647, ACL 2025 Long)** - Both missing as well, despite being confirmed publications in recent ACL venues.
4. **URIEL+ expansion (arXiv:2510.27183)** - Not cited, yet it directly extends the tool TWMP builds on, and the Kazakh work fine-tunes on instruction data using GPT-4o, making it directly competitive.
5. **DPO probe characterization** - Only partially addressed; the per-instruction fallback analysis remains incomplete.
6. **Budget-Xfer (arXiv:2603.27651)** and **Cross-Lingual Transfer Theoretical Framework for Turkic (arXiv:2604.06202)** - Two March 2026 papers that are newly identified gaps: the first tackles budget-constrained source language selection for cross-lingual transfer, directly adjacent to TWMP's multi-source selection problem, while the second introduces theoretical foundations for Turkic language transfer.

What concerns me is that all five moderate and minor issues flagged in the previous review remain unaddressed—the paper isn't making progress on citation completeness. For novelty, I'm settling on 3.5/5: the core contribution of typologically-weighted multi-pivot curriculum with DPO for low-resource agglutinative languages is genuinely novel, but LangGPS and arXiv:2410.07809 represent competing approaches that need clearer differentiation through proper citations.

On feasibility, the method scores well at 4/5—it's concretely specified with realistic compute requirements, smart safeguards like the DPO probe, and uses accessible tools like Qwen3.5-9B and URIEL+. Clarity also lands at 4/5 since the technical details are unusually precise, though the missing citations still create gaps in framing the related work. For impact, I'm at 3.5/5: while positive results could genuinely help low-resource Turkic and Mongolic NLP with well-chosen benchmarks, the scope is narrow at three target languages, and the key generalization claim about Swahili is held out rather than demonstrated.

That averages to 3.75, which falls short of the 4.0 threshold, so this needs revision. The critical issue is that all five Round 5 concerns—Foroutan, LangGPS, Code-Switching Curriculum, and those two arXiv papers—remain completely unaddressed in Round 6, which signals a pattern the generator needs to explicitly tackle. There's also a new March 2026 paper on budget-constrained multi-source language selection (Budget-Xfer) that should be flagged, and the per-instruction fallback characterization from Round 5 still needs clarification.

We're at Round 6 of 10 now, and the paper has been stuck in revise status for six rounds straight without actually fixing these moderate issues. The core contributions themselves are sound, but the citation gaps and writing problems keep blocking a pass. I need to make clear in this verdict that while these are fixable problems, they genuinely need to be addressed this time around.

I'm also noticing the submission has shifted its primary target from EMNLP 2026 to ACL 2027, which aligns with the May 25 deadline constraint, but the reviewer notes seem to reference rolling deadlines for EMNLP that don't quite line up with what was originally stated.

The resource estimates look solid—manual mode and human-in-loop both stay within the H100h constraints, while auto_research correctly flags the overage. Now I'll move into the formal review, starting with the novelty score of 3.5 for the typological weighting and multi-pivot curriculum approach.

However, LangGPS from AAAI 2026 addresses similar ground in multilingual instruction tuning data selection, and the missing citations to Foroutan and Code-Switching Curriculum undercut the novelty claim. Feasibility scores well at 4—the method is concrete with realistic compute requirements for the practical modes and a smart prerequisite probe as a safeguard. Clarity also rates 4 despite the technical precision, mainly held back by gaps in related work coverage. Impact sits at 3.5 since it tackles a genuine need for underrepresented language families, though the scope is somewhat limited and generalization beyond the three primary targets remains undemonstrated. That averages to 3.75, which calls for a revise recommendation. The first significant issue involves a pattern affecting all submissions.

The five Round 5 issues are still unresolved—Foroutan et al., LangGPS, Code-Switching Curriculum, and two arXiv papers remain uncited. Budget-Xfer from March 2026 is another adjacent work on budget-constrained source language selection for cross-lingual transfer that deserves mention. There's also a persistent gap in how the per-instruction fallback characterization is handled: the paper states that instructions with no target-language responses are discarded, but doesn't actually report the per-instruction fallback rate as a result, only the per-pair probe rate.

Now I need to work through the specific citations and positioning for each of these five papers. For Foroutan et al., the key distinction is that their findings on English-pivot pretraining and staged reweighting come from a large-scale pretraining setting, whereas TWMP operates in a narrower instruction-tuning regime with LoRA and a constrained pivot pool, so their results may not directly transfer. LangGPS uses language separability scores from the model's own representation space for data selection, which is fundamentally different from TWMP's external typological approach—I need to complete that contrast and work through the remaining three papers' positioning. ological features from URIEL+ to derive a principled ordering over pivot languages independent of training dynamics, and provides a staged curriculum that LangGPS does not."

(3) Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings): "CSCL proposes a 3-stage curriculum (token → sentence → monolingual code-switching). TWMP's curriculum operates over a pool of typologically ordered pivot languages, not within a single language pair, and does not require code-switching data."

(4) Kazakh instruction tuning (arXiv:2502.13647, ACL 2025 Long): "Laiyk et al. fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples, achieving strong KazMMLU performance—TWMP does not require any target-language instruction labels and applies to Mongolian and Uyghur where no comparable dataset exists."

(5) URIEL+ expansion (arXiv:2510.27183, LREC 2026): "A concurrent LREC 2026 paper extends URIEL+ with script vectors and Glottolog genealogies covering 26,449 languages, but TWMP uses the earlier COLING 2025 version which already provides sufficient coverage for the four qualifying Aya pivot languages." I should also note Budget-Xfer as related work on budget-constrained multi-source language selection for cross-lingual transfer. ACL 2027 with the August 3, 2026 ARR deadline remains the right target.

I'm now positioning TWMP against these related approaches by clarifying what makes it distinct—the typological ordering of pivots, the curriculum over language pools rather than within pairs, the label-free approach, and the fact that it works for low-resource languages without requiring target-language instruction data. The URIEL+ comparison is important because it shows we're using a stable, well-established version rather than waiting for the newer expansion. Budget-Xfer rounds out the positioning by showing we're addressing a similar constraint optimization problem but in the pivot selection space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ab60803-f816-4091-a1fb-6385c40d64b3",
  "isSidechain": false,
  "requestId": "req_011CatWsjTNusPTZnkc1Lqiq",
  "type": "assistant",
  "uuid": "da1120cb-5ca0-4f41-86d4-681f265690ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RbWJKjwsM6P4i7ztH9mR7V",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 54785,
      "output_tokens": 5457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5457,
          "cache_read_input_tokens": 54785,
          "cache_creation_input_tokens": 1033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1033
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

_source line 65 · 2026-05-10T07:47:00.305Z_

I now have sufficient information to complete my review. Let me compile the findings.

**Summary of research findings:**
1. All five Round 5 issues confirmed as still absent from Round 6: Foroutan et al. (arXiv:2510.25947), LangGPS (arXiv:2511.10229/AAAI 2026), Code-Switching Curriculum (arXiv:2411.02460/ACL 2025 Findings), Kazakh instruction tuning (arXiv:2502.13647/ACL 2025 Long), URIEL+ expansion (arXiv:2510.27183) — none appear in the landscape section or key_references list.
2. New paper found: Budget-Xfer (arXiv:2603.27651, March 2026) — budget-constrained multi-source language selection for cross-lingual transfer, directly adjacent to TWMP's core problem.
3. Theoretical Turkic framework (arXiv:2604.06202, April 2026) — purely theoretical, no experiments, low threat.
4. Foroutan et al. actual claims confirmed: focuses on pretraining-scale data mixtures (1.1B–3B models, 25–400 languages); curriculum/reweighting findings are at pretraining scale, not instruction-tuning scale.
5. LangGPS confirmed as AAAI 2026 main track with 22-language evaluation including low-resource languages — a genuine TWMP competitor on the data selection dimension.
6. Core method remains technically sound; compute estimates within budget for manual/HIL modes.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The core combination of typological-distance weighting, multi-pivot curriculum, and multi-source DPO is genuinely novel, but LangGPS (AAAI 2026, arXiv:2511.10229) addresses multilingual instruction tuning data selection using model-internal language separability signals across 22 languages including low-resource targets — an uncited AAAI 2026 peer-reviewed alternative that weakens the novelty claim until explicitly differentiated. The six-round accumulation of unaddressed competitor citations erodes the credibility of the novelty framing."
    },
    "feasibility": {
      "score": 4,
      "rationale": "The method is concretely specified with precise DPO formulation, D_25/D_60 percentile curriculum thresholds, the 500-instruction prerequisite probe, and the 20-token length gate; compute in manual (~120 H100h) and human-in-loop (~186 H100h) modes stays within the ≤200 H100h constraint, and Qwen3.5-9B, URIEL+ library, Aya collection, and evaluation benchmarks are all publicly accessible."
    },
    "clarity": {
      "score": 4,
      "rationale": "The technical specification — DPO pair construction, curriculum epoch ranges, probe threshold, fallback logic — is unusually precise and reproducible for a draft at this stage; the primary clarity deficit is in related work, where five gaps flagged in Round 5 remain absent, making the landscape section incomplete for EMNLP reviewers."
    },
    "impact": {
      "score": 3,
      "rationale": "The work addresses a real and documented performance gap for Kazakh, Mongolian, and Uyghur confirmed by three ACL 2025 peer-reviewed benchmarks; however, the method's generalizability beyond the Turkic–Mongolic cluster remains untested (Swahili is held out), and a competing single-language approach (arXiv:2502.13647) achieves strong KazMMLU performance with 10,600 GPT-4o-assisted Kazakh instructions, suggesting target-language data creation is a viable alternative the paper has not acknowledged."
    }
  },
  "issues": [
    "SIGNIFICANT (PATTERN) – All five Round 5 issues remain unaddressed in Round 6 for the second consecutive round. (1) Foroutan et al. (arXiv:2510.25947, ICLR-submitted): not in landscape or key_references. (2) LangGPS (arXiv:2511.10229, AAAI 2026 main): not in landscape or key_references — this is a peer-reviewed AAAI 2026 competitor on multilingual instruction tuning data selection across 22 languages including low-resource targets, and its omission is the most damaging gap. (3) Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings): not cited despite being published November 2024 and appearing in ACL Anthology. (4) arXiv:2502.13647 (ACL 2025 Long, Kazakh instruction tuning): not cited despite being a direct Kazakh-targeting baseline. (5) URIEL+ expansion (arXiv:2510.27183, LREC 2026): not cited despite directly extending the typological tool TWMP relies on.",
    "MODERATE (NEW) – Budget-Xfer (arXiv:2603.27651, March 2026) proposes budget-constrained source language selection for multi-source cross-lingual transfer, jointly optimizing which source languages to include and how much data to allocate from each — directly parallel to TWMP's multi-pivot selection problem. It evaluates on three African target languages (Hausa, Yoruba, Swahili) using a 288-experiment suite. While it targets classification tasks rather than instruction tuning, EMNLP reviewers in the cross-lingual track will expect it to be cited and contrasted: Budget-Xfer frames source selection as resource allocation without typological features or curriculum ordering; TWMP provides principled URIEL+-based weighting and staged scheduling.",
    "MINOR (PERSISTENT) – Per-instruction chosen-pool fallback characterization remains incomplete. The approach section states that 'instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' but does not report the per-instruction fallback rate as a characterization result. Round 5 feedback specifically requested one sentence confirming these instructions fall back to SFT-weighted objective (not silent skip) and reporting the empirical fallback rate per source-target pair. The current text says they are 'discarded,' which implies silent skip rather than SFT fallback — this ambiguity must be resolved and the frequency reported."
  ],
  "feedback": "This is Round 6. The core method is technically sound, the DPO formulation is precise, the compute budget is within constraint, and the evaluation design is appropriate. However, the same five citations flagged in Round 5 are absent for the second consecutive round, and a new paper (Budget-Xfer, arXiv:2603.27651) has appeared that is directly adjacent. Here is the exact text to add for each outstanding item:\n\n(1) Foroutan et al. (Section 2, one sentence): 'Revisiting Multilingual Data Mixtures [Foroutan et al., 2025] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime.'\n\n(2) LangGPS (Section 2, one paragraph — highest priority): 'LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address.'\n\n(3) Code-Switching Curriculum (Section 2, one sentence): 'Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target.'\n\n(4) Kazakh instruction tuning (Section 2, one sentence): 'Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists.'\n\n(5) URIEL+ expansion (Section 3, one sentence): 'A concurrent LREC 2026 extension [Shipton et al., arXiv:2510.27183] adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version [arXiv:2409.18472] with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages.'\n\n(6) Budget-Xfer (Section 2, one sentence): 'Budget-Xfer [arXiv:2603.27651, 2026] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address.'\n\n(7) Fix the per-instruction fallback: Change 'Instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' to 'Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe.'\n\nAll seven items are writing-only changes requiring no new experiments. ACL 2027 (ARR August 3, 2026) remains the appropriate primary target. At Round 6, the paper cannot pass until at minimum items (1)–(5) are resolved.",
  "reason": "All five Round 5 moderate/minor issues persist unaddressed for the second consecutive round, with LangGPS (AAAI 2026) being the most damaging omission; the core method is sound but the related work coverage is systematically incomplete, preventing a pass verdict."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da1120cb-5ca0-4f41-86d4-681f265690ab",
  "isSidechain": false,
  "requestId": "req_011CatWsjTNusPTZnkc1Lqiq",
  "type": "assistant",
  "uuid": "a825916a-696a-4471-a811-1a31afbc3229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RbWJKjwsM6P4i7ztH9mR7V",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 54785,
      "output_tokens": 5457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5457,
          "cache_read_input_tokens": 54785,
          "cache_creation_input_tokens": 1033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1033
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

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a825916a-696a-4471-a811-1a31afbc3229",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-pivot curriculum instruction tuning for agglutinative languages",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a825916a-696a-4471-a811-1a31afbc3229",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-pivot curriculum instruction tuning for agglutinative languages",
  "sessionId": "cec4e7e2-fbd6-4daa-bf82-06fb3be48a2a"
}
```

---
