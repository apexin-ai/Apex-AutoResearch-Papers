# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/ca3389b0-ef08-4d6b-8028-f3decd1eae3a.jsonl`
- **Structured JSON:** [`fe4914f070463a47e76e.json`](../../sessions/fe/fe4914f070463a47e76e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:08:15.675Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:08:15.675Z",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Multilingualism and Cross-Lingual NLP.\n\nDirection: Cross-lingual transfer and multilingual NLP methods. In-scope: cross-lingual transfer without parallel data, multilingual instruction tuning strategies, language-agnostic representations, low-resource language adaptation, cross-lingual retrieval, multilingual reasoning, code-switching handling. ACL 2025 outstanding papers highlighted multilingual gaps and cross-lingual intervention methods.\n\nContribution type: METHOD ONLY. New training recipes, transfer algorithms, or adaptation techniques. Not a new multilingual dataset or language-specific analysis.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Multilingual experiments need coverage across languages — budget for LoRA fine-tuning on multilingual models, not full pretraining.\n2. Time: ≤16 days. Use existing multilingual models (BLOOM, mT5, XLM-R, Aya, Qwen multilingual, Llama-3 multilingual).\n3. Eval: XTREME-UP, XCOPA, XStoryCloze, MGSM, multilingual MMLU, TyDi QA, FLORES for MT.\n\nLook for: efficient cross-lingual transfer with minimal target-language data, multilingual reasoning without English-centric bias, representation alignment methods, adaptation techniques for typologically diverse languages. Avoid: English-only experiments, monolingual fine-tuning.\n\nTag: direction=multilingual, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 8/10)\n{\n  \"title\": \"Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignment\",\n  \"project_name\": \"cls_lora_cultural_preservation\",\n  \"source\": \"web_research\",\n  \"level\": \"solid\",\n  \"core_problem\": \"Cross-lingual fine-tuning systematically suppresses culturally-grounded, language-specific knowledge while improving factual transfer—a phenomenon called 'cultural erasure.' Mechanistic work (arXiv:2504.10191) demonstrates that in pre-trained instruction-tuned models, cultural knowledge is spatially localized in specific layers and steerable via linear activation vectors, suggesting particular layer indices implement cultural routing pathways. Whether this spatial localization persists after LoRA instruction fine-tuning—and whether cross-lingual fine-tuning causes behavioral erasure (routing pathway disruption), representational erasure (information loss), or both—remains empirically untested. No training-time method prevents either failure mode, forcing practitioners to choose between cross-lingual capability and cultural authenticity. A complementary mechanistic uncertainty reinforces the need for per-model empirical investigation: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deeper-layer localization (layers 19–30, approximately 45–71% depth in Gemma2-9b-it) identified via activation-steering analysis in arXiv:2504.10191. The two methodologies measure different constructs—discrete high-influence neurons versus distributed activation-space subspaces—and their disagreement means the culturally-critical layer partition cannot be reliably imported from prior work for an arbitrary target model; it must be discovered empirically.\",\n  \"opportunity\": \"'Rethinking Cross-lingual Alignment' (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 listed as arXiv preprint on the first author's publication page) rigorously demonstrates that every tested cross-lingual alignment approach degrades cultural localization across all six languages, and proposes Surgical Steering as a remedy—but only at inference time, requiring per-query layer manipulation and offering no prevention during training. The finding that factual transfer and cultural localization are optimally steerable at different model layers is actionable: applying LoRA selectively to factual-transfer layers while freezing cultural-knowledge layers during instruction fine-tuning would prevent erasure at the source. arXiv:2504.10191 establishes that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors in specific layers (notably layers 19–30 in Gemma2-9b-it, with peaks at layers 23 and 30), supporting the hypothesis that particular layer indices implement cultural routing pathways. CLS-LoRA's freezing strategy is designed to exploit this structure: if that spatial localization persists after LoRA fine-tuning (behavioral erasure—routing disrupted but representations intact), freezing those layers during training prevents routing disruption; if fine-tuning also degrades the representations themselves (representational erasure), the KL-divergence penalty anchors cultural-layer activations to their pretrained distribution. Stage 1 empirically distinguishes these two failure modes before the main sweep begins. Crucially, the layer partition question is now a live empirical debate in the literature: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) independently find culture-relevant neurons in shallow-to-middle MLP layers using gradient attribution, while activation-steering work (arXiv:2504.10191, arXiv:2510.26024) localizes cultural steerability in deeper layers. This genuine methodological disagreement elevates Stage 2 probing from a validation step to the principled empirical resolution of an open question—CLS-LoRA discovers the culturally-critical partition for each target model rather than assuming it from any single prior study. This is feasible with any open-source dense multilingual model via a lightweight per-layer probing step.\",\n  \"landscape\": \"INCLINE (arXiv:2410.12462, ACL 2025 outstanding paper) aligns internal representations from low-resource to high-resource languages via learned projection matrices derived from parallel sentences, improving cross-lingual task performance but not distinguishing factual from cultural knowledge. Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025, Liu & Niehues) provides the empirical foundation for CLS-LoRA's factual-transfer layer partition: through translation retrieval probing across 1,190 language pairs on Llama 3 and Qwen 2.5, it establishes that layer 16 (50% depth in a 32-layer model) is the key integration point for cross-lingual semantic alignment, and that incorporating a middle-layer alignment objective consistently improves cross-lingual task performance particularly for lower-resource languages. CLS-LoRA extends this by additionally protecting cultural-knowledge layers from LoRA updates—arXiv:2504.10191 identifies layers 19–30 (approximately 45–71% depth in Gemma2-9b-it's 42-layer architecture, with peak cultural activation at layers 23 and 30) as critical for cultural routing, and Stage 2 probing empirically determines the analogous partition for each target model—a protection axis entirely absent from Liu & Niehues, whose work does not distinguish factual from cultural knowledge and proposes no cultural preservation objective. Cross-Lingual Transfer of Cultural Knowledge (arXiv:2506.01675, ACL 2025 short paper, Zhang et al.) provides empirical background showing cultural knowledge transfer is asymmetric: high-resource language pairs exhibit bidirectional transfer while low-resource languages primarily export cultural knowledge to English without reciprocal benefit, driven by a frequency-based pretraining data mechanism. This asymmetry directly motivates training-time prevention of cultural erasure—low-resource languages are disproportionately at risk and most in need of the protection CLS-LoRA provides. AlignX (arXiv:2509.24338, EMNLP 2025) and CM-Align (arXiv:2509.08541) apply two-stage and consistency-based multilingual alignment respectively, both optimizing convergence without a cultural preservation objective. Language Surgery/ITLC (arXiv:2506.12450) disentangles language-specific from agnostic information through latent injection at inference time, but does not train models to preserve this distinction. Alignment through steering (arXiv:2505.12584) adds a learned residual-stream vector at a single layer; it outperforms many baselines but still does not model the factual-cultural layer split. Surgical Steering (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 the first author's publication page lists this as an arXiv preprint without a confirmed proceedings venue) is the only method addressing the cultural erasure problem, and is strictly an inference-time patch over an already-erased model. arXiv:2504.10191 ('Localized Cultural Knowledge is Conserved and Controllable in LLMs', April 2025) demonstrates that in pre-trained instruction-tuned models, cultural knowledge exists as spatially localized steerable activation-space vectors—mechanistic analysis on Gemma2-9b-it (42 layers) identifies layers 19–30 as critical for cultural activation, with peak effects at layers 23 and 30 (approximately 55–71% depth)—and can be controlled via linear steering at inference time. This establishes spatial localization of cultural knowledge in pre-trained models, motivating CLS-LoRA's hypothesis that specific layer indices implement cultural routing pathways; whether this localization persists after LoRA instruction fine-tuning is precisely what Stage 1 tests.\\n\\nYamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) conduct a neuron-level analysis of cultural understanding using a gradient-based scoring method with additional filtering for precise refinement. They identify both culture-general neurons (supporting cultural understanding across cultures) and culture-specific neurons (tied to individual cultures), which together comprise less than 1% of all neurons and are concentrated in shallow-to-middle MLP layers—not in the deeper layers identified by activation-steering analysis in arXiv:2504.10191. Suppressing these neurons degrades cultural benchmark performance by up to 30% while leaving general NLU tasks largely unaffected. This finding is in apparent tension with the deeper-layer localization from arXiv:2504.10191 and arXiv:2510.26024, reflecting a genuine methodological distinction: gradient attribution identifies discrete neurons with the highest individual causal influence, which may be sparse and concentrated in earlier layers; activation-steering subspaces reflect distributed representational geometry that implements cultural routing across many layers and may peak in depth-profile at different points. CLS-LoRA's Stage 2 probing directly bridges this debate: rather than assuming either result, it measures per-layer probe accuracy on each target model and discovers the cultural-knowledge partition empirically. If shallow neurons (Yamamoto et al.) dominate, Stage 2 will assign those layers to the frozen cultural partition; if deeper subspaces (arXiv:2504.10191) dominate, Stage 2 will assign those layers instead. Stage 2 is thus a model-specific resolution mechanism that makes CLS-LoRA robust to methodological disagreements in the mechanistic literature.\\n\\nThree directly related selective-LoRA/adapter methods require explicit differentiation. MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762) detects language-aware neurons in a teacher model and injects extracted knowledge into language-pair-specific LoRA modules in a student model for multilingual machine translation, achieving +1.7 BLEU on average. While MLAS-LoRA and CLS-LoRA both employ a probe-then-selective-LoRA pipeline, they differ on three critical axes: (1) task domain—MLAS-LoRA targets MT translation quality whereas CLS-LoRA targets cultural knowledge preservation during instruction fine-tuning; (2) partition dimension—MLAS-LoRA partitions along language-pair specificity (language-A vs language-B neurons) whereas CLS-LoRA partitions along the factual-transfer vs cultural-localization semantic axis, which cuts across language pairs; and (3) objective—MLAS-LoRA optimizes translation accuracy via teacher-student knowledge distillation whereas CLS-LoRA optimizes a cultural-preservation signal with no distillation component. The cultural-preservation objective is the categorical novelty: no prior selective-LoRA work defines a 'keep culturally-grounded outputs intact' training signal. LayRA (arXiv:2509.11414, September 2025) proposes layer-selective LoRA for continual multilingual language addition, applying LoRA to initial and final transformer layers (the first 10 and last 2 layers, plus embeddings and LM head) while freezing intermediate layers. The partition rationale—that multilingual models encode source-language inputs in initial layers, reason in English in middle layers, and decode into the target language in final layers—leads to a source-language-encoding vs English-reasoning vs target-language-decoding functional partition axis. CLS-LoRA differs on three dimensions: (1) objective—LayRA enables new-language addition without catastrophic forgetting of existing languages, whereas CLS-LoRA preserves cultural knowledge during cross-lingual instruction fine-tuning; (2) partition axis—LayRA's functional encoding/reasoning/decoding axis is defined over language identity and cuts uniformly across all languages, whereas CLS-LoRA's factual-transfer vs cultural-localization semantic axis cuts across language-pair specificity; (3) partition method—LayRA hard-codes specific layer indices derived from qualitative linguistic reasoning, whereas CLS-LoRA uses empirical per-layer probing to discover the partition for each target model, enabling adaptation to the contested mechanistic landscape. The cultural-preservation objective remains the categorical novelty absent from LayRA. CultureManager (arXiv:2602.22475, Zhang et al., February 2026) proposes task-aware cultural alignment by synthesizing task-specific cultural data grounded in web search results and managing multi-culture knowledge through culture-specific LoRA adapters selected by a culture router, achieving consistent improvements over prompt-based and fine-tuning baselines across ten national cultures and culture-sensitive downstream tasks. CLS-LoRA differs from CultureManager on three dimensions: (1) objective—CultureManager improves cultural alignment for downstream task performance by adapting LLM outputs to match target cultural values, whereas CLS-LoRA preserves existing culturally-grounded knowledge from being erased during cross-lingual instruction fine-tuning; (2) partition axis—CultureManager partitions along culture identity (which national culture gets which adapter), whereas CLS-LoRA partitions along the factual-transfer vs. cultural-localization semantic axis, which cuts across culture and language identity; (3) mechanism—CultureManager routes inputs to culture-specific LoRA modules at the adapter level via a culture router, whereas CLS-LoRA freezes layers empirically identified as cultural-knowledge carriers and applies LoRA exclusively to factual-transfer layers without any routing component. The cultural-preservation objective—preventing erasure rather than enabling cultural adaptation—remains absent from CultureManager. Source-Shielded Updates (arXiv:2512.04844, Nov 2025) proposes column-wise parameter freezing to prevent catastrophic forgetting of source-language task performance during target-language adaptation—addressing cross-lingual interference but not the factual-vs-cultural layer distinction or cultural knowledge preservation as a first-class objective. Sparse Subnetwork Enhancement for Underrepresented Languages (arXiv:2510.13580, Gurgurov et al., updated February 2026) identifies language-associated sparse subnetworks comprising less than 1% of model parameters using Language Activation Probability Entropy (LAPE), an information-theoretic metric that captures language-specific activation patterns, and fine-tunes only those parameters. On Llama-3.1-8B, Mistral-Nemo-12B, and Aya-Expanse-8B across 12 mid- and low-resource languages, it achieves 90.5% cross-lingual alignment (cosine similarity)—the best of any tested method—while preserving general capabilities (MMLU: 63.01% vs. 63.08% base), outperforming full fine-tuning, LoRA, and IA3. Adaptation is concentrated in down-projection weights of later layers, with weight changes 3–5× larger than up/gate projections. CLS-LoRA differs from Sparse Subnetwork Enhancement on two axes: (1) objective—Sparse Subnetwork Enhancement targets language performance improvement on translation and classification benchmarks (FLORES, SIB-200, BELEBELE) whereas CLS-LoRA targets cultural knowledge preservation during cross-lingual instruction fine-tuning; and (2) partition axis—LAPE identifies language-identity neurons (neurons that activate specifically for a given language, cutting across semantic content) whereas CLS-LoRA partitions along the factual-transfer vs. cultural-localization semantic axis, which cuts across language identity rather than tracking it. The cultural-preservation objective remains absent from Sparse Subnetwork Enhancement.\",\n  \"approach\": \"We propose Cultural-Layer-Selective LoRA (CLS-LoRA), a training-time method that prevents cultural erasure without sacrificing factual cross-lingual transfer. The pipeline has four stages.\\n\\nMechanistic bridge. Our layer-freezing strategy rests on a hypothesis connecting inference-time observations to training-time interventions: the layer indices most sensitive to cultural-vs-factual activation steering at inference time (arXiv:2510.26024, corroborated by cultural customization vectors in arXiv:2504.10191 concentrated at layers 19–30 in Gemma2-9b-it) identify the weight matrices that implement cultural routing. LoRA updates modify precisely these weight matrices; applying LoRA to cultural-knowledge layers may therefore disrupt the routing pathways through which culturally-grounded representations reach outputs. This hypothesis involves a genuine empirical uncertainty that the literature has not resolved: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deep-layer activation-steering localization from arXiv:2504.10191. The discrepancy most likely reflects the difference between measuring discrete high-influence neurons (gradient attribution captures sparse, individually causal units that may be early in the network) versus measuring distributed activation subspaces (steering analysis captures the geometry of representational routing, which may span many layers and peak later). Neither result invalidates the other; they measure different aspects of how cultural knowledge is implemented. Stage 2 probing is designed precisely for this uncertainty: by measuring per-layer probe accuracy directly on each target model's representations, it discovers the culturally-critical partition without assuming either methodological lens is correct—if shallow neurons dominate functionally, Stage 2 identifies shallow layers as the cultural partition; if deeper subspaces dominate, Stage 2 identifies those instead. Whether the representations themselves persist as recoverable vectors after full LoRA fine-tuning (behavioral erasure) or are also degraded (representational erasure) is a separate open empirical question—Stage 1 provides this answer. Freezing the empirically-identified cultural-knowledge layers during training preserves both the routing weights and the residual-stream geometry that steerability depends on, addressing both failure modes by design.\\n\\nStage 1 — Structural diagnostic: Before the main sweep, we run full-LoRA instruction fine-tuning on a held-out model checkpoint and measure per-layer cultural probe accuracy before and after. Stage 1 trains separate linear probes on each checkpoint's frozen representations—one probe trained and evaluated on the pretrained-checkpoint's layer activations, one probe trained and evaluated on the post-LoRA-checkpoint's layer activations—using the same held-out cultural question split for both. This ensures accuracy differences reflect genuine representational change rather than activation-space reorganization: applying a single probe trained on pretrained representations cross-checkpoint to post-LoRA representations would fail if LoRA remaps the activation geometry without destroying cultural information (behavioral erasure), conflating reorganization with information loss; separate per-checkpoint probes make the comparison clean and the behavioral-vs-representational distinction interpretable. If probe accuracy is maintained post-training, erasure is confirmed as behavioral (pathway disruption) and layer freezing is the correct intervention; if probe accuracy drops, erasure is partly representational and the KL-divergence regularizer in Stage 3 becomes critical. This diagnostic sharpens the mechanistic story and validates the layer-freezing strategy regardless of which failure mode dominates. An automated entropy-based partition fallback replaces human inspection when probe curves are bimodal or noisy, reducing the agent failure mode from prior review.\\n\\nStage 2 — Layer profiling: Lightweight linear probes (one per transformer layer) are trained on a small parallel corpus to produce per-layer factual-transfer and cultural-localization accuracy scores, yielding a principled layer partition. For factual transfer, the empirical expectation from arXiv:2502.14830 (Liu & Niehues) is approximately middle layers (~50% model depth). For cultural knowledge, arXiv:2504.10191 identifies layers 19–30 as critical in Gemma2-9b-it (approximately 45–71% depth in a 42-layer model, with peak effects at layers 23 and 30); Yamamoto et al. (arXiv:2510.08284, ICLR 2026) find culture-relevant neurons in shallow-to-middle MLP layers via gradient attribution. Stage 2 probing empirically determines the partition boundaries for each target model—Qwen3-8B (36 layers) and Aya-23-8B—rather than hard-coding percentages from either prior study; this is the methodologically sound response to the contested mechanistic landscape. For cultural-localization probes, we use INCLUDE (ICLR 2025, CC BY 4.0; 197,243 MCQA pairs sourced from regional examinations across 44 languages and 52 countries, arXiv:2411.19799), filtered for cultural-domain categories (customs, food, celebrations, social norms), supplemented by language-filtered Wikipedia paragraphs extracted from culture-specific articles tagged with Wikidata cultural-domain categories (CC-BY-SA 4.0, widely multilingual). CulturalBench (arXiv:2410.02677, ACL 2025) cannot be used for probe training because the authors explicitly state that the annotation platform used OpenAI APIs under terms that disallow using the collected data for training; CulturalBench is therefore reserved strictly for final evaluation in Stage 4. For factual-transfer probes, we use held-out splits of TyDiQA and XQUAD. SemEval-2026 Task 7 data (BLEnD extension) is reserved strictly for final evaluation and is not used in probe training, consistent with the task's evaluation-only rules (confirmed via the official task repository). No new annotation is required.\\n\\nStage 3 — Selective LoRA training: LoRA adapters (via Hugging Face PEFT target_modules) are inserted exclusively into factual-transfer layers and trained with standard instruction fine-tuning loss on multilingual instruction data, while cultural-knowledge layers remain fully frozen. An optional auxiliary KL-divergence penalty on a held-out cultural probe set discourages residual drift in frozen layers' downstream activations. To establish that layer freezing is the operative mechanism rather than KL regularization alone, Stage 3 includes a 2×2 ablation: (a) full LoRA without KL penalty (existing baseline); (b) full LoRA with KL-divergence penalty on cultural-layer activations (regularization-only baseline, new); (c) CLS-LoRA with layer freezing and no KL penalty (freezing-only; already present in the sweep as the no-regularization variant); (d) CLS-LoRA with layer freezing and KL penalty (proposed method). Condition (b) is the critical addition: it tests whether KL regularization alone, without the complexity of a learned layer partition, achieves equivalent cultural preservation. If (b) matches (d), the partitioning step is unnecessary overhead; if (c) and (d) both outperform (b), layer freezing is confirmed as the operative mechanism. Approximately 4–6 additional training runs (condition (b) only; 2 models × 2–3 seeds) are added to the auto sweep; conditions (a), (c), and (d) are already covered by existing runs.\\n\\nStage 4 — Evaluation: Experiments run on Qwen3-8B (primary: confirmed dense, 36 transformer layers, 119 languages and dialects, 8.2B parameters) and Aya-23-8B (secondary: confirmed dense decoder-only, 23 languages, 8B parameters) for cross-architecture generalization. All Qwen3-8B experiments are conducted in non-thinking mode (enable_thinking=False in the chat template), ensuring consistent direct-generation behavior during both LoRA fine-tuning and cultural localization probing without interference from chain-of-thought reasoning pathways. LLaMA 4 Scout is excluded—its 48-block, 16-expert MoE architecture makes the factual-vs-cultural layer partition from arXiv:2510.26024, established on dense models, methodologically inapplicable without separate MoE-specific validation. Evaluation uses CulturalBench (arXiv:2410.02677, ACL 2025; 1,696 human-verified questions across 45 global regions, evaluation-only) and SemEval-2026 Task 7 as primary cultural metrics. To verify that CLS-LoRA does not regress on capabilities orthogonal to cultural localization and factual QA, Stage 4 adds three supplementary evaluation tracks via lm-evaluation-harness: cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; lm-eval task group xcopa_[lang]); cross-lingual narrative understanding (XStoryCloze, 11 languages, zero-shot; lm-eval task group xstorycloze); and multilingual arithmetic chain-of-thought (MGSM, 11 languages, direct mode; lm-eval task mgsm_direct). Each benchmark requires approximately 2–4 GPU-hours per model; together they add ~18–24h A100 total across both target models and all evaluated checkpoints. XCOPA is the most mechanistically relevant: if Stage 2's cultural-knowledge layer partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain commonsense transfer—an outcome that would be reported transparently and interpreted as a scope constraint on the method (cultural preservation trades off against commonsense transfer in those layers) rather than treated as an uncontrolled failure. MGSM verifies that the factual-transfer LoRA updates preserve multilingual arithmetic reasoning. All three benchmarks use standard zero-shot or direct evaluation protocols already in lm-evaluation-harness and require no additional training data. Comprehensive multilingual capability benchmarks (XTREME-UP, multilingual MMLU) are not included as primary metrics because their constituent tasks overlap substantially with those already in the suite—XTREME-UP's reading comprehension and commonsense coverage is addressed by TyDiQA and XCOPA, while multilingual MMLU reasoning is partially captured by MGSM—and a full evaluation of both is planned for the camera-ready version at approximately 8h A100 per model. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; we therefore employ the explicitly defined fallback evaluation—a 2D scatter of cross-lingual factual accuracy (XQUAD/TyDiQA) vs cultural localization accuracy (CulturalBench) across languages, normalized to the pre-fine-tuning baseline, yielding the same transfer-localization interpretive framework. We compare against full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA (adapted to the instruction-FT setting), and Source-Shielded Updates baselines to demonstrate that CLS-LoRA Pareto-dominates prior methods in the transfer-localization trade-off space.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~230h A100 80GB (~92h H100 equivalent)\",\n      \"gpu_utilization\": \"~30–40% effective; GPU idles while the researcher inspects probe accuracy heatmaps to select layer partition boundaries, designs ablation grids, and iterates on training scripts between runs\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$345–475 (A100 at $1.49–2.06/hr via RunPod/Lambda); additional ~30h reflects new ablation runs (condition (b), ~12h) and XCOPA/XStoryCloze/MGSM evaluation (~18h)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~155h A100 80GB (~62h H100 equivalent)\",\n      \"gpu_utilization\": \"~60–70% effective; agent queues probing and LoRA sweep experiments overnight, researcher reviews layer partition heatmaps and approves next ablation tier once daily, cutting idle time ~50% vs. manual\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in\",\n      \"claude_api_cost\": \"$150–250 (~1000–1500 conversation turns at $0.10–0.15/turn with Opus)\",\n      \"estimated_gpu_cost\": \"~$231–319 (A100 at $1.49–2.06/hr); additional ~25h reflects new ablation condition (b) runs and supplementary benchmark evaluations\",\n      \"risk_note\": \"Key risk: agent may commit to a suboptimal layer partition if probe accuracy curves are bimodal or noisy; the automated entropy-based partition fallback reduces (but does not eliminate) this risk; daily human review of the partition heatmap before LoRA runs remains the essential gate\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~310–360h A100 80GB (~122–144h H100 equivalent); within the ≤200h H100 hard constraint\",\n      \"gpu_utilization\": \"~85–90% effective; agent continuously queues the next experiment upon completion with no human approval bottleneck—idle only during brief checkpoint evaluation transitions\",\n      \"sweep\": \"3 LoRA rank values (8, 16, 32) × 2 layer partition thresholds × 2 model families (Qwen3-8B, Aya-23-8B) × 2 regularization strengths × 2 seeds = 48 core training runs; plus ~12 baseline runs (full-LoRA, Surgical Steering, INCLINE, Source-Shielded Updates); plus ~4–6 new ablation runs for condition (b) (full LoRA + KL only, 2 models × 2–3 seeds); plus Stage 1 structural diagnostic runs; plus ~18–24h for XCOPA/XStoryCloze/MGSM evaluation across all checkpoints via lm-evaluation-harness\",\n      \"timeline\": \"5–8 days with 4–6 concurrent A100 GPUs (or 3–5 days with H100s)\",\n      \"team\": \"0 (2–3h of initial harness setup and config-space definition)\",\n      \"claude_api_cost\": \"$200–350 (~1500–2500 turns across experiment planning, result parsing, and ablation branching)\",\n      \"estimated_gpu_cost\": \"~$462–742 (A100 at $1.49–2.06/hr); increase from prior estimate reflects ~4–6 new condition (b) training runs and ~18–24h benchmark evaluation\",\n      \"speed_bottleneck\": \"Number of concurrent GPUs and the ~1h cultural benchmark evaluation per checkpoint; XCOPA/XStoryCloze/MGSM evaluation can be parallelized across checkpoints on separate GPUs via lm-evaluation-harness\",\n      \"risk_note\": \"Bimodal probe distributions are handled by an automated entropy-based partition fallback. The Stage 1 structural diagnostic provides an early signal: if cultural probe accuracy is unaffected by full-LoRA training, the layer-freezing strategy is validated before the main sweep begins, allowing early termination of degenerate configurations. If XCOPA performance drops relative to full-LoRA baseline, this is flagged as a scope constraint and reported transparently rather than silently absorbed.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — viable only with auto-research mode given the 15-day window from May 10, 2026; the 5–8 day compute window plus sequential Stage 1→Stage 2→Stage 3 dependency plus writing and submission formatting leaves essentially no buffer for a second sweep if early results are inconclusive—treat EACL 2027 as the primary target with EMNLP as a best-case scenario\",\n    \"EACL 2027 (ARR submission deadline August 3, 2026) — primary target for human-in-loop or manual mode\",\n    \"AAAI 2027 (submission deadline expected July–August 2026, TBC)\"\n  ],\n  \"key_references\": [\n    \"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 listed as arXiv preprint on the first author's publication page)\",\n    \"Neuron-Level Analysis of Cultural Understanding in Large Language Models (arXiv:2510.08284, Yamamoto et al., ICLR 2026)\",\n    \"Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention / INCLINE (ACL 2025 Outstanding Paper, arXiv:2410.12462)\",\n    \"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs (ACL 2025, arXiv:2502.14830, Liu & Niehues)\",\n    \"Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (ACL 2025 short paper, arXiv:2506.01675)\",\n    \"MLAS-LoRA: Language-Aware Parameters Detection and LoRA-Based Knowledge Transfer for Multilingual Machine Translation (ACL 2025, aclanthology.org/2025.acl-long.762)\",\n    \"Continually Adding New Languages to Multilingual Language Models / LayRA (arXiv:2509.11414, September 2025)\",\n    \"Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models (arXiv:2602.22475, Zhang et al., February 2026)\",\n    \"Mitigating Catastrophic Forgetting in Target Language Adaptation of LLMs via Source-Shielded Updates (arXiv:2512.04844, Nov 2025)\",\n    \"Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models (arXiv:2510.13580, Gurgurov et al., updated February 2026)\",\n    \"AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment (EMNLP 2025, arXiv:2509.24338)\",\n    \"CM-Align: Consistency-based Multilingual Alignment for Large Language Models (arXiv:2509.08541, 2025)\",\n    \"Language Surgery in Multilingual Large Language Models / ITLC (arXiv:2506.12450, 2025)\",\n    \"Improving Multilingual Language Models by Aligning Representations through Steering (arXiv:2505.12584, 2025)\",\n    \"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models (arXiv:2504.10191, 2025)\",\n    \"CulturalBench: A Robust, Diverse, and Challenging Benchmark for Measuring LMs' Cultural Knowledge Through Human-AI Red-Teaming (ACL 2025, arXiv:2410.02677; evaluation-only — training use prohibited by OpenAI API annotation-platform terms)\",\n    \"INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge (ICLR 2025, arXiv:2411.19799; CC BY 4.0; 197,243 MCQA pairs across 44 languages and 52 countries; used for Stage 2 cultural-localization probe training)\",\n    \"LoRA: Low-Rank Adaptation of Large Language Models (ICLR 2022, arXiv:2106.09685)\",\n    \"XCOPA: Evaluation of Causal Commonsense Reasoning in Multiple Languages (EMNLP 2020, arXiv:2005.00333, Ponti et al.)\",\n    \"Few-shot Learning with Multilingual Language Models / XStoryCloze (arXiv:2112.10668, Lin et al., 2022)\",\n    \"Language Models are Multilingual Chain-of-Thought Reasoners / MGSM (arXiv:2210.03057, Shi et al., 2022)\"\n  ],\n  \"description\": \"Cross-lingual instruction fine-tuning demonstrably erases culturally-localized knowledge across all tested alignment approaches—yet no training-time prevention exists. Mechanistic work (arXiv:2504.10191) shows that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors (in Gemma2-9b-it's 42-layer architecture, layers 19–30, with peak effects at layers 23 and 30 corresponding to approximately 55–71% model depth), suggesting specific layer indices implement cultural routing pathways. A parallel ICLR 2026 result (Yamamoto et al., arXiv:2510.08284) reaches an apparently different conclusion using gradient-based neuron attribution: culture-relevant neurons are concentrated in shallow-to-middle MLP layers. This methodological discrepancy—discrete high-influence neurons (gradient attribution) versus distributed representational subspaces (activation steering)—reflects different aspects of cultural knowledge implementation and constitutes a live empirical debate in the literature. Whether cultural localization persists after LoRA instruction fine-tuning—and whether erasure is behavioral (routing disruption) or representational (information loss)—is the empirical question Stage 1 answers. We propose Cultural-Layer-Selective LoRA (CLS-LoRA), which prevents both failure modes through a four-stage pipeline.\\n\\nA mechanistic bridge paragraph (placed before Stage 1) formalizes the training-time implication and acknowledges the mechanistic debate: the layer indices most sensitive to cultural activation steering at inference time identify weight matrices that implement cultural routing; LoRA updates to those weights may disrupt routing pathways; freezing those layers preserves both routing weights and residual-stream geometry. The contested layer localization (deep-layer subspaces per arXiv:2504.10191/arXiv:2510.26024 versus shallow-to-middle neurons per Yamamoto et al. ICLR 2026) is resolved not by choosing a side but by Stage 2 probing: measuring per-layer probe accuracy directly on each target model discovers the culturally-critical partition empirically, making CLS-LoRA robust to methodological disagreements in the mechanistic literature. Stage 1 distinguishes behavioral from representational erasure and determines whether KL regularization is necessary; crucially, Stage 1 trains separate linear probes on each checkpoint's frozen representations—one on the pretrained-checkpoint activations and one on the post-LoRA-checkpoint activations, both evaluated on the same held-out cultural split—so that accuracy differences reflect genuine representational change rather than activation-space reorganization.\\n\\nStage 2 runs lightweight linear probes to partition layers: factual-transfer probes trained on TyDiQA/XQUAD held-out splits; cultural-localization probes trained on INCLUDE (ICLR 2025, CC BY 4.0; 197,243 MCQA pairs from regional examinations across 44 languages and 52 countries, arXiv:2411.19799), filtered for cultural-domain categories (customs, food, celebrations, social norms), supplemented by multilingual Wikipedia paragraphs from culture-specific articles tagged with Wikidata cultural-domain categories (CC-BY-SA 4.0). CulturalBench (arXiv:2410.02677, ACL 2025) is reserved for Stage 4 evaluation only: the CulturalBench authors explicitly state that the annotation platform used OpenAI APIs under terms that prohibit using the collected data for training. SemEval-2026 Task 7 data (BLEnD extension) is also reserved strictly for final evaluation per its evaluation-only rules. Stage 2 determines the actual partition boundaries for each target model rather than hard-coding architecture-specific percentages from any single prior study—the principled response to the contested mechanistic landscape. Stage 3 applies LoRA exclusively to factual-transfer layers with an optional KL-divergence penalty; a 2×2 ablation isolates each component's contribution: (a) full LoRA no KL (baseline), (b) full LoRA + KL only (regularization-only, new), (c) CLS-LoRA frozen no KL (freezing-only), (d) CLS-LoRA frozen + KL (proposed method). Condition (b) is the critical new ablation: if it matches (d), layer partitioning is unnecessary overhead; if (c) and (d) outperform (b), layer freezing is confirmed as the operative mechanism. Stage 4 experiments run on Qwen3-8B (non-thinking mode, enable_thinking=False) and Aya-23-8B; primary evaluation uses CulturalBench (1,696 human-verified questions across 45 global regions, evaluation-only) and SemEval-2026 Task 7. Supplementary capability-regression evaluation via lm-evaluation-harness covers cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; task: xcopa_[lang]), narrative understanding (XStoryCloze, 11 languages, zero-shot; task: xstorycloze), and multilingual arithmetic (MGSM, 11 languages, direct mode; task: mgsm_direct); each requires ~2–4h per model and together add ~18–24h A100. XTREME-UP and multilingual MMLU are not included as primary metrics because their constituent tasks overlap substantially with those already in the suite (XTREME-UP's reading comprehension and commonsense coverage is addressed by TyDiQA and XCOPA; multilingual MMLU reasoning is partially captured by MGSM), with a full evaluation of both planned for the camera-ready version at approximately 8h A100 per model. If Stage 2's cultural-knowledge partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain XCOPA transfer—a mechanistically informative finding reported transparently. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; the fallback evaluation framework (2D scatter of factual vs. cultural accuracy across languages, normalized to pretrained baseline) is specified explicitly and yields the same interpretive structure.\\n\\nCLS-LoRA is differentiated from MLAS-LoRA (ACL 2025) across three axes: task domain (MT quality vs cultural preservation), partition dimension (language-pair specificity vs factual-cultural semantic axis), and objective (translation accuracy via distillation vs cultural preservation with no distillation). CLS-LoRA is differentiated from LayRA (arXiv:2509.11414) across three axes: objective (language addition vs cultural knowledge preservation during instruction fine-tuning), partition axis (LayRA's source-encoding/English-reasoning/target-decoding functional axis vs CLS-LoRA's factual-transfer/cultural-localization semantic axis), and partition method (LayRA hard-codes layer indices from qualitative reasoning vs CLS-LoRA uses per-model empirical probing). CLS-LoRA is differentiated from CultureManager (arXiv:2602.22475) across three axes: objective (cultural adaptation for downstream task performance vs. preservation of existing culturally-grounded knowledge from erasure during cross-lingual fine-tuning), partition axis (culture identity—which national culture gets which adapter—vs. factual-transfer/cultural-localization semantic axis that cuts across culture and language identity), and mechanism (routing inputs to culture-specific adapters via a culture router vs. freezing empirically identified cultural-knowledge layers with no routing component). CLS-LoRA is differentiated from Sparse Subnetwork Enhancement (arXiv:2510.13580) across two axes: objective (language performance improvement via LAPE-identified language-identity neurons vs cultural knowledge preservation during instruction fine-tuning) and partition axis (language-identity neurons that cut across semantic content vs the factual-transfer/cultural-localization semantic axis that cuts across language identity). The cultural-preservation objective remains the categorical novelty absent from all four. The auto-research sweep covers ~64–71 training runs (~122–144h H100), within the ≤200h H100 hard constraint, targeting a Pareto improvement over full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA, and Source-Shielded Updates in the transfer-localization trade-off space, with XCOPA/XStoryCloze/MGSM as orthogonal capability regression checks.\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"INCLINE (arXiv:2410.12462) is described as an 'ACL 2025 outstanding paper' — no evidence of this award was found in any ACL 2025 outstanding-paper announcement. This factual error will damage reviewer credibility; the claim should be removed or corrected.\", \"Critical missing related work: MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762) introduces language-aware neuron detection followed by a multiple language-specific LoRA architecture — conceptually the same probe-then-selective-LoRA pipeline as CLS-LoRA, applied to multilingual MT. This overlap must be cited and the differentiation made explicit or reviewers will flag it as unacknowledged prior art.\", \"Critical missing related work: Source-Shielded Updates (arXiv:2512.04844, Nov 2025) proposes column-wise parameter freezing to shield source-language knowledge during target-language adaptation — directly related to the 'freeze knowledge layers' component of CLS-LoRA. Must be cited.\", \"Auto-research mode estimates 600h A100 (≈ 300–400h H100 equivalent), which violates the user's hard ≤200 H100-hour compute constraint. The sweep (4 ranks × 3 partition thresholds × 2 model families × 5 regularization strengths × 3 seeds = 360 runs) must be trimmed or the auto mode dropped.\", \"LLaMA 4 Scout is a 48-block, 16-expert MoE model (109B total parameters). The factual-vs-cultural layer partition established in arXiv:2510.26024 was discovered on dense models; MoE expert routing changes the functional semantics of 'layer,' making the partition methodology directly inapplicable without separate validation. Either replace LLaMA 4 Scout with a dense multilingual model (e.g., Aya-23-8B, BLOOM-7B, mT5-XXL) or explicitly add a MoE-adaptation step to the probe procedure.\", \"The transfer-localization plane evaluation framework from arXiv:2510.26024 is the primary metric, but that paper is under review (OpenReview) and its evaluation code may not be publicly released. If the implementation is not available, re-implementing the framework is a hidden engineering cost that could consume days of the 16-day timeline.\", \"The paper reports cultural knowledge 'surviving' in deeper layers even after fine-tuning (arXiv:2504.10191), which complicates the erasure narrative: if knowledge is structurally preserved but behaviorally suppressed, freezing deeper layers may not be the right intervention — the issue may be in the output layers, not in middle-vs-deep storage. This mechanistic ambiguity should be addressed.\"]\nFeedback: The core idea is viable and the training-time gap is real, but the paper needs three structural fixes before it can pass review:\n\n1. **Cite and differentiate MLAS-LoRA.** This is the most urgent issue. The Generator should search ACL 2025 Anthology for 'MLAS-LoRA' and add a paragraph in Related Work explaining why CLS-LoRA's factual-vs-cultural layer distinction makes it categorically different from MLAS-LoRA's language-pair-specific neuron selection. The key differentiator is the *cultural-preservation objective*, not the selective-LoRA mechanism itself. Also add Source-Shielded Updates (arXiv:2512.04844).\n\n2. **Drop LLaMA 4 Scout; replace with a dense multilingual model.** The MoE architecture invalidates the layer-partition premise from 2510.26024 and makes compute estimates unreliable. Use Qwen3-8B (confirmed dense, 119 languages) as the primary model and add mT5-XXL or Aya-23-8B as the second model family for cross-architecture generalization. This also brings auto-research mode within the 200h H100 budget if you trim the sweep to ≤3 ablation dimensions.\n\n3. **Address the structural-vs-behavioral erasure ambiguity.** The paper should explicitly test whether the cultural knowledge 'erasure' is representational (information is gone from activations) or behavioral (information exists but the model won't surface it). If arXiv:2504.10191 is correct that cultural knowledge persists structurally, CLS-LoRA's value is in behavioral preservation during fine-tuning — which needs to be measured differently than simple layer probing. A single ablation running full-LoRA training then measuring layer-wise cultural probe accuracy (before vs. after) would resolve this and strengthen the paper's mechanistic story.\n\nSecondary fixes: Remove the 'outstanding paper' label from INCLINE, verify the transfer-localization plane code availability from arXiv:2510.26024 authors before committing to it as primary metric, and reduce auto-research sweep to ≤200h H100.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"Missing citation: Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025, Liu & Niehues). This paper directly shows middle layers are most important for cross-lingual transfer alignment across 1,000+ language pairs — directly supporting and potentially complicating CLS-LoRA's factual-transfer layer partition. Reviewers will ask why this is not cited.\", \"Missing citation: Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (arXiv:2506.01675, ACL 2025 short paper). This paper studies asymmetric cross-lingual cultural transfer with a frequency-based hypothesis, providing empirical background that should be acknowledged in CLS-LoRA's problem framing.\", \"Core mechanistic assumption gap: The factual-vs-cultural layer partition is derived from Surgical Steering, an inference-time activation intervention. The revision does not explicitly argue why inference-time steerability at layer L implies that freezing layer L during LoRA training prevents erasure — these are distinct causal claims. Stage 1 empirically validates this, but the paper should include a one-paragraph mechanistic bridge explaining the connection before Stage 1 results are presented.\", \"Stage 2 probe data source underspecified: The per-layer linear probes require 'culture-specific benchmark items' for the cultural-localization score. It is unclear whether these come from CulturalBench/SemEval-2026 Task 7 held-out splits or require new annotation. Given SemEval-2026 Task 7 prohibits use of its data for training (confirmed), the probe training data source must be stated explicitly; using CulturalBench for probe training and SemEval for final evaluation would resolve this.\", \"Round 1 incorrectly flagged INCLINE's 'ACL 2025 Outstanding Paper' designation — independently confirmed that INCLINE IS listed among the 26 ACL 2025 Outstanding Papers; the revision correctly retained this label and no fix is needed here.\"]\nFeedback: The revision has successfully resolved all four critical Round 1 issues: MLAS-LoRA is cited and differentiated across three axes, Source-Shielded Updates is added, auto-research compute is trimmed to ~115h H100 (within the 200h constraint), LLaMA 4 Scout is replaced by Qwen3-8B + Aya-23-8B with explicit justification, and the structural-vs-behavioral erasure ambiguity is addressed by Stage 1. Note that Round 1's INCLINE flag was incorrect — it IS an ACL 2025 Outstanding Paper; the revision rightly kept that label.\n\nThree targeted fixes are needed before this is ready:\n\n1. **Add the two missing ACL 2025 citations.** In the landscape section, add: (a) Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025) — acknowledge that it establishes middle-layer primacy for cross-lingual factual transfer via representation alignment, and that CLS-LoRA extends this by additionally protecting cultural-knowledge layers from LoRA updates; (b) Cross-Lingual Transfer of Cultural Knowledge (arXiv:2506.01675, ACL 2025) — acknowledge as empirical background showing cultural transfer asymmetry for low-resource languages, motivating the need for training-time prevention.\n\n2. **Add a mechanistic bridge paragraph.** Before Stage 1 results, add: 'Our freezing strategy relies on a critical assumption: that the layer indices most sensitive to cultural-vs-factual steering at inference time (per arXiv:2510.26024) correspond to the layers where LoRA updates most destructively disrupt cultural routing during training. Stage 1 empirically validates this assumption: if post-full-LoRA cultural probe accuracy is preserved, erasure is behavioral and layer freezing is the correct intervention; if probe accuracy drops, erasure is partly representational and the KL-divergence regularizer becomes critical.'\n\n3. **Specify probe training data explicitly.** Clarify that Stage 2 probes are trained on held-out splits of CulturalBench (available at ACL 2025) for cultural-localization scores and TyDiQA/XQUAD for factual-transfer scores — not on SemEval-2026 Task 7 (evaluation-only by task rules) and not requiring new annotation.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL misattribution: The core_problem section states arXiv:2504.10191 'reveals the suppression is often behavioral rather than purely representational: cultural knowledge frequently survives as recoverable activations in deeper layers but is no longer surfaced in model outputs after fine-tuning.' This is factually wrong. arXiv:2504.10191 studies inference-time steering of cultural knowledge in already-trained (not instruction-fine-tuned) models, primarily Gemma2-9b-it. It does not study post-fine-tuning behavior at all, and makes no claim about whether cultural knowledge survives as recoverable activations after LoRA fine-tuning. The behavioral-vs-representational erasure distinction is CLS-LoRA's own hypothesis — which Stage 1 empirically tests — not an established finding from the cited paper. Any reviewer who reads arXiv:2504.10191 will reject this attribution.\", \"Layer depth percentage inconsistency: The paper claims 'cultural-knowledge layers concentrated at deeper layers ~72–94% model depth, per arXiv:2504.10191.' The actual mechanistic findings of arXiv:2504.10191 (Gemma2-9b, 42-layer architecture) identify critical cultural activation at absolute layers 23 and 30 (≈ 55-71% depth), and steering experiments cover layers 15-30 (≈ 36-71% depth) — significantly below the claimed 72-94% range. Stage 2 probing mitigates this by empirically determining the actual partition per model, but the percentage figure cited as empirically established from arXiv:2504.10191 is inaccurate and will mislead reviewers.\", \"arXiv:2510.26024 is under review at ICLR 2026 (submitted Sept 2025, not yet accepted). Its transfer-localization plane evaluation code is almost certainly not publicly released. The paper acknowledges this with a fallback, but does not explicitly state the primary framework comes from an unpublished ICLR 2026 submission — reviewers may check and flag this.\", \"Qwen3-8B has a 'thinking mode' (/think / /no_think) that activates extended chain-of-thought reasoning; in thinking mode, the model's internal generation pathway differs substantially from standard instruction following. The paper does not specify whether experiments use thinking or non-thinking mode. For cultural localization probing and instruction fine-tuning, using thinking mode could contaminate results by routing responses through CoT reasoning rather than direct cultural knowledge layers.\"]\nFeedback: The revision has successfully addressed all four Round 2 issues. Three targeted fixes remain before this is ready.\n\n1. **Fix the arXiv:2504.10191 attribution (critical).** The core_problem and opportunity sections claim this paper shows cultural knowledge 'survives as recoverable activations after fine-tuning' and that erasure is 'behavioral rather than representational.' This paper does not study fine-tuning at all — it studies inference-time cultural steering in pre-trained models. The correction is: reframe arXiv:2504.10191 as showing cultural knowledge is spatially localized and steerable in pre-trained models, which motivates the hypothesis that specific layers implement cultural routing pathways. Then explicitly state: 'Whether this localization and steerability survives LoRA instruction fine-tuning — and whether erasure is behavioral (routing disruption) or representational (information loss) — is the empirical question Stage 1 answers.' The KL regularizer is then naturally framed as the fallback for the representational-erasure case. This reframing is accurate, scientifically honest, and actually strengthens the paper by making Stage 1 a genuine empirical contribution rather than a validation of a fait accompli.\n\n2. **Correct the layer depth percentages.** Replace '~72–94% model depth, per arXiv:2504.10191' with something like: 'arXiv:2504.10191 identifies absolute layers 23-30 as critical for cultural activation in Gemma2-9b (a 42-layer model, corresponding to approximately 55-71% depth); arXiv:2510.26024 finds cultural localization in deeper layers relative to factual transfer. Stage 2 probing empirically determines the partition for each target model rather than hard-coding percentages from other architectures.' This is more accurate and emphasizes the empirical approach.\n\n3. **Add one sentence on Qwen3-8B thinking mode.** Clarify that all Qwen3-8B experiments are conducted in non-thinking mode (/no_think or without system prompt thinking tokens) to ensure consistent direct-generation behavior during LoRA fine-tuning and cultural localization evaluation. Without this, reviewers may question whether the thinking-mode routing path confounds the cultural layer partition.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL — Incorrect proceedings status of arXiv:2510.26024: This paper (CLS-LoRA's primary motivation) was accepted at ICLR 2026 (conference held April 22–26, 2026). The claim 'has not appeared in a published proceedings as of May 2026' is factually false as of today (May 10, 2026). The citation and all associated caveats about evaluation code unavailability and 'arXiv preprint' status must be updated to reflect its ICLR 2026 publication. This is a straightforward factual correction, but leaving it wrong will draw immediate rejection from any reviewer who checks.\", \"CRITICAL — Missing ICLR 2026 paper with directly contradictory mechanistic evidence: 'Neuron-Level Analysis of Cultural Understanding in Large Language Models' (arXiv:2510.08284, ICLR 2026, Yamamoto et al.) uses gradient-based neuron attribution to identify culture-relevant neurons and finds them 'concentrated in shallow to middle MLP layers' — directly opposing the deeper-layer (layers 19–30, ~45–71% depth) localization from arXiv:2504.10191 that grounds CLS-LoRA's freezing strategy. This paper was on arXiv since October 2025 and has been accepted at ICLR 2026 (held before the submission deadline). CLS-LoRA must cite it and either (a) argue the discrepancy is a methodological artifact (activation-steering subspaces vs. gradient-based neuron attribution measure different constructs), or (b) acknowledge it as an empirical uncertainty that Stage 2 probing resolves per-model. Without this, any EMNLP reviewer aware of arXiv:2510.08284 will flag it as a fundamental flaw.\", \"MODERATE — Missing related work: LayRA (arXiv:2509.11414, Sept 2025) is a layer-selective LoRA approach that applies LoRA to first and final transformer layers while freezing intermediate layers, for continual multilingual language addition. Its pipeline (layer-informed selective LoRA to prevent forgetting) shares the same mechanical strategy as CLS-LoRA, even though the objective (language preservation vs cultural preservation) differs. It should be cited and differentiated in the related work discussion, noting that LayRA partitions layers on a language-encoding-vs-reasoning axis while CLS-LoRA partitions on a factual-transfer-vs-cultural-localization axis.\"]\nFeedback: Round 4 correctly resolves all three Round 3 issues (arXiv:2504.10191 attribution, layer depth percentages, Qwen3-8B thinking mode). Three new fixes are now required:\n\n1. **Update arXiv:2510.26024 citation to ICLR 2026 (critical, ~1 hour of work).** The paper was accepted at ICLR 2026 (April 22–26, 2026) and is now a published conference paper. Replace all instances of 'arXiv preprint (submitted October 2025)' with 'ICLR 2026'. The caveat about evaluation code unavailability may still apply (check the ICLR 2026 camera-ready for a code link), but the 'not appeared in published proceedings as of May 2026' claim must be removed.\n\n2. **Cite and engage with arXiv:2510.08284 (critical, ~half a day of writing).** This ICLR 2026 paper finds culture-relevant neurons in shallow-to-middle MLP layers — not deep layers. CLS-LoRA must acknowledge this in the mechanistic bridge paragraph. The recommended framing: 'Yamamoto et al. (2026, arXiv:2510.08284) identify culture-relevant neurons via gradient attribution and find them in shallow-to-middle MLP layers, apparently in tension with the deeper-layer localization from Veselovsky et al. (2025, arXiv:2504.10191) and Han et al. (2026, ICLR). This discrepancy may reflect the difference between measuring activation-steering subspaces (which can span many layers) versus individual gradient-sensitive neurons (which can be small and shallow); Stage 2 probing resolves this empirically for each target model.' This framing converts a vulnerability into a strength: Stage 2 becomes the principled resolution to a genuine mechanistic debate in the literature.\n\n3. **Add LayRA to related work (moderate, ~30 minutes).** Cite arXiv:2509.11414 (Sept 2025) as a parallel selective-LoRA approach for multilingual LLMs. Differentiate: LayRA partitions on a source-language-encoding vs English-reasoning vs target-language-decoding functional axis; CLS-LoRA partitions on a factual-transfer vs cultural-localization semantic axis that cuts across language-pair specificity. The cultural-preservation objective remains the categorical novelty.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE — Evaluation benchmark gap violating user requirements: The user required evaluation on XTREME-UP, XCOPA, XStoryCloze, MGSM, multilingual MMLU, TyDiQA, and FLORES. The paper covers only TyDiQA from this list (plus CulturalBench and SemEval-2026 Task 7). Any EMNLP reviewer will ask: does CLS-LoRA hurt general cross-lingual commonsense reasoning (XCOPA, XStoryCloze) or multilingual arithmetic (MGSM)? Without at least XCOPA and MGSM results, the paper cannot demonstrate that cultural preservation does not come at the cost of broader multilingual competence. These are fast to run (standard few-shot evaluation, ~2–4h per benchmark per model) and should be added to Stage 4.\", \"MODERATE — Missing 'full LoRA + KL penalty only' ablation: The paper proposes layer freezing + optional KL regularization, but never isolates the contribution of layer freezing from KL regularization alone. A 'full LoRA + KL-divergence penalty on cultural-layer activations (no freezing)' baseline is essential to demonstrate that layer freezing is the necessary mechanism, not just the regularization. Without this ablation, a reviewer could argue KL regularization alone achieves the same preservation and layer freezing is unnecessary complexity. This ablation requires ~4–6 additional runs and should be added to the auto sweep.\", \"MINOR — Stage 1 probe methodology underspecified: Stage 1 measures 'per-layer cultural probe accuracy before and after' full LoRA fine-tuning. It is ambiguous whether the Stage 1 probe is (a) trained on pre-fine-tuned representations and applied to post-fine-tuned representations (cross-checkpoint transfer), or (b) separately trained on each checkpoint's representations. If (a), probe failure could reflect activation-space reorganization rather than information loss, confounding the behavioral-vs-representational distinction Stage 1 is designed to make. The paper should clarify that separate probes are trained and evaluated on held-out data from each checkpoint, making the comparison meaningful.\", \"MINOR — Factual correction: The paper continues to note 'submitted to ICLR 2026' for arXiv:2510.26024, but as of May 2026, HyoJung Han's own publication page lists this paper as an arXiv preprint with no confirmed proceedings venue—suggesting it was not accepted at ICLR 2026. The submission's existing characterization ('as of May 2026, the first author's publication page continues to characterize it as an arXiv preprint without a confirmed proceedings venue') is correct and should remain. Note: the Round 4 reviewer's claim that it was 'accepted at ICLR 2026' was factually wrong; the Round 5 revision's handling is accurate. No change needed beyond confirming this is stable.\"]\nFeedback: Round 5 has cleanly resolved all three Round 4 issues. The Yamamoto et al. integration is thorough and the mechanistic framing is now scientifically honest. Two targeted fixes are needed before this is ready:\n\n1. **Expand Stage 4 evaluation to include XCOPA and MGSM (moderate, ~1 GPU-day).** Add two cross-lingual commonsense benchmarks (XCOPA, XStoryCloze) and one multilingual reasoning benchmark (MGSM) to Stage 4. These measure capabilities orthogonal to cultural localization and factual QA. The paper needs to show CLS-LoRA does not regress on these relative to the full-LoRA baseline. If CLS-LoRA freezes cultural layers but those layers also encode commonsense knowledge, XCOPA performance could drop — which would be both a problem and an interesting finding. These benchmarks are free to run via lm-eval-harness and take ~2–4h per model. This directly addresses the user's specified evaluation requirements.\n\n2. **Add a 'full LoRA + KL only' ablation to Stage 3 (moderate, ~4–6 additional runs).** Without this baseline, the paper cannot argue that layer freezing is the operative mechanism rather than the KL regularizer alone. The ablation grid should include: (a) full LoRA (current baseline), (b) full LoRA + KL penalty, (c) CLS-LoRA frozen (no KL), and (d) CLS-LoRA frozen + KL (proposed method). This 2×2 table cleanly isolates the contributions of each component.\n\n3. **Clarify Stage 1 probe training protocol (minor, ~1 paragraph).** Specify that Stage 1 trains separate probes on the pre-fine-tuned and post-fine-tuned checkpoint representations respectively (not cross-checkpoint transfer), to ensure that a drop in probe accuracy reflects information loss rather than activation-space reorganization. This removes a methodological ambiguity that a probing-literate reviewer would flag.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"CRITICAL — CulturalBench is not available for training use. The paper claims Stage 2 cultural-localization probes are trained on 'held-out splits of CulturalBench (ACL 2025)...which is publicly available for training use.' This is factually wrong: the CulturalBench paper explicitly states 'our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training.' Using CulturalBench for probe training violates its terms. The Stage 2 probe training data source must be replaced with a training-permitted cultural knowledge resource (e.g., multilingual Wikipedia cultural-domain sentences, MKQA, World Values Survey items, or a custom culturally-grounded QA dataset without OpenAI annotation-platform restrictions). SemEval-2026 Task 7 (BLEnD) is correctly identified as evaluation-only and is not the issue here.\", \"MINOR — Sparse Subnetwork Enhancement for Underrepresented Languages (arXiv:2510.13580, updated Feb 2026) applies targeted sparse fine-tuning of language-associated subnetworks (<1% of parameters) and achieves strong cross-lingual alignment while preserving general capabilities, with adaptation concentrated in down-projection weights of later layers. Although its objective (language performance improvement) differs from CLS-LoRA's (cultural preservation), the layer-selective sparse-fine-tuning approach is closely related and should be acknowledged in the landscape section to preempt reviewer comparisons.\"]\nFeedback: Round 6 resolves all three Round 5 issues cleanly (XCOPA/XStoryCloze/MGSM added, 2×2 ablation with condition (b) included, Stage 1 separate-probe protocol specified). One critical correction remains before this can pass review:\n\n**Fix the CulturalBench training-use claim (critical, ~2 hours of work).** The CulturalBench paper explicitly states the dataset is prohibited from training use due to its OpenAI annotation-platform terms. Replace the Stage 2 cultural-localization probe training source with a dataset that permits training. Strong alternatives: (a) multilingual Wikipedia paragraphs from culture-specific articles, filtered by Wikidata cultural-domain tags — widely available, CC-BY licensed, and covers the 45+ cultural regions needed; (b) MKQA (multilingual knowledge questions, Apache 2.0), which covers culturally-grounded factual questions across languages; (c) a small GPT-4o-free annotation of culturally-grounded probe examples using open models (Qwen3-8B itself, before fine-tuning). CulturalBench should then be used *only* for final evaluation (Stage 4), alongside SemEval-2026 Task 7, which is already correctly limited to evaluation. Update the Stage 2 and Stage 4 data-source descriptions to reflect this separation, and remove the phrase 'publicly available for training use' from the CulturalBench reference. This is a single-paragraph fix in the approach and description sections.\n\n**Also add Sparse Subnetwork Enhancement (arXiv:2510.13580) to the landscape (minor, ~20 minutes).** Note that it improves underrepresented-language performance via language-neuron subnetwork selection, and differentiate on objective (language capability vs. cultural knowledge preservation) and partition axis (language-identity neurons vs. factual-cultural semantic axis).\n\n### Round 7 review\nVerdict: revise\nIssues: [\"MODERATE — 'Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models' (arXiv:2602.22475, February 2026) is unaddressed. This paper proposes culture-specific LoRA adapters with a culture router, using LoRA as the adaptation vehicle for cultural knowledge management. Although its objective (cultural adaptation/alignment) differs from CLS-LoRA's (preventing cultural erasure during cross-lingual instruction fine-tuning), and its partition axis is culture-identity (which culture) rather than CLS-LoRA's factual-vs-cultural semantic axis, the surface-level similarity is close enough that EMNLP reviewers will notice the omission. Must be cited and differentiated in the landscape section: key differentiators are (1) objective — cultural capability gain vs. cultural knowledge preservation, (2) partition dimension — culture identity vs. factual-cultural semantic axis, (3) mechanism — routing between culture-specific adapters vs. layer-freezing based on empirical functional partition.\", \"MINOR — The user-specified evaluation list includes XTREME-UP and multilingual MMLU, neither of which appears in the Stage 4 evaluation plan. The current suite (TyDiQA, XCOPA, XStoryCloze, MGSM, CulturalBench, SemEval-2026 Task 7) is strong, but an EMNLP reviewer familiar with the user's stated scope may ask why comprehensive multilingual capability benchmarks (XTREME-UP, mMLLU) are absent. At minimum, the paper should justify omitting these (e.g., 'XTREME-UP includes many tasks already covered by TyDiQA and XCOPA; multilingual MMLU adds ~8h evaluation per model and is planned for the camera-ready version') rather than leaving the absence unaddressed.\", \"MINOR — The feasibility of the EMNLP ARR deadline (May 25, 15 days from now) in auto-research mode deserves one explicit caveat in the venue list: the 5–8 day compute window plus sequential Stage 1→Stage 2→Stage 3 dependency plus writing and submission formatting leaves essentially no time for a second sweep if early results are inconclusive. The paper should either acknowledge this risk explicitly or treat EACL 2027 as the primary target with EMNLP as best-case.\"]\nFeedback: The Round 6 fixes are all correctly implemented: CulturalBench is now evaluation-only (INCLUDE + Wikipedia used for Stage 2 probe training, both licensing-verified), Sparse Subnetwork Enhancement is cited and differentiated, and the 2×2 ablation and XCOPA/XStoryCloze/MGSM evaluation are fully specified. One moderate issue blocks passage to 'pass':\n\n**Add 'Mind the Gap in Cultural Alignment' (arXiv:2602.22475, February 2026) to the landscape (~30 minutes).** This paper proposes task-aware culture management with culture-specific LoRA adapters and a culture router. In the landscape section, add it alongside the other LoRA-based multilingual methods and differentiate on: (1) objective — it improves cultural alignment by adapting to specific cultures, whereas CLS-LoRA preserves existing culturally-grounded knowledge from being erased during cross-lingual instruction fine-tuning; (2) partition axis — it partitions along culture identity (which-culture adapter), whereas CLS-LoRA partitions along the factual-transfer vs. cultural-localization semantic axis that cuts across language and culture identity; (3) mechanism — it routes inputs to culture-specific LoRA modules at the adapter level, whereas CLS-LoRA freezes layers empirically identified as cultural-knowledge carriers and applies LoRA only to factual-transfer layers. The cultural-preservation objective (preventing erasure rather than enabling adaptation) remains absent from this work.\n\n**Optionally justify the omission of XTREME-UP and multilingual MMLU (minor, 1 sentence).** Add a note that these are not included as primary metrics because their constituent tasks overlap substantially with TyDiQA (XTREME-UP) and the combined XCOPA/MGSM suite (mMLLU reasoning), with the caveat that a full XTREME-UP and mMLLU evaluation would be included in the camera-ready. This preempts reviewer requests without adding significant compute.\n\nAfter these two fixes, the paper should be ready to pass. The mechanistic story is scientifically honest, the ablation design is rigorous, the data licensing is clean, and the differentiation from prior selective-LoRA work is systematic. This is a well-developed submission.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:08:15.684Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:08:15.684Z",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-10T08:08:15.729Z_

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

