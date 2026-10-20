# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-19 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 150
- **Recorded user turns:** 1
- **Tool calls:** 48
- **Original source:** `logs/chats/exported-trajectories/account-2/3fb644f2-5f5b-4b36-aa26-243980802dbe.jsonl`
- **Structured JSON:** [`2ed4e228baac09d94270.json`](../../sessions/2e/2ed4e228baac09d94270.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T09:36:55.294Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T09:36:55.294Z",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-19 (UTC).**\n\nYour job: independently verify this idea's claims via web_search, then issue a verdict.\n\n## User requirements\nThe user asked for: **calibration**\nEvaluate whether this idea actually meets the user's requirements. An idea that doesn't match should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：用 WebFetch 实际阅读相关论文的 abstract 和关键章节。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献\n\n6. **评分诚实**：\n   - 4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} 2026` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} 2026` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} 2026 site:scholar.google.com`\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} 2026` — 按活跃作者追踪\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} 2026` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey 2026` — 找综述论文\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n\n### 搜索维度\n\n1. **正向搜索**：直接搜索主题相关论文\n2. **竞争论文搜索**（最关键！）：有没有人在解决同样的问题？用类似方法？\n3. **相邻领域搜索**：其他领域是否已解决类似问题\n4. **反面搜索**：找到反对你 idea 的证据\n5. **引用链追踪**：找到核心论文后，查看 cited-by 发现 concurrent work\n\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n2. **知名团队追踪**：搜索相关团队最近的论文\n3. **会议最新录用**：搜索 `site:openreview.net {topic} 2026`\n4. **arXiv 近 3 个月密集搜索**\n\n## Review checklist\n1. **SOTA freshness**: Are baselines actually current SOTA?\n2. **Reference verification**: Do cited papers actually exist?\n3. **Gap validity**: Does the claimed gap still exist?\n4. **Venue validity**: Are target venue deadlines after 2026-05-19?\n5. **Feasibility**: Is the resource estimate realistic?\n6. **Novelty**: Is this sufficiently different from existing work?\n7. **Cost realism**: Are the three mode estimates internally consistent?\n\n## Idea under review (round 3/10)\n{\n  \"revision_notes\": {\n    \"issues_addressed\": [\n      \"FIXED (R2-1, MODERATE): Architecture-specific hidden state extraction now explicitly specified. Residual-stream extraction defined per architecture: post-DeltaNet/attention block for Qwen3.6-27B, post-MoE-aggregation (after expert outputs are merged) for LLaMA 4 Scout, post-attention+FFN for Aya Expanse 32B. Cited Yap (arXiv 2603.16335) demonstrating steering vectors work in Qwen 3.5's hybrid GatedDeltaNet/attention architecture with Cohen's d=1.01. Added note on AEON-7 abliteration project confirming difference-in-means extraction from residual stream works for Qwen3.6-27B with differential treatment of DeltaNet vs attention layers.\",\n      \"FIXED (R2-2, MODERATE): Explicit layer-depth mapping table added. Hypothesized calibration zones at ~88-94% depth: Qwen3.6-27B layers 56-60/64, LLaMA 4 Scout layers 42-45/48, Aya Expanse 32B layers 35-38/40. Language-agnostic zone (~50% depth) comparison points also mapped: Qwen3.6 layer 32, Scout layer 24, Aya layer 20.\",\n      \"FIXED (R2-3, MINOR): Statistical power for ECE estimation addressed. Bootstrap confidence intervals (BCa, 1000 resamples) will be reported for all per-language ECE estimates. Languages with <200 Belebele samples flagged as low-reliability. Adaptive binning (equal-mass bins) used instead of fixed-width bins to mitigate small-sample bin sparsity. Cited Sun et al. (arXiv 2408.08998) on debiased ECE estimators.\",\n      \"FIXED (R2-4, MINOR): SteerConf (Zhou et al., arXiv 2503.02863, NeurIPS 2025) added to landscape as complementary prompt-based confidence steering approach. Positioned as orthogonal: SteerConf steers verbalized confidence via prompts while our method steers representational confidence geometry.\",\n      \"FIXED (R2-5, MINOR): Impact framing strengthened. Quantified 122× data efficiency advantage over LACE (O(1) English-only vs O(L) per-language validation sets for L=122 Belebele languages). Added Phase 6: practical selective prediction demonstration showing calibration transfer improves abstention quality on 10 low-resource languages, measuring coverage@90% accuracy and AURCC improvement over uncalibrated baselines. Framed as direct practical value for multilingual deployment.\",\n      \"ADDED: Feng et al. (arXiv 2406.15948) on multilingual abstention gaps (20.5% gap between high/low-resource languages) as motivation for selective prediction demonstration.\",\n      \"ADDED: Yap (arXiv 2603.16335) as key evidence for steering in hybrid DeltaNet/attention architectures.\",\n      \"RETAINED: All round-1 fixes remain intact.\"\n    ]\n  },\n  \"title\": \"Cross-Lingual Calibration Transfer via Shared Confidence Geometry in Late-Intermediate Layers\",\n  \"core_problem\": \"Non-English languages suffer 5× worse calibration error (ECE) compared to English in multilingual LLMs, undermining downstream deployment for selective prediction and abstention — where calibration gaps translate to 20.5% performance gaps between high- and low-resource languages (Feng et al., 2024). Can we transfer English calibration quality to 122+ other languages by exploiting the shared geometric structure of confidence directions at late-intermediate layers, achieving a 122× reduction in per-language data requirements compared to existing methods? And how does transfer effectiveness degrade with typological distance from English?\",\n  \"opportunity\": \"Three convergent lines of research remain unconnected: (1) Ji et al. (EMNLP 2025) discovered that verbal uncertainty is governed by a single linear direction in representation space; (2) Zhou et al. (arXiv 2510.03136, LACE) and Joshi et al. (EMNLP 2025) showed that late-intermediate layers (layers 28-30 in 32-layer models, ~88-94% depth) encode better-calibrated signals than the final layer — particularly for non-English languages, where the final layer reintroduces English-centric bias; (3) Wang et al. (NeurIPS 2025) demonstrated that behaviorally meaningful linear directions (refusal vectors) transfer cross-lingually with >90% effectiveness across 14 languages spanning 7 language families, using difference-in-means extraction. Nobody has tested whether the calibration confidence direction — extracted via the same contrastive methodology — similarly transfers across languages. If the confidence correction mechanism at late-intermediate layers follows a shared geometric pattern across languages (even though the representations themselves are language-specific at that depth), it can be extracted from abundant English calibration data and applied to other languages zero-shot, bypassing per-language labeled calibration sets entirely — a 122× data efficiency improvement over LACE for the full Belebele language set. Unlike refusal (which is explicitly trained multilingually via RLHF/DPO), calibration is emergent — making this transfer an open empirical question with high potential impact for practical multilingual deployment, where calibration quality directly determines selective prediction and abstention reliability.\",\n  \"landscape\": \"LACE (Zhou et al., arXiv 2510.03136) adaptively ensembles intermediate layers per language but still requires per-language validation data — O(L) labeled sets for L languages. MKA (Duwal, ICLR Workshop 2025) uses cross-lingual consensus for abstention but at 5× inference cost. Zhou et al. confirmed the 5× ECE gap across 100+ languages and 6 model families, with LLaMA-3 showing 23.1% vs. 4.6% ECE for non-English vs. English. Joshi et al. (EMNLP 2025, 'Calibration Across Layers') identified that accuracy crystallizes by layer 26 but a distinct confidence correction phase operates in layers 28-31, with a low-dimensional calibration direction whose perturbation improves ECE/MCE. CCPS (Khanmohammadi et al., EMNLP 2025) reduces ECE ~55% via perturbation-based probing but is English-only. Gupta et al. (arXiv 2601.01362, Jan 2026) showed instruction-tuning inflates confidence in low-resource languages without accuracy gains, further motivating a representation-level fix. SteerConf (Zhou et al., arXiv 2503.02863, NeurIPS 2025) steers verbalized confidence via prompt engineering — using steering prompts at varying levels to elicit conservative or optimistic confidence scores, then aggregating via a consistency measure. While effective and training-free, SteerConf operates in prompt/output space rather than representation space, requires multiple forward passes per sample, and has not been evaluated multilingually. Our approach is complementary: we steer representational confidence geometry directly at the hidden-state level in a single forward pass.\\n\\nCross-lingual direction transfer landscape: Wang et al. (arXiv 2505.17306, NeurIPS 2025) showed refusal directions are universal across 14 languages and 7 language families — the strongest evidence that linear directions can transfer cross-lingually. However, Mahmoud et al. (arXiv 2505.12584v2) found that task-performance steering vectors are largely limited to within-family transfer — cross-family transfers (e.g., Spanish→Japanese) are ineffective for task alignment. This discrepancy reflects the nature of the direction: explicitly trained behaviors (refusal) produce universal directions, while task-performance mappings are family-specific. CLaS-Bench (arXiv 2601.08331) benchmarked steering across 32 languages and found DiffMean achieves 84.5% average steering score, with typologically related languages clustering in representation space. Pokharel et al. (arXiv 2601.16390) found cross-lingual activation steering produces larger gains for languages with greater functional divergence from English.\\n\\nLayer-depth evidence: Civelli et al. (arXiv 2601.12731) found cross-lingual difficulty probes generalize best at shallow-to-middle layers (~45% depth), while Liu & Niehues (ACL 2025) showed cross-lingual semantic alignment peaks at ~50% depth. Critically, calibration is a distinct post-decisional process at much greater depth: Zhou et al. found multilingual calibration peaks at layers 28-29/32 (~88-91% depth), avoiding the English-centric bias of the final layer. This means calibration transfer operates in a fundamentally different representational regime than difficulty or semantic transfer.\\n\\nMultilingual abstention gap: Feng et al. (arXiv 2406.15948) showed that directly applying English-centric abstention methods to other languages produces up to 20.5% performance gaps between high- and low-resource languages, partly due to calibration degradation. This motivates our practical demonstration that improved calibration transfer directly improves selective prediction quality for low-resource languages.\\n\\nNo prior work has attempted to transfer calibration directions cross-lingually; all existing methods either train per-language calibrators or rely on expensive multi-lingual sampling.\",\n  \"inspired_by\": \"Gap: 5× non-English ECE gap (Zhou et al. LACE) producing 20.5% abstention performance gaps (Feng et al.). Pattern: Ji et al.'s linear calibration direction + Wang et al.'s cross-lingual universality of refusal directions + late-intermediate layer calibration optimum. Open question: do calibration directions (emergent, not explicitly trained) transfer like refusal directions (explicitly trained)? Untried combination: representation-engineering calibration transfer across languages with language-distance degradation analysis and practical selective prediction demonstration.\",\n  \"approach\": \"**Phase 1 — Direction Extraction.** Extract a confidence/calibration direction from English-labeled data using contrastive difference-in-means on hidden states from correct vs. incorrect model answers, following Wang et al.'s methodology. Compute this at every layer independently to identify the optimal extraction layer.\\n\\n**Phase 2 — Systematic Layer Sweep (Primary Experiment).** For each of 3 model families, sweep all layers to test calibration direction transfer, with three hypothesized zones of interest:\\n\\n| Zone | Description | Qwen3.6-27B (64L) | LLaMA 4 Scout (48L) | Aya Expanse 32B (40L) |\\n|------|-------------|-------------------|---------------------|----------------------|\\n| A: Language-agnostic (~50% depth) | Cross-lingual semantic alignment peak (Civelli et al.; Liu & Niehues) | Layer 32 | Layer 24 | Layer 20 |\\n| B: Calibration zone (~88-94% depth) | Multilingual calibration peak (Zhou et al.; Joshi et al.) | Layers 56-60 | Layers 42-45 | Layers 35-38 |\\n| C: Final layer | English-centric bias zone | Layer 64 | Layer 48 | Layer 40 |\\n\\nThis resolves the shallow-vs-late-intermediate layer debate for calibration transfer specifically, as a primary rather than ablation contribution.\\n\\n**Phase 3 — Architecture-Specific Hidden State Extraction.** Hidden states are extracted from the residual stream at each layer boundary, but the three target architectures require architecture-aware extraction:\\n\\n- *Qwen3.6-27B (hybrid DeltaNet/attention)*: The 64-layer network uses 16 repeated blocks of (3 × Gated DeltaNet → FFN, 1 × Gated Attention → FFN). We extract from the residual stream after each complete sub-layer (DeltaNet+FFN or Attention+FFN). Yap (arXiv 2603.16335) demonstrated that steering vectors achieve Cohen's d = 1.01 (p < 0.0001) in the closely related Qwen 3.5-35B-A3B hybrid GatedDeltaNet/attention architecture, confirming that contrastive direction extraction from the residual stream works despite the non-standard attention mechanism. Following the AEON-7 abliteration methodology for Qwen3.6-27B, we extract directions from residual-stream activations, noting that DeltaNet layers and attention layers may contribute differently to the calibration direction — an ablation we explicitly test by comparing directions extracted from DeltaNet-only vs. attention-only layer subsets.\\n\\n- *LLaMA 4 Scout (MoE, 16 experts)*: Each of the 48 transformer blocks contains a standard attention layer followed by a MoE feed-forward layer with 16 experts and top-k routing. We extract hidden states from the residual stream after the full MoE block (post-expert-aggregation), where the routed expert outputs have already been merged. This is the standard extraction point for representation engineering in MoE models, as the post-aggregation residual captures the combined expert contribution. We verify extraction consistency by also testing pre-MoE (post-attention) extraction as an ablation.\\n\\n- *Aya Expanse 32B (dense transformer)*: Standard 40-layer dense transformer with hidden dimension 8192. Extraction follows the conventional post-layer residual stream approach with no architecture-specific considerations.\\n\\n**Phase 4 — Cross-Lingual Transfer Evaluation.** Apply the English-derived calibration direction zero-shot to target languages by projecting their hidden-state activations onto it to obtain calibrated confidence scores. Primary 100+ language evaluation uses Belebele (122 language variants); focused multi-benchmark evaluation on a 14-language subset (matching MMMLU coverage) across MMMLU, XQuAD (11 languages), and MLQA (7 languages). Compare against LACE (with per-language validation data), MKA, CCPS, temperature scaling, SteerConf, and verbalized-confidence baselines.\\n\\n**Statistical reliability:** Per-language ECE estimates are computed using adaptive equal-mass binning (rather than fixed-width bins) to mitigate small-sample bin sparsity — Belebele provides ~900 samples per language, yielding ~90 samples per bin with 10 bins. We report bias-corrected and accelerated (BCa) bootstrap confidence intervals (1000 resamples) for all ECE estimates following Sun et al. (arXiv 2408.08998). Languages with <200 samples or bootstrap CI width >0.10 are flagged as low-reliability and excluded from primary transfer curve analysis but reported in supplementary materials. We additionally report the debiased ℓ₂ ECE estimator to account for finite-sample bias.\\n\\n**Phase 5 — Language-Distance Degradation Analysis (Key Contribution).** Plot ECE improvement (Δ ECE relative to uncalibrated baseline) as a function of typological distance from English, computed using URIEL+ typological features (syntactic, phonological, genetic, geographic). Stratify by language family (Indo-European, Sino-Tibetan, Japonic, Koreanic, Afroasiatic, Dravidian, Austronesian, Niger-Congo, Turkic, etc.) to quantify the within-family vs. cross-family transfer gap for calibration specifically. This directly addresses Mahmoud et al.'s finding that task-performance steering fails cross-family — if calibration transfer shows a similar family boundary, we characterize it precisely; if it shows a smoother gradient (as refusal directions do), we provide evidence that calibration directions are more universal than task-alignment directions.\\n\\n**Phase 6 — Selective Prediction Demonstration (Practical Impact).** To demonstrate concrete deployment value, we apply the transferred calibration directions to selective prediction (abstention) on 10 low-resource languages spanning 5 language families, selected from the Belebele set. Using the calibrated confidence scores as the selection function, we measure: (a) coverage@90% accuracy — the fraction of queries the model can answer while maintaining ≥90% accuracy, (b) Area Under the Risk-Coverage Curve (AURCC), and (c) the abstention performance gap between high- and low-resource languages (following Feng et al.'s 20.5% gap metric). We compare against: uncalibrated softmax probability, temperature-scaled confidence, LACE (with per-language data), and MKA (with 5× inference cost). The hypothesis is that zero-shot calibration transfer closes a substantial portion of the abstention performance gap without any target-language labeled data, providing a training-free, single-pass alternative to existing methods for multilingual selective prediction.\\n\\n**Phase 7 — Ablations and Analysis.** (a) Cosine similarity heatmaps of calibration directions extracted independently from different languages (following Wang et al.'s refusal direction analysis) to test if calibration directions are geometrically parallel across languages. (b) Per-language-family optimal layer analysis. (c) Effect of model scale and architecture (dense Qwen3.6 vs. MoE LLaMA 4 vs. dense Aya). (d) Comparison of calibration direction extraction methods: difference-in-means, PCA, and CCPS perturbation-based probing. (e) DeltaNet-only vs. attention-only layer subsets for direction extraction in Qwen3.6. (f) Pre-MoE vs. post-MoE extraction points in LLaMA 4 Scout.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"400–550 H100\",\n      \"timeline\": \"11–13 weeks\",\n      \"estimated_gpu_cost\": \"$1000–1375 (H100 at ~$2.50/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"400–550 H100\",\n      \"timeline\": \"8–9 weeks\",\n      \"claude_api_cost\": \"$120–180\",\n      \"estimated_gpu_cost\": \"$1000–1375\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"400–550 H100\",\n      \"timeline\": \"5–6 weeks\",\n      \"claude_api_cost\": \"$200–350\",\n      \"estimated_gpu_cost\": \"$1000–1375\",\n      \"speed_bottleneck\": \"Sequential full forward passes with hidden-state extraction across 122 Belebele languages × 3 model families × all layers; LLaMA 4 Scout requires 4×H100 at BF16 for full hidden-state extraction (109B total parameters). Qwen3.6-27B requires 2×H100 at BF16 (27B dense, hidden dim 5120 across 64 layers). Phase 6 selective prediction adds ~50 GPU-hours for 10-language focused evaluation. Parallelizable across models but sequential within each model's language passes.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract Jul 21, full paper Jul 28 2026 — best fit, ~10 weeks runway)\",\n    \"EACL 2027 (ARR August cycle, submission Aug 3 2026 — 11 weeks runway)\",\n    \"NAACL 2027 (ARR October cycle — 20 weeks runway, allows thorough experimentation)\"\n  ],\n  \"level\": \"strong\",\n  \"key_references\": [\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations — Ji et al. (EMNLP 2025)\",\n    \"Calibration Across Layers: Understanding Calibration Evolution in LLMs — Joshi, Ahmad & Modi (EMNLP 2025)\",\n    \"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models — Zhou et al. (arXiv 2510.03136, 2025) [LACE]\",\n    \"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs — Liu & Niehues (ACL 2025)\",\n    \"Refusal Direction is Universal Across Safety-Aligned Languages — Wang et al. (arXiv 2505.17306, NeurIPS 2025)\",\n    \"SteerConf: Steering LLMs for Confidence Elicitation — Zhou, Jin, Shi & Li (arXiv 2503.02863, NeurIPS 2025)\",\n    \"Improving Multilingual Language Models by Aligning Representations through Steering — Mahmoud et al. (arXiv 2505.12584v2, 2025)\",\n    \"CLaS-Bench: A Benchmark for Cross-Lingual Activation Steering — arXiv 2601.08331 (2026)\",\n    \"Cross-Lingual Activation Steering — Pokharel et al. (arXiv 2601.16390, 2026)\",\n    \"A Shared Geometry of Difficulty in Multilingual Language Models — Civelli, Bernardelle, Brunello & Demartini (arXiv 2601.12731, 2026)\",\n    \"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning — Gupta et al. (arXiv 2601.01362, 2026)\",\n    \"Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM — Chimoto et al. (EACL 2026)\",\n    \"MKA: Leveraging Cross-Lingual Consensus for Model Abstention — Duwal (ICLR Workshop 2025)\",\n    \"Calibrating LLM Confidence by Probing Perturbed Representation Stability — Khanmohammadi et al. (EMNLP 2025) [CCPS]\",\n    \"Language Steering for Multilingual In-Context Learning — Kirtane & Huang (arXiv 2602.02326, 2026)\",\n    \"Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits — Yap (arXiv 2603.16335, 2026)\",\n    \"Teaching LLMs to Abstain across Languages via Multilingual Feedback — Feng et al. (arXiv 2406.15948, 2024)\",\n    \"A Confidence Interval for the ℓ₂ Expected Calibration Error — Sun, Chaudhari, Barnett & Dobriban (arXiv 2408.08998, 2024)\"\n  ],\n  \"description\": \"Non-English languages suffer 5× worse calibration error (ECE) than English in multilingual LLMs, yet existing remedies demand per-language labeled data (LACE) or expensive multi-pass inference (MKA). For the 122 languages in Belebele, LACE requires 122 separate validation sets — we propose reducing this to a single English-only calibration set, a 122× data efficiency improvement. We investigate whether an English-derived confidence direction — extracted via contrastive difference-in-means from the residual stream at late-intermediate model layers — can transfer zero-shot to improve calibration across languages. Our approach is motivated by three converging findings: (1) verbal uncertainty follows a single linear direction in representation space (Ji et al., EMNLP 2025), (2) multilingual calibration peaks at late-intermediate layers (~88-94% depth) that avoid English-centric final-layer bias (Zhou et al., 2025; Joshi et al., EMNLP 2025), and (3) behaviorally meaningful linear directions such as refusal vectors transfer with >90% effectiveness across 7 language families (Wang et al., NeurIPS 2025). We critically note that cross-family transfer of task-performance steering vectors is limited (Mahmoud et al., 2025), making the transferability of calibration directions — which are emergent rather than explicitly trained — an open empirical question.\\n\\nWe conduct a systematic layer sweep across three architecturally diverse model families — Qwen3.6-27B (64-layer hybrid GatedDeltaNet/attention dense model), LLaMA 4 Scout (48-layer MoE with 16 experts, 17B active/109B total), and Aya Expanse 32B (40-layer dense transformer) — with architecture-specific extraction from the residual stream (post-DeltaNet/attention block, post-MoE-aggregation, and post-FFN respectively). Recent work confirms that steering vectors are effective in hybrid DeltaNet/attention architectures (Yap, arXiv 2603.16335, Cohen's d = 1.01 in Qwen 3.5-35B). We evaluate on Belebele (122 languages) for broad coverage and MMMLU (14 languages), XQuAD (11), and MLQA (7) for multi-benchmark depth, with bootstrap confidence intervals for all per-language ECE estimates. A central analytical contribution is the language-distance calibration transfer curve: plotting ECE improvement against URIEL+ typological distance from English to map the typological boundary of calibration direction universality. As a practical deployment demonstration, we show that zero-shot calibration transfer improves selective prediction (abstention) on low-resource languages, directly addressing the 20.5% abstention performance gap between high- and low-resource languages (Feng et al., 2024). This is the first work to (a) transfer calibration directions cross-lingually, (b) map their typological transfer boundary, and (c) demonstrate practical selective prediction gains from training-free cross-lingual calibration — requiring only English-labeled data and a single forward pass.\",\n  \"project_name\": \"xlingual_cal_transfer\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: Author attribution error — arXiv 2601.12731 is by Civelli, Bernardelle, Brunello & Demartini, NOT 'Patel et al.' This casts doubt on the thoroughness of reference checking.\", \"KEY RISK UNACKNOWLEDGED: Cross-lingual steering transfer is 'largely limited to languages within the same linguistic family' and 'cross-family transfers such as from Spanish to Japanese are ineffective' (arXiv 2505.12584v2). The idea does not discuss this critical limitation despite claiming 100+ language coverage.\", \"LAYER DISCREPANCY: Civelli et al. (arXiv 2601.12731) found cross-lingual generalization of difficulty probes works best at SHALLOW layers, while the proposed approach assumes INTERMEDIATE layers are optimal. This contradicts the foundational hypothesis without acknowledgment.\", \"BENCHMARK COVERAGE MISMATCH: Claiming '100+ languages' evaluation is misleading—only Belebele (122 languages) provides that coverage. MMMLU covers only 14 languages, XQuAD ~11, MLQA ~7. The idea should be transparent about per-benchmark language coverage.\", \"RESOURCE UNDERESTIMATE: LLaMA 4 Scout requires 4×H100 for full-weight inference with hidden state extraction. At ~110K Belebele samples alone (900 × 122 languages), forward passes across 3 models × multiple benchmarks × multiple layers likely require 300–500 H100 GPU hours, not 150–200.\", \"LACE ATTRIBUTION CONFUSION: The opportunity section says 'Joshi et al. (EMNLP 2025, LACE)' but LACE (Language-Aware Confidence Ensemble) is from Zhou et al. (arXiv 2510.03136). Joshi et al.'s paper is 'Calibration Across Layers' — distinct from LACE.\", \"MISSING RELEVANT WORK: The paper 'Refusal Direction is Universal Across Safety-Aligned Languages' (arXiv 2505.17306) provides strong supporting evidence that some representation directions transfer cross-lingually (across 14 languages). This should be cited as supporting evidence while noting the domain difference (refusal ≠ calibration).\", \"AACL 2026 TARGET UNREALISTIC: ARR May 25 deadline is 6 days away; listing it as a viable target is misleading.\"]\nFeedback: The core idea is novel and well-motivated, but needs significant revisions: (1) Fix the Civelli et al. author attribution error. (2) Fix the LACE/Joshi attribution confusion. (3) Explicitly acknowledge the cross-family steering transfer limitation as a key risk and adjust the framing—the method will likely work best for languages typologically close to English and degrade for distant families. Design the experiments to test this gradient explicitly. (4) Reconcile the shallow-vs-intermediate layer discrepancy: Civelli et al. found shallow layers generalize best cross-lingually for difficulty, while you hypothesize intermediate layers. Either argue why calibration differs from difficulty, or propose a systematic layer sweep as a key experiment. (5) Revise resource estimates to 300–500 H100 GPU hours. (6) Be transparent about per-benchmark language coverage rather than uniformly claiming '100+ languages.' (7) Add arXiv 2505.17306 (refusal direction universality) as supporting evidence. (8) Drop AACL 2026 as a target venue. (9) Consider a focused 'language distance' analysis: plot ECE improvement vs. typological distance from English to quantify the transfer degradation curve—this would be a strong contribution even if transfer fails for distant languages.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MODERATE: Architecture-specific hidden state extraction not discussed. Qwen3.6-27B uses a hybrid DeltaNet/attention architecture (75% DeltaNet layers) with fundamentally different information flow than standard transformers. LLaMA 4 Scout is MoE with 16 experts — hidden states before vs. after expert routing differ semantically. The experimental design must specify extraction points. Cite arXiv 2603.16335 (March 2026) as evidence steering vectors work in Qwen 3.5 DeltaNet/attention hybrids.\", \"MODERATE: Layer depth mapping across architectures is implicit. The '28-30/32 (~88-94% depth)' framework comes from 32-layer models, but the target models have 48 (Scout), 64 (Qwen3.6), and 40 (Aya) layers. The systematic layer sweep handles this experimentally, but the experimental design should include an explicit depth-percentage mapping table showing hypothesized optimal layers per model.\", \"MINOR: Statistical power for ECE estimation with 900 Belebele samples per language is not discussed. With 10 ECE bins, ~90 samples per bin produces noisy estimates for some languages. Consider reporting bootstrap confidence intervals and discussing reliability thresholds.\", \"MINOR: SteerConf (Zhou et al., arXiv 2503.02863, NeurIPS 2025) is not cited despite being the most relevant confidence-steering paper at NeurIPS 2025. While it's prompt-based rather than representation-based, it's close enough to warrant acknowledgment in the landscape.\", \"MINOR: Impact framing could be stronger. The hedged framing ('the core hypothesis might be false, and that's informative') is honest but undersells the practical value. Explicitly quantify the practical gain: LACE requires O(L) per-language validation sets; this method requires O(1) English-only data. For 122 Belebele languages, that's a concrete 122× data efficiency improvement if transfer works.\"]\nFeedback: The revision is very responsive — all 8 round-1 issues are addressed thoroughly, and the reframing of the layer hypothesis and cross-family transfer risk is intellectually rigorous. The idea is close to passing. To get there: (1) Add a paragraph on architecture-specific considerations: specify that hidden states are extracted from the residual stream (post-MoE block for Scout, post-DeltaNet/attention block for Qwen3.6), and cite arXiv 2603.16335 as evidence that steering vectors work in DeltaNet hybrids. (2) Include an explicit layer-mapping table: Scout layers 42-45/48, Qwen3.6 layers 56-60/64, Aya layers 35-38/40 as hypothesized calibration zones at ~88-94% depth. (3) Add SteerConf to related work. (4) Strengthen the impact framing by quantifying the data efficiency advantage over LACE (122× reduction in per-language data requirements). (5) The impact score is the binding constraint — consider whether the contribution can be elevated by adding a practical deployment demonstration (e.g., using the transferred calibration direction to improve selective prediction/abstention on low-resource languages).\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"...\"}\n  },\n  \"issues\": [\"specific issue 1\", ...],\n  \"feedback\": \"Actionable feedback (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold\n- \"fail\": fundamental flaw (gap doesn't exist, approach provably wrong)\n- Threshold is HIGH (4.0/5.0): only truly outstanding ideas should pass.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-19T09:36:55.298Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T09:36:55.298Z",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

## Round 1

148 recorded events

### User

_source line 3 · 2026-05-19T09:36:55.311Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-19 (UTC).**

Your job: independently verify this idea's claims via web_search, then issue a verdict.

## User requirements
The user asked for: **calibration**
Evaluate whether this idea actually meets the user's requirements. An idea that doesn't match should be "revise" or "fail".

## 核心要求：非常仔细地调研，非常仔细地思考

你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证。

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

4. **深入阅读**：用 WebFetch 实际阅读相关论文的 abstract 和关键章节。

### 思考要求

5. **独立判断**：
   - 不要因为 Generator 说得有道理就轻易 pass
   - 思考这个 idea 在实际执行中会遇到什么困难
   - 考虑这个 idea 对领域的真实贡献

6. **评分诚实**：
   - 4 分意味着"确实很好"，5 分意味着"令人兴奋"
   - Agent 评分经常虚高，你的职责就是纠正这种偏差


## 论文搜索策略

你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。

### 搜索源（推荐每个维度使用 2 个不同来源）

1. **arXiv 预印本**（最新工作）:
   - `site:arxiv.org {topic} 2026` — 按主题搜索最新论文
   - `site:arxiv.org {method_name}` — 按具体方法名搜索
   - `arxiv {topic} {month} 2026` — 精确到月份，找最近 3 个月的工作

2. **Google Scholar**（引用关系 + 综合覆盖）:
   - `{topic} 2026 site:scholar.google.com`
   - `"{exact paper title}"` — 验证论文是否真实存在
   - `"{author name}" {topic} 2026` — 按活跃作者追踪

3. **Papers With Code**（SOTA 排行 + 代码可用性）:
   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜
   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局

4. **OpenReview**（会议审稿 + 同行评价）:
   - `site:openreview.net {topic} 2026` — 搜索会议提交的论文
   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价

5. **Semantic Scholar**（语义搜索 + 引用图谱）:
   - `semantic scholar {topic} survey 2026` — 找综述论文

6. **GitHub**（实现验证）:
   - `site:github.com {method_name} {task}` — 验证开源实现是否存在

### 搜索维度

1. **正向搜索**：直接搜索主题相关论文
2. **竞争论文搜索**（最关键！）：有没有人在解决同样的问题？用类似方法？
3. **相邻领域搜索**：其他领域是否已解决类似问题
4. **反面搜索**：找到反对你 idea 的证据
5. **引用链追踪**：找到核心论文后，查看 cited-by 发现 concurrent work


## 竞争论文专项搜索（Reviewer 独有）

1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题
2. **知名团队追踪**：搜索相关团队最近的论文
3. **会议最新录用**：搜索 `site:openreview.net {topic} 2026`
4. **arXiv 近 3 个月密集搜索**

## Review checklist
1. **SOTA freshness**: Are baselines actually current SOTA?
2. **Reference verification**: Do cited papers actually exist?
3. **Gap validity**: Does the claimed gap still exist?
4. **Venue validity**: Are target venue deadlines after 2026-05-19?
5. **Feasibility**: Is the resource estimate realistic?
6. **Novelty**: Is this sufficiently different from existing work?
7. **Cost realism**: Are the three mode estimates internally consistent?

## Idea under review (round 3/10)
{
  "revision_notes": {
    "issues_addressed": [
      "FIXED (R2-1, MODERATE): Architecture-specific hidden state extraction now explicitly specified. Residual-stream extraction defined per architecture: post-DeltaNet/attention block for Qwen3.6-27B, post-MoE-aggregation (after expert outputs are merged) for LLaMA 4 Scout, post-attention+FFN for Aya Expanse 32B. Cited Yap (arXiv 2603.16335) demonstrating steering vectors work in Qwen 3.5's hybrid GatedDeltaNet/attention architecture with Cohen's d=1.01. Added note on AEON-7 abliteration project confirming difference-in-means extraction from residual stream works for Qwen3.6-27B with differential treatment of DeltaNet vs attention layers.",
      "FIXED (R2-2, MODERATE): Explicit layer-depth mapping table added. Hypothesized calibration zones at ~88-94% depth: Qwen3.6-27B layers 56-60/64, LLaMA 4 Scout layers 42-45/48, Aya Expanse 32B layers 35-38/40. Language-agnostic zone (~50% depth) comparison points also mapped: Qwen3.6 layer 32, Scout layer 24, Aya layer 20.",
      "FIXED (R2-3, MINOR): Statistical power for ECE estimation addressed. Bootstrap confidence intervals (BCa, 1000 resamples) will be reported for all per-language ECE estimates. Languages with <200 Belebele samples flagged as low-reliability. Adaptive binning (equal-mass bins) used instead of fixed-width bins to mitigate small-sample bin sparsity. Cited Sun et al. (arXiv 2408.08998) on debiased ECE estimators.",
      "FIXED (R2-4, MINOR): SteerConf (Zhou et al., arXiv 2503.02863, NeurIPS 2025) added to landscape as complementary prompt-based confidence steering approach. Positioned as orthogonal: SteerConf steers verbalized confidence via prompts while our method steers representational confidence geometry.",
      "FIXED (R2-5, MINOR): Impact framing strengthened. Quantified 122× data efficiency advantage over LACE (O(1) English-only vs O(L) per-language validation sets for L=122 Belebele languages). Added Phase 6: practical selective prediction demonstration showing calibration transfer improves abstention quality on 10 low-resource languages, measuring coverage@90% accuracy and AURCC improvement over uncalibrated baselines. Framed as direct practical value for multilingual deployment.",
      "ADDED: Feng et al. (arXiv 2406.15948) on multilingual abstention gaps (20.5% gap between high/low-resource languages) as motivation for selective prediction demonstration.",
      "ADDED: Yap (arXiv 2603.16335) as key evidence for steering in hybrid DeltaNet/attention architectures.",
      "RETAINED: All round-1 fixes remain intact."
    ]
  },
  "title": "Cross-Lingual Calibration Transfer via Shared Confidence Geometry in Late-Intermediate Layers",
  "core_problem": "Non-English languages suffer 5× worse calibration error (ECE) compared to English in multilingual LLMs, undermining downstream deployment for selective prediction and abstention — where calibration gaps translate to 20.5% performance gaps between high- and low-resource languages (Feng et al., 2024). Can we transfer English calibration quality to 122+ other languages by exploiting the shared geometric structure of confidence directions at late-intermediate layers, achieving a 122× reduction in per-language data requirements compared to existing methods? And how does transfer effectiveness degrade with typological distance from English?",
  "opportunity": "Three convergent lines of research remain unconnected: (1) Ji et al. (EMNLP 2025) discovered that verbal uncertainty is governed by a single linear direction in representation space; (2) Zhou et al. (arXiv 2510.03136, LACE) and Joshi et al. (EMNLP 2025) showed that late-intermediate layers (layers 28-30 in 32-layer models, ~88-94% depth) encode better-calibrated signals than the final layer — particularly for non-English languages, where the final layer reintroduces English-centric bias; (3) Wang et al. (NeurIPS 2025) demonstrated that behaviorally meaningful linear directions (refusal vectors) transfer cross-lingually with >90% effectiveness across 14 languages spanning 7 language families, using difference-in-means extraction. Nobody has tested whether the calibration confidence direction — extracted via the same contrastive methodology — similarly transfers across languages. If the confidence correction mechanism at late-intermediate layers follows a shared geometric pattern across languages (even though the representations themselves are language-specific at that depth), it can be extracted from abundant English calibration data and applied to other languages zero-shot, bypassing per-language labeled calibration sets entirely — a 122× data efficiency improvement over LACE for the full Belebele language set. Unlike refusal (which is explicitly trained multilingually via RLHF/DPO), calibration is emergent — making this transfer an open empirical question with high potential impact for practical multilingual deployment, where calibration quality directly determines selective prediction and abstention reliability.",
  "landscape": "LACE (Zhou et al., arXiv 2510.03136) adaptively ensembles intermediate layers per language but still requires per-language validation data — O(L) labeled sets for L languages. MKA (Duwal, ICLR Workshop 2025) uses cross-lingual consensus for abstention but at 5× inference cost. Zhou et al. confirmed the 5× ECE gap across 100+ languages and 6 model families, with LLaMA-3 showing 23.1% vs. 4.6% ECE for non-English vs. English. Joshi et al. (EMNLP 2025, 'Calibration Across Layers') identified that accuracy crystallizes by layer 26 but a distinct confidence correction phase operates in layers 28-31, with a low-dimensional calibration direction whose perturbation improves ECE/MCE. CCPS (Khanmohammadi et al., EMNLP 2025) reduces ECE ~55% via perturbation-based probing but is English-only. Gupta et al. (arXiv 2601.01362, Jan 2026) showed instruction-tuning inflates confidence in low-resource languages without accuracy gains, further motivating a representation-level fix. SteerConf (Zhou et al., arXiv 2503.02863, NeurIPS 2025) steers verbalized confidence via prompt engineering — using steering prompts at varying levels to elicit conservative or optimistic confidence scores, then aggregating via a consistency measure. While effective and training-free, SteerConf operates in prompt/output space rather than representation space, requires multiple forward passes per sample, and has not been evaluated multilingually. Our approach is complementary: we steer representational confidence geometry directly at the hidden-state level in a single forward pass.\n\nCross-lingual direction transfer landscape: Wang et al. (arXiv 2505.17306, NeurIPS 2025) showed refusal directions are universal across 14 languages and 7 language families — the strongest evidence that linear directions can transfer cross-lingually. However, Mahmoud et al. (arXiv 2505.12584v2) found that task-performance steering vectors are largely limited to within-family transfer — cross-family transfers (e.g., Spanish→Japanese) are ineffective for task alignment. This discrepancy reflects the nature of the direction: explicitly trained behaviors (refusal) produce universal directions, while task-performance mappings are family-specific. CLaS-Bench (arXiv 2601.08331) benchmarked steering across 32 languages and found DiffMean achieves 84.5% average steering score, with typologically related languages clustering in representation space. Pokharel et al. (arXiv 2601.16390) found cross-lingual activation steering produces larger gains for languages with greater functional divergence from English.\n\nLayer-depth evidence: Civelli et al. (arXiv 2601.12731) found cross-lingual difficulty probes generalize best at shallow-to-middle layers (~45% depth), while Liu & Niehues (ACL 2025) showed cross-lingual semantic alignment peaks at ~50% depth. Critically, calibration is a distinct post-decisional process at much greater depth: Zhou et al. found multilingual calibration peaks at layers 28-29/32 (~88-91% depth), avoiding the English-centric bias of the final layer. This means calibration transfer operates in a fundamentally different representational regime than difficulty or semantic transfer.\n\nMultilingual abstention gap: Feng et al. (arXiv 2406.15948) showed that directly applying English-centric abstention methods to other languages produces up to 20.5% performance gaps between high- and low-resource languages, partly due to calibration degradation. This motivates our practical demonstration that improved calibration transfer directly improves selective prediction quality for low-resource languages.\n\nNo prior work has attempted to transfer calibration directions cross-lingually; all existing methods either train per-language calibrators or rely on expensive multi-lingual sampling.",
  "inspired_by": "Gap: 5× non-English ECE gap (Zhou et al. LACE) producing 20.5% abstention performance gaps (Feng et al.). Pattern: Ji et al.'s linear calibration direction + Wang et al.'s cross-lingual universality of refusal directions + late-intermediate layer calibration optimum. Open question: do calibration directions (emergent, not explicitly trained) transfer like refusal directions (explicitly trained)? Untried combination: representation-engineering calibration transfer across languages with language-distance degradation analysis and practical selective prediction demonstration.",
  "approach": "**Phase 1 — Direction Extraction.** Extract a confidence/calibration direction from English-labeled data using contrastive difference-in-means on hidden states from correct vs. incorrect model answers, following Wang et al.'s methodology. Compute this at every layer independently to identify the optimal extraction layer.\n\n**Phase 2 — Systematic Layer Sweep (Primary Experiment).** For each of 3 model families, sweep all layers to test calibration direction transfer, with three hypothesized zones of interest:\n\n| Zone | Description | Qwen3.6-27B (64L) | LLaMA 4 Scout (48L) | Aya Expanse 32B (40L) |\n|------|-------------|-------------------|---------------------|----------------------|\n| A: Language-agnostic (~50% depth) | Cross-lingual semantic alignment peak (Civelli et al.; Liu & Niehues) | Layer 32 | Layer 24 | Layer 20 |\n| B: Calibration zone (~88-94% depth) | Multilingual calibration peak (Zhou et al.; Joshi et al.) | Layers 56-60 | Layers 42-45 | Layers 35-38 |\n| C: Final layer | English-centric bias zone | Layer 64 | Layer 48 | Layer 40 |\n\nThis resolves the shallow-vs-late-intermediate layer debate for calibration transfer specifically, as a primary rather than ablation contribution.\n\n**Phase 3 — Architecture-Specific Hidden State Extraction.** Hidden states are extracted from the residual stream at each layer boundary, but the three target architectures require architecture-aware extraction:\n\n- *Qwen3.6-27B (hybrid DeltaNet/attention)*: The 64-layer network uses 16 repeated blocks of (3 × Gated DeltaNet → FFN, 1 × Gated Attention → FFN). We extract from the residual stream after each complete sub-layer (DeltaNet+FFN or Attention+FFN). Yap (arXiv 2603.16335) demonstrated that steering vectors achieve Cohen's d = 1.01 (p < 0.0001) in the closely related Qwen 3.5-35B-A3B hybrid GatedDeltaNet/attention architecture, confirming that contrastive direction extraction from the residual stream works despite the non-standard attention mechanism. Following the AEON-7 abliteration methodology for Qwen3.6-27B, we extract directions from residual-stream activations, noting that DeltaNet layers and attention layers may contribute differently to the calibration direction — an ablation we explicitly test by comparing directions extracted from DeltaNet-only vs. attention-only layer subsets.\n\n- *LLaMA 4 Scout (MoE, 16 experts)*: Each of the 48 transformer blocks contains a standard attention layer followed by a MoE feed-forward layer with 16 experts and top-k routing. We extract hidden states from the residual stream after the full MoE block (post-expert-aggregation), where the routed expert outputs have already been merged. This is the standard extraction point for representation engineering in MoE models, as the post-aggregation residual captures the combined expert contribution. We verify extraction consistency by also testing pre-MoE (post-attention) extraction as an ablation.\n\n- *Aya Expanse 32B (dense transformer)*: Standard 40-layer dense transformer with hidden dimension 8192. Extraction follows the conventional post-layer residual stream approach with no architecture-specific considerations.\n\n**Phase 4 — Cross-Lingual Transfer Evaluation.** Apply the English-derived calibration direction zero-shot to target languages by projecting their hidden-state activations onto it to obtain calibrated confidence scores. Primary 100+ language evaluation uses Belebele (122 language variants); focused multi-benchmark evaluation on a 14-language subset (matching MMMLU coverage) across MMMLU, XQuAD (11 languages), and MLQA (7 languages). Compare against LACE (with per-language validation data), MKA, CCPS, temperature scaling, SteerConf, and verbalized-confidence baselines.\n\n**Statistical reliability:** Per-language ECE estimates are computed using adaptive equal-mass binning (rather than fixed-width bins) to mitigate small-sample bin sparsity — Belebele provides ~900 samples per language, yielding ~90 samples per bin with 10 bins. We report bias-corrected and accelerated (BCa) bootstrap confidence intervals (1000 resamples) for all ECE estimates following Sun et al. (arXiv 2408.08998). Languages with <200 samples or bootstrap CI width >0.10 are flagged as low-reliability and excluded from primary transfer curve analysis but reported in supplementary materials. We additionally report the debiased ℓ₂ ECE estimator to account for finite-sample bias.\n\n**Phase 5 — Language-Distance Degradation Analysis (Key Contribution).** Plot ECE improvement (Δ ECE relative to uncalibrated baseline) as a function of typological distance from English, computed using URIEL+ typological features (syntactic, phonological, genetic, geographic). Stratify by language family (Indo-European, Sino-Tibetan, Japonic, Koreanic, Afroasiatic, Dravidian, Austronesian, Niger-Congo, Turkic, etc.) to quantify the within-family vs. cross-family transfer gap for calibration specifically. This directly addresses Mahmoud et al.'s finding that task-performance steering fails cross-family — if calibration transfer shows a similar family boundary, we characterize it precisely; if it shows a smoother gradient (as refusal directions do), we provide evidence that calibration directions are more universal than task-alignment directions.\n\n**Phase 6 — Selective Prediction Demonstration (Practical Impact).** To demonstrate concrete deployment value, we apply the transferred calibration directions to selective prediction (abstention) on 10 low-resource languages spanning 5 language families, selected from the Belebele set. Using the calibrated confidence scores as the selection function, we measure: (a) coverage@90% accuracy — the fraction of queries the model can answer while maintaining ≥90% accuracy, (b) Area Under the Risk-Coverage Curve (AURCC), and (c) the abstention performance gap between high- and low-resource languages (following Feng et al.'s 20.5% gap metric). We compare against: uncalibrated softmax probability, temperature-scaled confidence, LACE (with per-language data), and MKA (with 5× inference cost). The hypothesis is that zero-shot calibration transfer closes a substantial portion of the abstention performance gap without any target-language labeled data, providing a training-free, single-pass alternative to existing methods for multilingual selective prediction.\n\n**Phase 7 — Ablations and Analysis.** (a) Cosine similarity heatmaps of calibration directions extracted independently from different languages (following Wang et al.'s refusal direction analysis) to test if calibration directions are geometrically parallel across languages. (b) Per-language-family optimal layer analysis. (c) Effect of model scale and architecture (dense Qwen3.6 vs. MoE LLaMA 4 vs. dense Aya). (d) Comparison of calibration direction extraction methods: difference-in-means, PCA, and CCPS perturbation-based probing. (e) DeltaNet-only vs. attention-only layer subsets for direction extraction in Qwen3.6. (f) Pre-MoE vs. post-MoE extraction points in LLaMA 4 Scout.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "400–550 H100",
      "timeline": "11–13 weeks",
      "estimated_gpu_cost": "$1000–1375 (H100 at ~$2.50/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "400–550 H100",
      "timeline": "8–9 weeks",
      "claude_api_cost": "$120–180",
      "estimated_gpu_cost": "$1000–1375"
    },
    "auto_research": {
      "gpu_hours": "400–550 H100",
      "timeline": "5–6 weeks",
      "claude_api_cost": "$200–350",
      "estimated_gpu_cost": "$1000–1375",
      "speed_bottleneck": "Sequential full forward passes with hidden-state extraction across 122 Belebele languages × 3 model families × all layers; LLaMA 4 Scout requires 4×H100 at BF16 for full hidden-state extraction (109B total parameters). Qwen3.6-27B requires 2×H100 at BF16 (27B dense, hidden dim 5120 across 64 layers). Phase 6 selective prediction adds ~50 GPU-hours for 10-language focused evaluation. Parallelizable across models but sequential within each model's language passes."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract Jul 21, full paper Jul 28 2026 — best fit, ~10 weeks runway)",
    "EACL 2027 (ARR August cycle, submission Aug 3 2026 — 11 weeks runway)",
    "NAACL 2027 (ARR October cycle — 20 weeks runway, allows thorough experimentation)"
  ],
  "level": "strong",
  "key_references": [
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations — Ji et al. (EMNLP 2025)",
    "Calibration Across Layers: Understanding Calibration Evolution in LLMs — Joshi, Ahmad & Modi (EMNLP 2025)",
    "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models — Zhou et al. (arXiv 2510.03136, 2025) [LACE]",
    "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs — Liu & Niehues (ACL 2025)",
    "Refusal Direction is Universal Across Safety-Aligned Languages — Wang et al. (arXiv 2505.17306, NeurIPS 2025)",
    "SteerConf: Steering LLMs for Confidence Elicitation — Zhou, Jin, Shi & Li (arXiv 2503.02863, NeurIPS 2025)",
    "Improving Multilingual Language Models by Aligning Representations through Steering — Mahmoud et al. (arXiv 2505.12584v2, 2025)",
    "CLaS-Bench: A Benchmark for Cross-Lingual Activation Steering — arXiv 2601.08331 (2026)",
    "Cross-Lingual Activation Steering — Pokharel et al. (arXiv 2601.16390, 2026)",
    "A Shared Geometry of Difficulty in Multilingual Language Models — Civelli, Bernardelle, Brunello & Demartini (arXiv 2601.12731, 2026)",
    "Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning — Gupta et al. (arXiv 2601.01362, 2026)",
    "Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM — Chimoto et al. (EACL 2026)",
    "MKA: Leveraging Cross-Lingual Consensus for Model Abstention — Duwal (ICLR Workshop 2025)",
    "Calibrating LLM Confidence by Probing Perturbed Representation Stability — Khanmohammadi et al. (EMNLP 2025) [CCPS]",
    "Language Steering for Multilingual In-Context Learning — Kirtane & Huang (arXiv 2602.02326, 2026)",
    "Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits — Yap (arXiv 2603.16335, 2026)",
    "Teaching LLMs to Abstain across Languages via Multilingual Feedback — Feng et al. (arXiv 2406.15948, 2024)",
    "A Confidence Interval for the ℓ₂ Expected Calibration Error — Sun, Chaudhari, Barnett & Dobriban (arXiv 2408.08998, 2024)"
  ],
  "description": "Non-English languages suffer 5× worse calibration error (ECE) than English in multilingual LLMs, yet existing remedies demand per-language labeled data (LACE) or expensive multi-pass inference (MKA). For the 122 languages in Belebele, LACE requires 122 separate validation sets — we propose reducing this to a single English-only calibration set, a 122× data efficiency improvement. We investigate whether an English-derived confidence direction — extracted via contrastive difference-in-means from the residual stream at late-intermediate model layers — can transfer zero-shot to improve calibration across languages. Our approach is motivated by three converging findings: (1) verbal uncertainty follows a single linear direction in representation space (Ji et al., EMNLP 2025), (2) multilingual calibration peaks at late-intermediate layers (~88-94% depth) that avoid English-centric final-layer bias (Zhou et al., 2025; Joshi et al., EMNLP 2025), and (3) behaviorally meaningful linear directions such as refusal vectors transfer with >90% effectiveness across 7 language families (Wang et al., NeurIPS 2025). We critically note that cross-family transfer of task-performance steering vectors is limited (Mahmoud et al., 2025), making the transferability of calibration directions — which are emergent rather than explicitly trained — an open empirical question.\n\nWe conduct a systematic layer sweep across three architecturally diverse model families — Qwen3.6-27B (64-layer hybrid GatedDeltaNet/attention dense model), LLaMA 4 Scout (48-layer MoE with 16 experts, 17B active/109B total), and Aya Expanse 32B (40-layer dense transformer) — with architecture-specific extraction from the residual stream (post-DeltaNet/attention block, post-MoE-aggregation, and post-FFN respectively). Recent work confirms that steering vectors are effective in hybrid DeltaNet/attention architectures (Yap, arXiv 2603.16335, Cohen's d = 1.01 in Qwen 3.5-35B). We evaluate on Belebele (122 languages) for broad coverage and MMMLU (14 languages), XQuAD (11), and MLQA (7) for multi-benchmark depth, with bootstrap confidence intervals for all per-language ECE estimates. A central analytical contribution is the language-distance calibration transfer curve: plotting ECE improvement against URIEL+ typological distance from English to map the typological boundary of calibration direction universality. As a practical deployment demonstration, we show that zero-shot calibration transfer improves selective prediction (abstention) on low-resource languages, directly addressing the 20.5% abstention performance gap between high- and low-resource languages (Feng et al., 2024). This is the first work to (a) transfer calibration directions cross-lingually, (b) map their typological transfer boundary, and (c) demonstrate practical selective prediction gains from training-free cross-lingual calibration — requiring only English-labeled data and a single forward pass.",
  "project_name": "xlingual_cal_transfer",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL: Author attribution error — arXiv 2601.12731 is by Civelli, Bernardelle, Brunello & Demartini, NOT 'Patel et al.' This casts doubt on the thoroughness of reference checking.", "KEY RISK UNACKNOWLEDGED: Cross-lingual steering transfer is 'largely limited to languages within the same linguistic family' and 'cross-family transfers such as from Spanish to Japanese are ineffective' (arXiv 2505.12584v2). The idea does not discuss this critical limitation despite claiming 100+ language coverage.", "LAYER DISCREPANCY: Civelli et al. (arXiv 2601.12731) found cross-lingual generalization of difficulty probes works best at SHALLOW layers, while the proposed approach assumes INTERMEDIATE layers are optimal. This contradicts the foundational hypothesis without acknowledgment.", "BENCHMARK COVERAGE MISMATCH: Claiming '100+ languages' evaluation is misleading—only Belebele (122 languages) provides that coverage. MMMLU covers only 14 languages, XQuAD ~11, MLQA ~7. The idea should be transparent about per-benchmark language coverage.", "RESOURCE UNDERESTIMATE: LLaMA 4 Scout requires 4×H100 for full-weight inference with hidden state extraction. At ~110K Belebele samples alone (900 × 122 languages), forward passes across 3 models × multiple benchmarks × multiple layers likely require 300–500 H100 GPU hours, not 150–200.", "LACE ATTRIBUTION CONFUSION: The opportunity section says 'Joshi et al. (EMNLP 2025, LACE)' but LACE (Language-Aware Confidence Ensemble) is from Zhou et al. (arXiv 2510.03136). Joshi et al.'s paper is 'Calibration Across Layers' — distinct from LACE.", "MISSING RELEVANT WORK: The paper 'Refusal Direction is Universal Across Safety-Aligned Languages' (arXiv 2505.17306) provides strong supporting evidence that some representation directions transfer cross-lingually (across 14 languages). This should be cited as supporting evidence while noting the domain difference (refusal ≠ calibration).", "AACL 2026 TARGET UNREALISTIC: ARR May 25 deadline is 6 days away; listing it as a viable target is misleading."]
Feedback: The core idea is novel and well-motivated, but needs significant revisions: (1) Fix the Civelli et al. author attribution error. (2) Fix the LACE/Joshi attribution confusion. (3) Explicitly acknowledge the cross-family steering transfer limitation as a key risk and adjust the framing—the method will likely work best for languages typologically close to English and degrade for distant families. Design the experiments to test this gradient explicitly. (4) Reconcile the shallow-vs-intermediate layer discrepancy: Civelli et al. found shallow layers generalize best cross-lingually for difficulty, while you hypothesize intermediate layers. Either argue why calibration differs from difficulty, or propose a systematic layer sweep as a key experiment. (5) Revise resource estimates to 300–500 H100 GPU hours. (6) Be transparent about per-benchmark language coverage rather than uniformly claiming '100+ languages.' (7) Add arXiv 2505.17306 (refusal direction universality) as supporting evidence. (8) Drop AACL 2026 as a target venue. (9) Consider a focused 'language distance' analysis: plot ECE improvement vs. typological distance from English to quantify the transfer degradation curve—this would be a strong contribution even if transfer fails for distant languages.

### Round 2 review
Verdict: revise
Issues: ["MODERATE: Architecture-specific hidden state extraction not discussed. Qwen3.6-27B uses a hybrid DeltaNet/attention architecture (75% DeltaNet layers) with fundamentally different information flow than standard transformers. LLaMA 4 Scout is MoE with 16 experts — hidden states before vs. after expert routing differ semantically. The experimental design must specify extraction points. Cite arXiv 2603.16335 (March 2026) as evidence steering vectors work in Qwen 3.5 DeltaNet/attention hybrids.", "MODERATE: Layer depth mapping across architectures is implicit. The '28-30/32 (~88-94% depth)' framework comes from 32-layer models, but the target models have 48 (Scout), 64 (Qwen3.6), and 40 (Aya) layers. The systematic layer sweep handles this experimentally, but the experimental design should include an explicit depth-percentage mapping table showing hypothesized optimal layers per model.", "MINOR: Statistical power for ECE estimation with 900 Belebele samples per language is not discussed. With 10 ECE bins, ~90 samples per bin produces noisy estimates for some languages. Consider reporting bootstrap confidence intervals and discussing reliability thresholds.", "MINOR: SteerConf (Zhou et al., arXiv 2503.02863, NeurIPS 2025) is not cited despite being the most relevant confidence-steering paper at NeurIPS 2025. While it's prompt-based rather than representation-based, it's close enough to warrant acknowledgment in the landscape.", "MINOR: Impact framing could be stronger. The hedged framing ('the core hypothesis might be false, and that's informative') is honest but undersells the practical value. Explicitly quantify the practical gain: LACE requires O(L) per-language validation sets; this method requires O(1) English-only data. For 122 Belebele languages, that's a concrete 122× data efficiency improvement if transfer works."]
Feedback: The revision is very responsive — all 8 round-1 issues are addressed thoroughly, and the reframing of the layer hypothesis and cross-family transfer risk is intellectually rigorous. The idea is close to passing. To get there: (1) Add a paragraph on architecture-specific considerations: specify that hidden states are extracted from the residual stream (post-MoE block for Scout, post-DeltaNet/attention block for Qwen3.6), and cite arXiv 2603.16335 as evidence that steering vectors work in DeltaNet hybrids. (2) Include an explicit layer-mapping table: Scout layers 42-45/48, Qwen3.6 layers 56-60/64, Aya layers 35-38/40 as hypothesized calibration zones at ~88-94% depth. (3) Add SteerConf to related work. (4) Strengthen the impact framing by quantifying the data efficiency advantage over LACE (122× reduction in per-language data requirements). (5) The impact score is the binding constraint — consider whether the contribution can be elevated by adding a practical deployment demonstration (e.g., using the transferred calibration direction to improve selective prediction/abstention on low-resource languages).


## Output format
Output ONLY a JSON object:
{
  "verdict": "pass | revise | fail",
  "scores": {
    "novelty": {"score": 0-5, "rationale": "1-2 sentence justification"},
    "feasibility": {"score": 0-5, "rationale": "..."},
    "clarity": {"score": 0-5, "rationale": "..."},
    "impact": {"score": 0-5, "rationale": "..."}
  },
  "issues": ["specific issue 1", ...],
  "feedback": "Actionable feedback (if verdict=revise)",
  "reason": "One-line summary of verdict rationale"
}

Rules:
- "pass": sound AND high quality — avg score >= 4.0, no critical issues
- "revise": fixable issues OR scores below threshold
- "fail": fundamental flaw (gap doesn't exist, approach provably wrong)
- Threshold is HIGH (4.0/5.0): only truly outstanding ideas should pass.
- Round 10 only: if still "revise", you MUST choose "pass" or "fail".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "d06b9d70-af63-41bc-88b1-2f216b70c256",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T09:36:55.310Z_

```json
{
  "parentUuid": "d06b9d70-af63-41bc-88b1-2f216b70c256",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "c060a1da-1ae0-47c4-853a-7471c3b2d8a6",
  "timestamp": "2026-05-19T09:36:55.310Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T09:36:55.310Z_

```json
{
  "parentUuid": "c060a1da-1ae0-47c4-853a-7471c3b2d8a6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "81f3ec8e-8ae6-487a-b805-adedc05d084b",
  "timestamp": "2026-05-19T09:36:55.310Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "81f3ec8e-8ae6-487a-b805-adedc05d084b",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Assistant

_source line 8 · 2026-05-19T09:37:04.266Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea by independently verifying its claims through web searches. This is round 3/10, and the idea has been revised twice already. I need to be thorough and strict.

Let me start by verifying the key claims and references, checking for competing work, and assessing feasibility.

Key claims to verify:
1. 5× worse ECE for non-English languages (Zhou et al., LACE)
2. Ji et al. (EMNLP 2025) - linear calibration direction
3. Wang et al. (NeurIPS 2025) - refusal direction universality


4. Mahmoud et al. - cross-family transfer limitations
5. Yap (arXiv 2603.16335) - steering in DeltaNet/attention hybrids
6. Feng et al. - 20.5% abstention gap
7. SteerConf (Zhou et al., NeurIPS 2025)
8. CLaS-Bench, Pokharel et al., Civelli et al.
9. Target venue deadlines
10. Whether anyone has done cross-lingual calibration transfer via representation engineering

I need to search systematically through these references to validate the core claims and identify any existing work that overlaps with this approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81f3ec8e-8ae6-487a-b805-adedc05d084b",
  "isSidechain": false,
  "requestId": "req_011CbBhgArrbZBCgRvZmvJoD",
  "type": "assistant",
  "uuid": "d90a227d-1dab-4c19-9c40-f5b286829709",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjScoyYe156izcTZrjPhHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11048,
      "cache_read_input_tokens": 11374,
      "output_tokens": 401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11048,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 401,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 11048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11048
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-19T09:37:04.269Z_

I'll conduct a thorough independent review of this idea. Let me start with parallel searches to verify key claims, references, and check for competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d90a227d-1dab-4c19-9c40-f5b286829709",
  "isSidechain": false,
  "requestId": "req_011CbBhgArrbZBCgRvZmvJoD",
  "type": "assistant",
  "uuid": "fd02a887-59a5-445a-9b3f-d41839c0a8c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjScoyYe156izcTZrjPhHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11048,
      "cache_read_input_tokens": 11374,
      "output_tokens": 401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11048,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 401,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 11048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11048
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T09:37:04.577Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01J5XPsFB2BbWhwKDo4s9e3T`</summary>

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
  "parentUuid": "fd02a887-59a5-445a-9b3f-d41839c0a8c9",
  "isSidechain": false,
  "requestId": "req_011CbBhgArrbZBCgRvZmvJoD",
  "type": "assistant",
  "uuid": "e38564a9-3176-42b1-a3af-8d92a55917b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjScoyYe156izcTZrjPhHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11048,
      "cache_read_input_tokens": 11374,
      "output_tokens": 401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11048,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 401,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 11048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11048
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T09:37:04.585Z_

<details><summary>↩ Tool result · `toolu_01J5XPsFB2BbWhwKDo4s9e3T`</summary>

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
  "parentUuid": "e38564a9-3176-42b1-a3af-8d92a55917b0",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "614cbb28-dd00-4862-854f-e47c15f792ae",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "e38564a9-3176-42b1-a3af-8d92a55917b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T09:37:07.603Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start with parallel searches to verify the key references and check for competing work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "614cbb28-dd00-4862-854f-e47c15f792ae",
  "isSidechain": false,
  "requestId": "req_011CbBhgrHgUKiCUcYA8NbND",
  "type": "assistant",
  "uuid": "811eb845-fa42-4b53-acc1-da783a1b98d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ULycNTELXhdEbmJdQfyuCn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 22422,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1420,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 22422,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1420
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-19T09:37:07.605Z_

Now let me launch parallel searches to verify key claims and references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "811eb845-fa42-4b53-acc1-da783a1b98d2",
  "isSidechain": false,
  "requestId": "req_011CbBhgrHgUKiCUcYA8NbND",
  "type": "assistant",
  "uuid": "106f9d76-7186-44d2-8a4a-ab4b40410422",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ULycNTELXhdEbmJdQfyuCn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 22422,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1420,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 22422,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1420
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T09:37:08.217Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R1cc5kdcFDMEdQcL6Swawa`</summary>

```json
{
  "query": "Zhou et al. \"Beyond the Final Layer\" multilingual calibration LACE arXiv 2510.03136"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "106f9d76-7186-44d2-8a4a-ab4b40410422",
  "isSidechain": false,
  "requestId": "req_011CbBhgrHgUKiCUcYA8NbND",
  "type": "assistant",
  "uuid": "bfda5c60-1042-4144-8ee8-b8c3ba710d91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ULycNTELXhdEbmJdQfyuCn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 22422,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1420,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 22422,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1420
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T09:37:13.948Z_

<details><summary>↩ Tool result · `toolu_01R1cc5kdcFDMEdQcL6Swawa`</summary>

```text
Web search results for query: "Zhou et al. "Beyond the Final Layer" multilingual calibration LACE arXiv 2510.03136"

Links: [{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://www.researchgate.net/publication/396223351_Beyond_the_Final_Layer_Intermediate_Representations_for_Better_Multilingual_Calibration_in_Large_Language_Models"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"dblp: Nigel Collier","url":"https://dblp.org/pid/90/2619.html"}]

I found the paper you're looking for! Here's what I found:

The paper is authored by Ej Zhou, Caiqi Zhang, Tiancheng Hu, Chengzu Li, Nigel Collier, Ivan Vulić, and Anna Korhonen from the Language Technology Lab at the University of Cambridge.

**Main Findings:**

The paper conducts the first large-scale, systematic studies of multilingual calibration across six model families and over 100 languages, revealing that non-English languages suffer from systematically worse calibration. 

The researchers investigated the model's internal representations and found that the final layer, biased by English-centric training, provides a poor signal for multilingual confidence. In contrast, their layer-wise analysis uncovered that late-intermediate layers consistently offer a more reliable and better-calibrated signal.

The paper introduces a suite of training-free methods, including Language-Aware Confidence Ensemble (LACE), which adaptively selects an optimal ensemble of layers for each specific language.

The paper was published on arXiv on October 3, 2025, with identifier 2510.03136. You can access it directly at https://arxiv.org/abs/2510.03136.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfda5c60-1042-4144-8ee8-b8c3ba710d91",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "1d32183a-5493-42fb-8057-d6bff0ff852b",
  "toolUseResult": {
    "query": "Zhou et al. \"Beyond the Final Layer\" multilingual calibration LACE arXiv 2510.03136",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RtSkFKps1bcB9ZiuhAc48L",
        "content": [
          {
            "title": "[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/abs/2510.03136"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://www.researchgate.net/publication/396223351_Beyond_the_Final_Layer_Intermediate_Representations_for_Better_Multilingual_Calibration_in_Large_Language_Models"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/html/2510.03136v1"
          },
          {
            "title": "dblp: Nigel Collier",
            "url": "https://dblp.org/pid/90/2619.html"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\nThe paper is authored by Ej Zhou, Caiqi Zhang, Tiancheng Hu, Chengzu Li, Nigel Collier, Ivan Vulić, and Anna Korhonen from the Language Technology Lab at the University of Cambridge.\n\n**Main Findings:**\n\nThe paper conducts the first large-scale, systematic studies of multilingual calibration across six model families and over 100 languages, revealing that non-English languages suffer from systematically worse calibration. \n\nThe researchers investigated the model's internal representations and found that the final layer, biased by English-centric training, provides a poor signal for multilingual confidence. In contrast, their layer-wise analysis uncovered that late-intermediate layers consistently offer a more reliable and better-calibrated signal.\n\nThe paper introduces a suite of training-free methods, including Language-Aware Confidence Ensemble (LACE), which adaptively selects an optimal ensemble of layers for each specific language.\n\nThe paper was published on arXiv on October 3, 2025, with identifier 2510.03136. You can access it directly at https://arxiv.org/abs/2510.03136."
    ],
    "durationSeconds": 5.722700166999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bfda5c60-1042-4144-8ee8-b8c3ba710d91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T09:37:17.139Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D15SnG3jNzE5GmtqmM2WQk`</summary>

```json
{
  "query": "Ji et al. \"Calibrating Verbal Uncertainty as a Linear Feature\" EMNLP 2025 hallucinations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d32183a-5493-42fb-8057-d6bff0ff852b",
  "isSidechain": false,
  "requestId": "req_011CbBhhXydQi9x5p39wVNuc",
  "type": "assistant",
  "uuid": "46ab2d40-81b4-4264-a626-ef0227da7e3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Weg5r3itFHZJBAad9xmi1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2137,
      "cache_read_input_tokens": 22422,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 22422,
          "cache_creation_input_tokens": 2137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2137
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T09:37:23.473Z_

<details><summary>↩ Tool result · `toolu_01D15SnG3jNzE5GmtqmM2WQk`</summary>

```text
Web search results for query: "Ji et al. "Calibrating Verbal Uncertainty as a Linear Feature" EMNLP 2025 hallucinations"

Links: [{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"dblp: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations.","url":"https://dblp.org/rec/journals/corr/abs-2503-14477.html"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce   Hallucinations","url":"https://arxiv.org/pdf/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"}]

I found the paper! Here's what I found about the research:

## Overview

The paper "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" was published at EMNLP 2025 by Ji, Ziwei, Yu, Lei, Koishekenov, Yeskendir, Bang, Yejin, Hartshorn, Anthony, Schelten, Alan, Zhang, Cheng, Fung, Pascale, and Cancedda, Nicola.

## Key Findings

The paper addresses the problem that "LLMs often adopt an assertive language style also when making false claims" and that "such 'overconfident hallucinations' mislead users and erode trust".

The main contribution is that "verbal uncertainty" is governed by a single linear feature in the representation space of LLMs, and this has only moderate correlation with the actual "semantic uncertainty" of the model.

## Results

The researchers show that the mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone, and they can intervene on verbal uncertainty at inference time to reduce hallucinations on short-form answers, achieving an average relative reduction of 32%.

The paper is available on arXiv (2503.14477) and the ACL Anthology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46ab2d40-81b4-4264-a626-ef0227da7e3a",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "3ee239af-37a2-4945-92ae-f99a2f370e20",
  "toolUseResult": {
    "query": "Ji et al. \"Calibrating Verbal Uncertainty as a Linear Feature\" EMNLP 2025 hallucinations",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DqGxpQ2q5yWCf2o5MaaTvA",
        "content": [
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.187/"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://arxiv.org/html/2503.14477v1"
          },
          {
            "title": "(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"
          },
          {
            "title": "dblp: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations.",
            "url": "https://dblp.org/rec/journals/corr/abs-2503-14477.html"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce   Hallucinations",
            "url": "https://arxiv.org/pdf/2503.14477"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"
          },
          {
            "title": "[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://arxiv.org/abs/2503.14477"
          }
        ]
      },
      "I found the paper! Here's what I found about the research:\n\n## Overview\n\nThe paper \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\" was published at EMNLP 2025 by Ji, Ziwei, Yu, Lei, Koishekenov, Yeskendir, Bang, Yejin, Hartshorn, Anthony, Schelten, Alan, Zhang, Cheng, Fung, Pascale, and Cancedda, Nicola.\n\n## Key Findings\n\nThe paper addresses the problem that \"LLMs often adopt an assertive language style also when making false claims\" and that \"such 'overconfident hallucinations' mislead users and erode trust\".\n\nThe main contribution is that \"verbal uncertainty\" is governed by a single linear feature in the representation space of LLMs, and this has only moderate correlation with the actual \"semantic uncertainty\" of the model.\n\n## Results\n\nThe researchers show that the mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone, and they can intervene on verbal uncertainty at inference time to reduce hallucinations on short-form answers, achieving an average relative reduction of 32%.\n\nThe paper is available on arXiv (2503.14477) and the ACL Anthology."
    ],
    "durationSeconds": 6.329045613000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "46ab2d40-81b4-4264-a626-ef0227da7e3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T09:37:26.255Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015kR1b1em2CcHCZi1iTj6Lp`</summary>

```json
{
  "query": "Wang et al. \"Refusal Direction is Universal Across Safety-Aligned Languages\" arXiv 2505.17306 NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ee239af-37a2-4945-92ae-f99a2f370e20",
  "isSidechain": false,
  "requestId": "req_011CbBhiEt173qXhmp5D29cY",
  "type": "assistant",
  "uuid": "7e1d7800-bdd7-4c24-a375-7f4dbf9bb90b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuBvgonMbQrq1kPrUGiPAE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 826,
      "cache_read_input_tokens": 24559,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 24559,
          "cache_creation_input_tokens": 826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 826
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T09:37:31.992Z_

<details><summary>↩ Tool result · `toolu_015kR1b1em2CcHCZi1iTj6Lp`</summary>

```text
Web search results for query: "Wang et al. "Refusal Direction is Universal Across Safety-Aligned Languages" arXiv 2505.17306 NeurIPS 2025"

Links: [{"title":"[2505.17306] Refusal Direction is Universal Across Safety-Aligned Languages","url":"https://arxiv.org/abs/2505.17306"},{"title":"Refusal Direction is Universal Across Safety-Aligned Languages","url":"https://arxiv.org/pdf/2505.17306"},{"title":"Refusal Direction is Universal Across Safety-Aligned Languages - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2505.17306"},{"title":"Refusal Direction is Universal Across Safety-Aligned Languages","url":"https://arxiv.org/html/2505.17306v1"},{"title":"[PDF] Refusal Direction is Universal Across Safety-Aligned Languages | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Refusal-Direction-is-Universal-Across-Languages-Wang-Wang/7e8245cb11171e5a7c3caacded1521e6bd71c78c"},{"title":"Paper page - Refusal Direction is Universal Across Safety-Aligned Languages","url":"https://huggingface.co/papers/2505.17306"},{"title":"Refusal Direction is Universal Across Safety-Aligned Languages","url":"https://openreview.net/pdf/066153bcff2e9a8b54d827454a6f02b16c7d79c7.pdf"}]

I found the paper! Here are the details:

**Title:** Refusal Direction is Universal Across Safety-Aligned Languages

**Authors:** Xinpeng Wang, Mingyang Wang, Yihong Liu, Hinrich Schütze, Barbara Plank

**Paper Details:** arXiv:2505.17306, submitted on 22 May 2025

**Overview:** The paper investigates the refusal behavior in LLMs across 14 languages using PolyRefuse, a multilingual safety dataset created by translating malicious and benign English prompts into these languages.

**Key Findings:** A vector extracted from English can bypass refusals in other languages with near-perfect effectiveness, without any additional fine-tuning, and refusal directions derived from any safety-aligned language transfer seamlessly to others.

The paper is available on arXiv at https://arxiv.org/abs/2505.17306, and the code is publicly available at https://github.com/mainlp/Multilingual-Refusal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e1d7800-bdd7-4c24-a375-7f4dbf9bb90b",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "f7d0cd4c-c2e0-4f40-a310-2eb321a74492",
  "toolUseResult": {
    "query": "Wang et al. \"Refusal Direction is Universal Across Safety-Aligned Languages\" arXiv 2505.17306 NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M68ZubZqdm4LLXTxRqE5xs",
        "content": [
          {
            "title": "[2505.17306] Refusal Direction is Universal Across Safety-Aligned Languages",
            "url": "https://arxiv.org/abs/2505.17306"
          },
          {
            "title": "Refusal Direction is Universal Across Safety-Aligned Languages",
            "url": "https://arxiv.org/pdf/2505.17306"
          },
          {
            "title": "Refusal Direction is Universal Across Safety-Aligned Languages - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2505.17306"
          },
          {
            "title": "Refusal Direction is Universal Across Safety-Aligned Languages",
            "url": "https://arxiv.org/html/2505.17306v1"
          },
          {
            "title": "[PDF] Refusal Direction is Universal Across Safety-Aligned Languages | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Refusal-Direction-is-Universal-Across-Languages-Wang-Wang/7e8245cb11171e5a7c3caacded1521e6bd71c78c"
          },
          {
            "title": "Paper page - Refusal Direction is Universal Across Safety-Aligned Languages",
            "url": "https://huggingface.co/papers/2505.17306"
          },
          {
            "title": "Refusal Direction is Universal Across Safety-Aligned Languages",
            "url": "https://openreview.net/pdf/066153bcff2e9a8b54d827454a6f02b16c7d79c7.pdf"
          }
        ]
      },
      "I found the paper! Here are the details:\n\n**Title:** Refusal Direction is Universal Across Safety-Aligned Languages\n\n**Authors:** Xinpeng Wang, Mingyang Wang, Yihong Liu, Hinrich Schütze, Barbara Plank\n\n**Paper Details:** arXiv:2505.17306, submitted on 22 May 2025\n\n**Overview:** The paper investigates the refusal behavior in LLMs across 14 languages using PolyRefuse, a multilingual safety dataset created by translating malicious and benign English prompts into these languages.\n\n**Key Findings:** A vector extracted from English can bypass refusals in other languages with near-perfect effectiveness, without any additional fine-tuning, and refusal directions derived from any safety-aligned language transfer seamlessly to others.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2505.17306, and the code is publicly available at https://github.com/mainlp/Multilingual-Refusal."
    ],
    "durationSeconds": 5.730149102000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7e1d7800-bdd7-4c24-a375-7f4dbf9bb90b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T09:37:34.944Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qfar353uyZej429kvy1BK6`</summary>

```json
{
  "query": "Mahmoud et al. \"Improving Multilingual Language Models by Aligning Representations through Steering\" arXiv 2505.12584"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7d0cd4c-c2e0-4f40-a310-2eb321a74492",
  "isSidechain": false,
  "requestId": "req_011CbBhis85zmJDQ9NcMc1f9",
  "type": "assistant",
  "uuid": "65272506-b63a-430b-a8d2-33968fe7e3b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAaCJTFQFMxtzFEtWRHHZ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 25385,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 741,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 25385,
          "cache_creation_input_tokens": 741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 741
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T09:37:41.182Z_

<details><summary>↩ Tool result · `toolu_01Qfar353uyZej429kvy1BK6`</summary>

```text
Web search results for query: "Mahmoud et al. "Improving Multilingual Language Models by Aligning Representations through Steering" arXiv 2505.12584"

Links: [{"title":"[2505.12584] Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/abs/2505.12584"},{"title":"[Literature Review] Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://www.themoonlight.io/en/review/improving-multilingual-language-models-by-aligning-representations-through-steering"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/html/2505.12584v1"},{"title":"Improving Multilingual Language Models by Aligning Representations","url":"https://arxiv.org/pdf/2505.12584"},{"title":"Language Lives in Sparse Dimensions: Toward Interpretable and Efficient Multilingual Control for Large Language Models","url":"https://arxiv.org/html/2510.07213v1"},{"title":"Paper page - Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://huggingface.co/papers/2505.12584"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/pdf/2502.15639"},{"title":"[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/abs/2502.15639"}]

I found the paper for you. Here's what the search revealed:

"Improving Multilingual Language Models by Aligning Representations through Steering" investigates how Large Language Models (LLMs) represent non-English tokens and proposes a lightweight intervention method using representation steering, where a learned vector is added to the residual stream at a single model layer to enhance multilingual performance.

The paper is authored by Omar Mahmoud, Buddhika Laknath Semage, Thommen George Karimpanal, and Santu Rana from Deakin University, Australia.

Through extensive experiments across seven competitive baselines including prompt optimization, supervised fine-tuning (SFT), in-context learning, cross-lingual transfer, and translation-based methods, the approach consistently outperforms most alternatives and achieves performance on par with production-grade translation systems while requiring far fewer resources.

The core technique involves training a steering vector that, when added to the hidden state representation of a non-English prompt at a specific layer, shifts its representation closer to that of its English equivalent.

The paper is available on arXiv at https://arxiv.org/abs/2505.12584


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65272506-b63a-430b-a8d2-33968fe7e3b9",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "d31db87b-2eaf-4f0a-ba13-9187f44c8edf",
  "toolUseResult": {
    "query": "Mahmoud et al. \"Improving Multilingual Language Models by Aligning Representations through Steering\" arXiv 2505.12584",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EARhhRGqVUotQ1FZNy5c7g",
        "content": [
          {
            "title": "[2505.12584] Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/abs/2505.12584"
          },
          {
            "title": "[Literature Review] Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://www.themoonlight.io/en/review/improving-multilingual-language-models-by-aligning-representations-through-steering"
          },
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/html/2505.12584v1"
          },
          {
            "title": "Improving Multilingual Language Models by Aligning Representations",
            "url": "https://arxiv.org/pdf/2505.12584"
          },
          {
            "title": "Language Lives in Sparse Dimensions: Toward Interpretable and Efficient Multilingual Control for Large Language Models",
            "url": "https://arxiv.org/html/2510.07213v1"
          },
          {
            "title": "Paper page - Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://huggingface.co/papers/2505.12584"
          },
          {
            "title": "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2502.15639"
          },
          {
            "title": "[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models",
            "url": "https://arxiv.org/abs/2502.15639"
          }
        ]
      },
      "I found the paper for you. Here's what the search revealed:\n\n\"Improving Multilingual Language Models by Aligning Representations through Steering\" investigates how Large Language Models (LLMs) represent non-English tokens and proposes a lightweight intervention method using representation steering, where a learned vector is added to the residual stream at a single model layer to enhance multilingual performance.\n\nThe paper is authored by Omar Mahmoud, Buddhika Laknath Semage, Thommen George Karimpanal, and Santu Rana from Deakin University, Australia.\n\nThrough extensive experiments across seven competitive baselines including prompt optimization, supervised fine-tuning (SFT), in-context learning, cross-lingual transfer, and translation-based methods, the approach consistently outperforms most alternatives and achieves performance on par with production-grade translation systems while requiring far fewer resources.\n\nThe core technique involves training a steering vector that, when added to the hidden state representation of a non-English prompt at a specific layer, shifts its representation closer to that of its English equivalent.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2505.12584"
    ],
    "durationSeconds": 6.232830917999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "65272506-b63a-430b-a8d2-33968fe7e3b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "d31db87b-2eaf-4f0a-ba13-9187f44c8edf",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Tool call

_source line 24 · 2026-05-19T09:37:50.601Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LSYSwr2FLm1ikBbZKpyhTM`</summary>

```json
{
  "query": "Yap \"Behavioral Steering 35B MoE Language Model SAE-Decoded Probe Vectors\" arXiv 2603.16335 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d31db87b-2eaf-4f0a-ba13-9187f44c8edf",
  "isSidechain": false,
  "requestId": "req_011CbBhjYNzmmzQBTdz4BLVR",
  "type": "assistant",
  "uuid": "ee265987-787d-4081-a71f-ff2ef7ef1a91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuucDqTqez9gV99s4GQxUL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 26126,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 26126,
          "cache_creation_input_tokens": 801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 801
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T09:38:02.163Z_

<details><summary>↩ Tool result · `toolu_01LSYSwr2FLm1ikBbZKpyhTM`</summary>

```text
Web search results for query: "Yap "Behavioral Steering 35B MoE Language Model SAE-Decoded Probe Vectors" arXiv 2603.16335 2026"

Links: [{"title":"[2603.16335] Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits","url":"https://arxiv.org/abs/2603.16335"},{"title":"Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits","url":"https://arxiv.org/html/2603.16335v1"},{"title":"Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors:","url":"https://arxiv.org/pdf/2603.16335"},{"title":"Steering MoE LLMs via Expert (De)Activation","url":"https://arxiv.org/html/2509.09660v1"},{"title":"Reliable Control-Point Selection for Steering Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2604.02113"},{"title":"Can sparse autoencoders be used to decompose and interpret steering   vectors?","url":"https://arxiv.org/pdf/2411.08790"},{"title":"[2509.09660] Steering MoE LLMs via Expert (De)Activation","url":"https://arxiv.org/abs/2509.09660"},{"title":"Understanding (Un)Reliability of Steering Vectors in Language Models","url":"https://arxiv.org/pdf/2505.22637"}]

I found the paper you were searching for! Here's what I can tell you about it:

The paper "Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits" by Jia Qing Yap trains nine sparse autoencoders (SAEs) on the residual stream of Qwen 3.5-35B-A3B, a 35-billion-parameter Mixture-of-Experts model with a hybrid GatedDeltaNet/attention architecture, to identify and steer five agentic behavioral traits.

The method trains linear probes on SAE latent activations, then projects the probe weights back through the SAE decoder to obtain continuous steering vectors in the model's native activation space, which bypasses the SAE's top-k discretization and enables fine-grained behavioral intervention at inference time with no retraining.

Across 1,800 agent rollouts (50 scenarios times 36 conditions), the research finds that autonomy steering at multiplier 2 achieves Cohen's d = 1.01 (p < 0.0001), shifting the model from asking the user for help 78% of the time to a different behavior distribution.

The cross-trait analysis reveals that all five steering vectors primarily modulate a single dominant agency axis (the disposition to act independently versus defer to the user), with trait specific effects appearing only as secondary modulations.

The paper was submitted on March 17, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee265987-787d-4081-a71f-ff2ef7ef1a91",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "d1ef3cd5-5fb7-4de6-ad6e-90c36d53b2ac",
  "toolUseResult": {
    "query": "Yap \"Behavioral Steering 35B MoE Language Model SAE-Decoded Probe Vectors\" arXiv 2603.16335 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CFTrg8NMaX8ZxJ3NFudHWz",
        "content": [
          {
            "title": "[2603.16335] Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits",
            "url": "https://arxiv.org/abs/2603.16335"
          },
          {
            "title": "Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits",
            "url": "https://arxiv.org/html/2603.16335v1"
          },
          {
            "title": "Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors:",
            "url": "https://arxiv.org/pdf/2603.16335"
          },
          {
            "title": "Steering MoE LLMs via Expert (De)Activation",
            "url": "https://arxiv.org/html/2509.09660v1"
          },
          {
            "title": "Reliable Control-Point Selection for Steering Reasoning in Large Language Models",
            "url": "https://arxiv.org/pdf/2604.02113"
          },
          {
            "title": "Can sparse autoencoders be used to decompose and interpret steering   vectors?",
            "url": "https://arxiv.org/pdf/2411.08790"
          },
          {
            "title": "[2509.09660] Steering MoE LLMs via Expert (De)Activation",
            "url": "https://arxiv.org/abs/2509.09660"
          },
          {
            "title": "Understanding (Un)Reliability of Steering Vectors in Language Models",
            "url": "https://arxiv.org/pdf/2505.22637"
          }
        ]
      },
      "I found the paper you were searching for! Here's what I can tell you about it:\n\nThe paper \"Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits\" by Jia Qing Yap trains nine sparse autoencoders (SAEs) on the residual stream of Qwen 3.5-35B-A3B, a 35-billion-parameter Mixture-of-Experts model with a hybrid GatedDeltaNet/attention architecture, to identify and steer five agentic behavioral traits.\n\nThe method trains linear probes on SAE latent activations, then projects the probe weights back through the SAE decoder to obtain continuous steering vectors in the model's native activation space, which bypasses the SAE's top-k discretization and enables fine-grained behavioral intervention at inference time with no retraining.\n\nAcross 1,800 agent rollouts (50 scenarios times 36 conditions), the research finds that autonomy steering at multiplier 2 achieves Cohen's d = 1.01 (p < 0.0001), shifting the model from asking the user for help 78% of the time to a different behavior distribution.\n\nThe cross-trait analysis reveals that all five steering vectors primarily modulate a single dominant agency axis (the disposition to act independently versus defer to the user), with trait specific effects appearing only as secondary modulations.\n\nThe paper was submitted on March 17, 2026."
    ],
    "durationSeconds": 11.558284971000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ee265987-787d-4081-a71f-ff2ef7ef1a91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T09:38:04.923Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019WFkt9y65ycL2MbJYZXymf`</summary>

```json
{
  "query": "Feng et al. \"Teaching LLMs to Abstain across Languages via Multilingual Feedback\" arXiv 2406.15948"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1ef3cd5-5fb7-4de6-ad6e-90c36d53b2ac",
  "isSidechain": false,
  "requestId": "req_011CbBhm68yk4fRWrcw4h8vf",
  "type": "assistant",
  "uuid": "0a3a5a7f-1f9e-45c6-8066-422b8b59ef69",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYNXzf9e6C1sGpjm3ALzXg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 26927,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 26927,
          "cache_creation_input_tokens": 869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 869
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T09:38:11.082Z_

<details><summary>↩ Tool result · `toolu_019WFkt9y65ycL2MbJYZXymf`</summary>

```text
Web search results for query: "Feng et al. "Teaching LLMs to Abstain across Languages via Multilingual Feedback" arXiv 2406.15948"

Links: [{"title":"[2406.15948] Teaching LLMs to Abstain across Languages via Multilingual Feedback","url":"https://arxiv.org/abs/2406.15948"},{"title":"Teaching LLMs to Abstain across Languages via Multilingual Feedback","url":"https://arxiv.org/pdf/2406.15948"},{"title":"Teaching LLMs to Abstain across Languages via Multilingual Feedback","url":"https://arxiv.org/html/2406.15948v3"},{"title":"[Literature Review] Teaching LLMs to Abstain across Languages via Multilingual Feedback","url":"https://www.themoonlight.io/en/review/teaching-llms-to-abstain-across-languages-via-multilingual-feedback"},{"title":"Teaching LLMs to Abstain across Languages via Multilingual Feedback - Paper Detail","url":"https://deeplearn.org/arxiv/536173/teaching-llms-to-abstain-across-languages-via-multilingual-feedback"},{"title":"MKA: Leveraging Cross-Lingual Consensus for Model Abstention","url":"https://arxiv.org/html/2503.23687v1"},{"title":"Teaching LLMs to Abstain across Languages via Multilingual Feedback","url":"https://scispace.com/pdf/teaching-llms-to-abstain-across-languages-via-multilingual-3g5gzjdr4o.pdf"},{"title":"(PDF) Teaching LLMs to Abstain across Languages via Multilingual Feedback","url":"https://www.researchgate.net/publication/381666781_Teaching_LLMs_to_Abstain_across_Languages_via_Multilingual_Feedback"},{"title":"GitHub - BunsenFeng/M-AbstainQA: Multilingual AbstainQA @ EMNLP 2024 · GitHub","url":"https://github.com/BunsenFeng/M-AbstainQA"}]

I found the paper you're looking for. Here's a summary of "Teaching LLMs to Abstain across Languages via Multilingual Feedback":

**Paper Overview:**

The paper addresses knowledge disparities in multilingual LLMs, with larger gaps in under-resourced languages. Teaching LLMs to abstain in the face of knowledge gaps is presented as a promising strategy to mitigate hallucinations in multilingual settings.

**Key Findings:**

The researchers evaluated seven existing abstain methods on multilingual datasets, finding that performance degrades by up to 12.8% and 20.5% for different datasets, while existing approaches perform well in English but are limited by LLMs' diminishing utility and calibration accuracy in low-resource languages.

**Proposed Solution:**

The authors propose strategies to enhance LLM abstention by learning from multilingual feedback, where LLMs self-reflect on proposed answers in one language by generating multiple feedback items in related languages.

**Publication:**

The paper was published on arXiv with the identifier 2406.15948 and was presented at EMNLP 2024. The authors have made their code and data publicly available on GitHub at the repository M-AbstainQA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a3a5a7f-1f9e-45c6-8066-422b8b59ef69",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "90fde8c2-b68b-41f0-b8e6-fe6ac6bfb426",
  "toolUseResult": {
    "query": "Feng et al. \"Teaching LLMs to Abstain across Languages via Multilingual Feedback\" arXiv 2406.15948",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KpaeXEPnU1UmgpnLyih2FM",
        "content": [
          {
            "title": "[2406.15948] Teaching LLMs to Abstain across Languages via Multilingual Feedback",
            "url": "https://arxiv.org/abs/2406.15948"
          },
          {
            "title": "Teaching LLMs to Abstain across Languages via Multilingual Feedback",
            "url": "https://arxiv.org/pdf/2406.15948"
          },
          {
            "title": "Teaching LLMs to Abstain across Languages via Multilingual Feedback",
            "url": "https://arxiv.org/html/2406.15948v3"
          },
          {
            "title": "[Literature Review] Teaching LLMs to Abstain across Languages via Multilingual Feedback",
            "url": "https://www.themoonlight.io/en/review/teaching-llms-to-abstain-across-languages-via-multilingual-feedback"
          },
          {
            "title": "Teaching LLMs to Abstain across Languages via Multilingual Feedback - Paper Detail",
            "url": "https://deeplearn.org/arxiv/536173/teaching-llms-to-abstain-across-languages-via-multilingual-feedback"
          },
          {
            "title": "MKA: Leveraging Cross-Lingual Consensus for Model Abstention",
            "url": "https://arxiv.org/html/2503.23687v1"
          },
          {
            "title": "Teaching LLMs to Abstain across Languages via Multilingual Feedback",
            "url": "https://scispace.com/pdf/teaching-llms-to-abstain-across-languages-via-multilingual-3g5gzjdr4o.pdf"
          },
          {
            "title": "(PDF) Teaching LLMs to Abstain across Languages via Multilingual Feedback",
            "url": "https://www.researchgate.net/publication/381666781_Teaching_LLMs_to_Abstain_across_Languages_via_Multilingual_Feedback"
          },
          {
            "title": "GitHub - BunsenFeng/M-AbstainQA: Multilingual AbstainQA @ EMNLP 2024 · GitHub",
            "url": "https://github.com/BunsenFeng/M-AbstainQA"
          }
        ]
      },
      "I found the paper you're looking for. Here's a summary of \"Teaching LLMs to Abstain across Languages via Multilingual Feedback\":\n\n**Paper Overview:**\n\nThe paper addresses knowledge disparities in multilingual LLMs, with larger gaps in under-resourced languages. Teaching LLMs to abstain in the face of knowledge gaps is presented as a promising strategy to mitigate hallucinations in multilingual settings.\n\n**Key Findings:**\n\nThe researchers evaluated seven existing abstain methods on multilingual datasets, finding that performance degrades by up to 12.8% and 20.5% for different datasets, while existing approaches perform well in English but are limited by LLMs' diminishing utility and calibration accuracy in low-resource languages.\n\n**Proposed Solution:**\n\nThe authors propose strategies to enhance LLM abstention by learning from multilingual feedback, where LLMs self-reflect on proposed answers in one language by generating multiple feedback items in related languages.\n\n**Publication:**\n\nThe paper was published on arXiv with the identifier 2406.15948 and was presented at EMNLP 2024. The authors have made their code and data publicly available on GitHub at the repository M-AbstainQA."
    ],
    "durationSeconds": 6.1535534489999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0a3a5a7f-1f9e-45c6-8066-422b8b59ef69",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-19T09:38:14.295Z_

Good, references are checking out. Now let me search for competing work and the most critical gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90fde8c2-b68b-41f0-b8e6-fe6ac6bfb426",
  "isSidechain": false,
  "requestId": "req_011CbBhmkyLFaRVqmrZe3VjX",
  "type": "assistant",
  "uuid": "ea0f6fc9-58e6-4023-b61d-033ffad8d83e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iu9VjaQqkG3YGeN8Y2LCC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 27796,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 903,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 27796,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 903
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T09:38:14.814Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Amqk6reZKd6GDpnu9yG5gX`</summary>

```json
{
  "query": "cross-lingual calibration transfer representation engineering confidence direction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea0f6fc9-58e6-4023-b61d-033ffad8d83e",
  "isSidechain": false,
  "requestId": "req_011CbBhmkyLFaRVqmrZe3VjX",
  "type": "assistant",
  "uuid": "297ba444-cd91-435b-9997-30ed97107f35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iu9VjaQqkG3YGeN8Y2LCC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 27796,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 903,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 27796,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 903
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T09:38:21.726Z_

<details><summary>↩ Tool result · `toolu_01Amqk6reZKd6GDpnu9yG5gX`</summary>

```text
Web search results for query: "cross-lingual calibration transfer representation engineering confidence direction 2025 2026"

Links: [{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"Enhancing Cross-lingual Transfer by Manifold Mixup","url":"https://arxiv.org/pdf/2205.04182"},{"title":"Cross-Lingual Representation Alignment Through ...","url":"https://aclanthology.org/2025.acl-short.95.pdf"},{"title":"Cross-Language Calibration Performance","url":"https://www.emergentmind.com/topics/cross-language-calibration-performance"},{"title":"Cross-Lingual Transfer Learning in Large Language Models","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176799777.79169627/v1?onload=true"},{"title":"How Do Multilingual Encoders Learn Cross-lingual Representation?","url":"https://arxiv.org/pdf/2207.05737"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/pdf/2502.14830"},{"title":"Cross-lingual zero-shot transfer via semantic and synthetic representation learning","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12050870"}]

Based on the search results, I found several highly relevant papers and resources on cross-lingual calibration, transfer, and representation engineering from 2025-2026:

## Key Recent Work

**Multilingual Calibration (2025)**

A recent systematic evaluation presents the first comprehensive assessment of multilingual calibration across high-quality, human-curated datasets spanning over 100 languages and covering six prominent LLM families. Researchers have introduced novel, training-free calibration methods that leverage intermediate representations, demonstrating their effectiveness in closing the cross-lingual calibration gap.

**Cross-Lingual Representation Alignment (2025)**

Recent work on cross-lingual representation alignment through contrastive learning was presented at ACL in July-August 2025. The research explores techniques for improving representation alignment across languages, particularly for multilingual image-text models.

**Middle-Layer Representation Alignment (2026)**

Recent experiments on slot filling, machine translation, and structured text generation show consistent improvements in cross-lingual transfer, especially to lower-resource languages, with methods robust to the choice of alignment languages and generalizing to unseen languages.

**Cross-Lingual Transfer Overview (2026)**

A comprehensive review covers how knowledge is transferred across languages, the evolution of pretrained multilingual models, zero-shot and few-shot transfer techniques, and prompt-based adaptation strategies.

These resources indicate active research in improving confidence calibration, representation alignment, and transfer efficiency across languages in modern language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "297ba444-cd91-435b-9997-30ed97107f35",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "9d5200eb-d15a-490d-a0ae-4fe82932e512",
  "toolUseResult": {
    "query": "cross-lingual calibration transfer representation engineering confidence direction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XxCyWwsKzTy9KuRuyLq7Q6",
        "content": [
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/html/2510.03136v1"
          },
          {
            "title": "Enhancing Cross-lingual Transfer by Manifold Mixup",
            "url": "https://arxiv.org/pdf/2205.04182"
          },
          {
            "title": "Cross-Lingual Representation Alignment Through ...",
            "url": "https://aclanthology.org/2025.acl-short.95.pdf"
          },
          {
            "title": "Cross-Language Calibration Performance",
            "url": "https://www.emergentmind.com/topics/cross-language-calibration-performance"
          },
          {
            "title": "Cross-Lingual Transfer Learning in Large Language Models",
            "url": "https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176799777.79169627/v1?onload=true"
          },
          {
            "title": "How Do Multilingual Encoders Learn Cross-lingual Representation?",
            "url": "https://arxiv.org/pdf/2207.05737"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://arxiv.org/pdf/2502.14830"
          },
          {
            "title": "Cross-lingual zero-shot transfer via semantic and synthetic representation learning",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12050870"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers and resources on cross-lingual calibration, transfer, and representation engineering from 2025-2026:\n\n## Key Recent Work\n\n**Multilingual Calibration (2025)**\n\nA recent systematic evaluation presents the first comprehensive assessment of multilingual calibration across high-quality, human-curated datasets spanning over 100 languages and covering six prominent LLM families. Researchers have introduced novel, training-free calibration methods that leverage intermediate representations, demonstrating their effectiveness in closing the cross-lingual calibration gap.\n\n**Cross-Lingual Representation Alignment (2025)**\n\nRecent work on cross-lingual representation alignment through contrastive learning was presented at ACL in July-August 2025. The research explores techniques for improving representation alignment across languages, particularly for multilingual image-text models.\n\n**Middle-Layer Representation Alignment (2026)**\n\nRecent experiments on slot filling, machine translation, and structured text generation show consistent improvements in cross-lingual transfer, especially to lower-resource languages, with methods robust to the choice of alignment languages and generalizing to unseen languages.\n\n**Cross-Lingual Transfer Overview (2026)**\n\nA comprehensive review covers how knowledge is transferred across languages, the evolution of pretrained multilingual models, zero-shot and few-shot transfer techniques, and prompt-based adaptation strategies.\n\nThese resources indicate active research in improving confidence calibration, representation alignment, and transfer efficiency across languages in modern language models."
    ],
    "durationSeconds": 6.905959426000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "297ba444-cd91-435b-9997-30ed97107f35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-19T09:38:21.731Z_

```json
{
  "parentUuid": "9d5200eb-d15a-490d-a0ae-4fe82932e512",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "30c81775-5f0e-44e2-852d-3431e4789197",
  "timestamp": "2026-05-19T09:38:21.731Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 32 · 2026-05-19T09:38:25.559Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018jSSzY8TMrYvuCThMWETiW`</summary>

```json
{
  "query": "site:arxiv.org cross-lingual confidence steering calibration transfer hidden states 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30c81775-5f0e-44e2-852d-3431e4789197",
  "isSidechain": false,
  "requestId": "req_011CbBhnXnN52eT3iaw3e8rs",
  "type": "assistant",
  "uuid": "98b57d7d-f391-45c2-86b2-e4ad44b0e600",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xvzNJuV7bmLoZPtnQsC1T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 28699,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 957,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 28699,
          "cache_creation_input_tokens": 957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 957
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T09:38:33.022Z_

<details><summary>↩ Tool result · `toolu_018jSSzY8TMrYvuCThMWETiW`</summary>

```text
Web search results for query: "site:arxiv.org cross-lingual confidence steering calibration transfer hidden states 2026"

Links: [{"title":"[2601.03042v2] BaseCal: Unsupervised Confidence Calibration via Base Model Signals","url":"https://arxiv.org/abs/2601.03042v2"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/html/2601.16390v1"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.12299"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/pdf/2601.08331"}]

I found several relevant arXiv papers from 2026 related to your search query. Here are the key results:

1. **BaseCal: Unsupervised Confidence Calibration via Base Model Signals** (2601.03042v2, January 2026)
   - Proposes BaseCal-Proj, which trains a lightweight projection to map final-layer hidden states of post-trained LLMs back to those of their base LLMs

2. **Cross-Lingual Activation Steering for Multilingual Language Models** (2601.16390v1, January 2026)
   - Shows that best performance comes from a calibrated balance between shared semantics and language-specific neurons

3. **Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering** (2602.06022v1, February 2026)
   - A frozen LLM produces per-option hidden states, which are mean-pooled over answer tokens, z-score normalized, and passed through a trained probe to predict residual correctness

4. **Language Steering for Multilingual In-Context Learning** (2602.02326, February 2026)
   - Focuses on cross-lingual steering methods for multilingual LLMs

5. **CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark** (2601.08331, January 2026)
   - Discusses representation-based steering that intervenes directly on hidden representations to induce desired behaviors

These papers directly address the intersection of cross-lingual methods, confidence calibration, steering, and hidden state manipulation that your search query targets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98b57d7d-f391-45c2-86b2-e4ad44b0e600",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "bb9bd92a-8b4d-4fbf-b947-8b3bb8f08893",
  "toolUseResult": {
    "query": "site:arxiv.org cross-lingual confidence steering calibration transfer hidden states 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RBbhdNsKbwMuoBT3SVoHti",
        "content": [
          {
            "title": "[2601.03042v2] BaseCal: Unsupervised Confidence Calibration via Base Model Signals",
            "url": "https://arxiv.org/abs/2601.03042v2"
          },
          {
            "title": "Cross-Lingual Activation Steering for Multilingual Language Models",
            "url": "https://arxiv.org/html/2601.16390v1"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/html/2602.06022v1"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/pdf/2602.02326"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2410.12299"
          },
          {
            "title": "CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark",
            "url": "https://arxiv.org/pdf/2601.08331"
          }
        ]
      },
      "I found several relevant arXiv papers from 2026 related to your search query. Here are the key results:\n\n1. **BaseCal: Unsupervised Confidence Calibration via Base Model Signals** (2601.03042v2, January 2026)\n   - Proposes BaseCal-Proj, which trains a lightweight projection to map final-layer hidden states of post-trained LLMs back to those of their base LLMs\n\n2. **Cross-Lingual Activation Steering for Multilingual Language Models** (2601.16390v1, January 2026)\n   - Shows that best performance comes from a calibrated balance between shared semantics and language-specific neurons\n\n3. **Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering** (2602.06022v1, February 2026)\n   - A frozen LLM produces per-option hidden states, which are mean-pooled over answer tokens, z-score normalized, and passed through a trained probe to predict residual correctness\n\n4. **Language Steering for Multilingual In-Context Learning** (2602.02326, February 2026)\n   - Focuses on cross-lingual steering methods for multilingual LLMs\n\n5. **CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark** (2601.08331, January 2026)\n   - Discusses representation-based steering that intervenes directly on hidden representations to induce desired behaviors\n\nThese papers directly address the intersection of cross-lingual methods, confidence calibration, steering, and hidden state manipulation that your search query targets."
    ],
    "durationSeconds": 7.458745249,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "98b57d7d-f391-45c2-86b2-e4ad44b0e600",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T09:38:35.795Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01874JF7UMaKyhGTnSjejotZ`</summary>

```json
{
  "query": "CORAL \"Correctness-Optimized Residual Activation Lens\" calibration steering arXiv 2602.06022 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb9bd92a-8b4d-4fbf-b947-8b3bb8f08893",
  "isSidechain": false,
  "requestId": "req_011CbBhoN4F7gF7xsfYA2Jtk",
  "type": "assistant",
  "uuid": "79b97f8c-c1eb-4133-a424-9ce76b169e3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZ3PEenSZiLFTGP4tFpBDB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 780,
      "cache_read_input_tokens": 29656,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 780,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 29656,
          "cache_creation_input_tokens": 780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 780
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "79b97f8c-c1eb-4133-a424-9ce76b169e3a",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Tool result

_source line 37 · 2026-05-19T09:38:42.794Z_

<details><summary>↩ Tool result · `toolu_01874JF7UMaKyhGTnSjejotZ`</summary>

```text
Web search results for query: "CORAL "Correctness-Optimized Residual Activation Lens" calibration steering arXiv 2602.06022 2026"

Links: [{"title":"[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/abs/2602.06022"},{"title":"[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL):","url":"https://arxiv.org/pdf/2602.06022"},{"title":"Correctness-Optimized Residual Activation Lens : Transferrable and Calibration-Aware Inference-Time Steering","url":"http://paperreading.club/page?id=374945"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2602.06022"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"},{"title":"Paper page - Steer2Edit: From Activation Steering to Component-Level Editing","url":"https://huggingface.co/papers/2602.09870"}]

I've found the research paper you're looking for. Here's what the search revealed:

CORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes.

## Problem and Motivation

Large language models (LLMs) exhibit persistent miscalibration, especially after instruction tuning and preference alignment. Modified training objectives can improve calibration, but retraining is expensive. Inference-time steering offers a lightweight alternative, yet most existing methods optimize proxies for correctness rather than correctness itself.

## Key Results

The method consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average across three 7B-parameter models. 

These gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.

## Methodology

The method trains a regularized probe that predicts correctness directly from frozen residual stream activations, then uses these predictions to steer model behavior at inference time. By jointly optimizing for the accuracy and calibration components of the Brier score, CORAL improves both metrics and transfers its impact successfully to unseen benchmarks without any retraining.

The paper was published on arXiv on February 5-6, 2026 (arXiv:2602.06022).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79b97f8c-c1eb-4133-a424-9ce76b169e3a",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "6f77a599-1140-410a-bdb9-3e5c95dda9fc",
  "toolUseResult": {
    "query": "CORAL \"Correctness-Optimized Residual Activation Lens\" calibration steering arXiv 2602.06022 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X9ZFx4SPZ7qLcHtfqUTvcM",
        "content": [
          {
            "title": "[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/abs/2602.06022"
          },
          {
            "title": "[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/html/2602.06022v1"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL):",
            "url": "https://arxiv.org/pdf/2602.06022"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens : Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "http://paperreading.club/page?id=374945"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2602.06022"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"
          },
          {
            "title": "Paper page - Steer2Edit: From Activation Steering to Component-Level Editing",
            "url": "https://huggingface.co/papers/2602.09870"
          }
        ]
      },
      "I've found the research paper you're looking for. Here's what the search revealed:\n\nCORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes.\n\n## Problem and Motivation\n\nLarge language models (LLMs) exhibit persistent miscalibration, especially after instruction tuning and preference alignment. Modified training objectives can improve calibration, but retraining is expensive. Inference-time steering offers a lightweight alternative, yet most existing methods optimize proxies for correctness rather than correctness itself.\n\n## Key Results\n\nThe method consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average across three 7B-parameter models. \n\nThese gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.\n\n## Methodology\n\nThe method trains a regularized probe that predicts correctness directly from frozen residual stream activations, then uses these predictions to steer model behavior at inference time. By jointly optimizing for the accuracy and calibration components of the Brier score, CORAL improves both metrics and transfers its impact successfully to unseen benchmarks without any retraining.\n\nThe paper was published on arXiv on February 5-6, 2026 (arXiv:2602.06022)."
    ],
    "durationSeconds": 6.9937640079999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "79b97f8c-c1eb-4133-a424-9ce76b169e3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-19T09:38:46.805Z_

<details><summary>Logged reasoning block</summary>

```text
CORAL is very interesting - it's a calibration-aware inference-time steering method. Let me check if it has been evaluated multilingually and whether it does cross-lingual transfer. This could be a significant competing work that the idea under review hasn't cited.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f77a599-1140-410a-bdb9-3e5c95dda9fc",
  "isSidechain": false,
  "requestId": "req_011CbBhp5rCX4nR4mKyXNAtu",
  "type": "assistant",
  "uuid": "7857a7e6-7ba0-432a-bf4b-861bb7baa55d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qQyUXWAVgEC7wWXvW89M1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1013,
      "cache_read_input_tokens": 30436,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1013,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 30436,
          "cache_creation_input_tokens": 1013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1013
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-19T09:38:47.752Z_

This is interesting - CORAL is a calibration-aware steering method from Feb 2026. Let me dig deeper into it and search for more potential competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7857a7e6-7ba0-432a-bf4b-861bb7baa55d",
  "isSidechain": false,
  "requestId": "req_011CbBhp5rCX4nR4mKyXNAtu",
  "type": "assistant",
  "uuid": "243b73b7-3a8d-44a7-a372-14598887b88f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qQyUXWAVgEC7wWXvW89M1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1013,
      "cache_read_input_tokens": 30436,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1013,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 30436,
          "cache_creation_input_tokens": 1013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1013
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T09:38:49.092Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EiXLiWv8r5nJpHzTWivoVZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.06022",
  "prompt": "Extract the full abstract, list of authors, and key details: Does CORAL work multilingually? Does it transfer cross-lingually? What layers does it use? What models are tested? What datasets? Is the probe trained per-language or language-agnostic?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "243b73b7-3a8d-44a7-a372-14598887b88f",
  "isSidechain": false,
  "requestId": "req_011CbBhp5rCX4nR4mKyXNAtu",
  "type": "assistant",
  "uuid": "d078d435-3007-469e-a2f3-dfbbe074e9a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qQyUXWAVgEC7wWXvW89M1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1013,
      "cache_read_input_tokens": 30436,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1013,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 30436,
          "cache_creation_input_tokens": 1013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1013
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T09:38:55.643Z_

<details><summary>↩ Tool result · `toolu_01EiXLiWv8r5nJpHzTWivoVZ`</summary>

```text
# CORAL Paper: Key Details

## Full Abstract
"Large language models (LLMs) exhibit persistent miscalibration, especially after instruction tuning and preference alignment. Modified training objectives can improve calibration, but retraining is expensive. Inference-time steering offers a lightweight alternative, yet most existing methods optimize proxies for correctness rather than correctness itself. We introduce CORAL (Correctness-Optimized Residual Activation Lens), a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes. We evaluate CORAL across three 7B-parameter models and find that it consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average. We additionally demonstrate that these gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements. Our results support the hypothesis that distributed information in model internals can be extracted using regularized probes when individual neurons are insufficient. CORAL thus provides a compute-efficient, transferable, and calibration-aware approach to improve MCQA performance during inference."

## Authors
Miranda Muqing Miao, Young-Min Cho, Lyle Ungar

## Key Findings

**Multilingual & Cross-lingual Performance:** Not addressed in the available content.

**Layers Used:** Not specified in the abstract or page content.

**Models Tested:** Three 7B-parameter models (specific names not listed in excerpt).

**Datasets:** ARC-Challenge, HellaSwag, Math-MC, OpenBookQA.

**Probe Training:** The abstract mentions "weight-decay MLP probes" but does not clarify whether training occurs per-language or language-agnostic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d078d435-3007-469e-a2f3-dfbbe074e9a1",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "98003256-8c1b-487a-9397-fcda069532f9",
  "toolUseResult": {
    "bytes": 47094,
    "code": 200,
    "codeText": "OK",
    "result": "# CORAL Paper: Key Details\n\n## Full Abstract\n\"Large language models (LLMs) exhibit persistent miscalibration, especially after instruction tuning and preference alignment. Modified training objectives can improve calibration, but retraining is expensive. Inference-time steering offers a lightweight alternative, yet most existing methods optimize proxies for correctness rather than correctness itself. We introduce CORAL (Correctness-Optimized Residual Activation Lens), a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes. We evaluate CORAL across three 7B-parameter models and find that it consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average. We additionally demonstrate that these gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements. Our results support the hypothesis that distributed information in model internals can be extracted using regularized probes when individual neurons are insufficient. CORAL thus provides a compute-efficient, transferable, and calibration-aware approach to improve MCQA performance during inference.\"\n\n## Authors\nMiranda Muqing Miao, Young-Min Cho, Lyle Ungar\n\n## Key Findings\n\n**Multilingual & Cross-lingual Performance:** Not addressed in the available content.\n\n**Layers Used:** Not specified in the abstract or page content.\n\n**Models Tested:** Three 7B-parameter models (specific names not listed in excerpt).\n\n**Datasets:** ARC-Challenge, HellaSwag, Math-MC, OpenBookQA.\n\n**Probe Training:** The abstract mentions \"weight-decay MLP probes\" but does not clarify whether training occurs per-language or language-agnostic.",
    "durationMs": 6547,
    "url": "https://arxiv.org/abs/2602.06022"
  },
  "sourceToolAssistantUUID": "d078d435-3007-469e-a2f3-dfbbe074e9a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T09:38:58.067Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012JsaizwhTU4QgCqtVNKxyt`</summary>

```json
{
  "query": "CORAL calibration steering multilingual cross-lingual 2602.06022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98003256-8c1b-487a-9397-fcda069532f9",
  "isSidechain": false,
  "requestId": "req_011CbBhq2jhnJo82dtwwvxK5",
  "type": "assistant",
  "uuid": "874ec6e4-c770-41e9-b202-ea0b58430fb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjcDssEZeLKchGUHF5yJ7E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 31449,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 31449,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-19T09:39:05.122Z_

<details><summary>↩ Tool result · `toolu_012JsaizwhTU4QgCqtVNKxyt`</summary>

```text
Web search results for query: "CORAL calibration steering multilingual cross-lingual 2602.06022"

Links: [{"title":"[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/abs/2602.06022"},{"title":"Correctness-Optimized Residual Activation Lens : Transferrable and Calibration-Aware Inference-Time Steering","url":"http://paperreading.club/page?id=374945"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL):","url":"https://arxiv.org/pdf/2602.06022"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"},{"title":"[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2602.06022"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022"},{"title":"Cross-Lingual Prompt Steerability: Towards Accurate and Robust LLM Behavior across Languages","url":"https://arxiv.org/pdf/2512.02841"}]

Based on the search results, here's what I found about the paper 2602.06022:

The paper is titled "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering" by Miranda Muqing Miao, Young-Min Cho, and Lyle Ungar, submitted on February 5, 2026.

**Key Details:**

Large language models exhibit persistent miscalibration, especially after instruction tuning and preference alignment. While modified training objectives can improve calibration, retraining is expensive. Inference-time steering offers a lightweight alternative, yet most existing methods optimize proxies for correctness rather than correctness itself.

**The CORAL Method:**

CORAL is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes. By jointly optimizing for the accuracy and calibration components of the Brier score, CORAL improves both metrics and transfers its impact successfully to unseen benchmarks without any retraining.

**Results:**

The paper evaluates CORAL across three 7B-parameter models and finds that it consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average. These gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "874ec6e4-c770-41e9-b202-ea0b58430fb2",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "4df7d4ea-b995-4c5b-a909-ba9d9e984f7e",
  "toolUseResult": {
    "query": "CORAL calibration steering multilingual cross-lingual 2602.06022",
    "results": [
      {
        "tool_use_id": "srvtoolu_018QoS6pwcTdF48ZSfTwGYvZ",
        "content": [
          {
            "title": "[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/abs/2602.06022"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens : Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "http://paperreading.club/page?id=374945"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL):",
            "url": "https://arxiv.org/pdf/2602.06022"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"
          },
          {
            "title": "[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2602.06022"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/html/2602.02326"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/html/2602.06022"
          },
          {
            "title": "Cross-Lingual Prompt Steerability: Towards Accurate and Robust LLM Behavior across Languages",
            "url": "https://arxiv.org/pdf/2512.02841"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper 2602.06022:\n\nThe paper is titled \"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering\" by Miranda Muqing Miao, Young-Min Cho, and Lyle Ungar, submitted on February 5, 2026.\n\n**Key Details:**\n\nLarge language models exhibit persistent miscalibration, especially after instruction tuning and preference alignment. While modified training objectives can improve calibration, retraining is expensive. Inference-time steering offers a lightweight alternative, yet most existing methods optimize proxies for correctness rather than correctness itself.\n\n**The CORAL Method:**\n\nCORAL is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes. By jointly optimizing for the accuracy and calibration components of the Brier score, CORAL improves both metrics and transfers its impact successfully to unseen benchmarks without any retraining.\n\n**Results:**\n\nThe paper evaluates CORAL across three 7B-parameter models and finds that it consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average. These gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements."
    ],
    "durationSeconds": 7.05142452500001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "874ec6e4-c770-41e9-b202-ea0b58430fb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T09:39:08.423Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CSuDd5tS685tvRpPEswZF6`</summary>

```json
{
  "query": "BaseCal \"Unsupervised Confidence Calibration via Base Model Signals\" arXiv 2601.03042 multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4df7d4ea-b995-4c5b-a909-ba9d9e984f7e",
  "isSidechain": false,
  "requestId": "req_011CbBhqjLiefVVfEAVsei9o",
  "type": "assistant",
  "uuid": "bcaa7383-0827-421b-bac7-037ad8148bb4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbQAA64QGFmu6s2HvpBA8N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1014,
      "cache_read_input_tokens": 32128,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1014,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 32128,
          "cache_creation_input_tokens": 1014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1014
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-19T09:39:15.603Z_

<details><summary>↩ Tool result · `toolu_01CSuDd5tS685tvRpPEswZF6`</summary>

```text
Web search results for query: "BaseCal "Unsupervised Confidence Calibration via Base Model Signals" arXiv 2601.03042 multilingual"

Links: [{"title":"[2601.03042v2] BaseCal: Unsupervised Confidence Calibration via Base Model Signals","url":"https://arxiv.org/abs/2601.03042v2"},{"title":"[2601.03042] BaseCal: Unsupervised Confidence Calibration via Base Model Signals","url":"https://arxiv.org/abs/2601.03042"},{"title":"BaseCal: Unsupervised Confidence Calibration via Base Model Signals","url":"https://arxiv.org/pdf/2601.03042"},{"title":"BaseCal: Unsupervised Confidence Calibration via Base Model Signals | OpenReview","url":"https://openreview.net/forum?id=QwGdjqq2pp"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1106&show=250"},{"title":"BaseCal: Unsupervised Confidence Calibration via Base Model Signals","url":"https://arxiv.org/html/2601.03042v1"},{"title":"BaseCal: Unsupervised Confidence Calibration via Base Model Signals Hexiang Tan","url":"https://web3.arxiv.org/pdf/2601.03042"},{"title":"Unsupervised Confidence Calibration for Reasoning LLMs from a Single Generation","url":"https://arxiv.org/html/2604.19444"}]

I found the paper successfully! Here's what the search reveals about BaseCal:

## Overview

BaseCal addresses the problem that widely deployed post-trained LLMs (PoLLMs) typically exhibit severe overconfidence, whereas their corresponding base LLMs often remain well-calibrated, motivating calibration of PoLLM confidence using the base LLM as a reference.

## Two Proposed Approaches

BaseCal-ReEval evaluates PoLLM's responses by feeding them into the base LLM to get average probabilities as confidence. However, this approach introduces additional inference overhead.

To address this, BaseCal-Proj trains a lightweight projection to map the final-layer hidden states of PoLLMs back to those of their base LLMs, with these projected states then processed by the base LLM's output layer to derive base-calibrated confidence for PoLLM's responses.

## Key Features and Results

BaseCal is an unsupervised, plug-and-play solution that operates without human labels or LLM modifications. Experiments across five datasets and three LLM families demonstrate effectiveness, reducing Expected Calibration Error (ECE) by an average of 42.90% compared to the best unsupervised baselines.

The paper is authored by Hexiang Tan and colleagues and was submitted to arXiv on January 6, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcaa7383-0827-421b-bac7-037ad8148bb4",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "c1954c51-f1bb-4268-b7ee-c86f75ecf3f3",
  "toolUseResult": {
    "query": "BaseCal \"Unsupervised Confidence Calibration via Base Model Signals\" arXiv 2601.03042 multilingual",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AhYdn9jiWBKJvBpEYTimok",
        "content": [
          {
            "title": "[2601.03042v2] BaseCal: Unsupervised Confidence Calibration via Base Model Signals",
            "url": "https://arxiv.org/abs/2601.03042v2"
          },
          {
            "title": "[2601.03042] BaseCal: Unsupervised Confidence Calibration via Base Model Signals",
            "url": "https://arxiv.org/abs/2601.03042"
          },
          {
            "title": "BaseCal: Unsupervised Confidence Calibration via Base Model Signals",
            "url": "https://arxiv.org/pdf/2601.03042"
          },
          {
            "title": "BaseCal: Unsupervised Confidence Calibration via Base Model Signals | OpenReview",
            "url": "https://openreview.net/forum?id=QwGdjqq2pp"
          },
          {
            "title": "Computer Science",
            "url": "https://www.arxiv.org/list/cs/recent?skip=1106&show=250"
          },
          {
            "title": "BaseCal: Unsupervised Confidence Calibration via Base Model Signals",
            "url": "https://arxiv.org/html/2601.03042v1"
          },
          {
            "title": "BaseCal: Unsupervised Confidence Calibration via Base Model Signals Hexiang Tan",
            "url": "https://web3.arxiv.org/pdf/2601.03042"
          },
          {
            "title": "Unsupervised Confidence Calibration for Reasoning LLMs from a Single Generation",
            "url": "https://arxiv.org/html/2604.19444"
          }
        ]
      },
      "I found the paper successfully! Here's what the search reveals about BaseCal:\n\n## Overview\n\nBaseCal addresses the problem that widely deployed post-trained LLMs (PoLLMs) typically exhibit severe overconfidence, whereas their corresponding base LLMs often remain well-calibrated, motivating calibration of PoLLM confidence using the base LLM as a reference.\n\n## Two Proposed Approaches\n\nBaseCal-ReEval evaluates PoLLM's responses by feeding them into the base LLM to get average probabilities as confidence. However, this approach introduces additional inference overhead.\n\nTo address this, BaseCal-Proj trains a lightweight projection to map the final-layer hidden states of PoLLMs back to those of their base LLMs, with these projected states then processed by the base LLM's output layer to derive base-calibrated confidence for PoLLM's responses.\n\n## Key Features and Results\n\nBaseCal is an unsupervised, plug-and-play solution that operates without human labels or LLM modifications. Experiments across five datasets and three LLM families demonstrate effectiveness, reducing Expected Calibration Error (ECE) by an average of 42.90% compared to the best unsupervised baselines.\n\nThe paper is authored by Hexiang Tan and colleagues and was submitted to arXiv on January 6, 2026."
    ],
    "durationSeconds": 7.175669840999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bcaa7383-0827-421b-bac7-037ad8148bb4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "c1954c51-f1bb-4268-b7ee-c86f75ecf3f3",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Tool call

_source line 48 · 2026-05-19T09:39:20.708Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H2g3EGYV4D7bW7x9Ahnt4J`</summary>

```json
{
  "query": "site:arxiv.org multilingual calibration LLM steering representation 2026 confidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1954c51-f1bb-4268-b7ee-c86f75ecf3f3",
  "isSidechain": false,
  "requestId": "req_011CbBhrW71rsdhAQjA23vFC",
  "type": "assistant",
  "uuid": "3cdf23ca-ba3d-44fb-b44b-3ff494666233",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtNKGEKrL3m1HWZL4gjUQn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 33142,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 825,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 33142,
          "cache_creation_input_tokens": 825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 825
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T09:39:27.261Z_

<details><summary>↩ Tool result · `toolu_01H2g3EGYV4D7bW7x9Ahnt4J`</summary>

```text
Web search results for query: "site:arxiv.org multilingual calibration LLM steering representation 2026 confidence"

Links: [{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/pdf/2505.12584"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt","url":"https://arxiv.org/pdf/2503.02863v1"},{"title":"Multicalibration for Confidence Scoring in LLMs","url":"https://arxiv.org/pdf/2404.04689"},{"title":"On the Calibration of Multilingual Question Answering LLMs","url":"https://arxiv.org/pdf/2311.08669"},{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework","url":"https://arxiv.org/html/2503.02863v1"},{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"}]

I found several relevant arxiv papers matching your search query. Here are the key results:

1. **"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models"** (October 2025)
   - This paper presents the first systematic evaluation of multilingual calibration across high-quality, human-curated datasets spanning over 100 languages and covering six prominent LLM families. A key finding is that late-intermediate layers consistently offer a more reliable and better-calibrated signal.

2. **"Improving Multilingual Language Models by Aligning Representations through Steering"** (May 2025)
   - This work learns a manifold that maps between English and target languages, then applies it during inference instead of fine-tuning, making it more efficient and less disruptive to the original model.

3. **"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework"** (March 2025)
   - The authors rigorously confirm the existence of directional confidence shifts by probing three models across 7 benchmarks, demonstrating that explicit instructions can inflate or deflate confidence scores in a regulated manner.

4. **"Multicalibration for Confidence Scoring in LLMs"** (April 2024)
   - This paper introduces novel variations of multicalibration methods for improving confidence scoring in LLMs.

5. **"On the Calibration of Multilingual Question Answering LLMs"** (November 2023)
   - This earlier work studies calibration of multilingual pre-trained LLMs like mBERT and XLM on various downstream tasks, showing that multilingual models are not well-calibrated in the classification setting, especially for low-resource languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cdf23ca-ba3d-44fb-b44b-3ff494666233",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "0afd7c22-0627-4d57-9717-bf30d49e26bb",
  "toolUseResult": {
    "query": "site:arxiv.org multilingual calibration LLM steering representation 2026 confidence",
    "results": [
      {
        "tool_use_id": "srvtoolu_011JNY3JWqACKwwV7KWKRrNv",
        "content": [
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          },
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/pdf/2505.12584"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/html/2510.03136v1"
          },
          {
            "title": "Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt",
            "url": "https://arxiv.org/pdf/2503.02863v1"
          },
          {
            "title": "Multicalibration for Confidence Scoring in LLMs",
            "url": "https://arxiv.org/pdf/2404.04689"
          },
          {
            "title": "On the Calibration of Multilingual Question Answering LLMs",
            "url": "https://arxiv.org/pdf/2311.08669"
          },
          {
            "title": "Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework",
            "url": "https://arxiv.org/html/2503.02863v1"
          },
          {
            "title": "[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/abs/2510.03136"
          }
        ]
      },
      "I found several relevant arxiv papers matching your search query. Here are the key results:\n\n1. **\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models\"** (October 2025)\n   - This paper presents the first systematic evaluation of multilingual calibration across high-quality, human-curated datasets spanning over 100 languages and covering six prominent LLM families. A key finding is that late-intermediate layers consistently offer a more reliable and better-calibrated signal.\n\n2. **\"Improving Multilingual Language Models by Aligning Representations through Steering\"** (May 2025)\n   - This work learns a manifold that maps between English and target languages, then applies it during inference instead of fine-tuning, making it more efficient and less disruptive to the original model.\n\n3. **\"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework\"** (March 2025)\n   - The authors rigorously confirm the existence of directional confidence shifts by probing three models across 7 benchmarks, demonstrating that explicit instructions can inflate or deflate confidence scores in a regulated manner.\n\n4. **\"Multicalibration for Confidence Scoring in LLMs\"** (April 2024)\n   - This paper introduces novel variations of multicalibration methods for improving confidence scoring in LLMs.\n\n5. **\"On the Calibration of Multilingual Question Answering LLMs\"** (November 2023)\n   - This earlier work studies calibration of multilingual pre-trained LLMs like mBERT and XLM on various downstream tasks, showing that multilingual models are not well-calibrated in the classification setting, especially for low-resource languages."
    ],
    "durationSeconds": 6.548787540999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3cdf23ca-ba3d-44fb-b44b-3ff494666233",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-19T09:39:31.180Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GWmdMNXXEz91Peb5212b7t`</summary>

```json
{
  "query": "cross-lingual calibration direction transfer zero-shot representation engineering confidence arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0afd7c22-0627-4d57-9717-bf30d49e26bb",
  "isSidechain": false,
  "requestId": "req_011CbBhsMuvbz2d6GSu6gQd1",
  "type": "assistant",
  "uuid": "fa6ba2cf-8a9d-4fc3-85f7-613aeb7e1505",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RG1SCArAL6oXZmML2vzW1W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 33967,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 33967,
          "cache_creation_input_tokens": 870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 870
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-19T09:39:37.634Z_

<details><summary>↩ Tool result · `toolu_01GWmdMNXXEz91Peb5212b7t`</summary>

```text
Web search results for query: "cross-lingual calibration direction transfer zero-shot representation engineering confidence arXiv 2026"

Links: [{"title":"Improving Zero-shot Multilingual Neural Machine Translation by   Leveraging Cross-lingual Consistency Regularization","url":"https://arxiv.org/pdf/2305.07310"},{"title":"Zero-shot Cross-Lingual Transfer in NLP","url":"https://www.emergentmind.com/topics/zero-shot-cross-lingual-transfer"},{"title":"On the Calibration of Massively Multilingual Language Models","url":"https://arxiv.org/pdf/2210.12265"},{"title":"Cross-lingual zero-shot transfer via semantic and synthetic representation learning","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12050870"},{"title":"The Impact of Cross-Lingual Adjustment of Contextual Word   Representations on Zero-Shot Transfer","url":"https://arxiv.org/pdf/2204.06457"},{"title":"Improving Zero-Shot Cross-Lingual Transfer via Progressive Code-Switching","url":"https://arxiv.org/html/2406.13361v1"}]

The search results cover various topics related to cross-lingual transfer, zero-shot learning, and calibration in multilingual NLP models. Here's what I found:

**Key Topics from Results:**

Several methods have been proposed to improve zero-shot translation performance by learning language-agnostic representations and maximizing cross-lingual transfer.

Zero-shot cross-lingual transfer represents shifts in data distribution where point estimates are likely to be miscalibrated, which is an important consideration for confidence calibration in these systems.

Cross-lingual adjustment methods use parallel corpora to make embeddings of related words across languages similar to each other.

Progressive code-switching methods have been proposed to mitigate negative impacts of uncontrolled code-switching data and improve multilingual representation alignment.

Success in zero-shot cross-lingual transfer relies on robust multilingual pretraining, effective representation alignment, and practical implementations including embedding and attention alignment, adversarial training, and parameter-efficient adaptations.

The results include papers from arXiv covering these topics, with the most recent papers being from 2024-2026. However, I didn't find a specific paper exactly matching all the keywords in your search query, so there may be a more recent 2026 paper on this exact combination of topics that wasn't captured in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa6ba2cf-8a9d-4fc3-85f7-613aeb7e1505",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "44d7aeac-978e-4146-9f5c-81e0075dd6a9",
  "toolUseResult": {
    "query": "cross-lingual calibration direction transfer zero-shot representation engineering confidence arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XkU3DjqefBwY9VcXCM4KiA",
        "content": [
          {
            "title": "Improving Zero-shot Multilingual Neural Machine Translation by   Leveraging Cross-lingual Consistency Regularization",
            "url": "https://arxiv.org/pdf/2305.07310"
          },
          {
            "title": "Zero-shot Cross-Lingual Transfer in NLP",
            "url": "https://www.emergentmind.com/topics/zero-shot-cross-lingual-transfer"
          },
          {
            "title": "On the Calibration of Massively Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2210.12265"
          },
          {
            "title": "Cross-lingual zero-shot transfer via semantic and synthetic representation learning",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12050870"
          },
          {
            "title": "The Impact of Cross-Lingual Adjustment of Contextual Word   Representations on Zero-Shot Transfer",
            "url": "https://arxiv.org/pdf/2204.06457"
          },
          {
            "title": "Improving Zero-Shot Cross-Lingual Transfer via Progressive Code-Switching",
            "url": "https://arxiv.org/html/2406.13361v1"
          }
        ]
      },
      "The search results cover various topics related to cross-lingual transfer, zero-shot learning, and calibration in multilingual NLP models. Here's what I found:\n\n**Key Topics from Results:**\n\nSeveral methods have been proposed to improve zero-shot translation performance by learning language-agnostic representations and maximizing cross-lingual transfer.\n\nZero-shot cross-lingual transfer represents shifts in data distribution where point estimates are likely to be miscalibrated, which is an important consideration for confidence calibration in these systems.\n\nCross-lingual adjustment methods use parallel corpora to make embeddings of related words across languages similar to each other.\n\nProgressive code-switching methods have been proposed to mitigate negative impacts of uncontrolled code-switching data and improve multilingual representation alignment.\n\nSuccess in zero-shot cross-lingual transfer relies on robust multilingual pretraining, effective representation alignment, and practical implementations including embedding and attention alignment, adversarial training, and parameter-efficient adaptations.\n\nThe results include papers from arXiv covering these topics, with the most recent papers being from 2024-2026. However, I didn't find a specific paper exactly matching all the keywords in your search query, so there may be a more recent 2026 paper on this exact combination of topics that wasn't captured in these results."
    ],
    "durationSeconds": 6.45079920399998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fa6ba2cf-8a9d-4fc3-85f7-613aeb7e1505",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-19T09:39:40.216Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PVRku8zrtnvBwP84CvM6jF`</summary>

```json
{
  "query": "\"confidence direction\" \"calibration direction\" cross-lingual multilingual transfer LLM hidden states 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44d7aeac-978e-4146-9f5c-81e0075dd6a9",
  "isSidechain": false,
  "requestId": "req_011CbBht8KPmXaWRt9KLPySD",
  "type": "assistant",
  "uuid": "a2f40938-3e78-4965-82b5-83b1e8b03120",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvgiwwBKAFrkcr8CPswJyY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 34837,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 34837,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-19T09:39:47.993Z_

<details><summary>↩ Tool result · `toolu_01PVRku8zrtnvBwP84CvM6jF`</summary>

```text
Web search results for query: ""confidence direction" "calibration direction" cross-lingual multilingual transfer LLM hidden states 2025 2026"

Links: [{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326"},{"title":"On the Calibration of Multilingual Question Answering LLMs","url":"https://arxiv.org/pdf/2311.08669"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"Understanding Cross-Lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2505.13141v1"},{"title":"Language-Specific Latent Process Hinders Cross-Lingual Performance","url":"https://arxiv.org/html/2505.13141v2"},{"title":"Lost in Alignment: A Survey on Cross-Lingual Alignment Methods for Contextualized Representation | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3764112"},{"title":"On the Calibration of Multilingual Question Answering LLMs","url":"https://arxiv.org/html/2311.08669v2"},{"title":"MKA: Leveraging Cross-Lingual Consensus for Model Abstention","url":"https://arxiv.org/pdf/2503.23687"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"}]

I found several highly relevant papers on cross-lingual transfer and calibration in multilingual LLMs. Here are the key findings:

## Recent Research on Confidence, Calibration, and Cross-Lingual Transfer

**Language Steering and Multilingual In-Context Learning:**
A training-free approach called language vectors computes mean activation differences between hidden states of parallel source and target language examples and adds them as an offset at inference time. When demonstrations are provided in a source language (English) but the test query is in a low-resource target language, models must internally recognize the language switch and transfer their task understanding across languages, a computationally and representationally demanding process that often fails.

**Calibration in Multilingual LLMs:**
Prior studies have primarily documented calibration issues at the final output layer, none have examined confidence behaviour in depth or investigated its architectural origins. Intermediate layers encode cross-lingual semantic knowledge in a largely language-agnostic manner, forming a shared representational space.

**Cross-Lingual Inconsistency:**
LLMs predict inconsistently and are less accurate because they rely on subspaces of individual languages, rather than working in a shared semantic space. However, knowledge sharing can be modulated by steering the models' latent processing towards the shared semantic space.

These papers from 2025-2026 demonstrate active research into steering hidden states and managing confidence directions across languages, with emphasis on manipulating latent representations for improved multilingual performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2f40938-3e78-4965-82b5-83b1e8b03120",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "7517d964-1547-4df0-8cbb-ea2b8f30e3da",
  "toolUseResult": {
    "query": "\"confidence direction\" \"calibration direction\" cross-lingual multilingual transfer LLM hidden states 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D5RiuaxzFoDPfDnVa8ckVE",
        "content": [
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/html/2602.02326"
          },
          {
            "title": "On the Calibration of Multilingual Question Answering LLMs",
            "url": "https://arxiv.org/pdf/2311.08669"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/html/2510.03136v1"
          },
          {
            "title": "Understanding Cross-Lingual Inconsistency in Large Language Models",
            "url": "https://arxiv.org/html/2505.13141v1"
          },
          {
            "title": "Language-Specific Latent Process Hinders Cross-Lingual Performance",
            "url": "https://arxiv.org/html/2505.13141v2"
          },
          {
            "title": "Lost in Alignment: A Survey on Cross-Lingual Alignment Methods for Contextualized Representation | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3764112"
          },
          {
            "title": "On the Calibration of Multilingual Question Answering LLMs",
            "url": "https://arxiv.org/html/2311.08669v2"
          },
          {
            "title": "MKA: Leveraging Cross-Lingual Consensus for Model Abstention",
            "url": "https://arxiv.org/pdf/2503.23687"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/pdf/2505.21772"
          }
        ]
      },
      "I found several highly relevant papers on cross-lingual transfer and calibration in multilingual LLMs. Here are the key findings:\n\n## Recent Research on Confidence, Calibration, and Cross-Lingual Transfer\n\n**Language Steering and Multilingual In-Context Learning:**\nA training-free approach called language vectors computes mean activation differences between hidden states of parallel source and target language examples and adds them as an offset at inference time. When demonstrations are provided in a source language (English) but the test query is in a low-resource target language, models must internally recognize the language switch and transfer their task understanding across languages, a computationally and representationally demanding process that often fails.\n\n**Calibration in Multilingual LLMs:**\nPrior studies have primarily documented calibration issues at the final output layer, none have examined confidence behaviour in depth or investigated its architectural origins. Intermediate layers encode cross-lingual semantic knowledge in a largely language-agnostic manner, forming a shared representational space.\n\n**Cross-Lingual Inconsistency:**\nLLMs predict inconsistently and are less accurate because they rely on subspaces of individual languages, rather than working in a shared semantic space. However, knowledge sharing can be modulated by steering the models' latent processing towards the shared semantic space.\n\nThese papers from 2025-2026 demonstrate active research into steering hidden states and managing confidence directions across languages, with emphasis on manipulating latent representations for improved multilingual performance."
    ],
    "durationSeconds": 7.771788136999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a2f40938-3e78-4965-82b5-83b1e8b03120",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-19T09:39:51.256Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015W2czFhMXCM8DofWLcYbJo`</summary>

```json
{
  "query": "SteerConf Zhou Jin Shi Li \"Steering LLMs for Confidence Elicitation\" NeurIPS 2025 arXiv 2503.02863"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7517d964-1547-4df0-8cbb-ea2b8f30e3da",
  "isSidechain": false,
  "requestId": "req_011CbBhtticXbdDPzJqsTnnc",
  "type": "assistant",
  "uuid": "d933a3e2-7137-4b8f-960f-6c385c2af857",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Z31Amd79wmJvc9eybkLfD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 35513,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 837,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 35513,
          "cache_creation_input_tokens": 837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 837
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-19T09:39:59.520Z_

<details><summary>↩ Tool result · `toolu_015W2czFhMXCM8DofWLcYbJo`</summary>

```text
Web search results for query: "SteerConf Zhou Jin Shi Li "Steering LLMs for Confidence Elicitation" NeurIPS 2025 arXiv 2503.02863"

Links: [{"title":"NeurIPS Poster SteerConf: Steering LLMs for Confidence Elicitation","url":"https://neurips.cc/virtual/2025/poster/119826"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://neurips.cc/media/neurips-2025/Slides/119826.pdf"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation | OpenReview","url":"https://openreview.net/forum?id=5sgK63Zshg"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/pdf/2503.02863"},{"title":"[2503.02863] SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/abs/2503.02863"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250302863Z/abstract"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/html/2503.02863v2"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation Ziang Zhou","url":"https://openreview.net/pdf/2dea5d57488bdb780105be0720fc4b246ed074ec.pdf"},{"title":"GitHub - scottjiao/SteerConf · GitHub","url":"https://github.com/scottjiao/SteerConf"}]

I found the paper! Here's information about **SteerConf: Steering LLMs for Confidence Elicitation**:

## Overview

The paper proposes SteerConf, a novel framework that systematically steers LLMs' confidence scores to improve their calibration and reliability, addressing the issue that large language models often suffer from overconfidence, limiting their reliability in critical applications.

## Key Components

SteerConf introduces three key components: (1) a steering prompt strategy that guides LLMs to produce confidence scores in specified directions (e.g., conservative or optimistic) by leveraging prompts with varying steering levels; (2) a steered confidence consistency measure that quantifies alignment across multiple steered confidences to enhance calibration; and (3) a steered confidence calibration method that aggregates confidence scores using consistency measures and applies linear quantization for answer selection.

## Key Advantages

SteerConf operates without additional training or fine-tuning, making it broadly applicable to existing LLMs.

## Experimental Results

Experiments on seven benchmarks spanning professional knowledge, common sense, ethics, and reasoning tasks, using advanced LLM models (GPT-3.5, LLaMA 3, GPT-4), demonstrate that SteerConf significantly outperforms existing methods, often by a significant margin. For example, SteerConf achieves up to a 39.8% reduction in ECE on GSM8K dataset with GPT-3.5 and a 43.3% improvement in AUROC on the Object Counting dataset with GPT-4.

## Authors and Publication

The paper is authored by Ziang Zhou, Tianyuan Jin, Jieming Shi, and Qing Li from The Hong Kong Polytechnic University and National University of Singapore. The paper was submitted on March 4, 2025, with the last revision on May 23, 2025 (arXiv 2503.02863).

The paper was published as a NeurIPS 2025 poster.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d933a3e2-7137-4b8f-960f-6c385c2af857",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "a5bf4d51-1fcf-4d7c-9e64-0b6deaabe1ab",
  "toolUseResult": {
    "query": "SteerConf Zhou Jin Shi Li \"Steering LLMs for Confidence Elicitation\" NeurIPS 2025 arXiv 2503.02863",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UfwWUKPuxmFw43iwTkLYRR",
        "content": [
          {
            "title": "NeurIPS Poster SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://neurips.cc/virtual/2025/poster/119826"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://neurips.cc/media/neurips-2025/Slides/119826.pdf"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation | OpenReview",
            "url": "https://openreview.net/forum?id=5sgK63Zshg"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/pdf/2503.02863"
          },
          {
            "title": "[2503.02863] SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/abs/2503.02863"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250302863Z/abstract"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/html/2503.02863v2"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation Ziang Zhou",
            "url": "https://openreview.net/pdf/2dea5d57488bdb780105be0720fc4b246ed074ec.pdf"
          },
          {
            "title": "GitHub - scottjiao/SteerConf · GitHub",
            "url": "https://github.com/scottjiao/SteerConf"
          }
        ]
      },
      "I found the paper! Here's information about **SteerConf: Steering LLMs for Confidence Elicitation**:\n\n## Overview\n\nThe paper proposes SteerConf, a novel framework that systematically steers LLMs' confidence scores to improve their calibration and reliability, addressing the issue that large language models often suffer from overconfidence, limiting their reliability in critical applications.\n\n## Key Components\n\nSteerConf introduces three key components: (1) a steering prompt strategy that guides LLMs to produce confidence scores in specified directions (e.g., conservative or optimistic) by leveraging prompts with varying steering levels; (2) a steered confidence consistency measure that quantifies alignment across multiple steered confidences to enhance calibration; and (3) a steered confidence calibration method that aggregates confidence scores using consistency measures and applies linear quantization for answer selection.\n\n## Key Advantages\n\nSteerConf operates without additional training or fine-tuning, making it broadly applicable to existing LLMs.\n\n## Experimental Results\n\nExperiments on seven benchmarks spanning professional knowledge, common sense, ethics, and reasoning tasks, using advanced LLM models (GPT-3.5, LLaMA 3, GPT-4), demonstrate that SteerConf significantly outperforms existing methods, often by a significant margin. For example, SteerConf achieves up to a 39.8% reduction in ECE on GSM8K dataset with GPT-3.5 and a 43.3% improvement in AUROC on the Object Counting dataset with GPT-4.\n\n## Authors and Publication\n\nThe paper is authored by Ziang Zhou, Tianyuan Jin, Jieming Shi, and Qing Li from The Hong Kong Polytechnic University and National University of Singapore. The paper was submitted on March 4, 2025, with the last revision on May 23, 2025 (arXiv 2503.02863).\n\nThe paper was published as a NeurIPS 2025 poster."
    ],
    "durationSeconds": 8.259166606000013,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d933a3e2-7137-4b8f-960f-6c385c2af857",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56 · 2026-05-19T09:39:59.523Z_

```json
{
  "parentUuid": "a5bf4d51-1fcf-4d7c-9e64-0b6deaabe1ab",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "22a2655d-769e-4fc8-b983-2865195115e1",
  "timestamp": "2026-05-19T09:39:59.523Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 57 · 2026-05-19T09:40:02.491Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0176sSNaoqx7vdBGXUxtp5FF`</summary>

```json
{
  "query": "Joshi Ahmad Modi \"Calibration Across Layers\" EMNLP 2025 calibration LLM intermediate layers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22a2655d-769e-4fc8-b983-2865195115e1",
  "isSidechain": false,
  "requestId": "req_011CbBhujuZhEQw3LZ2BwR5S",
  "type": "assistant",
  "uuid": "9b543bc0-43e8-4f80-88b7-b01e01c19cb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MLiN56SPwNYNYE63Xmpky2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 36350,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1138,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 36350,
          "cache_creation_input_tokens": 1138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1138
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "9b543bc0-43e8-4f80-88b7-b01e01c19cb0",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Tool result

_source line 60 · 2026-05-19T09:40:12.919Z_

<details><summary>↩ Tool result · `toolu_0176sSNaoqx7vdBGXUxtp5FF`</summary>

```text
Web search results for query: "Joshi Ahmad Modi "Calibration Across Layers" EMNLP 2025 calibration LLM intermediate layers"

Links: [{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.742/"},{"title":"GitHub - Exploration-Lab/LLM-Calibration-Mechanism · GitHub","url":"https://github.com/Exploration-Lab/LLM-Calibration-Mechanism"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=22850&show=2000"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs | Request PDF","url":"https://www.researchgate.net/publication/397421796_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"dblp: Ashutosh Modi","url":"https://dblp.org/pid/139/0873.html"},{"title":"(PDF) Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://www.researchgate.net/publication/397231243_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"[2511.00280] Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/abs/2511.00280"},{"title":"Ashutosh Modi's lab | Indian Institute of Technology Kanpur (IIT Kanpur)","url":"https://www.researchgate.net/lab/Exploration-Lab-Ashutosh-Modi-Lab-Ashutosh-Modi"}]

I found the paper! Here are the key details about "Calibration Across Layers: Understanding Calibration Evolution in LLMs":

**Publication Details:**
The paper "Calibration Across Layers: Understanding Calibration Evolution in LLMs" was authored by Abhinav Joshi, Areeb Ahmad, and Ashutosh Modi and published at the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) in Suzhou, China, with pages 14697–14725.

**Main Findings:**
Large Language Models (LLMs) have demonstrated inherent calibration capabilities, where predicted probabilities align well with correctness, despite prior findings that deep neural networks are often overconfident. The researchers analyzed multiple open-weight models on the MMLU benchmark and uncovered a distinct confidence correction phase in the upper/later layers, where model confidence is actively recalibrated after decision certainty has been reached.

**Key Technical Contributions:**
The researchers identified a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.

Their findings suggest that calibration is a distributed phenomenon, shaped throughout the network's forward pass, not just in its final projection, providing new insights into how confidence-regulating mechanisms operate within LLMs.

You can access the paper at the ACL Anthology (https://aclanthology.org/2025.emnlp-main.742/) or on arXiv (https://arxiv.org/abs/2511.00280).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b543bc0-43e8-4f80-88b7-b01e01c19cb0",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "9eb1d09d-6acf-4c8d-8295-25fa332a5d4f",
  "toolUseResult": {
    "query": "Joshi Ahmad Modi \"Calibration Across Layers\" EMNLP 2025 calibration LLM intermediate layers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Uigkv9d3i3RAvVpc2ivP7Q",
        "content": [
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.742/"
          },
          {
            "title": "GitHub - Exploration-Lab/LLM-Calibration-Mechanism · GitHub",
            "url": "https://github.com/Exploration-Lab/LLM-Calibration-Mechanism"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=22850&show=2000"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/397421796_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"
          },
          {
            "title": "dblp: Ashutosh Modi",
            "url": "https://dblp.org/pid/139/0873.html"
          },
          {
            "title": "(PDF) Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://www.researchgate.net/publication/397231243_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"
          },
          {
            "title": "[2511.00280] Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://arxiv.org/abs/2511.00280"
          },
          {
            "title": "Ashutosh Modi's lab | Indian Institute of Technology Kanpur (IIT Kanpur)",
            "url": "https://www.researchgate.net/lab/Exploration-Lab-Ashutosh-Modi-Lab-Ashutosh-Modi"
          }
        ]
      },
      "I found the paper! Here are the key details about \"Calibration Across Layers: Understanding Calibration Evolution in LLMs\":\n\n**Publication Details:**\nThe paper \"Calibration Across Layers: Understanding Calibration Evolution in LLMs\" was authored by Abhinav Joshi, Areeb Ahmad, and Ashutosh Modi and published at the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) in Suzhou, China, with pages 14697–14725.\n\n**Main Findings:**\nLarge Language Models (LLMs) have demonstrated inherent calibration capabilities, where predicted probabilities align well with correctness, despite prior findings that deep neural networks are often overconfident. The researchers analyzed multiple open-weight models on the MMLU benchmark and uncovered a distinct confidence correction phase in the upper/later layers, where model confidence is actively recalibrated after decision certainty has been reached.\n\n**Key Technical Contributions:**\nThe researchers identified a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.\n\nTheir findings suggest that calibration is a distributed phenomenon, shaped throughout the network's forward pass, not just in its final projection, providing new insights into how confidence-regulating mechanisms operate within LLMs.\n\nYou can access the paper at the ACL Anthology (https://aclanthology.org/2025.emnlp-main.742/) or on arXiv (https://arxiv.org/abs/2511.00280)."
    ],
    "durationSeconds": 10.424037533000025,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9b543bc0-43e8-4f80-88b7-b01e01c19cb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T09:40:15.706Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Gz2uWjUUyXrDCpa1VnkaR`</summary>

```json
{
  "query": "AAAI 2027 submission deadline July 2026 call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9eb1d09d-6acf-4c8d-8295-25fa332a5d4f",
  "isSidechain": false,
  "requestId": "req_011CbBhvj8hp42XUDrnfSwMk",
  "type": "assistant",
  "uuid": "d84170d3-8067-4d45-ba58-521339a408de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gLDpDtV1cxfsK6cJzrWmR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 923,
      "cache_read_input_tokens": 37488,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 37488,
          "cache_creation_input_tokens": 923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 923
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T09:40:19.917Z_

<details><summary>↩ Tool result · `toolu_012Gz2uWjUUyXrDCpa1VnkaR`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline July 2026 call for papers"

Links: [{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"}]

Based on the search results, here's the information about AAAI 2027 submission deadlines:

The full paper submission deadline for AAAI 2027 is July 28, 2026 at 11:59 PM UTC-12. The abstract submission deadline is July 21, 2026 at 11:59 PM UTC-12, and supplementary material and code are due by July 31, 2026 at 11:59 PM UTC-12.

The Open Review submission site opens for author registration on June 17, 2026 and for paper submission on June 24, 2026.

AAAI 2027 is being held in Montréal, Québec, Canada on February 16-23, 2027. The official call for papers can be found at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d84170d3-8067-4d45-ba58-521339a408de",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "4f94680d-ecf6-4ace-83a7-248e967ecce1",
  "toolUseResult": {
    "query": "AAAI 2027 submission deadline July 2026 call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EK2mUTiHvEMxBfuWCVEDxz",
        "content": [
          {
            "title": "AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot",
            "url": "https://www.getpaperpilot.com/deadlines/aaai-2027.html"
          },
          {
            "title": "AI Deadlines – AI Conference Call For Paper Deadlines",
            "url": "http://aideadlines.org/conference/?id=aaai27"
          },
          {
            "title": "Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "AAAI-27 Main Technical Track - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"
          },
          {
            "title": "AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/aaai"
          },
          {
            "title": "Key deadlines in AI and ML conferences | Yutori",
            "url": "https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"
          },
          {
            "title": "AAAI-26 Submission Instructions - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/submission-instructions/"
          },
          {
            "title": "🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...",
            "url": "https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"
          },
          {
            "title": "AAAI 2027 Conference | OpenReview",
            "url": "https://openreview.net/group?id=AAAI.org%2F2027%2FConference"
          }
        ]
      },
      "Based on the search results, here's the information about AAAI 2027 submission deadlines:\n\nThe full paper submission deadline for AAAI 2027 is July 28, 2026 at 11:59 PM UTC-12. The abstract submission deadline is July 21, 2026 at 11:59 PM UTC-12, and supplementary material and code are due by July 31, 2026 at 11:59 PM UTC-12.\n\nThe Open Review submission site opens for author registration on June 17, 2026 and for paper submission on June 24, 2026.\n\nAAAI 2027 is being held in Montréal, Québec, Canada on February 16-23, 2027. The official call for papers can be found at https://aaai.org/conference/aaai/aaai-27/."
    ],
    "durationSeconds": 4.205793105999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d84170d3-8067-4d45-ba58-521339a408de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T09:40:23.035Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Bh6Xtx63yGf1ozCqokqqE`</summary>

```json
{
  "query": "ARR August 2026 submission deadline ACL Rolling Review EACL NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f94680d-ecf6-4ace-83a7-248e967ecce1",
  "isSidechain": false,
  "requestId": "req_011CbBhwF3Hf6nThydL8cCUj",
  "type": "assistant",
  "uuid": "e8dbcce3-822f-419f-8e41-e4cff39707ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXNrdV7njKUPkgLMcwfaeE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 38411,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 885,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 38411,
          "cache_creation_input_tokens": 885,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 885
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T09:40:29.216Z_

<details><summary>↩ Tool result · `toolu_011Bh6Xtx63yGf1ozCqokqqE`</summary>

```text
Web search results for query: "ARR August 2026 submission deadline ACL Rolling Review EACL NAACL"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"}]

Based on the search results, here's what I found regarding ARR (ACL Rolling Review) submission deadlines for August 2026:

The August 2026 ARR submission deadline is August 3, 2026. However, this deadline is specifically for papers aiming to commit to EACL 2027, with a commitment date of October 11, 2026.

For the other major *ACL conferences in 2026, the earlier submission deadlines are:
- EMNLP 2026: May 25, 2026 (commitment by August 2, 2026)
- AACL 2026: May 25, 2026 (commitment by August 26, 2026)

So while there is an August 3, 2026 deadline for ARR submissions intended for EACL 2027, submissions for EMNLP 2026 and AACL 2026 have already passed (they were due in May 2026). Note that NAACL does not appear to have a 2026 conference listed in the current ARR schedule.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8dbcce3-822f-419f-8e41-e4cff39707ab",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "efd5d99e-891b-428c-a27b-4870ad6642a7",
  "toolUseResult": {
    "query": "ARR August 2026 submission deadline ACL Rolling Review EACL NAACL",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JKY8j2ZkoeGejyZ6Ear2ym",
        "content": [
          {
            "title": "Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "aclrollingreview/dates.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/dates.md"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "https://aclrollingreview.org/"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "ACL ARR | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2FARR"
          },
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "ACLRollingReview (@ReviewAcl) / Posts / X",
            "url": "https://x.com/ReviewAcl"
          },
          {
            "title": "ACL ARR 2026 March | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"
          }
        ]
      },
      "Based on the search results, here's what I found regarding ARR (ACL Rolling Review) submission deadlines for August 2026:\n\nThe August 2026 ARR submission deadline is August 3, 2026. However, this deadline is specifically for papers aiming to commit to EACL 2027, with a commitment date of October 11, 2026.\n\nFor the other major *ACL conferences in 2026, the earlier submission deadlines are:\n- EMNLP 2026: May 25, 2026 (commitment by August 2, 2026)\n- AACL 2026: May 25, 2026 (commitment by August 26, 2026)\n\nSo while there is an August 3, 2026 deadline for ARR submissions intended for EACL 2027, submissions for EMNLP 2026 and AACL 2026 have already passed (they were due in May 2026). Note that NAACL does not appear to have a 2026 conference listed in the current ARR schedule."
    ],
    "durationSeconds": 6.177409308000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e8dbcce3-822f-419f-8e41-e4cff39707ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T09:40:35.449Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NTTGxfmsoS9MVjMypVFPEC`</summary>

```json
{
  "query": "NAACL 2027 ARR October 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efd5d99e-891b-428c-a27b-4870ad6642a7",
  "isSidechain": false,
  "requestId": "req_011CbBhwvsB3ZRiGT71JSWAk",
  "type": "assistant",
  "uuid": "d3c62127-2d70-4758-bcf4-590f2a0db391",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWP1aL2E8hZ9LwBUgrdYzo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 39296,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 39296,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 781
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T09:40:40.454Z_

<details><summary>↩ Tool result · `toolu_01NTTGxfmsoS9MVjMypVFPEC`</summary>

```text
Web search results for query: "NAACL 2027 ARR October 2026 submission deadline call for papers"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"Community announcement: Submission dates and process for EACL, NAACL and ACL","url":"https://www.aclweb.org/portal/sites/default/files/Submission%20Dates%20and%20Process%20for%20EACL_NAACL%20and%20ACL%202024-2.pdf"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"NAACL 2026 - Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/naacl"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"}]

Based on my search results, I found information about NAACL 2027 and ARR submission deadlines:

For NAACL (North American Chapter of the ACL), the ARR commitment deadline is October 16, 2026, 11:59 AM UTC, with the conference scheduled for April/May 2027.

This indicates that while papers are submitted to the ARR (ACL Rolling Review) system in earlier cycles, authors who want to commit their reviewed papers to NAACL 2027 have an October 16, 2026 deadline.

The search results also note that starting from 2024, all main *ACL conferences used ARR exclusively, meaning NAACL 2027 will follow the ARR submission process rather than accepting direct submissions.

If you're looking for the actual ARR submission deadline for papers that would eventually be committed to NAACL 2027, those would be in an earlier ARR cycle (likely in August 2026 or earlier, based on the 10-week cycle schedule mentioned in the search results).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3c62127-2d70-4758-bcf4-590f2a0db391",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "b40cf2dd-e044-45cf-815f-f3e7b227cdda",
  "toolUseResult": {
    "query": "NAACL 2027 ARR October 2026 submission deadline call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_016aK9C7H3L96ZFQN9zZU32p",
        "content": [
          {
            "title": "Dates and Venues",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "Year-Round Deadlines - Imranur Rahman",
            "url": "https://imranur-rahman.github.io/deadlines/"
          },
          {
            "title": "NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=2170"
          },
          {
            "title": "NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)",
            "url": "https://naacl.org/"
          },
          {
            "title": "Second Call for Main Conference Papers - NAACL-HLT 2025",
            "url": "https://2025.naacl.org/calls/papers/"
          },
          {
            "title": "Community announcement: Submission dates and process for EACL, NAACL and ACL",
            "url": "https://www.aclweb.org/portal/sites/default/files/Submission%20Dates%20and%20Process%20for%20EACL_NAACL%20and%20ACL%202024-2.pdf"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "aclrollingreview/dates.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/dates.md"
          },
          {
            "title": "NAACL 2026 - Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics Deadline | ConferenceDeadlines.com",
            "url": "https://www.conferencedeadlines.com/venue/naacl"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          }
        ]
      },
      "Based on my search results, I found information about NAACL 2027 and ARR submission deadlines:\n\nFor NAACL (North American Chapter of the ACL), the ARR commitment deadline is October 16, 2026, 11:59 AM UTC, with the conference scheduled for April/May 2027.\n\nThis indicates that while papers are submitted to the ARR (ACL Rolling Review) system in earlier cycles, authors who want to commit their reviewed papers to NAACL 2027 have an October 16, 2026 deadline.\n\nThe search results also note that starting from 2024, all main *ACL conferences used ARR exclusively, meaning NAACL 2027 will follow the ARR submission process rather than accepting direct submissions.\n\nIf you're looking for the actual ARR submission deadline for papers that would eventually be committed to NAACL 2027, those would be in an earlier ARR cycle (likely in August 2026 or earlier, based on the 10-week cycle schedule mentioned in the search results)."
    ],
    "durationSeconds": 4.997483120000019,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d3c62127-2d70-4758-bcf4-590f2a0db391",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-19T09:40:43.974Z_

Good. Now let me search for the most critical potential competing work — anyone doing cross-lingual calibration transfer via representation geometry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b40cf2dd-e044-45cf-815f-f3e7b227cdda",
  "isSidechain": false,
  "requestId": "req_011CbBhxm7pTGZgyi3NQ3bYe",
  "type": "assistant",
  "uuid": "92709337-50e4-4ff8-8d39-417ba76bc3aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EK2SwRwi6zKqzvqhsHZEG7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 824,
      "cache_read_input_tokens": 40077,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 40077,
          "cache_creation_input_tokens": 824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 824
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-19T09:40:44.334Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016vvDrhngPzghuEFA6aA3iU`</summary>

```json
{
  "query": "\"calibration transfer\" \"representation space\" multilingual LLM zero-shot English 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92709337-50e4-4ff8-8d39-417ba76bc3aa",
  "isSidechain": false,
  "requestId": "req_011CbBhxm7pTGZgyi3NQ3bYe",
  "type": "assistant",
  "uuid": "7614888e-e270-4763-8ae6-0bf9a973e02a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EK2SwRwi6zKqzvqhsHZEG7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 824,
      "cache_read_input_tokens": 40077,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 40077,
          "cache_creation_input_tokens": 824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 824
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-19T09:40:50.626Z_

<details><summary>↩ Tool result · `toolu_016vvDrhngPzghuEFA6aA3iU`</summary>

```text
Web search results for query: ""calibration transfer" "representation space" multilingual LLM zero-shot English 2025 2026"

Links: [{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"On the Calibration of Massively Multilingual Language Models","url":"https://arxiv.org/pdf/2210.12265"},{"title":"Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=vQhn4wrQ6j"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"On the Calibration of Multilingual Question Answering LLMs","url":"https://arxiv.org/pdf/2311.08669"},{"title":"On Representation Transfer in Zero-Shot Multilingual ...","url":"https://aclanthology.org/2025.mtsummit-1.7.pdf"},{"title":"Languages Transferred Within the Encoder: On Representation Transfer in Zero-Shot Multilingual Translation","url":"https://arxiv.org/html/2406.08092v2"},{"title":"LUSIFER: Language Universal Space Integration for Enhanced Multilingual   Embeddings with Large Language Models","url":"https://arxiv.org/pdf/2501.00874"}]

I found several relevant papers on this topic. Here are the search results:

**Key Recent Research (2025-2026):**

1. **"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models"** (October 2025)
   - Conducts the first large-scale systematic studies of multilingual calibration, analyzing six major model families and over 100 languages using high-quality, human-curated benchmarks
   - Reveals that non-English languages consistently exhibit lower accuracy and dramatically worse calibration—for instance, LLaMA-3's Expected Calibration Error (ECE) is nearly five times higher on average for non-English than for English

2. **"On Representation Transfer in Zero-Shot Multilingual Translation"** (April 2025)
   - Identifies that zero-shot translation deficiency arises because the representation of a translation is entangled with other languages and not transferred to the target language effectively

3. **"LUSIFER: Language Universal Space Integration for Enhanced Multilingual Embeddings with Large Language Models"** (January 2025)
   - Presents a zero-shot approach that combines a multilingual encoder with an LLM-based embedding model, integrated through trainable parameters that transfer the multilingual encoder's language understanding capabilities to the specialized embedding model

4. **"On the Calibration of Massively Multilingual Language Models"** (2022)
   - Shows that calibration methods like temperature scaling and label smoothing do reasonably well towards improving calibration in the zero-shot scenario

These papers address the intersection of calibration, representation spaces, and zero-shot cross-lingual transfer in multilingual LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7614888e-e270-4763-8ae6-0bf9a973e02a",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "2e87aae8-a7c6-46ae-8252-14f290247fb8",
  "toolUseResult": {
    "query": "\"calibration transfer\" \"representation space\" multilingual LLM zero-shot English 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UEdTswB82s6XZpLEajwzed",
        "content": [
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          },
          {
            "title": "On the Calibration of Massively Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2210.12265"
          },
          {
            "title": "Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=vQhn4wrQ6j"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/html/2510.03136v1"
          },
          {
            "title": "On the Calibration of Multilingual Question Answering LLMs",
            "url": "https://arxiv.org/pdf/2311.08669"
          },
          {
            "title": "On Representation Transfer in Zero-Shot Multilingual ...",
            "url": "https://aclanthology.org/2025.mtsummit-1.7.pdf"
          },
          {
            "title": "Languages Transferred Within the Encoder: On Representation Transfer in Zero-Shot Multilingual Translation",
            "url": "https://arxiv.org/html/2406.08092v2"
          },
          {
            "title": "LUSIFER: Language Universal Space Integration for Enhanced Multilingual   Embeddings with Large Language Models",
            "url": "https://arxiv.org/pdf/2501.00874"
          }
        ]
      },
      "I found several relevant papers on this topic. Here are the search results:\n\n**Key Recent Research (2025-2026):**\n\n1. **\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models\"** (October 2025)\n   - Conducts the first large-scale systematic studies of multilingual calibration, analyzing six major model families and over 100 languages using high-quality, human-curated benchmarks\n   - Reveals that non-English languages consistently exhibit lower accuracy and dramatically worse calibration—for instance, LLaMA-3's Expected Calibration Error (ECE) is nearly five times higher on average for non-English than for English\n\n2. **\"On Representation Transfer in Zero-Shot Multilingual Translation\"** (April 2025)\n   - Identifies that zero-shot translation deficiency arises because the representation of a translation is entangled with other languages and not transferred to the target language effectively\n\n3. **\"LUSIFER: Language Universal Space Integration for Enhanced Multilingual Embeddings with Large Language Models\"** (January 2025)\n   - Presents a zero-shot approach that combines a multilingual encoder with an LLM-based embedding model, integrated through trainable parameters that transfer the multilingual encoder's language understanding capabilities to the specialized embedding model\n\n4. **\"On the Calibration of Massively Multilingual Language Models\"** (2022)\n   - Shows that calibration methods like temperature scaling and label smoothing do reasonably well towards improving calibration in the zero-shot scenario\n\nThese papers address the intersection of calibration, representation spaces, and zero-shot cross-lingual transfer in multilingual LLMs."
    ],
    "durationSeconds": 6.288638586999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7614888e-e270-4763-8ae6-0bf9a973e02a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "2e87aae8-a7c6-46ae-8252-14f290247fb8",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Tool call

_source line 72 · 2026-05-19T09:40:53.566Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015EsDtmUn5NTJe3Zd3MwNdR`</summary>

```json
{
  "query": "Chimoto \"Calibrating Beyond English\" EACL 2026 multilingual calibration quantized LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e87aae8-a7c6-46ae-8252-14f290247fb8",
  "isSidechain": false,
  "requestId": "req_011CbBhyWLbfUxSHwZU5wTMi",
  "type": "assistant",
  "uuid": "bd8e5f79-2123-44bb-bb33-51e29c514b4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPvhqUradkTxkm6fvfFdVb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 40901,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 40901,
          "cache_creation_input_tokens": 884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 884
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-19T09:40:59.924Z_

<details><summary>↩ Tool result · `toolu_015EsDtmUn5NTJe3Zd3MwNdR`</summary>

```text
Web search results for query: "Chimoto "Calibrating Beyond English" EACL 2026 multilingual calibration quantized LLM"

Links: [{"title":"Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLMs - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.223/"},{"title":"Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM","url":"https://arxiv.org/pdf/2601.18306"},{"title":"[2601.18306] Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM","url":"https://arxiv.org/abs/2601.18306"},{"title":"Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLMs","url":"https://arxiv.org/html/2601.18306"},{"title":"Post-Training Quantization Methods","url":"https://www.emergentmind.com/topics/post-training-quantization-methods"},{"title":"Language Diversity for Better Quantized Multilingual LLMs","url":"https://aclanthology.org/2026.eacl-long.223.pdf"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"}]

I found the paper you're looking for! Here are the search results:

The paper "Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLMs" was published in the Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026) in Rabat, Morocco.

**Key Details:**

- **Authors:** Everlyn Asiko Chimoto, Mostafa Elhoushi, and Bruce Bassett
- **Focus:** The paper examines how existing post-training quantization methods typically use small, English-only calibration sets and systematically evaluates eight calibration settings (five single-language and three multilingual mixes) on two quantizers (GPTQ, AWQ) on data from 10 languages

**Main Findings:**

Non-English and multilingual calibration sets significantly improve perplexity compared to English-only baselines, with multilingual mixes achieving the largest overall reductions of up to 3.52 points in perplexity on Llama3.1 8B and Qwen2.5 7B. Additionally, tailoring calibration sets to the evaluation language yields the largest improvements for individual languages, underscoring the importance of linguistic alignment.

The paper is available through both the ACL Anthology and arXiv (paper ID: 2601.18306).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd8e5f79-2123-44bb-bb33-51e29c514b4a",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "7462a80b-87c3-4da7-93b8-ebb406536798",
  "toolUseResult": {
    "query": "Chimoto \"Calibrating Beyond English\" EACL 2026 multilingual calibration quantized LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JS44CsCoV3iP5GZLrgi2YK",
        "content": [
          {
            "title": "Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2026.eacl-long.223/"
          },
          {
            "title": "Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM",
            "url": "https://arxiv.org/pdf/2601.18306"
          },
          {
            "title": "[2601.18306] Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM",
            "url": "https://arxiv.org/abs/2601.18306"
          },
          {
            "title": "Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLMs",
            "url": "https://arxiv.org/html/2601.18306"
          },
          {
            "title": "Post-Training Quantization Methods",
            "url": "https://www.emergentmind.com/topics/post-training-quantization-methods"
          },
          {
            "title": "Language Diversity for Better Quantized Multilingual LLMs",
            "url": "https://aclanthology.org/2026.eacl-long.223.pdf"
          },
          {
            "title": "Main Conference Accepted Papers -",
            "url": "https://2026.eacl.org/program/main-accepted/"
          }
        ]
      },
      "I found the paper you're looking for! Here are the search results:\n\nThe paper \"Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLMs\" was published in the Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026) in Rabat, Morocco.\n\n**Key Details:**\n\n- **Authors:** Everlyn Asiko Chimoto, Mostafa Elhoushi, and Bruce Bassett\n- **Focus:** The paper examines how existing post-training quantization methods typically use small, English-only calibration sets and systematically evaluates eight calibration settings (five single-language and three multilingual mixes) on two quantizers (GPTQ, AWQ) on data from 10 languages\n\n**Main Findings:**\n\nNon-English and multilingual calibration sets significantly improve perplexity compared to English-only baselines, with multilingual mixes achieving the largest overall reductions of up to 3.52 points in perplexity on Llama3.1 8B and Qwen2.5 7B. Additionally, tailoring calibration sets to the evaluation language yields the largest improvements for individual languages, underscoring the importance of linguistic alignment.\n\nThe paper is available through both the ACL Anthology and arXiv (paper ID: 2601.18306)."
    ],
    "durationSeconds": 6.354890240000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bd8e5f79-2123-44bb-bb33-51e29c514b4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-19T09:41:03.314Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X9PGXnaJTcTFA85NCmBVqA`</summary>

```json
{
  "query": "CLaS-Bench cross-lingual activation steering benchmark arXiv 2601.08331 DiffMean 84.5%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7462a80b-87c3-4da7-93b8-ebb406536798",
  "isSidechain": false,
  "requestId": "req_011CbBhzCCxpsAQ4zUn9t1KY",
  "type": "assistant",
  "uuid": "ae52b883-79c7-4b42-b49c-4116fca6786e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W7Z7xHhQiT8Fx9AsGZpueQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1637,
      "cache_read_input_tokens": 40901,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 40901,
          "cache_creation_input_tokens": 1637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1637
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-19T09:41:09.753Z_

<details><summary>↩ Tool result · `toolu_01X9PGXnaJTcTFA85NCmBVqA`</summary>

```text
Web search results for query: "CLaS-Bench cross-lingual activation steering benchmark arXiv 2601.08331 DiffMean 84.5%"

Links: [{"title":"[2601.08331] CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/abs/2601.08331"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/html/2601.08331"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/pdf/2601.08331"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"},{"title":"[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/abs/2601.16390"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/html/2601.16390v1"}]

Based on the web search results, I found information about CLaS-Bench (arXiv 2601.08331):

CLaS-Bench is a lightweight parallel-question benchmark for evaluating language-forcing behavior in LLMs across 32 languages, enabling systematic evaluation of multilingual steering methods. 

The benchmark evaluates a broad array of steering techniques, including residual-stream DiffMean interventions, probe-derived directions, language-specific neurons, PCA/LDA vectors, and Sparse Autoencoders. Steering performance is measured along two axes: language control and semantic relevance, combined into a single harmonic-mean steering score.

Regarding the DiffMean method you mentioned: the simple residual-based DiffMean method consistently outperforms all other methods across languages. A layer-wise analysis reveals that language-specific structure emerges predominantly in later layers and steering directions cluster based on language family.

CLaS-Bench is the first standardized benchmark for multilingual steering, enabling both rigorous scientific analysis of language representations and practical evaluation of steering as a low-cost adaptation alternative.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae52b883-79c7-4b42-b49c-4116fca6786e",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "a1b04470-0303-4072-b78f-15248b2f8f9a",
  "toolUseResult": {
    "query": "CLaS-Bench cross-lingual activation steering benchmark arXiv 2601.08331 DiffMean 84.5%",
    "results": [
      {
        "tool_use_id": "srvtoolu_019sMtgk3DFxE8XAJCT2WnqA",
        "content": [
          {
            "title": "[2601.08331] CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark",
            "url": "https://arxiv.org/abs/2601.08331"
          },
          {
            "title": "CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark",
            "url": "https://arxiv.org/html/2601.08331"
          },
          {
            "title": "CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark",
            "url": "https://arxiv.org/pdf/2601.08331"
          },
          {
            "title": "Cross-Lingual Activation Steering for Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2601.16390"
          },
          {
            "title": "[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models",
            "url": "https://arxiv.org/abs/2601.16390"
          },
          {
            "title": "Cross-Lingual Activation Steering for Multilingual Language Models",
            "url": "https://arxiv.org/html/2601.16390v1"
          }
        ]
      },
      "Based on the web search results, I found information about CLaS-Bench (arXiv 2601.08331):\n\nCLaS-Bench is a lightweight parallel-question benchmark for evaluating language-forcing behavior in LLMs across 32 languages, enabling systematic evaluation of multilingual steering methods. \n\nThe benchmark evaluates a broad array of steering techniques, including residual-stream DiffMean interventions, probe-derived directions, language-specific neurons, PCA/LDA vectors, and Sparse Autoencoders. Steering performance is measured along two axes: language control and semantic relevance, combined into a single harmonic-mean steering score.\n\nRegarding the DiffMean method you mentioned: the simple residual-based DiffMean method consistently outperforms all other methods across languages. A layer-wise analysis reveals that language-specific structure emerges predominantly in later layers and steering directions cluster based on language family.\n\nCLaS-Bench is the first standardized benchmark for multilingual steering, enabling both rigorous scientific analysis of language representations and practical evaluation of steering as a low-cost adaptation alternative."
    ],
    "durationSeconds": 6.435526171000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ae52b883-79c7-4b42-b49c-4116fca6786e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-19T09:41:13.091Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CFVUNqYzJFgjttuAXbDkx4`</summary>

```json
{
  "query": "Qwen 3.6 27B model architecture DeltaNet hybrid GatedDeltaNet attention 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1b04470-0303-4072-b78f-15248b2f8f9a",
  "isSidechain": false,
  "requestId": "req_011CbBhzvC5oBDbEkg4X9egi",
  "type": "assistant",
  "uuid": "93e7479a-0952-470e-a969-c63fa34adbae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RggDvERDuJx4Wp9PuJ4KmM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 42538,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 42538,
          "cache_creation_input_tokens": 654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 654
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-19T09:41:25.116Z_

<details><summary>↩ Tool result · `toolu_01CFVUNqYzJFgjttuAXbDkx4`</summary>

```text
Web search results for query: "Qwen 3.6 27B model architecture DeltaNet hybrid GatedDeltaNet attention 2026"

Links: [{"title":"Qwen3.6-27B: 27B Model Beats 397B on Coding (2026)","url":"https://www.buildfastwithai.com/blogs/qwen3-6-27b-review-2026"},{"title":"Qwen3.6-27B Explained: Agentic Coding, Hybrid Architecture, Benchmarks & API on Qubrid AI - Qubrid AI","url":"https://www.qubrid.com/blog/qwen36-27b-explained-agentic-coding-hybrid-architecture-benchmarks-api-on-qubrid-ai"},{"title":"Qwen3.6–27B Is Here: A Practical Open-Weight Model for Agentic Coding | by Cristian Marcu | Apr, 2026 | Medium","url":"https://medium.com/@cristian-marcu/qwen3-6-27b-is-here-a-practical-open-weight-model-for-agentic-coding-433be43df637"},{"title":"Qwen3.6-27B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen3.6-27b"},{"title":"Qwen3.6-27B is here. How to use Qwen3.6–27B for free? | by Mehul Gupta | Data Science in Your Pocket | Apr, 2026 | Medium","url":"https://medium.com/data-science-in-your-pocket/qwen3-27b-is-here-197fb2256b97"},{"title":"An Overnight Stack for Qwen3.6–27B: 85 TPS, 125K Context, Vision — on One RTX 3090 | Medium","url":"https://medium.com/@fzbcwvv/an-overnight-stack-for-qwen3-6-27b-85-tps-125k-context-vision-on-one-rtx-3090-0d95c6291914"},{"title":"Alibaba Qwen Team Releases Qwen3.6-27B: A Dense Open-Weight Model Outperforming 397B MoE on Agentic Coding Benchmarks - MarkTechPost","url":"https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/"},{"title":"How to Use Qwen3.6-27B: Complete Guide to Alibaba's New Open-Weight Coding Model | Tosea.ai","url":"https://tosea.ai/blog/qwen-3-6-27b-complete-guide"}]

Based on the search results, here's what I found about the Qwen3.6-27B model architecture:

## Model Release & Overview

Qwen3.6-27B is a dense causal language model with an integrated vision encoder, released by Alibaba's Qwen team in April 2026. It was released on April 22, 2026 under the Apache 2.0 license.

## Hybrid Architecture (DeltaNet + Gated Attention)

The model introduces a hybrid attention mechanism combining Gated DeltaNet linear attention with standard Gated Attention. More specifically, Qwen3.6-27B is organized as 64 layers, structured as 16 repeating blocks, each composed of three Gated DeltaNet sublayers followed by a single Gated Attention sublayer, with feed-forward networks interleaved throughout.

## Technical Details

The 64-layer language model uses a hybrid layout of 16 repeats of (3 × Gated DeltaNet → FFN, 1 × Gated Attention → FFN) with hidden dim 5120 and FFN intermediate 17408 — Gated DeltaNet has 48/16 heads for V/QK (head dim 128) and Gated Attention has 24/4 heads for Q/KV (head dim 256).

## Design Rationale

Three-quarters of the model's attention budget runs on linear attention; only every fourth sublayer performs full self-attention. Gated DeltaNet, a linear-attention variant, trades a small amount of expressive capacity for O(n) complexity. Full Gated Attention appears only where it earns its keep — roughly once per block — to preserve the long-range precision that linear attention alone cannot.

## Context Window

It supports a native 262,144-token context extensible to ~1,010,000 via YaRN and is trained with multi-token prediction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93e7479a-0952-470e-a969-c63fa34adbae",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "36a01882-2c33-4b15-bca0-cb86766b0e0e",
  "toolUseResult": {
    "query": "Qwen 3.6 27B model architecture DeltaNet hybrid GatedDeltaNet attention 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MwyJZe7t6zbrKzgAv9s9Ec",
        "content": [
          {
            "title": "Qwen3.6-27B: 27B Model Beats 397B on Coding (2026)",
            "url": "https://www.buildfastwithai.com/blogs/qwen3-6-27b-review-2026"
          },
          {
            "title": "Qwen3.6-27B Explained: Agentic Coding, Hybrid Architecture, Benchmarks & API on Qubrid AI - Qubrid AI",
            "url": "https://www.qubrid.com/blog/qwen36-27b-explained-agentic-coding-hybrid-architecture-benchmarks-api-on-qubrid-ai"
          },
          {
            "title": "Qwen3.6–27B Is Here: A Practical Open-Weight Model for Agentic Coding | by Cristian Marcu | Apr, 2026 | Medium",
            "url": "https://medium.com/@cristian-marcu/qwen3-6-27b-is-here-a-practical-open-weight-model-for-agentic-coding-433be43df637"
          },
          {
            "title": "Qwen3.6-27B Benchmarks, Pricing & Context Window",
            "url": "https://llm-stats.com/models/qwen3.6-27b"
          },
          {
            "title": "Qwen3.6-27B is here. How to use Qwen3.6–27B for free? | by Mehul Gupta | Data Science in Your Pocket | Apr, 2026 | Medium",
            "url": "https://medium.com/data-science-in-your-pocket/qwen3-27b-is-here-197fb2256b97"
          },
          {
            "title": "An Overnight Stack for Qwen3.6–27B: 85 TPS, 125K Context, Vision — on One RTX 3090 | Medium",
            "url": "https://medium.com/@fzbcwvv/an-overnight-stack-for-qwen3-6-27b-85-tps-125k-context-vision-on-one-rtx-3090-0d95c6291914"
          },
          {
            "title": "Alibaba Qwen Team Releases Qwen3.6-27B: A Dense Open-Weight Model Outperforming 397B MoE on Agentic Coding Benchmarks - MarkTechPost",
            "url": "https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/"
          },
          {
            "title": "How to Use Qwen3.6-27B: Complete Guide to Alibaba's New Open-Weight Coding Model | Tosea.ai",
            "url": "https://tosea.ai/blog/qwen-3-6-27b-complete-guide"
          }
        ]
      },
      "Based on the search results, here's what I found about the Qwen3.6-27B model architecture:\n\n## Model Release & Overview\n\nQwen3.6-27B is a dense causal language model with an integrated vision encoder, released by Alibaba's Qwen team in April 2026. It was released on April 22, 2026 under the Apache 2.0 license.\n\n## Hybrid Architecture (DeltaNet + Gated Attention)\n\nThe model introduces a hybrid attention mechanism combining Gated DeltaNet linear attention with standard Gated Attention. More specifically, Qwen3.6-27B is organized as 64 layers, structured as 16 repeating blocks, each composed of three Gated DeltaNet sublayers followed by a single Gated Attention sublayer, with feed-forward networks interleaved throughout.\n\n## Technical Details\n\nThe 64-layer language model uses a hybrid layout of 16 repeats of (3 × Gated DeltaNet → FFN, 1 × Gated Attention → FFN) with hidden dim 5120 and FFN intermediate 17408 — Gated DeltaNet has 48/16 heads for V/QK (head dim 128) and Gated Attention has 24/4 heads for Q/KV (head dim 256).\n\n## Design Rationale\n\nThree-quarters of the model's attention budget runs on linear attention; only every fourth sublayer performs full self-attention. Gated DeltaNet, a linear-attention variant, trades a small amount of expressive capacity for O(n) complexity. Full Gated Attention appears only where it earns its keep — roughly once per block — to preserve the long-range precision that linear attention alone cannot.\n\n## Context Window\n\nIt supports a native 262,144-token context extensible to ~1,010,000 via YaRN and is trained with multi-token prediction."
    ],
    "durationSeconds": 12.018735665999964,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "93e7479a-0952-470e-a969-c63fa34adbae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-19T09:41:28.069Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Va5w9KTKzJBcz8dcM22Esi`</summary>

```json
{
  "query": "LLaMA 4 Scout architecture 48 layers 16 experts MoE 109B parameters specifications"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36a01882-2c33-4b15-bca0-cb86766b0e0e",
  "isSidechain": false,
  "requestId": "req_011CbBi23pzZ5NEQiV2gBMFk",
  "type": "assistant",
  "uuid": "e3204496-1dfc-4f50-9aad-b8daea81e3c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CapxWhmeJm9fNmJuCr3BUc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1278,
      "cache_read_input_tokens": 43192,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1278,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 43192,
          "cache_creation_input_tokens": 1278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1278
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-19T09:41:35.225Z_

<details><summary>↩ Tool result · `toolu_01Va5w9KTKzJBcz8dcM22Esi`</summary>

```text
Web search results for query: "LLaMA 4 Scout architecture 48 layers 16 experts MoE 109B parameters specifications"

Links: [{"title":"Llama 4’s Architecture Deconstructed: MoE, iRoPE, and Early Fusion Explained | by Mandeep Singh | Medium","url":"https://medium.com/@mandeep0405/llama-4s-architecture-deconstructed-moe-irope-and-early-fusion-explained-e58eb9403067"},{"title":"llama-4-scout-17b-16e-instruct: Open-Source Powerhouse with MoE, Multimodality & 10M-Token Memory","url":"https://blog.promptlayer.com/llama-4-scout-17b-16e-instruct-open-source-powerhouse-with-moe-multimodality-10m-token-memory/"},{"title":"Llama 4: The Challenges of Creating a Frontier-Level LLM","url":"https://cameronrwolfe.substack.com/p/llama-4"},{"title":"Deep Technical Analysis of Llama 4 Scout, Maverick and Behemoth - Collabnix","url":"https://collabnix.com/deep-technical-analysis-of-llama-4-scout-maverick-and-behemoth/"},{"title":"Llama 4 Scout - GroqDocs","url":"https://console.groq.com/docs/model/meta-llama/llama-4-scout-17b-16e-instruct"},{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"},{"title":"Meta Llama 4 Maverick and Llama 4 Scout now available in watsonx.ai | IBM","url":"https://www.ibm.com/new/announcements/meta-llama-4-maverick-and-llama-4-scout-now-available-in-watsonx-ai"},{"title":"Llama 4: Models, Architecture, Benchmarks & More","url":"https://www.gocodeo.com/post/llama-4-models-architecture-benchmarks-more"},{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"meta-llama/Llama-4-Scout-17B-16E · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E"}]

Based on the search results, here's comprehensive information about the LLaMA 4 Scout architecture:

## Parameter Configuration

LLaMA 4 Scout has 16 experts with 109B total parameters, and only about 17B parameters activate for any given inference, yet the model can tap into the full 109B parameter knowledge base when needed.

## Architecture Details

The transformer stack contains 48 identical transformer blocks. The MoE architecture replaces standard feed-forward networks in all transformer blocks with a gating mechanism that routes tokens to selected experts based on router network decisions.

The model uses 16 experts to efficiently handle both text and image inputs while maintaining high performance across chat, knowledge, and code generation tasks.

## Key Features

- Scout features an auto-regressive language model that uses a mixture-of-experts (MoE) architecture with 17B activated parameters (109B total) and incorporates early fusion for native multimodality

- The model has a 128K token context window and support for 12 languages (Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese)

- Scout was trained on up to 40 trillion tokens on data encompassing 200 languages

This architecture represents Meta's first implementation of mixture-of-experts in the LLaMA series, offering significant efficiency gains compared to traditional dense models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3204496-1dfc-4f50-9aad-b8daea81e3c7",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "2ccede2d-788d-47d1-8533-57afab4fa28f",
  "toolUseResult": {
    "query": "LLaMA 4 Scout architecture 48 layers 16 experts MoE 109B parameters specifications",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Kf8msKRQ9rV1GkSxphy24X",
        "content": [
          {
            "title": "Llama 4’s Architecture Deconstructed: MoE, iRoPE, and Early Fusion Explained | by Mandeep Singh | Medium",
            "url": "https://medium.com/@mandeep0405/llama-4s-architecture-deconstructed-moe-irope-and-early-fusion-explained-e58eb9403067"
          },
          {
            "title": "llama-4-scout-17b-16e-instruct: Open-Source Powerhouse with MoE, Multimodality & 10M-Token Memory",
            "url": "https://blog.promptlayer.com/llama-4-scout-17b-16e-instruct-open-source-powerhouse-with-moe-multimodality-10m-token-memory/"
          },
          {
            "title": "Llama 4: The Challenges of Creating a Frontier-Level LLM",
            "url": "https://cameronrwolfe.substack.com/p/llama-4"
          },
          {
            "title": "Deep Technical Analysis of Llama 4 Scout, Maverick and Behemoth - Collabnix",
            "url": "https://collabnix.com/deep-technical-analysis-of-llama-4-scout-maverick-and-behemoth/"
          },
          {
            "title": "Llama 4 Scout - GroqDocs",
            "url": "https://console.groq.com/docs/model/meta-llama/llama-4-scout-17b-16e-instruct"
          },
          {
            "title": "Welcome Llama 4 Maverick & Scout on Hugging Face",
            "url": "https://huggingface.co/blog/llama4-release"
          },
          {
            "title": "Meta Llama 4 Maverick and Llama 4 Scout now available in watsonx.ai | IBM",
            "url": "https://www.ibm.com/new/announcements/meta-llama-4-maverick-and-llama-4-scout-now-available-in-watsonx-ai"
          },
          {
            "title": "Llama 4: Models, Architecture, Benchmarks & More",
            "url": "https://www.gocodeo.com/post/llama-4-models-architecture-benchmarks-more"
          },
          {
            "title": "The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation",
            "url": "https://ai.meta.com/blog/llama-4-multimodal-intelligence/"
          },
          {
            "title": "meta-llama/Llama-4-Scout-17B-16E · Hugging Face",
            "url": "https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E"
          }
        ]
      },
      "Based on the search results, here's comprehensive information about the LLaMA 4 Scout architecture:\n\n## Parameter Configuration\n\nLLaMA 4 Scout has 16 experts with 109B total parameters, and only about 17B parameters activate for any given inference, yet the model can tap into the full 109B parameter knowledge base when needed.\n\n## Architecture Details\n\nThe transformer stack contains 48 identical transformer blocks. The MoE architecture replaces standard feed-forward networks in all transformer blocks with a gating mechanism that routes tokens to selected experts based on router network decisions.\n\nThe model uses 16 experts to efficiently handle both text and image inputs while maintaining high performance across chat, knowledge, and code generation tasks.\n\n## Key Features\n\n- Scout features an auto-regressive language model that uses a mixture-of-experts (MoE) architecture with 17B activated parameters (109B total) and incorporates early fusion for native multimodality\n\n- The model has a 128K token context window and support for 12 languages (Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese)\n\n- Scout was trained on up to 40 trillion tokens on data encompassing 200 languages\n\nThis architecture represents Meta's first implementation of mixture-of-experts in the LLaMA series, offering significant efficiency gains compared to traditional dense models."
    ],
    "durationSeconds": 7.151465331000043,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e3204496-1dfc-4f50-9aad-b8daea81e3c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 80 · 2026-05-19T09:41:35.228Z_

```json
{
  "parentUuid": "2ccede2d-788d-47d1-8533-57afab4fa28f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7e2c9925-dd30-4828-90f8-8ba13410707c",
  "timestamp": "2026-05-19T09:41:35.228Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 81 · 2026-05-19T09:41:38.032Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MVdsBFGMGbF41wTewjwEho`</summary>

```json
{
  "query": "Aya Expanse 32B architecture specifications layers hidden dimension Cohere multilingual 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e2c9925-dd30-4828-90f8-8ba13410707c",
  "isSidechain": false,
  "requestId": "req_011CbBi2o6174LvaurFiouWp",
  "type": "assistant",
  "uuid": "d9140f85-549f-45bd-99f2-e6dd19edd8ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fijetk9ene6FSbBLVzAqQ3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2455,
      "cache_read_input_tokens": 43192,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 43192,
          "cache_creation_input_tokens": 2455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2455
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Runtime record

_source line 82_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "d9140f85-549f-45bd-99f2-e6dd19edd8ea",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 83_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Tool result

_source line 84 · 2026-05-19T09:41:44.276Z_

<details><summary>↩ Tool result · `toolu_01MVdsBFGMGbF41wTewjwEho`</summary>

```text
Web search results for query: "Aya Expanse 32B architecture specifications layers hidden dimension Cohere multilingual 2025"

Links: [{"title":"Andrewwwwww/aya-expanse-32b · Hugging Face","url":"https://huggingface.co/Andrewwwwww/aya-expanse-32b"},{"title":"CohereLabs/aya-expanse-32b · Hugging Face","url":"https://huggingface.co/CohereLabs/aya-expanse-32b"},{"title":"README.md · CohereLabs/aya-expanse-32b at main","url":"https://huggingface.co/CohereLabs/aya-expanse-32b/blob/main/README.md"},{"title":"aya-expanse-32b | PromptLayer Models","url":"https://www.promptlayer.com/models/aya-expanse-32b/"},{"title":"Aya Expanse 32b GGUF · Models · Dataloop","url":"https://dataloop.ai/library/model/bartowski_aya-expanse-32b-gguf/"},{"title":"Aya Expanse 32b · Models · Dataloop","url":"https://dataloop.ai/library/model/cohereforai_aya-expanse-32b/"},{"title":"aya-expanse:32b/model","url":"https://ollama.com/library/aya-expanse:32b/blobs/818f3b17285b"},{"title":"Aya-Expanse 8B: Scalable Multilingual LLM","url":"https://www.emergentmind.com/topics/aya-expanse-8b-model"},{"title":"aya-expanse:32b","url":"https://ollama.com/library/aya-expanse:32b"}]

Based on the search results, here's what I found about the Aya Expanse 32B architecture specifications:

## Architecture Overview

Aya Expanse 32B is an auto-regressive language model that uses an optimized transformer architecture. Post-training includes supervised finetuning, preference training, and model merging.

## Key Specifications

Based on metadata from the Ollama library, the model has the following technical specifications:

- **Block Count (Layers)**: 40 layers
- **Embedding/Hidden Dimension**: 8192
- **Attention Heads**: 64 attention heads with 8 key-value heads
- **Feed-Forward Inner Dimension**: 24576
- **Context Length**: 128K tokens
- **Layer Norm Epsilon**: 1e-05

## Multilingual Capabilities

The model is particularly optimized for multilinguality and supports the following languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese.

## Developer

Aya-expanse-32b is a large language model developed by CohereForAI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9140f85-549f-45bd-99f2-e6dd19edd8ea",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "37f59656-087d-4160-bd98-c05c437b0837",
  "toolUseResult": {
    "query": "Aya Expanse 32B architecture specifications layers hidden dimension Cohere multilingual 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V2fSwMLGZEBfVkiiWoJ3pX",
        "content": [
          {
            "title": "Andrewwwwww/aya-expanse-32b · Hugging Face",
            "url": "https://huggingface.co/Andrewwwwww/aya-expanse-32b"
          },
          {
            "title": "CohereLabs/aya-expanse-32b · Hugging Face",
            "url": "https://huggingface.co/CohereLabs/aya-expanse-32b"
          },
          {
            "title": "README.md · CohereLabs/aya-expanse-32b at main",
            "url": "https://huggingface.co/CohereLabs/aya-expanse-32b/blob/main/README.md"
          },
          {
            "title": "aya-expanse-32b | PromptLayer Models",
            "url": "https://www.promptlayer.com/models/aya-expanse-32b/"
          },
          {
            "title": "Aya Expanse 32b GGUF · Models · Dataloop",
            "url": "https://dataloop.ai/library/model/bartowski_aya-expanse-32b-gguf/"
          },
          {
            "title": "Aya Expanse 32b · Models · Dataloop",
            "url": "https://dataloop.ai/library/model/cohereforai_aya-expanse-32b/"
          },
          {
            "title": "aya-expanse:32b/model",
            "url": "https://ollama.com/library/aya-expanse:32b/blobs/818f3b17285b"
          },
          {
            "title": "Aya-Expanse 8B: Scalable Multilingual LLM",
            "url": "https://www.emergentmind.com/topics/aya-expanse-8b-model"
          },
          {
            "title": "aya-expanse:32b",
            "url": "https://ollama.com/library/aya-expanse:32b"
          }
        ]
      },
      "Based on the search results, here's what I found about the Aya Expanse 32B architecture specifications:\n\n## Architecture Overview\n\nAya Expanse 32B is an auto-regressive language model that uses an optimized transformer architecture. Post-training includes supervised finetuning, preference training, and model merging.\n\n## Key Specifications\n\nBased on metadata from the Ollama library, the model has the following technical specifications:\n\n- **Block Count (Layers)**: 40 layers\n- **Embedding/Hidden Dimension**: 8192\n- **Attention Heads**: 64 attention heads with 8 key-value heads\n- **Feed-Forward Inner Dimension**: 24576\n- **Context Length**: 128K tokens\n- **Layer Norm Epsilon**: 1e-05\n\n## Multilingual Capabilities\n\nThe model is particularly optimized for multilinguality and supports the following languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese.\n\n## Developer\n\nAya-expanse-32b is a large language model developed by CohereForAI."
    ],
    "durationSeconds": 6.240770689999976,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d9140f85-549f-45bd-99f2-e6dd19edd8ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-19T09:41:48.296Z_

Good - the architecture details check out. Now let me search for the most critical issue: has anyone already published or pre-printed work on cross-lingual calibration direction transfer?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37f59656-087d-4160-bd98-c05c437b0837",
  "isSidechain": false,
  "requestId": "req_011CbBi3TmgHn31CHVP5XrZs",
  "type": "assistant",
  "uuid": "d82e945a-9801-45bf-ae63-3d66c2a64aed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Gf7ykpZnTRkZS6T77FCKs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 45647,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 45647,
          "cache_creation_input_tokens": 853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 853
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-19T09:41:48.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015cetExfunfsKBbu59rEhP3`</summary>

```json
{
  "query": "site:arxiv.org \"calibration direction\" OR \"confidence direction\" cross-lingual transfer multilingual representation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d82e945a-9801-45bf-ae63-3d66c2a64aed",
  "isSidechain": false,
  "requestId": "req_011CbBi3TmgHn31CHVP5XrZs",
  "type": "assistant",
  "uuid": "fcd54924-c133-4233-b5e3-f45d95636a47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Gf7ykpZnTRkZS6T77FCKs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 45647,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 45647,
          "cache_creation_input_tokens": 853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 853
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-19T09:41:55.439Z_

<details><summary>↩ Tool result · `toolu_015cetExfunfsKBbu59rEhP3`</summary>

```text
Web search results for query: "site:arxiv.org "calibration direction" OR "confidence direction" cross-lingual transfer multilingual representation 2026"

Links: [{"title":"[2601.04036] Analyzing and Improving Cross-lingual Knowledge Transfer for Machine Translation","url":"https://arxiv.org/abs/2601.04036"},{"title":"On the Calibration of Multilingual Question Answering LLMs","url":"https://arxiv.org/pdf/2311.08669"},{"title":"Cross-lingual Transfer of Reward Models in Multilingual Alignment","url":"https://arxiv.org/html/2410.18027v1"},{"title":"Continual Learning with Multilingual Foundation Model","url":"https://arxiv.org/html/2605.13415"},{"title":"On the Calibration of Massively Multilingual Language Models","url":"https://arxiv.org/pdf/2210.12265"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Cross-lingual Transfer of Monolingual Models","url":"https://arxiv.org/pdf/2109.07348"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"[2604.20549] Toward Cross-Lingual Quality Classifiers for Multilingual Pretraining Data Selection","url":"https://arxiv.org/abs/2604.20549"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of   Multilingual BERT","url":"https://arxiv.org/pdf/2101.11109"}]

Based on the search results, I found several relevant papers on arXiv related to cross-lingual transfer and multilingual representation, though I should note that the exact terms "calibration direction" or "confidence direction" don't appear prominently in these results. Here are the key findings:

**Most Relevant to Your Query:**

One recent paper (October 2025) discovered that intermediate layers offer more reliable calibration signals than the final layer and introduced novel, training-free calibration methods that leverage intermediate representations to close the cross-lingual calibration gap.

Massively Multilingual Language Models like mBERT, XLMR, mT5 and mBART have been effective at zero-shot cross-lingual transfer, where models fine-tuned on tasks in one language generalize well in unseen languages.

**Other Recent 2026 Research:**

A January 2026 thesis studies cross-lingual knowledge transfer in neural models and analyzes how language similarity influences transfer, how retrieval and auxiliary supervision strengthen low-resource translation, and how fine-tuning introduces trade-offs in large language models.

The search results include papers on multilingual calibration, cross-lingual transfer, and multilingual representation learning, but they don't contain papers with the exact phrase combinations you specified. If you're looking for papers with those specific terms, you may want to check arXiv directly or refine your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcd54924-c133-4233-b5e3-f45d95636a47",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "9e72fb38-99a6-4c97-8cb3-23fd637ae90c",
  "toolUseResult": {
    "query": "site:arxiv.org \"calibration direction\" OR \"confidence direction\" cross-lingual transfer multilingual representation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QEGFsDpgnnCZ1uz4uvJb7x",
        "content": [
          {
            "title": "[2601.04036] Analyzing and Improving Cross-lingual Knowledge Transfer for Machine Translation",
            "url": "https://arxiv.org/abs/2601.04036"
          },
          {
            "title": "On the Calibration of Multilingual Question Answering LLMs",
            "url": "https://arxiv.org/pdf/2311.08669"
          },
          {
            "title": "Cross-lingual Transfer of Reward Models in Multilingual Alignment",
            "url": "https://arxiv.org/html/2410.18027v1"
          },
          {
            "title": "Continual Learning with Multilingual Foundation Model",
            "url": "https://arxiv.org/html/2605.13415"
          },
          {
            "title": "On the Calibration of Massively Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2210.12265"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          },
          {
            "title": "Cross-lingual Transfer of Monolingual Models",
            "url": "https://arxiv.org/pdf/2109.07348"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/html/2510.03136v1"
          },
          {
            "title": "[2604.20549] Toward Cross-Lingual Quality Classifiers for Multilingual Pretraining Data Selection",
            "url": "https://arxiv.org/abs/2604.20549"
          },
          {
            "title": "First Align, then Predict: Understanding the Cross-Lingual Ability of   Multilingual BERT",
            "url": "https://arxiv.org/pdf/2101.11109"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on arXiv related to cross-lingual transfer and multilingual representation, though I should note that the exact terms \"calibration direction\" or \"confidence direction\" don't appear prominently in these results. Here are the key findings:\n\n**Most Relevant to Your Query:**\n\nOne recent paper (October 2025) discovered that intermediate layers offer more reliable calibration signals than the final layer and introduced novel, training-free calibration methods that leverage intermediate representations to close the cross-lingual calibration gap.\n\nMassively Multilingual Language Models like mBERT, XLMR, mT5 and mBART have been effective at zero-shot cross-lingual transfer, where models fine-tuned on tasks in one language generalize well in unseen languages.\n\n**Other Recent 2026 Research:**\n\nA January 2026 thesis studies cross-lingual knowledge transfer in neural models and analyzes how language similarity influences transfer, how retrieval and auxiliary supervision strengthen low-resource translation, and how fine-tuning introduces trade-offs in large language models.\n\nThe search results include papers on multilingual calibration, cross-lingual transfer, and multilingual representation learning, but they don't contain papers with the exact phrase combinations you specified. If you're looking for papers with those specific terms, you may want to check arXiv directly or refine your search query."
    ],
    "durationSeconds": 6.615253276000032,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fcd54924-c133-4233-b5e3-f45d95636a47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-19T09:41:58.627Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JpgiV7apqi62AiYWim2y3M`</summary>

```json
{
  "query": "linear direction uncertainty confidence multilingual transfer representation engineering steering cross-lingual ECE 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e72fb38-99a6-4c97-8cb3-23fd637ae90c",
  "isSidechain": false,
  "requestId": "req_011CbBi4HWKD5MkvXevDs5FJ",
  "type": "assistant",
  "uuid": "1708916e-2532-4b9e-9cea-2c44e4bd1b1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgNk1XKDkGmRDCT96uUuRA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 892,
      "cache_read_input_tokens": 46500,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 46500,
          "cache_creation_input_tokens": 892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 892
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-19T09:42:05.615Z_

<details><summary>↩ Tool result · `toolu_01JpgiV7apqi62AiYWim2y3M`</summary>

```text
Web search results for query: "linear direction uncertainty confidence multilingual transfer representation engineering steering cross-lingual ECE 2026 arXiv"

Links: [{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/pdf/2505.12584"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v2"},{"title":"Boosting Cross-Lingual Transfer via Self-Learning with Uncertainty   Estimation","url":"https://arxiv.org/pdf/2109.00194"},{"title":"[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/abs/2502.15639"},{"title":"Self-learning framework of zero-shot cross-lingual transfer with uncertainty estimation","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12073183"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/html/2502.15639v1"}]

I found several relevant research papers related to your query. Here are the key results:

**Most Relevant Papers:**

1. **"Improving Multilingual Language Models by Aligning Representations through Steering"** (arXiv:2505.12584)
   - Focuses on representation engineering and learning a manifold that maps between English and target languages, then applying it during inference.

2. **"Language Steering for Multilingual In-Context Learning"** (arXiv:2602.02326v2, April 2026)
   - Proposes language steering to bridge cross-lingual gaps by treating language identity as a separable direction in activation space, using language vectors computed as mean activation differences between parallel examples.

3. **"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models"** (arXiv:2502.15639, February 2025)
   - Examines model interventions as a data-efficient alternative to fine-tuning for manipulating model activations, analyzing the effect on cross-lingual representation alignment by identifying neurons to manipulate.

4. **"Boosting Cross-Lingual Transfer via Self-Learning with Uncertainty Estimation"** (arXiv:2109.00194)
   - Addresses cross-lingual transfer by analyzing different types of uncertainty (Language Heteroscedastic/Homoscedastic Uncertainty and Evidential Uncertainty) across 40 languages for NER and NLI tasks.

These papers collectively cover the themes of multilingual model representation steering, cross-lingual transfer, uncertainty estimation, and representation engineering that your query encompasses.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1708916e-2532-4b9e-9cea-2c44e4bd1b1a",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "b697bb08-6527-4933-ad25-1f4a505c6ca9",
  "toolUseResult": {
    "query": "linear direction uncertainty confidence multilingual transfer representation engineering steering cross-lingual ECE 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FjoeeULRg2631Hz7b1H9kM",
        "content": [
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/pdf/2505.12584"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/html/2602.02326v2"
          },
          {
            "title": "Boosting Cross-Lingual Transfer via Self-Learning with Uncertainty   Estimation",
            "url": "https://arxiv.org/pdf/2109.00194"
          },
          {
            "title": "[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models",
            "url": "https://arxiv.org/abs/2502.15639"
          },
          {
            "title": "Self-learning framework of zero-shot cross-lingual transfer with uncertainty estimation",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12073183"
          },
          {
            "title": "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models",
            "url": "https://arxiv.org/html/2502.15639v1"
          }
        ]
      },
      "I found several relevant research papers related to your query. Here are the key results:\n\n**Most Relevant Papers:**\n\n1. **\"Improving Multilingual Language Models by Aligning Representations through Steering\"** (arXiv:2505.12584)\n   - Focuses on representation engineering and learning a manifold that maps between English and target languages, then applying it during inference.\n\n2. **\"Language Steering for Multilingual In-Context Learning\"** (arXiv:2602.02326v2, April 2026)\n   - Proposes language steering to bridge cross-lingual gaps by treating language identity as a separable direction in activation space, using language vectors computed as mean activation differences between parallel examples.\n\n3. **\"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models\"** (arXiv:2502.15639, February 2025)\n   - Examines model interventions as a data-efficient alternative to fine-tuning for manipulating model activations, analyzing the effect on cross-lingual representation alignment by identifying neurons to manipulate.\n\n4. **\"Boosting Cross-Lingual Transfer via Self-Learning with Uncertainty Estimation\"** (arXiv:2109.00194)\n   - Addresses cross-lingual transfer by analyzing different types of uncertainty (Language Heteroscedastic/Homoscedastic Uncertainty and Evidential Uncertainty) across 40 languages for NER and NLI tasks.\n\nThese papers collectively cover the themes of multilingual model representation steering, cross-lingual transfer, uncertainty estimation, and representation engineering that your query encompasses."
    ],
    "durationSeconds": 6.984143482000043,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1708916e-2532-4b9e-9cea-2c44e4bd1b1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-19T09:42:08.274Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S5SsUsNMfQfoWLB7fG7nLw`</summary>

```json
{
  "query": "\"Steering into New Embedding Spaces\" arXiv 2502.15639 cross-lingual alignment model interventions multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b697bb08-6527-4933-ad25-1f4a505c6ca9",
  "isSidechain": false,
  "requestId": "req_011CbBi52yUdUqRLRBDwyTbd",
  "type": "assistant",
  "uuid": "8f75738c-ac7f-4fc0-8c3e-3e12127b2001",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYhU6EihE4nUHAo63V4Lfw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 795,
      "cache_read_input_tokens": 47392,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 795,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 47392,
          "cache_creation_input_tokens": 795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 795
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-19T09:42:17.675Z_

<details><summary>↩ Tool result · `toolu_01S5SsUsNMfQfoWLB7fG7nLw`</summary>

```text
Web search results for query: ""Steering into New Embedding Spaces" arXiv 2502.15639 cross-lingual alignment model interventions multilingual"

Links: [{"title":"[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/abs/2502.15639"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=3800&show=100"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://www.researchgate.net/publication/389274280_Steering_into_New_Embedding_Spaces_Analyzing_Cross-Lingual_Alignment_Induced_by_Model_Interventions_in_Multilingual_Language_Models"},{"title":"Computation and Language Feb 2025","url":"http://www.arxiv.org/list/cs.CL/2025-02?skip=1325&show=25"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=2750&show=100"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment","url":"https://arxiv.org/pdf/2502.15639"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/new-embedding-spaces"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/html/2502.15639v1"},{"title":"LLM-Augmented Semantic Steering of Text Embedding Projection Spaces","url":"https://arxiv.org/html/2605.01957"}]

I found the paper! Here's information about "Steering into New Embedding Spaces" (arXiv 2502.15639):

**Paper Overview:**

The paper is titled "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models" by Anirudh Sundar and 5 other authors.

**Main Research Focus:**

Aligned representations across languages is a desired property in multilingual large language models (mLLMs), as alignment can improve performance in cross-lingual tasks. Typically alignment requires fine-tuning a model, which is computationally expensive, and sizable language data, which often may not be available. A data-efficient alternative to fine-tuning is model interventions -- a method for manipulating model activations to steer generation into the desired direction.

**Research Approach and Findings:**

The authors analyze the effect of a popular intervention (finding experts) on the alignment of cross-lingual representations in mLLMs, identifying the neurons to manipulate for a given language and introspecting the embedding space of mLLMs pre- and post-manipulation. They show that modifying the mLLM's activations changes its embedding space such that cross-lingual alignment is enhanced.

The paper is available on arXiv and is classified under Computation and Language (cs.CL), Artificial Intelligence (cs.AI), and Machine Learning (cs.LG).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f75738c-ac7f-4fc0-8c3e-3e12127b2001",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "50003951-5c3d-4522-9e61-141d29b0b67e",
  "toolUseResult": {
    "query": "\"Steering into New Embedding Spaces\" arXiv 2502.15639 cross-lingual alignment model interventions multilingual",
    "results": [
      {
        "tool_use_id": "srvtoolu_0186aNbCQRCdU7ov1jx2x6ho",
        "content": [
          {
            "title": "[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models",
            "url": "https://arxiv.org/abs/2502.15639"
          },
          {
            "title": "Machine Learning Feb 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-02?skip=3800&show=100"
          },
          {
            "title": "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models",
            "url": "https://www.researchgate.net/publication/389274280_Steering_into_New_Embedding_Spaces_Analyzing_Cross-Lingual_Alignment_Induced_by_Model_Interventions_in_Multilingual_Language_Models"
          },
          {
            "title": "Computation and Language Feb 2025",
            "url": "http://www.arxiv.org/list/cs.CL/2025-02?skip=1325&show=25"
          },
          {
            "title": "Artificial Intelligence Feb 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-02?skip=2750&show=100"
          },
          {
            "title": "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment",
            "url": "https://arxiv.org/pdf/2502.15639"
          },
          {
            "title": "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/new-embedding-spaces"
          },
          {
            "title": "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models",
            "url": "https://arxiv.org/html/2502.15639v1"
          },
          {
            "title": "LLM-Augmented Semantic Steering of Text Embedding Projection Spaces",
            "url": "https://arxiv.org/html/2605.01957"
          }
        ]
      },
      "I found the paper! Here's information about \"Steering into New Embedding Spaces\" (arXiv 2502.15639):\n\n**Paper Overview:**\n\nThe paper is titled \"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models\" by Anirudh Sundar and 5 other authors.\n\n**Main Research Focus:**\n\nAligned representations across languages is a desired property in multilingual large language models (mLLMs), as alignment can improve performance in cross-lingual tasks. Typically alignment requires fine-tuning a model, which is computationally expensive, and sizable language data, which often may not be available. A data-efficient alternative to fine-tuning is model interventions -- a method for manipulating model activations to steer generation into the desired direction.\n\n**Research Approach and Findings:**\n\nThe authors analyze the effect of a popular intervention (finding experts) on the alignment of cross-lingual representations in mLLMs, identifying the neurons to manipulate for a given language and introspecting the embedding space of mLLMs pre- and post-manipulation. They show that modifying the mLLM's activations changes its embedding space such that cross-lingual alignment is enhanced.\n\nThe paper is available on arXiv and is classified under Computation and Language (cs.CL), Artificial Intelligence (cs.AI), and Machine Learning (cs.LG)."
    ],
    "durationSeconds": 9.396727878000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8f75738c-ac7f-4fc0-8c3e-3e12127b2001",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-19T09:42:20.770Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HqFfkgC69xbnbWCJBqX6Nm`</summary>

```json
{
  "query": "Pokharel \"Cross-Lingual Activation Steering\" arXiv 2601.16390 \"functional divergence\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50003951-5c3d-4522-9e61-141d29b0b67e",
  "isSidechain": false,
  "requestId": "req_011CbBi5vZYm7K1u86w3i8ga",
  "type": "assistant",
  "uuid": "c6f6c830-9ff3-43d0-8214-189979b7ec95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mCquX5G8UezDvMmqGSWkQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 959,
      "cache_read_input_tokens": 48187,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 48187,
          "cache_creation_input_tokens": 959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-19T09:42:26.542Z_

<details><summary>↩ Tool result · `toolu_01HqFfkgC69xbnbWCJBqX6Nm`</summary>

```text
Web search results for query: "Pokharel "Cross-Lingual Activation Steering" arXiv 2601.16390 "functional divergence""

Links: [{"title":"[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/abs/2601.16390"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v1"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/pdf/2502.15639"},{"title":"Enhancing Cross-task Transfer of Large Language Models via Activation Steering","url":"https://arxiv.org/pdf/2507.13236"},{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://arxiv.org/pdf/2510.26024"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"}]

Based on the search results, I found the paper you're looking for. Here's the relevant information:

Cross-Lingual Activation Steering (CLAS) is a training-free inference-time intervention that selectively modulates neuron activations. The paper was authored by Rhitabrat Pokharel, Ameeta Agrawal, and Tanay Nagar, and was submitted to arXiv on January 23, 2026.

Regarding the specific concept of "functional divergence" that you mentioned: The researchers discovered that effective transfer operates through functional divergence rather than strict alignment; performance gains correlate with increased language cluster separation. Their comprehensive analysis of cross-lingual representations found that effective transfer is driven by functional divergence rather than proximity to the anchor language.

The method achieved average improvements of 2.3% (Acc.) and 3.4% (F1) respectively on classification and generation benchmarks, while maintaining high-resource language performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6f6c830-9ff3-43d0-8214-189979b7ec95",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "354a80ac-72b8-4adc-a2d0-8b8e50f87f76",
  "toolUseResult": {
    "query": "Pokharel \"Cross-Lingual Activation Steering\" arXiv 2601.16390 \"functional divergence\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Qoww5QP8fycv6Cetd3UwQ7",
        "content": [
          {
            "title": "[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models",
            "url": "https://arxiv.org/abs/2601.16390"
          },
          {
            "title": "Cross-Lingual Activation Steering for Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2601.16390"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/html/2602.02326v1"
          },
          {
            "title": "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2502.15639"
          },
          {
            "title": "Enhancing Cross-task Transfer of Large Language Models via Activation Steering",
            "url": "https://arxiv.org/pdf/2507.13236"
          },
          {
            "title": "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs",
            "url": "https://arxiv.org/pdf/2510.26024"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/pdf/2602.02326"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's the relevant information:\n\nCross-Lingual Activation Steering (CLAS) is a training-free inference-time intervention that selectively modulates neuron activations. The paper was authored by Rhitabrat Pokharel, Ameeta Agrawal, and Tanay Nagar, and was submitted to arXiv on January 23, 2026.\n\nRegarding the specific concept of \"functional divergence\" that you mentioned: The researchers discovered that effective transfer operates through functional divergence rather than strict alignment; performance gains correlate with increased language cluster separation. Their comprehensive analysis of cross-lingual representations found that effective transfer is driven by functional divergence rather than proximity to the anchor language.\n\nThe method achieved average improvements of 2.3% (Acc.) and 3.4% (F1) respectively on classification and generation benchmarks, while maintaining high-resource language performance."
    ],
    "durationSeconds": 5.767101863000018,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c6f6c830-9ff3-43d0-8214-189979b7ec95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 94_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "354a80ac-72b8-4adc-a2d0-8b8e50f87f76",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 95_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Tool call

_source line 96 · 2026-05-19T09:42:29.569Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UejfyD7Kv2Z5n4DkdV1TyB`</summary>

```json
{
  "query": "Gupta et al. \"Investigating Multilingual Calibration Effects Language Model Instruction-Tuning\" arXiv 2601.01362 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "354a80ac-72b8-4adc-a2d0-8b8e50f87f76",
  "isSidechain": false,
  "requestId": "req_011CbBi6aTqwAU5F8NzfVMDk",
  "type": "assistant",
  "uuid": "3ebcaeec-676a-4be9-b11a-15205dfce069",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHwaZiRjf3UEuh8DDFuwGz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 653,
      "cache_read_input_tokens": 49146,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 653,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 49146,
          "cache_creation_input_tokens": 653,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 653
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-19T09:42:37.788Z_

<details><summary>↩ Tool result · `toolu_01UejfyD7Kv2Z5n4DkdV1TyB`</summary>

```text
Web search results for query: "Gupta et al. "Investigating Multilingual Calibration Effects Language Model Instruction-Tuning" arXiv 2601.01362 2026"

Links: [{"title":"[2601.01362] Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/abs/2601.01362"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/pdf/2601.01362"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/html/2601.01362"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/pdf/2401.01854"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"}]

I found the paper you're looking for! Here are the details:

**Title:** Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning

**Authors:** Jerry Huang, Peng Lu, Qiuhao Zeng, Yusuke Iwasawa, Yutaka Matsuo, Sarath Chandar, Edison Marrese-Taylor, and Irene Li

**arXiv ID:** 2601.01362

**Publication Date:** January 4, 2026

**Summary:** The work examines calibration gaps in large language models within multilingual settings and reveals that even in low-resource languages, model confidence can increase significantly after instruction-tuning on high-resource language SFT datasets. However, improvements in accuracy are marginal or non-existent, resulting in mis-calibration. The researchers observe that label smoothing is a reasonable method to alleviate this concern while maintaining better calibration across all languages.

You can access the paper directly at: https://arxiv.org/abs/2601.01362


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ebcaeec-676a-4be9-b11a-15205dfce069",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "572eda37-020b-4095-abe8-27fa67488e39",
  "toolUseResult": {
    "query": "Gupta et al. \"Investigating Multilingual Calibration Effects Language Model Instruction-Tuning\" arXiv 2601.01362 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FwKXzhQDa6WKS6sGhoFfJE",
        "content": [
          {
            "title": "[2601.01362] Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning",
            "url": "https://arxiv.org/abs/2601.01362"
          },
          {
            "title": "Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning",
            "url": "https://arxiv.org/pdf/2601.01362"
          },
          {
            "title": "Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning",
            "url": "https://arxiv.org/html/2601.01362"
          },
          {
            "title": "Multilingual Instruction Tuning With Just a Pinch of Multilinguality",
            "url": "https://arxiv.org/pdf/2401.01854"
          },
          {
            "title": "Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?",
            "url": "https://arxiv.org/html/2402.13703v3"
          }
        ]
      },
      "I found the paper you're looking for! Here are the details:\n\n**Title:** Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning\n\n**Authors:** Jerry Huang, Peng Lu, Qiuhao Zeng, Yusuke Iwasawa, Yutaka Matsuo, Sarath Chandar, Edison Marrese-Taylor, and Irene Li\n\n**arXiv ID:** 2601.01362\n\n**Publication Date:** January 4, 2026\n\n**Summary:** The work examines calibration gaps in large language models within multilingual settings and reveals that even in low-resource languages, model confidence can increase significantly after instruction-tuning on high-resource language SFT datasets. However, improvements in accuracy are marginal or non-existent, resulting in mis-calibration. The researchers observe that label smoothing is a reasonable method to alleviate this concern while maintaining better calibration across all languages.\n\nYou can access the paper directly at: https://arxiv.org/abs/2601.01362"
    ],
    "durationSeconds": 8.21534291299997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3ebcaeec-676a-4be9-b11a-15205dfce069",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 98 · 2026-05-19T09:42:40.858Z_

Now let me check for very recent work (March-May 2026) that might have scooped this idea:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "572eda37-020b-4095-abe8-27fa67488e39",
  "isSidechain": false,
  "requestId": "req_011CbBi7QdXgwhNTQNtAaN8y",
  "type": "assistant",
  "uuid": "51d4079a-73e3-4a47-8e89-cc66272b997f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019AUbzdo4LsLXPcuEAK18Q1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 49799,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 49799,
          "cache_creation_input_tokens": 627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 627
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-19T09:42:41.331Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QgCkAL5MEvbAQPAsVcN46F`</summary>

```json
{
  "query": "site:arxiv.org multilingual calibration representation engineering steering direction transfer 2026 March April May"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51d4079a-73e3-4a47-8e89-cc66272b997f",
  "isSidechain": false,
  "requestId": "req_011CbBi7QdXgwhNTQNtAaN8y",
  "type": "assistant",
  "uuid": "5cb62d35-e04e-4f98-a427-f515fa2e3137",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019AUbzdo4LsLXPcuEAK18Q1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 49799,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 49799,
          "cache_creation_input_tokens": 627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 627
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-19T09:42:48.338Z_

<details><summary>↩ Tool result · `toolu_01QgCkAL5MEvbAQPAsVcN46F`</summary>

```text
Web search results for query: "site:arxiv.org multilingual calibration representation engineering steering direction transfer 2026 March April May"

Links: [{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/pdf/2505.12584"},{"title":"Language steering in latent space to mitigate unintended code-switching","url":"https://arxiv.org/pdf/2510.13849"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/html/2505.12584v1"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"}]

I've found several relevant papers on arXiv related to multilingual calibration, representation engineering, and steering direction transfer from March-May 2026. Here are the key results:

1. **"Improving Multilingual Language Models by Aligning Representations through Steering"** (arxiv.org/pdf/2505.12584)
   - Investigates how large language models process non-English tokens within their layer representations using representation steering

2. **"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models"** (arxiv.org/pdf/2510.03136)
   - Presents the first systematic evaluation of multilingual calibration across high-quality, human-curated datasets spanning over 100 languages and covering six prominent LLM families

3. **"Cross-Lingual Activation Steering for Multilingual Language Models"** (arxiv.org/pdf/2601.16390)
   - Discovers that effective transfer operates through functional divergence rather than strict alignment, and demonstrates that targeted activation steering can unlock latent multilingual capacity in existing models without modification to model weights

4. **"Language Steering for Multilingual In-Context Learning"** (arxiv.org/pdf/2602.02326)
   - Discusses how mean activation differences between contrastive inputs encode interpretable directions in representation space and have been applied to address language confusion in multilingual models

5. **"Language steering in latent space to mitigate unintended code-switching"** (arxiv.org/pdf/2510.13849)
   - Introduces representation engineering using PCA on contrastive prompt pairs to identify concept directions and steer activations


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cb62d35-e04e-4f98-a427-f515fa2e3137",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "c6998fdd-f17e-4fcb-b6d4-96c2592a4a9b",
  "toolUseResult": {
    "query": "site:arxiv.org multilingual calibration representation engineering steering direction transfer 2026 March April May",
    "results": [
      {
        "tool_use_id": "srvtoolu_014oskL7RBM1Tcvzteo4Aa1J",
        "content": [
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/pdf/2505.12584"
          },
          {
            "title": "Language steering in latent space to mitigate unintended code-switching",
            "url": "https://arxiv.org/pdf/2510.13849"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          },
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/html/2505.12584v1"
          },
          {
            "title": "Cross-Lingual Activation Steering for Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2601.16390"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/pdf/2602.02326"
          }
        ]
      },
      "I've found several relevant papers on arXiv related to multilingual calibration, representation engineering, and steering direction transfer from March-May 2026. Here are the key results:\n\n1. **\"Improving Multilingual Language Models by Aligning Representations through Steering\"** (arxiv.org/pdf/2505.12584)\n   - Investigates how large language models process non-English tokens within their layer representations using representation steering\n\n2. **\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models\"** (arxiv.org/pdf/2510.03136)\n   - Presents the first systematic evaluation of multilingual calibration across high-quality, human-curated datasets spanning over 100 languages and covering six prominent LLM families\n\n3. **\"Cross-Lingual Activation Steering for Multilingual Language Models\"** (arxiv.org/pdf/2601.16390)\n   - Discovers that effective transfer operates through functional divergence rather than strict alignment, and demonstrates that targeted activation steering can unlock latent multilingual capacity in existing models without modification to model weights\n\n4. **\"Language Steering for Multilingual In-Context Learning\"** (arxiv.org/pdf/2602.02326)\n   - Discusses how mean activation differences between contrastive inputs encode interpretable directions in representation space and have been applied to address language confusion in multilingual models\n\n5. **\"Language steering in latent space to mitigate unintended code-switching\"** (arxiv.org/pdf/2510.13849)\n   - Introduces representation engineering using PCA on contrastive prompt pairs to identify concept directions and steer activations"
    ],
    "durationSeconds": 7.002029056,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5cb62d35-e04e-4f98-a427-f515fa2e3137",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-19T09:42:51.187Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QCiWdjSZN7sGZg57sqAsgT`</summary>

```json
{
  "query": "arXiv \"confidence geometry\" OR \"calibration geometry\" OR \"uncertainty geometry\" cross-lingual multilingual LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6998fdd-f17e-4fcb-b6d4-96c2592a4a9b",
  "isSidechain": false,
  "requestId": "req_011CbBi8C8it2FyRWyQar2Uv",
  "type": "assistant",
  "uuid": "deaed966-8572-4562-8aa7-199fd8b3f516",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCEcTGy1t3vMXAegLH4RXQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 50426,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 50426,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 770
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-19T09:43:00.563Z_

<details><summary>↩ Tool result · `toolu_01QCiWdjSZN7sGZg57sqAsgT`</summary>

```text
Web search results for query: "arXiv "confidence geometry" OR "calibration geometry" OR "uncertainty geometry" cross-lingual multilingual LLM 2026"

Links: [{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"On the Calibration of Multilingual Question Answering LLMs","url":"https://arxiv.org/pdf/2311.08669"},{"title":"[2605.03299] LLM-XTM: Enhancing Cross-Lingual Topic Models with Large Language Models","url":"https://arxiv.org/abs/2605.03299"},{"title":"Multicalibration for Confidence Scoring in LLMs","url":"https://arxiv.org/pdf/2404.04689"},{"title":"MKA: Leveraging Cross-Lingual Consensus for Model Abstention","url":"https://arxiv.org/pdf/2503.23687"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/pdf/2601.01362"}]

Based on the search results, I found several highly relevant arXiv papers related to calibration and uncertainty in multilingual LLMs from recent periods:

## Key Findings:

**Most Relevant Papers:**

1. "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models" (October 2025) - introduces novel, training-free calibration methods that leverage intermediate representations to close the cross-lingual calibration gap.

2. "MKA: Leveraging Cross-Lingual Consensus for Model Abstention" (2025) - focuses on utilizing the multilingual knowledge of an LLM to calibrate the model's confidence and let it abstain when uncertain.

3. "Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning" (2026) - examines how the relationship between large language models and calibration remains an open area of research, specifically addressing calibration within multilingual settings.

4. "On the Calibration of Multilingual Question Answering LLMs" - demonstrates that despite high zero-shot cross-lingual accuracy, zero-shot cross-lingual calibration is not good for LLMs unless dedicated calibration strategies are used.

5. "Multicalibration for Confidence Scoring in LLMs" - explores uncertainty quantification and confidence scoring approaches to reduce hallucination generation.

These papers directly address the intersection of calibration/uncertainty estimation, multilingual/cross-lingual settings, and LLMs, which aligns closely with your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "deaed966-8572-4562-8aa7-199fd8b3f516",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "b1730955-5a0c-436c-8e48-a78e246613f0",
  "toolUseResult": {
    "query": "arXiv \"confidence geometry\" OR \"calibration geometry\" OR \"uncertainty geometry\" cross-lingual multilingual LLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q521ZNYmtz2GWX6CDbnyDC",
        "content": [
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/html/2510.03136v1"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          },
          {
            "title": "On the Calibration of Multilingual Question Answering LLMs",
            "url": "https://arxiv.org/pdf/2311.08669"
          },
          {
            "title": "[2605.03299] LLM-XTM: Enhancing Cross-Lingual Topic Models with Large Language Models",
            "url": "https://arxiv.org/abs/2605.03299"
          },
          {
            "title": "Multicalibration for Confidence Scoring in LLMs",
            "url": "https://arxiv.org/pdf/2404.04689"
          },
          {
            "title": "MKA: Leveraging Cross-Lingual Consensus for Model Abstention",
            "url": "https://arxiv.org/pdf/2503.23687"
          },
          {
            "title": "Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning",
            "url": "https://arxiv.org/pdf/2601.01362"
          }
        ]
      },
      "Based on the search results, I found several highly relevant arXiv papers related to calibration and uncertainty in multilingual LLMs from recent periods:\n\n## Key Findings:\n\n**Most Relevant Papers:**\n\n1. \"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models\" (October 2025) - introduces novel, training-free calibration methods that leverage intermediate representations to close the cross-lingual calibration gap.\n\n2. \"MKA: Leveraging Cross-Lingual Consensus for Model Abstention\" (2025) - focuses on utilizing the multilingual knowledge of an LLM to calibrate the model's confidence and let it abstain when uncertain.\n\n3. \"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning\" (2026) - examines how the relationship between large language models and calibration remains an open area of research, specifically addressing calibration within multilingual settings.\n\n4. \"On the Calibration of Multilingual Question Answering LLMs\" - demonstrates that despite high zero-shot cross-lingual accuracy, zero-shot cross-lingual calibration is not good for LLMs unless dedicated calibration strategies are used.\n\n5. \"Multicalibration for Confidence Scoring in LLMs\" - explores uncertainty quantification and confidence scoring approaches to reduce hallucination generation.\n\nThese papers directly address the intersection of calibration/uncertainty estimation, multilingual/cross-lingual settings, and LLMs, which aligns closely with your search query."
    ],
    "durationSeconds": 9.370582580999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "deaed966-8572-4562-8aa7-199fd8b3f516",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 103 · 2026-05-19T09:43:00.566Z_

```json
{
  "parentUuid": "b1730955-5a0c-436c-8e48-a78e246613f0",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ef58c18d-d3da-43e6-9b4d-229ce0989571",
  "timestamp": "2026-05-19T09:43:00.566Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 104 · 2026-05-19T09:43:04.532Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018grGSWFKoZL3qqVk6cb7f9`</summary>

```json
{
  "query": "AEON-7 abliteration Qwen3.6-27B DeltaNet residual stream difference-in-means"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef58c18d-d3da-43e6-9b4d-229ce0989571",
  "isSidechain": false,
  "requestId": "req_011CbBi95tD66jrJse1ZnjKZ",
  "type": "assistant",
  "uuid": "763d465e-7b9d-46a1-b136-1c2fad814f53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wr7KfDUxrBYCBpa7WRzf5F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 890,
      "cache_read_input_tokens": 51196,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 890,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 51196,
          "cache_creation_input_tokens": 890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 890
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-19T09:43:11.938Z_

<details><summary>↩ Tool result · `toolu_018grGSWFKoZL3qqVk6cb7f9`</summary>

```text
Web search results for query: "AEON-7 abliteration Qwen3.6-27B DeltaNet residual stream difference-in-means"

Links: [{"title":"AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored · Hugging Face","url":"https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored"},{"title":"AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16 · Hugging Face","url":"https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16"},{"title":"GitHub - AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash: Lossless abliteration of Qwen3.6-27B with NVFP4 hardware quantization for DGX Spark / Blackwell. BF16 (51 GB) + NVFP4 (26 GB) deployment guide, docker-compose, and QuickStart. · GitHub","url":"https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash"},{"title":"Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash/README.md at main · AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash","url":"https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash/blob/main/README.md"},{"title":"AEON-7/Qwen3.6-35B-A3B-heretic-NVFP4 · Hugging Face","url":"https://huggingface.co/AEON-7/Qwen3.6-35B-A3B-heretic-NVFP4"},{"title":"AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-Multimodal-NVFP4-MTP-XS · Hugging Face","url":"https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-Multimodal-NVFP4-MTP-XS"},{"title":"AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-Multimodal-NVFP4-MTP · Hugging Face","url":"https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-Multimodal-NVFP4-MTP"},{"title":"AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-NVFP4 · Hugging Face","url":"https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-NVFP4"},{"title":"wangzhang/Qwen3.6-27B-abliterated · Hugging Face","url":"https://huggingface.co/wangzhang/Qwen3.6-27B-abliterated"}]

Based on the search results, I found relevant information about AEON-7's abliteration of the Qwen 3.6-27B model. Here's what the search reveals:

## Key Technical Details

The abliteration ablates the orthogonal component of the refusal direction relative to the harmless-prompt mean — the helpfulness-aligned signal is preserved, and outlier residual vectors are clipped before projection.

The pipeline integrates Arditi-style mean-difference refusal vectors, grimjim's norm-preserving biprojected abliteration (NPBA), projected abliteration with outlier-aware winsorization, and other methodologies.

## GatedDeltaNet and Residual Stream

Regarding the DeltaNet components specifically, certain late SSM / GatedDeltaNet blocks in Qwen3.5 / 3.6 hybrids have linear_attn.conv1d.weight σ inflated 50–100% above the median across all SSM blocks. GDN linear-attention is preserved BF16 for best long-context fidelity.

## Difference-in-Means Approach

Remaining refusals live in residual-stream directions that are orthogonal to the first pass's primary refusal direction, which relates to the difference-in-means methodology used to identify and target specific refusal vectors in the model's residual stream.

The AEON-7 abliteration represents a sophisticated application of residual stream intervention techniques targeting Qwen 3.6's hybrid architecture.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "763d465e-7b9d-46a1-b136-1c2fad814f53",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "ca60f03d-84ff-4cc0-8275-639f1d5c8c99",
  "toolUseResult": {
    "query": "AEON-7 abliteration Qwen3.6-27B DeltaNet residual stream difference-in-means",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C8YMvJD8EjFmXsFwbVJfpZ",
        "content": [
          {
            "title": "AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored · Hugging Face",
            "url": "https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored"
          },
          {
            "title": "AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16 · Hugging Face",
            "url": "https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16"
          },
          {
            "title": "GitHub - AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash: Lossless abliteration of Qwen3.6-27B with NVFP4 hardware quantization for DGX Spark / Blackwell. BF16 (51 GB) + NVFP4 (26 GB) deployment guide, docker-compose, and QuickStart. · GitHub",
            "url": "https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash"
          },
          {
            "title": "Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash/README.md at main · AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash",
            "url": "https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash/blob/main/README.md"
          },
          {
            "title": "AEON-7/Qwen3.6-35B-A3B-heretic-NVFP4 · Hugging Face",
            "url": "https://huggingface.co/AEON-7/Qwen3.6-35B-A3B-heretic-NVFP4"
          },
          {
            "title": "AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-Multimodal-NVFP4-MTP-XS · Hugging Face",
            "url": "https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-Multimodal-NVFP4-MTP-XS"
          },
          {
            "title": "AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-Multimodal-NVFP4-MTP · Hugging Face",
            "url": "https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-Multimodal-NVFP4-MTP"
          },
          {
            "title": "AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-NVFP4 · Hugging Face",
            "url": "https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-NVFP4"
          },
          {
            "title": "wangzhang/Qwen3.6-27B-abliterated · Hugging Face",
            "url": "https://huggingface.co/wangzhang/Qwen3.6-27B-abliterated"
          }
        ]
      },
      "Based on the search results, I found relevant information about AEON-7's abliteration of the Qwen 3.6-27B model. Here's what the search reveals:\n\n## Key Technical Details\n\nThe abliteration ablates the orthogonal component of the refusal direction relative to the harmless-prompt mean — the helpfulness-aligned signal is preserved, and outlier residual vectors are clipped before projection.\n\nThe pipeline integrates Arditi-style mean-difference refusal vectors, grimjim's norm-preserving biprojected abliteration (NPBA), projected abliteration with outlier-aware winsorization, and other methodologies.\n\n## GatedDeltaNet and Residual Stream\n\nRegarding the DeltaNet components specifically, certain late SSM / GatedDeltaNet blocks in Qwen3.5 / 3.6 hybrids have linear_attn.conv1d.weight σ inflated 50–100% above the median across all SSM blocks. GDN linear-attention is preserved BF16 for best long-context fidelity.\n\n## Difference-in-Means Approach\n\nRemaining refusals live in residual-stream directions that are orthogonal to the first pass's primary refusal direction, which relates to the difference-in-means methodology used to identify and target specific refusal vectors in the model's residual stream.\n\nThe AEON-7 abliteration represents a sophisticated application of residual stream intervention techniques targeting Qwen 3.6's hybrid architecture."
    ],
    "durationSeconds": 7.401381840999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "763d465e-7b9d-46a1-b136-1c2fad814f53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-19T09:43:15.493Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SUymJV2nBJ5Kp6XssuqnLq`</summary>

```json
{
  "query": "Civelli Bernardelle Brunello Demartini \"shared geometry difficulty multilingual\" arXiv 2601.12731"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca60f03d-84ff-4cc0-8275-639f1d5c8c99",
  "isSidechain": false,
  "requestId": "req_011CbBi9vZA8hVjjUd3FxUb3",
  "type": "assistant",
  "uuid": "0337e695-f968-40a6-a8c6-028407bf147b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M7vMvya2UQucpqR35KnKBE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1352,
      "cache_read_input_tokens": 52086,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1352,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 52086,
          "cache_creation_input_tokens": 1352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1352
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-19T09:43:22.335Z_

<details><summary>↩ Tool result · `toolu_01SUymJV2nBJ5Kp6XssuqnLq`</summary>

```text
Web search results for query: "Civelli Bernardelle Brunello Demartini "shared geometry difficulty multilingual" arXiv 2601.12731"

Links: [{"title":"[2601.12731] A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/abs/2601.12731"},{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/html/2601.12731"},{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/pdf/2601.12731"},{"title":"Gianluca Demartini - Publication List","url":"https://www.gianlucademartini.net/"},{"title":"[2412.14843] Mapping and Influencing the Political Ideology of Large Language Models using Synthetic Personas","url":"https://arxiv.org/abs/2412.14843"}]

I found the paper! Here are the key details:

**Title:** A Shared Geometry of Difficulty in Multilingual Language Models

**Authors:** Stefano Civelli, Pietro Bernardelle, Nicolò Brunello, Gianluca Demartini

**Affiliations:** The University of Queensland and Polytechnic University of Milan

**Summary:** The work studies the multilingual geometry of problem-difficulty in LLMs by training linear probes using the AMC subset of the Easy2Hard benchmark, translated into 21 languages. Difficulty-related signals emerge at two distinct stages of the model internals (shallow early-layers and deep later-layers) that exhibit functionally different behaviors. Probes trained on deep representations achieve high accuracy within the same language but poor cross-lingual generalization, while probes trained on shallow representations generalize substantially better across languages despite lower within-language performance.

The paper was submitted to arXiv on January 19, 2026, with ID 2601.12731, and is scheduled to be presented as a short paper at the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026) in San Diego, California, July 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0337e695-f968-40a6-a8c6-028407bf147b",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "8b7415f5-41ff-46ba-b01e-2fdf04fc62f9",
  "toolUseResult": {
    "query": "Civelli Bernardelle Brunello Demartini \"shared geometry difficulty multilingual\" arXiv 2601.12731",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UUUphvjGNH48TzXc6K9mRU",
        "content": [
          {
            "title": "[2601.12731] A Shared Geometry of Difficulty in Multilingual Language Models",
            "url": "https://arxiv.org/abs/2601.12731"
          },
          {
            "title": "A Shared Geometry of Difficulty in Multilingual Language Models",
            "url": "https://arxiv.org/html/2601.12731"
          },
          {
            "title": "A Shared Geometry of Difficulty in Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2601.12731"
          },
          {
            "title": "Gianluca Demartini - Publication List",
            "url": "https://www.gianlucademartini.net/"
          },
          {
            "title": "[2412.14843] Mapping and Influencing the Political Ideology of Large Language Models using Synthetic Personas",
            "url": "https://arxiv.org/abs/2412.14843"
          }
        ]
      },
      "I found the paper! Here are the key details:\n\n**Title:** A Shared Geometry of Difficulty in Multilingual Language Models\n\n**Authors:** Stefano Civelli, Pietro Bernardelle, Nicolò Brunello, Gianluca Demartini\n\n**Affiliations:** The University of Queensland and Polytechnic University of Milan\n\n**Summary:** The work studies the multilingual geometry of problem-difficulty in LLMs by training linear probes using the AMC subset of the Easy2Hard benchmark, translated into 21 languages. Difficulty-related signals emerge at two distinct stages of the model internals (shallow early-layers and deep later-layers) that exhibit functionally different behaviors. Probes trained on deep representations achieve high accuracy within the same language but poor cross-lingual generalization, while probes trained on shallow representations generalize substantially better across languages despite lower within-language performance.\n\nThe paper was submitted to arXiv on January 19, 2026, with ID 2601.12731, and is scheduled to be presented as a short paper at the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026) in San Diego, California, July 2026."
    ],
    "durationSeconds": 6.837168170999968,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0337e695-f968-40a6-a8c6-028407bf147b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 108_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "8b7415f5-41ff-46ba-b01e-2fdf04fc62f9",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 109_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Tool call

_source line 110 · 2026-05-19T09:43:25.851Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019oqpDs95eV6eDDu1fDLBCY`</summary>

```json
{
  "query": "Sun Chaudhari Barnett Dobriban \"confidence interval l2 expected calibration error\" arXiv 2408.08998"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b7415f5-41ff-46ba-b01e-2fdf04fc62f9",
  "isSidechain": false,
  "requestId": "req_011CbBiAgz7XYm9SpScbYzj2",
  "type": "assistant",
  "uuid": "19a25af1-871b-4910-9d44-a4d7f881700f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUYLEo2Sixr5Wb5QmdMygV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 53438,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 53438,
          "cache_creation_input_tokens": 613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 613
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-19T09:43:30.223Z_

<details><summary>↩ Tool result · `toolu_019oqpDs95eV6eDDu1fDLBCY`</summary>

```text
Web search results for query: "Sun Chaudhari Barnett Dobriban "confidence interval l2 expected calibration error" arXiv 2408.08998"

Links: [{"title":"[2408.08998] A Confidence Interval for the $\\ell_2$ Expected Calibration Error","url":"https://arxiv.org/abs/2408.08998"},{"title":"(PDF) A Confidence Interval for the $\\ell_2$ Expected Calibration Error","url":"https://www.researchgate.net/publication/383236449_A_Confidence_Interval_for_the_ell_2_Expected_Calibration_Error"},{"title":"Machine Learning Aug 2024","url":"https://arxiv.org/list/stat.ML/2024-08?skip=45&show=25"},{"title":"dblp: Edgar Dobriban","url":"https://dblp.org/pid/99/11269.html"},{"title":"A Confidence Interval for the l2 Expected Calibration Error","url":"https://arxiv.org/pdf/2408.08998"},{"title":"A Confidence Interval for the ℓ₂ Expected Calibration Error","url":"https://arxiv.org/html/2408.08998"},{"title":"A Confidence Interval for the $\\ell_2$ Expected Calibration ...","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2408.08998"},{"title":"[2109.03480] Estimating Expected Calibration Errors","url":"https://ar5iv.labs.arxiv.org/html/2109.03480"}]

I found the paper you're searching for! The paper "A Confidence Interval for the ℓ₂ Expected Calibration Error" is authored by Yan Sun, Pratik Chaudhari, Ian J. Barnett, and Edgar Dobriban.

The work develops confidence intervals for the ℓ₂ Expected Calibration Error (ECE), considering top-1-to-k calibration, which includes both confidence calibration as well as full calibration. For a debiased estimator of the ECE, the authors show asymptotic normality, but with different convergence rates and asymptotic variances for calibrated and miscalibrated models.

The paper is available on arXiv (arXiv:2408.08998) and has been categorized under Machine Learning (stat.ML) and Machine Learning (cs.LG).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19a25af1-871b-4910-9d44-a4d7f881700f",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "3f28b578-1a06-4671-b125-f3dfc120c6fc",
  "toolUseResult": {
    "query": "Sun Chaudhari Barnett Dobriban \"confidence interval l2 expected calibration error\" arXiv 2408.08998",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AX5KQVJQRezLGfaTQspJ4X",
        "content": [
          {
            "title": "[2408.08998] A Confidence Interval for the $\\ell_2$ Expected Calibration Error",
            "url": "https://arxiv.org/abs/2408.08998"
          },
          {
            "title": "(PDF) A Confidence Interval for the $\\ell_2$ Expected Calibration Error",
            "url": "https://www.researchgate.net/publication/383236449_A_Confidence_Interval_for_the_ell_2_Expected_Calibration_Error"
          },
          {
            "title": "Machine Learning Aug 2024",
            "url": "https://arxiv.org/list/stat.ML/2024-08?skip=45&show=25"
          },
          {
            "title": "dblp: Edgar Dobriban",
            "url": "https://dblp.org/pid/99/11269.html"
          },
          {
            "title": "A Confidence Interval for the l2 Expected Calibration Error",
            "url": "https://arxiv.org/pdf/2408.08998"
          },
          {
            "title": "A Confidence Interval for the ℓ₂ Expected Calibration Error",
            "url": "https://arxiv.org/html/2408.08998"
          },
          {
            "title": "A Confidence Interval for the $\\ell_2$ Expected Calibration ...",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2408.08998"
          },
          {
            "title": "[2109.03480] Estimating Expected Calibration Errors",
            "url": "https://ar5iv.labs.arxiv.org/html/2109.03480"
          }
        ]
      },
      "I found the paper you're searching for! The paper \"A Confidence Interval for the ℓ₂ Expected Calibration Error\" is authored by Yan Sun, Pratik Chaudhari, Ian J. Barnett, and Edgar Dobriban.\n\nThe work develops confidence intervals for the ℓ₂ Expected Calibration Error (ECE), considering top-1-to-k calibration, which includes both confidence calibration as well as full calibration. For a debiased estimator of the ECE, the authors show asymptotic normality, but with different convergence rates and asymptotic variances for calibrated and miscalibrated models.\n\nThe paper is available on arXiv (arXiv:2408.08998) and has been categorized under Machine Learning (stat.ML) and Machine Learning (cs.LG)."
    ],
    "durationSeconds": 4.369571296999988,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "19a25af1-871b-4910-9d44-a4d7f881700f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 112 · 2026-05-19T09:43:39.761Z_

Now let me check for very recent work (March-May 2026) that could specifically scoop the exact idea of transferring calibration directions cross-lingually:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f28b578-1a06-4671-b125-f3dfc120c6fc",
  "isSidechain": false,
  "requestId": "req_011CbBiBGm7eFoarxNvxNnq4",
  "type": "assistant",
  "uuid": "ff80aeb7-e979-4597-9ba3-79e9aaa3de9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nYuemZv77pjW8LUDtDoYx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 54051,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 54051,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 710
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-19T09:43:40.885Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014V1deBh4sYeBKy9WjEnEMq`</summary>

```json
{
  "query": "\"calibration\" \"steering vector\" OR \"activation steering\" OR \"representation engineering\" multilingual transfer arXiv March April May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff80aeb7-e979-4597-9ba3-79e9aaa3de9a",
  "isSidechain": false,
  "requestId": "req_011CbBiBGm7eFoarxNvxNnq4",
  "type": "assistant",
  "uuid": "c21a2bee-26a6-4318-87d5-e7f88fc57783",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nYuemZv77pjW8LUDtDoYx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 54051,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 54051,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 710
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-19T09:43:49.327Z_

<details><summary>↩ Tool result · `toolu_014V1deBh4sYeBKy9WjEnEMq`</summary>

```text
Web search results for query: ""calibration" "steering vector" OR "activation steering" OR "representation engineering" multilingual transfer arXiv March April May 2026"

Links: [{"title":"[2602.02326] Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/abs/2602.02326"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v2"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/pdf/2505.12584"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/html/2505.12584v1"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"},{"title":"STEERING LANGUAGE MODELS WITH ACTIVATION EN- GINEERING Alexander Matt Turner","url":"https://arxiv.org/pdf/2308.10248"},{"title":"Activation Addition: Steering Language Models Without Optimization","url":"https://arxiv.org/html/2308.10248v4"}]

Based on the search results, I found several relevant papers on steering vectors, activation steering, and representation engineering for multilingual transfer from arXiv in the March-May 2026 timeframe:

## Key Papers Found:

1. **Language Steering for Multilingual In-Context Learning** (February 2026, updated April 2026)
   - Proposes language vectors -- a training-free language steering approach that leverages activation differences between source and target languages to guide model behavior
   - The method steers model generations by adding vectors to intermediate model activations during inference to make the model's internal representations shift towards the target language space without any parameter updates
   - The steering vectors reveal meaningful linguistic structure aligned with language families and successfully transfer across tasks, demonstrating that these representations are task-agnostic

2. **Cross-Lingual Activation Steering for Multilingual Language Models** (January 2026)
   - Introduces Cross-Lingual Activation Steering (CLAS), a test-time neuron-level method that rebalances shared and language-specific representations during inference by boosting neurons that encode cross-lingual structure and suppressing those that overspecialize to a single language, improving performance on non-dominant languages without requiring additional data or parameter updates

3. **Improving Multilingual Language Models by Aligning Representations through Steering** (May 2026)
   - The approach learns a manifold that maps between English and target languages, then applies it during inference instead of fine-tuning
   - Representation Engineering has been used to enhance model alignment and detect vulnerabilities


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c21a2bee-26a6-4318-87d5-e7f88fc57783",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "679e3068-5034-4055-bc98-a74ae5cfac95",
  "toolUseResult": {
    "query": "\"calibration\" \"steering vector\" OR \"activation steering\" OR \"representation engineering\" multilingual transfer arXiv March April May 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J7qxjVXkFAg5SLW2bWeVZC",
        "content": [
          {
            "title": "[2602.02326] Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/abs/2602.02326"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/html/2602.02326v2"
          },
          {
            "title": "Cross-Lingual Activation Steering for Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2601.16390"
          },
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/pdf/2505.12584"
          },
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/html/2505.12584v1"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/pdf/2602.02326"
          },
          {
            "title": "STEERING LANGUAGE MODELS WITH ACTIVATION EN- GINEERING Alexander Matt Turner",
            "url": "https://arxiv.org/pdf/2308.10248"
          },
          {
            "title": "Activation Addition: Steering Language Models Without Optimization",
            "url": "https://arxiv.org/html/2308.10248v4"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on steering vectors, activation steering, and representation engineering for multilingual transfer from arXiv in the March-May 2026 timeframe:\n\n## Key Papers Found:\n\n1. **Language Steering for Multilingual In-Context Learning** (February 2026, updated April 2026)\n   - Proposes language vectors -- a training-free language steering approach that leverages activation differences between source and target languages to guide model behavior\n   - The method steers model generations by adding vectors to intermediate model activations during inference to make the model's internal representations shift towards the target language space without any parameter updates\n   - The steering vectors reveal meaningful linguistic structure aligned with language families and successfully transfer across tasks, demonstrating that these representations are task-agnostic\n\n2. **Cross-Lingual Activation Steering for Multilingual Language Models** (January 2026)\n   - Introduces Cross-Lingual Activation Steering (CLAS), a test-time neuron-level method that rebalances shared and language-specific representations during inference by boosting neurons that encode cross-lingual structure and suppressing those that overspecialize to a single language, improving performance on non-dominant languages without requiring additional data or parameter updates\n\n3. **Improving Multilingual Language Models by Aligning Representations through Steering** (May 2026)\n   - The approach learns a manifold that maps between English and target languages, then applies it during inference instead of fine-tuning\n   - Representation Engineering has been used to enhance model alignment and detect vulnerabilities"
    ],
    "durationSeconds": 8.439537185000022,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c21a2bee-26a6-4318-87d5-e7f88fc57783",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-19T09:43:53.288Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NKuDRPmQAM7h5w5PFsb6Q5`</summary>

```json
{
  "query": "Kirtane Huang \"Language Steering for Multilingual In-Context Learning\" arXiv 2602.02326 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "679e3068-5034-4055-bc98-a74ae5cfac95",
  "isSidechain": false,
  "requestId": "req_011CbBiCgMxnBqjLq3zZHHV5",
  "type": "assistant",
  "uuid": "320d0bc8-561a-4015-8355-196c42dc93a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmJBqqb8p3o8XPPcCRFY5Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 54761,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 831,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 54761,
          "cache_creation_input_tokens": 831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 831
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-19T09:43:59.555Z_

<details><summary>↩ Tool result · `toolu_01NKuDRPmQAM7h5w5PFsb6Q5`</summary>

```text
Web search results for query: "Kirtane Huang "Language Steering for Multilingual In-Context Learning" arXiv 2602.02326 2026"

Links: [{"title":"[2602.02326] Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/abs/2602.02326"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/pdf/2505.12584"},{"title":"Language steering in latent space to mitigate unintended code-switching","url":"https://arxiv.org/pdf/2510.13849"},{"title":"[2505.12584] Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/abs/2505.12584"},{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature Steering","url":"https://arxiv.org/pdf/2507.13410"},{"title":"[2510.13849] Language steering in latent space to mitigate unintended code-switching","url":"https://arxiv.org/abs/2510.13849"},{"title":"The Impact of Demonstrations on Multilingual In-Context Learning: A   Multidimensional Analysis","url":"https://arxiv.org/pdf/2402.12976"},{"title":"Blessing of Multilinguality: A Systematic Analysis of Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2502.11364"}]

Based on the search results, here's what I found about the paper:

The paper "Language Steering for Multilingual In-Context Learning" (arXiv:2602.02326) was authored by Neeraja Kirtane and Kuan-Hao Huang and was submitted on February 2, 2026.

The paper addresses the problem that while multilingual large language models have become widely adopted, their performance on non-English languages remains substantially inferior to English, and this disparity is particularly evident in in-context learning scenarios where providing demonstrations in English but testing on non-English inputs leads to significant performance degradation.

The authors hypothesize that LLMs develop a universal semantic space for understanding languages, where different languages are encoded as distinct directions within this space. Based on this hypothesis, they propose language vectors -- a training-free language steering approach that leverages activation differences between source and target languages to guide model behavior, by adding the vector to intermediate model activations during inference to make the model's internal representations shift towards the target language space without any parameter updates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "320d0bc8-561a-4015-8355-196c42dc93a2",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "b6df81dc-26bb-4145-8cf5-d1a5b1eab145",
  "toolUseResult": {
    "query": "Kirtane Huang \"Language Steering for Multilingual In-Context Learning\" arXiv 2602.02326 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01STbznuYeXWpf73bDsCdr4d",
        "content": [
          {
            "title": "[2602.02326] Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/abs/2602.02326"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/pdf/2602.02326"
          },
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/pdf/2505.12584"
          },
          {
            "title": "Language steering in latent space to mitigate unintended code-switching",
            "url": "https://arxiv.org/pdf/2510.13849"
          },
          {
            "title": "[2505.12584] Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/abs/2505.12584"
          },
          {
            "title": "Causal Language Control in Multilingual Transformers via Sparse Feature Steering",
            "url": "https://arxiv.org/pdf/2507.13410"
          },
          {
            "title": "[2510.13849] Language steering in latent space to mitigate unintended code-switching",
            "url": "https://arxiv.org/abs/2510.13849"
          },
          {
            "title": "The Impact of Demonstrations on Multilingual In-Context Learning: A   Multidimensional Analysis",
            "url": "https://arxiv.org/pdf/2402.12976"
          },
          {
            "title": "Blessing of Multilinguality: A Systematic Analysis of Multilingual In-Context Learning",
            "url": "https://arxiv.org/pdf/2502.11364"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\nThe paper \"Language Steering for Multilingual In-Context Learning\" (arXiv:2602.02326) was authored by Neeraja Kirtane and Kuan-Hao Huang and was submitted on February 2, 2026.\n\nThe paper addresses the problem that while multilingual large language models have become widely adopted, their performance on non-English languages remains substantially inferior to English, and this disparity is particularly evident in in-context learning scenarios where providing demonstrations in English but testing on non-English inputs leads to significant performance degradation.\n\nThe authors hypothesize that LLMs develop a universal semantic space for understanding languages, where different languages are encoded as distinct directions within this space. Based on this hypothesis, they propose language vectors -- a training-free language steering approach that leverages activation differences between source and target languages to guide model behavior, by adding the vector to intermediate model activations during inference to make the model's internal representations shift towards the target language space without any parameter updates."
    ],
    "durationSeconds": 6.2586554280000275,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "320d0bc8-561a-4015-8355-196c42dc93a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-19T09:44:02.473Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ne78zRYepEvUg9gCbSeuEB`</summary>

```json
{
  "query": "URIEL+ typological features cross-lingual distance syntactic phonological genetic 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6df81dc-26bb-4145-8cf5-d1a5b1eab145",
  "isSidechain": false,
  "requestId": "req_011CbBiDS9E56RArNV4feyhH",
  "type": "assistant",
  "uuid": "2e74aec9-e9e1-441a-b444-bb73e8d3a140",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015U2KfGb45HcN5Fcmig6QwH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 55592,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 55592,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-19T09:44:10.540Z_

<details><summary>↩ Tool result · `toolu_01Ne78zRYepEvUg9gCbSeuEB`</summary>

```text
Web search results for query: "URIEL+ typological features cross-lingual distance syntactic phonological genetic 2025 2026"

Links: [{"title":"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base","url":"https://arxiv.org/html/2409.18472v3"},{"title":"urielplus · PyPI","url":"https://pypi.org/project/urielplus/"},{"title":"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/html/2510.19217"},{"title":"[2510.19217] Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/abs/2510.19217"},{"title":"arXiv:2409.18472v3 [cs.CL] 14 Feb 2025","url":"https://arxiv.org/pdf/2409.18472"},{"title":"Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages for Cross-Lingual POS Tagging","url":"https://arxiv.org/html/2503.19979v1"},{"title":"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/pdf/2510.19217"}]

Based on the search results, I found highly relevant and recent information about URIEL+ and its typological features:

## URIEL+ Overview

URIEL aggregates linguistic data from multiple sources to provide a standardized, all-in-one measure of language distance by incorporating linguistic domains as feature categories within typological vectors.

## Distance Types

URIEL+ measures linguistic distance across three modalities: geographic (locations of languages), genetic (linguistic family trees), and typological (linguistic features unique to each language).

## Typological Features

The typological domain includes several specific feature types:

- Syntactic distance measures similarities and differences in grammatical structures using frameworks such as dependency trees and part-of-speech distributions, providing quantitative comparisons of syntactic patterns between languages.

- Linguists measure typological distance by focusing on particular linguistic domains including syntax, phonology, and phonemic inventory.

## Recent Developments

An example of URIEL distances shows that English and French are geographically identical, moderately distant typologically (syntactic, phonological, inventory), and genetically distant.

Additionally, recent work has introduced a framework for type-matched language distances, proposing novel, structure-aware representations for each distance type: speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, and a latent variables model for typology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e74aec9-e9e1-441a-b444-bb73e8d3a140",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "f116ad5d-5ef4-427f-8ef1-515436dc6310",
  "toolUseResult": {
    "query": "URIEL+ typological features cross-lingual distance syntactic phonological genetic 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FuFtyXe5dqZ9eFMhKNKYuS",
        "content": [
          {
            "title": "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base",
            "url": "https://arxiv.org/html/2409.18472v3"
          },
          {
            "title": "urielplus · PyPI",
            "url": "https://pypi.org/project/urielplus/"
          },
          {
            "title": "Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+",
            "url": "https://arxiv.org/html/2510.19217"
          },
          {
            "title": "[2510.19217] Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+",
            "url": "https://arxiv.org/abs/2510.19217"
          },
          {
            "title": "arXiv:2409.18472v3 [cs.CL] 14 Feb 2025",
            "url": "https://arxiv.org/pdf/2409.18472"
          },
          {
            "title": "Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages for Cross-Lingual POS Tagging",
            "url": "https://arxiv.org/html/2503.19979v1"
          },
          {
            "title": "Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+",
            "url": "https://arxiv.org/pdf/2510.19217"
          }
        ]
      },
      "Based on the search results, I found highly relevant and recent information about URIEL+ and its typological features:\n\n## URIEL+ Overview\n\nURIEL aggregates linguistic data from multiple sources to provide a standardized, all-in-one measure of language distance by incorporating linguistic domains as feature categories within typological vectors.\n\n## Distance Types\n\nURIEL+ measures linguistic distance across three modalities: geographic (locations of languages), genetic (linguistic family trees), and typological (linguistic features unique to each language).\n\n## Typological Features\n\nThe typological domain includes several specific feature types:\n\n- Syntactic distance measures similarities and differences in grammatical structures using frameworks such as dependency trees and part-of-speech distributions, providing quantitative comparisons of syntactic patterns between languages.\n\n- Linguists measure typological distance by focusing on particular linguistic domains including syntax, phonology, and phonemic inventory.\n\n## Recent Developments\n\nAn example of URIEL distances shows that English and French are geographically identical, moderately distant typologically (syntactic, phonological, inventory), and genetically distant.\n\nAdditionally, recent work has introduced a framework for type-matched language distances, proposing novel, structure-aware representations for each distance type: speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, and a latent variables model for typology."
    ],
    "durationSeconds": 8.063572523999959,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2e74aec9-e9e1-441a-b444-bb73e8d3a140",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 119 · 2026-05-19T09:44:14.240Z_

Let me now look deeper at the CORAL paper to check if it's a significant overlooked competitor, and also search for any other very recent work that could threaten novelty:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f116ad5d-5ef4-427f-8ef1-515436dc6310",
  "isSidechain": false,
  "requestId": "req_011CbBiEF7ySm4EerYioCJNn",
  "type": "assistant",
  "uuid": "69565691-53fe-481a-95e1-b7c62df1667c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtuenVienRPb9fMSZAsVzT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 759,
      "cache_read_input_tokens": 56338,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 56338,
          "cache_creation_input_tokens": 759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 759
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-19T09:44:16.377Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012ewpucj4EQ5KyjMExN65sg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.06022",
  "prompt": "Read this paper carefully. Does CORAL do any multilingual or cross-lingual evaluation? Does it transfer calibration across languages? What languages are tested? What models are used? What layer does the probe operate on? Does it use difference-in-means or probe-based extraction? How is it different from transferring a calibration direction cross-lingually?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69565691-53fe-481a-95e1-b7c62df1667c",
  "isSidechain": false,
  "requestId": "req_011CbBiEF7ySm4EerYioCJNn",
  "type": "assistant",
  "uuid": "f0b3efa7-e986-4756-82bd-02b582da686b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtuenVienRPb9fMSZAsVzT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 759,
      "cache_read_input_tokens": 56338,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 56338,
          "cache_creation_input_tokens": 759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 759
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 121_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "f0b3efa7-e986-4756-82bd-02b582da686b",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 122_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Tool result

_source line 123 · 2026-05-19T09:44:21.329Z_

<details><summary>↩ Tool result · `toolu_012ewpucj4EQ5KyjMExN65sg`</summary>

```text
# CORAL Paper Analysis

Based on the webpage content provided, I cannot answer most of your specific technical questions because the abstract does not contain those details.

## What the abstract reveals:

The paper does **not** mention multilingual or cross-lingual evaluation. There is no discussion of language transfer or calibration across languages.

The abstract states the method was evaluated on "three 7B-parameter models" and demonstrates transfer to "four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA)," but does not specify which models or whether they tested multiple languages.

## What cannot be determined from this page:

The following technical details are absent from the visible abstract:
- Specific layer where the probe operates
- Whether it uses difference-in-means or probe-based extraction
- How it compares to cross-lingual calibration direction transfer
- Which specific model architectures were tested

The abstract only states that CORAL uses "weight-decay MLP probes" to "capture distributed correctness signals from model internal activations," but layer specifications and methodological comparisons would require reading the full paper itself.

To answer your detailed technical questions accurately, you would need to access the complete PDF or HTML version of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0b3efa7-e986-4756-82bd-02b582da686b",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "457a8f17-e5bb-45e3-8a8f-3596b14cc2e5",
  "toolUseResult": {
    "bytes": 47094,
    "code": 200,
    "codeText": "OK",
    "result": "# CORAL Paper Analysis\n\nBased on the webpage content provided, I cannot answer most of your specific technical questions because the abstract does not contain those details.\n\n## What the abstract reveals:\n\nThe paper does **not** mention multilingual or cross-lingual evaluation. There is no discussion of language transfer or calibration across languages.\n\nThe abstract states the method was evaluated on \"three 7B-parameter models\" and demonstrates transfer to \"four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA),\" but does not specify which models or whether they tested multiple languages.\n\n## What cannot be determined from this page:\n\nThe following technical details are absent from the visible abstract:\n- Specific layer where the probe operates\n- Whether it uses difference-in-means or probe-based extraction\n- How it compares to cross-lingual calibration direction transfer\n- Which specific model architectures were tested\n\nThe abstract only states that CORAL uses \"weight-decay MLP probes\" to \"capture distributed correctness signals from model internal activations,\" but layer specifications and methodological comparisons would require reading the full paper itself.\n\nTo answer your detailed technical questions accurately, you would need to access the complete PDF or HTML version of the paper.",
    "durationMs": 4950,
    "url": "https://arxiv.org/abs/2602.06022"
  },
  "sourceToolAssistantUUID": "f0b3efa7-e986-4756-82bd-02b582da686b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-19T09:44:26.706Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CFncaJHHabX2ys9sZTxLGd`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.06022v1",
  "prompt": "Read this paper. Key questions: (1) Is there ANY multilingual or cross-lingual evaluation? (2) What specific layers does the probe operate on? (3) Is the probe language-specific or language-agnostic? (4) What's the relation to calibration direction transfer? (5) What models are tested? (6) How is the direction/probe extracted - via difference-in-means or supervised training?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "457a8f17-e5bb-45e3-8a8f-3596b14cc2e5",
  "isSidechain": false,
  "requestId": "req_011CbBiF3Hrca1T47va9YhvK",
  "type": "assistant",
  "uuid": "67396e01-d9b9-4366-9769-f665c85e2dff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHfgbkzMvV6dkQFQQ9wxij",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 478,
      "cache_read_input_tokens": 57097,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 478,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 57097,
          "cache_creation_input_tokens": 478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 478
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-19T09:44:33.723Z_

<details><summary>↩ Tool result · `toolu_01CFncaJHHabX2ys9sZTxLGd`</summary>

```text
# CORAL Paper Analysis: Key Findings

## (1) Multilingual or Cross-Lingual Evaluation
**No multilingual evaluation exists.** The paper exclusively evaluates on English-language benchmarks (MMLU, RACE, CommonsenseQA, ARC-Challenge, HellaSwag, OpenBookQA, Math-MC). The limitations section acknowledges this constraint: "CORAL's evaluation is limited to multiple-choice question answering, leaving open whether correctness signals generalize to free-form generation."

## (2) Specific Layers for Probe Operation
The probe operates on **middle transformer layers**, specifically layers 17–21 for DeepSeek-7B-Chat. Figure 2 shows "layers 17–21 yield the strongest improvements in both accuracy and calibration," with early layers (0–6) producing below-baseline performance and final layers showing marginal decline.

## (3) Language-Specific vs. Language-Agnostic
**Not addressed.** The paper provides no discussion of language specificity. Given training exclusively on English datasets and testing on English benchmarks only, the probe's cross-lingual properties remain unexplored.

## (4) Relation to Calibration Direction Transfer
The paper demonstrates **empirical transferability across tasks** but doesn't theoretically explain why. The discussion notes: "Strong transfer across four complete independent benchmark test sets suggests that CORAL captures task-general correctness representations rather than dataset-specific patterns."

## (5) Models Tested
Three 7B-parameter models:
- Mistral-7B-Instruct-v0.3
- Qwen2.5-7B-Instruct
- Deepseek-7B-Chat

## (6) Direction/Probe Extraction Method
**Supervised training via MLP probe.** The approach uses "a four-hidden-layer MLP with weight-decay regularization" trained via "AdamW with weight decay," not difference-in-means contrasts. This supervised aggregation distinguishes CORAL from sparse autoencoder approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67396e01-d9b9-4366-9769-f665c85e2dff",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "4122f096-3437-4e9c-8bae-40bfa79e68d7",
  "toolUseResult": {
    "bytes": 462666,
    "code": 200,
    "codeText": "OK",
    "result": "# CORAL Paper Analysis: Key Findings\n\n## (1) Multilingual or Cross-Lingual Evaluation\n**No multilingual evaluation exists.** The paper exclusively evaluates on English-language benchmarks (MMLU, RACE, CommonsenseQA, ARC-Challenge, HellaSwag, OpenBookQA, Math-MC). The limitations section acknowledges this constraint: \"CORAL's evaluation is limited to multiple-choice question answering, leaving open whether correctness signals generalize to free-form generation.\"\n\n## (2) Specific Layers for Probe Operation\nThe probe operates on **middle transformer layers**, specifically layers 17–21 for DeepSeek-7B-Chat. Figure 2 shows \"layers 17–21 yield the strongest improvements in both accuracy and calibration,\" with early layers (0–6) producing below-baseline performance and final layers showing marginal decline.\n\n## (3) Language-Specific vs. Language-Agnostic\n**Not addressed.** The paper provides no discussion of language specificity. Given training exclusively on English datasets and testing on English benchmarks only, the probe's cross-lingual properties remain unexplored.\n\n## (4) Relation to Calibration Direction Transfer\nThe paper demonstrates **empirical transferability across tasks** but doesn't theoretically explain why. The discussion notes: \"Strong transfer across four complete independent benchmark test sets suggests that CORAL captures task-general correctness representations rather than dataset-specific patterns.\"\n\n## (5) Models Tested\nThree 7B-parameter models:\n- Mistral-7B-Instruct-v0.3\n- Qwen2.5-7B-Instruct\n- Deepseek-7B-Chat\n\n## (6) Direction/Probe Extraction Method\n**Supervised training via MLP probe.** The approach uses \"a four-hidden-layer MLP with weight-decay regularization\" trained via \"AdamW with weight decay,\" not difference-in-means contrasts. This supervised aggregation distinguishes CORAL from sparse autoencoder approaches.",
    "durationMs": 7014,
    "url": "https://arxiv.org/html/2602.06022v1"
  },
  "sourceToolAssistantUUID": "67396e01-d9b9-4366-9769-f665c85e2dff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 126 · 2026-05-19T09:44:33.732Z_

```json
{
  "parentUuid": "4122f096-3437-4e9c-8bae-40bfa79e68d7",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ed49a60a-5aa8-4518-ace2-bcf26744f29c",
  "timestamp": "2026-05-19T09:44:33.732Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 127 · 2026-05-19T09:44:40.409Z_

<details><summary>Logged reasoning block</summary>

```text
Good - CORAL is English-only and uses supervised MLP probes (not difference-in-means), so it's related but distinct. It should be cited in the landscape but doesn't scoop the idea.

Let me now check some more details about the idea's feasibility and look for any other missed work.

Key things I still need to verify:
1. Is the Belebele dataset actually providing 900 samples per language?
2. The resource estimates - are they realistic?
3. Any more recent work in April/May 2026 that could be competing?
4. The Khanmohammadi CCPS paper - does it exist and is it English-only?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed49a60a-5aa8-4518-ace2-bcf26744f29c",
  "isSidechain": false,
  "requestId": "req_011CbBiFxGGbBHMAfbEpv6Ta",
  "type": "assistant",
  "uuid": "fa85d68b-26cf-4204-a002-fde91166aa63",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTBrS86bkfv7zUaVvDjouR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 57575,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 57575,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-19T09:44:40.969Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XHQ2vvPrDLgMZcdwSnZZsv`</summary>

```json
{
  "query": "Belebele benchmark number of samples per language 122 languages multilingual evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa85d68b-26cf-4204-a002-fde91166aa63",
  "isSidechain": false,
  "requestId": "req_011CbBiFxGGbBHMAfbEpv6Ta",
  "type": "assistant",
  "uuid": "c792755a-ffb2-40ee-bc3e-56a66232c305",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTBrS86bkfv7zUaVvDjouR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 57575,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 57575,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-19T09:44:46.149Z_

<details><summary>↩ Tool result · `toolu_01XHQ2vvPrDLgMZcdwSnZZsv`</summary>

```text
Web search results for query: "Belebele benchmark number of samples per language 122 languages multilingual evaluation"

Links: [{"title":"The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants | Request PDF","url":"https://www.researchgate.net/publication/384198848_The_Belebele_Benchmark_a_Parallel_Reading_Comprehension_Dataset_in_122_Language_Variants"},{"title":"Meta Releases BELEBELE, A Multilingual AI Benchmark Spanning 122 Languages","url":"https://www.maginative.com/article/meta-releases-belebele-a-multilingual-ai-benchmark-spanning-122-languages/"},{"title":"The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants","url":"https://arxiv.org/html/2308.16884v2"},{"title":"The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122   Language Variants","url":"https://arxiv.org/pdf/2308.16884"},{"title":"Evaluating Language Competence of Llama 2-based models: Belebele Benchmark | by Geronimo | Medium","url":"https://medium.com/@geronimo7/evaluating-language-competence-of-llama-2-based-models-belebele-benchmark-91d4bbd250df"},{"title":"The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.44/"},{"title":"The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants - Paper Detail","url":"https://deeplearn.org/arxiv/408125/the-belebele-benchmark:-a-parallel-reading-comprehension-dataset-in-122-language-variants"},{"title":"[2308.16884] The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants","url":"https://arxiv.org/abs/2308.16884"},{"title":"The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants | Research - AI at Meta","url":"https://ai.meta.com/research/publications/the-belebele-benchmark-a-parallel-reading-comprehension-dataset-in-122-language-variants/"}]

Based on the search results, I can provide you with information about the Belebele benchmark:

The Belebele dataset contains 900 unique multiple-choice reading comprehension passages and questions. Since the benchmark spans 122 diverse languages, this means there are approximately 7-8 samples (questions) per language on average across the entire benchmark.

Each question is based on a short passage from the FLoRES-200 dataset and has four multiple-choice answers. The Belebele dataset was created completely without machine translation, relying solely on human experts fluent in both English and each target language.

BELEBELE represents the largest parallel multilingual benchmark ever created specifically for reading comprehension. The benchmark enables the evaluation of text models in high-, medium-, and low-resource languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c792755a-ffb2-40ee-bc3e-56a66232c305",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "f0305b7b-0ef3-4a2a-9511-6c649c9260d0",
  "toolUseResult": {
    "query": "Belebele benchmark number of samples per language 122 languages multilingual evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Set6BM977EkX89Vm3paEKZ",
        "content": [
          {
            "title": "The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants | Request PDF",
            "url": "https://www.researchgate.net/publication/384198848_The_Belebele_Benchmark_a_Parallel_Reading_Comprehension_Dataset_in_122_Language_Variants"
          },
          {
            "title": "Meta Releases BELEBELE, A Multilingual AI Benchmark Spanning 122 Languages",
            "url": "https://www.maginative.com/article/meta-releases-belebele-a-multilingual-ai-benchmark-spanning-122-languages/"
          },
          {
            "title": "The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants",
            "url": "https://arxiv.org/html/2308.16884v2"
          },
          {
            "title": "The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122   Language Variants",
            "url": "https://arxiv.org/pdf/2308.16884"
          },
          {
            "title": "Evaluating Language Competence of Llama 2-based models: Belebele Benchmark | by Geronimo | Medium",
            "url": "https://medium.com/@geronimo7/evaluating-language-competence-of-llama-2-based-models-belebele-benchmark-91d4bbd250df"
          },
          {
            "title": "The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants - ACL Anthology",
            "url": "https://aclanthology.org/2024.acl-long.44/"
          },
          {
            "title": "The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants - Paper Detail",
            "url": "https://deeplearn.org/arxiv/408125/the-belebele-benchmark:-a-parallel-reading-comprehension-dataset-in-122-language-variants"
          },
          {
            "title": "[2308.16884] The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants",
            "url": "https://arxiv.org/abs/2308.16884"
          },
          {
            "title": "The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants | Research - AI at Meta",
            "url": "https://ai.meta.com/research/publications/the-belebele-benchmark-a-parallel-reading-comprehension-dataset-in-122-language-variants/"
          }
        ]
      },
      "Based on the search results, I can provide you with information about the Belebele benchmark:\n\nThe Belebele dataset contains 900 unique multiple-choice reading comprehension passages and questions. Since the benchmark spans 122 diverse languages, this means there are approximately 7-8 samples (questions) per language on average across the entire benchmark.\n\nEach question is based on a short passage from the FLoRES-200 dataset and has four multiple-choice answers. The Belebele dataset was created completely without machine translation, relying solely on human experts fluent in both English and each target language.\n\nBELEBELE represents the largest parallel multilingual benchmark ever created specifically for reading comprehension. The benchmark enables the evaluation of text models in high-, medium-, and low-resource languages."
    ],
    "durationSeconds": 5.1752173170000315,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c792755a-ffb2-40ee-bc3e-56a66232c305",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 130 · 2026-05-19T09:44:50.990Z_

<details><summary>Logged reasoning block</summary>

```text
Wait, the search result says "900 unique multiple-choice reading comprehension passages and questions" - but that's 900 total per language (since they're parallel), not 900 total across all languages. Let me verify this.

Actually, from the paper description: Belebele has 900 questions per language (the same 900 questions translated into each of the 122 languages). So the idea's claim of ~900 samples per language is correct.

Let me verify this more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0305b7b-0ef3-4a2a-9511-6c649c9260d0",
  "isSidechain": false,
  "requestId": "req_011CbBiGsM7vKPWbzfVJMqVs",
  "type": "assistant",
  "uuid": "c670bcee-8d28-4649-b4d9-b71f402818e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RU55HWHwkM46G3qEMsvc8Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 58322,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1035,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 58322,
          "cache_creation_input_tokens": 1035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1035
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-19T09:44:51.979Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012zUt6FxfREy49kPmXzgsVq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2308.16884",
  "prompt": "How many questions/samples does Belebele have per language? Is it 900 per language (parallel across all 122 languages), or 900 total? What is the exact dataset size?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c670bcee-8d28-4649-b4d9-b71f402818e0",
  "isSidechain": false,
  "requestId": "req_011CbBiGsM7vKPWbzfVJMqVs",
  "type": "assistant",
  "uuid": "a7a6b111-90b7-4691-8d5f-80d747505950",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RU55HWHwkM46G3qEMsvc8Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 58322,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1035,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 58322,
          "cache_creation_input_tokens": 1035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1035
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-19T09:44:53.720Z_

<details><summary>↩ Tool result · `toolu_012zUt6FxfREy49kPmXzgsVq`</summary>

```text
Based on the content provided, the exact dataset size and number of questions per language is not specified. The abstract states the dataset "spans 122 language variants" and mentions "Each question is based on a short passage," but does not provide the specific number of samples per language or in total.

To get this information, you would need to access the full paper PDF or the dataset documentation itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7a6b111-90b7-4691-8d5f-80d747505950",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "acc3320b-9058-450b-a98c-4c9772ece7bc",
  "toolUseResult": {
    "bytes": 50114,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the content provided, the exact dataset size and number of questions per language is not specified. The abstract states the dataset \"spans 122 language variants\" and mentions \"Each question is based on a short passage,\" but does not provide the specific number of samples per language or in total.\n\nTo get this information, you would need to access the full paper PDF or the dataset documentation itself.",
    "durationMs": 1739,
    "url": "https://arxiv.org/abs/2308.16884"
  },
  "sourceToolAssistantUUID": "a7a6b111-90b7-4691-8d5f-80d747505950",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-19T09:44:56.863Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q3FwJowHubZYvpezKX2NTf`</summary>

```json
{
  "url": "https://arxiv.org/html/2308.16884v2",
  "prompt": "How many questions/samples does Belebele have? Is it 900 questions per language (parallel across all 122 language variants)? What is the exact total dataset size?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acc3320b-9058-450b-a98c-4c9772ece7bc",
  "isSidechain": false,
  "requestId": "req_011CbBiHRgZUZ7hRdyJ3mm7M",
  "type": "assistant",
  "uuid": "70227a0c-51a8-4ef4-a368-4aaa8e496456",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186YgwTpVpnm7LSaVMCP1Kx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 59357,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 341,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 59357,
          "cache_creation_input_tokens": 341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 341
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-19T09:45:00.420Z_

<details><summary>↩ Tool result · `toolu_01Q3FwJowHubZYvpezKX2NTf`</summary>

```text
# Belebele Dataset Size

Belebele contains **900 unique questions** that are parallel across all 122 language variants.

According to the document: "The dataset contains 900 unique multiple-choice reading comprehension passages and questions."

## Total Dataset Composition

- **900 distinct questions**
- **488 distinct passages** (most passages have 1-2 associated questions)
- **109,800 total rows** when accounting for all 122 language variants

The dataset is fully parallel, meaning the same 900 questions appear in all 122 languages, allowing for direct performance comparison across languages. Each question has 4 multiple-choice answers with exactly 1 correct answer.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70227a0c-51a8-4ef4-a368-4aaa8e496456",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "341e2cc9-54b8-4117-9f85-244bb5cab394",
  "toolUseResult": {
    "bytes": 452678,
    "code": 200,
    "codeText": "OK",
    "result": "# Belebele Dataset Size\n\nBelebele contains **900 unique questions** that are parallel across all 122 language variants.\n\nAccording to the document: \"The dataset contains 900 unique multiple-choice reading comprehension passages and questions.\"\n\n## Total Dataset Composition\n\n- **900 distinct questions**\n- **488 distinct passages** (most passages have 1-2 associated questions)\n- **109,800 total rows** when accounting for all 122 language variants\n\nThe dataset is fully parallel, meaning the same 900 questions appear in all 122 languages, allowing for direct performance comparison across languages. Each question has 4 multiple-choice answers with exactly 1 correct answer.",
    "durationMs": 3556,
    "url": "https://arxiv.org/html/2308.16884v2"
  },
  "sourceToolAssistantUUID": "70227a0c-51a8-4ef4-a368-4aaa8e496456",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 135 · 2026-05-19T09:46:27.105Z_

<details><summary>Logged reasoning block</summary>

```text
Good - so 900 questions per language, exactly as claimed. That confirms the idea's sample size estimate.

Now let me think about the key issues I want to raise:

1. **CORAL (arXiv 2602.06022)** - This is a calibration-aware inference-time steering method from February 2026 that the idea doesn't cite. While it's English-only and uses supervised MLP probes rather than difference-in-means, it's very relevant to the landscape. It uses middle layers (17-21 in 32-layer models, ~53-66% depth), which is interesting because the proposed idea hypothesizes calibration at ~88-94% depth. 

There's a potential tension here - CORAL probes correctness at middle layers while Zhou et al. and Joshi et al. found calibration signals peaking at late-intermediate depths, so the evidence on where calibration information concentrates isn't entirely settled. That said, CORAL's focus on correctness prediction is somewhat orthogonal to the proposed method's focus on calibration direction at deeper layers.

Now I'm seeing that CORAL uses supervised MLP probes rather than contrastive directions, so it should be cited as related work. The core novelty claim - that no one has transferred calibration directions across languages - seems to hold up based on my search, which is genuinely interesting. The feasibility looks reasonable too with the revised 400-550 H100 hour estimate accounting for 3 models across 122 languages with full layer sweeps, though I'm working through the exact math on forward pass requirements across that many samples. .6-27B (27B params, 2×H100): ~0.5 seconds per sample at BF16 with hidden state extraction → ~55,000 seconds → ~15 hours. But you need all 64 layers, so it's a single pass with caching.
   - For LLaMA 4 Scout (109B total, 4×H100): ~2-3 seconds per sample → ~220,000-330,000 seconds → ~60-90 hours
   - For Aya Expanse 32B (~2×H100): similar to Qwen
   - Then you need to do this for multiple benchmarks too (MMMLU, XQuAD, MLQA)
   - Plus ablations, direction extraction experiments, etc.
   - 400-550 GPU hours seems plausible.

4. **Missing work: CORAL** - This is a moderate issue. The idea should cite CORAL in the landscape.

5. **The "Language Steering for Multilingual In-Context Learning" (Kirtane & Huang, arXiv 2602.02326)** is already cited, and I'm checking whether the Mahmoud et al. cross-family limitation is properly addressed—the paper now frames this around testing whether calibration directions behave more like refusal directions (universal) or task-performance directions (family-limited), which handles it well. For the shallow vs. late-intermediate discrepancy with Civelli et al., the argument is that calibration is a distinct post-hoc phenomenon, separate from their findings.

6. **"Steering into New Embedding Spaces" (arXiv 2502.15639)** from Apple analyzes cross-lingual alignment from model interventions and is relevant but less directly competing with the core idea.

7. **Venue deadlines and timeline**: AAAI 2027 (July 21/28 2026) gives roughly 10 weeks, ARR August gives about 11 weeks, and NAACL 2027 via ARR October gives around 20 weeks—all feasible. Statistical rigor is solid with BCa bootstrap confidence intervals, adaptive binning, and debiased ECE. Author attributions have been corrected from the previous round.

Now I'm assessing whether this clears the pass threshold. The novelty is strong—testing cross-lingual calibration direction transfer is genuinely untested, and the convergence of Ji et al.'s linear steering approach with multilingual calibration is a fresh angle.

The feasibility looks solid too. Models and benchmarks are publicly available, methods are established, and the architecture-specific extraction is now well-specified. The main uncertainty is whether calibration directions actually transfer cross-lingually, but that's framed as informative regardless. The statistical approach is rigorous.

The writeup itself is exceptionally clear, and the layer mapping strategy is carefully thought through.

On impact, if this holds up, it'd be practically useful—122× better data efficiency than LACE is significant—and theoretically interesting for understanding where calibration universality breaks down. The selective prediction application adds real-world value. But the scope is somewhat narrow, and simpler baselines like temperature scaling might already be sufficient for most deployment scenarios.

Let me recalibrate the scores: novelty is 4/5 (genuinely novel combination, though the methodology itself is incremental), feasibility is 4/5 (well-specified and realistic, but the core hypothesis could fail). That puts me in the right range.

Now I'm noticing some gaps in the landscape. CORAL from February 2026 is a calibration-aware inference-time steering method that should be included—it's not a direct competitor since it's English-only with supervised probes, but it's a notable omission. I also need to verify what changed between v1 and v2 of the Mahmoud et al. paper to confirm whether the cross-family limitations are actually from the version being cited.

BaseCal is another relevant method from January 2026 using unsupervised calibration via base model signals, though it's similarly English-only and uses a different approach. Given that the idea has been thoroughly revised and addresses all major issues from previous rounds, the remaining gaps are whether to add these two calibration methods to the landscape—CORAL being the more pressing inclusion. The core requirement is calibration, and this proposal delivers exactly that through multilingual transfer via shared confidence geometry. Looking at the individual scores—novelty at 4, feasibility at 4, clarity at 5, and impact at 4—the average sits at 4.25, which suggests a pass is warranted. But I need to think through the impact claim more carefully: it hinges on whether the hypothesis actually holds, whether practitioners genuinely need this for real deployments given the documented abstention gaps, and whether the contribution is substantial enough for a top venue like AAAI.

Framing it for ACL/NAACL, if the hypothesis holds, this becomes a strong contribution with 122× data efficiency gains, the first typological transfer boundary for calibration, and practical selective prediction improvements. Even if it doesn't hold, it's still a meaningful negative result with detailed analysis of why calibration directions fail to transfer. That's solid framing—the paper contributes either way. I'm settling on impact: 4 for a competitive top-venue submission.

One thing I should examine more closely: there's potential tension between CORAL's findings at middle layers (53-66% depth) for correctness signals and this approach targeting late-intermediate layers (88-94% depth) for calibration. These could be measuring different phenomena entirely, so the proposal should at least acknowledge this distinction rather than treating them as directly comparable.

Actually, thinking about this more carefully—CORAL's probe is optimizing for correctness prediction, not calibration itself. The calibration direction is specifically about the model's confidence-correctness alignment, which is a related but distinct concept. The focus on calibration correction at late-intermediate layers is well-grounded in Joshi et al. and Zhou et al., so this distinction matters.

I've done enough research to form a judgment. The three rounds of revision have genuinely strengthened this, and what remains are mostly citation gaps that don't undermine the core contribution. I'm inclined to pass it with minor issues flagged.

Though I should pause here—is there a risk this is too incremental? The core move is combining known techniques: difference-in-means direction extraction plus the established finding that calibration directions exist plus evidence that some directions transfer cross-lingually, then testing whether calibration directions specifically transfer. The methodological novelty is minimal; the contribution is primarily empirical.

But that's acceptable for an empirical paper, especially with the language-distance analysis providing additional analytical depth. I'll pass with two minor issues: CORAL needs to be cited, and there's a tension worth discussing between CORAL's finding that middle layers optimize best for correctness and the hypothesis that calibration transfer peaks at much deeper layers. The discrepancy in optimal depths—around 60% for correctness versus 88-94% for calibration—deserves some justification, though it's not a fatal problem.

Actually, Joshi et al. make a useful distinction: accuracy crystallizes early, but the confidence correction phase happens later in the network. Since CORAL optimizes for accuracy while this work targets calibration specifically, there's a valid distinction that the paper already captures.

I'm settling on a pass. The 122× data efficiency gain is substantial if the hypothesis holds, and the typological transfer boundary analysis offers novel insights regardless of outcome. Even if calibration directions don't transfer as expected, the selective prediction demonstration and analytical framework provide meaningful contributions.

For impact, I'm going with 4 out of 5 — the combination of bridging representation engineering with multilingual NLP, plus the practical deployment value of selective prediction, pushes it above a 3.

Now I should flag a couple of minor issues. CORAL's recent work on calibration-aware steering from hidden states is the closest precedent, though it focuses on middle layers for correctness while this proposes late-intermediate layers for calibration — that tension deserves a brief mention. BaseCal's unsupervised approach to calibration is also worth noting as related work.

Neither of these are blocking issues though — the core contribution is solid enough to move forward. Let me prepare the review JSON.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "341e2cc9-54b8-4117-9f85-244bb5cab394",
  "isSidechain": false,
  "requestId": "req_011CbBiHvJVyCHJRQLNAb8BW",
  "type": "assistant",
  "uuid": "ae39200c-1ce2-42db-a8c9-cdbb8a5a6d04",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mHGY1rEjp177udAX2H63F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 288,
      "cache_read_input_tokens": 59698,
      "output_tokens": 3615,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3615,
          "cache_read_input_tokens": 59698,
          "cache_creation_input_tokens": 288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 288
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 136 · 2026-05-19T09:46:27.107Z_

Now let me do one final check for very recent papers (April-May 2026) that could directly compete:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae39200c-1ce2-42db-a8c9-cdbb8a5a6d04",
  "isSidechain": false,
  "requestId": "req_011CbBiHvJVyCHJRQLNAb8BW",
  "type": "assistant",
  "uuid": "28d9305f-b77f-4b0e-b0c8-9d585d645723",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mHGY1rEjp177udAX2H63F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 288,
      "cache_read_input_tokens": 59698,
      "output_tokens": 3615,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3615,
          "cache_read_input_tokens": 59698,
          "cache_creation_input_tokens": 288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 288
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-19T09:46:27.110Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011cyeaK5FPZTRFpik1bnQmZ`</summary>

```json
{
  "query": "arxiv calibration multilingual representation steering transfer 2026 April May zero-shot low-resource"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28d9305f-b77f-4b0e-b0c8-9d585d645723",
  "isSidechain": false,
  "requestId": "req_011CbBiHvJVyCHJRQLNAb8BW",
  "type": "assistant",
  "uuid": "e30acaa8-6e1e-4dd9-8393-0be73e509393",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mHGY1rEjp177udAX2H63F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 288,
      "cache_read_input_tokens": 59698,
      "output_tokens": 3615,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3615,
          "cache_read_input_tokens": 59698,
          "cache_creation_input_tokens": 288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 288
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 138_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "e30acaa8-6e1e-4dd9-8393-0be73e509393",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 139_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Tool result

_source line 140 · 2026-05-19T09:46:33.839Z_

<details><summary>↩ Tool result · `toolu_011cyeaK5FPZTRFpik1bnQmZ`</summary>

```text
Web search results for query: "arxiv calibration multilingual representation steering transfer 2026 April May zero-shot low-resource"

Links: [{"title":"[2210.12265] On the Calibration of Massively Multilingual Language Models","url":"https://arxiv.org/abs/2210.12265"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/html/2505.12584"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326"},{"title":"Languages Transferred Within the Encoder: On Representation Transfer in Zero-Shot Multilingual Translation","url":"https://arxiv.org/html/2406.08092v2"},{"title":"On the Calibration of Massively Multilingual Language Models","url":"https://arxiv.org/pdf/2210.12265"},{"title":"[2104.08645] Improving Zero-Shot Cross-Lingual Transfer Learning via Robust Training","url":"https://arxiv.org/abs/2104.08645"},{"title":"A Simple and Effective Method to Improve Zero-Shot Cross-Lingual   Transfer Learning","url":"https://arxiv.org/pdf/2210.09934"},{"title":"[2406.08092] Languages Transferred Within the Encoder: On Representation Transfer in Zero-Shot Multilingual Translation","url":"https://arxiv.org/abs/2406.08092"}]

Based on the search results, here are the relevant papers found:

## Recent Papers on Multilingual Representation, Steering, and Transfer (April-May 2026):

1. **Language Steering for Multilingual In-Context Learning** (April 1, 2026)
   - This approach requires no parameter updates or fine-tuning, making it practical for low-resource settings.
   - The work evaluates across three datasets spanning mathematical reasoning and natural language inference, 19 languages, and three models, with results validating consistent performance improvements over baselines.

2. **Improving Multilingual Language Models by Aligning Representations through Steering** (August 26, 2025)
   - The method enhances multilingual capabilities of LLMs by steering the representations of a single layer, using a learned alignment with English, enabling zero-shot cross-linguistic transfer without language-specific fine-tuning.

## Related Earlier Work on Calibration and Zero-Shot Transfer:

3. **On the Calibration of Massively Multilingual Language Models** (October 2022)
   - The paper investigates calibration of MMLMs in the zero-shot setting and observes miscalibration in low-resource languages or those typologically diverse from English, showing that calibration methods like temperature scaling and label smoothing do reasonably well towards improving calibration.

These papers directly address the intersection of calibration, multilingual representation steering, transfer learning, and zero-shot performance in low-resource contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e30acaa8-6e1e-4dd9-8393-0be73e509393",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "f8120f7d-f3c8-4679-9a4b-d1bf9aab83ac",
  "toolUseResult": {
    "query": "arxiv calibration multilingual representation steering transfer 2026 April May zero-shot low-resource",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V6jS4hjmRGpeJw1j36oT8V",
        "content": [
          {
            "title": "[2210.12265] On the Calibration of Massively Multilingual Language Models",
            "url": "https://arxiv.org/abs/2210.12265"
          },
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/html/2505.12584"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/html/2602.02326"
          },
          {
            "title": "Languages Transferred Within the Encoder: On Representation Transfer in Zero-Shot Multilingual Translation",
            "url": "https://arxiv.org/html/2406.08092v2"
          },
          {
            "title": "On the Calibration of Massively Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2210.12265"
          },
          {
            "title": "[2104.08645] Improving Zero-Shot Cross-Lingual Transfer Learning via Robust Training",
            "url": "https://arxiv.org/abs/2104.08645"
          },
          {
            "title": "A Simple and Effective Method to Improve Zero-Shot Cross-Lingual   Transfer Learning",
            "url": "https://arxiv.org/pdf/2210.09934"
          },
          {
            "title": "[2406.08092] Languages Transferred Within the Encoder: On Representation Transfer in Zero-Shot Multilingual Translation",
            "url": "https://arxiv.org/abs/2406.08092"
          }
        ]
      },
      "Based on the search results, here are the relevant papers found:\n\n## Recent Papers on Multilingual Representation, Steering, and Transfer (April-May 2026):\n\n1. **Language Steering for Multilingual In-Context Learning** (April 1, 2026)\n   - This approach requires no parameter updates or fine-tuning, making it practical for low-resource settings.\n   - The work evaluates across three datasets spanning mathematical reasoning and natural language inference, 19 languages, and three models, with results validating consistent performance improvements over baselines.\n\n2. **Improving Multilingual Language Models by Aligning Representations through Steering** (August 26, 2025)\n   - The method enhances multilingual capabilities of LLMs by steering the representations of a single layer, using a learned alignment with English, enabling zero-shot cross-linguistic transfer without language-specific fine-tuning.\n\n## Related Earlier Work on Calibration and Zero-Shot Transfer:\n\n3. **On the Calibration of Massively Multilingual Language Models** (October 2022)\n   - The paper investigates calibration of MMLMs in the zero-shot setting and observes miscalibration in low-resource languages or those typologically diverse from English, showing that calibration methods like temperature scaling and label smoothing do reasonably well towards improving calibration.\n\nThese papers directly address the intersection of calibration, multilingual representation steering, transfer learning, and zero-shot performance in low-resource contexts."
    ],
    "durationSeconds": 6.72315271100006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e30acaa8-6e1e-4dd9-8393-0be73e509393",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-19T09:46:37.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013rUAcqcLZMUG8g7rL62Nrg`</summary>

```json
{
  "query": "site:openreview.net cross-lingual calibration confidence direction steering multilingual 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8120f7d-f3c8-4679-9a4b-d1bf9aab83ac",
  "isSidechain": false,
  "requestId": "req_011CbBiQomnniXv5zHDEHUFg",
  "type": "assistant",
  "uuid": "ed7a1bf4-edcd-406c-8fce-9e2ce2517d9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZVeg1AB9QhyZR2e1SVGW3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4328,
      "cache_read_input_tokens": 59986,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 59986,
          "cache_creation_input_tokens": 4328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4328
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-19T09:46:45.064Z_

<details><summary>↩ Tool result · `toolu_013rUAcqcLZMUG8g7rL62Nrg`</summary>

```text
Web search results for query: "site:openreview.net cross-lingual calibration confidence direction steering multilingual 2026"

Links: [{"title":"Language-Specific Latent Process Hinders Cross-Lingual Performance | OpenReview","url":"https://openreview.net/forum?id=A5YyXBg79E"},{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | OpenReview","url":"https://openreview.net/forum?id=8DBHkEe0sm"},{"title":"C: Confidence Calibration Model Cascade for Inference-Efficient Cross-Lingual Natural Language Understanding | OpenReview","url":"https://openreview.net/forum?id=gmo4R1b2xB"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/pdf/2601.08331"},{"title":"Align after Pre-train: Improving Multilingual Generative Models with Cross-lingual Alignment | OpenReview","url":"https://openreview.net/forum?id=3PaVCdeEmW"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/pdf/2505.12584"},{"title":"Mexa: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | OpenReview","url":"https://openreview.net/forum?id=hsMkpzr9Oy"}]

I found several relevant research papers on OpenReview and related platforms matching your search query about cross-lingual calibration, confidence, direction steering, and multilingual models. Here are the key results:

**OpenReview Papers Found:**

1. **Language-Specific Latent Process Hinders Cross-Lingual Performance** - Demonstrates that knowledge sharing in small models can be facilitated by steering their latent processing towards the shared semantic space, which improves the models' multilingual reasoning performance and results in better output consistency with English.

2. **Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs** - Research revealing that universal factual transfer and culturally-specific knowledge are optimally steerable at different model layers, proposing "Surgical Steering," a novel inference-time method that disentangles these two objectives.

3. **Confidence Calibration Model Cascade for Inference-Efficient Cross-Lingual Natural Language Understanding** - Introduces a confidence calibration model cascade method that involves calibration prior to cascade inference, enhancing cascade accuracy through more reliable predictions.

4. **CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark** - A lightweight parallel-question benchmark for evaluating language-forcing behavior in LLMs across 32 languages, enabling systematic evaluation of multilingual steering methods.

5. **Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models** - First layer-wise investigation of multilingual calibration, discovering that intermediate layers offer more reliable calibration signals than the final layer, and introducing training-free calibration methods that leverage intermediate representations.

These papers cover confidence calibration, direction steering, and cross-lingual alignment techniques for multilingual language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed7a1bf4-edcd-406c-8fce-9e2ce2517d9d",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "69d4eb69-9c16-4625-849b-83e95c87a1d9",
  "toolUseResult": {
    "query": "site:openreview.net cross-lingual calibration confidence direction steering multilingual 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JsDMSRCqArv72iPuTZNQc6",
        "content": [
          {
            "title": "Language-Specific Latent Process Hinders Cross-Lingual Performance | OpenReview",
            "url": "https://openreview.net/forum?id=A5YyXBg79E"
          },
          {
            "title": "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=8DBHkEe0sm"
          },
          {
            "title": "C: Confidence Calibration Model Cascade for Inference-Efficient Cross-Lingual Natural Language Understanding | OpenReview",
            "url": "https://openreview.net/forum?id=gmo4R1b2xB"
          },
          {
            "title": "CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark",
            "url": "https://arxiv.org/pdf/2601.08331"
          },
          {
            "title": "Align after Pre-train: Improving Multilingual Generative Models with Cross-lingual Alignment | OpenReview",
            "url": "https://openreview.net/forum?id=3PaVCdeEmW"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          },
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/pdf/2505.12584"
          },
          {
            "title": "Mexa: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | OpenReview",
            "url": "https://openreview.net/forum?id=hsMkpzr9Oy"
          }
        ]
      },
      "I found several relevant research papers on OpenReview and related platforms matching your search query about cross-lingual calibration, confidence, direction steering, and multilingual models. Here are the key results:\n\n**OpenReview Papers Found:**\n\n1. **Language-Specific Latent Process Hinders Cross-Lingual Performance** - Demonstrates that knowledge sharing in small models can be facilitated by steering their latent processing towards the shared semantic space, which improves the models' multilingual reasoning performance and results in better output consistency with English.\n\n2. **Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs** - Research revealing that universal factual transfer and culturally-specific knowledge are optimally steerable at different model layers, proposing \"Surgical Steering,\" a novel inference-time method that disentangles these two objectives.\n\n3. **Confidence Calibration Model Cascade for Inference-Efficient Cross-Lingual Natural Language Understanding** - Introduces a confidence calibration model cascade method that involves calibration prior to cascade inference, enhancing cascade accuracy through more reliable predictions.\n\n4. **CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark** - A lightweight parallel-question benchmark for evaluating language-forcing behavior in LLMs across 32 languages, enabling systematic evaluation of multilingual steering methods.\n\n5. **Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models** - First layer-wise investigation of multilingual calibration, discovering that intermediate layers offer more reliable calibration signals than the final layer, and introducing training-free calibration methods that leverage intermediate representations.\n\nThese papers cover confidence calibration, direction steering, and cross-lingual alignment techniques for multilingual language models."
    ],
    "durationSeconds": 7.895801762999967,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ed7a1bf4-edcd-406c-8fce-9e2ce2517d9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-19T09:46:48.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SbbDFECqZUZwLoY6V2CVXh`</summary>

```json
{
  "query": "Khanmohammadi \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\" CCPS EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69d4eb69-9c16-4625-849b-83e95c87a1d9",
  "isSidechain": false,
  "requestId": "req_011CbBiRdk52XUnNkumj32ih",
  "type": "assistant",
  "uuid": "eec9d66b-f808-4f82-8f70-13d12f1b0f9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnuYT5ySQz8TPCZyoxpYzJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 64314,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 64314,
          "cache_creation_input_tokens": 933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 933
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-19T09:46:55.616Z_

<details><summary>↩ Tool result · `toolu_01SbbDFECqZUZwLoY6V2CVXh`</summary>

```text
Web search results for query: "Khanmohammadi "Calibrating LLM Confidence by Probing Perturbed Representation Stability" CCPS EMNLP 2025"

Links: [{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.530/"},{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"CCPS: Calibrating LLM Confidence via Perturbation Stability – EMNLP 2025 | Hacker News","url":"https://news.ycombinator.com/item?id=45055315"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF","url":"https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/calibrating-llm-confidence-by-probing-perturbed-representation"},{"title":"(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"}]

I found the paper! Here are the details about this research:

## Paper Overview

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method analyzing internal representational stability in LLMs.

## Authors and Affiliation

The paper was authored by Reza Khanmohammadi (Michigan State University), Erfan Miahi (Independent AI Researcher), Mehrsa Mardikoraem (Independent AI Researcher), Simerjot Kaur (JPMorgan AI Research), Ivan Brugere (JPMorgan AI Research), Charese H. Smiley (JPMorgan AI Research), Kundan Thind (Henry Ford Health), and Mohammad M. Ghassemi (Michigan State University).

## Publication

The paper was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, in Suzhou, China.

## Method

CCPS operates on frozen base LLMs, applying targeted adversarial perturbations to the final hidden states that generate an answer's tokens, and extracts a rich feature set to train a lightweight classifier to predict answer correctness.

## Key Results

Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curve by 6 percentage points, all relative to the strongest prior method.

The official implementation is available on [GitHub](https://github.com/ledengary/CCPS), and the paper is available on [arXiv](https://arxiv.org/abs/2505.21772) and the [ACL Anthology](https://aclanthology.org/2025.emnlp-main.530/).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eec9d66b-f808-4f82-8f70-13d12f1b0f9d",
  "isSidechain": false,
  "promptId": "ccbc7a65-027c-403c-951a-c347981c1d09",
  "type": "user",
  "uuid": "d37f2ada-5b30-4256-9759-1705ba78f4f6",
  "toolUseResult": {
    "query": "Khanmohammadi \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\" CCPS EMNLP 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ud7iMK4qD7iZkspAPDpVU2",
        "content": [
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.530/"
          },
          {
            "title": "[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/abs/2505.21772"
          },
          {
            "title": "CCPS: Calibrating LLM Confidence via Perturbation Stability – EMNLP 2025 | Hacker News",
            "url": "https://news.ycombinator.com/item?id=45055315"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/pdf/2505.21772"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/html/2505.21772v1"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF",
            "url": "https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"
          },
          {
            "title": "GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://github.com/ledengary/CCPS"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/calibrating-llm-confidence-by-probing-perturbed-representation"
          },
          {
            "title": "(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"
          }
        ]
      },
      "I found the paper! Here are the details about this research:\n\n## Paper Overview\n\nCCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method analyzing internal representational stability in LLMs.\n\n## Authors and Affiliation\n\nThe paper was authored by Reza Khanmohammadi (Michigan State University), Erfan Miahi (Independent AI Researcher), Mehrsa Mardikoraem (Independent AI Researcher), Simerjot Kaur (JPMorgan AI Research), Ivan Brugere (JPMorgan AI Research), Charese H. Smiley (JPMorgan AI Research), Kundan Thind (Henry Ford Health), and Mohammad M. Ghassemi (Michigan State University).\n\n## Publication\n\nThe paper was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, in Suzhou, China.\n\n## Method\n\nCCPS operates on frozen base LLMs, applying targeted adversarial perturbations to the final hidden states that generate an answer's tokens, and extracts a rich feature set to train a lightweight classifier to predict answer correctness.\n\n## Key Results\n\nAcross four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curve by 6 percentage points, all relative to the strongest prior method.\n\nThe official implementation is available on [GitHub](https://github.com/ledengary/CCPS), and the paper is available on [arXiv](https://arxiv.org/abs/2505.21772) and the [ACL Anthology](https://aclanthology.org/2025.emnlp-main.530/)."
    ],
    "durationSeconds": 7.235156224999926,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eec9d66b-f808-4f82-8f70-13d12f1b0f9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 145 · 2026-05-19T09:47:26.855Z_

<details><summary>Logged reasoning block</summary>

```text
Good. All references check out. Now let me also verify the claim that "Gupta et al. showed instruction-tuning inflates confidence in low-resource languages without accuracy gains" — this was confirmed above.

Let me also check if the idea's specific claim about the "5× worse calibration error" number is accurate — from Zhou et al., they say LLaMA-3 shows 23.1% vs. 4.6% ECE for non-English vs. English — that's about 5.0×. ✓

Let me also note a potential issue: LLaMA 4 Scout officially supports only 12 languages, but was trained on data from 200 languages. 

Using it for Belebele's 122 languages would test many languages outside its official support, which is actually fine for the experiment since it reveals how the model handles unsupported languages, though it's worth flagging. After thorough verification, all key references check out: Zhou et al. on calibration error, Ji et al. on linear calibration directions, and Wang et al. on refusal direction universality. I'm verifying a series of papers from early 2026, checking that the citations, results, and claims are accurate across venues like EACL and EMNLP, with the last entry appearing to be cut off mid-arxiv number.

Now I'm confirming the architecture details for three major models—Qwen3.6-27B with its hybrid layer structure, LLaMA 4 Scout's mixture-of-experts setup, and Aya Expanse's dense transformer configuration—and noting that AAAI 2027 has an abstract deadline in late July.

I'm also verifying the Belebele dataset spans 122 languages with 900 questions each, and checking that the cross-lingual calibration direction transfer approach hasn't been explored before. There are a couple of recent papers I should cite—CORAL from February 2026 on calibration-aware steering and BaseCal from January 2026 on hidden-state projection methods—both of which are relevant but currently missing from the references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d37f2ada-5b30-4256-9759-1705ba78f4f6",
  "isSidechain": false,
  "requestId": "req_011CbBiSQugHXRufQYpCgQ7p",
  "type": "assistant",
  "uuid": "3b9ef7fb-b649-4b81-99dd-92efd9b0f820",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxamNUCERpuqyPGmXEBx5w",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 65247,
      "output_tokens": 2343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2343,
          "cache_read_input_tokens": 65247,
          "cache_creation_input_tokens": 1128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1128
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 146 · 2026-05-19T09:47:50.604Z_

I've now completed thorough verification. Let me compile my final assessment.

**Summary of verification:**

All 18 key references verified as existing and correctly described. Architecture specs for all 3 models confirmed. Venue deadlines confirmed. Belebele dataset size (900/language) confirmed. No competing work found that directly scoops the cross-lingual calibration direction transfer idea. Two minor citation gaps identified.

```json
{
  "verdict": "pass",
  "scores": {
    "novelty": {"score": 4, "rationale": "The specific combination — transferring calibration directions (emergent, not explicitly trained) cross-lingually via difference-in-means extraction — is genuinely untested. My extensive searches across arXiv, OpenReview, and Semantic Scholar found no prior work doing this. The typological transfer boundary analysis adds unique analytical value. However, the methodology itself (contrastive direction extraction + cross-lingual application) is well-established from refusal/steering literature, making this an incremental-but-meaningful extension."},
    "feasibility": {"score": 4, "rationale": "All models (Qwen3.6-27B, LLaMA 4 Scout, Aya Expanse 32B) are publicly available. Benchmarks exist. Resource estimates (400-550 H100-hours) are realistic for 3 models × 122 languages × full layer sweeps with hidden-state extraction. Architecture-specific extraction is well-specified and supported by prior evidence (Yap 2603.16335 for DeltaNet hybrids, AEON-7 abliteration). Statistical methodology (BCa bootstrap, adaptive binning, debiased ECE) is sound. Main risk is empirical — the hypothesis may not hold — but this is acknowledged and framed as informative either way."},
    "clarity": {"score": 5, "rationale": "Exceptionally well-organized: explicit layer-mapping table, architecture-specific extraction details, 7-phase experimental plan with clear hypotheses, comprehensive landscape covering both supporting and counter-evidence (Mahmoud et al. cross-family limitations). The framing of calibration as a distinct post-decisional process separate from difficulty/semantics is convincing and well-argued."},
    "impact": {"score": 4, "rationale": "The 122× data efficiency improvement over LACE (if hypothesis holds) is practically significant for multilingual deployment. The typological transfer boundary analysis is a novel contribution regardless of outcome. The Phase 6 selective prediction demonstration directly addresses the 20.5% abstention gap (Feng et al.), providing concrete deployment value. The work bridges representation engineering and multilingual NLP — two active fields. Bounded by: (a) the hypothesis might fail, and (b) simpler methods (temperature scaling) may suffice for some use cases."}
  },
  "issues": [
    "MINOR: CORAL (arXiv 2602.06022, Feb 2026) is not cited. This is the most relevant recent work on calibration-aware inference-time steering from hidden states — it uses MLP probes on middle layers (53-66% depth in 30-layer models) to improve both accuracy and ECE by ~50%. While English-only and using supervised probes rather than contrastive directions, it should appear in the landscape. The tension between CORAL's middle-layer finding and the proposed late-intermediate layer (88-94% depth) hypothesis deserves brief discussion — CORAL optimizes for correctness prediction while the proposed calibration direction targets the distinct confidence correction phase (Joshi et al.).",
    "MINOR: BaseCal (arXiv 2601.03042, Jan 2026) — unsupervised calibration via projecting post-trained hidden states to base model space — is a tangentially relevant calibration method from the same period that could be briefly mentioned as an alternative paradigm.",
    "MINOR: LLaMA 4 Scout officially supports only 12 languages despite being trained on 200-language data. The experimental design should note which of the 122 Belebele languages fall outside Scout's official support and whether this affects interpretation of calibration transfer results for those languages."
  ],
  "feedback": "",
  "reason": "All references independently verified, novelty claim holds (no prior cross-lingual calibration direction transfer work found), architecture specs confirmed, venue deadlines valid, resource estimates realistic. Three rounds of revision have produced a thorough, well-specified proposal with genuine novelty and practical impact. Remaining issues are minor citation gaps that do not threaten core contributions."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b9ef7fb-b649-4b81-99dd-92efd9b0f820",
  "isSidechain": false,
  "requestId": "req_011CbBiSQugHXRufQYpCgQ7p",
  "type": "assistant",
  "uuid": "ee6c11c0-149c-4be6-8ca6-aeae253be3c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxamNUCERpuqyPGmXEBx5w",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 65247,
      "output_tokens": 2343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2343,
          "cache_read_input_tokens": 65247,
          "cache_creation_input_tokens": 1128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1128
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 147_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "ee6c11c0-149c-4be6-8ca6-aeae253be3c9",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 148_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 149_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "ee6c11c0-149c-4be6-8ca6-aeae253be3c9",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---

### Runtime record

_source line 150_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual calibration transfer via steering vectors",
  "sessionId": "3fb644f2-5f5b-4b36-aa26-243980802dbe"
}
```

---
