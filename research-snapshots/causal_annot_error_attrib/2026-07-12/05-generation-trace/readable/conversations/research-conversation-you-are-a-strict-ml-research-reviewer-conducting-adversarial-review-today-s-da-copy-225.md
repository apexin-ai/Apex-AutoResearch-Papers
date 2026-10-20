# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-19 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7.jsonl`
- **Structured JSON:** [`e0a63c97e8f6e00e968f.json`](../../sessions/e0/e0a63c97e8f6e00e968f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T16:37:20.020Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T16:37:20.020Z",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-19 (UTC).**\n\nYour job: independently verify this idea's claims via web_search, then issue a verdict.\n\n## User requirements\nThe user asked for: **calibration**\nEvaluate whether this idea actually meets the user's requirements. An idea that doesn't match should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：用 WebFetch 实际阅读相关论文的 abstract 和关键章节。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献\n\n6. **评分诚实**：\n   - 4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} 2026` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} 2026` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} 2026 site:scholar.google.com`\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} 2026` — 按活跃作者追踪\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} 2026` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey 2026` — 找综述论文\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n\n### 搜索维度\n\n1. **正向搜索**：直接搜索主题相关论文\n2. **竞争论文搜索**（最关键！）：有没有人在解决同样的问题？用类似方法？\n3. **相邻领域搜索**：其他领域是否已解决类似问题\n4. **反面搜索**：找到反对你 idea 的证据\n5. **引用链追踪**：找到核心论文后，查看 cited-by 发现 concurrent work\n\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n2. **知名团队追踪**：搜索相关团队最近的论文\n3. **会议最新录用**：搜索 `site:openreview.net {topic} 2026`\n4. **arXiv 近 3 个月密集搜索**\n\n## Review checklist\n1. **SOTA freshness**: Are baselines actually current SOTA?\n2. **Reference verification**: Do cited papers actually exist?\n3. **Gap validity**: Does the claimed gap still exist?\n4. **Venue validity**: Are target venue deadlines after 2026-05-19?\n5. **Feasibility**: Is the resource estimate realistic?\n6. **Novelty**: Is this sufficiently different from existing work?\n7. **Cost realism**: Are the three mode estimates internally consistent?\n\n## Idea under review (round 9/10)\n{\n  \"title\": \"Competing Biases, Asymmetric Steerability: Decomposing LLM Miscalibration for Targeted Activation Correction\",\n  \"core_problem\": \"LLM miscalibration arises from at least two competing biases — choice-supportive bias (CSB, inflating confidence in initial answers) and contradictory-evidence overweighting (CEO, causing excessive confidence revision under criticism) — that are simultaneously active and pull confidence in opposite directions on the same instances (Kumaran et al., Nature MI 2026). This creates a bias interference problem: competing biases can partially cancel (producing illusory calibration where global metrics look good but localized failures persist) or one can dominate instance-by-instance (producing heterogeneous over/under-confidence patterns). Kobalczyk & van der Schaar (2605.13484) independently confirmed that global reliability diagrams 'hide rather than reveal calibration failures' because 'opposing errors cancel when aggregated by confidence' — with worst-calibrated slices containing on average 41% of test instances across 48 model-dataset pairs — but provide no mechanistic explanation for WHY opposing errors exist. Five lines of related work address parts of this problem but not the whole: (1) CogBias (Huang et al., 2604.01366) demonstrates family-dependent bias mitigation — but addresses independently-active biases, not simultaneously competing ones. (2) Billa (2604.15557) proposes a three-regime steerability framework with LAP diagnostic (ρ=0.86–0.91) — but operates per-concept with synthetic binary features. (3) MERA (Hedström et al., ICML 2025) provides adaptive steering with non-degradation guarantees — but treats errors monolithically. (4) SteerConf (Zhou et al., NeurIPS 2025) achieves 29% AUROC increase via prompt-level confidence steering — but operates without mechanistic decomposition. (5) 'Sycophancy Is Not One Thing' (Vennemeyer et al., 2509.21305) demonstrates that complex behaviors decompose into independently steerable sub-components — but their sub-components are co-aligned, not opposing. The classification-correction gap (Liu, 2605.05715; Patel et al., 2604.19974) adds a further obstacle: linearly decodable directions may not be linearly steerable. A critical open question — central to practical impact — is whether the interference subpopulation (instances where both biases partially cancel) is large enough to justify decomposed correction over monolithic approaches, or whether the contribution is primarily mechanistic. Can we characterize competing biases at the activation level, measure their asymmetric steerability profiles, quantify interference prevalence, and demonstrate that decomposed correction outperforms monolithic methods on the interference subpopulation?\",\n  \"opportunity\": \"Kumaran et al. (Nature Machine Intelligence, 2026; arXiv 2507.03120) established behavioral evidence that LLM miscalibration results from two mechanistically distinct biases: CSB inflates confidence in selected answers (+0.21 confidence boost, p<0.001), while CEO causes models to over-react to opposing evidence (overweighting ratio 2.58 for opposing vs. 1.095 for supporting advice). Critically, in the dual-active condition (Answer Shown + Opposite Advice), both biases are simultaneously active — CSB partially suppresses CEO-driven behavior (change-of-mind drops from 85.0% to 39.2%), and the Over/Underconfidence Score drops from +0.210 to +0.086, providing condition-level evidence of partial cancellation. However, Kumaran et al. provided only behavioral evidence with no activation-level analysis, and their study covered Gemma 3 (12B/27B), GPT-4o, o1-preview, and DeepSeek R1 7B — but not the Llama or Qwen families widely used for mechanistic interpretability.\\n\\nKumaran, Conmy et al. ('How do LLMs Compute Verbal Confidence,' arXiv 2603.17839, March 2026) provided the mechanistic foundation: verbal confidence is cached at the Post-Answer-Newline (PANL) token position, with information flowing answer tokens → PANL (layers 22–28) → Confidence-Colon position (layers 30–36) in Gemma 3 27B. Token log-probabilities explain only 8.4% of variance (R²_CV = 0.084), while PANL-cached representations explain substantial additional variance. This directly validates our token-position-specific extraction strategy. However, these layer ranges are architecture-specific — verified only on Gemma 3 27B and Qwen 2.5 7B. Cross-architecture evidence suggests the qualitative strategy (caching at answer-adjacent positions) transfers broadly: behavioral axes align tightly across Llama-Qwen-Mistral-Phi architectures with mean binary AUROC of 0.95 (arXiv 2605.09875), and task-schema representations transfer at 100% via late MLP patching across 9 models from 7 Transformer families (arXiv 2512.17325). Nevertheless, architecture-specific layer ranges require verification for each target model — motivating our Phase 0A confidence pathway verification step.\\n\\nCogBias (Huang et al., arXiv 2604.01366) demonstrated that cognitive biases are encoded as linearly separable directions and that bias-family-specific intervention is both viable and necessary: activation steering achieves 26–32% bias reduction overall, with effectiveness varying dramatically by family. CogBias establishes that different biases need different interventions — but addresses independently-active biases on different task types, not simultaneously competing biases.\\n\\n'Sycophancy Is Not One Thing' (Vennemeyer et al., arXiv 2509.21305) provides the closest methodological precedent: using difference-in-means and activation additions across 5 models, they decomposed sycophancy into independently steerable sub-components. The critical distinction: their sub-components are co-aligned (various forms of user-pleasing output), whereas CSB and CEO are opposing biases creating destructive interference — a strictly harder decomposition problem.\\n\\nBilla (arXiv 2604.15557) established the routing-by-steerability paradigm: LAP predicts steering effectiveness at ρ=0.86–0.91 across 24 concept families. SteerConf (Zhou et al., NeurIPS 2025) achieves 29% AUROC increase and 16% ECE reduction via prompt-level confidence steering — the strongest training-free behavioral baseline. CCPS (Khanmohammadi et al., arXiv 2505.21772, EMNLP 2025) achieves ~55% ECE reduction via perturbation-stability probing on Llama/Qwen/Mistral 8B–32B — a strong representation-based baseline, though monolithic.\\n\\nMiao & Ungar (arXiv 2603.25052) showed calibration and verbalized confidence are orthogonal in the residual stream (cosine <0.04), achieving 4–7× ECE improvement via adaptive steering. Liu (arXiv 2605.05715) demonstrated the classification-correction gap: decodable failure directions yield Δ≈0 under linear steering (specificity ratio ≤0.152), but a nonlinear bottleneck MLP achieves Δ=+2.8pp. Patel et al. (arXiv 2604.19974) independently confirmed via SAE analysis that 'pure incorrectness features' are functionally inert despite being decodable — reinforcing that separability does NOT guarantee steerability. Kobalczyk & van der Schaar (arXiv 2605.13484) discovered hidden miscalibration regimes across 48 model-dataset pairs where opposing errors cancel when aggregated, with worst-calibrated slices averaging 41% of test instances — but no per-instance interference prevalence estimate exists.\\n\\nThe convergence of (a) behavioral evidence of competing biases with quantitative effect sizes and condition-level cancellation evidence, (b) mechanistic understanding of confidence computation pathways with cross-architecture transferability support, (c) established decompose-then-steer and routing-by-steerability paradigms, (d) the decodable–steerable distinction, and (e) hidden miscalibration regimes suggesting substantial subpopulations affected by opposing errors creates an opportunity for the next step: extending from independently-active and co-aligned biases to simultaneously competing and opposing calibration biases.\",\n  \"landscape\": \"Kumaran et al. (Nature MI, 2026) identified competing biases (CSB and CEO) via behavioral experiments on Gemma 3 12B/27B, GPT-4o, o1-preview, and DeepSeek R1 7B but proposed no correction framework and provided no activation-level evidence. Effect magnitudes varied substantially across models, and no Llama or Qwen models were tested. Kumaran, Conmy et al. (arXiv 2603.17839) subsequently showed that verbal confidence is cached at the PANL token position with information flowing answer tokens → PANL (layers 22–28) → CC (layers 30–36) in Gemma 3 27B, and verified on Qwen 2.5 7B. However, these architecture-specific layer ranges have not been validated on Llama models or on the newer Gemma 4 and Qwen3 generations — the qualitative strategy (answer-adjacent caching) has cross-architecture support (behavioral axes align at AUROC 0.95 across Llama-Qwen-Mistral-Phi, arXiv 2605.09875; task schemas transfer at 100% across 7 families, arXiv 2512.17325), but specific layer ranges are architecture-dependent and require per-model verification.\\n\\nCogBias (Huang et al., arXiv 2604.01366) organizes cognitive biases into four families, demonstrates linear separability, and shows family-dependent mitigation (26–32% steering reduction, with prompt debiasing backfiring for Judgment biases). CogBias establishes two principles: (a) biases are linearly encoded and separable, and (b) different families require different interventions. However, CogBias addresses independently-active biases on different task types — not simultaneously competing biases on the same instances.\\n\\n'Sycophancy Is Not One Thing' (Vennemeyer et al., arXiv 2509.21305) is the closest methodological precedent: across 5 models, they decomposed sycophancy into independently steerable sub-components via difference-in-means. Key distinction: their sub-components (sycophantic agreement, praise, genuine agreement) are co-aligned, while our target biases (CSB, CEO) are opposing — creating destructive interference that makes individual directions harder to isolate via difference-in-means.\\n\\nBilla (arXiv 2604.15557) proposes three steerability regimes with LAP diagnostic (ρ=0.86–0.91 across 24 concept families on 5 models). Key distinctions: Billa operates per-concept with synthetic binary features, not per-instance with naturalistic competing biases; LAP's correlation weakens on smaller models (ρ=0.50–0.52 on Pythia-2.8B); and its applicability to non-binary calibration constructs is untested.\\n\\nSteerConf (Zhou et al., NeurIPS 2025) achieves 29% AUROC increase and 16% ECE reduction via prompt-level confidence steering on GPT-3.5, LLaMA 3, and GPT-4 — the strongest training-free baseline. CCPS (Khanmohammadi et al., EMNLP 2025) achieves ~55% ECE reduction and 21% Brier score reduction via perturbation-stability probing on Llama/Qwen/Mistral 8B–32B — a strong representation-based baseline. Both are monolithic (no bias decomposition).\\n\\nLiu (arXiv 2605.05715) demonstrated the classification-correction gap: failure directions (71.6% balanced accuracy) yield Δ≈0 across 29 linear steering configurations (specificity ratio ≤0.152), but a bottleneck MLP achieves Δ=+2.8pp. Patel et al. (arXiv 2604.19974) confirmed via SAE analysis on Llama-3.1-8B and Gemma-2-9B that 'pure incorrectness features' are functionally inert while confounded features yield 1.1% accuracy improvement — both studied single failure modes, not decomposed competing biases.\\n\\nKobalczyk & van der Schaar (arXiv 2605.13484) discovered hidden miscalibration regimes across 48 model-dataset pairs where opposing errors cancel when aggregated, with worst-calibrated slices containing on average 41% of test instances in the 18 most-affected pairs. This provides independent evidence for bias interference but no mechanistic explanation, no bias decomposition, and — critically — no per-instance prevalence estimate for competing-bias interference. Whether the 41% figure reflects CSB-CEO cancellation or other sources of heterogeneous miscalibration is an open question our Phase 2 interference prevalence estimation addresses.\\n\\nMERA (Hedström et al., ICML 2025) provides adaptive steering with non-degradation guarantees via constrained optimization — but with a single monolithic probe. The nonlinear steering landscape (ODESteer, ICLR 2026; Curveball Steering, 2026; FLAS, 2026) provides powerful alternatives when linear steering fails. Spherical Steering (ICML 2026) preserves activation norms via geodesic rotation, and COAST (2605.01167) minimizes collateral damage.\\n\\nNo existing method addresses simultaneously competing calibration biases with per-instance diagnosis and bias-specific correction: CogBias decomposes independently-active families; 'Sycophancy Is Not One Thing' decomposes co-aligned sub-components; MERA adapts monolithically; Kobalczyk identifies hidden regimes without decomposition. Our work uniquely targets opposing biases that create interference, requiring joint decomposition, steerability assessment, and interference prevalence quantification.\",\n  \"inspired_by\": \"Gap: Competing biases create interference — partially canceling on some instances (Kumaran et al.'s OUCS dropping from +0.210 to +0.086 in the dual-active condition; Kobalczyk's 41% worst-calibrated slices) and producing heterogeneous patterns on others — that no existing method decomposes or quantifies at the per-instance level. Pattern: CogBias proves family-specific intervention works → 'Sycophancy Is Not One Thing' proves complex behaviors decompose into steerable sub-components → Billa proves steerability-based routing works (LAP, ρ=0.86–0.91) → SteerConf proves calibration is steerable → Liu + Patel et al. prove decodable ≠ steerable → Kumaran & Conmy map confidence computation pathways (PANL caching) → cross-architecture evidence (2605.09875) supports pathway transferability. Untried combination: Extend these principles from independent/co-aligned biases to simultaneously competing and opposing calibration biases, with interference prevalence quantification as a novel empirical core. Key hypothesis: CSB and CEO have asymmetric steerability profiles because they involve different cognitive processes (self-evaluation vs. evidence integration), and the interference subpopulation is substantial enough (>30%, given Kobalczyk's 41% worst-slice finding) to justify decomposed correction.\",\n  \"approach\": \"We investigate whether competing calibration biases (CSB and CEO) are distinguishable in activation space, exhibit asymmetric steerability, and can be corrected through bias-specific intervention that outperforms monolithic approaches — with interference prevalence quantification as a central empirical question determining the paper's practical impact framing. Evaluated on 3 models × 3 datasets with 7 core baselines.\\n\\n**Phase 0A — Behavioral Replication & Confidence Pathway Verification (Week 1):**\\n\\nWe replicate Kumaran et al.'s 2×3 factorial design on each target model (Llama-3.1-8B-Instruct, Qwen3-8B, Gemma 4 31B Dense) with 500 questions per condition at 70% stated advice accuracy. We measure CSB magnitude (confidence difference between Answer Shown-Neutral and Answer Hidden-Neutral) and CEO magnitude (overweighting ratio for opposing vs. supporting advice).\\n\\nGo/no-go: If a model shows CSB ≥+0.105 AND CEO overweighting ratio ≥1.29 (≥50% of Kumaran's reported effects), it proceeds. Models showing one bias are retained for single-bias characterization. Models showing neither are replaced (candidates: Gemma 3 27B, Mistral-8B).\\n\\n**Confidence Pathway Verification (end of Week 1, ~1 day per model):** Before committing to PANL-based extraction in Phase 0B, we verify that each target model caches confidence information at answer-adjacent positions. For each model: (a) train linear probes at the PANL position across all layers to identify where confidence-predictive information peaks, adapting Kumaran & Conmy's layer-sweep methodology; (b) perform attribution patching (Nanda et al., arXiv 2310.10348) — a gradient-based approximation of activation patching testing all candidate positions in a single backward pass — to confirm PANL activations causally influence confidence output; (c) apply LogitLens4LLMs (arXiv 2503.11667) to identify where confidence-relevant logits crystallize layer-by-layer. If a model caches confidence at a different structural position (e.g., last answer token rather than PANL), we adjust extraction positions for that model — the matched-content confound controls in Phase 0B remain valid regardless of extraction position. This uses the Phase 0A stimulus set (already generated), requiring only additional forward/backward passes (~4-8 GPU-hours per model). We report verified extraction positions and layer ranges for each model as part of contribution (5).\\n\\n**Phase 0B — Confound-Controlled De-Risking Pilot (Weeks 2–4):**\\n\\nWe allocate 3 weeks for Phase 0B to accommodate the expanded factorial design: stimulus generation with token-length matching and semantic neutrality validation (~1 week, the primary bottleneck as no published contrastive activation extraction study has attempted this level of confound control); activation extraction at verified positions across ~4000 pairs (~3-4 days); confound diagnostic battery and statistical analysis (~1 week); and iteration buffer if initial diagnostics partially fail (~3-4 days).\\n\\nThe translation from behavioral paradigm to contrastive activation extraction faces a critical confound: contrastive pairs differ not only in bias activation but in prompt information content. We address this with a four-pronged mitigation strategy:\\n\\n*(1) Matched-content contrastive pairs:*\\n- **CSB pairs:** CSB-active: 'You previously answered [X].' CSB-control: plausible alternative answer of matched token length attributed to 'another LLM.' Additional 'scrambled-answer' control with token-length-matched neutral text.\\n- **CEO pairs:** CEO-active: contradictory advice. CEO-control: irrelevant neutral advice of matched token length. Additional supporting-advice condition for directional validation.\\n\\n*(2) Same-content-different-attribution CSB control:* The model's OWN answer text attributed to 'another LLM,' creating a 2×2 factorial: {own text, other text} × {self-attributed, other-attributed}. The self-own vs. other-own contrast isolates pure ownership/attribution effects (the CSB core mechanism) while holding content exactly constant.\\n\\n*(3) Token-position-specific extraction:* Extraction at the positions verified in Phase 0A (PANL, CC, and first confidence token), targeting where bias-relevant confidence signals mechanistically concentrate rather than averaging across all positions.\\n\\n*(4) Confound diagnostic tests:* (a) Correlation with prompt token count <0.1; (b) prompt-structure probe cosine similarity <0.2 to candidate bias directions; (c) generalization to held-out question types; (d) CSB direction aligns more with attribution contrast than content contrast.\\n\\nPilot conducted on the strongest Phase 0A model with ~500 pairs per bias type per control condition (~4000 total across the full factorial).\\n\\nGo/no-go: Linear probe ≥60% balanced accuracy on matched-content pairs AND confound diagnostics pass → proceed. Accuracy 60%+ with partial diagnostic failure → expand extraction positions, apply mean-centering. Accuracy 55–60% with clean diagnostics → expand to 1000 pairs. Accuracy <55% or consistent diagnostic failure → activate behavioral-signal fallback (correlational rather than causal evidence, repositioning paper for EMNLP/NAACL).\\n\\n**Phase 1 — Separability Validation & Steerability Assessment (Weeks 5–9):**\\n\\n*Phase 1A — Separability (Weeks 5–7):* Scale confound-controlled extraction to all passing models with 2000+ matched-content pairs per bias type per model, extracting at verified positions. Validate separability via: (a) cosine similarity between directions (<0.3), (b) principal angle analysis, (c) PCA dimensionality, (d) cross-prediction ablations, (e) confound diagnostic replication at scale. Caveat (Patel et al., 2604.19974): separability does NOT guarantee functional relevance — Phase 1B is essential.\\n\\n*Phase 1B — Steerability Diagnostics (Weeks 7–9):* For each direction: (a) specificity ratio (Liu 2605.05715); (b) adapted LAP (Billa 2604.15557) along the verified PANL→CC pathway; (c) LEACE concept erasure; (d) pilot Spherical Steering test; (e) functional inertness test (Patel et al. methodology). Routing thresholds learned via validation-set sweeps. The core empirical hypothesis — CSB and CEO have asymmetric steerability profiles — would explain inconsistent monolithic steering results and hidden miscalibration regimes.\\n\\n**Phase 2 — Per-Instance Bias Diagnosis & Interference Prevalence Estimation (Weeks 8–11):**\\n\\nA lightweight logistic probe trained on per-instance projection magnitudes classifies which bias dominates per query. We stratify by difficulty and validate against behavioral predictions (CSB dominates on easy questions; CEO dominates under criticism on hard questions).\\n\\n**Interference Prevalence Estimation (new):** This analysis is central to the paper's practical impact framing. For each instance, we compute projection magnitudes onto CSB (p_CSB) and CEO (p_CEO) directions, then classify into four categories: (a) **CSB-dominant** — p_CSB above median, p_CEO below; (b) **CEO-dominant** — p_CEO above median, p_CSB below; (c) **Interference** — both above median with opposing confidence effects (biases partially cancel, producing deceptively low net error); (d) **Low-bias** — both below median. For interference instances, we estimate the 'cancellation magnitude' — how much gross miscalibration is hidden by opposing bias cancellation.\\n\\nBehavioral evidence suggests substantial interference prevalence: Kumaran et al.'s dual-active condition shows OUCS dropping from +0.210 to +0.086 (partial cancellation at condition level), and Kobalczyk & van der Schaar's worst-calibrated slices average 41% of instances in affected pairs. However, no per-instance prevalence estimate exists — making this analysis both necessary and itself a contribution.\\n\\nWe adopt conditional framing based on measured prevalence: (a) **>30% interference** → decomposed correction addresses a substantial practical subpopulation; emphasize calibration improvement as primary contribution alongside mechanistic characterization; (b) **15–30%** → moderate practical improvement; emphasize mechanistic characterization as primary with calibration gains as secondary; (c) **<15%** → paper's contribution is primarily mechanistic/interpretive (understanding WHY hidden miscalibration regimes exist), with practical gains limited to the interference subpopulation. Expected improvement on interference instances: decomposed correction should recover ~2×min(|p_CSB|, |p_CEO|) in gross miscalibration that monolithic methods conflate.\\n\\n**Phase 3 — Bias-Specific Intervention (Weeks 10–16):**\\n\\nBuilding on Billa's routing-by-steerability paradigm extended to per-instance competing biases, informed by 'Sycophancy Is Not One Thing's demonstration that decomposed sub-components can be independently steered:\\n\\n*Route A — Adaptive Spherical Steering (steerable directions):* Spherical Steering (You et al., ICML 2026) with MERA-inspired per-direction adaptive strength. Layer selection informed by adapted LAP profiles and the verified PANL→CC pathway.\\n\\n*Route B — Learned Nonlinear Residual Correction (entangled directions):* Bottleneck residual MLP per bias type (<0.1% parameters), with COAST-informed collateral-damage-aware training.\\n\\n*Route C — Selective Abstention (uncorrectable instances):* MERA's Hoeffding-based statistical framework when neither route improves calibration without >3% accuracy damage.\\n\\nPhase 3 results are interpreted conditional on Phase 2 interference prevalence: aggregate metrics (ECE, Brier) will reflect improvement proportional to interference prevalence × per-instance correction magnitude. We report both aggregate and interference-subpopulation-stratified metrics to disambiguate mechanistic success from practical impact.\\n\\n**Generalizability:** The Phase 0→3 pipeline is reusable for other competing-bias pairs: sycophantic agreement vs. truthfulness commitment (opposing training objectives), primacy vs. recency bias (opposing positional effects shifting with context usage, arXiv 2508.07479), and anchoring vs. evidence updating in multi-turn reasoning. We discuss these as future work.\\n\\n**Fallback Path:** If Phase 0B fails despite matched-content controls and attribution factorial, the behavioral-signal-guided fallback produces correlational rather than causal evidence — still informative but repositioned for EMNLP/NAACL rather than ICLR.\\n\\nWe evaluate on TriviaQA, MMLU, and PopQA across Gemma 4 31B Dense, Qwen3-8B, and Llama-3.1-8B-Instruct (subject to Phase 0A replication). Metrics: ECE, Brier score, AUROC, difficulty-stratified ECE, per-direction specificity and LAP profiles, interference prevalence and cancellation magnitude, collateral damage, route distribution. Core baselines: (1) temperature scaling, (2) CORAL, (3) Miao & Ungar adaptive steering, (4) MERA monolithic, (5) monolithic Spherical Steering, (6) monolithic nonlinear MLP, (7) SteerConf prompt-level steering. Extended baselines in supplementary: CogBias-style family-level steering, CCPS perturbation-stability probing.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"675-925 H100\",\n      \"timeline\": \"17-21 weeks (includes 1-week behavioral replication with pathway verification + 3-week pilot with expanded factorial)\",\n      \"estimated_gpu_cost\": \"$1,688-$2,313 (H100 @ ~$2.50/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"575-775 H100\",\n      \"timeline\": \"13-17 weeks (includes 1-week behavioral replication with pathway verification + 3-week pilot with expanded factorial)\",\n      \"claude_api_cost\": \"$400-$600 (Sonnet 4.6 for matched-content and attribution-factorial contrastive dataset generation, confound diagnostics, probing, LAP computation, adapter training, analysis)\",\n      \"estimated_gpu_cost\": \"$1,438-$1,938\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"875-1175 H100\",\n      \"timeline\": \"8-12 weeks (includes behavioral replication with pathway verification + pilot)\",\n      \"claude_api_cost\": \"$750-$1,275 (Opus 4.7 for experiment orchestration, matched-content and attribution-factorial pair generation, confound analysis, validation analysis, steerability diagnostics, adapter training sweeps)\",\n      \"estimated_gpu_cost\": \"$2,188-$2,938\",\n      \"speed_bottleneck\": \"Phase 0A behavioral replication + pathway verification (1 week, parallelizable across 3 models) → Phase 0B pilot is sequential gate (3 weeks, expanded for attribution factorial + confound diagnostics). Phase 1A→1B is sequential. Evaluation across 3 models × 3 datasets × 3 routes + 7 baselines is parallelizable.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (estimated deadline ~Sep 24, 2026 — primary target, ~18 weeks from start date of May 19; human-in-loop timeline of 13-17 weeks requires aggressive parallel writing of introduction, related work, and methodology starting at Phase 1 (week 5). At 13-week execution: ~5 weeks for results writing — comfortable. At 17-week execution: ~1 week for final results integration — very tight, feasible only with substantial sections pre-written. Honest assessment: feasible at the shorter timeline bound with disciplined parallel writing; risky at the upper bound.)\",\n    \"NeurIPS 2026 Workshops (~Aug 29, 2026 — Phase 0 + Phase 1 results as standalone contribution on competing bias geometry with confound-controlled methodology and interference prevalence estimation)\",\n    \"ARR October 2026 cycle (Oct 12, 2026 — backup full paper targeting NAACL 2027 or EACL 2027; comfortable timeline)\",\n    \"EMNLP 2027 (if Phase 0 fallback activated — correlational contribution repositioned for empirical venue)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Competing Biases underlie Overconfidence and Underconfidence in LLMs (Kumaran et al., Nature Machine Intelligence 2026; arXiv 2507.03120)\",\n    \"How do LLMs Compute Verbal Confidence (Kumaran, Conmy et al., arXiv 2603.17839, March 2026) — confidence cached at PANL position, answer→PANL→CC information flow, token log-probs explain only 8.4% of variance\",\n    \"CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models (Huang et al., arXiv 2604.01366, April 2026) — linearly separable bias directions, family-dependent mitigation, 26-32% steering reduction\",\n    \"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs (Vennemeyer et al., arXiv 2509.21305, submitted ICLR 2026) — decomposition of sycophancy into independently steerable sub-components via difference-in-means\",\n    \"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders (Patel et al., arXiv 2604.19974, April 2026) — pure incorrectness features functionally inert, SAE-based classification-correction gap confirmation\",\n    \"Calibrating LLM Confidence by Probing Perturbed Representation Stability (Khanmohammadi et al., arXiv 2505.21772, EMNLP 2025) — CCPS, ~55% ECE reduction via perturbation-stability probing on Llama/Qwen/Mistral 8B-32B\",\n    \"Predicting Where Steering Vectors Succeed (Billa, arXiv 2604.15557, April 2026) — three-regime steerability framework, LAP diagnostic, routing-by-steerability paradigm\",\n    \"SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., arXiv 2503.02863, NeurIPS 2025) — prompt-level confidence steering, 29% AUROC increase, 16% ECE reduction\",\n    \"Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, arXiv 2603.25052, 2026) — orthogonal calibration/confidence encoding, adaptive steering\",\n    \"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes (Liu, arXiv 2605.05715, May 2026) — classification-correction gap, specificity ratio diagnostic\",\n    \"To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models (Hedström et al., ICML 2025; arXiv 2510.13290) — MERA: adaptive strength, provable non-degradation, selective abstention\",\n    \"Discovery of Hidden Miscalibration Regimes (Kobalczyk & van der Schaar, arXiv 2605.13484, May 2026) — input-dependent calibration heterogeneity, opposing errors cancel when aggregated, worst-calibrated slices average 41% of instances\",\n    \"Cross-Family Universality of Behavioral Axes in Language Models (arXiv 2605.09875, May 2026) — behavioral axes align at AUROC 0.95 across Llama-Qwen-Mistral-Phi, transferable directions from 2 source models\",\n    \"Task Schema and Binding: A Double Dissociation Across Transformer Families (arXiv 2512.17325, 2025) — task schemas transfer at 100% via late MLP patching across 9 models from 7 families\",\n    \"LogitLens4LLMs: Extending Logit Lens to Modern Architectures (arXiv 2503.11667, 2025) — practical tool for layer-by-layer confidence crystallization analysis\",\n    \"Attribution Patching: Activation Patching At Industrial Scale (Nanda et al., arXiv 2310.10348, 2023) — gradient-based approximation of activation patching for efficient causal verification\",\n    \"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (Chen et al., ICLR 2026; arXiv 2602.17560)\",\n    \"Curveball Steering: The Right Direction To Steer Isn't Always Linear (Raval et al., arXiv 2603.09313, Mar 2026)\",\n    \"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (arXiv 2605.05892, May 2026) — FLAS\",\n    \"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs (arXiv 2604.01457, 2026)\",\n    \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., ICML 2026; arXiv 2602.08169)\",\n    \"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection (Dang & Ngo, arXiv 2601.19375, Jan 2026)\",\n    \"Minimizing Collateral Damage in Activation Steering (Nguyen et al., arXiv 2605.01167, May 2026) — COAST framework\",\n    \"Where to Steer: Input-Dependent Layer Selection for Steering Improves LLM Alignment (Gadgil et al., arXiv 2604.03867, April 2026)\",\n    \"Steered LLM Activations are Non-Surjective (Mishra et al., arXiv 2604.09839, 2026)\",\n    \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models (arXiv 2602.08159, 2026)\",\n    \"LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components (Tsujimura & Tagade, arXiv 2508.17182, 2025)\",\n    \"A Sober Look at Steering Vectors for LLMs (Tan et al., NeurIPS 2024)\",\n    \"Patterns and Mechanisms of Contrastive Activation Engineering (Hao et al., arXiv 2505.03189, 2025)\",\n    \"CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022, 2026)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025)\",\n    \"Calibrating Verbalized Confidence with Self-Generated Distractors (Wang & Stengel-Eskin, ICLR 2026)\",\n    \"Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (arXiv 2509.03647, 2025)\",\n    \"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation (Zhuang et al., arXiv 2512.03082, 2025)\",\n    \"Fine-Grained Activation Steering: Steering Less, Achieving More (arXiv 2602.04428, 2026)\",\n    \"Contextual Linear Activation Steering of Language Models (arXiv 2604.24693, 2026)\",\n    \"Positional Biases Shift as Inputs Approach Context Window Limits (arXiv 2508.07479, 2025) — primacy vs. recency bias dynamics\"\n  ],\n  \"description\": \"We investigate whether two competing sources of LLM miscalibration — choice-supportive bias (CSB) and contradictory-evidence overweighting (CEO), identified behaviorally by Kumaran et al. (Nature MI 2026) — produce distinguishable activation signatures, exhibit asymmetric steerability profiles, and can be corrected through bias-specific intervention that outperforms monolithic approaches. A central empirical question — what fraction of instances exhibit genuine CSB-CEO interference (partial cancellation) — determines whether the practical impact is substantial or the contribution is primarily mechanistic.\\n\\nOur work targets the bias interference problem: CSB and CEO are simultaneously active on the same instances, pulling confidence in opposite directions, creating illusory calibration where biases partially cancel (consistent with hidden miscalibration regimes where worst-calibrated slices average 41% of instances, Kobalczyk & van der Schaar 2605.13484) and heterogeneous over/under-confidence where one bias dominates instance-by-instance.\\n\\nCogBias (2604.01366) established family-dependent bias mitigation for independently-active biases; 'Sycophancy Is Not One Thing' (2509.21305) demonstrated decompose-then-steer for co-aligned sub-components; Billa (2604.15557) established routing-by-steerability; SteerConf (NeurIPS 2025) proved calibration is steerable at the prompt level; Liu (2605.05715) and Patel et al. (2604.19974) established the classification-correction gap. We extend these paradigms to the strictly harder case of opposing biases creating destructive interference.\\n\\nPhase 0A (Week 1) replicates Kumaran et al.'s behavioral paradigm on Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma 4 31B Dense, and verifies confidence computation pathways for each model via attribution patching (arXiv 2310.10348) and linear probing at PANL positions — ensuring extraction targets mechanistically validated positions rather than assuming cross-architecture transferability of Kumaran & Conmy's (2603.17839) Gemma 3-specific layer ranges. Phase 0B (Weeks 2–4, extended to 3 weeks for the expanded factorial) conducts confound-controlled contrastive extraction with matched-content pairs, a 2×2 source-attribution factorial isolating CSB's ownership mechanism, position-specific extraction at verified positions, and confound diagnostics. Phase 1 validates separability and measures steerability with complementary diagnostics (specificity ratio, adapted LAP, functional inertness test). Phase 2 trains per-instance bias dominance classifiers and — critically — estimates interference prevalence by classifying instances into CSB-dominant, CEO-dominant, interference (both active, opposing), and low-bias categories, with conditional framing: >30% interference → strong practical impact; 15–30% → primarily mechanistic with moderate practical gains; <15% → primarily interpretive. Phase 3 implements bias-specific routing (Spherical Steering / nonlinear MLP / abstention), with results interpreted both in aggregate and stratified by interference prevalence.\\n\\nCore baselines: temperature scaling, CORAL, Miao & Ungar, MERA monolithic, monolithic Spherical Steering, monolithic nonlinear MLP, SteerConf. Extended: CCPS, CogBias-style steering.\\n\\nContributions: (1) first causal activation-level characterization of simultaneously competing calibration biases with confound-controlled extraction and architecture-specific pathway verification; (2) asymmetric steerability profiles with complementary diagnostics; (3) interference prevalence quantification connecting competing biases to hidden miscalibration regimes; (4) bias-specific adaptive correction with steerability-informed routing; (5) cross-architecture behavioral replication and confidence pathway verification on Llama and Qwen families; (6) conditional impact framing establishing whether decomposed calibration correction yields substantial practical improvement or primarily mechanistic insight.\",\n  \"project_name\": \"competing_bias_steer\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"round1_issue_1_missing_competitor\": \"Tsujimura & Tagade (2508.17182) cited and differentiated. [Carried from R1]\",\n    \"round1_issue_2_model_names\": \"Fixed. [Carried from R1]\",\n    \"round1_issue_3_untested_assumption\": \"Phase 1A separability tests with thresholds; preceded by Phase 0A+0B. [Carried from R1]\",\n    \"round1_issue_4_steering_reliability\": \"Spherical Steering + MERA adaptive strength. [Carried from R1]\",\n    \"round1_issue_5_baseline_comparison\": \"MERA as critical baseline. [Carried from R1]\",\n    \"round1_issue_6_behavioral_mechanistic_leap\": \"Phase 0B pilot addresses this risk. [Carried from R1]\",\n    \"round2_issue_1_critical_missing_competitor\": \"Liu (2605.05715) integrated. [Carried from R2]\",\n    \"round2_issue_2_separability_steerability_gap\": \"Phase 1A + 1B. [Carried from R2]\",\n    \"round2_issue_3_minor_missing_references\": \"All retained. [Carried from R2]\",\n    \"round2_issue_4_nonlinear_steering_fallback\": \"Routes A/B/C. [Carried from R2]\",\n    \"round3_issue_1_MERA_baseline\": \"MERA integration. [Carried from R3]\",\n    \"round3_issue_2_nonlinear_steering_competitors\": \"ODESteer, Curveball, FLAS. [Carried from R3]\",\n    \"round3_issue_3_venue_targeting\": \"ICLR 2027 primary with honest timeline assessment. [Updated R9]\",\n    \"round3_issue_4_specificity_thresholds\": \"Empirically-learned thresholds. [Carried from R3]\",\n    \"round3_issue_5_overcomplexity\": \"Streamlined 3×3×3 + 7 baselines; prose tightened in R9 to address complexity bloat. [Updated R9]\",\n    \"round4_issue_1_missing_steerability_routing\": \"Billa (2604.15557) integrated. [Carried from R4]\",\n    \"round4_issue_2_missing_cogbias\": \"CogBias integrated. [Carried from R4]\",\n    \"round4_issue_3_novelty_overstated\": \"Novelty claims properly scoped. [Carried from R4]\",\n    \"round4_issue_4_phase1a_risk\": \"Phase 0 pilot with confound controls. [Carried from R4]\",\n    \"round4_additional_hidden_miscalibration\": \"Kobalczyk & van der Schaar, W2S. [Carried from R4]\",\n    \"round5_issue_1_prompt_content_confound\": \"Matched-content pairs, attribution factorial, confound diagnostics. [Carried from R5/R7]\",\n    \"round5_issue_2_cross_model_behavioral_generalization\": \"Phase 0A behavioral replication. [Carried from R5]\",\n    \"round5_issue_3_fallback_is_weaker_project\": \"Explicit scope reduction for fallback. [Carried from R5]\",\n    \"round5_issue_4_missing_baseline_steerconf\": \"SteerConf integrated as 7th core baseline. [Carried from R5]\",\n    \"round5_issue_5_arr_date_correction\": \"ARR October 2026 = Oct 12. [Carried from R5]\",\n    \"round7_issue_1_verbal_confidence_mechanism\": \"Kumaran & Conmy (2603.17839) integrated throughout. [Carried from R7]\",\n    \"round7_issue_2_source_attribution_confound\": \"2×2 attribution factorial in Phase 0B. [Carried from R7]\",\n    \"round7_issue_3_CCPS_missing\": \"CCPS integrated. [Carried from R7]\",\n    \"round7_issue_4_generalizability\": \"Generalizability section with 3 competing-bias pairs. [Carried from R7]\",\n    \"round7_issue_5_sycophancy_decomposition\": \"'Sycophancy Is Not One Thing' integrated throughout. [Carried from R7]\",\n    \"round7_issue_6_SAE_functional_dissociation\": \"Patel et al. (2604.19974) integrated. [Carried from R7]\",\n    \"round7_issue_7_cogbias_accuracy_verification\": \"CogBias claims scoped to abstract-verifiable figures. [Carried from R7]\",\n    \"round8_issue_1_phase0b_timeline\": \"ADDRESSED: Extended Phase 0B from 2 weeks to 3 weeks with honest breakdown (stimulus generation ~1 week bottleneck, extraction ~3-4 days, diagnostics ~1 week, iteration buffer ~3-4 days). Cascaded through all timelines: human-in-loop 12-16 → 13-17 weeks, manual 16-20 → 17-21 weeks, auto_research 7-11 → 8-12 weeks. Updated ICLR 2027 feasibility assessment: ~18 weeks available from May 19 to Sep 24; at 13-week execution → comfortable (5 weeks writing); at 17-week execution → very tight (1 week for final integration), feasible only with aggressive parallel writing starting at Phase 1. Transparent that ICLR 2027 is achievable at the shorter bound but risky at the upper bound.\",\n    \"round8_issue_2_pathway_verification\": \"ADDRESSED: Added 'Confidence Pathway Verification' sub-step at end of Phase 0A (~1 day per model, ~4-8 GPU-hours). Three complementary methods: (a) linear probes at PANL across all layers (adapting Kumaran & Conmy's layer-sweep), (b) attribution patching (Nanda et al., arXiv 2310.10348) for causal confirmation in a single backward pass, (c) LogitLens4LLMs (arXiv 2503.11667) for layer-by-layer confidence crystallization. If a model caches confidence at a different position, extraction positions adjusted accordingly. Grounded in cross-architecture evidence: behavioral axes align at AUROC 0.95 across Llama-Qwen-Mistral-Phi (arXiv 2605.09875), task schemas transfer at 100% across 7 families (arXiv 2512.17325) — supporting qualitative transferability while acknowledging architecture-specific layer ranges require verification. Added 4 new references: 2605.09875, 2512.17325, 2503.11667, 2310.10348.\",\n    \"round8_issue_3_interference_prevalence\": \"ADDRESSED: Added dedicated 'Interference Prevalence Estimation' analysis in Phase 2. Methodology: project each instance onto CSB and CEO directions, classify into 4 categories (CSB-dominant, CEO-dominant, interference with partial cancellation, low-bias), compute prevalence and cancellation magnitude. Grounded in existing evidence: Kumaran et al.'s OUCS drops from +0.210 to +0.086 in dual-active condition (condition-level cancellation); Kobalczyk's worst-calibrated slices average 41% of instances (regime-level heterogeneity). Adopted conditional framing: >30% interference → strong practical impact framing; 15-30% → primarily mechanistic; <15% → primarily interpretive. Phase 3 results reported both aggregate and interference-stratified. This analysis is itself a contribution: first per-instance quantification of competing-bias interference prevalence, connecting behavioral evidence to hidden miscalibration regimes.\",\n    \"round9_complexity_tightening\": \"MAJOR: Tightened prose throughout to address complexity bloat identified via stagnation analysis (scores declining 3.8→3.5 despite positive qualitative feedback). Compressed fallback section, generalizability section, and verbose cross-references. Removed redundant hedging. Net text reduced despite 3 substantive additions. Research on successful papers in the space (ITI/ICLR 2024, CAA/ACL 2024, CAST spotlight/ICLR 2025, 'Sycophancy Is Not One Thing') confirms that focused designs with one core claim outperform complex multi-phase proposals — the interference prevalence conditional framing helps focus the contribution claim.\"\n  }\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"MISSING CRITICAL COMPETITOR: Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) 'LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components' already decomposes overconfidence-related behavior into two orthogonal sub-components in the residual stream using difference-in-means, with distinct steering effects. This is methodologically very similar to DBS and must be cited and explicitly distinguished.\", \"MODEL NAMING ERRORS: 'Gemma 4 27B' does not exist — Gemma 4 ships as E2B, E4B, 26B-A4B (MoE), and 31B (Dense). 'Llama-3.3-8B-Instruct' has no confirmed official release — Llama 3.3 was released only as 70B; the 8B variant in the Llama 3 family is Llama-3.1-8B-Instruct.\", \"UNTESTED CORE ASSUMPTION: The entire approach rests on CSB and CEO being linearly separable in the residual stream, but Kumaran et al.'s analysis is purely behavioral (Gemma 3, GPT-4o, o1-preview) with no mechanistic evidence. 'Breaking the Mirror' found that even a simpler bias (self-preference) 'spans multiple or nonlinear directions,' challenging the linear orthogonality assumption.\", \"ACTIVATION STEERING RELIABILITY: Recent work 'Steered LLM Activations are Non-Surjective' (2604.09839) formally proves steering pushes activations off the natural prompt-reachable manifold, and 'A Sober Look at Steering Vectors' notes many behaviors are unsteerable even when sweeping layers and strengths.\", \"BASELINE COMPARISON CHALLENGE: The 96.5% ECE reduction target from 'Wired for Overconfidence' was achieved on 3B models (Qwen2.5-3B, Llama-3.2-3B) on PopQA specifically; the proposal tests 8B-31B models where circuit structure may differ substantially. Direct comparison claims need qualification.\", \"BEHAVIORAL-TO-MECHANISTIC LEAP: The proposal assumes behavioral-level biases (identified via confidence elicitation experiments) will have clean mechanistic signatures in hidden states. This is a significant empirical assumption that the paper should explicitly acknowledge and test for.\"]\nFeedback: The idea is well-motivated and the gap is real, but needs several revisions: (1) Cite and distinguish from Tsujimura & Tagade (2508.17182) — their orthogonal decomposition of assertiveness is the closest methodological precedent. Argue why CSB/CEO decomposition is more principled than emotional/logical. (2) Fix model names: use Gemma 4 31B (dense) or 26B-A4B (MoE), and Llama-3.1-8B-Instruct instead of the non-existent variants. (3) Add an explicit 'assumption validation' experiment phase: before the full DBS pipeline, verify that CSB and CEO produce distinguishable activation signatures. Consider ablating with PCA/ICA to test whether two directions suffice. (4) Temper claims about outperforming monolithic steering — frame the contribution more around interpretability and difficulty-stratified improvement rather than raw ECE numbers. (5) Acknowledge and address the non-surjectivity concern — discuss why targeted dampening of bias directions may be more robust than general steering, or include experiments that validate steered states remain on-manifold. (6) Consider adding a fallback: if CSB and CEO are not orthogonally separable, can you still improve calibration via a non-orthogonal decomposition or a multi-direction approach?\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING COMPETITOR: 'Decodable but Not Corrected by Fixed Residual-Stream Linear Steering' (arXiv 2605.05715, May 2026) demonstrates a classification-correction gap where linearly decodable directions (71.6% balanced accuracy) yield Δ≈0 under steering because the failure directions have 85-88% overlap with task-critical computation (specificity ratio ≤0.152). This directly threatens DBS-v2's Phase 3: even if CSB/CEO are decodable (Phase 1 succeeds), steering may fail due to entanglement. The paper proposes specificity ratio as a pre-intervention diagnostic — DBS-v2 must incorporate this.\", \"SEPARABILITY ≠ STEERABILITY GAP: Phase 1 validates whether CSB and CEO are separable (cosine similarity, PCA/ICA, cross-prediction ablation) but does NOT test whether identified directions are steerable without collateral damage. The 'Decodable but Not Corrected' paper shows these are empirically distinct questions. Phase 1 needs a steerability diagnostic: compute the specificity ratio (shared vs. mode-specific variance) of CSB/CEO directions relative to the overall correct-vs-incorrect subspace.\", \"MINOR MISSING REFERENCES: (a) 'Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection' (arXiv 2601.19375, Jan 2026) — another norm-preserving rotation method predating Spherical Steering, with discriminative layer selection. (b) 'Minimizing Collateral Damage in Activation Steering' (arXiv 2605.01167, May 2026) — formalizes collateral damage from steering interventions and proposes minimum-damage solutions, directly relevant to the manifold-preservation rationale.\", \"NO NON-LINEAR STEERING FALLBACK: The proposal's fallback (SAE-based features) addresses the case where CSB/CEO are not linearly separable, but not the case where they are separable but not linearly steerable. The 'Decodable but Not Corrected' paper shows a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods yield Δ≈0. Phase 3 should include a non-linear steering fallback (e.g., learned MLP correction) alongside Spherical Steering.\"]\nFeedback: The revision from round 1 is excellent — all prior issues were addressed thoroughly and honestly. The main new concern is a very recent paper (2605.05715, this month) that identifies a 'classification-correction gap': failure directions can be linearly decodable but not steerable because they overlap heavily with task-critical computation. This is distinct from the off-manifold concern already addressed via Spherical Steering. Concrete fixes: (1) Add a 'steerability diagnostic' to Phase 1 — after extracting CSB/CEO directions, compute their specificity ratio (proportion of mode-specific vs. shared variance with the correct/incorrect subspace). If specificity is low (<0.2), flag high entanglement risk. (2) Add a non-linear steering fallback in Phase 3: when specificity is low, use a learned non-linear residual correction (small MLP) instead of fixed-direction rotation. (3) Cite Selective Steering and Minimizing Collateral Damage as part of the geometry-aware steering landscape. (4) Explicitly discuss the separation between 'decodable' and 'steerable' in the approach section — this strengthens the paper's contribution by showing awareness of a subtle and important distinction.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MISSING CRITICAL BASELINE: MERA ('To Steer or Not to Steer?', Hedström et al., ICML 2025, arXiv 2510.13290) implements selective steering with adaptive strength and abstention — directly overlapping with Routes C and D. MERA optimizes intervention direction AND calibrates when/how much to steer, with provable non-degradation guarantees. It can be applied ON TOP of existing steering methods. This must be cited as a baseline and distinguished from: DBS-v2 decomposes biases while MERA treats errors monolithically; DBS-v2 routes between intervention types while MERA modulates a single intervention's strength.\", \"MISSING NONLINEAR STEERING COMPETITORS: The landscape fails to cite (a) Curveball Steering (arXiv 2603.09313, March 2026) — polynomial kernel PCA-based nonlinear steering that explicitly addresses geometric distortion in activation spaces, directly relevant to the linear vs. nonlinear routing rationale; (b) FLAS (arXiv 2605.05892, May 2026) — flow-based activation steering learning concept-conditioned velocity fields, first method to outperform prompting on AxBench; (c) ODESteer (arXiv 2602.17560, ICLR 2026) — ODE-based multi-step adaptive steering with barrier functions. These represent the rapidly maturing nonlinear steering landscape that Route B must be positioned against.\", \"AAAI 2027 PRIMARY TARGET IS INFEASIBLE: The full paper deadline is July 28, 2026 — approximately 10 weeks from now. The manual timeline estimate is 16-20 weeks. Even the auto_research timeline (6-10 weeks) is at the edge, and auto_research is the most expensive mode. No honest accounting of Phase 1A→1B sequential dependency, model access setup time, or writing time supports AAAI 2027 as 'primary target.' ARR August 2026 (Aug 3) is similarly tight. Realistic primary target should be ICLR 2027 or NeurIPS 2026 workshop for Phase 1 results.\", \"SPECIFICITY RATIO THRESHOLDS ARE WEAKLY JUSTIFIED: The proposed routing thresholds (≥0.5 HIGH, 0.2-0.5 MEDIUM, <0.2 LOW) are interpolated from exactly two empirical data points in Liu (2605.05715): overthinking at ≤0.152 (LOW, linear steering fails) and refusal at ~0.999 (HIGH, linear steering succeeds). There is no empirical or theoretical basis for the 0.2 and 0.5 boundaries. These thresholds should be explicitly framed as initial hypotheses to be refined during Phase 1B rather than as calibrated routing criteria.\", \"OVERCOMPLEXITY RISK: The proposal includes 4 intervention routes, 5 models (3 primary + 2 supplementary), 4 datasets, 10+ baselines, Phase 1A with 5 separability tests, Phase 1B with 4 steerability diagnostics, 2 alternative norm-preserving methods to ablate, and COAST-informed loss weighting. This is an enormous experimental matrix that risks under-execution. Consider scoping to 2-3 models and 2 routes (linear + nonlinear with abstention) for the primary paper, with the full matrix as supplementary.\"]\nFeedback: The revision from round 2 is strong — the integration of Liu (2605.05715) and the decodable-steerable distinction is thorough and genuine. Three concrete fixes for round 4: (1) Cite MERA (ICML 2025) as a key baseline — it's the closest existing work on selective steering + abstention, and failing to cite a published ICML paper implementing core components of your Route C/D would be a serious oversight for reviewers. Distinguish DBS-v2 by emphasizing the multi-bias decomposition and steerability-based routing that MERA lacks. (2) Add Curveball Steering, FLAS, and ODESteer to the landscape — these are the 2026 nonlinear steering methods your Route B competes against. Position Route B's bottleneck MLP as motivated by Liu's calibration-specific finding, while acknowledging these general-purpose alternatives. (3) Revise venue targeting: drop AAAI 2027 as primary (the math doesn't work). Make ICLR 2027 (~Oct 2026) the primary target, NeurIPS 2026 workshop (Aug 29) for Phase 1 results, and ARR cycle for full paper backup. (4) Explicitly frame specificity ratio thresholds as hypotheses, not established boundaries. (5) Consider streamlining the experimental matrix — 5 models × 4 routes × 10+ baselines may impress but also signals unfocused ambition to reviewers.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MISSING REFERENCE: 'Predicting Where Steering Vectors Succeed' (arXiv 2604.15557, April 2026) proposes a three-regime framework — (1) concept not represented (no method works), (2) nonlinear encoding (nonlinear methods needed), (3) output-aligned (linear steering works) — that directly parallels DBS-v2's Route C/Route B/Route A routing. The paper uses Linear Accessibility Profile (LAP) as a training-free steerability diagnostic (ρ=0.86-0.91 correlation with steering effectiveness), which is conceptually adjacent to Liu's specificity ratio and Phase 1B's steerability assessment. This must be cited and distinguished from. Key distinction: 2604.15557 operates per-concept/per-layer with synthetic binary concepts, not per-instance with naturalistic calibration biases; it doesn't decompose biases. But it establishes the routing-by-steerability paradigm that DBS-v2 claims as novel.\", \"MISSING REFERENCE: CogBias (arXiv 2604.01366, April 2026) decomposes cognitive biases into four families (Judgment, Information Processing, Social, Response), finds them linearly separable in activation space (97.8% classification accuracy), and demonstrates family-dependent mitigation — 'prompt-level debiasing substantially reduces Response biases but backfires for Judgment biases.' This is the closest existing work to the 'different biases need different interventions' principle underlying DBS-v2. Must be cited alongside Tsujimura & Tagade. Key distinction: CogBias addresses cognitive biases broadly, not calibration-specific competing biases; its interventions are not steerability-aware.\", \"NOVELTY CLAIM OVERSTATED: With CogBias demonstrating bias-family-specific intervention, 2604.15557 demonstrating three-regime steerability routing, and MERA demonstrating adaptive steering + abstention, the claim of being 'first to jointly decompose + route' needs significant qualification. The novelty is more precisely: first to apply bias-grounded decomposition to competing calibration biases (CSB/CEO) specifically, with per-direction steerability assessment — not first to route interventions by steerability regime or to decompose biases for differential treatment.\", \"PHASE 1A RISK STILL UNDERSPECIFIED: The contingency plan (SAE-based features + subspace projection classifier) if CSB/CEO are not separable adds significant complexity and is not well-developed. What if the contrastive stimuli themselves don't reliably elicit the target biases in a controlled way? The behavioral phenomena in Kumaran et al. were observed in multi-turn conversational setups with specific confidence elicitation protocols — translating this to a contrastive activation extraction paradigm is non-trivial and could easily produce noisy or confounded directions.\"]\nFeedback: The revision from round 3 is strong — MERA integration, nonlinear steering landscape, venue corrections, threshold reframing, and experimental streamlining are all well-executed. Two concrete fixes for round 5: (1) Cite 'Predicting Where Steering Vectors Succeed' (2604.15557) as a key methodological predecessor for the routing logic. Its three-regime framework (no representation / nonlinear / output-aligned) directly parallels Routes C/B/A. Distinguish DBS-v2 by emphasizing that your routing operates per-instance with naturalistic competing biases, not per-concept with synthetic binary features, and that your steerability assessment is grounded in bias-specific specificity ratios rather than general logit-lens accessibility. Consider whether LAP could complement the specificity ratio as an additional diagnostic in Phase 1B. (2) Cite CogBias (2604.01366) alongside Tsujimura & Tagade as showing that bias-family-specific intervention is viable and that different bias types respond differently to interventions — this actually strengthens your motivation (the principle works for cognitive biases broadly; you apply it to the specific competing-bias calibration problem). (3) Tighten the novelty framing: the contribution is NOT 'first to route interventions by steerability' (2604.15557 does this) or 'first to decompose biases for differential treatment' (CogBias does this). The contribution IS: first to identify competing calibration biases (CSB vs. CEO) in activation space, measure their asymmetric steerability profiles, and apply bias-specific correction with non-degradation guarantees. This is still a meaningful contribution if Phase 1A succeeds.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"PHASE 0 PROMPT-CONTENT CONFOUND: The contrastive extraction methodology has an unaddressed confound. For CSB: contrasting 'answer shown' vs. 'answer hidden' prompts differ not only in bias activation but in information content (one prompt literally contains more text — the model's own answer). For CEO: contrasting 'contradictory advice present' vs. 'absent' prompts differ in the presence of additional advisory text. The extracted direction may capture 'prompt contains additional evaluative content' rather than 'bias is active.' This is distinct from the behavioral-to-mechanistic gap already acknowledged and requires explicit mitigation: matched-length prompts with semantically neutral filler, attention-weighted extraction focusing on confidence-bearing tokens rather than global mean, or information-theoretic controls. Without this, Phase 0 success (>60% probe accuracy) may reflect prompt-content confounds rather than genuine bias detection.\", \"CROSS-MODEL BEHAVIORAL GENERALIZATION UNADDRESSED: Kumaran et al.'s competing biases were characterized on Gemma 3, GPT-4o, and o1-preview. Phase 0 pilot uses Llama-3.1-8B-Instruct — a model not in the original study. The full evaluation uses Gemma 4 31B Dense (different from Gemma 3) and Qwen3-8B. The behavioral phenomena (CSB magnitude, CEO overweighting ratio) may differ substantially or not replicate across these architectures. The proposal should explicitly plan to verify behavioral replication on each target model before assuming the contrastive paradigm applies.\", \"PHASE 0 FALLBACK PATH IS A DIFFERENT (WEAKER) PROJECT: The proposal states that if probing accuracy is <55%, it will 'pivot to behavioral-signal-guided probing: use model output changes to label instances post-hoc, then probe for internal signatures correlated with these behavioral labels.' This fallback trades causal contrastive evidence for correlational association, fundamentally weakening contribution (1) from 'first causal activation-level characterization' to 'statistical association between behavioral labels and activations.' The proposal should be more explicit that this fallback, while still informative, would require repositioning the paper's claims and likely reduces it from a top-tier to a solid contribution.\", \"MISSING BASELINE: SteerConf (Zhou et al., arXiv 2503.02863, NeurIPS 2025) applies steering-based confidence calibration without training, achieving 29% AUROC increase and 16% ECE reduction across 7 benchmarks. While it operates at the prompt level (not activation level), it is a published NeurIPS paper directly addressing confidence calibration via steering and should be acknowledged in the landscape and considered as a baseline — it represents the 'prompt-level steering' approach that activation-level methods should outperform.\", \"MINOR: ARR October 2026 deadline is October 12, not '~Oct 15' as stated.\"]\nFeedback: This is a well-crafted proposal after 4 strong revision rounds. All references verified, the gap is genuine, and the novelty claims are now properly scoped. Three concrete improvements for round 6: (1) Address the prompt-content confound in Phase 0 explicitly — design contrastive pairs that control for information content differences (e.g., matched-length prompts where 'answer hidden' condition replaces the answer with a semantically neutral placeholder of equal length, and 'advice absent' condition replaces contradictory advice with irrelevant neutral text). This is the most important fix because it determines whether Phase 0 measures bias activation or prompt structure. (2) Add a 'behavioral replication' step at the start of Phase 0: before extracting activations, verify that each target model exhibits both CSB and CEO in Kumaran et al.'s behavioral paradigm. If CSB/CEO magnitudes are <50% of Kumaran's reported effect sizes on a given model, flag that model as potentially unsuitable. (3) Be honest about the fallback path: explicitly state that the behavioral-signal-guided probing fallback would change the paper's contribution from causal mechanistic evidence to correlational analysis, and discuss what venue/framing would be appropriate for that weaker result. Also add SteerConf as a landscape reference and fix the ARR date.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"MISSING REFERENCE: 'How do LLMs Compute Verbal Confidence' (arXiv 2603.17839, March 2026) provides mechanistic evidence that confidence representations are cached at answer-adjacent positions and retrieved at verbalization sites, with confidence being gathered from answer tokens. This directly informs Phase 0B's token-position-specific extraction methodology — the 'confidence-bearing token position' that the proposal identifies as a key extraction point is studied mechanistically in this paper. Citing it would both strengthen the extraction strategy and demonstrate awareness of where confidence signals actually reside.\", \"SOURCE ATTRIBUTION CONFOUND IN MATCHED-CONTENT CSB PAIRS: The Phase 0B design for CSB replaces the model's own answer with 'a plausible but randomly-selected alternative answer attributed to another LLM.' However, this introduces a source attribution confound: the model may process 'my answer' vs. 'another LLM's answer' differently beyond bias activation — e.g., models may have learned to attend differently to self-generated vs. externally-attributed content. The 'scrambled-answer' control partially addresses this, but the primary contrast still confounds CSB with source attribution. Consider adding a condition where the model's own answer is presented but attributed to 'another LLM' (same content, different attribution) to isolate the self-generated aspect of CSB from the information-content aspect.\", \"MISSING LANDSCAPE REFERENCE: CCPS (arXiv 2505.21772, EMNLP 2025) achieves ~55% ECE reduction and 21% Brier score improvement via perturbation-stability probing across 8B-32B models (Llama, Qwen, Mistral). While a different paradigm (perturbation-based rather than steering), it's a recent published calibration method evaluated on overlapping model families and benchmarks. Should be mentioned in the landscape and considered as an extended baseline.\", \"IMPACT NARROWNESS AND GENERALIZABILITY: The paper should explicitly discuss whether the competing-bias framework generalizes beyond CSB/CEO. Are there other pairs of simultaneously competing biases in LLMs? What about sycophancy vs. truthfulness, or fluency vs. factuality? A brief discussion of generalizability would strengthen the impact argument and preempt reviewer concerns about the framework being overly specific to Kumaran's experimental paradigm.\"]\nFeedback: This is a strong proposal after 5 rigorous revision rounds. All references verified, the gap is genuine, and the methodology is thoughtful. Three concrete improvements for round 7: (1) Cite 'How do LLMs Compute Verbal Confidence' (2603.17839) — its finding that confidence is cached at answer-adjacent tokens and retrieved at verbalization directly validates your token-position-specific extraction in Phase 0B, and its mechanistic analysis on Gemma 3 27B and Qwen 2.5 7B provides complementary evidence for your target model families. (2) Add one more CSB confound control: present the model's own answer but attributed to 'another LLM' — this isolates the self-generated attribution from the information content, making the CSB extraction strictly about ownership-bias rather than content-presence. This is a small addition (~500 more pairs) but substantially strengthens the causal claim. (3) Add a brief generalizability discussion: identify 2-3 other plausible competing-bias pairs (e.g., sycophancy vs. truthfulness, fluency pressure vs. factual constraint) and note that the framework's Phase 0→3 pipeline is reusable. This addresses the main impact concern without requiring additional experiments. Also add CCPS to the landscape. The proposal is very close to the pass threshold — these are all addressable in one revision round.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"ALL FOUR ROUND 6 ISSUES UNADDRESSED: (1) 'How do LLMs Compute Verbal Confidence' (arXiv 2603.17839, March 2026) remains uncited despite directly validating the token-position-specific extraction in Phase 0B — it shows confidence is cached at answer-adjacent positions and retrieved at verbalization, studied on Gemma 3 27B and Qwen 2.5 7B. (2) The source attribution confound in CSB pairs is still not controlled: the requested control — presenting the model's OWN answer but attributed to 'another LLM' (same content, different attribution) — would isolate the self-generated ownership component of CSB from information-content differences. The current design changes BOTH content AND attribution simultaneously. (3) CCPS (arXiv 2505.21772, EMNLP 2025) remains uncited — it achieves ~55% ECE reduction via perturbation-stability probing on overlapping model families (Llama, Qwen, Mistral) at 8B-32B scale, making it a relevant landscape reference and potential extended baseline. (4) No generalizability discussion identifying other plausible competing-bias pairs.\", \"MISSING METHODOLOGICAL PRECEDENT: 'Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs' (arXiv 2509.21305, submitted ICLR 2026) decomposes sycophancy into distinct, independently steerable sub-components (sycophantic agreement vs. sycophantic praise vs. genuine agreement) using difference-in-means, activation additions, and subspace geometry — demonstrating that each can be independently amplified or suppressed without affecting others. This is the closest methodological precedent for decomposing a complex behavioral phenomenon into independently steerable activation-level components. The key distinction from this proposal: 'Sycophancy Is Not One Thing' decomposes co-existing but not opposing behaviors, while this proposal targets simultaneously OPPOSING biases that create interference. This distinction should be explicitly articulated.\", \"MISSING RELEVANT REFERENCE: 'Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders' (arXiv 2604.19974, April 2026) shows that statistically decodable features can be 'functionally inert' — pure incorrectness features have near-zero accuracy impact when suppressed despite being statistically distinguishable. This directly reinforces Liu's classification-correction gap with SAE-based evidence and implies that Phase 1A's separability success does NOT guarantee Phase 3's intervention success. Should be cited alongside Liu.\", \"UNVERIFIABLE CLAIM: The '97.8% mean classification accuracy via linear probes' attributed to CogBias (2604.01366) could not be independently confirmed from the abstract or accessible paper content. The abstract mentions linear separability and 26-32% steering reduction but does not surface this specific accuracy figure. If this number comes from the paper body, it should be noted as such; if it was inferred or estimated, it should be flagged.\"]\nFeedback: This is a strong proposal after 6 rigorous revision rounds, but the complete failure to address ANY of the 4 round 6 issues is a significant concern. Concrete fixes for round 8: (1) Cite 'How do LLMs Compute Verbal Confidence' (2603.17839) — its mechanistic finding that confidence is cached at answer-adjacent positions directly validates your Phase 0B token-position extraction strategy. This is a 1-sentence addition that substantially strengthens your methodology. (2) Add the same-content-different-attribution CSB control: present the model's OWN answer text but attributed to 'another LLM.' This isolates the ownership component of CSB from information content and requires only ~500 additional pairs. Without it, a reviewer can argue your CSB direction captures 'recognizing my own output' rather than 'choice-supportive confidence inflation.' (3) Add CCPS to landscape and extended baselines. (4) Add a brief generalizability paragraph: identify 2-3 other competing-bias pairs (e.g., sycophantic agreement vs. truthfulness, fluency pressure vs. factual constraint — note 'Sycophancy Is Not One Thing' already shows these are separable) and state that the Phase 0→3 pipeline is reusable. (5) Cite 'Sycophancy Is Not One Thing' (2509.21305) as a key methodological precedent and distinguish it: that paper decomposes co-existing behaviors; yours targets opposing biases creating interference effects. (6) Cite 'Are LLM Uncertainty and Correctness Encoded by the Same Features?' (2604.19974) alongside Liu — it independently confirms that decodable ≠ functional via SAE analysis, strengthening your rationale for Phase 1B steerability assessment. (7) Verify the CogBias 97.8% figure or add a caveat. All of these are small, focused additions — the core architecture is sound.\n\n### Round 8 review\nVerdict: revise\nIssues: [\"PHASE 0B TIMELINE UNDERESTIMATED: The expanded Phase 0B design now includes ~4000 contrastive pairs across matched-content pairs, scrambled-answer controls, supporting-advice controls, AND the 2×2 attribution factorial ({own text, other text} × {self-attributed, other-attributed}), all requiring token-length matching and semantic neutrality — plus token-position-specific extraction at three positions per instance, confound diagnostic battery (prompt-structure probes, token-count correlations, attribution-alignment verification), and analysis on the strongest Phase 0A model. Two weeks is likely insufficient: stimulus generation alone (creating plausible alternative answers of matched token length, irrelevant neutral advice of matched length, attribution-varied conditions) requires careful prompt engineering and validation. Budget 3-4 weeks for Phase 0B, which cascades through the entire timeline and threatens the ICLR 2027 Sep 24 deadline.\", \"MODEL-SPECIFIC PANL→CC PATHWAY NOT VALIDATED: The token-position-specific extraction strategy is grounded in Kumaran & Conmy's mechanistic findings on Gemma 3 27B (layers 22-28 for PANL caching, 30-36 for CC retrieval) and verified on Qwen 2.5 7B. However, the target models are Gemma 4 31B Dense (different architecture, released April 2026), Qwen3-8B (different generation), and Llama-3.1-8B-Instruct (never studied for confidence computation). The PANL and CC token positions are structurally transferable, but the layer ranges where confidence caching and retrieval occur could differ substantially — especially for Llama, which has a different architecture family entirely. Phase 0B should include a preliminary confidence-pathway verification step for each target model (e.g., confirming via attention pattern analysis or activation patching that confidence information flows through answer-adjacent positions).\", \"IMPACT ARGUMENT NEEDS STRENGTHENING: The practical value proposition — that decomposed bias-specific correction outperforms monolithic methods — faces a quantitative challenge. Hidden miscalibration regimes (Kobalczyk & van der Schaar) represent input-dependent heterogeneity, but the proposal doesn't estimate what fraction of miscalibration instances involve genuine CSB-CEO interference (partial cancellation). If interference cases are only 10-20% of all miscalibrated instances, aggregate ECE/Brier improvements may be modest even with perfect decomposed correction. The proposal should include a Phase 2 analysis estimating the prevalence of interference-dominated instances and present expected improvement bounds conditional on interference prevalence.\"]\nFeedback: This is an excellent proposal after 7 rigorous revision rounds — all round 7 issues were thoroughly addressed, all references verified as accurate, and the gap is genuine. Three targeted improvements for round 9: (1) Revise Phase 0B timeline to 3-4 weeks (acknowledging the attribution factorial adds ~500 pairs per condition and the confound diagnostic battery requires careful statistical analysis), and cascade the timeline impact to honest ICLR 2027 feasibility assessment — if this pushes the human-in-loop timeline to 14-18 weeks, be transparent that ICLR 2027 is feasible only with the shorter bound and aggressive parallel writing. (2) Add a brief 'confidence pathway verification' step at the start of Phase 0B or end of Phase 0A: for each target model, verify that confidence information flows through answer-adjacent positions (PANL→CC) using lightweight activation patching or attention analysis, before committing to the extraction positions. This is ~1 day of compute per model and prevents committing the entire Phase 0B pipeline to positions that may not be confidence-relevant in the target architecture. (3) In Phase 2, add an 'interference prevalence estimation' analysis: quantify what fraction of instances show substantial CSB-CEO partial cancellation (e.g., instances where both bias projections are above median magnitude but in opposing directions). This directly addresses the impact concern — if prevalence is high (>30%), the decomposed approach has clear practical value; if low (<15%), the paper's contribution is more interpretive than practical, and the framing should adjust accordingly.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"...\"}\n  },\n  \"issues\": [\"specific issue 1\", ...],\n  \"feedback\": \"Actionable feedback (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold\n- \"fail\": fundamental flaw (gap doesn't exist, approach provably wrong)\n- Threshold is HIGH (4.0/5.0): only truly outstanding ideas should pass.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-19T16:37:20.023Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T16:37:20.023Z",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-19T16:37:20.037Z_

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

## Idea under review (round 9/10)
{
  "title": "Competing Biases, Asymmetric Steerability: Decomposing LLM Miscalibration for Targeted Activation Correction",
  "core_problem": "LLM miscalibration arises from at least two competing biases — choice-supportive bias (CSB, inflating confidence in initial answers) and contradictory-evidence overweighting (CEO, causing excessive confidence revision under criticism) — that are simultaneously active and pull confidence in opposite directions on the same instances (Kumaran et al., Nature MI 2026). This creates a bias interference problem: competing biases can partially cancel (producing illusory calibration where global metrics look good but localized failures persist) or one can dominate instance-by-instance (producing heterogeneous over/under-confidence patterns). Kobalczyk & van der Schaar (2605.13484) independently confirmed that global reliability diagrams 'hide rather than reveal calibration failures' because 'opposing errors cancel when aggregated by confidence' — with worst-calibrated slices containing on average 41% of test instances across 48 model-dataset pairs — but provide no mechanistic explanation for WHY opposing errors exist. Five lines of related work address parts of this problem but not the whole: (1) CogBias (Huang et al., 2604.01366) demonstrates family-dependent bias mitigation — but addresses independently-active biases, not simultaneously competing ones. (2) Billa (2604.15557) proposes a three-regime steerability framework with LAP diagnostic (ρ=0.86–0.91) — but operates per-concept with synthetic binary features. (3) MERA (Hedström et al., ICML 2025) provides adaptive steering with non-degradation guarantees — but treats errors monolithically. (4) SteerConf (Zhou et al., NeurIPS 2025) achieves 29% AUROC increase via prompt-level confidence steering — but operates without mechanistic decomposition. (5) 'Sycophancy Is Not One Thing' (Vennemeyer et al., 2509.21305) demonstrates that complex behaviors decompose into independently steerable sub-components — but their sub-components are co-aligned, not opposing. The classification-correction gap (Liu, 2605.05715; Patel et al., 2604.19974) adds a further obstacle: linearly decodable directions may not be linearly steerable. A critical open question — central to practical impact — is whether the interference subpopulation (instances where both biases partially cancel) is large enough to justify decomposed correction over monolithic approaches, or whether the contribution is primarily mechanistic. Can we characterize competing biases at the activation level, measure their asymmetric steerability profiles, quantify interference prevalence, and demonstrate that decomposed correction outperforms monolithic methods on the interference subpopulation?",
  "opportunity": "Kumaran et al. (Nature Machine Intelligence, 2026; arXiv 2507.03120) established behavioral evidence that LLM miscalibration results from two mechanistically distinct biases: CSB inflates confidence in selected answers (+0.21 confidence boost, p<0.001), while CEO causes models to over-react to opposing evidence (overweighting ratio 2.58 for opposing vs. 1.095 for supporting advice). Critically, in the dual-active condition (Answer Shown + Opposite Advice), both biases are simultaneously active — CSB partially suppresses CEO-driven behavior (change-of-mind drops from 85.0% to 39.2%), and the Over/Underconfidence Score drops from +0.210 to +0.086, providing condition-level evidence of partial cancellation. However, Kumaran et al. provided only behavioral evidence with no activation-level analysis, and their study covered Gemma 3 (12B/27B), GPT-4o, o1-preview, and DeepSeek R1 7B — but not the Llama or Qwen families widely used for mechanistic interpretability.\n\nKumaran, Conmy et al. ('How do LLMs Compute Verbal Confidence,' arXiv 2603.17839, March 2026) provided the mechanistic foundation: verbal confidence is cached at the Post-Answer-Newline (PANL) token position, with information flowing answer tokens → PANL (layers 22–28) → Confidence-Colon position (layers 30–36) in Gemma 3 27B. Token log-probabilities explain only 8.4% of variance (R²_CV = 0.084), while PANL-cached representations explain substantial additional variance. This directly validates our token-position-specific extraction strategy. However, these layer ranges are architecture-specific — verified only on Gemma 3 27B and Qwen 2.5 7B. Cross-architecture evidence suggests the qualitative strategy (caching at answer-adjacent positions) transfers broadly: behavioral axes align tightly across Llama-Qwen-Mistral-Phi architectures with mean binary AUROC of 0.95 (arXiv 2605.09875), and task-schema representations transfer at 100% via late MLP patching across 9 models from 7 Transformer families (arXiv 2512.17325). Nevertheless, architecture-specific layer ranges require verification for each target model — motivating our Phase 0A confidence pathway verification step.\n\nCogBias (Huang et al., arXiv 2604.01366) demonstrated that cognitive biases are encoded as linearly separable directions and that bias-family-specific intervention is both viable and necessary: activation steering achieves 26–32% bias reduction overall, with effectiveness varying dramatically by family. CogBias establishes that different biases need different interventions — but addresses independently-active biases on different task types, not simultaneously competing biases.\n\n'Sycophancy Is Not One Thing' (Vennemeyer et al., arXiv 2509.21305) provides the closest methodological precedent: using difference-in-means and activation additions across 5 models, they decomposed sycophancy into independently steerable sub-components. The critical distinction: their sub-components are co-aligned (various forms of user-pleasing output), whereas CSB and CEO are opposing biases creating destructive interference — a strictly harder decomposition problem.\n\nBilla (arXiv 2604.15557) established the routing-by-steerability paradigm: LAP predicts steering effectiveness at ρ=0.86–0.91 across 24 concept families. SteerConf (Zhou et al., NeurIPS 2025) achieves 29% AUROC increase and 16% ECE reduction via prompt-level confidence steering — the strongest training-free behavioral baseline. CCPS (Khanmohammadi et al., arXiv 2505.21772, EMNLP 2025) achieves ~55% ECE reduction via perturbation-stability probing on Llama/Qwen/Mistral 8B–32B — a strong representation-based baseline, though monolithic.\n\nMiao & Ungar (arXiv 2603.25052) showed calibration and verbalized confidence are orthogonal in the residual stream (cosine <0.04), achieving 4–7× ECE improvement via adaptive steering. Liu (arXiv 2605.05715) demonstrated the classification-correction gap: decodable failure directions yield Δ≈0 under linear steering (specificity ratio ≤0.152), but a nonlinear bottleneck MLP achieves Δ=+2.8pp. Patel et al. (arXiv 2604.19974) independently confirmed via SAE analysis that 'pure incorrectness features' are functionally inert despite being decodable — reinforcing that separability does NOT guarantee steerability. Kobalczyk & van der Schaar (arXiv 2605.13484) discovered hidden miscalibration regimes across 48 model-dataset pairs where opposing errors cancel when aggregated, with worst-calibrated slices averaging 41% of test instances — but no per-instance interference prevalence estimate exists.\n\nThe convergence of (a) behavioral evidence of competing biases with quantitative effect sizes and condition-level cancellation evidence, (b) mechanistic understanding of confidence computation pathways with cross-architecture transferability support, (c) established decompose-then-steer and routing-by-steerability paradigms, (d) the decodable–steerable distinction, and (e) hidden miscalibration regimes suggesting substantial subpopulations affected by opposing errors creates an opportunity for the next step: extending from independently-active and co-aligned biases to simultaneously competing and opposing calibration biases.",
  "landscape": "Kumaran et al. (Nature MI, 2026) identified competing biases (CSB and CEO) via behavioral experiments on Gemma 3 12B/27B, GPT-4o, o1-preview, and DeepSeek R1 7B but proposed no correction framework and provided no activation-level evidence. Effect magnitudes varied substantially across models, and no Llama or Qwen models were tested. Kumaran, Conmy et al. (arXiv 2603.17839) subsequently showed that verbal confidence is cached at the PANL token position with information flowing answer tokens → PANL (layers 22–28) → CC (layers 30–36) in Gemma 3 27B, and verified on Qwen 2.5 7B. However, these architecture-specific layer ranges have not been validated on Llama models or on the newer Gemma 4 and Qwen3 generations — the qualitative strategy (answer-adjacent caching) has cross-architecture support (behavioral axes align at AUROC 0.95 across Llama-Qwen-Mistral-Phi, arXiv 2605.09875; task schemas transfer at 100% across 7 families, arXiv 2512.17325), but specific layer ranges are architecture-dependent and require per-model verification.\n\nCogBias (Huang et al., arXiv 2604.01366) organizes cognitive biases into four families, demonstrates linear separability, and shows family-dependent mitigation (26–32% steering reduction, with prompt debiasing backfiring for Judgment biases). CogBias establishes two principles: (a) biases are linearly encoded and separable, and (b) different families require different interventions. However, CogBias addresses independently-active biases on different task types — not simultaneously competing biases on the same instances.\n\n'Sycophancy Is Not One Thing' (Vennemeyer et al., arXiv 2509.21305) is the closest methodological precedent: across 5 models, they decomposed sycophancy into independently steerable sub-components via difference-in-means. Key distinction: their sub-components (sycophantic agreement, praise, genuine agreement) are co-aligned, while our target biases (CSB, CEO) are opposing — creating destructive interference that makes individual directions harder to isolate via difference-in-means.\n\nBilla (arXiv 2604.15557) proposes three steerability regimes with LAP diagnostic (ρ=0.86–0.91 across 24 concept families on 5 models). Key distinctions: Billa operates per-concept with synthetic binary features, not per-instance with naturalistic competing biases; LAP's correlation weakens on smaller models (ρ=0.50–0.52 on Pythia-2.8B); and its applicability to non-binary calibration constructs is untested.\n\nSteerConf (Zhou et al., NeurIPS 2025) achieves 29% AUROC increase and 16% ECE reduction via prompt-level confidence steering on GPT-3.5, LLaMA 3, and GPT-4 — the strongest training-free baseline. CCPS (Khanmohammadi et al., EMNLP 2025) achieves ~55% ECE reduction and 21% Brier score reduction via perturbation-stability probing on Llama/Qwen/Mistral 8B–32B — a strong representation-based baseline. Both are monolithic (no bias decomposition).\n\nLiu (arXiv 2605.05715) demonstrated the classification-correction gap: failure directions (71.6% balanced accuracy) yield Δ≈0 across 29 linear steering configurations (specificity ratio ≤0.152), but a bottleneck MLP achieves Δ=+2.8pp. Patel et al. (arXiv 2604.19974) confirmed via SAE analysis on Llama-3.1-8B and Gemma-2-9B that 'pure incorrectness features' are functionally inert while confounded features yield 1.1% accuracy improvement — both studied single failure modes, not decomposed competing biases.\n\nKobalczyk & van der Schaar (arXiv 2605.13484) discovered hidden miscalibration regimes across 48 model-dataset pairs where opposing errors cancel when aggregated, with worst-calibrated slices containing on average 41% of test instances in the 18 most-affected pairs. This provides independent evidence for bias interference but no mechanistic explanation, no bias decomposition, and — critically — no per-instance prevalence estimate for competing-bias interference. Whether the 41% figure reflects CSB-CEO cancellation or other sources of heterogeneous miscalibration is an open question our Phase 2 interference prevalence estimation addresses.\n\nMERA (Hedström et al., ICML 2025) provides adaptive steering with non-degradation guarantees via constrained optimization — but with a single monolithic probe. The nonlinear steering landscape (ODESteer, ICLR 2026; Curveball Steering, 2026; FLAS, 2026) provides powerful alternatives when linear steering fails. Spherical Steering (ICML 2026) preserves activation norms via geodesic rotation, and COAST (2605.01167) minimizes collateral damage.\n\nNo existing method addresses simultaneously competing calibration biases with per-instance diagnosis and bias-specific correction: CogBias decomposes independently-active families; 'Sycophancy Is Not One Thing' decomposes co-aligned sub-components; MERA adapts monolithically; Kobalczyk identifies hidden regimes without decomposition. Our work uniquely targets opposing biases that create interference, requiring joint decomposition, steerability assessment, and interference prevalence quantification.",
  "inspired_by": "Gap: Competing biases create interference — partially canceling on some instances (Kumaran et al.'s OUCS dropping from +0.210 to +0.086 in the dual-active condition; Kobalczyk's 41% worst-calibrated slices) and producing heterogeneous patterns on others — that no existing method decomposes or quantifies at the per-instance level. Pattern: CogBias proves family-specific intervention works → 'Sycophancy Is Not One Thing' proves complex behaviors decompose into steerable sub-components → Billa proves steerability-based routing works (LAP, ρ=0.86–0.91) → SteerConf proves calibration is steerable → Liu + Patel et al. prove decodable ≠ steerable → Kumaran & Conmy map confidence computation pathways (PANL caching) → cross-architecture evidence (2605.09875) supports pathway transferability. Untried combination: Extend these principles from independent/co-aligned biases to simultaneously competing and opposing calibration biases, with interference prevalence quantification as a novel empirical core. Key hypothesis: CSB and CEO have asymmetric steerability profiles because they involve different cognitive processes (self-evaluation vs. evidence integration), and the interference subpopulation is substantial enough (>30%, given Kobalczyk's 41% worst-slice finding) to justify decomposed correction.",
  "approach": "We investigate whether competing calibration biases (CSB and CEO) are distinguishable in activation space, exhibit asymmetric steerability, and can be corrected through bias-specific intervention that outperforms monolithic approaches — with interference prevalence quantification as a central empirical question determining the paper's practical impact framing. Evaluated on 3 models × 3 datasets with 7 core baselines.\n\n**Phase 0A — Behavioral Replication & Confidence Pathway Verification (Week 1):**\n\nWe replicate Kumaran et al.'s 2×3 factorial design on each target model (Llama-3.1-8B-Instruct, Qwen3-8B, Gemma 4 31B Dense) with 500 questions per condition at 70% stated advice accuracy. We measure CSB magnitude (confidence difference between Answer Shown-Neutral and Answer Hidden-Neutral) and CEO magnitude (overweighting ratio for opposing vs. supporting advice).\n\nGo/no-go: If a model shows CSB ≥+0.105 AND CEO overweighting ratio ≥1.29 (≥50% of Kumaran's reported effects), it proceeds. Models showing one bias are retained for single-bias characterization. Models showing neither are replaced (candidates: Gemma 3 27B, Mistral-8B).\n\n**Confidence Pathway Verification (end of Week 1, ~1 day per model):** Before committing to PANL-based extraction in Phase 0B, we verify that each target model caches confidence information at answer-adjacent positions. For each model: (a) train linear probes at the PANL position across all layers to identify where confidence-predictive information peaks, adapting Kumaran & Conmy's layer-sweep methodology; (b) perform attribution patching (Nanda et al., arXiv 2310.10348) — a gradient-based approximation of activation patching testing all candidate positions in a single backward pass — to confirm PANL activations causally influence confidence output; (c) apply LogitLens4LLMs (arXiv 2503.11667) to identify where confidence-relevant logits crystallize layer-by-layer. If a model caches confidence at a different structural position (e.g., last answer token rather than PANL), we adjust extraction positions for that model — the matched-content confound controls in Phase 0B remain valid regardless of extraction position. This uses the Phase 0A stimulus set (already generated), requiring only additional forward/backward passes (~4-8 GPU-hours per model). We report verified extraction positions and layer ranges for each model as part of contribution (5).\n\n**Phase 0B — Confound-Controlled De-Risking Pilot (Weeks 2–4):**\n\nWe allocate 3 weeks for Phase 0B to accommodate the expanded factorial design: stimulus generation with token-length matching and semantic neutrality validation (~1 week, the primary bottleneck as no published contrastive activation extraction study has attempted this level of confound control); activation extraction at verified positions across ~4000 pairs (~3-4 days); confound diagnostic battery and statistical analysis (~1 week); and iteration buffer if initial diagnostics partially fail (~3-4 days).\n\nThe translation from behavioral paradigm to contrastive activation extraction faces a critical confound: contrastive pairs differ not only in bias activation but in prompt information content. We address this with a four-pronged mitigation strategy:\n\n*(1) Matched-content contrastive pairs:*\n- **CSB pairs:** CSB-active: 'You previously answered [X].' CSB-control: plausible alternative answer of matched token length attributed to 'another LLM.' Additional 'scrambled-answer' control with token-length-matched neutral text.\n- **CEO pairs:** CEO-active: contradictory advice. CEO-control: irrelevant neutral advice of matched token length. Additional supporting-advice condition for directional validation.\n\n*(2) Same-content-different-attribution CSB control:* The model's OWN answer text attributed to 'another LLM,' creating a 2×2 factorial: {own text, other text} × {self-attributed, other-attributed}. The self-own vs. other-own contrast isolates pure ownership/attribution effects (the CSB core mechanism) while holding content exactly constant.\n\n*(3) Token-position-specific extraction:* Extraction at the positions verified in Phase 0A (PANL, CC, and first confidence token), targeting where bias-relevant confidence signals mechanistically concentrate rather than averaging across all positions.\n\n*(4) Confound diagnostic tests:* (a) Correlation with prompt token count <0.1; (b) prompt-structure probe cosine similarity <0.2 to candidate bias directions; (c) generalization to held-out question types; (d) CSB direction aligns more with attribution contrast than content contrast.\n\nPilot conducted on the strongest Phase 0A model with ~500 pairs per bias type per control condition (~4000 total across the full factorial).\n\nGo/no-go: Linear probe ≥60% balanced accuracy on matched-content pairs AND confound diagnostics pass → proceed. Accuracy 60%+ with partial diagnostic failure → expand extraction positions, apply mean-centering. Accuracy 55–60% with clean diagnostics → expand to 1000 pairs. Accuracy <55% or consistent diagnostic failure → activate behavioral-signal fallback (correlational rather than causal evidence, repositioning paper for EMNLP/NAACL).\n\n**Phase 1 — Separability Validation & Steerability Assessment (Weeks 5–9):**\n\n*Phase 1A — Separability (Weeks 5–7):* Scale confound-controlled extraction to all passing models with 2000+ matched-content pairs per bias type per model, extracting at verified positions. Validate separability via: (a) cosine similarity between directions (<0.3), (b) principal angle analysis, (c) PCA dimensionality, (d) cross-prediction ablations, (e) confound diagnostic replication at scale. Caveat (Patel et al., 2604.19974): separability does NOT guarantee functional relevance — Phase 1B is essential.\n\n*Phase 1B — Steerability Diagnostics (Weeks 7–9):* For each direction: (a) specificity ratio (Liu 2605.05715); (b) adapted LAP (Billa 2604.15557) along the verified PANL→CC pathway; (c) LEACE concept erasure; (d) pilot Spherical Steering test; (e) functional inertness test (Patel et al. methodology). Routing thresholds learned via validation-set sweeps. The core empirical hypothesis — CSB and CEO have asymmetric steerability profiles — would explain inconsistent monolithic steering results and hidden miscalibration regimes.\n\n**Phase 2 — Per-Instance Bias Diagnosis & Interference Prevalence Estimation (Weeks 8–11):**\n\nA lightweight logistic probe trained on per-instance projection magnitudes classifies which bias dominates per query. We stratify by difficulty and validate against behavioral predictions (CSB dominates on easy questions; CEO dominates under criticism on hard questions).\n\n**Interference Prevalence Estimation (new):** This analysis is central to the paper's practical impact framing. For each instance, we compute projection magnitudes onto CSB (p_CSB) and CEO (p_CEO) directions, then classify into four categories: (a) **CSB-dominant** — p_CSB above median, p_CEO below; (b) **CEO-dominant** — p_CEO above median, p_CSB below; (c) **Interference** — both above median with opposing confidence effects (biases partially cancel, producing deceptively low net error); (d) **Low-bias** — both below median. For interference instances, we estimate the 'cancellation magnitude' — how much gross miscalibration is hidden by opposing bias cancellation.\n\nBehavioral evidence suggests substantial interference prevalence: Kumaran et al.'s dual-active condition shows OUCS dropping from +0.210 to +0.086 (partial cancellation at condition level), and Kobalczyk & van der Schaar's worst-calibrated slices average 41% of instances in affected pairs. However, no per-instance prevalence estimate exists — making this analysis both necessary and itself a contribution.\n\nWe adopt conditional framing based on measured prevalence: (a) **>30% interference** → decomposed correction addresses a substantial practical subpopulation; emphasize calibration improvement as primary contribution alongside mechanistic characterization; (b) **15–30%** → moderate practical improvement; emphasize mechanistic characterization as primary with calibration gains as secondary; (c) **<15%** → paper's contribution is primarily mechanistic/interpretive (understanding WHY hidden miscalibration regimes exist), with practical gains limited to the interference subpopulation. Expected improvement on interference instances: decomposed correction should recover ~2×min(|p_CSB|, |p_CEO|) in gross miscalibration that monolithic methods conflate.\n\n**Phase 3 — Bias-Specific Intervention (Weeks 10–16):**\n\nBuilding on Billa's routing-by-steerability paradigm extended to per-instance competing biases, informed by 'Sycophancy Is Not One Thing's demonstration that decomposed sub-components can be independently steered:\n\n*Route A — Adaptive Spherical Steering (steerable directions):* Spherical Steering (You et al., ICML 2026) with MERA-inspired per-direction adaptive strength. Layer selection informed by adapted LAP profiles and the verified PANL→CC pathway.\n\n*Route B — Learned Nonlinear Residual Correction (entangled directions):* Bottleneck residual MLP per bias type (<0.1% parameters), with COAST-informed collateral-damage-aware training.\n\n*Route C — Selective Abstention (uncorrectable instances):* MERA's Hoeffding-based statistical framework when neither route improves calibration without >3% accuracy damage.\n\nPhase 3 results are interpreted conditional on Phase 2 interference prevalence: aggregate metrics (ECE, Brier) will reflect improvement proportional to interference prevalence × per-instance correction magnitude. We report both aggregate and interference-subpopulation-stratified metrics to disambiguate mechanistic success from practical impact.\n\n**Generalizability:** The Phase 0→3 pipeline is reusable for other competing-bias pairs: sycophantic agreement vs. truthfulness commitment (opposing training objectives), primacy vs. recency bias (opposing positional effects shifting with context usage, arXiv 2508.07479), and anchoring vs. evidence updating in multi-turn reasoning. We discuss these as future work.\n\n**Fallback Path:** If Phase 0B fails despite matched-content controls and attribution factorial, the behavioral-signal-guided fallback produces correlational rather than causal evidence — still informative but repositioned for EMNLP/NAACL rather than ICLR.\n\nWe evaluate on TriviaQA, MMLU, and PopQA across Gemma 4 31B Dense, Qwen3-8B, and Llama-3.1-8B-Instruct (subject to Phase 0A replication). Metrics: ECE, Brier score, AUROC, difficulty-stratified ECE, per-direction specificity and LAP profiles, interference prevalence and cancellation magnitude, collateral damage, route distribution. Core baselines: (1) temperature scaling, (2) CORAL, (3) Miao & Ungar adaptive steering, (4) MERA monolithic, (5) monolithic Spherical Steering, (6) monolithic nonlinear MLP, (7) SteerConf prompt-level steering. Extended baselines in supplementary: CogBias-style family-level steering, CCPS perturbation-stability probing.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "675-925 H100",
      "timeline": "17-21 weeks (includes 1-week behavioral replication with pathway verification + 3-week pilot with expanded factorial)",
      "estimated_gpu_cost": "$1,688-$2,313 (H100 @ ~$2.50/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "575-775 H100",
      "timeline": "13-17 weeks (includes 1-week behavioral replication with pathway verification + 3-week pilot with expanded factorial)",
      "claude_api_cost": "$400-$600 (Sonnet 4.6 for matched-content and attribution-factorial contrastive dataset generation, confound diagnostics, probing, LAP computation, adapter training, analysis)",
      "estimated_gpu_cost": "$1,438-$1,938"
    },
    "auto_research": {
      "gpu_hours": "875-1175 H100",
      "timeline": "8-12 weeks (includes behavioral replication with pathway verification + pilot)",
      "claude_api_cost": "$750-$1,275 (Opus 4.7 for experiment orchestration, matched-content and attribution-factorial pair generation, confound analysis, validation analysis, steerability diagnostics, adapter training sweeps)",
      "estimated_gpu_cost": "$2,188-$2,938",
      "speed_bottleneck": "Phase 0A behavioral replication + pathway verification (1 week, parallelizable across 3 models) → Phase 0B pilot is sequential gate (3 weeks, expanded for attribution factorial + confound diagnostics). Phase 1A→1B is sequential. Evaluation across 3 models × 3 datasets × 3 routes + 7 baselines is parallelizable."
    }
  },
  "target_venues": [
    "ICLR 2027 (estimated deadline ~Sep 24, 2026 — primary target, ~18 weeks from start date of May 19; human-in-loop timeline of 13-17 weeks requires aggressive parallel writing of introduction, related work, and methodology starting at Phase 1 (week 5). At 13-week execution: ~5 weeks for results writing — comfortable. At 17-week execution: ~1 week for final results integration — very tight, feasible only with substantial sections pre-written. Honest assessment: feasible at the shorter timeline bound with disciplined parallel writing; risky at the upper bound.)",
    "NeurIPS 2026 Workshops (~Aug 29, 2026 — Phase 0 + Phase 1 results as standalone contribution on competing bias geometry with confound-controlled methodology and interference prevalence estimation)",
    "ARR October 2026 cycle (Oct 12, 2026 — backup full paper targeting NAACL 2027 or EACL 2027; comfortable timeline)",
    "EMNLP 2027 (if Phase 0 fallback activated — correlational contribution repositioned for empirical venue)"
  ],
  "level": "top-tier",
  "key_references": [
    "Competing Biases underlie Overconfidence and Underconfidence in LLMs (Kumaran et al., Nature Machine Intelligence 2026; arXiv 2507.03120)",
    "How do LLMs Compute Verbal Confidence (Kumaran, Conmy et al., arXiv 2603.17839, March 2026) — confidence cached at PANL position, answer→PANL→CC information flow, token log-probs explain only 8.4% of variance",
    "CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models (Huang et al., arXiv 2604.01366, April 2026) — linearly separable bias directions, family-dependent mitigation, 26-32% steering reduction",
    "Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs (Vennemeyer et al., arXiv 2509.21305, submitted ICLR 2026) — decomposition of sycophancy into independently steerable sub-components via difference-in-means",
    "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders (Patel et al., arXiv 2604.19974, April 2026) — pure incorrectness features functionally inert, SAE-based classification-correction gap confirmation",
    "Calibrating LLM Confidence by Probing Perturbed Representation Stability (Khanmohammadi et al., arXiv 2505.21772, EMNLP 2025) — CCPS, ~55% ECE reduction via perturbation-stability probing on Llama/Qwen/Mistral 8B-32B",
    "Predicting Where Steering Vectors Succeed (Billa, arXiv 2604.15557, April 2026) — three-regime steerability framework, LAP diagnostic, routing-by-steerability paradigm",
    "SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., arXiv 2503.02863, NeurIPS 2025) — prompt-level confidence steering, 29% AUROC increase, 16% ECE reduction",
    "Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, arXiv 2603.25052, 2026) — orthogonal calibration/confidence encoding, adaptive steering",
    "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes (Liu, arXiv 2605.05715, May 2026) — classification-correction gap, specificity ratio diagnostic",
    "To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models (Hedström et al., ICML 2025; arXiv 2510.13290) — MERA: adaptive strength, provable non-degradation, selective abstention",
    "Discovery of Hidden Miscalibration Regimes (Kobalczyk & van der Schaar, arXiv 2605.13484, May 2026) — input-dependent calibration heterogeneity, opposing errors cancel when aggregated, worst-calibrated slices average 41% of instances",
    "Cross-Family Universality of Behavioral Axes in Language Models (arXiv 2605.09875, May 2026) — behavioral axes align at AUROC 0.95 across Llama-Qwen-Mistral-Phi, transferable directions from 2 source models",
    "Task Schema and Binding: A Double Dissociation Across Transformer Families (arXiv 2512.17325, 2025) — task schemas transfer at 100% via late MLP patching across 9 models from 7 families",
    "LogitLens4LLMs: Extending Logit Lens to Modern Architectures (arXiv 2503.11667, 2025) — practical tool for layer-by-layer confidence crystallization analysis",
    "Attribution Patching: Activation Patching At Industrial Scale (Nanda et al., arXiv 2310.10348, 2023) — gradient-based approximation of activation patching for efficient causal verification",
    "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (Chen et al., ICLR 2026; arXiv 2602.17560)",
    "Curveball Steering: The Right Direction To Steer Isn't Always Linear (Raval et al., arXiv 2603.09313, Mar 2026)",
    "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (arXiv 2605.05892, May 2026) — FLAS",
    "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs (arXiv 2604.01457, 2026)",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., ICML 2026; arXiv 2602.08169)",
    "Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection (Dang & Ngo, arXiv 2601.19375, Jan 2026)",
    "Minimizing Collateral Damage in Activation Steering (Nguyen et al., arXiv 2605.01167, May 2026) — COAST framework",
    "Where to Steer: Input-Dependent Layer Selection for Steering Improves LLM Alignment (Gadgil et al., arXiv 2604.03867, April 2026)",
    "Steered LLM Activations are Non-Surjective (Mishra et al., arXiv 2604.09839, 2026)",
    "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models (arXiv 2602.08159, 2026)",
    "LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components (Tsujimura & Tagade, arXiv 2508.17182, 2025)",
    "A Sober Look at Steering Vectors for LLMs (Tan et al., NeurIPS 2024)",
    "Patterns and Mechanisms of Contrastive Activation Engineering (Hao et al., arXiv 2505.03189, 2025)",
    "CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022, 2026)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025)",
    "Calibrating Verbalized Confidence with Self-Generated Distractors (Wang & Stengel-Eskin, ICLR 2026)",
    "Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (arXiv 2509.03647, 2025)",
    "Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation (Zhuang et al., arXiv 2512.03082, 2025)",
    "Fine-Grained Activation Steering: Steering Less, Achieving More (arXiv 2602.04428, 2026)",
    "Contextual Linear Activation Steering of Language Models (arXiv 2604.24693, 2026)",
    "Positional Biases Shift as Inputs Approach Context Window Limits (arXiv 2508.07479, 2025) — primacy vs. recency bias dynamics"
  ],
  "description": "We investigate whether two competing sources of LLM miscalibration — choice-supportive bias (CSB) and contradictory-evidence overweighting (CEO), identified behaviorally by Kumaran et al. (Nature MI 2026) — produce distinguishable activation signatures, exhibit asymmetric steerability profiles, and can be corrected through bias-specific intervention that outperforms monolithic approaches. A central empirical question — what fraction of instances exhibit genuine CSB-CEO interference (partial cancellation) — determines whether the practical impact is substantial or the contribution is primarily mechanistic.\n\nOur work targets the bias interference problem: CSB and CEO are simultaneously active on the same instances, pulling confidence in opposite directions, creating illusory calibration where biases partially cancel (consistent with hidden miscalibration regimes where worst-calibrated slices average 41% of instances, Kobalczyk & van der Schaar 2605.13484) and heterogeneous over/under-confidence where one bias dominates instance-by-instance.\n\nCogBias (2604.01366) established family-dependent bias mitigation for independently-active biases; 'Sycophancy Is Not One Thing' (2509.21305) demonstrated decompose-then-steer for co-aligned sub-components; Billa (2604.15557) established routing-by-steerability; SteerConf (NeurIPS 2025) proved calibration is steerable at the prompt level; Liu (2605.05715) and Patel et al. (2604.19974) established the classification-correction gap. We extend these paradigms to the strictly harder case of opposing biases creating destructive interference.\n\nPhase 0A (Week 1) replicates Kumaran et al.'s behavioral paradigm on Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma 4 31B Dense, and verifies confidence computation pathways for each model via attribution patching (arXiv 2310.10348) and linear probing at PANL positions — ensuring extraction targets mechanistically validated positions rather than assuming cross-architecture transferability of Kumaran & Conmy's (2603.17839) Gemma 3-specific layer ranges. Phase 0B (Weeks 2–4, extended to 3 weeks for the expanded factorial) conducts confound-controlled contrastive extraction with matched-content pairs, a 2×2 source-attribution factorial isolating CSB's ownership mechanism, position-specific extraction at verified positions, and confound diagnostics. Phase 1 validates separability and measures steerability with complementary diagnostics (specificity ratio, adapted LAP, functional inertness test). Phase 2 trains per-instance bias dominance classifiers and — critically — estimates interference prevalence by classifying instances into CSB-dominant, CEO-dominant, interference (both active, opposing), and low-bias categories, with conditional framing: >30% interference → strong practical impact; 15–30% → primarily mechanistic with moderate practical gains; <15% → primarily interpretive. Phase 3 implements bias-specific routing (Spherical Steering / nonlinear MLP / abstention), with results interpreted both in aggregate and stratified by interference prevalence.\n\nCore baselines: temperature scaling, CORAL, Miao & Ungar, MERA monolithic, monolithic Spherical Steering, monolithic nonlinear MLP, SteerConf. Extended: CCPS, CogBias-style steering.\n\nContributions: (1) first causal activation-level characterization of simultaneously competing calibration biases with confound-controlled extraction and architecture-specific pathway verification; (2) asymmetric steerability profiles with complementary diagnostics; (3) interference prevalence quantification connecting competing biases to hidden miscalibration regimes; (4) bias-specific adaptive correction with steerability-informed routing; (5) cross-architecture behavioral replication and confidence pathway verification on Llama and Qwen families; (6) conditional impact framing establishing whether decomposed calibration correction yields substantial practical improvement or primarily mechanistic insight.",
  "project_name": "competing_bias_steer",
  "source": "web_research",
  "revision_notes": {
    "round1_issue_1_missing_competitor": "Tsujimura & Tagade (2508.17182) cited and differentiated. [Carried from R1]",
    "round1_issue_2_model_names": "Fixed. [Carried from R1]",
    "round1_issue_3_untested_assumption": "Phase 1A separability tests with thresholds; preceded by Phase 0A+0B. [Carried from R1]",
    "round1_issue_4_steering_reliability": "Spherical Steering + MERA adaptive strength. [Carried from R1]",
    "round1_issue_5_baseline_comparison": "MERA as critical baseline. [Carried from R1]",
    "round1_issue_6_behavioral_mechanistic_leap": "Phase 0B pilot addresses this risk. [Carried from R1]",
    "round2_issue_1_critical_missing_competitor": "Liu (2605.05715) integrated. [Carried from R2]",
    "round2_issue_2_separability_steerability_gap": "Phase 1A + 1B. [Carried from R2]",
    "round2_issue_3_minor_missing_references": "All retained. [Carried from R2]",
    "round2_issue_4_nonlinear_steering_fallback": "Routes A/B/C. [Carried from R2]",
    "round3_issue_1_MERA_baseline": "MERA integration. [Carried from R3]",
    "round3_issue_2_nonlinear_steering_competitors": "ODESteer, Curveball, FLAS. [Carried from R3]",
    "round3_issue_3_venue_targeting": "ICLR 2027 primary with honest timeline assessment. [Updated R9]",
    "round3_issue_4_specificity_thresholds": "Empirically-learned thresholds. [Carried from R3]",
    "round3_issue_5_overcomplexity": "Streamlined 3×3×3 + 7 baselines; prose tightened in R9 to address complexity bloat. [Updated R9]",
    "round4_issue_1_missing_steerability_routing": "Billa (2604.15557) integrated. [Carried from R4]",
    "round4_issue_2_missing_cogbias": "CogBias integrated. [Carried from R4]",
    "round4_issue_3_novelty_overstated": "Novelty claims properly scoped. [Carried from R4]",
    "round4_issue_4_phase1a_risk": "Phase 0 pilot with confound controls. [Carried from R4]",
    "round4_additional_hidden_miscalibration": "Kobalczyk & van der Schaar, W2S. [Carried from R4]",
    "round5_issue_1_prompt_content_confound": "Matched-content pairs, attribution factorial, confound diagnostics. [Carried from R5/R7]",
    "round5_issue_2_cross_model_behavioral_generalization": "Phase 0A behavioral replication. [Carried from R5]",
    "round5_issue_3_fallback_is_weaker_project": "Explicit scope reduction for fallback. [Carried from R5]",
    "round5_issue_4_missing_baseline_steerconf": "SteerConf integrated as 7th core baseline. [Carried from R5]",
    "round5_issue_5_arr_date_correction": "ARR October 2026 = Oct 12. [Carried from R5]",
    "round7_issue_1_verbal_confidence_mechanism": "Kumaran & Conmy (2603.17839) integrated throughout. [Carried from R7]",
    "round7_issue_2_source_attribution_confound": "2×2 attribution factorial in Phase 0B. [Carried from R7]",
    "round7_issue_3_CCPS_missing": "CCPS integrated. [Carried from R7]",
    "round7_issue_4_generalizability": "Generalizability section with 3 competing-bias pairs. [Carried from R7]",
    "round7_issue_5_sycophancy_decomposition": "'Sycophancy Is Not One Thing' integrated throughout. [Carried from R7]",
    "round7_issue_6_SAE_functional_dissociation": "Patel et al. (2604.19974) integrated. [Carried from R7]",
    "round7_issue_7_cogbias_accuracy_verification": "CogBias claims scoped to abstract-verifiable figures. [Carried from R7]",
    "round8_issue_1_phase0b_timeline": "ADDRESSED: Extended Phase 0B from 2 weeks to 3 weeks with honest breakdown (stimulus generation ~1 week bottleneck, extraction ~3-4 days, diagnostics ~1 week, iteration buffer ~3-4 days). Cascaded through all timelines: human-in-loop 12-16 → 13-17 weeks, manual 16-20 → 17-21 weeks, auto_research 7-11 → 8-12 weeks. Updated ICLR 2027 feasibility assessment: ~18 weeks available from May 19 to Sep 24; at 13-week execution → comfortable (5 weeks writing); at 17-week execution → very tight (1 week for final integration), feasible only with aggressive parallel writing starting at Phase 1. Transparent that ICLR 2027 is achievable at the shorter bound but risky at the upper bound.",
    "round8_issue_2_pathway_verification": "ADDRESSED: Added 'Confidence Pathway Verification' sub-step at end of Phase 0A (~1 day per model, ~4-8 GPU-hours). Three complementary methods: (a) linear probes at PANL across all layers (adapting Kumaran & Conmy's layer-sweep), (b) attribution patching (Nanda et al., arXiv 2310.10348) for causal confirmation in a single backward pass, (c) LogitLens4LLMs (arXiv 2503.11667) for layer-by-layer confidence crystallization. If a model caches confidence at a different position, extraction positions adjusted accordingly. Grounded in cross-architecture evidence: behavioral axes align at AUROC 0.95 across Llama-Qwen-Mistral-Phi (arXiv 2605.09875), task schemas transfer at 100% across 7 families (arXiv 2512.17325) — supporting qualitative transferability while acknowledging architecture-specific layer ranges require verification. Added 4 new references: 2605.09875, 2512.17325, 2503.11667, 2310.10348.",
    "round8_issue_3_interference_prevalence": "ADDRESSED: Added dedicated 'Interference Prevalence Estimation' analysis in Phase 2. Methodology: project each instance onto CSB and CEO directions, classify into 4 categories (CSB-dominant, CEO-dominant, interference with partial cancellation, low-bias), compute prevalence and cancellation magnitude. Grounded in existing evidence: Kumaran et al.'s OUCS drops from +0.210 to +0.086 in dual-active condition (condition-level cancellation); Kobalczyk's worst-calibrated slices average 41% of instances (regime-level heterogeneity). Adopted conditional framing: >30% interference → strong practical impact framing; 15-30% → primarily mechanistic; <15% → primarily interpretive. Phase 3 results reported both aggregate and interference-stratified. This analysis is itself a contribution: first per-instance quantification of competing-bias interference prevalence, connecting behavioral evidence to hidden miscalibration regimes.",
    "round9_complexity_tightening": "MAJOR: Tightened prose throughout to address complexity bloat identified via stagnation analysis (scores declining 3.8→3.5 despite positive qualitative feedback). Compressed fallback section, generalizability section, and verbose cross-references. Removed redundant hedging. Net text reduced despite 3 substantive additions. Research on successful papers in the space (ITI/ICLR 2024, CAA/ACL 2024, CAST spotlight/ICLR 2025, 'Sycophancy Is Not One Thing') confirms that focused designs with one core claim outperform complex multi-phase proposals — the interference prevalence conditional framing helps focus the contribution claim."
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

### Round 3 review
Verdict: revise
Issues: ["MISSING CRITICAL BASELINE: MERA ('To Steer or Not to Steer?', Hedström et al., ICML 2025, arXiv 2510.13290) implements selective steering with adaptive strength and abstention — directly overlapping with Routes C and D. MERA optimizes intervention direction AND calibrates when/how much to steer, with provable non-degradation guarantees. It can be applied ON TOP of existing steering methods. This must be cited as a baseline and distinguished from: DBS-v2 decomposes biases while MERA treats errors monolithically; DBS-v2 routes between intervention types while MERA modulates a single intervention's strength.", "MISSING NONLINEAR STEERING COMPETITORS: The landscape fails to cite (a) Curveball Steering (arXiv 2603.09313, March 2026) — polynomial kernel PCA-based nonlinear steering that explicitly addresses geometric distortion in activation spaces, directly relevant to the linear vs. nonlinear routing rationale; (b) FLAS (arXiv 2605.05892, May 2026) — flow-based activation steering learning concept-conditioned velocity fields, first method to outperform prompting on AxBench; (c) ODESteer (arXiv 2602.17560, ICLR 2026) — ODE-based multi-step adaptive steering with barrier functions. These represent the rapidly maturing nonlinear steering landscape that Route B must be positioned against.", "AAAI 2027 PRIMARY TARGET IS INFEASIBLE: The full paper deadline is July 28, 2026 — approximately 10 weeks from now. The manual timeline estimate is 16-20 weeks. Even the auto_research timeline (6-10 weeks) is at the edge, and auto_research is the most expensive mode. No honest accounting of Phase 1A→1B sequential dependency, model access setup time, or writing time supports AAAI 2027 as 'primary target.' ARR August 2026 (Aug 3) is similarly tight. Realistic primary target should be ICLR 2027 or NeurIPS 2026 workshop for Phase 1 results.", "SPECIFICITY RATIO THRESHOLDS ARE WEAKLY JUSTIFIED: The proposed routing thresholds (≥0.5 HIGH, 0.2-0.5 MEDIUM, <0.2 LOW) are interpolated from exactly two empirical data points in Liu (2605.05715): overthinking at ≤0.152 (LOW, linear steering fails) and refusal at ~0.999 (HIGH, linear steering succeeds). There is no empirical or theoretical basis for the 0.2 and 0.5 boundaries. These thresholds should be explicitly framed as initial hypotheses to be refined during Phase 1B rather than as calibrated routing criteria.", "OVERCOMPLEXITY RISK: The proposal includes 4 intervention routes, 5 models (3 primary + 2 supplementary), 4 datasets, 10+ baselines, Phase 1A with 5 separability tests, Phase 1B with 4 steerability diagnostics, 2 alternative norm-preserving methods to ablate, and COAST-informed loss weighting. This is an enormous experimental matrix that risks under-execution. Consider scoping to 2-3 models and 2 routes (linear + nonlinear with abstention) for the primary paper, with the full matrix as supplementary."]
Feedback: The revision from round 2 is strong — the integration of Liu (2605.05715) and the decodable-steerable distinction is thorough and genuine. Three concrete fixes for round 4: (1) Cite MERA (ICML 2025) as a key baseline — it's the closest existing work on selective steering + abstention, and failing to cite a published ICML paper implementing core components of your Route C/D would be a serious oversight for reviewers. Distinguish DBS-v2 by emphasizing the multi-bias decomposition and steerability-based routing that MERA lacks. (2) Add Curveball Steering, FLAS, and ODESteer to the landscape — these are the 2026 nonlinear steering methods your Route B competes against. Position Route B's bottleneck MLP as motivated by Liu's calibration-specific finding, while acknowledging these general-purpose alternatives. (3) Revise venue targeting: drop AAAI 2027 as primary (the math doesn't work). Make ICLR 2027 (~Oct 2026) the primary target, NeurIPS 2026 workshop (Aug 29) for Phase 1 results, and ARR cycle for full paper backup. (4) Explicitly frame specificity ratio thresholds as hypotheses, not established boundaries. (5) Consider streamlining the experimental matrix — 5 models × 4 routes × 10+ baselines may impress but also signals unfocused ambition to reviewers.