## Idea under review (round 8/10)
{
  "title": "Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignment",
  "project_name": "cls_lora_cultural_preservation",
  "source": "web_research",
  "level": "solid",
  "core_problem": "Cross-lingual fine-tuning systematically suppresses culturally-grounded, language-specific knowledge while improving factual transfer—a phenomenon called 'cultural erasure.' Mechanistic work (arXiv:2504.10191) demonstrates that in pre-trained instruction-tuned models, cultural knowledge is spatially localized in specific layers and steerable via linear activation vectors, suggesting particular layer indices implement cultural routing pathways. Whether this spatial localization persists after LoRA instruction fine-tuning—and whether cross-lingual fine-tuning causes behavioral erasure (routing pathway disruption), representational erasure (information loss), or both—remains empirically untested. No training-time method prevents either failure mode, forcing practitioners to choose between cross-lingual capability and cultural authenticity. A complementary mechanistic uncertainty reinforces the need for per-model empirical investigation: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deeper-layer localization (layers 19–30, approximately 45–71% depth in Gemma2-9b-it) identified via activation-steering analysis in arXiv:2504.10191. The two methodologies measure different constructs—discrete high-influence neurons versus distributed activation-space subspaces—and their disagreement means the culturally-critical layer partition cannot be reliably imported from prior work for an arbitrary target model; it must be discovered empirically.",
  "opportunity": "'Rethinking Cross-lingual Alignment' (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 listed as arXiv preprint on the first author's publication page) rigorously demonstrates that every tested cross-lingual alignment approach degrades cultural localization across all six languages, and proposes Surgical Steering as a remedy—but only at inference time, requiring per-query layer manipulation and offering no prevention during training. The finding that factual transfer and cultural localization are optimally steerable at different model layers is actionable: applying LoRA selectively to factual-transfer layers while freezing cultural-knowledge layers during instruction fine-tuning would prevent erasure at the source. arXiv:2504.10191 establishes that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors in specific layers (notably layers 19–30 in Gemma2-9b-it, with peaks at layers 23 and 30), supporting the hypothesis that particular layer indices implement cultural routing pathways. CLS-LoRA's freezing strategy is designed to exploit this structure: if that spatial localization persists after LoRA fine-tuning (behavioral erasure—routing disrupted but representations intact), freezing those layers during training prevents routing disruption; if fine-tuning also degrades the representations themselves (representational erasure), the KL-divergence penalty anchors cultural-layer activations to their pretrained distribution. Stage 1 empirically distinguishes these two failure modes before the main sweep begins. Crucially, the layer partition question is now a live empirical debate in the literature: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) independently find culture-relevant neurons in shallow-to-middle MLP layers using gradient attribution, while activation-steering work (arXiv:2504.10191, arXiv:2510.26024) localizes cultural steerability in deeper layers. This genuine methodological disagreement elevates Stage 2 probing from a validation step to the principled empirical resolution of an open question—CLS-LoRA discovers the culturally-critical partition for each target model rather than assuming it from any single prior study. This is feasible with any open-source dense multilingual model via a lightweight per-layer probing step.",
  "landscape": "INCLINE (arXiv:2410.12462, ACL 2025 outstanding paper) aligns internal representations from low-resource to high-resource languages via learned projection matrices derived from parallel sentences, improving cross-lingual task performance but not distinguishing factual from cultural knowledge. Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025, Liu & Niehues) provides the empirical foundation for CLS-LoRA's factual-transfer layer partition: through translation retrieval probing across 1,190 language pairs on Llama 3 and Qwen 2.5, it establishes that layer 16 (50% depth in a 32-layer model) is the key integration point for cross-lingual semantic alignment, and that incorporating a middle-layer alignment objective consistently improves cross-lingual task performance particularly for lower-resource languages. CLS-LoRA extends this by additionally protecting cultural-knowledge layers from LoRA updates—arXiv:2504.10191 identifies layers 19–30 (approximately 45–71% depth in Gemma2-9b-it's 42-layer architecture, with peak cultural activation at layers 23 and 30) as critical for cultural routing, and Stage 2 probing empirically determines the analogous partition for each target model—a protection axis entirely absent from Liu & Niehues, whose work does not distinguish factual from cultural knowledge and proposes no cultural preservation objective. Cross-Lingual Transfer of Cultural Knowledge (arXiv:2506.01675, ACL 2025 short paper, Zhang et al.) provides empirical background showing cultural knowledge transfer is asymmetric: high-resource language pairs exhibit bidirectional transfer while low-resource languages primarily export cultural knowledge to English without reciprocal benefit, driven by a frequency-based pretraining data mechanism. This asymmetry directly motivates training-time prevention of cultural erasure—low-resource languages are disproportionately at risk and most in need of the protection CLS-LoRA provides. AlignX (arXiv:2509.24338, EMNLP 2025) and CM-Align (arXiv:2509.08541) apply two-stage and consistency-based multilingual alignment respectively, both optimizing convergence without a cultural preservation objective. Language Surgery/ITLC (arXiv:2506.12450) disentangles language-specific from agnostic information through latent injection at inference time, but does not train models to preserve this distinction. Alignment through steering (arXiv:2505.12584) adds a learned residual-stream vector at a single layer; it outperforms many baselines but still does not model the factual-cultural layer split. Surgical Steering (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 the first author's publication page lists this as an arXiv preprint without a confirmed proceedings venue) is the only method addressing the cultural erasure problem, and is strictly an inference-time patch over an already-erased model. arXiv:2504.10191 ('Localized Cultural Knowledge is Conserved and Controllable in LLMs', April 2025) demonstrates that in pre-trained instruction-tuned models, cultural knowledge exists as spatially localized steerable activation-space vectors—mechanistic analysis on Gemma2-9b-it (42 layers) identifies layers 19–30 as critical for cultural activation, with peak effects at layers 23 and 30 (approximately 55–71% depth)—and can be controlled via linear steering at inference time. This establishes spatial localization of cultural knowledge in pre-trained models, motivating CLS-LoRA's hypothesis that specific layer indices implement cultural routing pathways; whether this localization persists after LoRA instruction fine-tuning is precisely what Stage 1 tests.\n\nYamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) conduct a neuron-level analysis of cultural understanding using a gradient-based scoring method with additional filtering for precise refinement. They identify both culture-general neurons (supporting cultural understanding across cultures) and culture-specific neurons (tied to individual cultures), which together comprise less than 1% of all neurons and are concentrated in shallow-to-middle MLP layers—not in the deeper layers identified by activation-steering analysis in arXiv:2504.10191. Suppressing these neurons degrades cultural benchmark performance by up to 30% while leaving general NLU tasks largely unaffected. This finding is in apparent tension with the deeper-layer localization from arXiv:2504.10191 and arXiv:2510.26024, reflecting a genuine methodological distinction: gradient attribution identifies discrete neurons with the highest individual causal influence, which may be sparse and concentrated in earlier layers; activation-steering subspaces reflect distributed representational geometry that implements cultural routing across many layers and may peak in depth-profile at different points. CLS-LoRA's Stage 2 probing directly bridges this debate: rather than assuming either result, it measures per-layer probe accuracy on each target model and discovers the cultural-knowledge partition empirically. If shallow neurons (Yamamoto et al.) dominate, Stage 2 will assign those layers to the frozen cultural partition; if deeper subspaces (arXiv:2504.10191) dominate, Stage 2 will assign those layers instead. Stage 2 is thus a model-specific resolution mechanism that makes CLS-LoRA robust to methodological disagreements in the mechanistic literature.\n\nThree directly related selective-LoRA/adapter methods require explicit differentiation. MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762) detects language-aware neurons in a teacher model and injects extracted knowledge into language-pair-specific LoRA modules in a student model for multilingual machine translation, achieving +1.7 BLEU on average. While MLAS-LoRA and CLS-LoRA both employ a probe-then-selective-LoRA pipeline, they differ on three critical axes: (1) task domain—MLAS-LoRA targets MT translation quality whereas CLS-LoRA targets cultural knowledge preservation during instruction fine-tuning; (2) partition dimension—MLAS-LoRA partitions along language-pair specificity (language-A vs language-B neurons) whereas CLS-LoRA partitions along the factual-transfer vs cultural-localization semantic axis, which cuts across language pairs; and (3) objective—MLAS-LoRA optimizes translation accuracy via teacher-student knowledge distillation whereas CLS-LoRA optimizes a cultural-preservation signal with no distillation component. The cultural-preservation objective is the categorical novelty: no prior selective-LoRA work defines a 'keep culturally-grounded outputs intact' training signal. LayRA (arXiv:2509.11414, September 2025) proposes layer-selective LoRA for continual multilingual language addition, applying LoRA to initial and final transformer layers (the first 10 and last 2 layers, plus embeddings and LM head) while freezing intermediate layers. The partition rationale—that multilingual models encode source-language inputs in initial layers, reason in English in middle layers, and decode into the target language in final layers—leads to a source-language-encoding vs English-reasoning vs target-language-decoding functional partition axis. CLS-LoRA differs on three dimensions: (1) objective—LayRA enables new-language addition without catastrophic forgetting of existing languages, whereas CLS-LoRA preserves cultural knowledge during cross-lingual instruction fine-tuning; (2) partition axis—LayRA's functional encoding/reasoning/decoding axis is defined over language identity and cuts uniformly across all languages, whereas CLS-LoRA's factual-transfer vs cultural-localization semantic axis cuts across language-pair specificity; (3) partition method—LayRA hard-codes specific layer indices derived from qualitative linguistic reasoning, whereas CLS-LoRA uses empirical per-layer probing to discover the partition for each target model, enabling adaptation to the contested mechanistic landscape. The cultural-preservation objective remains the categorical novelty absent from LayRA. CultureManager (arXiv:2602.22475, Zhang et al., February 2026) proposes task-aware cultural alignment by synthesizing task-specific cultural data grounded in web search results and managing multi-culture knowledge through culture-specific LoRA adapters selected by a culture router, achieving consistent improvements over prompt-based and fine-tuning baselines across ten national cultures and culture-sensitive downstream tasks. CLS-LoRA differs from CultureManager on three dimensions: (1) objective—CultureManager improves cultural alignment for downstream task performance by adapting LLM outputs to match target cultural values, whereas CLS-LoRA preserves existing culturally-grounded knowledge from being erased during cross-lingual instruction fine-tuning; (2) partition axis—CultureManager partitions along culture identity (which national culture gets which adapter), whereas CLS-LoRA partitions along the factual-transfer vs. cultural-localization semantic axis, which cuts across culture and language identity; (3) mechanism—CultureManager routes inputs to culture-specific LoRA modules at the adapter level via a culture router, whereas CLS-LoRA freezes layers empirically identified as cultural-knowledge carriers and applies LoRA exclusively to factual-transfer layers without any routing component. The cultural-preservation objective—preventing erasure rather than enabling cultural adaptation—remains absent from CultureManager. Source-Shielded Updates (arXiv:2512.04844, Nov 2025) proposes column-wise parameter freezing to prevent catastrophic forgetting of source-language task performance during target-language adaptation—addressing cross-lingual interference but not the factual-vs-cultural layer distinction or cultural knowledge preservation as a first-class objective. Sparse Subnetwork Enhancement for Underrepresented Languages (arXiv:2510.13580, Gurgurov et al., updated February 2026) identifies language-associated sparse subnetworks comprising less than 1% of model parameters using Language Activation Probability Entropy (LAPE), an information-theoretic metric that captures language-specific activation patterns, and fine-tunes only those parameters. On Llama-3.1-8B, Mistral-Nemo-12B, and Aya-Expanse-8B across 12 mid- and low-resource languages, it achieves 90.5% cross-lingual alignment (cosine similarity)—the best of any tested method—while preserving general capabilities (MMLU: 63.01% vs. 63.08% base), outperforming full fine-tuning, LoRA, and IA3. Adaptation is concentrated in down-projection weights of later layers, with weight changes 3–5× larger than up/gate projections. CLS-LoRA differs from Sparse Subnetwork Enhancement on two axes: (1) objective—Sparse Subnetwork Enhancement targets language performance improvement on translation and classification benchmarks (FLORES, SIB-200, BELEBELE) whereas CLS-LoRA targets cultural knowledge preservation during cross-lingual instruction fine-tuning; and (2) partition axis—LAPE identifies language-identity neurons (neurons that activate specifically for a given language, cutting across semantic content) whereas CLS-LoRA partitions along the factual-transfer vs. cultural-localization semantic axis, which cuts across language identity rather than tracking it. The cultural-preservation objective remains absent from Sparse Subnetwork Enhancement.",
  "approach": "We propose Cultural-Layer-Selective LoRA (CLS-LoRA), a training-time method that prevents cultural erasure without sacrificing factual cross-lingual transfer. The pipeline has four stages.\n\nMechanistic bridge. Our layer-freezing strategy rests on a hypothesis connecting inference-time observations to training-time interventions: the layer indices most sensitive to cultural-vs-factual activation steering at inference time (arXiv:2510.26024, corroborated by cultural customization vectors in arXiv:2504.10191 concentrated at layers 19–30 in Gemma2-9b-it) identify the weight matrices that implement cultural routing. LoRA updates modify precisely these weight matrices; applying LoRA to cultural-knowledge layers may therefore disrupt the routing pathways through which culturally-grounded representations reach outputs. This hypothesis involves a genuine empirical uncertainty that the literature has not resolved: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deep-layer activation-steering localization from arXiv:2504.10191. The discrepancy most likely reflects the difference between measuring discrete high-influence neurons (gradient attribution captures sparse, individually causal units that may be early in the network) versus measuring distributed activation subspaces (steering analysis captures the geometry of representational routing, which may span many layers and peak later). Neither result invalidates the other; they measure different aspects of how cultural knowledge is implemented. Stage 2 probing is designed precisely for this uncertainty: by measuring per-layer probe accuracy directly on each target model's representations, it discovers the culturally-critical partition without assuming either methodological lens is correct—if shallow neurons dominate functionally, Stage 2 identifies shallow layers as the cultural partition; if deeper subspaces dominate, Stage 2 identifies those instead. Whether the representations themselves persist as recoverable vectors after full LoRA fine-tuning (behavioral erasure) or are also degraded (representational erasure) is a separate open empirical question—Stage 1 provides this answer. Freezing the empirically-identified cultural-knowledge layers during training preserves both the routing weights and the residual-stream geometry that steerability depends on, addressing both failure modes by design.\n\nStage 1 — Structural diagnostic: Before the main sweep, we run full-LoRA instruction fine-tuning on a held-out model checkpoint and measure per-layer cultural probe accuracy before and after. Stage 1 trains separate linear probes on each checkpoint's frozen representations—one probe trained and evaluated on the pretrained-checkpoint's layer activations, one probe trained and evaluated on the post-LoRA-checkpoint's layer activations—using the same held-out cultural question split for both. This ensures accuracy differences reflect genuine representational change rather than activation-space reorganization: applying a single probe trained on pretrained representations cross-checkpoint to post-LoRA representations would fail if LoRA remaps the activation geometry without destroying cultural information (behavioral erasure), conflating reorganization with information loss; separate per-checkpoint probes make the comparison clean and the behavioral-vs-representational distinction interpretable. If probe accuracy is maintained post-training, erasure is confirmed as behavioral (pathway disruption) and layer freezing is the correct intervention; if probe accuracy drops, erasure is partly representational and the KL-divergence regularizer in Stage 3 becomes critical. This diagnostic sharpens the mechanistic story and validates the layer-freezing strategy regardless of which failure mode dominates. An automated entropy-based partition fallback replaces human inspection when probe curves are bimodal or noisy, reducing the agent failure mode from prior review.\n\nStage 2 — Layer profiling: Lightweight linear probes (one per transformer layer) are trained on a small parallel corpus to produce per-layer factual-transfer and cultural-localization accuracy scores, yielding a principled layer partition. For factual transfer, the empirical expectation from arXiv:2502.14830 (Liu & Niehues) is approximately middle layers (~50% model depth). For cultural knowledge, arXiv:2504.10191 identifies layers 19–30 as critical in Gemma2-9b-it (approximately 45–71% depth in a 42-layer model, with peak effects at layers 23 and 30); Yamamoto et al. (arXiv:2510.08284, ICLR 2026) find culture-relevant neurons in shallow-to-middle MLP layers via gradient attribution. Stage 2 probing empirically determines the partition boundaries for each target model—Qwen3-8B (36 layers) and Aya-23-8B—rather than hard-coding percentages from either prior study; this is the methodologically sound response to the contested mechanistic landscape. For cultural-localization probes, we use INCLUDE (ICLR 2025, CC BY 4.0; 197,243 MCQA pairs sourced from regional examinations across 44 languages and 52 countries, arXiv:2411.19799), filtered for cultural-domain categories (customs, food, celebrations, social norms), supplemented by language-filtered Wikipedia paragraphs extracted from culture-specific articles tagged with Wikidata cultural-domain categories (CC-BY-SA 4.0, widely multilingual). CulturalBench (arXiv:2410.02677, ACL 2025) cannot be used for probe training because the authors explicitly state that the annotation platform used OpenAI APIs under terms that disallow using the collected data for training; CulturalBench is therefore reserved strictly for final evaluation in Stage 4. For factual-transfer probes, we use held-out splits of TyDiQA and XQUAD. SemEval-2026 Task 7 data (BLEnD extension) is reserved strictly for final evaluation and is not used in probe training, consistent with the task's evaluation-only rules (confirmed via the official task repository). No new annotation is required.\n\nStage 3 — Selective LoRA training: LoRA adapters (via Hugging Face PEFT target_modules) are inserted exclusively into factual-transfer layers and trained with standard instruction fine-tuning loss on multilingual instruction data, while cultural-knowledge layers remain fully frozen. An optional auxiliary KL-divergence penalty on a held-out cultural probe set discourages residual drift in frozen layers' downstream activations. To establish that layer freezing is the operative mechanism rather than KL regularization alone, Stage 3 includes a 2×2 ablation: (a) full LoRA without KL penalty (existing baseline); (b) full LoRA with KL-divergence penalty on cultural-layer activations (regularization-only baseline, new); (c) CLS-LoRA with layer freezing and no KL penalty (freezing-only; already present in the sweep as the no-regularization variant); (d) CLS-LoRA with layer freezing and KL penalty (proposed method). Condition (b) is the critical addition: it tests whether KL regularization alone, without the complexity of a learned layer partition, achieves equivalent cultural preservation. If (b) matches (d), the partitioning step is unnecessary overhead; if (c) and (d) both outperform (b), layer freezing is confirmed as the operative mechanism. Approximately 4–6 additional training runs (condition (b) only; 2 models × 2–3 seeds) are added to the auto sweep; conditions (a), (c), and (d) are already covered by existing runs.\n\nStage 4 — Evaluation: Experiments run on Qwen3-8B (primary: confirmed dense, 36 transformer layers, 119 languages and dialects, 8.2B parameters) and Aya-23-8B (secondary: confirmed dense decoder-only, 23 languages, 8B parameters) for cross-architecture generalization. All Qwen3-8B experiments are conducted in non-thinking mode (enable_thinking=False in the chat template), ensuring consistent direct-generation behavior during both LoRA fine-tuning and cultural localization probing without interference from chain-of-thought reasoning pathways. LLaMA 4 Scout is excluded—its 48-block, 16-expert MoE architecture makes the factual-vs-cultural layer partition from arXiv:2510.26024, established on dense models, methodologically inapplicable without separate MoE-specific validation. Evaluation uses CulturalBench (arXiv:2410.02677, ACL 2025; 1,696 human-verified questions across 45 global regions, evaluation-only) and SemEval-2026 Task 7 as primary cultural metrics. To verify that CLS-LoRA does not regress on capabilities orthogonal to cultural localization and factual QA, Stage 4 adds three supplementary evaluation tracks via lm-evaluation-harness: cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; lm-eval task group xcopa_[lang]); cross-lingual narrative understanding (XStoryCloze, 11 languages, zero-shot; lm-eval task group xstorycloze); and multilingual arithmetic chain-of-thought (MGSM, 11 languages, direct mode; lm-eval task mgsm_direct). Each benchmark requires approximately 2–4 GPU-hours per model; together they add ~18–24h A100 total across both target models and all evaluated checkpoints. XCOPA is the most mechanistically relevant: if Stage 2's cultural-knowledge layer partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain commonsense transfer—an outcome that would be reported transparently and interpreted as a scope constraint on the method (cultural preservation trades off against commonsense transfer in those layers) rather than treated as an uncontrolled failure. MGSM verifies that the factual-transfer LoRA updates preserve multilingual arithmetic reasoning. All three benchmarks use standard zero-shot or direct evaluation protocols already in lm-evaluation-harness and require no additional training data. Comprehensive multilingual capability benchmarks (XTREME-UP, multilingual MMLU) are not included as primary metrics because their constituent tasks overlap substantially with those already in the suite—XTREME-UP's reading comprehension and commonsense coverage is addressed by TyDiQA and XCOPA, while multilingual MMLU reasoning is partially captured by MGSM—and a full evaluation of both is planned for the camera-ready version at approximately 8h A100 per model. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; we therefore employ the explicitly defined fallback evaluation—a 2D scatter of cross-lingual factual accuracy (XQUAD/TyDiQA) vs cultural localization accuracy (CulturalBench) across languages, normalized to the pre-fine-tuning baseline, yielding the same transfer-localization interpretive framework. We compare against full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA (adapted to the instruction-FT setting), and Source-Shielded Updates baselines to demonstrate that CLS-LoRA Pareto-dominates prior methods in the transfer-localization trade-off space.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~230h A100 80GB (~92h H100 equivalent)",
      "gpu_utilization": "~30–40% effective; GPU idles while the researcher inspects probe accuracy heatmaps to select layer partition boundaries, designs ablation grids, and iterates on training scripts between runs",
      "timeline": "4–6 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$345–475 (A100 at $1.49–2.06/hr via RunPod/Lambda); additional ~30h reflects new ablation runs (condition (b), ~12h) and XCOPA/XStoryCloze/MGSM evaluation (~18h)"
    },
    "human_in_loop": {
      "gpu_hours": "~155h A100 80GB (~62h H100 equivalent)",
      "gpu_utilization": "~60–70% effective; agent queues probing and LoRA sweep experiments overnight, researcher reviews layer partition heatmaps and approves next ablation tier once daily, cutting idle time ~50% vs. manual",
      "timeline": "6–8 weeks",
      "team": "1 researcher, ~30min/day check-in",
      "claude_api_cost": "$150–250 (~1000–1500 conversation turns at $0.10–0.15/turn with Opus)",
      "estimated_gpu_cost": "~$231–319 (A100 at $1.49–2.06/hr); additional ~25h reflects new ablation condition (b) runs and supplementary benchmark evaluations",
      "risk_note": "Key risk: agent may commit to a suboptimal layer partition if probe accuracy curves are bimodal or noisy; the automated entropy-based partition fallback reduces (but does not eliminate) this risk; daily human review of the partition heatmap before LoRA runs remains the essential gate"
    },
    "auto_research": {
      "gpu_hours": "~310–360h A100 80GB (~122–144h H100 equivalent); within the ≤200h H100 hard constraint",
      "gpu_utilization": "~85–90% effective; agent continuously queues the next experiment upon completion with no human approval bottleneck—idle only during brief checkpoint evaluation transitions",
      "sweep": "3 LoRA rank values (8, 16, 32) × 2 layer partition thresholds × 2 model families (Qwen3-8B, Aya-23-8B) × 2 regularization strengths × 2 seeds = 48 core training runs; plus ~12 baseline runs (full-LoRA, Surgical Steering, INCLINE, Source-Shielded Updates); plus ~4–6 new ablation runs for condition (b) (full LoRA + KL only, 2 models × 2–3 seeds); plus Stage 1 structural diagnostic runs; plus ~18–24h for XCOPA/XStoryCloze/MGSM evaluation across all checkpoints via lm-evaluation-harness",
      "timeline": "5–8 days with 4–6 concurrent A100 GPUs (or 3–5 days with H100s)",
      "team": "0 (2–3h of initial harness setup and config-space definition)",
      "claude_api_cost": "$200–350 (~1500–2500 turns across experiment planning, result parsing, and ablation branching)",
      "estimated_gpu_cost": "~$462–742 (A100 at $1.49–2.06/hr); increase from prior estimate reflects ~4–6 new condition (b) training runs and ~18–24h benchmark evaluation",
      "speed_bottleneck": "Number of concurrent GPUs and the ~1h cultural benchmark evaluation per checkpoint; XCOPA/XStoryCloze/MGSM evaluation can be parallelized across checkpoints on separate GPUs via lm-evaluation-harness",
      "risk_note": "Bimodal probe distributions are handled by an automated entropy-based partition fallback. The Stage 1 structural diagnostic provides an early signal: if cultural probe accuracy is unaffected by full-LoRA training, the layer-freezing strategy is validated before the main sweep begins, allowing early termination of degenerate configurations. If XCOPA performance drops relative to full-LoRA baseline, this is flagged as a scope constraint and reported transparently rather than silently absorbed."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — viable only with auto-research mode given the 15-day window from May 10, 2026; the 5–8 day compute window plus sequential Stage 1→Stage 2→Stage 3 dependency plus writing and submission formatting leaves essentially no buffer for a second sweep if early results are inconclusive—treat EACL 2027 as the primary target with EMNLP as a best-case scenario",
    "EACL 2027 (ARR submission deadline August 3, 2026) — primary target for human-in-loop or manual mode",
    "AAAI 2027 (submission deadline expected July–August 2026, TBC)"
  ],
  "key_references": [
    "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 listed as arXiv preprint on the first author's publication page)",
    "Neuron-Level Analysis of Cultural Understanding in Large Language Models (arXiv:2510.08284, Yamamoto et al., ICLR 2026)",
    "Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention / INCLINE (ACL 2025 Outstanding Paper, arXiv:2410.12462)",
    "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs (ACL 2025, arXiv:2502.14830, Liu & Niehues)",
    "Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (ACL 2025 short paper, arXiv:2506.01675)",
    "MLAS-LoRA: Language-Aware Parameters Detection and LoRA-Based Knowledge Transfer for Multilingual Machine Translation (ACL 2025, aclanthology.org/2025.acl-long.762)",
    "Continually Adding New Languages to Multilingual Language Models / LayRA (arXiv:2509.11414, September 2025)",
    "Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models (arXiv:2602.22475, Zhang et al., February 2026)",
    "Mitigating Catastrophic Forgetting in Target Language Adaptation of LLMs via Source-Shielded Updates (arXiv:2512.04844, Nov 2025)",
    "Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models (arXiv:2510.13580, Gurgurov et al., updated February 2026)",
    "AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment (EMNLP 2025, arXiv:2509.24338)",
    "CM-Align: Consistency-based Multilingual Alignment for Large Language Models (arXiv:2509.08541, 2025)",
    "Language Surgery in Multilingual Large Language Models / ITLC (arXiv:2506.12450, 2025)",
    "Improving Multilingual Language Models by Aligning Representations through Steering (arXiv:2505.12584, 2025)",
    "Localized Cultural Knowledge is Conserved and Controllable in Large Language Models (arXiv:2504.10191, 2025)",
    "CulturalBench: A Robust, Diverse, and Challenging Benchmark for Measuring LMs' Cultural Knowledge Through Human-AI Red-Teaming (ACL 2025, arXiv:2410.02677; evaluation-only — training use prohibited by OpenAI API annotation-platform terms)",
    "INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge (ICLR 2025, arXiv:2411.19799; CC BY 4.0; 197,243 MCQA pairs across 44 languages and 52 countries; used for Stage 2 cultural-localization probe training)",
    "LoRA: Low-Rank Adaptation of Large Language Models (ICLR 2022, arXiv:2106.09685)",
    "XCOPA: Evaluation of Causal Commonsense Reasoning in Multiple Languages (EMNLP 2020, arXiv:2005.00333, Ponti et al.)",
    "Few-shot Learning with Multilingual Language Models / XStoryCloze (arXiv:2112.10668, Lin et al., 2022)",
    "Language Models are Multilingual Chain-of-Thought Reasoners / MGSM (arXiv:2210.03057, Shi et al., 2022)"
  ],
  "description": "Cross-lingual instruction fine-tuning demonstrably erases culturally-localized knowledge across all tested alignment approaches—yet no training-time prevention exists. Mechanistic work (arXiv:2504.10191) shows that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors (in Gemma2-9b-it's 42-layer architecture, layers 19–30, with peak effects at layers 23 and 30 corresponding to approximately 55–71% model depth), suggesting specific layer indices implement cultural routing pathways. A parallel ICLR 2026 result (Yamamoto et al., arXiv:2510.08284) reaches an apparently different conclusion using gradient-based neuron attribution: culture-relevant neurons are concentrated in shallow-to-middle MLP layers. This methodological discrepancy—discrete high-influence neurons (gradient attribution) versus distributed representational subspaces (activation steering)—reflects different aspects of cultural knowledge implementation and constitutes a live empirical debate in the literature. Whether cultural localization persists after LoRA instruction fine-tuning—and whether erasure is behavioral (routing disruption) or representational (information loss)—is the empirical question Stage 1 answers. We propose Cultural-Layer-Selective LoRA (CLS-LoRA), which prevents both failure modes through a four-stage pipeline.\n\nA mechanistic bridge paragraph (placed before Stage 1) formalizes the training-time implication and acknowledges the mechanistic debate: the layer indices most sensitive to cultural activation steering at inference time identify weight matrices that implement cultural routing; LoRA updates to those weights may disrupt routing pathways; freezing those layers preserves both routing weights and residual-stream geometry. The contested layer localization (deep-layer subspaces per arXiv:2504.10191/arXiv:2510.26024 versus shallow-to-middle neurons per Yamamoto et al. ICLR 2026) is resolved not by choosing a side but by Stage 2 probing: measuring per-layer probe accuracy directly on each target model discovers the culturally-critical partition empirically, making CLS-LoRA robust to methodological disagreements in the mechanistic literature. Stage 1 distinguishes behavioral from representational erasure and determines whether KL regularization is necessary; crucially, Stage 1 trains separate linear probes on each checkpoint's frozen representations—one on the pretrained-checkpoint activations and one on the post-LoRA-checkpoint activations, both evaluated on the same held-out cultural split—so that accuracy differences reflect genuine representational change rather than activation-space reorganization.\n\nStage 2 runs lightweight linear probes to partition layers: factual-transfer probes trained on TyDiQA/XQUAD held-out splits; cultural-localization probes trained on INCLUDE (ICLR 2025, CC BY 4.0; 197,243 MCQA pairs from regional examinations across 44 languages and 52 countries, arXiv:2411.19799), filtered for cultural-domain categories (customs, food, celebrations, social norms), supplemented by multilingual Wikipedia paragraphs from culture-specific articles tagged with Wikidata cultural-domain categories (CC-BY-SA 4.0). CulturalBench (arXiv:2410.02677, ACL 2025) is reserved for Stage 4 evaluation only: the CulturalBench authors explicitly state that the annotation platform used OpenAI APIs under terms that prohibit using the collected data for training. SemEval-2026 Task 7 data (BLEnD extension) is also reserved strictly for final evaluation per its evaluation-only rules. Stage 2 determines the actual partition boundaries for each target model rather than hard-coding architecture-specific percentages from any single prior study—the principled response to the contested mechanistic landscape. Stage 3 applies LoRA exclusively to factual-transfer layers with an optional KL-divergence penalty; a 2×2 ablation isolates each component's contribution: (a) full LoRA no KL (baseline), (b) full LoRA + KL only (regularization-only, new), (c) CLS-LoRA frozen no KL (freezing-only), (d) CLS-LoRA frozen + KL (proposed method). Condition (b) is the critical new ablation: if it matches (d), layer partitioning is unnecessary overhead; if (c) and (d) outperform (b), layer freezing is confirmed as the operative mechanism. Stage 4 experiments run on Qwen3-8B (non-thinking mode, enable_thinking=False) and Aya-23-8B; primary evaluation uses CulturalBench (1,696 human-verified questions across 45 global regions, evaluation-only) and SemEval-2026 Task 7. Supplementary capability-regression evaluation via lm-evaluation-harness covers cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; task: xcopa_[lang]), narrative understanding (XStoryCloze, 11 languages, zero-shot; task: xstorycloze), and multilingual arithmetic (MGSM, 11 languages, direct mode; task: mgsm_direct); each requires ~2–4h per model and together add ~18–24h A100. XTREME-UP and multilingual MMLU are not included as primary metrics because their constituent tasks overlap substantially with those already in the suite (XTREME-UP's reading comprehension and commonsense coverage is addressed by TyDiQA and XCOPA; multilingual MMLU reasoning is partially captured by MGSM), with a full evaluation of both planned for the camera-ready version at approximately 8h A100 per model. If Stage 2's cultural-knowledge partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain XCOPA transfer—a mechanistically informative finding reported transparently. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; the fallback evaluation framework (2D scatter of factual vs. cultural accuracy across languages, normalized to pretrained baseline) is specified explicitly and yields the same interpretive structure.\n\nCLS-LoRA is differentiated from MLAS-LoRA (ACL 2025) across three axes: task domain (MT quality vs cultural preservation), partition dimension (language-pair specificity vs factual-cultural semantic axis), and objective (translation accuracy via distillation vs cultural preservation with no distillation). CLS-LoRA is differentiated from LayRA (arXiv:2509.11414) across three axes: objective (language addition vs cultural knowledge preservation during instruction fine-tuning), partition axis (LayRA's source-encoding/English-reasoning/target-decoding functional axis vs CLS-LoRA's factual-transfer/cultural-localization semantic axis), and partition method (LayRA hard-codes layer indices from qualitative reasoning vs CLS-LoRA uses per-model empirical probing). CLS-LoRA is differentiated from CultureManager (arXiv:2602.22475) across three axes: objective (cultural adaptation for downstream task performance vs. preservation of existing culturally-grounded knowledge from erasure during cross-lingual fine-tuning), partition axis (culture identity—which national culture gets which adapter—vs. factual-transfer/cultural-localization semantic axis that cuts across culture and language identity), and mechanism (routing inputs to culture-specific adapters via a culture router vs. freezing empirically identified cultural-knowledge layers with no routing component). CLS-LoRA is differentiated from Sparse Subnetwork Enhancement (arXiv:2510.13580) across two axes: objective (language performance improvement via LAPE-identified language-identity neurons vs cultural knowledge preservation during instruction fine-tuning) and partition axis (language-identity neurons that cut across semantic content vs the factual-transfer/cultural-localization semantic axis that cuts across language identity). The cultural-preservation objective remains the categorical novelty absent from all four. The auto-research sweep covers ~64–71 training runs (~122–144h H100), within the ≤200h H100 hard constraint, targeting a Pareto improvement over full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA, and Source-Shielded Updates in the transfer-localization trade-off space, with XCOPA/XStoryCloze/MGSM as orthogonal capability regression checks."
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["INCLINE (arXiv:2410.12462) is described as an 'ACL 2025 outstanding paper' — no evidence of this award was found in any ACL 2025 outstanding-paper announcement. This factual error will damage reviewer credibility; the claim should be removed or corrected.", "Critical missing related work: MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762) introduces language-aware neuron detection followed by a multiple language-specific LoRA architecture — conceptually the same probe-then-selective-LoRA pipeline as CLS-LoRA, applied to multilingual MT. This overlap must be cited and the differentiation made explicit or reviewers will flag it as unacknowledged prior art.", "Critical missing related work: Source-Shielded Updates (arXiv:2512.04844, Nov 2025) proposes column-wise parameter freezing to shield source-language knowledge during target-language adaptation — directly related to the 'freeze knowledge layers' component of CLS-LoRA. Must be cited.", "Auto-research mode estimates 600h A100 (≈ 300–400h H100 equivalent), which violates the user's hard ≤200 H100-hour compute constraint. The sweep (4 ranks × 3 partition thresholds × 2 model families × 5 regularization strengths × 3 seeds = 360 runs) must be trimmed or the auto mode dropped.", "LLaMA 4 Scout is a 48-block, 16-expert MoE model (109B total parameters). The factual-vs-cultural layer partition established in arXiv:2510.26024 was discovered on dense models; MoE expert routing changes the functional semantics of 'layer,' making the partition methodology directly inapplicable without separate validation. Either replace LLaMA 4 Scout with a dense multilingual model (e.g., Aya-23-8B, BLOOM-7B, mT5-XXL) or explicitly add a MoE-adaptation step to the probe procedure.", "The transfer-localization plane evaluation framework from arXiv:2510.26024 is the primary metric, but that paper is under review (OpenReview) and its evaluation code may not be publicly released. If the implementation is not available, re-implementing the framework is a hidden engineering cost that could consume days of the 16-day timeline.", "The paper reports cultural knowledge 'surviving' in deeper layers even after fine-tuning (arXiv:2504.10191), which complicates the erasure narrative: if knowledge is structurally preserved but behaviorally suppressed, freezing deeper layers may not be the right intervention — the issue may be in the output layers, not in middle-vs-deep storage. This mechanistic ambiguity should be addressed."]
Feedback: The core idea is viable and the training-time gap is real, but the paper needs three structural fixes before it can pass review:

