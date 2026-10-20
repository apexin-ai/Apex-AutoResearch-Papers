# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/a9dbecfc-cc1f-4e48-9f6b-0d066b966530.jsonl`
- **Structured JSON:** [`4c38266b771e9634cce3.json`](../../sessions/4c/4c38266b771e9634cce3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:44:17.350Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:44:17.350Z",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Multilingualism and Cross-Lingual NLP.\n\nDirection: Cross-lingual transfer and multilingual NLP methods. In-scope: cross-lingual transfer without parallel data, multilingual instruction tuning strategies, language-agnostic representations, low-resource language adaptation, cross-lingual retrieval, multilingual reasoning, code-switching handling. ACL 2025 outstanding papers highlighted multilingual gaps and cross-lingual intervention methods.\n\nContribution type: METHOD ONLY. New training recipes, transfer algorithms, or adaptation techniques. Not a new multilingual dataset or language-specific analysis.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Multilingual experiments need coverage across languages — budget for LoRA fine-tuning on multilingual models, not full pretraining.\n2. Time: ≤16 days. Use existing multilingual models (BLOOM, mT5, XLM-R, Aya, Qwen multilingual, Llama-3 multilingual).\n3. Eval: XTREME-UP, XCOPA, XStoryCloze, MGSM, multilingual MMLU, TyDi QA, FLORES for MT.\n\nLook for: efficient cross-lingual transfer with minimal target-language data, multilingual reasoning without English-centric bias, representation alignment methods, adaptation techniques for typologically diverse languages. Avoid: English-only experiments, monolingual fine-tuning.\n\nTag: direction=multilingual, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 6/10)\n{\n  \"title\": \"Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignment\",\n  \"project_name\": \"cls_lora_cultural_preservation\",\n  \"source\": \"web_research\",\n  \"level\": \"solid\",\n  \"core_problem\": \"Cross-lingual fine-tuning systematically suppresses culturally-grounded, language-specific knowledge while improving factual transfer—a phenomenon called 'cultural erasure.' Mechanistic work (arXiv:2504.10191) demonstrates that in pre-trained instruction-tuned models, cultural knowledge is spatially localized in specific layers and steerable via linear activation vectors, suggesting particular layer indices implement cultural routing pathways. Whether this spatial localization persists after LoRA instruction fine-tuning—and whether cross-lingual fine-tuning causes behavioral erasure (routing pathway disruption), representational erasure (information loss), or both—remains empirically untested. No training-time method prevents either failure mode, forcing practitioners to choose between cross-lingual capability and cultural authenticity. A complementary mechanistic uncertainty reinforces the need for per-model empirical investigation: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deeper-layer localization (layers 19–30, approximately 45–71% depth in Gemma2-9b-it) identified via activation-steering analysis in arXiv:2504.10191. The two methodologies measure different constructs—discrete high-influence neurons versus distributed activation-space subspaces—and their disagreement means the culturally-critical layer partition cannot be reliably imported from prior work for an arbitrary target model; it must be discovered empirically.\",\n  \"opportunity\": \"'Rethinking Cross-lingual Alignment' (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026) rigorously demonstrates that every tested cross-lingual alignment approach degrades cultural localization across all six languages, and proposes Surgical Steering as a remedy—but only at inference time, requiring per-query layer manipulation and offering no prevention during training. The finding that factual transfer and cultural localization are optimally steerable at different model layers is actionable: applying LoRA selectively to factual-transfer layers while freezing cultural-knowledge layers during instruction fine-tuning would prevent erasure at the source. arXiv:2504.10191 establishes that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors in specific layers (notably layers 19–30 in Gemma2-9b-it, with peaks at layers 23 and 30), supporting the hypothesis that particular layer indices implement cultural routing pathways. CLS-LoRA's freezing strategy is designed to exploit this structure: if that spatial localization persists after LoRA fine-tuning (behavioral erasure—routing disrupted but representations intact), freezing those layers during training prevents routing disruption; if fine-tuning also degrades the representations themselves (representational erasure), the KL-divergence penalty anchors cultural-layer activations to their pretrained distribution. Stage 1 empirically distinguishes these two failure modes before the main sweep begins. Crucially, the layer partition question is now a live empirical debate in the literature: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) independently find culture-relevant neurons in shallow-to-middle MLP layers using gradient attribution, while activation-steering work (arXiv:2504.10191, arXiv:2510.26024) localizes cultural steerability in deeper layers. This genuine methodological disagreement elevates Stage 2 probing from a validation step to the principled empirical resolution of an open question—CLS-LoRA discovers the culturally-critical partition for each target model rather than assuming it from any single prior study. This is feasible with any open-source dense multilingual model via a lightweight per-layer probing step.\",\n  \"landscape\": \"INCLINE (arXiv:2410.12462, ACL 2025 outstanding paper) aligns internal representations from low-resource to high-resource languages via learned projection matrices derived from parallel sentences, improving cross-lingual task performance but not distinguishing factual from cultural knowledge. Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025, Liu & Niehues) provides the empirical foundation for CLS-LoRA's factual-transfer layer partition: through translation retrieval probing across 1,190 language pairs on Llama 3 and Qwen 2.5, it establishes that layer 16 (50% depth in a 32-layer model) is the key integration point for cross-lingual semantic alignment, and that incorporating a middle-layer alignment objective consistently improves cross-lingual task performance particularly for lower-resource languages. CLS-LoRA extends this by additionally protecting cultural-knowledge layers from LoRA updates—arXiv:2504.10191 identifies layers 19–30 (approximately 45–71% depth in Gemma2-9b-it's 42-layer architecture, with peak cultural activation at layers 23 and 30) as critical for cultural routing, and Stage 2 probing empirically determines the analogous partition for each target model—a protection axis entirely absent from Liu & Niehues, whose work does not distinguish factual from cultural knowledge and proposes no cultural preservation objective. Cross-Lingual Transfer of Cultural Knowledge (arXiv:2506.01675, ACL 2025 short paper, Zhang et al.) provides empirical background showing cultural knowledge transfer is asymmetric: high-resource language pairs exhibit bidirectional transfer while low-resource languages primarily export cultural knowledge to English without reciprocal benefit, driven by a frequency-based pretraining data mechanism. This asymmetry directly motivates training-time prevention of cultural erasure—low-resource languages are disproportionately at risk and most in need of the protection CLS-LoRA provides. AlignX (arXiv:2509.24338, EMNLP 2025) and CM-Align (arXiv:2509.08541) apply two-stage and consistency-based multilingual alignment respectively, both optimizing convergence without a cultural preservation objective. Language Surgery/ITLC (arXiv:2506.12450) disentangles language-specific from agnostic information through latent injection at inference time, but does not train models to preserve this distinction. Alignment through steering (arXiv:2505.12584) adds a learned residual-stream vector at a single layer; it outperforms many baselines but still does not model the factual-cultural layer split. Surgical Steering (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 the first author's publication page lists this as an arXiv preprint without a confirmed proceedings venue) is the only method addressing the cultural erasure problem, and is strictly an inference-time patch over an already-erased model. arXiv:2504.10191 ('Localized Cultural Knowledge is Conserved and Controllable in LLMs', April 2025) demonstrates that in pre-trained instruction-tuned models, cultural knowledge exists as spatially localized steerable activation-space vectors—mechanistic analysis on Gemma2-9b-it (42 layers) identifies layers 19–30 as critical for cultural activation, with peak effects at layers 23 and 30 (approximately 55–71% depth)—and can be controlled via linear steering at inference time. This establishes spatial localization of cultural knowledge in pre-trained models, motivating CLS-LoRA's hypothesis that specific layer indices implement cultural routing pathways; whether this localization persists after LoRA instruction fine-tuning is precisely what Stage 1 tests.\\n\\nYamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) conduct a neuron-level analysis of cultural understanding using a gradient-based scoring method with additional filtering for precise refinement. They identify both culture-general neurons (supporting cultural understanding across cultures) and culture-specific neurons (tied to individual cultures), which together comprise less than 1% of all neurons and are concentrated in shallow-to-middle MLP layers—not in the deeper layers identified by activation-steering analysis in arXiv:2504.10191. Suppressing these neurons degrades cultural benchmark performance by up to 30% while leaving general NLU tasks largely unaffected. This finding is in apparent tension with the deeper-layer localization from arXiv:2504.10191 and arXiv:2510.26024, reflecting a genuine methodological distinction: gradient attribution identifies discrete neurons with the highest individual causal influence, which may be sparse and concentrated in earlier layers; activation-steering subspaces reflect distributed representational geometry that implements cultural routing across many layers and may peak in depth-profile at different points. CLS-LoRA's Stage 2 probing directly bridges this debate: rather than assuming either result, it measures per-layer probe accuracy on each target model and discovers the cultural-knowledge partition empirically. If shallow neurons (Yamamoto et al.) dominate, Stage 2 will assign those layers to the frozen cultural partition; if deeper subspaces (arXiv:2504.10191) dominate, Stage 2 will assign those layers instead. Stage 2 is thus a model-specific resolution mechanism that makes CLS-LoRA robust to methodological disagreements in the mechanistic literature.\\n\\nTwo directly related selective-LoRA methods require explicit differentiation. MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762) detects language-aware neurons in a teacher model and injects extracted knowledge into language-pair-specific LoRA modules in a student model for multilingual machine translation, achieving +1.7 BLEU on average. While MLAS-LoRA and CLS-LoRA both employ a probe-then-selective-LoRA pipeline, they differ on three critical axes: (1) task domain—MLAS-LoRA targets MT translation quality whereas CLS-LoRA targets cultural knowledge preservation during instruction fine-tuning; (2) partition dimension—MLAS-LoRA partitions along language-pair specificity (language-A vs language-B neurons) whereas CLS-LoRA partitions along the factual-transfer vs cultural-localization semantic axis, which cuts across language pairs; and (3) objective—MLAS-LoRA optimizes translation accuracy via teacher-student knowledge distillation whereas CLS-LoRA optimizes a cultural-preservation signal with no distillation component. The cultural-preservation objective is the categorical novelty: no prior selective-LoRA work defines a 'keep culturally-grounded outputs intact' training signal. LayRA (arXiv:2509.11414, September 2025) proposes layer-selective LoRA for continual multilingual language addition, applying LoRA to initial and final transformer layers (the first 10 and last 2 layers, plus embeddings and LM head) while freezing intermediate layers. The partition rationale—that multilingual models encode source-language inputs in initial layers, reason in English in middle layers, and decode into the target language in final layers—leads to a source-language-encoding vs English-reasoning vs target-language-decoding functional partition axis. CLS-LoRA differs on three dimensions: (1) objective—LayRA enables new-language addition without catastrophic forgetting of existing languages, whereas CLS-LoRA preserves cultural knowledge during cross-lingual instruction fine-tuning; (2) partition axis—LayRA's functional encoding/reasoning/decoding axis is defined over language identity and cuts uniformly across all languages, whereas CLS-LoRA's factual-transfer vs cultural-localization semantic axis cuts across language-pair specificity; (3) partition method—LayRA hard-codes specific layer indices derived from qualitative linguistic reasoning, whereas CLS-LoRA uses empirical per-layer probing to discover the partition for each target model, enabling adaptation to the contested mechanistic landscape. The cultural-preservation objective remains the categorical novelty absent from LayRA. Source-Shielded Updates (arXiv:2512.04844, Nov 2025) proposes column-wise parameter freezing to prevent catastrophic forgetting of source-language task performance during target-language adaptation—addressing cross-lingual interference but not the factual-vs-cultural layer distinction or cultural knowledge preservation as a first-class objective.\",\n  \"approach\": \"We propose Cultural-Layer-Selective LoRA (CLS-LoRA), a training-time method that prevents cultural erasure without sacrificing factual cross-lingual transfer. The pipeline has four stages.\\n\\nMechanistic bridge. Our layer-freezing strategy rests on a hypothesis connecting inference-time observations to training-time interventions: the layer indices most sensitive to cultural-vs-factual activation steering at inference time (arXiv:2510.26024, corroborated by cultural customization vectors in arXiv:2504.10191 concentrated at layers 19–30 in Gemma2-9b-it) identify the weight matrices that implement cultural routing. LoRA updates modify precisely these weight matrices; applying LoRA to cultural-knowledge layers may therefore disrupt the routing pathways through which culturally-grounded representations reach outputs. This hypothesis involves a genuine empirical uncertainty that the literature has not resolved: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deep-layer activation-steering localization from arXiv:2504.10191. The discrepancy most likely reflects the difference between measuring discrete high-influence neurons (gradient attribution captures sparse, individually causal units that may be early in the network) versus measuring distributed activation subspaces (steering analysis captures the geometry of representational routing, which may span many layers and peak later). Neither result invalidates the other; they measure different aspects of how cultural knowledge is implemented. Stage 2 probing is designed precisely for this uncertainty: by measuring per-layer probe accuracy directly on each target model's representations, it discovers the culturally-critical partition without assuming either methodological lens is correct—if shallow neurons dominate functionally, Stage 2 identifies shallow layers as the cultural partition; if deeper subspaces dominate, Stage 2 identifies those instead. Whether the representations themselves persist as recoverable vectors after full LoRA fine-tuning (behavioral erasure) or are also degraded (representational erasure) is a separate open empirical question—Stage 1 provides this answer. Freezing the empirically-identified cultural-knowledge layers during training preserves both the routing weights and the residual-stream geometry that steerability depends on, addressing both failure modes by design.\\n\\nStage 1 — Structural diagnostic: Before the main sweep, we run full-LoRA instruction fine-tuning on a held-out model checkpoint and measure per-layer cultural probe accuracy before and after. Stage 1 trains separate linear probes on each checkpoint's frozen representations—one probe trained and evaluated on the pretrained-checkpoint's layer activations, one probe trained and evaluated on the post-LoRA-checkpoint's layer activations—using the same held-out cultural question split for both. This ensures accuracy differences reflect genuine representational change rather than activation-space reorganization: applying a single probe trained on pretrained representations cross-checkpoint to post-LoRA representations would fail if LoRA remaps the activation geometry without destroying cultural information (behavioral erasure), conflating reorganization with information loss; separate per-checkpoint probes make the comparison clean and the behavioral-vs-representational distinction interpretable. If probe accuracy is maintained post-training, erasure is confirmed as behavioral (pathway disruption) and layer freezing is the correct intervention; if probe accuracy drops, erasure is partly representational and the KL-divergence regularizer in Stage 3 becomes critical. This diagnostic sharpens the mechanistic story and validates the layer-freezing strategy regardless of which failure mode dominates. An automated entropy-based partition fallback replaces human inspection when probe curves are bimodal or noisy, reducing the agent failure mode from prior review.\\n\\nStage 2 — Layer profiling: Lightweight linear probes (one per transformer layer) are trained on a small parallel corpus to produce per-layer factual-transfer and cultural-localization accuracy scores, yielding a principled layer partition. For factual transfer, the empirical expectation from arXiv:2502.14830 (Liu & Niehues) is approximately middle layers (~50% model depth). For cultural knowledge, arXiv:2504.10191 identifies layers 19–30 as critical in Gemma2-9b-it (approximately 45–71% depth in a 42-layer model, with peak effects at layers 23 and 30); Yamamoto et al. (arXiv:2510.08284, ICLR 2026) find culture-relevant neurons in shallow-to-middle MLP layers via gradient attribution. Stage 2 probing empirically determines the partition boundaries for each target model—Qwen3-8B (36 layers) and Aya-23-8B—rather than hard-coding percentages from either prior study; this is the methodologically sound response to the contested mechanistic landscape. For cultural-localization probes, we use held-out splits of CulturalBench (ACL 2025; 1,696 human-verified questions across 45 global regions), which is publicly available for training use. For factual-transfer probes, we use held-out splits of TyDiQA and XQUAD. SemEval-2026 Task 7 data (BLEnD) is reserved strictly for final evaluation and is not used in probe training, consistent with the task's evaluation-only rules (confirmed via the official task repository). No new annotation is required.\\n\\nStage 3 — Selective LoRA training: LoRA adapters (via Hugging Face PEFT target_modules) are inserted exclusively into factual-transfer layers and trained with standard instruction fine-tuning loss on multilingual instruction data, while cultural-knowledge layers remain fully frozen. An optional auxiliary KL-divergence penalty on a held-out cultural probe set discourages residual drift in frozen layers' downstream activations. To establish that layer freezing is the operative mechanism rather than KL regularization alone, Stage 3 includes a 2×2 ablation: (a) full LoRA without KL penalty (existing baseline); (b) full LoRA with KL-divergence penalty on cultural-layer activations (regularization-only baseline, new); (c) CLS-LoRA with layer freezing and no KL penalty (freezing-only; already present in the sweep as the no-regularization variant); (d) CLS-LoRA with layer freezing and KL penalty (proposed method). Condition (b) is the critical addition: it tests whether KL regularization alone, without the complexity of a learned layer partition, achieves equivalent cultural preservation. If (b) matches (d), the partitioning step is unnecessary overhead; if (c) and (d) both outperform (b), layer freezing is confirmed as the operative mechanism. Approximately 4–6 additional training runs (condition (b) only; 2 models × 2–3 seeds) are added to the auto sweep; conditions (a), (c), and (d) are already covered by existing runs.\\n\\nStage 4 — Evaluation: Experiments run on Qwen3-8B (primary: confirmed dense, 36 transformer layers, 119 languages and dialects, 8.2B parameters) and Aya-23-8B (secondary: confirmed dense decoder-only, 23 languages, 8B parameters) for cross-architecture generalization. All Qwen3-8B experiments are conducted in non-thinking mode (enable_thinking=False in the chat template), ensuring consistent direct-generation behavior during both LoRA fine-tuning and cultural localization probing without interference from chain-of-thought reasoning pathways. LLaMA 4 Scout is excluded—its 48-block, 16-expert MoE architecture makes the factual-vs-cultural layer partition from arXiv:2510.26024, established on dense models, methodologically inapplicable without separate MoE-specific validation. Evaluation uses CulturalBench and SemEval-2026 Task 7 as primary cultural metrics. To verify that CLS-LoRA does not regress on capabilities orthogonal to cultural localization and factual QA, Stage 4 adds three supplementary evaluation tracks via lm-evaluation-harness: cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; lm-eval task group xcopa_[lang]); cross-lingual narrative understanding (XStoryCloze, 11 languages, zero-shot; lm-eval task group xstorycloze); and multilingual arithmetic chain-of-thought (MGSM, 11 languages, direct mode; lm-eval task mgsm_direct). Each benchmark requires approximately 2–4 GPU-hours per model; together they add ~18–24h A100 total across both target models and all evaluated checkpoints. XCOPA is the most mechanistically relevant: if Stage 2's cultural-knowledge layer partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain commonsense transfer—an outcome that would be reported transparently and interpreted as a scope constraint on the method (cultural preservation trades off against commonsense transfer in those layers) rather than treated as an uncontrolled failure. MGSM verifies that the factual-transfer LoRA updates preserve multilingual arithmetic reasoning. All three benchmarks use standard zero-shot or direct evaluation protocols already in lm-evaluation-harness and require no additional training data. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; we therefore employ the explicitly defined fallback evaluation—a 2D scatter of cross-lingual factual accuracy (XQUAD/TyDiQA) vs cultural localization accuracy (CulturalBench) across languages, normalized to the pre-fine-tuning baseline, yielding the same transfer-localization interpretive framework. We compare against full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA (adapted to the instruction-FT setting), and Source-Shielded Updates baselines to demonstrate that CLS-LoRA Pareto-dominates prior methods in the transfer-localization trade-off space.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~230h A100 80GB (~92h H100 equivalent)\",\n      \"gpu_utilization\": \"~30–40% effective; GPU idles while the researcher inspects probe accuracy heatmaps to select layer partition boundaries, designs ablation grids, and iterates on training scripts between runs\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$345–475 (A100 at $1.49–2.06/hr via RunPod/Lambda); additional ~30h reflects new ablation runs (condition (b), ~12h) and XCOPA/XStoryCloze/MGSM evaluation (~18h)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~155h A100 80GB (~62h H100 equivalent)\",\n      \"gpu_utilization\": \"~60–70% effective; agent queues probing and LoRA sweep experiments overnight, researcher reviews layer partition heatmaps and approves next ablation tier once daily, cutting idle time ~50% vs. manual\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in\",\n      \"claude_api_cost\": \"$150–250 (~1000–1500 conversation turns at $0.10–0.15/turn with Opus)\",\n      \"estimated_gpu_cost\": \"~$231–319 (A100 at $1.49–2.06/hr); additional ~25h reflects new ablation condition (b) runs and supplementary benchmark evaluations\",\n      \"risk_note\": \"Key risk: agent may commit to a suboptimal layer partition if probe accuracy curves are bimodal or noisy; the automated entropy-based partition fallback reduces (but does not eliminate) this risk; daily human review of the partition heatmap before LoRA runs remains the essential gate\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~310–360h A100 80GB (~122–144h H100 equivalent); within the ≤200h H100 hard constraint\",\n      \"gpu_utilization\": \"~85–90% effective; agent continuously queues the next experiment upon completion with no human approval bottleneck—idle only during brief checkpoint evaluation transitions\",\n      \"sweep\": \"3 LoRA rank values (8, 16, 32) × 2 layer partition thresholds × 2 model families (Qwen3-8B, Aya-23-8B) × 2 regularization strengths × 2 seeds = 48 core training runs; plus ~12 baseline runs (full-LoRA, Surgical Steering, INCLINE, Source-Shielded Updates); plus ~4–6 new ablation runs for condition (b) (full LoRA + KL only, 2 models × 2–3 seeds); plus Stage 1 structural diagnostic runs; plus ~18–24h for XCOPA/XStoryCloze/MGSM evaluation across all checkpoints via lm-evaluation-harness\",\n      \"timeline\": \"5–8 days with 4–6 concurrent A100 GPUs (or 3–5 days with H100s)\",\n      \"team\": \"0 (2–3h of initial harness setup and config-space definition)\",\n      \"claude_api_cost\": \"$200–350 (~1500–2500 turns across experiment planning, result parsing, and ablation branching)\",\n      \"estimated_gpu_cost\": \"~$462–742 (A100 at $1.49–2.06/hr); increase from prior estimate reflects ~4–6 new condition (b) training runs and ~18–24h benchmark evaluation\",\n      \"speed_bottleneck\": \"Number of concurrent GPUs and the ~1h cultural benchmark evaluation per checkpoint; XCOPA/XStoryCloze/MGSM evaluation can be parallelized across checkpoints on separate GPUs via lm-evaluation-harness\",\n      \"risk_note\": \"Bimodal probe distributions are handled by an automated entropy-based partition fallback. The Stage 1 structural diagnostic provides an early signal: if cultural probe accuracy is unaffected by full-LoRA training, the layer-freezing strategy is validated before the main sweep begins, allowing early termination of degenerate configurations. If XCOPA performance drops relative to full-LoRA baseline, this is flagged as a scope constraint and reported transparently rather than silently absorbed.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — viable only with auto-research mode given the 15-day window from May 10, 2026\",\n    \"EACL 2027 (ARR submission deadline August 3, 2026) — primary target for human-in-loop or manual mode\",\n    \"AAAI 2027 (submission deadline expected July–August 2026, TBC)\"\n  ],\n  \"key_references\": [\n    \"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 listed as arXiv preprint on the first author's publication page)\",\n    \"Neuron-Level Analysis of Cultural Understanding in Large Language Models (arXiv:2510.08284, Yamamoto et al., ICLR 2026)\",\n    \"Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention / INCLINE (ACL 2025 Outstanding Paper, arXiv:2410.12462)\",\n    \"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs (ACL 2025, arXiv:2502.14830, Liu & Niehues)\",\n    \"Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (ACL 2025 short paper, arXiv:2506.01675)\",\n    \"MLAS-LoRA: Language-Aware Parameters Detection and LoRA-Based Knowledge Transfer for Multilingual Machine Translation (ACL 2025, aclanthology.org/2025.acl-long.762)\",\n    \"Continually Adding New Languages to Multilingual Language Models / LayRA (arXiv:2509.11414, September 2025)\",\n    \"Mitigating Catastrophic Forgetting in Target Language Adaptation of LLMs via Source-Shielded Updates (arXiv:2512.04844, Nov 2025)\",\n    \"AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment (EMNLP 2025, arXiv:2509.24338)\",\n    \"CM-Align: Consistency-based Multilingual Alignment for Large Language Models (arXiv:2509.08541, 2025)\",\n    \"Language Surgery in Multilingual Large Language Models / ITLC (arXiv:2506.12450, 2025)\",\n    \"Improving Multilingual Language Models by Aligning Representations through Steering (arXiv:2505.12584, 2025)\",\n    \"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models (arXiv:2504.10191, 2025)\",\n    \"LoRA: Low-Rank Adaptation of Large Language Models (ICLR 2022, arXiv:2106.09685)\",\n    \"XCOPA: Evaluation of Causal Commonsense Reasoning in Multiple Languages (EMNLP 2020, arXiv:2005.00333, Ponti et al.)\",\n    \"Few-shot Learning with Multilingual Language Models / XStoryCloze (arXiv:2112.10668, Lin et al., 2022)\",\n    \"Language Models are Multilingual Chain-of-Thought Reasoners / MGSM (arXiv:2210.03057, Shi et al., 2022)\"\n  ],\n  \"description\": \"Cross-lingual instruction fine-tuning demonstrably erases culturally-localized knowledge across all tested alignment approaches—yet no training-time prevention exists. Mechanistic work (arXiv:2504.10191) shows that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors (in Gemma2-9b-it's 42-layer architecture, layers 19–30, with peak effects at layers 23 and 30 corresponding to approximately 55–71% model depth), suggesting specific layer indices implement cultural routing pathways. A parallel ICLR 2026 result (Yamamoto et al., arXiv:2510.08284) reaches an apparently different conclusion using gradient-based neuron attribution: culture-relevant neurons are concentrated in shallow-to-middle MLP layers. This methodological discrepancy—discrete high-influence neurons (gradient attribution) versus distributed representational subspaces (activation steering)—reflects different aspects of cultural knowledge implementation and constitutes a live empirical debate in the literature. Whether cultural localization persists after LoRA instruction fine-tuning—and whether erasure is behavioral (routing disruption) or representational (information loss)—is the empirical question Stage 1 answers. We propose Cultural-Layer-Selective LoRA (CLS-LoRA), which prevents both failure modes through a four-stage pipeline.\\n\\nA mechanistic bridge paragraph (placed before Stage 1) formalizes the training-time implication and acknowledges the mechanistic debate: the layer indices most sensitive to cultural activation steering at inference time identify weight matrices that implement cultural routing; LoRA updates to those weights may disrupt routing pathways; freezing those layers preserves both routing weights and residual-stream geometry. The contested layer localization (deep-layer subspaces per arXiv:2504.10191/arXiv:2510.26024 versus shallow-to-middle neurons per Yamamoto et al. ICLR 2026) is resolved not by choosing a side but by Stage 2 probing: measuring per-layer probe accuracy directly on each target model discovers the culturally-critical partition empirically, making CLS-LoRA robust to methodological disagreements in the mechanistic literature. Stage 1 distinguishes behavioral from representational erasure and determines whether KL regularization is necessary; crucially, Stage 1 trains separate linear probes on each checkpoint's frozen representations—one on the pretrained-checkpoint activations and one on the post-LoRA-checkpoint activations, both evaluated on the same held-out cultural split—so that accuracy differences reflect genuine representational change rather than activation-space reorganization.\\n\\nStage 2 runs lightweight linear probes to partition layers: factual-transfer probes trained on TyDiQA/XQUAD held-out splits; cultural-localization probes trained on held-out splits of CulturalBench (ACL 2025, publicly available for training use); SemEval-2026 Task 7 data (BLEnD) reserved strictly for final evaluation per its evaluation-only rules. Stage 2 determines the actual partition boundaries for each target model rather than hard-coding architecture-specific percentages from any single prior study—the principled response to the contested mechanistic landscape. Stage 3 applies LoRA exclusively to factual-transfer layers with an optional KL-divergence penalty; a 2×2 ablation isolates each component's contribution: (a) full LoRA no KL (baseline), (b) full LoRA + KL only (regularization-only, new), (c) CLS-LoRA frozen no KL (freezing-only), (d) CLS-LoRA frozen + KL (proposed method). Condition (b) is the critical new ablation: if it matches (d), layer partitioning is unnecessary overhead; if (c) and (d) outperform (b), layer freezing is confirmed as the operative mechanism. Stage 4 experiments run on Qwen3-8B (non-thinking mode, enable_thinking=False) and Aya-23-8B; primary evaluation uses CulturalBench and SemEval-2026 Task 7. Supplementary capability-regression evaluation via lm-evaluation-harness covers cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; task: xcopa_[lang]), narrative understanding (XStoryCloze, 11 languages, zero-shot; task: xstorycloze), and multilingual arithmetic (MGSM, 11 languages, direct mode; task: mgsm_direct); each requires ~2–4h per model and together add ~18–24h A100. If Stage 2's cultural-knowledge partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain XCOPA transfer—a mechanistically informative finding reported transparently. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; the fallback evaluation framework (2D scatter of factual vs. cultural accuracy across languages, normalized to pretrained baseline) is specified explicitly and yields the same interpretive structure.\\n\\nCLS-LoRA is differentiated from MLAS-LoRA (ACL 2025) across three axes: task domain (MT quality vs cultural preservation), partition dimension (language-pair specificity vs factual-cultural semantic axis), and objective (translation accuracy via distillation vs cultural preservation with no distillation). CLS-LoRA is differentiated from LayRA (arXiv:2509.11414) across three axes: objective (language addition vs cultural knowledge preservation during instruction fine-tuning), partition axis (LayRA's source-encoding/English-reasoning/target-decoding functional axis vs CLS-LoRA's factual-transfer/cultural-localization semantic axis), and partition method (LayRA hard-codes layer indices from qualitative reasoning vs CLS-LoRA uses per-model empirical probing). The cultural-preservation objective remains the categorical novelty absent from both. The auto-research sweep covers ~64–71 training runs (~122–144h H100), within the ≤200h H100 constraint, targeting a Pareto improvement over full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA, and Source-Shielded Updates in the transfer-localization trade-off space, with XCOPA/XStoryCloze/MGSM as orthogonal capability regression checks.\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"INCLINE (arXiv:2410.12462) is described as an 'ACL 2025 outstanding paper' — no evidence of this award was found in any ACL 2025 outstanding-paper announcement. This factual error will damage reviewer credibility; the claim should be removed or corrected.\", \"Critical missing related work: MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762) introduces language-aware neuron detection followed by a multiple language-specific LoRA architecture — conceptually the same probe-then-selective-LoRA pipeline as CLS-LoRA, applied to multilingual MT. This overlap must be cited and the differentiation made explicit or reviewers will flag it as unacknowledged prior art.\", \"Critical missing related work: Source-Shielded Updates (arXiv:2512.04844, Nov 2025) proposes column-wise parameter freezing to shield source-language knowledge during target-language adaptation — directly related to the 'freeze knowledge layers' component of CLS-LoRA. Must be cited.\", \"Auto-research mode estimates 600h A100 (≈ 300–400h H100 equivalent), which violates the user's hard ≤200 H100-hour compute constraint. The sweep (4 ranks × 3 partition thresholds × 2 model families × 5 regularization strengths × 3 seeds = 360 runs) must be trimmed or the auto mode dropped.\", \"LLaMA 4 Scout is a 48-block, 16-expert MoE model (109B total parameters). The factual-vs-cultural layer partition established in arXiv:2510.26024 was discovered on dense models; MoE expert routing changes the functional semantics of 'layer,' making the partition methodology directly inapplicable without separate validation. Either replace LLaMA 4 Scout with a dense multilingual model (e.g., Aya-23-8B, BLOOM-7B, mT5-XXL) or explicitly add a MoE-adaptation step to the probe procedure.\", \"The transfer-localization plane evaluation framework from arXiv:2510.26024 is the primary metric, but that paper is under review (OpenReview) and its evaluation code may not be publicly released. If the implementation is not available, re-implementing the framework is a hidden engineering cost that could consume days of the 16-day timeline.\", \"The paper reports cultural knowledge 'surviving' in deeper layers even after fine-tuning (arXiv:2504.10191), which complicates the erasure narrative: if knowledge is structurally preserved but behaviorally suppressed, freezing deeper layers may not be the right intervention — the issue may be in the output layers, not in middle-vs-deep storage. This mechanistic ambiguity should be addressed.\"]\nFeedback: The core idea is viable and the training-time gap is real, but the paper needs three structural fixes before it can pass review:\n\n1. **Cite and differentiate MLAS-LoRA.** This is the most urgent issue. The Generator should search ACL 2025 Anthology for 'MLAS-LoRA' and add a paragraph in Related Work explaining why CLS-LoRA's factual-vs-cultural layer distinction makes it categorically different from MLAS-LoRA's language-pair-specific neuron selection. The key differentiator is the *cultural-preservation objective*, not the selective-LoRA mechanism itself. Also add Source-Shielded Updates (arXiv:2512.04844).\n\n2. **Drop LLaMA 4 Scout; replace with a dense multilingual model.** The MoE architecture invalidates the layer-partition premise from 2510.26024 and makes compute estimates unreliable. Use Qwen3-8B (confirmed dense, 119 languages) as the primary model and add mT5-XXL or Aya-23-8B as the second model family for cross-architecture generalization. This also brings auto-research mode within the 200h H100 budget if you trim the sweep to ≤3 ablation dimensions.\n\n3. **Address the structural-vs-behavioral erasure ambiguity.** The paper should explicitly test whether the cultural knowledge 'erasure' is representational (information is gone from activations) or behavioral (information exists but the model won't surface it). If arXiv:2504.10191 is correct that cultural knowledge persists structurally, CLS-LoRA's value is in behavioral preservation during fine-tuning — which needs to be measured differently than simple layer probing. A single ablation running full-LoRA training then measuring layer-wise cultural probe accuracy (before vs. after) would resolve this and strengthen the paper's mechanistic story.\n\nSecondary fixes: Remove the 'outstanding paper' label from INCLINE, verify the transfer-localization plane code availability from arXiv:2510.26024 authors before committing to it as primary metric, and reduce auto-research sweep to ≤200h H100.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"Missing citation: Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025, Liu & Niehues). This paper directly shows middle layers are most important for cross-lingual transfer alignment across 1,000+ language pairs — directly supporting and potentially complicating CLS-LoRA's factual-transfer layer partition. Reviewers will ask why this is not cited.\", \"Missing citation: Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (arXiv:2506.01675, ACL 2025 short paper). This paper studies asymmetric cross-lingual cultural transfer with a frequency-based hypothesis, providing empirical background that should be acknowledged in CLS-LoRA's problem framing.\", \"Core mechanistic assumption gap: The factual-vs-cultural layer partition is derived from Surgical Steering, an inference-time activation intervention. The revision does not explicitly argue why inference-time steerability at layer L implies that freezing layer L during LoRA training prevents erasure — these are distinct causal claims. Stage 1 empirically validates this, but the paper should include a one-paragraph mechanistic bridge explaining the connection before Stage 1 results are presented.\", \"Stage 2 probe data source underspecified: The per-layer linear probes require 'culture-specific benchmark items' for the cultural-localization score. It is unclear whether these come from CulturalBench/SemEval-2026 Task 7 held-out splits or require new annotation. Given SemEval-2026 Task 7 prohibits use of its data for training (confirmed), the probe training data source must be stated explicitly; using CulturalBench for probe training and SemEval for final evaluation would resolve this.\", \"Round 1 incorrectly flagged INCLINE's 'ACL 2025 Outstanding Paper' designation — independently confirmed that INCLINE IS listed among the 26 ACL 2025 Outstanding Papers; the revision correctly retained this label and no fix is needed here.\"]\nFeedback: The revision has successfully resolved all four critical Round 1 issues: MLAS-LoRA is cited and differentiated across three axes, Source-Shielded Updates is added, auto-research compute is trimmed to ~115h H100 (within the 200h constraint), LLaMA 4 Scout is replaced by Qwen3-8B + Aya-23-8B with explicit justification, and the structural-vs-behavioral erasure ambiguity is addressed by Stage 1. Note that Round 1's INCLINE flag was incorrect — it IS an ACL 2025 Outstanding Paper; the revision rightly kept that label.\n\nThree targeted fixes are needed before this is ready:\n\n1. **Add the two missing ACL 2025 citations.** In the landscape section, add: (a) Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025) — acknowledge that it establishes middle-layer primacy for cross-lingual factual transfer via representation alignment, and that CLS-LoRA extends this by additionally protecting cultural-knowledge layers from LoRA updates; (b) Cross-Lingual Transfer of Cultural Knowledge (arXiv:2506.01675, ACL 2025) — acknowledge as empirical background showing cultural transfer asymmetry for low-resource languages, motivating the need for training-time prevention.\n\n2. **Add a mechanistic bridge paragraph.** Before Stage 1 results, add: 'Our freezing strategy relies on a critical assumption: that the layer indices most sensitive to cultural-vs-factual steering at inference time (per arXiv:2510.26024) correspond to the layers where LoRA updates most destructively disrupt cultural routing during training. Stage 1 empirically validates this assumption: if post-full-LoRA cultural probe accuracy is preserved, erasure is behavioral and layer freezing is the correct intervention; if probe accuracy drops, erasure is partly representational and the KL-divergence regularizer becomes critical.'\n\n3. **Specify probe training data explicitly.** Clarify that Stage 2 probes are trained on held-out splits of CulturalBench (available at ACL 2025) for cultural-localization scores and TyDiQA/XQUAD for factual-transfer scores — not on SemEval-2026 Task 7 (evaluation-only by task rules) and not requiring new annotation.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL misattribution: The core_problem section states arXiv:2504.10191 'reveals the suppression is often behavioral rather than purely representational: cultural knowledge frequently survives as recoverable activations in deeper layers but is no longer surfaced in model outputs after fine-tuning.' This is factually wrong. arXiv:2504.10191 studies inference-time steering of cultural knowledge in already-trained (not instruction-fine-tuned) models, primarily Gemma2-9b-it. It does not study post-fine-tuning behavior at all, and makes no claim about whether cultural knowledge survives as recoverable activations after LoRA fine-tuning. The behavioral-vs-representational erasure distinction is CLS-LoRA's own hypothesis — which Stage 1 empirically tests — not an established finding from the cited paper. Any reviewer who reads arXiv:2504.10191 will reject this attribution.\", \"Layer depth percentage inconsistency: The paper claims 'cultural-knowledge layers concentrated at deeper layers ~72–94% model depth, per arXiv:2504.10191.' The actual mechanistic findings of arXiv:2504.10191 (Gemma2-9b, 42-layer architecture) identify critical cultural activation at absolute layers 23 and 30 (≈ 55-71% depth), and steering experiments cover layers 15-30 (≈ 36-71% depth) — significantly below the claimed 72-94% range. Stage 2 probing mitigates this by empirically determining the actual partition per model, but the percentage figure cited as empirically established from arXiv:2504.10191 is inaccurate and will mislead reviewers.\", \"arXiv:2510.26024 is under review at ICLR 2026 (submitted Sept 2025, not yet accepted). Its transfer-localization plane evaluation code is almost certainly not publicly released. The paper acknowledges this with a fallback, but does not explicitly state the primary framework comes from an unpublished ICLR 2026 submission — reviewers may check and flag this.\", \"Qwen3-8B has a 'thinking mode' (/think / /no_think) that activates extended chain-of-thought reasoning; in thinking mode, the model's internal generation pathway differs substantially from standard instruction following. The paper does not specify whether experiments use thinking or non-thinking mode. For cultural localization probing and instruction fine-tuning, using thinking mode could contaminate results by routing responses through CoT reasoning rather than direct cultural knowledge layers.\"]\nFeedback: The revision has successfully addressed all four Round 2 issues. Three targeted fixes remain before this is ready.\n\n1. **Fix the arXiv:2504.10191 attribution (critical).** The core_problem and opportunity sections claim this paper shows cultural knowledge 'survives as recoverable activations after fine-tuning' and that erasure is 'behavioral rather than representational.' This paper does not study fine-tuning at all — it studies inference-time cultural steering in pre-trained models. The correction is: reframe arXiv:2504.10191 as showing cultural knowledge is spatially localized and steerable in pre-trained models, which motivates the hypothesis that specific layers implement cultural routing pathways. Then explicitly state: 'Whether this localization and steerability survives LoRA instruction fine-tuning — and whether erasure is behavioral (routing disruption) or representational (information loss) — is the empirical question Stage 1 answers.' The KL regularizer is then naturally framed as the fallback for the representational-erasure case. This reframing is accurate, scientifically honest, and actually strengthens the paper by making Stage 1 a genuine empirical contribution rather than a validation of a fait accompli.\n\n2. **Correct the layer depth percentages.** Replace '~72–94% model depth, per arXiv:2504.10191' with something like: 'arXiv:2504.10191 identifies absolute layers 23-30 as critical for cultural activation in Gemma2-9b (a 42-layer model, corresponding to approximately 55-71% depth); arXiv:2510.26024 finds cultural localization in deeper layers relative to factual transfer. Stage 2 probing empirically determines the partition for each target model rather than hard-coding percentages from other architectures.' This is more accurate and emphasizes the empirical approach.\n\n3. **Add one sentence on Qwen3-8B thinking mode.** Clarify that all Qwen3-8B experiments are conducted in non-thinking mode (/no_think or without system prompt thinking tokens) to ensure consistent direct-generation behavior during LoRA fine-tuning and cultural localization evaluation. Without this, reviewers may question whether the thinking-mode routing path confounds the cultural layer partition.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL — Incorrect proceedings status of arXiv:2510.26024: This paper (CLS-LoRA's primary motivation) was accepted at ICLR 2026 (conference held April 22–26, 2026). The claim 'has not appeared in a published proceedings as of May 2026' is factually false as of today (May 10, 2026). The citation and all associated caveats about evaluation code unavailability and 'arXiv preprint' status must be updated to reflect its ICLR 2026 publication. This is a straightforward factual correction, but leaving it wrong will draw immediate rejection from any reviewer who checks.\", \"CRITICAL — Missing ICLR 2026 paper with directly contradictory mechanistic evidence: 'Neuron-Level Analysis of Cultural Understanding in Large Language Models' (arXiv:2510.08284, ICLR 2026, Yamamoto et al.) uses gradient-based neuron attribution to identify culture-relevant neurons and finds them 'concentrated in shallow to middle MLP layers' — directly opposing the deeper-layer (layers 19–30, ~45–71% depth) localization from arXiv:2504.10191 that grounds CLS-LoRA's freezing strategy. This paper was on arXiv since October 2025 and has been accepted at ICLR 2026 (held before the submission deadline). CLS-LoRA must cite it and either (a) argue the discrepancy is a methodological artifact (activation-steering subspaces vs. gradient-based neuron attribution measure different constructs), or (b) acknowledge it as an empirical uncertainty that Stage 2 probing resolves per-model. Without this, any EMNLP reviewer aware of arXiv:2510.08284 will flag it as a fundamental flaw.\", \"MODERATE — Missing related work: LayRA (arXiv:2509.11414, Sept 2025) is a layer-selective LoRA approach that applies LoRA to first and final transformer layers while freezing intermediate layers, for continual multilingual language addition. Its pipeline (layer-informed selective LoRA to prevent forgetting) shares the same mechanical strategy as CLS-LoRA, even though the objective (language preservation vs cultural preservation) differs. It should be cited and differentiated in the related work discussion, noting that LayRA partitions layers on a language-encoding-vs-reasoning axis while CLS-LoRA partitions on a factual-transfer-vs-cultural-localization axis.\"]\nFeedback: Round 4 correctly resolves all three Round 3 issues (arXiv:2504.10191 attribution, layer depth percentages, Qwen3-8B thinking mode). Three new fixes are now required:\n\n1. **Update arXiv:2510.26024 citation to ICLR 2026 (critical, ~1 hour of work).** The paper was accepted at ICLR 2026 (April 22–26, 2026) and is now a published conference paper. Replace all instances of 'arXiv preprint (submitted October 2025)' with 'ICLR 2026'. The caveat about evaluation code unavailability may still apply (check the ICLR 2026 camera-ready for a code link), but the 'not appeared in published proceedings as of May 2026' claim must be removed.\n\n2. **Cite and engage with arXiv:2510.08284 (critical, ~half a day of writing).** This ICLR 2026 paper finds culture-relevant neurons in shallow-to-middle MLP layers — not deep layers. CLS-LoRA must acknowledge this in the mechanistic bridge paragraph. The recommended framing: 'Yamamoto et al. (2026, arXiv:2510.08284) identify culture-relevant neurons via gradient attribution and find them in shallow-to-middle MLP layers, apparently in tension with the deeper-layer localization from Veselovsky et al. (2025, arXiv:2504.10191) and Han et al. (2026, ICLR). This discrepancy may reflect the difference between measuring activation-steering subspaces (which can span many layers) versus individual gradient-sensitive neurons (which can be small and shallow); Stage 2 probing resolves this empirically for each target model.' This framing converts a vulnerability into a strength: Stage 2 becomes the principled resolution to a genuine mechanistic debate in the literature.\n\n3. **Add LayRA to related work (moderate, ~30 minutes).** Cite arXiv:2509.11414 (Sept 2025) as a parallel selective-LoRA approach for multilingual LLMs. Differentiate: LayRA partitions on a source-language-encoding vs English-reasoning vs target-language-decoding functional axis; CLS-LoRA partitions on a factual-transfer vs cultural-localization semantic axis that cuts across language-pair specificity. The cultural-preservation objective remains the categorical novelty.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE — Evaluation benchmark gap violating user requirements: The user required evaluation on XTREME-UP, XCOPA, XStoryCloze, MGSM, multilingual MMLU, TyDiQA, and FLORES. The paper covers only TyDiQA from this list (plus CulturalBench and SemEval-2026 Task 7). Any EMNLP reviewer will ask: does CLS-LoRA hurt general cross-lingual commonsense reasoning (XCOPA, XStoryCloze) or multilingual arithmetic (MGSM)? Without at least XCOPA and MGSM results, the paper cannot demonstrate that cultural preservation does not come at the cost of broader multilingual competence. These are fast to run (standard few-shot evaluation, ~2–4h per benchmark per model) and should be added to Stage 4.\", \"MODERATE — Missing 'full LoRA + KL penalty only' ablation: The paper proposes layer freezing + optional KL regularization, but never isolates the contribution of layer freezing from KL regularization alone. A 'full LoRA + KL-divergence penalty on cultural-layer activations (no freezing)' baseline is essential to demonstrate that layer freezing is the necessary mechanism, not just the regularization. Without this ablation, a reviewer could argue KL regularization alone achieves the same preservation and layer freezing is unnecessary complexity. This ablation requires ~4–6 additional runs and should be added to the auto sweep.\", \"MINOR — Stage 1 probe methodology underspecified: Stage 1 measures 'per-layer cultural probe accuracy before and after' full LoRA fine-tuning. It is ambiguous whether the Stage 1 probe is (a) trained on pre-fine-tuned representations and applied to post-fine-tuned representations (cross-checkpoint transfer), or (b) separately trained on each checkpoint's representations. If (a), probe failure could reflect activation-space reorganization rather than information loss, confounding the behavioral-vs-representational distinction Stage 1 is designed to make. The paper should clarify that separate probes are trained and evaluated on held-out data from each checkpoint, making the comparison meaningful.\", \"MINOR — Factual correction: The paper continues to note 'submitted to ICLR 2026' for arXiv:2510.26024, but as of May 2026, HyoJung Han's own publication page lists this paper as an arXiv preprint with no confirmed proceedings venue—suggesting it was not accepted at ICLR 2026. The submission's existing characterization ('as of May 2026, the first author's publication page continues to characterize it as an arXiv preprint without a confirmed proceedings venue') is correct and should remain. Note: the Round 4 reviewer's claim that it was 'accepted at ICLR 2026' was factually wrong; the Round 5 revision's handling is accurate. No change needed beyond confirming this is stable.\"]\nFeedback: Round 5 has cleanly resolved all three Round 4 issues. The Yamamoto et al. integration is thorough and the mechanistic framing is now scientifically honest. Two targeted fixes are needed before this is ready:\n\n1. **Expand Stage 4 evaluation to include XCOPA and MGSM (moderate, ~1 GPU-day).** Add two cross-lingual commonsense benchmarks (XCOPA, XStoryCloze) and one multilingual reasoning benchmark (MGSM) to Stage 4. These measure capabilities orthogonal to cultural localization and factual QA. The paper needs to show CLS-LoRA does not regress on these relative to the full-LoRA baseline. If CLS-LoRA freezes cultural layers but those layers also encode commonsense knowledge, XCOPA performance could drop — which would be both a problem and an interesting finding. These benchmarks are free to run via lm-eval-harness and take ~2–4h per model. This directly addresses the user's specified evaluation requirements.\n\n2. **Add a 'full LoRA + KL only' ablation to Stage 3 (moderate, ~4–6 additional runs).** Without this baseline, the paper cannot argue that layer freezing is the operative mechanism rather than the KL regularizer alone. The ablation grid should include: (a) full LoRA (current baseline), (b) full LoRA + KL penalty, (c) CLS-LoRA frozen (no KL), and (d) CLS-LoRA frozen + KL (proposed method). This 2×2 table cleanly isolates the contributions of each component.\n\n3. **Clarify Stage 1 probe training protocol (minor, ~1 paragraph).** Specify that Stage 1 trains separate probes on the pre-fine-tuned and post-fine-tuned checkpoint representations respectively (not cross-checkpoint transfer), to ensure that a drop in probe accuracy reflects information loss rather than activation-space reorganization. This removes a methodological ambiguity that a probing-literate reviewer would flag.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:44:17.353Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:44:17.353Z",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