### Round 4 review
Verdict: revise
Issues: ["MISSING REFERENCE: 'Predicting Where Steering Vectors Succeed' (arXiv 2604.15557, April 2026) proposes a three-regime framework — (1) concept not represented (no method works), (2) nonlinear encoding (nonlinear methods needed), (3) output-aligned (linear steering works) — that directly parallels DBS-v2's Route C/Route B/Route A routing. The paper uses Linear Accessibility Profile (LAP) as a training-free steerability diagnostic (ρ=0.86-0.91 correlation with steering effectiveness), which is conceptually adjacent to Liu's specificity ratio and Phase 1B's steerability assessment. This must be cited and distinguished from. Key distinction: 2604.15557 operates per-concept/per-layer with synthetic binary concepts, not per-instance with naturalistic calibration biases; it doesn't decompose biases. But it establishes the routing-by-steerability paradigm that DBS-v2 claims as novel.", "MISSING REFERENCE: CogBias (arXiv 2604.01366, April 2026) decomposes cognitive biases into four families (Judgment, Information Processing, Social, Response), finds them linearly separable in activation space (97.8% classification accuracy), and demonstrates family-dependent mitigation — 'prompt-level debiasing substantially reduces Response biases but backfires for Judgment biases.' This is the closest existing work to the 'different biases need different interventions' principle underlying DBS-v2. Must be cited alongside Tsujimura & Tagade. Key distinction: CogBias addresses cognitive biases broadly, not calibration-specific competing biases; its interventions are not steerability-aware.", "NOVELTY CLAIM OVERSTATED: With CogBias demonstrating bias-family-specific intervention, 2604.15557 demonstrating three-regime steerability routing, and MERA demonstrating adaptive steering + abstention, the claim of being 'first to jointly decompose + route' needs significant qualification. The novelty is more precisely: first to apply bias-grounded decomposition to competing calibration biases (CSB/CEO) specifically, with per-direction steerability assessment — not first to route interventions by steerability regime or to decompose biases for differential treatment.", "PHASE 1A RISK STILL UNDERSPECIFIED: The contingency plan (SAE-based features + subspace projection classifier) if CSB/CEO are not separable adds significant complexity and is not well-developed. What if the contrastive stimuli themselves don't reliably elicit the target biases in a controlled way? The behavioral phenomena in Kumaran et al. were observed in multi-turn conversational setups with specific confidence elicitation protocols — translating this to a contrastive activation extraction paradigm is non-trivial and could easily produce noisy or confounded directions."]
Feedback: The revision from round 3 is strong — MERA integration, nonlinear steering landscape, venue corrections, threshold reframing, and experimental streamlining are all well-executed. Two concrete fixes for round 5: (1) Cite 'Predicting Where Steering Vectors Succeed' (2604.15557) as a key methodological predecessor for the routing logic. Its three-regime framework (no representation / nonlinear / output-aligned) directly parallels Routes C/B/A. Distinguish DBS-v2 by emphasizing that your routing operates per-instance with naturalistic competing biases, not per-concept with synthetic binary features, and that your steerability assessment is grounded in bias-specific specificity ratios rather than general logit-lens accessibility. Consider whether LAP could complement the specificity ratio as an additional diagnostic in Phase 1B. (2) Cite CogBias (2604.01366) alongside Tsujimura & Tagade as showing that bias-family-specific intervention is viable and that different bias types respond differently to interventions — this actually strengthens your motivation (the principle works for cognitive biases broadly; you apply it to the specific competing-bias calibration problem). (3) Tighten the novelty framing: the contribution is NOT 'first to route interventions by steerability' (2604.15557 does this) or 'first to decompose biases for differential treatment' (CogBias does this). The contribution IS: first to identify competing calibration biases (CSB vs. CEO) in activation space, measure their asymmetric steerability profiles, and apply bias-specific correction with non-degradation guarantees. This is still a meaningful contribution if Phase 1A succeeds.

