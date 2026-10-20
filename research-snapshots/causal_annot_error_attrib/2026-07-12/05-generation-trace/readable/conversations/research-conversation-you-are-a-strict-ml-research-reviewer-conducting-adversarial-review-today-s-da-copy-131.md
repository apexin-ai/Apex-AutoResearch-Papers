# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-19 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 150
- **Recorded user turns:** 1
- **Tool calls:** 48
- **Original source:** `logs/chats/exported-trajectories/account-2/b373d757-44ed-4e47-bf31-3bb789326a9d.jsonl`
- **Structured JSON:** [`84085bcf605bbed6d9ab.json`](../../sessions/84/84085bcf605bbed6d9ab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T13:14:07.977Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T13:14:07.977Z",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-19 (UTC).**\n\nYour job: independently verify this idea's claims via web_search, then issue a verdict.\n\n## User requirements\nThe user asked for: **calibration**\nEvaluate whether this idea actually meets the user's requirements. An idea that doesn't match should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：用 WebFetch 实际阅读相关论文的 abstract 和关键章节。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献\n\n6. **评分诚实**：\n   - 4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} 2026` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} 2026` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} 2026 site:scholar.google.com`\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} 2026` — 按活跃作者追踪\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} 2026` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey 2026` — 找综述论文\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n\n### 搜索维度\n\n1. **正向搜索**：直接搜索主题相关论文\n2. **竞争论文搜索**（最关键！）：有没有人在解决同样的问题？用类似方法？\n3. **相邻领域搜索**：其他领域是否已解决类似问题\n4. **反面搜索**：找到反对你 idea 的证据\n5. **引用链追踪**：找到核心论文后，查看 cited-by 发现 concurrent work\n\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n2. **知名团队追踪**：搜索相关团队最近的论文\n3. **会议最新录用**：搜索 `site:openreview.net {topic} 2026`\n4. **arXiv 近 3 个月密集搜索**\n\n## Review checklist\n1. **SOTA freshness**: Are baselines actually current SOTA?\n2. **Reference verification**: Do cited papers actually exist?\n3. **Gap validity**: Does the claimed gap still exist?\n4. **Venue validity**: Are target venue deadlines after 2026-05-19?\n5. **Feasibility**: Is the resource estimate realistic?\n6. **Novelty**: Is this sufficiently different from existing work?\n7. **Cost realism**: Are the three mode estimates internally consistent?\n\n## Idea under review (round 3/10)\n{\n  \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activation Steering\",\n  \"core_problem\": \"LLM miscalibration arises from at least two competing biases — choice-supportive bias (inflating confidence in initial answers) and contradictory-evidence overweighting (causing excessive confidence revision under criticism) — that require opposing corrections. Existing calibration methods apply uniform corrections that cannot simultaneously address biases pulling confidence in opposite directions. Recent work (Liu, 2605.05715) further reveals a classification-correction gap: failure-mode directions that are linearly decodable may not be linearly steerable due to entanglement with task-critical computation (specificity ratio ≤0.152). This means even if competing biases can be identified in activations, correcting them requires knowing not just WHICH bias dominates but WHETHER each bias direction is steerable — and routing to appropriate interventions (linear rotation, non-linear correction, or selective abstention) accordingly. Can we jointly diagnose per-instance bias dominance AND steerability to apply targeted, manifold-preserving corrections where possible and graceful degradation where not?\",\n  \"opportunity\": \"Kumaran et al. (Nature Machine Intelligence, 2026; arXiv 2507.03120) identified that LLM miscalibration results from two mechanistically distinct behavioral biases in Gemma 3, GPT-4o, and o1-preview: choice-supportive bias inflates confidence in selected answers, while contradictory-advice overweighting causes models to over-react to opposing evidence. Miao & Ungar (arXiv 2603.25052, 2026) independently showed that calibration and verbalized confidence signals are encoded linearly but orthogonally in the residual stream across three 7-8B models, establishing that confidence-related constructs have accessible geometric structure. Liu (arXiv 2605.05715, May 2026) demonstrated a critical classification-correction gap: linearly decodable failure directions (71.6% balanced accuracy) yield Δ≈0 under 29 steering configurations because the failure directions have 85-88% overlap with task-critical computation (specificity ratio ≤0.152) — but crucially, the paper also shows that (a) a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods fail, and (b) the decodable signal still supports selective abstention (AUROC 0.610, outperforming 5 uncertainty baselines). The 'Confidence Manifold' study (arXiv 2602.08159) found correctness signals occupy only 3-8 dimensions with simple mean-shift geometry across 9 models, suggesting that for calibration-related directions, the geometric structure may be more favorable than for the medical overthinking phenomenon Liu studied. The convergence of (a) identified competing biases, (b) linear confidence encoding evidence, (c) the decodable-steerable distinction with quantitative diagnostics, and (d) both norm-preserving rotation (Spherical Steering, ICML 2026) and collateral-damage-aware optimization (COAST, 2605.01167) creates an opportunity for a principled pipeline: diagnose bias identity, assess steerability, and route to the appropriate intervention.\",\n  \"landscape\": \"Kumaran et al. (Nature MI, 2026) identified competing biases (CSB and CEO) via behavioral experiments on Gemma 3, GPT-4o, and o1-preview but proposed no correction framework and provided no mechanistic (activation-level) evidence. Miao & Ungar (arXiv 2603.25052, 2026) demonstrated that calibration accuracy and verbalized confidence are linearly encoded but orthogonal in 7-8B models (cosine similarity <0.04 across layers), and introduced adaptive steering achieving 4-7× ECE improvement — but they target the confidence-accuracy misalignment gap, not the competing bias structure. Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) decomposed LLM assertiveness into emotional and logical sub-components via unsupervised clustering on Llama-3.2-1B-Instruct (645 samples), finding two clusters in high-assertive representations — methodologically adjacent but critically different: their decomposition is descriptive (post-hoc ChatGPT-labeled clusters of communication style) rather than causally grounded in identified cognitive biases, uses a single 1B model, reports no calibration metrics, and addresses assertiveness rather than calibration. The 'Wired for Overconfidence' paper (2604.01457, April 2026) identifies overconfidence circuits in Qwen2.5-3B and Llama-3.2-3B, achieving 96.9% ECE reduction on PopQA via monolithic activation steering, but only tests 3B models and treats overconfidence as a single phenomenon. Liu (arXiv 2605.05715, May 2026) is the most directly relevant recent advance: the paper demonstrates a classification-correction gap where linearly decodable failure directions (71.6% balanced accuracy on Llama-3.1-8B) yield Δ≈0 across five families of linear steering (29 configurations) because the failure direction has 85-88% overlap with task-critical computation (specificity ratio ≤0.152). Three convergent evidence lines confirm entanglement: low specificity, shared-direction steering damages accuracy (-12.1pp), and LEACE concept erasure damages accuracy (-3.6pp). Crucially, a learned non-linear bottleneck MLP (4096→64→4096) achieves Δ=+2.8pp (p=0.025) where linear methods fail, though with 8.2% damage rate — demonstrating that partial disentanglement is possible via non-linear transforms. The paper proposes the specificity ratio as a pre-intervention diagnostic and recommends selective abstention (AUROC 0.610) when steering fails. However, this was studied for medical overthinking, a single failure mode; whether calibration biases (CSB/CEO) exhibit similar or different entanglement profiles is an open question. Ji et al. (EMNLP 2025) modulates a single Verbal Uncertainty Feature direction, reducing hallucinations by ~30%, capturing only the net effect of competing biases. Joshi et al. (EMNLP 2025) found a single calibration direction but did not decompose it. CORAL (arXiv 2602.06022, Feb 2026) achieves 49% ECE improvement via correctness-subspace probing on 7B models but uses a single MLP probe direction. The 'Confidence Manifold' study (arXiv 2602.08159, Feb 2026) found correctness signals occupy 3-8 dimensions with simple mean-shift geometry across 9 models from 5 families, and causally validated via steering (10.9pp error rate change) — importantly, the low dimensionality and linear separability of correctness signals contrasts with Liu's high-entanglement finding for overthinking, suggesting calibration-related directions may have more favorable specificity profiles. Wang & Stengel-Eskin (ICLR 2026) introduced DINCO to normalize suggestibility bias via self-generated distractors at the output level. Zhuang et al. (arXiv 2025) proposed RDG to alleviate choice-supportive bias through fine-tuning but did not address CEO. CCPS (arXiv 2025) achieves ~55% ECE reduction via representation stability probing on MMLU. 'Breaking the Mirror' (arXiv 2509.03647) found that self-preference bias 'spans multiple or nonlinear directions,' achieving 97% unjustified bias reduction but with instability on legitimate cases — a direct warning that some biases may not be linearly separable. On the steering methodology side, the landscape has rapidly matured: Spherical Steering (arXiv 2602.08169, ICML 2026) performs norm-preserving geodesic rotation, outperforming addition-based baselines by +10% on TruthfulQA while maintaining generation quality. Selective Steering (Dang & Ngo, arXiv 2601.19375, Jan 2026) independently developed norm-preserving rotation with discriminative layer selection — applying steering only where feature representations exhibit opposite-signed class alignment, achieving 5.5× higher attack success rates with zero perplexity violations across 8 models from 3 families (Llama, Qwen, Gemma). COAST (Nguyen et al., arXiv 2605.01167, May 2026) formalizes collateral damage from steering interventions as unintended alignment changes along non-target feature directions, models steering as a constrained optimization minimizing expected squared collateral change weighted by the empirical second-moment matrix of activations, achieving up to 30% improvement over Angular Steering with strong negative correlation (r<-0.9) between collateral damage and accuracy loss across six benchmarks. AUSteer (arXiv 2602.04428, Feb 2026) decomposes block activations into fine-grained atomic units, steering fewer activations more precisely. CLAS (arXiv 2604.24693, Apr 2026) dynamically adapts steering strengths per-context across 11 benchmarks and 4 model families. 'Steered LLM Activations are Non-Surjective' (2604.09839, April 2026) formally proved that additive steering pushes activations off-manifold; 'A Sober Look at Steering Vectors' (NeurIPS 2024) showed many behaviors are unsteerable. No existing method jointly diagnoses which calibration bias dominates, assesses the steerability of each bias direction (via specificity ratio or equivalent), and routes to bias-specific interventions that range from manifold-preserving rotation to learned non-linear correction to selective abstention — yet the competing effects of CSB and CEO on calibration, combined with the now-established decodable-steerable gap, mean that both uniform correction AND uniform intervention strategy are fundamentally suboptimal.\",\n  \"inspired_by\": \"Gap: Competing biases create non-uniform miscalibration patterns that single-direction methods cannot fix (Kumaran et al. 2026), while the classification-correction gap (Liu, 2605.05715) shows that decodable directions are not necessarily steerable — meaning Phase 1's separability validation is necessary but insufficient. Pattern: Theory-driven contrastive probing (Miao & Ungar 2026) + steerability diagnostics (specificity ratio, Liu 2026) + adaptive intervention routing (geometry-aware rotation for steerable directions, learned non-linear correction for entangled directions). Untried combination: Cognitive-bias-grounded contrastive stimuli → per-instance bias diagnosis → specificity-informed intervention routing (Spherical Steering / non-linear MLP / selective abstention), with the hypothesis that CSB and CEO may have asymmetric steerability profiles — which would explain why monolithic steering sometimes succeeds and sometimes fails at calibration correction.\",\n  \"approach\": \"We design DBS-v2 (Disentangled Bias Steering) in three phases, now incorporating the critical distinction between decodability and steerability identified by Liu (2605.05715).\\n\\n**Phase 1 — Assumption Validation & Steerability Assessment (Weeks 1-5):** This phase tests TWO assumptions, not one: (A) that CSB and CEO produce distinguishable activation signatures, and (B) that identified directions are steerable without catastrophic collateral damage.\\n\\n*Phase 1A — Separability (Weeks 1-3):* We construct two contrastive stimulus sets: for CSB, we compare hidden states when the model reviews its own prior answer vs. a fresh unattributed answer (eliciting choice-supportive inflation); for CEO, we compare states when contradictory expert advice is present vs. absent (eliciting evidence overweighting). Using difference-in-means on these contrastive pairs, we extract candidate bias directions in the residual stream. We validate separability via: (a) cosine similarity between candidate directions, (b) principal angle analysis between CSB and CEO subspaces using the methodology of Miao & Ungar (2026), (c) PCA to assess whether 2 directions capture sufficient variance vs. requiring higher-dimensional subspaces, (d) ICA to test whether statistically independent (not just orthogonal) components emerge, and (e) cross-prediction ablations to confirm removing one bias subspace does not collapse the other. If CSB and CEO directions show cosine similarity >0.3 or shared variance >15%, we activate the separability fallback: extracting a multi-direction bias subspace via SAE-derived features and training a subspace projection classifier.\\n\\n*Phase 1B — Steerability Diagnostics (Weeks 3-5):* This is a critical addition motivated by Liu (2605.05715). Even if CSB and CEO are separable (Phase 1A succeeds), steering along identified directions may fail if those directions are entangled with task-critical computation. For each identified bias direction, we compute: (a) the **specificity ratio** — the proportion of mode-specific variance vs. shared variance with the correct-vs-incorrect subspace, following Liu's shared-specific decomposition methodology. Concretely, we extract the correctness subspace (correct vs. incorrect answer centroids), then decompose each bias direction into a component within this subspace (shared) and a component orthogonal to it (mode-specific). The specificity ratio = ||mode-specific||² / ||total||². (b) **Within-class variance analysis** — comparing within-class variance to inter-centroid gap for each bias direction (Liu's second diagnostic). (c) **LEACE concept erasure test** — applying concept erasure to each bias direction and measuring accuracy damage as causal evidence of entanglement. (d) **Cross-architecture stability** — verifying specificity ratios are consistent across model families.\\n\\nWe establish quantitative thresholds informed by Liu's findings: specificity ratio ≥0.5 → HIGH steerability (linear rotation expected to work); 0.2-0.5 → MEDIUM (rotation may partially work, monitor collateral damage); <0.2 → LOW (linear steering unlikely to succeed, route to non-linear intervention). These thresholds are calibrated against Liu's findings where specificity ≤0.152 yielded Δ≈0 for linear steering while ≥0.999 succeeded for refusal steering. Crucially, we hypothesize that CSB and CEO may have ASYMMETRIC specificity profiles — one may be more steerable than the other — which would provide a mechanistic explanation for why monolithic calibration steering sometimes succeeds partially.\\n\\nPhase 1 results constitute an independent contribution: the first joint separability-and-steerability assessment of behaviorally-identified competing biases, providing the field's first specificity ratio measurements for calibration-related bias directions.\\n\\n**Phase 2 — Per-Instance Bias Diagnosis (Weeks 4-8):** A lightweight logistic probe (or, in the fallback case, a small MLP) trained on per-instance projection magnitudes onto each bias direction classifies which bias dominates for a given query. We stratify by difficulty: on easy questions where models are already confident, CSB likely dominates; on hard questions under criticism, CEO likely dominates. The probe output provides a continuous dominance score. NEW: The Phase 1B steerability assessment informs a per-direction intervention routing table, so the probe's output determines not only which bias is active but which intervention to apply.\\n\\n**Phase 3 — Adaptive Geometry-Aware Intervention (Weeks 6-14):** Instead of a single intervention strategy, Phase 3 now implements an adaptive routing pipeline informed by Phase 1B's steerability diagnostics:\\n\\n*Route A — Spherical Steering (for HIGH-specificity directions):* When a bias direction has specificity ratio ≥0.5, we adopt Spherical Steering (You et al., ICML 2026) as the primary intervention: rotating activations along a geodesic away from the dominant bias direction while preserving activation norms. This addresses the off-manifold concern (Mishra et al., 2604.09839) while the high specificity ensures minimal collateral damage to task-critical computation. A confidence gate modulates rotation magnitude based on the probe's dominance score. We note that Selective Steering (Dang & Ngo, 2601.19375) provides an alternative norm-preserving formulation with discriminative layer selection; we ablate both to determine which is more effective for calibration-specific interventions.\\n\\n*Route B — Learned Non-Linear Residual Correction (for LOW-specificity directions):* When a bias direction has specificity ratio <0.2, linear steering of any kind (additive, rotational, or projected) is expected to fail due to entanglement with task-critical computation (Liu, 2605.05715). Following Liu's finding that a bottleneck residual MLP (d→64→d) achieves Δ=+2.8pp where all 29 linear configurations yield Δ≈0, we train a small non-linear residual adapter per bias type. The adapter takes the hidden state as input and outputs a residual correction, trained via supervision on (biased state, corrected state) pairs extracted from the contrastive dataset. We incorporate the COAST framework (Nguyen et al., 2605.01167) by weighting the training loss by the empirical second-moment matrix to minimize expected collateral damage along non-target feature directions. The adapter's bottleneck architecture (d→64→d, <0.1% of model parameters) keeps the intervention lightweight and inference-efficient.\\n\\n*Route C — Selective Abstention (for UNSTEERABLE directions):* When Phase 1B indicates low specificity AND Phase 3 ablations confirm that neither Route A nor Route B improves calibration without excessive damage (>5% accuracy degradation), we leverage the decodable signal for selective abstention: the bias probe flags instances where the dominant bias has high activation but low steerability, outputting a reliability score. Following Liu's demonstration that decodable signals support post-generation reliability estimation (AUROC 0.610) even when correction fails, this provides a graceful degradation path.\\n\\n*Route D — Medium-Specificity Hybrid (for intermediate cases):* For directions with specificity 0.2-0.5, we apply Spherical Steering with conservative rotation magnitude (capped at 50% of the high-specificity coefficient) and monitor collateral damage via the COAST second-moment diagnostic. If per-instance collateral damage exceeds a threshold, we fall back to Route B for that instance.\\n\\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct. We additionally include Qwen2.5-3B and Llama-3.2-3B as supplementary models to enable fair comparison with 'Wired for Overconfidence' results at the same scale. Metrics: ECE, Brier score, AUROC, difficulty-stratified ECE (easy/medium/hard partitions), AND NEW: per-direction specificity ratios, collateral damage measurements (accuracy on non-target tasks before/after steering), and route-distribution analysis (what fraction of instances are routed to each intervention). Baselines: temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic circuit ablation (Wired for Overconfidence replication at 3B scale), monolithic Spherical Steering (single direction, no bias decomposition), and NEW: monolithic non-linear residual MLP (single direction, no bias decomposition) to isolate the contribution of bias decomposition from the contribution of non-linear correction.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"750-1050 H100\",\n      \"timeline\": \"16-20 weeks\",\n      \"estimated_gpu_cost\": \"$1,875-$2,625 (H100 @ ~$2.50/hr mid-tier provider)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"650-900 H100\",\n      \"timeline\": \"12-15 weeks\",\n      \"claude_api_cost\": \"$350-$600 (Sonnet 4.6 for contrastive dataset generation, probing code, specificity ratio computation scripts, non-linear adapter training, analysis)\",\n      \"estimated_gpu_cost\": \"$1,625-$2,250\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1000-1400 H100\",\n      \"timeline\": \"6-10 weeks\",\n      \"claude_api_cost\": \"$800-$1,400 (Opus 4.7 for experiment orchestration, assumption validation analysis, steerability diagnostics, adapter training sweeps, ablation design)\",\n      \"estimated_gpu_cost\": \"$2,500-$3,500\",\n      \"speed_bottleneck\": \"Phase 1A→1B is inherently sequential (separability must be established before steerability diagnostics are meaningful). Phase 1B requires extracting the correctness subspace and computing specificity ratios per-direction per-model, which is parallelizable across models but adds ~2 weeks over original timeline. Route B adapter training requires supervision pairs from Phase 1 contrastive data. Steering coefficient search across 5 models × 4 datasets × 3-4 intervention routes generates large evaluation matrices. Fair replication of 'Wired for Overconfidence' baselines on 3B models adds overhead.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target, tight but feasible with aggressive Phase 1 timeline)\",\n    \"ARR August 2026 cycle (Aug 3, 2026 — targets EMNLP 2027 or future *CL venues)\",\n    \"NeurIPS 2026 Workshops (~Aug 29, 2026 — workshop paper track for Phase 1 separability + steerability results)\",\n    \"AACL-IJCNLP 2026 (ARR May 25 commitment deadline Aug 26, 2026 — if Phase 1 completes early)\",\n    \"ICLR 2027 (expected Oct 2026 deadline — full paper with all phases and routes complete)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Competing Biases underlie Overconfidence and Underconfidence in LLMs (Kumaran et al., Nature Machine Intelligence 2026; arXiv 2507.03120)\",\n    \"Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, arXiv 2603.25052, 2026) — orthogonal calibration/confidence encoding, adaptive steering\",\n    \"LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components (Tsujimura & Tagade, arXiv 2508.17182, 2025) — closest methodological precedent\",\n    \"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes (Liu, arXiv 2605.05715, May 2026) — classification-correction gap, specificity ratio diagnostic\",\n    \"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs (arXiv 2604.01457, 2026)\",\n    \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., ICML 2026; arXiv 2602.08169)\",\n    \"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection (Dang & Ngo, arXiv 2601.19375, Jan 2026) — independent norm-preserving rotation with discriminative layer selection\",\n    \"Minimizing Collateral Damage in Activation Steering (Nguyen et al., arXiv 2605.01167, May 2026) — COAST framework, collateral damage formalization, second-moment optimization\",\n    \"Steered LLM Activations are Non-Surjective (Mishra et al., arXiv 2604.09839, 2026)\",\n    \"A Sober Look at Steering Vectors for LLMs (Tan et al., NeurIPS 2024)\",\n    \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models (arXiv 2602.08159, 2026) — 3-8 dimensional correctness signals, linear separability across 9 models\",\n    \"Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (arXiv 2509.03647, 2025) — nonlinear bias warning\",\n    \"CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022, 2026) — calibration-aware steering baseline\",\n    \"Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models (Chhikara, TMLR 2025)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025)\",\n    \"Calibrating Verbalized Confidence with Self-Generated Distractors (Wang & Stengel-Eskin, ICLR 2026)\",\n    \"Calibration Across Layers: Understanding Calibration Evolution in LLMs (Joshi et al., EMNLP 2025)\",\n    \"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation (Zhuang et al., arXiv 2512.03082, 2025)\",\n    \"Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv 2505.21772, 2025)\",\n    \"Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection (arXiv 2603.06604, 2026)\",\n    \"Fine-Grained Activation Steering: Steering Less, Achieving More (arXiv 2602.04428, 2026) — atomic-unit-level steering\",\n    \"Contextual Linear Activation Steering of Language Models (arXiv 2604.24693, 2026) — context-adaptive steering strengths\"\n  ],\n  \"description\": \"We propose DBS-v2 (Disentangled Bias Steering), a method that separately identifies, assesses the steerability of, and adaptively corrects two competing sources of LLM miscalibration identified by Kumaran et al. (2026): choice-supportive bias (CSB, inflating confidence in selected answers) and contradictory-evidence overweighting (CEO, causing excessive confidence revision under criticism). Unlike Tsujimura & Tagade (2025), who descriptively decomposed assertiveness into emotion/logic clusters via unsupervised methods on a 1B model without calibration evaluation, DBS-v2 is grounded in causally-identified cognitive biases with theory-driven contrastive stimuli and directly targets calibration metrics.\\n\\nA critical insight motivating this revision is the classification-correction gap demonstrated by Liu (2605.05715): linearly decodable failure directions (71.6% balanced accuracy) can yield Δ≈0 under steering because they overlap 85-88% with task-critical computation. This means that separability (Phase 1A) is necessary but insufficient — we must also assess steerability before committing to an intervention strategy.\\n\\nThe method proceeds in three phases. Phase 1A (Separability Validation) tests whether CSB and CEO produce distinguishable activation signatures using contrastive activation probing, validated via cosine similarity, principal angle analysis, PCA/ICA dimensionality assessment, and cross-prediction ablation (following Miao & Ungar, 2026). Phase 1B (Steerability Assessment) — the key new addition — computes the specificity ratio (mode-specific vs. shared variance with the correct/incorrect subspace) for each identified bias direction, following Liu's shared-specific decomposition methodology. This diagnostic distinguishes between directions that are decodable-and-steerable vs. decodable-but-entangled. We hypothesize that CSB and CEO may have asymmetric specificity profiles, which would explain why monolithic calibration steering yields inconsistent results across settings. The Confidence Manifold study (2602.08159) provides encouraging evidence that correctness-related signals occupy only 3-8 dimensions with simple mean-shift geometry, suggesting calibration-related directions may have more favorable specificity than the medical overthinking phenomenon Liu studied.\\n\\nPhase 2 trains a lightweight per-instance bias dominance classifier whose output determines both which bias is active and which intervention route to apply. Phase 3 implements adaptive routing: (Route A) Spherical Steering for high-specificity directions (≥0.5), with Selective Steering (Dang & Ngo, 2601.19375) as an ablation alternative providing discriminative layer selection; (Route B) a learned non-linear bottleneck residual MLP (d→64→d) for low-specificity directions (<0.2), trained with COAST-informed (Nguyen et al., 2605.01167) collateral-damage-aware loss weighting; (Route C) selective abstention leveraging the decodable signal for reliability estimation when neither linear nor non-linear correction is safe; and (Route D) conservative hybrid steering for intermediate specificity (0.2-0.5).\\n\\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across five models: Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct as primary targets, plus Qwen2.5-3B and Llama-3.2-3B for fair comparison with 'Wired for Overconfidence' baselines. We compare against temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic Spherical Steering (without bias decomposition), and monolithic non-linear MLP (without bias decomposition). The primary contributions are: (1) the first joint separability-and-steerability assessment of competing calibration biases, providing specificity ratio measurements that the field currently lacks; (2) interpretable, bias-specific diagnostics revealing which bias source drives miscalibration per-instance AND whether it is correctable; (3) adaptive intervention routing that gracefully degrades from manifold-preserving rotation to non-linear correction to selective abstention based on measured entanglement; and (4) the hypothesis that CSB and CEO have asymmetric steerability profiles, offering a mechanistic explanation for inconsistent monolithic steering results. Phase 1 results constitute an independent contribution regardless of Phase 2-3 outcomes.\",\n  \"project_name\": \"bias_disentangle_calib\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"round1_issue_1_missing_competitor\": \"Tsujimura & Tagade (2508.17182) cited as closest methodological precedent, differentiated on four axes (theory-driven vs. post-hoc, calibration vs. assertiveness, 5 models vs. 1, causal intervention vs. descriptive). [Carried from R1]\",\n    \"round1_issue_2_model_names\": \"Fixed model names (Gemma 4 31B Dense, Llama-3.1-8B-Instruct, Qwen3-8B). [Carried from R1]\",\n    \"round1_issue_3_untested_assumption\": \"Phase 1A retains all 5 separability tests with quantitative thresholds. [Carried from R1, now labeled Phase 1A]\",\n    \"round1_issue_4_steering_reliability\": \"Spherical Steering retained as primary Route A intervention; now augmented with Route B non-linear fallback and Route C abstention for when even rotation fails. [Extended from R1]\",\n    \"round1_issue_5_baseline_comparison\": \"Contribution framing around interpretability, difficulty-stratification, and robustness retained. Added monolithic non-linear MLP as new baseline. [Extended from R1]\",\n    \"round1_issue_6_behavioral_mechanistic_leap\": \"Phase 1A tests separability; Phase 1B now ALSO tests steerability. [Extended from R1]\",\n    \"round2_issue_1_critical_missing_competitor\": \"Liu (2605.05715) now thoroughly integrated as a foundational reference rather than treated as merely a competitor. The classification-correction gap is incorporated into the core problem framing, opportunity statement, and landscape. The specificity ratio is adopted as a pre-intervention diagnostic in Phase 1B. The non-linear MLP finding (Δ=+2.8pp) motivates Route B. The selective abstention finding (AUROC 0.610) motivates Route C. We differentiate from Liu by (a) studying calibration biases rather than medical overthinking, (b) testing multiple competing directions rather than a single failure mode, (c) hypothesizing asymmetric steerability profiles, and (d) providing the Confidence Manifold evidence (2602.08159) that calibration-related directions may have more favorable geometry.\",\n    \"round2_issue_2_separability_steerability_gap\": \"Phase 1 now has two explicit sub-phases: 1A (separability, carried from R1) and 1B (steerability, NEW). Phase 1B computes specificity ratio, within-class variance analysis, LEACE concept erasure, and cross-architecture stability for each bias direction. Quantitative thresholds established: ≥0.5 HIGH, 0.2-0.5 MEDIUM, <0.2 LOW. The separability≠steerability distinction is elevated to a core theme of the paper, discussed in the core_problem, opportunity, and approach.\",\n    \"round2_issue_3_minor_missing_references\": \"Selective Steering (Dang & Ngo, 2601.19375) now cited in landscape and used as Route A ablation alternative. COAST (Nguyen et al., 2605.01167) cited in landscape and used for collateral-damage-aware training in Route B. Additionally cited: Confidence Manifold (2602.08159), AUSteer (2602.04428), CLAS (2604.24693) in landscape for completeness.\",\n    \"round2_issue_4_nonlinear_steering_fallback\": \"Route B (learned non-linear residual MLP) added as Phase 3 intervention for low-specificity directions, directly motivated by Liu's finding that a 4096→64→4096 bottleneck achieves Δ=+2.8pp where 29 linear methods fail. Route C (selective abstention) added as ultimate fallback. Route D (conservative hybrid) added for intermediate specificity. This creates a principled four-tier intervention hierarchy that degrades gracefully based on measured entanglement rather than assuming all directions are equally steerable.\"\n  }\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"MISSING CRITICAL COMPETITOR: Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) 'LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components' already decomposes overconfidence-related behavior into two orthogonal sub-components in the residual stream using difference-in-means, with distinct steering effects. This is methodologically very similar to DBS and must be cited and explicitly distinguished.\", \"MODEL NAMING ERRORS: 'Gemma 4 27B' does not exist — Gemma 4 ships as E2B, E4B, 26B-A4B (MoE), and 31B (Dense). 'Llama-3.3-8B-Instruct' has no confirmed official release — Llama 3.3 was released only as 70B; the 8B variant in the Llama 3 family is Llama-3.1-8B-Instruct.\", \"UNTESTED CORE ASSUMPTION: The entire approach rests on CSB and CEO being linearly separable in the residual stream, but Kumaran et al.'s analysis is purely behavioral (Gemma 3, GPT-4o, o1-preview) with no mechanistic evidence. 'Breaking the Mirror' found that even a simpler bias (self-preference) 'spans multiple or nonlinear directions,' challenging the linear orthogonality assumption.\", \"ACTIVATION STEERING RELIABILITY: Recent work 'Steered LLM Activations are Non-Surjective' (2604.09839) formally proves steering pushes activations off the natural prompt-reachable manifold, and 'A Sober Look at Steering Vectors' notes many behaviors are unsteerable even when sweeping layers and strengths.\", \"BASELINE COMPARISON CHALLENGE: The 96.5% ECE reduction target from 'Wired for Overconfidence' was achieved on 3B models (Qwen2.5-3B, Llama-3.2-3B) on PopQA specifically; the proposal tests 8B-31B models where circuit structure may differ substantially. Direct comparison claims need qualification.\", \"BEHAVIORAL-TO-MECHANISTIC LEAP: The proposal assumes behavioral-level biases (identified via confidence elicitation experiments) will have clean mechanistic signatures in hidden states. This is a significant empirical assumption that the paper should explicitly acknowledge and test for.\"]\nFeedback: The idea is well-motivated and the gap is real, but needs several revisions: (1) Cite and distinguish from Tsujimura & Tagade (2508.17182) — their orthogonal decomposition of assertiveness is the closest methodological precedent. Argue why CSB/CEO decomposition is more principled than emotional/logical. (2) Fix model names: use Gemma 4 31B (dense) or 26B-A4B (MoE), and Llama-3.1-8B-Instruct instead of the non-existent variants. (3) Add an explicit 'assumption validation' experiment phase: before the full DBS pipeline, verify that CSB and CEO produce distinguishable activation signatures. Consider ablating with PCA/ICA to test whether two directions suffice. (4) Temper claims about outperforming monolithic steering — frame the contribution more around interpretability and difficulty-stratified improvement rather than raw ECE numbers. (5) Acknowledge and address the non-surjectivity concern — discuss why targeted dampening of bias directions may be more robust than general steering, or include experiments that validate steered states remain on-manifold. (6) Consider adding a fallback: if CSB and CEO are not orthogonally separable, can you still improve calibration via a non-orthogonal decomposition or a multi-direction approach?\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING COMPETITOR: 'Decodable but Not Corrected by Fixed Residual-Stream Linear Steering' (arXiv 2605.05715, May 2026) demonstrates a classification-correction gap where linearly decodable directions (71.6% balanced accuracy) yield Δ≈0 under steering because the failure directions have 85-88% overlap with task-critical computation (specificity ratio ≤0.152). This directly threatens DBS-v2's Phase 3: even if CSB/CEO are decodable (Phase 1 succeeds), steering may fail due to entanglement. The paper proposes specificity ratio as a pre-intervention diagnostic — DBS-v2 must incorporate this.\", \"SEPARABILITY ≠ STEERABILITY GAP: Phase 1 validates whether CSB and CEO are separable (cosine similarity, PCA/ICA, cross-prediction ablation) but does NOT test whether identified directions are steerable without collateral damage. The 'Decodable but Not Corrected' paper shows these are empirically distinct questions. Phase 1 needs a steerability diagnostic: compute the specificity ratio (shared vs. mode-specific variance) of CSB/CEO directions relative to the overall correct-vs-incorrect subspace.\", \"MINOR MISSING REFERENCES: (a) 'Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection' (arXiv 2601.19375, Jan 2026) — another norm-preserving rotation method predating Spherical Steering, with discriminative layer selection. (b) 'Minimizing Collateral Damage in Activation Steering' (arXiv 2605.01167, May 2026) — formalizes collateral damage from steering interventions and proposes minimum-damage solutions, directly relevant to the manifold-preservation rationale.\", \"NO NON-LINEAR STEERING FALLBACK: The proposal's fallback (SAE-based features) addresses the case where CSB/CEO are not linearly separable, but not the case where they are separable but not linearly steerable. The 'Decodable but Not Corrected' paper shows a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods yield Δ≈0. Phase 3 should include a non-linear steering fallback (e.g., learned MLP correction) alongside Spherical Steering.\"]\nFeedback: The revision from round 1 is excellent — all prior issues were addressed thoroughly and honestly. The main new concern is a very recent paper (2605.05715, this month) that identifies a 'classification-correction gap': failure directions can be linearly decodable but not steerable because they overlap heavily with task-critical computation. This is distinct from the off-manifold concern already addressed via Spherical Steering. Concrete fixes: (1) Add a 'steerability diagnostic' to Phase 1 — after extracting CSB/CEO directions, compute their specificity ratio (proportion of mode-specific vs. shared variance with the correct/incorrect subspace). If specificity is low (<0.2), flag high entanglement risk. (2) Add a non-linear steering fallback in Phase 3: when specificity is low, use a learned non-linear residual correction (small MLP) instead of fixed-direction rotation. (3) Cite Selective Steering and Minimizing Collateral Damage as part of the geometry-aware steering landscape. (4) Explicitly discuss the separation between 'decodable' and 'steerable' in the approach section — this strengthens the paper's contribution by showing awareness of a subtle and important distinction.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"...\"}\n  },\n  \"issues\": [\"specific issue 1\", ...],\n  \"feedback\": \"Actionable feedback (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold\n- \"fail\": fundamental flaw (gap doesn't exist, approach provably wrong)\n- Threshold is HIGH (4.0/5.0): only truly outstanding ideas should pass.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-19T13:14:07.980Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T13:14:07.980Z",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

## Round 1

148 recorded events

### User

_source line 3 · 2026-05-19T13:14:07.995Z_

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
  "title": "Disentangling Competing Calibration Biases via Geometry-Aware Activation Steering",
  "core_problem": "LLM miscalibration arises from at least two competing biases — choice-supportive bias (inflating confidence in initial answers) and contradictory-evidence overweighting (causing excessive confidence revision under criticism) — that require opposing corrections. Existing calibration methods apply uniform corrections that cannot simultaneously address biases pulling confidence in opposite directions. Recent work (Liu, 2605.05715) further reveals a classification-correction gap: failure-mode directions that are linearly decodable may not be linearly steerable due to entanglement with task-critical computation (specificity ratio ≤0.152). This means even if competing biases can be identified in activations, correcting them requires knowing not just WHICH bias dominates but WHETHER each bias direction is steerable — and routing to appropriate interventions (linear rotation, non-linear correction, or selective abstention) accordingly. Can we jointly diagnose per-instance bias dominance AND steerability to apply targeted, manifold-preserving corrections where possible and graceful degradation where not?",
  "opportunity": "Kumaran et al. (Nature Machine Intelligence, 2026; arXiv 2507.03120) identified that LLM miscalibration results from two mechanistically distinct behavioral biases in Gemma 3, GPT-4o, and o1-preview: choice-supportive bias inflates confidence in selected answers, while contradictory-advice overweighting causes models to over-react to opposing evidence. Miao & Ungar (arXiv 2603.25052, 2026) independently showed that calibration and verbalized confidence signals are encoded linearly but orthogonally in the residual stream across three 7-8B models, establishing that confidence-related constructs have accessible geometric structure. Liu (arXiv 2605.05715, May 2026) demonstrated a critical classification-correction gap: linearly decodable failure directions (71.6% balanced accuracy) yield Δ≈0 under 29 steering configurations because the failure directions have 85-88% overlap with task-critical computation (specificity ratio ≤0.152) — but crucially, the paper also shows that (a) a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods fail, and (b) the decodable signal still supports selective abstention (AUROC 0.610, outperforming 5 uncertainty baselines). The 'Confidence Manifold' study (arXiv 2602.08159) found correctness signals occupy only 3-8 dimensions with simple mean-shift geometry across 9 models, suggesting that for calibration-related directions, the geometric structure may be more favorable than for the medical overthinking phenomenon Liu studied. The convergence of (a) identified competing biases, (b) linear confidence encoding evidence, (c) the decodable-steerable distinction with quantitative diagnostics, and (d) both norm-preserving rotation (Spherical Steering, ICML 2026) and collateral-damage-aware optimization (COAST, 2605.01167) creates an opportunity for a principled pipeline: diagnose bias identity, assess steerability, and route to the appropriate intervention.",
  "landscape": "Kumaran et al. (Nature MI, 2026) identified competing biases (CSB and CEO) via behavioral experiments on Gemma 3, GPT-4o, and o1-preview but proposed no correction framework and provided no mechanistic (activation-level) evidence. Miao & Ungar (arXiv 2603.25052, 2026) demonstrated that calibration accuracy and verbalized confidence are linearly encoded but orthogonal in 7-8B models (cosine similarity <0.04 across layers), and introduced adaptive steering achieving 4-7× ECE improvement — but they target the confidence-accuracy misalignment gap, not the competing bias structure. Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) decomposed LLM assertiveness into emotional and logical sub-components via unsupervised clustering on Llama-3.2-1B-Instruct (645 samples), finding two clusters in high-assertive representations — methodologically adjacent but critically different: their decomposition is descriptive (post-hoc ChatGPT-labeled clusters of communication style) rather than causally grounded in identified cognitive biases, uses a single 1B model, reports no calibration metrics, and addresses assertiveness rather than calibration. The 'Wired for Overconfidence' paper (2604.01457, April 2026) identifies overconfidence circuits in Qwen2.5-3B and Llama-3.2-3B, achieving 96.9% ECE reduction on PopQA via monolithic activation steering, but only tests 3B models and treats overconfidence as a single phenomenon. Liu (arXiv 2605.05715, May 2026) is the most directly relevant recent advance: the paper demonstrates a classification-correction gap where linearly decodable failure directions (71.6% balanced accuracy on Llama-3.1-8B) yield Δ≈0 across five families of linear steering (29 configurations) because the failure direction has 85-88% overlap with task-critical computation (specificity ratio ≤0.152). Three convergent evidence lines confirm entanglement: low specificity, shared-direction steering damages accuracy (-12.1pp), and LEACE concept erasure damages accuracy (-3.6pp). Crucially, a learned non-linear bottleneck MLP (4096→64→4096) achieves Δ=+2.8pp (p=0.025) where linear methods fail, though with 8.2% damage rate — demonstrating that partial disentanglement is possible via non-linear transforms. The paper proposes the specificity ratio as a pre-intervention diagnostic and recommends selective abstention (AUROC 0.610) when steering fails. However, this was studied for medical overthinking, a single failure mode; whether calibration biases (CSB/CEO) exhibit similar or different entanglement profiles is an open question. Ji et al. (EMNLP 2025) modulates a single Verbal Uncertainty Feature direction, reducing hallucinations by ~30%, capturing only the net effect of competing biases. Joshi et al. (EMNLP 2025) found a single calibration direction but did not decompose it. CORAL (arXiv 2602.06022, Feb 2026) achieves 49% ECE improvement via correctness-subspace probing on 7B models but uses a single MLP probe direction. The 'Confidence Manifold' study (arXiv 2602.08159, Feb 2026) found correctness signals occupy 3-8 dimensions with simple mean-shift geometry across 9 models from 5 families, and causally validated via steering (10.9pp error rate change) — importantly, the low dimensionality and linear separability of correctness signals contrasts with Liu's high-entanglement finding for overthinking, suggesting calibration-related directions may have more favorable specificity profiles. Wang & Stengel-Eskin (ICLR 2026) introduced DINCO to normalize suggestibility bias via self-generated distractors at the output level. Zhuang et al. (arXiv 2025) proposed RDG to alleviate choice-supportive bias through fine-tuning but did not address CEO. CCPS (arXiv 2025) achieves ~55% ECE reduction via representation stability probing on MMLU. 'Breaking the Mirror' (arXiv 2509.03647) found that self-preference bias 'spans multiple or nonlinear directions,' achieving 97% unjustified bias reduction but with instability on legitimate cases — a direct warning that some biases may not be linearly separable. On the steering methodology side, the landscape has rapidly matured: Spherical Steering (arXiv 2602.08169, ICML 2026) performs norm-preserving geodesic rotation, outperforming addition-based baselines by +10% on TruthfulQA while maintaining generation quality. Selective Steering (Dang & Ngo, arXiv 2601.19375, Jan 2026) independently developed norm-preserving rotation with discriminative layer selection — applying steering only where feature representations exhibit opposite-signed class alignment, achieving 5.5× higher attack success rates with zero perplexity violations across 8 models from 3 families (Llama, Qwen, Gemma). COAST (Nguyen et al., arXiv 2605.01167, May 2026) formalizes collateral damage from steering interventions as unintended alignment changes along non-target feature directions, models steering as a constrained optimization minimizing expected squared collateral change weighted by the empirical second-moment matrix of activations, achieving up to 30% improvement over Angular Steering with strong negative correlation (r<-0.9) between collateral damage and accuracy loss across six benchmarks. AUSteer (arXiv 2602.04428, Feb 2026) decomposes block activations into fine-grained atomic units, steering fewer activations more precisely. CLAS (arXiv 2604.24693, Apr 2026) dynamically adapts steering strengths per-context across 11 benchmarks and 4 model families. 'Steered LLM Activations are Non-Surjective' (2604.09839, April 2026) formally proved that additive steering pushes activations off-manifold; 'A Sober Look at Steering Vectors' (NeurIPS 2024) showed many behaviors are unsteerable. No existing method jointly diagnoses which calibration bias dominates, assesses the steerability of each bias direction (via specificity ratio or equivalent), and routes to bias-specific interventions that range from manifold-preserving rotation to learned non-linear correction to selective abstention — yet the competing effects of CSB and CEO on calibration, combined with the now-established decodable-steerable gap, mean that both uniform correction AND uniform intervention strategy are fundamentally suboptimal.",
  "inspired_by": "Gap: Competing biases create non-uniform miscalibration patterns that single-direction methods cannot fix (Kumaran et al. 2026), while the classification-correction gap (Liu, 2605.05715) shows that decodable directions are not necessarily steerable — meaning Phase 1's separability validation is necessary but insufficient. Pattern: Theory-driven contrastive probing (Miao & Ungar 2026) + steerability diagnostics (specificity ratio, Liu 2026) + adaptive intervention routing (geometry-aware rotation for steerable directions, learned non-linear correction for entangled directions). Untried combination: Cognitive-bias-grounded contrastive stimuli → per-instance bias diagnosis → specificity-informed intervention routing (Spherical Steering / non-linear MLP / selective abstention), with the hypothesis that CSB and CEO may have asymmetric steerability profiles — which would explain why monolithic steering sometimes succeeds and sometimes fails at calibration correction.",
  "approach": "We design DBS-v2 (Disentangled Bias Steering) in three phases, now incorporating the critical distinction between decodability and steerability identified by Liu (2605.05715).\n\n**Phase 1 — Assumption Validation & Steerability Assessment (Weeks 1-5):** This phase tests TWO assumptions, not one: (A) that CSB and CEO produce distinguishable activation signatures, and (B) that identified directions are steerable without catastrophic collateral damage.\n\n*Phase 1A — Separability (Weeks 1-3):* We construct two contrastive stimulus sets: for CSB, we compare hidden states when the model reviews its own prior answer vs. a fresh unattributed answer (eliciting choice-supportive inflation); for CEO, we compare states when contradictory expert advice is present vs. absent (eliciting evidence overweighting). Using difference-in-means on these contrastive pairs, we extract candidate bias directions in the residual stream. We validate separability via: (a) cosine similarity between candidate directions, (b) principal angle analysis between CSB and CEO subspaces using the methodology of Miao & Ungar (2026), (c) PCA to assess whether 2 directions capture sufficient variance vs. requiring higher-dimensional subspaces, (d) ICA to test whether statistically independent (not just orthogonal) components emerge, and (e) cross-prediction ablations to confirm removing one bias subspace does not collapse the other. If CSB and CEO directions show cosine similarity >0.3 or shared variance >15%, we activate the separability fallback: extracting a multi-direction bias subspace via SAE-derived features and training a subspace projection classifier.\n\n*Phase 1B — Steerability Diagnostics (Weeks 3-5):* This is a critical addition motivated by Liu (2605.05715). Even if CSB and CEO are separable (Phase 1A succeeds), steering along identified directions may fail if those directions are entangled with task-critical computation. For each identified bias direction, we compute: (a) the **specificity ratio** — the proportion of mode-specific variance vs. shared variance with the correct-vs-incorrect subspace, following Liu's shared-specific decomposition methodology. Concretely, we extract the correctness subspace (correct vs. incorrect answer centroids), then decompose each bias direction into a component within this subspace (shared) and a component orthogonal to it (mode-specific). The specificity ratio = ||mode-specific||² / ||total||². (b) **Within-class variance analysis** — comparing within-class variance to inter-centroid gap for each bias direction (Liu's second diagnostic). (c) **LEACE concept erasure test** — applying concept erasure to each bias direction and measuring accuracy damage as causal evidence of entanglement. (d) **Cross-architecture stability** — verifying specificity ratios are consistent across model families.\n\nWe establish quantitative thresholds informed by Liu's findings: specificity ratio ≥0.5 → HIGH steerability (linear rotation expected to work); 0.2-0.5 → MEDIUM (rotation may partially work, monitor collateral damage); <0.2 → LOW (linear steering unlikely to succeed, route to non-linear intervention). These thresholds are calibrated against Liu's findings where specificity ≤0.152 yielded Δ≈0 for linear steering while ≥0.999 succeeded for refusal steering. Crucially, we hypothesize that CSB and CEO may have ASYMMETRIC specificity profiles — one may be more steerable than the other — which would provide a mechanistic explanation for why monolithic calibration steering sometimes succeeds partially.\n\nPhase 1 results constitute an independent contribution: the first joint separability-and-steerability assessment of behaviorally-identified competing biases, providing the field's first specificity ratio measurements for calibration-related bias directions.\n\n**Phase 2 — Per-Instance Bias Diagnosis (Weeks 4-8):** A lightweight logistic probe (or, in the fallback case, a small MLP) trained on per-instance projection magnitudes onto each bias direction classifies which bias dominates for a given query. We stratify by difficulty: on easy questions where models are already confident, CSB likely dominates; on hard questions under criticism, CEO likely dominates. The probe output provides a continuous dominance score. NEW: The Phase 1B steerability assessment informs a per-direction intervention routing table, so the probe's output determines not only which bias is active but which intervention to apply.\n\n**Phase 3 — Adaptive Geometry-Aware Intervention (Weeks 6-14):** Instead of a single intervention strategy, Phase 3 now implements an adaptive routing pipeline informed by Phase 1B's steerability diagnostics:\n\n*Route A — Spherical Steering (for HIGH-specificity directions):* When a bias direction has specificity ratio ≥0.5, we adopt Spherical Steering (You et al., ICML 2026) as the primary intervention: rotating activations along a geodesic away from the dominant bias direction while preserving activation norms. This addresses the off-manifold concern (Mishra et al., 2604.09839) while the high specificity ensures minimal collateral damage to task-critical computation. A confidence gate modulates rotation magnitude based on the probe's dominance score. We note that Selective Steering (Dang & Ngo, 2601.19375) provides an alternative norm-preserving formulation with discriminative layer selection; we ablate both to determine which is more effective for calibration-specific interventions.\n\n*Route B — Learned Non-Linear Residual Correction (for LOW-specificity directions):* When a bias direction has specificity ratio <0.2, linear steering of any kind (additive, rotational, or projected) is expected to fail due to entanglement with task-critical computation (Liu, 2605.05715). Following Liu's finding that a bottleneck residual MLP (d→64→d) achieves Δ=+2.8pp where all 29 linear configurations yield Δ≈0, we train a small non-linear residual adapter per bias type. The adapter takes the hidden state as input and outputs a residual correction, trained via supervision on (biased state, corrected state) pairs extracted from the contrastive dataset. We incorporate the COAST framework (Nguyen et al., 2605.01167) by weighting the training loss by the empirical second-moment matrix to minimize expected collateral damage along non-target feature directions. The adapter's bottleneck architecture (d→64→d, <0.1% of model parameters) keeps the intervention lightweight and inference-efficient.\n\n*Route C — Selective Abstention (for UNSTEERABLE directions):* When Phase 1B indicates low specificity AND Phase 3 ablations confirm that neither Route A nor Route B improves calibration without excessive damage (>5% accuracy degradation), we leverage the decodable signal for selective abstention: the bias probe flags instances where the dominant bias has high activation but low steerability, outputting a reliability score. Following Liu's demonstration that decodable signals support post-generation reliability estimation (AUROC 0.610) even when correction fails, this provides a graceful degradation path.\n\n*Route D — Medium-Specificity Hybrid (for intermediate cases):* For directions with specificity 0.2-0.5, we apply Spherical Steering with conservative rotation magnitude (capped at 50% of the high-specificity coefficient) and monitor collateral damage via the COAST second-moment diagnostic. If per-instance collateral damage exceeds a threshold, we fall back to Route B for that instance.\n\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct. We additionally include Qwen2.5-3B and Llama-3.2-3B as supplementary models to enable fair comparison with 'Wired for Overconfidence' results at the same scale. Metrics: ECE, Brier score, AUROC, difficulty-stratified ECE (easy/medium/hard partitions), AND NEW: per-direction specificity ratios, collateral damage measurements (accuracy on non-target tasks before/after steering), and route-distribution analysis (what fraction of instances are routed to each intervention). Baselines: temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic circuit ablation (Wired for Overconfidence replication at 3B scale), monolithic Spherical Steering (single direction, no bias decomposition), and NEW: monolithic non-linear residual MLP (single direction, no bias decomposition) to isolate the contribution of bias decomposition from the contribution of non-linear correction.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "750-1050 H100",
      "timeline": "16-20 weeks",
      "estimated_gpu_cost": "$1,875-$2,625 (H100 @ ~$2.50/hr mid-tier provider)"
    },
    "human_in_loop": {
      "gpu_hours": "650-900 H100",
      "timeline": "12-15 weeks",
      "claude_api_cost": "$350-$600 (Sonnet 4.6 for contrastive dataset generation, probing code, specificity ratio computation scripts, non-linear adapter training, analysis)",
      "estimated_gpu_cost": "$1,625-$2,250"
    },
    "auto_research": {
      "gpu_hours": "1000-1400 H100",
      "timeline": "6-10 weeks",
      "claude_api_cost": "$800-$1,400 (Opus 4.7 for experiment orchestration, assumption validation analysis, steerability diagnostics, adapter training sweeps, ablation design)",
      "estimated_gpu_cost": "$2,500-$3,500",
      "speed_bottleneck": "Phase 1A→1B is inherently sequential (separability must be established before steerability diagnostics are meaningful). Phase 1B requires extracting the correctness subspace and computing specificity ratios per-direction per-model, which is parallelizable across models but adds ~2 weeks over original timeline. Route B adapter training requires supervision pairs from Phase 1 contrastive data. Steering coefficient search across 5 models × 4 datasets × 3-4 intervention routes generates large evaluation matrices. Fair replication of 'Wired for Overconfidence' baselines on 3B models adds overhead."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target, tight but feasible with aggressive Phase 1 timeline)",
    "ARR August 2026 cycle (Aug 3, 2026 — targets EMNLP 2027 or future *CL venues)",
    "NeurIPS 2026 Workshops (~Aug 29, 2026 — workshop paper track for Phase 1 separability + steerability results)",
    "AACL-IJCNLP 2026 (ARR May 25 commitment deadline Aug 26, 2026 — if Phase 1 completes early)",
    "ICLR 2027 (expected Oct 2026 deadline — full paper with all phases and routes complete)"
  ],
  "level": "top-tier",
  "key_references": [
    "Competing Biases underlie Overconfidence and Underconfidence in LLMs (Kumaran et al., Nature Machine Intelligence 2026; arXiv 2507.03120)",
    "Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, arXiv 2603.25052, 2026) — orthogonal calibration/confidence encoding, adaptive steering",
    "LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components (Tsujimura & Tagade, arXiv 2508.17182, 2025) — closest methodological precedent",
    "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes (Liu, arXiv 2605.05715, May 2026) — classification-correction gap, specificity ratio diagnostic",
    "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs (arXiv 2604.01457, 2026)",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., ICML 2026; arXiv 2602.08169)",
    "Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection (Dang & Ngo, arXiv 2601.19375, Jan 2026) — independent norm-preserving rotation with discriminative layer selection",
    "Minimizing Collateral Damage in Activation Steering (Nguyen et al., arXiv 2605.01167, May 2026) — COAST framework, collateral damage formalization, second-moment optimization",
    "Steered LLM Activations are Non-Surjective (Mishra et al., arXiv 2604.09839, 2026)",
    "A Sober Look at Steering Vectors for LLMs (Tan et al., NeurIPS 2024)",
    "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models (arXiv 2602.08159, 2026) — 3-8 dimensional correctness signals, linear separability across 9 models",
    "Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (arXiv 2509.03647, 2025) — nonlinear bias warning",
    "CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022, 2026) — calibration-aware steering baseline",
    "Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models (Chhikara, TMLR 2025)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025)",
    "Calibrating Verbalized Confidence with Self-Generated Distractors (Wang & Stengel-Eskin, ICLR 2026)",
    "Calibration Across Layers: Understanding Calibration Evolution in LLMs (Joshi et al., EMNLP 2025)",
    "Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation (Zhuang et al., arXiv 2512.03082, 2025)",
    "Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv 2505.21772, 2025)",
    "Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection (arXiv 2603.06604, 2026)",
    "Fine-Grained Activation Steering: Steering Less, Achieving More (arXiv 2602.04428, 2026) — atomic-unit-level steering",
    "Contextual Linear Activation Steering of Language Models (arXiv 2604.24693, 2026) — context-adaptive steering strengths"
  ],
  "description": "We propose DBS-v2 (Disentangled Bias Steering), a method that separately identifies, assesses the steerability of, and adaptively corrects two competing sources of LLM miscalibration identified by Kumaran et al. (2026): choice-supportive bias (CSB, inflating confidence in selected answers) and contradictory-evidence overweighting (CEO, causing excessive confidence revision under criticism). Unlike Tsujimura & Tagade (2025), who descriptively decomposed assertiveness into emotion/logic clusters via unsupervised methods on a 1B model without calibration evaluation, DBS-v2 is grounded in causally-identified cognitive biases with theory-driven contrastive stimuli and directly targets calibration metrics.\n\nA critical insight motivating this revision is the classification-correction gap demonstrated by Liu (2605.05715): linearly decodable failure directions (71.6% balanced accuracy) can yield Δ≈0 under steering because they overlap 85-88% with task-critical computation. This means that separability (Phase 1A) is necessary but insufficient — we must also assess steerability before committing to an intervention strategy.\n\nThe method proceeds in three phases. Phase 1A (Separability Validation) tests whether CSB and CEO produce distinguishable activation signatures using contrastive activation probing, validated via cosine similarity, principal angle analysis, PCA/ICA dimensionality assessment, and cross-prediction ablation (following Miao & Ungar, 2026). Phase 1B (Steerability Assessment) — the key new addition — computes the specificity ratio (mode-specific vs. shared variance with the correct/incorrect subspace) for each identified bias direction, following Liu's shared-specific decomposition methodology. This diagnostic distinguishes between directions that are decodable-and-steerable vs. decodable-but-entangled. We hypothesize that CSB and CEO may have asymmetric specificity profiles, which would explain why monolithic calibration steering yields inconsistent results across settings. The Confidence Manifold study (2602.08159) provides encouraging evidence that correctness-related signals occupy only 3-8 dimensions with simple mean-shift geometry, suggesting calibration-related directions may have more favorable specificity than the medical overthinking phenomenon Liu studied.\n\nPhase 2 trains a lightweight per-instance bias dominance classifier whose output determines both which bias is active and which intervention route to apply. Phase 3 implements adaptive routing: (Route A) Spherical Steering for high-specificity directions (≥0.5), with Selective Steering (Dang & Ngo, 2601.19375) as an ablation alternative providing discriminative layer selection; (Route B) a learned non-linear bottleneck residual MLP (d→64→d) for low-specificity directions (<0.2), trained with COAST-informed (Nguyen et al., 2605.01167) collateral-damage-aware loss weighting; (Route C) selective abstention leveraging the decodable signal for reliability estimation when neither linear nor non-linear correction is safe; and (Route D) conservative hybrid steering for intermediate specificity (0.2-0.5).\n\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across five models: Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct as primary targets, plus Qwen2.5-3B and Llama-3.2-3B for fair comparison with 'Wired for Overconfidence' baselines. We compare against temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic Spherical Steering (without bias decomposition), and monolithic non-linear MLP (without bias decomposition). The primary contributions are: (1) the first joint separability-and-steerability assessment of competing calibration biases, providing specificity ratio measurements that the field currently lacks; (2) interpretable, bias-specific diagnostics revealing which bias source drives miscalibration per-instance AND whether it is correctable; (3) adaptive intervention routing that gracefully degrades from manifold-preserving rotation to non-linear correction to selective abstention based on measured entanglement; and (4) the hypothesis that CSB and CEO have asymmetric steerability profiles, offering a mechanistic explanation for inconsistent monolithic steering results. Phase 1 results constitute an independent contribution regardless of Phase 2-3 outcomes.",
  "project_name": "bias_disentangle_calib",
  "source": "web_research",
  "revision_notes": {
    "round1_issue_1_missing_competitor": "Tsujimura & Tagade (2508.17182) cited as closest methodological precedent, differentiated on four axes (theory-driven vs. post-hoc, calibration vs. assertiveness, 5 models vs. 1, causal intervention vs. descriptive). [Carried from R1]",
    "round1_issue_2_model_names": "Fixed model names (Gemma 4 31B Dense, Llama-3.1-8B-Instruct, Qwen3-8B). [Carried from R1]",
    "round1_issue_3_untested_assumption": "Phase 1A retains all 5 separability tests with quantitative thresholds. [Carried from R1, now labeled Phase 1A]",
    "round1_issue_4_steering_reliability": "Spherical Steering retained as primary Route A intervention; now augmented with Route B non-linear fallback and Route C abstention for when even rotation fails. [Extended from R1]",
    "round1_issue_5_baseline_comparison": "Contribution framing around interpretability, difficulty-stratification, and robustness retained. Added monolithic non-linear MLP as new baseline. [Extended from R1]",
    "round1_issue_6_behavioral_mechanistic_leap": "Phase 1A tests separability; Phase 1B now ALSO tests steerability. [Extended from R1]",
    "round2_issue_1_critical_missing_competitor": "Liu (2605.05715) now thoroughly integrated as a foundational reference rather than treated as merely a competitor. The classification-correction gap is incorporated into the core problem framing, opportunity statement, and landscape. The specificity ratio is adopted as a pre-intervention diagnostic in Phase 1B. The non-linear MLP finding (Δ=+2.8pp) motivates Route B. The selective abstention finding (AUROC 0.610) motivates Route C. We differentiate from Liu by (a) studying calibration biases rather than medical overthinking, (b) testing multiple competing directions rather than a single failure mode, (c) hypothesizing asymmetric steerability profiles, and (d) providing the Confidence Manifold evidence (2602.08159) that calibration-related directions may have more favorable geometry.",
    "round2_issue_2_separability_steerability_gap": "Phase 1 now has two explicit sub-phases: 1A (separability, carried from R1) and 1B (steerability, NEW). Phase 1B computes specificity ratio, within-class variance analysis, LEACE concept erasure, and cross-architecture stability for each bias direction. Quantitative thresholds established: ≥0.5 HIGH, 0.2-0.5 MEDIUM, <0.2 LOW. The separability≠steerability distinction is elevated to a core theme of the paper, discussed in the core_problem, opportunity, and approach.",
    "round2_issue_3_minor_missing_references": "Selective Steering (Dang & Ngo, 2601.19375) now cited in landscape and used as Route A ablation alternative. COAST (Nguyen et al., 2605.01167) cited in landscape and used for collateral-damage-aware training in Route B. Additionally cited: Confidence Manifold (2602.08159), AUSteer (2602.04428), CLAS (2604.24693) in landscape for completeness.",
    "round2_issue_4_nonlinear_steering_fallback": "Route B (learned non-linear residual MLP) added as Phase 3 intervention for low-specificity directions, directly motivated by Liu's finding that a 4096→64→4096 bottleneck achieves Δ=+2.8pp where 29 linear methods fail. Route C (selective abstention) added as ultimate fallback. Route D (conservative hybrid) added for intermediate specificity. This creates a principled four-tier intervention hierarchy that degrades gracefully based on measured entanglement rather than assuming all directions are equally steerable."
  }
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["MISSING CRITICAL COMPETITOR: Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) 'LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components' already decomposes overconfidence-related behavior into two orthogonal sub-components in the residual stream using difference-in-means, with distinct steering effects. This is methodologically very similar to DBS and must be cited and explicitly distinguished.", "MODEL NAMING ERRORS: 'Gemma 4 27B' does not exist — Gemma 4 ships as E2B, E4B, 26B-A4B (MoE), and 31B (Dense). 'Llama-3.3-8B-Instruct' has no confirmed official release — Llama 3.3 was released only as 70B; the 8B variant in the Llama 3 family is Llama-3.1-8B-Instruct.", "UNTESTED CORE ASSUMPTION: The entire approach rests on CSB and CEO being linearly separable in the residual stream, but Kumaran et al.'s analysis is purely behavioral (Gemma 3, GPT-4o, o1-preview) with no mechanistic evidence. 'Breaking the Mirror' found that even a simpler bias (self-preference) 'spans multiple or nonlinear directions,' challenging the linear orthogonality assumption.", "ACTIVATION STEERING RELIABILITY: Recent work 'Steered LLM Activations are Non-Surjective' (2604.09839) formally proves steering pushes activations off the natural prompt-reachable manifold, and 'A Sober Look at Steering Vectors' notes many behaviors are unsteerable even when sweeping layers and strengths.", "BASELINE COMPARISON CHALLENGE: The 96.5% ECE reduction target from 'Wired for Overconfidence' was achieved on 3B models (Qwen2.5-3B, Llama-3.2-3B) on PopQA specifically; the proposal tests 8B-31B models where circuit structure may differ substantially. Direct comparison claims need qualification.", "BEHAVIORAL-TO-MECHANISTIC LEAP: The proposal assumes behavioral-level biases (identified via confidence elicitation experiments) will have clean mechanistic signatures in hidden states. This is a significant empirical assumption that the paper should explicitly acknowledge and test for."]
Feedback: The idea is well-motivated and the gap is real, but needs several revisions: (1) Cite and distinguish from Tsujimura & Tagade (2508.17182) — their orthogonal decomposition of assertiveness is the closest methodological precedent. Argue why CSB/CEO decomposition is more principled than emotional/logical. (2) Fix model names: use Gemma 4 31B (dense) or 26B-A4B (MoE), and Llama-3.1-8B-Instruct instead of the non-existent variants. (3) Add an explicit 'assumption validation' experiment phase: before the full DBS pipeline, verify that CSB and CEO produce distinguishable activation signatures. Consider ablating with PCA/ICA to test whether two directions suffice. (4) Temper claims about outperforming monolithic steering — frame the contribution more around interpretability and difficulty-stratified improvement rather than raw ECE numbers. (5) Acknowledge and address the non-surjectivity concern — discuss why targeted dampening of bias directions may be more robust than general steering, or include experiments that validate steered states remain on-manifold. (6) Consider adding a fallback: if CSB and CEO are not orthogonally separable, can you still improve calibration via a non-orthogonal decomposition or a multi-direction approach?

### Round 2 review
Verdict: revise
Issues: ["CRITICAL MISSING COMPETITOR: 'Decodable but Not Corrected by Fixed Residual-Stream Linear Steering' (arXiv 2605.05715, May 2026) demonstrates a classification-correction gap where linearly decodable directions (71.6% balanced accuracy) yield Δ≈0 under steering because the failure directions have 85-88% overlap with task-critical computation (specificity ratio ≤0.152). This directly threatens DBS-v2's Phase 3: even if CSB/CEO are decodable (Phase 1 succeeds), steering may fail due to entanglement. The paper proposes specificity ratio as a pre-intervention diagnostic — DBS-v2 must incorporate this.", "SEPARABILITY ≠ STEERABILITY GAP: Phase 1 validates whether CSB and CEO are separable (cosine similarity, PCA/ICA, cross-prediction ablation) but does NOT test whether identified directions are steerable without collateral damage. The 'Decodable but Not Corrected' paper shows these are empirically distinct questions. Phase 1 needs a steerability diagnostic: compute the specificity ratio (shared vs. mode-specific variance) of CSB/CEO directions relative to the overall correct-vs-incorrect subspace.", "MINOR MISSING REFERENCES: (a) 'Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection' (arXiv 2601.19375, Jan 2026) — another norm-preserving rotation method predating Spherical Steering, with discriminative layer selection. (b) 'Minimizing Collateral Damage in Activation Steering' (arXiv 2605.01167, May 2026) — formalizes collateral damage from steering interventions and proposes minimum-damage solutions, directly relevant to the manifold-preservation rationale.", "NO NON-LINEAR STEERING FALLBACK: The proposal's fallback (SAE-based features) addresses the case where CSB/CEO are not linearly separable, but not the case where they are separable but not linearly steerable. The 'Decodable but Not Corrected' paper shows a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods yield Δ≈0. Phase 3 should include a non-linear steering fallback (e.g., learned MLP correction) alongside Spherical Steering."]
Feedback: The revision from round 1 is excellent — all prior issues were addressed thoroughly and honestly. The main new concern is a very recent paper (2605.05715, this month) that identifies a 'classification-correction gap': failure directions can be linearly decodable but not steerable because they overlap heavily with task-critical computation. This is distinct from the off-manifold concern already addressed via Spherical Steering. Concrete fixes: (1) Add a 'steerability diagnostic' to Phase 1 — after extracting CSB/CEO directions, compute their specificity ratio (proportion of mode-specific vs. shared variance with the correct/incorrect subspace). If specificity is low (<0.2), flag high entanglement risk. (2) Add a non-linear steering fallback in Phase 3: when specificity is low, use a learned non-linear residual correction (small MLP) instead of fixed-direction rotation. (3) Cite Selective Steering and Minimizing Collateral Damage as part of the geometry-aware steering landscape. (4) Explicitly discuss the separation between 'decodable' and 'steerable' in the approach section — this strengthens the paper's contribution by showing awareness of a subtle and important distinction.


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
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "e7a2d6d0-8367-4aea-a101-37e6e5a783db",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T13:14:07.993Z_

```json
{
  "parentUuid": "e7a2d6d0-8367-4aea-a101-37e6e5a783db",
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
  "uuid": "43ad238c-3259-45ad-80a9-d969af51e9dc",
  "timestamp": "2026-05-19T13:14:07.993Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T13:14:07.993Z_

```json
{
  "parentUuid": "43ad238c-3259-45ad-80a9-d969af51e9dc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "eee6afc7-4471-4b94-95dc-293c8364e1fa",
  "timestamp": "2026-05-19T13:14:07.993Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
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
  "leafUuid": "eee6afc7-4471-4b94-95dc-293c8364e1fa",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Assistant

_source line 8 · 2026-05-19T13:14:12.534Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea by independently verifying its claims through web searches. This is a complex proposal about calibration in LLMs, specifically about disentangling competing calibration biases via geometry-aware activation steering. Let me systematically verify the key claims and references.

Let me start by searching for the key references and checking if the claimed gaps still exist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eee6afc7-4471-4b94-95dc-293c8364e1fa",
  "isSidechain": false,
  "requestId": "req_011CbBzErt9dE77HzfjKwcXn",
  "type": "assistant",
  "uuid": "c25016e6-ea40-4f4d-a7dd-36119de32f5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Qq7ajcZ4XaKScVcDXCTtK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13362,
      "cache_read_input_tokens": 11374,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 13362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13362
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

_source line 9 · 2026-05-19T13:14:13.522Z_

I'll conduct a thorough independent review of this idea. Let me start by verifying the key references and claims through multiple parallel searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c25016e6-ea40-4f4d-a7dd-36119de32f5a",
  "isSidechain": false,
  "requestId": "req_011CbBzErt9dE77HzfjKwcXn",
  "type": "assistant",
  "uuid": "1d8c4f83-0a05-4056-a7f4-cf522860d208",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Qq7ajcZ4XaKScVcDXCTtK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13362,
      "cache_read_input_tokens": 11374,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 13362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13362
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

_source line 10 · 2026-05-19T13:14:13.610Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JNkD46MXftyLKE4kh5oJ3t`</summary>

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
  "parentUuid": "1d8c4f83-0a05-4056-a7f4-cf522860d208",
  "isSidechain": false,
  "requestId": "req_011CbBzErt9dE77HzfjKwcXn",
  "type": "assistant",
  "uuid": "4fa74dc9-3120-4297-8c1c-0b92f45474d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Qq7ajcZ4XaKScVcDXCTtK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13362,
      "cache_read_input_tokens": 11374,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 13362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13362
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

_source line 11 · 2026-05-19T13:14:13.618Z_

<details><summary>↩ Tool result · `toolu_01JNkD46MXftyLKE4kh5oJ3t`</summary>

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
  "parentUuid": "4fa74dc9-3120-4297-8c1c-0b92f45474d0",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "e247a570-b776-4b75-9097-bd8ccc2ec58d",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "4fa74dc9-3120-4297-8c1c-0b92f45474d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T13:14:16.477Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now conduct systematic searches to verify the key claims and references in this proposal. I'll start with multiple parallel searches covering different aspects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e247a570-b776-4b75-9097-bd8ccc2ec58d",
  "isSidechain": false,
  "requestId": "req_011CbBzFGroEZdzHoVoD2CRZ",
  "type": "assistant",
  "uuid": "272f20ce-6686-4033-bdbb-2f477546a925",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HeBfm1nqAYjQ17GSvmfyR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14583,
      "cache_read_input_tokens": 11374,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 130,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14583
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

### Assistant

_source line 13 · 2026-05-19T13:14:16.853Z_

Now let me conduct systematic verification searches in parallel across multiple dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "272f20ce-6686-4033-bdbb-2f477546a925",
  "isSidechain": false,
  "requestId": "req_011CbBzFGroEZdzHoVoD2CRZ",
  "type": "assistant",
  "uuid": "95619b3b-054f-4524-99af-e426135b58e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HeBfm1nqAYjQ17GSvmfyR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14583,
      "cache_read_input_tokens": 11374,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 130,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14583
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

### Tool call

_source line 14 · 2026-05-19T13:14:17.506Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013ZYG9kBJPXqnQux3sGK1sG`</summary>

```json
{
  "query": "Kumaran competing biases overconfidence underconfidence LLM Nature Machine Intelligence 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95619b3b-054f-4524-99af-e426135b58e1",
  "isSidechain": false,
  "requestId": "req_011CbBzFGroEZdzHoVoD2CRZ",
  "type": "assistant",
  "uuid": "5cc58d6e-e4a8-4990-b4f5-fc55a6461813",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HeBfm1nqAYjQ17GSvmfyR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14583,
      "cache_read_input_tokens": 11374,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 130,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14583
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

_source line 15 · 2026-05-19T13:14:23.417Z_

<details><summary>↩ Tool result · `toolu_013ZYG9kBJPXqnQux3sGK1sG`</summary>

```text
Web search results for query: "Kumaran competing biases overconfidence underconfidence LLM Nature Machine Intelligence 2026"

Links: [{"title":"Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-026-01217-9"},{"title":"Articles in 2026 | Nature Machine Intelligence","url":"https://www.nature.com/natmachintell/articles?year=2026"},{"title":"Browse Articles | Nature Machine Intelligence","url":"https://www.nature.com/natmachintell/articles"},{"title":"Research articles | Nature Machine Intelligence","url":"https://www.nature.com/natmachintell/research-articles"},{"title":"How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models","url":"https://arxiv.org/html/2507.03120v1"},{"title":"How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models","url":"https://arxiv.org/pdf/2507.03120"},{"title":"[2507.03120] How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models","url":"https://arxiv.org/abs/2507.03120"},{"title":"Large Language Models are overconfident and amplify human bias","url":"https://arxiv.org/pdf/2505.02151"},{"title":"Do Language Models Mirror Human Confidence? Exploring Psychological Insights to Address Overconfidence in LLMs","url":"https://arxiv.org/pdf/2506.00582"},{"title":"New research reveals AI has a confidence problem","url":"https://techxplore.com/news/2025-07-reveals-ai-confidence-problem.html"}]

I found the research you're looking for! Here's what the search revealed:

Kumaran et al. show in Nature Machine Intelligence that large language model (LLM) confidence is shaped by two competing biases: a choice-supportive bias that inflates confidence in initial answers, and a systematic overweighting of contradictory advice, deviating from optimal Bayesian reasoning.

The research demonstrates that LLMs exhibit strikingly conflicting behaviors: they can appear steadfastly overconfident in their initial answers whilst at the same time being prone to excessive doubt when challenged. 

The study shows that LLMs – Gemma 3, GPT4o and o1-preview – exhibit a pronounced choice-supportive bias that reinforces and boosts their estimate of confidence in their answer, resulting in a marked resistance to change their mind.

The paper appears to be published in Nature Machine Intelligence in 2026, with the preprint available on arXiv from July 2025. Together, these findings furnish a mechanistic account of LLM confidence that explains both their stubbornness and excessive sensitivity to criticism.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cc58d6e-e4a8-4990-b4f5-fc55a6461813",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "55cf537d-8a96-47e5-b2bc-e6e9d196a114",
  "toolUseResult": {
    "query": "Kumaran competing biases overconfidence underconfidence LLM Nature Machine Intelligence 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016BP8Cd9kBYaFdFrJ5BtX5T",
        "content": [
          {
            "title": "Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence",
            "url": "https://www.nature.com/articles/s42256-026-01217-9"
          },
          {
            "title": "Articles in 2026 | Nature Machine Intelligence",
            "url": "https://www.nature.com/natmachintell/articles?year=2026"
          },
          {
            "title": "Browse Articles | Nature Machine Intelligence",
            "url": "https://www.nature.com/natmachintell/articles"
          },
          {
            "title": "Research articles | Nature Machine Intelligence",
            "url": "https://www.nature.com/natmachintell/research-articles"
          },
          {
            "title": "How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models",
            "url": "https://arxiv.org/html/2507.03120v1"
          },
          {
            "title": "How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models",
            "url": "https://arxiv.org/pdf/2507.03120"
          },
          {
            "title": "[2507.03120] How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models",
            "url": "https://arxiv.org/abs/2507.03120"
          },
          {
            "title": "Large Language Models are overconfident and amplify human bias",
            "url": "https://arxiv.org/pdf/2505.02151"
          },
          {
            "title": "Do Language Models Mirror Human Confidence? Exploring Psychological Insights to Address Overconfidence in LLMs",
            "url": "https://arxiv.org/pdf/2506.00582"
          },
          {
            "title": "New research reveals AI has a confidence problem",
            "url": "https://techxplore.com/news/2025-07-reveals-ai-confidence-problem.html"
          }
        ]
      },
      "I found the research you're looking for! Here's what the search revealed:\n\nKumaran et al. show in Nature Machine Intelligence that large language model (LLM) confidence is shaped by two competing biases: a choice-supportive bias that inflates confidence in initial answers, and a systematic overweighting of contradictory advice, deviating from optimal Bayesian reasoning.\n\nThe research demonstrates that LLMs exhibit strikingly conflicting behaviors: they can appear steadfastly overconfident in their initial answers whilst at the same time being prone to excessive doubt when challenged. \n\nThe study shows that LLMs – Gemma 3, GPT4o and o1-preview – exhibit a pronounced choice-supportive bias that reinforces and boosts their estimate of confidence in their answer, resulting in a marked resistance to change their mind.\n\nThe paper appears to be published in Nature Machine Intelligence in 2026, with the preprint available on arXiv from July 2025. Together, these findings furnish a mechanistic account of LLM confidence that explains both their stubbornness and excessive sensitivity to criticism."
    ],
    "durationSeconds": 5.907326413999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5cc58d6e-e4a8-4990-b4f5-fc55a6461813",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T13:14:28.353Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YQ2zRzDUbZ5v68uAHWctfQ`</summary>

```json
{
  "query": "Miao Ungar \"Closing the Confidence-Faithfulness Gap\" arXiv 2603.25052 calibration steering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55cf537d-8a96-47e5-b2bc-e6e9d196a114",
  "isSidechain": false,
  "requestId": "req_011CbBzFztPPF4zNboRqrPN3",
  "type": "assistant",
  "uuid": "367355df-65b3-45e6-af90-7d0f58883b1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ag9c61wFYuhAXbKfXowY1A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 25957,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 859,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 25957,
          "cache_creation_input_tokens": 859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 859
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

_source line 17 · 2026-05-19T13:14:36.323Z_

<details><summary>↩ Tool result · `toolu_01YQ2zRzDUbZ5v68uAHWctfQ`</summary>

```text
Web search results for query: "Miao Ungar "Closing the Confidence-Faithfulness Gap" arXiv 2603.25052 calibration steering"

Links: [{"title":"[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/abs/2603.25052"},{"title":"Fugu-MT 論文翻訳(概要): Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://fugumt.com/fugumt/paper_check/2603.25052v1"},{"title":"[2603.25052v1] Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/abs/2603.25052v1"},{"title":"Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/html/2603.25052"},{"title":"Closing the Confidence-Faithfulness Gap in Large ...","url":"https://arxiv.org/pdf/2603.25052"},{"title":"Closing the Confidence-Faithfulness Gap in Large ...","url":"https://x.com/HEI/status/2037535763399651595"},{"title":"Teaching Language Models to Faithfully Express their Uncertainty","url":"https://arxiv.org/pdf/2510.12587"},{"title":"To Trust or Not to Trust? Enhancing Large Language Models' Situated   Faithfulness to External Contexts","url":"https://arxiv.org/pdf/2410.14675"}]

I found the paper! Here are the key details about the work:

"Closing the Confidence-Faithfulness Gap in Large Language Models" is authored by Miranda Muqing Miao and Lyle Ungar from University of Pennsylvania.

**Main Findings:**

Large language models tend to verbalize confidence scores that are largely detached from their actual accuracy. The paper presents a mechanistic interpretability analysis of verbalized confidence, using linear probes and contrastive activation addition (CAA) steering to show that calibration and verbalized confidence signals are encoded linearly but are orthogonal to one another, with this finding consistent across three open-weight models and four datasets.

**The "Reasoning Contamination Effect":**

When models are prompted to simultaneously reason through a problem and verbalize a confidence score, the reasoning process disrupts the verbalized confidence direction, exacerbating miscalibration.

**Proposed Solution:**

The researchers introduce a two-stage adaptive steering pipeline that reads the model's internal accuracy estimate and steers verbalized output to match it.

The paper was submitted on March 26, 2026, with a revised version on April 1, 2026, and is available on arXiv as 2603.25052.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "367355df-65b3-45e6-af90-7d0f58883b1c",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "54242e7e-d8f0-4da1-bf99-6d62de45380b",
  "toolUseResult": {
    "query": "Miao Ungar \"Closing the Confidence-Faithfulness Gap\" arXiv 2603.25052 calibration steering",
    "results": [
      {
        "tool_use_id": "srvtoolu_017Rt72j1aJvDFk7yeWuqdA3",
        "content": [
          {
            "title": "[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/abs/2603.25052"
          },
          {
            "title": "Fugu-MT 論文翻訳(概要): Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://fugumt.com/fugumt/paper_check/2603.25052v1"
          },
          {
            "title": "[2603.25052v1] Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/abs/2603.25052v1"
          },
          {
            "title": "Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/html/2603.25052"
          },
          {
            "title": "Closing the Confidence-Faithfulness Gap in Large ...",
            "url": "https://arxiv.org/pdf/2603.25052"
          },
          {
            "title": "Closing the Confidence-Faithfulness Gap in Large ...",
            "url": "https://x.com/HEI/status/2037535763399651595"
          },
          {
            "title": "Teaching Language Models to Faithfully Express their Uncertainty",
            "url": "https://arxiv.org/pdf/2510.12587"
          },
          {
            "title": "To Trust or Not to Trust? Enhancing Large Language Models' Situated   Faithfulness to External Contexts",
            "url": "https://arxiv.org/pdf/2410.14675"
          }
        ]
      },
      "I found the paper! Here are the key details about the work:\n\n\"Closing the Confidence-Faithfulness Gap in Large Language Models\" is authored by Miranda Muqing Miao and Lyle Ungar from University of Pennsylvania.\n\n**Main Findings:**\n\nLarge language models tend to verbalize confidence scores that are largely detached from their actual accuracy. The paper presents a mechanistic interpretability analysis of verbalized confidence, using linear probes and contrastive activation addition (CAA) steering to show that calibration and verbalized confidence signals are encoded linearly but are orthogonal to one another, with this finding consistent across three open-weight models and four datasets.\n\n**The \"Reasoning Contamination Effect\":**\n\nWhen models are prompted to simultaneously reason through a problem and verbalize a confidence score, the reasoning process disrupts the verbalized confidence direction, exacerbating miscalibration.\n\n**Proposed Solution:**\n\nThe researchers introduce a two-stage adaptive steering pipeline that reads the model's internal accuracy estimate and steers verbalized output to match it.\n\nThe paper was submitted on March 26, 2026, with a revised version on April 1, 2026, and is available on arXiv as 2603.25052."
    ],
    "durationSeconds": 7.963257647999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "367355df-65b3-45e6-af90-7d0f58883b1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T13:14:39.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D22uZNf2sv5LfSazcCV72J`</summary>

```json
{
  "query": "Liu \"Decodable but Not Corrected\" residual stream linear steering medical LLM arXiv 2605.05715 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54242e7e-d8f0-4da1-bf99-6d62de45380b",
  "isSidechain": false,
  "requestId": "req_011CbBzGwkQNfjV2q9GegSbJ",
  "type": "assistant",
  "uuid": "e225acbd-9094-43f8-9fc7-9742b39698c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131Uwa7L3j4gFcRruz4bHMX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 26816,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 766,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 26816,
          "cache_creation_input_tokens": 766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 766
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

_source line 19 · 2026-05-19T13:14:45.658Z_

<details><summary>↩ Tool result · `toolu_01D22uZNf2sv5LfSazcCV72J`</summary>

```text
Web search results for query: "Liu "Decodable but Not Corrected" residual stream linear steering medical LLM arXiv 2605.05715 2026"

Links: [{"title":"[2605.05715] Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/abs/2605.05715"},{"title":"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/html/2605.05715"},{"title":"Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens","url":"https://arxiv.org/html/2604.02608v1"},{"title":"Refusal in Language Models Is Mediated by a Single Direction Andy Arditi∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f545448535dfde4f9786555403ab7c49-Paper-Conference.pdf"},{"title":"Toward Preference-aligned Large Language Models via Residual-based Model Steering","url":"https://arxiv.org/pdf/2509.23982"},{"title":"Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens","url":"https://arxiv.org/pdf/2604.02608"}]

I found the paper you're looking for! Here's what the search revealed:

The paper "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes" is by Ming Liu and was posted to arXiv on May 7, 2026.

The paper investigates whether linearly decodable failure signals in LLM hidden states can be leveraged to correct those failures, using Overthinking (OT)—a stable behavioral regime in medical QA where models answer correctly under resampling yet fail in extended chain-of-thought. 

Key findings include: OT is linearly decodable at 71.6% balanced accuracy, but five families of fixed linear steering (29 configurations) all yield no improvement, with identical null results across different architectures and domains.

The paper provides evidence suggesting representational entanglement, with the OT direction having 85-88% overlap with task-critical computation, which appears to explain why linear steering interventions cannot successfully correct these decodable failure signals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e225acbd-9094-43f8-9fc7-9742b39698c9",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "83834646-3402-4a65-a6ab-f575ae801640",
  "toolUseResult": {
    "query": "Liu \"Decodable but Not Corrected\" residual stream linear steering medical LLM arXiv 2605.05715 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01USVuGZqkhvDpRWHZ9YKW2f",
        "content": [
          {
            "title": "[2605.05715] Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/abs/2605.05715"
          },
          {
            "title": "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/html/2605.05715"
          },
          {
            "title": "Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens",
            "url": "https://arxiv.org/html/2604.02608v1"
          },
          {
            "title": "Refusal in Language Models Is Mediated by a Single Direction Andy Arditi∗",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/f545448535dfde4f9786555403ab7c49-Paper-Conference.pdf"
          },
          {
            "title": "Toward Preference-aligned Large Language Models via Residual-based Model Steering",
            "url": "https://arxiv.org/pdf/2509.23982"
          },
          {
            "title": "Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens",
            "url": "https://arxiv.org/pdf/2604.02608"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\nThe paper \"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes\" is by Ming Liu and was posted to arXiv on May 7, 2026.\n\nThe paper investigates whether linearly decodable failure signals in LLM hidden states can be leveraged to correct those failures, using Overthinking (OT)—a stable behavioral regime in medical QA where models answer correctly under resampling yet fail in extended chain-of-thought. \n\nKey findings include: OT is linearly decodable at 71.6% balanced accuracy, but five families of fixed linear steering (29 configurations) all yield no improvement, with identical null results across different architectures and domains.\n\nThe paper provides evidence suggesting representational entanglement, with the OT direction having 85-88% overlap with task-critical computation, which appears to explain why linear steering interventions cannot successfully correct these decodable failure signals."
    ],
    "durationSeconds": 6.599750663999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e225acbd-9094-43f8-9fc7-9742b39698c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-19T13:14:48.383Z_

Good, the three main references are verified. Let me now search for competing work and verify additional claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83834646-3402-4a65-a6ab-f575ae801640",
  "isSidechain": false,
  "requestId": "req_011CbBzHdeG1h2fZphSmdC9M",
  "type": "assistant",
  "uuid": "ce42161f-b52c-4949-812c-1cd6325a1332",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPVT8M9YY2dWu1AUs6n9e6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 27582,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 101,
          "cache_read_input_tokens": 27582,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 706
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

_source line 21 · 2026-05-19T13:14:48.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YbSU4XwS953vavuTpzmBoV`</summary>

```json
{
  "query": "Spherical Steering geometry-aware activation rotation language models ICML 2026 arXiv 2602.08169"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce42161f-b52c-4949-812c-1cd6325a1332",
  "isSidechain": false,
  "requestId": "req_011CbBzHdeG1h2fZphSmdC9M",
  "type": "assistant",
  "uuid": "2da94ef4-53af-4b35-b9ae-bab71ec63584",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPVT8M9YY2dWu1AUs6n9e6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 27582,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 101,
          "cache_read_input_tokens": 27582,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 706
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

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "2da94ef4-53af-4b35-b9ae-bab71ec63584",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Tool result

_source line 24 · 2026-05-19T13:14:56.375Z_

<details><summary>↩ Tool result · `toolu_01YbSU4XwS953vavuTpzmBoV`</summary>

```text
Web search results for query: "Spherical Steering geometry-aware activation rotation language models ICML 2026 arXiv 2602.08169"

Links: [{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/html/2602.08169v1"},{"title":"GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub","url":"https://github.com/chili-lab/Spherical-Steering"},{"title":"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/html/2605.05892"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"Publications","url":"https://hanjiechen.github.io/publication.html"},{"title":"From Directions to Regions: Decomposing Activations in Language Models via Local Geometry","url":"https://arxiv.org/pdf/2602.02464"},{"title":"Steering Language Models With Activation Engineering","url":"https://arxiv.org/pdf/2308.10248"}]

I found information about this paper! Here are the details:

**"Spherical Steering: Geometry-Aware Activation Rotation for Language Models"** is an arXiv paper (2602.08169) submitted on February 9, 2026 by Zejia You, Chunyuan Deng, and Hanjie Chen.

**Summary of the work:**

The paper focuses on inference-time steering as a promising paradigm for controlling language models without retraining. Standard approaches rely on activation addition, a geometric operation that alters the magnitude of hidden representations, raising concerns about representation collapse and degradation of open-ended generation capabilities.

The paper proposes Spherical Steering, a training-free primitive that resolves this trade-off through activation rotation—rotating activations along a geodesic toward a target direction while preserving the integrity of the representations. The method incorporates a confidence gate that dynamically modulates steering strength based on input uncertainty.

**Results:**

Experiments across multiple-choice benchmarks demonstrate that Spherical Steering significantly outperforms addition-based baselines (notably by +10% on TruthfulQA, COPA, and Storycloze), while simultaneously maintaining the model's general open-ended generation quality.

The paper was accepted to The Forty-Third International Conference on Machine Learning (ICML) in Seoul, South Korea, July 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2da94ef4-53af-4b35-b9ae-bab71ec63584",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "166444d6-d10f-4d05-8d92-adb9a875d783",
  "toolUseResult": {
    "query": "Spherical Steering geometry-aware activation rotation language models ICML 2026 arXiv 2602.08169",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SkKbztJhyESm27azWmo8up",
        "content": [
          {
            "title": "[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/abs/2602.08169"
          },
          {
            "title": "Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/html/2602.08169v1"
          },
          {
            "title": "GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub",
            "url": "https://github.com/chili-lab/Spherical-Steering"
          },
          {
            "title": "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/html/2605.05892"
          },
          {
            "title": "(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"
          },
          {
            "title": "Publications",
            "url": "https://hanjiechen.github.io/publication.html"
          },
          {
            "title": "From Directions to Regions: Decomposing Activations in Language Models via Local Geometry",
            "url": "https://arxiv.org/pdf/2602.02464"
          },
          {
            "title": "Steering Language Models With Activation Engineering",
            "url": "https://arxiv.org/pdf/2308.10248"
          }
        ]
      },
      "I found information about this paper! Here are the details:\n\n**\"Spherical Steering: Geometry-Aware Activation Rotation for Language Models\"** is an arXiv paper (2602.08169) submitted on February 9, 2026 by Zejia You, Chunyuan Deng, and Hanjie Chen.\n\n**Summary of the work:**\n\nThe paper focuses on inference-time steering as a promising paradigm for controlling language models without retraining. Standard approaches rely on activation addition, a geometric operation that alters the magnitude of hidden representations, raising concerns about representation collapse and degradation of open-ended generation capabilities.\n\nThe paper proposes Spherical Steering, a training-free primitive that resolves this trade-off through activation rotation—rotating activations along a geodesic toward a target direction while preserving the integrity of the representations. The method incorporates a confidence gate that dynamically modulates steering strength based on input uncertainty.\n\n**Results:**\n\nExperiments across multiple-choice benchmarks demonstrate that Spherical Steering significantly outperforms addition-based baselines (notably by +10% on TruthfulQA, COPA, and Storycloze), while simultaneously maintaining the model's general open-ended generation quality.\n\nThe paper was accepted to The Forty-Third International Conference on Machine Learning (ICML) in Seoul, South Korea, July 2026."
    ],
    "durationSeconds": 7.373455812,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2da94ef4-53af-4b35-b9ae-bab71ec63584",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T13:14:59.329Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ABVsSoRDYzkGb9jYTvEMcC`</summary>

```json
{
  "query": "COAST \"Minimizing Collateral Damage in Activation Steering\" Nguyen arXiv 2605.01167 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "166444d6-d10f-4d05-8d92-adb9a875d783",
  "isSidechain": false,
  "requestId": "req_011CbBzJRTobLe87SqsZq6Ga",
  "type": "assistant",
  "uuid": "fa03b272-b366-49fa-ad63-3d43371c7ea4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfpmfPzwsqUs4ydGhT9S5y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1544,
      "cache_read_input_tokens": 27582,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 27582,
          "cache_creation_input_tokens": 1544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1544
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

_source line 26 · 2026-05-19T13:15:05.346Z_

<details><summary>↩ Tool result · `toolu_01ABVsSoRDYzkGb9jYTvEMcC`</summary>

```text
Web search results for query: "COAST "Minimizing Collateral Damage in Activation Steering" Nguyen arXiv 2605.01167 2026"

Links: [{"title":"[2605.01167] Minimizing Collateral Damage in Activation Steering","url":"https://arxiv.org/abs/2605.01167"},{"title":"Minimizing Collateral Damage in Activation Steering","url":"https://arxiv.org/html/2605.01167v1"},{"title":"Minimizing Collateral Damage in Activation Steering","url":"https://www.researchgate.net/publication/404427927_Minimizing_Collateral_Damage_in_Activation_Steering"},{"title":"Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/html/2605.03907v1"},{"title":"Don’t Lose Focus: Activation Steering via Key-Orthogonal Projections","url":"https://arxiv.org/html/2605.06342v1"},{"title":"Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk for Large Language Models","url":"https://arxiv.org/pdf/2602.04896"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

"Minimizing Collateral Damage in Activation Steering" is authored by Tam Nguyen, Tu Anh Nguyen, and others, and describes activation steering as a method for controlling Large Language Model (LLM) behavior by intervening in its internal representations to increase alignment with a specific target feature direction.

The paper addresses the problem that standard interventions, such as vector addition, often cause "collateral damage," defined as unintended changes in the alignment of activations along other non-target feature directions. This damage occurs because standard methods implicitly assume the isotropy of non-target features.

The work provides a mathematical formalization of collateral damage and introduces a principled framework that models steering as a constrained optimization problem, with a method that finds a new activation minimizing the expected squared collateral change weighted by the empirical second-moment matrix of activations.

The paper is available on arXiv at https://arxiv.org/abs/2605.01167 and was published on May 1, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa03b272-b366-49fa-ad63-3d43371c7ea4",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "08299bfa-cc2a-4304-99f9-3a3a90401835",
  "toolUseResult": {
    "query": "COAST \"Minimizing Collateral Damage in Activation Steering\" Nguyen arXiv 2605.01167 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CqG2Qp1LFiWT2MbwyTU2rP",
        "content": [
          {
            "title": "[2605.01167] Minimizing Collateral Damage in Activation Steering",
            "url": "https://arxiv.org/abs/2605.01167"
          },
          {
            "title": "Minimizing Collateral Damage in Activation Steering",
            "url": "https://arxiv.org/html/2605.01167v1"
          },
          {
            "title": "Minimizing Collateral Damage in Activation Steering",
            "url": "https://www.researchgate.net/publication/404427927_Minimizing_Collateral_Damage_in_Activation_Steering"
          },
          {
            "title": "Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/html/2605.03907v1"
          },
          {
            "title": "Don’t Lose Focus: Activation Steering via Key-Orthogonal Projections",
            "url": "https://arxiv.org/html/2605.06342v1"
          },
          {
            "title": "Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk for Large Language Models",
            "url": "https://arxiv.org/pdf/2602.04896"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what I found:\n\n\"Minimizing Collateral Damage in Activation Steering\" is authored by Tam Nguyen, Tu Anh Nguyen, and others, and describes activation steering as a method for controlling Large Language Model (LLM) behavior by intervening in its internal representations to increase alignment with a specific target feature direction.\n\nThe paper addresses the problem that standard interventions, such as vector addition, often cause \"collateral damage,\" defined as unintended changes in the alignment of activations along other non-target feature directions. This damage occurs because standard methods implicitly assume the isotropy of non-target features.\n\nThe work provides a mathematical formalization of collateral damage and introduces a principled framework that models steering as a constrained optimization problem, with a method that finds a new activation minimizing the expected squared collateral change weighted by the empirical second-moment matrix of activations.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2605.01167 and was published on May 1, 2026."
    ],
    "durationSeconds": 6.010398341,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fa03b272-b366-49fa-ad63-3d43371c7ea4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T13:15:08.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Eh5ocwvBvYC1AdBJmEGg3B`</summary>

```json
{
  "query": "\"Selective Steering\" norm-preserving discriminative layer selection Dang Ngo arXiv 2601.19375 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08299bfa-cc2a-4304-99f9-3a3a90401835",
  "isSidechain": false,
  "requestId": "req_011CbBzK5tMGNkUQqDGUaQ9g",
  "type": "assistant",
  "uuid": "37718815-1ff2-4374-b9ea-cfabf8fa45ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGkVcazeMCkkDfKjYZxDfN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 29126,
      "output_tokens": 83,
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
          "output_tokens": 83,
          "cache_read_input_tokens": 29126,
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

_source line 28 · 2026-05-19T13:15:14.604Z_

<details><summary>↩ Tool result · `toolu_01Eh5ocwvBvYC1AdBJmEGg3B`</summary>

```text
Web search results for query: ""Selective Steering" norm-preserving discriminative layer selection Dang Ngo arXiv 2601.19375 2026"

Links: [{"title":"GitHub - knoveleng/steering: Official repo for the paper: \"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection\"","url":"https://github.com/knoveleng/steering"},{"title":"[2601.19375] Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection","url":"https://arxiv.org/abs/2601.19375"},{"title":"Selective Steering: Norm-Preserving Control Through Discriminative","url":"https://arxiv.org/pdf/2601.19375"},{"title":"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection","url":"https://arxiv.org/html/2601.19375v1"},{"title":"Where to Steer: Input-Dependent Layer Selection for Steering Improves LLM Alignment","url":"https://arxiv.org/pdf/2604.03867"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/pdf/2602.04428"}]

Based on the search results, I found the paper you're looking for:

**"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection"** by Quy-Anh Dang and Chris Ngo, published in 2026 with arXiv identifier 2601.19375.

**Key Details:**

The paper addresses the vulnerability of large language models to adversarial attacks. It proposes an improvement over existing activation steering techniques, which suffer from limitations like activation addition requiring careful coefficient tuning and sensitivity to layer-specific norm variations. Previous Angular Steering methods violate norm preservation, causing distribution shift and generation collapse, particularly in models below 7B parameters.

**The Proposed Solution:**

Selective Steering addresses these limitations through two key innovations: (1) a mathematically rigorous norm-preserving rotation formulation that maintains activation distribution integrity, and (2) discriminative layer selection that applies steering only where feature representations are meaningful.

**GitHub Repository:** The official repository is available at https://github.com/knoveleng/steering, and the paper itself can be accessed at https://arxiv.org/abs/2601.19375.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37718815-1ff2-4374-b9ea-cfabf8fa45ab",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "be78bf14-df56-484a-87f1-0a4814ee189f",
  "toolUseResult": {
    "query": "\"Selective Steering\" norm-preserving discriminative layer selection Dang Ngo arXiv 2601.19375 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N5b1WfhRQWuyJKfCebFTM9",
        "content": [
          {
            "title": "GitHub - knoveleng/steering: Official repo for the paper: \"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection\"",
            "url": "https://github.com/knoveleng/steering"
          },
          {
            "title": "[2601.19375] Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection",
            "url": "https://arxiv.org/abs/2601.19375"
          },
          {
            "title": "Selective Steering: Norm-Preserving Control Through Discriminative",
            "url": "https://arxiv.org/pdf/2601.19375"
          },
          {
            "title": "Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection",
            "url": "https://arxiv.org/html/2601.19375v1"
          },
          {
            "title": "Where to Steer: Input-Dependent Layer Selection for Steering Improves LLM Alignment",
            "url": "https://arxiv.org/pdf/2604.03867"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/pdf/2602.04428"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**\"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection\"** by Quy-Anh Dang and Chris Ngo, published in 2026 with arXiv identifier 2601.19375.\n\n**Key Details:**\n\nThe paper addresses the vulnerability of large language models to adversarial attacks. It proposes an improvement over existing activation steering techniques, which suffer from limitations like activation addition requiring careful coefficient tuning and sensitivity to layer-specific norm variations. Previous Angular Steering methods violate norm preservation, causing distribution shift and generation collapse, particularly in models below 7B parameters.\n\n**The Proposed Solution:**\n\nSelective Steering addresses these limitations through two key innovations: (1) a mathematically rigorous norm-preserving rotation formulation that maintains activation distribution integrity, and (2) discriminative layer selection that applies steering only where feature representations are meaningful.\n\n**GitHub Repository:** The official repository is available at https://github.com/knoveleng/steering, and the paper itself can be accessed at https://arxiv.org/abs/2601.19375."
    ],
    "durationSeconds": 6.348033023999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "37718815-1ff2-4374-b9ea-cfabf8fa45ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-19T13:15:14.608Z_

```json
{
  "parentUuid": "be78bf14-df56-484a-87f1-0a4814ee189f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2ce7fe07-8348-4f8b-a3b1-1f6a6ad53994",
  "timestamp": "2026-05-19T13:15:14.608Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-19T13:15:17.390Z_

Good, key references are verified. Now let me search for competing work that the proposal might be missing, and verify SOTA claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ce7fe07-8348-4f8b-a3b1-1f6a6ad53994",
  "isSidechain": false,
  "requestId": "req_011CbBzKmRd23qLoSZmiFmDT",
  "type": "assistant",
  "uuid": "3dd27903-a105-4e4b-ab26-65abe83d9012",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DDJwreTPQABmiJ82mJkdh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 29802,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 29802,
          "cache_creation_input_tokens": 778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 778
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

_source line 31 · 2026-05-19T13:15:18.034Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014HrubbsJwEyM2sJPw8D8D4`</summary>

```json
{
  "query": "LLM calibration activation steering competing biases disentangle 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dd27903-a105-4e4b-ab26-65abe83d9012",
  "isSidechain": false,
  "requestId": "req_011CbBzKmRd23qLoSZmiFmDT",
  "type": "assistant",
  "uuid": "8ab8b343-dfd6-42c5-84fc-d798e83c3a51",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DDJwreTPQABmiJ82mJkdh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 29802,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 29802,
          "cache_creation_input_tokens": 778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 778
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

_source line 32 · 2026-05-19T13:15:24.310Z_

<details><summary>↩ Tool result · `toolu_014HrubbsJwEyM2sJPw8D8D4`</summary>

```text
Web search results for query: "LLM calibration activation steering competing biases disentangle 2026 arXiv"

Links: [{"title":"Mitigating Content Effects on Reasoning in Language Models through Fine-Grained Activation Steering","url":"https://arxiv.org/pdf/2505.12189"},{"title":"Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs","url":"https://arxiv.org/html/2508.09019v1"},{"title":"Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs","url":"https://arxiv.org/pdf/2508.09019"},{"title":"Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs","url":"https://arxiv.org/pdf/2503.05371"},{"title":"Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators","url":"https://arxiv.org/pdf/2509.03647"},{"title":"Investigating Bias Representations in Llama 2 Chat via Activation   Steering","url":"https://arxiv.org/pdf/2402.00402"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/pdf/2602.04428"},{"title":"Steered LLM Activations are Non-Surjective","url":"https://arxiv.org/html/2604.09839v1"}]

I found several recent arXiv papers related to LLM calibration, activation steering, and bias mitigation from 2025-2026. Here are the key findings:

## Recent Research on Activation Steering and Bias Mitigation

A complete end-to-end system uses techniques from mechanistic interpretability to identify and actively mitigate bias directly within a model's internal workings. Steering vectors are computed by contrasting the model's activation patterns for biased and neutral statements, and by adding these vectors during inference, models can actively steer away from producing harmful, stereotypical, or biased content in real-time.

## Fine-Grained Approaches

Prior work generally builds task-specific steering vectors and injects them at inference time as biases or rescaling factors in selected LLM components, thereby steering the model toward the target objective. However, a main limitation of block-level intervention is that it ignores heterogeneity within block activations, which often span hundreds or thousands of dimensions, each indicating a different feature.

## Challenges with Competing Biases

Recent research has identified important considerations around steering reliability. Anthropic's SAE analysis cautions that even seemingly interpretable features can have off-target effects, for example, a feature suspected to affect one bias substantially shifting another, making causal consequences difficult to anticipate.

These papers represent cutting-edge work in understanding and controlling LLM behavior at the activation level.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ab8b343-dfd6-42c5-84fc-d798e83c3a51",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "2a2c5812-d1b0-40c9-a73b-bfd40a1cdbe5",
  "toolUseResult": {
    "query": "LLM calibration activation steering competing biases disentangle 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SgV26ZFMFehcaQCv1cfZRm",
        "content": [
          {
            "title": "Mitigating Content Effects on Reasoning in Language Models through Fine-Grained Activation Steering",
            "url": "https://arxiv.org/pdf/2505.12189"
          },
          {
            "title": "Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs",
            "url": "https://arxiv.org/html/2508.09019v1"
          },
          {
            "title": "Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs",
            "url": "https://arxiv.org/pdf/2508.09019"
          },
          {
            "title": "Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs",
            "url": "https://arxiv.org/pdf/2503.05371"
          },
          {
            "title": "Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators",
            "url": "https://arxiv.org/pdf/2509.03647"
          },
          {
            "title": "Investigating Bias Representations in Llama 2 Chat via Activation   Steering",
            "url": "https://arxiv.org/pdf/2402.00402"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/pdf/2602.04428"
          },
          {
            "title": "Steered LLM Activations are Non-Surjective",
            "url": "https://arxiv.org/html/2604.09839v1"
          }
        ]
      },
      "I found several recent arXiv papers related to LLM calibration, activation steering, and bias mitigation from 2025-2026. Here are the key findings:\n\n## Recent Research on Activation Steering and Bias Mitigation\n\nA complete end-to-end system uses techniques from mechanistic interpretability to identify and actively mitigate bias directly within a model's internal workings. Steering vectors are computed by contrasting the model's activation patterns for biased and neutral statements, and by adding these vectors during inference, models can actively steer away from producing harmful, stereotypical, or biased content in real-time.\n\n## Fine-Grained Approaches\n\nPrior work generally builds task-specific steering vectors and injects them at inference time as biases or rescaling factors in selected LLM components, thereby steering the model toward the target objective. However, a main limitation of block-level intervention is that it ignores heterogeneity within block activations, which often span hundreds or thousands of dimensions, each indicating a different feature.\n\n## Challenges with Competing Biases\n\nRecent research has identified important considerations around steering reliability. Anthropic's SAE analysis cautions that even seemingly interpretable features can have off-target effects, for example, a feature suspected to affect one bias substantially shifting another, making causal consequences difficult to anticipate.\n\nThese papers represent cutting-edge work in understanding and controlling LLM behavior at the activation level."
    ],
    "durationSeconds": 6.271596843999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8ab8b343-dfd6-42c5-84fc-d798e83c3a51",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T13:15:27.467Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PgbsxvERMa9xBa4wvFZ4Yu`</summary>

```json
{
  "query": "LLM calibration bias decomposition mechanistic interpretability confidence 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a2c5812-d1b0-40c9-a73b-bfd40a1cdbe5",
  "isSidechain": false,
  "requestId": "req_011CbBzLUwDPFiL4ARmQBGEU",
  "type": "assistant",
  "uuid": "31866ddb-1ba8-4e22-bbd7-ec1219923904",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBubN2wnE9ZdtgBTWAdFU4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 30580,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 30580,
          "cache_creation_input_tokens": 814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 814
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

_source line 34 · 2026-05-19T13:15:35.099Z_

<details><summary>↩ Tool result · `toolu_01PgbsxvERMa9xBa4wvFZ4Yu`</summary>

```text
Web search results for query: "LLM calibration bias decomposition mechanistic interpretability confidence 2026 site:arxiv.org"

Links: [{"title":"Dissecting Bias in LLMs: A Mechanistic Interpretability Perspective","url":"https://arxiv.org/pdf/2506.05166"},{"title":"Dissecting Bias in LLMs: A Mechanistic Interpretability Perspective","url":"https://arxiv.org/html/2506.05166v2"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs","url":"https://arxiv.org/pdf/2508.09019"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"[2506.05166] Dissecting Bias in LLMs: A Mechanistic Interpretability Perspective","url":"https://arxiv.org/abs/2506.05166"},{"title":"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs","url":"https://arxiv.org/pdf/2604.01457"},{"title":"The Dunning-Kruger Effect in Large Language Models: An Empirical Study of Confidence Calibration","url":"https://arxiv.org/html/2603.09985"}]

I found several relevant papers on arxiv.org related to your search query. Here are the key results:

1. **"Dissecting Bias in LLMs: A Mechanistic Interpretability Perspective"** (2506.05166, June 2025): This paper adopts a mechanistic interpretability approach to analyze how biases are structurally represented within models like GPT-2 and Llama2, exploring different metrics to identify the internal edges responsible for biased behavior. The research demonstrates that bias-related computations are highly localized, often concentrated in a small subset of layers.

2. **"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models"** (2510.03136, October 2025): This work presents the first systematic evaluation of multilingual calibration across high-quality, human-curated datasets spanning over 100 languages and covering six prominent LLM families.

3. **"Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs"** (2508.09019, August 2025): This paper introduces an end-to-end system that uses techniques from mechanistic interpretability to both identify and actively mitigate bias directly within a model's internal workings.

4. **"Calibration Across Layers: Understanding Calibration Evolution in LLMs"** (2511.00280, October 2025): This work provides a mechanistic, layer-wise perspective on calibration, tracking how uncertainty evolves throughout the forward pass.

5. **"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs"** (2604.01457, April 2026): This study found that a compact set of MLP blocks and attention heads, primarily in the middle-to-late layers, consistently write the confidence-inflation signal at the final token position.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31866ddb-1ba8-4e22-bbd7-ec1219923904",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "a00318c9-c063-49a1-8032-23d5aa0a2f42",
  "toolUseResult": {
    "query": "LLM calibration bias decomposition mechanistic interpretability confidence 2026 site:arxiv.org",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q75WXenBkj9pMRo3BBoppS",
        "content": [
          {
            "title": "Dissecting Bias in LLMs: A Mechanistic Interpretability Perspective",
            "url": "https://arxiv.org/pdf/2506.05166"
          },
          {
            "title": "Dissecting Bias in LLMs: A Mechanistic Interpretability Perspective",
            "url": "https://arxiv.org/html/2506.05166v2"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          },
          {
            "title": "Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs",
            "url": "https://arxiv.org/pdf/2508.09019"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://arxiv.org/html/2511.00280v1"
          },
          {
            "title": "[2506.05166] Dissecting Bias in LLMs: A Mechanistic Interpretability Perspective",
            "url": "https://arxiv.org/abs/2506.05166"
          },
          {
            "title": "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs",
            "url": "https://arxiv.org/pdf/2604.01457"
          },
          {
            "title": "The Dunning-Kruger Effect in Large Language Models: An Empirical Study of Confidence Calibration",
            "url": "https://arxiv.org/html/2603.09985"
          }
        ]
      },
      "I found several relevant papers on arxiv.org related to your search query. Here are the key results:\n\n1. **\"Dissecting Bias in LLMs: A Mechanistic Interpretability Perspective\"** (2506.05166, June 2025): This paper adopts a mechanistic interpretability approach to analyze how biases are structurally represented within models like GPT-2 and Llama2, exploring different metrics to identify the internal edges responsible for biased behavior. The research demonstrates that bias-related computations are highly localized, often concentrated in a small subset of layers.\n\n2. **\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models\"** (2510.03136, October 2025): This work presents the first systematic evaluation of multilingual calibration across high-quality, human-curated datasets spanning over 100 languages and covering six prominent LLM families.\n\n3. **\"Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs\"** (2508.09019, August 2025): This paper introduces an end-to-end system that uses techniques from mechanistic interpretability to both identify and actively mitigate bias directly within a model's internal workings.\n\n4. **\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\"** (2511.00280, October 2025): This work provides a mechanistic, layer-wise perspective on calibration, tracking how uncertainty evolves throughout the forward pass.\n\n5. **\"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs\"** (2604.01457, April 2026): This study found that a compact set of MLP blocks and attention heads, primarily in the middle-to-late layers, consistently write the confidence-inflation signal at the final token position."
    ],
    "durationSeconds": 7.625373273000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "31866ddb-1ba8-4e22-bbd7-ec1219923904",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
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
  "leafUuid": "a00318c9-c063-49a1-8032-23d5aa0a2f42",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Tool call

_source line 37 · 2026-05-19T13:15:38.462Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0114CrBQx3Jepn5Z6bDtkE4W`</summary>

```json
{
  "query": "choice supportive bias LLM activation steering correction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a00318c9-c063-49a1-8032-23d5aa0a2f42",
  "isSidechain": false,
  "requestId": "req_011CbBzMH3dBNFkTyduUorsR",
  "type": "assistant",
  "uuid": "3aea4e20-fc11-4c3b-b697-6e63688bdceb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AW8i8ezPz2Qrfx89sVAy9F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 926,
      "cache_read_input_tokens": 31394,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 926,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 31394,
          "cache_creation_input_tokens": 926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 926
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

_source line 38 · 2026-05-19T13:15:45.452Z_

<details><summary>↩ Tool result · `toolu_0114CrBQx3Jepn5Z6bDtkE4W`</summary>

```text
Web search results for query: "choice supportive bias LLM activation steering correction 2025 2026"

Links: [{"title":"Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs","url":"https://arxiv.org/pdf/2503.05371"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Steering LLM Reasoning Through Bias-Only Adaptation","url":"https://arxiv.org/html/2505.18706v1"},{"title":"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation","url":"https://arxiv.org/html/2512.03082v1"},{"title":"Programming Refusal with Conditional Activation Steering","url":"https://arxiv.org/pdf/2409.05907"},{"title":"Mitigating Content Effects on Reasoning in Language Models through Fine-Grained Activation Steering","url":"https://arxiv.org/pdf/2505.12189"},{"title":"(PDF) Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation","url":"https://www.researchgate.net/publication/398312753_Alleviating_Choice_Supportive_Bias_in_LLM_with_Reasoning_Dependency_Generation"},{"title":"Steering Code LLMs with Activation Directions for Language and Library Control","url":"https://arxiv.org/pdf/2603.23629"}]

I found several relevant research papers on this topic. Here's what the search revealed:

## Choice Supportive Bias in LLMs

Choice supportive bias (CSB) is context-dependent and favors whatever option was chosen, regardless of its inherent qualities. Recent work demonstrated that commercial LLMs exhibit significant CSB, systematically inflating positive assessments of chosen options across diverse domains.

CSB may not be addressed well by existing debiasing methods, which are designed to correct static correlations between protected attributes and outcomes. When standard debiasing techniques balance demographic representation, they may miss CSB because the bias target shifts with each decision context.

## Recent Approaches to Correction

A paper from November 2025 titled "Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation" proposes a method called RDG (Reasoning Dependency Generation) to address this specific bias by restructuring choice-justification dependencies.

## Activation Steering Methods

Steering vectors, a technique within activation engineering, provide a direct way to probe and manipulate model behavior with minimal changes to the underlying weights. Conditional Activation Steering (CAST), presented at ICLR 2025 as a spotlight paper, solves the problem of vanilla steering always being on by analyzing activation patterns during inference to decide whether to steer.

The research indicates this is an active and evolving field with multiple approaches being developed to address bias correction in LLMs during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3aea4e20-fc11-4c3b-b697-6e63688bdceb",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "cd912f98-f379-45b1-bad6-809058d05cd6",
  "toolUseResult": {
    "query": "choice supportive bias LLM activation steering correction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016fANmtT9B29F93Lm473bVN",
        "content": [
          {
            "title": "Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs",
            "url": "https://arxiv.org/pdf/2503.05371"
          },
          {
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "Steering LLM Reasoning Through Bias-Only Adaptation",
            "url": "https://arxiv.org/html/2505.18706v1"
          },
          {
            "title": "Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation",
            "url": "https://arxiv.org/html/2512.03082v1"
          },
          {
            "title": "Programming Refusal with Conditional Activation Steering",
            "url": "https://arxiv.org/pdf/2409.05907"
          },
          {
            "title": "Mitigating Content Effects on Reasoning in Language Models through Fine-Grained Activation Steering",
            "url": "https://arxiv.org/pdf/2505.12189"
          },
          {
            "title": "(PDF) Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation",
            "url": "https://www.researchgate.net/publication/398312753_Alleviating_Choice_Supportive_Bias_in_LLM_with_Reasoning_Dependency_Generation"
          },
          {
            "title": "Steering Code LLMs with Activation Directions for Language and Library Control",
            "url": "https://arxiv.org/pdf/2603.23629"
          }
        ]
      },
      "I found several relevant research papers on this topic. Here's what the search revealed:\n\n## Choice Supportive Bias in LLMs\n\nChoice supportive bias (CSB) is context-dependent and favors whatever option was chosen, regardless of its inherent qualities. Recent work demonstrated that commercial LLMs exhibit significant CSB, systematically inflating positive assessments of chosen options across diverse domains.\n\nCSB may not be addressed well by existing debiasing methods, which are designed to correct static correlations between protected attributes and outcomes. When standard debiasing techniques balance demographic representation, they may miss CSB because the bias target shifts with each decision context.\n\n## Recent Approaches to Correction\n\nA paper from November 2025 titled \"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation\" proposes a method called RDG (Reasoning Dependency Generation) to address this specific bias by restructuring choice-justification dependencies.\n\n## Activation Steering Methods\n\nSteering vectors, a technique within activation engineering, provide a direct way to probe and manipulate model behavior with minimal changes to the underlying weights. Conditional Activation Steering (CAST), presented at ICLR 2025 as a spotlight paper, solves the problem of vanilla steering always being on by analyzing activation patterns during inference to decide whether to steer.\n\nThe research indicates this is an active and evolving field with multiple approaches being developed to address bias correction in LLMs during 2025-2026."
    ],
    "durationSeconds": 6.986817987999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3aea4e20-fc11-4c3b-b697-6e63688bdceb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T13:15:48.685Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FSPvZREaMNwDbhoSZF9wzi`</summary>

```json
{
  "query": "\"confidence manifold\" correctness representations language models arXiv 2602.08159"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd912f98-f379-45b1-bad6-809058d05cd6",
  "isSidechain": false,
  "requestId": "req_011CbBzN3FSG57aomNYPU5r1",
  "type": "assistant",
  "uuid": "c0329ac0-b286-4158-ae9f-6210aff5bec2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017afqAr3SNm44NFYXpuaRzd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 32320,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 818,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 32320,
          "cache_creation_input_tokens": 818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 818
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

_source line 40 · 2026-05-19T13:15:54.459Z_

<details><summary>↩ Tool result · `toolu_01FSPvZREaMNwDbhoSZF9wzi`</summary>

```text
Web search results for query: ""confidence manifold" correctness representations language models arXiv 2602.08159"

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"Graph-based Confidence Calibration for Large Language Models","url":"https://arxiv.org/pdf/2411.02454"}]

I found the paper! Here are the results for your search:

The paper characterizes the geometry of correctness representations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation.

The key finding is that internally, LLMs encode a rich correctness signal that is never expressed in their outputs, and it lives in a surprisingly low-dimensional subspace of just 3 to 8 dimensions, consistent across architectures. This subspace is called the confidence manifold.

The research demonstrates that centroid distance in the low-dimensional subspace matches trained probe performance (0.90 AUC), enabling few-shot detection, and validates causally through activation steering with learned directions producing 10.9 percentage point changes in error rates.

Internal probes achieve 0.80-0.97 AUC while output-based methods (P(True), semantic entropy) achieve only 0.44–0.64 AUC, indicating that the correctness signal exists internally but is not expressed in outputs.

The paper was published on February 8, 2026 (arXiv:2602.08159v1).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0329ac0-b286-4158-ae9f-6210aff5bec2",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "59a0176f-08c1-4c6c-8f4d-991cb1aa5813",
  "toolUseResult": {
    "query": "\"confidence manifold\" correctness representations language models arXiv 2602.08159",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SgeKLNab74QhDsbe6Spmiy",
        "content": [
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/html/2602.08159v1"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/pdf/2602.08159"
          },
          {
            "title": "The Confidence Manifold:",
            "url": "https://www.arxiv.org/pdf/2602.08159"
          },
          {
            "title": "The Confidence Manifold - Seongland",
            "url": "https://seongland.com/article/confidence-manifold/"
          },
          {
            "title": "Graph-based Confidence Calibration for Large Language Models",
            "url": "https://arxiv.org/pdf/2411.02454"
          }
        ]
      },
      "I found the paper! Here are the results for your search:\n\nThe paper characterizes the geometry of correctness representations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation.\n\nThe key finding is that internally, LLMs encode a rich correctness signal that is never expressed in their outputs, and it lives in a surprisingly low-dimensional subspace of just 3 to 8 dimensions, consistent across architectures. This subspace is called the confidence manifold.\n\nThe research demonstrates that centroid distance in the low-dimensional subspace matches trained probe performance (0.90 AUC), enabling few-shot detection, and validates causally through activation steering with learned directions producing 10.9 percentage point changes in error rates.\n\nInternal probes achieve 0.80-0.97 AUC while output-based methods (P(True), semantic entropy) achieve only 0.44–0.64 AUC, indicating that the correctness signal exists internally but is not expressed in outputs.\n\nThe paper was published on February 8, 2026 (arXiv:2602.08159v1)."
    ],
    "durationSeconds": 5.767590664000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c0329ac0-b286-4158-ae9f-6210aff5bec2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T13:15:58.378Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GeKXrjgKvkbPcwpzPDaW5k`</summary>

```json
{
  "query": "Tsujimura Tagade \"LLM Assertiveness Mechanistically Decomposed Emotional Logical\" arXiv 2508.17182"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59a0176f-08c1-4c6c-8f4d-991cb1aa5813",
  "isSidechain": false,
  "requestId": "req_011CbBzNhqf9uJHR4DAaJxiz",
  "type": "assistant",
  "uuid": "1872f7a6-de87-47d3-a73f-8eb930e5825c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcTUuSXGkbuwUt23vxNfhY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 589,
      "cache_read_input_tokens": 33138,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 33138,
          "cache_creation_input_tokens": 589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 589
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

_source line 42 · 2026-05-19T13:16:04.486Z_

<details><summary>↩ Tool result · `toolu_01GeKXrjgKvkbPcwpzPDaW5k`</summary>

```text
Web search results for query: "Tsujimura Tagade "LLM Assertiveness Mechanistically Decomposed Emotional Logical" arXiv 2508.17182"

Links: [{"title":"[2508.17182] LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components","url":"https://arxiv.org/abs/2508.17182"},{"title":"dblp: Hikaru Tsujimura","url":"https://dblp.org/pid/220/2785.html"},{"title":"LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components","url":"https://arxiv.org/html/2508.17182v1"},{"title":"LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components","url":"https://arxiv.org/pdf/2508.17182"},{"title":"LLM Assertiveness can be Mechanistically Decomposed ...","url":"https://www.arxiv.org/pdf/2508.17182"},{"title":"GitHub - gauravfs-14/awesome-mechanistic-interpretability: A carefully curated collection of high-quality libraries, projects, tutorials, research papers, and other essential resources focused on Mechanistic Interpretability, a growing subfield in machine learning interpretability research that aims to reverse-engineer neural networks into understandable computational components. · GitHub","url":"https://github.com/gauravfs-14/awesome-mechanistic-interpretability"},{"title":"Epistemic Integrity in Large Language Models","url":"https://arxiv.org/html/2411.06528v2"}]

I found the paper! Here are the details:

**Title:** "LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components"

**Authors:** Hikaru Tsujimura and Arush Tagade

**arXiv ID:** 2508.17182

**Submission Date:** August 24, 2025 (revised August 31, 2025)

**Summary of the Research:**

The paper addresses how Large Language Models (LLMs) often display overconfidence, presenting information with unwarranted certainty in high-stakes contexts. The researchers used open-sourced Llama 3.2 models fine-tuned on human annotated assertiveness datasets, extracting residual activations across all layers to localize assertive representations.

Their analysis reveals that high-assertive representations decompose into two orthogonal sub-components of emotional and logical clusters, paralleling the dual-route Elaboration Likelihood Model in psychology. Steering vectors derived from these sub-components show distinct causal effects: emotional vectors broadly influence prediction accuracy, while logical vectors exert more localized effects.

You can access the paper directly at https://arxiv.org/abs/2508.17182


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1872f7a6-de87-47d3-a73f-8eb930e5825c",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "6a26d566-9938-4192-9bbb-5aae64f98d1a",
  "toolUseResult": {
    "query": "Tsujimura Tagade \"LLM Assertiveness Mechanistically Decomposed Emotional Logical\" arXiv 2508.17182",
    "results": [
      {
        "tool_use_id": "srvtoolu_016EtxyQsrr4unWJCJ1NB8L2",
        "content": [
          {
            "title": "[2508.17182] LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components",
            "url": "https://arxiv.org/abs/2508.17182"
          },
          {
            "title": "dblp: Hikaru Tsujimura",
            "url": "https://dblp.org/pid/220/2785.html"
          },
          {
            "title": "LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components",
            "url": "https://arxiv.org/html/2508.17182v1"
          },
          {
            "title": "LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components",
            "url": "https://arxiv.org/pdf/2508.17182"
          },
          {
            "title": "LLM Assertiveness can be Mechanistically Decomposed ...",
            "url": "https://www.arxiv.org/pdf/2508.17182"
          },
          {
            "title": "GitHub - gauravfs-14/awesome-mechanistic-interpretability: A carefully curated collection of high-quality libraries, projects, tutorials, research papers, and other essential resources focused on Mechanistic Interpretability, a growing subfield in machine learning interpretability research that aims to reverse-engineer neural networks into understandable computational components. · GitHub",
            "url": "https://github.com/gauravfs-14/awesome-mechanistic-interpretability"
          },
          {
            "title": "Epistemic Integrity in Large Language Models",
            "url": "https://arxiv.org/html/2411.06528v2"
          }
        ]
      },
      "I found the paper! Here are the details:\n\n**Title:** \"LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components\"\n\n**Authors:** Hikaru Tsujimura and Arush Tagade\n\n**arXiv ID:** 2508.17182\n\n**Submission Date:** August 24, 2025 (revised August 31, 2025)\n\n**Summary of the Research:**\n\nThe paper addresses how Large Language Models (LLMs) often display overconfidence, presenting information with unwarranted certainty in high-stakes contexts. The researchers used open-sourced Llama 3.2 models fine-tuned on human annotated assertiveness datasets, extracting residual activations across all layers to localize assertive representations.\n\nTheir analysis reveals that high-assertive representations decompose into two orthogonal sub-components of emotional and logical clusters, paralleling the dual-route Elaboration Likelihood Model in psychology. Steering vectors derived from these sub-components show distinct causal effects: emotional vectors broadly influence prediction accuracy, while logical vectors exert more localized effects.\n\nYou can access the paper directly at https://arxiv.org/abs/2508.17182"
    ],
    "durationSeconds": 6.102175927000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1872f7a6-de87-47d3-a73f-8eb930e5825c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-19T13:16:07.815Z_

Now let me search for critical competing work that might have been missed, and check venue deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a26d566-9938-4192-9bbb-5aae64f98d1a",
  "isSidechain": false,
  "requestId": "req_011CbBzPSibeAEtRp4wDCpX2",
  "type": "assistant",
  "uuid": "7c1d53d5-3bc1-4a1b-b70e-f6e3f0c68911",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M92yM97E8vdNRYhM2VFYJu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 33727,
      "output_tokens": 88,
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
          "output_tokens": 88,
          "cache_read_input_tokens": 33727,
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

### Tool call

_source line 44 · 2026-05-19T13:16:08.271Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XzNr3bR12QHF6mNHNpjeUJ`</summary>

```json
{
  "query": "AAAI 2027 call for papers deadline July 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c1d53d5-3bc1-4a1b-b70e-f6e3f0c68911",
  "isSidechain": false,
  "requestId": "req_011CbBzPSibeAEtRp4wDCpX2",
  "type": "assistant",
  "uuid": "92468792-98af-4e72-ab6e-cb8600541ef4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M92yM97E8vdNRYhM2VFYJu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 33727,
      "output_tokens": 88,
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
          "output_tokens": 88,
          "cache_read_input_tokens": 33727,
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

_source line 45 · 2026-05-19T13:16:12.515Z_

<details><summary>↩ Tool result · `toolu_01XzNr3bR12QHF6mNHNpjeUJ`</summary>

```text
Web search results for query: "AAAI 2027 call for papers deadline July 2026"

Links: [{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"}]

Based on the search results, I found the AAAI 2027 call for papers deadlines:

For AAAI-27, the submission deadlines are:
- June 24, 2026: Open Review submission site opens for paper submission
- July 21, 2026: Abstracts due at 11:59 PM UTC-12
- July 28, 2026: Full papers due at 11:59 PM UTC-12
- July 31, 2026: Supplementary material and code due by 11:59 PM UTC-12

The Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027.

All deadlines are "anywhere on earth" (UTC-12), and track-specific deadlines are listed on their respective CFP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92468792-98af-4e72-ab6e-cb8600541ef4",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "35a259d9-2026-402f-856b-3dccf3f0a885",
  "toolUseResult": {
    "query": "AAAI 2027 call for papers deadline July 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WzzZEt2kgrf3SodXgBdvdD",
        "content": [
          {
            "title": "AI Deadlines – AI Conference Call For Paper Deadlines",
            "url": "http://aideadlines.org/conference/?id=aaai27"
          },
          {
            "title": "AAAI-27 - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-27/"
          },
          {
            "title": "AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/aaai"
          },
          {
            "title": "AAAI Conference on Artificial Intelligence - AAAI",
            "url": "https://aaai.org/conference/aaai/"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "AAAI-27 Main Technical Track - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"
          },
          {
            "title": "Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"
          },
          {
            "title": "🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...",
            "url": "https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"
          },
          {
            "title": "AI/ML Conference Timeline | NIU AI",
            "url": "https://www.niuai.org/resources/conference-timeline/"
          }
        ]
      },
      "Based on the search results, I found the AAAI 2027 call for papers deadlines:\n\nFor AAAI-27, the submission deadlines are:\n- June 24, 2026: Open Review submission site opens for paper submission\n- July 21, 2026: Abstracts due at 11:59 PM UTC-12\n- July 28, 2026: Full papers due at 11:59 PM UTC-12\n- July 31, 2026: Supplementary material and code due by 11:59 PM UTC-12\n\nThe Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027.\n\nAll deadlines are \"anywhere on earth\" (UTC-12), and track-specific deadlines are listed on their respective CFP."
    ],
    "durationSeconds": 4.240974130000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "92468792-98af-4e72-ab6e-cb8600541ef4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-19T13:16:15.005Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RDU8UZT3sB77fiFT8V79Tp`</summary>

```json
{
  "query": "ARR August 2026 submission deadline ACL rolling review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35a259d9-2026-402f-856b-3dccf3f0a885",
  "isSidechain": false,
  "requestId": "req_011CbBzQ2yd6s18zkbwewqhg",
  "type": "assistant",
  "uuid": "36f799a4-337c-4fd0-a67f-912d521e595c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qbcqkY4tSZYn9EqcjDPd8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 34508,
      "output_tokens": 64,
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
          "output_tokens": 64,
          "cache_read_input_tokens": 34508,
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

_source line 47 · 2026-05-19T13:16:19.816Z_

<details><summary>↩ Tool result · `toolu_01RDU8UZT3sB77fiFT8V79Tp`</summary>

```text
Web search results for query: "ARR August 2026 submission deadline ACL rolling review"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, I found information about ARR submission cycles and ACL Rolling Review. However, the search results don't contain specific information about an "August 2026 submission deadline" for ARR.

Here's what I found regarding ARR cycles and deadlines:

ARR switched to 10-week review cycles starting in May 2025, which means fewer cycles per year. For the August 2026 cycle, there is an EACL 2027 submission with an August 3, 2026 final ARR submission date and an October 11, 2026 commitment date.

The search results indicate that instead of 6 cycles a year there will generally be 5 cycles under the new 10-week schedule. The exact August 2026 submission deadline doesn't appear to be explicitly listed in the available search results, but the EACL 2027 venue shows an August 3, 2026 deadline for final submissions to ARR.

If you're looking for more specific details about an August 2026 ARR submission cycle, you may want to check the official ARR website at aclrollingreview.org/dates for the complete schedule.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36f799a4-337c-4fd0-a67f-912d521e595c",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "26841418-382a-49d9-a3d1-1efef56b31f6",
  "toolUseResult": {
    "query": "ARR August 2026 submission deadline ACL rolling review",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AQsUQ9Nd8cAut42hgeiVnX",
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
            "title": "ACLRollingReview (@ReviewAcl) / Posts / X",
            "url": "https://x.com/ReviewAcl"
          },
          {
            "title": "Main Conference - ACL 2026",
            "url": "https://2026.aclweb.org/calls/main_conference_papers/"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          }
        ]
      },
      "Based on the search results, I found information about ARR submission cycles and ACL Rolling Review. However, the search results don't contain specific information about an \"August 2026 submission deadline\" for ARR.\n\nHere's what I found regarding ARR cycles and deadlines:\n\nARR switched to 10-week review cycles starting in May 2025, which means fewer cycles per year. For the August 2026 cycle, there is an EACL 2027 submission with an August 3, 2026 final ARR submission date and an October 11, 2026 commitment date.\n\nThe search results indicate that instead of 6 cycles a year there will generally be 5 cycles under the new 10-week schedule. The exact August 2026 submission deadline doesn't appear to be explicitly listed in the available search results, but the EACL 2027 venue shows an August 3, 2026 deadline for final submissions to ARR.\n\nIf you're looking for more specific details about an August 2026 ARR submission cycle, you may want to check the official ARR website at aclrollingreview.org/dates for the complete schedule."
    ],
    "durationSeconds": 4.806294174999988,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "36f799a4-337c-4fd0-a67f-912d521e595c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "26841418-382a-49d9-a3d1-1efef56b31f6",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Tool call

_source line 50 · 2026-05-19T13:16:22.695Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SgZwUS9d81LazQvyyCbPH7`</summary>

```json
{
  "query": "per-instance adaptive calibration steering LLM confidence correction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26841418-382a-49d9-a3d1-1efef56b31f6",
  "isSidechain": false,
  "requestId": "req_011CbBzQaKXKJwozeVWkFHCS",
  "type": "assistant",
  "uuid": "e9d02d85-1e5c-4f43-b2db-f73a852961a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZAdNX7RmjJojMRqLQmWju",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 35333,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 760,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 35333,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 760
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

_source line 51 · 2026-05-19T13:16:33.364Z_

<details><summary>↩ Tool result · `toolu_01SgZwUS9d81LazQvyyCbPH7`</summary>

```text
Web search results for query: "per-instance adaptive calibration steering LLM confidence correction 2026"

Links: [{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/pdf/2503.02863"},{"title":"Confidence Calibration in LLMs","url":"https://www.emergentmind.com/topics/confidence-calibration-in-llms"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation Ziang Zhou","url":"https://openreview.net/pdf/2dea5d57488bdb780105be0720fc4b246ed074ec.pdf"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/html/2503.02863v2"},{"title":"Focus On This, Not That! Steering LLMs with Adaptive Feature Specification | OpenReview","url":"https://openreview.net/forum?id=rbI5mOUA8Z"},{"title":"Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection","url":"https://arxiv.org/html/2603.06604"},{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework","url":"https://arxiv.org/html/2503.02863v1"}]

Based on the search results, here's what I found regarding per-instance adaptive calibration steering for LLM confidence correction in 2026:

## SteerConf: A Leading Framework

SteerConf introduces three key components: (1) a steering prompt strategy that guides LLMs to produce confidence scores in specified directions (e.g., conservative or optimistic) by leveraging prompts with varying steering levels; (2) a steered confidence consistency measure that quantifies alignment across multiple steered confidences to enhance calibration; and (3) a steered confidence calibration method that aggregates confidence scores using consistency measures and applies linear quantization for answer selection.

SteerConf operates without additional training or fine-tuning, making it broadly applicable to existing LLMs. Experiments on seven benchmarks spanning professional knowledge, common sense, ethics, and reasoning tasks, using advanced LLM models (GPT-3.5, LLaMA 3, GPT-4), demonstrate that SteerConf significantly outperforms existing methods, often by a significant margin.

## Current Research Directions

Practical guidelines for combining black-box post-hoc methods with lightweight plug-and-play calibration modules, and for scaling to very large, multilingual, or high-noise deployment settings have emerged as of January 2026.

This represents the state-of-the-art in per-instance adaptive calibration approaches for improving LLM confidence reliability and alignment with actual accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9d02d85-1e5c-4f43-b2db-f73a852961a8",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "debf43be-a441-4d61-88d3-7d78c927e4da",
  "toolUseResult": {
    "query": "per-instance adaptive calibration steering LLM confidence correction 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UWyefMNmBofywKMFbp5chw",
        "content": [
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/pdf/2503.02863"
          },
          {
            "title": "Confidence Calibration in LLMs",
            "url": "https://www.emergentmind.com/topics/confidence-calibration-in-llms"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation Ziang Zhou",
            "url": "https://openreview.net/pdf/2dea5d57488bdb780105be0720fc4b246ed074ec.pdf"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/html/2503.02863v2"
          },
          {
            "title": "Focus On This, Not That! Steering LLMs with Adaptive Feature Specification | OpenReview",
            "url": "https://openreview.net/forum?id=rbI5mOUA8Z"
          },
          {
            "title": "Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection",
            "url": "https://arxiv.org/html/2603.06604"
          },
          {
            "title": "Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework",
            "url": "https://arxiv.org/html/2503.02863v1"
          }
        ]
      },
      "Based on the search results, here's what I found regarding per-instance adaptive calibration steering for LLM confidence correction in 2026:\n\n## SteerConf: A Leading Framework\n\nSteerConf introduces three key components: (1) a steering prompt strategy that guides LLMs to produce confidence scores in specified directions (e.g., conservative or optimistic) by leveraging prompts with varying steering levels; (2) a steered confidence consistency measure that quantifies alignment across multiple steered confidences to enhance calibration; and (3) a steered confidence calibration method that aggregates confidence scores using consistency measures and applies linear quantization for answer selection.\n\nSteerConf operates without additional training or fine-tuning, making it broadly applicable to existing LLMs. Experiments on seven benchmarks spanning professional knowledge, common sense, ethics, and reasoning tasks, using advanced LLM models (GPT-3.5, LLaMA 3, GPT-4), demonstrate that SteerConf significantly outperforms existing methods, often by a significant margin.\n\n## Current Research Directions\n\nPractical guidelines for combining black-box post-hoc methods with lightweight plug-and-play calibration modules, and for scaling to very large, multilingual, or high-noise deployment settings have emerged as of January 2026.\n\nThis represents the state-of-the-art in per-instance adaptive calibration approaches for improving LLM confidence reliability and alignment with actual accuracy."
    ],
    "durationSeconds": 10.664636988000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e9d02d85-1e5c-4f43-b2db-f73a852961a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 52 · 2026-05-19T13:16:33.367Z_

```json
{
  "parentUuid": "debf43be-a441-4d61-88d3-7d78c927e4da",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "56b1dfea-99ff-4816-8182-1cf8d884384b",
  "timestamp": "2026-05-19T13:16:33.367Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 53 · 2026-05-19T13:16:36.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A5nJUDC9AHgEkdh3LNkUgH`</summary>

```json
{
  "query": "multi-bias decomposition activation space LLM steering routing different corrections 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56b1dfea-99ff-4816-8182-1cf8d884384b",
  "isSidechain": false,
  "requestId": "req_011CbBzRa8PsWeThXqyy3gVi",
  "type": "assistant",
  "uuid": "d8ce089f-cb6a-415c-8491-406a4e1ead72",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuEXiTqhBocft63d1WtUhb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 36093,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 859,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 36093,
          "cache_creation_input_tokens": 859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 859
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

_source line 54 · 2026-05-19T13:16:43.256Z_

<details><summary>↩ Tool result · `toolu_01A5nJUDC9AHgEkdh3LNkUgH`</summary>

```text
Web search results for query: "multi-bias decomposition activation space LLM steering routing different corrections 2025 2026"

Links: [{"title":"Steering Vectors: Beamforming to LLM Control","url":"https://www.emergentmind.com/topics/steering-vectors"},{"title":"Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs","url":"https://arxiv.org/html/2503.05371v2"},{"title":"Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs","url":"https://arxiv.org/pdf/2503.05371"},{"title":"Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence","url":"https://arxiv.org/pdf/2604.08169"},{"title":"[2503.05371] Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs","url":"https://arxiv.org/abs/2503.05371"},{"title":"FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering","url":"https://arxiv.org/pdf/2504.14492"},{"title":"Curveball Steering: The Right Direction To Steer Isn't Always Linear","url":"https://arxiv.org/pdf/2603.09313"},{"title":"Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250809019D/abstract"}]

I found relevant research on LLM steering and bias mitigation. Here are the key findings:

## Recent Research on Steering Vectors and Bias Mitigation

Recent work applies steering vectors to modify model activations, computing multiple steering vectors each corresponding to different social bias axes such as age, gender, or race.

The FairSteer framework operates through three steps: biased activation detection using lightweight linear classifiers, debiasing steering vector computation derived from contrastive prompt pairs, and dynamic activation steering to adjust activations during inference.

## Multi-Bias Approach

One approach computes 8 steering vectors on the BBQ dataset, achieving average improvements of 12.8% on BBQ, 8.3% on CLEAR-Bias, and 1% on StereoSet.

## Theoretical Foundations

Research demonstrates that fairness-related features can be encoded into separable directions in the hidden activation space, based on the linear representation hypothesis where semantic features are encoded as linearly separable directions in LLM activation spaces.

## Activation Space Challenges

Recent work reveals geometric distortions in LLM activation spaces by learning latent manifolds using variational autoencoders and estimating geometric distortion as the ratio between geodesic and Euclidean distances.

The search results show active research in 2025 on steering vector methods for bias mitigation in LLMs using activation space interventions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8ce089f-cb6a-415c-8491-406a4e1ead72",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "178617ad-8a0a-4a1c-9aad-ed4fd7736b31",
  "toolUseResult": {
    "query": "multi-bias decomposition activation space LLM steering routing different corrections 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MnTgsPSPX9xjikMGdyyJ9k",
        "content": [
          {
            "title": "Steering Vectors: Beamforming to LLM Control",
            "url": "https://www.emergentmind.com/topics/steering-vectors"
          },
          {
            "title": "Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs",
            "url": "https://arxiv.org/html/2503.05371v2"
          },
          {
            "title": "Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs",
            "url": "https://arxiv.org/pdf/2503.05371"
          },
          {
            "title": "Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence",
            "url": "https://arxiv.org/pdf/2604.08169"
          },
          {
            "title": "[2503.05371] Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs",
            "url": "https://arxiv.org/abs/2503.05371"
          },
          {
            "title": "FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering",
            "url": "https://arxiv.org/pdf/2504.14492"
          },
          {
            "title": "Curveball Steering: The Right Direction To Steer Isn't Always Linear",
            "url": "https://arxiv.org/pdf/2603.09313"
          },
          {
            "title": "Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250809019D/abstract"
          }
        ]
      },
      "I found relevant research on LLM steering and bias mitigation. Here are the key findings:\n\n## Recent Research on Steering Vectors and Bias Mitigation\n\nRecent work applies steering vectors to modify model activations, computing multiple steering vectors each corresponding to different social bias axes such as age, gender, or race.\n\nThe FairSteer framework operates through three steps: biased activation detection using lightweight linear classifiers, debiasing steering vector computation derived from contrastive prompt pairs, and dynamic activation steering to adjust activations during inference.\n\n## Multi-Bias Approach\n\nOne approach computes 8 steering vectors on the BBQ dataset, achieving average improvements of 12.8% on BBQ, 8.3% on CLEAR-Bias, and 1% on StereoSet.\n\n## Theoretical Foundations\n\nResearch demonstrates that fairness-related features can be encoded into separable directions in the hidden activation space, based on the linear representation hypothesis where semantic features are encoded as linearly separable directions in LLM activation spaces.\n\n## Activation Space Challenges\n\nRecent work reveals geometric distortions in LLM activation spaces by learning latent manifolds using variational autoencoders and estimating geometric distortion as the ratio between geodesic and Euclidean distances.\n\nThe search results show active research in 2025 on steering vector methods for bias mitigation in LLMs using activation space interventions."
    ],
    "durationSeconds": 6.929213399,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d8ce089f-cb6a-415c-8491-406a4e1ead72",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T13:16:46.319Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SMsmq7AhpfK3bKU1NwP8tk`</summary>

```json
{
  "query": "\"Curveball Steering\" nonlinear steering direction LLM arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "178617ad-8a0a-4a1c-9aad-ed4fd7736b31",
  "isSidechain": false,
  "requestId": "req_011CbBzSJTbYMiWJ7hX2CDYW",
  "type": "assistant",
  "uuid": "10154711-2c27-4ca5-a9b7-59374f2b7b78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BB2V6URretMYK2fZmneBsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 36952,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 36952,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 800
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

_source line 56 · 2026-05-19T13:16:55.430Z_

<details><summary>↩ Tool result · `toolu_01SMsmq7AhpfK3bKU1NwP8tk`</summary>

```text
Web search results for query: ""Curveball Steering" nonlinear steering direction LLM arXiv 2026"

Links: [{"title":"[2603.09313] Curveball Steering: The Right Direction To Steer Isn't Always Linear","url":"https://arxiv.org/abs/2603.09313"},{"title":"Curveball Steering: The Right Direction To Steer Isn't Always Linear","url":"https://arxiv.org/pdf/2603.09313"},{"title":"Curveball Steering: The Right Direction To Steer Isn’t Always Linear","url":"https://arxiv.org/html/2603.09313v2"},{"title":"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/html/2605.05892"},{"title":"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment","url":"https://arxiv.org/html/2602.17560v1"}]

I found detailed information about "Curveball Steering" from the arXiv search results:

## Curveball Steering Overview

Curveball steering is a nonlinear steering method based on polynomial kernel PCA that performs interventions in a feature space, better respecting the learned activation geometry.

## The Problem It Addresses

Existing steering methods rely on the Linear Representation Hypothesis, assuming behavioral attributes can be manipulated using global linear directions, but such linear interventions often behave inconsistently in practice.

## Motivation

The researchers observed substantial and concept-dependent geometric distortions in LLM activation spaces, indicating that activation spaces are not well-approximated by a globally linear geometry.

## Key Results

Curveball steering consistently outperforms linear PCA-based steering, particularly in regimes exhibiting strong geometric distortion, suggesting that geometry-aware, nonlinear steering provides a principled alternative to global, linear interventions.

The paper (arXiv:2603.09313) was submitted in March 2026 and demonstrates that the assumption of linear steering directions in LLMs is fundamentally limited, and that nonlinear approaches can be more effective for controlling LLM behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10154711-2c27-4ca5-a9b7-59374f2b7b78",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "a00ebb6b-f7bd-44e2-a474-feb1a997ee53",
  "toolUseResult": {
    "query": "\"Curveball Steering\" nonlinear steering direction LLM arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0184iPYMGvzNd6DMf5yDR685",
        "content": [
          {
            "title": "[2603.09313] Curveball Steering: The Right Direction To Steer Isn't Always Linear",
            "url": "https://arxiv.org/abs/2603.09313"
          },
          {
            "title": "Curveball Steering: The Right Direction To Steer Isn't Always Linear",
            "url": "https://arxiv.org/pdf/2603.09313"
          },
          {
            "title": "Curveball Steering: The Right Direction To Steer Isn’t Always Linear",
            "url": "https://arxiv.org/html/2603.09313v2"
          },
          {
            "title": "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/html/2605.05892"
          },
          {
            "title": "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment",
            "url": "https://arxiv.org/html/2602.17560v1"
          }
        ]
      },
      "I found detailed information about \"Curveball Steering\" from the arXiv search results:\n\n## Curveball Steering Overview\n\nCurveball steering is a nonlinear steering method based on polynomial kernel PCA that performs interventions in a feature space, better respecting the learned activation geometry.\n\n## The Problem It Addresses\n\nExisting steering methods rely on the Linear Representation Hypothesis, assuming behavioral attributes can be manipulated using global linear directions, but such linear interventions often behave inconsistently in practice.\n\n## Motivation\n\nThe researchers observed substantial and concept-dependent geometric distortions in LLM activation spaces, indicating that activation spaces are not well-approximated by a globally linear geometry.\n\n## Key Results\n\nCurveball steering consistently outperforms linear PCA-based steering, particularly in regimes exhibiting strong geometric distortion, suggesting that geometry-aware, nonlinear steering provides a principled alternative to global, linear interventions.\n\nThe paper (arXiv:2603.09313) was submitted in March 2026 and demonstrates that the assumption of linear steering directions in LLMs is fundamentally limited, and that nonlinear approaches can be more effective for controlling LLM behavior."
    ],
    "durationSeconds": 9.105385516000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "10154711-2c27-4ca5-a9b7-59374f2b7b78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-19T13:16:59.778Z_

This is very relevant — let me check this more closely and look for more potential competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a00ebb6b-f7bd-44e2-a474-feb1a997ee53",
  "isSidechain": false,
  "requestId": "req_011CbBzTCTxmUDdmRYwpqZVP",
  "type": "assistant",
  "uuid": "012d12f2-986f-4cde-8d77-58a8a1064864",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nqyHmwP8wvxwLHWZXEbSS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 37752,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 37752,
          "cache_creation_input_tokens": 618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 618
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

_source line 58 · 2026-05-19T13:17:01.336Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EMuTvfNfg2heMPtE3Xb9Uf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.09313",
  "prompt": "Extract the full abstract, key methods, and main results. Does this paper address calibration specifically? Does it perform per-instance routing between linear and non-linear steering? What models and benchmarks are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "012d12f2-986f-4cde-8d77-58a8a1064864",
  "isSidechain": false,
  "requestId": "req_011CbBzTCTxmUDdmRYwpqZVP",
  "type": "assistant",
  "uuid": "18d6527f-c29a-4853-8198-8913587a42ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nqyHmwP8wvxwLHWZXEbSS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 37752,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 37752,
          "cache_creation_input_tokens": 618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 618
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

_source line 59 · 2026-05-19T13:17:07.696Z_

<details><summary>↩ Tool result · `toolu_01EMuTvfNfg2heMPtE3Xb9Uf`</summary>

```text
# Analysis of "Curveball Steering" Paper

## Full Abstract
"Activation steering is a widely used approach for controlling large language model (LLM) behavior by intervening on internal representations. Existing methods largely rely on the Linear Representation Hypothesis, assuming behavioral attributes can be manipulated using global linear directions. In practice, however, such linear interventions often behave inconsistently. We question this assumption by analyzing the intrinsic geometry of LLM activation spaces. Measuring geometric distortion via the ratio of geodesic to Euclidean distances, we observe substantial and concept-dependent distortions, indicating that activation spaces are not well-approximated by a globally linear geometry. Motivated by this, we propose "Curveball steering", a nonlinear steering method based on polynomial kernel PCA that performs interventions in a feature space, better respecting the learned activation geometry. Curveball steering consistently outperforms linear PCA-based steering, particularly in regimes exhibiting strong geometric distortion, suggesting that geometry-aware, nonlinear steering provides a principled alternative to global, linear interventions."

## Key Methods
- Analyzes geometric properties of LLM activation spaces through geodesic-to-Euclidean distance ratios
- Proposes polynomial kernel PCA-based steering to respect learned activation geometry
- Compares performance against linear PCA-based steering approaches

## Main Results
Nonlinear steering achieves superior performance relative to linear methods, particularly when geometric distortion is pronounced.

## Regarding Your Specific Questions

**Calibration addressed?** Not mentioned in provided content.

**Per-instance routing?** No evidence in the abstract or submission details of adaptive selection between methods.

**Models/benchmarks?** Not specified in this webpage excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18d6527f-c29a-4853-8198-8913587a42ac",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "8f60ac49-2de8-417f-b4c9-a0da5acea6f3",
  "toolUseResult": {
    "bytes": 46902,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of \"Curveball Steering\" Paper\n\n## Full Abstract\n\"Activation steering is a widely used approach for controlling large language model (LLM) behavior by intervening on internal representations. Existing methods largely rely on the Linear Representation Hypothesis, assuming behavioral attributes can be manipulated using global linear directions. In practice, however, such linear interventions often behave inconsistently. We question this assumption by analyzing the intrinsic geometry of LLM activation spaces. Measuring geometric distortion via the ratio of geodesic to Euclidean distances, we observe substantial and concept-dependent distortions, indicating that activation spaces are not well-approximated by a globally linear geometry. Motivated by this, we propose \"Curveball steering\", a nonlinear steering method based on polynomial kernel PCA that performs interventions in a feature space, better respecting the learned activation geometry. Curveball steering consistently outperforms linear PCA-based steering, particularly in regimes exhibiting strong geometric distortion, suggesting that geometry-aware, nonlinear steering provides a principled alternative to global, linear interventions.\"\n\n## Key Methods\n- Analyzes geometric properties of LLM activation spaces through geodesic-to-Euclidean distance ratios\n- Proposes polynomial kernel PCA-based steering to respect learned activation geometry\n- Compares performance against linear PCA-based steering approaches\n\n## Main Results\nNonlinear steering achieves superior performance relative to linear methods, particularly when geometric distortion is pronounced.\n\n## Regarding Your Specific Questions\n\n**Calibration addressed?** Not mentioned in provided content.\n\n**Per-instance routing?** No evidence in the abstract or submission details of adaptive selection between methods.\n\n**Models/benchmarks?** Not specified in this webpage excerpt.",
    "durationMs": 6356,
    "url": "https://arxiv.org/abs/2603.09313"
  },
  "sourceToolAssistantUUID": "18d6527f-c29a-4853-8198-8913587a42ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-19T13:17:10.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KsQKPot7q8H2VMymPRJSVr`</summary>

```json
{
  "query": "\"Beyond Steering Vector\" flow-based activation steering arXiv 2605.05892 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f60ac49-2de8-417f-b4c9-a0da5acea6f3",
  "isSidechain": false,
  "requestId": "req_011CbBzU7HSgdyZkuuxK24t3",
  "type": "assistant",
  "uuid": "5fd5f24d-e0e2-4aaa-b2f4-7b1d93cf3637",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsXEksCVLEv7oK2G4WJciG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 543,
      "cache_read_input_tokens": 38370,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 38370,
          "cache_creation_input_tokens": 543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 543
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

_source line 61 · 2026-05-19T13:17:18.714Z_

<details><summary>↩ Tool result · `toolu_01KsQKPot7q8H2VMymPRJSVr`</summary>

```text
Web search results for query: ""Beyond Steering Vector" flow-based activation steering arXiv 2605.05892 2026"

Links: [{"title":"[2605.05892] Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/abs/2605.05892"},{"title":"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/html/2605.05892"},{"title":"Extending Activation Steering to Broad Skills and Multiple Behaviours","url":"https://arxiv.org/pdf/2403.05767"},{"title":"Steering Large Language Models using Conceptors: Improving Addition-Based Activation Engineering","url":"https://arxiv.org/pdf/2410.16314"},{"title":"On the Non-Identifiability of Steering Vectors in Large Language Models","url":"https://arxiv.org/pdf/2602.06801"},{"title":"Improving Activation Steering in Language Models with Mean-Centring","url":"https://arxiv.org/pdf/2312.03813"},{"title":"Understanding (Un)Reliability of Steering Vectors in Language Models","url":"https://arxiv.org/pdf/2505.22637"},{"title":"Interpretable Steering of Large Language Models with Feature Guided   Activation Additions","url":"https://arxiv.org/pdf/2501.09929"}]

I found the paper you're looking for. Here's what I found about it:

## "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention"

**Paper Details:**
- arXiv: 2605.05892, submitted on May 7, 2026
- **Authors:** Zehao Jin, Ruixuan Deng, Junran Wang, Xinjie Shen, and Chao Zhang from Georgia Institute of Technology

**Main Contribution:**

Activation steering has emerged as a promising alternative for controlling language-model behavior at inference time by modifying intermediate representations while keeping model parameters frozen. However, large-scale evaluations such as AxBench show that existing steering methods are often outperformed by simple in-context prompting and generalize poorly to unseen concepts.

**The Proposed Solution:**

The paper proposes FLAS (Flow-based Activation Steering), which learns a general, concept-conditioned velocity field that transports unsteered activations to steered ones without relying on the assumptions of prior methods. On AxBench, FLAS is the first learned method to consistently outperform prompting, reaching held-out harmonic means of 1.015 on Gemma-2-2B-IT and 1.113 on Gemma-2-9B-IT.

The paper addresses the limitations of existing steering methods by moving beyond the restrictive assumptions of traditional steering vector approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fd5f24d-e0e2-4aaa-b2f4-7b1d93cf3637",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "4d66f9fd-dd8b-45eb-9ea9-8d37ac9f0194",
  "toolUseResult": {
    "query": "\"Beyond Steering Vector\" flow-based activation steering arXiv 2605.05892 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X34Y8QfkdeszQfdY4DGCcu",
        "content": [
          {
            "title": "[2605.05892] Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/abs/2605.05892"
          },
          {
            "title": "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/html/2605.05892"
          },
          {
            "title": "Extending Activation Steering to Broad Skills and Multiple Behaviours",
            "url": "https://arxiv.org/pdf/2403.05767"
          },
          {
            "title": "Steering Large Language Models using Conceptors: Improving Addition-Based Activation Engineering",
            "url": "https://arxiv.org/pdf/2410.16314"
          },
          {
            "title": "On the Non-Identifiability of Steering Vectors in Large Language Models",
            "url": "https://arxiv.org/pdf/2602.06801"
          },
          {
            "title": "Improving Activation Steering in Language Models with Mean-Centring",
            "url": "https://arxiv.org/pdf/2312.03813"
          },
          {
            "title": "Understanding (Un)Reliability of Steering Vectors in Language Models",
            "url": "https://arxiv.org/pdf/2505.22637"
          },
          {
            "title": "Interpretable Steering of Large Language Models with Feature Guided   Activation Additions",
            "url": "https://arxiv.org/pdf/2501.09929"
          }
        ]
      },
      "I found the paper you're looking for. Here's what I found about it:\n\n## \"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention\"\n\n**Paper Details:**\n- arXiv: 2605.05892, submitted on May 7, 2026\n- **Authors:** Zehao Jin, Ruixuan Deng, Junran Wang, Xinjie Shen, and Chao Zhang from Georgia Institute of Technology\n\n**Main Contribution:**\n\nActivation steering has emerged as a promising alternative for controlling language-model behavior at inference time by modifying intermediate representations while keeping model parameters frozen. However, large-scale evaluations such as AxBench show that existing steering methods are often outperformed by simple in-context prompting and generalize poorly to unseen concepts.\n\n**The Proposed Solution:**\n\nThe paper proposes FLAS (Flow-based Activation Steering), which learns a general, concept-conditioned velocity field that transports unsteered activations to steered ones without relying on the assumptions of prior methods. On AxBench, FLAS is the first learned method to consistently outperform prompting, reaching held-out harmonic means of 1.015 on Gemma-2-2B-IT and 1.113 on Gemma-2-9B-IT.\n\nThe paper addresses the limitations of existing steering methods by moving beyond the restrictive assumptions of traditional steering vector approaches."
    ],
    "durationSeconds": 8.146528418,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5fd5f24d-e0e2-4aaa-b2f4-7b1d93cf3637",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "4d66f9fd-dd8b-45eb-9ea9-8d37ac9f0194",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Tool call

_source line 64 · 2026-05-19T13:17:21.215Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VgoMdddfjmPxwJ5FGT3ai5`</summary>

```json
{
  "query": "FairSteer dynamic activation steering bias detection routing per-instance 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d66f9fd-dd8b-45eb-9ea9-8d37ac9f0194",
  "isSidechain": false,
  "requestId": "req_011CbBzUv2oGSv1D2NCXH4xv",
  "type": "assistant",
  "uuid": "25a9bf2c-b247-4ef5-83b3-1c83799161d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTs82WUjtNTUZEryPxvJQL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 38913,
      "output_tokens": 67,
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
          "output_tokens": 67,
          "cache_read_input_tokens": 38913,
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

_source line 65 · 2026-05-19T13:17:27.227Z_

<details><summary>↩ Tool result · `toolu_01VgoMdddfjmPxwJ5FGT3ai5`</summary>

```text
Web search results for query: "FairSteer dynamic activation steering bias detection routing per-instance 2026"

Links: [{"title":"FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.589/"},{"title":"FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering","url":"https://arxiv.org/html/2504.14492"},{"title":"FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering","url":"https://arxiv.org/pdf/2504.14492"},{"title":"[2504.14492] FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering","url":"https://arxiv.org/abs/2504.14492"},{"title":"[Literature Review] FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering","url":"https://www.themoonlight.io/en/review/fairsteer-inference-time-debiasing-for-llms-with-dynamic-activation-steering"},{"title":"dblp: FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering.","url":"https://dblp.org/rec/conf/acl/LiFCGG0L25.html"}]

I found research on FairSteer! Here are the key findings:

FairSteer is a novel inference-time debiasing framework for LLMs that doesn't require customized prompt design or model retraining. 

FairSteer operates in three steps: biased activation detection, debiasing steering vector (DSV) computation, and dynamic activation steering. More specifically:

- It trains a lightweight linear classifier to detect bias signatures in activations, and then computes DSVs as intervention directions derived from small contrastive prompt pairs.

- During inference, dynamic activation steering acts as a plug-in and is applied only when a bias is detected—when an input prompt is processed, the classifier computes the bias probability, and if it indicates biased activation, the activations are adjusted.

The research demonstrates that fairness-related features are encoded in separable directions within the hidden activation space of LLMs, with bias signatures exhibiting over 90% linear separability in intermediate layers.

The paper was published in ACL Findings 2025 by Yichen Li, Zhiting Fan, Ruizhe Chen, Xiaotang Gai, Luqi Gong, Yan Zhang, and Zuozhu Liu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25a9bf2c-b247-4ef5-83b3-1c83799161d1",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "514f8c19-b79b-424b-9a41-328c23e569eb",
  "toolUseResult": {
    "query": "FairSteer dynamic activation steering bias detection routing per-instance 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011P1RfYARa8Eh72MiUisZ7o",
        "content": [
          {
            "title": "FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.589/"
          },
          {
            "title": "FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering",
            "url": "https://arxiv.org/html/2504.14492"
          },
          {
            "title": "FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering",
            "url": "https://arxiv.org/pdf/2504.14492"
          },
          {
            "title": "[2504.14492] FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering",
            "url": "https://arxiv.org/abs/2504.14492"
          },
          {
            "title": "[Literature Review] FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering",
            "url": "https://www.themoonlight.io/en/review/fairsteer-inference-time-debiasing-for-llms-with-dynamic-activation-steering"
          },
          {
            "title": "dblp: FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering.",
            "url": "https://dblp.org/rec/conf/acl/LiFCGG0L25.html"
          }
        ]
      },
      "I found research on FairSteer! Here are the key findings:\n\nFairSteer is a novel inference-time debiasing framework for LLMs that doesn't require customized prompt design or model retraining. \n\nFairSteer operates in three steps: biased activation detection, debiasing steering vector (DSV) computation, and dynamic activation steering. More specifically:\n\n- It trains a lightweight linear classifier to detect bias signatures in activations, and then computes DSVs as intervention directions derived from small contrastive prompt pairs.\n\n- During inference, dynamic activation steering acts as a plug-in and is applied only when a bias is detected—when an input prompt is processed, the classifier computes the bias probability, and if it indicates biased activation, the activations are adjusted.\n\nThe research demonstrates that fairness-related features are encoded in separable directions within the hidden activation space of LLMs, with bias signatures exhibiting over 90% linear separability in intermediate layers.\n\nThe paper was published in ACL Findings 2025 by Yichen Li, Zhiting Fan, Ruizhe Chen, Xiaotang Gai, Luqi Gong, Yan Zhang, and Zuozhu Liu."
    ],
    "durationSeconds": 6.008372709000017,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "25a9bf2c-b247-4ef5-83b3-1c83799161d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-19T13:17:30.029Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ch2JNNQnoDT1Rrd51NRtir`</summary>

```json
{
  "query": "specificity ratio activation steering entanglement task-critical computation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "514f8c19-b79b-424b-9a41-328c23e569eb",
  "isSidechain": false,
  "requestId": "req_011CbBzVYRoxrTVq9AYH9PZs",
  "type": "assistant",
  "uuid": "9bc232ef-af0b-4bf6-ad2a-d6943d25630e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JUwsLryzjLwAzHxGU8ktWb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 39694,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 39694,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 67 · 2026-05-19T13:17:36.748Z_

<details><summary>↩ Tool result · `toolu_01Ch2JNNQnoDT1Rrd51NRtir`</summary>

```text
Web search results for query: "specificity ratio activation steering entanglement task-critical computation 2026"

Links: [{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Super-Activation of Quantum Steering","url":"https://arxiv.org/pdf/1610.01037"},{"title":"Hidden Steering Nonlocality in Quantum Networks","url":"https://arxiv.org/pdf/2303.11902"},{"title":"Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY","url":"https://arxiv.org/pdf/2510.02917"},{"title":"Extending Activation Steering to Broad Skills and Multiple Behaviours","url":"https://arxiv.org/pdf/2403.05767"},{"title":"Steering Awareness: Detecting Activation Steering from Within","url":"https://arxiv.org/html/2511.21399v3"}]

I found several relevant search results related to your query. Here's what the search uncovered:

## Activation Steering and Task-Critical Computation (2026)

Late layers (last 25%) work best for behavioral steering, as these layers encode high-level semantic properties including intent, style, and register. Additionally, steering directions demand categorical exclusivity for clean intervention, which relates to the specificity aspect of your query.

## Entanglement and Steering in Quantum Contexts

The search also returned quantum physics research, which discusses a different type of steering. Quantum steering is a form of nonlocality that is intermediate between entanglement and Bell nonlocality. Instances of steerability activation are observed in nonlinear networks.

## Mechanistic Interpretability Approaches

Recent 2026 research on mechanistic interpretability discusses how pre-trained autoencoders decompose activations into interpretable latents, and complementary metrics are applied based on each mechanism's computational role.

The search results include a 2026 practitioner's guide on activation steering and several peer-reviewed papers from 2026 on related topics, though the results don't specifically address a "specificity ratio" metric in the exact combination you mentioned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bc232ef-af0b-4bf6-ad2a-d6943d25630e",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "303e532a-09f1-4aee-984f-71bbb829eddb",
  "toolUseResult": {
    "query": "specificity ratio activation steering entanglement task-critical computation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ETDRLReNgbJCu9CbUHGkDN",
        "content": [
          {
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "Super-Activation of Quantum Steering",
            "url": "https://arxiv.org/pdf/1610.01037"
          },
          {
            "title": "Hidden Steering Nonlocality in Quantum Networks",
            "url": "https://arxiv.org/pdf/2303.11902"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY",
            "url": "https://arxiv.org/pdf/2510.02917"
          },
          {
            "title": "Extending Activation Steering to Broad Skills and Multiple Behaviours",
            "url": "https://arxiv.org/pdf/2403.05767"
          },
          {
            "title": "Steering Awareness: Detecting Activation Steering from Within",
            "url": "https://arxiv.org/html/2511.21399v3"
          }
        ]
      },
      "I found several relevant search results related to your query. Here's what the search uncovered:\n\n## Activation Steering and Task-Critical Computation (2026)\n\nLate layers (last 25%) work best for behavioral steering, as these layers encode high-level semantic properties including intent, style, and register. Additionally, steering directions demand categorical exclusivity for clean intervention, which relates to the specificity aspect of your query.\n\n## Entanglement and Steering in Quantum Contexts\n\nThe search also returned quantum physics research, which discusses a different type of steering. Quantum steering is a form of nonlocality that is intermediate between entanglement and Bell nonlocality. Instances of steerability activation are observed in nonlinear networks.\n\n## Mechanistic Interpretability Approaches\n\nRecent 2026 research on mechanistic interpretability discusses how pre-trained autoencoders decompose activations into interpretable latents, and complementary metrics are applied based on each mechanism's computational role.\n\nThe search results include a 2026 practitioner's guide on activation steering and several peer-reviewed papers from 2026 on related topics, though the results don't specifically address a \"specificity ratio\" metric in the exact combination you mentioned."
    ],
    "durationSeconds": 6.7147486280000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9bc232ef-af0b-4bf6-ad2a-d6943d25630e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-19T13:17:41.105Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MrgrkV1tDQ8nmovd1uLQWx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05715",
  "prompt": "Extract the full abstract, key findings, and specific numbers mentioned (specificity ratio, balanced accuracy, steering results Δ, non-linear MLP results, AUROC for selective abstention). What model was studied? What is the key recommendation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "303e532a-09f1-4aee-984f-71bbb829eddb",
  "isSidechain": false,
  "requestId": "req_011CbBzWFAWnUGQg8C2fXxkc",
  "type": "assistant",
  "uuid": "39f34f25-07cf-4cd9-a2b4-790e9a4b2218",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQsa3jk6CR6hjPTPF5z71P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 40413,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 623,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 40413,
          "cache_creation_input_tokens": 623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 623
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

_source line 69 · 2026-05-19T13:17:47.567Z_

<details><summary>↩ Tool result · `toolu_01MrgrkV1tDQ8nmovd1uLQWx`</summary>

```text
# Research Summary: Medical LLM Steering Study

## Full Abstract
"Can linearly decodable failure signals in LLM hidden states be leveraged to correct those failures? We investigate this classification-correction gap via Overthinking (OT)--a stable behavioral regime (Jaccard >= 0.81, 94% inter-annotator agreement) in medical QA where models answer correctly under resampling yet fail in extended chain-of-thought."

## Key Findings

**Model Studied:** Qwen2.5-7B (with cross-architecture validation)

**Specific Numbers:**
- Linear decodability: 71.6% balanced accuracy (p < 10⁻¹⁶)
- Fixed steering effectiveness: Δ ≈ 0 across 29 configurations
- Representational overlap: 85-88% with task-critical computation
- Specificity ratio: ≤ 0.152
- Non-targeted steering damage: -12.1 percentage points
- LEACE concept erasure damage: -3.6pp (p=0.01)
- Random erasure control: Δ = +0.3pp
- Selective abstention AUROC: 0.610 (outperforming all baseline methods, p=0.009)

## Key Recommendation

Although fixed linear steering proved ineffective for correction, the research demonstrates that decodable failure patterns enable "selective abstention (held-out AUROC=0.610, exceeding all five uncertainty baselines, p=0.009)" for improved reliability estimation rather than direct error correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39f34f25-07cf-4cd9-a2b4-790e9a4b2218",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "da470192-5928-4a68-88f3-23c0ff0295c5",
  "toolUseResult": {
    "bytes": 46810,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Summary: Medical LLM Steering Study\n\n## Full Abstract\n\"Can linearly decodable failure signals in LLM hidden states be leveraged to correct those failures? We investigate this classification-correction gap via Overthinking (OT)--a stable behavioral regime (Jaccard >= 0.81, 94% inter-annotator agreement) in medical QA where models answer correctly under resampling yet fail in extended chain-of-thought.\"\n\n## Key Findings\n\n**Model Studied:** Qwen2.5-7B (with cross-architecture validation)\n\n**Specific Numbers:**\n- Linear decodability: 71.6% balanced accuracy (p < 10⁻¹⁶)\n- Fixed steering effectiveness: Δ ≈ 0 across 29 configurations\n- Representational overlap: 85-88% with task-critical computation\n- Specificity ratio: ≤ 0.152\n- Non-targeted steering damage: -12.1 percentage points\n- LEACE concept erasure damage: -3.6pp (p=0.01)\n- Random erasure control: Δ = +0.3pp\n- Selective abstention AUROC: 0.610 (outperforming all baseline methods, p=0.009)\n\n## Key Recommendation\n\nAlthough fixed linear steering proved ineffective for correction, the research demonstrates that decodable failure patterns enable \"selective abstention (held-out AUROC=0.610, exceeding all five uncertainty baselines, p=0.009)\" for improved reliability estimation rather than direct error correction.",
    "durationMs": 6457,
    "url": "https://arxiv.org/abs/2605.05715"
  },
  "sourceToolAssistantUUID": "39f34f25-07cf-4cd9-a2b4-790e9a4b2218",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-19T13:17:50.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012kHKs31xEdn9RDkkNiRnET`</summary>

```json
{
  "query": "LLM confidence calibration competing opposing biases correction intervention routing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da470192-5928-4a68-88f3-23c0ff0295c5",
  "isSidechain": false,
  "requestId": "req_011CbBzX3QcXTwcRUdc3GN1c",
  "type": "assistant",
  "uuid": "097cb86e-3889-4900-8411-331eed4c10ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XPBSHSYxrvSXqFRdp6g6uT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 507,
      "cache_read_input_tokens": 41036,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 41036,
          "cache_creation_input_tokens": 507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 507
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

_source line 71 · 2026-05-19T13:18:01.705Z_

<details><summary>↩ Tool result · `toolu_012kHKs31xEdn9RDkkNiRnET`</summary>

```text
Web search results for query: "LLM confidence calibration competing opposing biases correction intervention routing 2025 2026"

Links: [{"title":"Confidence Calibration in LLMs","url":"https://www.emergentmind.com/topics/confidence-calibration-in-llms"},{"title":"Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection","url":"https://arxiv.org/html/2603.06604"},{"title":"Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-026-01217-9"},{"title":"Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of Large Language Models","url":"https://arxiv.org/pdf/2503.02623"},{"title":"Rubric-Based Evaluations & LLM-as-a-Judge — Methodologies, Biases, and Empirical Validation in Domain-Specific Contexts. | by Adnan Masood, PhD. | Apr, 2026 | Medium","url":"https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80"},{"title":"BEYOND CONSENSUS: MITIGATING THE AGREEABLE- NESS BIAS IN LLM JUDGE EVALUATIONS","url":"https://aicet.comp.nus.edu.sg/wp-content/uploads/2025/10/Beyond-Consensus-Mitigating-the-agreeableness-bias-in-LLM-judge-evaluations.pdf"},{"title":"Beyond Accuracy: The Role of Calibration in Self-Improving Large   Language Models","url":"https://arxiv.org/pdf/2504.02902"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"}]

Based on the web search results, here's what I found regarding LLM confidence calibration, competing biases, and correction interventions in 2025-2026:

## Competing Biases in LLM Confidence

LLM confidence is governed by two competing mechanisms: a choice-supportive bias that causes LLMs to exhibit inflated confidence when viewing their initial answers and maintain original responses even when presented with contrary evidence. LLMs also show systematic overweighting of contradictory advice, deviating from optimal Bayesian reasoning.

## Calibration and Correction Interventions

Several recent approaches address these issues:

**Critique-Based Methods:** Natural language critique prompts and supervised critique calibration teach LLMs patterns of over-/under-confidence, yielding significant Expected Calibration Error (ECE) reduction even out-of-domain.

**Reinforcement Learning:** Reinforcement learning with proper scoring rule rewards provably aligns expressed confidence with empirical accuracy, achieving state-of-the-art calibration and robust out-of-distribution generalization.

**Calibration-Aware RL:** Calibration-aware reinforcement learning mitigates reward-induced overconfidence on decision tokens from RLHF/RLVR, reducing ECE by up to 9 points.

**RAG-Based Approaches:** Rule-based schemes and supervised fine-tuning enable models to dynamically downgrade confidence when context is unreliable under noisy or conflicting evidence.

## Routing and Selective Application

Well-calibrated confidence estimates enable selective application of expensive strategies—retrieving context for uncertain queries, engaging deeper reasoning for complex problems, or escalating to human experts—only when needed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "097cb86e-3889-4900-8411-331eed4c10ae",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "379c38eb-d1bf-4d14-81dd-68acbe934685",
  "toolUseResult": {
    "query": "LLM confidence calibration competing opposing biases correction intervention routing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J8sCTBP3dcjzttCr531Qck",
        "content": [
          {
            "title": "Confidence Calibration in LLMs",
            "url": "https://www.emergentmind.com/topics/confidence-calibration-in-llms"
          },
          {
            "title": "Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection",
            "url": "https://arxiv.org/html/2603.06604"
          },
          {
            "title": "Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence",
            "url": "https://www.nature.com/articles/s42256-026-01217-9"
          },
          {
            "title": "Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of Large Language Models",
            "url": "https://arxiv.org/pdf/2503.02623"
          },
          {
            "title": "Rubric-Based Evaluations & LLM-as-a-Judge — Methodologies, Biases, and Empirical Validation in Domain-Specific Contexts. | by Adnan Masood, PhD. | Apr, 2026 | Medium",
            "url": "https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80"
          },
          {
            "title": "BEYOND CONSENSUS: MITIGATING THE AGREEABLE- NESS BIAS IN LLM JUDGE EVALUATIONS",
            "url": "https://aicet.comp.nus.edu.sg/wp-content/uploads/2025/10/Beyond-Consensus-Mitigating-the-agreeableness-bias-in-LLM-judge-evaluations.pdf"
          },
          {
            "title": "Beyond Accuracy: The Role of Calibration in Self-Improving Large   Language Models",
            "url": "https://arxiv.org/pdf/2504.02902"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding LLM confidence calibration, competing biases, and correction interventions in 2025-2026:\n\n## Competing Biases in LLM Confidence\n\nLLM confidence is governed by two competing mechanisms: a choice-supportive bias that causes LLMs to exhibit inflated confidence when viewing their initial answers and maintain original responses even when presented with contrary evidence. LLMs also show systematic overweighting of contradictory advice, deviating from optimal Bayesian reasoning.\n\n## Calibration and Correction Interventions\n\nSeveral recent approaches address these issues:\n\n**Critique-Based Methods:** Natural language critique prompts and supervised critique calibration teach LLMs patterns of over-/under-confidence, yielding significant Expected Calibration Error (ECE) reduction even out-of-domain.\n\n**Reinforcement Learning:** Reinforcement learning with proper scoring rule rewards provably aligns expressed confidence with empirical accuracy, achieving state-of-the-art calibration and robust out-of-distribution generalization.\n\n**Calibration-Aware RL:** Calibration-aware reinforcement learning mitigates reward-induced overconfidence on decision tokens from RLHF/RLVR, reducing ECE by up to 9 points.\n\n**RAG-Based Approaches:** Rule-based schemes and supervised fine-tuning enable models to dynamically downgrade confidence when context is unreliable under noisy or conflicting evidence.\n\n## Routing and Selective Application\n\nWell-calibrated confidence estimates enable selective application of expensive strategies—retrieving context for uncertain queries, engaging deeper reasoning for complex problems, or escalating to human experts—only when needed."
    ],
    "durationSeconds": 11.50508598199999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "097cb86e-3889-4900-8411-331eed4c10ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-19T13:18:04.686Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LJGfNyt3A8hZNJuKffdQGy`</summary>

```json
{
  "query": "CORAL correctness-optimized residual activation lens calibration arXiv 2602.06022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "379c38eb-d1bf-4d14-81dd-68acbe934685",
  "isSidechain": false,
  "requestId": "req_011CbBzY5pk8t4vbKMpQcQjY",
  "type": "assistant",
  "uuid": "f5bd0273-3df5-4241-9bfc-04bcda93b0c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013rBPGFAJpUnkda39BTc9hD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1489,
      "cache_read_input_tokens": 41036,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 41036,
          "cache_creation_input_tokens": 1489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1489
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

_source line 73 · 2026-05-19T13:18:13.009Z_

<details><summary>↩ Tool result · `toolu_01LJGfNyt3A8hZNJuKffdQGy`</summary>

```text
Web search results for query: "CORAL correctness-optimized residual activation lens calibration arXiv 2602.06022"

Links: [{"title":"[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/abs/2602.06022"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL):","url":"https://arxiv.org/pdf/2602.06022"},{"title":"Correctness-Optimized Residual Activation Lens : Transferrable and Calibration-Aware Inference-Time Steering","url":"http://paperreading.club/page?id=374945"},{"title":"[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2602.06022"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"},{"title":"Method for dynamically calibrating an image capture device","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10148945"}]

Based on the search results, I found comprehensive information about the CORAL paper (arXiv 2602.06022):

## Overview

CORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes.

## Problem and Motivation

Large language models (LLMs) exhibit persistent miscalibration, especially after instruction tuning and preference alignment, and while modified training objectives can improve calibration, retraining is expensive. Inference-time steering offers a lightweight alternative, yet most existing methods optimize proxies for correctness rather than correctness itself.

## Methodology

The method trains a regularized probe that predicts correctness directly from frozen residual stream activations, then uses these predictions to steer model behavior at inference time. By jointly optimizing for the accuracy and calibration components of the Brier score, CORAL improves both metrics and transfers its impact successfully to unseen benchmarks without any retraining.

## Results

CORAL consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average across three 7B-parameter models. These gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.

The paper was submitted to arXiv on February 5, 2026, with authors Miranda Muqing Miao, Young-Min Cho, and Lyle Ungar.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5bd0273-3df5-4241-9bfc-04bcda93b0c9",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "064b0b10-1e67-4291-8c51-e8ed5359a4ae",
  "toolUseResult": {
    "query": "CORAL correctness-optimized residual activation lens calibration arXiv 2602.06022",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AhjueMKv6yj7J17FtEDpXk",
        "content": [
          {
            "title": "[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/abs/2602.06022"
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
            "title": "[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/html/2602.06022v1"
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
            "title": "Method for dynamically calibrating an image capture device",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10148945"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the CORAL paper (arXiv 2602.06022):\n\n## Overview\n\nCORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes.\n\n## Problem and Motivation\n\nLarge language models (LLMs) exhibit persistent miscalibration, especially after instruction tuning and preference alignment, and while modified training objectives can improve calibration, retraining is expensive. Inference-time steering offers a lightweight alternative, yet most existing methods optimize proxies for correctness rather than correctness itself.\n\n## Methodology\n\nThe method trains a regularized probe that predicts correctness directly from frozen residual stream activations, then uses these predictions to steer model behavior at inference time. By jointly optimizing for the accuracy and calibration components of the Brier score, CORAL improves both metrics and transfers its impact successfully to unseen benchmarks without any retraining.\n\n## Results\n\nCORAL consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average across three 7B-parameter models. These gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.\n\nThe paper was submitted to arXiv on February 5, 2026, with authors Miranda Muqing Miao, Young-Min Cho, and Lyle Ungar."
    ],
    "durationSeconds": 8.318882851000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f5bd0273-3df5-4241-9bfc-04bcda93b0c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 74 · 2026-05-19T13:18:13.011Z_

```json
{
  "parentUuid": "064b0b10-1e67-4291-8c51-e8ed5359a4ae",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5ae95fed-542b-4d6c-aaaf-b12258b81952",
  "timestamp": "2026-05-19T13:18:13.011Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "5ae95fed-542b-4d6c-aaaf-b12258b81952",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 76_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Assistant

_source line 77 · 2026-05-19T13:18:16.322Z_

Now let me do the critical novelty pressure test — searching for work that directly combines bias decomposition with adaptive steering routing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ae95fed-542b-4d6c-aaaf-b12258b81952",
  "isSidechain": false,
  "requestId": "req_011CbBzYv8s32BW61g9jdMiZ",
  "type": "assistant",
  "uuid": "2d93bca3-eea8-4bf5-a528-f47c065ff671",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A72zGnWqQc8D2xaBGqC7op",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 42525,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 42525,
          "cache_creation_input_tokens": 1111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1111
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

_source line 78 · 2026-05-19T13:18:16.606Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sv1CCNy6VwWbe4jN2dC3BX`</summary>

```json
{
  "query": "disentangle overconfidence underconfidence separate directions activation steering LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d93bca3-eea8-4bf5-a528-f47c065ff671",
  "isSidechain": false,
  "requestId": "req_011CbBzYv8s32BW61g9jdMiZ",
  "type": "assistant",
  "uuid": "3bdc5f58-c66d-4a25-98a3-4598d6111adc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A72zGnWqQc8D2xaBGqC7op",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 42525,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 42525,
          "cache_creation_input_tokens": 1111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1111
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

_source line 79 · 2026-05-19T13:18:24.517Z_

<details><summary>↩ Tool result · `toolu_01Sv1CCNy6VwWbe4jN2dC3BX`</summary>

```text
Web search results for query: "disentangle overconfidence underconfidence separate directions activation steering LLM 2026"

Links: [{"title":"SteerConf: Steering LLMs for Confidence Elicitation | OpenReview","url":"https://openreview.net/forum?id=5sgK63Zshg"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/pdf/2503.02863"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/pdf/2602.04428"},{"title":"Effectively Steer LLM To Follow Preference via Building Confident   Directions","url":"https://arxiv.org/pdf/2503.02989"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/html/2503.02863v2"},{"title":"Do Language Models Mirror Human Confidence? Exploring Psychological Insights to Address Overconfidence in LLMs","url":"https://arxiv.org/pdf/2506.00582"},{"title":"Understanding (Un)Reliability of Steering Vectors in Language Models","url":"https://arxiv.org/pdf/2505.22637"},{"title":"Controlling Large Language Model Agents with Entropic Activation   Steering","url":"https://arxiv.org/pdf/2406.00244"}]

Based on the search results, I found several relevant papers on steering LLMs for confidence and activation control:

## Key Findings:

**SteerConf Framework**: SteerConf is a novel framework that systematically steers LLMs' confidence scores to improve their calibration and reliability. The approach addresses the fact that LLMs often exhibit overconfidence, producing predictions that fail to align with their true likelihood of correctness, even when uncertain. The framework employs a set of steering levels to guide the LLM's confidence elicitation from very cautious to very confident: {very cautious, cautious, vanilla, confident, very confident}.

**Activation Steering for Confidence**: Recent work explores fine-grained control over LLM behavior. Activation steering has emerged as a powerful paradigm for modulating model behavior, intervening directly in the LLM intermediate activations during forward propagation, enabling fine-grained control without additional training.

**Steering Vector Reliability**: Datasets where positive and negative activations are better separated are more steerable, and vector steering is unreliable when the target behavior is not represented by a coherent direction.

**Entropy-Based Steering**: Entropic Activation Steering (EAST) is a method to alter an LLM agent's subjective uncertainty over decisions and entropy over actions, effectively addressing the overconfidence exhibited by LLM agents.

The search results show active research into separating confidence directions and improving LLM calibration through various steering approaches in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bdc5f58-c66d-4a25-98a3-4598d6111adc",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "5c60bb25-93dd-4c91-b9dd-cc9f48b004d7",
  "toolUseResult": {
    "query": "disentangle overconfidence underconfidence separate directions activation steering LLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HWayMq52BpmVc9M6u5RgLm",
        "content": [
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation | OpenReview",
            "url": "https://openreview.net/forum?id=5sgK63Zshg"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/pdf/2503.02863"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/pdf/2602.04428"
          },
          {
            "title": "Effectively Steer LLM To Follow Preference via Building Confident   Directions",
            "url": "https://arxiv.org/pdf/2503.02989"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/html/2503.02863v2"
          },
          {
            "title": "Do Language Models Mirror Human Confidence? Exploring Psychological Insights to Address Overconfidence in LLMs",
            "url": "https://arxiv.org/pdf/2506.00582"
          },
          {
            "title": "Understanding (Un)Reliability of Steering Vectors in Language Models",
            "url": "https://arxiv.org/pdf/2505.22637"
          },
          {
            "title": "Controlling Large Language Model Agents with Entropic Activation   Steering",
            "url": "https://arxiv.org/pdf/2406.00244"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on steering LLMs for confidence and activation control:\n\n## Key Findings:\n\n**SteerConf Framework**: SteerConf is a novel framework that systematically steers LLMs' confidence scores to improve their calibration and reliability. The approach addresses the fact that LLMs often exhibit overconfidence, producing predictions that fail to align with their true likelihood of correctness, even when uncertain. The framework employs a set of steering levels to guide the LLM's confidence elicitation from very cautious to very confident: {very cautious, cautious, vanilla, confident, very confident}.\n\n**Activation Steering for Confidence**: Recent work explores fine-grained control over LLM behavior. Activation steering has emerged as a powerful paradigm for modulating model behavior, intervening directly in the LLM intermediate activations during forward propagation, enabling fine-grained control without additional training.\n\n**Steering Vector Reliability**: Datasets where positive and negative activations are better separated are more steerable, and vector steering is unreliable when the target behavior is not represented by a coherent direction.\n\n**Entropy-Based Steering**: Entropic Activation Steering (EAST) is a method to alter an LLM agent's subjective uncertainty over decisions and entropy over actions, effectively addressing the overconfidence exhibited by LLM agents.\n\nThe search results show active research into separating confidence directions and improving LLM calibration through various steering approaches in 2025-2026."
    ],
    "durationSeconds": 7.90565480399999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3bdc5f58-c66d-4a25-98a3-4598d6111adc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-19T13:18:27.421Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BsGuWd8uZsdnP7ahDzUSUv`</summary>

```json
{
  "query": "\"Wired for Overconfidence\" mechanistic perspective inflated verbalized confidence LLM arXiv 2604.01457"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c60bb25-93dd-4c91-b9dd-cc9f48b004d7",
  "isSidechain": false,
  "requestId": "req_011CbBzZmRGeEccq4ivxdWAQ",
  "type": "assistant",
  "uuid": "3c66f5ec-5a27-412b-bd30-61fd22a62d77",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdajRXNLN6MTCkpLBcXopD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 43636,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 43636,
          "cache_creation_input_tokens": 817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 817
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

_source line 81 · 2026-05-19T13:18:34.428Z_

<details><summary>↩ Tool result · `toolu_01BsGuWd8uZsdnP7ahDzUSUv`</summary>

```text
Web search results for query: ""Wired for Overconfidence" mechanistic perspective inflated verbalized confidence LLM arXiv 2604.01457"

Links: [{"title":"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs","url":"https://arxiv.org/html/2604.01457v1"},{"title":"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs","url":"https://arxiv.org/pdf/2604.01457"},{"title":"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs | Takara TLDR","url":"https://tldr.takara.ai/p/2604.01457"},{"title":"How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models","url":"https://arxiv.org/html/2507.03120v1"},{"title":"Calibrating Verbalized Confidence with Self-Generated Distractors","url":"https://arxiv.org/pdf/2509.25532"}]

I found the paper you're looking for! Here's what the search results show:

"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs" is a paper by researchers from the University of Virginia (Tianyi Zhao, Yinhan He, Wendy Zheng, Yujie Zhang, and Chen Chen) that addresses how large language models are often confidently wrong—when they produce factually incorrect answers, they tend to verbalize overly high confidence rather than signal uncertainty.

The paper presents a circuit-level mechanistic analysis organized around three axes: capturing verbalized confidence as a differentiable internal signal, identifying the circuits that causally inflate it, and leveraging these insights for targeted inference-time recalibration.

The researchers found that across two instruction-tuned LLMs on three datasets, a compact set of MLP blocks and attention heads concentrated in middle-to-late layers consistently write the confidence-inflation signal at the final token position, and targeted inference-time interventions on these circuits substantially improve calibration.

The results suggest that verbalized overconfidence in LLMs is driven by identifiable internal circuits and can be mitigated through targeted intervention.

The paper was published on arXiv on April 1, 2026 (arXiv:2604.01457v1).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c66f5ec-5a27-412b-bd30-61fd22a62d77",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "1d8f6c9e-6444-4fb2-9bff-f60cd8eda48a",
  "toolUseResult": {
    "query": "\"Wired for Overconfidence\" mechanistic perspective inflated verbalized confidence LLM arXiv 2604.01457",
    "results": [
      {
        "tool_use_id": "srvtoolu_0172Q36EW9994zkACMuakbBY",
        "content": [
          {
            "title": "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs",
            "url": "https://arxiv.org/html/2604.01457v1"
          },
          {
            "title": "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs",
            "url": "https://arxiv.org/pdf/2604.01457"
          },
          {
            "title": "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs | Takara TLDR",
            "url": "https://tldr.takara.ai/p/2604.01457"
          },
          {
            "title": "How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models",
            "url": "https://arxiv.org/html/2507.03120v1"
          },
          {
            "title": "Calibrating Verbalized Confidence with Self-Generated Distractors",
            "url": "https://arxiv.org/pdf/2509.25532"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search results show:\n\n\"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs\" is a paper by researchers from the University of Virginia (Tianyi Zhao, Yinhan He, Wendy Zheng, Yujie Zhang, and Chen Chen) that addresses how large language models are often confidently wrong—when they produce factually incorrect answers, they tend to verbalize overly high confidence rather than signal uncertainty.\n\nThe paper presents a circuit-level mechanistic analysis organized around three axes: capturing verbalized confidence as a differentiable internal signal, identifying the circuits that causally inflate it, and leveraging these insights for targeted inference-time recalibration.\n\nThe researchers found that across two instruction-tuned LLMs on three datasets, a compact set of MLP blocks and attention heads concentrated in middle-to-late layers consistently write the confidence-inflation signal at the final token position, and targeted inference-time interventions on these circuits substantially improve calibration.\n\nThe results suggest that verbalized overconfidence in LLMs is driven by identifiable internal circuits and can be mitigated through targeted intervention.\n\nThe paper was published on arXiv on April 1, 2026 (arXiv:2604.01457v1)."
    ],
    "durationSeconds": 7.002560824000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3c66f5ec-5a27-412b-bd30-61fd22a62d77",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-19T13:18:37.145Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0115X7CQmWoLrDe75maZN44N`</summary>

```json
{
  "query": "ODESteer unified ODE steering framework LLM alignment nonlinear continuous arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d8f6c9e-6444-4fb2-9bff-f60cd8eda48a",
  "isSidechain": false,
  "requestId": "req_011CbBzaVnCiAZqdiS47SCwT",
  "type": "assistant",
  "uuid": "28025e8e-9c52-443b-8a27-aefb523aa7d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vmb4Ux9g63bSQGRA4pMobh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 44453,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 44453,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 83 · 2026-05-19T13:18:42.545Z_

<details><summary>↩ Tool result · `toolu_0115X7CQmWoLrDe75maZN44N`</summary>

```text
Web search results for query: "ODESteer unified ODE steering framework LLM alignment nonlinear continuous arXiv 2026"

Links: [{"title":"[2602.17560] ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment","url":"https://arxiv.org/abs/2602.17560"},{"title":"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment","url":"https://arxiv.org/html/2602.17560v1"},{"title":"[2602.17560v1] ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment","url":"https://arxiv.org/abs/2602.17560v1"},{"title":"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment | OpenReview","url":"https://openreview.net/forum?id=CFewUmgIIL"},{"title":"(PDF) ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment","url":"https://www.researchgate.net/publication/400971006_ODESteer_A_Unified_ODE-Based_Steering_Framework_for_LLM_Alignment"},{"title":"GitHub - ZhaoHongjue/odesteer: Code for \"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment\" · GitHub","url":"https://github.com/ZhaoHongjue/odesteer"}]

I found the paper you're looking for! Here's what the search revealed:

ODESteer is an ODE-based steering guided by barrier functions for LLM alignment. The paper proposes a unified ordinary differential equations (ODEs)-based theoretical framework for activation steering in LLM alignment.

Key aspects of the research include:

- **Theoretical Foundation**: Conventional activation addition can be interpreted as a first-order approximation to the solution of an ODE, and identifying a steering direction becomes equivalent to designing a barrier function from control theory.

- **Method**: ODESteer identifies steering directions by defining the barrier function as the log-density ratio between positive and negative activations, and employs it to construct an ODE for multi-step and adaptive steering.

- **Empirical Results**: ODESteer achieves consistent empirical improvements on diverse LLM alignment benchmarks, including a 5.7% improvement over TruthfulQA, 2.5% over UltraFeedback, and 2.4% over RealToxicityPrompts.

The paper was accepted at ICLR 2026, and the arXiv preprint is available as arXiv:2602.17560.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28025e8e-9c52-443b-8a27-aefb523aa7d5",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "d599300e-4a5a-4db0-a69e-44a3fc95eb64",
  "toolUseResult": {
    "query": "ODESteer unified ODE steering framework LLM alignment nonlinear continuous arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U9yvQaFrRLFjPos7b2EqWM",
        "content": [
          {
            "title": "[2602.17560] ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment",
            "url": "https://arxiv.org/abs/2602.17560"
          },
          {
            "title": "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment",
            "url": "https://arxiv.org/html/2602.17560v1"
          },
          {
            "title": "[2602.17560v1] ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment",
            "url": "https://arxiv.org/abs/2602.17560v1"
          },
          {
            "title": "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment | OpenReview",
            "url": "https://openreview.net/forum?id=CFewUmgIIL"
          },
          {
            "title": "(PDF) ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment",
            "url": "https://www.researchgate.net/publication/400971006_ODESteer_A_Unified_ODE-Based_Steering_Framework_for_LLM_Alignment"
          },
          {
            "title": "GitHub - ZhaoHongjue/odesteer: Code for \"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment\" · GitHub",
            "url": "https://github.com/ZhaoHongjue/odesteer"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\nODESteer is an ODE-based steering guided by barrier functions for LLM alignment. The paper proposes a unified ordinary differential equations (ODEs)-based theoretical framework for activation steering in LLM alignment.\n\nKey aspects of the research include:\n\n- **Theoretical Foundation**: Conventional activation addition can be interpreted as a first-order approximation to the solution of an ODE, and identifying a steering direction becomes equivalent to designing a barrier function from control theory.\n\n- **Method**: ODESteer identifies steering directions by defining the barrier function as the log-density ratio between positive and negative activations, and employs it to construct an ODE for multi-step and adaptive steering.\n\n- **Empirical Results**: ODESteer achieves consistent empirical improvements on diverse LLM alignment benchmarks, including a 5.7% improvement over TruthfulQA, 2.5% over UltraFeedback, and 2.4% over RealToxicityPrompts.\n\nThe paper was accepted at ICLR 2026, and the arXiv preprint is available as arXiv:2602.17560."
    ],
    "durationSeconds": 5.3955530380000125,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "28025e8e-9c52-443b-8a27-aefb523aa7d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-19T13:18:45.540Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YGfUD1VERvdT7N8diJLbCq`</summary>

```json
{
  "query": "FLAS flow-based activation steering AxBench arXiv 2605.05892 concept-conditioned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d599300e-4a5a-4db0-a69e-44a3fc95eb64",
  "isSidechain": false,
  "requestId": "req_011CbBzb6R3gUsoQ6ShqqYPS",
  "type": "assistant",
  "uuid": "24364e5a-8c5a-4ef7-9b66-3344272afa09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ejeyi2khQFoWnF5o2GiNq2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 45156,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 45156,
          "cache_creation_input_tokens": 751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 751
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

_source line 85 · 2026-05-19T13:18:54.898Z_

<details><summary>↩ Tool result · `toolu_01YGfUD1VERvdT7N8diJLbCq`</summary>

```text
Web search results for query: "FLAS flow-based activation steering AxBench arXiv 2605.05892 concept-conditioned"

Links: [{"title":"[2605.05892] Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/abs/2605.05892"},{"title":"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/html/2605.05892"},{"title":"Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/html/2605.03907v1"},{"title":"HyperSteer: Activation Steering at Scale with Hypernetworks","url":"https://arxiv.org/html/2506.03292v1"},{"title":"Activation Steering at Scale with Hypernetworks - HyperSteer","url":"https://arxiv.org/pdf/2506.03292"},{"title":"Steering Large Language Models using Conceptors: Improving Addition-Based Activation Engineering","url":"https://arxiv.org/pdf/2410.16314"},{"title":"AXBENCH: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders","url":"https://openreview.net/pdf?id=K2CckZjNy0"}]

Based on the search results, I found relevant information about your query:

FLAS (Flow-based Activation Steering) learns a general, concept-conditioned velocity field that transports unsteered activations to steered ones. Activation steering has emerged as a promising alternative for controlling language-model behavior at inference time by modifying intermediate representations while keeping model parameters frozen.

The research addresses limitations of existing steering methods. Large-scale evaluations such as AxBench show that existing steering methods are often outperformed by simple in-context prompting and generalize poorly to unseen concepts. These limitations arise from unvalidated simplifying assumptions shared across prior methods, which typically restrict steering interventions to fixed, single-step, position-invariant transforms.

On AxBench, FLAS is the first learned method to consistently outperform prompting, reaching held-out harmonic means of 1.015 on Gemma-2-2B-IT and 1.113 on Gemma-2-9B-IT.

The paper (arXiv 2605.05892) was authored by researchers from Georgia Institute of Technology and was published on May 7, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24364e5a-8c5a-4ef7-9b66-3344272afa09",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "790058c5-f31d-45cf-83cb-aa3f0c1e6ec4",
  "toolUseResult": {
    "query": "FLAS flow-based activation steering AxBench arXiv 2605.05892 concept-conditioned",
    "results": [
      {
        "tool_use_id": "srvtoolu_011G7fZC2jfvqysuK6yNT8ZC",
        "content": [
          {
            "title": "[2605.05892] Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/abs/2605.05892"
          },
          {
            "title": "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/html/2605.05892"
          },
          {
            "title": "Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/html/2605.03907v1"
          },
          {
            "title": "HyperSteer: Activation Steering at Scale with Hypernetworks",
            "url": "https://arxiv.org/html/2506.03292v1"
          },
          {
            "title": "Activation Steering at Scale with Hypernetworks - HyperSteer",
            "url": "https://arxiv.org/pdf/2506.03292"
          },
          {
            "title": "Steering Large Language Models using Conceptors: Improving Addition-Based Activation Engineering",
            "url": "https://arxiv.org/pdf/2410.16314"
          },
          {
            "title": "AXBENCH: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders",
            "url": "https://openreview.net/pdf?id=K2CckZjNy0"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query:\n\nFLAS (Flow-based Activation Steering) learns a general, concept-conditioned velocity field that transports unsteered activations to steered ones. Activation steering has emerged as a promising alternative for controlling language-model behavior at inference time by modifying intermediate representations while keeping model parameters frozen.\n\nThe research addresses limitations of existing steering methods. Large-scale evaluations such as AxBench show that existing steering methods are often outperformed by simple in-context prompting and generalize poorly to unseen concepts. These limitations arise from unvalidated simplifying assumptions shared across prior methods, which typically restrict steering interventions to fixed, single-step, position-invariant transforms.\n\nOn AxBench, FLAS is the first learned method to consistently outperform prompting, reaching held-out harmonic means of 1.015 on Gemma-2-2B-IT and 1.113 on Gemma-2-9B-IT.\n\nThe paper (arXiv 2605.05892) was authored by researchers from Georgia Institute of Technology and was published on May 7, 2026."
    ],
    "durationSeconds": 9.352695123000013,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "24364e5a-8c5a-4ef7-9b66-3344272afa09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-19T13:18:57.988Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mq8RM1ZRJzQHbbtzRA6xc7`</summary>

```json
{
  "query": "HyperSteer activation steering hypernetworks scale multi-concept arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "790058c5-f31d-45cf-83cb-aa3f0c1e6ec4",
  "isSidechain": false,
  "requestId": "req_011CbBzc1NiGQfk6NsE23CAP",
  "type": "assistant",
  "uuid": "0d107dd4-7f18-4e75-8783-60ffa4a3666a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162NwxvXae7T5sLDZTufJ3j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 45907,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 45907,
          "cache_creation_input_tokens": 712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 712
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

_source line 87 · 2026-05-19T13:19:05.498Z_

<details><summary>↩ Tool result · `toolu_01Mq8RM1ZRJzQHbbtzRA6xc7`</summary>

```text
Web search results for query: "HyperSteer activation steering hypernetworks scale multi-concept arXiv 2026"

Links: [{"title":"[2506.03292] HyperSteer: Activation Steering at Scale with Hypernetworks","url":"https://arxiv.org/abs/2506.03292"},{"title":"Activation Steering in Neural Networks","url":"https://www.emergentmind.com/topics/activation-steering"},{"title":"(PDF) HyperSteer: Activation Steering at Scale with Hypernetworks","url":"https://www.researchgate.net/publication/392406160_HyperSteer_Activation_Steering_at_Scale_with_Hypernetworks"},{"title":"[Literature Review] HyperSteer: Activation Steering at Scale with Hypernetworks","url":"https://www.themoonlight.io/en/review/hypersteer-activation-steering-at-scale-with-hypernetworks"},{"title":"HyperSteer: Activation Steering at Scale with Hypernetworks","url":"https://arxiv.org/html/2506.03292v1"},{"title":"Activation Steering at Scale with Hypernetworks - HyperSteer","url":"https://arxiv.org/pdf/2506.03292"},{"title":"HYPER STEER - Activation Steering at Scale With Hypernetworks - Standford - June2025 | PDF | Learning | Machine Learning","url":"https://www.scribd.com/document/985249757/HYPER-STEER-Activation-Steering-at-Scale-with-Hypernetworks-Standford-June2025"},{"title":"Computation and Language Jun 2025","url":"https://www.arxiv.org/list/cs.CL/2025-06?skip=325&show=25"},{"title":"EasyEdit2: An Easy-to-use Steering Framework for Editing Large Language Models","url":"https://arxiv.org/html/2504.15133v3"}]

I found the paper! Here's what I found about HyperSteer:

## Overview

HyperSteer is a family of hypernetwork-based architectures trained end-to-end to generate steering vectors conditioned on natural language steering prompts and the internals of the steered language model.

## Key Problem and Solution

Steering language models by modifying internal activations is popular for controlling text generation. Unsupervised dictionary learning methods like sparse autoencoders can be scaled to produce many steering vectors but lack guarantees on individual efficacy, while supervised methods are targeted and effective but require more data collection and training for each additional steering vector.

HyperSteer addresses this gap by combining scalability with targeted control.

## Architecture and Performance

The state-of-the-art HyperSteer model uses a transformer hypernetwork that applies self-attention to process a steering prompt and cross-attention to read from the residual stream of a base language model, outputting a steering vector that is added to the base LM's residual stream.

Scaling HyperSteer with thousands of steering prompts exceeds the performance of state-of-the-art activation steering methods, even on steering prompts never seen during training.

## Evaluation

HyperSteer is evaluated on two datasets: Concept500-HI (held-in) with 500 steering prompts seen during training plus unseen base prompts, and Concept500-HO (held-out) with 500 steering prompts not seen during training.

The paper was published on arXiv as arXiv:2506.03292 on June 3, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d107dd4-7f18-4e75-8783-60ffa4a3666a",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "806ba098-ed3d-400d-8ac0-324386e89658",
  "toolUseResult": {
    "query": "HyperSteer activation steering hypernetworks scale multi-concept arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019sbayWfrd5KPVM7Aq2jeh8",
        "content": [
          {
            "title": "[2506.03292] HyperSteer: Activation Steering at Scale with Hypernetworks",
            "url": "https://arxiv.org/abs/2506.03292"
          },
          {
            "title": "Activation Steering in Neural Networks",
            "url": "https://www.emergentmind.com/topics/activation-steering"
          },
          {
            "title": "(PDF) HyperSteer: Activation Steering at Scale with Hypernetworks",
            "url": "https://www.researchgate.net/publication/392406160_HyperSteer_Activation_Steering_at_Scale_with_Hypernetworks"
          },
          {
            "title": "[Literature Review] HyperSteer: Activation Steering at Scale with Hypernetworks",
            "url": "https://www.themoonlight.io/en/review/hypersteer-activation-steering-at-scale-with-hypernetworks"
          },
          {
            "title": "HyperSteer: Activation Steering at Scale with Hypernetworks",
            "url": "https://arxiv.org/html/2506.03292v1"
          },
          {
            "title": "Activation Steering at Scale with Hypernetworks - HyperSteer",
            "url": "https://arxiv.org/pdf/2506.03292"
          },
          {
            "title": "HYPER STEER - Activation Steering at Scale With Hypernetworks - Standford - June2025 | PDF | Learning | Machine Learning",
            "url": "https://www.scribd.com/document/985249757/HYPER-STEER-Activation-Steering-at-Scale-with-Hypernetworks-Standford-June2025"
          },
          {
            "title": "Computation and Language Jun 2025",
            "url": "https://www.arxiv.org/list/cs.CL/2025-06?skip=325&show=25"
          },
          {
            "title": "EasyEdit2: An Easy-to-use Steering Framework for Editing Large Language Models",
            "url": "https://arxiv.org/html/2504.15133v3"
          }
        ]
      },
      "I found the paper! Here's what I found about HyperSteer:\n\n## Overview\n\nHyperSteer is a family of hypernetwork-based architectures trained end-to-end to generate steering vectors conditioned on natural language steering prompts and the internals of the steered language model.\n\n## Key Problem and Solution\n\nSteering language models by modifying internal activations is popular for controlling text generation. Unsupervised dictionary learning methods like sparse autoencoders can be scaled to produce many steering vectors but lack guarantees on individual efficacy, while supervised methods are targeted and effective but require more data collection and training for each additional steering vector.\n\nHyperSteer addresses this gap by combining scalability with targeted control.\n\n## Architecture and Performance\n\nThe state-of-the-art HyperSteer model uses a transformer hypernetwork that applies self-attention to process a steering prompt and cross-attention to read from the residual stream of a base language model, outputting a steering vector that is added to the base LM's residual stream.\n\nScaling HyperSteer with thousands of steering prompts exceeds the performance of state-of-the-art activation steering methods, even on steering prompts never seen during training.\n\n## Evaluation\n\nHyperSteer is evaluated on two datasets: Concept500-HI (held-in) with 500 steering prompts seen during training plus unseen base prompts, and Concept500-HO (held-out) with 500 steering prompts not seen during training.\n\nThe paper was published on arXiv as arXiv:2506.03292 on June 3, 2025."
    ],
    "durationSeconds": 7.504915047000046,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0d107dd4-7f18-4e75-8783-60ffa4a3666a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 88_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "806ba098-ed3d-400d-8ac0-324386e89658",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Tool call

_source line 90 · 2026-05-19T13:19:08.170Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PG1U6ZbVY7mndtSBRNy8mv`</summary>

```json
{
  "query": "steer like LLM activation steering mimics prompting 2605.03907 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "806ba098-ed3d-400d-8ac0-324386e89658",
  "isSidechain": false,
  "requestId": "req_011CbBzcnbYYRre6N8AT9WS5",
  "type": "assistant",
  "uuid": "ce817105-d52f-4ae2-ac32-b5cc2dc2412b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011k2bfEkTz5WbeBA6Dg1TVb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 46619,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 955,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 46619,
          "cache_creation_input_tokens": 955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 955
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

_source line 91 · 2026-05-19T13:19:16.701Z_

<details><summary>↩ Tool result · `toolu_01PG1U6ZbVY7mndtSBRNy8mv`</summary>

```text
Web search results for query: "steer like LLM activation steering mimics prompting 2605.03907 2026"

Links: [{"title":"[2605.03907] Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/abs/2605.03907"},{"title":"[2605.03907v1] Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/abs/2605.03907v1"},{"title":"Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/html/2605.03907"},{"title":"Steering Language Models with Activation Engineering | OpenReview","url":"https://openreview.net/forum?id=2XBPdPIcFK"},{"title":"Effectively Steer LLM To Follow Preference via Building Confident   Directions","url":"https://arxiv.org/pdf/2503.02989"},{"title":"Steering Code LLMs with Activation Directions for Language and Library Control","url":"https://arxiv.org/pdf/2603.23629"},{"title":"Fusion Steering: Prompt-Specific Activation Control","url":"https://arxiv.org/pdf/2505.22572"},{"title":"Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence","url":"https://arxiv.org/pdf/2604.08169"},{"title":"Programming Refusal with Conditional Activation Steering","url":"https://arxiv.org/pdf/2409.05907"}]

Based on the search results, I found the paper you're looking for:

**"Steer Like the LLM: Activation Steering that Mimics Prompting"** (arXiv:2605.03907)

The paper, submitted on May 5, 2026, by Geert Heyman and Frederik Vandeputte, addresses a key challenge in steering large language models.

The paper notes that activation steering methods often underperform compared to prompt-based approaches. The authors propose a framework that formulates prompt steering as a form of activation steering and investigates whether distilling successful prompt steering behavior into simpler, interpretable models can close this gap.

Their analysis reveals that popular activation steering methods are not faithful to the mechanics of prompt steering, which applies strong interventions on some tokens while barely affecting others.

To address this, they introduce Prompt Steering Replacement (PSR) models that estimate token-specific steering coefficients from the activations themselves and are trained to imitate prompt-based interventions. Experiments on three steering benchmarks across multiple language models show that PSR models outperform existing activation steering methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce817105-d52f-4ae2-ac32-b5cc2dc2412b",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "404aada9-bd3f-400f-be94-1d58647f76d1",
  "toolUseResult": {
    "query": "steer like LLM activation steering mimics prompting 2605.03907 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H1f7eQ9StUGnDAFWYdJjEw",
        "content": [
          {
            "title": "[2605.03907] Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/abs/2605.03907"
          },
          {
            "title": "[2605.03907v1] Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/abs/2605.03907v1"
          },
          {
            "title": "Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/html/2605.03907"
          },
          {
            "title": "Steering Language Models with Activation Engineering | OpenReview",
            "url": "https://openreview.net/forum?id=2XBPdPIcFK"
          },
          {
            "title": "Effectively Steer LLM To Follow Preference via Building Confident   Directions",
            "url": "https://arxiv.org/pdf/2503.02989"
          },
          {
            "title": "Steering Code LLMs with Activation Directions for Language and Library Control",
            "url": "https://arxiv.org/pdf/2603.23629"
          },
          {
            "title": "Fusion Steering: Prompt-Specific Activation Control",
            "url": "https://arxiv.org/pdf/2505.22572"
          },
          {
            "title": "Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence",
            "url": "https://arxiv.org/pdf/2604.08169"
          },
          {
            "title": "Programming Refusal with Conditional Activation Steering",
            "url": "https://arxiv.org/pdf/2409.05907"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**\"Steer Like the LLM: Activation Steering that Mimics Prompting\"** (arXiv:2605.03907)\n\nThe paper, submitted on May 5, 2026, by Geert Heyman and Frederik Vandeputte, addresses a key challenge in steering large language models.\n\nThe paper notes that activation steering methods often underperform compared to prompt-based approaches. The authors propose a framework that formulates prompt steering as a form of activation steering and investigates whether distilling successful prompt steering behavior into simpler, interpretable models can close this gap.\n\nTheir analysis reveals that popular activation steering methods are not faithful to the mechanics of prompt steering, which applies strong interventions on some tokens while barely affecting others.\n\nTo address this, they introduce Prompt Steering Replacement (PSR) models that estimate token-specific steering coefficients from the activations themselves and are trained to imitate prompt-based interventions. Experiments on three steering benchmarks across multiple language models show that PSR models outperform existing activation steering methods."
    ],
    "durationSeconds": 8.52732027799997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ce817105-d52f-4ae2-ac32-b5cc2dc2412b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-19T13:19:19.973Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y7cBkTNWEGmkU7uqzdvQtt`</summary>

```json
{
  "query": "\"Don't Lose Focus\" key-orthogonal projections activation steering 2605.06342 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "404aada9-bd3f-400f-be94-1d58647f76d1",
  "isSidechain": false,
  "requestId": "req_011CbBzdcVcBGdTpwGmTHDdi",
  "type": "assistant",
  "uuid": "10c19e30-9a6d-4f5c-88c4-17a81ca1512e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETSY3tTmaL8TtHui2tGWk5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 47574,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 47574,
          "cache_creation_input_tokens": 749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 749
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

_source line 93 · 2026-05-19T13:19:31.939Z_

<details><summary>↩ Tool result · `toolu_01Y7cBkTNWEGmkU7uqzdvQtt`</summary>

```text
Web search results for query: ""Don't Lose Focus" key-orthogonal projections activation steering 2605.06342 2026"

Links: [{"title":"[2605.06342] Don't Lose Focus: Activation Steering via Key-Orthogonal Projections","url":"https://arxiv.org/abs/2605.06342"},{"title":"Don’t Lose Focus: Activation Steering via Key-Orthogonal Projections","url":"https://arxiv.org/html/2605.06342v1"},{"title":"Steering Llama 2 via Contrastive Activation Addition","url":"https://www.researchgate.net/publication/384215189_Steering_Llama_2_via_Contrastive_Activation_Addition"},{"title":"Don't Lose Focus: Activation Steering via Key-Orthogonal ...","url":"https://www.researchgate.net/publication/404628326_Don't_Lose_Focus_Activation_Steering_via_Key-Orthogonal_Projections"},{"title":"Steering smarter. Why K-Steering is reshaping LLM… | by Thoughtworks | Medium","url":"https://thoughtworks.medium.com/steering-smarter-4fbfbdb58803"},{"title":"Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence","url":"https://arxiv.org/pdf/2604.08169"}]

Based on the search results, I found the paper you're looking for:

"Don't Lose Focus: Activation Steering via Key-Orthogonal Projections" (arXiv:2605.06342) proposes SKOP, a steering method that constrains harmful attention rerouting without eliminating steering efficacy by preserving attention patterns on a small set of focus tokens the model relies on for reasoning and retrieval, while allowing redistribution among less critical tail tokens.

The paper argues that a primary cause of performance trade-offs with activation steering is attention rerouting: steering vectors alter query-key matching, shifting attention away from contextually important tokens toward less informative ones.

According to the authors, SKOP achieves the best joint steering-utility trade-off, reducing utility degradation by 5-7x while retaining over 95% of vanilla steering efficacy.

The method works by removing only the components that strongly shift attention from the focus set to the tail set by comparing the tokens a head attends to strongly on utility tasks with those it attends to weakly, using differences in their key representations to identify steering components likely to cause harmful attention shifts, and then removing only these components selectively from a small set of risk heads.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10c19e30-9a6d-4f5c-88c4-17a81ca1512e",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "5eff44a0-bc96-4efc-9e98-2ba27e53b5a2",
  "toolUseResult": {
    "query": "\"Don't Lose Focus\" key-orthogonal projections activation steering 2605.06342 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E3ue1dGgYhSzVdYjHYxNcZ",
        "content": [
          {
            "title": "[2605.06342] Don't Lose Focus: Activation Steering via Key-Orthogonal Projections",
            "url": "https://arxiv.org/abs/2605.06342"
          },
          {
            "title": "Don’t Lose Focus: Activation Steering via Key-Orthogonal Projections",
            "url": "https://arxiv.org/html/2605.06342v1"
          },
          {
            "title": "Steering Llama 2 via Contrastive Activation Addition",
            "url": "https://www.researchgate.net/publication/384215189_Steering_Llama_2_via_Contrastive_Activation_Addition"
          },
          {
            "title": "Don't Lose Focus: Activation Steering via Key-Orthogonal ...",
            "url": "https://www.researchgate.net/publication/404628326_Don't_Lose_Focus_Activation_Steering_via_Key-Orthogonal_Projections"
          },
          {
            "title": "Steering smarter. Why K-Steering is reshaping LLM… | by Thoughtworks | Medium",
            "url": "https://thoughtworks.medium.com/steering-smarter-4fbfbdb58803"
          },
          {
            "title": "Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence",
            "url": "https://arxiv.org/pdf/2604.08169"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Don't Lose Focus: Activation Steering via Key-Orthogonal Projections\" (arXiv:2605.06342) proposes SKOP, a steering method that constrains harmful attention rerouting without eliminating steering efficacy by preserving attention patterns on a small set of focus tokens the model relies on for reasoning and retrieval, while allowing redistribution among less critical tail tokens.\n\nThe paper argues that a primary cause of performance trade-offs with activation steering is attention rerouting: steering vectors alter query-key matching, shifting attention away from contextually important tokens toward less informative ones.\n\nAccording to the authors, SKOP achieves the best joint steering-utility trade-off, reducing utility degradation by 5-7x while retaining over 95% of vanilla steering efficacy.\n\nThe method works by removing only the components that strongly shift attention from the focus set to the tail set by comparing the tokens a head attends to strongly on utility tasks with those it attends to weakly, using differences in their key representations to identify steering components likely to cause harmful attention shifts, and then removing only these components selectively from a small set of risk heads."
    ],
    "durationSeconds": 11.962793307999965,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "10c19e30-9a6d-4f5c-88c4-17a81ca1512e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 94 · 2026-05-19T13:19:36.032Z_

<details><summary>Logged reasoning block</summary>

```text
The activation steering landscape has gotten very crowded in 2026 with many new methods. Let me check for a few more potentially missing competitors and then assess the overall idea.

Let me search for some more specific things:
1. Any work that directly combines bias decomposition with adaptive routing
2. The Liu paper's non-linear MLP approach more specifically
3. Any recent survey of activation steering methods
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eff44a0-bc96-4efc-9e98-2ba27e53b5a2",
  "isSidechain": false,
  "requestId": "req_011CbBzejfVNGcTAM92Z2eN8",
  "type": "assistant",
  "uuid": "4cf8f7f8-d670-43e1-9dd5-b814cb4e34ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMnxtdEX835oTrvoRcgVCN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 48323,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 48323,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 95 · 2026-05-19T13:19:37.452Z_

The steering landscape is very crowded. Let me now check for the most critical gap — whether anyone has already done what this proposal claims is novel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cf8f7f8-d670-43e1-9dd5-b814cb4e34ba",
  "isSidechain": false,
  "requestId": "req_011CbBzejfVNGcTAM92Z2eN8",
  "type": "assistant",
  "uuid": "c3dccba4-7cd6-48f4-8bd3-739d49dcda9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMnxtdEX835oTrvoRcgVCN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 48323,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 48323,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 96 · 2026-05-19T13:19:37.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Quxqt4w597UgwvH2ufop6W`</summary>

```json
{
  "query": "adaptive routing different steering interventions per-instance LLM linear nonlinear abstention 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3dccba4-7cd6-48f4-8bd3-739d49dcda9b",
  "isSidechain": false,
  "requestId": "req_011CbBzejfVNGcTAM92Z2eN8",
  "type": "assistant",
  "uuid": "89cd2d12-b19b-407d-8417-1185cadbe468",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMnxtdEX835oTrvoRcgVCN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 48323,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 48323,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 97 · 2026-05-19T13:19:45.151Z_

<details><summary>↩ Tool result · `toolu_01Quxqt4w597UgwvH2ufop6W`</summary>

```text
Web search results for query: "adaptive routing different steering interventions per-instance LLM linear nonlinear abstention 2026"

Links: [{"title":"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs","url":"https://arxiv.org/pdf/2505.20309"},{"title":"Steering Frozen LLMs: Adaptive Social Alignment via Online Prompt Routing","url":"https://arxiv.org/pdf/2603.15647"},{"title":"Curveball Steering: The Right Direction To Steer Isn’t Always Linear","url":"https://arxiv.org/html/2603.09313v2"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories | Request PDF","url":"https://www.researchgate.net/publication/391029754_Adaptive_Activation_Steering_A_Tuning-Free_LLM_Truthfulness_Improvement_Method_for_Diverse_Hallucinations_Categories"},{"title":"Behavioral Alignment & Steering in LLMs","url":"https://www.emergentmind.com/topics/behavioral-alignment-and-steering-in-llms"},{"title":"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/html/2605.05715"},{"title":"Beyond Linear Steering: Unified Multi-Attribute Control for Language Models","url":"https://arxiv.org/pdf/2505.24535"}]

I found several relevant results on adaptive routing and steering interventions for LLMs in 2026. Here's what the search returned:

## Key Findings:

**Adaptive Steering with Abstention:**
Mechanistic Error Reduction with Abstention (MERA) is a principled framework for steering language models to mitigate errors through selective, adaptive interventions. MERA optimizes intervention direction and calibrates when and how much to steer, thereby provably improving performance or abstaining when no confident correction is possible.

**Linear vs. Nonlinear Steering:**
Reliable LLM control requires geometry-aware interventions, and nonlinear steering provides a principled and practical alternative to global linear steering methods. Curveball steering is a nonlinear steering method based on polynomial kernel PCA that performs interventions in a feature space, better respecting the learned activation geometry.

**Instance-Adaptive Methods:**
K-Steering is a unified approach that trains a single non-linear multi-label classifier on hidden activations and computes intervention directions via gradients at inference time, avoiding linearity assumptions and allowing dynamic composition of behaviors without retraining. Instance-adaptive methods like K-CAST are being explored as more sophisticated learned interventions.

**Recent Directions:**
Emergent directions include adaptive, input-conditioned, or context-sensitive vector selection and hierarchical/feedback-driven controllers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89cd2d12-b19b-407d-8417-1185cadbe468",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "8db05ac5-c535-482a-b6ff-1509ef572648",
  "toolUseResult": {
    "query": "adaptive routing different steering interventions per-instance LLM linear nonlinear abstention 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017uKoijthuJBEYecUJ6tR4s",
        "content": [
          {
            "title": "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs",
            "url": "https://arxiv.org/pdf/2505.20309"
          },
          {
            "title": "Steering Frozen LLMs: Adaptive Social Alignment via Online Prompt Routing",
            "url": "https://arxiv.org/pdf/2603.15647"
          },
          {
            "title": "Curveball Steering: The Right Direction To Steer Isn’t Always Linear",
            "url": "https://arxiv.org/html/2603.09313v2"
          },
          {
            "title": "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories | Request PDF",
            "url": "https://www.researchgate.net/publication/391029754_Adaptive_Activation_Steering_A_Tuning-Free_LLM_Truthfulness_Improvement_Method_for_Diverse_Hallucinations_Categories"
          },
          {
            "title": "Behavioral Alignment & Steering in LLMs",
            "url": "https://www.emergentmind.com/topics/behavioral-alignment-and-steering-in-llms"
          },
          {
            "title": "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/html/2605.05715"
          },
          {
            "title": "Beyond Linear Steering: Unified Multi-Attribute Control for Language Models",
            "url": "https://arxiv.org/pdf/2505.24535"
          }
        ]
      },
      "I found several relevant results on adaptive routing and steering interventions for LLMs in 2026. Here's what the search returned:\n\n## Key Findings:\n\n**Adaptive Steering with Abstention:**\nMechanistic Error Reduction with Abstention (MERA) is a principled framework for steering language models to mitigate errors through selective, adaptive interventions. MERA optimizes intervention direction and calibrates when and how much to steer, thereby provably improving performance or abstaining when no confident correction is possible.\n\n**Linear vs. Nonlinear Steering:**\nReliable LLM control requires geometry-aware interventions, and nonlinear steering provides a principled and practical alternative to global linear steering methods. Curveball steering is a nonlinear steering method based on polynomial kernel PCA that performs interventions in a feature space, better respecting the learned activation geometry.\n\n**Instance-Adaptive Methods:**\nK-Steering is a unified approach that trains a single non-linear multi-label classifier on hidden activations and computes intervention directions via gradients at inference time, avoiding linearity assumptions and allowing dynamic composition of behaviors without retraining. Instance-adaptive methods like K-CAST are being explored as more sophisticated learned interventions.\n\n**Recent Directions:**\nEmergent directions include adaptive, input-conditioned, or context-sensitive vector selection and hierarchical/feedback-driven controllers."
    ],
    "durationSeconds": 7.147035884999961,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "89cd2d12-b19b-407d-8417-1185cadbe468",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 98 · 2026-05-19T13:19:45.158Z_

```json
{
  "parentUuid": "8db05ac5-c535-482a-b6ff-1509ef572648",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6f3e8e62-2ff6-4491-84bc-7fd1b9ea61bd",
  "timestamp": "2026-05-19T13:19:45.158Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 99 · 2026-05-19T13:19:47.538Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uc8CkZ68iLG6Cy9E5qmsew`</summary>

```json
{
  "query": "\"Beyond Linear Steering\" unified multi-attribute control language models arXiv 2505.24535"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f3e8e62-2ff6-4491-84bc-7fd1b9ea61bd",
  "isSidechain": false,
  "requestId": "req_011CbBzfiAyNLF3tS1tRwhgX",
  "type": "assistant",
  "uuid": "3d76bda9-8cb5-4ad2-b357-f81f07669d4b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hi7NVLZXGyQ1iA6ukC4ooT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1026,
      "cache_read_input_tokens": 49046,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 49046,
          "cache_creation_input_tokens": 1026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1026
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

_source line 100 · 2026-05-19T13:19:56.349Z_

<details><summary>↩ Tool result · `toolu_01Uc8CkZ68iLG6Cy9E5qmsew`</summary>

```text
Web search results for query: ""Beyond Linear Steering" unified multi-attribute control language models arXiv 2505.24535"

Links: [{"title":"[2505.24535] Beyond Linear Steering: Unified Multi-Attribute Control for Language Models","url":"https://arxiv.org/abs/2505.24535"},{"title":"Beyond Linear Steering: Unified Multi-Attribute Control for Language Models","url":"https://arxiv.org/html/2505.24535"},{"title":"Beyond Linear Steering: Unified Multi-Attribute Control for Language Models | OpenReview","url":"https://openreview.net/forum?id=jPP3zT5Q4s"},{"title":"Beyond Linear Steering: Unified Multi-Attribute Control for Language Models","url":"https://arxiv.org/pdf/2505.24535"},{"title":"MSRS: Adaptive Multi-Subspace Representation Steering for Attribute Alignment in Large Language Models","url":"https://arxiv.org/html/2508.10599v1"},{"title":"Steering smarter. Why K-Steering is reshaping LLM… | by Thoughtworks | Medium","url":"https://thoughtworks.medium.com/steering-smarter-4fbfbdb58803"},{"title":"PIXEL: Adaptive Steering Via Position-wise Injection with eXact Estimated Levels under Subspace Calibration","url":"https://arxiv.org/html/2510.10205v1"},{"title":"Artificial Intelligence May 2025","url":"https://arxiv.org/list/cs.AI/2025-05?skip=4450&show=250"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=19775&show=100"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=2800&show=50"}]

I found the paper you were looking for. Here's what the research is about:

## "Beyond Linear Steering: Unified Multi-Attribute Control for Language Models"

**Authors:** Narmeen Oozeer, Luke Marks, Shreyans Jain, Fazl Barez, and Amirali Abdullah

**arXiv ID:** 2505.24535 (Accepted to Findings of EMNLP, 2025)

### Overview

The paper addresses the challenging problem of controlling multiple behavioral attributes in large language models (LLMs) at inference time, which is complicated by interference between attributes and the limitations of linear steering methods that assume additive behavior in activation space and require per-attribute tuning.

### Key Contribution

The authors introduce K-Steering, a unified and flexible approach that trains a single non-linear multi-label classifier on hidden activations and computes intervention directions via gradients at inference time, avoiding linearity assumptions, removing the need for storing and tuning separate attribute vectors, and allowing dynamic composition of behaviors without retraining.

### Evaluation

The paper proposes two new benchmarks, ToneBank and DebateMix, targeting compositional behavioral control. Empirical results across 3 model families, validated by both activation-based classifiers and LLM-based judges, demonstrate that K-Steering outperforms strong baselines in accurately steering multiple behaviors.

The paper is available on arXiv and has been submitted to major venues in the field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d76bda9-8cb5-4ad2-b357-f81f07669d4b",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "2d5f2e27-9edb-455e-abda-948d232c9c51",
  "toolUseResult": {
    "query": "\"Beyond Linear Steering\" unified multi-attribute control language models arXiv 2505.24535",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MdBQgLUo84NBbWDqgX97xQ",
        "content": [
          {
            "title": "[2505.24535] Beyond Linear Steering: Unified Multi-Attribute Control for Language Models",
            "url": "https://arxiv.org/abs/2505.24535"
          },
          {
            "title": "Beyond Linear Steering: Unified Multi-Attribute Control for Language Models",
            "url": "https://arxiv.org/html/2505.24535"
          },
          {
            "title": "Beyond Linear Steering: Unified Multi-Attribute Control for Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=jPP3zT5Q4s"
          },
          {
            "title": "Beyond Linear Steering: Unified Multi-Attribute Control for Language Models",
            "url": "https://arxiv.org/pdf/2505.24535"
          },
          {
            "title": "MSRS: Adaptive Multi-Subspace Representation Steering for Attribute Alignment in Large Language Models",
            "url": "https://arxiv.org/html/2508.10599v1"
          },
          {
            "title": "Steering smarter. Why K-Steering is reshaping LLM… | by Thoughtworks | Medium",
            "url": "https://thoughtworks.medium.com/steering-smarter-4fbfbdb58803"
          },
          {
            "title": "PIXEL: Adaptive Steering Via Position-wise Injection with eXact Estimated Levels under Subspace Calibration",
            "url": "https://arxiv.org/html/2510.10205v1"
          },
          {
            "title": "Artificial Intelligence May 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-05?skip=4450&show=250"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=19775&show=100"
          },
          {
            "title": "Computation and Language May 2025",
            "url": "https://www.arxiv.org/list/cs.CL/2025-05?skip=2800&show=50"
          }
        ]
      },
      "I found the paper you were looking for. Here's what the research is about:\n\n## \"Beyond Linear Steering: Unified Multi-Attribute Control for Language Models\"\n\n**Authors:** Narmeen Oozeer, Luke Marks, Shreyans Jain, Fazl Barez, and Amirali Abdullah\n\n**arXiv ID:** 2505.24535 (Accepted to Findings of EMNLP, 2025)\n\n### Overview\n\nThe paper addresses the challenging problem of controlling multiple behavioral attributes in large language models (LLMs) at inference time, which is complicated by interference between attributes and the limitations of linear steering methods that assume additive behavior in activation space and require per-attribute tuning.\n\n### Key Contribution\n\nThe authors introduce K-Steering, a unified and flexible approach that trains a single non-linear multi-label classifier on hidden activations and computes intervention directions via gradients at inference time, avoiding linearity assumptions, removing the need for storing and tuning separate attribute vectors, and allowing dynamic composition of behaviors without retraining.\n\n### Evaluation\n\nThe paper proposes two new benchmarks, ToneBank and DebateMix, targeting compositional behavioral control. Empirical results across 3 model families, validated by both activation-based classifiers and LLM-based judges, demonstrate that K-Steering outperforms strong baselines in accurately steering multiple behaviors.\n\nThe paper is available on arXiv and has been submitted to major venues in the field."
    ],
    "durationSeconds": 8.806934427,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3d76bda9-8cb5-4ad2-b357-f81f07669d4b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 101_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "2d5f2e27-9edb-455e-abda-948d232c9c51",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 102_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Tool call

_source line 103 · 2026-05-19T13:20:00.349Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TqY6ah3H14A4sdhfbsefrN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.24535",
  "prompt": "Extract the full abstract. Does K-Steering do per-instance routing between different intervention strategies (linear vs nonlinear)? Does it address calibration? What exactly does the gradient-based steering do?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d5f2e27-9edb-455e-abda-948d232c9c51",
  "isSidechain": false,
  "requestId": "req_011CbBzgY2Z2hoh7U9EQ68cT",
  "type": "assistant",
  "uuid": "e27bbc55-247b-4c97-bd6e-0dd83e940644",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016A2B4BdXnLFWoefS6dqzZ5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 49046,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1935,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 49046,
          "cache_creation_input_tokens": 1935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1935
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

_source line 104 · 2026-05-19T13:20:05.891Z_

<details><summary>↩ Tool result · `toolu_01TqY6ah3H14A4sdhfbsefrN`</summary>

```text
# Analysis of K-Steering Paper

## Full Abstract

"Controlling multiple behavioral attributes in large language models (LLMs) at inference time is a challenging problem due to interference between attributes and the limitations of linear steering methods, which assume additive behavior in activation space and require per-attribute tuning. We introduce K-Steering, a unified and flexible approach that trains a single non-linear multi-label classifier on hidden activations and computes intervention directions via gradients at inference time. This avoids linearity assumptions, removes the need for storing and tuning separate attribute vectors, and allows dynamic composition of behaviors without retraining. To evaluate our method, we propose two new benchmarks, ToneBank and DebateMix, targeting compositional behavioral control. Empirical results across 3 model families, validated by both activation-based classifiers and LLM-based judges, demonstrate that K-Steering outperforms strong baselines in accurately steering multiple behaviors."

## Answers to Your Questions

**Per-instance routing between strategies?** The abstract does not mention any per-instance routing mechanism that dynamically selects between linear versus nonlinear approaches.

**Calibration addressed?** The abstract makes no reference to calibration or calibration methods.

**Gradient-based steering mechanism?** The approach "computes intervention directions via gradients at inference time" by utilizing a trained classifier on hidden activations, though the exact computational details remain unspecified in this summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e27bbc55-247b-4c97-bd6e-0dd83e940644",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "33a24b7e-4c1f-4581-923f-687b5cbc3436",
  "toolUseResult": {
    "bytes": 47121,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of K-Steering Paper\n\n## Full Abstract\n\n\"Controlling multiple behavioral attributes in large language models (LLMs) at inference time is a challenging problem due to interference between attributes and the limitations of linear steering methods, which assume additive behavior in activation space and require per-attribute tuning. We introduce K-Steering, a unified and flexible approach that trains a single non-linear multi-label classifier on hidden activations and computes intervention directions via gradients at inference time. This avoids linearity assumptions, removes the need for storing and tuning separate attribute vectors, and allows dynamic composition of behaviors without retraining. To evaluate our method, we propose two new benchmarks, ToneBank and DebateMix, targeting compositional behavioral control. Empirical results across 3 model families, validated by both activation-based classifiers and LLM-based judges, demonstrate that K-Steering outperforms strong baselines in accurately steering multiple behaviors.\"\n\n## Answers to Your Questions\n\n**Per-instance routing between strategies?** The abstract does not mention any per-instance routing mechanism that dynamically selects between linear versus nonlinear approaches.\n\n**Calibration addressed?** The abstract makes no reference to calibration or calibration methods.\n\n**Gradient-based steering mechanism?** The approach \"computes intervention directions via gradients at inference time\" by utilizing a trained classifier on hidden activations, though the exact computational details remain unspecified in this summary.",
    "durationMs": 5534,
    "url": "https://arxiv.org/abs/2505.24535"
  },
  "sourceToolAssistantUUID": "e27bbc55-247b-4c97-bd6e-0dd83e940644",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-19T13:20:08.293Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ts1G5iSxkaG6zHEEEWbNG2`</summary>

```json
{
  "query": "MERA mechanistic error reduction abstention steering selective intervention language model arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33a24b7e-4c1f-4581-923f-687b5cbc3436",
  "isSidechain": false,
  "requestId": "req_011CbBzhEpytpMWWEehxhk8T",
  "type": "assistant",
  "uuid": "4646802a-094e-40d7-8574-822f6df3ab8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Ap7CEtmZM87pbj34JkzF1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 50981,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 450,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 50981,
          "cache_creation_input_tokens": 450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 450
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

_source line 106 · 2026-05-19T13:20:14.180Z_

<details><summary>↩ Tool result · `toolu_01Ts1G5iSxkaG6zHEEEWbNG2`</summary>

```text
Web search results for query: "MERA mechanistic error reduction abstention steering selective intervention language model arXiv 2026"

Links: [{"title":"To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models | OpenReview","url":"https://openreview.net/forum?id=fUCPq5RvmH"},{"title":"To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models","url":"https://proceedings.mlr.press/v267/hedstrom25a.html"},{"title":"ICML Poster To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models","url":"https://icml.cc/virtual/2025/poster/44524"},{"title":"[2510.13290] To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models","url":"https://arxiv.org/abs/2510.13290"},{"title":"To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models","url":"https://arxiv.org/html/2510.13290v1"},{"title":"(PDF) To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models","url":"https://www.researchgate.net/publication/396517741_To_Steer_or_Not_to_Steer_Mechanistic_Error_Reduction_with_Abstention_for_Language_Models"},{"title":"GitHub - annahedstroem/MERA-steering: Code and notebooks for Mechanistic Error Reduction with Abstention (MERA) — for effective and safe language model steering 🔥","url":"https://github.com/annahedstroem/MERA-steering"}]

Based on the search results, I found relevant information about MERA:

MERA (Mechanistic Error Reduction with Abstention) is a principled framework for steering language models to mitigate errors through selective, adaptive interventions. 

Unlike existing methods that rely on fixed, manually tuned steering strengths, MERA addresses these limitations by optimizing the intervention direction and calibrating when and how much to steer, thereby provably improving performance or abstaining when no confident correction is possible.

Experiments across diverse datasets and LM families demonstrate safe, effective, non-degrading error correction, and MERA can be applied on top of existing steering techniques to further enhance their performance, establishing it as a general-purpose and efficient approach to mechanistic activation steering.

The paper was authored by Hedström et al. and published at ICML 2025. The arXiv paper number is 2510.13290, and the framework features selective steering (steer only if the probe's estimated error is larger than a calibrated threshold), adaptive strength (steering intensity scales with the probe's estimated error), and global abstention (steer only when confident).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4646802a-094e-40d7-8574-822f6df3ab8f",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "5cf47946-0651-4838-aa9b-b650984f121c",
  "toolUseResult": {
    "query": "MERA mechanistic error reduction abstention steering selective intervention language model arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018QCD34GCLbyuL4ty3NefN1",
        "content": [
          {
            "title": "To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=fUCPq5RvmH"
          },
          {
            "title": "To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models",
            "url": "https://proceedings.mlr.press/v267/hedstrom25a.html"
          },
          {
            "title": "ICML Poster To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models",
            "url": "https://icml.cc/virtual/2025/poster/44524"
          },
          {
            "title": "[2510.13290] To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models",
            "url": "https://arxiv.org/abs/2510.13290"
          },
          {
            "title": "To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models",
            "url": "https://arxiv.org/html/2510.13290v1"
          },
          {
            "title": "(PDF) To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models",
            "url": "https://www.researchgate.net/publication/396517741_To_Steer_or_Not_to_Steer_Mechanistic_Error_Reduction_with_Abstention_for_Language_Models"
          },
          {
            "title": "GitHub - annahedstroem/MERA-steering: Code and notebooks for Mechanistic Error Reduction with Abstention (MERA) — for effective and safe language model steering 🔥",
            "url": "https://github.com/annahedstroem/MERA-steering"
          }
        ]
      },
      "Based on the search results, I found relevant information about MERA:\n\nMERA (Mechanistic Error Reduction with Abstention) is a principled framework for steering language models to mitigate errors through selective, adaptive interventions. \n\nUnlike existing methods that rely on fixed, manually tuned steering strengths, MERA addresses these limitations by optimizing the intervention direction and calibrating when and how much to steer, thereby provably improving performance or abstaining when no confident correction is possible.\n\nExperiments across diverse datasets and LM families demonstrate safe, effective, non-degrading error correction, and MERA can be applied on top of existing steering techniques to further enhance their performance, establishing it as a general-purpose and efficient approach to mechanistic activation steering.\n\nThe paper was authored by Hedström et al. and published at ICML 2025. The arXiv paper number is 2510.13290, and the framework features selective steering (steer only if the probe's estimated error is larger than a calibrated threshold), adaptive strength (steering intensity scales with the probe's estimated error), and global abstention (steer only when confident)."
    ],
    "durationSeconds": 5.883680068999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4646802a-094e-40d7-8574-822f6df3ab8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 107 · 2026-05-19T13:20:18.002Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important! MERA (ICML 2025) already does selective steering with abstention, optimizing when/how much to steer. This is quite relevant to the DBS-v2 proposal which claims to route between steering and abstention. Let me check this more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cf47946-0651-4838-aa9b-b650984f121c",
  "isSidechain": false,
  "requestId": "req_011CbBzhrEDWD3A3onhWjWBU",
  "type": "assistant",
  "uuid": "a02d7b8a-9af9-40db-bc4a-10d67d66f069",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TX55j6ek5RoTKMXbZ82MiM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 51431,
      "output_tokens": 247,
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
          "output_tokens": 247,
          "cache_read_input_tokens": 51431,
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
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 108 · 2026-05-19T13:20:18.511Z_

This is a critical finding — MERA at ICML 2025 already does selective steering with abstention. Let me investigate deeper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a02d7b8a-9af9-40db-bc4a-10d67d66f069",
  "isSidechain": false,
  "requestId": "req_011CbBzhrEDWD3A3onhWjWBU",
  "type": "assistant",
  "uuid": "d96a797e-4b1b-41b7-8dea-9e25853a4482",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TX55j6ek5RoTKMXbZ82MiM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 51431,
      "output_tokens": 247,
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
          "output_tokens": 247,
          "cache_read_input_tokens": 51431,
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-19T13:20:19.976Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V46GVeXRqFnBmSx179ryZM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.13290",
  "prompt": "Extract the full abstract. Does MERA route between different intervention strategies (e.g., linear vs nonlinear)? Does it address calibration specifically? Does it handle multiple competing biases/directions? What's the relationship between probe-based diagnosis and intervention?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d96a797e-4b1b-41b7-8dea-9e25853a4482",
  "isSidechain": false,
  "requestId": "req_011CbBzhrEDWD3A3onhWjWBU",
  "type": "assistant",
  "uuid": "134a17da-ace5-40ab-a63a-173494e06808",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TX55j6ek5RoTKMXbZ82MiM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 51431,
      "output_tokens": 247,
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
          "output_tokens": 247,
          "cache_read_input_tokens": 51431,
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-19T13:20:30.781Z_

<details><summary>↩ Tool result · `toolu_01V46GVeXRqFnBmSx179ryZM`</summary>

```text
# Analysis of MERA Paper

## Full Abstract
"We introduce Mechanistic Error Reduction with Abstention (MERA), a principled framework for steering language models (LMs) to mitigate errors through selective, adaptive interventions. Unlike existing methods that rely on fixed, manually tuned steering strengths, often resulting in under or oversteering, MERA addresses these limitations by (i) optimising the intervention direction, and (ii) calibrating when, and how much to steer, thereby provably improving performance or abstaining when no confident correction is possible."

## Answers Based on Available Information

**Routing between intervention strategies:** The abstract does not specify whether MERA routes between different intervention types (linear vs. nonlinear). It only mentions "optimising the intervention direction" without clarifying if multiple strategy types are evaluated.

**Calibration:** Yes, the framework explicitly addresses calibration. The abstract states it involves "calibrating when, and how much to steer," representing a core component of the method.

**Multiple competing biases:** The provided content does not discuss handling multiple competing biases or directions—only optimization of "the intervention direction" (singular form).

**Probe-based diagnosis and intervention relationship:** The webpage excerpt does not contain information about probe-based diagnosis or its connection to intervention mechanisms.

**Note:** For detailed answers on routing strategies, competing biases, and diagnostic approaches, the full paper would need to be consulted beyond this abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "134a17da-ace5-40ab-a63a-173494e06808",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "5b438837-9011-4b24-b1ba-9523222063ac",
  "toolUseResult": {
    "bytes": 46663,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of MERA Paper\n\n## Full Abstract\n\"We introduce Mechanistic Error Reduction with Abstention (MERA), a principled framework for steering language models (LMs) to mitigate errors through selective, adaptive interventions. Unlike existing methods that rely on fixed, manually tuned steering strengths, often resulting in under or oversteering, MERA addresses these limitations by (i) optimising the intervention direction, and (ii) calibrating when, and how much to steer, thereby provably improving performance or abstaining when no confident correction is possible.\"\n\n## Answers Based on Available Information\n\n**Routing between intervention strategies:** The abstract does not specify whether MERA routes between different intervention types (linear vs. nonlinear). It only mentions \"optimising the intervention direction\" without clarifying if multiple strategy types are evaluated.\n\n**Calibration:** Yes, the framework explicitly addresses calibration. The abstract states it involves \"calibrating when, and how much to steer,\" representing a core component of the method.\n\n**Multiple competing biases:** The provided content does not discuss handling multiple competing biases or directions—only optimization of \"the intervention direction\" (singular form).\n\n**Probe-based diagnosis and intervention relationship:** The webpage excerpt does not contain information about probe-based diagnosis or its connection to intervention mechanisms.\n\n**Note:** For detailed answers on routing strategies, competing biases, and diagnostic approaches, the full paper would need to be consulted beyond this abstract.",
    "durationMs": 10800,
    "url": "https://arxiv.org/abs/2510.13290"
  },
  "sourceToolAssistantUUID": "134a17da-ace5-40ab-a63a-173494e06808",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-19T13:20:33.306Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NmNaP2WS5HoFraa6RuVkBN`</summary>

```json
{
  "query": "Gemma 4 31B dense model Google 2026 release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b438837-9011-4b24-b1ba-9523222063ac",
  "isSidechain": false,
  "requestId": "req_011CbBzj5EaaZTYoEuiSjn6v",
  "type": "assistant",
  "uuid": "aa58b972-2fa0-4ab6-91af-6200d4ddf940",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZtpoPupV1UqBTc3iQGkj2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 574,
      "cache_read_input_tokens": 52232,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 52232,
          "cache_creation_input_tokens": 574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 574
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

_source line 112 · 2026-05-19T13:20:39.678Z_

<details><summary>↩ Tool result · `toolu_01NmNaP2WS5HoFraa6RuVkBN`</summary>

```text
Web search results for query: "Gemma 4 31B dense model Google 2026 release"

Links: [{"title":"google/gemma-4-31B · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B"},{"title":"Gemma 4: Byte for byte, the most capable open models","url":"https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/"},{"title":"Gemma 4: How a 31B Model Beats 400B Rivals [2026]","url":"https://tech-insider.org/google-gemma-4-open-model-benchmarks-2026/"},{"title":"Gemma 4 by Google: Specs, Benchmarks, Model Sizes, and How to Run It Locally (2026 Guide)","url":"https://aurigait.com/blog/gemma-4-features-benchmarks-guide/"},{"title":"Gemma 4 Review: Google's 31B Open Model Beats 600B Rivals (2026) - TokenMix Blog","url":"https://tokenmix.ai/blog/gemma-4-review-open-source-benchmarks-2026"},{"title":"Benchmarking Google Gemma 4 26B and 31B Locally | Enterprise Unified LLM API Gateway (One Key for All Models) | n1n.ai","url":"https://explore.n1n.ai/blog/benchmarking-google-gemma-4-26b-31b-locally-2026-04-06"},{"title":"google/gemma-4-31B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B-it"},{"title":"Google Gemma 4 Review: How a 31B Open Model Beats 400B Rivals | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/technology/2026/google-gemma-4-review-2026"},{"title":"Gemma 4 31B Inference, Google's Dense Vision Model | Modular","url":"https://www.modular.com/models/gemma-4-31b-it"},{"title":"Google Gemma 4: A Technical Overview","url":"https://www.labellerr.com/blog/gemma-4-open-weight-ai-model-overview/"}]

Based on the search results, here's what I found about Google's Gemma 4 31B dense model:

## Release Information

Google released Gemma 4 on April 2, 2026, with four versatile sizes: Effective 2B (E2B), Effective 4B (E4B), 26B Mixture of Experts (MoE) and 31B Dense.

## Key Features of the 31B Dense Model

The 31B Dense is maximizing raw quality and provides a powerful foundation for fine-tuning. The Gemma 4 31B is a 31-billion-parameter dense model with a 256K context window, built for demanding tasks that require deep reasoning across large inputs.

## Performance

The 31B model currently ranks as the #3 open model in the world on the industry-standard Arena AI text leaderboard. On benchmarks, Gemma 4 scored 89.2% on AIME 2026 Mathematics, 80.0% on LiveCodeBench v6 coding benchmark, and 84.3% on GPQA Diamond science benchmark.

## Licensing and Availability

All models are available under the Apache 2.0 open-source license. All four models are available on Hugging Face, Kaggle, and Ollama, and Google AI Studio lets you test the 31B and 26B MoE in a browser with no setup.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa58b972-2fa0-4ab6-91af-6200d4ddf940",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "3e6f0135-a4e1-4466-b6fc-fcd11bea958e",
  "toolUseResult": {
    "query": "Gemma 4 31B dense model Google 2026 release",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JSWg4sm4xCk1KHmVpDn1Vj",
        "content": [
          {
            "title": "google/gemma-4-31B · Hugging Face",
            "url": "https://huggingface.co/google/gemma-4-31B"
          },
          {
            "title": "Gemma 4: Byte for byte, the most capable open models",
            "url": "https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/"
          },
          {
            "title": "Gemma 4: How a 31B Model Beats 400B Rivals [2026]",
            "url": "https://tech-insider.org/google-gemma-4-open-model-benchmarks-2026/"
          },
          {
            "title": "Gemma 4 by Google: Specs, Benchmarks, Model Sizes, and How to Run It Locally (2026 Guide)",
            "url": "https://aurigait.com/blog/gemma-4-features-benchmarks-guide/"
          },
          {
            "title": "Gemma 4 Review: Google's 31B Open Model Beats 600B Rivals (2026) - TokenMix Blog",
            "url": "https://tokenmix.ai/blog/gemma-4-review-open-source-benchmarks-2026"
          },
          {
            "title": "Benchmarking Google Gemma 4 26B and 31B Locally | Enterprise Unified LLM API Gateway (One Key for All Models) | n1n.ai",
            "url": "https://explore.n1n.ai/blog/benchmarking-google-gemma-4-26b-31b-locally-2026-04-06"
          },
          {
            "title": "google/gemma-4-31B-it · Hugging Face",
            "url": "https://huggingface.co/google/gemma-4-31B-it"
          },
          {
            "title": "Google Gemma 4 Review: How a 31B Open Model Beats 400B Rivals | StartupHub.ai",
            "url": "https://www.startuphub.ai/ai-news/technology/2026/google-gemma-4-review-2026"
          },
          {
            "title": "Gemma 4 31B Inference, Google's Dense Vision Model | Modular",
            "url": "https://www.modular.com/models/gemma-4-31b-it"
          },
          {
            "title": "Google Gemma 4: A Technical Overview",
            "url": "https://www.labellerr.com/blog/gemma-4-open-weight-ai-model-overview/"
          }
        ]
      },
      "Based on the search results, here's what I found about Google's Gemma 4 31B dense model:\n\n## Release Information\n\nGoogle released Gemma 4 on April 2, 2026, with four versatile sizes: Effective 2B (E2B), Effective 4B (E4B), 26B Mixture of Experts (MoE) and 31B Dense.\n\n## Key Features of the 31B Dense Model\n\nThe 31B Dense is maximizing raw quality and provides a powerful foundation for fine-tuning. The Gemma 4 31B is a 31-billion-parameter dense model with a 256K context window, built for demanding tasks that require deep reasoning across large inputs.\n\n## Performance\n\nThe 31B model currently ranks as the #3 open model in the world on the industry-standard Arena AI text leaderboard. On benchmarks, Gemma 4 scored 89.2% on AIME 2026 Mathematics, 80.0% on LiveCodeBench v6 coding benchmark, and 84.3% on GPQA Diamond science benchmark.\n\n## Licensing and Availability\n\nAll models are available under the Apache 2.0 open-source license. All four models are available on Hugging Face, Kaggle, and Ollama, and Google AI Studio lets you test the 31B and 26B MoE in a browser with no setup."
    ],
    "durationSeconds": 6.366569112000056,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "aa58b972-2fa0-4ab6-91af-6200d4ddf940",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-19T13:20:42.558Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P3FKwveFTr3sUAzmh9U9Wc`</summary>

```json
{
  "query": "Qwen3-8B model release 2026 open weight"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e6f0135-a4e1-4466-b6fc-fcd11bea958e",
  "isSidechain": false,
  "requestId": "req_011CbBzjjHK8Az2NTHUNGiqK",
  "type": "assistant",
  "uuid": "bbbb176c-89e0-4ddb-a234-e00369525ce9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpzBfxvLmPDATuEe4Qziwc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1579,
      "cache_read_input_tokens": 52232,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1579,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 52232,
          "cache_creation_input_tokens": 1579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1579
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

_source line 114 · 2026-05-19T13:20:48.945Z_

<details><summary>↩ Tool result · `toolu_01P3FKwveFTr3sUAzmh9U9Wc`</summary>

```text
Web search results for query: "Qwen3-8B model release 2026 open weight"

Links: [{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen - Wikipedia","url":"https://en.wikipedia.org/wiki/Qwen"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3"},{"title":"Qwen/Qwen3-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B"},{"title":"Qwen3-Coder-Next: The Complete 2026 Guide to Running Powerful AI Coding Agents Locally - DEV Community","url":"https://dev.to/sienna/qwen3-coder-next-the-complete-2026-guide-to-running-powerful-ai-coding-agents-locally-1k95"},{"title":"Alibaba Qwen Team Releases Qwen3.6-27B: A Dense Open-Weight Model Outperforming 397B MoE on Agentic Coding Benchmarks - MarkTechPost","url":"https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/"},{"title":"Qwen3.5","url":"https://qwen.ai/research"},{"title":"Qwen 3.7: Release Date, Status, and What's Real vs Rumored (2026)","url":"https://codersera.com/blog/qwen-3-7-release-date-whats-new-2026/"},{"title":"Qwen 3 Release Date: AI Performance Analysis and Model Timeline - H3sync","url":"https://h3sync.com/blog/qwen-3-release-date/"}]

Based on the search results, here's what I found about the Qwen3-8B model release:

## Qwen3-8B Open-Weight Release

Qwen3-8B is an open-weighted dense model released under the Apache 2.0 license, making it freely available for public use. The model is available on platforms like Hugging Face, ModelScope, and Kaggle.

### Key Features

Qwen3-8B uniquely supports seamless switching between thinking mode for complex logical reasoning, math, and coding, and non-thinking mode for efficient, general-purpose dialogue. The model surpasses previous QwQ (in thinking mode) and Qwen2.5 instruct models (in non-thinking mode) on mathematics, code generation, and commonsense logical reasoning.

### Performance and Capabilities

Due to advancements in model architecture, increased training data, and more effective training methods, Qwen3-8B-Base performs as well as Qwen2.5-14B-Base. The model supports 100+ languages and dialects with strong capabilities for multilingual instruction following and translation.

### Context Window

Qwen3-8B has a native context length of 32,768 tokens and supports 131,072 tokens with YaRN.

The model represents Alibaba's commitment to providing high-quality open-weight models that can compete with larger, proprietary alternatives.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbbb176c-89e0-4ddb-a234-e00369525ce9",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "6ec97376-2c42-4561-9aa7-0c8df421de80",
  "toolUseResult": {
    "query": "Qwen3-8B model release 2026 open weight",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pu3GdyMiCmSBamoPx9sUKu",
        "content": [
          {
            "title": "Qwen3: Think Deeper, Act Faster | Qwen",
            "url": "https://qwenlm.github.io/blog/qwen3/"
          },
          {
            "title": "GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub",
            "url": "https://github.com/QwenLM/Qwen3.6"
          },
          {
            "title": "Qwen - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Qwen"
          },
          {
            "title": "GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub",
            "url": "https://github.com/QwenLM/Qwen3"
          },
          {
            "title": "Qwen/Qwen3-8B · Hugging Face",
            "url": "https://huggingface.co/Qwen/Qwen3-8B"
          },
          {
            "title": "Qwen3-Coder-Next: The Complete 2026 Guide to Running Powerful AI Coding Agents Locally - DEV Community",
            "url": "https://dev.to/sienna/qwen3-coder-next-the-complete-2026-guide-to-running-powerful-ai-coding-agents-locally-1k95"
          },
          {
            "title": "Alibaba Qwen Team Releases Qwen3.6-27B: A Dense Open-Weight Model Outperforming 397B MoE on Agentic Coding Benchmarks - MarkTechPost",
            "url": "https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/"
          },
          {
            "title": "Qwen3.5",
            "url": "https://qwen.ai/research"
          },
          {
            "title": "Qwen 3.7: Release Date, Status, and What's Real vs Rumored (2026)",
            "url": "https://codersera.com/blog/qwen-3-7-release-date-whats-new-2026/"
          },
          {
            "title": "Qwen 3 Release Date: AI Performance Analysis and Model Timeline - H3sync",
            "url": "https://h3sync.com/blog/qwen-3-release-date/"
          }
        ]
      },
      "Based on the search results, here's what I found about the Qwen3-8B model release:\n\n## Qwen3-8B Open-Weight Release\n\nQwen3-8B is an open-weighted dense model released under the Apache 2.0 license, making it freely available for public use. The model is available on platforms like Hugging Face, ModelScope, and Kaggle.\n\n### Key Features\n\nQwen3-8B uniquely supports seamless switching between thinking mode for complex logical reasoning, math, and coding, and non-thinking mode for efficient, general-purpose dialogue. The model surpasses previous QwQ (in thinking mode) and Qwen2.5 instruct models (in non-thinking mode) on mathematics, code generation, and commonsense logical reasoning.\n\n### Performance and Capabilities\n\nDue to advancements in model architecture, increased training data, and more effective training methods, Qwen3-8B-Base performs as well as Qwen2.5-14B-Base. The model supports 100+ languages and dialects with strong capabilities for multilingual instruction following and translation.\n\n### Context Window\n\nQwen3-8B has a native context length of 32,768 tokens and supports 131,072 tokens with YaRN.\n\nThe model represents Alibaba's commitment to providing high-quality open-weight models that can compete with larger, proprietary alternatives."
    ],
    "durationSeconds": 6.382376089999976,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bbbb176c-89e0-4ddb-a234-e00369525ce9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 115_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "6ec97376-2c42-4561-9aa7-0c8df421de80",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 116_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Assistant

_source line 117 · 2026-05-19T13:20:51.861Z_

Good, model availability is confirmed. Now let me check for the most recent (May 2026) potential competitors I might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ec97376-2c42-4561-9aa7-0c8df421de80",
  "isSidechain": false,
  "requestId": "req_011CbBzkQsJjwGxVXCnGhJr1",
  "type": "assistant",
  "uuid": "5f9fa497-67a0-4c7a-b162-cc9f7f8fe45a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1Lfs9xSgRjuUzGmmYMkBp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 53811,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 100,
          "cache_read_input_tokens": 53811,
          "cache_creation_input_tokens": 1020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1020
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

_source line 118 · 2026-05-19T13:20:52.609Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G3e8xF16vkAeE9qMJmhWji`</summary>

```json
{
  "query": "calibration LLM activation steering probe correction May 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f9fa497-67a0-4c7a-b162-cc9f7f8fe45a",
  "isSidechain": false,
  "requestId": "req_011CbBzkQsJjwGxVXCnGhJr1",
  "type": "assistant",
  "uuid": "e35900d3-d1d1-40af-a3be-a3dd9f31a86b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1Lfs9xSgRjuUzGmmYMkBp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 53811,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 100,
          "cache_read_input_tokens": 53811,
          "cache_creation_input_tokens": 1020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1020
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

_source line 119 · 2026-05-19T13:20:59.885Z_

<details><summary>↩ Tool result · `toolu_01G3e8xF16vkAeE9qMJmhWji`</summary>

```text
Web search results for query: "calibration LLM activation steering probe correction May 2026 site:arxiv.org"

Links: [{"title":"Correctness-Optimized Residual Activation Lens (CORAL):","url":"https://arxiv.org/pdf/2602.06022"},{"title":"[2605.03907] Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/abs/2605.03907"},{"title":"[2605.03907v1] Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/abs/2605.03907v1"},{"title":"Steering Evaluation-Aware Language Models to Act Like They Are Deployed","url":"https://arxiv.org/html/2510.20487"},{"title":"Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs","url":"https://arxiv.org/pdf/2508.09019"},{"title":"Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering","url":"https://arxiv.org/html/2601.19847v1"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/pdf/2602.04428"},{"title":"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs","url":"https://arxiv.org/pdf/2505.20309"}]

I found several relevant arxiv papers matching your search query about LLM activation steering, calibration, and probes. Here are the main results:

1. **CORAL (Correctness-Optimized Residual Activation Lens)** - A regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes, which consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average. This paper was submitted in February 2026.

2. **Steer Like the LLM: Activation Steering that Mimics Prompting** - Introduces Prompt Steering Replacement (PSR) models that estimate token-specific steering coefficients from the activations themselves and are trained to imitate prompt-based interventions. This paper was submitted on May 5, 2026.

3. **Activation Steering for Bias Mitigation** - Uses techniques that train linear probes on internal activations to detect latent representations of biases, and leverages these findings to compute steering vectors by contrasting activation patterns for biased and neutral statements.

4. **Fine-Grained Activation Steering** - Addresses the limitation that block-level interventions ignore heterogeneity within block activations, which often span hundreds or thousands of dimensions.

The search returned several papers on this intersection of topics, with recent work from May 2026 focusing on improving how activation steering methods work and how they calibrate model behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e35900d3-d1d1-40af-a3be-a3dd9f31a86b",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "76e8b053-51c9-470c-93f5-0cd3d6a99d08",
  "toolUseResult": {
    "query": "calibration LLM activation steering probe correction May 2026 site:arxiv.org",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UzGJNtB6J9EqNWyKh8k1Je",
        "content": [
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL):",
            "url": "https://arxiv.org/pdf/2602.06022"
          },
          {
            "title": "[2605.03907] Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/abs/2605.03907"
          },
          {
            "title": "[2605.03907v1] Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/abs/2605.03907v1"
          },
          {
            "title": "Steering Evaluation-Aware Language Models to Act Like They Are Deployed",
            "url": "https://arxiv.org/html/2510.20487"
          },
          {
            "title": "Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs",
            "url": "https://arxiv.org/pdf/2508.09019"
          },
          {
            "title": "Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering",
            "url": "https://arxiv.org/html/2601.19847v1"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/html/2602.06022v1"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/pdf/2602.04428"
          },
          {
            "title": "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs",
            "url": "https://arxiv.org/pdf/2505.20309"
          }
        ]
      },
      "I found several relevant arxiv papers matching your search query about LLM activation steering, calibration, and probes. Here are the main results:\n\n1. **CORAL (Correctness-Optimized Residual Activation Lens)** - A regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes, which consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average. This paper was submitted in February 2026.\n\n2. **Steer Like the LLM: Activation Steering that Mimics Prompting** - Introduces Prompt Steering Replacement (PSR) models that estimate token-specific steering coefficients from the activations themselves and are trained to imitate prompt-based interventions. This paper was submitted on May 5, 2026.\n\n3. **Activation Steering for Bias Mitigation** - Uses techniques that train linear probes on internal activations to detect latent representations of biases, and leverages these findings to compute steering vectors by contrasting activation patterns for biased and neutral statements.\n\n4. **Fine-Grained Activation Steering** - Addresses the limitation that block-level interventions ignore heterogeneity within block activations, which often span hundreds or thousands of dimensions.\n\nThe search returned several papers on this intersection of topics, with recent work from May 2026 focusing on improving how activation steering methods work and how they calibrate model behavior."
    ],
    "durationSeconds": 7.272446499999962,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e35900d3-d1d1-40af-a3be-a3dd9f31a86b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-19T13:21:02.695Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011cUJZmT1dQFNH1c5iTA95Z`</summary>

```json
{
  "query": "overconfidence underconfidence LLM separate mechanisms decompose internal representations 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76e8b053-51c9-470c-93f5-0cd3d6a99d08",
  "isSidechain": false,
  "requestId": "req_011CbBzmDeu9ND17dEUhXX76",
  "type": "assistant",
  "uuid": "cd89565f-36b0-4b67-b097-4dca21e424cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHPfPTQ3KQ6M6ZymvdhPb8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1925,
      "cache_read_input_tokens": 53811,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 53811,
          "cache_creation_input_tokens": 1925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1925
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

_source line 121 · 2026-05-19T13:21:09.044Z_

<details><summary>↩ Tool result · `toolu_011cUJZmT1dQFNH1c5iTA95Z`</summary>

```text
Web search results for query: "overconfidence underconfidence LLM separate mechanisms decompose internal representations 2026"

Links: [{"title":"LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components","url":"https://arxiv.org/pdf/2508.17182"},{"title":"LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components","url":"https://arxiv.org/html/2508.17182"},{"title":"Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-026-01217-9"},{"title":"(PDF) How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models","url":"https://www.researchgate.net/publication/393476673_How_Overconfidence_in_Initial_Choices_and_Underconfidence_Under_Criticism_Modulate_Change_of_Mind_in_Large_Language_Models"},{"title":"Do Language Models Mirror Human Confidence? ...","url":"https://aclanthology.org/2025.findings-acl.1316.pdf"},{"title":"Do Language Models Mirror Human Confidence? Exploring Psychological Insights to Address Overconfidence in LLMs","url":"https://arxiv.org/pdf/2506.00582"},{"title":"How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models","url":"https://arxiv.org/pdf/2507.03120"},{"title":"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs","url":"https://arxiv.org/pdf/2604.01457"}]

Based on the search results, here are the key findings related to overconfidence and underconfidence in LLMs with separate mechanisms and internal representation decomposition:

## Dual Mechanisms in LLM Confidence

LLM confidence is governed by two competing mechanisms: a choice-supportive bias where LLMs exhibit inflated confidence and maintain their original responses when viewing their initial answers, even when presented with contrary evidence. LLMs markedly overweight inconsistent compared to consistent advice, and these two mechanisms – a drive to maintain consistency with prior commitments and hypersensitivity to contradictory feedback – capture LLM behavior.

## Mechanistic Decomposition of Assertiveness

High-assertive representations decompose into two orthogonal sub-components of emotional and logical clusters, paralleling the dual-route Elaboration Likelihood Model in Psychology. Steering vectors derived from these sub-components show distinct causal effects: emotional vectors broadly influence prediction accuracy, while logical vectors exert more localized effects.

## Internal Circuits for Overconfidence

Research has also identified specific internal mechanisms: A compact set of MLP blocks and attention heads, primarily in the middle-to-late layers, consistently write the confidence-inflation signal, with cross-dataset conservation indicating that verbalized overconfidence is driven by a stable model-internal mechanism.

These findings suggest that LLM confidence issues arise from distinct, separable internal mechanisms rather than a single monolithic behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd89565f-36b0-4b67-b097-4dca21e424cc",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "924ed250-8e5a-4817-bd87-3c72c7b1aa0d",
  "toolUseResult": {
    "query": "overconfidence underconfidence LLM separate mechanisms decompose internal representations 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018ZNt7UY8gpcFZrwNmaE7mU",
        "content": [
          {
            "title": "LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components",
            "url": "https://arxiv.org/pdf/2508.17182"
          },
          {
            "title": "LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components",
            "url": "https://arxiv.org/html/2508.17182"
          },
          {
            "title": "Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence",
            "url": "https://www.nature.com/articles/s42256-026-01217-9"
          },
          {
            "title": "(PDF) How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models",
            "url": "https://www.researchgate.net/publication/393476673_How_Overconfidence_in_Initial_Choices_and_Underconfidence_Under_Criticism_Modulate_Change_of_Mind_in_Large_Language_Models"
          },
          {
            "title": "Do Language Models Mirror Human Confidence? ...",
            "url": "https://aclanthology.org/2025.findings-acl.1316.pdf"
          },
          {
            "title": "Do Language Models Mirror Human Confidence? Exploring Psychological Insights to Address Overconfidence in LLMs",
            "url": "https://arxiv.org/pdf/2506.00582"
          },
          {
            "title": "How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models",
            "url": "https://arxiv.org/pdf/2507.03120"
          },
          {
            "title": "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs",
            "url": "https://arxiv.org/pdf/2604.01457"
          }
        ]
      },
      "Based on the search results, here are the key findings related to overconfidence and underconfidence in LLMs with separate mechanisms and internal representation decomposition:\n\n## Dual Mechanisms in LLM Confidence\n\nLLM confidence is governed by two competing mechanisms: a choice-supportive bias where LLMs exhibit inflated confidence and maintain their original responses when viewing their initial answers, even when presented with contrary evidence. LLMs markedly overweight inconsistent compared to consistent advice, and these two mechanisms – a drive to maintain consistency with prior commitments and hypersensitivity to contradictory feedback – capture LLM behavior.\n\n## Mechanistic Decomposition of Assertiveness\n\nHigh-assertive representations decompose into two orthogonal sub-components of emotional and logical clusters, paralleling the dual-route Elaboration Likelihood Model in Psychology. Steering vectors derived from these sub-components show distinct causal effects: emotional vectors broadly influence prediction accuracy, while logical vectors exert more localized effects.\n\n## Internal Circuits for Overconfidence\n\nResearch has also identified specific internal mechanisms: A compact set of MLP blocks and attention heads, primarily in the middle-to-late layers, consistently write the confidence-inflation signal, with cross-dataset conservation indicating that verbalized overconfidence is driven by a stable model-internal mechanism.\n\nThese findings suggest that LLM confidence issues arise from distinct, separable internal mechanisms rather than a single monolithic behavior."
    ],
    "durationSeconds": 6.346172100999975,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cd89565f-36b0-4b67-b097-4dca21e424cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 122 · 2026-05-19T13:21:09.047Z_

```json
{
  "parentUuid": "924ed250-8e5a-4817-bd87-3c72c7b1aa0d",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "875a0531-86f8-44d3-917e-cfebba7d793e",
  "timestamp": "2026-05-19T13:21:09.047Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 123 · 2026-05-19T13:21:11.421Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HQL2oHMQn3VvUZY718VEBV`</summary>

```json
{
  "query": "ICLR 2027 submission deadline October 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "875a0531-86f8-44d3-917e-cfebba7d793e",
  "isSidechain": false,
  "requestId": "req_011CbBzmtoMjuVhVLZrg7qZJ",
  "type": "assistant",
  "uuid": "b725dc40-efa5-4ee4-83e6-2ebd5817c889",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoiiV6bxNoZx4vVs1biroL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 55736,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 955,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 55736,
          "cache_creation_input_tokens": 955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 955
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

_source line 124 · 2026-05-19T13:21:15.794Z_

<details><summary>↩ Tool result · `toolu_01HQL2oHMQn3VvUZY718VEBV`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline October 2026"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"When is ICLR 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/iclr"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"}]

Based on the search results, I found information about ICLR conferences, but the search results primarily show information about ICLR 2026 rather than ICLR 2027.

The search results indicate that ICLR 2026 is scheduled for November 10-14, 2026, in Rio de Janeiro, Brazil, with an abstract deadline on March 25, 2026.

However, specific information about an ICLR 2027 submission deadline in October 2026 was not found in these results. One source notes that some 2026/2027 CFPs are not yet posted, which suggests that ICLR 2027 details may not yet be publicly available. I recommend checking the official ICLR website (iclr.cc) directly for the most current information about ICLR 2027 deadlines once they are announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b725dc40-efa5-4ee4-83e6-2ebd5817c889",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "04a0d9ee-41d0-431d-8896-653fddebab68",
  "toolUseResult": {
    "query": "ICLR 2027 submission deadline October 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A8iMgsA8vviusFEznN3P8z",
        "content": [
          {
            "title": "2026 Dates and Deadlines",
            "url": "https://iclr.cc/Conferences/2026/Dates"
          },
          {
            "title": "Year-Round Deadlines - Imranur Rahman",
            "url": "https://imranur-rahman.github.io/deadlines/"
          },
          {
            "title": "Key deadlines in AI and ML conferences | Yutori",
            "url": "https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "International Conference on Learning Representations ICLR in August 2027 in Sydney",
            "url": "https://waset.org/learning-representations-conference-in-august-2027-in-sydney"
          },
          {
            "title": "ICLR 2026",
            "url": "https://iclr.cc/"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "When is ICLR 2026? Dates, Deadline & Location | ConferenceDeadlines.com",
            "url": "https://www.conferencedeadlines.com/conference/iclr"
          },
          {
            "title": "ICLR 2026 Call for Papers",
            "url": "https://iclr.cc/Conferences/2026/CallForPapers"
          },
          {
            "title": "AI Deadlines – AI Conference Call For Paper Deadlines",
            "url": "http://aideadlines.org/"
          }
        ]
      },
      "Based on the search results, I found information about ICLR conferences, but the search results primarily show information about ICLR 2026 rather than ICLR 2027.\n\nThe search results indicate that ICLR 2026 is scheduled for November 10-14, 2026, in Rio de Janeiro, Brazil, with an abstract deadline on March 25, 2026.\n\nHowever, specific information about an ICLR 2027 submission deadline in October 2026 was not found in these results. One source notes that some 2026/2027 CFPs are not yet posted, which suggests that ICLR 2027 details may not yet be publicly available. I recommend checking the official ICLR website (iclr.cc) directly for the most current information about ICLR 2027 deadlines once they are announced."
    ],
    "durationSeconds": 4.370615378999966,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b725dc40-efa5-4ee4-83e6-2ebd5817c889",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-19T13:21:18.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EhZg6HJvg57CqtVAdXLbt2`</summary>

```json
{
  "query": "NeurIPS 2026 workshop deadline August 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04a0d9ee-41d0-431d-8896-653fddebab68",
  "isSidechain": false,
  "requestId": "req_011CbBznPfSMYVW9Z4HttNPQ",
  "type": "assistant",
  "uuid": "30239494-86ff-44b7-b461-758d0d012d23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015amxmnqsC5gj5yUQCYLCVY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 55736,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 55736,
          "cache_creation_input_tokens": 1645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1645
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

_source line 126 · 2026-05-19T13:21:22.393Z_

<details><summary>↩ Tool result · `toolu_01EhZg6HJvg57CqtVAdXLbt2`</summary>

```text
Web search results for query: "NeurIPS 2026 workshop deadline August 2026"

Links: [{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"Guidance for NeurIPS Workshop Proposals 2026","url":"https://neurips.cc/Conferences/2026/WorkshopsGuidance"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"2025 Dates and Deadlines - NeurIPS 2026","url":"https://neurips.cc/Conferences/2025/Dates"},{"title":"NeurIPS 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=neurips26"},{"title":"2026 Conference","url":"https://neurips.cc/"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"}]

Based on the search results, here's the information about NeurIPS 2026 workshop deadlines in August 2026:

The suggested submission date for workshop contributions is August 29, 2026, AoE (Anywhere on Earth). This is the date when workshop participants can submit their contributions (papers, talks, etc.) to the workshops.

It's worth noting that this is a *suggested* submission date rather than a hard deadline. The mandatory accept/reject notification date is September 29, 2026, AoE, which is when workshop organizers must notify all contributors of their acceptance status.

Other key workshop-related deadlines for NeurIPS 2026 include:
- Workshop Application Deadline: June 06, 2026, AoE (for organizers proposing workshops)
- Workshop Acceptance Notification: July 11, 2026, AoE (when organizers learn if their workshop proposals were accepted)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30239494-86ff-44b7-b461-758d0d012d23",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "f619d377-f4d8-476f-9b2a-724697bfa83c",
  "toolUseResult": {
    "query": "NeurIPS 2026 workshop deadline August 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SogVVo3L8kbK6cDN97K6Rq",
        "content": [
          {
            "title": "2026 Dates and Deadlines",
            "url": "https://neurips.cc/Conferences/2026/Dates"
          },
          {
            "title": "NeurIPS 2026 Call for Workshops",
            "url": "https://neurips.cc/Conferences/2026/CallForWorkshops"
          },
          {
            "title": "NeurIPS 2026 Call For Competitions",
            "url": "https://neurips.cc/Conferences/2026/CallForCompetitions"
          },
          {
            "title": "Guidance for NeurIPS Workshop Proposals 2026",
            "url": "https://neurips.cc/Conferences/2026/WorkshopsGuidance"
          },
          {
            "title": "Call for Papers 2026",
            "url": "https://neurips.cc/Conferences/2026/CallForPapers"
          },
          {
            "title": "2025 Dates and Deadlines - NeurIPS 2026",
            "url": "https://neurips.cc/Conferences/2025/Dates"
          },
          {
            "title": "NeurIPS 2026 - AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/conference/?id=neurips26"
          },
          {
            "title": "2026 Conference",
            "url": "https://neurips.cc/"
          },
          {
            "title": "2026 Conference – NeurIPS Blog",
            "url": "https://blog.neurips.cc/category/2026-conference/"
          }
        ]
      },
      "Based on the search results, here's the information about NeurIPS 2026 workshop deadlines in August 2026:\n\nThe suggested submission date for workshop contributions is August 29, 2026, AoE (Anywhere on Earth). This is the date when workshop participants can submit their contributions (papers, talks, etc.) to the workshops.\n\nIt's worth noting that this is a *suggested* submission date rather than a hard deadline. The mandatory accept/reject notification date is September 29, 2026, AoE, which is when workshop organizers must notify all contributors of their acceptance status.\n\nOther key workshop-related deadlines for NeurIPS 2026 include:\n- Workshop Application Deadline: June 06, 2026, AoE (for organizers proposing workshops)\n- Workshop Acceptance Notification: July 11, 2026, AoE (when organizers learn if their workshop proposals were accepted)"
    ],
    "durationSeconds": 4.326568168000027,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "30239494-86ff-44b7-b461-758d0d012d23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 127 · 2026-05-19T13:21:27.804Z_

Now let me do one final critical search — for very recent work combining steerability diagnostics with calibration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f619d377-f4d8-476f-9b2a-724697bfa83c",
  "isSidechain": false,
  "requestId": "req_011CbBznstp5SkZuQi2Rd1eN",
  "type": "assistant",
  "uuid": "1ae87e90-8134-4b07-a10c-90fe07fbb999",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdfWN7CPf2UAirPPreKyX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 57381,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 639,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 57381,
          "cache_creation_input_tokens": 639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 639
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

_source line 128 · 2026-05-19T13:21:29.036Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dbip5yVCwefKyLzcKP6Ct3`</summary>

```json
{
  "query": "steerability assessment pre-intervention diagnostic activation direction specificity entanglement 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ae87e90-8134-4b07-a10c-90fe07fbb999",
  "isSidechain": false,
  "requestId": "req_011CbBznstp5SkZuQi2Rd1eN",
  "type": "assistant",
  "uuid": "4ec9acc4-ca0f-484b-88b7-02e38b125718",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdfWN7CPf2UAirPPreKyX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 57381,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 639,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 57381,
          "cache_creation_input_tokens": 639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 639
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

_source line 129_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "4ec9acc4-ca0f-484b-88b7-02e38b125718",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 130_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Tool result

_source line 131 · 2026-05-19T13:21:38.639Z_

<details><summary>↩ Tool result · `toolu_01Dbip5yVCwefKyLzcKP6Ct3`</summary>

```text
Web search results for query: "steerability assessment pre-intervention diagnostic activation direction specificity entanglement 2026"

Links: [{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Understanding (Un)Reliability of Steering Vectors in ...","url":"https://arxiv.org/pdf/2505.22637"},{"title":"SteeringControl: Holistic Evaluation of Alignment Steering in LLMs","url":"https://arxiv.org/pdf/2509.13450"},{"title":"CBMAS: Cognitive Behavioral Modeling via Activation Steering","url":"https://arxiv.org/pdf/2601.06109"},{"title":"Steering Awareness: Models Can Be Trained to Detect Activation Steering","url":"https://arxiv.org/html/2511.21399v2"},{"title":"On the Non-Identifiability of Steering Vectors in Large Language Models","url":"https://arxiv.org/pdf/2602.06801"},{"title":"What Can We Actually Steer? A Multi-Behavior Study of Activation Control","url":"https://arxiv.org/html/2511.18284"}]

I found several relevant sources on activation steering and steerability assessment. Here's what the recent research shows:

## Key Findings on Steerability Assessment

**Directional Specificity and Activation Direction:**

The most steerable behaviors exhibit high directional agreement between individual activation differences and steering vectors, whereas least steerable directions are more dispersed or even orthogonal. Additionally, steerability is often asymmetric—models can be steered more easily in one direction than another for the same dimension.

**Behavioral Specificity and Entanglement:**

No method achieves clean, orthogonal control over target behaviors, and effective steering requires balancing directional strength and behavioral specificity. There is notable entanglement with social behaviors like sycophancy and anthropomorphism, and even between primary targets.

**Pre-Intervention Assessment:**

Recent work emphasizes the importance of pre-assessment. Not everything is steerable, and the literature buries this fact. Many behaviors turn out to be unsteerable, and some concepts are even "anti-steerable"—using the steering vector produces the reverse effect.

**Diagnostic Approaches:**

Non-identifiability is a robust geometric property that persists across diverse prompt distributions, revealing fundamental interpretability limits and highlighting the need for structural constraints beyond behavioral testing to enable reliable alignment interventions.

The research suggests that comprehensive pre-intervention diagnostics assessing directional alignment, behavioral specificity, and potential entanglement are crucial for effective activation steering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ec9acc4-ca0f-484b-88b7-02e38b125718",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "0dbac045-4250-416f-b6e7-0c9d00d75492",
  "toolUseResult": {
    "query": "steerability assessment pre-intervention diagnostic activation direction specificity entanglement 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U2k8xr22jgoXMKTXUDEhXi",
        "content": [
          {
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "Understanding (Un)Reliability of Steering Vectors in ...",
            "url": "https://arxiv.org/pdf/2505.22637"
          },
          {
            "title": "SteeringControl: Holistic Evaluation of Alignment Steering in LLMs",
            "url": "https://arxiv.org/pdf/2509.13450"
          },
          {
            "title": "CBMAS: Cognitive Behavioral Modeling via Activation Steering",
            "url": "https://arxiv.org/pdf/2601.06109"
          },
          {
            "title": "Steering Awareness: Models Can Be Trained to Detect Activation Steering",
            "url": "https://arxiv.org/html/2511.21399v2"
          },
          {
            "title": "On the Non-Identifiability of Steering Vectors in Large Language Models",
            "url": "https://arxiv.org/pdf/2602.06801"
          },
          {
            "title": "What Can We Actually Steer? A Multi-Behavior Study of Activation Control",
            "url": "https://arxiv.org/html/2511.18284"
          }
        ]
      },
      "I found several relevant sources on activation steering and steerability assessment. Here's what the recent research shows:\n\n## Key Findings on Steerability Assessment\n\n**Directional Specificity and Activation Direction:**\n\nThe most steerable behaviors exhibit high directional agreement between individual activation differences and steering vectors, whereas least steerable directions are more dispersed or even orthogonal. Additionally, steerability is often asymmetric—models can be steered more easily in one direction than another for the same dimension.\n\n**Behavioral Specificity and Entanglement:**\n\nNo method achieves clean, orthogonal control over target behaviors, and effective steering requires balancing directional strength and behavioral specificity. There is notable entanglement with social behaviors like sycophancy and anthropomorphism, and even between primary targets.\n\n**Pre-Intervention Assessment:**\n\nRecent work emphasizes the importance of pre-assessment. Not everything is steerable, and the literature buries this fact. Many behaviors turn out to be unsteerable, and some concepts are even \"anti-steerable\"—using the steering vector produces the reverse effect.\n\n**Diagnostic Approaches:**\n\nNon-identifiability is a robust geometric property that persists across diverse prompt distributions, revealing fundamental interpretability limits and highlighting the need for structural constraints beyond behavioral testing to enable reliable alignment interventions.\n\nThe research suggests that comprehensive pre-intervention diagnostics assessing directional alignment, behavioral specificity, and potential entanglement are crucial for effective activation steering."
    ],
    "durationSeconds": 9.599897773000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4ec9acc4-ca0f-484b-88b7-02e38b125718",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-19T13:21:42.165Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SKNwSpqDr3H94smY6pZAQs`</summary>

```json
{
  "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/",
  "prompt": "Extract the key points about activation steering in 2026. What are the main methods discussed? Is there any discussion of steerability assessment, specificity ratio, or diagnostics for when steering fails? Any mention of calibration? What is the state of the field according to this guide?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dbac045-4250-416f-b6e7-0c9d00d75492",
  "isSidechain": false,
  "requestId": "req_011CbBzp5LBHZybGAkndEzYD",
  "type": "assistant",
  "uuid": "179e0fbc-d814-40bb-a095-8a7951069853",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARWTAioNvW23MK2E1hFawF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 58020,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 760,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 150,
          "cache_read_input_tokens": 58020,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 760
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

_source line 133 · 2026-05-19T13:21:48.708Z_

<details><summary>↩ Tool result · `toolu_01SKNwSpqDr3H94smY6pZAQs`</summary>

```text
# Activation Steering in 2026: Key Insights

## Core Method

The guide outlines a four-step process: create contrast pairs representing desired vs. undesired behaviors, extract activations from both, compute mean differences as steering vectors, and apply these during inference by adding `alpha * steering_vector` to hidden states at selected layers.

## Steerability Assessment

The author provides critical clarity on what actually works versus fails:

**Reliably steerable:** refusal/compliance, sentiment/tone, conciseness, uncertainty expression

**Unreliably steerable:** instruction hierarchy, creativity, technical depth

**Effectively unsteerable:** factual accuracy, complex reasoning, specific fact injection

The author explains that steering cannot inject knowledge or fix reasoning: "you cannot steer a model into knowing things it doesn't know."

## Diagnostic Indicators

Several failure modes are documented:

- **Non-monotonic strength effects**: increasing alpha doesn't always increase intended effects
- **Prompt-dependent variance**: identical vectors produce different effects across inputs
- **Long-generation degradation**: steering effects fade after 300-500 tokens
- **Coherence trade-offs**: stronger vectors reduce output quality

## Calibration Issues

The guide addresses calibration shifts: steering can "actually shift the distribution of token probabilities" rather than just changing surface behavior. One critical concern noted is that "overrefusal steering maintains general abilities and _looks_ reliable in standard evals, but consistently fails under adversarial conditions."

## Field State

The 2026 landscape emphasizes conditional application (CAST), sparse steering via SAEs, and context-aware vector fields over simple mean-difference approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "179e0fbc-d814-40bb-a095-8a7951069853",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "a4e1d8c7-938d-4cb4-923a-3b0d1aef896e",
  "toolUseResult": {
    "bytes": 80503,
    "code": 200,
    "codeText": "OK",
    "result": "# Activation Steering in 2026: Key Insights\n\n## Core Method\n\nThe guide outlines a four-step process: create contrast pairs representing desired vs. undesired behaviors, extract activations from both, compute mean differences as steering vectors, and apply these during inference by adding `alpha * steering_vector` to hidden states at selected layers.\n\n## Steerability Assessment\n\nThe author provides critical clarity on what actually works versus fails:\n\n**Reliably steerable:** refusal/compliance, sentiment/tone, conciseness, uncertainty expression\n\n**Unreliably steerable:** instruction hierarchy, creativity, technical depth\n\n**Effectively unsteerable:** factual accuracy, complex reasoning, specific fact injection\n\nThe author explains that steering cannot inject knowledge or fix reasoning: \"you cannot steer a model into knowing things it doesn't know.\"\n\n## Diagnostic Indicators\n\nSeveral failure modes are documented:\n\n- **Non-monotonic strength effects**: increasing alpha doesn't always increase intended effects\n- **Prompt-dependent variance**: identical vectors produce different effects across inputs\n- **Long-generation degradation**: steering effects fade after 300-500 tokens\n- **Coherence trade-offs**: stronger vectors reduce output quality\n\n## Calibration Issues\n\nThe guide addresses calibration shifts: steering can \"actually shift the distribution of token probabilities\" rather than just changing surface behavior. One critical concern noted is that \"overrefusal steering maintains general abilities and _looks_ reliable in standard evals, but consistently fails under adversarial conditions.\"\n\n## Field State\n\nThe 2026 landscape emphasizes conditional application (CAST), sparse steering via SAEs, and context-aware vector fields over simple mean-difference approaches.",
    "durationMs": 6541,
    "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
  },
  "sourceToolAssistantUUID": "179e0fbc-d814-40bb-a095-8a7951069853",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-19T13:21:51.534Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CtbZGyq3Wc1pHbXCtuHdx8`</summary>

```json
{
  "query": "\"Guiding Giants\" lightweight controllers weighted activation steering arXiv 2505.20309 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4e1d8c7-938d-4cb4-923a-3b0d1aef896e",
  "isSidechain": false,
  "requestId": "req_011CbBzppM3qi2RL9o2vGQNY",
  "type": "assistant",
  "uuid": "9c066e37-d48a-49d5-b4e7-d01ee490e6a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MF7LhH4zRoApauFc3WzWhA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 58780,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 524,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 58780,
          "cache_creation_input_tokens": 524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 524
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

_source line 135 · 2026-05-19T13:21:57.538Z_

<details><summary>↩ Tool result · `toolu_01CtbZGyq3Wc1pHbXCtuHdx8`</summary>

```text
Web search results for query: ""Guiding Giants" lightweight controllers weighted activation steering arXiv 2505.20309 2026"

Links: [{"title":"[2505.20309] Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs","url":"https://arxiv.org/abs/2505.20309"},{"title":"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs","url":"https://arxiv.org/pdf/2505.20309"},{"title":"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs","url":"https://arxiv.org/html/2505.20309"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=10425&show=500"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=4325&show=50"},{"title":"Computation and Language May 2025","url":"https://arxiv.org/list/cs.CL/2025-05?skip=1475&show=250"},{"title":"The Anatomy of Alignment: Decomposing Preference Optimization by Steering Sparse Features","url":"https://arxiv.org/html/2509.12934v1"},{"title":"MASteer: Multi-Agent Adaptive Steer Strategy for End-to-End LLM Trustworthiness Repair","url":"https://arxiv.org/html/2508.06963v1"}]

I found the paper you're looking for. Here's what I found:

**"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs"** (arXiv:2505.20309)

The paper addresses controlling undesirable Large Language Model behaviors like unsafe content generation by introducing a lightweight, trainable controller network integrated during inference, which observes specific intermediate LLM activations and predicts both a global scaling factor and layer-specific weights.

The predicted global scaling factor and layer-specific weights dynamically modulate the intensity of a steering patch derived from a pre-computed "refusal direction" vector, applied across the LLM's layers during generation.

Trained on activations from both harmful and benign prompts, the controller learns to discriminatively apply nuanced, layer-aware interventions, activating steering primarily for harmful inputs.

**Authors:** Amr Hegazy, Mostafa Elhoushi, and Amr Alanwar

**Latest version:** The paper has been revised, with version 3 dating to March 15, 2026 (as of your search date).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c066e37-d48a-49d5-b4e7-d01ee490e6a3",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "fa30571f-9294-4359-9dbf-d20ad85a1e45",
  "toolUseResult": {
    "query": "\"Guiding Giants\" lightweight controllers weighted activation steering arXiv 2505.20309 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M7iqyJbdwMpDk4B15UtNdE",
        "content": [
          {
            "title": "[2505.20309] Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs",
            "url": "https://arxiv.org/abs/2505.20309"
          },
          {
            "title": "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs",
            "url": "https://arxiv.org/pdf/2505.20309"
          },
          {
            "title": "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs",
            "url": "https://arxiv.org/html/2505.20309"
          },
          {
            "title": "Computer Science May 2025",
            "url": "https://www.arxiv.org/list/cs/2025-05?skip=10425&show=500"
          },
          {
            "title": "Machine Learning May 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-05?skip=4325&show=50"
          },
          {
            "title": "Computation and Language May 2025",
            "url": "https://arxiv.org/list/cs.CL/2025-05?skip=1475&show=250"
          },
          {
            "title": "The Anatomy of Alignment: Decomposing Preference Optimization by Steering Sparse Features",
            "url": "https://arxiv.org/html/2509.12934v1"
          },
          {
            "title": "MASteer: Multi-Agent Adaptive Steer Strategy for End-to-End LLM Trustworthiness Repair",
            "url": "https://arxiv.org/html/2508.06963v1"
          }
        ]
      },
      "I found the paper you're looking for. Here's what I found:\n\n**\"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs\"** (arXiv:2505.20309)\n\nThe paper addresses controlling undesirable Large Language Model behaviors like unsafe content generation by introducing a lightweight, trainable controller network integrated during inference, which observes specific intermediate LLM activations and predicts both a global scaling factor and layer-specific weights.\n\nThe predicted global scaling factor and layer-specific weights dynamically modulate the intensity of a steering patch derived from a pre-computed \"refusal direction\" vector, applied across the LLM's layers during generation.\n\nTrained on activations from both harmful and benign prompts, the controller learns to discriminatively apply nuanced, layer-aware interventions, activating steering primarily for harmful inputs.\n\n**Authors:** Amr Hegazy, Mostafa Elhoushi, and Amr Alanwar\n\n**Latest version:** The paper has been revised, with version 3 dating to March 15, 2026 (as of your search date)."
    ],
    "durationSeconds": 6.000827939999988,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9c066e37-d48a-49d5-b4e7-d01ee490e6a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 136 · 2026-05-19T13:23:10.272Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize all my findings and form a comprehensive review.

## Summary of Verification

### References Verified:
1. ✅ Kumaran et al. (Nature MI 2026, arXiv 2507.03120) — Confirmed. Identifies CSB and CEO as competing biases in LLM confidence.
2. ✅ Miao & Ungar (arXiv 2603.25052) — Confirmed. Linear but orthogonal encoding of calibration/confidence in residual stream.


3. ✅ Liu (arXiv 2605.05715) — Confirmed. Classification-correction gap with specificity ratio ≤0.152, non-linear MLP improvements of +2.8pp.
4. ✅ Spherical Steering (arXiv 2602.08169, ICML 2026) — Confirmed.
5. ✅ COAST (arXiv 2605.01167) — Confirmed.
6. ✅ Selective Steering (arXiv 2601.19375) — Confirmed.
7. ✅ Confidence Manifold (arXiv 2602.08159) — Confirmed.
8. ✅ Tsujimura & Tagade (arXiv 2508.17182) — Confirmed. Working with 3-8 dimensional spaces achieving 0.90 AUC and 10.9pp steering effect through emotional and logical decomposition of assertiveness.
9. ✅ Wired for Overconfidence (arXiv 2604.01457) — Confirmed.
10. ✅ CORAL (arXiv 2602.06022) — Confirmed. Same group as Miao & Ungar.
11. ✅ Gemma 4 31B Dense — Confirmed. Released April 2026.
12. ✅ Qwen3-8B — Confirmed. Available.
13. ✅ AAAI 2027 deadline verified.
14. ✅ ARR August 2026 confirmed for EACL 2027.
15. ✅ NeurIPS 2026 Workshops around late August.
16. ⚠️ ICLR 2027 not yet announced, but October 2026 seems reasonable based on ICLR 2026's March deadline.

Now I'm noticing a critical gap — MERA from ICML 2025 implements selective, adaptive steering with abstention, optimizing both intervention direction and when/how much to steer, which is a significant competitor I should have caught earlier.

K-Steering from EMNLP 2025 uses nonlinear classifiers for dynamic multi-attribute control, and Curveball Steering demonstrates that linear approaches fail under geometric distortion, both relevant to my linear versus nonlinear routing discussion. FLAS is a very recent flow-based method that learns concept representations, which I should examine more closely. The combination of cognitive-bias grounding, the specificity ratio for routing decisions, and the four-route hierarchy is genuinely novel—no existing work combines all three, though papers like MERA, K-Steering, FairSteer, and Curveball each tackle subsets of these ideas. The main risk is bridging from behavioral observations to mechanistic explanations, which remains the hardest part to validate.

The separability test in Phase 1A has clear success criteria, but Phase 1B's specificity ratio requires defining what counts as the correct versus incorrect subspace, adding methodological complexity. Training nonlinear MLPs across five models, four datasets, and multiple layers is computationally expensive—the 750-1050 H100 hours estimate seems reasonable but tight. The timeline to AAAI 2027 is extremely aggressive with only about ten weeks until the deadline, and whether the behavioral-to-mechanistic leap actually holds in activation space remains entirely uncertain.

If Phase 1 succeeds and CSB and CEO prove both separable and steerable in different ways, that's a genuinely important contribution. But if it fails, the paper becomes a negative result on bias separability with significantly reduced impact. The four-route adaptive system feels over-engineered—if only one or two routes end up being necessary in practice, much of that complexity becomes wasted effort.

The proposal is impressively detailed and well-structured, but it's gotten quite dense with all the routes, model variants, and fallback mechanisms. The core idea—that competing biases need different correction strategies—is clear, but the execution is intricate. There's also a critical gap: MERA from ICML 2025 does selective steering with abstention and adaptive strength modulation, which directly overlaps with the routing concepts here, and that citation is missing.

Beyond MERA, I'm also not seeing Curveball Steering cited, which is directly relevant to the linear versus nonlinear distinction that drives the routing logic. FLAS and ODESteer are recent alternatives to linear steering that should be in the landscape discussion too. The experimental scope itself—four routes, five models, four datasets, multiple baselines—is ambitious enough that there's real risk of spreading effort too thin and not executing any single component thoroughly. And realistically, with only ten weeks until AAAI 2027 and a sixteen to twenty week timeline, hitting that deadline seems infeasible even with aggressive Phase 1 execution. Most pressingly, the core assumption that CSB and CEO are separable and steerable differently hasn't actually been tested yet, and that's the foundation everything else rests on.

The asymmetric steerability hypothesis is intriguing but also somewhat unfalsifiable—if both biases show similar specificity, the result is just null for that hypothesis, so the paper needs contingency framing for that outcome. And the specificity ratio thresholds Liu's work extrapolates to (≥0.5 for HIGH, 0.2-0.5 for MEDIUM, <0.2 for LOW) are essentially constructed from single data points—there's no empirical basis for where calibration biases would actually fall on this spectrum, which the proposal should acknowledge more directly.

On novelty, the combination itself is novel, but each component borrows from existing work: contrastive probing from prior research, specificity metrics from Liu, spherical steering from You et al., and non-linear approaches from Liu again. The adaptive routing between these methods is where the real novelty lies, though adjacent work like FairSteer and K-Steering already covers significant ground. Feasibility is the bigger concern—the whole thing hinges on an untested assumption about separability, the system has many interdependent parts, and the AAAI 2027 timeline is unrealistic. The Phase 1 validation is solid but will likely take longer than projected. The proposal is exceptionally detailed and well-organized, though it's becoming dense enough that clarity starts to suffer.

If Phase 1 pans out, the specificity ratio measurements could be a real contribution, and the adaptive routing framework is genuinely interesting. But everything depends on whether the core empirical findings hold up. Averaging the scores puts this at 3.5, below the 4.0 threshold.

I'm reconsidering since this is round 3 of 10—I have room to request revisions. The main gaps are a missing MERA citation, recent nonlinear steering work like Curveball and ODESteer that isn't cited, and the timeline for AAAI 2027 is just too compressed.

Let me re-examine the novelty score. The combination of bias-specific diagnosis, steerability assessment, and adaptive routing actually is novel—no existing paper tackles all three together. MERA handles abstention but not bias decomposition, K-Steering does multi-attribute work but misses calibration and routing logic, FairSteer detects-then-steers but lacks the steerability diagnostic. That's genuinely 3.5 territory. On feasibility, the jump from behavioral to mechanistic understanding is risky, but the Phase 1 validation is thorough and the resource estimates are solid. The complexity is high but workable.

The timeline issue is solvable by shifting the primary target, so I'm settling on 3 for feasibility. The writing is clear and well-organized with good revision responsiveness—that's a 4. Impact hinges on whether the empirical findings pan out, but if they do, the steerability profiling across competing biases would be genuinely valuable—3.5 seems right. That puts me at 3.5 overall, so revise is the call.

The main gaps I need to flag: MERA from ICML 2025 on selective steering with abstention is missing, several recent nonlinear steering methods like Curveball, FLAS, and ODESteer aren't covered, the AAAI timeline is unrealistic, and the specificity ratio thresholds need stronger justification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa30571f-9294-4359-9dbf-d20ad85a1e45",
  "isSidechain": false,
  "requestId": "req_011CbBzqUC88CSqAwHWiqpSJ",
  "type": "assistant",
  "uuid": "ef604ec4-dda2-48fa-8e2f-02516cc241cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBHaUQjV6uLFpUxHuQG1sK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 59304,
      "output_tokens": 3056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3056,
          "cache_read_input_tokens": 59304,
          "cache_creation_input_tokens": 736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 736
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

_source line 137 · 2026-05-19T13:23:10.278Z_

Now let me do a final check on whether the core contribution (joint separability + steerability assessment) has been scooped.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef604ec4-dda2-48fa-8e2f-02516cc241cc",
  "isSidechain": false,
  "requestId": "req_011CbBzqUC88CSqAwHWiqpSJ",
  "type": "assistant",
  "uuid": "01fd46fa-9e72-42c4-8043-a37c92e18390",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBHaUQjV6uLFpUxHuQG1sK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 59304,
      "output_tokens": 3056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3056,
          "cache_read_input_tokens": 59304,
          "cache_creation_input_tokens": 736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 736
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

_source line 138 · 2026-05-19T13:23:10.281Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CW2ZUCnFEqtMSwKtgpuSYe`</summary>

```json
{
  "query": "\"specificity ratio\" steering vector bias direction decodable steerable diagnostic LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01fd46fa-9e72-42c4-8043-a37c92e18390",
  "isSidechain": false,
  "requestId": "req_011CbBzqUC88CSqAwHWiqpSJ",
  "type": "assistant",
  "uuid": "c7341d20-e840-4865-bd85-33a7219072a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBHaUQjV6uLFpUxHuQG1sK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 59304,
      "output_tokens": 3056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3056,
          "cache_read_input_tokens": 59304,
          "cache_creation_input_tokens": 736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 736
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

_source line 139_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "c7341d20-e840-4865-bd85-33a7219072a3",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 140_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Tool result

_source line 141 · 2026-05-19T13:23:20.365Z_

<details><summary>↩ Tool result · `toolu_01CW2ZUCnFEqtMSwKtgpuSYe`</summary>

```text
Web search results for query: ""specificity ratio" steering vector bias direction decodable steerable diagnostic LLM 2026"

Links: [{"title":"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/html/2605.05715"},{"title":"[2605.05715] Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/abs/2605.05715"},{"title":"Understanding (Un)Reliability of Steering Vectors in Language Models","url":"https://arxiv.org/html/2505.22637v1"},{"title":"SteeringControl: Holistic Evaluation of Alignment Steering in LLMs","url":"https://arxiv.org/html/2509.13450v1"},{"title":"Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs","url":"https://arxiv.org/pdf/2503.05371"},{"title":"Steering Vectors: Beamforming to LLM Control","url":"https://www.emergentmind.com/topics/steering-vectors"},{"title":"Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs","url":"https://arxiv.org/html/2503.05371v2"}]

Based on the search results, I found highly relevant information about specificity ratio in the context of steering vectors and LLM diagnosis. Here are the key findings:

## Specificity Ratio in LLM Steering and Decodability

The specificity ratio is a measure of how much a decodable direction overlaps with task-critical computation, with lower values indicating greater entanglement. One study found the Overthinking direction had 85-88% overlap with task-critical computation (specificity ratio <= 0.152).

In one case, the OT-specific specificity ratio was only 0.119, indicating that 88% of the signal is shared with task-relevant directions.

## Key Finding: The Decodability-Steerability Gap

The research demonstrates an important diagnostic discovery: while Overthinking failure modes are linearly decodable at 71.6% balanced accuracy, fixed linear steering yields nearly zero effect across five families of steering approaches and different architectures.

## Implications for Diagnostic Use

The specificity ratio serves as a diagnostic tool to understand why steering may fail even when signals are decodable. The low specificity ratio, combined with evidence that non-targeted shared-direction steering damages accuracy and that LEACE concept erasure damages accuracy, suggests representational entanglement where failure signals are intertwined with task-critical computation.

This research indicates that the specificity ratio is crucial for distinguishing between signals that are merely decodable versus those that can actually be used for steering interventions in LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7341d20-e840-4865-bd85-33a7219072a3",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "debb691d-bb38-4d33-b327-d8a075962d69",
  "toolUseResult": {
    "query": "\"specificity ratio\" steering vector bias direction decodable steerable diagnostic LLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GXpShvPFnM8kp2b2ubfM4W",
        "content": [
          {
            "title": "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/html/2605.05715"
          },
          {
            "title": "[2605.05715] Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/abs/2605.05715"
          },
          {
            "title": "Understanding (Un)Reliability of Steering Vectors in Language Models",
            "url": "https://arxiv.org/html/2505.22637v1"
          },
          {
            "title": "SteeringControl: Holistic Evaluation of Alignment Steering in LLMs",
            "url": "https://arxiv.org/html/2509.13450v1"
          },
          {
            "title": "Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs",
            "url": "https://arxiv.org/pdf/2503.05371"
          },
          {
            "title": "Steering Vectors: Beamforming to LLM Control",
            "url": "https://www.emergentmind.com/topics/steering-vectors"
          },
          {
            "title": "Shifting Perspectives: Steering Vectors for Robust Bias Mitigation in LLMs",
            "url": "https://arxiv.org/html/2503.05371v2"
          }
        ]
      },
      "Based on the search results, I found highly relevant information about specificity ratio in the context of steering vectors and LLM diagnosis. Here are the key findings:\n\n## Specificity Ratio in LLM Steering and Decodability\n\nThe specificity ratio is a measure of how much a decodable direction overlaps with task-critical computation, with lower values indicating greater entanglement. One study found the Overthinking direction had 85-88% overlap with task-critical computation (specificity ratio <= 0.152).\n\nIn one case, the OT-specific specificity ratio was only 0.119, indicating that 88% of the signal is shared with task-relevant directions.\n\n## Key Finding: The Decodability-Steerability Gap\n\nThe research demonstrates an important diagnostic discovery: while Overthinking failure modes are linearly decodable at 71.6% balanced accuracy, fixed linear steering yields nearly zero effect across five families of steering approaches and different architectures.\n\n## Implications for Diagnostic Use\n\nThe specificity ratio serves as a diagnostic tool to understand why steering may fail even when signals are decodable. The low specificity ratio, combined with evidence that non-targeted shared-direction steering damages accuracy and that LEACE concept erasure damages accuracy, suggests representational entanglement where failure signals are intertwined with task-critical computation.\n\nThis research indicates that the specificity ratio is crucial for distinguishing between signals that are merely decodable versus those that can actually be used for steering interventions in LLMs."
    ],
    "durationSeconds": 10.073120401000022,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c7341d20-e840-4865-bd85-33a7219072a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-19T13:23:23.310Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NWfBQLRMmUmdcDGQhDodbd`</summary>

```json
{
  "query": "\"To Steer or Not to Steer\" MERA mechanistic error reduction abstention adaptive strength ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "debb691d-bb38-4d33-b327-d8a075962d69",
  "isSidechain": false,
  "requestId": "req_011CbBzwahxJUvhqBeHwBJt8",
  "type": "assistant",
  "uuid": "174915ba-d31f-48ec-8476-6d7b2d26c73e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6H3ysjzMQAXYhvs4NiLET",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3765,
      "cache_read_input_tokens": 60040,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 60040,
          "cache_creation_input_tokens": 3765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3765
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

_source line 143 · 2026-05-19T13:23:30.124Z_

<details><summary>↩ Tool result · `toolu_01NWfBQLRMmUmdcDGQhDodbd`</summary>

```text
Web search results for query: ""To Steer or Not to Steer" MERA mechanistic error reduction abstention adaptive strength ICML 2025"

Links: [{"title":"To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models | OpenReview","url":"https://openreview.net/forum?id=fUCPq5RvmH"},{"title":"ICML Poster To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models","url":"https://icml.cc/virtual/2025/poster/44524"},{"title":"To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models","url":"https://proceedings.mlr.press/v267/hedstrom25a.html"},{"title":"[2510.13290] To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models","url":"https://arxiv.org/abs/2510.13290"},{"title":"(PDF) To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models","url":"https://www.researchgate.net/publication/396517741_To_Steer_or_Not_to_Steer_Mechanistic_Error_Reduction_with_Abstention_for_Language_Models"},{"title":"To Steer or Not to Steer? Mechanistic Error Reduction with ...","url":"https://arxiv.org/pdf/2510.13290"}]

I found the paper! Here's what the search revealed:

"To Steer or Not to Steer?" introduces Mechanistic Error Reduction with Abstention (MERA), a principled framework for steering language models (LMs) to mitigate errors through selective, adaptive interventions.

Unlike existing methods that rely on fixed, manually tuned steering strengths, often resulting in under or oversteering, MERA addresses these limitations by optimizing the intervention direction and calibrating when and how much to steer, thereby provably improving performance or abstaining when no confident correction is possible.

The method uses a lightweight helper model to estimate how likely the LM is to be wrong, then gently shifts the model's internal activity to reduce the probability of an error being made. If the input is already predicted to be correct, then MERA does nothing.

Experiments across diverse datasets and LM families demonstrate safe, effective, non-degrading error correction and that MERA outperforms existing baselines. Moreover, MERA can be applied on top of existing steering techniques to further enhance their performance, establishing it as a general-purpose and efficient approach to mechanistic activation steering.

The paper was published in the Proceedings of the 42nd International Conference on Machine Learning (ICML 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "174915ba-d31f-48ec-8476-6d7b2d26c73e",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "21a84661-0b36-4655-b722-03708a05b242",
  "toolUseResult": {
    "query": "\"To Steer or Not to Steer\" MERA mechanistic error reduction abstention adaptive strength ICML 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Phb7B7BGCvQjP1MmHWTn5Y",
        "content": [
          {
            "title": "To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=fUCPq5RvmH"
          },
          {
            "title": "ICML Poster To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models",
            "url": "https://icml.cc/virtual/2025/poster/44524"
          },
          {
            "title": "To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models",
            "url": "https://proceedings.mlr.press/v267/hedstrom25a.html"
          },
          {
            "title": "[2510.13290] To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models",
            "url": "https://arxiv.org/abs/2510.13290"
          },
          {
            "title": "(PDF) To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models",
            "url": "https://www.researchgate.net/publication/396517741_To_Steer_or_Not_to_Steer_Mechanistic_Error_Reduction_with_Abstention_for_Language_Models"
          },
          {
            "title": "To Steer or Not to Steer? Mechanistic Error Reduction with ...",
            "url": "https://arxiv.org/pdf/2510.13290"
          }
        ]
      },
      "I found the paper! Here's what the search revealed:\n\n\"To Steer or Not to Steer?\" introduces Mechanistic Error Reduction with Abstention (MERA), a principled framework for steering language models (LMs) to mitigate errors through selective, adaptive interventions.\n\nUnlike existing methods that rely on fixed, manually tuned steering strengths, often resulting in under or oversteering, MERA addresses these limitations by optimizing the intervention direction and calibrating when and how much to steer, thereby provably improving performance or abstaining when no confident correction is possible.\n\nThe method uses a lightweight helper model to estimate how likely the LM is to be wrong, then gently shifts the model's internal activity to reduce the probability of an error being made. If the input is already predicted to be correct, then MERA does nothing.\n\nExperiments across diverse datasets and LM families demonstrate safe, effective, non-degrading error correction and that MERA outperforms existing baselines. Moreover, MERA can be applied on top of existing steering techniques to further enhance their performance, establishing it as a general-purpose and efficient approach to mechanistic activation steering.\n\nThe paper was published in the Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)."
    ],
    "durationSeconds": 6.810385156999924,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "174915ba-d31f-48ec-8476-6d7b2d26c73e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 144 · 2026-05-19T13:23:33.159Z_

Now I have comprehensive evidence to write my review. Let me compile my findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21a84661-0b36-4655-b722-03708a05b242",
  "isSidechain": false,
  "requestId": "req_011CbBzxHyALhMEMwMLL7b9h",
  "type": "assistant",
  "uuid": "db34ad74-cf72-4964-95fa-e9fe38a71f92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RVoLi1Z2fohz6K7YxZbhp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 63805,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 772,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 63805,
          "cache_creation_input_tokens": 772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 772
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

_source line 145 · 2026-05-19T13:23:33.914Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S219zwa71RwZHAkrQjTmrP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.09313",
  "prompt": "Extract the full abstract and key results. Does Curveball Steering route between linear and nonlinear methods adaptively? What models and tasks were evaluated?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db34ad74-cf72-4964-95fa-e9fe38a71f92",
  "isSidechain": false,
  "requestId": "req_011CbBzxHyALhMEMwMLL7b9h",
  "type": "assistant",
  "uuid": "7e772128-d16e-4b82-a2f4-43e1d691cbb1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RVoLi1Z2fohz6K7YxZbhp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 63805,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 772,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 63805,
          "cache_creation_input_tokens": 772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 772
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

_source line 146 · 2026-05-19T13:23:37.888Z_

<details><summary>↩ Tool result · `toolu_01S219zwa71RwZHAkrQjTmrP`</summary>

```text
# Curveball Steering Paper Summary

## Full Abstract

The paper addresses limitations in activation steering for large language models. The researchers challenge the Linear Representation Hypothesis by analyzing geometric properties of LLM activation spaces. They measure distortion using geodesic-to-Euclidean distance ratios and find "substantial and concept-dependent distortions, indicating that activation spaces are not well-approximated by a globally linear geometry." They propose Curveball steering, which uses polynomial kernel PCA for nonlinear interventions that respect learned activation geometry, and report that it "consistently outperforms linear PCA-based steering" especially in high-distortion regimes.

## Adaptive Routing Question

The content provided does **not indicate** that Curveball Steering adaptively routes between linear and nonlinear methods. Rather, it presents Curveball as a unified nonlinear alternative that performs better than linear approaches.

## Models and Tasks

The webpage abstract does not specify which models or tasks were evaluated. You would need to access the full PDF or HTML version to find experimental details about the specific LLMs tested and downstream tasks used.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e772128-d16e-4b82-a2f4-43e1d691cbb1",
  "isSidechain": false,
  "promptId": "5926c660-05a6-42a7-bbdd-05f3e62ebfe5",
  "type": "user",
  "uuid": "af40ee23-9519-4796-8318-62ac3d565211",
  "toolUseResult": {
    "bytes": 46902,
    "code": 200,
    "codeText": "OK",
    "result": "# Curveball Steering Paper Summary\n\n## Full Abstract\n\nThe paper addresses limitations in activation steering for large language models. The researchers challenge the Linear Representation Hypothesis by analyzing geometric properties of LLM activation spaces. They measure distortion using geodesic-to-Euclidean distance ratios and find \"substantial and concept-dependent distortions, indicating that activation spaces are not well-approximated by a globally linear geometry.\" They propose Curveball steering, which uses polynomial kernel PCA for nonlinear interventions that respect learned activation geometry, and report that it \"consistently outperforms linear PCA-based steering\" especially in high-distortion regimes.\n\n## Adaptive Routing Question\n\nThe content provided does **not indicate** that Curveball Steering adaptively routes between linear and nonlinear methods. Rather, it presents Curveball as a unified nonlinear alternative that performs better than linear approaches.\n\n## Models and Tasks\n\nThe webpage abstract does not specify which models or tasks were evaluated. You would need to access the full PDF or HTML version to find experimental details about the specific LLMs tested and downstream tasks used.",
    "durationMs": 3971,
    "url": "https://arxiv.org/abs/2603.09313"
  },
  "sourceToolAssistantUUID": "7e772128-d16e-4b82-a2f4-43e1d691cbb1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 147 · 2026-05-19T13:23:37.890Z_

```json
{
  "parentUuid": "af40ee23-9519-4796-8318-62ac3d565211",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "54089487-23d3-4ca1-ae4f-23df2a0f9d60",
  "timestamp": "2026-05-19T13:23:37.890Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 148 · 2026-05-19T13:24:22.007Z_

I now have comprehensive evidence to compile my final review. Let me synthesize all findings.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "The combination of cognitive-bias-grounded decomposition + steerability diagnostics + adaptive multi-route intervention is novel in its specific formulation, but the individual components are heavily borrowed (specificity ratio from Liu, Spherical Steering from You et al., non-linear MLP from Liu, abstention from Liu/MERA). Critical missing work: MERA (ICML 2025) already implements selective steering + abstention + adaptive strength; K-Steering (EMNLP Findings 2025) does multi-attribute nonlinear steering via gradient-based routing; FairSteer (ACL Findings 2025) detects bias → routes to intervention; Curveball Steering (2603.09313) provides geometry-aware nonlinear steering; FLAS (2605.05892) learns concept-conditioned velocity fields; ODESteer (ICLR 2026) does ODE-based multi-step adaptive steering. The novelty space is significantly more crowded than the landscape section suggests."},
    "feasibility": {"score": 3, "rationale": "The core assumption (CSB/CEO separability in activations) remains entirely untested after 3 rounds. Phase 1 validation is well-designed with clear success/failure criteria, but the system's complexity (4 routes × 5 models × 4 datasets × extensive ablations × per-direction diagnostics) is enormous. The AAAI 2027 primary target (July 28 deadline = ~10 weeks) is unrealistic given the 16-20 week manual timeline. Specificity ratio thresholds (≥0.5 HIGH, 0.2-0.5 MEDIUM, <0.2 LOW) are extrapolated from exactly two data points in Liu's paper (0.152 for overthinking, ~1.0 for refusal) — this is thin justification for a routing architecture."},
    "clarity": {"score": 4, "rationale": "Extremely thorough and well-organized. Revision history shows excellent responsiveness. The four-route architecture is clearly described with quantitative thresholds. However, the proposal is approaching over-engineering — the sheer volume of fallbacks, routes, baselines, and ablations risks burying the core contribution under methodological complexity."},
    "impact": {"score": 3, "rationale": "Phase 1 results (separability + steerability profiles for competing calibration biases) would be a genuine contribution regardless of Phase 2-3 outcomes, as the proposal correctly notes. However, impact is conditional: if CSB/CEO are not separable (entirely possible), the paper becomes a negative result with limited scope. The adaptive routing contribution depends on finding asymmetric steerability profiles — otherwise, a uniform intervention suffices. The crowded steering landscape (8+ new methods in 2026 alone) means the framework risks being outdated by the time it's published."}
  },
  "issues": [
    "MISSING CRITICAL BASELINE: MERA ('To Steer or Not to Steer?', Hedström et al., ICML 2025, arXiv 2510.13290) implements selective steering with adaptive strength and abstention — directly overlapping with Routes C and D. MERA optimizes intervention direction AND calibrates when/how much to steer, with provable non-degradation guarantees. It can be applied ON TOP of existing steering methods. This must be cited as a baseline and distinguished from: DBS-v2 decomposes biases while MERA treats errors monolithically; DBS-v2 routes between intervention types while MERA modulates a single intervention's strength.",
    "MISSING NONLINEAR STEERING COMPETITORS: The landscape fails to cite (a) Curveball Steering (arXiv 2603.09313, March 2026) — polynomial kernel PCA-based nonlinear steering that explicitly addresses geometric distortion in activation spaces, directly relevant to the linear vs. nonlinear routing rationale; (b) FLAS (arXiv 2605.05892, May 2026) — flow-based activation steering learning concept-conditioned velocity fields, first method to outperform prompting on AxBench; (c) ODESteer (arXiv 2602.17560, ICLR 2026) — ODE-based multi-step adaptive steering with barrier functions. These represent the rapidly maturing nonlinear steering landscape that Route B must be positioned against.",
    "AAAI 2027 PRIMARY TARGET IS INFEASIBLE: The full paper deadline is July 28, 2026 — approximately 10 weeks from now. The manual timeline estimate is 16-20 weeks. Even the auto_research timeline (6-10 weeks) is at the edge, and auto_research is the most expensive mode. No honest accounting of Phase 1A→1B sequential dependency, model access setup time, or writing time supports AAAI 2027 as 'primary target.' ARR August 2026 (Aug 3) is similarly tight. Realistic primary target should be ICLR 2027 or NeurIPS 2026 workshop for Phase 1 results.",
    "SPECIFICITY RATIO THRESHOLDS ARE WEAKLY JUSTIFIED: The proposed routing thresholds (≥0.5 HIGH, 0.2-0.5 MEDIUM, <0.2 LOW) are interpolated from exactly two empirical data points in Liu (2605.05715): overthinking at ≤0.152 (LOW, linear steering fails) and refusal at ~0.999 (HIGH, linear steering succeeds). There is no empirical or theoretical basis for the 0.2 and 0.5 boundaries. These thresholds should be explicitly framed as initial hypotheses to be refined during Phase 1B rather than as calibrated routing criteria.",
    "OVERCOMPLEXITY RISK: The proposal includes 4 intervention routes, 5 models (3 primary + 2 supplementary), 4 datasets, 10+ baselines, Phase 1A with 5 separability tests, Phase 1B with 4 steerability diagnostics, 2 alternative norm-preserving methods to ablate, and COAST-informed loss weighting. This is an enormous experimental matrix that risks under-execution. Consider scoping to 2-3 models and 2 routes (linear + nonlinear with abstention) for the primary paper, with the full matrix as supplementary."
  ],
  "feedback": "The revision from round 2 is strong — the integration of Liu (2605.05715) and the decodable-steerable distinction is thorough and genuine. Three concrete fixes for round 4: (1) Cite MERA (ICML 2025) as a key baseline — it's the closest existing work on selective steering + abstention, and failing to cite a published ICML paper implementing core components of your Route C/D would be a serious oversight for reviewers. Distinguish DBS-v2 by emphasizing the multi-bias decomposition and steerability-based routing that MERA lacks. (2) Add Curveball Steering, FLAS, and ODESteer to the landscape — these are the 2026 nonlinear steering methods your Route B competes against. Position Route B's bottleneck MLP as motivated by Liu's calibration-specific finding, while acknowledging these general-purpose alternatives. (3) Revise venue targeting: drop AAAI 2027 as primary (the math doesn't work). Make ICLR 2027 (~Oct 2026) the primary target, NeurIPS 2026 workshop (Aug 29) for Phase 1 results, and ARR cycle for full paper backup. (4) Explicitly frame specificity ratio thresholds as hypotheses, not established boundaries. (5) Consider streamlining the experimental matrix — 5 models × 4 routes × 10+ baselines may impress but also signals unfocused ambition to reviewers.",
  "reason": "Sound core idea with genuine novelty in bias-specific steerability diagnostics, but missing critical baseline (MERA, ICML 2025), several 2026 nonlinear steering competitors, and has an infeasible primary venue timeline."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54089487-23d3-4ca1-ae4f-23df2a0f9d60",
  "isSidechain": false,
  "requestId": "req_011CbBzxs9wbi7Af8o6KEWvX",
  "type": "assistant",
  "uuid": "7ee89fe9-de87-4007-9a07-8e86ee855a36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BEEYeCDNH32s4KuC18oSTk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 486,
      "cache_read_input_tokens": 64577,
      "output_tokens": 1962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 486,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1962,
          "cache_read_input_tokens": 64577,
          "cache_creation_input_tokens": 486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 486
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

_source line 149_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "7ee89fe9-de87-4007-9a07-8e86ee855a36",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---

### Runtime record

_source line 150_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML idea: Disentangling calibration biases via geometry-aware steering",
  "sessionId": "b373d757-44ed-4e47-bf31-3bb789326a9d"
}
```

---