## Round 1

75 recorded events

### User

_source line 3 · 2026-05-10T07:44:17.374Z_

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
  "title": "Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignment",
  "project_name": "cls_lora_cultural_preservation",
  "source": "web_research",
  "level": "solid",
  "core_problem": "Cross-lingual fine-tuning systematically suppresses culturally-grounded, language-specific knowledge while improving factual transfer—a phenomenon called 'cultural erasure.' Mechanistic work (arXiv:2504.10191) demonstrates that in pre-trained instruction-tuned models, cultural knowledge is spatially localized in specific layers and steerable via linear activation vectors, suggesting particular layer indices implement cultural routing pathways. Whether this spatial localization persists after LoRA instruction fine-tuning—and whether cross-lingual fine-tuning causes behavioral erasure (routing pathway disruption), representational erasure (information loss), or both—remains empirically untested. No training-time method prevents either failure mode, forcing practitioners to choose between cross-lingual capability and cultural authenticity. A complementary mechanistic uncertainty reinforces the need for per-model empirical investigation: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deeper-layer localization (layers 19–30, approximately 45–71% depth in Gemma2-9b-it) identified via activation-steering analysis in arXiv:2504.10191. The two methodologies measure different constructs—discrete high-influence neurons versus distributed activation-space subspaces—and their disagreement means the culturally-critical layer partition cannot be reliably imported from prior work for an arbitrary target model; it must be discovered empirically.",
  "opportunity": "'Rethinking Cross-lingual Alignment' (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026) rigorously demonstrates that every tested cross-lingual alignment approach degrades cultural localization across all six languages, and proposes Surgical Steering as a remedy—but only at inference time, requiring per-query layer manipulation and offering no prevention during training. The finding that factual transfer and cultural localization are optimally steerable at different model layers is actionable: applying LoRA selectively to factual-transfer layers while freezing cultural-knowledge layers during instruction fine-tuning would prevent erasure at the source. arXiv:2504.10191 establishes that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors in specific layers (notably layers 19–30 in Gemma2-9b-it, with peaks at layers 23 and 30), supporting the hypothesis that particular layer indices implement cultural routing pathways. CLS-LoRA's freezing strategy is designed to exploit this structure: if that spatial localization persists after LoRA fine-tuning (behavioral erasure—routing disrupted but representations intact), freezing those layers during training prevents routing disruption; if fine-tuning also degrades the representations themselves (representational erasure), the KL-divergence penalty anchors cultural-layer activations to their pretrained distribution. Stage 1 empirically distinguishes these two failure modes before the main sweep begins. Crucially, the layer partition question is now a live empirical debate in the literature: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) independently find culture-relevant neurons in shallow-to-middle MLP layers using gradient attribution, while activation-steering work (arXiv:2504.10191, arXiv:2510.26024) localizes cultural steerability in deeper layers. This genuine methodological disagreement elevates Stage 2 probing from a validation step to the principled empirical resolution of an open question—CLS-LoRA discovers the culturally-critical partition for each target model rather than assuming it from any single prior study. This is feasible with any open-source dense multilingual model via a lightweight per-layer probing step.",
  "landscape": "INCLINE (arXiv:2410.12462, ACL 2025 outstanding paper) aligns internal representations from low-resource to high-resource languages via learned projection matrices derived from parallel sentences, improving cross-lingual task performance but not distinguishing factual from cultural knowledge. Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025, Liu & Niehues) provides the empirical foundation for CLS-LoRA's factual-transfer layer partition: through translation retrieval probing across 1,190 language pairs on Llama 3 and Qwen 2.5, it establishes that layer 16 (50% depth in a 32-layer model) is the key integration point for cross-lingual semantic alignment, and that incorporating a middle-layer alignment objective consistently improves cross-lingual task performance particularly for lower-resource languages. CLS-LoRA extends this by additionally protecting cultural-knowledge layers from LoRA updates—arXiv:2504.10191 identifies layers 19–30 (approximately 45–71% depth in Gemma2-9b-it's 42-layer architecture, with peak cultural activation at layers 23 and 30) as critical for cultural routing, and Stage 2 probing empirically determines the analogous partition for each target model—a protection axis entirely absent from Liu & Niehues, whose work does not distinguish factual from cultural knowledge and proposes no cultural preservation objective. Cross-Lingual Transfer of Cultural Knowledge (arXiv:2506.01675, ACL 2025 short paper, Zhang et al.) provides empirical background showing cultural knowledge transfer is asymmetric: high-resource language pairs exhibit bidirectional transfer while low-resource languages primarily export cultural knowledge to English without reciprocal benefit, driven by a frequency-based pretraining data mechanism. This asymmetry directly motivates training-time prevention of cultural erasure—low-resource languages are disproportionately at risk and most in need of the protection CLS-LoRA provides. AlignX (arXiv:2509.24338, EMNLP 2025) and CM-Align (arXiv:2509.08541) apply two-stage and consistency-based multilingual alignment respectively, both optimizing convergence without a cultural preservation objective. Language Surgery/ITLC (arXiv:2506.12450) disentangles language-specific from agnostic information through latent injection at inference time, but does not train models to preserve this distinction. Alignment through steering (arXiv:2505.12584) adds a learned residual-stream vector at a single layer; it outperforms many baselines but still does not model the factual-cultural layer split. Surgical Steering (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 the first author's publication page lists this as an arXiv preprint without a confirmed proceedings venue) is the only method addressing the cultural erasure problem, and is strictly an inference-time patch over an already-erased model. arXiv:2504.10191 ('Localized Cultural Knowledge is Conserved and Controllable in LLMs', April 2025) demonstrates that in pre-trained instruction-tuned models, cultural knowledge exists as spatially localized steerable activation-space vectors—mechanistic analysis on Gemma2-9b-it (42 layers) identifies layers 19–30 as critical for cultural activation, with peak effects at layers 23 and 30 (approximately 55–71% depth)—and can be controlled via linear steering at inference time. This establishes spatial localization of cultural knowledge in pre-trained models, motivating CLS-LoRA's hypothesis that specific layer indices implement cultural routing pathways; whether this localization persists after LoRA instruction fine-tuning is precisely what Stage 1 tests.\n\nYamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) conduct a neuron-level analysis of cultural understanding using a gradient-based scoring method with additional filtering for precise refinement. They identify both culture-general neurons (supporting cultural understanding across cultures) and culture-specific neurons (tied to individual cultures), which together comprise less than 1% of all neurons and are concentrated in shallow-to-middle MLP layers—not in the deeper layers identified by activation-steering analysis in arXiv:2504.10191. Suppressing these neurons degrades cultural benchmark performance by up to 30% while leaving general NLU tasks largely unaffected. This finding is in apparent tension with the deeper-layer localization from arXiv:2504.10191 and arXiv:2510.26024, reflecting a genuine methodological distinction: gradient attribution identifies discrete neurons with the highest individual causal influence, which may be sparse and concentrated in earlier layers; activation-steering subspaces reflect distributed representational geometry that implements cultural routing across many layers and may peak in depth-profile at different points. CLS-LoRA's Stage 2 probing directly bridges this debate: rather than assuming either result, it measures per-layer probe accuracy on each target model and discovers the cultural-knowledge partition empirically. If shallow neurons (Yamamoto et al.) dominate, Stage 2 will assign those layers to the frozen cultural partition; if deeper subspaces (arXiv:2504.10191) dominate, Stage 2 will assign those layers instead. Stage 2 is thus a model-specific resolution mechanism that makes CLS-LoRA robust to methodological disagreements in the mechanistic literature.\n\nTwo directly related selective-LoRA methods require explicit differentiation. MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762) detects language-aware neurons in a teacher model and injects extracted knowledge into language-pair-specific LoRA modules in a student model for multilingual machine translation, achieving +1.7 BLEU on average. While MLAS-LoRA and CLS-LoRA both employ a probe-then-selective-LoRA pipeline, they differ on three critical axes: (1) task domain—MLAS-LoRA targets MT translation quality whereas CLS-LoRA targets cultural knowledge preservation during instruction fine-tuning; (2) partition dimension—MLAS-LoRA partitions along language-pair specificity (language-A vs language-B neurons) whereas CLS-LoRA partitions along the factual-transfer vs cultural-localization semantic axis, which cuts across language pairs; and (3) objective—MLAS-LoRA optimizes translation accuracy via teacher-student knowledge distillation whereas CLS-LoRA optimizes a cultural-preservation signal with no distillation component. The cultural-preservation objective is the categorical novelty: no prior selective-LoRA work defines a 'keep culturally-grounded outputs intact' training signal. LayRA (arXiv:2509.11414, September 2025) proposes layer-selective LoRA for continual multilingual language addition, applying LoRA to initial and final transformer layers (the first 10 and last 2 layers, plus embeddings and LM head) while freezing intermediate layers. The partition rationale—that multilingual models encode source-language inputs in initial layers, reason in English in middle layers, and decode into the target language in final layers—leads to a source-language-encoding vs English-reasoning vs target-language-decoding functional partition axis. CLS-LoRA differs on three dimensions: (1) objective—LayRA enables new-language addition without catastrophic forgetting of existing languages, whereas CLS-LoRA preserves cultural knowledge during cross-lingual instruction fine-tuning; (2) partition axis—LayRA's functional encoding/reasoning/decoding axis is defined over language identity and cuts uniformly across all languages, whereas CLS-LoRA's factual-transfer vs cultural-localization semantic axis cuts across language-pair specificity; (3) partition method—LayRA hard-codes specific layer indices derived from qualitative linguistic reasoning, whereas CLS-LoRA uses empirical per-layer probing to discover the partition for each target model, enabling adaptation to the contested mechanistic landscape. The cultural-preservation objective remains the categorical novelty absent from LayRA. Source-Shielded Updates (arXiv:2512.04844, Nov 2025) proposes column-wise parameter freezing to prevent catastrophic forgetting of source-language task performance during target-language adaptation—addressing cross-lingual interference but not the factual-vs-cultural layer distinction or cultural knowledge preservation as a first-class objective.",
  "approach": "We propose Cultural-Layer-Selective LoRA (CLS-LoRA), a training-time method that prevents cultural erasure without sacrificing factual cross-lingual transfer. The pipeline has four stages.\n\nMechanistic bridge. Our layer-freezing strategy rests on a hypothesis connecting inference-time observations to training-time interventions: the layer indices most sensitive to cultural-vs-factual activation steering at inference time (arXiv:2510.26024, corroborated by cultural customization vectors in arXiv:2504.10191 concentrated at layers 19–30 in Gemma2-9b-it) identify the weight matrices that implement cultural routing. LoRA updates modify precisely these weight matrices; applying LoRA to cultural-knowledge layers may therefore disrupt the routing pathways through which culturally-grounded representations reach outputs. This hypothesis involves a genuine empirical uncertainty that the literature has not resolved: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deep-layer activation-steering localization from arXiv:2504.10191. The discrepancy most likely reflects the difference between measuring discrete high-influence neurons (gradient attribution captures sparse, individually causal units that may be early in the network) versus measuring distributed activation subspaces (steering analysis captures the geometry of representational routing, which may span many layers and peak later). Neither result invalidates the other; they measure different aspects of how cultural knowledge is implemented. Stage 2 probing is designed precisely for this uncertainty: by measuring per-layer probe accuracy directly on each target model's representations, it discovers the culturally-critical partition without assuming either methodological lens is correct—if shallow neurons dominate functionally, Stage 2 identifies shallow layers as the cultural partition; if deeper subspaces dominate, Stage 2 identifies those instead. Whether the representations themselves persist as recoverable vectors after full LoRA fine-tuning (behavioral erasure) or are also degraded (representational erasure) is a separate open empirical question—Stage 1 provides this answer. Freezing the empirically-identified cultural-knowledge layers during training preserves both the routing weights and the residual-stream geometry that steerability depends on, addressing both failure modes by design.\n\nStage 1 — Structural diagnostic: Before the main sweep, we run full-LoRA instruction fine-tuning on a held-out model checkpoint and measure per-layer cultural probe accuracy before and after. Stage 1 trains separate linear probes on each checkpoint's frozen representations—one probe trained and evaluated on the pretrained-checkpoint's layer activations, one probe trained and evaluated on the post-LoRA-checkpoint's layer activations—using the same held-out cultural question split for both. This ensures accuracy differences reflect genuine representational change rather than activation-space reorganization: applying a single probe trained on pretrained representations cross-checkpoint to post-LoRA representations would fail if LoRA remaps the activation geometry without destroying cultural information (behavioral erasure), conflating reorganization with information loss; separate per-checkpoint probes make the comparison clean and the behavioral-vs-representational distinction interpretable. If probe accuracy is maintained post-training, erasure is confirmed as behavioral (pathway disruption) and layer freezing is the correct intervention; if probe accuracy drops, erasure is partly representational and the KL-divergence regularizer in Stage 3 becomes critical. This diagnostic sharpens the mechanistic story and validates the layer-freezing strategy regardless of which failure mode dominates. An automated entropy-based partition fallback replaces human inspection when probe curves are bimodal or noisy, reducing the agent failure mode from prior review.\n\nStage 2 — Layer profiling: Lightweight linear probes (one per transformer layer) are trained on a small parallel corpus to produce per-layer factual-transfer and cultural-localization accuracy scores, yielding a principled layer partition. For factual transfer, the empirical expectation from arXiv:2502.14830 (Liu & Niehues) is approximately middle layers (~50% model depth). For cultural knowledge, arXiv:2504.10191 identifies layers 19–30 as critical in Gemma2-9b-it (approximately 45–71% depth in a 42-layer model, with peak effects at layers 23 and 30); Yamamoto et al. (arXiv:2510.08284, ICLR 2026) find culture-relevant neurons in shallow-to-middle MLP layers via gradient attribution. Stage 2 probing empirically determines the partition boundaries for each target model—Qwen3-8B (36 layers) and Aya-23-8B—rather than hard-coding percentages from either prior study; this is the methodologically sound response to the contested mechanistic landscape. For cultural-localization probes, we use held-out splits of CulturalBench (ACL 2025; 1,696 human-verified questions across 45 global regions), which is publicly available for training use. For factual-transfer probes, we use held-out splits of TyDiQA and XQUAD. SemEval-2026 Task 7 data (BLEnD) is reserved strictly for final evaluation and is not used in probe training, consistent with the task's evaluation-only rules (confirmed via the official task repository). No new annotation is required.\n\nStage 3 — Selective LoRA training: LoRA adapters (via Hugging Face PEFT target_modules) are inserted exclusively into factual-transfer layers and trained with standard instruction fine-tuning loss on multilingual instruction data, while cultural-knowledge layers remain fully frozen. An optional auxiliary KL-divergence penalty on a held-out cultural probe set discourages residual drift in frozen layers' downstream activations. To establish that layer freezing is the operative mechanism rather than KL regularization alone, Stage 3 includes a 2×2 ablation: (a) full LoRA without KL penalty (existing baseline); (b) full LoRA with KL-divergence penalty on cultural-layer activations (regularization-only baseline, new); (c) CLS-LoRA with layer freezing and no KL penalty (freezing-only; already present in the sweep as the no-regularization variant); (d) CLS-LoRA with layer freezing and KL penalty (proposed method). Condition (b) is the critical addition: it tests whether KL regularization alone, without the complexity of a learned layer partition, achieves equivalent cultural preservation. If (b) matches (d), the partitioning step is unnecessary overhead; if (c) and (d) both outperform (b), layer freezing is confirmed as the operative mechanism. Approximately 4–6 additional training runs (condition (b) only; 2 models × 2–3 seeds) are added to the auto sweep; conditions (a), (c), and (d) are already covered by existing runs.\n\nStage 4 — Evaluation: Experiments run on Qwen3-8B (primary: confirmed dense, 36 transformer layers, 119 languages and dialects, 8.2B parameters) and Aya-23-8B (secondary: confirmed dense decoder-only, 23 languages, 8B parameters) for cross-architecture generalization. All Qwen3-8B experiments are conducted in non-thinking mode (enable_thinking=False in the chat template), ensuring consistent direct-generation behavior during both LoRA fine-tuning and cultural localization probing without interference from chain-of-thought reasoning pathways. LLaMA 4 Scout is excluded—its 48-block, 16-expert MoE architecture makes the factual-vs-cultural layer partition from arXiv:2510.26024, established on dense models, methodologically inapplicable without separate MoE-specific validation. Evaluation uses CulturalBench and SemEval-2026 Task 7 as primary cultural metrics. To verify that CLS-LoRA does not regress on capabilities orthogonal to cultural localization and factual QA, Stage 4 adds three supplementary evaluation tracks via lm-evaluation-harness: cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; lm-eval task group xcopa_[lang]); cross-lingual narrative understanding (XStoryCloze, 11 languages, zero-shot; lm-eval task group xstorycloze); and multilingual arithmetic chain-of-thought (MGSM, 11 languages, direct mode; lm-eval task mgsm_direct). Each benchmark requires approximately 2–4 GPU-hours per model; together they add ~18–24h A100 total across both target models and all evaluated checkpoints. XCOPA is the most mechanistically relevant: if Stage 2's cultural-knowledge layer partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain commonsense transfer—an outcome that would be reported transparently and interpreted as a scope constraint on the method (cultural preservation trades off against commonsense transfer in those layers) rather than treated as an uncontrolled failure. MGSM verifies that the factual-transfer LoRA updates preserve multilingual arithmetic reasoning. All three benchmarks use standard zero-shot or direct evaluation protocols already in lm-evaluation-harness and require no additional training data. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; we therefore employ the explicitly defined fallback evaluation—a 2D scatter of cross-lingual factual accuracy (XQUAD/TyDiQA) vs cultural localization accuracy (CulturalBench) across languages, normalized to the pre-fine-tuning baseline, yielding the same transfer-localization interpretive framework. We compare against full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA (adapted to the instruction-FT setting), and Source-Shielded Updates baselines to demonstrate that CLS-LoRA Pareto-dominates prior methods in the transfer-localization trade-off space.",
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
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — viable only with auto-research mode given the 15-day window from May 10, 2026",
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
    "Mitigating Catastrophic Forgetting in Target Language Adaptation of LLMs via Source-Shielded Updates (arXiv:2512.04844, Nov 2025)",
    "AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment (EMNLP 2025, arXiv:2509.24338)",
    "CM-Align: Consistency-based Multilingual Alignment for Large Language Models (arXiv:2509.08541, 2025)",
    "Language Surgery in Multilingual Large Language Models / ITLC (arXiv:2506.12450, 2025)",
    "Improving Multilingual Language Models by Aligning Representations through Steering (arXiv:2505.12584, 2025)",
    "Localized Cultural Knowledge is Conserved and Controllable in Large Language Models (arXiv:2504.10191, 2025)",
    "LoRA: Low-Rank Adaptation of Large Language Models (ICLR 2022, arXiv:2106.09685)",
    "XCOPA: Evaluation of Causal Commonsense Reasoning in Multiple Languages (EMNLP 2020, arXiv:2005.00333, Ponti et al.)",
    "Few-shot Learning with Multilingual Language Models / XStoryCloze (arXiv:2112.10668, Lin et al., 2022)",
    "Language Models are Multilingual Chain-of-Thought Reasoners / MGSM (arXiv:2210.03057, Shi et al., 2022)"
  ],
  "description": "Cross-lingual instruction fine-tuning demonstrably erases culturally-localized knowledge across all tested alignment approaches—yet no training-time prevention exists. Mechanistic work (arXiv:2504.10191) shows that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors (in Gemma2-9b-it's 42-layer architecture, layers 19–30, with peak effects at layers 23 and 30 corresponding to approximately 55–71% model depth), suggesting specific layer indices implement cultural routing pathways. A parallel ICLR 2026 result (Yamamoto et al., arXiv:2510.08284) reaches an apparently different conclusion using gradient-based neuron attribution: culture-relevant neurons are concentrated in shallow-to-middle MLP layers. This methodological discrepancy—discrete high-influence neurons (gradient attribution) versus distributed representational subspaces (activation steering)—reflects different aspects of cultural knowledge implementation and constitutes a live empirical debate in the literature. Whether cultural localization persists after LoRA instruction fine-tuning—and whether erasure is behavioral (routing disruption) or representational (information loss)—is the empirical question Stage 1 answers. We propose Cultural-Layer-Selective LoRA (CLS-LoRA), which prevents both failure modes through a four-stage pipeline.\n\nA mechanistic bridge paragraph (placed before Stage 1) formalizes the training-time implication and acknowledges the mechanistic debate: the layer indices most sensitive to cultural activation steering at inference time identify weight matrices that implement cultural routing; LoRA updates to those weights may disrupt routing pathways; freezing those layers preserves both routing weights and residual-stream geometry. The contested layer localization (deep-layer subspaces per arXiv:2504.10191/arXiv:2510.26024 versus shallow-to-middle neurons per Yamamoto et al. ICLR 2026) is resolved not by choosing a side but by Stage 2 probing: measuring per-layer probe accuracy directly on each target model discovers the culturally-critical partition empirically, making CLS-LoRA robust to methodological disagreements in the mechanistic literature. Stage 1 distinguishes behavioral from representational erasure and determines whether KL regularization is necessary; crucially, Stage 1 trains separate linear probes on each checkpoint's frozen representations—one on the pretrained-checkpoint activations and one on the post-LoRA-checkpoint activations, both evaluated on the same held-out cultural split—so that accuracy differences reflect genuine representational change rather than activation-space reorganization.\n\nStage 2 runs lightweight linear probes to partition layers: factual-transfer probes trained on TyDiQA/XQUAD held-out splits; cultural-localization probes trained on held-out splits of CulturalBench (ACL 2025, publicly available for training use); SemEval-2026 Task 7 data (BLEnD) reserved strictly for final evaluation per its evaluation-only rules. Stage 2 determines the actual partition boundaries for each target model rather than hard-coding architecture-specific percentages from any single prior study—the principled response to the contested mechanistic landscape. Stage 3 applies LoRA exclusively to factual-transfer layers with an optional KL-divergence penalty; a 2×2 ablation isolates each component's contribution: (a) full LoRA no KL (baseline), (b) full LoRA + KL only (regularization-only, new), (c) CLS-LoRA frozen no KL (freezing-only), (d) CLS-LoRA frozen + KL (proposed method). Condition (b) is the critical new ablation: if it matches (d), layer partitioning is unnecessary overhead; if (c) and (d) outperform (b), layer freezing is confirmed as the operative mechanism. Stage 4 experiments run on Qwen3-8B (non-thinking mode, enable_thinking=False) and Aya-23-8B; primary evaluation uses CulturalBench and SemEval-2026 Task 7. Supplementary capability-regression evaluation via lm-evaluation-harness covers cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; task: xcopa_[lang]), narrative understanding (XStoryCloze, 11 languages, zero-shot; task: xstorycloze), and multilingual arithmetic (MGSM, 11 languages, direct mode; task: mgsm_direct); each requires ~2–4h per model and together add ~18–24h A100. If Stage 2's cultural-knowledge partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain XCOPA transfer—a mechanistically informative finding reported transparently. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; the fallback evaluation framework (2D scatter of factual vs. cultural accuracy across languages, normalized to pretrained baseline) is specified explicitly and yields the same interpretive structure.\n\nCLS-LoRA is differentiated from MLAS-LoRA (ACL 2025) across three axes: task domain (MT quality vs cultural preservation), partition dimension (language-pair specificity vs factual-cultural semantic axis), and objective (translation accuracy via distillation vs cultural preservation with no distillation). CLS-LoRA is differentiated from LayRA (arXiv:2509.11414) across three axes: objective (language addition vs cultural knowledge preservation during instruction fine-tuning), partition axis (LayRA's source-encoding/English-reasoning/target-decoding functional axis vs CLS-LoRA's factual-transfer/cultural-localization semantic axis), and partition method (LayRA hard-codes layer indices from qualitative reasoning vs CLS-LoRA uses per-model empirical probing). The cultural-preservation objective remains the categorical novelty absent from both. The auto-research sweep covers ~64–71 training runs (~122–144h H100), within the ≤200h H100 constraint, targeting a Pareto improvement over full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA, and Source-Shielded Updates in the transfer-localization trade-off space, with XCOPA/XStoryCloze/MGSM as orthogonal capability regression checks."
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
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "2820128c-6ba5-4b05-bf53-b336515554a4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:44:17.372Z_