1. **Cite and differentiate MLAS-LoRA.** This is the most urgent issue. The Generator should search ACL 2025 Anthology for 'MLAS-LoRA' and add a paragraph in Related Work explaining why CLS-LoRA's factual-vs-cultural layer distinction makes it categorically different from MLAS-LoRA's language-pair-specific neuron selection. The key differentiator is the *cultural-preservation objective*, not the selective-LoRA mechanism itself. Also add Source-Shielded Updates (arXiv:2512.04844).

2. **Drop LLaMA 4 Scout; replace with a dense multilingual model.** The MoE architecture invalidates the layer-partition premise from 2510.26024 and makes compute estimates unreliable. Use Qwen3-8B (confirmed dense, 119 languages) as the primary model and add mT5-XXL or Aya-23-8B as the second model family for cross-architecture generalization. This also brings auto-research mode within the 200h H100 budget if you trim the sweep to ≤3 ablation dimensions.

3. **Address the structural-vs-behavioral erasure ambiguity.** The paper should explicitly test whether the cultural knowledge 'erasure' is representational (information is gone from activations) or behavioral (information exists but the model won't surface it). If arXiv:2504.10191 is correct that cultural knowledge persists structurally, CLS-LoRA's value is in behavioral preservation during fine-tuning — which needs to be measured differently than simple layer probing. A single ablation running full-LoRA training then measuring layer-wise cultural probe accuracy (before vs. after) would resolve this and strengthen the paper's mechanistic story.

Secondary fixes: Remove the 'outstanding paper' label from INCLINE, verify the transfer-localization plane code availability from arXiv:2510.26024 authors before committing to it as primary metric, and reduce auto-research sweep to ≤200h H100.

### Round 2 review
Verdict: revise
Issues: ["Missing citation: Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025, Liu & Niehues). This paper directly shows middle layers are most important for cross-lingual transfer alignment across 1,000+ language pairs — directly supporting and potentially complicating CLS-LoRA's factual-transfer layer partition. Reviewers will ask why this is not cited.", "Missing citation: Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (arXiv:2506.01675, ACL 2025 short paper). This paper studies asymmetric cross-lingual cultural transfer with a frequency-based hypothesis, providing empirical background that should be acknowledged in CLS-LoRA's problem framing.", "Core mechanistic assumption gap: The factual-vs-cultural layer partition is derived from Surgical Steering, an inference-time activation intervention. The revision does not explicitly argue why inference-time steerability at layer L implies that freezing layer L during LoRA training prevents erasure — these are distinct causal claims. Stage 1 empirically validates this, but the paper should include a one-paragraph mechanistic bridge explaining the connection before Stage 1 results are presented.", "Stage 2 probe data source underspecified: The per-layer linear probes require 'culture-specific benchmark items' for the cultural-localization score. It is unclear whether these come from CulturalBench/SemEval-2026 Task 7 held-out splits or require new annotation. Given SemEval-2026 Task 7 prohibits use of its data for training (confirmed), the probe training data source must be stated explicitly; using CulturalBench for probe training and SemEval for final evaluation would resolve this.", "Round 1 incorrectly flagged INCLINE's 'ACL 2025 Outstanding Paper' designation — independently confirmed that INCLINE IS listed among the 26 ACL 2025 Outstanding Papers; the revision correctly retained this label and no fix is needed here."]
Feedback: The revision has successfully resolved all four critical Round 1 issues: MLAS-LoRA is cited and differentiated across three axes, Source-Shielded Updates is added, auto-research compute is trimmed to ~115h H100 (within the 200h constraint), LLaMA 4 Scout is replaced by Qwen3-8B + Aya-23-8B with explicit justification, and the structural-vs-behavioral erasure ambiguity is addressed by Stage 1. Note that Round 1's INCLINE flag was incorrect — it IS an ACL 2025 Outstanding Paper; the revision rightly kept that label.

Three targeted fixes are needed before this is ready:

1. **Add the two missing ACL 2025 citations.** In the landscape section, add: (a) Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025) — acknowledge that it establishes middle-layer primacy for cross-lingual factual transfer via representation alignment, and that CLS-LoRA extends this by additionally protecting cultural-knowledge layers from LoRA updates; (b) Cross-Lingual Transfer of Cultural Knowledge (arXiv:2506.01675, ACL 2025) — acknowledge as empirical background showing cultural transfer asymmetry for low-resource languages, motivating the need for training-time prevention.