### Round 5 review
Verdict: revise
Issues: ["PHASE 0 PROMPT-CONTENT CONFOUND: The contrastive extraction methodology has an unaddressed confound. For CSB: contrasting 'answer shown' vs. 'answer hidden' prompts differ not only in bias activation but in information content (one prompt literally contains more text — the model's own answer). For CEO: contrasting 'contradictory advice present' vs. 'absent' prompts differ in the presence of additional advisory text. The extracted direction may capture 'prompt contains additional evaluative content' rather than 'bias is active.' This is distinct from the behavioral-to-mechanistic gap already acknowledged and requires explicit mitigation: matched-length prompts with semantically neutral filler, attention-weighted extraction focusing on confidence-bearing tokens rather than global mean, or information-theoretic controls. Without this, Phase 0 success (>60% probe accuracy) may reflect prompt-content confounds rather than genuine bias detection.", "CROSS-MODEL BEHAVIORAL GENERALIZATION UNADDRESSED: Kumaran et al.'s competing biases were characterized on Gemma 3, GPT-4o, and o1-preview. Phase 0 pilot uses Llama-3.1-8B-Instruct — a model not in the original study. The full evaluation uses Gemma 4 31B Dense (different from Gemma 3) and Qwen3-8B. The behavioral phenomena (CSB magnitude, CEO overweighting ratio) may differ substantially or not replicate across these architectures. The proposal should explicitly plan to verify behavioral replication on each target model before assuming the contrastive paradigm applies.", "PHASE 0 FALLBACK PATH IS A DIFFERENT (WEAKER) PROJECT: The proposal states that if probing accuracy is <55%, it will 'pivot to behavioral-signal-guided probing: use model output changes to label instances post-hoc, then probe for internal signatures correlated with these behavioral labels.' This fallback trades causal contrastive evidence for correlational association, fundamentally weakening contribution (1) from 'first causal activation-level characterization' to 'statistical association between behavioral labels and activations.' The proposal should be more explicit that this fallback, while still informative, would require repositioning the paper's claims and likely reduces it from a top-tier to a solid contribution.", "MISSING BASELINE: SteerConf (Zhou et al., arXiv 2503.02863, NeurIPS 2025) applies steering-based confidence calibration without training, achieving 29% AUROC increase and 16% ECE reduction across 7 benchmarks. While it operates at the prompt level (not activation level), it is a published NeurIPS paper directly addressing confidence calibration via steering and should be acknowledged in the landscape and considered as a baseline — it represents the 'prompt-level steering' approach that activation-level methods should outperform.", "MINOR: ARR October 2026 deadline is October 12, not '~Oct 15' as stated."]
Feedback: This is a well-crafted proposal after 4 strong revision rounds. All references verified, the gap is genuine, and the novelty claims are now properly scoped. Three concrete improvements for round 6: (1) Address the prompt-content confound in Phase 0 explicitly — design contrastive pairs that control for information content differences (e.g., matched-length prompts where 'answer hidden' condition replaces the answer with a semantically neutral placeholder of equal length, and 'advice absent' condition replaces contradictory advice with irrelevant neutral text). This is the most important fix because it determines whether Phase 0 measures bias activation or prompt structure. (2) Add a 'behavioral replication' step at the start of Phase 0: before extracting activations, verify that each target model exhibits both CSB and CEO in Kumaran et al.'s behavioral paradigm. If CSB/CEO magnitudes are <50% of Kumaran's reported effect sizes on a given model, flag that model as potentially unsuitable. (3) Be honest about the fallback path: explicitly state that the behavioral-signal-guided probing fallback would change the paper's contribution from causal mechanistic evidence to correlational analysis, and discuss what venue/framing would be appropriate for that weaker result. Also add SteerConf as a landscape reference and fix the ARR date.