```json
{
  "parentUuid": "2820128c-6ba5-4b05-bf53-b336515554a4",
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
  "uuid": "db106bff-9b02-460f-b747-7b722fa6094f",
  "timestamp": "2026-05-10T07:44:17.372Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:44:17.372Z_

```json
{
  "parentUuid": "db106bff-9b02-460f-b747-7b722fa6094f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c0a3c2a1-e4a1-467f-983d-25325b8b9aef",
  "timestamp": "2026-05-10T07:44:17.372Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
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
  "leafUuid": "c0a3c2a1-e4a1-467f-983d-25325b8b9aef",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cultural preservation in cross-lingual LoRA fine-tuning",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:44:34.845Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea (Round 6/10) for the paper "Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignment." I need to independently verify claims via WebSearch and assess whether the Round 5 issues have been addressed.

Looking at the Round 5 issues that needed fixing:
1. **MODERATE** — Evaluation benchmark gap (XCOPA, XStoryCloze, MGSM) - The current paper mentions adding these in Stage 4, so let me check if this is resolved.


2. **MODERATE** — Missing 'full LoRA + KL penalty only' ablation - The paper now has a 2×2 ablation with condition (b) being "full LoRA + KL only."
3. **MINOR** — Stage 1 probe methodology underspecified - The paper now clarifies separate probes.
4. **MINOR** — Factual correction about arXiv:2510.26024 status.

Checking the current paper, I can see the evaluation benchmarks are now included with supplementary capability-regression evaluation via lm-evaluation-harness covering cross-lingual tasks.

The full LoRA + KL ablation is also present in the 2×2 ablation setup with the regularization-only baseline.

For Stage 1, the paper describes how separate linear probes are trained on each checkpoint's frozen representations—evaluating both the pretrained and post-LoRA activations using the same held-out cultural question split.

The arXiv:2510.26024 status confirms it remains a preprint without a confirmed venue as of May 2026, matching the Round 5 confirmation.

Now I'm doing independent searches to verify whether there are newer competitive papers, confirm the key papers exist as described, and check if the compute estimates are realistic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0a3c2a1-e4a1-467f-983d-25325b8b9aef",
  "isSidechain": false,
  "requestId": "req_011CatWomLcrtyHm3bvA2W2X",
  "type": "assistant",
  "uuid": "dee49d43-87f6-4705-bcee-b9fb5363c59a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C8ijE7yPN4F7BfriWSsTLS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23764,
      "cache_read_input_tokens": 11631,
      "output_tokens": 897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 897,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23764
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

_source line 9 · 2026-05-10T07:44:34.849Z_

I'll conduct independent verification searches before issuing my verdict on this Round 6 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dee49d43-87f6-4705-bcee-b9fb5363c59a",
  "isSidechain": false,
  "requestId": "req_011CatWomLcrtyHm3bvA2W2X",
  "type": "assistant",
  "uuid": "f49be371-e25d-42ab-a294-a4fc9599d4f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C8ijE7yPN4F7BfriWSsTLS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23764,
      "cache_read_input_tokens": 11631,
      "output_tokens": 897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 897,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23764
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

_source line 10 · 2026-05-10T07:44:34.999Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01X2aYxqYzCcYDQHponEmhW8`</summary>

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
  "parentUuid": "f49be371-e25d-42ab-a294-a4fc9599d4f4",
  "isSidechain": false,
  "requestId": "req_011CatWomLcrtyHm3bvA2W2X",
  "type": "assistant",
  "uuid": "b1891d1a-82be-4f43-9748-8e01acff44c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C8ijE7yPN4F7BfriWSsTLS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23764,
      "cache_read_input_tokens": 11631,
      "output_tokens": 897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 897,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23764
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

_source line 11 · 2026-05-10T07:44:35.006Z_

<details><summary>↩ Tool result · `toolu_01X2aYxqYzCcYDQHponEmhW8`</summary>

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
  "parentUuid": "b1891d1a-82be-4f43-9748-8e01acff44c3",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "b124522f-9913-4ac5-8404-4132050ab3a7",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "b1891d1a-82be-4f43-9748-8e01acff44c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T07:44:37.965Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct my independent research. I need to:

1. Verify the key papers exist as described
2. Search for competing/concurrent work that might have been missed
3. Check the resource estimates
4. Verify whether Round 5 issues have been addressed in Round 6

Let me start with parallel searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b124522f-9913-4ac5-8404-4132050ab3a7",
  "isSidechain": false,
  "requestId": "req_011CatWq4tb23a2svo2WDSiS",
  "type": "assistant",
  "uuid": "460c8dbf-e3fd-4406-a2b3-f525bac52d1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FhsECtM1qjupwnvgo1rmiy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 35395,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 304,
          "cache_read_input_tokens": 35395,
          "cache_creation_input_tokens": 1917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1917
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

_source line 13 · 2026-05-10T07:44:38.376Z_

I'll run parallel searches to independently verify the key claims and find potential competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "460c8dbf-e3fd-4406-a2b3-f525bac52d1d",
  "isSidechain": false,
  "requestId": "req_011CatWq4tb23a2svo2WDSiS",
  "type": "assistant",
  "uuid": "6beca623-20b2-4569-9297-c143797f9120",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FhsECtM1qjupwnvgo1rmiy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 35395,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 304,
          "cache_read_input_tokens": 35395,
          "cache_creation_input_tokens": 1917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1917
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

_source line 14 · 2026-05-10T07:44:38.885Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Lgy7TnTyP2jkAXMT1ZUuo`</summary>

```json
{
  "query": "cultural erasure cross-lingual fine-tuning LoRA layer selective 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6beca623-20b2-4569-9297-c143797f9120",
  "isSidechain": false,
  "requestId": "req_011CatWq4tb23a2svo2WDSiS",
  "type": "assistant",
  "uuid": "a1ce22c1-9677-4e85-9061-ebabf9ac1955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FhsECtM1qjupwnvgo1rmiy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 35395,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 304,
          "cache_read_input_tokens": 35395,
          "cache_creation_input_tokens": 1917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1917
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

_source line 15 · 2026-05-10T07:44:39.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011tCUGjC6iuAaW2y7PhVXgB`</summary>

```json
{
  "query": "arXiv 2510.26024 \"rethinking cross-lingual alignment\" cultural localization ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1ce22c1-9677-4e85-9061-ebabf9ac1955",
  "isSidechain": false,
  "requestId": "req_011CatWq4tb23a2svo2WDSiS",
  "type": "assistant",
  "uuid": "d949a01e-7c7f-4a22-8cfc-64fb9ee56bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FhsECtM1qjupwnvgo1rmiy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 35395,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 304,
          "cache_read_input_tokens": 35395,
          "cache_creation_input_tokens": 1917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1917
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

_source line 16 · 2026-05-10T07:44:40.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015WcyepgNzSaeBUKAQuxi4C`</summary>

```json
{
  "query": "arXiv 2504.10191 \"localized cultural knowledge\" conserved controllable LLMs Gemma layers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d949a01e-7c7f-4a22-8cfc-64fb9ee56bc2",
  "isSidechain": false,
  "requestId": "req_011CatWq4tb23a2svo2WDSiS",
  "type": "assistant",
  "uuid": "197b4e3f-3916-4d95-8747-76a71b6af4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FhsECtM1qjupwnvgo1rmiy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 35395,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 304,
          "cache_read_input_tokens": 35395,
          "cache_creation_input_tokens": 1917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1917
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

_source line 17 · 2026-05-10T07:44:46.668Z_

<details><summary>↩ Tool result · `toolu_015WcyepgNzSaeBUKAQuxi4C`</summary>

```text
Web search results for query: "arXiv 2504.10191 "localized cultural knowledge" conserved controllable LLMs Gemma layers"

Links: [{"title":"[2504.10191] Localized Cultural Knowledge is Conserved and Controllable in Large Language Models","url":"https://arxiv.org/abs/2504.10191"},{"title":"Localized Cultural Knowledge is Conserved and Controllable in Large","url":"https://arxiv.org/pdf/2504.10191"},{"title":"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models","url":"https://arxiv.org/html/2504.10191"},{"title":"[2504.10191v1] Localized Cultural Knowledge is Conserved and Controllable in Large Language Models","url":"https://arxiv.org/abs/2504.10191v1"},{"title":"[Literature Review] Localized Cultural Knowledge is Conserved and Controllable in Large Language Models","url":"https://www.themoonlight.io/en/review/localized-cultural-knowledge-is-conserved-and-controllable-in-large-language-models"},{"title":"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/390773600_Localized_Cultural_Knowledge_is_Conserved_and_Controllable_in_Large_Language_Models"},{"title":"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=sK06hYt75z"},{"title":"James Evans on X: \"I'm thrilled about this new work that demonstrates the existence of cultural world models within LLMs and how local cultural and linguistic knowledge is conserved and controllable within them. To be clear, this doesn't yet occur \"for free\", but this makes clear how intelligent https://t.co/KAFhsipqZH\" / X","url":"https://x.com/profjamesevans/status/1912540823079485781"},{"title":"GitHub - vminvsky/localization-gap · GitHub","url":"https://github.com/vminvsky/localization-gap"},{"title":"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models","url":"https://citp.princeton.edu/resource-links/localized-cultural-knowledge-conserved-and-controllable-large-language-models"}]

I found the paper! Here's what I discovered about arXiv 2504.10191:

**Paper Title:** Localized Cultural Knowledge is Conserved and Controllable in Large Language Models

**Authors:** Veniamin Veselovsky, Berke Argin, Benedikt Stroebl, Chris Wendler, Robert West, James Evans, Thomas L. Griffiths, Arvind Narayanan

**Key Findings:**

Local cultural information persists within the models and can be readily activated for cultural customization. The researchers identified an "explicit-implicit localization gap," where while cultural knowledge exists within LLMs, it may not naturally surface in multilingual interactions if cultural context is not explicitly provided.

**Main Technical Contribution:**

An explicit cultural customization vector was identified, conserved across all non-English languages explored, which enables LLMs to be steered from the synthetic English cultural world-model toward each non-English cultural world.

**Models Studied:**

Seven models were evaluated: Aya-8b-it, Gemma2-9b-it, Gemma2-27b-it, Llama-3.1-70b-it, Llama-3.1-8b-it, Llama-3.1-8b-base, and GPT-4o.

**Mechanistic Analysis:**

For mechanistic interpretability analysis, the study examined Gemma2-9b-it using nnsight.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "197b4e3f-3916-4d95-8747-76a71b6af4a5",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "48d9fd34-2470-4df6-8c6a-74283ccb8601",
  "toolUseResult": {
    "query": "arXiv 2504.10191 \"localized cultural knowledge\" conserved controllable LLMs Gemma layers",
    "results": [
      {
        "tool_use_id": "srvtoolu_018fxyZc6GwpZALqBg9vMKF4",
        "content": [
          {
            "title": "[2504.10191] Localized Cultural Knowledge is Conserved and Controllable in Large Language Models",
            "url": "https://arxiv.org/abs/2504.10191"
          },
          {
            "title": "Localized Cultural Knowledge is Conserved and Controllable in Large",
            "url": "https://arxiv.org/pdf/2504.10191"
          },
          {
            "title": "Localized Cultural Knowledge is Conserved and Controllable in Large Language Models",
            "url": "https://arxiv.org/html/2504.10191"
          },
          {
            "title": "[2504.10191v1] Localized Cultural Knowledge is Conserved and Controllable in Large Language Models",
            "url": "https://arxiv.org/abs/2504.10191v1"
          },
          {
            "title": "[Literature Review] Localized Cultural Knowledge is Conserved and Controllable in Large Language Models",
            "url": "https://www.themoonlight.io/en/review/localized-cultural-knowledge-is-conserved-and-controllable-in-large-language-models"
          },
          {
            "title": "Localized Cultural Knowledge is Conserved and Controllable in Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/390773600_Localized_Cultural_Knowledge_is_Conserved_and_Controllable_in_Large_Language_Models"
          },
          {
            "title": "Localized Cultural Knowledge is Conserved and Controllable in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=sK06hYt75z"
          },
          {
            "title": "James Evans on X: \"I'm thrilled about this new work that demonstrates the existence of cultural world models within LLMs and how local cultural and linguistic knowledge is conserved and controllable within them. To be clear, this doesn't yet occur \"for free\", but this makes clear how intelligent https://t.co/KAFhsipqZH\" / X",
            "url": "https://x.com/profjamesevans/status/1912540823079485781"
          },
          {
            "title": "GitHub - vminvsky/localization-gap · GitHub",
            "url": "https://github.com/vminvsky/localization-gap"
          },
          {
            "title": "Localized Cultural Knowledge is Conserved and Controllable in Large Language Models",
            "url": "https://citp.princeton.edu/resource-links/localized-cultural-knowledge-conserved-and-controllable-large-language-models"
          }
        ]
      },
      "I found the paper! Here's what I discovered about arXiv 2504.10191:\n\n**Paper Title:** Localized Cultural Knowledge is Conserved and Controllable in Large Language Models\n\n**Authors:** Veniamin Veselovsky, Berke Argin, Benedikt Stroebl, Chris Wendler, Robert West, James Evans, Thomas L. Griffiths, Arvind Narayanan\n\n**Key Findings:**\n\nLocal cultural information persists within the models and can be readily activated for cultural customization. The researchers identified an \"explicit-implicit localization gap,\" where while cultural knowledge exists within LLMs, it may not naturally surface in multilingual interactions if cultural context is not explicitly provided.\n\n**Main Technical Contribution:**\n\nAn explicit cultural customization vector was identified, conserved across all non-English languages explored, which enables LLMs to be steered from the synthetic English cultural world-model toward each non-English cultural world.\n\n**Models Studied:**\n\nSeven models were evaluated: Aya-8b-it, Gemma2-9b-it, Gemma2-27b-it, Llama-3.1-70b-it, Llama-3.1-8b-it, Llama-3.1-8b-base, and GPT-4o.\n\n**Mechanistic Analysis:**\n\nFor mechanistic interpretability analysis, the study examined Gemma2-9b-it using nnsight."
    ],
    "durationSeconds": 6.159858718000003
  },
  "sourceToolAssistantUUID": "197b4e3f-3916-4d95-8747-76a71b6af4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T07:44:46.762Z_

<details><summary>↩ Tool result · `toolu_011tCUGjC6iuAaW2y7PhVXgB`</summary>

```text
Web search results for query: "arXiv 2510.26024 "rethinking cross-lingual alignment" cultural localization ICLR 2026"

Links: [{"title":"[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://arxiv.org/abs/2510.26024"},{"title":"Under review RETHINKING CROSS-LINGUAL ALIGNMENT:","url":"https://arxiv.org/pdf/2510.26024"},{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | Request PDF","url":"https://www.researchgate.net/publication/397089048_Rethinking_Cross-lingual_Alignment_Balancing_Transfer_and_Cultural_Erasure_in_Multilingual_LLMs"},{"title":"HyoJung Han","url":"https://h-j-han.github.io/"},{"title":"Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://www.alphaxiv.org/overview/2510.26024v1"},{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | OpenReview","url":"https://openreview.net/forum?id=8DBHkEe0sm"},{"title":"Understanding Cross-Lingual Alignment—A Survey","url":"https://arxiv.org/html/2404.06228v2"},{"title":"Investigating Cultural Alignment of Large Language Models","url":"https://arxiv.org/html/2402.13231v2"},{"title":"Bridging Language Gaps: Advances in Cross-Lingual Information Retrieval with Multilingual LLMs","url":"https://arxiv.org/html/2510.00908v1"},{"title":"Rethinking AI cultural alignment","url":"https://arxiv.org/html/2501.07751"}]

Based on the search results, here's what I found about arXiv paper 2510.26024:

## Paper Overview

The paper titled "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs" was submitted on October 29, 2025, with authors HyoJung Han, Sweta Agrawal, and Eleftheria Briakou.

## Main Research Focus

Cross-lingual alignment (CLA) aims to align multilingual representations, enabling Large Language Models (LLMs) to seamlessly transfer knowledge across languages. However, this pursuit of representational convergence can inadvertently cause "cultural erasure"—the functional loss of providing culturally-situated responses that should diverge based on the query language.

## Key Methodology

The researchers systematically analyze this trade-off by introducing a holistic evaluation framework called the transfer-localization plane, which quantifies both desirable knowledge transfer and undesirable cultural erasure.

## Key Findings

Using this framework, the researchers re-evaluated recent CLA approaches and found that they consistently improve factual transfer at the direct cost of cultural localization across all six languages studied.

**Note:** The search results show this paper is "under review" (as indicated on the arXiv PDF page), so it may not have been accepted to ICLR 2026 yet. The paper was submitted in October 2025 and appears to be in the review process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d949a01e-7c7f-4a22-8cfc-64fb9ee56bc2",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "6c066f90-ee33-49b8-a1b5-36e1c3e81e98",
  "toolUseResult": {
    "query": "arXiv 2510.26024 \"rethinking cross-lingual alignment\" cultural localization ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0196uqLsP6jowfqGTyzkAQVS",
        "content": [
          {
            "title": "[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs",
            "url": "https://arxiv.org/abs/2510.26024"
          },
          {
            "title": "Under review RETHINKING CROSS-LINGUAL ALIGNMENT:",
            "url": "https://arxiv.org/pdf/2510.26024"
          },
          {
            "title": "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/397089048_Rethinking_Cross-lingual_Alignment_Balancing_Transfer_and_Cultural_Erasure_in_Multilingual_LLMs"
          },
          {
            "title": "HyoJung Han",
            "url": "https://h-j-han.github.io/"
          },
          {
            "title": "Balancing Transfer and Cultural Erasure in Multilingual LLMs",
            "url": "https://www.alphaxiv.org/overview/2510.26024v1"
          },
          {
            "title": "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=8DBHkEe0sm"
          },
          {
            "title": "Understanding Cross-Lingual Alignment—A Survey",
            "url": "https://arxiv.org/html/2404.06228v2"
          },
          {
            "title": "Investigating Cultural Alignment of Large Language Models",
            "url": "https://arxiv.org/html/2402.13231v2"
          },
          {
            "title": "Bridging Language Gaps: Advances in Cross-Lingual Information Retrieval with Multilingual LLMs",
            "url": "https://arxiv.org/html/2510.00908v1"
          },
          {
            "title": "Rethinking AI cultural alignment",
            "url": "https://arxiv.org/html/2501.07751"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2510.26024:\n\n## Paper Overview\n\nThe paper titled \"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs\" was submitted on October 29, 2025, with authors HyoJung Han, Sweta Agrawal, and Eleftheria Briakou.\n\n## Main Research Focus\n\nCross-lingual alignment (CLA) aims to align multilingual representations, enabling Large Language Models (LLMs) to seamlessly transfer knowledge across languages. However, this pursuit of representational convergence can inadvertently cause \"cultural erasure\"—the functional loss of providing culturally-situated responses that should diverge based on the query language.\n\n## Key Methodology\n\nThe researchers systematically analyze this trade-off by introducing a holistic evaluation framework called the transfer-localization plane, which quantifies both desirable knowledge transfer and undesirable cultural erasure.\n\n## Key Findings\n\nUsing this framework, the researchers re-evaluated recent CLA approaches and found that they consistently improve factual transfer at the direct cost of cultural localization across all six languages studied.\n\n**Note:** The search results show this paper is \"under review\" (as indicated on the arXiv PDF page), so it may not have been accepted to ICLR 2026 yet. The paper was submitted in October 2025 and appears to be in the review process."
    ],
    "durationSeconds": 7.214866029999998
  },
  "sourceToolAssistantUUID": "d949a01e-7c7f-4a22-8cfc-64fb9ee56bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T07:44:50.934Z_

<details><summary>↩ Tool result · `toolu_011Lgy7TnTyP2jkAXMT1ZUuo`</summary>

```text
Web search results for query: "cultural erasure cross-lingual fine-tuning LoRA layer selective 2025 2026 arxiv"

Links: [{"title":"[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://arxiv.org/abs/2510.26024"},{"title":"Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models","url":"https://arxiv.org/html/2510.13580"},{"title":"Governance-Aware Hybrid Fine-Tuning for Multilingual Large Language Models","url":"https://arxiv.org/html/2512.17344"},{"title":"Z-Erase: Enabling Concept Erasure in Single-Stream Diffusion Transformers","url":"https://arxiv.org/pdf/2603.25074"},{"title":"GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer","url":"https://www.arxiv.org/pdf/2601.06702"},{"title":"CE-LoRA: Computation-Efficient LoRA Fine-Tuning for Language Models","url":"https://arxiv.org/pdf/2502.01378"},{"title":"Cross-LoRA: A Data-Free LoRA Transfer Framework across Heterogeneous LLMs","url":"https://arxiv.org/html/2508.05232v1"},{"title":"Final Report - Fine Tuning Methods for Low-resource Languages","url":"https://arxiv.org/html/2510.04139v1"},{"title":"Beyond Training for Cultural Awareness: The Role of Dataset Linguistic Structure in Large Language Models","url":"https://arxiv.org/html/2602.01161"},{"title":"[2502.01378] CE-LoRA: Computation-Efficient LoRA Fine-Tuning for Language Models","url":"https://arxiv.org/abs/2502.01378"}]

I found several relevant arxiv papers related to your search query. Here are the most relevant results:

## Key Papers Found:

1. **"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs"** (arXiv 2510.26024, October 2025)
   - This work addresses "cultural erasure," the functional loss of providing culturally-situated responses that should diverge based on the query language
   - The authors introduce a holistic evaluation framework called the transfer-localization plane, which quantifies both desirable knowledge transfer and undesirable cultural erasure
   - They find that recent cross-lingual alignment approaches consistently improve factual transfer at the direct cost of cultural localization across all six languages studied

2. **"Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models"** (arXiv 2510.13580, February 2026)
   - This paper presents targeted sparse fine-tuning that achieves strong cross-lingual alignment, outperforming LoRA and random-subset fine-tuning
   - Targeted sparse fine-tuning of language-specific subnetworks consistently yields the largest gains on target-language tasks, while fully preserving general capabilities

3. **"GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer"** (arXiv 2601.06702, January 2026)
   - Focuses on sparsity policy learning for cross-lingual LoRA adaptation using pruning and fine-tuning strategies

4. **"Beyond Training for Cultural Awareness: The Role of Dataset Linguistic Structure in Large Language Models"** (arXiv 2602.01161, February 2026)
   - Explores whether cultural fine-tuning datasets exhibit consistent, measurable patterns in semantic content, lexical diversity, and stylistic variability that can be quantified prior to training

These papers directly address the intersection of cultural preservation, cross-lingual fine-tuning, layer-selective approaches, and LoRA-based methods in recent 2025-2026 research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1ce22c1-9677-4e85-9061-ebabf9ac1955",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "fbe4d075-6d04-4080-98ae-1eda3aed5ef5",
  "toolUseResult": {
    "query": "cultural erasure cross-lingual fine-tuning LoRA layer selective 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C9LGHehEznwyfUY7xKUAW7",
        "content": [
          {
            "title": "[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs",
            "url": "https://arxiv.org/abs/2510.26024"
          },
          {
            "title": "Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models",
            "url": "https://arxiv.org/html/2510.13580"
          },
          {
            "title": "Governance-Aware Hybrid Fine-Tuning for Multilingual Large Language Models",
            "url": "https://arxiv.org/html/2512.17344"
          },
          {
            "title": "Z-Erase: Enabling Concept Erasure in Single-Stream Diffusion Transformers",
            "url": "https://arxiv.org/pdf/2603.25074"
          },
          {
            "title": "GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer",
            "url": "https://www.arxiv.org/pdf/2601.06702"
          },
          {
            "title": "CE-LoRA: Computation-Efficient LoRA Fine-Tuning for Language Models",
            "url": "https://arxiv.org/pdf/2502.01378"
          },
          {
            "title": "Cross-LoRA: A Data-Free LoRA Transfer Framework across Heterogeneous LLMs",
            "url": "https://arxiv.org/html/2508.05232v1"
          },
          {
            "title": "Final Report - Fine Tuning Methods for Low-resource Languages",
            "url": "https://arxiv.org/html/2510.04139v1"
          },
          {
            "title": "Beyond Training for Cultural Awareness: The Role of Dataset Linguistic Structure in Large Language Models",
            "url": "https://arxiv.org/html/2602.01161"
          },
          {
            "title": "[2502.01378] CE-LoRA: Computation-Efficient LoRA Fine-Tuning for Language Models",
            "url": "https://arxiv.org/abs/2502.01378"
          }
        ]
      },
      "I found several relevant arxiv papers related to your search query. Here are the most relevant results:\n\n## Key Papers Found:\n\n1. **\"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs\"** (arXiv 2510.26024, October 2025)\n   - This work addresses \"cultural erasure,\" the functional loss of providing culturally-situated responses that should diverge based on the query language\n   - The authors introduce a holistic evaluation framework called the transfer-localization plane, which quantifies both desirable knowledge transfer and undesirable cultural erasure\n   - They find that recent cross-lingual alignment approaches consistently improve factual transfer at the direct cost of cultural localization across all six languages studied\n\n2. **\"Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models\"** (arXiv 2510.13580, February 2026)\n   - This paper presents targeted sparse fine-tuning that achieves strong cross-lingual alignment, outperforming LoRA and random-subset fine-tuning\n   - Targeted sparse fine-tuning of language-specific subnetworks consistently yields the largest gains on target-language tasks, while fully preserving general capabilities\n\n3. **\"GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer\"** (arXiv 2601.06702, January 2026)\n   - Focuses on sparsity policy learning for cross-lingual LoRA adaptation using pruning and fine-tuning strategies\n\n4. **\"Beyond Training for Cultural Awareness: The Role of Dataset Linguistic Structure in Large Language Models\"** (arXiv 2602.01161, February 2026)\n   - Explores whether cultural fine-tuning datasets exhibit consistent, measurable patterns in semantic content, lexical diversity, and stylistic variability that can be quantified prior to training\n\nThese papers directly address the intersection of cultural preservation, cross-lingual fine-tuning, layer-selective approaches, and LoRA-based methods in recent 2025-2026 research."
    ],
    "durationSeconds": 12.045834201999998
  },
  "sourceToolAssistantUUID": "a1ce22c1-9677-4e85-9061-ebabf9ac1955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "fbe4d075-6d04-4080-98ae-1eda3aed5ef5",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Cultural preservation in cross-lingual LoRA fine-tuning",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Assistant