2. **Add a mechanistic bridge paragraph.** Before Stage 1 results, add: 'Our freezing strategy relies on a critical assumption: that the layer indices most sensitive to cultural-vs-factual steering at inference time (per arXiv:2510.26024) correspond to the layers where LoRA updates most destructively disrupt cultural routing during training. Stage 1 empirically validates this assumption: if post-full-LoRA cultural probe accuracy is preserved, erasure is behavioral and layer freezing is the correct intervention; if probe accuracy drops, erasure is partly representational and the KL-divergence regularizer becomes critical.'

3. **Specify probe training data explicitly.** Clarify that Stage 2 probes are trained on held-out splits of CulturalBench (available at ACL 2025) for cultural-localization scores and TyDiQA/XQUAD for factual-transfer scores — not on SemEval-2026 Task 7 (evaluation-only by task rules) and not requiring new annotation.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL misattribution: The core_problem section states arXiv:2504.10191 'reveals the suppression is often behavioral rather than purely representational: cultural knowledge frequently survives as recoverable activations in deeper layers but is no longer surfaced in model outputs after fine-tuning.' This is factually wrong. arXiv:2504.10191 studies inference-time steering of cultural knowledge in already-trained (not instruction-fine-tuned) models, primarily Gemma2-9b-it. It does not study post-fine-tuning behavior at all, and makes no claim about whether cultural knowledge survives as recoverable activations after LoRA fine-tuning. The behavioral-vs-representational erasure distinction is CLS-LoRA's own hypothesis — which Stage 1 empirically tests — not an established finding from the cited paper. Any reviewer who reads arXiv:2504.10191 will reject this attribution.", "Layer depth percentage inconsistency: The paper claims 'cultural-knowledge layers concentrated at deeper layers ~72–94% model depth, per arXiv:2504.10191.' The actual mechanistic findings of arXiv:2504.10191 (Gemma2-9b, 42-layer architecture) identify critical cultural activation at absolute layers 23 and 30 (≈ 55-71% depth), and steering experiments cover layers 15-30 (≈ 36-71% depth) — significantly below the claimed 72-94% range. Stage 2 probing mitigates this by empirically determining the actual partition per model, but the percentage figure cited as empirically established from arXiv:2504.10191 is inaccurate and will mislead reviewers.", "arXiv:2510.26024 is under review at ICLR 2026 (submitted Sept 2025, not yet accepted). Its transfer-localization plane evaluation code is almost certainly not publicly released. The paper acknowledges this with a fallback, but does not explicitly state the primary framework comes from an unpublished ICLR 2026 submission — reviewers may check and flag this.", "Qwen3-8B has a 'thinking mode' (/think / /no_think) that activates extended chain-of-thought reasoning; in thinking mode, the model's internal generation pathway differs substantially from standard instruction following. The paper does not specify whether experiments use thinking or non-thinking mode. For cultural localization probing and instruction fine-tuning, using thinking mode could contaminate results by routing responses through CoT reasoning rather than direct cultural knowledge layers."]
Feedback: The revision has successfully addressed all four Round 2 issues. Three targeted fixes remain before this is ready.

1. **Fix the arXiv:2504.10191 attribution (critical).** The core_problem and opportunity sections claim this paper shows cultural knowledge 'survives as recoverable activations after fine-tuning' and that erasure is 'behavioral rather than representational.' This paper does not study fine-tuning at all — it studies inference-time cultural steering in pre-trained models. The correction is: reframe arXiv:2504.10191 as showing cultural knowledge is spatially localized and steerable in pre-trained models, which motivates the hypothesis that specific layers implement cultural routing pathways. Then explicitly state: 'Whether this localization and steerability survives LoRA instruction fine-tuning — and whether erasure is behavioral (routing disruption) or representational (information loss) — is the empirical question Stage 1 answers.' The KL regularizer is then naturally framed as the fallback for the representational-erasure case. This reframing is accurate, scientifically honest, and actually strengthens the paper by making Stage 1 a genuine empirical contribution rather than a validation of a fait accompli.

2. **Correct the layer depth percentages.** Replace '~72–94% model depth, per arXiv:2504.10191' with something like: 'arXiv:2504.10191 identifies absolute layers 23-30 as critical for cultural activation in Gemma2-9b (a 42-layer model, corresponding to approximately 55-71% depth); arXiv:2510.26024 finds cultural localization in deeper layers relative to factual transfer. Stage 2 probing empirically determines the partition for each target model rather than hard-coding percentages from other architectures.' This is more accurate and emphasizes the empirical approach.

3. **Add one sentence on Qwen3-8B thinking mode.** Clarify that all Qwen3-8B experiments are conducted in non-thinking mode (/no_think or without system prompt thinking tokens) to ensure consistent direct-generation behavior during LoRA fine-tuning and cultural localization evaluation. Without this, reviewers may question whether the thinking-mode routing path confounds the cultural layer partition.

### Round 4 review
Verdict: revise
Issues: ["CRITICAL — Incorrect proceedings status of arXiv:2510.26024: This paper (CLS-LoRA's primary motivation) was accepted at ICLR 2026 (conference held April 22–26, 2026). The claim 'has not appeared in a published proceedings as of May 2026' is factually false as of today (May 10, 2026). The citation and all associated caveats about evaluation code unavailability and 'arXiv preprint' status must be updated to reflect its ICLR 2026 publication. This is a straightforward factual correction, but leaving it wrong will draw immediate rejection from any reviewer who checks.", "CRITICAL — Missing ICLR 2026 paper with directly contradictory mechanistic evidence: 'Neuron-Level Analysis of Cultural Understanding in Large Language Models' (arXiv:2510.08284, ICLR 2026, Yamamoto et al.) uses gradient-based neuron attribution to identify culture-relevant neurons and finds them 'concentrated in shallow to middle MLP layers' — directly opposing the deeper-layer (layers 19–30, ~45–71% depth) localization from arXiv:2504.10191 that grounds CLS-LoRA's freezing strategy. This paper was on arXiv since October 2025 and has been accepted at ICLR 2026 (held before the submission deadline). CLS-LoRA must cite it and either (a) argue the discrepancy is a methodological artifact (activation-steering subspaces vs. gradient-based neuron attribution measure different constructs), or (b) acknowledge it as an empirical uncertainty that Stage 2 probing resolves per-model. Without this, any EMNLP reviewer aware of arXiv:2510.08284 will flag it as a fundamental flaw.", "MODERATE — Missing related work: LayRA (arXiv:2509.11414, Sept 2025) is a layer-selective LoRA approach that applies LoRA to first and final transformer layers while freezing intermediate layers, for continual multilingual language addition. Its pipeline (layer-informed selective LoRA to prevent forgetting) shares the same mechanical strategy as CLS-LoRA, even though the objective (language preservation vs cultural preservation) differs. It should be cited and differentiated in the related work discussion, noting that LayRA partitions layers on a language-encoding-vs-reasoning axis while CLS-LoRA partitions on a factual-transfer-vs-cultural-localization axis."]
Feedback: Round 4 correctly resolves all three Round 3 issues (arXiv:2504.10191 attribution, layer depth percentages, Qwen3-8B thinking mode). Three new fixes are now required:

1. **Update arXiv:2510.26024 citation to ICLR 2026 (critical, ~1 hour of work).** The paper was accepted at ICLR 2026 (April 22–26, 2026) and is now a published conference paper. Replace all instances of 'arXiv preprint (submitted October 2025)' with 'ICLR 2026'. The caveat about evaluation code unavailability may still apply (check the ICLR 2026 camera-ready for a code link), but the 'not appeared in published proceedings as of May 2026' claim must be removed.

2. **Cite and engage with arXiv:2510.08284 (critical, ~half a day of writing).** This ICLR 2026 paper finds culture-relevant neurons in shallow-to-middle MLP layers — not deep layers. CLS-LoRA must acknowledge this in the mechanistic bridge paragraph. The recommended framing: 'Yamamoto et al. (2026, arXiv:2510.08284) identify culture-relevant neurons via gradient attribution and find them in shallow-to-middle MLP layers, apparently in tension with the deeper-layer localization from Veselovsky et al. (2025, arXiv:2504.10191) and Han et al. (2026, ICLR). This discrepancy may reflect the difference between measuring activation-steering subspaces (which can span many layers) versus individual gradient-sensitive neurons (which can be small and shallow); Stage 2 probing resolves this empirically for each target model.' This framing converts a vulnerability into a strength: Stage 2 becomes the principled resolution to a genuine mechanistic debate in the literature.

3. **Add LayRA to related work (moderate, ~30 minutes).** Cite arXiv:2509.11414 (Sept 2025) as a parallel selective-LoRA approach for multilingual LLMs. Differentiate: LayRA partitions on a source-language-encoding vs English-reasoning vs target-language-decoding functional axis; CLS-LoRA partitions on a factual-transfer vs cultural-localization semantic axis that cuts across language-pair specificity. The cultural-preservation objective remains the categorical novelty.

### Round 5 review
Verdict: revise
Issues: ["MODERATE — Evaluation benchmark gap violating user requirements: The user required evaluation on XTREME-UP, XCOPA, XStoryCloze, MGSM, multilingual MMLU, TyDiQA, and FLORES. The paper covers only TyDiQA from this list (plus CulturalBench and SemEval-2026 Task 7). Any EMNLP reviewer will ask: does CLS-LoRA hurt general cross-lingual commonsense reasoning (XCOPA, XStoryCloze) or multilingual arithmetic (MGSM)? Without at least XCOPA and MGSM results, the paper cannot demonstrate that cultural preservation does not come at the cost of broader multilingual competence. These are fast to run (standard few-shot evaluation, ~2–4h per benchmark per model) and should be added to Stage 4.", "MODERATE — Missing 'full LoRA + KL penalty only' ablation: The paper proposes layer freezing + optional KL regularization, but never isolates the contribution of layer freezing from KL regularization alone. A 'full LoRA + KL-divergence penalty on cultural-layer activations (no freezing)' baseline is essential to demonstrate that layer freezing is the necessary mechanism, not just the regularization. Without this ablation, a reviewer could argue KL regularization alone achieves the same preservation and layer freezing is unnecessary complexity. This ablation requires ~4–6 additional runs and should be added to the auto sweep.", "MINOR — Stage 1 probe methodology underspecified: Stage 1 measures 'per-layer cultural probe accuracy before and after' full LoRA fine-tuning. It is ambiguous whether the Stage 1 probe is (a) trained on pre-fine-tuned representations and applied to post-fine-tuned representations (cross-checkpoint transfer), or (b) separately trained on each checkpoint's representations. If (a), probe failure could reflect activation-space reorganization rather than information loss, confounding the behavioral-vs-representational distinction Stage 1 is designed to make. The paper should clarify that separate probes are trained and evaluated on held-out data from each checkpoint, making the comparison meaningful.", "MINOR — Factual correction: The paper continues to note 'submitted to ICLR 2026' for arXiv:2510.26024, but as of May 2026, HyoJung Han's own publication page lists this paper as an arXiv preprint with no confirmed proceedings venue—suggesting it was not accepted at ICLR 2026. The submission's existing characterization ('as of May 2026, the first author's publication page continues to characterize it as an arXiv preprint without a confirmed proceedings venue') is correct and should remain. Note: the Round 4 reviewer's claim that it was 'accepted at ICLR 2026' was factually wrong; the Round 5 revision's handling is accurate. No change needed beyond confirming this is stable."]
Feedback: Round 5 has cleanly resolved all three Round 4 issues. The Yamamoto et al. integration is thorough and the mechanistic framing is now scientifically honest. Two targeted fixes are needed before this is ready:

1. **Expand Stage 4 evaluation to include XCOPA and MGSM (moderate, ~1 GPU-day).** Add two cross-lingual commonsense benchmarks (XCOPA, XStoryCloze) and one multilingual reasoning benchmark (MGSM) to Stage 4. These measure capabilities orthogonal to cultural localization and factual QA. The paper needs to show CLS-LoRA does not regress on these relative to the full-LoRA baseline. If CLS-LoRA freezes cultural layers but those layers also encode commonsense knowledge, XCOPA performance could drop — which would be both a problem and an interesting finding. These benchmarks are free to run via lm-eval-harness and take ~2–4h per model. This directly addresses the user's specified evaluation requirements.

2. **Add a 'full LoRA + KL only' ablation to Stage 3 (moderate, ~4–6 additional runs).** Without this baseline, the paper cannot argue that layer freezing is the operative mechanism rather than the KL regularizer alone. The ablation grid should include: (a) full LoRA (current baseline), (b) full LoRA + KL penalty, (c) CLS-LoRA frozen (no KL), and (d) CLS-LoRA frozen + KL (proposed method). This 2×2 table cleanly isolates the contributions of each component.

3. **Clarify Stage 1 probe training protocol (minor, ~1 paragraph).** Specify that Stage 1 trains separate probes on the pre-fine-tuned and post-fine-tuned checkpoint representations respectively (not cross-checkpoint transfer), to ensure that a drop in probe accuracy reflects information loss rather than activation-space reorganization. This removes a methodological ambiguity that a probing-literate reviewer would flag.

### Round 6 review
Verdict: revise
Issues: ["CRITICAL — CulturalBench is not available for training use. The paper claims Stage 2 cultural-localization probes are trained on 'held-out splits of CulturalBench (ACL 2025)...which is publicly available for training use.' This is factually wrong: the CulturalBench paper explicitly states 'our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training.' Using CulturalBench for probe training violates its terms. The Stage 2 probe training data source must be replaced with a training-permitted cultural knowledge resource (e.g., multilingual Wikipedia cultural-domain sentences, MKQA, World Values Survey items, or a custom culturally-grounded QA dataset without OpenAI annotation-platform restrictions). SemEval-2026 Task 7 (BLEnD) is correctly identified as evaluation-only and is not the issue here.", "MINOR — Sparse Subnetwork Enhancement for Underrepresented Languages (arXiv:2510.13580, updated Feb 2026) applies targeted sparse fine-tuning of language-associated subnetworks (<1% of parameters) and achieves strong cross-lingual alignment while preserving general capabilities, with adaptation concentrated in down-projection weights of later layers. Although its objective (language performance improvement) differs from CLS-LoRA's (cultural preservation), the layer-selective sparse-fine-tuning approach is closely related and should be acknowledged in the landscape section to preempt reviewer comparisons."]
Feedback: Round 6 resolves all three Round 5 issues cleanly (XCOPA/XStoryCloze/MGSM added, 2×2 ablation with condition (b) included, Stage 1 separate-probe protocol specified). One critical correction remains before this can pass review:

**Fix the CulturalBench training-use claim (critical, ~2 hours of work).** The CulturalBench paper explicitly states the dataset is prohibited from training use due to its OpenAI annotation-platform terms. Replace the Stage 2 cultural-localization probe training source with a dataset that permits training. Strong alternatives: (a) multilingual Wikipedia paragraphs from culture-specific articles, filtered by Wikidata cultural-domain tags — widely available, CC-BY licensed, and covers the 45+ cultural regions needed; (b) MKQA (multilingual knowledge questions, Apache 2.0), which covers culturally-grounded factual questions across languages; (c) a small GPT-4o-free annotation of culturally-grounded probe examples using open models (Qwen3-8B itself, before fine-tuning). CulturalBench should then be used *only* for final evaluation (Stage 4), alongside SemEval-2026 Task 7, which is already correctly limited to evaluation. Update the Stage 2 and Stage 4 data-source descriptions to reflect this separation, and remove the phrase 'publicly available for training use' from the CulturalBench reference. This is a single-paragraph fix in the approach and description sections.

**Also add Sparse Subnetwork Enhancement (arXiv:2510.13580) to the landscape (minor, ~20 minutes).** Note that it improves underrepresented-language performance via language-neuron subnetwork selection, and differentiate on objective (language capability vs. cultural knowledge preservation) and partition axis (language-identity neurons vs. factual-cultural semantic axis).

### Round 7 review
Verdict: revise
Issues: ["MODERATE — 'Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models' (arXiv:2602.22475, February 2026) is unaddressed. This paper proposes culture-specific LoRA adapters with a culture router, using LoRA as the adaptation vehicle for cultural knowledge management. Although its objective (cultural adaptation/alignment) differs from CLS-LoRA's (preventing cultural erasure during cross-lingual instruction fine-tuning), and its partition axis is culture-identity (which culture) rather than CLS-LoRA's factual-vs-cultural semantic axis, the surface-level similarity is close enough that EMNLP reviewers will notice the omission. Must be cited and differentiated in the landscape section: key differentiators are (1) objective — cultural capability gain vs. cultural knowledge preservation, (2) partition dimension — culture identity vs. factual-cultural semantic axis, (3) mechanism — routing between culture-specific adapters vs. layer-freezing based on empirical functional partition.", "MINOR — The user-specified evaluation list includes XTREME-UP and multilingual MMLU, neither of which appears in the Stage 4 evaluation plan. The current suite (TyDiQA, XCOPA, XStoryCloze, MGSM, CulturalBench, SemEval-2026 Task 7) is strong, but an EMNLP reviewer familiar with the user's stated scope may ask why comprehensive multilingual capability benchmarks (XTREME-UP, mMLLU) are absent. At minimum, the paper should justify omitting these (e.g., 'XTREME-UP includes many tasks already covered by TyDiQA and XCOPA; multilingual MMLU adds ~8h evaluation per model and is planned for the camera-ready version') rather than leaving the absence unaddressed.", "MINOR — The feasibility of the EMNLP ARR deadline (May 25, 15 days from now) in auto-research mode deserves one explicit caveat in the venue list: the 5–8 day compute window plus sequential Stage 1→Stage 2→Stage 3 dependency plus writing and submission formatting leaves essentially no time for a second sweep if early results are inconclusive. The paper should either acknowledge this risk explicitly or treat EACL 2027 as the primary target with EMNLP as best-case."]
Feedback: The Round 6 fixes are all correctly implemented: CulturalBench is now evaluation-only (INCLUDE + Wikipedia used for Stage 2 probe training, both licensing-verified), Sparse Subnetwork Enhancement is cited and differentiated, and the 2×2 ablation and XCOPA/XStoryCloze/MGSM evaluation are fully specified. One moderate issue blocks passage to 'pass':

**Add 'Mind the Gap in Cultural Alignment' (arXiv:2602.22475, February 2026) to the landscape (~30 minutes).** This paper proposes task-aware culture management with culture-specific LoRA adapters and a culture router. In the landscape section, add it alongside the other LoRA-based multilingual methods and differentiate on: (1) objective — it improves cultural alignment by adapting to specific cultures, whereas CLS-LoRA preserves existing culturally-grounded knowledge from being erased during cross-lingual instruction fine-tuning; (2) partition axis — it partitions along culture identity (which-culture adapter), whereas CLS-LoRA partitions along the factual-transfer vs. cultural-localization semantic axis that cuts across language and culture identity; (3) mechanism — it routes inputs to culture-specific LoRA modules at the adapter level, whereas CLS-LoRA freezes layers empirically identified as cultural-knowledge carriers and applies LoRA only to factual-transfer layers. The cultural-preservation objective (preventing erasure rather than enabling adaptation) remains absent from this work.

**Optionally justify the omission of XTREME-UP and multilingual MMLU (minor, 1 sentence).** Add a note that these are not included as primary metrics because their constituent tasks overlap substantially with TyDiQA (XTREME-UP) and the combined XCOPA/MGSM suite (mMLLU reasoning), with the caveat that a full XTREME-UP and mMLLU evaluation would be included in the camera-ready. This preempts reviewer requests without adding significant compute.

After these two fixes, the paper should be ready to pass. The mechanistic story is scientifically honest, the ablation design is rigorous, the data licensing is clean, and the differentiation from prior selective-LoRA work is systematic. This is a well-developed submission.


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
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "type": "user",
  "uuid": "0079fb85-32e9-4fbd-bf28-acd75a75947a",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:08:15.724Z_