### Round 6 review
Verdict: revise
Issues: ["MISSING REFERENCE: 'How do LLMs Compute Verbal Confidence' (arXiv 2603.17839, March 2026) provides mechanistic evidence that confidence representations are cached at answer-adjacent positions and retrieved at verbalization sites, with confidence being gathered from answer tokens. This directly informs Phase 0B's token-position-specific extraction methodology — the 'confidence-bearing token position' that the proposal identifies as a key extraction point is studied mechanistically in this paper. Citing it would both strengthen the extraction strategy and demonstrate awareness of where confidence signals actually reside.", "SOURCE ATTRIBUTION CONFOUND IN MATCHED-CONTENT CSB PAIRS: The Phase 0B design for CSB replaces the model's own answer with 'a plausible but randomly-selected alternative answer attributed to another LLM.' However, this introduces a source attribution confound: the model may process 'my answer' vs. 'another LLM's answer' differently beyond bias activation — e.g., models may have learned to attend differently to self-generated vs. externally-attributed content. The 'scrambled-answer' control partially addresses this, but the primary contrast still confounds CSB with source attribution. Consider adding a condition where the model's own answer is presented but attributed to 'another LLM' (same content, different attribution) to isolate the self-generated aspect of CSB from the information-content aspect.", "MISSING LANDSCAPE REFERENCE: CCPS (arXiv 2505.21772, EMNLP 2025) achieves ~55% ECE reduction and 21% Brier score improvement via perturbation-stability probing across 8B-32B models (Llama, Qwen, Mistral). While a different paradigm (perturbation-based rather than steering), it's a recent published calibration method evaluated on overlapping model families and benchmarks. Should be mentioned in the landscape and considered as an extended baseline.", "IMPACT NARROWNESS AND GENERALIZABILITY: The paper should explicitly discuss whether the competing-bias framework generalizes beyond CSB/CEO. Are there other pairs of simultaneously competing biases in LLMs? What about sycophancy vs. truthfulness, or fluency vs. factuality? A brief discussion of generalizability would strengthen the impact argument and preempt reviewer concerns about the framework being overly specific to Kumaran's experimental paradigm."]
Feedback: This is a strong proposal after 5 rigorous revision rounds. All references verified, the gap is genuine, and the methodology is thoughtful. Three concrete improvements for round 7: (1) Cite 'How do LLMs Compute Verbal Confidence' (2603.17839) — its finding that confidence is cached at answer-adjacent tokens and retrieved at verbalization directly validates your token-position-specific extraction in Phase 0B, and its mechanistic analysis on Gemma 3 27B and Qwen 2.5 7B provides complementary evidence for your target model families. (2) Add one more CSB confound control: present the model's own answer but attributed to 'another LLM' — this isolates the self-generated attribution from the information content, making the CSB extraction strictly about ownership-bias rather than content-presence. This is a small addition (~500 more pairs) but substantially strengthens the causal claim. (3) Add a brief generalizability discussion: identify 2-3 other plausible competing-bias pairs (e.g., sycophancy vs. truthfulness, fluency pressure vs. factual constraint) and note that the framework's Phase 0→3 pipeline is reusable. This addresses the main impact concern without requiring additional experiments. Also add CCPS to the landscape. The proposal is very close to the pass threshold — these are all addressable in one revision round.

### Round 7 review
Verdict: revise
Issues: ["ALL FOUR ROUND 6 ISSUES UNADDRESSED: (1) 'How do LLMs Compute Verbal Confidence' (arXiv 2603.17839, March 2026) remains uncited despite directly validating the token-position-specific extraction in Phase 0B — it shows confidence is cached at answer-adjacent positions and retrieved at verbalization, studied on Gemma 3 27B and Qwen 2.5 7B. (2) The source attribution confound in CSB pairs is still not controlled: the requested control — presenting the model's OWN answer but attributed to 'another LLM' (same content, different attribution) — would isolate the self-generated ownership component of CSB from information-content differences. The current design changes BOTH content AND attribution simultaneously. (3) CCPS (arXiv 2505.21772, EMNLP 2025) remains uncited — it achieves ~55% ECE reduction via perturbation-stability probing on overlapping model families (Llama, Qwen, Mistral) at 8B-32B scale, making it a relevant landscape reference and potential extended baseline. (4) No generalizability discussion identifying other plausible competing-bias pairs.", "MISSING METHODOLOGICAL PRECEDENT: 'Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs' (arXiv 2509.21305, submitted ICLR 2026) decomposes sycophancy into distinct, independently steerable sub-components (sycophantic agreement vs. sycophantic praise vs. genuine agreement) using difference-in-means, activation additions, and subspace geometry — demonstrating that each can be independently amplified or suppressed without affecting others. This is the closest methodological precedent for decomposing a complex behavioral phenomenon into independently steerable activation-level components. The key distinction from this proposal: 'Sycophancy Is Not One Thing' decomposes co-existing but not opposing behaviors, while this proposal targets simultaneously OPPOSING biases that create interference. This distinction should be explicitly articulated.", "MISSING RELEVANT REFERENCE: 'Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders' (arXiv 2604.19974, April 2026) shows that statistically decodable features can be 'functionally inert' — pure incorrectness features have near-zero accuracy impact when suppressed despite being statistically distinguishable. This directly reinforces Liu's classification-correction gap with SAE-based evidence and implies that Phase 1A's separability success does NOT guarantee Phase 3's intervention success. Should be cited alongside Liu.", "UNVERIFIABLE CLAIM: The '97.8% mean classification accuracy via linear probes' attributed to CogBias (2604.01366) could not be independently confirmed from the abstract or accessible paper content. The abstract mentions linear separability and 26-32% steering reduction but does not surface this specific accuracy figure. If this number comes from the paper body, it should be noted as such; if it was inferred or estimated, it should be flagged."]
Feedback: This is a strong proposal after 6 rigorous revision rounds, but the complete failure to address ANY of the 4 round 6 issues is a significant concern. Concrete fixes for round 8: (1) Cite 'How do LLMs Compute Verbal Confidence' (2603.17839) — its mechanistic finding that confidence is cached at answer-adjacent positions directly validates your Phase 0B token-position extraction strategy. This is a 1-sentence addition that substantially strengthens your methodology. (2) Add the same-content-different-attribution CSB control: present the model's OWN answer text but attributed to 'another LLM.' This isolates the ownership component of CSB from information content and requires only ~500 additional pairs. Without it, a reviewer can argue your CSB direction captures 'recognizing my own output' rather than 'choice-supportive confidence inflation.' (3) Add CCPS to landscape and extended baselines. (4) Add a brief generalizability paragraph: identify 2-3 other competing-bias pairs (e.g., sycophantic agreement vs. truthfulness, fluency pressure vs. factual constraint — note 'Sycophancy Is Not One Thing' already shows these are separable) and state that the Phase 0→3 pipeline is reusable. (5) Cite 'Sycophancy Is Not One Thing' (2509.21305) as a key methodological precedent and distinguish it: that paper decomposes co-existing behaviors; yours targets opposing biases creating interference effects. (6) Cite 'Are LLM Uncertainty and Correctness Encoded by the Same Features?' (2604.19974) alongside Liu — it independently confirms that decodable ≠ functional via SAE analysis, strengthening your rationale for Phase 1B steerability assessment. (7) Verify the CogBias 97.8% figure or add a caveat. All of these are small, focused additions — the core architecture is sound.

### Round 8 review
Verdict: revise
Issues: ["PHASE 0B TIMELINE UNDERESTIMATED: The expanded Phase 0B design now includes ~4000 contrastive pairs across matched-content pairs, scrambled-answer controls, supporting-advice controls, AND the 2×2 attribution factorial ({own text, other text} × {self-attributed, other-attributed}), all requiring token-length matching and semantic neutrality — plus token-position-specific extraction at three positions per instance, confound diagnostic battery (prompt-structure probes, token-count correlations, attribution-alignment verification), and analysis on the strongest Phase 0A model. Two weeks is likely insufficient: stimulus generation alone (creating plausible alternative answers of matched token length, irrelevant neutral advice of matched length, attribution-varied conditions) requires careful prompt engineering and validation. Budget 3-4 weeks for Phase 0B, which cascades through the entire timeline and threatens the ICLR 2027 Sep 24 deadline.", "MODEL-SPECIFIC PANL→CC PATHWAY NOT VALIDATED: The token-position-specific extraction strategy is grounded in Kumaran & Conmy's mechanistic findings on Gemma 3 27B (layers 22-28 for PANL caching, 30-36 for CC retrieval) and verified on Qwen 2.5 7B. However, the target models are Gemma 4 31B Dense (different architecture, released April 2026), Qwen3-8B (different generation), and Llama-3.1-8B-Instruct (never studied for confidence computation). The PANL and CC token positions are structurally transferable, but the layer ranges where confidence caching and retrieval occur could differ substantially — especially for Llama, which has a different architecture family entirely. Phase 0B should include a preliminary confidence-pathway verification step for each target model (e.g., confirming via attention pattern analysis or activation patching that confidence information flows through answer-adjacent positions).", "IMPACT ARGUMENT NEEDS STRENGTHENING: The practical value proposition — that decomposed bias-specific correction outperforms monolithic methods — faces a quantitative challenge. Hidden miscalibration regimes (Kobalczyk & van der Schaar) represent input-dependent heterogeneity, but the proposal doesn't estimate what fraction of miscalibration instances involve genuine CSB-CEO interference (partial cancellation). If interference cases are only 10-20% of all miscalibrated instances, aggregate ECE/Brier improvements may be modest even with perfect decomposed correction. The proposal should include a Phase 2 analysis estimating the prevalence of interference-dominated instances and present expected improvement bounds conditional on interference prevalence."]
Feedback: This is an excellent proposal after 7 rigorous revision rounds — all round 7 issues were thoroughly addressed, all references verified as accurate, and the gap is genuine. Three targeted improvements for round 9: (1) Revise Phase 0B timeline to 3-4 weeks (acknowledging the attribution factorial adds ~500 pairs per condition and the confound diagnostic battery requires careful statistical analysis), and cascade the timeline impact to honest ICLR 2027 feasibility assessment — if this pushes the human-in-loop timeline to 14-18 weeks, be transparent that ICLR 2027 is feasible only with the shorter bound and aggressive parallel writing. (2) Add a brief 'confidence pathway verification' step at the start of Phase 0B or end of Phase 0A: for each target model, verify that confidence information flows through answer-adjacent positions (PANL→CC) using lightweight activation patching or attention analysis, before committing to the extraction positions. This is ~1 day of compute per model and prevents committing the entire Phase 0B pipeline to positions that may not be confidence-relevant in the target architecture. (3) In Phase 2, add an 'interference prevalence estimation' analysis: quantify what fraction of instances show substantial CSB-CEO partial cancellation (e.g., instances where both bias projections are above median magnitude but in opposing directions). This directly addresses the impact concern — if prevalence is high (>30%), the decomposed approach has clear practical value; if low (<15%), the paper's contribution is more interpretive than practical, and the framing should adjust accordingly.


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
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "type": "user",
  "uuid": "5bad7731-960a-428d-a9f4-6db6289b87b4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T16:37:20.035Z_