_source line 22 · 2026-05-10T07:44:58.741Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've confirmed the existence of the key papers. Now let me search for more competitive work, specifically:
1. Sparse Subnetwork Enhancement for Underrepresented Languages (2510.13580) which could be related
2. GRASP LoRA (2601.06702) for cross-lingual transfer
3. Whether Yamamoto et al. ICLR 2026 paper exists (2510.08284)
4. Status of arXiv:2510.26024 regarding ICLR 2026 acceptance


I'm seeing that arXiv:2510.26024 is still under review rather than confirmed for ICLR 2026, and I've verified arXiv:2504.10191 exists. Now I need to track down those other potential competitors—the sparse subnetwork work, GRASP LoRA, and the Yamamoto paper—to get a complete picture of the competitive landscape.

I should also look into any very recent work from early 2026 specifically focused on cultural preservation in multilingual language models, since that might reveal newer approaches I haven't encountered yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbe4d075-6d04-4080-98ae-1eda3aed5ef5",
  "isSidechain": false,
  "requestId": "req_011CatWrEiDShy4hUfckJjDg",
  "type": "assistant",
  "uuid": "e99f6aae-5707-4263-828b-7be869f51b20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01F3Upgri5qzsUkaZW1LxdVb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1843,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 37312,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1843,
          "output_tokens": 522,
          "cache_read_input_tokens": 37312,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 23 · 2026-05-10T07:44:58.816Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q3F7TTgc67wPuKPamZVug4`</summary>

```json
{
  "query": "arXiv 2510.08284 \"neuron-level analysis cultural understanding\" LLMs Yamamoto ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e99f6aae-5707-4263-828b-7be869f51b20",
  "isSidechain": false,
  "requestId": "req_011CatWrEiDShy4hUfckJjDg",
  "type": "assistant",
  "uuid": "a7b6e155-23fa-4ee2-81c5-4970b76cd966",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01F3Upgri5qzsUkaZW1LxdVb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1843,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 37312,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1843,
          "output_tokens": 522,
          "cache_read_input_tokens": 37312,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 24 · 2026-05-10T07:44:59.105Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XAyjyy1ZaVKpyRrx82HNaa`</summary>

```json
{
  "query": "\"sparse subnetwork\" cross-lingual language-specific underrepresented languages 2510.13580 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7b6e155-23fa-4ee2-81c5-4970b76cd966",
  "isSidechain": false,
  "requestId": "req_011CatWrEiDShy4hUfckJjDg",
  "type": "assistant",
  "uuid": "2e756f10-4938-4207-a1e5-d374f22b04a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01F3Upgri5qzsUkaZW1LxdVb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1843,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 37312,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1843,
          "output_tokens": 522,
          "cache_read_input_tokens": 37312,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 25 · 2026-05-10T07:44:59.399Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K9pQVBPhBiASybJBWPQXi8`</summary>

```json
{
  "query": "cultural knowledge preservation multilingual fine-tuning training method LoRA freezing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e756f10-4938-4207-a1e5-d374f22b04a0",
  "isSidechain": false,
  "requestId": "req_011CatWrEiDShy4hUfckJjDg",
  "type": "assistant",
  "uuid": "50ba0803-82ec-42a1-bcd4-93ee6406b1d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01F3Upgri5qzsUkaZW1LxdVb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1843,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 37312,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1843,
          "output_tokens": 522,
          "cache_read_input_tokens": 37312,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 26 · 2026-05-10T07:45:05.621Z_

<details><summary>↩ Tool result · `toolu_01XAyjyy1ZaVKpyRrx82HNaa`</summary>

```text
Web search results for query: ""sparse subnetwork" cross-lingual language-specific underrepresented languages 2510.13580 2025 2026"

Links: [{"title":"[2510.13580] Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models","url":"https://arxiv.org/abs/2510.13580"},{"title":"Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models","url":"https://arxiv.org/html/2510.13580"},{"title":"Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"},{"title":"DeFT-X: Denoised Sparse Fine-Tuning for Zero-Shot Cross-Lingual Transfer","url":"https://arxiv.org/html/2505.15090"},{"title":"Language Adaptive Cross-lingual Speech Representation Learning with Sparse Sharing Sub-networks | Request PDF","url":"https://www.researchgate.net/publication/359129931_Language_Adaptive_Cross-lingual_Speech_Representation_Learning_with_Sparse_Sharing_Sub-networks"},{"title":"Unveiling Language Routing Isolation in Multilingual MoE Models for Interpretable Subnetwork Adaptation","url":"https://arxiv.org/html/2604.03592"},{"title":"Discovering Language-neutral Sub-networks in Multilingual Language Models | Request PDF","url":"https://www.researchgate.net/publication/372921957_Discovering_Language-neutral_Sub-networks_in_Multilingual_Language_Models?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbH19"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=language-specific+sub-networks"},{"title":"[2507.11230] Sparse Autoencoders Can Capture Language-Specific Concepts Across Diverse Languages","url":"https://arxiv.org/abs/2507.11230"},{"title":"Language Lives in Sparse Dimensions: Toward Interpretable and Efficient Multilingual Control for Large Language Models","url":"https://arxiv.org/html/2510.07213"}]

Based on the search results, I found highly relevant information about your query. Here's what I found:

## Paper 2510.13580: Sparse Subnetwork Enhancement for Underrepresented Languages

The paper proposes a framework for improving performance in underrepresented languages while preserving general-purpose capabilities via targeted fine-tuning of sparse, language-associated subnetworks. The paper was last updated on February 4, 2026.

### Key Findings:

The research demonstrates that language capabilities can be injected by updating less than 1% of parameters. The work shows consistent improvements over full fine-tuning, FFN-only fine-tuning, LoRA, IA3, and random subset baselines across 12 mid- and low-resource languages on three models, with full preservation of general capabilities.

### Cross-Lingual Insights:

Mechanistic analyses of weight updates and internal representations reveal asymmetric roles of FFN projections in language adaptation and improved cross-lingual alignment. Adaptation concentrates in down-projection weights of later layers and improves cross-lingual alignment more effectively than dense fine-tuning.

### Resources Released:

The authors release language neuron sets for over 100 languages together with their adaptation pipeline, enabling a cost-effective path for extending LLMs to underrepresented languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e756f10-4938-4207-a1e5-d374f22b04a0",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "357fb03b-b750-4cfa-a12b-4d07c14e027c",
  "toolUseResult": {
    "query": "\"sparse subnetwork\" cross-lingual language-specific underrepresented languages 2510.13580 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LLXooprS6VUMK7byEXTg9L",
        "content": [
          {
            "title": "[2510.13580] Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models",
            "url": "https://arxiv.org/abs/2510.13580"
          },
          {
            "title": "Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models",
            "url": "https://arxiv.org/html/2510.13580"
          },
          {
            "title": "Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"
          },
          {
            "title": "DeFT-X: Denoised Sparse Fine-Tuning for Zero-Shot Cross-Lingual Transfer",
            "url": "https://arxiv.org/html/2505.15090"
          },
          {
            "title": "Language Adaptive Cross-lingual Speech Representation Learning with Sparse Sharing Sub-networks | Request PDF",
            "url": "https://www.researchgate.net/publication/359129931_Language_Adaptive_Cross-lingual_Speech_Representation_Learning_with_Sparse_Sharing_Sub-networks"
          },
          {
            "title": "Unveiling Language Routing Isolation in Multilingual MoE Models for Interpretable Subnetwork Adaptation",
            "url": "https://arxiv.org/html/2604.03592"
          },
          {
            "title": "Discovering Language-neutral Sub-networks in Multilingual Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/372921957_Discovering_Language-neutral_Sub-networks_in_Multilingual_Language_Models?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbH19"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=language-specific+sub-networks"
          },
          {
            "title": "[2507.11230] Sparse Autoencoders Can Capture Language-Specific Concepts Across Diverse Languages",
            "url": "https://arxiv.org/abs/2507.11230"
          },
          {
            "title": "Language Lives in Sparse Dimensions: Toward Interpretable and Efficient Multilingual Control for Large Language Models",
            "url": "https://arxiv.org/html/2510.07213"
          }
        ]
      },
      "Based on the search results, I found highly relevant information about your query. Here's what I found:\n\n## Paper 2510.13580: Sparse Subnetwork Enhancement for Underrepresented Languages\n\nThe paper proposes a framework for improving performance in underrepresented languages while preserving general-purpose capabilities via targeted fine-tuning of sparse, language-associated subnetworks. The paper was last updated on February 4, 2026.\n\n### Key Findings:\n\nThe research demonstrates that language capabilities can be injected by updating less than 1% of parameters. The work shows consistent improvements over full fine-tuning, FFN-only fine-tuning, LoRA, IA3, and random subset baselines across 12 mid- and low-resource languages on three models, with full preservation of general capabilities.\n\n### Cross-Lingual Insights:\n\nMechanistic analyses of weight updates and internal representations reveal asymmetric roles of FFN projections in language adaptation and improved cross-lingual alignment. Adaptation concentrates in down-projection weights of later layers and improves cross-lingual alignment more effectively than dense fine-tuning.\n\n### Resources Released:\n\nThe authors release language neuron sets for over 100 languages together with their adaptation pipeline, enabling a cost-effective path for extending LLMs to underrepresented languages."
    ],
    "durationSeconds": 6.512373698999996
  },
  "sourceToolAssistantUUID": "2e756f10-4938-4207-a1e5-d374f22b04a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T07:45:06.865Z_

<details><summary>↩ Tool result · `toolu_01Q3F7TTgc67wPuKPamZVug4`</summary>

```text
Web search results for query: "arXiv 2510.08284 "neuron-level analysis cultural understanding" LLMs Yamamoto ICLR 2026"

Links: [{"title":"[2510.08284] Neuron-Level Analysis of Cultural Understanding in Large Language Models","url":"https://arxiv.org/abs/2510.08284"},{"title":"Neuron-Level Analysis of Cultural Understanding in Large Language Models","url":"https://arxiv.org/html/2510.08284v1"},{"title":"Neuron-Level Analysis of Cultural Understanding in Large ...","url":"https://arxiv.org/pdf/2510.08284"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"Publications - NYU Web Publishing - New York University","url":"https://wp.nyu.edu/cilvr/cilvr-group-publications/"},{"title":"Under review as a conference paper at ICLR 2026","url":"https://www.arxiv.org/pdf/2509.21798"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.10690"},{"title":"GitHub - azminewasi/Awesome-LLMs-ICLR-24: It is a comprehensive resource hub compiling all LLM papers accepted at the International Conference on Learning Representations (ICLR) in 2024. · GitHub","url":"https://github.com/azminewasi/Awesome-LLMs-ICLR-24"}]

I found the paper you're looking for. Here are the details:

## Paper Information

The paper is titled "Neuron-Level Analysis of Cultural Understanding in Large Language Models" by Taisei Yamamoto and 3 other authors. The paper was submitted on October 9, 2025.

## Research Overview

As LLMs are increasingly deployed worldwide, ensuring their fair and comprehensive cultural understanding is important. However, LLMs exhibit cultural bias and limited awareness of underrepresented cultures, while the mechanisms underlying their cultural understanding remain underexplored.

## Key Findings

The researchers conducted a neuron-level analysis to identify neurons that drive cultural behavior, introducing a gradient-based scoring method with additional filtering for precise refinement. They identify both culture-general neurons contributing to cultural understanding regardless of cultures, and culture-specific neurons tied to an individual culture.

These neurons account for less than 1% of all neurons and are concentrated in shallow to middle MLP layers. Suppressing them substantially degrades performance on cultural benchmarks (by up to 30%), while performance on general natural language understanding (NLU) benchmarks remains largely unaffected.

The paper appears to be under consideration or has been accepted to ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7b6e155-23fa-4ee2-81c5-4970b76cd966",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "b2c66829-effa-44a7-811a-41dcd7b04836",
  "toolUseResult": {
    "query": "arXiv 2510.08284 \"neuron-level analysis cultural understanding\" LLMs Yamamoto ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LRGWdBPBCvaFQJL6R1zuHp",
        "content": [
          {
            "title": "[2510.08284] Neuron-Level Analysis of Cultural Understanding in Large Language Models",
            "url": "https://arxiv.org/abs/2510.08284"
          },
          {
            "title": "Neuron-Level Analysis of Cultural Understanding in Large Language Models",
            "url": "https://arxiv.org/html/2510.08284v1"
          },
          {
            "title": "Neuron-Level Analysis of Cultural Understanding in Large ...",
            "url": "https://arxiv.org/pdf/2510.08284"
          },
          {
            "title": "ICLR 2026 Papers",
            "url": "https://iclr.cc/virtual/2026/papers.html"
          },
          {
            "title": "2026 Conference",
            "url": "https://iclr.cc/"
          },
          {
            "title": "ICLR 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"
          },
          {
            "title": "Publications - NYU Web Publishing - New York University",
            "url": "https://wp.nyu.edu/cilvr/cilvr-group-publications/"
          },
          {
            "title": "Under review as a conference paper at ICLR 2026",
            "url": "https://www.arxiv.org/pdf/2509.21798"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2604.10690"
          },
          {
            "title": "GitHub - azminewasi/Awesome-LLMs-ICLR-24: It is a comprehensive resource hub compiling all LLM papers accepted at the International Conference on Learning Representations (ICLR) in 2024. · GitHub",
            "url": "https://github.com/azminewasi/Awesome-LLMs-ICLR-24"
          }
        ]
      },
      "I found the paper you're looking for. Here are the details:\n\n## Paper Information\n\nThe paper is titled \"Neuron-Level Analysis of Cultural Understanding in Large Language Models\" by Taisei Yamamoto and 3 other authors. The paper was submitted on October 9, 2025.\n\n## Research Overview\n\nAs LLMs are increasingly deployed worldwide, ensuring their fair and comprehensive cultural understanding is important. However, LLMs exhibit cultural bias and limited awareness of underrepresented cultures, while the mechanisms underlying their cultural understanding remain underexplored.\n\n## Key Findings\n\nThe researchers conducted a neuron-level analysis to identify neurons that drive cultural behavior, introducing a gradient-based scoring method with additional filtering for precise refinement. They identify both culture-general neurons contributing to cultural understanding regardless of cultures, and culture-specific neurons tied to an individual culture.\n\nThese neurons account for less than 1% of all neurons and are concentrated in shallow to middle MLP layers. Suppressing them substantially degrades performance on cultural benchmarks (by up to 30%), while performance on general natural language understanding (NLU) benchmarks remains largely unaffected.\n\nThe paper appears to be under consideration or has been accepted to ICLR 2026."
    ],
    "durationSeconds": 8.045112722000006
  },
  "sourceToolAssistantUUID": "a7b6e155-23fa-4ee2-81c5-4970b76cd966",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T07:45:09.161Z_

<details><summary>↩ Tool result · `toolu_01K9pQVBPhBiASybJBWPQXi8`</summary>

```text
Web search results for query: "cultural knowledge preservation multilingual fine-tuning training method LoRA freezing 2025 2026"

Links: [{"title":"Final Report - Fine Tuning Methods for Low-resource Languages","url":"https://arxiv.org/html/2510.04139v1"},{"title":"Published in Transactions on Machine Learning Research (11/2025)","url":"https://openreview.net/pdf?id=oapsbIO1Bd"},{"title":"SC-LoRA: Balancing Efficient Fine-tuning and Knowledge Preservation via Subspace-Constrained LoRA","url":"https://arxiv.org/html/2505.23724v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf"},{"title":"What is Lora Fine Tuning? The Definitive Guide","url":"https://www.truefoundry.com/blog/lora-fine-tuning"},{"title":"Challenges in Adapting Multilingual LLMs to Low- ...","url":"https://aclanthology.org/2025.chipsal-1.22.pdf"},{"title":"META-LORA: DATA-EFFICIENT MULTI-TASK FINE-TUNING FOR LARGE LANGUAGE MODELS","url":"https://arxiv.org/pdf/2510.11598"},{"title":"Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=s7DkcgpRxL"},{"title":"Fine-Tuning Transformers Efficiently: A Survey on LoRA and Its Impact[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202502.1637/v1"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=12350&show=50"}]

Based on the web search results, here's what I found on cultural knowledge preservation with multilingual fine-tuning using LoRA and freezing methods from 2025-2026:

## Key Findings

**LoRA and Knowledge Preservation:**
LoRA freezes most of a model's parameters to efficiently fine-tune models for specific languages, which is particularly relevant for cultural knowledge preservation. Since LoRA keeps the base model frozen, it avoids "catastrophic forgetting," where full fine-tuning may overwrite useful general-purpose knowledge, making LoRA particularly useful when adapting large models to niche domains while preserving their original language understanding.

**Recent Advances in Knowledge Preservation:**
A notable 2025 approach is Subspace-Constrained LoRA (SC-LoRA), a novel LoRA initialization framework engineered to navigate the trade-off between efficient fine-tuning and knowledge preservation.

**Multilingual Applications:**
This hybrid technique is particularly useful in multilingual NLP, where different adapters can be used for different languages while LoRA fine-tunes shared knowledge. Additionally, by improving these suggestions, Gemma 2 could increasingly serve diverse cultural contexts and preserve global language heritage.

**Data-Efficient Multilingual Training:**
META-LORA demonstrates competitive performance in both multi-task learning and multilingual learning scenarios while requiring significantly less task-specific data.

These research directions show active development in preserving cultural and linguistic knowledge through parameter-efficient fine-tuning methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50ba0803-82ec-42a1-bcd4-93ee6406b1d7",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "7d100264-9abc-4653-b53b-16234c54c75a",
  "toolUseResult": {
    "query": "cultural knowledge preservation multilingual fine-tuning training method LoRA freezing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VCCxRrg6iJ8EYqdNGXzgTt",
        "content": [
          {
            "title": "Final Report - Fine Tuning Methods for Low-resource Languages",
            "url": "https://arxiv.org/html/2510.04139v1"
          },
          {
            "title": "Published in Transactions on Machine Learning Research (11/2025)",
            "url": "https://openreview.net/pdf?id=oapsbIO1Bd"
          },
          {
            "title": "SC-LoRA: Balancing Efficient Fine-tuning and Knowledge Preservation via Subspace-Constrained LoRA",
            "url": "https://arxiv.org/html/2505.23724v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf"
          },
          {
            "title": "What is Lora Fine Tuning? The Definitive Guide",
            "url": "https://www.truefoundry.com/blog/lora-fine-tuning"
          },
          {
            "title": "Challenges in Adapting Multilingual LLMs to Low- ...",
            "url": "https://aclanthology.org/2025.chipsal-1.22.pdf"
          },
          {
            "title": "META-LORA: DATA-EFFICIENT MULTI-TASK FINE-TUNING FOR LARGE LANGUAGE MODELS",
            "url": "https://arxiv.org/pdf/2510.11598"
          },
          {
            "title": "Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=s7DkcgpRxL"
          },
          {
            "title": "Fine-Tuning Transformers Efficiently: A Survey on LoRA and Its Impact[v1] | Preprints.org",
            "url": "https://www.preprints.org/manuscript/202502.1637/v1"
          },
          {
            "title": "Computer Science May 2025",
            "url": "https://arxiv.org/list/cs/2025-05?skip=12350&show=50"
          }
        ]
      },
      "Based on the web search results, here's what I found on cultural knowledge preservation with multilingual fine-tuning using LoRA and freezing methods from 2025-2026:\n\n## Key Findings\n\n**LoRA and Knowledge Preservation:**\nLoRA freezes most of a model's parameters to efficiently fine-tune models for specific languages, which is particularly relevant for cultural knowledge preservation. Since LoRA keeps the base model frozen, it avoids \"catastrophic forgetting,\" where full fine-tuning may overwrite useful general-purpose knowledge, making LoRA particularly useful when adapting large models to niche domains while preserving their original language understanding.\n\n**Recent Advances in Knowledge Preservation:**\nA notable 2025 approach is Subspace-Constrained LoRA (SC-LoRA), a novel LoRA initialization framework engineered to navigate the trade-off between efficient fine-tuning and knowledge preservation.\n\n**Multilingual Applications:**\nThis hybrid technique is particularly useful in multilingual NLP, where different adapters can be used for different languages while LoRA fine-tunes shared knowledge. Additionally, by improving these suggestions, Gemma 2 could increasingly serve diverse cultural contexts and preserve global language heritage.\n\n**Data-Efficient Multilingual Training:**\nMETA-LORA demonstrates competitive performance in both multi-task learning and multilingual learning scenarios while requiring significantly less task-specific data.\n\nThese research directions show active development in preserving cultural and linguistic knowledge through parameter-efficient fine-tuning methods."
    ],
    "durationSeconds": 9.759016851
  },
  "sourceToolAssistantUUID": "50ba0803-82ec-42a1-bcd4-93ee6406b1d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-10T07:45:18.272Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now look more carefully at competing papers:

1. **Sparse Subnetwork Enhancement for Underrepresented Languages** (arXiv:2510.13580) - This is a potentially important competitor that I need to investigate more carefully. It proposes targeted fine-tuning of sparse, language-associated subnetworks for underrepresented languages. The adaptation concentrates in down-projection weights of later layers, which is relevant to CLS-LoRA's layer partition hypothesis. However, it focuses on underrepresented language performance improvement, not cultural preservation per se.


2. **GRASP LoRA** (arXiv:2601.06702) - This one targets sparsity in cross-lingual LoRA but doesn't address cultural preservation directly. I should pull the abstract for the first paper to determine if it's truly a direct competitor, and I also need to verify whether those ICLR 2026 papers actually got accepted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d100264-9abc-4653-b53b-16234c54c75a",
  "isSidechain": false,
  "requestId": "req_011CatWsadZLJo1BTviw2Nqd",
  "type": "assistant",
  "uuid": "2b0c26ce-baea-4efe-988d-3d889ffa630a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PVkGFB4CeADmeAgF2QsJsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5005,
      "cache_read_input_tokens": 38631,
      "output_tokens": 504,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 504,
          "cache_read_input_tokens": 38631,
          "cache_creation_input_tokens": 5005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5005
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

_source line 30 · 2026-05-10T07:45:18.348Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015hvdYFekmG6VvoL6FSCrF8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.13580",
  "prompt": "What is this paper about? Does it address cultural knowledge preservation during cross-lingual fine-tuning? Does it use layer-selective approaches? What are the key contributions vs CLS-LoRA which freezes cultural-knowledge layers during cross-lingual instruction fine-tuning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b0c26ce-baea-4efe-988d-3d889ffa630a",
  "isSidechain": false,
  "requestId": "req_011CatWsadZLJo1BTviw2Nqd",
  "type": "assistant",
  "uuid": "40f80bde-316b-434e-9864-32c3d0fb835a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PVkGFB4CeADmeAgF2QsJsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5005,
      "cache_read_input_tokens": 38631,
      "output_tokens": 504,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 504,
          "cache_read_input_tokens": 38631,
          "cache_creation_input_tokens": 5005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5005
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

_source line 31 · 2026-05-10T07:45:19.024Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017B5DyXrCEbgzXJDZcmMj5n`</summary>

```json
{
  "url": "https://openreview.net/forum?id=8DBHkEe0sm",
  "prompt": "What is the review status of this paper? Has it been accepted at ICLR 2026? What are the reviewer scores and decisions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40f80bde-316b-434e-9864-32c3d0fb835a",
  "isSidechain": false,
  "requestId": "req_011CatWsadZLJo1BTviw2Nqd",
  "type": "assistant",
  "uuid": "60cab6ed-46c0-4a99-873f-2b4cae694867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PVkGFB4CeADmeAgF2QsJsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5005,
      "cache_read_input_tokens": 38631,
      "output_tokens": 504,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 504,
          "cache_read_input_tokens": 38631,
          "cache_creation_input_tokens": 5005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5005
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "60cab6ed-46c0-4a99-873f-2b4cae694867",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Cultural preservation in cross-lingual LoRA fine-tuning",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Tool result

_source line 34 · 2026-05-10T07:45:21.657Z_

<details><summary>↩ Tool result · `toolu_017B5DyXrCEbgzXJDZcmMj5n`</summary>

```text
Based on the content provided, I cannot determine the review status or acceptance decision for this paper. The webpage displays the paper's abstract and metadata from OpenReview, but it does not include information about reviewer scores, review decisions, or acceptance status at ICLR 2026.

The page shows the paper was "Submitted to ICLR 2026" with a submission date of "18 Sept 2025 (modified: 11 Feb 2026)," but no decision information is visible in the provided content. To find this information, you would need to access the full paper page on OpenReview, which may contain additional sections showing review status and decisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60cab6ed-46c0-4a99-873f-2b4cae694867",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "f766c68d-2f77-4abf-bb0a-c57a64d9af88",
  "toolUseResult": {
    "bytes": 69049,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the content provided, I cannot determine the review status or acceptance decision for this paper. The webpage displays the paper's abstract and metadata from OpenReview, but it does not include information about reviewer scores, review decisions, or acceptance status at ICLR 2026.\n\nThe page shows the paper was \"Submitted to ICLR 2026\" with a submission date of \"18 Sept 2025 (modified: 11 Feb 2026),\" but no decision information is visible in the provided content. To find this information, you would need to access the full paper page on OpenReview, which may contain additional sections showing review status and decisions.",
    "durationMs": 2629,
    "url": "https://openreview.net/forum?id=8DBHkEe0sm"
  },
  "sourceToolAssistantUUID": "60cab6ed-46c0-4a99-873f-2b4cae694867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T07:45:23.450Z_

<details><summary>↩ Tool result · `toolu_015hvdYFekmG6VvoL6FSCrF8`</summary>

```text
# Summary of Paper arXiv:2510.13580

## Main Topic
This paper addresses performance disparities in large language models across languages by proposing sparse subnetwork fine-tuning for underrepresented languages. The approach identifies "language-relevant neurons using Language Activation Probability Entropy (LAPE)" and fine-tunes only those weights while updating "only 0.2-1% of model parameters."

## Cultural Knowledge Preservation
The abstract does not explicitly address cultural knowledge preservation during cross-lingual fine-tuning. It focuses on preventing "catastrophic forgetting" of general-purpose capabilities but doesn't discuss preservation of cultural or linguistic-specific knowledge.

## Layer-Selective Approaches
Yes, the paper employs layer-selective strategies. It mentions "FFN-only fine-tuning" as a baseline comparison and discusses "asymmetric roles of FFN projections in language adaptation," indicating targeted attention to specific neural components rather than full-model updates.

## Comparison to CLS-LoRA
The provided content does not mention CLS-LoRA or any approach that specifically freezes cultural-knowledge layers. The paper compares against "LoRA, IA³, and random-subset baselines" but makes no reference to CLS-LoRA methodology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40f80bde-316b-434e-9864-32c3d0fb835a",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "7031b590-ee33-4adf-8864-0708169cd0ea",
  "toolUseResult": {
    "bytes": 47095,
    "code": 200,
    "codeText": "OK",
    "result": "# Summary of Paper arXiv:2510.13580\n\n## Main Topic\nThis paper addresses performance disparities in large language models across languages by proposing sparse subnetwork fine-tuning for underrepresented languages. The approach identifies \"language-relevant neurons using Language Activation Probability Entropy (LAPE)\" and fine-tunes only those weights while updating \"only 0.2-1% of model parameters.\"\n\n## Cultural Knowledge Preservation\nThe abstract does not explicitly address cultural knowledge preservation during cross-lingual fine-tuning. It focuses on preventing \"catastrophic forgetting\" of general-purpose capabilities but doesn't discuss preservation of cultural or linguistic-specific knowledge.\n\n## Layer-Selective Approaches\nYes, the paper employs layer-selective strategies. It mentions \"FFN-only fine-tuning\" as a baseline comparison and discusses \"asymmetric roles of FFN projections in language adaptation,\" indicating targeted attention to specific neural components rather than full-model updates.\n\n## Comparison to CLS-LoRA\nThe provided content does not mention CLS-LoRA or any approach that specifically freezes cultural-knowledge layers. The paper compares against \"LoRA, IA³, and random-subset baselines\" but makes no reference to CLS-LoRA methodology.",
    "durationMs": 5097,
    "url": "https://arxiv.org/abs/2510.13580"
  },
  "sourceToolAssistantUUID": "40f80bde-316b-434e-9864-32c3d0fb835a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-10T07:45:23.453Z_

```json
{
  "parentUuid": "7031b590-ee33-4adf-8864-0708169cd0ea",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1bee3a52-2fe0-4937-95fc-ec5e31f44a27",
  "timestamp": "2026-05-10T07:45:23.453Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-10T07:45:28.627Z_

<details><summary>Logged reasoning block</summary>

```text
The OpenReview page didn't give me clear information about whether arXiv:2510.26024 was accepted at ICLR 2026 or not. Let me check the ICLR 2026 papers list directly and also check on the author's publication page.

Also, the sparse subnetwork paper (2510.13580) seems to be focused on language performance improvement for underrepresented languages, not cultural knowledge preservation, so it's a different objective. However, it's worth noting as a related work.

Let me now check:
1. ICLR 2026 accepted papers to verify status of arXiv:2510.26024 and arXiv:2510.08284


2. Any new training-time cultural preservation methods from early 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bee3a52-2fe0-4937-95fc-ec5e31f44a27",
  "isSidechain": false,
  "requestId": "req_011CatWtdkrYonudVgDvv9fu",
  "type": "assistant",
  "uuid": "a0b89d5e-59e9-4939-aac9-10ab4ce8a98a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YTKFiuRz4dNjdtjeLHtivp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 174,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 43636,
      "output_tokens": 402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 174,
          "output_tokens": 402,
          "cache_read_input_tokens": 43636,
          "cache_creation_input_tokens": 920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 920
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

_source line 38 · 2026-05-10T07:45:30.362Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019mwpZYWFMNKXqthnMc9F84`</summary>

```json
{
  "url": "https://iclr.cc/virtual/2026/papers.html",
  "prompt": "List any papers related to: cultural knowledge, multilingual LLMs, cross-lingual alignment, cultural erasure, neuron analysis of culture. Specifically check if \"Neuron-Level Analysis of Cultural Understanding\" by Yamamoto is listed, and if \"Rethinking Cross-lingual Alignment\" by HyoJung Han is listed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0b89d5e-59e9-4939-aac9-10ab4ce8a98a",
  "isSidechain": false,
  "requestId": "req_011CatWtdkrYonudVgDvv9fu",
  "type": "assistant",
  "uuid": "81f31a89-e3b4-46e6-a06e-d162b93cf887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YTKFiuRz4dNjdtjeLHtivp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 174,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 43636,
      "output_tokens": 402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 174,
          "output_tokens": 402,
          "cache_read_input_tokens": 43636,
          "cache_creation_input_tokens": 920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 920
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

_source line 39 · 2026-05-10T07:45:30.678Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U8DdkKAcLBy5VqKRRwxoRa`</summary>

```json
{
  "query": "CulturalBench ACL 2025 dataset training evaluation split availability download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81f31a89-e3b4-46e6-a06e-d162b93cf887",
  "isSidechain": false,
  "requestId": "req_011CatWtdkrYonudVgDvv9fu",
  "type": "assistant",
  "uuid": "9409cb7b-957c-4587-95c7-133945f330f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YTKFiuRz4dNjdtjeLHtivp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 174,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 43636,
      "output_tokens": 402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 174,
          "output_tokens": 402,
          "cache_read_input_tokens": 43636,
          "cache_creation_input_tokens": 920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 920
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

_source line 40 · 2026-05-10T07:45:36.663Z_

<details><summary>↩ Tool result · `toolu_019mwpZYWFMNKXqthnMc9F84`</summary>

```text
Based on the web page content provided, I cannot identify any papers related to cultural knowledge, multilingual LLMs, cross-lingual alignment, cultural erasure, or neuron analysis of culture.

The page shows navigation menus and general conference structure for ICLR 2026, but does not display actual paper titles, authors, or abstracts. The content includes links to sections like "[Papers](/virtual/2026/papers.html)" and "[Orals](/virtual/2026/events/oral)," but the actual paper listings are not included in the provided text.

Therefore, I cannot confirm whether "Neuron-Level Analysis of Cultural Understanding" by Yamamoto or "Rethinking Cross-lingual Alignment" by HyoJung Han appear in the ICLR 2026 proceedings based on this content alone.

To find these papers, you would need to visit the Papers section directly through the navigation links provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81f31a89-e3b4-46e6-a06e-d162b93cf887",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "5bb5ffed-ae68-4b62-8125-0075c5e23281",
  "toolUseResult": {
    "bytes": 757014,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot identify any papers related to cultural knowledge, multilingual LLMs, cross-lingual alignment, cultural erasure, or neuron analysis of culture.\n\nThe page shows navigation menus and general conference structure for ICLR 2026, but does not display actual paper titles, authors, or abstracts. The content includes links to sections like \"[Papers](/virtual/2026/papers.html)\" and \"[Orals](/virtual/2026/events/oral),\" but the actual paper listings are not included in the provided text.\n\nTherefore, I cannot confirm whether \"Neuron-Level Analysis of Cultural Understanding\" by Yamamoto or \"Rethinking Cross-lingual Alignment\" by HyoJung Han appear in the ICLR 2026 proceedings based on this content alone.\n\nTo find these papers, you would need to visit the Papers section directly through the navigation links provided.",
    "durationMs": 6298,
    "url": "https://iclr.cc/virtual/2026/papers.html"
  },
  "sourceToolAssistantUUID": "81f31a89-e3b4-46e6-a06e-d162b93cf887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T07:45:38.057Z_

<details><summary>↩ Tool result · `toolu_01U8DdkKAcLBy5VqKRRwxoRa`</summary>

```text
Web search results for query: "CulturalBench ACL 2025 dataset training evaluation split availability download"

Links: [{"title":"CulturalBench: A Robust, Diverse and Challenging Benchmark for Measuring LMs’ Cultural Knowledge Through Human-AI Red-Teaming - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1247/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Improving Model Evaluation using SMART Filtering of Benchmark Datasets - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.235/"},{"title":"CultureBench: Cultural Competence Benchmarks","url":"https://www.emergentmind.com/topics/culturebench"},{"title":"BI-Bench : A Comprehensive Benchmark Dataset and Unsupervised Evaluation for BI Systems - ACL Anthology","url":"https://aclanthology.org/2025.acl-industry.90/"},{"title":"Twenty-two papers by CSE researchers at ACL 2025","url":"https://cse.engin.umich.edu/stories/twenty-two-papers-by-cse-researchers-at-acl-2025"},{"title":"CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark by Human-AI CulturalTeaming","url":"https://arxiv.org/html/2410.02677v2"},{"title":"CulturalBench: a Robust, Diverse and Challenging Benchmark on Measuring the (Lack of) Cultural Knowledge of LLMs","url":"https://arxiv.org/html/2410.02677v1"},{"title":"MASSW: A New Dataset and Benchmark Tasks for AI-Assisted Scientific Workflows - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.127/"},{"title":"Multilingual Physical Reasoning Datasets: Shared Task for the MRL Workshop at EMNLP 2025 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/multilingual-physical-reasoning-datasets-shared-task-mrl-workshop-emnlp-2025"}]

Based on the search results, I found information about CulturalBench and its publication at ACL 2025:

## CulturalBench at ACL 2025

CulturalBench: A Robust, Diverse and Challenging Benchmark for Measuring LMs' Cultural Knowledge Through Human-AI Red-Teaming was published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) in Vienna, Austria, pages 25663–25701.

## Dataset Evaluation Splits

The dataset includes two evaluation setups: (1) CulturalBench-Easy with Multiple choice format; (2) CulturalBench-Hard with True/False format. In the hard version, each question is transformed into four binary true/false questions, requiring models to evaluate each option separately.

## Data Collection and Annotation

The researchers constructed CulturalBench using methods inspired by Human-AI Red-Teaming. The annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training.

## Availability and Download

The official ACL paper is available at the ACL Anthology: https://aclanthology.org/2025.acl-long.1247/

The paper's HTML version is also available on arXiv, which includes detailed methodology and results information.

However, the search results do not contain specific information about dataset download links or explicit details about training/evaluation/test split percentages. For information about downloading the actual dataset or its specific split breakdown, you may need to check the paper's supplementary materials section, the authors' GitHub repository, or contact the authors directly through the ACL paper page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9409cb7b-957c-4587-95c7-133945f330f8",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "6e9d029f-7c3d-4b19-b941-efdf1b550aa7",
  "toolUseResult": {
    "query": "CulturalBench ACL 2025 dataset training evaluation split availability download",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TGoJjFPyEXbJcWZYmBKbyf",
        "content": [
          {
            "title": "CulturalBench: A Robust, Diverse and Challenging Benchmark for Measuring LMs’ Cultural Knowledge Through Human-AI Red-Teaming - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.1247/"
          },
          {
            "title": "Accepted Main Conference Papers - ACL 2025",
            "url": "https://2025.aclweb.org/program/main_papers/"
          },
          {
            "title": "Improving Model Evaluation using SMART Filtering of Benchmark Datasets - ACL Anthology",
            "url": "https://aclanthology.org/2025.naacl-long.235/"
          },
          {
            "title": "CultureBench: Cultural Competence Benchmarks",
            "url": "https://www.emergentmind.com/topics/culturebench"
          },
          {
            "title": "BI-Bench : A Comprehensive Benchmark Dataset and Unsupervised Evaluation for BI Systems - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-industry.90/"
          },
          {
            "title": "Twenty-two papers by CSE researchers at ACL 2025",
            "url": "https://cse.engin.umich.edu/stories/twenty-two-papers-by-cse-researchers-at-acl-2025"
          },
          {
            "title": "CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark by Human-AI CulturalTeaming",
            "url": "https://arxiv.org/html/2410.02677v2"
          },
          {
            "title": "CulturalBench: a Robust, Diverse and Challenging Benchmark on Measuring the (Lack of) Cultural Knowledge of LLMs",
            "url": "https://arxiv.org/html/2410.02677v1"
          },
          {
            "title": "MASSW: A New Dataset and Benchmark Tasks for AI-Assisted Scientific Workflows - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-naacl.127/"
          },
          {
            "title": "Multilingual Physical Reasoning Datasets: Shared Task for the MRL Workshop at EMNLP 2025 | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/multilingual-physical-reasoning-datasets-shared-task-mrl-workshop-emnlp-2025"
          }
        ]
      },
      "Based on the search results, I found information about CulturalBench and its publication at ACL 2025:\n\n## CulturalBench at ACL 2025\n\nCulturalBench: A Robust, Diverse and Challenging Benchmark for Measuring LMs' Cultural Knowledge Through Human-AI Red-Teaming was published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) in Vienna, Austria, pages 25663–25701.\n\n## Dataset Evaluation Splits\n\nThe dataset includes two evaluation setups: (1) CulturalBench-Easy with Multiple choice format; (2) CulturalBench-Hard with True/False format. In the hard version, each question is transformed into four binary true/false questions, requiring models to evaluate each option separately.\n\n## Data Collection and Annotation\n\nThe researchers constructed CulturalBench using methods inspired by Human-AI Red-Teaming. The annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training.\n\n## Availability and Download\n\nThe official ACL paper is available at the ACL Anthology: https://aclanthology.org/2025.acl-long.1247/\n\nThe paper's HTML version is also available on arXiv, which includes detailed methodology and results information.\n\nHowever, the search results do not contain specific information about dataset download links or explicit details about training/evaluation/test split percentages. For information about downloading the actual dataset or its specific split breakdown, you may need to check the paper's supplementary materials section, the authors' GitHub repository, or contact the authors directly through the ACL paper page."
    ],
    "durationSeconds": 7.376681171999997
  },
  "sourceToolAssistantUUID": "9409cb7b-957c-4587-95c7-133945f330f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T07:45:45.272Z_

<details><summary>Logged reasoning block</summary>

```text
This is significant! The CulturalBench dataset was built using OpenAI APIs for annotation, which means the annotation platform's terms of service disallowed the collected data to be used for training. This could directly conflict with the paper's claim that "CulturalBench (ACL 2025; 1,696 human-verified questions across 45 global regions), which is publicly available for training use."

Let me investigate this more carefully - if the OpenAI API was used in the construction of CulturalBench and the platform's terms disallow training use, then using CulturalBench for probe training in Stage 2 might violate usage terms.


I need to double-check whether arXiv:2510.26024 was actually accepted at ICLR 2026, and also determine if the GRASP LoRA paper represents a direct competitor to this work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e9d029f-7c3d-4b19-b941-efdf1b550aa7",
  "isSidechain": false,
  "requestId": "req_011CatWuiD2Sderq7HCChPvL",
  "type": "assistant",
  "uuid": "245d314a-b509-4c7a-90d3-8bf3bd8ec992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014MayqCzUvTPjPRNHBgzp1g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1808,
      "cache_read_input_tokens": 44556,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 414,
          "cache_read_input_tokens": 44556,
          "cache_creation_input_tokens": 1808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1808
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

_source line 43 · 2026-05-10T07:45:45.384Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018kE2hAhbyE3vnCnhGpUC1E`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.02677",
  "prompt": "What are the usage terms for CulturalBench? Can it be used for training? Is there a license that allows or prohibits training use? Does it mention OpenAI API terms of service restrictions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "245d314a-b509-4c7a-90d3-8bf3bd8ec992",
  "isSidechain": false,
  "requestId": "req_011CatWuiD2Sderq7HCChPvL",
  "type": "assistant",
  "uuid": "1cf94eaa-8033-4022-a2d0-154ab6cc5884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014MayqCzUvTPjPRNHBgzp1g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1808,
      "cache_read_input_tokens": 44556,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 414,
          "cache_read_input_tokens": 44556,
          "cache_creation_input_tokens": 1808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1808
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

_source line 44 · 2026-05-10T07:45:46.024Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UQ1PZR6W6xUcg3QBZdvbj5`</summary>

```json
{
  "query": "GRASP LoRA 2601.06702 cross-lingual transfer cultural knowledge GRPO sparsity 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cf94eaa-8033-4022-a2d0-154ab6cc5884",
  "isSidechain": false,
  "requestId": "req_011CatWuiD2Sderq7HCChPvL",
  "type": "assistant",
  "uuid": "e52d3fa6-36be-41ff-9ca2-20f16de4bfac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014MayqCzUvTPjPRNHBgzp1g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1808,
      "cache_read_input_tokens": 44556,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 414,
          "cache_read_input_tokens": 44556,
          "cache_creation_input_tokens": 1808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1808
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

_source line 45 · 2026-05-10T07:45:49.083Z_

<details><summary>↩ Tool result · `toolu_018kE2hAhbyE3vnCnhGpUC1E`</summary>

```text
# CulturalBench Usage Terms

Based on the webpage content provided, here's what is disclosed about usage:

**License Information:**
The paper is released under a Creative Commons Attribution 4.0 (CC BY 4.0) license, indicated by the license icon displayed on the page.

**What's Not Specified:**
The webpage does not contain explicit information about:
- Whether the benchmark can be used for training language models
- Specific restrictions on training use
- References to OpenAI API terms of service restrictions

The CC BY 4.0 license generally permits broad use including commercial and derivative works with attribution, but the specific application to training scenarios would require reviewing the full paper or dataset documentation not included in this excerpt.

**Recommendation:**
To determine permissible uses for training, you would need to consult the complete paper (available as PDF or HTML) or contact the authors directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cf94eaa-8033-4022-a2d0-154ab6cc5884",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "df2b08bf-21c0-4412-a413-7618f5e21ac1",
  "toolUseResult": {
    "bytes": 48213,
    "code": 200,
    "codeText": "OK",
    "result": "# CulturalBench Usage Terms\n\nBased on the webpage content provided, here's what is disclosed about usage:\n\n**License Information:**\nThe paper is released under a Creative Commons Attribution 4.0 (CC BY 4.0) license, indicated by the license icon displayed on the page.\n\n**What's Not Specified:**\nThe webpage does not contain explicit information about:\n- Whether the benchmark can be used for training language models\n- Specific restrictions on training use\n- References to OpenAI API terms of service restrictions\n\nThe CC BY 4.0 license generally permits broad use including commercial and derivative works with attribution, but the specific application to training scenarios would require reviewing the full paper or dataset documentation not included in this excerpt.\n\n**Recommendation:**\nTo determine permissible uses for training, you would need to consult the complete paper (available as PDF or HTML) or contact the authors directly.",
    "durationMs": 3695,
    "url": "https://arxiv.org/abs/2410.02677"
  },
  "sourceToolAssistantUUID": "1cf94eaa-8033-4022-a2d0-154ab6cc5884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-10T07:45:52.706Z_

<details><summary>↩ Tool result · `toolu_01UQ1PZR6W6xUcg3QBZdvbj5`</summary>

```text
Web search results for query: "GRASP LoRA 2601.06702 cross-lingual transfer cultural knowledge GRPO sparsity 2026"

Links: [{"title":"[2601.06702] GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer","url":"https://arxiv.org/abs/2601.06702"},{"title":"GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer","url":"https://arxiv.org/html/2601.06702"},{"title":"GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer","url":"https://www.arxiv.org/pdf/2601.06702"},{"title":"[2506.01675] Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon","url":"https://arxiv.org/abs/2506.01675"},{"title":"Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon","url":"https://arxiv.org/html/2506.01675v1"},{"title":"Cross-Lingual Transfer of Cultural Knowledge","url":"https://arxiv.org/pdf/2506.01675"},{"title":"Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon - ACL Anthology","url":"https://aclanthology.org/2025.acl-short.13/"},{"title":"[2601.04036] Analyzing and Improving Cross-lingual Knowledge Transfer for Machine Translation","url":"https://arxiv.org/abs/2601.04036"},{"title":"CultureLLM: Incorporating Cultural Differences into Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf"},{"title":"[2404.04042] Teaching Llama a New Language Through Cross-Lingual Knowledge Transfer","url":"https://arxiv.org/abs/2404.04042"}]

Based on the search results, I found information about the GRASP LoRA paper (2601.06702) and a related paper on cross-lingual transfer of cultural knowledge:

## GRASP LoRA (2601.06702)

GRASP LoRA (GRPO Guided Adapter Sparsity Policy) treats global sparsity as a learnable control variable. A GRPO controller interleaves with training, periodically probing candidate prune ratios on a small micro development set and updating a single global prune ratio online from its reward signal.

On cross lingual transfer from English into Arabic and Chinese, including XL-Sum summarization and MLQA extractive question answering with Llama 3 8B, GRASP LoRA improves semantic faithfulness, content coverage, and answer quality over strong baselines, reduces end to end runtime by multiple times relative to grid search, and lowers reliance on large development sets.

## Cross-Lingual Transfer of Cultural Knowledge

A related research paper on cultural knowledge transfer was also identified. A study of four non-Anglophonic cultures observed bidirectional cultural transfer between English and other high-resource languages, while low-resource languages primarily transfer knowledge to English with limited reverse flow. The research proposes a frequency-based hypothesis: cultural knowledge appearing more frequently in the pretraining data transfers more easily.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e52d3fa6-36be-41ff-9ca2-20f16de4bfac",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "d31df74c-0c2f-40f8-8b8f-12ea6efee617",
  "toolUseResult": {
    "query": "GRASP LoRA 2601.06702 cross-lingual transfer cultural knowledge GRPO sparsity 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011iLgiGR1oX3ZV8D8bXm2Fr",
        "content": [
          {
            "title": "[2601.06702] GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer",
            "url": "https://arxiv.org/abs/2601.06702"
          },
          {
            "title": "GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer",
            "url": "https://arxiv.org/html/2601.06702"
          },
          {
            "title": "GRASP LoRA: GRPO Guided Adapter Sparsity Policy for Cross Lingual Transfer",
            "url": "https://www.arxiv.org/pdf/2601.06702"
          },
          {
            "title": "[2506.01675] Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon",
            "url": "https://arxiv.org/abs/2506.01675"
          },
          {
            "title": "Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon",
            "url": "https://arxiv.org/html/2506.01675v1"
          },
          {
            "title": "Cross-Lingual Transfer of Cultural Knowledge",
            "url": "https://arxiv.org/pdf/2506.01675"
          },
          {
            "title": "Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-short.13/"
          },
          {
            "title": "[2601.04036] Analyzing and Improving Cross-lingual Knowledge Transfer for Machine Translation",
            "url": "https://arxiv.org/abs/2601.04036"
          },
          {
            "title": "CultureLLM: Incorporating Cultural Differences into Large Language Models",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf"
          },
          {
            "title": "[2404.04042] Teaching Llama a New Language Through Cross-Lingual Knowledge Transfer",
            "url": "https://arxiv.org/abs/2404.04042"
          }
        ]
      },
      "Based on the search results, I found information about the GRASP LoRA paper (2601.06702) and a related paper on cross-lingual transfer of cultural knowledge:\n\n## GRASP LoRA (2601.06702)\n\nGRASP LoRA (GRPO Guided Adapter Sparsity Policy) treats global sparsity as a learnable control variable. A GRPO controller interleaves with training, periodically probing candidate prune ratios on a small micro development set and updating a single global prune ratio online from its reward signal.\n\nOn cross lingual transfer from English into Arabic and Chinese, including XL-Sum summarization and MLQA extractive question answering with Llama 3 8B, GRASP LoRA improves semantic faithfulness, content coverage, and answer quality over strong baselines, reduces end to end runtime by multiple times relative to grid search, and lowers reliance on large development sets.\n\n## Cross-Lingual Transfer of Cultural Knowledge\n\nA related research paper on cultural knowledge transfer was also identified. A study of four non-Anglophonic cultures observed bidirectional cultural transfer between English and other high-resource languages, while low-resource languages primarily transfer knowledge to English with limited reverse flow. The research proposes a frequency-based hypothesis: cultural knowledge appearing more frequently in the pretraining data transfers more easily."
    ],
    "durationSeconds": 6.679385733999996
  },
  "sourceToolAssistantUUID": "e52d3fa6-36be-41ff-9ca2-20f16de4bfac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d31df74c-0c2f-40f8-8b8f-12ea6efee617",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Cultural preservation in cross-lingual LoRA fine-tuning",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Assistant

_source line 49 · 2026-05-10T07:46:01.447Z_

<details><summary>Logged reasoning block</summary>

```text
Okay. Let me now search for more recent potential competing work that the paper might have missed in early 2026. I want to look specifically for:
1. Any training-time methods for cultural preservation in multilingual models
2. Any layer-selective fine-tuning approaches for multilingual/cultural NLP

I'm noticing that GRASP LoRA doesn't seem to directly compete with CLS-LoRA - it's focused on cross-lingual transfer for machine translation and QA, not cultural preservation.

Let me check the CulturalBench dataset more carefully about training use. 

There's a discrepancy I need to resolve - the paper claims CulturalBench is "publicly available for training use" but the annotation platform's terms appear to restrict training data usage. I should also verify whether any new 2026 work actually tackles cultural preservation as a training-time objective, since that's what would directly compete with this approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d31df74c-0c2f-40f8-8b8f-12ea6efee617",
  "isSidechain": false,
  "requestId": "req_011CatWvnqbwKDRFFNLz3bhh",
  "type": "assistant",
  "uuid": "7459442d-4475-48c2-85ce-e19b7ea318a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FU49YssmX3WZVih51ER63c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 46364,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1500,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 403,
          "cache_read_input_tokens": 46364,
          "cache_creation_input_tokens": 1500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1500
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

_source line 50 · 2026-05-10T07:46:01.662Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CpRkC2KVYnjSvXCfbiGuGp`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.02677v2",
  "prompt": "What are the dataset usage terms? Can CulturalBench be used for training models? Is there a GitHub link or HuggingFace link for the dataset? What does the paper say about permitted uses?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7459442d-4475-48c2-85ce-e19b7ea318a4",
  "isSidechain": false,
  "requestId": "req_011CatWvnqbwKDRFFNLz3bhh",
  "type": "assistant",
  "uuid": "66d34b6a-6570-4236-a3e6-686f8d12a527",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FU49YssmX3WZVih51ER63c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 46364,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1500,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 403,
          "cache_read_input_tokens": 46364,
          "cache_creation_input_tokens": 1500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1500
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

_source line 51 · 2026-05-10T07:46:02.018Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S2k2oGiqug3ir3huydwUWj`</summary>

```json
{
  "query": "training-time cultural preservation multilingual LLM instruction fine-tuning prevent cultural knowledge loss 2026 arxiv method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66d34b6a-6570-4236-a3e6-686f8d12a527",
  "isSidechain": false,
  "requestId": "req_011CatWvnqbwKDRFFNLz3bhh",
  "type": "assistant",
  "uuid": "5f0592c7-38d0-4d5a-b114-528b8e81696b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FU49YssmX3WZVih51ER63c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 46364,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1500,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 403,
          "cache_read_input_tokens": 46364,
          "cache_creation_input_tokens": 1500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1500
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

_source line 52 · 2026-05-10T07:46:05.663Z_

<details><summary>↩ Tool result · `toolu_01CpRkC2KVYnjSvXCfbiGuGp`</summary>

```text
# CulturalBench Dataset Usage Terms

**License & Distribution:**
The paper states: "We publicly release the CulturalBench data with Creative Commons Attribution 4.0 license."

**Training Restrictions:**
The authors explicitly note: "To avoid exposing the correct answers to models for fair comparison, our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training."

**Access Points:**
The paper provides two official links for accessing the benchmark:
- HuggingFace Spaces: https://hf.co/spaces/kellycyy/CulturalBench
- The data appears publicly available through these official channels

**Summary:** CulturalBench is released under CC-BY 4.0, making it freely usable with attribution. However, it cannot be used for model training due to contractual restrictions with the annotation platform. The dataset is intended exclusively for evaluation purposes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66d34b6a-6570-4236-a3e6-686f8d12a527",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "0559d505-98fe-4bb2-840e-0fe0c0175f5a",
  "toolUseResult": {
    "bytes": 468424,
    "code": 200,
    "codeText": "OK",
    "result": "# CulturalBench Dataset Usage Terms\n\n**License & Distribution:**\nThe paper states: \"We publicly release the CulturalBench data with Creative Commons Attribution 4.0 license.\"\n\n**Training Restrictions:**\nThe authors explicitly note: \"To avoid exposing the correct answers to models for fair comparison, our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training.\"\n\n**Access Points:**\nThe paper provides two official links for accessing the benchmark:\n- HuggingFace Spaces: https://hf.co/spaces/kellycyy/CulturalBench\n- The data appears publicly available through these official channels\n\n**Summary:** CulturalBench is released under CC-BY 4.0, making it freely usable with attribution. However, it cannot be used for model training due to contractual restrictions with the annotation platform. The dataset is intended exclusively for evaluation purposes.",
    "durationMs": 3997,
    "url": "https://arxiv.org/html/2410.02677v2"
  },
  "sourceToolAssistantUUID": "66d34b6a-6570-4236-a3e6-686f8d12a527",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-10T07:46:10.556Z_

<details><summary>↩ Tool result · `toolu_01S2k2oGiqug3ir3huydwUWj`</summary>

```text
Web search results for query: "training-time cultural preservation multilingual LLM instruction fine-tuning prevent cultural knowledge loss 2026 arxiv method"

Links: [{"title":"Final Report - Fine Tuning Methods for Low-resource Languages","url":"https://arxiv.org/html/2510.04139v1"},{"title":"Opportunities and Challenges of Large Language Models for","url":"https://arxiv.org/pdf/2412.04497"},{"title":"Improving Multilingual Capabilities with Cultural and Local Knowledge","url":"https://arxiv.org/pdf/2504.09753"},{"title":"Improving Multilingual Capabilities with Cultural and Local Knowledge in Large Language Models While Enhancing Native Performance","url":"https://arxiv.org/html/2504.09753"},{"title":"Identity-Aware Large Language Models require Cultural Reasoning","url":"https://arxiv.org/html/2510.18510v1"},{"title":"CultureLLM: Incorporating Cultural Differences into Large Language Models","url":"https://arxiv.org/pdf/2402.10946"},{"title":"CRAFT: Extracting and Tuning Cultural Instructions from the Wild","url":"https://arxiv.org/html/2405.03138"},{"title":"A Survey of Instruction Tuning in Large Language Models","url":"https://www.arxiv.org/pdf/2508.17184"},{"title":"Cultural Learning-Based Culture Adaptation of Language Models","url":"https://arxiv.org/html/2504.02953v1"},{"title":"Bridging the Gap: Enhancing LLM Performance for Low-Resource African Languages with New Benchmarks, Fine-Tuning, and Cultural Adjustments","url":"https://arxiv.org/html/2412.12417v1"}]

Based on the web search results, here are the key findings related to training-time cultural preservation in multilingual LLM instruction fine-tuning:

## Key Research Areas

**Cultural Knowledge Preservation Through Fine-Tuning**

Recent work demonstrates that using curated datasets composed of English and Hindi instruction data, researchers can instruction-tune models to improve performance over both English and Hindi, with experiments showing that it is possible to significantly improve multilingual performance without compromising native performance.

**Preventing Cultural Knowledge Loss**

The rise of Large Language Models has not been inclusive of all cultures, with models mostly trained on English texts and culture which makes them underperform in other languages and cultural contexts. UNESCO's 'Language Technologies for All' initiative ensures that AI models support a broad range of languages, which is vital to preserve global cultural heritage and prevent digital language extinction.

**Cultural Instruction Fine-Tuning Methods**

One pioneering approach involves deriving instruction tuning sets from unlabeled corpora by using keyword filtering to isolate culturally relevant concepts from a vast corpus, then utilizing these selected regional text segments to prompt LLMs for both questions and answers.

**Addressing Cultural Reasoning**

An approach treats cultural reasoning as testable behaviour grounded in validated cultural descriptions and value statements, enables assessment in mixed-identity scenarios, and yields actionable signals for data curation and fine-tuning.

**Future Research Directions**

The next phase of instruction-tuning research will include maintaining robustness under ambiguous or conflicting instructions, building culturally pluralistic datasets, enabling context-aware multi-agent collaboration, establishing evaluation frameworks that reflect both performance and ethical alignment, and embedding LLMs into real-world domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f0592c7-38d0-4d5a-b114-528b8e81696b",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "211be493-1259-4f92-9719-8c79fef13e7a",
  "toolUseResult": {
    "query": "training-time cultural preservation multilingual LLM instruction fine-tuning prevent cultural knowledge loss 2026 arxiv method",
    "results": [
      {
        "tool_use_id": "srvtoolu_019asBQf4iCT8gUXsQPbSFdA",
        "content": [
          {
            "title": "Final Report - Fine Tuning Methods for Low-resource Languages",
            "url": "https://arxiv.org/html/2510.04139v1"
          },
          {
            "title": "Opportunities and Challenges of Large Language Models for",
            "url": "https://arxiv.org/pdf/2412.04497"
          },
          {
            "title": "Improving Multilingual Capabilities with Cultural and Local Knowledge",
            "url": "https://arxiv.org/pdf/2504.09753"
          },
          {
            "title": "Improving Multilingual Capabilities with Cultural and Local Knowledge in Large Language Models While Enhancing Native Performance",
            "url": "https://arxiv.org/html/2504.09753"
          },
          {
            "title": "Identity-Aware Large Language Models require Cultural Reasoning",
            "url": "https://arxiv.org/html/2510.18510v1"
          },
          {
            "title": "CultureLLM: Incorporating Cultural Differences into Large Language Models",
            "url": "https://arxiv.org/pdf/2402.10946"
          },
          {
            "title": "CRAFT: Extracting and Tuning Cultural Instructions from the Wild",
            "url": "https://arxiv.org/html/2405.03138"
          },
          {
            "title": "A Survey of Instruction Tuning in Large Language Models",
            "url": "https://www.arxiv.org/pdf/2508.17184"
          },
          {
            "title": "Cultural Learning-Based Culture Adaptation of Language Models",
            "url": "https://arxiv.org/html/2504.02953v1"
          },
          {
            "title": "Bridging the Gap: Enhancing LLM Performance for Low-Resource African Languages with New Benchmarks, Fine-Tuning, and Cultural Adjustments",
            "url": "https://arxiv.org/html/2412.12417v1"
          }
        ]
      },
      "Based on the web search results, here are the key findings related to training-time cultural preservation in multilingual LLM instruction fine-tuning:\n\n## Key Research Areas\n\n**Cultural Knowledge Preservation Through Fine-Tuning**\n\nRecent work demonstrates that using curated datasets composed of English and Hindi instruction data, researchers can instruction-tune models to improve performance over both English and Hindi, with experiments showing that it is possible to significantly improve multilingual performance without compromising native performance.\n\n**Preventing Cultural Knowledge Loss**\n\nThe rise of Large Language Models has not been inclusive of all cultures, with models mostly trained on English texts and culture which makes them underperform in other languages and cultural contexts. UNESCO's 'Language Technologies for All' initiative ensures that AI models support a broad range of languages, which is vital to preserve global cultural heritage and prevent digital language extinction.\n\n**Cultural Instruction Fine-Tuning Methods**\n\nOne pioneering approach involves deriving instruction tuning sets from unlabeled corpora by using keyword filtering to isolate culturally relevant concepts from a vast corpus, then utilizing these selected regional text segments to prompt LLMs for both questions and answers.\n\n**Addressing Cultural Reasoning**\n\nAn approach treats cultural reasoning as testable behaviour grounded in validated cultural descriptions and value statements, enables assessment in mixed-identity scenarios, and yields actionable signals for data curation and fine-tuning.\n\n**Future Research Directions**\n\nThe next phase of instruction-tuning research will include maintaining robustness under ambiguous or conflicting instructions, building culturally pluralistic datasets, enabling context-aware multi-agent collaboration, establishing evaluation frameworks that reflect both performance and ethical alignment, and embedding LLMs into real-world domains."
    ],
    "durationSeconds": 8.534635231000008
  },
  "sourceToolAssistantUUID": "5f0592c7-38d0-4d5a-b114-528b8e81696b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-10T07:46:16.440Z_

<details><summary>Logged reasoning block</summary>

```text
This is a CRITICAL finding! 

CulturalBench explicitly states: "To avoid exposing the correct answers to models for fair comparison, our annotation platform, which involves using OpenAI APIs, **disallowed the collected data to be used for training.**"

The paper claims CulturalBench is "publicly available for training use" for Stage 2 probes, but this is factually incorrect. CulturalBench cannot be used for training per its own license terms.

This is a significant issue that needs to be flagged:


- If CulturalBench can't be used for training the cultural-localization probes, the paper needs an alternative data source
- The claim about it being "publicly available for training use" is demonstrably false

Now I need to search for more recent work that might address training-time prevention of cultural erasure, and check if there's anything from 2026 that tackles this problem directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "211be493-1259-4f92-9719-8c79fef13e7a",
  "isSidechain": false,
  "requestId": "req_011CatWx78xpcrL9C4XYWAXB",
  "type": "assistant",
  "uuid": "1803e5fe-c71f-4614-9c9b-ed1727bc3edd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AZDLsPkTQ3rFYsx8RQ4gL2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1474,
      "cache_read_input_tokens": 47864,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1474,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 47864,
          "cache_creation_input_tokens": 1474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1474
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

_source line 55 · 2026-05-10T07:46:16.452Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PbMrFP3nwKU5v52cm85Boo`</summary>

```json
{
  "query": "arxiv 2025 2026 \"cultural preservation\" OR \"prevent cultural erasure\" cross-lingual fine-tuning training layer freezing method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1803e5fe-c71f-4614-9c9b-ed1727bc3edd",
  "isSidechain": false,
  "requestId": "req_011CatWx78xpcrL9C4XYWAXB",
  "type": "assistant",
  "uuid": "bf4c7c20-9315-4439-b495-6e987b3ba4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AZDLsPkTQ3rFYsx8RQ4gL2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1474,
      "cache_read_input_tokens": 47864,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1474,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 47864,
          "cache_creation_input_tokens": 1474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1474
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

_source line 56 · 2026-05-10T07:46:16.937Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016nKU59BQJeEsBnWPeCpxa9`</summary>

```json
{
  "query": "HyoJung Han publication page 2026 \"rethinking cross-lingual alignment\" ICLR accepted preprint status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf4c7c20-9315-4439-b495-6e987b3ba4a5",
  "isSidechain": false,
  "requestId": "req_011CatWx78xpcrL9C4XYWAXB",
  "type": "assistant",
  "uuid": "afc08f8b-44ab-43f4-ad63-1ea144009fd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AZDLsPkTQ3rFYsx8RQ4gL2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1474,
      "cache_read_input_tokens": 47864,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1474,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 47864,
          "cache_creation_input_tokens": 1474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1474
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

_source line 57 · 2026-05-10T07:46:22.596Z_

<details><summary>↩ Tool result · `toolu_016nKU59BQJeEsBnWPeCpxa9`</summary>

```text
Web search results for query: "HyoJung Han publication page 2026 "rethinking cross-lingual alignment" ICLR accepted preprint status"

Links: [{"title":"HyoJung Han","url":"https://h-j-han.github.io/"},{"title":"[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://arxiv.org/abs/2510.26024"},{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | OpenReview","url":"https://openreview.net/forum?id=8DBHkEe0sm"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in the Multilingual Performance of LLMs - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.225/"},{"title":"HyoJung Han on X: \"Lots of work on cross-lingual alignment encourages multilingual LLMs to generalize knowledge across languages. But this push for uniformity creates a tension: what happens to knowledge that should remain local? We look into this trade-off of transfer and cultural erasure:🧵 https://t.co/yA3wCChCzW\" / X","url":"https://x.com/h__j___han/status/1984076295295443341"},{"title":"RETHINKING CROSS-LINGUAL ALIGNMENT","url":"https://openreview.net/pdf/abfa92cdcf181286524673db4ccf7335b915639f.pdf"},{"title":"Rethinking Alignment in Cross-Lingual Knowledge Transfer | OpenReview","url":"https://openreview.net/forum?id=nId47dxIr2"},{"title":"Can you map it to English? The Role of Cross-Lingual ...","url":"https://aclanthology.org/2026.eacl-long.225.pdf"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | Request PDF","url":"https://www.researchgate.net/publication/397089048_Rethinking_Cross-lingual_Alignment_Balancing_Transfer_and_Cultural_Erasure_in_Multilingual_LLMs"}]

Based on the web search results, here's what I found regarding HyoJung Han's publication related to "Rethinking Cross-lingual Alignment":

## Paper Status

The paper "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs" is under review as a conference paper at ICLR 2026. 

The paper is authored by HyoJung Han, Sweta Agrawal and Eleftheria Briakou, and appears as an arXiv preprint (arXiv:2510.26024), which was posted on October 29, 2025.

## Paper Overview

Cross-lingual alignment (CLA) aims to align multilingual representations, enabling Large Language Models (LLMs) to seamlessly transfer knowledge across languages, but the paper hypothesizes this pursuit of representational convergence can inadvertently cause "cultural erasure". The authors introduce a holistic evaluation framework, the transfer-localization plane, which quantifies both desirable knowledge transfer and undesirable cultural erasure.

The paper is currently available as an arXiv preprint and is under review for ICLR 2026, so it has not yet received an official acceptance decision at this time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afc08f8b-44ab-43f4-ad63-1ea144009fd4",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "36d0d4a1-207b-416a-84d1-9c43fed57643",
  "toolUseResult": {
    "query": "HyoJung Han publication page 2026 \"rethinking cross-lingual alignment\" ICLR accepted preprint status",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JfgcJCG18nQEQXEoBCXbu4",
        "content": [
          {
            "title": "HyoJung Han",
            "url": "https://h-j-han.github.io/"
          },
          {
            "title": "[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs",
            "url": "https://arxiv.org/abs/2510.26024"
          },
          {
            "title": "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=8DBHkEe0sm"
          },
          {
            "title": "Can you map it to English? The Role of Cross-Lingual Alignment in the Multilingual Performance of LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2026.eacl-long.225/"
          },
          {
            "title": "HyoJung Han on X: \"Lots of work on cross-lingual alignment encourages multilingual LLMs to generalize knowledge across languages. But this push for uniformity creates a tension: what happens to knowledge that should remain local? We look into this trade-off of transfer and cultural erasure:🧵 https://t.co/yA3wCChCzW\" / X",
            "url": "https://x.com/h__j___han/status/1984076295295443341"
          },
          {
            "title": "RETHINKING CROSS-LINGUAL ALIGNMENT",
            "url": "https://openreview.net/pdf/abfa92cdcf181286524673db4ccf7335b915639f.pdf"
          },
          {
            "title": "Rethinking Alignment in Cross-Lingual Knowledge Transfer | OpenReview",
            "url": "https://openreview.net/forum?id=nId47dxIr2"
          },
          {
            "title": "Can you map it to English? The Role of Cross-Lingual ...",
            "url": "https://aclanthology.org/2026.eacl-long.225.pdf"
          },
          {
            "title": "Main Conference Accepted Papers -",
            "url": "https://2026.eacl.org/program/main-accepted/"
          },
          {
            "title": "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/397089048_Rethinking_Cross-lingual_Alignment_Balancing_Transfer_and_Cultural_Erasure_in_Multilingual_LLMs"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding HyoJung Han's publication related to \"Rethinking Cross-lingual Alignment\":\n\n## Paper Status\n\nThe paper \"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs\" is under review as a conference paper at ICLR 2026. \n\nThe paper is authored by HyoJung Han, Sweta Agrawal and Eleftheria Briakou, and appears as an arXiv preprint (arXiv:2510.26024), which was posted on October 29, 2025.\n\n## Paper Overview\n\nCross-lingual alignment (CLA) aims to align multilingual representations, enabling Large Language Models (LLMs) to seamlessly transfer knowledge across languages, but the paper hypothesizes this pursuit of representational convergence can inadvertently cause \"cultural erasure\". The authors introduce a holistic evaluation framework, the transfer-localization plane, which quantifies both desirable knowledge transfer and undesirable cultural erasure.\n\nThe paper is currently available as an arXiv preprint and is under review for ICLR 2026, so it has not yet received an official acceptance decision at this time."
    ],
    "durationSeconds": 5.654977299999999
  },
  "sourceToolAssistantUUID": "afc08f8b-44ab-43f4-ad63-1ea144009fd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T07:46:24.163Z_

<details><summary>↩ Tool result · `toolu_01PbMrFP3nwKU5v52cm85Boo`</summary>

```text
Web search results for query: "arxiv 2025 2026 "cultural preservation" OR "prevent cultural erasure" cross-lingual fine-tuning training layer freezing method"

Links: [{"title":"[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://arxiv.org/abs/2510.26024"},{"title":"When AI Writes, Whose Voice Remains? Quantifying Cultural Marker Erasure Across World English Varieties in Large Language Models","url":"https://arxiv.org/html/2602.22145"},{"title":"Opportunities and Challenges of Large Language Models for","url":"https://arxiv.org/pdf/2412.04497"},{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | Request PDF","url":"https://www.researchgate.net/publication/397089048_Rethinking_Cross-lingual_Alignment_Balancing_Transfer_and_Cultural_Erasure_in_Multilingual_LLMs"},{"title":"Where Culture Fades: Revealing the Cultural Gap in Text-to-Image Generation","url":"https://arxiv.org/html/2511.17282"},{"title":"Risks of Cultural Erasure in Large Language Models","url":"https://arxiv.org/pdf/2501.01056"},{"title":"On The Conceptualization and Societal Impact of Cross-Cultural Bias","url":"https://arxiv.org/html/2512.21809v1"},{"title":"Survey of Cultural Awareness in Language Models: Text and Beyond","url":"https://arxiv.org/html/2411.00860v1"},{"title":"Identity-Aware Large Language Models require Cultural Reasoning","url":"https://arxiv.org/html/2510.18510v1"},{"title":"CulturePark: Boosting Cross-cultural Understanding in Large Language Models","url":"https://arxiv.org/html/2405.15145v1"}]

Based on the web search results, I found several highly relevant research papers from 2025-2026 on cultural preservation and preventing cultural erasure in cross-lingual fine-tuning:

## Key Findings:

**1. "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs" (arXiv 2510.26024, October 2025)**

This paper addresses how cross-lingual alignment aims to align multilingual representations across languages, but can inadvertently cause "cultural erasure", the functional loss of providing culturally-situated responses that should diverge based on the query language. The authors introduce a transfer-localization plane framework which quantifies both desirable knowledge transfer and undesirable cultural erasure.

**2. "Where Culture Fades: Revealing the Cultural Gap in Text-to-Image Generation" (arXiv 2511.17282, November 2025)**

This work reveals that multilingual models often yield culturally neutral or English-biased outputs due to weak activation of culture-sensitive representations, and introduces two lightweight remedies: inference-time cultural activation and layer-targeted cultural enhancement. The paper localizes culture-sensitive signals to a small set of neurons in a few fixed layers, and proposes both a zero-training activation scheme and a layer-specific fine-tuned scheme that updates only culturally relevant layers.

**3. "When AI Writes, Whose Voice Remains?" (arXiv 2602.22145, February 2026)**

This paper addresses whether explicit cultural-preservation prompts can reduce erasure without sacrificing semantic quality, demonstrating that pragmatic markers face higher vulnerability and that prompts reduce erasure by 29% without semantic cost.

These papers directly address cross-lingual fine-tuning methods with layer freezing/targeting approaches to prevent cultural erasure.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf4c7c20-9315-4439-b495-6e987b3ba4a5",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "3ca6d6c3-1024-4e16-8028-ac8f8bdcc151",
  "toolUseResult": {
    "query": "arxiv 2025 2026 \"cultural preservation\" OR \"prevent cultural erasure\" cross-lingual fine-tuning training layer freezing method",
    "results": [
      {
        "tool_use_id": "srvtoolu_014Q8B5YsShRQ8Z5VK5LtLqM",
        "content": [
          {
            "title": "[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs",
            "url": "https://arxiv.org/abs/2510.26024"
          },
          {
            "title": "When AI Writes, Whose Voice Remains? Quantifying Cultural Marker Erasure Across World English Varieties in Large Language Models",
            "url": "https://arxiv.org/html/2602.22145"
          },
          {
            "title": "Opportunities and Challenges of Large Language Models for",
            "url": "https://arxiv.org/pdf/2412.04497"
          },
          {
            "title": "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/397089048_Rethinking_Cross-lingual_Alignment_Balancing_Transfer_and_Cultural_Erasure_in_Multilingual_LLMs"
          },
          {
            "title": "Where Culture Fades: Revealing the Cultural Gap in Text-to-Image Generation",
            "url": "https://arxiv.org/html/2511.17282"
          },
          {
            "title": "Risks of Cultural Erasure in Large Language Models",
            "url": "https://arxiv.org/pdf/2501.01056"
          },
          {
            "title": "On The Conceptualization and Societal Impact of Cross-Cultural Bias",
            "url": "https://arxiv.org/html/2512.21809v1"
          },
          {
            "title": "Survey of Cultural Awareness in Language Models: Text and Beyond",
            "url": "https://arxiv.org/html/2411.00860v1"
          },
          {
            "title": "Identity-Aware Large Language Models require Cultural Reasoning",
            "url": "https://arxiv.org/html/2510.18510v1"
          },
          {
            "title": "CulturePark: Boosting Cross-cultural Understanding in Large Language Models",
            "url": "https://arxiv.org/html/2405.15145v1"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant research papers from 2025-2026 on cultural preservation and preventing cultural erasure in cross-lingual fine-tuning:\n\n## Key Findings:\n\n**1. \"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs\" (arXiv 2510.26024, October 2025)**\n\nThis paper addresses how cross-lingual alignment aims to align multilingual representations across languages, but can inadvertently cause \"cultural erasure\", the functional loss of providing culturally-situated responses that should diverge based on the query language. The authors introduce a transfer-localization plane framework which quantifies both desirable knowledge transfer and undesirable cultural erasure.\n\n**2. \"Where Culture Fades: Revealing the Cultural Gap in Text-to-Image Generation\" (arXiv 2511.17282, November 2025)**\n\nThis work reveals that multilingual models often yield culturally neutral or English-biased outputs due to weak activation of culture-sensitive representations, and introduces two lightweight remedies: inference-time cultural activation and layer-targeted cultural enhancement. The paper localizes culture-sensitive signals to a small set of neurons in a few fixed layers, and proposes both a zero-training activation scheme and a layer-specific fine-tuned scheme that updates only culturally relevant layers.\n\n**3. \"When AI Writes, Whose Voice Remains?\" (arXiv 2602.22145, February 2026)**\n\nThis paper addresses whether explicit cultural-preservation prompts can reduce erasure without sacrificing semantic quality, demonstrating that pragmatic markers face higher vulnerability and that prompts reduce erasure by 29% without semantic cost.\n\nThese papers directly address cross-lingual fine-tuning methods with layer freezing/targeting approaches to prevent cultural erasure."
    ],
    "durationSeconds": 7.706712886000008
  },
  "sourceToolAssistantUUID": "bf4c7c20-9315-4439-b495-6e987b3ba4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 59_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3ca6d6c3-1024-4e16-8028-ac8f8bdcc151",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Cultural preservation in cross-lingual LoRA fine-tuning",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Assistant

_source line 61 · 2026-05-10T07:46:32.919Z_

<details><summary>Logged reasoning block</summary>

```text
I found some very important issues:

1. **CulturalBench Training Restriction**: The paper explicitly states that CulturalBench cannot be used for training (their annotation platform with OpenAI APIs disallowed training use). CLS-LoRA claims it's "publicly available for training use" for Stage 2 probes, but this is factually wrong.

2. **"Where Culture Fades" (arXiv:2511.17282, November 2025)**: This paper on text-to-image generation introduces "layer-targeted cultural enhancement" that updates only culturally relevant layers. While this is for image generation (different domain), the conceptual parallel is close: layer-selective updates to preserve cultural signals. I should check this more carefully.


3. The arXiv:2510.26024 paper appears to still be under review at ICLR 2026 rather than accepted, and I need to verify the actual publication status through HyoJung Han's page. Let me examine "Where Culture Fades" more closely since it also discusses layer-targeted approaches to cultural sensitivity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ca6d6c3-1024-4e16-8028-ac8f8bdcc151",
  "isSidechain": false,
  "requestId": "req_011CatWy7JfhSvmHTyzLy5r2",
  "type": "assistant",
  "uuid": "b9a52d2a-78c0-4e78-86c6-54a5db81b883",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MFnYRwHwXr4U1mmxFYSLLs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 953,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 49338,
      "output_tokens": 519,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 953,
          "output_tokens": 519,
          "cache_read_input_tokens": 49338,
          "cache_creation_input_tokens": 1335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1335
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

_source line 62 · 2026-05-10T07:46:32.935Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KLpkvRfyc4GWN6iTyjBggm`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.17282",
  "prompt": "What does this paper do specifically? Does it identify culturally sensitive layers and fine-tune only those layers? Is this for text-to-image generation or LLMs? What models are used? How does the layer-targeted cultural enhancement work? Does it involve LoRA?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9a52d2a-78c0-4e78-86c6-54a5db81b883",
  "isSidechain": false,
  "requestId": "req_011CatWy7JfhSvmHTyzLy5r2",
  "type": "assistant",
  "uuid": "c3eccf85-29d4-4e21-af50-fa6f4c685302",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MFnYRwHwXr4U1mmxFYSLLs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 953,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 49338,
      "output_tokens": 519,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 953,
          "output_tokens": 519,
          "cache_read_input_tokens": 49338,
          "cache_creation_input_tokens": 1335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1335
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

_source line 63 · 2026-05-10T07:46:33.662Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014jiF8xL1gYR74wCou1E5SB`</summary>

```json
{
  "query": "SemEval 2026 task 7 BLEnD evaluation-only training use restrictions cultural benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3eccf85-29d4-4e21-af50-fa6f4c685302",
  "isSidechain": false,
  "requestId": "req_011CatWy7JfhSvmHTyzLy5r2",
  "type": "assistant",
  "uuid": "a9d2ba2f-69c7-4732-8202-e5727afee683",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MFnYRwHwXr4U1mmxFYSLLs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 953,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 49338,
      "output_tokens": 519,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 953,
          "output_tokens": 519,
          "cache_read_input_tokens": 49338,
          "cache_creation_input_tokens": 1335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1335
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

_source line 64 · 2026-05-10T07:46:37.465Z_

<details><summary>↩ Tool result · `toolu_01KLpkvRfyc4GWN6iTyjBggm`</summary>

```text
# Paper Summary: "Where Culture Fades"

**Domain:** Text-to-image (T2I) generation, not LLMs.

**Core Finding:** The paper identifies that current multilingual T2I models produce "culturally neutral or English-biased results" due to insufficient activation of culture-related representations, not missing cultural knowledge.

**Technical Approach:**

The researchers use a "probing method that localizes culture-sensitive signals to a small set of neurons in a few fixed layers." Based on this discovery, they introduce two complementary strategies:

1. **Inference-time activation** - amplifies identified culture-sensitive neurons without backbone fine-tuning
2. **Layer-targeted enhancement** - updates "only culturally relevant layers"

**Models Tested:** The abstract references "two representative models" but doesn't specify which ones in the provided content.

**LoRA Usage:** Not mentioned in the abstract or available text.

**Key Result:** Their CultureBench demonstrates "consistent improvements over strong baselines in cultural consistency while preserving fidelity and diversity."

The approach is notably efficient—targeting specific neurons and layers rather than full model retraining—though the exact implementation details of layer-targeted enhancement aren't elaborated in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3eccf85-29d4-4e21-af50-fa6f4c685302",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "640aac5e-b343-4e24-87c4-7f2f4cbb8326",
  "toolUseResult": {
    "bytes": 47555,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: \"Where Culture Fades\"\n\n**Domain:** Text-to-image (T2I) generation, not LLMs.\n\n**Core Finding:** The paper identifies that current multilingual T2I models produce \"culturally neutral or English-biased results\" due to insufficient activation of culture-related representations, not missing cultural knowledge.\n\n**Technical Approach:**\n\nThe researchers use a \"probing method that localizes culture-sensitive signals to a small set of neurons in a few fixed layers.\" Based on this discovery, they introduce two complementary strategies:\n\n1. **Inference-time activation** - amplifies identified culture-sensitive neurons without backbone fine-tuning\n2. **Layer-targeted enhancement** - updates \"only culturally relevant layers\"\n\n**Models Tested:** The abstract references \"two representative models\" but doesn't specify which ones in the provided content.\n\n**LoRA Usage:** Not mentioned in the abstract or available text.\n\n**Key Result:** Their CultureBench demonstrates \"consistent improvements over strong baselines in cultural consistency while preserving fidelity and diversity.\"\n\nThe approach is notably efficient—targeting specific neurons and layers rather than full model retraining—though the exact implementation details of layer-targeted enhancement aren't elaborated in this excerpt.",
    "durationMs": 4527,
    "url": "https://arxiv.org/abs/2511.17282"
  },
  "sourceToolAssistantUUID": "c3eccf85-29d4-4e21-af50-fa6f4c685302",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-10T07:46:40.549Z_

<details><summary>↩ Tool result · `toolu_014jiF8xL1gYR74wCou1E5SB`</summary>

```text
Web search results for query: "SemEval 2026 task 7 BLEnD evaluation-only training use restrictions cultural benchmark"

Links: [{"title":"GitHub - BLEnD-SemEval2026/SemEval-2026-Task-7: SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures · GitHub","url":"https://github.com/BLEnD-SemEval2026/SemEval-2026-Task-7"},{"title":"SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures","url":"https://arxiv.org/html/2605.02601"},{"title":"[2605.02601v1] SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures","url":"https://arxiv.org/abs/2605.02601v1"},{"title":"[2605.02601] SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures","url":"https://arxiv.org/abs/2605.02601"},{"title":"[Corpora-List] CFP SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures","url":"https://www.mail-archive.com/corpora@list.elra.info/msg05362.html"},{"title":"Chenyang Lyu 吕晨阳 on X: \"Check out our SemEval 2026 Shared Task 7: Everyday Knowledge Across Diverse Languages &amp; Cultures !\" / X","url":"https://x.com/Chenyang_Lyu/status/1970417910427590935"},{"title":"SemEval-2026 Tasks | SemEval-2026","url":"https://semeval.github.io/SemEval2026/tasks.html"},{"title":"SemEval 2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures - Codabench","url":"https://www.codabench.org/competitions/10281/"},{"title":"POLAR @ SemEval-2026","url":"https://polar-semeval.github.io/"},{"title":"SemEval-2025 Tasks | SemEval-2025","url":"https://semeval.github.io/SemEval2025/tasks.html"}]

Based on the search results, here's information about SemEval 2026 Task 7 regarding the BLEnD benchmark and training use restrictions:

## Task Overview
SemEval-2026 Task 7 is a shared task on evaluating the adaptability of LLMs and NLP systems across multiple languages and cultures.

## BLEnD Benchmark and Training Restrictions
The task data consist of an extended version of the manually constructed BLEnD benchmark (Myung et al. 2024), covering more than 30 language-culture pairs, predominantly representing low-resource languages spoken across multiple continents.

**Crucially, regarding training use restrictions:** As the task is designed strictly for evaluation, participants were not permitted to use the data for training, fine-tuning, few-shot learning, or any other form of model modification.

Participants were required to predict labels and were allowed to submit any NLP system and adopt diverse modelling strategies, provided that the benchmark was used solely for evaluation.

## Cultural Benchmark Coverage
BLEnD currently covers 13 languages and 16 cultures, and for this shared task, the scope will be expanded to include 17 additional language–culture pairs.

## Task Structure
The task includes two tracks: (a) Short-Answer Questions (SAQ) and (b) Multiple-Choice Questions (MCQ).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9d2ba2f-69c7-4732-8202-e5727afee683",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "f39916d6-50c0-4d37-b24e-c96fd5181b6e",
  "toolUseResult": {
    "query": "SemEval 2026 task 7 BLEnD evaluation-only training use restrictions cultural benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_01247ZPSj1YTfBkh3ZMufo1E",
        "content": [
          {
            "title": "GitHub - BLEnD-SemEval2026/SemEval-2026-Task-7: SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures · GitHub",
            "url": "https://github.com/BLEnD-SemEval2026/SemEval-2026-Task-7"
          },
          {
            "title": "SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures",
            "url": "https://arxiv.org/html/2605.02601"
          },
          {
            "title": "[2605.02601v1] SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures",
            "url": "https://arxiv.org/abs/2605.02601v1"
          },
          {
            "title": "[2605.02601] SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures",
            "url": "https://arxiv.org/abs/2605.02601"
          },
          {
            "title": "[Corpora-List] CFP SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures",
            "url": "https://www.mail-archive.com/corpora@list.elra.info/msg05362.html"
          },
          {
            "title": "Chenyang Lyu 吕晨阳 on X: \"Check out our SemEval 2026 Shared Task 7: Everyday Knowledge Across Diverse Languages &amp; Cultures !\" / X",
            "url": "https://x.com/Chenyang_Lyu/status/1970417910427590935"
          },
          {
            "title": "SemEval-2026 Tasks | SemEval-2026",
            "url": "https://semeval.github.io/SemEval2026/tasks.html"
          },
          {
            "title": "SemEval 2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures - Codabench",
            "url": "https://www.codabench.org/competitions/10281/"
          },
          {
            "title": "POLAR @ SemEval-2026",
            "url": "https://polar-semeval.github.io/"
          },
          {
            "title": "SemEval-2025 Tasks | SemEval-2025",
            "url": "https://semeval.github.io/SemEval2025/tasks.html"
          }
        ]
      },
      "Based on the search results, here's information about SemEval 2026 Task 7 regarding the BLEnD benchmark and training use restrictions:\n\n## Task Overview\nSemEval-2026 Task 7 is a shared task on evaluating the adaptability of LLMs and NLP systems across multiple languages and cultures.\n\n## BLEnD Benchmark and Training Restrictions\nThe task data consist of an extended version of the manually constructed BLEnD benchmark (Myung et al. 2024), covering more than 30 language-culture pairs, predominantly representing low-resource languages spoken across multiple continents.\n\n**Crucially, regarding training use restrictions:** As the task is designed strictly for evaluation, participants were not permitted to use the data for training, fine-tuning, few-shot learning, or any other form of model modification.\n\nParticipants were required to predict labels and were allowed to submit any NLP system and adopt diverse modelling strategies, provided that the benchmark was used solely for evaluation.\n\n## Cultural Benchmark Coverage\nBLEnD currently covers 13 languages and 16 cultures, and for this shared task, the scope will be expanded to include 17 additional language–culture pairs.\n\n## Task Structure\nThe task includes two tracks: (a) Short-Answer Questions (SAQ) and (b) Multiple-Choice Questions (MCQ)."
    ],
    "durationSeconds": 6.884314111000014
  },
  "sourceToolAssistantUUID": "a9d2ba2f-69c7-4732-8202-e5727afee683",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 66 · 2026-05-10T07:46:40.553Z_

```json
{
  "parentUuid": "f39916d6-50c0-4d37-b24e-c96fd5181b6e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ebf67dc8-7c88-463e-b04f-fd2c722bef19",
  "timestamp": "2026-05-10T07:46:40.553Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 67 · 2026-05-10T07:47:09.536Z_

<details><summary>Logged reasoning block</summary>

```text
Key findings now:

1. **CulturalBench training restriction CONFIRMED**: "our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training." The paper's claim that CulturalBench is "publicly available for training use" is INCORRECT. This is a critical issue because Stage 2 relies on using CulturalBench held-out splits for probe training.

2. **SemEval-2026 Task 7 (BLEnD) evaluation-only confirmed**: "participants were not permitted to use the data for training, fine-tuning, few-shot learning, or any other form of model modification." The paper correctly characterizes this as evaluation-only.
   
3. **"Where Culture Fades" is for text-to-image generation**, not language models, so it's operating in a different domain entirely and doesn't directly compete with this work.

4. **arXiv:2510.26024 remains under review** at ICLR 2026 and hasn't been confirmed as accepted yet, which the paper does characterize correctly.

The core problem is becoming clear: CulturalBench explicitly prohibits training use, yet the paper's Stage 2 methodology depends on using held-out splits from this benchmark for probe training.

Looking at the Round 5 revisions, most of the requested changes have been incorporated—the multilingual benchmarks are now in Stage 4, the LoRA ablation is complete, and the Stage 1 probe methodology is clarified. But this data availability issue for Stage 2 remains unresolved and represents a genuine flaw in the experimental design.

Evaluating the paper's overall strength: the core contribution of using layer-selective LoRA to prevent cultural degradation during training is genuinely novel, and the 2×2 ablation combined with the Stage 1 structural diagnostics provides solid empirical grounding. The positioning against MLAS-LoRA and LayRA is well-differentiated. However, the CulturalBench training constraint drops feasibility to 3/5—the compute budget is manageable at 122-144 hours on H100s, and the 16-day timeline is realistic, but the missing training data source is a critical blocker.

The writing is clear and well-justified throughout, and the problem itself—preserving cultural knowledge in multilingual models rather than patching it post-hoc—addresses something genuinely important. Let me verify the compute breakdown more carefully: the core training runs, baselines, ablations, and structural diagnostics should fit within budget, with evaluation on XCOPA, XStoryCloze, and MGSM adding another 18-24 hours on A100s.

All three operational modes—auto-research, manual, and human-in-loop—stay comfortably under the 200-hour H100 equivalent constraint, and the evaluation protocol using standard benchmarks across 11 languages is solid.

But there's a major red flag: CulturalBench is explicitly restricted from training use, yet the paper claims to use it for Stage 2 probe training—that's a direct violation that undermines the entire methodology.

Let me search once more to catch any other competing work from 2026 I might have overlooked.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf67dc8-7c88-463e-b04f-fd2c722bef19",
  "isSidechain": false,
  "requestId": "req_011CatWzKNUbHgRY7vCgYRo6",
  "type": "assistant",
  "uuid": "47bf10a3-c90b-4836-aede-2ba718a82968",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016xhDAbLB4dvcdGcU9zUZnT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2814,
      "cache_read_input_tokens": 50673,
      "output_tokens": 1513,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1513,
          "cache_read_input_tokens": 50673,
          "cache_creation_input_tokens": 2814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2814
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

_source line 68 · 2026-05-10T07:47:09.549Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013qew1jvsWRB3Bp3Bho7sTi`</summary>

```json
{
  "query": "arxiv 2025 2026 multilingual instruction tuning \"cultural knowledge\" layer partition \"selective LoRA\" OR \"layer freezing\" OR \"layer-selective\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47bf10a3-c90b-4836-aede-2ba718a82968",
  "isSidechain": false,
  "requestId": "req_011CatWzKNUbHgRY7vCgYRo6",
  "type": "assistant",
  "uuid": "04d78128-8549-4403-ade8-69a2d272eb9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016xhDAbLB4dvcdGcU9zUZnT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2814,
      "cache_read_input_tokens": 50673,
      "output_tokens": 1513,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1513,
          "cache_read_input_tokens": 50673,
          "cache_creation_input_tokens": 2814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2814
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

_source line 69 · 2026-05-10T07:47:10.309Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012zPaxX8793FoYJ8teHuaS2`</summary>

```json
{
  "url": "https://h-j-han.github.io/",
  "prompt": "What is listed under publications? Is \"Rethinking Cross-lingual Alignment\" listed as an arXiv preprint, ICLR 2026 accepted paper, or just under review? What are the most recent publications listed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04d78128-8549-4403-ade8-69a2d272eb9e",
  "isSidechain": false,
  "requestId": "req_011CatWzKNUbHgRY7vCgYRo6",
  "type": "assistant",
  "uuid": "5bc1d4b8-2004-4358-8259-57b73bb767db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016xhDAbLB4dvcdGcU9zUZnT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2814,
      "cache_read_input_tokens": 50673,
      "output_tokens": 1513,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1513,
          "cache_read_input_tokens": 50673,
          "cache_creation_input_tokens": 2814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2814
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

_source line 70 · 2026-05-10T07:47:13.708Z_

<details><summary>↩ Tool result · `toolu_012zPaxX8793FoYJ8teHuaS2`</summary>

```text
# Publications Listed

Under the "Selected Publications" section, **"Rethinking Cross-lingual Alignment"** is presented as an arXiv preprint, not an accepted conference paper. It's described as:

"arXiv preprint arXiv:2510.26024"

## Most Recent Publications

The three most recent items listed are:

1. **"Measuring User's Mental Models of Speech Translation in Human-AI Collaboration"** – ACL 2026 (main, long, oral)

2. **"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure..."** – arXiv preprint only

3. **"Can you map it to English? The Role of Cross-Lingual Alignment..."** – EACL 2026 (main, long, oral)

The first and third are accepted conference papers, while the second remains an arXiv preprint without conference acceptance listed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bc1d4b8-2004-4358-8259-57b73bb767db",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "ea4c4fe0-3eaa-46a9-abfb-4dc13ba12e9b",
  "toolUseResult": {
    "bytes": 25268,
    "code": 200,
    "codeText": "OK",
    "result": "# Publications Listed\n\nUnder the \"Selected Publications\" section, **\"Rethinking Cross-lingual Alignment\"** is presented as an arXiv preprint, not an accepted conference paper. It's described as:\n\n\"arXiv preprint arXiv:2510.26024\"\n\n## Most Recent Publications\n\nThe three most recent items listed are:\n\n1. **\"Measuring User's Mental Models of Speech Translation in Human-AI Collaboration\"** – ACL 2026 (main, long, oral)\n\n2. **\"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure...\"** – arXiv preprint only\n\n3. **\"Can you map it to English? The Role of Cross-Lingual Alignment...\"** – EACL 2026 (main, long, oral)\n\nThe first and third are accepted conference papers, while the second remains an arXiv preprint without conference acceptance listed.",
    "durationMs": 3396,
    "url": "https://h-j-han.github.io/"
  },
  "sourceToolAssistantUUID": "5bc1d4b8-2004-4358-8259-57b73bb767db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 71_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ea4c4fe0-3eaa-46a9-abfb-4dc13ba12e9b",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "Cultural preservation in cross-lingual LoRA fine-tuning",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Tool result

_source line 73 · 2026-05-10T07:47:17.920Z_

<details><summary>↩ Tool result · `toolu_013qew1jvsWRB3Bp3Bho7sTi`</summary>

```text
Web search results for query: "arxiv 2025 2026 multilingual instruction tuning "cultural knowledge" layer partition "selective LoRA" OR "layer freezing" OR "layer-selective""

Links: [{"title":"SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures","url":"https://arxiv.org/html/2605.02601"},{"title":"Improving Multilingual Capabilities with Cultural and Local Knowledge","url":"https://arxiv.org/pdf/2504.09753"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=8575&show=50"},{"title":"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly","url":"https://arxiv.org/html/2404.04659v1"},{"title":"[2508.17324] CultranAI at PalmX 2025: Data Augmentation for Cultural Knowledge Representation","url":"https://arxiv.org/abs/2508.17324"},{"title":"[2411.18571] Challenges in Adapting Multilingual LLMs to Low-Resource Languages using LoRA PEFT Tuning","url":"https://arxiv.org/abs/2411.18571"},{"title":"Improving Multilingual Capabilities with Cultural and Local Knowledge in Large Language Models While Enhancing Native Performance","url":"https://arxiv.org/html/2504.09753"},{"title":"Final Report - Fine Tuning Methods for Low-resource Languages","url":"https://arxiv.org/html/2510.04139v1"},{"title":"Published in Transactions on Machine Learning Research (02/2026)","url":"https://arxiv.org/pdf/2503.12016"},{"title":"Layer by Layer: Uncovering Where Multi-Task Learning Happens in Instruction-Tuned Large Language Models","url":"https://arxiv.org/html/2410.20008"}]

Based on the web search results, I found several relevant papers from 2025-2026 related to multilingual instruction tuning and cultural knowledge. Here are the key findings:

## Relevant Papers Found:

**1. SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures**
Submitted systems typically generated responses using models such as Gemini, GPT, Qwen, DeepSeek, or LLaMA, with approaches placing emphasis on prompt engineering and incorporating multilingual strategies, including pivot translation or direct prompting in the target language. Notably, some teams explored fine-tuning approaches, such as LoRA with synthetic training data, while a smaller number investigated more experimental techniques, such as activation steering using language vectors.

**2. Improving Multilingual Capabilities with Cultural and Local Knowledge in Large Language Models**
This recent paper from 2025 focuses on developing bilingual LLMs for English and Hindi tasks. The work develops a bilingual LLM performing well on English and Hindi tasks while maintaining smaller model sizes and employing computationally efficient fine-tuning methods such as Supervised Fine-Tuning (SFT) with Low-Rank Adaptation (LoRA).

**3. CultranAI at PalmX 2025: Data Augmentation for Cultural Knowledge Representation**
This system focused on data augmentation and LoRA fine-tuning of large language models for Arabic cultural knowledge representation, augmenting the PalmX dataset by incorporating the Palm dataset and curating a new dataset of over 22K culturally grounded multiple-choice questions.

**4. Layer-Based Insights on Instruction Tuning**
Research uncovered clear differences between pre-trained and instruction-tuned models, with the most significant representational transformations occurring in the middle transitional layers, highlighting the critical role of middle layers in encoding the specialized task knowledge induced by instruction tuning.

However, the search results don't appear to contain papers specifically combining all the exact elements you're looking for (layer partition with selective LoRA/layer freezing strategies specifically for multilingual instruction tuning with cultural knowledge layers). You may want to search arXiv directly or refine the query further.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04d78128-8549-4403-ade8-69a2d272eb9e",
  "isSidechain": false,
  "promptId": "19a8c537-763e-4eb2-904c-0601d6f42e9a",
  "type": "user",
  "uuid": "2c102846-5e0c-43c7-b38b-192e3765f173",
  "toolUseResult": {
    "query": "arxiv 2025 2026 multilingual instruction tuning \"cultural knowledge\" layer partition \"selective LoRA\" OR \"layer freezing\" OR \"layer-selective\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Kdm2mQFXwtT9D5S2Vfx4bk",
        "content": [
          {
            "title": "SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures",
            "url": "https://arxiv.org/html/2605.02601"
          },
          {
            "title": "Improving Multilingual Capabilities with Cultural and Local Knowledge",
            "url": "https://arxiv.org/pdf/2504.09753"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=8575&show=50"
          },
          {
            "title": "Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly",
            "url": "https://arxiv.org/html/2404.04659v1"
          },
          {
            "title": "[2508.17324] CultranAI at PalmX 2025: Data Augmentation for Cultural Knowledge Representation",
            "url": "https://arxiv.org/abs/2508.17324"
          },
          {
            "title": "[2411.18571] Challenges in Adapting Multilingual LLMs to Low-Resource Languages using LoRA PEFT Tuning",
            "url": "https://arxiv.org/abs/2411.18571"
          },
          {
            "title": "Improving Multilingual Capabilities with Cultural and Local Knowledge in Large Language Models While Enhancing Native Performance",
            "url": "https://arxiv.org/html/2504.09753"
          },
          {
            "title": "Final Report - Fine Tuning Methods for Low-resource Languages",
            "url": "https://arxiv.org/html/2510.04139v1"
          },
          {
            "title": "Published in Transactions on Machine Learning Research (02/2026)",
            "url": "https://arxiv.org/pdf/2503.12016"
          },
          {
            "title": "Layer by Layer: Uncovering Where Multi-Task Learning Happens in Instruction-Tuned Large Language Models",
            "url": "https://arxiv.org/html/2410.20008"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers from 2025-2026 related to multilingual instruction tuning and cultural knowledge. Here are the key findings:\n\n## Relevant Papers Found:\n\n**1. SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures**\nSubmitted systems typically generated responses using models such as Gemini, GPT, Qwen, DeepSeek, or LLaMA, with approaches placing emphasis on prompt engineering and incorporating multilingual strategies, including pivot translation or direct prompting in the target language. Notably, some teams explored fine-tuning approaches, such as LoRA with synthetic training data, while a smaller number investigated more experimental techniques, such as activation steering using language vectors.\n\n**2. Improving Multilingual Capabilities with Cultural and Local Knowledge in Large Language Models**\nThis recent paper from 2025 focuses on developing bilingual LLMs for English and Hindi tasks. The work develops a bilingual LLM performing well on English and Hindi tasks while maintaining smaller model sizes and employing computationally efficient fine-tuning methods such as Supervised Fine-Tuning (SFT) with Low-Rank Adaptation (LoRA).\n\n**3. CultranAI at PalmX 2025: Data Augmentation for Cultural Knowledge Representation**\nThis system focused on data augmentation and LoRA fine-tuning of large language models for Arabic cultural knowledge representation, augmenting the PalmX dataset by incorporating the Palm dataset and curating a new dataset of over 22K culturally grounded multiple-choice questions.\n\n**4. Layer-Based Insights on Instruction Tuning**\nResearch uncovered clear differences between pre-trained and instruction-tuned models, with the most significant representational transformations occurring in the middle transitional layers, highlighting the critical role of middle layers in encoding the specialized task knowledge induced by instruction tuning.\n\nHowever, the search results don't appear to contain papers specifically combining all the exact elements you're looking for (layer partition with selective LoRA/layer freezing strategies specifically for multilingual instruction tuning with cultural knowledge layers). You may want to search arXiv directly or refine the query further."
    ],
    "durationSeconds": 8.366606283000001
  },
  "sourceToolAssistantUUID": "04d78128-8549-4403-ade8-69a2d272eb9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-10T07:47:49.513Z_

<details><summary>Logged reasoning block</summary>

```text
Very important: This confirms that arXiv:2510.26024 ("Rethinking Cross-lingual Alignment") is indeed still an arXiv preprint - it was NOT accepted at ICLR 2026 as the Round 4 reviewer claimed. The paper correctly maintains this characterization. The Round 4 reviewer was wrong about the ICLR acceptance.

Now let me compile all the issues I've found:

**CRITICAL ISSUE**: 
1. **CulturalBench cannot be used for training**: The paper claims Stage 2 uses "held-out splits of CulturalBench (ACL 2025; 1,696 human-verified questions across 45 global regions), which is publicly available for training use" for probe training. 

But CulturalBench's own paper explicitly prohibits this - it states the collected data cannot be used for training due to OpenAI API restrictions. This means the Stage 2 probe training data source is invalid and the authors need to find an alternative.

**MODERATE ISSUES**:
2. **Compute estimate in auto mode slightly over 200h H100 upper bound in some interpretations**: The paper's claim of 310-360h A100 equivalent to 122-144h H100 appears roughly accurate when accounting for the ~2.5x performance ratio between these GPUs, though the estimate sits at the edge of what might be considered conservative.

3. **arXiv:2510.26024 status**: This is confirmed as an arXiv preprint rather than an accepted ICLR 2026 paper, which the authors have correctly characterized.

**What has been resolved from Round 5**:
1. ✅ XCOPA, XStoryCloze, MGSM added to Stage 4
2. ✅ Full LoRA + KL ablation (condition b) added
3. ✅ Stage 1 probe methodology clarified with separate probes
4. ✅ arXiv:2510.26024 status handled correctly

Looking at the overall quality assessment now: the core novelty here is strong - training-time cultural erasure prevention through layer-selective LoRA is genuinely novel, and no existing work addresses this specific mechanism.

The feasibility concern is significant though: the CulturalBench training restriction creates a real problem with the Stage 2 probe training data source being invalid. If that's resolved by using a different cultural dataset, the method becomes feasible within the compute constraints. The paper is well-organized with clear explanations of the mechanistic approach, Stage 1 methodology, and ablation design. Cultural preservation in multilingual models is an important problem with meaningful potential impact.

The overall score comes to 3.75, which falls short of the 4.0 pass threshold and suggests a revise decision. The critical fix is finding a valid source for the cultural-localization probe training that doesn't violate CulturalBench's restrictions—options like mC4 with cultural filtering, WikiData, MKQA, or World Values Survey questions could work. I'm reconsidering whether the SemEval-2026 Task 7 might offer another angle here.

The core issue is that both SemEval-2026 and CulturalBench are evaluation-only, so I need to figure out what cultural data is actually available for training probes. I could potentially use the raw cultural questions before benchmark formatting, or generate probe-appropriate data from multilingual Wikipedia articles on culture-specific topics. This feels fixable rather than a fundamental flaw, so revise is the right call.

Now I'm wondering if I'm being too strict about CulturalBench's restrictions—linear probing might fall into a different category than full model training, so the restriction might not actually apply here. The BLEnD data restriction is being followed correctly, but the CulturalBench training issue remains a critical problem that significantly undermines the paper's validity. Weighing all the scores together—4, 3, 4, and 4—brings the average to 3.75, which falls below the 4.0 threshold and points toward a "revise" recommendation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c102846-5e0c-43c7-b38b-192e3765f173",
  "isSidechain": false,
  "requestId": "req_011CatX358ocNcFuWc3J2G8n",
  "type": "assistant",
  "uuid": "c9fb74d0-e5d6-4336-87d7-2323a25cd020",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013gshrosAJnSYVBVBKQJHrX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 243,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 53487,
      "output_tokens": 3218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 243,
          "output_tokens": 3218,
          "cache_read_input_tokens": 53487,
          "cache_creation_input_tokens": 2535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2535
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

_source line 75 · 2026-05-10T07:48:16.528Z_

I now have enough information to issue my verdict. Let me compile the key findings from my independent research.

**Key findings from my research:**

1. **CulturalBench training restriction (CRITICAL)**: The paper claims "CulturalBench (ACL 2025; 1,696 human-verified questions across 45 global regions), which is publicly available for training use" for Stage 2 probe training. But the CulturalBench paper explicitly states: *"our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training."* The claim that CulturalBench is available for training use is factually false and invalidates the Stage 2 probe training data source.

2. **arXiv:2510.26024 status confirmed as preprint**: HyoJung Han's own publication page lists this as "arXiv preprint arXiv:2510.26024" — not an ICLR 2026 accepted paper. The paper correctly characterizes it this way.

3. **No direct competing training-time cultural preservation method found**: My searches confirmed no published work specifically addresses training-time prevention of cultural erasure via layer-selective LoRA.

4. **Round 5 issues all addressed**: XCOPA/XStoryCloze/MGSM added to Stage 4; 2×2 ablation with condition (b) added; Stage 1 probe protocol clarified with separate per-checkpoint probes.

5. **Sparse Subnetwork Enhancement (arXiv:2510.13580)** addresses language performance for underrepresented languages but not cultural knowledge preservation — not a direct competitor, but should be acknowledged in related work.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "Training-time prevention of cultural erasure via empirically-derived layer-selective LoRA is genuinely novel; no existing work occupies this combination of objective (cultural preservation), mechanism (layer freezing based on per-model probing), and setting (cross-lingual instruction fine-tuning). The 2×2 ablation and Stage 1 structural diagnostic are methodologically credible differentiators."
    },
    "feasibility": {
      "score": 3,
      "rationale": "The CulturalBench training-restriction violation is a blocking dependency for Stage 2 probe training: the dataset explicitly forbids training use due to OpenAI API annotation-platform terms, contradicting the paper's claim that it is 'publicly available for training use.' This leaves Stage 2 cultural-localization probes without a valid data source. Compute and timeline are otherwise feasible at 122–144h H100 within the 200h constraint."
    },
    "clarity": {
      "score": 4,
      "rationale": "The mechanistic bridge, 2×2 ablation design, Stage 1 separate-probe protocol, and evaluation framework are all precisely specified; the paper is among the clearest in this review sequence. Minor ambiguity remains about what replaces CulturalBench for probe training."
    },
    "impact": {
      "score": 4,
      "rationale": "If the method works, training-time cultural-erasure prevention is practically valuable: practitioners currently must choose between cross-lingual capability and cultural authenticity, and an inference-time patch (Surgical Steering) is the only alternative. A training recipe that avoids this trade-off would be widely adopted."
    }
  },
  "issues": [
    "CRITICAL — CulturalBench is not available for training use. The paper claims Stage 2 cultural-localization probes are trained on 'held-out splits of CulturalBench (ACL 2025)...which is publicly available for training use.' This is factually wrong: the CulturalBench paper explicitly states 'our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training.' Using CulturalBench for probe training violates its terms. The Stage 2 probe training data source must be replaced with a training-permitted cultural knowledge resource (e.g., multilingual Wikipedia cultural-domain sentences, MKQA, World Values Survey items, or a custom culturally-grounded QA dataset without OpenAI annotation-platform restrictions). SemEval-2026 Task 7 (BLEnD) is correctly identified as evaluation-only and is not the issue here.",
    "MINOR — Sparse Subnetwork Enhancement for Underrepresented Languages (arXiv:2510.13580, updated Feb 2026) applies targeted sparse fine-tuning of language-associated subnetworks (<1% of parameters) and achieves strong cross-lingual alignment while preserving general capabilities, with adaptation concentrated in down-projection weights of later layers. Although its objective (language performance improvement) differs from CLS-LoRA's (cultural preservation), the layer-selective sparse-fine-tuning approach is closely related and should be acknowledged in the landscape section to preempt reviewer comparisons."
  ],
  "feedback": "Round 6 resolves all three Round 5 issues cleanly (XCOPA/XStoryCloze/MGSM added, 2×2 ablation with condition (b) included, Stage 1 separate-probe protocol specified). One critical correction remains before this can pass review:\n\n**Fix the CulturalBench training-use claim (critical, ~2 hours of work).** The CulturalBench paper explicitly states the dataset is prohibited from training use due to its OpenAI annotation-platform terms. Replace the Stage 2 cultural-localization probe training source with a dataset that permits training. Strong alternatives: (a) multilingual Wikipedia paragraphs from culture-specific articles, filtered by Wikidata cultural-domain tags — widely available, CC-BY licensed, and covers the 45+ cultural regions needed; (b) MKQA (multilingual knowledge questions, Apache 2.0), which covers culturally-grounded factual questions across languages; (c) a small GPT-4o-free annotation of culturally-grounded probe examples using open models (Qwen3-8B itself, before fine-tuning). CulturalBench should then be used *only* for final evaluation (Stage 4), alongside SemEval-2026 Task 7, which is already correctly limited to evaluation. Update the Stage 2 and Stage 4 data-source descriptions to reflect this separation, and remove the phrase 'publicly available for training use' from the CulturalBench reference. This is a single-paragraph fix in the approach and description sections.\n\n**Also add Sparse Subnetwork Enhancement (arXiv:2510.13580) to the landscape (minor, ~20 minutes).** Note that it improves underrepresented-language performance via language-neuron subnetwork selection, and differentiate on objective (language capability vs. cultural knowledge preservation) and partition axis (language-identity neurons vs. factual-cultural semantic axis).",
  "reason": "CulturalBench explicitly prohibits training use, invalidating Stage 2 probe training data; all Round 5 issues are otherwise resolved and the method is novel and well-designed."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9fb74d0-e5d6-4336-87d7-2323a25cd020",
  "isSidechain": false,
  "requestId": "req_011CatX358ocNcFuWc3J2G8n",
  "type": "assistant",
  "uuid": "0c3c49be-e51c-45ae-b62a-21ea5ec0ce5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013gshrosAJnSYVBVBKQJHrX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 243,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 53487,
      "output_tokens": 3218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 243,
          "output_tokens": 3218,
          "cache_read_input_tokens": 53487,
          "cache_creation_input_tokens": 2535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2535
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

_source line 76_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0c3c49be-e51c-45ae-b62a-21ea5ec0ce5e",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---

### Runtime record

_source line 77_

```json
{
  "type": "ai-title",
  "aiTitle": "Cultural preservation in cross-lingual LoRA fine-tuning",
  "sessionId": "a9dbecfc-cc1f-4e48-9f6b-0d066b966530"
}
```

---