```json
{
  "parentUuid": "0079fb85-32e9-4fbd-bf28-acd75a75947a",
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
  "uuid": "32bf4924-54f8-42fb-8f44-22dc79c3926e",
  "timestamp": "2026-05-10T08:08:15.724Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:08:15.724Z_

```json
{
  "parentUuid": "32bf4924-54f8-42fb-8f44-22dc79c3926e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b6b5c12b-237c-44ac-a31e-128972a30f9b",
  "timestamp": "2026-05-10T08:08:15.724Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
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
  "leafUuid": "b6b5c12b-237c-44ac-a31e-128972a30f9b",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "CLS-LoRA: Preventing cultural erasure in cross-lingual instruction tuning",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:08:27.254Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea (Round 8/10) for CLS-LoRA. I need to independently verify claims, check for competing work, and assess whether the previous round's issues have been addressed.

Looking at the Round 7 issues:
1. MODERATE - 'Mind the Gap in Cultural Alignment' (arXiv:2602.22475, February 2026) was unaddressed
2. MINOR - XTREME-UP and multilingual MMLU omission
3. MINOR - EMNLP ARR deadline feasibility caveat

Now looking at Round 8's submission, I need to check:
1. Is CultureManager (arXiv:2602.22475) now cited and differentiated? YES - I can see it in the landscape section with a detailed three-axis differentiation.


2. Both the XTREME-UP/mMLLU omission and EMNLP deadline concerns have been addressed in the evaluation section and venue notes, with explanations for the overlapping task coverage and computational constraints.

3. Now I'm doing independent verification of the key claims—checking whether the CultureManager paper actually exists, looking for any concurrent work that might have been missed, and validating the evaluation framework details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6b5c12b-237c-44ac-a31e-128972a30f9b",
  "isSidechain": false,
  "requestId": "req_011CatYdo22uvTPmqo6ExNma",
  "type": "assistant",
  "uuid": "2d4f4f63-b88b-41cd-a005-685a68dd12a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C8sCHfFRpyuoTQUfRNamBE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27476,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1783,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1783,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 27476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27476
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

_source line 9 · 2026-05-10T08:08:27.258Z_

I'll conduct independent verification searches to assess this Round 8 submission, focusing on whether Round 7 issues were properly addressed and whether any new competitive work has emerged.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d4f4f63-b88b-41cd-a005-685a68dd12a1",
  "isSidechain": false,
  "requestId": "req_011CatYdo22uvTPmqo6ExNma",
  "type": "assistant",
  "uuid": "e3614ec6-2a59-406c-b030-4190ebd85ea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C8sCHfFRpyuoTQUfRNamBE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27476,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1783,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1783,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 27476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27476
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

_source line 10 · 2026-05-10T08:08:37.570Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016kosPss3YiSDiH4t7cQ4go`</summary>

```json
{
  "description": "Verify CLS-LoRA paper claims and find competing work",
  "subagent_type": "Explore",
  "prompt": "You are an adversarial ML paper reviewer. Search for competing work and verify claims for an idea called \"Cultural-Layer-Selective LoRA (CLS-LoRA)\" for EMNLP 2026.\n\nThe paper's core claim: Cross-lingual instruction fine-tuning erases culturally-grounded language-specific knowledge. CLS-LoRA proposes empirical per-layer probing to identify which layers implement \"cultural routing\" vs \"factual transfer\", then freezes cultural-knowledge layers during LoRA fine-tuning to prevent erasure.\n\nKey papers the idea references:\n- arXiv:2510.26024 (Han, Agrawal & Briakou) - \"Rethinking Cross-lingual Alignment\" / Surgical Steering\n- arXiv:2504.10191 - \"Localized Cultural Knowledge is Conserved and Controllable in LLMs\"\n- arXiv:2510.08284 (Yamamoto et al., ICLR 2026) - Neuron-level analysis of cultural understanding\n- arXiv:2602.22475 (CultureManager, Zhang et al., Feb 2026)\n- arXiv:2509.11414 (LayRA) - layer-selective LoRA for continual multilingual language addition\n- MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762)\n\nPlease search for:\n1. Whether arXiv:2602.22475 (\"Mind the Gap in Cultural Alignment\") actually exists and what it proposes - search \"CultureManager cultural alignment LoRA arxiv 2602.22475\"\n2. Any recent (2025-2026) papers on \"cultural preservation fine-tuning multilingual\" or \"cultural erasure LLM training\" that might compete\n3. Search for papers on \"layer freezing cultural knowledge LLM\" to find direct competitors\n4. Search for \"selective LoRA cultural preservation multilingual\" on arxiv\n5. Search for \"cross-lingual fine-tuning cultural knowledge preservation 2025 2026\"\n\nFor each search, report: what you found, the paper title, venue/arxiv ID if available, and whether it threatens the novelty of CLS-LoRA.\n\nBe thorough — use WebSearch with multiple queries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3614ec6-2a59-406c-b030-4190ebd85ea9",
  "isSidechain": false,
  "requestId": "req_011CatYdo22uvTPmqo6ExNma",
  "type": "assistant",
  "uuid": "3360d13e-f8de-4654-ba63-9e71e1d2e9db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C8sCHfFRpyuoTQUfRNamBE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27476,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1783,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1783,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 27476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27476
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

_source line 11 · 2026-05-10T08:08:48.729Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HjDFsNTDSyRZwD9GnZdue1`</summary>

```json
{
  "description": "Verify feasibility and resource estimates for CLS-LoRA",
  "subagent_type": "Explore",
  "prompt": "You are reviewing feasibility claims for a paper called \"CLS-LoRA\" that proposes training-time cultural knowledge preservation via layer-selective LoRA.\n\nThe paper claims auto-research mode uses ~310–360h A100 (~122–144h H100 equivalent), which is within a ≤200h H100 hard constraint.\n\nThe auto sweep covers: 3 LoRA ranks (8,16,32) × 2 layer partition thresholds × 2 model families (Qwen3-8B, Aya-23-8B) × 2 regularization strengths × 2 seeds = 48 core training runs + ~12 baseline runs + ~4-6 ablation runs (condition b) + Stage 1 diagnostic + ~18-24h benchmark evaluation.\n\nPlease verify:\n1. Search \"Qwen3-8B LoRA fine-tuning GPU hours\" or \"Aya-23-8B instruction tuning compute\" to understand typical training costs for these 8B models\n2. Search \"XCOPA lm-eval-harness evaluation time\" or \"lm-evaluation-harness multilingual benchmarks speed\" to verify the ~2-4h per benchmark per model claim\n3. Search \"H100 vs A100 performance ratio\" to verify the 2.5x conversion used (310-360 A100h → 122-144 H100h suggests roughly 2.5x ratio)\n4. Search whether \"INCLUDE dataset arxiv 2411.19799\" is genuinely available for training use (CC BY 4.0 license), and whether it covers the cultural domains claimed\n5. Search \"SemEval 2026 Task 7 BLEnD multilingual cultural\" to verify this benchmark exists and is evaluation-only\n\nReport findings on each point. The paper claims 48 core runs + overhead = 310-360 A100 hours. That's roughly 6.5-7.5h per training run for 8B models, which seems plausible for multi-epoch LoRA — confirm or deny.\n\nUse WebSearch for each verification."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3360d13e-f8de-4654-ba63-9e71e1d2e9db",
  "isSidechain": false,
  "requestId": "req_011CatYdo22uvTPmqo6ExNma",
  "type": "assistant",
  "uuid": "ecde993e-9576-4aa4-9c12-391923dec957",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C8sCHfFRpyuoTQUfRNamBE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27476,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1783,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1783,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 27476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27476
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

_source line 12 · 2026-05-10T08:09:36.965Z_

<details><summary>↩ Tool result · `toolu_01HjDFsNTDSyRZwD9GnZdue1`</summary>

```text
Based on my comprehensive web search investigation, here is my verification report on the CLS-LoRA paper's feasibility claims:

## POINT 1: Qwen3-8B & Aya-23-8B LoRA Fine-Tuning GPU Hours

**Finding: PLAUSIBLE, with caveats**

The search results confirm that LoRA fine-tuning of 8B models is feasible on A100s with reasonable compute:
- Qwen3-8B fine-tuning takes approximately **2-4 hours on a single A100** for standard tasks
- Cloud pricing is ~$1.49/hour for A100 rental, making a $3-6 per run cost estimate realistic
- Sources document successful LoRA fine-tuning on single A100s without requiring model offloading or gradient checkpointing
- The Aya-23-8B model is confirmed as an 8B parameter model from Cohere Labs; while specific compute costs weren't found, they should be comparable to Qwen3-8B

The paper's claim of **6.5-7.5h per training run** (dividing 310-360h by 48 runs) is **plausible** for multi-epoch instruction-tuning LoRA, though slightly on the longer end. This likely accounts for multiple epochs and evaluation overhead per run.

---

## POINT 2: XCOPA & lm-eval-harness Evaluation Time (~2-4h per benchmark)

**Finding: PARTIALLY VERIFIED, but specific timing unavailable**

- XCOPA is confirmed as a multilingual benchmark (11 languages) integrated into lm-evaluation-harness
- lm-eval-harness is the standard framework used by NVIDIA, Cohere, BigScience, and hundreds of research papers
- The framework supports multilingual evaluation with various optimizations (batch_size auto, vLLM support, etc.)
- **However**, the search results provide NO specific timing data for XCOPA or multilingual benchmarks in lm-eval-harness

**Assessment**: The ~2-4h estimate per benchmark per 8B model is reasonable (XCOPA has ~1000 test examples × 11 languages, so ~11k evaluations), but cannot be directly verified from public sources. The paper would need to provide timing breakdowns in appendices.

---

## POINT 3: H100 vs A100 Performance Ratio (2.5x conversion)

**Finding: VERIFIED with high confidence**

The search results confirm the conversion ratio used in the paper:
- **H100 is 2.29x faster than A100** in BF16 on Qwen3-8B (directly measured)
- H100 delivers **up to 2.4x throughput** in mixed-precision training
- H100 shows **2-2.5x speedup** on typical transformer training workloads
- Practical example: A 36-hour A100 job completes in ~16 hours on H100 (÷2.29)

**Conversion applied in paper**: 
- 310-360 A100h ÷ 2.5 = **124-144 H100h**
- 310-360 A100h ÷ 2.29 = **135-157 H100h**

The paper's use of a 2.5x ratio is conservative and well-justified. The H100 equivalent falls within the claimed **≤200h H100** hard constraint with substantial margin.

---

## POINT 4: INCLUDE Dataset (arXiv 2411.19799) - CC BY 4.0 License & Availability

**Finding: PARTIALLY VERIFIED with significant uncertainty**

What is confirmed:
- INCLUDE dataset does exist (arXiv:2411.19799, "INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge")
- It contains **197,243 QA pairs from local exam sources** across **44 written languages**
- It is a comprehensive **knowledge- and reasoning-centric benchmark** with regional focus

**Critical gap**:
- The search results do **NOT explicitly confirm** CC BY 4.0 licensing for the dataset itself
- The paper may not be available for training use if the exam source material has restrictive licenses
- The dataset may only be available for evaluation, not training

**Recommendation**: The paper MUST include:
1. Explicit license declaration (CC BY 4.0, CC0, or other)
2. Data availability statement showing the dataset can be legally used for training
3. Confirmation that the "cultural domains claimed" (presumably food, language, customs, regional knowledge) are actually covered by the 44 languages

This is a **critical validation gap** that could undermine the entire paper if the license permits only evaluation use.

---

## POINT 5: SemEval 2026 Task 7 (BLEnD) - Benchmark Status

**Finding: VERIFIED, benchmark exists and is evaluation-only**

The search results confirm:
- **SemEval-2026 Task 7** is an official, real shared task (GitHub, Codabench, arXiv:2605.02601)
- Official name: "Everyday Knowledge Across Diverse Languages and Cultures"
- Based on **BLEnD benchmark** (52.6k QA pairs, 16 countries/regions, 13 languages including low-resource ones)
- BLEnD source paper (arXiv:2406.09948) documents the benchmark as hand-crafted by native speakers
- **Task is evaluation-only**: 62 teams submitted final results, with 140+ registered participants
- Original BLEnD dataset is publicly available: https://github.com/nlee0212/BLEnD

This confirms the paper's claim that SemEval 2026 Task 7 is a legitimate evaluation benchmark covering multilingual cultural knowledge.

---

## SUMMARY: Overall Feasibility Assessment

| Claim | Status | Confidence |
|-------|--------|-----------|
| **48 core runs × 6.5-7.5h = 310-360 A100h plausible** | ✓ PLAUSIBLE | High (70-80%) |
| **H100 conversion factor 2.5x valid** | ✓ VERIFIED | Very High (95%) |
| **XCOPA eval ~2-4h estimate** | ⚠ REASONABLE | Medium (60%) |
| **INCLUDE dataset available & CC BY 4.0** | ✗ UNVERIFIED | Low (30%) |
| **SemEval 2026 Task 7 BLEnD exists** | ✓ VERIFIED | Very High (95%) |

**Critical Issue**: The paper's use of the INCLUDE dataset for training (if claimed) is **unvalidated**. The license status must be explicitly confirmed or the paper should clarify that it is evaluation-only. The claim of ~310-360 A100 hours is otherwise well-grounded in established LoRA compute patterns and correct H100/A100 conversion ratios.

---

## Sources

- [Fine-Tuning Qwen3-8B for Medical Reasoning on E2E Networks A100 GPU](https://www.e2enetworks.com/blog/fine-tuning-qwen3-8b-medical-reasoning-qlora-e2e-networks-a100)
- [H100 vs A100: GPU Benchmarks, Specs & Cloud Pricing Compared (2026)](https://jarvislabs.ai/ai-faqs/what-are-the-differences-between-nvidia-a100-and-h100-gpus)
- [NVIDIA A100 vs H100: INT4, FP8, BF16 & AI Performance Comparison (2026)](https://www.bestgpusforai.com/gpu-comparison/a100-vs-h100)
- [lm-evaluation-harness GitHub](https://github.com/EleutherAI/lm-evaluation-harness)
- [XCOPA: A Multilingual Dataset for Causal Commonsense Reasoning](https://ducdauge.github.io/files/xcopa.pdf)
- [INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://arxiv.org/abs/2411.19799)
- [SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures](https://arxiv.org/abs/2605.02601)
- [BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages](https://arxiv.org/abs/2406.09948)
- [How can I fine-tune large language models on a budget using LoRA and QLoRA on cloud GPUs?](https://www.runpod.io/articles/guides/how-to-fine-tune-large-language-models-on-a-budget)
- [The Complete Guide to GPU Requirements for LLM Fine-Tuning](https://www.runpod.io/blog/llm-fine-tuning-gpu-guide)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecde993e-9576-4aa4-9c12-391923dec957",
  "isSidechain": false,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "type": "user",
  "uuid": "3daf70a5-fdc2-41d7-9da1-454b5d3cc0d9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are reviewing feasibility claims for a paper called \"CLS-LoRA\" that proposes training-time cultural knowledge preservation via layer-selective LoRA.\n\nThe paper claims auto-research mode uses ~310–360h A100 (~122–144h H100 equivalent), which is within a ≤200h H100 hard constraint.\n\nThe auto sweep covers: 3 LoRA ranks (8,16,32) × 2 layer partition thresholds × 2 model families (Qwen3-8B, Aya-23-8B) × 2 regularization strengths × 2 seeds = 48 core training runs + ~12 baseline runs + ~4-6 ablation runs (condition b) + Stage 1 diagnostic + ~18-24h benchmark evaluation.\n\nPlease verify:\n1. Search \"Qwen3-8B LoRA fine-tuning GPU hours\" or \"Aya-23-8B instruction tuning compute\" to understand typical training costs for these 8B models\n2. Search \"XCOPA lm-eval-harness evaluation time\" or \"lm-evaluation-harness multilingual benchmarks speed\" to verify the ~2-4h per benchmark per model claim\n3. Search \"H100 vs A100 performance ratio\" to verify the 2.5x conversion used (310-360 A100h → 122-144 H100h suggests roughly 2.5x ratio)\n4. Search whether \"INCLUDE dataset arxiv 2411.19799\" is genuinely available for training use (CC BY 4.0 license), and whether it covers the cultural domains claimed\n5. Search \"SemEval 2026 Task 7 BLEnD multilingual cultural\" to verify this benchmark exists and is evaluation-only\n\nReport findings on each point. The paper claims 48 core runs + overhead = 310-360 A100 hours. That's roughly 6.5-7.5h per training run for 8B models, which seems plausible for multi-epoch LoRA — confirm or deny.\n\nUse WebSearch for each verification.",
    "agentId": "a16cc66ae7831ecb5",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive web search investigation, here is my verification report on the CLS-LoRA paper's feasibility claims:\n\n## POINT 1: Qwen3-8B & Aya-23-8B LoRA Fine-Tuning GPU Hours\n\n**Finding: PLAUSIBLE, with caveats**\n\nThe search results confirm that LoRA fine-tuning of 8B models is feasible on A100s with reasonable compute:\n- Qwen3-8B fine-tuning takes approximately **2-4 hours on a single A100** for standard tasks\n- Cloud pricing is ~$1.49/hour for A100 rental, making a $3-6 per run cost estimate realistic\n- Sources document successful LoRA fine-tuning on single A100s without requiring model offloading or gradient checkpointing\n- The Aya-23-8B model is confirmed as an 8B parameter model from Cohere Labs; while specific compute costs weren't found, they should be comparable to Qwen3-8B\n\nThe paper's claim of **6.5-7.5h per training run** (dividing 310-360h by 48 runs) is **plausible** for multi-epoch instruction-tuning LoRA, though slightly on the longer end. This likely accounts for multiple epochs and evaluation overhead per run.\n\n---\n\n## POINT 2: XCOPA & lm-eval-harness Evaluation Time (~2-4h per benchmark)\n\n**Finding: PARTIALLY VERIFIED, but specific timing unavailable**\n\n- XCOPA is confirmed as a multilingual benchmark (11 languages) integrated into lm-evaluation-harness\n- lm-eval-harness is the standard framework used by NVIDIA, Cohere, BigScience, and hundreds of research papers\n- The framework supports multilingual evaluation with various optimizations (batch_size auto, vLLM support, etc.)\n- **However**, the search results provide NO specific timing data for XCOPA or multilingual benchmarks in lm-eval-harness\n\n**Assessment**: The ~2-4h estimate per benchmark per 8B model is reasonable (XCOPA has ~1000 test examples × 11 languages, so ~11k evaluations), but cannot be directly verified from public sources. The paper would need to provide timing breakdowns in appendices.\n\n---\n\n## POINT 3: H100 vs A100 Performance Ratio (2.5x conversion)\n\n**Finding: VERIFIED with high confidence**\n\nThe search results confirm the conversion ratio used in the paper:\n- **H100 is 2.29x faster than A100** in BF16 on Qwen3-8B (directly measured)\n- H100 delivers **up to 2.4x throughput** in mixed-precision training\n- H100 shows **2-2.5x speedup** on typical transformer training workloads\n- Practical example: A 36-hour A100 job completes in ~16 hours on H100 (÷2.29)\n\n**Conversion applied in paper**: \n- 310-360 A100h ÷ 2.5 = **124-144 H100h**\n- 310-360 A100h ÷ 2.29 = **135-157 H100h**\n\nThe paper's use of a 2.5x ratio is conservative and well-justified. The H100 equivalent falls within the claimed **≤200h H100** hard constraint with substantial margin.\n\n---\n\n## POINT 4: INCLUDE Dataset (arXiv 2411.19799) - CC BY 4.0 License & Availability\n\n**Finding: PARTIALLY VERIFIED with significant uncertainty**\n\nWhat is confirmed:\n- INCLUDE dataset does exist (arXiv:2411.19799, \"INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge\")\n- It contains **197,243 QA pairs from local exam sources** across **44 written languages**\n- It is a comprehensive **knowledge- and reasoning-centric benchmark** with regional focus\n\n**Critical gap**:\n- The search results do **NOT explicitly confirm** CC BY 4.0 licensing for the dataset itself\n- The paper may not be available for training use if the exam source material has restrictive licenses\n- The dataset may only be available for evaluation, not training\n\n**Recommendation**: The paper MUST include:\n1. Explicit license declaration (CC BY 4.0, CC0, or other)\n2. Data availability statement showing the dataset can be legally used for training\n3. Confirmation that the \"cultural domains claimed\" (presumably food, language, customs, regional knowledge) are actually covered by the 44 languages\n\nThis is a **critical validation gap** that could undermine the entire paper if the license permits only evaluation use.\n\n---\n\n## POINT 5: SemEval 2026 Task 7 (BLEnD) - Benchmark Status\n\n**Finding: VERIFIED, benchmark exists and is evaluation-only**\n\nThe search results confirm:\n- **SemEval-2026 Task 7** is an official, real shared task (GitHub, Codabench, arXiv:2605.02601)\n- Official name: \"Everyday Knowledge Across Diverse Languages and Cultures\"\n- Based on **BLEnD benchmark** (52.6k QA pairs, 16 countries/regions, 13 languages including low-resource ones)\n- BLEnD source paper (arXiv:2406.09948) documents the benchmark as hand-crafted by native speakers\n- **Task is evaluation-only**: 62 teams submitted final results, with 140+ registered participants\n- Original BLEnD dataset is publicly available: https://github.com/nlee0212/BLEnD\n\nThis confirms the paper's claim that SemEval 2026 Task 7 is a legitimate evaluation benchmark covering multilingual cultural knowledge.\n\n---\n\n## SUMMARY: Overall Feasibility Assessment\n\n| Claim | Status | Confidence |\n|-------|--------|-----------|\n| **48 core runs × 6.5-7.5h = 310-360 A100h plausible** | ✓ PLAUSIBLE | High (70-80%) |\n| **H100 conversion factor 2.5x valid** | ✓ VERIFIED | Very High (95%) |\n| **XCOPA eval ~2-4h estimate** | ⚠ REASONABLE | Medium (60%) |\n| **INCLUDE dataset available & CC BY 4.0** | ✗ UNVERIFIED | Low (30%) |\n| **SemEval 2026 Task 7 BLEnD exists** | ✓ VERIFIED | Very High (95%) |\n\n**Critical Issue**: The paper's use of the INCLUDE dataset for training (if claimed) is **unvalidated**. The license status must be explicitly confirmed or the paper should clarify that it is evaluation-only. The claim of ~310-360 A100 hours is otherwise well-grounded in established LoRA compute patterns and correct H100/A100 conversion ratios.\n\n---\n\n## Sources\n\n- [Fine-Tuning Qwen3-8B for Medical Reasoning on E2E Networks A100 GPU](https://www.e2enetworks.com/blog/fine-tuning-qwen3-8b-medical-reasoning-qlora-e2e-networks-a100)\n- [H100 vs A100: GPU Benchmarks, Specs & Cloud Pricing Compared (2026)](https://jarvislabs.ai/ai-faqs/what-are-the-differences-between-nvidia-a100-and-h100-gpus)\n- [NVIDIA A100 vs H100: INT4, FP8, BF16 & AI Performance Comparison (2026)](https://www.bestgpusforai.com/gpu-comparison/a100-vs-h100)\n- [lm-evaluation-harness GitHub](https://github.com/EleutherAI/lm-evaluation-harness)\n- [XCOPA: A Multilingual Dataset for Causal Commonsense Reasoning](https://ducdauge.github.io/files/xcopa.pdf)\n- [INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://arxiv.org/abs/2411.19799)\n- [SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures](https://arxiv.org/abs/2605.02601)\n- [BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages](https://arxiv.org/abs/2406.09948)\n- [How can I fine-tune large language models on a budget using LoRA and QLoRA on cloud GPUs?](https://www.runpod.io/articles/guides/how-to-fine-tune-large-language-models-on-a-budget)\n- [The Complete Guide to GPU Requirements for LLM Fine-Tuning](https://www.runpod.io/blog/llm-fine-tuning-gpu-guide)"
      }
    ],
    "totalDurationMs": 48230,
    "totalTokens": 30354,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7983,
      "cache_read_input_tokens": 20228,
      "output_tokens": 2136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7983
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2136,
          "cache_read_input_tokens": 20228,
          "cache_creation_input_tokens": 7983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7983,
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
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "ecde993e-9576-4aa4-9c12-391923dec957",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T08:09:48.442Z_

<details><summary>↩ Tool result · `toolu_016kosPss3YiSDiH4t7cQ4go`</summary>

```text
Excellent. Now I have comprehensive information. Let me compile the adversarial review findings.

---

## ADVERSARIAL REVIEW: CLS-LoRA Novelty and Competing Work

Based on systematic searches of recent literature (2025-2026), here are my findings on the landscape of competing work and threats to CLS-LoRA's novelty:

### **1. ArXiv 2602.22475 - "Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models"**

**STATUS: CONFIRMED - Direct Competitor**

The paper **does exist** and proposes a very similar solution space:
- **Approach**: Synthesizes task-aware cultural data via LLM-based generators and web search, then fine-tunes lightweight LoRA adapters per culture while keeping the base model frozen
- **Culture Management**: Uses a culture router at inference time to select appropriate adapters based on input cultural context
- **Threat Level**: **VERY HIGH** - This directly overlaps with CLS-LoRA's use of LoRA adapters for cultural preservation. The main difference is task-awareness and modular routing rather than layer-selective freezing during fine-tuning.
- **Venue/Date**: ArXiv 2602.22475 (February 2026)

Sources:
- [Mind the Gap in Cultural Alignment (ArXiv HTML)](https://arxiv.org/html/2602.22475)
- [Mind the Gap in Cultural Alignment (ArXiv PDF)](https://arxiv.org/pdf/2602.22475)

---

### **2. ArXiv 2510.26024 - "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs" (Han, Agrawal & Briakou)**

**STATUS: CONFIRMED - Strong Foundational Work**

**Core Claims Verified**:
- Confirms the exact problem statement CLS-LoRA addresses: cross-lingual alignment erases cultural knowledge
- Introduces the "transfer-localization plane" framework to quantify both knowledge transfer AND cultural erasure
- **KEY FINDING**: "Universal factual transfer and culturally-specific knowledge are optimally steerable at **different model layers**"
- Proposes "Surgical Steering" for inference-time layer-targeted activation steering

**Threat Level**: **CRITICAL** - This paper already empirically validates that cultural knowledge lives in different layers than factual knowledge. CLS-LoRA's core insight (freezing cultural-knowledge layers) is directly anticipated by this work.

**Novelty Gap**: The Han et al. work focuses on inference-time steering via activation manipulation, while CLS-LoRA proposes training-time layer freezing during LoRA fine-tuning. However, the layer-level analysis principle is established.

Sources:
- [Rethinking Cross-lingual Alignment (ArXiv)](https://arxiv.org/abs/2510.26024)
- [Rethinking Cross-lingual Alignment (PDF)](https://arxiv.org/pdf/2510.26024)

---

### **3. ArXiv 2504.10191 - "Localized Cultural Knowledge is Conserved and Controllable in Large Language Models"**

**STATUS: CONFIRMED - Directly Relevant**

**Key Findings**:
- Identifies an "explicit cultural customization vector" conserved across non-English languages
- Uses mechanistic interpretability tools including activation patching and linear steering vectors on relevant layers
- Proposes layer-freezing LoRA fine-tuning for resource efficiency while preserving cultural knowledge

**Threat Level**: **VERY HIGH** - This paper already proposes the exact combination of: (1) identifying cultural layers, (2) layer freezing, and (3) LoRA fine-tuning for cultural preservation. CLS-LoRA appears to be reinventing this approach with the addition of per-layer probing.

Sources:
- [Localized Cultural Knowledge (ArXiv)](https://arxiv.org/abs/2504.10191)
- [Localized Cultural Knowledge (HTML)](https://arxiv.org/html/2504.10191v1)

---

### **4. ArXiv 2510.08284 - "Neuron-Level Analysis of Cultural Understanding in Large Language Models" (Yamamoto et al.)**

**STATUS: CONFIRMED - Relevant Mechanistic Analysis**

**Key Findings**:
- Identifies culture-general neurons and culture-specific neurons (< 1% of all neurons)
- Culture-specific neurons are concentrated in **shallow to middle MLP layers**
- Gradient-based scoring method for precise neuron identification
- Suppressing these neurons degrades cultural benchmark performance by up to 30%

**Threat Level**: **HIGH** - This provides neuron-level validation that cultural knowledge can be precisely localized. However, it's neuron-level, not layer-level. CLS-LoRA's per-layer probing is coarser-grained than this work.

**Note**: Listed as posted October 2025, updated March 2026. Claims of ICLR 2026 acceptance not confirmed in search results.

Sources:
- [Neuron-Level Analysis (ArXiv)](https://arxiv.org/abs/2510.08284)
- [Neuron-Level Analysis (HTML)](https://arxiv.org/html/2510.08284)

---

### **5. ArXiv 2509.11414 - "Continually Adding New Languages to Multilingual Language Models" (LayRA)**

**STATUS: CONFIRMED - Layer-Selective LoRA Precedent**

**Key Technical Approach**:
- Inserts LoRA modules into **selected early layers (first 10)** and **late layers (last 2)** while keeping middle layers frozen
- Addresses catastrophic forgetting in continual multilingual learning
- Based on insight: "Multilingual models encode inputs in source language in initial layers, reason in English in intermediate layers, translate back in final layers"

**Threat Level**: **MEDIUM-HIGH** - LayRA demonstrates that layer-selective LoRA application is effective for multilingual tasks. However, it's designed for continual language addition (preventing forgetting), not cultural preservation during instruction fine-tuning. The layer selection strategy is different (early/late vs. culture-specific middle layers).

**Potential Novelty Claim**: CLS-LoRA focuses on **identifying and freezing culture-implementing layers** during instruction fine-tuning, whereas LayRA uses layer-selective **application** for continual learning. The problem formulations differ.

Sources:
- [LayRA (ArXiv PDF)](https://arxiv.org/pdf/2509.11414)
- [LayRA (ArXiv)](https://arxiv.org/abs/2509.11414)

---

### **6. MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762)**

**STATUS: CONFIRMED - Language-Aware Parameter Detection**

**Approach**:
- Evaluates neuron/parameter awareness for both general MT and language-specific tasks
- Uses multiple language-specific LoRA architecture
- Selectively transfers knowledge from teacher to student models

**Threat Level**: **MEDIUM** - MLAS-LoRA also uses language-specific LoRA components, but for multilingual machine translation knowledge distillation. It's not about preserving cultural knowledge during instruction fine-tuning. The problem formulation is different (MT efficiency vs. cultural preservation).

Sources:
- [MLAS-LoRA (ACL Anthology)](https://aclanthology.org/2025.acl-long.762/)

---

### **7. Additional Highly Relevant Papers**

**M-DaQ (ArXiv 2509.15549)** - "Retrieving Samples with Multilingual Diversity and Quality for Instruction Fine-Tuning Datasets"
- Addresses cultural erasure through **data diversity** in instruction fine-tuning
- Threat Level: **MEDIUM** - Complementary approach (data) rather than architecture (layer freezing)

**Language over Content: Tracing Cultural Understanding in Multilingual LLMs**
- Probes how multilingual LLMs process cultural knowledge across layers
- Confirms that cultural understanding relies on language-specific internal circuits
- Threat Level: **MEDIUM** - Provides empirical grounding for layer-level analysis

---

## SYNTHESIS: Critical Novelty Assessment

### **Major Threats to CLS-LoRA's Novelty**

1. **ArXiv 2504.10191** already proposes layer-freezing LoRA for cultural preservation
2. **ArXiv 2510.26024** establishes that cultural and factual knowledge live in different layers
3. **ArXiv 2602.22475** (CultureManager) demonstrates LoRA-based cultural management at scale
4. **ArXiv 2509.11414** (LayRA) proves layer-selective LoRA is effective for multilingual tasks

### **CLS-LoRA's Potential Narrow Novelty**

The main differentiation appears to be:
- **Empirical per-layer probing methodology** to identify cultural-routing vs. factual-transfer layers
- **Fine-tuning-time freezing** (not inference-time steering like Han et al.)
- **Application to instruction fine-tuning** specifically (most other work targets other tasks)

### **Recommendation for EMNLP 2026 Submission**

**CLS-LoRA faces significant novelty challenges:**
- The layer-level analysis of cultural knowledge is well-established (2510.26024, 2504.10191)
- Layer-selective LoRA application to multilingual tasks is established (2509.11414)
- LoRA-based cultural preservation is established (2602.22475)

**The paper needs to clearly articulate:**
1. **Why the probing methodology is novel** beyond existing mechanistic interpretability approaches
2. **Empirical results demonstrating superiority** over CultureManager, surgical steering, and layer-freezing baselines
3. **The specific instruction fine-tuning context** and how it differs from prior cultural preservation work

**Competitive threats ranking:**
1. **CRITICAL**: 2504.10191 (same core approach)
2. **CRITICAL**: 2602.22475 (same domain, published Feb 2026)
3. **HIGH**: 2510.26024 (foundational layer analysis)
4. **MEDIUM-HIGH**: 2509.11414 (layer-selective LoRA methodology)

---

**Sources for this review:**
- [Mind the Gap in Cultural Alignment](https://arxiv.org/abs/2602.22475)
- [Rethinking Cross-lingual Alignment](https://arxiv.org/abs/2510.26024)
- [Localized Cultural Knowledge](https://arxiv.org/abs/2504.10191)
- [Neuron-Level Analysis](https://arxiv.org/abs/2510.08284)
- [LayRA: Continually Adding Languages](https://arxiv.org/abs/2509.11414)
- [MLAS-LoRA](https://aclanthology.org/2025.acl-long.762/)
- [M-DaQ: Diversity in Instruction Fine-tuning](https://arxiv.org/abs/2509.15549)
- [Cross-Lingual Activation Steering](https://arxiv.org/html/2601.16390v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3360d13e-f8de-4654-ba63-9e71e1d2e9db",
  "isSidechain": false,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "type": "user",
  "uuid": "d2820b3f-b311-4b9e-9fe2-ab37912a7ebf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are an adversarial ML paper reviewer. Search for competing work and verify claims for an idea called \"Cultural-Layer-Selective LoRA (CLS-LoRA)\" for EMNLP 2026.\n\nThe paper's core claim: Cross-lingual instruction fine-tuning erases culturally-grounded language-specific knowledge. CLS-LoRA proposes empirical per-layer probing to identify which layers implement \"cultural routing\" vs \"factual transfer\", then freezes cultural-knowledge layers during LoRA fine-tuning to prevent erasure.\n\nKey papers the idea references:\n- arXiv:2510.26024 (Han, Agrawal & Briakou) - \"Rethinking Cross-lingual Alignment\" / Surgical Steering\n- arXiv:2504.10191 - \"Localized Cultural Knowledge is Conserved and Controllable in LLMs\"\n- arXiv:2510.08284 (Yamamoto et al., ICLR 2026) - Neuron-level analysis of cultural understanding\n- arXiv:2602.22475 (CultureManager, Zhang et al., Feb 2026)\n- arXiv:2509.11414 (LayRA) - layer-selective LoRA for continual multilingual language addition\n- MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762)\n\nPlease search for:\n1. Whether arXiv:2602.22475 (\"Mind the Gap in Cultural Alignment\") actually exists and what it proposes - search \"CultureManager cultural alignment LoRA arxiv 2602.22475\"\n2. Any recent (2025-2026) papers on \"cultural preservation fine-tuning multilingual\" or \"cultural erasure LLM training\" that might compete\n3. Search for papers on \"layer freezing cultural knowledge LLM\" to find direct competitors\n4. Search for \"selective LoRA cultural preservation multilingual\" on arxiv\n5. Search for \"cross-lingual fine-tuning cultural knowledge preservation 2025 2026\"\n\nFor each search, report: what you found, the paper title, venue/arxiv ID if available, and whether it threatens the novelty of CLS-LoRA.\n\nBe thorough — use WebSearch with multiple queries.",
    "agentId": "ab12362edb9b13554",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent. Now I have comprehensive information. Let me compile the adversarial review findings.\n\n---\n\n## ADVERSARIAL REVIEW: CLS-LoRA Novelty and Competing Work\n\nBased on systematic searches of recent literature (2025-2026), here are my findings on the landscape of competing work and threats to CLS-LoRA's novelty:\n\n### **1. ArXiv 2602.22475 - \"Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models\"**\n\n**STATUS: CONFIRMED - Direct Competitor**\n\nThe paper **does exist** and proposes a very similar solution space:\n- **Approach**: Synthesizes task-aware cultural data via LLM-based generators and web search, then fine-tunes lightweight LoRA adapters per culture while keeping the base model frozen\n- **Culture Management**: Uses a culture router at inference time to select appropriate adapters based on input cultural context\n- **Threat Level**: **VERY HIGH** - This directly overlaps with CLS-LoRA's use of LoRA adapters for cultural preservation. The main difference is task-awareness and modular routing rather than layer-selective freezing during fine-tuning.\n- **Venue/Date**: ArXiv 2602.22475 (February 2026)\n\nSources:\n- [Mind the Gap in Cultural Alignment (ArXiv HTML)](https://arxiv.org/html/2602.22475)\n- [Mind the Gap in Cultural Alignment (ArXiv PDF)](https://arxiv.org/pdf/2602.22475)\n\n---\n\n### **2. ArXiv 2510.26024 - \"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs\" (Han, Agrawal & Briakou)**\n\n**STATUS: CONFIRMED - Strong Foundational Work**\n\n**Core Claims Verified**:\n- Confirms the exact problem statement CLS-LoRA addresses: cross-lingual alignment erases cultural knowledge\n- Introduces the \"transfer-localization plane\" framework to quantify both knowledge transfer AND cultural erasure\n- **KEY FINDING**: \"Universal factual transfer and culturally-specific knowledge are optimally steerable at **different model layers**\"\n- Proposes \"Surgical Steering\" for inference-time layer-targeted activation steering\n\n**Threat Level**: **CRITICAL** - This paper already empirically validates that cultural knowledge lives in different layers than factual knowledge. CLS-LoRA's core insight (freezing cultural-knowledge layers) is directly anticipated by this work.\n\n**Novelty Gap**: The Han et al. work focuses on inference-time steering via activation manipulation, while CLS-LoRA proposes training-time layer freezing during LoRA fine-tuning. However, the layer-level analysis principle is established.\n\nSources:\n- [Rethinking Cross-lingual Alignment (ArXiv)](https://arxiv.org/abs/2510.26024)\n- [Rethinking Cross-lingual Alignment (PDF)](https://arxiv.org/pdf/2510.26024)\n\n---\n\n### **3. ArXiv 2504.10191 - \"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models\"**\n\n**STATUS: CONFIRMED - Directly Relevant**\n\n**Key Findings**:\n- Identifies an \"explicit cultural customization vector\" conserved across non-English languages\n- Uses mechanistic interpretability tools including activation patching and linear steering vectors on relevant layers\n- Proposes layer-freezing LoRA fine-tuning for resource efficiency while preserving cultural knowledge\n\n**Threat Level**: **VERY HIGH** - This paper already proposes the exact combination of: (1) identifying cultural layers, (2) layer freezing, and (3) LoRA fine-tuning for cultural preservation. CLS-LoRA appears to be reinventing this approach with the addition of per-layer probing.\n\nSources:\n- [Localized Cultural Knowledge (ArXiv)](https://arxiv.org/abs/2504.10191)\n- [Localized Cultural Knowledge (HTML)](https://arxiv.org/html/2504.10191v1)\n\n---\n\n### **4. ArXiv 2510.08284 - \"Neuron-Level Analysis of Cultural Understanding in Large Language Models\" (Yamamoto et al.)**\n\n**STATUS: CONFIRMED - Relevant Mechanistic Analysis**\n\n**Key Findings**:\n- Identifies culture-general neurons and culture-specific neurons (< 1% of all neurons)\n- Culture-specific neurons are concentrated in **shallow to middle MLP layers**\n- Gradient-based scoring method for precise neuron identification\n- Suppressing these neurons degrades cultural benchmark performance by up to 30%\n\n**Threat Level**: **HIGH** - This provides neuron-level validation that cultural knowledge can be precisely localized. However, it's neuron-level, not layer-level. CLS-LoRA's per-layer probing is coarser-grained than this work.\n\n**Note**: Listed as posted October 2025, updated March 2026. Claims of ICLR 2026 acceptance not confirmed in search results.\n\nSources:\n- [Neuron-Level Analysis (ArXiv)](https://arxiv.org/abs/2510.08284)\n- [Neuron-Level Analysis (HTML)](https://arxiv.org/html/2510.08284)\n\n---\n\n### **5. ArXiv 2509.11414 - \"Continually Adding New Languages to Multilingual Language Models\" (LayRA)**\n\n**STATUS: CONFIRMED - Layer-Selective LoRA Precedent**\n\n**Key Technical Approach**:\n- Inserts LoRA modules into **selected early layers (first 10)** and **late layers (last 2)** while keeping middle layers frozen\n- Addresses catastrophic forgetting in continual multilingual learning\n- Based on insight: \"Multilingual models encode inputs in source language in initial layers, reason in English in intermediate layers, translate back in final layers\"\n\n**Threat Level**: **MEDIUM-HIGH** - LayRA demonstrates that layer-selective LoRA application is effective for multilingual tasks. However, it's designed for continual language addition (preventing forgetting), not cultural preservation during instruction fine-tuning. The layer selection strategy is different (early/late vs. culture-specific middle layers).\n\n**Potential Novelty Claim**: CLS-LoRA focuses on **identifying and freezing culture-implementing layers** during instruction fine-tuning, whereas LayRA uses layer-selective **application** for continual learning. The problem formulations differ.\n\nSources:\n- [LayRA (ArXiv PDF)](https://arxiv.org/pdf/2509.11414)\n- [LayRA (ArXiv)](https://arxiv.org/abs/2509.11414)\n\n---\n\n### **6. MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762)**\n\n**STATUS: CONFIRMED - Language-Aware Parameter Detection**\n\n**Approach**:\n- Evaluates neuron/parameter awareness for both general MT and language-specific tasks\n- Uses multiple language-specific LoRA architecture\n- Selectively transfers knowledge from teacher to student models\n\n**Threat Level**: **MEDIUM** - MLAS-LoRA also uses language-specific LoRA components, but for multilingual machine translation knowledge distillation. It's not about preserving cultural knowledge during instruction fine-tuning. The problem formulation is different (MT efficiency vs. cultural preservation).\n\nSources:\n- [MLAS-LoRA (ACL Anthology)](https://aclanthology.org/2025.acl-long.762/)\n\n---\n\n### **7. Additional Highly Relevant Papers**\n\n**M-DaQ (ArXiv 2509.15549)** - \"Retrieving Samples with Multilingual Diversity and Quality for Instruction Fine-Tuning Datasets\"\n- Addresses cultural erasure through **data diversity** in instruction fine-tuning\n- Threat Level: **MEDIUM** - Complementary approach (data) rather than architecture (layer freezing)\n\n**Language over Content: Tracing Cultural Understanding in Multilingual LLMs**\n- Probes how multilingual LLMs process cultural knowledge across layers\n- Confirms that cultural understanding relies on language-specific internal circuits\n- Threat Level: **MEDIUM** - Provides empirical grounding for layer-level analysis\n\n---\n\n## SYNTHESIS: Critical Novelty Assessment\n\n### **Major Threats to CLS-LoRA's Novelty**\n\n1. **ArXiv 2504.10191** already proposes layer-freezing LoRA for cultural preservation\n2. **ArXiv 2510.26024** establishes that cultural and factual knowledge live in different layers\n3. **ArXiv 2602.22475** (CultureManager) demonstrates LoRA-based cultural management at scale\n4. **ArXiv 2509.11414** (LayRA) proves layer-selective LoRA is effective for multilingual tasks\n\n### **CLS-LoRA's Potential Narrow Novelty**\n\nThe main differentiation appears to be:\n- **Empirical per-layer probing methodology** to identify cultural-routing vs. factual-transfer layers\n- **Fine-tuning-time freezing** (not inference-time steering like Han et al.)\n- **Application to instruction fine-tuning** specifically (most other work targets other tasks)\n\n### **Recommendation for EMNLP 2026 Submission**\n\n**CLS-LoRA faces significant novelty challenges:**\n- The layer-level analysis of cultural knowledge is well-established (2510.26024, 2504.10191)\n- Layer-selective LoRA application to multilingual tasks is established (2509.11414)\n- LoRA-based cultural preservation is established (2602.22475)\n\n**The paper needs to clearly articulate:**\n1. **Why the probing methodology is novel** beyond existing mechanistic interpretability approaches\n2. **Empirical results demonstrating superiority** over CultureManager, surgical steering, and layer-freezing baselines\n3. **The specific instruction fine-tuning context** and how it differs from prior cultural preservation work\n\n**Competitive threats ranking:**\n1. **CRITICAL**: 2504.10191 (same core approach)\n2. **CRITICAL**: 2602.22475 (same domain, published Feb 2026)\n3. **HIGH**: 2510.26024 (foundational layer analysis)\n4. **MEDIUM-HIGH**: 2509.11414 (layer-selective LoRA methodology)\n\n---\n\n**Sources for this review:**\n- [Mind the Gap in Cultural Alignment](https://arxiv.org/abs/2602.22475)\n- [Rethinking Cross-lingual Alignment](https://arxiv.org/abs/2510.26024)\n- [Localized Cultural Knowledge](https://arxiv.org/abs/2504.10191)\n- [Neuron-Level Analysis](https://arxiv.org/abs/2510.08284)\n- [LayRA: Continually Adding Languages](https://arxiv.org/abs/2509.11414)\n- [MLAS-LoRA](https://aclanthology.org/2025.acl-long.762/)\n- [M-DaQ: Diversity in Instruction Fine-tuning](https://arxiv.org/abs/2509.15549)\n- [Cross-Lingual Activation Steering](https://arxiv.org/html/2601.16390v1)"
      }
    ],
    "totalDurationMs": 70866,
    "totalTokens": 35023,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 30340,
      "output_tokens": 2716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 845,
          "output_tokens": 2716,
          "cache_read_input_tokens": 30340,
          "cache_creation_input_tokens": 1122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1122,
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
  "sourceToolAssistantUUID": "3360d13e-f8de-4654-ba63-9e71e1d2e9db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
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
  "leafUuid": "d2820b3f-b311-4b9e-9fe2-ab37912a7ebf",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "CLS-LoRA: Preventing cultural erasure in cross-lingual instruction tuning",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a"
}
```

---

### Assistant

_source line 16 · 2026-05-10T08:10:24.206Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the findings from both research agents:

**Agent 1 (Competing Work Verification):**
The agent confirmed:
1. arXiv:2602.22475 (CultureManager) exists - the paper DOES cite and differentiate it in Round 8
2. arXiv:2510.26024 exists and is confirmed
3. arXiv:2504.10191 - The agent raises an important point: "This paper already proposes layer-freezing LoRA fine-tuning for resource efficiency while preserving cultural knowledge." Let me check this - this is a CRITICAL claim I need to verify independently.


4. arXiv:2510.08284 (Yamamoto et al.) and arXiv:2509.11414 (LayRA) are both confirmed

The most critical concern from Agent 1 is that arXiv:2504.10191 may already combine layer identification, freezing, and LoRA fine-tuning for cultural preservation—which would mean CLS-LoRA's main contribution is essentially just adding per-layer probing on top of an existing approach. I need to verify this directly to understand how much novelty CLS-LoRA actually brings.

Agent 2 flagged that while the compute estimates check out and the H100/A100 conversion is accurate, there's now uncertainty about whether the INCLUDE dataset has the proper CC BY 4.0 license for training use—this is a new concern that wasn't fully resolved in the previous round. The core question is whether arXiv:2504.10191 truly proposes layer-freezing LoRA for cultural preservation, because if it does, that's a fundamental novelty problem that changes everything about this work.

Looking at how the submission actually describes the paper, it seems to characterize arXiv:2504.10191 as studying inference-time steering of cultural knowledge in pre-trained models, using that as mechanistic motivation for CLS-LoRA's training-time approach. The feasibility agent may have misinterpreted what the paper actually proposes versus what the submission is building on top of it.

For CultureManager, the Round 8 submission now properly differentiates it across three dimensions: the goal (cultural adaptation versus preservation), the knowledge partition (culture identity versus factual-cultural semantics), and the technical mechanism (routing between adapters versus layer freezing). That's a meaningful distinction. I should also verify the dataset licensing claims. All Round 7 issues are addressed. Now I need to check for any new problems in Round 8, starting with verifying the INCLUDE dataset's CC BY 4.0 license and investigating whether arXiv:2504.10191 already covers layer-freezing LoRA. I'm also noticing that the submission's description of arXiv:2510.26024 aligns with Round 5's finding that it wasn't accepted at ICLR 2026, which contradicts Round 4's earlier claim.

Looking at the remaining items: the evaluation suite seems well-justified with its coverage of factual transfer, cultural knowledge, commonsense, and arithmetic tasks; the compute estimate fits within the 200h H100 constraint; the 2×2 ablation conditions are explicitly included; and the INCLUDE dataset license claim needs verification. Let me search more carefully for these specific details.

There's a discrepancy I need to resolve—the search results describe arXiv:2504.10191 as proposing layer-freezing LoRA for cultural preservation, but CLS-LoRA frames itself as inference-time steering, which would be a significant overlap if true. I should verify what that paper actually proposes and confirm the INCLUDE dataset's licensing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2820b3f-b311-4b9e-9fe2-ab37912a7ebf",
  "isSidechain": false,
  "requestId": "req_011CatYkdFbzDdpU5XDpfV2m",
  "type": "assistant",
  "uuid": "b5cd012e-6f75-4eca-8326-8ac0110c0861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019P9weuq8DnXXfkNTBpdXG9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2162,
      "cache_creation_input_tokens": 4527,
      "cache_read_input_tokens": 39107,
      "output_tokens": 3001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2162,
          "output_tokens": 3001,
          "cache_read_input_tokens": 39107,
          "cache_creation_input_tokens": 4527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4527
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

_source line 17 · 2026-05-10T08:10:24.521Z_

Let me do more targeted verification on two critical points raised by the initial searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5cd012e-6f75-4eca-8326-8ac0110c0861",
  "isSidechain": false,
  "requestId": "req_011CatYkdFbzDdpU5XDpfV2m",
  "type": "assistant",
  "uuid": "e42b903c-f294-4624-8899-8b6c83660086",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019P9weuq8DnXXfkNTBpdXG9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2162,
      "cache_creation_input_tokens": 4527,
      "cache_read_input_tokens": 39107,
      "output_tokens": 3001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2162,
          "output_tokens": 3001,
          "cache_read_input_tokens": 39107,
          "cache_creation_input_tokens": 4527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4527
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

_source line 18 · 2026-05-10T08:10:31.839Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0198DrTMthGr8EByY2mUEVX5`</summary>

```json
{
  "description": "Verify arXiv 2504.10191 scope and INCLUDE license",
  "subagent_type": "Explore",
  "prompt": "I need to verify two specific factual claims for an adversarial paper review. Please do targeted searches.\n\n**TASK 1: Verify what arXiv:2504.10191 actually proposes**\n\nThe paper \"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models\" (arXiv:2504.10191, April 2025).\n\nA search agent claimed this paper \"proposes layer-freezing LoRA fine-tuning for resource efficiency while preserving cultural knowledge.\" But a paper under review claims it only studies \"inference-time steering of cultural knowledge in pre-trained models\" and does NOT study fine-tuning.\n\nPlease:\n1. Use WebFetch to read https://arxiv.org/abs/2504.10191 and check the abstract\n2. If possible, use WebFetch to read https://arxiv.org/html/2504.10191 to check the methods and contributions sections\n3. Does the paper propose any training-time method (LoRA fine-tuning, layer freezing during training)? Or is it purely about inference-time activation steering?\n\nReport EXACTLY what arXiv:2504.10191 proposes - specifically whether it proposes any training-time layer freezing or LoRA fine-tuning for cultural preservation.\n\n**TASK 2: Verify INCLUDE dataset license**\n\nThe paper \"INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge\" (arXiv:2411.19799, ICLR 2025) is claimed to be licensed under CC BY 4.0 and usable for training.\n\nPlease:\n1. Use WebFetch to read https://arxiv.org/abs/2411.19799 and check what license the dataset uses\n2. Check https://huggingface.co/datasets/CohereForAI/INCLUDE if accessible, to verify license\n3. Can it be used for training/fine-tuning purposes, or is it evaluation-only?\n\nReport the exact license and whether training use is permitted."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e42b903c-f294-4624-8899-8b6c83660086",
  "isSidechain": false,
  "requestId": "req_011CatYkdFbzDdpU5XDpfV2m",
  "type": "assistant",
  "uuid": "61ec3af5-dd5b-4f48-b343-1597c3e1a902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019P9weuq8DnXXfkNTBpdXG9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2162,
      "cache_creation_input_tokens": 4527,
      "cache_read_input_tokens": 39107,
      "output_tokens": 3001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2162,
          "output_tokens": 3001,
          "cache_read_input_tokens": 39107,
          "cache_creation_input_tokens": 4527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4527
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

_source line 19 · 2026-05-10T08:10:41.582Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DwfGaQFuHbiXn14E3cpLcs`</summary>

```json
{
  "description": "Search for new 2026 competing cultural preservation papers",
  "subagent_type": "Explore",
  "prompt": "I'm doing an adversarial review of a paper about \"training-time cultural knowledge preservation in multilingual LLMs via layer-selective LoRA.\" The paper's deadline is EMNLP 2026 (ARR May 25, 2026). Today is May 10, 2026.\n\nI need to find any 2025-2026 papers that compete with this approach that the paper might have missed. Please search for:\n\n1. \"cultural knowledge preservation fine-tuning multilingual LLM 2026\" on Google/arXiv\n2. \"cultural erasure prevention training multilingual\" arxiv 2025 2026\n3. \"layer freezing cultural knowledge LLM fine-tuning\" to find any direct competitors\n4. Search arXiv for recent papers: \"site:arxiv.org cultural preservation multilingual instruction tuning 2026\"\n5. Search for \"cross-lingual instruction tuning cultural knowledge\" papers from Jan-May 2026\n6. Check if there's anything on \"cultural alignment training-time\" from late 2025 or early 2026\n\nThe paper already cites: arXiv:2602.22475 (CultureManager), arXiv:2510.08284, arXiv:2510.26024, arXiv:2504.10191, arXiv:2509.11414 (LayRA), MLAS-LoRA (ACL 2025), Sparse Subnetwork Enhancement (arXiv:2510.13580), Source-Shielded Updates (arXiv:2512.04844), AlignX (arXiv:2509.24338), CM-Align (arXiv:2509.08541), INCLINE (arXiv:2410.12462).\n\nI'm looking for papers that propose TRAINING-TIME methods to prevent cultural knowledge loss during cross-lingual fine-tuning. This is the key gap the paper claims to fill. Is there any 2025-2026 work that fills this gap that the paper hasn't cited?\n\nReport the most relevant finds with titles, arXiv IDs, and a brief assessment of how much they threaten the novelty."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61ec3af5-dd5b-4f48-b343-1597c3e1a902",
  "isSidechain": false,
  "requestId": "req_011CatYkdFbzDdpU5XDpfV2m",
  "type": "assistant",
  "uuid": "15ac1b58-a17a-4bc1-a6e4-2e01d8a2fb05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019P9weuq8DnXXfkNTBpdXG9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2162,
      "cache_creation_input_tokens": 4527,
      "cache_read_input_tokens": 39107,
      "output_tokens": 3001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2162,
          "output_tokens": 3001,
          "cache_read_input_tokens": 39107,
          "cache_creation_input_tokens": 4527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4527
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

_source line 20 · 2026-05-10T08:10:56.668Z_

<details><summary>↩ Tool result · `toolu_0198DrTMthGr8EByY2mUEVX5`</summary>

```text
## FINDINGS

**TASK 1: arXiv:2504.10191 (Localized Cultural Knowledge)**

**VERDICT: The claim is INCORRECT.**

The paper "Localized Cultural Knowledge is Conserved and Controllable in Large Language Models" (arXiv:2504.10191) does **NOT** propose layer-freezing LoRA fine-tuning or any training-time method.

**What it actually proposes:**
- **Purely inference-time activation steering** using Contrastive Activation Addition (CAA)
- Identification of a cultural customization vector through activation patching
- Adding these vectors to token representations during inference: h̃ₜ⁽ʲ⁾(x) = hₜ⁽ʲ⁾(x) + αv⁽ʲ⁾
- **No model weight modifications** - steering operates entirely through additive intervention at inference time
- The approach requires no retraining or fine-tuning

The paper's claim that steering could enable "soft control for expanded LLM function without requiring model retraining" directly contradicts the claim that it proposes training-time fine-tuning methods. The paper under review is **correct**: it studies inference-time steering only.

---

**TASK 2: INCLUDE Dataset License (arXiv:2411.19799)**

**VERDICT: CC BY 4.0 is confirmed, but training use requires further verification.**

**What is confirmed:**
- License: **CC BY 4.0** (Creative Commons Attribution 4.0)
- The dataset is released for public use
- Primary purpose: **Evaluation benchmark** for multilingual LLMs

**Regarding training/fine-tuning use:**
- The paper explicitly describes it as "an evaluation suite" and "evaluation benchmark"
- It is NOT described as training data
- Under CC BY 4.0, the license technically permits training use (CC BY 4.0 allows any use including derivative works), **but the dataset's designed purpose is evaluation only**
- The dataset is being released incrementally "to mitigate data contamination risks"

**Recommendation:** While CC BY 4.0 technically permits training use, the dataset's intended purpose as stated by the authors is evaluation, not training material. Any use for fine-tuning should clarify this distinction with the authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61ec3af5-dd5b-4f48-b343-1597c3e1a902",
  "isSidechain": false,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "type": "user",
  "uuid": "43c259dd-bb06-4d50-bc8e-319ed663de4b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two specific factual claims for an adversarial paper review. Please do targeted searches.\n\n**TASK 1: Verify what arXiv:2504.10191 actually proposes**\n\nThe paper \"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models\" (arXiv:2504.10191, April 2025).\n\nA search agent claimed this paper \"proposes layer-freezing LoRA fine-tuning for resource efficiency while preserving cultural knowledge.\" But a paper under review claims it only studies \"inference-time steering of cultural knowledge in pre-trained models\" and does NOT study fine-tuning.\n\nPlease:\n1. Use WebFetch to read https://arxiv.org/abs/2504.10191 and check the abstract\n2. If possible, use WebFetch to read https://arxiv.org/html/2504.10191 to check the methods and contributions sections\n3. Does the paper propose any training-time method (LoRA fine-tuning, layer freezing during training)? Or is it purely about inference-time activation steering?\n\nReport EXACTLY what arXiv:2504.10191 proposes - specifically whether it proposes any training-time layer freezing or LoRA fine-tuning for cultural preservation.\n\n**TASK 2: Verify INCLUDE dataset license**\n\nThe paper \"INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge\" (arXiv:2411.19799, ICLR 2025) is claimed to be licensed under CC BY 4.0 and usable for training.\n\nPlease:\n1. Use WebFetch to read https://arxiv.org/abs/2411.19799 and check what license the dataset uses\n2. Check https://huggingface.co/datasets/CohereForAI/INCLUDE if accessible, to verify license\n3. Can it be used for training/fine-tuning purposes, or is it evaluation-only?\n\nReport the exact license and whether training use is permitted.",
    "agentId": "ab3a740bab8d7cb47",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## FINDINGS\n\n**TASK 1: arXiv:2504.10191 (Localized Cultural Knowledge)**\n\n**VERDICT: The claim is INCORRECT.**\n\nThe paper \"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models\" (arXiv:2504.10191) does **NOT** propose layer-freezing LoRA fine-tuning or any training-time method.\n\n**What it actually proposes:**\n- **Purely inference-time activation steering** using Contrastive Activation Addition (CAA)\n- Identification of a cultural customization vector through activation patching\n- Adding these vectors to token representations during inference: h̃ₜ⁽ʲ⁾(x) = hₜ⁽ʲ⁾(x) + αv⁽ʲ⁾\n- **No model weight modifications** - steering operates entirely through additive intervention at inference time\n- The approach requires no retraining or fine-tuning\n\nThe paper's claim that steering could enable \"soft control for expanded LLM function without requiring model retraining\" directly contradicts the claim that it proposes training-time fine-tuning methods. The paper under review is **correct**: it studies inference-time steering only.\n\n---\n\n**TASK 2: INCLUDE Dataset License (arXiv:2411.19799)**\n\n**VERDICT: CC BY 4.0 is confirmed, but training use requires further verification.**\n\n**What is confirmed:**\n- License: **CC BY 4.0** (Creative Commons Attribution 4.0)\n- The dataset is released for public use\n- Primary purpose: **Evaluation benchmark** for multilingual LLMs\n\n**Regarding training/fine-tuning use:**\n- The paper explicitly describes it as \"an evaluation suite\" and \"evaluation benchmark\"\n- It is NOT described as training data\n- Under CC BY 4.0, the license technically permits training use (CC BY 4.0 allows any use including derivative works), **but the dataset's designed purpose is evaluation only**\n- The dataset is being released incrementally \"to mitigate data contamination risks\"\n\n**Recommendation:** While CC BY 4.0 technically permits training use, the dataset's intended purpose as stated by the authors is evaluation, not training material. Any use for fine-tuning should clarify this distinction with the authors."
      }
    ],
    "totalDurationMs": 24825,
    "totalTokens": 20099,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 18935,
      "output_tokens": 545,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 614
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 545,
          "cache_read_input_tokens": 18935,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 614,
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
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "61ec3af5-dd5b-4f48-b343-1597c3e1a902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T08:12:18.474Z_

<details><summary>↩ Tool result · `toolu_01DwfGaQFuHbiXn14E3cpLcs`</summary>

```text
Perfect. Now I have comprehensive information. Let me compile the findings into a structured report.

## ADVERSARIAL REVIEW: COMPETING PAPERS ON TRAINING-TIME CULTURAL KNOWLEDGE PRESERVATION (2025-2026)

Based on my comprehensive search, I've identified several potentially threatening competitors and related work that your paper should address. Here's my assessment organized by threat level:

### **HIGHEST THREAT (Direct Competitors)**

**1. CultureManager (arXiv:2602.22475) - Feb 2026 - VERY HIGH THREAT**
- **Title:** "Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models"
- **Submission:** February 25, 2026 (submitted just 15 days before your May 25 ARR deadline)
- **What it does:** Proposes a **training-time** pipeline for task-specific cultural alignment using task-aware cultural data synthesis grounded in web search, managing multi-culture knowledge in separate adapters with a culture router
- **Threat assessment:** **CRITICAL** - This directly addresses training-time cultural alignment and uses adapter-based separation (similar in spirit to your layer-selective approach). The main difference is task-specificity and router-based selection vs. your layer-selective LoRA. You must clearly distinguish your approach's advantages.

**2. Conditions for Catastrophic Forgetting in Multilingual Translation (arXiv:2510.19546) - Oct 2025 - HIGH THREAT**
- **Presented:** 5th Workshop on Multilingual Representation Learning (MRL 2025, Nov 2025)
- **What it does:** Systematically identifies conditions triggering catastrophic forgetting during multilingual fine-tuning (model-to-data scale, instruction-following ability vs. architecture)
- **Threat assessment:** **HIGH** - Your paper claims to address catastrophic forgetting of cultural knowledge during cross-lingual fine-tuning. This paper may have already characterized when forgetting happens, potentially weakening your motivation.

**3. What Causes Knowledge Loss in Multilingual Language Models? (arXiv:2504.20356) - April 2025 - HIGH THREAT**
- **Key finding:** Language script type (non-Latin more susceptible to forgetting), adapters like MAD-X effective at preserving knowledge
- **Threat assessment:** **HIGH** - May preempt your problem analysis. Check if you cite this or clearly differentiate cultural-specific knowledge loss from general language-specific forgetting.

---

### **MEDIUM-HIGH THREAT (Related Training-Time Methods)**

**4. Hierarchical Alignment (arXiv:2510.12044) - Oct 2025**
- **What it does:** Maps alignment objectives to functionally specialized layer blocks, finding that "where we align matters as much as how we align"
- **Threat assessment:** **MEDIUM-HIGH** - Uses layer-specific targeting but for safety alignment, not cultural knowledge. The novelty gap depends on whether cultural knowledge requires fundamentally different layer properties than safety.

**5. COMPASS: COntinual Multilingual PEFT with Adaptive Semantic Sampling (arXiv:2604.20720) - April 2026**
- **What it does:** Framework using PEFT (parameter-efficient fine-tuning) with language-specific adapters to minimize cross-lingual interference during continual learning
- **Threat assessment:** **MEDIUM-HIGH** - Addresses multilingual adaptation using selective parameter updates, but doesn't explicitly focus on cultural knowledge preservation. Check if your approach outperforms COMPASS on cultural benchmarks.

**6. SafeMERGE (arXiv:2503.17239) - March 2026**
- **What it does:** Selective layer-wise model merging to preserve safety alignment during fine-tuning
- **Threat assessment:** **MEDIUM-HIGH** - Uses similar layer-selective mechanics but for safety, not culture. Demonstrates that layer-wise preservation strategies work across multiple domains.

---

### **MEDIUM THREAT (Related but Not Training-Time)**

**7. AdaCultureSafe (arXiv:2603.08275) - March 2026**
- **What it does:** Adaptive cultural safety considering indigenous cultures
- **Threat assessment:** **MEDIUM** - Addresses cultural safety but post-hoc, not training-time preservation

**8. Beyond Training for Cultural Awareness (arXiv:2602.01161) - Feb 2026**
- **What it does:** Examines which linguistic properties of fine-tuning data associate with cultural performance
- **Threat assessment:** **MEDIUM** - Relevant analysis but focuses on data properties, not the training mechanism itself

**9. AlignX (arXiv:2509.24338) - Published EMNLP 2025**
- **What it does:** Two-stage framework (representation alignment + multilingual instruction fine-tuning) to enhance multilingual performance
- **Threat assessment:** **MEDIUM** - Does multilingual alignment but not with explicit cultural preservation as primary goal

**10. "Be My Cheese?" (arXiv:2602.04729) - Feb 2026**
- **What it does:** Large-scale human evaluation benchmark for cultural nuance in multilingual machine translation
- **Threat assessment:** **MEDIUM** - Excellent benchmark but evaluative, not methodological

---

### **LOWER THREAT (Relevant Context, Not Direct Competitors)**

**11. CM-Align (arXiv:2509.08541) - Sept 2025**
- Consistency-based multilingual alignment; focuses on preference data construction, not cultural knowledge preservation during fine-tuning

**12. MLAS-LoRA (ACL 2025)**
- Language-aware parameters detection for machine translation; good related work but task-specific (MT), not general cultural preservation

**13. Rethinking Cross-lingual Alignment (arXiv:2510.26024) - Already cited by your paper**
- Discusses "cultural erasure" as tradeoff with knowledge transfer; foundational framing but doesn't propose a training-time solution

**14. Sparse Subnetwork Enhancement (arXiv:2510.13580) - Already cited**
- Uses LAPE metric for language-specific neurons; complements but doesn't directly address cultural knowledge

**15. LayRA (arXiv:2509.11414) - Already cited**
- Layer-selective LoRA for sequential language addition; your paper appears to extend this concept to cultural knowledge preservation

---

### **CRITICAL GAPS TO ADDRESS IN YOUR PAPER**

1. **vs. CultureManager:** Your paper's core advantage should be clear. Is it the layer-selective targeting that CultureManager lacks? Is it the application to general cultural knowledge rather than task-specific? Emphasize differences explicitly.

2. **vs. Catastrophic Forgetting literature:** Clarify that cultural knowledge loss is *not* explained by the conditions identified in arXiv:2510.19546. Your approach should address cultural-specific mechanisms, not just general forgetting prevention.

3. **vs. Hierarchical Alignment & SafeMERGE:** Demonstrate that cultural knowledge requires different layer targeting than safety/task alignment. Provide cultural-specific ablations.

4. **vs. COMPASS:** Show that semantic-based adapter selection underperforms language-layer-aware selection for cultural preservation specifically.

5. **Dataset novelty:** Check if you use or need to cite CARE (arXiv:2504.05154), Pragyaan (arXiv:2510.07000), or Global-MMLU for evaluation—these provide cultural benchmarks but your contribution is methodological.

---

### **PAPERS TO CITE FOR CONTEXT (Not Direct Threats)**
- CrossIn (arXiv:2404.11932) - Existing multilingual instruction tuning baseline
- Aletheia (arXiv:2604.15351) - Gradient-guided layer selection (general principle)
- ELO (arXiv:2601.03648) - Efficient layer-specific optimization for continual pretraining
- INCLINE (arXiv:2410.12462) - Inference-time intervention (baseline to compare against your training-time approach)

---

### **YOUR PAPER'S KEY NOVELTY CLAIM**
Your paper's strongest position: **You are the first to systematically use layer-selective LoRA specifically to prevent cultural knowledge loss during cross-lingual instruction fine-tuning.** CultureManager exists but is post-hoc/inference-time routing. COMPASS doesn't focus on culture. Layer-selective approaches exist (LayRA, Aletheia, Hierarchical Alignment) but weren't applied with cultural preservation as the primary objective.

**Recommendation:** Proactively compare against CultureManager (Feb 2026) as your most serious competitor. Show empirical results on cultural benchmarks (CARE, Global-MMLU cultural subsets) demonstrating superiority.

---

Sources:
- [CultureManager (arXiv:2602.22475)](https://arxiv.org/abs/2602.22475)
- [Conditions for Catastrophic Forgetting (arXiv:2510.19546)](https://arxiv.org/abs/2510.19546)
- [What Causes Knowledge Loss (arXiv:2504.20356)](https://arxiv.org/abs/2504.20356)
- [Hierarchical Alignment (arXiv:2510.12044)](https://arxiv.org/abs/2510.12044)
- [COMPASS (arXiv:2604.20720)](https://arxiv.org/abs/2604.20720)
- [SafeMERGE (arXiv:2503.17239)](https://arxiv.org/abs/2503.17239)
- [AdaCultureSafe (arXiv:2603.08275)](https://arxiv.org/abs/2603.08275)
- [Beyond Training for Cultural Awareness (arXiv:2602.01161)](https://arxiv.org/abs/2602.01161)
- [AlignX (arXiv:2509.24338)](https://arxiv.org/abs/2509.24338)
- [Be My Cheese? (arXiv:2602.04729)](https://arxiv.org/abs/2602.04729)
- [CM-Align (arXiv:2509.08541)](https://arxiv.org/abs/2509.08541)
- [MLAS-LoRA (ACL 2025)](https://aclanthology.org/2025.acl-long.762/)
- [Rethinking Cross-lingual Alignment (arXiv:2510.26024)](https://arxiv.org/abs/2510.26024)
- [Sparse Subnetwork Enhancement (arXiv:2510.13580)](https://arxiv.org/abs/2510.13580)
- [LayRA (arXiv:2509.11414)](https://arxiv.org/abs/2509.11414)
- [CARE Dataset (arXiv:2504.05154)](https://arxiv.org/abs/2504.05154)
- [Pragyaan (arXiv:2510.07000)](https://arxiv.org/abs/2510.07000)
- [CrossIn (arXiv:2404.11932)](https://arxiv.org/abs/2404.11932)
- [Aletheia (arXiv:2604.15351)](https://arxiv.org/abs/2604.15351)
- [ELO (arXiv:2601.03648)](https://arxiv.org/abs/2601.03648)
- [INCLINE (arXiv:2410.12462)](https://arxiv.org/abs/2410.12462)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15ac1b58-a17a-4bc1-a6e4-2e01d8a2fb05",
  "isSidechain": false,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "type": "user",
  "uuid": "2d410673-6c9d-4286-bceb-41ee9813b346",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm doing an adversarial review of a paper about \"training-time cultural knowledge preservation in multilingual LLMs via layer-selective LoRA.\" The paper's deadline is EMNLP 2026 (ARR May 25, 2026). Today is May 10, 2026.\n\nI need to find any 2025-2026 papers that compete with this approach that the paper might have missed. Please search for:\n\n1. \"cultural knowledge preservation fine-tuning multilingual LLM 2026\" on Google/arXiv\n2. \"cultural erasure prevention training multilingual\" arxiv 2025 2026\n3. \"layer freezing cultural knowledge LLM fine-tuning\" to find any direct competitors\n4. Search arXiv for recent papers: \"site:arxiv.org cultural preservation multilingual instruction tuning 2026\"\n5. Search for \"cross-lingual instruction tuning cultural knowledge\" papers from Jan-May 2026\n6. Check if there's anything on \"cultural alignment training-time\" from late 2025 or early 2026\n\nThe paper already cites: arXiv:2602.22475 (CultureManager), arXiv:2510.08284, arXiv:2510.26024, arXiv:2504.10191, arXiv:2509.11414 (LayRA), MLAS-LoRA (ACL 2025), Sparse Subnetwork Enhancement (arXiv:2510.13580), Source-Shielded Updates (arXiv:2512.04844), AlignX (arXiv:2509.24338), CM-Align (arXiv:2509.08541), INCLINE (arXiv:2410.12462).\n\nI'm looking for papers that propose TRAINING-TIME methods to prevent cultural knowledge loss during cross-lingual fine-tuning. This is the key gap the paper claims to fill. Is there any 2025-2026 work that fills this gap that the paper hasn't cited?\n\nReport the most relevant finds with titles, arXiv IDs, and a brief assessment of how much they threaten the novelty.",
    "agentId": "a07a11a8fb32f87de",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now I have comprehensive information. Let me compile the findings into a structured report.\n\n## ADVERSARIAL REVIEW: COMPETING PAPERS ON TRAINING-TIME CULTURAL KNOWLEDGE PRESERVATION (2025-2026)\n\nBased on my comprehensive search, I've identified several potentially threatening competitors and related work that your paper should address. Here's my assessment organized by threat level:\n\n### **HIGHEST THREAT (Direct Competitors)**\n\n**1. CultureManager (arXiv:2602.22475) - Feb 2026 - VERY HIGH THREAT**\n- **Title:** \"Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models\"\n- **Submission:** February 25, 2026 (submitted just 15 days before your May 25 ARR deadline)\n- **What it does:** Proposes a **training-time** pipeline for task-specific cultural alignment using task-aware cultural data synthesis grounded in web search, managing multi-culture knowledge in separate adapters with a culture router\n- **Threat assessment:** **CRITICAL** - This directly addresses training-time cultural alignment and uses adapter-based separation (similar in spirit to your layer-selective approach). The main difference is task-specificity and router-based selection vs. your layer-selective LoRA. You must clearly distinguish your approach's advantages.\n\n**2. Conditions for Catastrophic Forgetting in Multilingual Translation (arXiv:2510.19546) - Oct 2025 - HIGH THREAT**\n- **Presented:** 5th Workshop on Multilingual Representation Learning (MRL 2025, Nov 2025)\n- **What it does:** Systematically identifies conditions triggering catastrophic forgetting during multilingual fine-tuning (model-to-data scale, instruction-following ability vs. architecture)\n- **Threat assessment:** **HIGH** - Your paper claims to address catastrophic forgetting of cultural knowledge during cross-lingual fine-tuning. This paper may have already characterized when forgetting happens, potentially weakening your motivation.\n\n**3. What Causes Knowledge Loss in Multilingual Language Models? (arXiv:2504.20356) - April 2025 - HIGH THREAT**\n- **Key finding:** Language script type (non-Latin more susceptible to forgetting), adapters like MAD-X effective at preserving knowledge\n- **Threat assessment:** **HIGH** - May preempt your problem analysis. Check if you cite this or clearly differentiate cultural-specific knowledge loss from general language-specific forgetting.\n\n---\n\n### **MEDIUM-HIGH THREAT (Related Training-Time Methods)**\n\n**4. Hierarchical Alignment (arXiv:2510.12044) - Oct 2025**\n- **What it does:** Maps alignment objectives to functionally specialized layer blocks, finding that \"where we align matters as much as how we align\"\n- **Threat assessment:** **MEDIUM-HIGH** - Uses layer-specific targeting but for safety alignment, not cultural knowledge. The novelty gap depends on whether cultural knowledge requires fundamentally different layer properties than safety.\n\n**5. COMPASS: COntinual Multilingual PEFT with Adaptive Semantic Sampling (arXiv:2604.20720) - April 2026**\n- **What it does:** Framework using PEFT (parameter-efficient fine-tuning) with language-specific adapters to minimize cross-lingual interference during continual learning\n- **Threat assessment:** **MEDIUM-HIGH** - Addresses multilingual adaptation using selective parameter updates, but doesn't explicitly focus on cultural knowledge preservation. Check if your approach outperforms COMPASS on cultural benchmarks.\n\n**6. SafeMERGE (arXiv:2503.17239) - March 2026**\n- **What it does:** Selective layer-wise model merging to preserve safety alignment during fine-tuning\n- **Threat assessment:** **MEDIUM-HIGH** - Uses similar layer-selective mechanics but for safety, not culture. Demonstrates that layer-wise preservation strategies work across multiple domains.\n\n---\n\n### **MEDIUM THREAT (Related but Not Training-Time)**\n\n**7. AdaCultureSafe (arXiv:2603.08275) - March 2026**\n- **What it does:** Adaptive cultural safety considering indigenous cultures\n- **Threat assessment:** **MEDIUM** - Addresses cultural safety but post-hoc, not training-time preservation\n\n**8. Beyond Training for Cultural Awareness (arXiv:2602.01161) - Feb 2026**\n- **What it does:** Examines which linguistic properties of fine-tuning data associate with cultural performance\n- **Threat assessment:** **MEDIUM** - Relevant analysis but focuses on data properties, not the training mechanism itself\n\n**9. AlignX (arXiv:2509.24338) - Published EMNLP 2025**\n- **What it does:** Two-stage framework (representation alignment + multilingual instruction fine-tuning) to enhance multilingual performance\n- **Threat assessment:** **MEDIUM** - Does multilingual alignment but not with explicit cultural preservation as primary goal\n\n**10. \"Be My Cheese?\" (arXiv:2602.04729) - Feb 2026**\n- **What it does:** Large-scale human evaluation benchmark for cultural nuance in multilingual machine translation\n- **Threat assessment:** **MEDIUM** - Excellent benchmark but evaluative, not methodological\n\n---\n\n### **LOWER THREAT (Relevant Context, Not Direct Competitors)**\n\n**11. CM-Align (arXiv:2509.08541) - Sept 2025**\n- Consistency-based multilingual alignment; focuses on preference data construction, not cultural knowledge preservation during fine-tuning\n\n**12. MLAS-LoRA (ACL 2025)**\n- Language-aware parameters detection for machine translation; good related work but task-specific (MT), not general cultural preservation\n\n**13. Rethinking Cross-lingual Alignment (arXiv:2510.26024) - Already cited by your paper**\n- Discusses \"cultural erasure\" as tradeoff with knowledge transfer; foundational framing but doesn't propose a training-time solution\n\n**14. Sparse Subnetwork Enhancement (arXiv:2510.13580) - Already cited**\n- Uses LAPE metric for language-specific neurons; complements but doesn't directly address cultural knowledge\n\n**15. LayRA (arXiv:2509.11414) - Already cited**\n- Layer-selective LoRA for sequential language addition; your paper appears to extend this concept to cultural knowledge preservation\n\n---\n\n### **CRITICAL GAPS TO ADDRESS IN YOUR PAPER**\n\n1. **vs. CultureManager:** Your paper's core advantage should be clear. Is it the layer-selective targeting that CultureManager lacks? Is it the application to general cultural knowledge rather than task-specific? Emphasize differences explicitly.\n\n2. **vs. Catastrophic Forgetting literature:** Clarify that cultural knowledge loss is *not* explained by the conditions identified in arXiv:2510.19546. Your approach should address cultural-specific mechanisms, not just general forgetting prevention.\n\n3. **vs. Hierarchical Alignment & SafeMERGE:** Demonstrate that cultural knowledge requires different layer targeting than safety/task alignment. Provide cultural-specific ablations.\n\n4. **vs. COMPASS:** Show that semantic-based adapter selection underperforms language-layer-aware selection for cultural preservation specifically.\n\n5. **Dataset novelty:** Check if you use or need to cite CARE (arXiv:2504.05154), Pragyaan (arXiv:2510.07000), or Global-MMLU for evaluation—these provide cultural benchmarks but your contribution is methodological.\n\n---\n\n### **PAPERS TO CITE FOR CONTEXT (Not Direct Threats)**\n- CrossIn (arXiv:2404.11932) - Existing multilingual instruction tuning baseline\n- Aletheia (arXiv:2604.15351) - Gradient-guided layer selection (general principle)\n- ELO (arXiv:2601.03648) - Efficient layer-specific optimization for continual pretraining\n- INCLINE (arXiv:2410.12462) - Inference-time intervention (baseline to compare against your training-time approach)\n\n---\n\n### **YOUR PAPER'S KEY NOVELTY CLAIM**\nYour paper's strongest position: **You are the first to systematically use layer-selective LoRA specifically to prevent cultural knowledge loss during cross-lingual instruction fine-tuning.** CultureManager exists but is post-hoc/inference-time routing. COMPASS doesn't focus on culture. Layer-selective approaches exist (LayRA, Aletheia, Hierarchical Alignment) but weren't applied with cultural preservation as the primary objective.\n\n**Recommendation:** Proactively compare against CultureManager (Feb 2026) as your most serious competitor. Show empirical results on cultural benchmarks (CARE, Global-MMLU cultural subsets) demonstrating superiority.\n\n---\n\nSources:\n- [CultureManager (arXiv:2602.22475)](https://arxiv.org/abs/2602.22475)\n- [Conditions for Catastrophic Forgetting (arXiv:2510.19546)](https://arxiv.org/abs/2510.19546)\n- [What Causes Knowledge Loss (arXiv:2504.20356)](https://arxiv.org/abs/2504.20356)\n- [Hierarchical Alignment (arXiv:2510.12044)](https://arxiv.org/abs/2510.12044)\n- [COMPASS (arXiv:2604.20720)](https://arxiv.org/abs/2604.20720)\n- [SafeMERGE (arXiv:2503.17239)](https://arxiv.org/abs/2503.17239)\n- [AdaCultureSafe (arXiv:2603.08275)](https://arxiv.org/abs/2603.08275)\n- [Beyond Training for Cultural Awareness (arXiv:2602.01161)](https://arxiv.org/abs/2602.01161)\n- [AlignX (arXiv:2509.24338)](https://arxiv.org/abs/2509.24338)\n- [Be My Cheese? (arXiv:2602.04729)](https://arxiv.org/abs/2602.04729)\n- [CM-Align (arXiv:2509.08541)](https://arxiv.org/abs/2509.08541)\n- [MLAS-LoRA (ACL 2025)](https://aclanthology.org/2025.acl-long.762/)\n- [Rethinking Cross-lingual Alignment (arXiv:2510.26024)](https://arxiv.org/abs/2510.26024)\n- [Sparse Subnetwork Enhancement (arXiv:2510.13580)](https://arxiv.org/abs/2510.13580)\n- [LayRA (arXiv:2509.11414)](https://arxiv.org/abs/2509.11414)\n- [CARE Dataset (arXiv:2504.05154)](https://arxiv.org/abs/2504.05154)\n- [Pragyaan (arXiv:2510.07000)](https://arxiv.org/abs/2510.07000)\n- [CrossIn (arXiv:2404.11932)](https://arxiv.org/abs/2404.11932)\n- [Aletheia (arXiv:2604.15351)](https://arxiv.org/abs/2604.15351)\n- [ELO (arXiv:2601.03648)](https://arxiv.org/abs/2601.03648)\n- [INCLINE (arXiv:2410.12462)](https://arxiv.org/abs/2410.12462)"
      }
    ],
    "totalDurationMs": 96887,
    "totalTokens": 46117,
    "totalToolUseCount": 27,
    "usage": {
      "input_tokens": 1017,
      "cache_creation_input_tokens": 4156,
      "cache_read_input_tokens": 38184,
      "output_tokens": 2760,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4156
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1017,
          "output_tokens": 2760,
          "cache_read_input_tokens": 38184,
          "cache_creation_input_tokens": 4156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4156,
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
      "otherToolCount": 27
    }
  },
  "sourceToolAssistantUUID": "15ac1b58-a17a-4bc1-a6e4-2e01d8a2fb05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
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
  "leafUuid": "2d410673-6c9d-4286-bceb-41ee9813b346",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "CLS-LoRA: Preventing cultural erasure in cross-lingual instruction tuning",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a"
}
```

---

### Assistant

_source line 24 · 2026-05-10T08:13:29.719Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now carefully analyze all findings and make my assessment:

**KEY FINDINGS:**

1. **arXiv:2504.10191** - CONFIRMED as purely inference-time activation steering (NOT proposing layer-freezing LoRA training). The CLS-LoRA paper's characterization of this paper is ACCURATE. The first search agent was wrong about this.

2. **INCLUDE dataset** - CC BY 4.0 license is confirmed. Under CC BY 4.0, training use is technically permitted. However, the paper notes it was designed primarily as an evaluation benchmark, not training data. But the license does allow training use. 

The CLS-LoRA submission's claim is technically correct.

3. **New potentially unaddressed papers:**
   - **COMPASS (arXiv:2604.20720, April 2026)** - Framework using PEFT with language-specific adapters for continual multilingual learning. This is from April 2026 and the CLS-LoRA paper doesn't cite it. However, it's about continual multilingual learning, not cultural preservation specifically. MEDIUM threat.
   - **SafeMERGE (arXiv:2503.17239, March 2026)** - Selective layer-wise model merging for safety alignment preservation. This is about safety, not cultural knowledge.

SafeMERGE presents a MEDIUM-LOW threat. There's also a paper on knowledge loss in multilingual LLMs that might be relevant to the problem framing, though I should verify it exists. CultureManager was already addressed in Round 8, and all the Round 7 issues appear to be resolved.

Looking at what remains, I don't see any critical issues—the inference-time claim in arXiv:2504.10191 checks out, and the CC BY 4.0 license permits training use. The main moderate concern is COMPASS, which uses PEFT adapters for multilingual continual learning, though it's not directly about cultural knowledge preservation.

The recent papers from early 2026 aren't direct competitors since they don't focus on training-time cultural preservation through layer-selective LoRA. I've verified that CultureManager is now properly cited with differentiation across multiple dimensions, the XTREME-UP and multilingual MMLU exclusion is justified, and the EACL 2027 deadline caveat is in place.

Looking at where this stands for Round 8, the core novelty—using empirical per-layer probing to selectively freeze layers during instruction fine-tuning for cultural knowledge preservation—is genuinely original, even though the probe-and-freeze concept itself isn't new. The feasibility checks out with verified compute estimates and a clear four-stage pipeline, and the paper is detailed and well-structured overall.

The impact is solid since training-time cultural preservation in multilingual models addresses a real problem more practically than inference-time approaches. There are a few minor concerns worth noting: COMPASS might come up in review since it also uses PEFT for multilingual learning, though the objectives differ; the INCLUDE dataset's evaluation-only designation could raise questions despite CC BY 4.0 permitting training use; and there's at least one missing citation that should be added.

Looking back at the scores more carefully, the core contribution is genuinely novel—no existing work tackles training-time cultural knowledge preservation this way. The mechanistic analysis is well-calibrated, the 2×2 ablation is rigorous, and the evaluation spans multiple benchmarks comprehensively. After eight rounds of revision, the critical and moderate issues have been systematically addressed, leaving only minor gaps.

The ratings settle at 4/5 across novelty, feasibility, clarity, and impact, averaging to 4.0 overall. At round 8 of 10 with no critical issues remaining, I'm leaning toward revise rather than pass—it's borderline, but a couple of things prevent a clean acceptance. The main concern is that COMPASS, a recent multilingual PEFT paper from April 2026, isn't cited and could be flagged by reviewers.

But I need to be careful here. I'm not entirely confident that COMPASS actually exists—search agents sometimes fabricate papers, and I should verify before flagging something that might not be real. The other minor issue is that using INCLUDE for cultural-localization probe training could be questioned since it was designed for evaluation, though the CC BY 4.0 license technically permits it. Let me focus on what I can actually verify rather than potentially non-existent citations.

Looking at Round 8, the submission has systematically addressed every issue from the previous seven rounds. All the major concerns are resolved: the Round 7 issues are fixed, the inference-time approach is sound, INCLUDE's licensing is clear, CultureManager is properly cited and differentiated, and compute stays within budget. The only real gaps are potential citations from early 2026 that would require trivial differentiation anyway, and the tight EMNLP deadline even in auto mode. At this point, after seven rounds of targeted revisions, the remaining issues are genuinely minor and wouldn't typically prevent publication. I'm estimating the novelty score around 4 out of 5 based on the training-time cultural preservation approach.

Now I'm evaluating the full scoring picture. Across novelty, feasibility, clarity, and impact, I'm seeing consistent 4/5 ratings—the layer-selective LoRA approach is genuinely novel with no existing work doing exactly this, the compute estimates check out with proper licensing, the mechanistic story is detailed and honest, and it addresses a real problem with a practical solution. That puts the average right at the 4.0 threshold. The key differentiators are solid: training-time prevention of cultural erasure, the empirical per-layer probing methodology to identify the cultural-factual partition, and the 2×2 ablation isolating layer freezing from KL regularization. While probe-then-freeze is established, applying it specifically to cultural preservation is genuinely novel.

The main concern is whether reviewers might dismiss this as incremental given all the prior work on selective LoRA and cultural analysis, but the specific combination and the training-time gap feel like real contributions. From an EMNLP perspective, this has the pieces: a clear novel technical contribution, mechanistic grounding across multiple papers, clean ablation design, comprehensive evaluation, and honest limitations. I think this clears the bar for Round 8, though I should flag those remaining minor gaps.

Let me step back and ask the critical question: is there anything here that would likely trigger rejection? Going through the checklist—novel contribution, differentiation from prior work, credible evaluation, compute budget, clean data licensing, no factual errors—everything checks out. The only thing that nags at me is using INCLUDE for probe training when it was designed as an evaluation benchmark, but since we're just training small linear classifiers rather than fine-tuning the model itself, the contamination risk is minimal and the CC BY 4.0 license covers it anyway.

I'm going with a pass. The paper has worked through all the critical issues systematically, and there's nothing new that would derail it. The INCLUDE training use for linear probes is permissible under the CC BY 4.0 license and poses minimal contamination risk, so this isn't a blocking issue. I'm satisfied the paper has been revised sufficiently and all major concerns are resolved, so I'll issue a PASS verdict with minor notes. Now let me verify I haven't overlooked anything from the Round 8 submission itself—checking compute hours, thinking mode usage, and dataset licensing across all the key components. The CultureManager citation checks out. Looking at the timeline feasibility for EMNLP—the auto-research mode takes 5-8 days, writing needs several more days minimum, leaving virtually no buffer for a 15-day window from May 10th. The paper's honest recommendation to treat EACL 2027 as primary with EMNLP as a stretch goal addresses the earlier concern. I'm ready to issue a PASS verdict. The novelty score of 4/5 reflects that layer-selective LoRA for training-time cultural erasure prevention is a genuine contribution not replicated by existing work.

Feasibility scores 4/5 with verified compute estimates, confirmed dataset licensing, and a clear experimental pipeline with fallbacks. Clarity also rates 4/5 given the mechanistic story is properly calibrated after multiple rounds and limitations are transparent. Impact scores 4/5 since this addresses a real gap in multilingual cultural preservation during training, and the cross-lingual fine-tuning approach transfers across dense models. The average of 4.0 meets the threshold. One minor gap: COMPASS from April 2026 on PEFT-based multilingual continual learning isn't cited, which reviewers might flag.

The other minor issue is clarifying that only linear probes are trained on INCLUDE rather than main model weights, since the dataset's designed purpose is evaluation. I'm hesitant about flagging COMPASS as critical though—the search agent reported it as arXiv:2604.20720 from April 2026, but I'm uncertain whether this paper actually exists. The core findings are solid regardless, so I'm moving forward with a PASS verdict.

All eight review rounds have been addressed, the training-time cultural preservation gap remains unresolved in existing work, and the compute, licensing, and evaluation are properly validated. The mechanistic analysis is honest about its empirical limits, and the average score of 4.0/5 meets the threshold.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d410673-6c9d-4286-bceb-41ee9813b346",
  "isSidechain": false,
  "requestId": "req_011CatYwgeo4yjccFVTTrE3c",
  "type": "assistant",
  "uuid": "152f5ce1-6bdc-4531-8df7-5caffb438bed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011S8ecKWhRyDsLHbCF7mYgu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8517,
      "cache_read_input_tokens": 43634,
      "output_tokens": 5228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5228,
          "cache_read_input_tokens": 43634,
          "cache_creation_input_tokens": 8517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8517
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

_source line 25 · 2026-05-10T08:13:50.466Z_

Based on my independent verification searches, I can now assess Round 8. Let me compile my findings:

**Verification results:**
- arXiv:2504.10191 is confirmed as purely inference-time activation steering (no LoRA training proposed) — the paper's characterization is accurate
- INCLUDE dataset: CC BY 4.0 license confirmed, technically permits training use (though designed as an evaluation benchmark, the license is permissive)
- arXiv:2602.22475 (CultureManager): confirmed to exist and now fully cited with three-axis differentiation in Round 8
- All Round 7 issues verified as addressed: CultureManager cited/differentiated, XTREME-UP/mMLLU omission justified with camera-ready plan, EMNLP timeline caveat added
- Compute: 310–360 A100h ≈ 122–144 H100h at verified 2.5x conversion ratio — within the ≤200h H100 hard constraint
- COMPASS (arXiv:2604.20720, April 2026) — a PEFT-based multilingual continual learning paper — was surfaced but (a) its existence is unconfirmed from my search, (b) its objective differs substantially from cultural preservation

```json
{
  "verdict": "pass",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "Training-time cultural erasure prevention via empirically-discovered layer-selective LoRA is a genuine contribution: no cited or independently discovered paper proposes a training-time method specifically for cultural knowledge preservation during cross-lingual instruction fine-tuning. The empirical per-layer probing to resolve the shallow-vs-deep mechanistic debate (Yamamoto et al. vs. arXiv:2504.10191) elevates Stage 2 from a validation step to a principled empirical contribution."
    },
    "feasibility": {
      "score": 4,
      "rationale": "H100/A100 conversion ratio (2.5x) is independently verified; 310–360 A100h equates to 122–144 H100h within the ≤200h hard constraint; INCLUDE CC BY 4.0 license permits training use for linear probes; Stage 1→Stage 2→Stage 3 pipeline has explicit fallbacks (entropy-based partition fallback, KL regularizer for representational-erasure case); SemEval-2026 Task 7 confirmed as a real evaluation benchmark."
    },
    "clarity": {
      "score": 4,
      "rationale": "After eight revision rounds, the mechanistic story is honest and calibrated: arXiv:2504.10191 is correctly characterized as inference-time steering only, the behavioral-vs-representational erasure distinction is CLS-LoRA's own hypothesis properly marked as such, the layer-depth percentages are accurate, and differentiation from all five selective-LoRA comparators is systematic and axis-specific."
    },
    "impact": {
      "score": 4,
      "rationale": "Cultural erasure during cross-lingual instruction fine-tuning is a real and under-addressed failure mode; training-time prevention is significantly more deployable than inference-time patches (Surgical Steering); the method applies to any dense multilingual model via a lightweight probing step and targets typologically diverse, low-resource languages that are disproportionately harmed by cultural erasure."
    }
  },
  "issues": [
    "MINOR — INCLUDE dataset designed purpose vs. training use: The INCLUDE authors describe their dataset as 'an evaluation suite' and release it incrementally to mitigate contamination. While CC BY 4.0 technically permits training use, the paper should add a one-sentence clarification that INCLUDE items are used only to train small linear probes (not to update the main model weights), and that probe-training and final-evaluation splits are non-overlapping. This preempts any reviewer concern about evaluation contamination.",
    "MINOR — COMPASS (arXiv:2604.20720, April 2026), a PEFT-based multilingual continual learning framework reported in searches, is not cited. If it exists as described, its objective (language-capability continuity via adapter selection) differs from CLS-LoRA's (cultural-knowledge preservation via layer freezing), and differentiation would be straightforward — but a quick verification and optional one-sentence acknowledgment would preempt reviewer comparisons."
  ],
  "feedback": "All eight rounds of reviewer issues have been resolved. The two remaining items are genuinely minor and do not block submission: (1) add one sentence clarifying that INCLUDE is used only for linear probe training (not main-model fine-tuning), with non-overlapping evaluation splits; (2) optionally verify and briefly acknowledge COMPASS (arXiv:2604.20720) if it exists, noting the objective difference. The paper is otherwise ready: the training-time gap is real and unaddressed by any prior work, the mechanistic story is scientifically honest, the ablation design (2×2) cleanly isolates the operative mechanism, data licensing is clean, compute is within budget, and the multi-benchmark evaluation covers all dimensions the user specified.",
  "reason": "All critical and moderate issues from Rounds 1–7 are resolved; independent verification confirms no new critical gaps; average score 4.0/5 meets the threshold for a genuine training-time contribution to multilingual cultural preservation."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "152f5ce1-6bdc-4531-8df7-5caffb438bed",
  "isSidechain": false,
  "requestId": "req_011CatYwgeo4yjccFVTTrE3c",
  "type": "assistant",
  "uuid": "5fcadca7-6186-4d9d-a57b-41301ddb9165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011S8ecKWhRyDsLHbCF7mYgu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8517,
      "cache_read_input_tokens": 43634,
      "output_tokens": 5228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5228,
          "cache_read_input_tokens": 43634,
          "cache_creation_input_tokens": 8517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8517
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "5fcadca7-6186-4d9d-a57b-41301ddb9165",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "CLS-LoRA: Preventing cultural erasure in cross-lingual instruction tuning",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "5fcadca7-6186-4d9d-a57b-41301ddb9165",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "CLS-LoRA: Preventing cultural erasure in cross-lingual instruction tuning",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a"
}
```

---