```json
{
  "parentUuid": "5bad7731-960a-428d-a9f4-6db6289b87b4",
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
  "uuid": "3bb1e383-bb05-4f0b-aca8-b3ae96ea07ef",
  "timestamp": "2026-05-19T16:37:20.035Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T16:37:20.035Z_

```json
{
  "parentUuid": "3bb1e383-bb05-4f0b-aca8-b3ae96ea07ef",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0fad6dca-2a32-4c8f-bd3f-d6bc3cbe2be5",
  "timestamp": "2026-05-19T16:37:20.035Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
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
  "leafUuid": "0fad6dca-2a32-4c8f-bd3f-d6bc3cbe2be5",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose competing calibration biases via activation steering",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Assistant

_source line 8 · 2026-05-19T16:37:25.215Z_

<details><summary>Logged reasoning block</summary>

```text
This is round 9/10 of reviewing a complex ML research proposal about decomposing LLM miscalibration into competing biases (CSB and CEO) and applying targeted activation correction. Let me conduct a thorough independent review.

Let me start by verifying the key claims and references, checking for missing competitors, and assessing the current state of the proposal after 8 rounds of revision.

Let me search for the key references and any new competing work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fad6dca-2a32-4c8f-bd3f-d6bc3cbe2be5",
  "isSidechain": false,
  "requestId": "req_011CbCFjavGfU9Xvy9JutDna",
  "type": "assistant",
  "uuid": "44856ac3-199b-4536-abb3-8c4d5374cd2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EbZgcAaoAsGC7sfNb2wFzg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23604,
      "cache_read_input_tokens": 11374,
      "output_tokens": 552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 552,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 23604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23604
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

_source line 9 · 2026-05-19T16:37:26.358Z_

I'll conduct a thorough independent review of this proposal. Let me start by verifying key claims, checking for missing competitors, and assessing the current SOTA across multiple dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44856ac3-199b-4536-abb3-8c4d5374cd2c",
  "isSidechain": false,
  "requestId": "req_011CbCFjavGfU9Xvy9JutDna",
  "type": "assistant",
  "uuid": "536e29f5-bb3b-493a-a2cc-dae22df84b83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EbZgcAaoAsGC7sfNb2wFzg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23604,
      "cache_read_input_tokens": 11374,
      "output_tokens": 552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 552,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 23604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23604
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

_source line 10 · 2026-05-19T16:37:34.175Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019KXn88ZaK1rYq83m2z9DYz`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Kumaran et al. references",
  "prompt": "Search the web to verify these two papers exist and check their claims:\n\n1. \"Competing Biases underlie Overconfidence and Underconfidence in LLMs\" by Kumaran et al. - claimed to be published in Nature Machine Intelligence 2026, with arXiv ID 2507.03120. Claims: CSB gives +0.21 confidence boost, CEO overweighting ratio 2.58 for opposing vs 1.095 for supporting advice, dual-active condition shows change-of-mind dropping from 85.0% to 39.2%.\n\n2. \"How do LLMs Compute Verbal Confidence\" by Kumaran, Conmy et al. - arXiv 2603.17839, March 2026. Claims: confidence cached at PANL (Post-Answer-Newline) position, information flow answer→PANL (layers 22-28)→CC (layers 30-36) in Gemma 3 27B, token log-probs explain only 8.4% of variance.\n\nFor each paper:\n- Search for the paper title and arXiv ID\n- Try to fetch the arXiv page to verify it exists\n- Check if the claimed venue (Nature MI) and claims match\n\nUse web search and web fetch tools. Report what you find concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "536e29f5-bb3b-493a-a2cc-dae22df84b83",
  "isSidechain": false,
  "requestId": "req_011CbCFjavGfU9Xvy9JutDna",
  "type": "assistant",
  "uuid": "601ceee6-621c-4c90-84c1-46e49781cc30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EbZgcAaoAsGC7sfNb2wFzg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23604,
      "cache_read_input_tokens": 11374,
      "output_tokens": 552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 552,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 23604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23604
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

_source line 11 · 2026-05-19T16:38:51.836Z_

<details><summary>↩ Tool result · `toolu_019KXn88ZaK1rYq83m2z9DYz`</summary>

```text
I now have enough information to give a comprehensive report. Here are my findings:

---

## Paper 1: "Competing Biases underlie Overconfidence and Underconfidence in LLMs"

**Existence: CONFIRMED**

- The arXiv preprint (ID 2507.03120) exists and was posted **July 3, 2025**. Its arXiv title is actually **"How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models"** -- this is different from the title you provided.
- The paper was subsequently published in **Nature Machine Intelligence** on **April 22, 2026** under the revised title **"Competing Biases underlie Overconfidence and Underconfidence in LLMs"** (DOI: s42256-026-01217-9). So the Nature MI venue claim is **correct**.
- Authors: Dharshan Kumaran et al. (Google DeepMind, UCL). **Correct.**

**Specific numerical claims:**

| Claim | Status |
|-------|--------|
| CSB gives +0.21 confidence boost | **CONFIRMED** -- The paper states "Shown coeff = 0.21; i.e. implying a +0.21 rise in confidence score when the initial answer was visible (p<0.001)" |
| CEO overweighting ratio 2.58 for opposing vs 1.095 for supporting advice | **CONFIRMED** -- Exact matches found in section 3.3 |
| Dual-active condition: change-of-mind dropping from 85.0% to 39.2% | **CONFIRMED but direction is reversed in your description** -- The paper reports 85.0% in the Answer Hidden-Opposite condition dropping to 39.2% in the Answer Shown-Opposite condition (i.e., showing the initial answer *reduces* change-of-mind from 85% to 39.2%). The numbers are correct; the "dual-active" terminology may be a paraphrase. |

---

## Paper 2: "How do LLMs Compute Verbal Confidence"

**Existence: CONFIRMED**

- arXiv ID 2603.17839 exists. Submitted **March 18, 2026** (v1), updated **March 31, 2026** (v2).
- Authors: Dharshan Kumaran, Arthur Conmy, Federico Barbero, Simon Osindero, Viorica Patraucean, Petar Velickovic. **Correct.**
- This is an arXiv preprint (no journal publication found yet).

**Specific numerical claims:**

| Claim | Status |
|-------|--------|
| Confidence cached at PANL (Post-Answer-Newline) position | **CONFIRMED** -- The paper explicitly identifies PANL as the caching location |
| Information flow answer -> PANL (layers 22-28) -> CC (layers 30-36) in Gemma 3 27B | **MOSTLY CONFIRMED** -- Answer-to-PANL attention blocking disruption at layers 22-28 is confirmed. PANL-to-CC effects peak at layers 30-35 in steering experiments and 30-36 in attention blocking. The 22-28 and 30-36 ranges are essentially correct. |
| Token log-probs explain only 8.4% of variance | **CONFIRMED EXACTLY** -- The paper reports r=0.29, R^2_CV=0.084 (8.4%) |

---

## Summary

Both papers are **real and verified**. All the specific numerical claims check out against the actual paper content. The only notable discrepancy is that the arXiv title of Paper 1 differs from the Nature MI published title (the arXiv title is longer and more descriptive; the Nature MI title is the shorter one you cited).

Sources:
- [arXiv 2507.03120](https://arxiv.org/abs/2507.03120)
- [Nature Machine Intelligence article](https://www.nature.com/articles/s42256-026-01217-9)
- [arXiv 2603.17839](https://arxiv.org/abs/2603.17839)
- [arXiv 2603.17839 HTML](https://arxiv.org/html/2603.17839v1)
- [TechXplore coverage](https://techxplore.com/news/2025-07-reveals-ai-confidence-problem.html)

agentId: abac1d0d91484ae82 (use SendMessage with to: 'abac1d0d91484ae82' to continue this agent)
&lt;usage>total_tokens: 18882
tool_uses: 13
duration_ms: 77653&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "601ceee6-621c-4c90-84c1-46e49781cc30",
  "isSidechain": false,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "type": "user",
  "uuid": "9beb6dfb-1640-4ffa-a470-d5494026b31e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify these two papers exist and check their claims:\n\n1. \"Competing Biases underlie Overconfidence and Underconfidence in LLMs\" by Kumaran et al. - claimed to be published in Nature Machine Intelligence 2026, with arXiv ID 2507.03120. Claims: CSB gives +0.21 confidence boost, CEO overweighting ratio 2.58 for opposing vs 1.095 for supporting advice, dual-active condition shows change-of-mind dropping from 85.0% to 39.2%.\n\n2. \"How do LLMs Compute Verbal Confidence\" by Kumaran, Conmy et al. - arXiv 2603.17839, March 2026. Claims: confidence cached at PANL (Post-Answer-Newline) position, information flow answer→PANL (layers 22-28)→CC (layers 30-36) in Gemma 3 27B, token log-probs explain only 8.4% of variance.\n\nFor each paper:\n- Search for the paper title and arXiv ID\n- Try to fetch the arXiv page to verify it exists\n- Check if the claimed venue (Nature MI) and claims match\n\nUse web search and web fetch tools. Report what you find concisely.",
    "agentId": "abac1d0d91484ae82",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have enough information to give a comprehensive report. Here are my findings:\n\n---\n\n## Paper 1: \"Competing Biases underlie Overconfidence and Underconfidence in LLMs\"\n\n**Existence: CONFIRMED**\n\n- The arXiv preprint (ID 2507.03120) exists and was posted **July 3, 2025**. Its arXiv title is actually **\"How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in Large Language Models\"** -- this is different from the title you provided.\n- The paper was subsequently published in **Nature Machine Intelligence** on **April 22, 2026** under the revised title **\"Competing Biases underlie Overconfidence and Underconfidence in LLMs\"** (DOI: s42256-026-01217-9). So the Nature MI venue claim is **correct**.\n- Authors: Dharshan Kumaran et al. (Google DeepMind, UCL). **Correct.**\n\n**Specific numerical claims:**\n\n| Claim | Status |\n|-------|--------|\n| CSB gives +0.21 confidence boost | **CONFIRMED** -- The paper states \"Shown coeff = 0.21; i.e. implying a +0.21 rise in confidence score when the initial answer was visible (p<0.001)\" |\n| CEO overweighting ratio 2.58 for opposing vs 1.095 for supporting advice | **CONFIRMED** -- Exact matches found in section 3.3 |\n| Dual-active condition: change-of-mind dropping from 85.0% to 39.2% | **CONFIRMED but direction is reversed in your description** -- The paper reports 85.0% in the Answer Hidden-Opposite condition dropping to 39.2% in the Answer Shown-Opposite condition (i.e., showing the initial answer *reduces* change-of-mind from 85% to 39.2%). The numbers are correct; the \"dual-active\" terminology may be a paraphrase. |\n\n---\n\n## Paper 2: \"How do LLMs Compute Verbal Confidence\"\n\n**Existence: CONFIRMED**\n\n- arXiv ID 2603.17839 exists. Submitted **March 18, 2026** (v1), updated **March 31, 2026** (v2).\n- Authors: Dharshan Kumaran, Arthur Conmy, Federico Barbero, Simon Osindero, Viorica Patraucean, Petar Velickovic. **Correct.**\n- This is an arXiv preprint (no journal publication found yet).\n\n**Specific numerical claims:**\n\n| Claim | Status |\n|-------|--------|\n| Confidence cached at PANL (Post-Answer-Newline) position | **CONFIRMED** -- The paper explicitly identifies PANL as the caching location |\n| Information flow answer -> PANL (layers 22-28) -> CC (layers 30-36) in Gemma 3 27B | **MOSTLY CONFIRMED** -- Answer-to-PANL attention blocking disruption at layers 22-28 is confirmed. PANL-to-CC effects peak at layers 30-35 in steering experiments and 30-36 in attention blocking. The 22-28 and 30-36 ranges are essentially correct. |\n| Token log-probs explain only 8.4% of variance | **CONFIRMED EXACTLY** -- The paper reports r=0.29, R^2_CV=0.084 (8.4%) |\n\n---\n\n## Summary\n\nBoth papers are **real and verified**. All the specific numerical claims check out against the actual paper content. The only notable discrepancy is that the arXiv title of Paper 1 differs from the Nature MI published title (the arXiv title is longer and more descriptive; the Nature MI title is the shorter one you cited).\n\nSources:\n- [arXiv 2507.03120](https://arxiv.org/abs/2507.03120)\n- [Nature Machine Intelligence article](https://www.nature.com/articles/s42256-026-01217-9)\n- [arXiv 2603.17839](https://arxiv.org/abs/2603.17839)\n- [arXiv 2603.17839 HTML](https://arxiv.org/html/2603.17839v1)\n- [TechXplore coverage](https://techxplore.com/news/2025-07-reveals-ai-confidence-problem.html)"
      }
    ],
    "totalDurationMs": 77653,
    "totalTokens": 18882,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 17402,
      "output_tokens": 1069,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 410
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1069,
          "cache_read_input_tokens": 17402,
          "cache_creation_input_tokens": 410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 410,
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
  "sourceToolAssistantUUID": "601ceee6-621c-4c90-84c1-46e49781cc30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T16:39:02.746Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MC4n5sGE67n4MPXy1rWh1F`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify key 2026 references batch 1",
  "prompt": "Search the web to verify these papers exist and check key claims. For each, search for the title and arXiv ID, and try to access the arXiv page.\n\n1. \"CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models\" - arXiv 2604.01366, April 2026. Claims: linearly separable bias directions, family-dependent mitigation, 26-32% steering reduction.\n\n2. \"Predicting Where Steering Vectors Succeed\" (Billa) - arXiv 2604.15557, April 2026. Claims: three-regime steerability framework, LAP diagnostic with ρ=0.86-0.91 across 24 concept families.\n\n3. \"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering\" (Liu) - arXiv 2605.05715, May 2026. Claims: classification-correction gap, specificity ratio ≤0.152, bottleneck MLP achieves Δ=+2.8pp.\n\n4. \"Are LLM Uncertainty and Correctness Encoded by the Same Features?\" (Patel et al.) - arXiv 2604.19974, April 2026. Claims: pure incorrectness features functionally inert, SAE-based classification-correction gap.\n\n5. \"Discovery of Hidden Miscalibration Regimes\" (Kobalczyk & van der Schaar) - arXiv 2605.13484, May 2026. Claims: opposing errors cancel when aggregated, worst-calibrated slices average 41% of instances.\n\nUse web search and web fetch. Report concisely what exists vs what doesn't."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9beb6dfb-1640-4ffa-a470-d5494026b31e",
  "isSidechain": false,
  "requestId": "req_011CbCFrMMe1kEwUXQFrPm1n",
  "type": "assistant",
  "uuid": "54c82f1b-bd28-4d69-be14-2e2596a975a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHRqDwzgXUkiUPSV9CBqjB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1699,
      "cache_read_input_tokens": 34978,
      "output_tokens": 496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 496,
          "cache_read_input_tokens": 34978,
          "cache_creation_input_tokens": 1699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1699
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

_source line 13 · 2026-05-19T16:40:03.921Z_

<details><summary>↩ Tool result · `toolu_01MC4n5sGE67n4MPXy1rWh1F`</summary>

```text
All verification is complete. Here is the summary:

---

**Verification Results: All 5 Papers Exist and Are Real**

**Paper 1: "CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models" (arXiv 2604.01366)**
- **EXISTS.** Authors: Fan Huang, Songheng Zhang, Haewoon Kwak, Jisun An. Submitted April 1, 2026.
- Claim "linearly separable bias directions": **CONFIRMED** -- abstract states biases are "encoded as linearly separable directions in model activation space."
- Claim "family-dependent mitigation": **CONFIRMED** -- debiasing is "strongly family-dependent."
- Claim "26-32% steering reduction": **CONFIRMED** -- paper reports "26--32% reduction in bias score."

**Paper 2: "Predicting Where Steering Vectors Succeed" (arXiv 2604.15557)**
- **EXISTS.** Author: Jayadev Billa. Submitted April 16, 2026.
- Claim "three-regime steerability framework": **CONFIRMED** -- describes when difference-of-means steering works, when nonlinear methods are needed, and when no method works.
- Claim "LAP diagnostic with rho=0.86-0.91 across 24 concept families": **CONFIRMED** -- peak A_lin predicts steering effectiveness at rho=+0.86 to +0.91 across 24 binary concept families on five models.

**Paper 3: "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering" (arXiv 2605.05715)**
- **EXISTS.** Author: Ming Liu (Amazon). Submitted May 7, 2026.
- Claim "classification-correction gap": **CONFIRMED** -- OT linearly decodable at 71.6% balanced accuracy but steering yields Delta approximately 0.
- Claim "specificity ratio <= 0.152": **CONFIRMED** -- OT direction has 85-88% overlap with task-critical computation, specificity ratio <= 0.152.
- Claim "bottleneck MLP achieves Delta=+2.8pp": **CONFIRMED** -- a learned non-linear residual MLP (4096->64->4096 bottleneck) achieves Delta=+2.8pp (p=0.025).

**Paper 4: "Are LLM Uncertainty and Correctness Encoded by the Same Features?" (arXiv 2604.19974)**
- **EXISTS.** Authors: Het Patel, Tiejin Chen, Hua Wei, Evangelos E. Papalexakis, Jia Chen. Submitted April 21, 2026.
- Claim "pure incorrectness features functionally inert": **CONFIRMED** -- explicitly stated in the abstract: they show statistically significant activation differences but produce "near-zero change in accuracy when suppressed."
- Claim "SAE-based classification-correction gap": **PARTIALLY CONFIRMED** -- the paper uses SAEs and demonstrates a dissociation between decodability and functional impact (i.e., a classification-correction gap), but does not use that exact term. The concept is present; the specific phrase is not.

**Paper 5: "Discovery of Hidden Miscalibration Regimes" (arXiv 2605.13484)**
- **EXISTS.** Authors: Katarzyna Kobalczyk, Mihaela van der Schaar (University of Cambridge). Submitted May 13, 2026.
- Claim "opposing errors cancel when aggregated": **CONFIRMED** -- paper states "opposing errors cancel when aggregated by confidence."
- Claim "worst-calibrated slices average 41% of instances": **CONFIRMED** -- paper reports "the worst-calibrated slice contains on average 41% of test examples."

**Bottom line:** All five papers are real, published on arXiv at the stated IDs and dates. All key claims checked out against the actual paper content, with only one minor nuance: Paper 4 demonstrates the classification-correction gap concept via SAEs but does not use that exact phrase.

Sources:
- [CogBias (2604.01366)](https://arxiv.org/abs/2604.01366)
- [Predicting Where Steering Vectors Succeed (2604.15557)](https://arxiv.org/abs/2604.15557)
- [Decodable but Not Corrected (2605.05715)](https://arxiv.org/abs/2605.05715)
- [LLM Uncertainty and Correctness Features (2604.19974)](https://arxiv.org/abs/2604.19974)
- [Hidden Miscalibration Regimes (2605.13484)](https://arxiv.org/abs/2605.13484)

agentId: a553eed3e4789a795 (use SendMessage with to: 'a553eed3e4789a795' to continue this agent)
&lt;usage>total_tokens: 18501
tool_uses: 13
duration_ms: 61171&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54c82f1b-bd28-4d69-be14-2e2596a975a3",
  "isSidechain": false,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "type": "user",
  "uuid": "324c8d24-d242-40d8-9173-5f2a9638907a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify these papers exist and check key claims. For each, search for the title and arXiv ID, and try to access the arXiv page.\n\n1. \"CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models\" - arXiv 2604.01366, April 2026. Claims: linearly separable bias directions, family-dependent mitigation, 26-32% steering reduction.\n\n2. \"Predicting Where Steering Vectors Succeed\" (Billa) - arXiv 2604.15557, April 2026. Claims: three-regime steerability framework, LAP diagnostic with ρ=0.86-0.91 across 24 concept families.\n\n3. \"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering\" (Liu) - arXiv 2605.05715, May 2026. Claims: classification-correction gap, specificity ratio ≤0.152, bottleneck MLP achieves Δ=+2.8pp.\n\n4. \"Are LLM Uncertainty and Correctness Encoded by the Same Features?\" (Patel et al.) - arXiv 2604.19974, April 2026. Claims: pure incorrectness features functionally inert, SAE-based classification-correction gap.\n\n5. \"Discovery of Hidden Miscalibration Regimes\" (Kobalczyk & van der Schaar) - arXiv 2605.13484, May 2026. Claims: opposing errors cancel when aggregated, worst-calibrated slices average 41% of instances.\n\nUse web search and web fetch. Report concisely what exists vs what doesn't.",
    "agentId": "a553eed3e4789a795",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "All verification is complete. Here is the summary:\n\n---\n\n**Verification Results: All 5 Papers Exist and Are Real**\n\n**Paper 1: \"CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models\" (arXiv 2604.01366)**\n- **EXISTS.** Authors: Fan Huang, Songheng Zhang, Haewoon Kwak, Jisun An. Submitted April 1, 2026.\n- Claim \"linearly separable bias directions\": **CONFIRMED** -- abstract states biases are \"encoded as linearly separable directions in model activation space.\"\n- Claim \"family-dependent mitigation\": **CONFIRMED** -- debiasing is \"strongly family-dependent.\"\n- Claim \"26-32% steering reduction\": **CONFIRMED** -- paper reports \"26--32% reduction in bias score.\"\n\n**Paper 2: \"Predicting Where Steering Vectors Succeed\" (arXiv 2604.15557)**\n- **EXISTS.** Author: Jayadev Billa. Submitted April 16, 2026.\n- Claim \"three-regime steerability framework\": **CONFIRMED** -- describes when difference-of-means steering works, when nonlinear methods are needed, and when no method works.\n- Claim \"LAP diagnostic with rho=0.86-0.91 across 24 concept families\": **CONFIRMED** -- peak A_lin predicts steering effectiveness at rho=+0.86 to +0.91 across 24 binary concept families on five models.\n\n**Paper 3: \"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering\" (arXiv 2605.05715)**\n- **EXISTS.** Author: Ming Liu (Amazon). Submitted May 7, 2026.\n- Claim \"classification-correction gap\": **CONFIRMED** -- OT linearly decodable at 71.6% balanced accuracy but steering yields Delta approximately 0.\n- Claim \"specificity ratio <= 0.152\": **CONFIRMED** -- OT direction has 85-88% overlap with task-critical computation, specificity ratio <= 0.152.\n- Claim \"bottleneck MLP achieves Delta=+2.8pp\": **CONFIRMED** -- a learned non-linear residual MLP (4096->64->4096 bottleneck) achieves Delta=+2.8pp (p=0.025).\n\n**Paper 4: \"Are LLM Uncertainty and Correctness Encoded by the Same Features?\" (arXiv 2604.19974)**\n- **EXISTS.** Authors: Het Patel, Tiejin Chen, Hua Wei, Evangelos E. Papalexakis, Jia Chen. Submitted April 21, 2026.\n- Claim \"pure incorrectness features functionally inert\": **CONFIRMED** -- explicitly stated in the abstract: they show statistically significant activation differences but produce \"near-zero change in accuracy when suppressed.\"\n- Claim \"SAE-based classification-correction gap\": **PARTIALLY CONFIRMED** -- the paper uses SAEs and demonstrates a dissociation between decodability and functional impact (i.e., a classification-correction gap), but does not use that exact term. The concept is present; the specific phrase is not.\n\n**Paper 5: \"Discovery of Hidden Miscalibration Regimes\" (arXiv 2605.13484)**\n- **EXISTS.** Authors: Katarzyna Kobalczyk, Mihaela van der Schaar (University of Cambridge). Submitted May 13, 2026.\n- Claim \"opposing errors cancel when aggregated\": **CONFIRMED** -- paper states \"opposing errors cancel when aggregated by confidence.\"\n- Claim \"worst-calibrated slices average 41% of instances\": **CONFIRMED** -- paper reports \"the worst-calibrated slice contains on average 41% of test examples.\"\n\n**Bottom line:** All five papers are real, published on arXiv at the stated IDs and dates. All key claims checked out against the actual paper content, with only one minor nuance: Paper 4 demonstrates the classification-correction gap concept via SAEs but does not use that exact phrase.\n\nSources:\n- [CogBias (2604.01366)](https://arxiv.org/abs/2604.01366)\n- [Predicting Where Steering Vectors Succeed (2604.15557)](https://arxiv.org/abs/2604.15557)\n- [Decodable but Not Corrected (2605.05715)](https://arxiv.org/abs/2605.05715)\n- [LLM Uncertainty and Correctness Features (2604.19974)](https://arxiv.org/abs/2604.19974)\n- [Hidden Miscalibration Regimes (2605.13484)](https://arxiv.org/abs/2605.13484)"
      }
    ],
    "totalDurationMs": 61171,
    "totalTokens": 18501,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 16235,
      "output_tokens": 1150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1150,
          "cache_read_input_tokens": 16235,
          "cache_creation_input_tokens": 1115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1115,
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
  "sourceToolAssistantUUID": "54c82f1b-bd28-4d69-be14-2e2596a975a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T16:40:18.468Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Xwwmu8eU2qALYt9JXheyUQ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify key 2026 references batch 2",
  "prompt": "Search the web to verify these papers exist and check key claims. For each, search for the title and arXiv ID, and try to access the arXiv page.\n\n1. \"Sycophancy Is Not One Thing\" (Vennemeyer et al.) - arXiv 2509.21305. Claims: decomposes sycophancy into independently steerable sub-components via difference-in-means across 5 models.\n\n2. \"Cross-Family Universality of Behavioral Axes in Language Models\" - arXiv 2605.09875, May 2026. Claims: behavioral axes align at AUROC 0.95 across Llama-Qwen-Mistral-Phi, transferable directions from 2 source models.\n\n3. \"Task Schema and Binding: A Double Dissociation Across Transformer Families\" - arXiv 2512.17325, 2025. Claims: task schemas transfer at 100% via late MLP patching across 9 models from 7 families.\n\n4. \"Closing the Confidence-Faithfulness Gap in Large Language Models\" (Miao & Ungar) - arXiv 2603.25052. Claims: calibration and verbalized confidence orthogonal in residual stream (cosine <0.04), 4-7× ECE improvement via adaptive steering.\n\n5. \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\" (CCPS, Khanmohammadi et al.) - arXiv 2505.21772, EMNLP 2025. Claims: ~55% ECE reduction, 21% Brier score reduction on Llama/Qwen/Mistral 8B-32B.\n\n6. \"SteerConf: Steering LLMs for Confidence Elicitation\" (Zhou et al.) - arXiv 2503.02863, NeurIPS 2025. Claims: 29% AUROC increase, 16% ECE reduction.\n\nUse web search and web fetch. Report concisely what exists vs what doesn't."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "324c8d24-d242-40d8-9173-5f2a9638907a",
  "isSidechain": false,
  "requestId": "req_011CbCFwfWfxPCF1B4uJhq6W",
  "type": "assistant",
  "uuid": "dc599b41-b9c9-4dc6-b831-8dc1794addfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EWqwxy2VH7BWdKXHAJoKR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1723,
      "cache_read_input_tokens": 36677,
      "output_tokens": 588,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 588,
          "cache_read_input_tokens": 36677,
          "cache_creation_input_tokens": 1723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1723
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

_source line 15 · 2026-05-19T16:41:33.741Z_

<details><summary>↩ Tool result · `toolu_01Xwwmu8eU2qALYt9JXheyUQ`</summary>

```text
Here is my verification report for all six papers:

---

## Paper 1: "Sycophancy Is Not One Thing" (Vennemeyer et al.) -- arXiv 2509.21305

**EXISTS. Verified on arXiv.**

- **Title:** "Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs"
- **Authors:** Daniel Vennemeyer, Phan Anh Duong, Tiffany Zhan, Tianyu Jiang
- **Submitted:** September 25, 2025; revised March 22, 2026 (v3)
- **Claim check -- "decomposes sycophancy into independently steerable sub-components via difference-in-means across 5 models":** Largely accurate. The paper decomposes sycophancy into sycophantic agreement and sycophantic praise, uses difference-in-means directions, and confirms independent steerability. It evaluates 5 instruction-tuned models (Qwen3-30B, LLaMA-3.1-8B, Qwen3-4B, LLaMA-3.3-70B, GPT-OSS-20B). The claim of 5 models is confirmed.

---

## Paper 2: "Cross-Family Universality of Behavioral Axes" -- arXiv 2605.09875

**EXISTS. Verified on arXiv.**

- **Title (slightly different):** "Cross-Family Universality of Behavioral Axes via Anchor-Projected Representations" (not just "...in Language Models")
- **Authors:** Su-Hyeon Kim, Yo-Sub Han (Yonsei University)
- **Submitted:** May 11, 2026
- **Claim check -- "AUROC 0.95 across Llama-Qwen-Mistral-Phi, transferable directions from 2 source models":** Confirmed. The paper reports 0.95 mean binary AUROC across the LQMP cluster, and states "two source models and small anchor pools already suffice to approximate transferable directions." The date (May 2026) is correct.

---

## Paper 3: "Task Schema and Binding" -- arXiv 2512.17325

**EXISTS. Verified on arXiv.**

- **Title (slightly different):** "Task Schema and Binding: A Double Dissociation Study of In-Context Learning" (not "...Across Transformer Families")
- **Author:** Chaeha Kim (single author)
- **Submitted:** December 19, 2025
- **Claim check -- "task schemas transfer at 100% via late MLP patching across 9 models from 7 families":** Confirmed. The paper explicitly states "Task Schema transfers at 100% via late MLP patching" and tests "9 models from 7 Transformer families plus Mamba (370M-13B parameters)."

---

## Paper 4: "Closing the Confidence-Faithfulness Gap" (Miao & Ungar) -- arXiv 2603.25052

**EXISTS. Verified on arXiv.**

- **Title:** "Closing the Confidence-Faithfulness Gap in Large Language Models"
- **Authors:** Miranda Muqing Miao, Lyle Ungar (University of Pennsylvania)
- **Submitted:** March 26, 2026; revised April 1, 2026
- **Claim check -- "calibration and verbalized confidence orthogonal (cosine <0.04), 4-7x ECE improvement via adaptive steering":** All confirmed from the full HTML paper. Cosine similarity between the two probe weight vectors "remains below 0.04 across all layers." "Adaptive steering reduces ECE by 4-7x relative to unsteered verbalized confidence."

---

## Paper 5: CCPS (Khanmohammadi et al.) -- arXiv 2505.21772

**EXISTS. Verified on arXiv and ACL Anthology.**

- **Title:** "Calibrating LLM Confidence by Probing Perturbed Representation Stability"
- **Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese H. Smiley, Kundan Thind, Mohammad M. Ghassemi
- **Submitted:** May 27, 2025; revised September 18, 2025
- **Claim check -- "~55% ECE reduction, 21% Brier score reduction on Llama/Qwen/Mistral 8B-32B":** Confirmed. The paper reports approximately 55% ECE reduction and 21% Brier score reduction across Llama, Qwen, and Mistral architectures (8B-32B).
- **Claim check -- "EMNLP 2025":** Confirmed. The paper appears in ACL Anthology as EMNLP 2025 main conference (2025.emnlp-main.530), and there is a Hacker News thread discussing it in that context.

---

## Paper 6: "SteerConf" (Zhou et al.) -- arXiv 2503.02863

**EXISTS. Verified on arXiv and NeurIPS.**

- **Title:** "SteerConf: Steering LLMs for Confidence Elicitation"
- **Authors:** Ziang Zhou, Tianyuan Jin, Jieming Shi, Qing Li
- **Submitted:** March 4, 2025; revised May 23, 2025
- **Claim check -- "NeurIPS 2025":** Confirmed via NeurIPS 2025 virtual poster page (neurips.cc/virtual/2025/poster/119826).
- **Claim check -- "29% AUROC increase, 16% ECE reduction":** Confirmed from the full paper HTML. These are reported specifically on the Object Counting dataset with GPT-3.5 using a "very cautious" steering prompt. Note: these are cherry-picked illustrative numbers from one dataset/model combination used in the introduction to motivate the work, not overall average improvements.

---

## Summary

All six papers are **real and verified** on arXiv with the correct arXiv IDs. The key claims are substantively accurate, with these caveats:

1. **Paper 2** has a slightly different subtitle ("...via Anchor-Projected Representations" vs. "...in Language Models").
2. **Paper 3** has a slightly different subtitle ("...Study of In-Context Learning" vs. "...Across Transformer Families").
3. **Paper 6's** 29% AUROC / 16% ECE numbers are from a single motivating example (Object Counting + GPT-3.5), not aggregate results across all benchmarks.

Sources:
- [Paper 1 - arXiv 2509.21305](https://arxiv.org/abs/2509.21305)
- [Paper 2 - arXiv 2605.09875](https://arxiv.org/abs/2605.09875)
- [Paper 3 - arXiv 2512.17325](https://arxiv.org/abs/2512.17325)
- [Paper 4 - arXiv 2603.25052](https://arxiv.org/abs/2603.25052)
- [Paper 5 - arXiv 2505.21772](https://arxiv.org/abs/2505.21772)
- [Paper 5 - ACL Anthology EMNLP 2025](https://aclanthology.org/2025.emnlp-main.530/)
- [Paper 6 - arXiv 2503.02863](https://arxiv.org/abs/2503.02863)
- [Paper 6 - NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/119826)

agentId: af552b3c31f0f6f64 (use SendMessage with to: 'af552b3c31f0f6f64' to continue this agent)
&lt;usage>total_tokens: 22125
tool_uses: 18
duration_ms: 75267&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc599b41-b9c9-4dc6-b831-8dc1794addfa",
  "isSidechain": false,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "type": "user",
  "uuid": "e360690f-c748-4f2e-8d5e-031aed2cc8d8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify these papers exist and check key claims. For each, search for the title and arXiv ID, and try to access the arXiv page.\n\n1. \"Sycophancy Is Not One Thing\" (Vennemeyer et al.) - arXiv 2509.21305. Claims: decomposes sycophancy into independently steerable sub-components via difference-in-means across 5 models.\n\n2. \"Cross-Family Universality of Behavioral Axes in Language Models\" - arXiv 2605.09875, May 2026. Claims: behavioral axes align at AUROC 0.95 across Llama-Qwen-Mistral-Phi, transferable directions from 2 source models.\n\n3. \"Task Schema and Binding: A Double Dissociation Across Transformer Families\" - arXiv 2512.17325, 2025. Claims: task schemas transfer at 100% via late MLP patching across 9 models from 7 families.\n\n4. \"Closing the Confidence-Faithfulness Gap in Large Language Models\" (Miao & Ungar) - arXiv 2603.25052. Claims: calibration and verbalized confidence orthogonal in residual stream (cosine <0.04), 4-7× ECE improvement via adaptive steering.\n\n5. \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\" (CCPS, Khanmohammadi et al.) - arXiv 2505.21772, EMNLP 2025. Claims: ~55% ECE reduction, 21% Brier score reduction on Llama/Qwen/Mistral 8B-32B.\n\n6. \"SteerConf: Steering LLMs for Confidence Elicitation\" (Zhou et al.) - arXiv 2503.02863, NeurIPS 2025. Claims: 29% AUROC increase, 16% ECE reduction.\n\nUse web search and web fetch. Report concisely what exists vs what doesn't.",
    "agentId": "af552b3c31f0f6f64",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my verification report for all six papers:\n\n---\n\n## Paper 1: \"Sycophancy Is Not One Thing\" (Vennemeyer et al.) -- arXiv 2509.21305\n\n**EXISTS. Verified on arXiv.**\n\n- **Title:** \"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs\"\n- **Authors:** Daniel Vennemeyer, Phan Anh Duong, Tiffany Zhan, Tianyu Jiang\n- **Submitted:** September 25, 2025; revised March 22, 2026 (v3)\n- **Claim check -- \"decomposes sycophancy into independently steerable sub-components via difference-in-means across 5 models\":** Largely accurate. The paper decomposes sycophancy into sycophantic agreement and sycophantic praise, uses difference-in-means directions, and confirms independent steerability. It evaluates 5 instruction-tuned models (Qwen3-30B, LLaMA-3.1-8B, Qwen3-4B, LLaMA-3.3-70B, GPT-OSS-20B). The claim of 5 models is confirmed.\n\n---\n\n## Paper 2: \"Cross-Family Universality of Behavioral Axes\" -- arXiv 2605.09875\n\n**EXISTS. Verified on arXiv.**\n\n- **Title (slightly different):** \"Cross-Family Universality of Behavioral Axes via Anchor-Projected Representations\" (not just \"...in Language Models\")\n- **Authors:** Su-Hyeon Kim, Yo-Sub Han (Yonsei University)\n- **Submitted:** May 11, 2026\n- **Claim check -- \"AUROC 0.95 across Llama-Qwen-Mistral-Phi, transferable directions from 2 source models\":** Confirmed. The paper reports 0.95 mean binary AUROC across the LQMP cluster, and states \"two source models and small anchor pools already suffice to approximate transferable directions.\" The date (May 2026) is correct.\n\n---\n\n## Paper 3: \"Task Schema and Binding\" -- arXiv 2512.17325\n\n**EXISTS. Verified on arXiv.**\n\n- **Title (slightly different):** \"Task Schema and Binding: A Double Dissociation Study of In-Context Learning\" (not \"...Across Transformer Families\")\n- **Author:** Chaeha Kim (single author)\n- **Submitted:** December 19, 2025\n- **Claim check -- \"task schemas transfer at 100% via late MLP patching across 9 models from 7 families\":** Confirmed. The paper explicitly states \"Task Schema transfers at 100% via late MLP patching\" and tests \"9 models from 7 Transformer families plus Mamba (370M-13B parameters).\"\n\n---\n\n## Paper 4: \"Closing the Confidence-Faithfulness Gap\" (Miao & Ungar) -- arXiv 2603.25052\n\n**EXISTS. Verified on arXiv.**\n\n- **Title:** \"Closing the Confidence-Faithfulness Gap in Large Language Models\"\n- **Authors:** Miranda Muqing Miao, Lyle Ungar (University of Pennsylvania)\n- **Submitted:** March 26, 2026; revised April 1, 2026\n- **Claim check -- \"calibration and verbalized confidence orthogonal (cosine <0.04), 4-7x ECE improvement via adaptive steering\":** All confirmed from the full HTML paper. Cosine similarity between the two probe weight vectors \"remains below 0.04 across all layers.\" \"Adaptive steering reduces ECE by 4-7x relative to unsteered verbalized confidence.\"\n\n---\n\n## Paper 5: CCPS (Khanmohammadi et al.) -- arXiv 2505.21772\n\n**EXISTS. Verified on arXiv and ACL Anthology.**\n\n- **Title:** \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\"\n- **Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese H. Smiley, Kundan Thind, Mohammad M. Ghassemi\n- **Submitted:** May 27, 2025; revised September 18, 2025\n- **Claim check -- \"~55% ECE reduction, 21% Brier score reduction on Llama/Qwen/Mistral 8B-32B\":** Confirmed. The paper reports approximately 55% ECE reduction and 21% Brier score reduction across Llama, Qwen, and Mistral architectures (8B-32B).\n- **Claim check -- \"EMNLP 2025\":** Confirmed. The paper appears in ACL Anthology as EMNLP 2025 main conference (2025.emnlp-main.530), and there is a Hacker News thread discussing it in that context.\n\n---\n\n## Paper 6: \"SteerConf\" (Zhou et al.) -- arXiv 2503.02863\n\n**EXISTS. Verified on arXiv and NeurIPS.**\n\n- **Title:** \"SteerConf: Steering LLMs for Confidence Elicitation\"\n- **Authors:** Ziang Zhou, Tianyuan Jin, Jieming Shi, Qing Li\n- **Submitted:** March 4, 2025; revised May 23, 2025\n- **Claim check -- \"NeurIPS 2025\":** Confirmed via NeurIPS 2025 virtual poster page (neurips.cc/virtual/2025/poster/119826).\n- **Claim check -- \"29% AUROC increase, 16% ECE reduction\":** Confirmed from the full paper HTML. These are reported specifically on the Object Counting dataset with GPT-3.5 using a \"very cautious\" steering prompt. Note: these are cherry-picked illustrative numbers from one dataset/model combination used in the introduction to motivate the work, not overall average improvements.\n\n---\n\n## Summary\n\nAll six papers are **real and verified** on arXiv with the correct arXiv IDs. The key claims are substantively accurate, with these caveats:\n\n1. **Paper 2** has a slightly different subtitle (\"...via Anchor-Projected Representations\" vs. \"...in Language Models\").\n2. **Paper 3** has a slightly different subtitle (\"...Study of In-Context Learning\" vs. \"...Across Transformer Families\").\n3. **Paper 6's** 29% AUROC / 16% ECE numbers are from a single motivating example (Object Counting + GPT-3.5), not aggregate results across all benchmarks.\n\nSources:\n- [Paper 1 - arXiv 2509.21305](https://arxiv.org/abs/2509.21305)\n- [Paper 2 - arXiv 2605.09875](https://arxiv.org/abs/2605.09875)\n- [Paper 3 - arXiv 2512.17325](https://arxiv.org/abs/2512.17325)\n- [Paper 4 - arXiv 2603.25052](https://arxiv.org/abs/2603.25052)\n- [Paper 5 - arXiv 2505.21772](https://arxiv.org/abs/2505.21772)\n- [Paper 5 - ACL Anthology EMNLP 2025](https://aclanthology.org/2025.emnlp-main.530/)\n- [Paper 6 - arXiv 2503.02863](https://arxiv.org/abs/2503.02863)\n- [Paper 6 - NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/119826)"
      }
    ],
    "totalDurationMs": 75267,
    "totalTokens": 22125,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 249,
      "cache_creation_input_tokens": 12176,
      "cache_read_input_tokens": 7773,
      "output_tokens": 1927,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 249,
          "output_tokens": 1927,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 12176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12176,
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
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "dc599b41-b9c9-4dc6-b831-8dc1794addfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "e360690f-c748-4f2e-8d5e-031aed2cc8d8",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose competing calibration biases via activation steering",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Tool call

_source line 18 · 2026-05-19T16:41:44.255Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LmuLcrocFzzm7p3dwFYEp3`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competing/missing work 2026",
  "prompt": "Search the web thoroughly for recent (2025-2026) papers that might be competing with or missing from a proposal about \"decomposing LLM miscalibration into competing biases and applying targeted activation correction.\" The proposal targets choice-supportive bias (CSB) and contradictory-evidence overweighting (CEO) as competing biases.\n\nSearch for these specific topics using multiple queries:\n\n1. \"LLM calibration activation steering 2026\" - any new calibration methods using activation steering\n2. \"competing biases language models 2026\" - work on multiple simultaneous biases\n3. \"decomposing overconfidence underconfidence LLM 2026\" - decomposition of confidence errors\n4. \"bias interference cancellation language models\" - interference between biases\n5. \"per-instance calibration correction LLM 2026\" - instance-level calibration methods\n6. \"confidence elicitation mechanistic interpretability 2026\" - mechanistic work on confidence\n7. \"activation steering calibration bias decomposition\" - combination approach\n8. site:arxiv.org \"choice supportive bias\" OR \"contradictory evidence\" language model 2026\n9. site:openreview.net calibration steering decomposition 2026\n10. \"multi-bias correction\" OR \"bias-specific steering\" language model\n\nFor each relevant paper found, report: title, authors, arXiv ID, date, and a brief description of why it's relevant. Focus especially on papers from March-May 2026 that might be concurrent work.\n\nBe thorough - search at least 8 of these queries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e360690f-c748-4f2e-8d5e-031aed2cc8d8",
  "isSidechain": false,
  "requestId": "req_011CbCG4HaWjgtSpZLxVLo6x",
  "type": "assistant",
  "uuid": "b56c38c3-7705-4c78-a338-2008381fabdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012reT8apZ5EQpQs2Sd5CprP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2596,
      "cache_read_input_tokens": 38400,
      "output_tokens": 456,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2596,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 456,
          "cache_read_input_tokens": 38400,
          "cache_creation_input_tokens": 2596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2596
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

_source line 19 · 2026-05-19T16:45:28.712Z_

<details><summary>↩ Tool result · `toolu_01LmuLcrocFzzm7p3dwFYEp3`</summary>

```text
Now I have comprehensive results. Here is my thorough report:

---

## Thorough Literature Search Results: Competing/Missing Work for "Decomposing LLM Miscalibration into Competing Biases with Targeted Activation Correction"

### TIER 1: MOST DIRECTLY RELEVANT / POTENTIAL COMPETITORS

---

**1. "Competing Biases underlie Overconfidence and Underconfidence in LLMs"**
- **Authors:** Dharshan Kumaran, Stephen M Fleming, Larisa Markeeva, Joe Heyward, Andrea Banino, Mrinal Mathur, Razvan Pascanu, Simon Osindero, Benedetto de Martino, Petar Velickovic, Viorica Patraucean
- **Venue:** Nature Machine Intelligence, April 2026
- **DOI:** https://www.nature.com/articles/s42256-026-01217-9
- **Why critical:** This appears to be the **direct precursor or possibly the same core finding** as the proposal. It identifies the same two competing biases -- choice-supportive bias (CSB) inflating confidence and systematic overweighting of contradictory evidence causing underconfidence. Tested on Gemma 3, GPT-4o, and o1-preview. However, this paper characterizes the biases **behaviorally** (via confidence experiments) and does NOT propose activation-level correction. The proposal's contribution of **targeted activation correction** would build directly on top of this work. This paper is the arXiv version 2507.03120 (July 2025), published in Nature MI in April 2026.

---

**2. "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs"**
- **Authors:** Tianyi Zhao, Yinhan He, Wendy Zheng, Yujie Zhang, Chen Chen
- **arXiv ID:** 2604.01457
- **Date:** April 1, 2026
- **Why critical:** This is the **closest concurrent competitor** for the mechanistic/activation side. It performs circuit-level analysis identifying specific MLP blocks and attention heads in middle-to-late layers that write the confidence-inflation signal, and demonstrates targeted inference-time recalibration interventions on these circuits. However, it focuses only on **overconfidence** (one side of the coin) and does not decompose miscalibration into competing biases. The proposal's novelty of addressing **both** CSB and CEO as competing forces and applying **bias-specific** correction vectors would differentiate it.

---

**3. "CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models"**
- **Authors:** Fan Huang, Songheng Zhang, Haewoon Kwak, Jisun An
- **arXiv ID:** 2604.01366
- **Date:** April 1, 2026
- **Why critical:** This paper organizes LLM cognitive biases into four families (Judgment, Information Processing, Social, Response), shows they are encoded as **linearly separable directions in activation space** with near-orthogonal representations, and applies activation steering achieving 26-32% bias reduction. The finding that different biases have near-orthogonal representations is directly relevant to whether CSB and CEO can be independently targeted. However, it does not specifically address calibration-related biases or the competing-bias framework.

---

**4. "Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs"**
- **Authors:** Daniel Vennemeyer, Phan Anh Duong, Tiffany Zhan, Tianyu Jiang
- **arXiv ID:** 2509.21305
- **Date:** September 25, 2025 (revised March 22, 2026)
- **Why critical:** Demonstrates that sycophantic behaviors decompose into **distinct sub-behaviors** (sycophantic agreement, sycophantic praise, genuine agreement) encoded along **distinct linear directions** in latent space, each independently steerable. This provides strong methodological precedent for the proposal's claim that CSB and CEO can be decomposed and independently corrected via activation steering. Choice-supportive bias is closely related to sycophancy.

---

**5. "CORAL: Correctness-Optimized Residual Activation Lens -- Transferrable and Calibration-Aware Inference-Time Steering"**
- **Authors:** Miranda Muqing Miao, Young-Min Cho, Lyle Ungar
- **arXiv ID:** 2602.06022
- **Date:** February 5, 2026
- **Why critical:** Directly connects **calibration improvement with activation steering**. Achieves 14% accuracy improvement and 49% ECE reduction on held-out benchmarks by extracting correctness signals from internal activations. However, it does not decompose miscalibration into competing biases -- it treats calibration as a monolithic signal. The proposal's decomposition approach would be differentiated.

---

### TIER 2: HIGHLY RELEVANT METHODOLOGICAL NEIGHBORS

---

**6. "Fine-Grained Activation Steering: Steering Less, Achieving More" (AUSteer)**
- **Authors:** Zijian Feng, Tianjiao Li, Zixiao Zhu, et al.
- **arXiv ID:** 2602.04428
- **Date:** February 4, 2026
- **Why relevant:** Proposes steering at the **atomic unit (AU) level** (individual activation dimensions) rather than block-level, with **input-adaptive steering strengths**. This per-instance, fine-grained approach is methodologically relevant to per-instance bias correction. Could be a complementary technique for the proposal's correction mechanism.

---

**7. "Discovery of Hidden Miscalibration Regimes"**
- **Authors:** Katarzyna Kobalczyk, Mihaela van der Schaar
- **arXiv ID:** 2605.13484
- **Date:** May 13, 2026 (very recent!)
- **Why relevant:** Discovers **input-dependent calibration heterogeneity** across LLM benchmarks -- models are systematically over/underconfident in different input regions. Proposes local confidence correction. This directly supports the proposal's premise that calibration errors are not uniform and require per-instance intervention, though it does not use activation steering or identify specific bias mechanisms.

---

**8. "Minimizing Collateral Damage in Activation Steering"**
- **Authors:** Tam Nguyen, Tu Anh Nguyen, Sina Alemohammad, Richard G. Baraniuk
- **arXiv ID:** 2605.01167
- **Date:** May 1, 2026 (very recent!)
- **Why relevant:** Addresses the problem of steering one behavior while **not degrading others** -- directly relevant if the proposal steers CSB and CEO independently. Proposes constrained optimization weighted by empirical second-moment matrix to minimize collateral effects. Essential methodological reference for ensuring bias-specific steering doesn't interfere.

---

**9. "Shifting Perspectives: Steering Vector Ensembles for Robust Bias Mitigation in LLMs"**
- **Authors:** Zara Siddique, Irtaza Khalid, Liam D. Turner, Luis Espinosa-Anke
- **arXiv ID:** 2503.05371
- **Date:** March 7, 2025 (revised March 28, 2026)
- **Why relevant:** Uses **8 simultaneous steering vectors**, one per bias axis, combined via ensemble averaging. Demonstrates that multiple bias-specific vectors can be applied concurrently. Directly relevant to the proposal's multi-bias correction approach.

---

**10. "Activation Steering with a Feedback Controller" (PID Steering)**
- **Authors:** Dung V. Nguyen, Hieu M. Vu, Nhi Y. Pham, Lei Zhang, Tan M. Nguyen
- **arXiv ID:** 2510.04309
- **Date:** October 5, 2025 (revised May 16, 2026)
- **Why relevant:** Formalizes steering as a control problem (PID controller) with proportional, integral, and derivative terms. The integral term provides persistent correction across layers, and the derivative prevents overshoot. Relevant as an alternative framework for the proposal's correction mechanism.

---

**11. "Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation"**
- **Authors:** Nan Zhuang, Wenshuo Wang, Lekai Qian, Yuxiao Wang, Boyu Cao, Qi Liu
- **arXiv ID:** 2512.03082
- **Date:** November 28, 2025
- **Why relevant:** Directly targets CSB in LLMs but uses a **fine-tuning approach** (training on generated unbiased reasoning data) rather than activation steering. Achieves 81.5-94.3% improvement. The proposal should cite this as an alternative approach to CSB mitigation and argue for the advantages of inference-time activation correction.

---

**12. "FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering"**
- **Authors:** Yichen Li, Zhiting Fan, Ruizhe Chen, et al.
- **arXiv ID:** 2504.14492
- **Date:** April 20, 2025 (ACL 2025 Findings)
- **Why relevant:** Detects bias signatures via lightweight linear classifiers on activations, computes debiasing steering vectors from contrastive pairs, and applies dynamic correction at inference time. Achieves >90% linear separability of bias in intermediate layers. Methodologically very close to what the proposal would do for CSB/CEO detection and correction.

---

### TIER 3: RELEVANT BACKGROUND / SUPPORTING WORK

---

**13. "Calibrating LLM Confidence by Probing Perturbed Representation Stability" (CCPS)**
- **Authors:** Reza Khanmohammadi et al.
- **arXiv ID:** 2505.21772
- **Date:** May 27, 2025
- **Why relevant:** Per-instance calibration via probing hidden state stability. Achieves 55% ECE reduction. Relevant as an alternative per-instance calibration approach that does not use steering.

---

**14. "Beacon: Single-Turn Diagnosis and Mitigation of Latent Sycophancy in LLMs"**
- **Authors:** Sanskar Pandey, Ruhaan Chopra, Angkul Puniya, Sohom Pal
- **arXiv ID:** 2510.16727
- **Date:** October 19, 2025 (revised May 17, 2026)
- **Why relevant:** Decomposes sycophancy into distinct linguistic and affective components, proposes activation-level interventions. Relevant to understanding CSB as related to sycophancy.

---

**15. "Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of LLMs"**
- **Authors:** David Bani-Harouni et al.
- **arXiv ID:** 2503.02623
- **Date:** March 4, 2025 (ICLR 2026)
- **Why relevant:** RL-based calibration that penalizes both over- and under-confidence. Alternative training-time approach to the proposal's inference-time method.

---

**16. "Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs"**
- **Authors:** Shivam Dubey
- **arXiv ID:** 2508.09019
- **Date:** August 12, 2025
- **Why relevant:** Trains linear probes to detect bias, computes steering vectors from contrasting biased/neutral activations. Foundational methodology for the proposal.

---

### KEY GAPS THE PROPOSAL WOULD FILL

Based on this search, the proposal's unique contribution appears to be the **combination** of:
1. **Decomposing** miscalibration into specific competing biases (CSB + CEO) -- building on Kumaran et al. 2026 (behavioral finding) but going mechanistic
2. **Identifying activation-level signatures** for each bias separately -- building on Zhao et al. 2604.01457 (overconfidence only) and CogBias 2604.01366 (cognitive biases generally, not calibration-specific)
3. **Applying targeted, per-instance correction** for each bias independently -- building on CORAL, AUSteer, FairSteer methods

No single paper found does all three together. The closest threats are:
- Kumaran et al. (Nature MI, April 2026) -- same behavioral decomposition but no activation correction
- Zhao et al. (April 2026) -- mechanistic overconfidence analysis but only one bias, no decomposition
- CogBias (April 2026) -- multi-bias activation steering but not for calibration-specific biases

Sources:
- [Competing Biases underlie Overconfidence and Underconfidence in LLMs](https://www.nature.com/articles/s42256-026-01217-9)
- [Wired for Overconfidence (2604.01457)](https://arxiv.org/abs/2604.01457)
- [CogBias (2604.01366)](https://arxiv.org/abs/2604.01366)
- [Sycophancy Is Not One Thing (2509.21305)](https://arxiv.org/abs/2509.21305)
- [CORAL (2602.06022)](https://arxiv.org/abs/2602.06022)
- [AUSteer: Fine-Grained Activation Steering (2602.04428)](https://arxiv.org/abs/2602.04428)
- [Discovery of Hidden Miscalibration Regimes (2605.13484)](https://arxiv.org/abs/2605.13484)
- [Minimizing Collateral Damage in Activation Steering (2605.01167)](https://arxiv.org/abs/2605.01167)
- [Shifting Perspectives: Steering Vector Ensembles (2503.05371)](https://arxiv.org/abs/2503.05371)
- [PID Steering (2510.04309)](https://arxiv.org/abs/2510.04309)
- [Alleviating Choice Supportive Bias via RDG (2512.03082)](https://arxiv.org/abs/2512.03082)
- [FairSteer (2504.14492)](https://arxiv.org/abs/2504.14492)
- [CCPS: Probing Perturbed Representation Stability (2505.21772)](https://arxiv.org/abs/2505.21772)
- [Beacon: Sycophancy Diagnosis (2510.16727)](https://arxiv.org/abs/2510.16727)
- [Rewarding Doubt (2503.02623)](https://arxiv.org/abs/2503.02623)
- [Activation Steering for Bias Mitigation (2508.09019)](https://arxiv.org/abs/2508.09019)
- [Activation Steering Field Guide](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)
- [MERA: Mechanistic Error Reduction with Abstention](https://openreview.net/forum?id=fUCPq5RvmH)

agentId: a83eed1f79442d829 (use SendMessage with to: 'a83eed1f79442d829' to continue this agent)
&lt;usage>total_tokens: 39610
tool_uses: 41
duration_ms: 224451&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b56c38c3-7705-4c78-a338-2008381fabdf",
  "isSidechain": false,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "type": "user",
  "uuid": "d7244ea0-a9dc-4138-9d8d-b37b089e2bf7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web thoroughly for recent (2025-2026) papers that might be competing with or missing from a proposal about \"decomposing LLM miscalibration into competing biases and applying targeted activation correction.\" The proposal targets choice-supportive bias (CSB) and contradictory-evidence overweighting (CEO) as competing biases.\n\nSearch for these specific topics using multiple queries:\n\n1. \"LLM calibration activation steering 2026\" - any new calibration methods using activation steering\n2. \"competing biases language models 2026\" - work on multiple simultaneous biases\n3. \"decomposing overconfidence underconfidence LLM 2026\" - decomposition of confidence errors\n4. \"bias interference cancellation language models\" - interference between biases\n5. \"per-instance calibration correction LLM 2026\" - instance-level calibration methods\n6. \"confidence elicitation mechanistic interpretability 2026\" - mechanistic work on confidence\n7. \"activation steering calibration bias decomposition\" - combination approach\n8. site:arxiv.org \"choice supportive bias\" OR \"contradictory evidence\" language model 2026\n9. site:openreview.net calibration steering decomposition 2026\n10. \"multi-bias correction\" OR \"bias-specific steering\" language model\n\nFor each relevant paper found, report: title, authors, arXiv ID, date, and a brief description of why it's relevant. Focus especially on papers from March-May 2026 that might be concurrent work.\n\nBe thorough - search at least 8 of these queries.",
    "agentId": "a83eed1f79442d829",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive results. Here is my thorough report:\n\n---\n\n## Thorough Literature Search Results: Competing/Missing Work for \"Decomposing LLM Miscalibration into Competing Biases with Targeted Activation Correction\"\n\n### TIER 1: MOST DIRECTLY RELEVANT / POTENTIAL COMPETITORS\n\n---\n\n**1. \"Competing Biases underlie Overconfidence and Underconfidence in LLMs\"**\n- **Authors:** Dharshan Kumaran, Stephen M Fleming, Larisa Markeeva, Joe Heyward, Andrea Banino, Mrinal Mathur, Razvan Pascanu, Simon Osindero, Benedetto de Martino, Petar Velickovic, Viorica Patraucean\n- **Venue:** Nature Machine Intelligence, April 2026\n- **DOI:** https://www.nature.com/articles/s42256-026-01217-9\n- **Why critical:** This appears to be the **direct precursor or possibly the same core finding** as the proposal. It identifies the same two competing biases -- choice-supportive bias (CSB) inflating confidence and systematic overweighting of contradictory evidence causing underconfidence. Tested on Gemma 3, GPT-4o, and o1-preview. However, this paper characterizes the biases **behaviorally** (via confidence experiments) and does NOT propose activation-level correction. The proposal's contribution of **targeted activation correction** would build directly on top of this work. This paper is the arXiv version 2507.03120 (July 2025), published in Nature MI in April 2026.\n\n---\n\n**2. \"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs\"**\n- **Authors:** Tianyi Zhao, Yinhan He, Wendy Zheng, Yujie Zhang, Chen Chen\n- **arXiv ID:** 2604.01457\n- **Date:** April 1, 2026\n- **Why critical:** This is the **closest concurrent competitor** for the mechanistic/activation side. It performs circuit-level analysis identifying specific MLP blocks and attention heads in middle-to-late layers that write the confidence-inflation signal, and demonstrates targeted inference-time recalibration interventions on these circuits. However, it focuses only on **overconfidence** (one side of the coin) and does not decompose miscalibration into competing biases. The proposal's novelty of addressing **both** CSB and CEO as competing forces and applying **bias-specific** correction vectors would differentiate it.\n\n---\n\n**3. \"CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models\"**\n- **Authors:** Fan Huang, Songheng Zhang, Haewoon Kwak, Jisun An\n- **arXiv ID:** 2604.01366\n- **Date:** April 1, 2026\n- **Why critical:** This paper organizes LLM cognitive biases into four families (Judgment, Information Processing, Social, Response), shows they are encoded as **linearly separable directions in activation space** with near-orthogonal representations, and applies activation steering achieving 26-32% bias reduction. The finding that different biases have near-orthogonal representations is directly relevant to whether CSB and CEO can be independently targeted. However, it does not specifically address calibration-related biases or the competing-bias framework.\n\n---\n\n**4. \"Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs\"**\n- **Authors:** Daniel Vennemeyer, Phan Anh Duong, Tiffany Zhan, Tianyu Jiang\n- **arXiv ID:** 2509.21305\n- **Date:** September 25, 2025 (revised March 22, 2026)\n- **Why critical:** Demonstrates that sycophantic behaviors decompose into **distinct sub-behaviors** (sycophantic agreement, sycophantic praise, genuine agreement) encoded along **distinct linear directions** in latent space, each independently steerable. This provides strong methodological precedent for the proposal's claim that CSB and CEO can be decomposed and independently corrected via activation steering. Choice-supportive bias is closely related to sycophancy.\n\n---\n\n**5. \"CORAL: Correctness-Optimized Residual Activation Lens -- Transferrable and Calibration-Aware Inference-Time Steering\"**\n- **Authors:** Miranda Muqing Miao, Young-Min Cho, Lyle Ungar\n- **arXiv ID:** 2602.06022\n- **Date:** February 5, 2026\n- **Why critical:** Directly connects **calibration improvement with activation steering**. Achieves 14% accuracy improvement and 49% ECE reduction on held-out benchmarks by extracting correctness signals from internal activations. However, it does not decompose miscalibration into competing biases -- it treats calibration as a monolithic signal. The proposal's decomposition approach would be differentiated.\n\n---\n\n### TIER 2: HIGHLY RELEVANT METHODOLOGICAL NEIGHBORS\n\n---\n\n**6. \"Fine-Grained Activation Steering: Steering Less, Achieving More\" (AUSteer)**\n- **Authors:** Zijian Feng, Tianjiao Li, Zixiao Zhu, et al.\n- **arXiv ID:** 2602.04428\n- **Date:** February 4, 2026\n- **Why relevant:** Proposes steering at the **atomic unit (AU) level** (individual activation dimensions) rather than block-level, with **input-adaptive steering strengths**. This per-instance, fine-grained approach is methodologically relevant to per-instance bias correction. Could be a complementary technique for the proposal's correction mechanism.\n\n---\n\n**7. \"Discovery of Hidden Miscalibration Regimes\"**\n- **Authors:** Katarzyna Kobalczyk, Mihaela van der Schaar\n- **arXiv ID:** 2605.13484\n- **Date:** May 13, 2026 (very recent!)\n- **Why relevant:** Discovers **input-dependent calibration heterogeneity** across LLM benchmarks -- models are systematically over/underconfident in different input regions. Proposes local confidence correction. This directly supports the proposal's premise that calibration errors are not uniform and require per-instance intervention, though it does not use activation steering or identify specific bias mechanisms.\n\n---\n\n**8. \"Minimizing Collateral Damage in Activation Steering\"**\n- **Authors:** Tam Nguyen, Tu Anh Nguyen, Sina Alemohammad, Richard G. Baraniuk\n- **arXiv ID:** 2605.01167\n- **Date:** May 1, 2026 (very recent!)\n- **Why relevant:** Addresses the problem of steering one behavior while **not degrading others** -- directly relevant if the proposal steers CSB and CEO independently. Proposes constrained optimization weighted by empirical second-moment matrix to minimize collateral effects. Essential methodological reference for ensuring bias-specific steering doesn't interfere.\n\n---\n\n**9. \"Shifting Perspectives: Steering Vector Ensembles for Robust Bias Mitigation in LLMs\"**\n- **Authors:** Zara Siddique, Irtaza Khalid, Liam D. Turner, Luis Espinosa-Anke\n- **arXiv ID:** 2503.05371\n- **Date:** March 7, 2025 (revised March 28, 2026)\n- **Why relevant:** Uses **8 simultaneous steering vectors**, one per bias axis, combined via ensemble averaging. Demonstrates that multiple bias-specific vectors can be applied concurrently. Directly relevant to the proposal's multi-bias correction approach.\n\n---\n\n**10. \"Activation Steering with a Feedback Controller\" (PID Steering)**\n- **Authors:** Dung V. Nguyen, Hieu M. Vu, Nhi Y. Pham, Lei Zhang, Tan M. Nguyen\n- **arXiv ID:** 2510.04309\n- **Date:** October 5, 2025 (revised May 16, 2026)\n- **Why relevant:** Formalizes steering as a control problem (PID controller) with proportional, integral, and derivative terms. The integral term provides persistent correction across layers, and the derivative prevents overshoot. Relevant as an alternative framework for the proposal's correction mechanism.\n\n---\n\n**11. \"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation\"**\n- **Authors:** Nan Zhuang, Wenshuo Wang, Lekai Qian, Yuxiao Wang, Boyu Cao, Qi Liu\n- **arXiv ID:** 2512.03082\n- **Date:** November 28, 2025\n- **Why relevant:** Directly targets CSB in LLMs but uses a **fine-tuning approach** (training on generated unbiased reasoning data) rather than activation steering. Achieves 81.5-94.3% improvement. The proposal should cite this as an alternative approach to CSB mitigation and argue for the advantages of inference-time activation correction.\n\n---\n\n**12. \"FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering\"**\n- **Authors:** Yichen Li, Zhiting Fan, Ruizhe Chen, et al.\n- **arXiv ID:** 2504.14492\n- **Date:** April 20, 2025 (ACL 2025 Findings)\n- **Why relevant:** Detects bias signatures via lightweight linear classifiers on activations, computes debiasing steering vectors from contrastive pairs, and applies dynamic correction at inference time. Achieves >90% linear separability of bias in intermediate layers. Methodologically very close to what the proposal would do for CSB/CEO detection and correction.\n\n---\n\n### TIER 3: RELEVANT BACKGROUND / SUPPORTING WORK\n\n---\n\n**13. \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\" (CCPS)**\n- **Authors:** Reza Khanmohammadi et al.\n- **arXiv ID:** 2505.21772\n- **Date:** May 27, 2025\n- **Why relevant:** Per-instance calibration via probing hidden state stability. Achieves 55% ECE reduction. Relevant as an alternative per-instance calibration approach that does not use steering.\n\n---\n\n**14. \"Beacon: Single-Turn Diagnosis and Mitigation of Latent Sycophancy in LLMs\"**\n- **Authors:** Sanskar Pandey, Ruhaan Chopra, Angkul Puniya, Sohom Pal\n- **arXiv ID:** 2510.16727\n- **Date:** October 19, 2025 (revised May 17, 2026)\n- **Why relevant:** Decomposes sycophancy into distinct linguistic and affective components, proposes activation-level interventions. Relevant to understanding CSB as related to sycophancy.\n\n---\n\n**15. \"Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of LLMs\"**\n- **Authors:** David Bani-Harouni et al.\n- **arXiv ID:** 2503.02623\n- **Date:** March 4, 2025 (ICLR 2026)\n- **Why relevant:** RL-based calibration that penalizes both over- and under-confidence. Alternative training-time approach to the proposal's inference-time method.\n\n---\n\n**16. \"Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs\"**\n- **Authors:** Shivam Dubey\n- **arXiv ID:** 2508.09019\n- **Date:** August 12, 2025\n- **Why relevant:** Trains linear probes to detect bias, computes steering vectors from contrasting biased/neutral activations. Foundational methodology for the proposal.\n\n---\n\n### KEY GAPS THE PROPOSAL WOULD FILL\n\nBased on this search, the proposal's unique contribution appears to be the **combination** of:\n1. **Decomposing** miscalibration into specific competing biases (CSB + CEO) -- building on Kumaran et al. 2026 (behavioral finding) but going mechanistic\n2. **Identifying activation-level signatures** for each bias separately -- building on Zhao et al. 2604.01457 (overconfidence only) and CogBias 2604.01366 (cognitive biases generally, not calibration-specific)\n3. **Applying targeted, per-instance correction** for each bias independently -- building on CORAL, AUSteer, FairSteer methods\n\nNo single paper found does all three together. The closest threats are:\n- Kumaran et al. (Nature MI, April 2026) -- same behavioral decomposition but no activation correction\n- Zhao et al. (April 2026) -- mechanistic overconfidence analysis but only one bias, no decomposition\n- CogBias (April 2026) -- multi-bias activation steering but not for calibration-specific biases\n\nSources:\n- [Competing Biases underlie Overconfidence and Underconfidence in LLMs](https://www.nature.com/articles/s42256-026-01217-9)\n- [Wired for Overconfidence (2604.01457)](https://arxiv.org/abs/2604.01457)\n- [CogBias (2604.01366)](https://arxiv.org/abs/2604.01366)\n- [Sycophancy Is Not One Thing (2509.21305)](https://arxiv.org/abs/2509.21305)\n- [CORAL (2602.06022)](https://arxiv.org/abs/2602.06022)\n- [AUSteer: Fine-Grained Activation Steering (2602.04428)](https://arxiv.org/abs/2602.04428)\n- [Discovery of Hidden Miscalibration Regimes (2605.13484)](https://arxiv.org/abs/2605.13484)\n- [Minimizing Collateral Damage in Activation Steering (2605.01167)](https://arxiv.org/abs/2605.01167)\n- [Shifting Perspectives: Steering Vector Ensembles (2503.05371)](https://arxiv.org/abs/2503.05371)\n- [PID Steering (2510.04309)](https://arxiv.org/abs/2510.04309)\n- [Alleviating Choice Supportive Bias via RDG (2512.03082)](https://arxiv.org/abs/2512.03082)\n- [FairSteer (2504.14492)](https://arxiv.org/abs/2504.14492)\n- [CCPS: Probing Perturbed Representation Stability (2505.21772)](https://arxiv.org/abs/2505.21772)\n- [Beacon: Sycophancy Diagnosis (2510.16727)](https://arxiv.org/abs/2510.16727)\n- [Rewarding Doubt (2503.02623)](https://arxiv.org/abs/2503.02623)\n- [Activation Steering for Bias Mitigation (2508.09019)](https://arxiv.org/abs/2508.09019)\n- [Activation Steering Field Guide](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)\n- [MERA: Mechanistic Error Reduction with Abstention](https://openreview.net/forum?id=fUCPq5RvmH)"
      }
    ],
    "totalDurationMs": 224451,
    "totalTokens": 39610,
    "totalToolUseCount": 41,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2483,
      "cache_read_input_tokens": 33350,
      "output_tokens": 3776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2483
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3776,
          "cache_read_input_tokens": 33350,
          "cache_creation_input_tokens": 2483,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2483,
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
      "otherToolCount": 41
    }
  },
  "sourceToolAssistantUUID": "b56c38c3-7705-4c78-a338-2008381fabdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T16:45:37.238Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Tt38K7V4XmLQ64UmAoV94S`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify venue deadlines and models",
  "prompt": "I need to verify three things:\n\n1. ICLR 2027 submission deadline - search for \"ICLR 2027 deadline\" or \"ICLR 2027 call for papers\". The proposal claims it's estimated ~Sep 24, 2026. Check if this is reasonable based on ICLR 2026's deadline pattern.\n\n2. Gemma 4 31B Dense model - search for \"Gemma 4 31B\" or \"Google Gemma 4 model\" to verify this model exists. Also check if Qwen3-8B exists.\n\n3. Spherical Steering ICML 2026 - search for \"Spherical Steering ICML 2026\" or arXiv 2602.08169 to verify this paper exists and was accepted at ICML 2026.\n\n4. MERA ICML 2025 - search for \"To Steer or Not to Steer ICML 2025\" or arXiv 2510.13290 to verify.\n\n5. ODESteer ICLR 2026 - search for arXiv 2602.17560 to verify.\n\nReport what you find for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7244ea0-a9dc-4138-9d8d-b37b089e2bf7",
  "isSidechain": false,
  "requestId": "req_011CbCGMc9CEQrw8yVktD1vp",
  "type": "assistant",
  "uuid": "47f50232-15aa-44f3-9272-e2b16b0c8c5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmRqSoYBzYCroH2DUQGkR2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4309,
      "cache_read_input_tokens": 40996,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4309,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 376,
          "cache_read_input_tokens": 40996,
          "cache_creation_input_tokens": 4309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4309
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "47f50232-15aa-44f3-9272-e2b16b0c8c5c",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose competing calibration biases via activation steering",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Tool result

_source line 23 · 2026-05-19T16:46:26.661Z_

<details><summary>↩ Tool result · `toolu_01Tt38K7V4XmLQ64UmAoV94S`</summary>

```text
Here are the findings for all five items:

---

**1. ICLR 2027 Submission Deadline (~Sep 24, 2026 estimate)**

The official ICLR 2027 call for papers has **not yet been announced**. However, the estimate of ~Sep 24, 2026 is **very reasonable** based on the ICLR 2026 pattern:
- ICLR 2026 abstract deadline: **September 19, 2025**
- ICLR 2026 full paper deadline: **September 24, 2025**
- ICLR 2026 conference: April 23-27, 2026

If ICLR 2027 follows the same annual cadence, a submission deadline around late September 2026 is a well-founded estimate. The proposal's "~Sep 24, 2026" figure directly mirrors the ICLR 2026 full paper deadline date shifted by one year.

**Verdict: Reasonable estimate, not yet officially confirmed.**

---

**2. Gemma 4 31B Dense Model and Qwen3-8B**

Both models are **confirmed to exist**:

- **Gemma 4 31B**: A 30.7B-parameter **dense** multimodal model from Google DeepMind. It supports 256K context, configurable thinking mode, native function calling, and 140+ languages. It is available on Hugging Face (`google/gemma-4-31B` and `google/gemma-4-31B-it`), OpenRouter, NVIDIA NIM, and LM Studio. Ranked #3 open model on the Arena AI text leaderboard.

- **Qwen3-8B**: An 8.2B-parameter dense causal language model from Alibaba. It supports dual thinking/non-thinking modes, 100+ languages, and 32K native context (131K with YaRN). Available on Hugging Face (`Qwen/Qwen3-8B`).

**Verdict: Both models confirmed.**

---

**3. Spherical Steering -- ICML 2026 (arXiv 2602.08169)**

**Confirmed.** The paper "Spherical Steering: Geometry-Aware Activation Rotation for Language Models" (arXiv [2602.08169](https://arxiv.org/abs/2602.08169)) by Zejia You, Chunyuan Deng, and Hanjie Chen is tagged as **[ICML 2026]** on its [GitHub repository](https://github.com/chili-lab/Spherical-Steering). The paper proposes activation rotation along geodesics rather than activation addition, addressing representation collapse concerns in steering.

**Verdict: Paper exists and is accepted at ICML 2026.**

---

**4. MERA / "To Steer or Not to Steer" -- ICML 2025 (arXiv 2510.13290)**

**Confirmed.** The paper "To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models" (arXiv [2510.13290](https://arxiv.org/abs/2510.13290)) was published at **ICML 2025** (PMLR 267). It has an [official ICML 2025 poster page](https://icml.cc/virtual/2025/poster/44524). The paper introduces the MERA framework for principled, adaptive activation steering with abstention.

**Verdict: Paper exists and was published at ICML 2025.**

---

**5. ODESteer -- ICLR 2026 (arXiv 2602.17560)**

**Partially confirmed.** The paper "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment" (arXiv [2602.17560](https://arxiv.org/abs/2602.17560)) exists, submitted February 19, 2026. It appears in [Paper Digest's ICLR 2026 highlights](https://www.paperdigest.org/2026/02/iclr-2026-papers-highlights/), suggesting it is associated with ICLR 2026. However, I could not find a definitive official acceptance confirmation (e.g., an OpenReview page marking it as accepted). Given ICLR 2026 is April 23-27, 2026 and we are currently in May 2026, it is likely accepted, but the evidence is indirect (Paper Digest listing + timing).

**Verdict: Paper exists; ICLR 2026 association is strongly supported but not 100% definitively confirmed from the search results.**

---

Sources:
- [ICLR 2026 Dates and Deadlines](https://iclr.cc/Conferences/2026/Dates)
- [ICLR 2026 Call for Papers](https://iclr.cc/Conferences/2026/CallForPapers)
- [Gemma 4 31B on Hugging Face](https://huggingface.co/google/gemma-4-31B)
- [Gemma 4 Blog Post](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)
- [Qwen3-8B on Hugging Face](https://huggingface.co/Qwen/Qwen3-8B)
- [Spherical Steering on arXiv](https://arxiv.org/abs/2602.08169)
- [Spherical Steering GitHub (ICML 2026)](https://github.com/chili-lab/Spherical-Steering)
- [MERA on arXiv](https://arxiv.org/abs/2510.13290)
- [MERA ICML 2025 Poster](https://icml.cc/virtual/2025/poster/44524)
- [ODESteer on arXiv](https://arxiv.org/abs/2602.17560)
- [Paper Digest: ICLR 2026 Highlights](https://www.paperdigest.org/2026/02/iclr-2026-papers-highlights/)

agentId: a90328eeee91f5a22 (use SendMessage with to: 'a90328eeee91f5a22' to continue this agent)
&lt;usage>total_tokens: 16680
tool_uses: 8
duration_ms: 49418&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47f50232-15aa-44f3-9272-e2b16b0c8c5c",
  "isSidechain": false,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "type": "user",
  "uuid": "8221be92-318f-4e7a-b00e-d5c2573bf820",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify three things:\n\n1. ICLR 2027 submission deadline - search for \"ICLR 2027 deadline\" or \"ICLR 2027 call for papers\". The proposal claims it's estimated ~Sep 24, 2026. Check if this is reasonable based on ICLR 2026's deadline pattern.\n\n2. Gemma 4 31B Dense model - search for \"Gemma 4 31B\" or \"Google Gemma 4 model\" to verify this model exists. Also check if Qwen3-8B exists.\n\n3. Spherical Steering ICML 2026 - search for \"Spherical Steering ICML 2026\" or arXiv 2602.08169 to verify this paper exists and was accepted at ICML 2026.\n\n4. MERA ICML 2025 - search for \"To Steer or Not to Steer ICML 2025\" or arXiv 2510.13290 to verify.\n\n5. ODESteer ICLR 2026 - search for arXiv 2602.17560 to verify.\n\nReport what you find for each.",
    "agentId": "a90328eeee91f5a22",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings for all five items:\n\n---\n\n**1. ICLR 2027 Submission Deadline (~Sep 24, 2026 estimate)**\n\nThe official ICLR 2027 call for papers has **not yet been announced**. However, the estimate of ~Sep 24, 2026 is **very reasonable** based on the ICLR 2026 pattern:\n- ICLR 2026 abstract deadline: **September 19, 2025**\n- ICLR 2026 full paper deadline: **September 24, 2025**\n- ICLR 2026 conference: April 23-27, 2026\n\nIf ICLR 2027 follows the same annual cadence, a submission deadline around late September 2026 is a well-founded estimate. The proposal's \"~Sep 24, 2026\" figure directly mirrors the ICLR 2026 full paper deadline date shifted by one year.\n\n**Verdict: Reasonable estimate, not yet officially confirmed.**\n\n---\n\n**2. Gemma 4 31B Dense Model and Qwen3-8B**\n\nBoth models are **confirmed to exist**:\n\n- **Gemma 4 31B**: A 30.7B-parameter **dense** multimodal model from Google DeepMind. It supports 256K context, configurable thinking mode, native function calling, and 140+ languages. It is available on Hugging Face (`google/gemma-4-31B` and `google/gemma-4-31B-it`), OpenRouter, NVIDIA NIM, and LM Studio. Ranked #3 open model on the Arena AI text leaderboard.\n\n- **Qwen3-8B**: An 8.2B-parameter dense causal language model from Alibaba. It supports dual thinking/non-thinking modes, 100+ languages, and 32K native context (131K with YaRN). Available on Hugging Face (`Qwen/Qwen3-8B`).\n\n**Verdict: Both models confirmed.**\n\n---\n\n**3. Spherical Steering -- ICML 2026 (arXiv 2602.08169)**\n\n**Confirmed.** The paper \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models\" (arXiv [2602.08169](https://arxiv.org/abs/2602.08169)) by Zejia You, Chunyuan Deng, and Hanjie Chen is tagged as **[ICML 2026]** on its [GitHub repository](https://github.com/chili-lab/Spherical-Steering). The paper proposes activation rotation along geodesics rather than activation addition, addressing representation collapse concerns in steering.\n\n**Verdict: Paper exists and is accepted at ICML 2026.**\n\n---\n\n**4. MERA / \"To Steer or Not to Steer\" -- ICML 2025 (arXiv 2510.13290)**\n\n**Confirmed.** The paper \"To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models\" (arXiv [2510.13290](https://arxiv.org/abs/2510.13290)) was published at **ICML 2025** (PMLR 267). It has an [official ICML 2025 poster page](https://icml.cc/virtual/2025/poster/44524). The paper introduces the MERA framework for principled, adaptive activation steering with abstention.\n\n**Verdict: Paper exists and was published at ICML 2025.**\n\n---\n\n**5. ODESteer -- ICLR 2026 (arXiv 2602.17560)**\n\n**Partially confirmed.** The paper \"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment\" (arXiv [2602.17560](https://arxiv.org/abs/2602.17560)) exists, submitted February 19, 2026. It appears in [Paper Digest's ICLR 2026 highlights](https://www.paperdigest.org/2026/02/iclr-2026-papers-highlights/), suggesting it is associated with ICLR 2026. However, I could not find a definitive official acceptance confirmation (e.g., an OpenReview page marking it as accepted). Given ICLR 2026 is April 23-27, 2026 and we are currently in May 2026, it is likely accepted, but the evidence is indirect (Paper Digest listing + timing).\n\n**Verdict: Paper exists; ICLR 2026 association is strongly supported but not 100% definitively confirmed from the search results.**\n\n---\n\nSources:\n- [ICLR 2026 Dates and Deadlines](https://iclr.cc/Conferences/2026/Dates)\n- [ICLR 2026 Call for Papers](https://iclr.cc/Conferences/2026/CallForPapers)\n- [Gemma 4 31B on Hugging Face](https://huggingface.co/google/gemma-4-31B)\n- [Gemma 4 Blog Post](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)\n- [Qwen3-8B on Hugging Face](https://huggingface.co/Qwen/Qwen3-8B)\n- [Spherical Steering on arXiv](https://arxiv.org/abs/2602.08169)\n- [Spherical Steering GitHub (ICML 2026)](https://github.com/chili-lab/Spherical-Steering)\n- [MERA on arXiv](https://arxiv.org/abs/2510.13290)\n- [MERA ICML 2025 Poster](https://icml.cc/virtual/2025/poster/44524)\n- [ODESteer on arXiv](https://arxiv.org/abs/2602.17560)\n- [Paper Digest: ICLR 2026 Highlights](https://www.paperdigest.org/2026/02/iclr-2026-papers-highlights/)"
      }
    ],
    "totalDurationMs": 49418,
    "totalTokens": 16680,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 702,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 13061,
      "output_tokens": 1496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 702,
          "output_tokens": 1496,
          "cache_read_input_tokens": 13061,
          "cache_creation_input_tokens": 1421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1421,
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
  "sourceToolAssistantUUID": "47f50232-15aa-44f3-9272-e2b16b0c8c5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T16:46:40.598Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01C6ti8oV3ZPH3pUDC6kD3ki`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for very recent competing work",
  "prompt": "Search for very recent papers (April-May 2026) that might compete with a proposal about decomposing LLM miscalibration into competing biases for targeted activation correction. Use the following search queries:\n\n1. Search: site:arxiv.org \"calibration\" \"activation steering\" OR \"activation intervention\" 2026\n2. Search: arxiv LLM overconfidence underconfidence mechanistic May 2026\n3. Search: \"competing biases\" OR \"opposing biases\" language model activation 2026\n4. Search: site:arxiv.org \"bias decomposition\" steering language model 2026\n5. Search: arxiv confidence calibration mechanistic interpretability April May 2026\n6. Search: \"Shifting Perspectives\" steering vector ensemble bias 2025 2026 (to verify paper arXiv 2503.05371)\n7. Search: \"FairSteer\" activation steering debiasing 2025\n8. Search: \"Beacon\" sycophancy latent activation 2025 2026\n9. Search: \"PID steering\" OR \"feedback controller\" activation steering 2025 2026\n10. Search: \"Contextual Linear Activation Steering\" arXiv 2604.24693\n\nFocus on finding papers NOT already cited in the proposal. The proposal already cites: Kumaran et al. (2507.03120, 2603.17839), CogBias (2604.01366), Billa (2604.15557), Liu (2605.05715), Patel et al. (2604.19974), Kobalczyk (2605.13484), Miao & Ungar (2603.25052), MERA (2510.13290), Spherical Steering (2602.08169), ODESteer (2602.17560), SteerConf (2503.02863), CCPS (2505.21772), Sycophancy Is Not One Thing (2509.21305), CORAL (2602.06022), COAST (2605.01167), Curveball (2603.09313), FLAS (2605.05892), etc.\n\nReport any paper that addresses calibration+activation intervention or multi-bias decomposition that is NOT in the above list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8221be92-318f-4e7a-b00e-d5c2573bf820",
  "isSidechain": false,
  "requestId": "req_011CbCGRstM8CzwCGJZRt5he",
  "type": "assistant",
  "uuid": "59dc9df5-70d1-48e7-8db9-aae798db4d31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lc5LvfWie53yWMzzHtWAgU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 45305,
      "output_tokens": 617,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 617,
          "cache_read_input_tokens": 45305,
          "cache_creation_input_tokens": 1951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1951
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

_source line 25 · 2026-05-19T16:49:24.716Z_

<details><summary>↩ Tool result · `toolu_01C6ti8oV3ZPH3pUDC6kD3ki`</summary>

```text
Now I have a comprehensive picture. Let me compile the findings. Based on all searches, here are the papers that are NOT in the already-cited list and are potentially competing with the proposal about decomposing LLM miscalibration into competing biases for targeted activation correction:

---

## Competitive Landscape Report: Papers NOT Already Cited

### HIGHEST RELEVANCE -- Direct Competitors

**1. "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs" (arXiv:2604.01457, April 2026)**
- Authors: Tianyi Zhao, Yinhan He, Wendy Zheng, Yujie Zhang, Chen Chen (U. Virginia)
- This is the strongest potential competitor. It presents a circuit-level mechanistic analysis of inflated verbalized confidence in LLMs, identifying specific MLP blocks and attention heads in middle-to-late layers that causally write a "confidence-inflation signal." They demonstrate targeted inference-time interventions on these circuits that substantially improve calibration. This directly overlaps with the proposal's core thesis of using mechanistic understanding of confidence to perform targeted activation corrections.
- [Paper link](https://arxiv.org/abs/2604.01457)

**2. "Contextual Linear Activation Steering" (CLAS) (arXiv:2604.24693, April 2026)**
- Authors: Brandon Hsu, Daniel Beaglehole, Adityanarayanan Radhakrishnan, Mikhail Belkin (UCSD, MIT, Broad Institute)
- Proposes dynamically adapting linear activation steering to context-dependent steering strengths, addressing the limitation of fixed steering strength across all tokens. Outperforms standard linear steering and matches ReFT/LoRA across 11 benchmarks and 4 model families. This is relevant because the proposal likely needs context-adaptive steering; CLAS shows a competing approach to the same problem.
- [Paper link](https://arxiv.org/abs/2604.24693)

**3. "Beacon: Single-Turn Diagnosis and Mitigation of Latent Sycophancy in LLMs" (arXiv:2510.16727, October 2025)**
- Demonstrates that sycophancy decomposes into discrete sub-biases (hedged sycophancy, tone penalty, emotional framing, fluency bias) and applies cluster-specific activation steering to manipulate sycophancy-related activation subspaces. This is a direct precedent for the "decompose bias into sub-components, then steer each" paradigm that the proposal advocates for confidence miscalibration.
- [Paper link](https://arxiv.org/abs/2510.16727)

**4. "Activation Steering with a Feedback Controller" (PID Steering) (arXiv:2510.04309, October 2025, revised March 2026, ICLR 2026)**
- Authors: Dung V. Nguyen et al.
- Formalizes activation steering via control theory (PID controllers). The integral term accumulates errors for persistent corrections across layers and the derivative term prevents overshoot. Directly relevant as an alternative framework for dynamically adjusting activation corrections -- the proposal's targeted correction could be seen as a special case of proportional control, while PID offers a more principled multi-layer approach.
- [Paper link](https://arxiv.org/abs/2510.04309)

### HIGH RELEVANCE -- Closely Related Methods

**5. "Fine-Grained Activation Steering: Steering Less, Achieving More" (AUSteer) (arXiv:2602.04428, February 2026)**
- Decomposes block-level activations into fine-grained "atomic unit" (AU)-level activations, showing heterogeneity where different AUs control distinct token distributions. Proposes steering at AU granularity with adaptive per-input strengths. This decomposition approach parallels the proposal's idea of decomposing miscalibration into component biases, but operates at the activation unit level rather than the bias-type level.
- [Paper link](https://arxiv.org/abs/2602.04428)

**6. "Don't Lose Focus: Activation Steering via Key-Orthogonal Projections" (SKOP) (arXiv:2605.06342, May 2026)**
- Authors: Haoyan Luo, Mateo Espinosa Zarlenga, Mateja Jamnik
- Identifies that steering vectors cause "attention rerouting" that degrades reasoning. SKOP constrains steering to preserve attention on focus tokens, reducing utility degradation by 5-7x while retaining 95% of steering efficacy. Relevant because calibration steering could similarly degrade reasoning quality; SKOP's approach is complementary/competing.
- [Paper link](https://arxiv.org/abs/2605.06342)

**7. "Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering" (arXiv:2511.00617, November 2025, revised March 2026)**
- Authors: Eric Bigelow et al. (Harvard, Stanford, MIT)
- Develops a Bayesian account unifying in-context learning and activation steering: steering changes concept priors, while ICL accumulates evidence. Provides a closed-form Bayesian model predictive of LLM behavior. Relevant theoretical framework that could inform or compete with the proposal's mechanistic decomposition.
- [Paper link](https://arxiv.org/abs/2511.00617)

**8. "COLD-Steer: Steering LLMs via In-Context One-step Learning Dynamics" (arXiv:2603.06495, March 2026, ICLR 2026)**
- Training-free framework that approximates representational changes from gradient descent on in-context examples. Relevant as an alternative efficient steering method that could be applied to calibration without requiring explicit bias decomposition.
- [Paper link](https://arxiv.org/abs/2603.06495)

**9. "Shifting Perspectives: Steering Vector Ensembles for Robust Bias Mitigation in LLMs" (arXiv:2503.05371, March 2025, EACL 2026)**
- Computes 8 steering vectors for different social bias axes and uses ensembles. Directly demonstrates multi-bias-axis steering vector decomposition, which is the same structural approach as the proposal but for social bias rather than confidence bias.
- [Paper link](https://arxiv.org/abs/2503.05371)

**10. "FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering" (arXiv:2504.14492, April 2025, ACL 2025)**
- Uses a lightweight linear classifier to detect bias signatures in activations (90%+ linear separability in intermediate layers), then applies dynamically computed debiasing steering vectors. The detect-then-steer paradigm closely mirrors what the proposal would need for detecting which type of miscalibration is active before applying targeted correction.
- [Paper link](https://arxiv.org/abs/2504.14492)

### MODERATE RELEVANCE -- Useful Context

**11. "Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk" (arXiv:2602.04896, February 2026)**
- Important cautionary finding: benign steering vectors can erode safety guardrails and increase jailbreak attack success rates to 80%+. The proposal should address whether targeted calibration corrections might have similar externalities.
- [Paper link](https://arxiv.org/abs/2602.04896)

**12. "K-Steering: Beyond Linear Steering: Unified Multi-Attribute Control for Language Models" (arXiv:2505.24535, May 2025, EMNLP 2025)**
- Non-linear multi-label classifier for multi-attribute steering via gradients. Avoids linearity assumptions and allows dynamic composition without retraining. Relevant alternative to additive multi-bias steering vectors.
- [Paper link](https://arxiv.org/abs/2505.24535)

**13. "MAT-Steer: Multi-Attribute Targeted Steering" (arXiv:2502.12446, February 2025, ACL 2025)**
- Addresses multi-attribute steering with conflict handling (e.g., helpfulness vs. toxicity reduction). Token-level selective intervention. Relevant framework for handling potentially conflicting calibration corrections.
- [Paper link](https://arxiv.org/abs/2502.12446)

**14. "Compositional Steering of LLMs with Steering Tokens" (arXiv:2601.05062, January 2026)**
- Multi-behavior steering via tokens rather than activation-space vectors, with composition tokens that generalize to unseen behavior combinations. An alternative paradigm to activation-space decomposition.
- [Paper link](https://arxiv.org/abs/2601.05062)

**15. "Guiding Giants: Lightweight Controllers for Weighted Activation Steering" (arXiv:2505.20309, May 2025)**
- Trainable controller network that predicts global scaling + layer-specific weights for steering, learning to discriminatively apply interventions. Relevant controller architecture for adaptive calibration correction.
- [Paper link](https://arxiv.org/abs/2505.20309)

**16. "LinEAS: End-to-end Learning of Activation Steering with a Distributional Loss" (arXiv:2503.10679, NeurIPS 2025)**
- Apple Research. Global distributional loss for learning steering across all layers simultaneously, with sparsifying norms for automatic neuron/layer selection. Could be applied to calibration steering.
- [Paper link](https://arxiv.org/abs/2503.10679)

**17. "PIXEL: Adaptive Steering Via Position-wise Injection with eXact Estimated Levels under Subspace Calibration" (arXiv:2510.10205, October 2025)**
- Position-wise activation steering with subspace calibration and orthogonal residual correction. The "subspace calibration" aspect is directly relevant terminology.
- [Paper link](https://arxiv.org/abs/2510.10205)

**18. "The Dunning-Kruger Effect in Large Language Models" (arXiv:2603.09985, March 2026)**
- Empirical study showing poorly performing models display markedly higher overconfidence (ECE up to 0.726). Relevant empirical context for the proposal's calibration claims.
- [Paper link](https://arxiv.org/abs/2603.09985)

**19. "The Confidence Dichotomy: Analyzing and Mitigating Miscalibration in Tool-Use Agents" (arXiv:2601.07264, January 2026)**
- Reveals tool-dependent calibration divergence: evidence tools induce overconfidence, verification tools preserve calibration. Uses RL for joint accuracy+calibration optimization. Relevant for domain-specific calibration.
- [Paper link](https://arxiv.org/abs/2601.07264)

**20. "Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection" (arXiv:2603.06604, March 2026)**
- Shows SFT yields well-calibrated confidence via MLE, while RL methods induce overconfidence. Proposes post-RL SFT with self-distillation. Different approach (training-time) but relevant analysis.
- [Paper link](https://arxiv.org/abs/2603.06604)

**21. "Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering" (AdaRAS) (arXiv:2601.19847, January 2026)**
- Identifies reasoning-critical neurons via polarity-aware criteria and adaptively steers their activations. 13%+ gains on AIME benchmarks. The neuron-identification-then-targeted-steering paradigm parallels the proposal's approach.
- [Paper link](https://arxiv.org/abs/2601.19847)

**22. "DSO: Direct Steering Optimization for Bias Mitigation" (arXiv:2512.15926, December 2025, Apple Research)**
- Uses RL to learn linear transformations for activation steering, enabling controllable bias-accuracy tradeoffs. Different optimization approach to learning steering directions.
- [Paper link](https://arxiv.org/abs/2512.15926)

---

### Summary Assessment

The **most threatening competitor** is **"Wired for Overconfidence" (2604.01457)**, which performs exactly the kind of mechanistic circuit-level analysis of confidence inflation that the proposal describes, and demonstrates targeted inference-time interventions on those circuits for improved calibration. However, it focuses only on overconfidence (one direction), while the proposal's key differentiator would be the decomposition into *competing* biases (both over- and under-confidence) and their simultaneous targeted correction.

The **second major competitor** is **Beacon (2510.16727)**, which already demonstrates decomposing a single behavioral phenomenon (sycophancy) into multiple sub-biases and applying cluster-specific activation steering -- the same paradigm the proposal advocates, just for a different target behavior.

The **PID Steering (2510.04309)** and **AUSteer (2602.04428)** papers present alternative frameworks for the "how to steer" component that could subsume or compete with the proposal's correction mechanism.

The proposal should explicitly differentiate from all of these, particularly emphasizing the novel combination of (a) decomposing calibration error into competing bias types and (b) applying bias-specific targeted activation corrections -- something none of the above papers do in an integrated manner for the calibration domain.

agentId: ad6c252b6fd22aa15 (use SendMessage with to: 'ad6c252b6fd22aa15' to continue this agent)
&lt;usage>total_tokens: 43791
tool_uses: 40
duration_ms: 164111&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59dc9df5-70d1-48e7-8db9-aae798db4d31",
  "isSidechain": false,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "type": "user",
  "uuid": "383224ed-21f1-4874-85c5-08b14e47bdd1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for very recent papers (April-May 2026) that might compete with a proposal about decomposing LLM miscalibration into competing biases for targeted activation correction. Use the following search queries:\n\n1. Search: site:arxiv.org \"calibration\" \"activation steering\" OR \"activation intervention\" 2026\n2. Search: arxiv LLM overconfidence underconfidence mechanistic May 2026\n3. Search: \"competing biases\" OR \"opposing biases\" language model activation 2026\n4. Search: site:arxiv.org \"bias decomposition\" steering language model 2026\n5. Search: arxiv confidence calibration mechanistic interpretability April May 2026\n6. Search: \"Shifting Perspectives\" steering vector ensemble bias 2025 2026 (to verify paper arXiv 2503.05371)\n7. Search: \"FairSteer\" activation steering debiasing 2025\n8. Search: \"Beacon\" sycophancy latent activation 2025 2026\n9. Search: \"PID steering\" OR \"feedback controller\" activation steering 2025 2026\n10. Search: \"Contextual Linear Activation Steering\" arXiv 2604.24693\n\nFocus on finding papers NOT already cited in the proposal. The proposal already cites: Kumaran et al. (2507.03120, 2603.17839), CogBias (2604.01366), Billa (2604.15557), Liu (2605.05715), Patel et al. (2604.19974), Kobalczyk (2605.13484), Miao & Ungar (2603.25052), MERA (2510.13290), Spherical Steering (2602.08169), ODESteer (2602.17560), SteerConf (2503.02863), CCPS (2505.21772), Sycophancy Is Not One Thing (2509.21305), CORAL (2602.06022), COAST (2605.01167), Curveball (2603.09313), FLAS (2605.05892), etc.\n\nReport any paper that addresses calibration+activation intervention or multi-bias decomposition that is NOT in the above list.",
    "agentId": "ad6c252b6fd22aa15",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Let me compile the findings. Based on all searches, here are the papers that are NOT in the already-cited list and are potentially competing with the proposal about decomposing LLM miscalibration into competing biases for targeted activation correction:\n\n---\n\n## Competitive Landscape Report: Papers NOT Already Cited\n\n### HIGHEST RELEVANCE -- Direct Competitors\n\n**1. \"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs\" (arXiv:2604.01457, April 2026)**\n- Authors: Tianyi Zhao, Yinhan He, Wendy Zheng, Yujie Zhang, Chen Chen (U. Virginia)\n- This is the strongest potential competitor. It presents a circuit-level mechanistic analysis of inflated verbalized confidence in LLMs, identifying specific MLP blocks and attention heads in middle-to-late layers that causally write a \"confidence-inflation signal.\" They demonstrate targeted inference-time interventions on these circuits that substantially improve calibration. This directly overlaps with the proposal's core thesis of using mechanistic understanding of confidence to perform targeted activation corrections.\n- [Paper link](https://arxiv.org/abs/2604.01457)\n\n**2. \"Contextual Linear Activation Steering\" (CLAS) (arXiv:2604.24693, April 2026)**\n- Authors: Brandon Hsu, Daniel Beaglehole, Adityanarayanan Radhakrishnan, Mikhail Belkin (UCSD, MIT, Broad Institute)\n- Proposes dynamically adapting linear activation steering to context-dependent steering strengths, addressing the limitation of fixed steering strength across all tokens. Outperforms standard linear steering and matches ReFT/LoRA across 11 benchmarks and 4 model families. This is relevant because the proposal likely needs context-adaptive steering; CLAS shows a competing approach to the same problem.\n- [Paper link](https://arxiv.org/abs/2604.24693)\n\n**3. \"Beacon: Single-Turn Diagnosis and Mitigation of Latent Sycophancy in LLMs\" (arXiv:2510.16727, October 2025)**\n- Demonstrates that sycophancy decomposes into discrete sub-biases (hedged sycophancy, tone penalty, emotional framing, fluency bias) and applies cluster-specific activation steering to manipulate sycophancy-related activation subspaces. This is a direct precedent for the \"decompose bias into sub-components, then steer each\" paradigm that the proposal advocates for confidence miscalibration.\n- [Paper link](https://arxiv.org/abs/2510.16727)\n\n**4. \"Activation Steering with a Feedback Controller\" (PID Steering) (arXiv:2510.04309, October 2025, revised March 2026, ICLR 2026)**\n- Authors: Dung V. Nguyen et al.\n- Formalizes activation steering via control theory (PID controllers). The integral term accumulates errors for persistent corrections across layers and the derivative term prevents overshoot. Directly relevant as an alternative framework for dynamically adjusting activation corrections -- the proposal's targeted correction could be seen as a special case of proportional control, while PID offers a more principled multi-layer approach.\n- [Paper link](https://arxiv.org/abs/2510.04309)\n\n### HIGH RELEVANCE -- Closely Related Methods\n\n**5. \"Fine-Grained Activation Steering: Steering Less, Achieving More\" (AUSteer) (arXiv:2602.04428, February 2026)**\n- Decomposes block-level activations into fine-grained \"atomic unit\" (AU)-level activations, showing heterogeneity where different AUs control distinct token distributions. Proposes steering at AU granularity with adaptive per-input strengths. This decomposition approach parallels the proposal's idea of decomposing miscalibration into component biases, but operates at the activation unit level rather than the bias-type level.\n- [Paper link](https://arxiv.org/abs/2602.04428)\n\n**6. \"Don't Lose Focus: Activation Steering via Key-Orthogonal Projections\" (SKOP) (arXiv:2605.06342, May 2026)**\n- Authors: Haoyan Luo, Mateo Espinosa Zarlenga, Mateja Jamnik\n- Identifies that steering vectors cause \"attention rerouting\" that degrades reasoning. SKOP constrains steering to preserve attention on focus tokens, reducing utility degradation by 5-7x while retaining 95% of steering efficacy. Relevant because calibration steering could similarly degrade reasoning quality; SKOP's approach is complementary/competing.\n- [Paper link](https://arxiv.org/abs/2605.06342)\n\n**7. \"Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering\" (arXiv:2511.00617, November 2025, revised March 2026)**\n- Authors: Eric Bigelow et al. (Harvard, Stanford, MIT)\n- Develops a Bayesian account unifying in-context learning and activation steering: steering changes concept priors, while ICL accumulates evidence. Provides a closed-form Bayesian model predictive of LLM behavior. Relevant theoretical framework that could inform or compete with the proposal's mechanistic decomposition.\n- [Paper link](https://arxiv.org/abs/2511.00617)\n\n**8. \"COLD-Steer: Steering LLMs via In-Context One-step Learning Dynamics\" (arXiv:2603.06495, March 2026, ICLR 2026)**\n- Training-free framework that approximates representational changes from gradient descent on in-context examples. Relevant as an alternative efficient steering method that could be applied to calibration without requiring explicit bias decomposition.\n- [Paper link](https://arxiv.org/abs/2603.06495)\n\n**9. \"Shifting Perspectives: Steering Vector Ensembles for Robust Bias Mitigation in LLMs\" (arXiv:2503.05371, March 2025, EACL 2026)**\n- Computes 8 steering vectors for different social bias axes and uses ensembles. Directly demonstrates multi-bias-axis steering vector decomposition, which is the same structural approach as the proposal but for social bias rather than confidence bias.\n- [Paper link](https://arxiv.org/abs/2503.05371)\n\n**10. \"FairSteer: Inference Time Debiasing for LLMs with Dynamic Activation Steering\" (arXiv:2504.14492, April 2025, ACL 2025)**\n- Uses a lightweight linear classifier to detect bias signatures in activations (90%+ linear separability in intermediate layers), then applies dynamically computed debiasing steering vectors. The detect-then-steer paradigm closely mirrors what the proposal would need for detecting which type of miscalibration is active before applying targeted correction.\n- [Paper link](https://arxiv.org/abs/2504.14492)\n\n### MODERATE RELEVANCE -- Useful Context\n\n**11. \"Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk\" (arXiv:2602.04896, February 2026)**\n- Important cautionary finding: benign steering vectors can erode safety guardrails and increase jailbreak attack success rates to 80%+. The proposal should address whether targeted calibration corrections might have similar externalities.\n- [Paper link](https://arxiv.org/abs/2602.04896)\n\n**12. \"K-Steering: Beyond Linear Steering: Unified Multi-Attribute Control for Language Models\" (arXiv:2505.24535, May 2025, EMNLP 2025)**\n- Non-linear multi-label classifier for multi-attribute steering via gradients. Avoids linearity assumptions and allows dynamic composition without retraining. Relevant alternative to additive multi-bias steering vectors.\n- [Paper link](https://arxiv.org/abs/2505.24535)\n\n**13. \"MAT-Steer: Multi-Attribute Targeted Steering\" (arXiv:2502.12446, February 2025, ACL 2025)**\n- Addresses multi-attribute steering with conflict handling (e.g., helpfulness vs. toxicity reduction). Token-level selective intervention. Relevant framework for handling potentially conflicting calibration corrections.\n- [Paper link](https://arxiv.org/abs/2502.12446)\n\n**14. \"Compositional Steering of LLMs with Steering Tokens\" (arXiv:2601.05062, January 2026)**\n- Multi-behavior steering via tokens rather than activation-space vectors, with composition tokens that generalize to unseen behavior combinations. An alternative paradigm to activation-space decomposition.\n- [Paper link](https://arxiv.org/abs/2601.05062)\n\n**15. \"Guiding Giants: Lightweight Controllers for Weighted Activation Steering\" (arXiv:2505.20309, May 2025)**\n- Trainable controller network that predicts global scaling + layer-specific weights for steering, learning to discriminatively apply interventions. Relevant controller architecture for adaptive calibration correction.\n- [Paper link](https://arxiv.org/abs/2505.20309)\n\n**16. \"LinEAS: End-to-end Learning of Activation Steering with a Distributional Loss\" (arXiv:2503.10679, NeurIPS 2025)**\n- Apple Research. Global distributional loss for learning steering across all layers simultaneously, with sparsifying norms for automatic neuron/layer selection. Could be applied to calibration steering.\n- [Paper link](https://arxiv.org/abs/2503.10679)\n\n**17. \"PIXEL: Adaptive Steering Via Position-wise Injection with eXact Estimated Levels under Subspace Calibration\" (arXiv:2510.10205, October 2025)**\n- Position-wise activation steering with subspace calibration and orthogonal residual correction. The \"subspace calibration\" aspect is directly relevant terminology.\n- [Paper link](https://arxiv.org/abs/2510.10205)\n\n**18. \"The Dunning-Kruger Effect in Large Language Models\" (arXiv:2603.09985, March 2026)**\n- Empirical study showing poorly performing models display markedly higher overconfidence (ECE up to 0.726). Relevant empirical context for the proposal's calibration claims.\n- [Paper link](https://arxiv.org/abs/2603.09985)\n\n**19. \"The Confidence Dichotomy: Analyzing and Mitigating Miscalibration in Tool-Use Agents\" (arXiv:2601.07264, January 2026)**\n- Reveals tool-dependent calibration divergence: evidence tools induce overconfidence, verification tools preserve calibration. Uses RL for joint accuracy+calibration optimization. Relevant for domain-specific calibration.\n- [Paper link](https://arxiv.org/abs/2601.07264)\n\n**20. \"Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection\" (arXiv:2603.06604, March 2026)**\n- Shows SFT yields well-calibrated confidence via MLE, while RL methods induce overconfidence. Proposes post-RL SFT with self-distillation. Different approach (training-time) but relevant analysis.\n- [Paper link](https://arxiv.org/abs/2603.06604)\n\n**21. \"Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering\" (AdaRAS) (arXiv:2601.19847, January 2026)**\n- Identifies reasoning-critical neurons via polarity-aware criteria and adaptively steers their activations. 13%+ gains on AIME benchmarks. The neuron-identification-then-targeted-steering paradigm parallels the proposal's approach.\n- [Paper link](https://arxiv.org/abs/2601.19847)\n\n**22. \"DSO: Direct Steering Optimization for Bias Mitigation\" (arXiv:2512.15926, December 2025, Apple Research)**\n- Uses RL to learn linear transformations for activation steering, enabling controllable bias-accuracy tradeoffs. Different optimization approach to learning steering directions.\n- [Paper link](https://arxiv.org/abs/2512.15926)\n\n---\n\n### Summary Assessment\n\nThe **most threatening competitor** is **\"Wired for Overconfidence\" (2604.01457)**, which performs exactly the kind of mechanistic circuit-level analysis of confidence inflation that the proposal describes, and demonstrates targeted inference-time interventions on those circuits for improved calibration. However, it focuses only on overconfidence (one direction), while the proposal's key differentiator would be the decomposition into *competing* biases (both over- and under-confidence) and their simultaneous targeted correction.\n\nThe **second major competitor** is **Beacon (2510.16727)**, which already demonstrates decomposing a single behavioral phenomenon (sycophancy) into multiple sub-biases and applying cluster-specific activation steering -- the same paradigm the proposal advocates, just for a different target behavior.\n\nThe **PID Steering (2510.04309)** and **AUSteer (2602.04428)** papers present alternative frameworks for the \"how to steer\" component that could subsume or compete with the proposal's correction mechanism.\n\nThe proposal should explicitly differentiate from all of these, particularly emphasizing the novel combination of (a) decomposing calibration error into competing bias types and (b) applying bias-specific targeted activation corrections -- something none of the above papers do in an integrated manner for the calibration domain."
      }
    ],
    "totalDurationMs": 164111,
    "totalTokens": 43791,
    "totalToolUseCount": 40,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4024,
      "cache_read_input_tokens": 36476,
      "output_tokens": 3290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4024
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3290,
          "cache_read_input_tokens": 36476,
          "cache_creation_input_tokens": 4024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4024,
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
      "otherToolCount": 40
    }
  },
  "sourceToolAssistantUUID": "59dc9df5-70d1-48e7-8db9-aae798db4d31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "383224ed-21f1-4874-85c5-08b14e47bdd1",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose competing calibration biases via activation steering",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Tool call

_source line 28 · 2026-05-19T16:49:33.924Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JYWAo3BdvXdMkvLGgwi8uM`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SteerConf claims specificity",
  "prompt": "The proposal cites SteerConf (Zhou et al., NeurIPS 2025, arXiv 2503.02863) as achieving \"29% AUROC increase and 16% ECE reduction.\" A previous verification found these are cherry-picked numbers from a single dataset/model (Object Counting + GPT-3.5), not aggregate results.\n\nPlease search for and fetch the SteerConf paper to verify:\n1. What are the AGGREGATE (average across datasets/models) improvements, not just the best-case numbers?\n2. Does the paper report overall average AUROC and ECE improvements?\n\nAlso verify: Does \"Wired for Overconfidence\" (arXiv 2604.01457) - which the proposal already cites - contain any per-instance decomposition of overconfidence vs underconfidence, or is it purely about overconfidence? Does it propose targeted correction? This is important because if it already does what the proposal claims as novel, that's a major issue.\n\nSearch and fetch the relevant papers. Report concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "383224ed-21f1-4874-85c5-08b14e47bdd1",
  "isSidechain": false,
  "requestId": "req_011CbCGf1CVd3o9j4Nbu84jf",
  "type": "assistant",
  "uuid": "e82315f7-55d0-40dd-8ddb-6b17817e0ef2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YNSqQ7BHp6mg3nqJKfxZS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3984,
      "cache_read_input_tokens": 47256,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 47256,
          "cache_creation_input_tokens": 3984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3984
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

_source line 29 · 2026-05-19T16:50:30.666Z_

<details><summary>↩ Tool result · `toolu_01JYWAo3BdvXdMkvLGgwi8uM`</summary>

```text
No proposal documents in the repo itself. I have all the information needed. Here are my findings:

---

## SteerConf (Zhou et al., arXiv 2503.02863) -- Verification of Cited Numbers

**The "29% AUROC increase and 16% ECE reduction" are confirmed as cherry-picked.** These come from a single dataset/model combination: **Object Counting + GPT-3.5 in the non-CoT setting** (Figure 1 of the paper). The paper itself uses these as a motivating example, not as representative results.

**Actual aggregate results (Table 2, CoT setting -- the paper's best configuration):**

| Model | AUROC Improvement | ECE Reduction |
|-------|-------------------|---------------|
| LLaMA 3 | +18.9 pp (58.1 -> 77.0) | -3.2 pp (11.1 -> 7.9) |
| GPT-3.5 | +19.0 pp (56.2 -> 75.2) | -17.1 pp (29.8 -> 12.7) |
| GPT-4 | +15.6 pp (65.5 -> 81.1) | -3.5 pp (10.7 -> 7.2) |
| **Cross-model average** | **~17.8 pp** | **~7.9 pp** |

Key observations:
- The average AUROC improvement across all models/datasets is **~18 pp, not 29 pp** (the cited number is ~60% inflated).
- The average ECE reduction is **~8 pp, not 16 pp** (the cited number is ~100% inflated). The 16 pp ECE number is almost entirely driven by GPT-3.5 which starts from a much worse baseline (29.8% ECE). For GPT-4 and LLaMA 3, ECE reductions are only 3-4 pp.
- The proposal should cite the aggregate numbers, not the cherry-picked best-case from a single dataset.

---

## "Wired for Overconfidence" (arXiv 2604.01457) -- Novelty Check

**This paper does NOT do what the proposal claims as novel.** Specifically:

1. **No per-instance decomposition**: The paper does not distinguish between overconfident and underconfident instances. It stratifies data into "buckets" for circuit discovery purposes (e.g., "confidently wrong" cases), but this is used to find overconfidence circuits, not to classify individual instances as needing different corrections.

2. **No directional/targeted correction**: Both intervention methods (mean ablation and activation steering) apply **uniform, unidirectional suppression** of confidence. They subtract a fixed overconfidence direction or replace activations with a global reference mean. There is no mechanism to push underconfident instances upward while pushing overconfident instances downward.

3. **No error-type decomposition**: The paper provides no breakdown of what fraction of calibration error comes from overconfidence vs. underconfidence. It treats overconfidence as the sole problem.

4. **Purely about overconfidence**: The entire framing assumes LLMs are systematically overconfident and that the fix is to dampen confidence signals uniformly.

**Bottom line for novelty**: If the proposal's core contribution is per-instance directional calibration (detecting whether each instance is overconfident or underconfident and correcting accordingly), this is genuinely distinct from "Wired for Overconfidence," which only does blanket confidence suppression. However, the proposal should explicitly articulate this distinction, because the cited paper's "targeted intervention" language could be confused with instance-level targeting (it actually means targeting specific neural circuits, not specific instances).

---

**Summary of issues the proposal should fix:**
1. Replace "29% AUROC increase and 16% ECE reduction" with the actual aggregate numbers (~18 pp AUROC, ~8 pp ECE), or explicitly note these are best-case single-dataset results.
2. Clearly differentiate the proposal's per-instance directional approach from "Wired for Overconfidence"'s uniform suppression approach, since the latter's "targeted intervention" language creates potential confusion about what's actually novel.

agentId: a1b635cf562fd7e32 (use SendMessage with to: 'a1b635cf562fd7e32' to continue this agent)
&lt;usage>total_tokens: 14489
tool_uses: 6
duration_ms: 56736&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e82315f7-55d0-40dd-8ddb-6b17817e0ef2",
  "isSidechain": false,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "type": "user",
  "uuid": "e910e1cf-e671-4988-9d53-7b4ced198e7d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "The proposal cites SteerConf (Zhou et al., NeurIPS 2025, arXiv 2503.02863) as achieving \"29% AUROC increase and 16% ECE reduction.\" A previous verification found these are cherry-picked numbers from a single dataset/model (Object Counting + GPT-3.5), not aggregate results.\n\nPlease search for and fetch the SteerConf paper to verify:\n1. What are the AGGREGATE (average across datasets/models) improvements, not just the best-case numbers?\n2. Does the paper report overall average AUROC and ECE improvements?\n\nAlso verify: Does \"Wired for Overconfidence\" (arXiv 2604.01457) - which the proposal already cites - contain any per-instance decomposition of overconfidence vs underconfidence, or is it purely about overconfidence? Does it propose targeted correction? This is important because if it already does what the proposal claims as novel, that's a major issue.\n\nSearch and fetch the relevant papers. Report concisely.",
    "agentId": "a1b635cf562fd7e32",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "No proposal documents in the repo itself. I have all the information needed. Here are my findings:\n\n---\n\n## SteerConf (Zhou et al., arXiv 2503.02863) -- Verification of Cited Numbers\n\n**The \"29% AUROC increase and 16% ECE reduction\" are confirmed as cherry-picked.** These come from a single dataset/model combination: **Object Counting + GPT-3.5 in the non-CoT setting** (Figure 1 of the paper). The paper itself uses these as a motivating example, not as representative results.\n\n**Actual aggregate results (Table 2, CoT setting -- the paper's best configuration):**\n\n| Model | AUROC Improvement | ECE Reduction |\n|-------|-------------------|---------------|\n| LLaMA 3 | +18.9 pp (58.1 -> 77.0) | -3.2 pp (11.1 -> 7.9) |\n| GPT-3.5 | +19.0 pp (56.2 -> 75.2) | -17.1 pp (29.8 -> 12.7) |\n| GPT-4 | +15.6 pp (65.5 -> 81.1) | -3.5 pp (10.7 -> 7.2) |\n| **Cross-model average** | **~17.8 pp** | **~7.9 pp** |\n\nKey observations:\n- The average AUROC improvement across all models/datasets is **~18 pp, not 29 pp** (the cited number is ~60% inflated).\n- The average ECE reduction is **~8 pp, not 16 pp** (the cited number is ~100% inflated). The 16 pp ECE number is almost entirely driven by GPT-3.5 which starts from a much worse baseline (29.8% ECE). For GPT-4 and LLaMA 3, ECE reductions are only 3-4 pp.\n- The proposal should cite the aggregate numbers, not the cherry-picked best-case from a single dataset.\n\n---\n\n## \"Wired for Overconfidence\" (arXiv 2604.01457) -- Novelty Check\n\n**This paper does NOT do what the proposal claims as novel.** Specifically:\n\n1. **No per-instance decomposition**: The paper does not distinguish between overconfident and underconfident instances. It stratifies data into \"buckets\" for circuit discovery purposes (e.g., \"confidently wrong\" cases), but this is used to find overconfidence circuits, not to classify individual instances as needing different corrections.\n\n2. **No directional/targeted correction**: Both intervention methods (mean ablation and activation steering) apply **uniform, unidirectional suppression** of confidence. They subtract a fixed overconfidence direction or replace activations with a global reference mean. There is no mechanism to push underconfident instances upward while pushing overconfident instances downward.\n\n3. **No error-type decomposition**: The paper provides no breakdown of what fraction of calibration error comes from overconfidence vs. underconfidence. It treats overconfidence as the sole problem.\n\n4. **Purely about overconfidence**: The entire framing assumes LLMs are systematically overconfident and that the fix is to dampen confidence signals uniformly.\n\n**Bottom line for novelty**: If the proposal's core contribution is per-instance directional calibration (detecting whether each instance is overconfident or underconfident and correcting accordingly), this is genuinely distinct from \"Wired for Overconfidence,\" which only does blanket confidence suppression. However, the proposal should explicitly articulate this distinction, because the cited paper's \"targeted intervention\" language could be confused with instance-level targeting (it actually means targeting specific neural circuits, not specific instances).\n\n---\n\n**Summary of issues the proposal should fix:**\n1. Replace \"29% AUROC increase and 16% ECE reduction\" with the actual aggregate numbers (~18 pp AUROC, ~8 pp ECE), or explicitly note these are best-case single-dataset results.\n2. Clearly differentiate the proposal's per-instance directional approach from \"Wired for Overconfidence\"'s uniform suppression approach, since the latter's \"targeted intervention\" language creates potential confusion about what's actually novel."
      }
    ],
    "totalDurationMs": 56736,
    "totalTokens": 14489,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1158,
      "cache_read_input_tokens": 12330,
      "output_tokens": 1000,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1158
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1000,
          "cache_read_input_tokens": 12330,
          "cache_creation_input_tokens": 1158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1158,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 1,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "e82315f7-55d0-40dd-8ddb-6b17817e0ef2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-19T16:51:39.001Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize all the findings and produce my review.

Key findings from my verification:

1. **All key references verified**: Both Kumaran papers, CogBias, Billa, Liu, Patel et al., Kobalczyk, Miao & Ungar, CCPS, SteerConf, Sycophancy Is Not One Thing, cross-architecture papers -- all confirmed real with correct claims.

2. **SteerConf numbers are cherry-picked**: The "29% AUROC increase and 16% ECE reduction" are from a single dataset/model combination, not aggregates. Actual aggregates are ~18pp AUROC and ~8pp ECE. 

This is problematic since the proposal relies on these inflated figures.

3. **Model names verified**: Gemma 4 31B Dense, Qwen3-8B, Llama-3.1-8B-Instruct all confirmed real.

4. **Venue deadlines reasonable**: ICLR 2027 ~Sep 24, 2026 is reasonable based on ICLR 2026 pattern.

5. **Missing competitors identified**: "Wired for Overconfidence" (2604.01457) is already cited in the proposal, which is good since it addresses a genuinely different approach.  Several other papers like "Shifting Perspectives: Steering Vector Ensembles," "FairSteer," "Beacon," "PID Steering," and "Don't Lose Focus: SKOP" are methodologically relevant but not direct competitors, and the proposal already has an extremely comprehensive reference list covering these areas.

6. **Gap validity**: The gap appears genuine. No paper does all three things together: decompose calibration error into competing biases at the activation level, measure asymmetric steerability across instances, and apply bias-specific correction. "Wired for Overconfidence" only suppresses overconfidence, CogBias steers entire bias families without targeting calibration-specific competing biases, and "Sycophancy Is Not One Thing" decomposes co-aligned biases rather than opposing ones that interfere with each other.

### Novelty

The proposal genuinely fills a gap at the intersection of competing bias identification at the activation level, bias decomposition for steering opposing biases, and steerability-aware routing for per-instance calibration.

Score: 3.5/5. The novelty is genuine but incremental—it's applying established decomposition and steering paradigms to a new problem setting rather than introducing fundamentally new methods.

### Feasibility

The proposal has solid safeguards with go/no-go gates and fallback paths, but Phase 0B remains ambitious even at three weeks, the contrastive pair generation with factorial attribution is complex, and running three models across three datasets with seven baselines creates substantial experimental overhead.

Score: 3.5/5. Feasible but risky—the multi-phase structure with gates helps, though the overall scope pushes against the timeline.

### Clarity

The proposal is thorough and well-organized, but its length and complexity might obscure the core contribution for reviewers, and the conditional framing around impact uncertainty, while honest, signals some doubt about the work's significance. The approach reads more like a detailed project plan than a concise research proposal, and nine rounds of refinement have made it comprehensive at the cost of conciseness.

Score: 3.5/5. Extremely detailed but potentially too dense.

### Impact

The real impact hinges on whether interference actually occurs at >30%, 15-30%, or <15%—a question the proposal frames transparently but can't yet answer. If interference is prevalent, the calibration improvements would be meaningful; if it's rare, the contribution becomes more mechanistic and niche. The honest conditional framing is intellectually sound but also undermines conviction about the work's significance. The proposal directly addresses the user's calibration focus, which is good.

Score: 3/5. Impact is contingent on an unknown prevalence rate.

### Issues

The SteerConf numbers appear cherry-picked—citing 29% AUROC and 16% ECE improvements from a single dataset rather than aggregated results across multiple settings.

Actually, wait—those cherry-picked numbers make SteerConf look *better* than its true average performance (closer to 18pp and 8pp respectively), which means the proposal is inadvertently positioning itself against a stronger baseline than actually exists. That's conservative framing, though still factually misleading.

There's also missing engagement with related work like Beacon's approach to decomposing sycophancy into sub-biases with cluster-specific steering, and FairSteer's detect-then-steer framework from ACL 2025.

The core issue is that despite tightening in revision, this still sprawls across four phases, three models, three datasets, seven baselines, and multiple intervention routes—it reads like a research program rather than a focused paper. And the conditional framing around interference prevalence, while honest, undermines the pitch for top-tier venues since the impact hinges on an unknown quantity.

The real vulnerability is Phase 0B: if the contrastive extraction doesn't produce distinguishable signatures between CSB and CEO under confound control, the whole pipeline collapses into a weaker correlational story. That fundamental risk persists even after nine rounds.

The average score sits at 3.375, below the 4.0 pass threshold, and this is the penultimate round. I'm weighing whether to pass it forward: the gap is genuine and well-characterized, references check out, the methodology is solid, and the go/no-go gates provide some protection.

But the complexity still feels bloated despite claims of tightening, the impact framing is heavily conditional, there's that careless cherry-picking of SteerConf numbers, and a few methodological references are missing. This reads as a "revise" rather than a pass—the work is fundamentally sound but hasn't quite cleared the bar. Since the next round must be final, I need to give specific guidance on what would push this over the threshold. The core idea has genuinely held up through nine rounds of scrutiny—the gap is real, the methodology is sound despite its complexity, and the central question about competing biases having distinct activation signatures is legitimately interesting. But I'm being honest that this is a borderline proposal: it could be a solid paper, though whether the answer turns out to be "yes" or "not usefully so" will determine its actual impact. I'll recommend revision with specific guidance for the final round.

Now I'm checking the SteerConf numbers more carefully—the proposal cites 29% AUROC improvement and 16% ECE reduction, but when I trace these back to the actual paper, those appear to be best-case figures from the introduction rather than the reported averages, which are closer to 18 percentage points and 8 percentage points respectively. I need to flag this discrepancy since the proposal is using the higher numbers throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e910e1cf-e671-4988-9d53-7b4ced198e7d",
  "isSidechain": false,
  "requestId": "req_011CbCGjsAh2FU4gaCSYPi8c",
  "type": "assistant",
  "uuid": "1f04a771-263c-4b29-89ac-09792876b16b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011SuRouxsjyEVN6Taaa2mcg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 51240,
      "output_tokens": 3346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3346,
          "cache_read_input_tokens": 51240,
          "cache_creation_input_tokens": 1410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1410
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

_source line 31 · 2026-05-19T16:51:39.155Z_

Now let me compile all findings and assess the proposal comprehensively.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f04a771-263c-4b29-89ac-09792876b16b",
  "isSidechain": false,
  "requestId": "req_011CbCGjsAh2FU4gaCSYPi8c",
  "type": "assistant",
  "uuid": "9875306b-42d9-4703-861e-a9827b08d9e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011SuRouxsjyEVN6Taaa2mcg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 51240,
      "output_tokens": 3346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3346,
          "cache_read_input_tokens": 51240,
          "cache_creation_input_tokens": 1410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1410
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

_source line 32 · 2026-05-19T16:51:44.360Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0165Nn7dfDviKSDwe6s3z5Yy`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check for May 2026 concurrent work",
  "prompt": "Search for very recent (May 2026) papers on arxiv that might be directly concurrent with a proposal about decomposing LLM calibration biases at the activation level. I need to check if anyone has published specifically on:\n\n1. Search: arxiv \"choice supportive bias\" OR \"choice-supportive\" activation OR mechanistic 2026\n2. Search: arxiv confidence calibration \"opposing biases\" OR \"competing biases\" OR \"bias interference\" 2026\n3. Search: arxiv.org \"per-instance calibration\" activation steering May 2026\n4. Search: \"Don't Lose Focus\" SKOP activation steering arxiv 2605.06342\n5. Search: \"Belief Dynamics\" \"Dual Nature\" in-context learning activation steering arxiv 2511.00617\n\nFor each relevant paper found, report title, arXiv ID, date, and key relevance. Focus on papers that do EXACTLY what the proposal does (decompose calibration into competing biases and steer per-instance). Report in under 200 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9875306b-42d9-4703-861e-a9827b08d9e5",
  "isSidechain": false,
  "requestId": "req_011CbCGjsAh2FU4gaCSYPi8c",
  "type": "assistant",
  "uuid": "1e9e0809-8a55-4e9e-9cb6-83c22231ee9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011SuRouxsjyEVN6Taaa2mcg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 51240,
      "output_tokens": 3346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3346,
          "cache_read_input_tokens": 51240,
          "cache_creation_input_tokens": 1410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1410
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "1e9e0809-8a55-4e9e-9cb6-83c22231ee9b",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose competing calibration biases via activation steering",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Tool result

_source line 35 · 2026-05-19T16:52:45.637Z_

<details><summary>↩ Tool result · `toolu_0165Nn7dfDviKSDwe6s3z5Yy`</summary>

```text
Here is the consolidated report.

---

**No exact match found.** None of the papers discovered do exactly what your proposal does (decompose calibration into competing/opposing biases at the activation level and steer per-instance). However, several papers are partially overlapping and should be cited or discussed:

**Closest papers (high relevance):**

1. **"Discovery of Hidden Miscalibration Regimes"** -- arXiv:2605.13484, May 2026. Discovers that LLMs are simultaneously overconfident on some inputs and underconfident on others, with global metrics masking this. Learns input-dependent calibration regimes. Does NOT do activation-level decomposition or steering. **Closest conceptual neighbor to your proposal.**

2. **"CORAL: Correctness-Optimized Residual Activation Lens"** -- arXiv:2602.06022, Feb 2026. Calibration-aware activation steering using residual stream probes; improves ECE by ~50%. Steers per-instance but does NOT decompose calibration into competing bias components.

3. **"Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering"** -- arXiv:2511.00617, Nov 2025 (v2 Mar 2026). Models ICL and steering as Bayesian belief updates (priors vs. evidence). Relevant framing but not about calibration bias decomposition.

**Moderate relevance:**

4. **"Don't Lose Focus: SKOP"** -- arXiv:2605.06342, May 2026. Key-orthogonal projection steering preserving attention. Activation steering method, not calibration-specific.

5. **"Alleviating Choice Supportive Bias in LLMs"** -- arXiv:2512.03082, Dec 2025. Addresses CSB via fine-tuning, not activation-level decomposition.

**Bottom line:** Papers 1 and 2 are the most important to position against. Paper 1 identifies the same phenomenon (hidden opposing calibration regimes) but lacks the mechanistic/activation-level decomposition and steering. Paper 2 does calibration-aware activation steering but without bias decomposition. Your proposal's unique contribution -- decomposing calibration into competing biases at the activation level and steering per-instance -- appears to be a genuine gap.

Sources:
- [Discovery of Hidden Miscalibration Regimes](https://arxiv.org/abs/2605.13484)
- [CORAL: Calibration-Aware Inference-Time Steering](https://arxiv.org/abs/2602.06022)
- [Belief Dynamics: Dual Nature of ICL and Activation Steering](https://arxiv.org/abs/2511.00617)
- [Don't Lose Focus: SKOP](https://arxiv.org/abs/2605.06342)
- [Alleviating Choice Supportive Bias in LLMs](https://arxiv.org/abs/2512.03082)
- [Dunning-Kruger Effect in LLMs](https://arxiv.org/abs/2603.09985)
- [Calibrating LLM Confidence with Semantic Steering](https://arxiv.org/abs/2503.02863)

agentId: a2ddd869ead476ede (use SendMessage with to: 'a2ddd869ead476ede' to continue this agent)
&lt;usage>total_tokens: 17465
tool_uses: 9
duration_ms: 61273&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e9e0809-8a55-4e9e-9cb6-83c22231ee9b",
  "isSidechain": false,
  "promptId": "970dcc78-11fd-4bee-b226-b1cf31ec1967",
  "type": "user",
  "uuid": "2ac6c6a0-9a53-4cf0-b8f2-8ca8140c7d9d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for very recent (May 2026) papers on arxiv that might be directly concurrent with a proposal about decomposing LLM calibration biases at the activation level. I need to check if anyone has published specifically on:\n\n1. Search: arxiv \"choice supportive bias\" OR \"choice-supportive\" activation OR mechanistic 2026\n2. Search: arxiv confidence calibration \"opposing biases\" OR \"competing biases\" OR \"bias interference\" 2026\n3. Search: arxiv.org \"per-instance calibration\" activation steering May 2026\n4. Search: \"Don't Lose Focus\" SKOP activation steering arxiv 2605.06342\n5. Search: \"Belief Dynamics\" \"Dual Nature\" in-context learning activation steering arxiv 2511.00617\n\nFor each relevant paper found, report title, arXiv ID, date, and key relevance. Focus on papers that do EXACTLY what the proposal does (decompose calibration into competing biases and steer per-instance). Report in under 200 words.",
    "agentId": "a2ddd869ead476ede",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the consolidated report.\n\n---\n\n**No exact match found.** None of the papers discovered do exactly what your proposal does (decompose calibration into competing/opposing biases at the activation level and steer per-instance). However, several papers are partially overlapping and should be cited or discussed:\n\n**Closest papers (high relevance):**\n\n1. **\"Discovery of Hidden Miscalibration Regimes\"** -- arXiv:2605.13484, May 2026. Discovers that LLMs are simultaneously overconfident on some inputs and underconfident on others, with global metrics masking this. Learns input-dependent calibration regimes. Does NOT do activation-level decomposition or steering. **Closest conceptual neighbor to your proposal.**\n\n2. **\"CORAL: Correctness-Optimized Residual Activation Lens\"** -- arXiv:2602.06022, Feb 2026. Calibration-aware activation steering using residual stream probes; improves ECE by ~50%. Steers per-instance but does NOT decompose calibration into competing bias components.\n\n3. **\"Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering\"** -- arXiv:2511.00617, Nov 2025 (v2 Mar 2026). Models ICL and steering as Bayesian belief updates (priors vs. evidence). Relevant framing but not about calibration bias decomposition.\n\n**Moderate relevance:**\n\n4. **\"Don't Lose Focus: SKOP\"** -- arXiv:2605.06342, May 2026. Key-orthogonal projection steering preserving attention. Activation steering method, not calibration-specific.\n\n5. **\"Alleviating Choice Supportive Bias in LLMs\"** -- arXiv:2512.03082, Dec 2025. Addresses CSB via fine-tuning, not activation-level decomposition.\n\n**Bottom line:** Papers 1 and 2 are the most important to position against. Paper 1 identifies the same phenomenon (hidden opposing calibration regimes) but lacks the mechanistic/activation-level decomposition and steering. Paper 2 does calibration-aware activation steering but without bias decomposition. Your proposal's unique contribution -- decomposing calibration into competing biases at the activation level and steering per-instance -- appears to be a genuine gap.\n\nSources:\n- [Discovery of Hidden Miscalibration Regimes](https://arxiv.org/abs/2605.13484)\n- [CORAL: Calibration-Aware Inference-Time Steering](https://arxiv.org/abs/2602.06022)\n- [Belief Dynamics: Dual Nature of ICL and Activation Steering](https://arxiv.org/abs/2511.00617)\n- [Don't Lose Focus: SKOP](https://arxiv.org/abs/2605.06342)\n- [Alleviating Choice Supportive Bias in LLMs](https://arxiv.org/abs/2512.03082)\n- [Dunning-Kruger Effect in LLMs](https://arxiv.org/abs/2603.09985)\n- [Calibrating LLM Confidence with Semantic Steering](https://arxiv.org/abs/2503.02863)"
      }
    ],
    "totalDurationMs": 61273,
    "totalTokens": 17465,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 15881,
      "output_tokens": 775,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 808
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 775,
          "cache_read_input_tokens": 15881,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 808,
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
      "otherToolCount": 9
    }
  },
  "sourceToolAssistantUUID": "1e9e0809-8a55-4e9e-9cb6-83c22231ee9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-19T16:52:45.641Z_

```json
{
  "parentUuid": "2ac6c6a0-9a53-4cf0-b8f2-8ca8140c7d9d",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "cb6a99a5-d2b4-4757-a713-735a04394ebd",
  "timestamp": "2026-05-19T16:52:45.641Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-19T16:53:24.297Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to compile a thorough review. Let me synthesize everything.

## Summary of Verification Results

### References
- **All key references verified as real** with correct arXiv IDs and claims
- **SteerConf numbers are cherry-picked**: "29% AUROC increase and 16% ECE reduction" are from a single dataset/model (Object Counting + GPT-3.5), not aggregate results. Actual averages: ~18pp AUROC, ~8pp ECE
- **Model names verified**: Gemma 4 31B Dense, Qwen3-8B, Llama-3.1-8B-Instruct all exist


- **Venue deadlines check out**: ICLR 2027's September 2026 deadline aligns with the pattern from ICLR 2026

### Gap Validity
The proposed work addresses a genuine gap—no existing paper combines activation-level calibration error decomposition with bias-specific steering mechanisms. Related work like "Wired for Overconfidence" only handles uniform suppression, Kobalczyk identifies hidden miscalibration regimes without mechanistic solutions, CogBias targets bias families rather than calibration-specific competing biases, and "Sycophancy Is Not One Thing" decomposes aligned behaviors rather than opposing ones.

### Citation Coverage
There are several methodologically relevant papers I haven't cited yet—"Beacon" decomposes sycophancy into sub-biases with cluster-specific steering, "FairSteer" uses a detect-then-steer paradigm with linear classifiers, "Shifting Perspectives" explores multi-bias steering vector ensembles, "PID Steering" applies control-theoretic frameworks, "SKOP" preserves attention during steering, and "Belief Dynamics" offers a Bayesian unification of in-context learning and steering. None are direct competitors, but adding them risks pushing the reference count beyond what's already substantial at 35+.

The novelty here is solid but incremental—I'm applying established techniques like contrastive extraction and routing-by-steerability to a new problem of competing calibration biases, but each component has precedent elsewhere. Feasibility looks reasonable with clear gates and controls, though Phase 0B's three-week window for 4000 pairs with full attribution is tight, and the overall scope across four phases, three models, three datasets, and seven baselines is genuinely ambitious for an ICLR 2027 deadline.

The proposal is extremely detailed and well-structured, but that detail works against it—it reads more like a full project plan than a research pitch, and after nine revisions the complexity has accumulated rather than tightened despite the claimed streamlining. The conditional framing around interference prevalence (>30% / 15-30% / <15%) is honest about uncertainty but weakens the pitch. Impact is genuinely conditional on whether interference actually occurs at meaningful rates and whether the mechanistic characterization translates to practical calibration improvements, which keeps this from being a strong unconditional contribution.

Now I'm seeing the actual performance numbers, and there's a significant discrepancy—the SteerConf results being cited (29% AUROC increase, 16% ECE reduction) are cherry-picked from a single dataset rather than aggregate performance, when the real averages across models are closer to 18 percentage points AUROC and 8 percentage points ECE. The fundamental problem remains that this is really a multi-paper research program compressed into one proposal: four phases, three models, three datasets, seven baselines, three intervention routes, a 2×2 attribution factorial, plus confound diagnostics. The scoring stagnation (3.8 down to 3.5) reflects that the core issue isn't presentation—it's scope.

The conditional framing ("if X then Y, if Z then W") is intellectually honest but signals weak conviction. Top-tier work needs a clear, confident contribution claim, not a decision tree of possible outcomes. There are also methodologically adjacent papers that should be cited (Beacon, FairSteer, Shifting Perspectives, PID Steering), but adding them would only compound the complexity problem.

With round 10 being the final decision, I need to be direct: to pass, this would need radical simplification—cutting down to a focused two-phase design with behavioral replication, activation characterization, and a single intervention approach, rather than the current sprawling architecture.

The core tension is real: the gap exists, the methodology is sound, but the execution is over-engineered and the impact remains genuinely uncertain. The novelty is incremental, feasibility is compromised by scope, clarity suffers from complexity, and impact hinges on unknowns. I'm settling on a revise recommendation with very specific guidance for the final round, though this genuinely sits on the borderline. I'm settling on 3.5 for clarity since the structure and writing are actually solid—the complexity comes from the scope rather than poor exposition. With those final scores averaging 3.375, the recommendation remains a revision with concrete guidance for the next round.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb6a99a5-d2b4-4757-a713-735a04394ebd",
  "isSidechain": false,
  "requestId": "req_011CbCGupBt2cNvyAj4RagPN",
  "type": "assistant",
  "uuid": "3e30d150-c8ad-4858-bc21-fb86bd7ea2a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqjssDgprDxb7hrmm17JRY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4293,
      "cache_read_input_tokens": 52650,
      "output_tokens": 3962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3962,
          "cache_read_input_tokens": 52650,
          "cache_creation_input_tokens": 4293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4293
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

_source line 38 · 2026-05-19T16:54:05.361Z_

Now I have comprehensive verification results across all dimensions. Let me synthesize into the final review.

## Verification Summary

**References**: All 35+ cited papers verified as real with correct arXiv IDs. Key claims from Kumaran et al. (both papers), CogBias, Billa, Liu, Patel et al., Kobalczyk, CCPS, Sycophancy decomposition, Miao & Ungar, MERA, Spherical Steering — all confirmed accurate.

**Models**: Gemma 4 31B Dense, Qwen3-8B, Llama-3.1-8B-Instruct all confirmed to exist.

**Venue deadlines**: ICLR 2027 ~Sep 24, 2026 is reasonable (mirrors ICLR 2026 pattern exactly).

**Gap validity**: Confirmed genuine — no existing paper decomposes calibration into competing biases at the activation level with bias-specific steering.

**One factual issue found**: SteerConf's cited numbers are cherry-picked (see below).

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3.5,
      "rationale": "The gap is genuine — no existing work decomposes simultaneously competing calibration biases at the activation level with steerability-informed routing. However, every individual component has direct precedents: contrastive extraction (CogBias, Sycophancy decomposition), routing-by-steerability (Billa), adaptive steering with abstention (MERA), nonlinear correction (Liu). The novelty is in applying these established paradigms to a new problem setting (opposing calibration biases), which is meaningful but incremental."
    },
    "feasibility": {
      "score": 3.5,
      "rationale": "Well-designed go/no-go gates and sophisticated confound controls mitigate Phase 0B risk. The 3-week Phase 0B allocation is more realistic than the prior 2-week estimate. However, the overall scope remains very ambitious: 4 multi-part phases, 3 models, 3 datasets, 7+ baselines, 3 intervention routes, 2×2 attribution factorial with ~4000 pairs, confound diagnostic battery. ICLR 2027 is achievable only at the shorter timeline bound with aggressive parallel writing."
    },
    "clarity": {
      "score": 3.5,
      "rationale": "The proposal is precisely written with clear structure, well-articulated contribution claims, and honest conditional framing. However, after 9 revision rounds it has accumulated significant complexity — the approach section reads more like a multi-year research program than a single paper. The conditional impact framing (>30% / 15-30% / <15% interference prevalence) is intellectually honest but makes the contribution claim feel uncertain rather than compelling."
    },
    "impact": {
      "score": 3,
      "rationale": "Impact is genuinely conditional on an unknown empirical quantity (interference prevalence). The proposal honestly acknowledges this but the conditional framing means: at >30% interference it's a strong calibration paper; at 15-30% it's primarily mechanistic; at <15% it's primarily interpretive. A reviewer cannot evaluate whether this paper will be impactful because the proposers themselves don't know. The mechanistic characterization is interesting regardless but may be niche if the practical gains are small."
    }
  },
  "issues": [
    "STEERCONF NUMBERS MISREPRESENTED: The proposal repeatedly cites SteerConf as achieving '29% AUROC increase and 16% ECE reduction' — these are cherry-picked from a single dataset/model combination (Object Counting + GPT-3.5 in non-CoT setting), presented as the paper's motivating example. Verified aggregate results across models: ~18pp AUROC improvement and ~8pp ECE reduction (GPT-4 and LLaMA 3 show only 3-4pp ECE reduction). Since SteerConf is listed as a core baseline, accurate characterization of its performance is important — the proposal should cite aggregate numbers or explicitly note these are best-case results.",
    "COMPLEXITY STAGNATION: The proposal's own revision notes acknowledge 'scores declining 3.8→3.5 despite positive qualitative feedback' and identify complexity bloat as the cause. Despite R9 tightening claims, the proposal still contains: Phase 0A (behavioral replication + pathway verification with 3 complementary methods), Phase 0B (3-week expanded factorial with ~4000 pairs, 2×2 attribution design, confound diagnostic battery), Phase 1A (5 separability tests), Phase 1B (5 steerability diagnostics), Phase 2 (per-instance classification + interference prevalence estimation), Phase 3 (3 intervention routes + routing logic), evaluation across 3×3×7+ configurations. Each addition was individually justified, but the accumulated design exceeds what a single paper can execute and present clearly. Successful papers in this space (ITI/ICLR 2024, CAA/ACL 2024, CAST/ICLR 2025) feature focused designs with one core claim — the proposal names these papers but doesn't follow their example.",
    "CONDITIONAL IMPACT FRAMING WEAKENS THE PITCH: The three-tier conditional framing (>30% → practical, 15-30% → mechanistic, <15% → interpretive) is honest but fundamentally weakens the case for top-tier publication. A reviewer evaluating this proposal cannot determine whether the contribution will be 'strong practical improvement' or 'primarily interpretive' — and the authors don't know either. This uncertainty is inherent to the research question, but a top-tier paper should have a strong primary contribution that holds regardless of the interference prevalence outcome.",
    "METHODOLOGICALLY RELEVANT UNCITED WORK: Several papers are methodologically adjacent and worth acknowledging: (a) 'Beacon' (arXiv 2510.16727) decomposes sycophancy into discrete sub-biases with cluster-specific activation steering — the same decompose-then-steer-per-cluster paradigm; (b) 'FairSteer' (arXiv 2504.14492, ACL 2025) implements detect-then-steer via lightweight linear classifiers on activations with >90% bias separability — closely mirrors Phase 2's per-instance classifier design; (c) 'Shifting Perspectives' (arXiv 2503.05371, EACL 2026) applies 8 simultaneous steering vectors for multi-bias mitigation — demonstrates concurrent multi-direction steering. None are critical competitors, but a reviewer familiar with any of them would expect acknowledgment. However, the proposal already has 35+ references and adding more risks exacerbating the complexity problem."
  ],
  "feedback": "This is round 9 of 10 — next round MUST be pass or fail. The proposal is well-researched with a genuine gap, verified references, and sound methodology, but scores average 3.375, below the 4.0 pass threshold. The core problem is clear: each revision round adds complexity to address reviewer concerns, but the accumulated design is now too heavy for a single paper. Three paths to pass in round 10:\n\n(1) SIMPLIFY RADICALLY: Cut to a focused 2-phase design: Phase 0 (behavioral replication + confound-controlled activation characterization on 2 models) and Phase 1 (separability + steerability + one intervention method). Drop the 3-route routing, the conditional impact framing, and the interference prevalence estimation as a separate contribution. Make the core claim: 'competing calibration biases are distinguishable in activation space and exhibit asymmetric steerability profiles.' This is testable, novel, and sufficient for a strong paper regardless of interference prevalence.\n\n(2) COMMIT TO A PRIMARY CONTRIBUTION: Replace the conditional framing with a strong claim. Either commit to 'mechanistic characterization of competing biases' (which holds regardless of prevalence) or 'practical calibration improvement via decomposed correction' (which requires prevalence to be high). Don't hedge between both.\n\n(3) FIX THE STEERCONF NUMBERS: Replace '29% AUROC increase and 16% ECE reduction' with the verified aggregate performance (~18pp AUROC, ~8pp ECE) or explicitly note these are best-case single-dataset numbers. This is a straightforward accuracy fix.\n\nWithout radical simplification, this proposal will fail in round 10 — not because the idea is bad (the gap is genuine), but because the execution plan is too complex for a single paper and the impact claim is too uncertain for a top-tier venue.",
  "reason": "Genuine gap and verified references, but accumulated complexity from 9 revision rounds creates an over-engineered design that exceeds single-paper scope, and conditional impact framing prevents a strong contribution claim."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e30d150-c8ad-4858-bc21-fb86bd7ea2a9",
  "isSidechain": false,
  "requestId": "req_011CbCGupBt2cNvyAj4RagPN",
  "type": "assistant",
  "uuid": "f72bb902-f2c5-43c6-8aac-a42f6c031ca6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqjssDgprDxb7hrmm17JRY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4293,
      "cache_read_input_tokens": 52650,
      "output_tokens": 3962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3962,
          "cache_read_input_tokens": 52650,
          "cache_creation_input_tokens": 4293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4293
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "f72bb902-f2c5-43c6-8aac-a42f6c031ca6",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose competing calibration biases via activation steering",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-19 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "f72bb902-f2c5-43c6-8aac-a42f6c031ca6",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Decompose competing calibration biases via activation steering",
  "sessionId": "91c40d6b-ebfa-4b40-90fa-7f9fa617f0a7"
}
```

---
